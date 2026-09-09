"""List which heads of withholding tax each jurisdiction's guides state.

Every other check here compares a stated value against something. An omitted
head of charge states nothing, so nothing could see it. This inverts that: it
reports what each jurisdiction DOES name, and a guide naming only dividends,
interest and royalties sits oddly beside one naming eight.

It is a queue, not a defect report. A jurisdiction is queued because its profile
is thin against its peers, which is a reason to spend an hour, not a finding.

Run --show <jurisdiction> before editing. It prints every withholding-labelled
line that jurisdiction has, with file and line number. Three wrong claims about
what a guide omits were written on this branch from the summary alone.

Usage: python3 scripts/list-withholding-scope.py [--selftest] [--classic-only]
       python3 scripts/list-withholding-scope.py --show <jurisdiction>
"""
import os, re, sys, collections

# Ordered for reading, not for precedence: a label matching several heads
# records all of them, because "interest and royalties" is two heads and
# recording only the first is how a guide comes to look complete.
HEADS = (
    ('dividends', r'dividend'),
    ('interest', r'\binterest\b'),
    ('royalties', r'royalt'),
    # A bare "fees" counts. Zimbabwe's head is called "non-residents' tax on
    # fees" and nothing else in the label says what kind, so requiring
    # "professional fees" left the whole head invisible and the jurisdiction
    # on the queue after it had been worked.
    ('services', r'\bservices?\b|\btechnical\b|\bmanagement\b|\bconsultanc|'
                 r'\bconsulting\b|\bfees?\b|\bcontractor'),
    ('rent', r'\brent\b|\brentals?\b|\bleas(?:e|ing)\b|\bhire\b|'
             r'\bimmovable propert|\bmovable propert'),
    ('insurance', r'\binsurance\b|\breinsurance\b|\bpremiums?\b'),
    ('telecoms', r'\btelecom|\btransport|\bfreight\b|\bshipping\b|\bairtime\b'),
    ('entertainment', r'\bentertain|\bsport|\bartistes?\b|\bperformer|\bathlete'),
    ('directors', r"\bdirectors?\b|\bboard fees?\b"),
    ('branch', r'\bbranch\b[^|\n]{0,20}(?:profit|remittance)|\bremittance tax\b'),
)
CLASSIC = ('dividends', 'interest', 'royalties')

# Same extraction as list-withholding-rates.py, and for the same reason: free
# prose put rates from other taxes into that script's output, so a fact has to
# arrive in a labelled bullet or a table row.
BULL = re.compile(r'^\s*-\s+\*\*([^*]{4,90}?)\*\*\s*[—-]+\s*(.+)$')
# The value is EVERY remaining cell, not just the second one. Israel's rate
# table is `| Payment type | Hebrew | Default rate | ITO Section |`, so reading
# only the second cell got the Hebrew term and no rate, and the whole table was
# discarded for stating no value. Any table that puts the rate in a later
# column had the same problem.
ROW = re.compile(r'^\s*\|\s*([^|]{4,90}?)\s*\|\s*(.+?)\s*\|?\s*$')
LABEL = re.compile(r'\b(?:WHT|withholding(?:\s+tax)?|NRST|'
                   r'non[- ]?residents?.{0,12}tax)\b', re.I)
# A head is only a head if the label commits to a rate or an exemption. "See
# the withholding section" is a cross-reference, not a charge.
VALUE = re.compile(r'\d|\bexempt\b|\bnil\b|\bno\b|\bzero\b', re.I)
PCT = re.compile(r'(\d{1,3}(?:\.\d+)?)\s?(?:%|per\s?cent\b|percent\b)', re.I)
NIL = re.compile(r'^\W*(none|nil|not applicable|n/?a)\b|\bno withholding\b|'
                 r'\bimposes no\b|\blevies no\b', re.I)


