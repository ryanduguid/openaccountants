"""Report cited hostnames that do not resolve.

Every other check in this repo asks whether a citation says the right thing.
None asks whether the thing it points at exists. A citation can be well-formed,
plausible, on a government domain, and address nothing at all -- Vanuatu's
payroll guide cited `employmentvanuatu.gov.vu`, which resolves to 192.0.2.1,
the RFC 5737 documentation range that is never routed. That is not a site that
went down. It is an address that was never a site.

The costlier case is a correction that moved a URL to a host that does not
exist. `za-income-tax.md` told readers to prefer `www.sarsefiling.gov.za` over
`www.sarsefiling.co.za`, calling the second "the older registered domain that
redirects". Only the second resolves, and it serves a page titled "SARS
eFiling". The guide was confidently, specifically wrong in the direction of a
hostname with no DNS record.

WHAT THIS DOES NOT PROVE. A name that fails here may be geo-restricted,
served only inside the country, behind split-horizon DNS, or briefly down.
This resolves names; it does not audit them. So the output is graded, and the
grades matter more than the count:

  hard        no address after 3 attempts, and no www/bare or parent variant
              resolves either. The strongest signal, and still not proof.
  deep-link   the cited subdomain has no address but its parent domain does.
              Usually an e-filing portal or API endpoint that moved. Also the
              most likely to be a false alarm from geo-DNS.
  reserved    resolves, but to loopback, private, link-local, or one of the
              RFC 5737 / RFC 2544 documentation and benchmark ranges. These
              are unambiguous: no public service is ever there.

Three design choices exist because the naive version got them wrong:

  * URL TEMPLATES ARE SKIPPED. Brazil's e-invoice guide documents
    `https://nfe.sefaz{UF}.{domain}/...`. A regex that stops at `{` invents the
    hostname `nfe.sefaz` and reports a defect in a correct line. Any URL
    carrying a placeholder is not a hostname and is not checked.
  * FAILURES ARE RETRIED. Three of the first forty-two failures resolved on a
    second attempt. Reporting them would have been three false accusations.
  * VARIANTS ARE TRIED. Most "dead" subdomains have a live parent, which is a
    different and much weaker finding than a dead domain.

Exits 0 always. This ranks leads for a human; it does not gate anything.

Usage: python3 scripts/check-cited-hosts.py [--selftest] [--grade hard|deep-link|reserved]
       python3 scripts/check-cited-hosts.py --no-network   # parse and classify only
"""
import os, re, sys, glob, json, time, socket, ipaddress, collections
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TREES = ('skills', 'agent-skills')

# Stop at whitespace and at the delimiters markdown wraps links in. The
# trailing-punctuation strip below handles "see https://x.gov/y." sentences.
URL = re.compile(r'https?://([^\s/?#\)\]>"\'`,]+)')

# A URL with a placeholder is a template, not an address.
PLACEHOLDER = re.compile(r'[{}<>$]|%[sd]|\.\.\.|XX+|YYYY|\bUF\b')

# The extractor above is deliberately loose, so everything it produces is
# validated against what a hostname can actually be. This is not belt and
# braces -- it is load-bearing, and the first version without it had a 59%
# false-positive rate on its strongest grade:
#
#   * `**https://www.sarsefiling.co.za**` yielded `www.sarsefiling.co.za**`,
#     so the checker reported a host that is demonstrably live as dead.
#   * China's guides write `（https://etax.chinatax.gov.cn）完成提交。...`,
#     and the full-width close paren is not in the stop set, so a whole
#     sentence of Chinese came through as a "hostname".
#
# A hostname in a URL is ASCII: letters, digits, hyphens, dots. An
# internationalised name would already be punycode. Anything else is the
# extractor's fault, not the corpus's, and must never reach the report.
HOSTNAME = re.compile(
    r'^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?'
    r'(?:\.[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)+$')

RESERVED_NETS = [
    ('TEST-NET-1 (RFC 5737)', '192.0.2.0/24'),
    ('TEST-NET-2 (RFC 5737)', '198.51.100.0/24'),
    ('TEST-NET-3 (RFC 5737)', '203.0.113.0/24'),
    ('benchmark (RFC 2544)', '198.18.0.0/15'),
]


