"""Find cited domains that no longer serve what the citation says they do.

Benin's tax overview cites its tax year to

    https://finances.bj/wp-content/uploads/2025/01/Benin-Code-General-des-Impots-2025.pdf

That was the Ministry of Finance. The domain is now an Indonesian online-casino
site ("PRIMATOTO -- Akses Resmi Toto Slot Togel"). The Direction Generale des
Impots has moved to www.impots.finances.gouv.bj, and still lists cdgi@finances.bj
as its own contact address, which is how you can tell the domain was theirs and
was lost rather than never having been theirs.

WHY A STATUS CODE WOULD NOT HAVE FOUND IT

finances.bj returns HTTP 200. It is not down, not a 404, not a redirect. Every
check that asks "does this link resolve" passes it. The domain is alive and
answering; it just is not the ministry any more. So this reads the body, not
only the code -- that is the whole point of the script, and the reason it is
worth the network round trips.

The harm is sharper than a bad citation. A misdescribed source sends a reader to
tax commentary. This sends a reader who is following a government citation to a
gambling site, from a file that names a Ministry of Finance beside the link.

WHAT THIS CAN AND CANNOT SEE

It checks HOSTS, not documents. A ministry whose site is healthy but whose 2019
PDF has been reorganised away still passes here, and that is the commoner kind
of link rot by a wide margin. Host-level is what catches the class above, and
it is the class that misleads rather than merely disappoints.

It does not report blocks. A live authority behind a WAF answers curl with 403
or 406 -- impots.finances.gouv.bj itself does, and onrc.ro and registrucentras.lt
do -- and calling those dead would fill the queue with sites that are perfectly
fine. They are counted as `blocked` and listed separately, unjudged.

ONE FAILURE IS NOT DEATH, AND THE FIRST RUN PROVED IT

The first full sweep put **github.com at the top of the dead list, with 169
citations**, and canada.ca just below it. Neither is dead. The selftest covers
`judge()`, which decides what a response means, and could not cover `fetch()`,
which decides what response you get -- so the classifier was measured and the
fetcher was not, and a whole bucket came back unvalidated. Under fourteen-way
concurrency a busy host times out, and a timeout looked exactly like a domain
that no longer exists.

So nothing is reported dead on a single failure. Anything the concurrent pass
would call dead is re-checked serially, with no contention, before it is
printed. That the loudest false positive was github.com is luck: a false
positive that obvious gets fixed, while a quiet one would have been believed.

It ranks, it does not accuse. Every hit prints the snippet that triggered it so
a reader can see exactly what the script saw and disagree. A gaming regulator
cited for betting duty will trip the gambling words; that is a false positive by
design, preferred over missing a hijacked ministry. Always exits 0, and it must:
it depends on the network, and a checker that fails CI when a foreign tax
authority has a bad morning teaches people to ignore CI.

Usage: python3 scripts/list-citation-rot.py [--selftest] [--limit N]
                                            [--jurisdiction NAME] [--jobs N]
"""
import os, re, sys, json, collections, urllib.request, urllib.error, socket, html
from concurrent.futures import ThreadPoolExecutor

URL = re.compile(r'https?://[^\s)\]>"\'`]+')
HOST = re.compile(r'https?://([^/\s)\]>"]+)')

# The corpus's own site and the booking link in every CTA block. Thousands of
# citations, three hosts, nothing to learn.
SELF = ('openaccountants.com', 'calendly.com')

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/124.0.0.0 Safari/537.36')

# Answers that mean "a server is there and declining to talk to a script", not
# "this citation is broken". Reported separately and not counted as rot.
BLOCKED = frozenset((401, 403, 405, 406, 429, 451))

# Content of a domain that has changed hands. Indonesian gambling SEO is the
# overwhelmingly common squatter on lapsed government domains, which is why
# those words are here in that language.
GAMBLING = re.compile(r'\b(?:togel|toto\s*4d|slot\s*(?:gacor|online|resmi)|judi|'
                      r'bandar\s*(?:slot|togel)|taruhan|situs\s*(?:slot|toto)|'
                      r'casino\s*online|agen\s*(?:slot|judi))\b', re.I)