def is_zero(value):
    """True where a withholding line commits to nothing being withheld.

    A jurisdiction that charges no withholding at all names no service, rent or
    insurance head because there is nothing to name, so it looks identical to a
    thin guide. The British Virgin Islands, Cayman, Bermuda, the Bahamas,
    Vanuatu and Bahrain were all sitting on the queue for that reason, and all
    six already state their zeros plainly. Reading the rate separates them.

    KNOWN MISS: a payroll PAYE line defeats this. Libya levies no withholding at
    all, but its payroll guide says employers withhold PIT at 5%/10%, so a
    non-zero rate is seen and Libya stays off the zero list. Employment
    withholding is a different tax, and no pattern separates the two without
    also losing a real non-resident employment-income head. Asserted in the
    selftest so it stays known.
    """
    rates = PCT.findall(value)
    if rates:
        return all(float(r) == 0 for r in rates)
    return bool(NIL.search(value))

SKIP_DIRS = ('orchestrator', 'cross-border', 'verticals', 'integrations')

# Whole trees whose directories are not jurisdictions that levy non-resident
# withholding. `us-states` is the one that matters: a US state does not charge
# withholding on dividends, interest or royalties paid abroad -- that is
# federal -- so all 52 directories under it are guaranteed noise, and the queue
# was carrying Indiana because `in-payroll.md` mentions an interest rate on
# unpaid PAYE withholding. The other three hold workflow bases and templates
# with no jurisdiction of their own.
SKIP_TREES = ('us-states', 'foundation', 'templates', 'patterns')
# Not skippable, and worth knowing before treating a major jurisdiction as thin:
# `canada` and `us` look classic-only because their withholding content sits in
# topic-sliced capital-gains guides (Part XIII and s.116; FIRPTA and the 30%
# dividend rate), not because a head is missing. Telling that apart from a thin
# CIT guide would mean encoding an expectation about which file a head belongs
# in. Check the filenames in --show first.


def heads_in(line, in_wht_guide=False):
    """Return the set of withholding heads a labelled line names, else None.

    `in_wht_guide` relaxes the requirement that the label itself say
    "withholding". Set it when the FILE is a dedicated withholding guide: such a
    guide does not repeat the word in every row label, so requiring it scored a
    proper withholding guide lower than three bullets bolted onto a CIT guide.
    Israel's whole rate table -- services 30%, business rent 35%, royalties 23%
    -- was invisible for that reason.
    """
    m = BULL.match(line) or ROW.match(line)
    if not m:
        return None
    label, value = m.group(1), m.group(2)
    if not (LABEL.search(label) or in_wht_guide):
        return None
    if not VALUE.search(value):
        return None
    found = {name for name, pat in HEADS if re.search(pat, label, re.I)}
    return found or None


# A file whose name says it is about withholding. Its rows do not need to
# repeat the word -- see heads_in.
WHT_FILE = re.compile(r'withhold|(?:^|[-_])wht(?:[-_.]|$)', re.I)


URL = re.compile(r'https?://\S+')


def strip_urls(text):
    """Remove citation URLs before matching head words against prose.

    San Marino sat on the triage list because its payroll guide cites
    `remotepeople.com/countries/san-marino/hire-employees/payroll-tax/` and the
    rent pattern matches the word "hire". A slug in a citation is not a head of
    charge, and every guide in this corpus carries citation URLs, so that was
    noise available to every jurisdiction rather than a fact about San Marino.

    Worth noting what fixing it did to the numbers, because it is the opposite
    of what removing a false positive usually does. San Marino and Guinea were
    in the cheap `triage` column *because* of the URL match. With it gone they
    have nothing anywhere, so they moved into the real queue: triage 11 -> 9,
    queue 18 -> 20. The artefact was not inflating the workload, it was hiding
    two entries from it. A checker's false positive can make a problem look
    smaller as easily as larger.
    """
    return URL.sub(' ', text)


