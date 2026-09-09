"""List stated dividend, interest and royalty withholding rates for review.

Reads labelled facts and tables in withholding sections. A shared rate is listed
for each named payment type. Multi-rate shared labels are omitted; single-type
facts retain the first stated rate. Residence comes from the label or section.
Treat these as claims to verify, not a complete rate schedule or legal findings.

Usage: python3 scripts/list-withholding-rates.py [--selftest]
"""
import os, re, sys, collections

KIND = (('dividends', r'dividend'),
        ('interest', r'interest'),
        ('royalties', r'royalt'))

# "- **WHT on royalties (paid abroad)** - 10% to foreign individuals"
# "- **Withholding tax on dividends** - 10% percent"
LABEL = re.compile(r'\b(?:WHT|withholding(?:\s+tax)?)\b[^|\n]{0,40}?'
                   r'\b(dividend|interest|royalt)', re.I)
# Same spelling problem as the hedged-claim lister: Peru writes its dividend,
# interest and royalty rates as "5 percent", and requiring "%" discarded all
# three.
PCT = re.compile(r'(\d{1,2}(?:\.\d+)?)\s?(?:%|per\s?cent\b|percent\b)', re.I)
NONRES = re.compile(r'\bnon[- ]?residents?\b|\babroad\b|\bforeign\b', re.I)
RESIDENT = re.compile(r'\bresidents?\b', re.I)
# A hedge the guide has put on itself.
HEDGE = re.compile(r'approx\b|confirm\b|uncertain\b|not uniformly published', re.I)


# Facts live in a labelled bullet or a table row. Free prose was tried first
# and the column filled with rates belonging to other taxes: Bahrain appeared to
# withhold 46% on dividends, from a sentence reading "a 46% tax on oil, gas and
# petroleum"; the BVI 15%, from "imposes no corporate income tax, no capital
# gains tax"; and Ireland 0.0219% on interest, from a note about pension
# deductibility. All three jurisdictions state 0% correctly on the line beside.
BULL = re.compile(r'^\s*-\s+\*\*([^*]{4,90}?)\*\*\s*[\u2014-]+\s*(.+)$')
ROW = re.compile(r'^\s*\|\s*([^|]{4,90}?)\s*\|\s*([^|]+?)\s*\|')


def withholding_in(line, context=''):
    """Return (kind, residence, rate, hedged) records for a labelled WHT fact."""
    m = BULL.match(line) or ROW.match(line)
    if not m:
        return None
    label, value = m.group(1), m.group(2)
    if not LABEL.search(label) and not (ROW.match(line) and context):
        return None
    kinds = [name for name, pat in KIND if re.search(pat, label, re.I)]
    if not kinds:
        return None
    p = PCT.search(value)
    if not p:
        return None
    if len(kinds) > 1 and len(set(PCT.findall(value))) > 1:
        return None  # Different rates need a human to assign payment types.
    residence = label if NONRES.search(label) or RESIDENT.search(label) else context
    if NONRES.search(residence):
        res = 'non-resident'
    elif RESIDENT.search(residence):
        res = 'resident'
    else:
        res = 'unspecified'
    return [(kind, res, p.group(1), bool(HEDGE.search(line))) for kind in kinds]


def selftest():
    """Real lines from the corpus, including two the guides hedge themselves."""
    cases = [
        ('- **WHT on dividends (resident)** - 15% percent  _(Income Tax Act)_',
         ('dividends', 'resident', '15', False)),
        ('- **WHT on dividends to non-residents** - 15% (subject to reduction under an '
         'applicable double tax treaty) %', ('dividends', 'non-resident', '15', False)),
        ('- **WHT on royalties (paid abroad)** - 10% to foreign individuals; 12% to foreign '
         'companies percent', ('royalties', 'non-resident', '10', False)),
        ('- **WHT on royalties to non-residents** - 10% (unless reduced by tax treaty) %',
         ('royalties', 'non-resident', '10', False)),
        ('- **WHT on interest (non-resident)** - 20% percent (Treaty relief may reduce this)',
         ('interest', 'non-resident', '20', False)),
        # the guide flags its own uncertainty, and that is the row worth chasing
        ('- **Withholding tax on dividends** - 10% percent ((approx - confirm; Finance Law 2025 '
         'repealed certain dividend WHT exemptions))', ('dividends', 'unspecified', '10', True)),
    ]
    for line, want in cases:
        got = withholding_in(line)
        assert got == [want], 'read %r from: %s' % (got, line[:70])
    # prose is not a labelled fact, whatever words it contains
    assert withholding_in('Bahrain has no general corporate income tax. Only two regimes impose '
                          'direct tax: a 46% tax on oil, gas and petroleum, and withholding on '
                          'dividends does not exist.') is None
    # a rate with no percentage is nothing to record
    assert withholding_in('- **WHT on interest** - Rate not uniformly published - confirm '
                          'with the Inland Revenue Department') is None
    # a line about something else entirely
    assert withholding_in('| Filing deadline | 31 October of the following year |') is None
    print('selftest: %d cases pass' % len(cases))


def main():
    out = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    hedged = collections.defaultdict(set)
    for dp, _, fns in os.walk('skills'):
        parts = dp.split(os.sep)
        jur = parts[2] if len(parts) >= 3 else ''
        if not jur or jur in ('orchestrator', 'cross-border', 'verticals', 'integrations'):
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            context = ''
            for line in open(os.path.join(dp, fn), encoding='utf-8', errors='replace'):
                if line.lstrip().startswith('#'):
                    context = line if (
                        re.search(r'\b(?:WHT|withholding)\b', line, re.I)
                        or (re.search(r'(?:wht|withholding)', fn, re.I)
                            and re.search(r'\brates\b', line, re.I))
                    ) else ''
                got = withholding_in(line, context)
                if not got:
                    continue
                for kind, res, rate, hedge in got:
                    out[jur]['%s/%s' % (kind, res)][rate + '%'] += 1
                    if hedge:
                        hedged[jur].add(kind)

    for jur in sorted(out):
        for key in sorted(out[jur]):
            counts = out[jur][key]
            flag = '  <-- guides disagree' if len(counts) > 1 else ''
            print('%-24s %-22s %s%s' % (jur, key, ', '.join(
                '%s (%d)' % (r, n) for r, n in counts.most_common()), flag))
    print('jurisdictions stating a withholding rate:', len(out))
    print('jurisdictions hedging at least one of them:', len(hedged))
    for jur in sorted(hedged):
        print('   hedged: %-22s %s' % (jur, ', '.join(sorted(hedged[jur]))))


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        main()
