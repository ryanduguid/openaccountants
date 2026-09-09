"""List each jurisdiction's stated withholding rate on dividends, interest and royalties.

The fourth field opened to an outside pass, after the standard VAT rate, the
annual return deadline and the registration threshold. Withholding is a good
one to take early: it is three small numbers per jurisdiction, PwC publishes
them per country in one table, and getting one wrong means a payer under-
deducts on a cross-border payment and carries the shortfall themselves.

Same shape as the other list-*.py scripts. It dumps the claim so a human can
compare it against a source outside the repository. A number here is a claim to
verify, not a defect found.

Rows that disagree usually show the corpus doing its job rather than failing.
A jurisdiction sets different rates for residents and non-residents, for listed
and unlisted companies, for individuals and companies, and for treaty and
non-treaty payees, and the guides carry all of them. The residence split is
kept apart below for that reason; the rest you have to read.

The hedges are the leads. Many of these lines already end in "(approx --
confirm)" or say the position is uncertain, and those are the rows where an
outside source settles something rather than confirming it.

Checked against an outside source so far. Two jurisdictions, both hedged by
their own guides, and both settled.

  * Ethiopia  Right numbers, wrong reason. The guide read "5% to 10% depending
              on residency/context (approx -- confirm split between
              resident/non-resident)". The split is by the KIND of royalty, not
              the residency of the payee: 5% for art and culture, 10% for
              everything else, both raised from a flat 5% by the Income Tax
              (Amendment) Proclamation No. 1395/2025. A non-resident gets 10%
              with no art-and-culture reduction. Its dividend rate of 15% and
              interest rate of 10% were already correct under the same
              proclamation, so only the reason was wrong, which is the class
              this corpus keeps producing.
  * Iceland   Understated. The guide led with 12% on interest to non-residents
              while its own hedge said "PwC cites 13% gross, statutory 12%".
              PwC publishes 13% for corporate and individual recipients alike.
              The two have not been reconciled, so the guide now deducts at 13%
              on the methodology's own rule of taking the higher-tax position
              where a rate is unsettled. An under-deduction is the payer's
              liability, which is why this field defaults upward.

Read and found correct, so not chased again: Benin states three real dividend
rates (15% standard, 10% regularly distributed, 7% for WAEMU-listed companies),
Chile withholds 4% on interest to foreign banks against 35% generally, Colombia
20% on dividends from taxed earnings and 48% from untaxed, Vietnam 0% to
corporate shareholders and 5% to individuals, Zimbabwe 5% on listed shares and
10% on unlisted, Hong Kong 4.95% on royalties to unassociated non-residents.

  * Guatemala CORRECT, hedge resolved. 5% on dividends to non-residents and the
              same 5% to residents, a final tax withheld by the distributing
              company under Decreto 10-2012. The guide had said "some guides
              cite up to 10% -- confirm". They do, and 10% is not the dividend
              rate.
  * Barbados  CORRECT, and it nearly was not. A first search gave 15% on
              royalties to non-residents and the guide says 0%, which looked
              like a clear error. PwC, the source the guide cites, publishes 0%
              for royalties and interest and 0% or 5% for dividends. The 15%
              appears in older summaries and predates the 2019 convergence of
              the domestic and international regimes. The rate stays at 0% and
              the vague hedge is replaced by the specific conflict and a
              warning, because the payer carries an under-deduction.

That is the sixth time in this pass that an outside source disagreed and the
corpus turned out right. Read the guide, and read what it cites, before you
change a number.

Still open: 118 jurisdictions state a rate, 28 hedge at least one of their own,
and 4 have been checked.

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
PCT = re.compile(r'(\d{1,2}(?:\.\d+)?)\s?%')
NONRES = re.compile(r'\bnon[- ]?residents?\b|\babroad\b|\bforeign\b', re.I)
RESIDENT = re.compile(r'\bresidents?\b', re.I)
# A hedge the guide has put on itself.
HEDGE = re.compile(r'approx\b|confirm\b|uncertain\b|not uniformly published', re.I)


def kind_of(text):
    for name, pat in KIND:
        if re.search(pat, text, re.I):
            return name
    return None


# Facts live in a labelled bullet or a table row. Free prose was tried first
# and the column filled with rates belonging to other taxes: Bahrain appeared to
# withhold 46% on dividends, from a sentence reading "a 46% tax on oil, gas and
# petroleum"; the BVI 15%, from "imposes no corporate income tax, no capital
# gains tax"; and Ireland 0.0219% on interest, from a note about pension
# deductibility. All three jurisdictions state 0% correctly on the line beside.
BULL = re.compile(r'^\s*-\s+\*\*([^*]{4,90}?)\*\*\s*[\u2014-]+\s*(.+)$')
ROW = re.compile(r'^\s*\|\s*([^|]{4,90}?)\s*\|\s*([^|]+?)\s*\|')


def withholding_in(line):
    """Return (kind, residence, rate, hedged) for a WHT line, else None."""
    m = BULL.match(line) or ROW.match(line)
    if not m:
        return None
    label, value = m.group(1), m.group(2)
    if not LABEL.search(label):
        return None
    kind = kind_of(label)
    if not kind:
        return None
    p = PCT.search(value)
    if not p:
        return None
    if NONRES.search(label):
        res = 'non-resident'
    elif RESIDENT.search(label):
        res = 'resident'
    else:
        res = 'unspecified'
    return kind, res, p.group(1), bool(HEDGE.search(line))


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
        assert got == want, 'read %r from: %s' % (got, line[:70])
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
            for line in open(os.path.join(dp, fn), encoding='utf-8', errors='replace'):
                got = withholding_in(line)
                if not got:
                    continue
                kind, res, rate, hedge = got
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