def body_heads_in(line):
    """Heads named in a withholding line's BODY rather than its label.

    URLs are stripped first -- see strip_urls.

    One false positive is left visible rather than patched: "National Insurance
    Scheme" reads as the insurance head, which is how Barbados reached the
    triage list from a payroll guide about NIS contributions. Social insurance
    is not withholding on insurance premiums, but no pattern separates them
    without also losing a real "insurance premiums" head. Triage means read the
    line.

    Weaker evidence than heads_in and reported separately for that reason. A
    body is prose: "insurance" turns up in a sentence about premiums that is
    really about something else, and a guide can mention a head in passing
    without stating a rate for it. It is still worth having, because 15 of the
    50 jurisdictions on the queue name an extra head this way, and working them
    as if nothing were there wastes the lookup.
    """
    m = BULL.match(line) or ROW.match(line)
    if not m:
        return None
    label, value = m.group(1), m.group(2)
    if not LABEL.search(label):
        return None
    found = {name for name, pat in HEADS
             if name not in CLASSIC and re.search(pat, strip_urls(value), re.I)}
    return found or None


def scan(root='skills'):
    """Return {jurisdiction: (label_heads, body_only_extras, all_rates_zero)}."""
    labels = collections.defaultdict(set)
    bodies = collections.defaultdict(set)
    nonzero = collections.defaultdict(bool)
    for dp, _, fns in os.walk(root):
        parts = dp.split(os.sep)
        if len(parts) >= 2 and parts[1] in SKIP_TREES:
            continue
        jur = parts[2] if len(parts) >= 3 else ''
        if not jur or jur in SKIP_DIRS:
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            wht_guide = bool(WHT_FILE.search(fn))
            with open(os.path.join(dp, fn), encoding='utf-8', errors='replace') as fh:
                for line in fh:
                    got = heads_in(line, wht_guide)
                    if got:
                        labels[jur] |= got
                        m = BULL.match(line) or ROW.match(line)
                        if not is_zero(m.group(2)):
                            nonzero[jur] = True
                    got = body_heads_in(line)
                    if got:
                        bodies[jur] |= got
    return {j: (labels[j], bodies[j] - labels[j], not nonzero[j]) for j in labels}