def classify_address(ip):
    """Return a reason string if this address can never host a public service."""
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return 'unparseable address'
    # Order matters and is not obvious. Python's is_private is True for the
    # RFC 5737 documentation ranges and for link-local, so checking it first
    # swallows every specific label below it and reports TEST-NET-1 as
    # "private". The selftest caught exactly that. Specific before generic.
    if addr.is_loopback:
        return 'loopback'
    if addr.is_unspecified:
        return 'unspecified'
    for label, net in RESERVED_NETS:
        if addr in ipaddress.ip_network(net):
            return label
    if addr.is_link_local:
        return 'link-local'
    if addr.is_private:
        return 'private (RFC 1918)'
    return None


def collect_hosts(root=ROOT, trees=TREES):
    """Map hostname -> set of files citing it, skipping URL templates."""
    hosts = collections.defaultdict(set)
    files = []
    for tree in trees:
        files += glob.glob(os.path.join(root, tree, '**', '*.md'), recursive=True)
    for path in files:
        try:
            text = open(path, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        rel = os.path.relpath(path, root)
        for match in URL.finditer(text):
            raw = match.group(1)
            # The whole URL matters for the template test, not just the host.
            tail = text[match.start():match.start() + 200].split()[0]
            if PLACEHOLDER.search(tail):
                continue
            host = raw.strip('.,;:*_').lower()
            if not HOSTNAME.match(host):
                continue
            hosts[host].add(rel)
    return hosts, len(files)


def resolve(host, attempts=3, pause=0.4):
    for i in range(attempts):
        try:
            return socket.gethostbyname(host)
        except Exception:
            if i + 1 < attempts:
                time.sleep(pause)
    return None


def variants(host):
    """The www/bare counterpart, then the parent domain."""
    out = []
    out.append(host[4:] if host.startswith('www.') else 'www.' + host)
    if host.count('.') >= 2:
        out.append(host.split('.', 1)[1])
    return out


def grade(host):
    """Return (grade, detail) or None when the host is fine."""
    ip = resolve(host)
    if ip:
        reason = classify_address(ip)
        return ('reserved', f'{ip} is {reason}') if reason else None
    for alt in variants(host):
        alt_ip = resolve(alt, attempts=1)
        if alt_ip and not classify_address(alt_ip):
            return ('deep-link', f'no address; {alt} resolves to {alt_ip}')
    return ('hard', 'no address, and no www/bare or parent variant resolves')


def selftest():
    ok = True

    def check(cond, msg):
        nonlocal ok
        if not cond:
            print('  FAIL:', msg)
            ok = False

    # Reserved-range classification is the part that must never be wrong,
    # because it is reported without hedging.
    check(classify_address('192.0.2.1') == 'TEST-NET-1 (RFC 5737)', 'TEST-NET-1')
    check(classify_address('198.51.100.7') == 'TEST-NET-2 (RFC 5737)', 'TEST-NET-2')
    check(classify_address('203.0.113.9') == 'TEST-NET-3 (RFC 5737)', 'TEST-NET-3')
    check(classify_address('198.19.0.1') == 'benchmark (RFC 2544)', 'RFC 2544')
    check(classify_address('127.0.0.1') == 'loopback', 'loopback')
    check(classify_address('10.1.2.3') == 'private (RFC 1918)', 'RFC 1918 /8')
    check(classify_address('192.168.1.1') == 'private (RFC 1918)', 'RFC 1918 /16')
    check(classify_address('169.254.1.1') == 'link-local', 'link-local')
    check(classify_address('8.8.8.8') is None, 'a real address must pass')
    check(classify_address('172.64.149.55') is None, 'sarsefiling address must pass')

    # The template rule. Brazil's line is the case that produced a false
    # positive, so it is pinned here rather than described in a comment.
    check(PLACEHOLDER.search('https://nfe.sefaz{UF}.{domain}/ws'), 'brace template')
    check(PLACEHOLDER.search('https://homologacao.nfe.sefaz{UF}.{domain}/'), 'homologacao template')
    check(PLACEHOLDER.search('https://api.example.gov/v1/<id>'), 'angle template')
    check(PLACEHOLDER.search('https://x.gov/%s/report'), 'printf template')
    check(not PLACEHOLDER.search('https://www.sarsefiling.co.za/landing'), 'real URL must pass')
    check(not PLACEHOLDER.search('https://ujp.gov.mk/mk/regulativa/opis/441'), 'real URL must pass')

    # Host extraction end to end, including the two failure modes that made
    # the first version of this script untrustworthy. Both are pinned with
    # the real corpus text that produced them.
    def extract(probe):
        m = URL.search(probe)
        if not m:
            return None
        host = m.group(1).strip('.,;:*_').lower()
        return host if HOSTNAME.match(host) else None

    for probe, want in [
        ('see https://www.sars.gov.za.', 'www.sars.gov.za'),
        ('(https://vfsc.vu/legislation/)', 'vfsc.vu'),
        ('[x](https://ujp.gov.mk/mk/x), and', 'ujp.gov.mk'),
        # markdown bold around a bare URL -- reported a LIVE host as dead
        ('**https://www.sarsefiling.co.za**', 'www.sarsefiling.co.za'),
        ('use **https://taxpromax.firs.gov.ng** to file', 'taxpromax.firs.gov.ng'),
        ('_https://anan.org.ng_', 'anan.org.ng'),
    ]:
        check(extract(probe) == want,
              f'extract {probe!r} -> {extract(probe)!r}, wanted {want!r}')

    # Full-width CJK punctuation: the close paren is not a URL delimiter, so
    # a whole Chinese sentence came through as a hostname. It must be dropped
    # entirely rather than salvaged -- guessing where the host ends is how the
    # bug got in.
    for probe in [
        '\uff08https://etax.chinatax.gov.cn\uff09\u5b8c\u6210\u63d0\u4ea4\u3002',
        'https://inv-veri.chinatax.gov.cn\uff09\uff1b\u767d\u6761\u5165\u8d26',
        'https://www.chinatax.gov.cn\uff09\u7684',
    ]:
        check(extract(probe) is None,
              f'CJK-punctuated URL must be skipped, got {extract(probe)!r}')

    # And a hostname that is merely odd-looking must still pass.
    check(extract('https://xn--80ak6aa92e.com/x') == 'xn--80ak6aa92e.com', 'punycode')
    check(extract('https://etax.atk-ks.org/') == 'etax.atk-ks.org', 'hyphenated label')

    # DELIBERATELY NOT ASSERTED: that any particular host resolves. A selftest
    # that needs the network fails on a train. The resolution path is exercised
    # by running the script, not by this.
    print('selftest: address and template classification passes' if ok
          else 'selftest: FAILURES above')
    return 0 if ok else 1


def main(argv):
    hosts, nfiles = collect_hosts()
    print(f'scanned {nfiles} files; {len(hosts)} unique hostnames cited')
    if '--no-network' in argv:
        print('(--no-network: parsed and classified only, nothing resolved)')
        return 0

    with ThreadPoolExecutor(max_workers=24) as pool:
        results = list(pool.map(lambda h: (h, grade(h)), sorted(hosts)))

    findings = collections.defaultdict(list)
    for host, verdict in results:
        if verdict:
            findings[verdict[0]].append((host, verdict[1]))

    wanted = None
    if '--grade' in argv:
        wanted = argv[argv.index('--grade') + 1]

    total = sum(len(v) for v in findings.values())
    for g, blurb in (
        ('reserved', 'RESOLVES TO AN ADDRESS THAT CANNOT HOST A PUBLIC SERVICE'),
        ('hard', 'NO ADDRESS, AND NO VARIANT RESOLVES'),
        ('deep-link', 'SUBDOMAIN HAS NO ADDRESS BUT ITS PARENT DOES'),
    ):
        rows = sorted(findings.get(g, []))
        if not rows or (wanted and wanted != g):
            continue
        print(f'\n== {blurb} ({len(rows)}) ==')
        for host, detail in rows:
            cites = sorted(hosts[host])
            print(f'  {host}')
            print(f'      {detail}')
            print(f'      cited in {len(cites)} file(s): {", ".join(cites[:3])}'
                  + (' ...' if len(cites) > 3 else ''))

    print(f'\n{total} of {len(hosts)} cited hostnames did not resolve cleanly.')
    print('A name that fails here may be geo-restricted or briefly down. This')
    print('resolves names; it does not audit them. Read every hit before')
    print('changing a citation -- and check the replacement resolves.')
    return 0


if __name__ == '__main__':
    sys.exit(selftest() if '--selftest' in sys.argv else main(sys.argv))