# A site that is up and serving a crash. obr.bi -- Burundi's Revenue Office, and
# an entry on the authority allowlist -- answers 200 with a Joomla fatal:
# "Application Instantiation Error: Failed to start the session because headers
# have already been sent by /home/obr/public_html/index.php at line 6". Status
# 200, no squatter words, so it scored `ok` until this existed. For a corpus
# that leans on authority citations, an authority whose site is broken is
# exactly the thing worth knowing, and nothing else here can see it.
BROKEN = re.compile(r'application\s+instantiation\s+error|'
                    r'error\s+displaying\s+the\s+error\s+page|'
                    r'\bfatal\s+error\b|\bparse\s+error\b|'
                    r'traceback\s+\(most\s+recent\s+call\s+last\)|'
                    r'whoops,\s+looks\s+like\s+something\s+went\s+wrong|'
                    r'database\s+connection\s+(?:error|failed)|'
                    r'error\s+establishing\s+a\s+database\s+connection|'
                    r'\bwarning:\s+\w+\(\)|\bnotice:\s+undefined\b', re.I)
PARKED = re.compile(r'\b(?:this\s+domain\s+(?:is|may\s+be)\s+for\s+sale|'
                    r'buy\s+this\s+domain|domain\s+for\s+sale|'
                    r'the\s+domain\s+has\s+expired|renew\s+(?:your|this)\s+domain|'
                    r'parked\s+(?:free\s+)?(?:at|by)|domain\s+parking|'
                    r'website\s+coming\s+soon|under\s+construction)\b', re.I)

# A page that still looks like the institution it claims to be. Checked so a
# gaming board or a lottery-duty page is not reported for using the words the
# squatters use.
INSTITUTIONAL = re.compile(r'\b(?:ministry|minist[eè]re|ministerio|government|'
                           r'gouvernement|revenue\s+(?:authority|service)|'
                           r'tax\s+(?:authority|administration|agency|office)|'
                           r'direction\s+g[eé]n[eé]rale|impôts|impots|'
                           r'parliament|legislation|gazette|statutory)\b', re.I)

SKIP_TREES = ('templates',)


def strip_html(body):
    body = re.sub(r'(?is)<(script|style|svg|noscript)[^>]*>.*?</\1>', ' ', body)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'(?s)<[^>]+>', ' ', body)))


def judge(status, text):
    """('rot'|'dead'|'blocked'|'ok', evidence) for one fetched host.

    Split out from the fetching so it can be tested without a network.
    """
    if status is None:
        return 'dead', 'no response'
    if status in BLOCKED:
        return 'blocked', 'HTTP %d' % status
    if status in (404, 410) or status >= 500:
        return 'dead', 'HTTP %d' % status
    if status >= 400:
        return 'dead', 'HTTP %d' % status
    m = BROKEN.search(text)
    if m:
        i = max(0, m.start() - 60)
        return 'broken', 'crash: ...%s...' % text[i:m.end() + 160].strip()
    for name, pat in (('gambling', GAMBLING), ('parked', PARKED)):
        m = pat.search(text)
        if not m:
            continue
        i = max(0, m.start() - 60)
        ev = '%s: ...%s...' % (name, text[i:m.end() + 120].strip())
        # A page that still reads like the institution it claims to be gets the
        # benefit of the doubt -- betting duty is a tax and somebody administers
        # it -- but it is DEMOTED, not dropped. Suppressing it outright would
        # mean a squatter page carrying the word "government" in a footer link
        # silently left the queue, and a wrong exemption is the error that never
        # reports itself. Both buckets are printed.
        if INSTITUTIONAL.search(text):
            return 'check', ev
        return 'rot', ev
    return 'ok', 'HTTP %d' % status