def selftest():
    """Real lines, including the ones the hand pass added or corrected."""
    cases = [
        ('- **Withholding tax on dividends** - 5% percent  _(Tax Code)_',
         {'dividends'}),
        ('- **Withholding tax on interest and royalties to non-residents** - 15% '
         '(general); 25% to non-cooperative jurisdictions %', {'interest', 'royalties'}),
        ('- **Withholding tax on management/consultancy/technical fees to '
         'non-residents** - 10 percent', {'services'}),
        ('- **Withholding tax on non-resident directors and foreign entertainers** '
         '- **25%**, and no treaty relief is available', {'directors', 'entertainment'}),
        ('- **Withholding on rent (movable and immovable property)** - **14%**',
         {'rent'}),
        ('- **Withholding on risk insurance and reinsurance premiums** - **4%**',
         {'insurance'}),
        ('- **Withholding on telecommunications and international transport '
         'services** - **6%**', {'telecoms', 'services'}),
        ('- **NRST on dividends - all other cases** - 20 percent', {'dividends'}),
        ('| WHT on branch remittance | 10% | Income Tax Act |', {'branch'}),
        # a bare "fees" head, as ZIMRA names it
        ("- **Non-residents' tax on fees** - **15%** of the gross where a person "
         'pays a non-resident for services performed in Zimbabwe', {'services'}),
        # PNG's technical-fee head, missed until the third pass over the queue
        ('- **Withholding / non-resident tax on technical fees** - **15%** on '
         'the gross fee', {'services'}),
    ]
    for line, want in cases:
        got = heads_in(line)
        assert got == want, 'read %r, wanted %r, from: %s' % (got, want, line[:60])
    # not a withholding line at all
    assert heads_in('- **Standard corporate income tax rate** - 25% percent') is None
    # a withholding label that commits to nothing is a cross-reference
    assert heads_in('- **Withholding tax on services** - see the withholding '
                    'section below') is None
    # prose, whatever words it contains
    assert heads_in('Withholding taxes apply to dividends, interest and royalties, '
                    'subject to EU directives and tax treaties.') is None

    # Inside a dedicated withholding guide the row labels do not repeat the
    # word "withholding" -- Israel's table is the case that found this.
    israel_row = ('| Services -- individuals, no certificate | '
                  'transliterated Hebrew term | 30% (up to ~47% for unverified '
                  'payees) | 164 |')
    assert heads_in(israel_row) is None, 'needs the guide-level flag'
    assert heads_in(israel_row, in_wht_guide=True) == {'services'}, \
        heads_in(israel_row, in_wht_guide=True)
    # and the rate is in the THIRD cell, so the value must be every cell after
    # the label, not just the second one
    rent_row = '| Rent -- business/commercial property | Hebrew | 35% | 170 |'
    assert heads_in(rent_row, in_wht_guide=True) == {'rent'}
    # the flag relaxes the label requirement, it does not stop requiring a rate
    assert heads_in('| Payment type | Hebrew | Default rate | ITO Section |',
                    in_wht_guide=True) is None
    # filenames that turn the flag on, and one that must not
    assert WHT_FILE.search('il-tax-withholding.md')
    assert WHT_FILE.search('ng-wht.md')
    assert not WHT_FILE.search('ba-corporate-income-tax.md')
    assert not WHT_FILE.search('mw-payroll-social.md')

    # a citation URL is not a head of charge (San Marino's "hire-employees" slug)
    assert body_heads_in(
        '- **Payroll income-tax withholding** - Employers withhold IGR at source '
        '_([Law 166/2013](https://remotepeople.com/countries/san-marino/'
        'hire-employees/payroll-tax/))_') is None
    # but the same word in the prose itself still counts
    assert body_heads_in(
        '- **Withholding on payments** - 15%, including hire of movable '
        'property') == {'rent'}

    # KNOWN FALSE POSITIVE, documented on body_heads_in: social insurance reads
    # as the insurance head. Left visible because no pattern separates it from a
    # real insurance-premium head.
    assert body_heads_in(
        '- **Employer PAYE and NIS withholding overview** - Employers withhold '
        'income tax under PAYE and deduct National Insurance Scheme (NIS) '
        'contributions') == {'insurance'}

    # zero detection, including the phrasings the hand pass wrote into the guides
    assert is_zero('**0% -- Libya levies no withholding tax on dividends**')
    assert is_zero('**Libya levies no withholding taxes at all.** Not on '
                   'dividends, interest, royalties, services or rent')
    assert is_zero('None')
    assert not is_zero('15% on the gross fee')

    # KNOWN MISS, documented above: a payroll PAYE line keeps a zero-WHT
    # jurisdiction off the zero list, because employment withholding is a
    # different tax from the non-resident payment withholding modelled here and
    # nothing distinguishes them at this level.
    assert not is_zero('Employers withhold personal income tax (5%/10%) at '
                       'source from salaries and remit it monthly')
    print('selftest: %d cases pass (plus zero detection and 1 known miss)'
          % len(cases))


def show(jur, root='skills'):
    """Print every withholding line one jurisdiction has, with its file.

    This exists because of a mistake made three times on this branch. The
    summary output prints a jurisdiction's HEADS, not its lines, and three
    times a fix was written asserting "this guide did not carry X" after
    reading only those heads. Seychelles already had the service-fee line three
    bullets below the ones the checker surfaced. Vietnam already had four FCT
    lines further down the same file. Both claims were false and both were
    caught only by the editor showing the whole file back.

    A resolution to read more carefully has now failed twice, so this is the
    mechanism instead: run --show before editing, read every line it prints,
    and only then write about what a guide omits.
    """
    seen = 0
    for dp, _, fns in sorted(os.walk(root)):
        parts = dp.split(os.sep)
        if len(parts) < 3 or parts[2] != jur:
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(dp, fn)
            with open(path, encoding='utf-8', errors='replace') as fh:
                for n, line in enumerate(fh, 1):
                    m = BULL.match(line) or ROW.match(line)
                    if not m or not LABEL.search(m.group(1)):
                        continue
                    heads = {name for name, pat in HEADS
                             if re.search(pat, m.group(1), re.I)}
                    body = {name for name, pat in HEADS
                            if name not in CLASSIC and re.search(pat, m.group(2), re.I)}
                    tag = ','.join(sorted(heads)) or '-'
                    extra = (' +body:' + ','.join(sorted(body - heads))) if body - heads else ''
                    print('%s:%d  [%s%s]\n    %s\n    %s' % (
                        path, n, tag, extra, m.group(1).strip(),
                        m.group(2).strip()[:300]))
                    seen += 1
    if not seen:
        print('no withholding-labelled lines found for %r' % jur)
    else:
        print('\n%d withholding-labelled line(s) in %s. Read all of them before '
              'writing that the guide omits anything.' % (seen, jur))
    return 0


def main(classic_only=False):
    found = scan()
    rows = []
    for jur, (heads, body, zero) in found.items():
        extras = sorted(heads - set(CLASSIC))
        rows.append((len(heads), jur, sorted(heads), extras, sorted(body), zero))
    rows.sort(key=lambda r: (r[0], r[1]))

    # A jurisdiction that withholds nothing names no extra head because there is
    # nothing to name. That is a complete guide, not a thin one.
    zero_rated = [r for r in rows if r[5] and not r[3]]
    classic = [r for r in rows if not r[3] and not r[5]]
    # Split what remains: an entry whose bullets MENTION an extra head in prose
    # is likely already half-covered, and is cheaper to triage than to research.
    bare = [r for r in classic if not r[4]]
    mentions = [r for r in classic if r[4]]

    if classic_only:
        for _, jur, heads, _, body, _z in classic:
            note = ('  (body mentions: %s)' % ', '.join(body)) if body else ''
            print('%-26s %s%s' % (jur, ', '.join(heads), note))
        print('\n%d of %d jurisdictions name only dividends, interest and/or '
              'royalties.' % (len(classic), len(rows)))
        print('%d name nothing else anywhere; %d mention an extra head in a '
              'bullet body.' % (len(bare), len(mentions)))
        return 1 if bare else 0

    for n, jur, heads, _, _, _z in rows:
        print('%2d  %-26s %s' % (n, jur, ', '.join(heads)))
    print()
    print('jurisdictions naming a withholding head:', len(rows))
    print('withholding nothing at all (complete, not thin):', len(zero_rated))
    for _, jur, heads, _, _, _z in zero_rated:
        print('   zero-wht: %-24s %s' % (jur, ', '.join(heads)))
    print('naming only classic heads:', len(classic))
    print('  of those, nothing else anywhere (the queue):', len(bare))
    for _, jur, heads, _, _, _z in bare:
        print('   queue:  %-24s %s' % (jur, ', '.join(heads)))
    print('  of those, an extra head appears in a bullet body (triage first):',
          len(mentions))
    for _, jur, _, _, body, _z in mentions:
        print('   triage: %-24s body mentions %s' % (jur, ', '.join(body)))
    spread = collections.Counter(n for n, _, _, _, _, _ in rows)
    print('heads named per jurisdiction:', ', '.join(
        '%d:%d' % (k, spread[k]) for k in sorted(spread)))
    return 1 if bare else 0


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    elif '--show' in sys.argv:
        i = sys.argv.index('--show')
        if i + 1 >= len(sys.argv):
            sys.exit('--show needs a jurisdiction, e.g. --show vietnam')
        sys.exit(show(sys.argv[i + 1]))
    else:
        sys.exit(main('--classic-only' in sys.argv))