def fetch(host, timeout=20):
    """(status, stripped body) for a host, or (None, '') if nothing answered.

    A 5xx is not taken as the answer. finances.bj serves the casino page over
    one scheme and a 500 over the other depending on when you ask, and stopping
    at the first 5xx reduces the sharpest finding in the corpus to "HTTP 500".
    So a server error keeps looking and is only reported if nothing better came.
    """
    fallback = (None, '')
    for scheme in ('https', 'http'):
        req = urllib.request.Request('%s://%s/' % (scheme, host),
                                     headers={'User-Agent': UA,
                                              'Accept': 'text/html,*/*'})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, strip_html(
                    r.read(200000).decode('utf-8', 'replace'))
        except urllib.error.HTTPError as e:
            body = ''
            try:
                body = strip_html(e.read(200000).decode('utf-8', 'replace'))
            except Exception:
                pass
            if e.code >= 500:
                fallback = (e.code, body)   # keep looking; report if nothing better
                continue
            return e.code, body
        except (urllib.error.URLError, socket.timeout, ConnectionError,
                TimeoutError, OSError):
            continue
        except Exception:
            continue
    return fallback


def cited_hosts(only=None):
    """{host: [(path, line, url)]} for every external host cited under skills/."""
    out = collections.defaultdict(list)
    for dp, _, fns in os.walk('skills'):
        parts = dp.split(os.sep)
        if len(parts) > 1 and parts[1] in SKIP_TREES:
            continue
        if only and (len(parts) < 3 or parts[2] != only):
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(dp, fn)
            with open(path, encoding='utf-8', errors='replace') as fh:
                for n, line in enumerate(fh, 1):
                    for u in URL.findall(line):
                        u = u.rstrip('.,;:')
                        h = HOST.match(u).group(1)
                        if any(h == s or h.endswith('.' + s) for s in SELF):
                            continue
                        out[h].append((path, n, u))
    return out


def selftest():
    # the Benin case, reduced: alive, answering 200, and not the ministry
    kind, ev = judge(200, 'PRIMATOTO Akses Resmi Toto Slot Togel Situs Toto 4D '
                          'Terlengkap BANDAR SLOT')
    assert kind == 'rot', (kind, ev)
    assert 'togel' in ev.lower(), ev

    # a WAF turning a script away is not a broken citation. impots.finances.gouv.bj
    # answers 406 and is perfectly healthy; onrc.ro answers with a rejection page.
    assert judge(406, 'Request Rejected')[0] == 'blocked'
    assert judge(403, 'Just a moment... Enable JavaScript')[0] == 'blocked'

    # genuinely gone
    assert judge(404, 'Not Found')[0] == 'dead'
    assert judge(None, '')[0] == 'dead'
    assert judge(503, 'Service Unavailable')[0] == 'dead'

    # the ordinary case
    assert judge(200, 'Fiji Revenue and Customs Service VAT')[0] == 'ok'

    # a real authority whose subject IS gambling is demoted, not dropped: betting
    # duty is a tax and somebody administers it. It still gets printed, because
    # an exemption that silently empties a queue is the error nothing catches.
    assert judge(200, 'Gaming Authority: casino online licence duty is set by '
                      'the Ministry of Finance')[0] == 'check'

    # a site that is up and serving a crash. obr.bi, Burundi's Revenue Office and
    # an authority-allowlist entry, answers 200 with a Joomla fatal -- no squatter
    # words anywhere, so it scored `ok` until BROKEN existed.
    kind, ev = judge(200, 'Error displaying the error page: Application '
                          'Instantiation Error: Failed to start the session')
    assert kind == 'broken', (kind, ev)
    assert judge(200, 'Error establishing a database connection')[0] == 'broken'
    assert judge(200, 'Fiji Revenue and Customs Service VAT')[0] == 'ok'

    # a parked domain, which is the other way a citation quietly stops being one
    assert judge(200, 'This domain is for sale. Buy this domain today.')[0] == 'rot'

    # ...and a ministry page saying a service is coming soon is the same demotion
    assert judge(200, 'Ministry of Finance -- e-services website coming soon')[0] == 'check'

    print('selftest: 13 cases pass')


def main(argv):
    only = None
    if '--jurisdiction' in argv:
        only = argv[argv.index('--jurisdiction') + 1]
    limit = int(argv[argv.index('--limit') + 1]) if '--limit' in argv else None
    jobs = int(argv[argv.index('--jobs') + 1]) if '--jobs' in argv else 8

    where = cited_hosts(only)
    hosts = sorted(where, key=lambda h: -len(where[h]))
    if '--hosts' in argv:
        wanted = set(argv[argv.index('--hosts') + 1].split(','))
        hosts = [h for h in hosts if h in wanted]
    if limit:
        hosts = hosts[:limit]
    sys.stderr.write('checking %d hosts with %d workers...\n' % (len(hosts), jobs))

    results = {}
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        for host, (status, text) in zip(hosts, pool.map(fetch, hosts)):
            results[host] = judge(status, text)

    # Nothing is called dead on one failure. See the docstring: the first sweep
    # reported github.com as dead because a busy host under concurrency times
    # out and a timeout is indistinguishable from a domain that is gone. This
    # second pass is serial on purpose -- no contention, and a host that fails
    # here too has failed twice, minutes apart.
    suspects = [h for h, (k, _) in results.items() if k == 'dead']
    if suspects:
        sys.stderr.write('re-checking %d suspected-dead hosts serially...\n'
                         % len(suspects))
        # Shorter timeout than the first pass, deliberately. The slow hosts here
        # are not the dead ones -- DNS failure returns immediately -- but the
        # ones that accept a connection and never answer. A host that does that
        # twice, minutes apart, is not serving citations to anybody either way,
        # and waiting 20s twice for each of 151 of them put the first run over
        # an hour and it was killed before it printed anything.
        for n, host in enumerate(suspects, 1):
            results[host] = judge(*fetch(host, timeout=8))
            if n % 25 == 0:
                sys.stderr.write('  %d/%d\n' % (n, len(suspects)))
        cleared = sum(1 for h in suspects if results[h][0] != 'dead')
        sys.stderr.write('  %d of %d cleared on re-check\n'
                         % (cleared, len(suspects)))

    buckets = collections.defaultdict(list)
    for host, (kind, ev) in results.items():
        buckets[kind].append((host, ev))

    for kind, heading in (
            ('rot', 'ANSWERING, BUT NO LONGER WHAT THE CITATION SAYS IT IS'),
            ('check', 'MATCHED A SQUATTER PATTERN BUT STILL READS INSTITUTIONAL'),
            ('broken', 'ANSWERING 200 WITH A CRASH INSTEAD OF CONTENT'),
            ('dead', 'NOTHING USABLE ANSWERS')):
        rows = sorted(buckets[kind], key=lambda r: -len(where[r[0]]))
        if not rows:
            continue
        print('\n== %s (%d) ==' % (heading, len(rows)))
        for host, ev in rows:
            cites = where[host]
            jurs = sorted({c[0].split(os.sep)[2] for c in cites
                           if len(c[0].split(os.sep)) > 2})
            print('\n%s  -- %d citation(s) in %s' % (host, len(cites),
                                                     ', '.join(jurs) or '?'))
            print('   %s' % ev[:300])
            for path, n, u in cites[:4]:
                print('   %s:%d  %s' % (path, n, u[:110]))
            if len(cites) > 4:
                print('   ... and %d more' % (len(cites) - 4))

    print('\n== SUMMARY ==')
    for kind in ('rot', 'check', 'broken', 'dead', 'blocked', 'ok'):
        n = len(buckets[kind])
        cites = sum(len(where[h]) for h, _ in buckets[kind])
        print('  %-8s %4d hosts  %5d citations' % (kind, n, cites))
    print('\nHosts only: a live site does not mean the cited document is still')
    print('there, and `blocked` is a WAF turning a script away, not a defect.')
    return 0  # never gates CI: this depends on the network


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        sys.exit(main(sys.argv))
