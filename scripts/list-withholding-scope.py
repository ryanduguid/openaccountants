"""List which heads of withholding tax each jurisdiction's guides actually state.

`list-withholding-rates.py` checks the RATE on dividends, interest and
royalties. Ten jurisdictions were then read by hand against their statutes, and
four were wrong. What is more interesting is the other six: every rate they
stated was correct and every one of them was materially incomplete. The defect
was not a number. It was a missing head of charge.

North Macedonia stated three of the eight categories its Law on Profit Tax
withholds on, omitting entertainment and sporting activities, management and
consulting services, insurance premiums, telecommunications and the lease of
immovable property. Azerbaijan stated four of eight, omitting rent at 14%,
insurance at 4% and telecommunications at 6%. Namibia stated the 10% on
management fees and not the 25% on non-resident directors and entertainers,
which carries no treaty relief at all.

A guide that names dividends, interest and royalties and stops reads as
complete. Nothing in this repo could see that it was not, because every check
here compares a stated value against something, and an omitted head states
nothing. This script inverts that: it reports what each jurisdiction's guides
DO name, so the gaps become visible as gaps.

WHAT THIS CATCHES, AND WHAT IT DOES NOT

Of the ten jurisdictions read by hand, this would have flagged one: North
Macedonia, which named only the classic three. That is not a good hit rate and
saying so is the point of this note. There are three failure shapes here and
this sees one of them.

  1. NAMES ONLY THE CLASSIC THREE.  Seen: North Macedonia. Caught here, as
     `classic-only`.
  2. NAMES SOME EXTRA HEADS, MISSES OTHERS.  Seen: Azerbaijan, which had a
     services line and no rent, insurance or telecommunications line. Partly
     caught: it shows up as a thin profile against jurisdictions that name
     seven, but nothing here knows which heads Azerbaijan's Tax Code actually
     charges, so it is a ranking and not a finding.
  3. NAMES THE HEAD, MISSES THE CARVE-OUT.  Seen: Namibia, whose service line
     was right and whose 25% director and entertainer rate was absent; Angola,
     whose 6.5% was right and which did not say the rate is an advance for a
     resident and final for a non-resident. NOT caught, and not catchable this
     way. A head that is named passes.

So this is a queue, not a report of defects. A jurisdiction near the top of it
has either a thin withholding regime or a thin guide, and only the statute
distinguishes those. Estonia genuinely charges few heads. North Macedonia
charged eight and said three.

The heads below were chosen from what the ten hand-read jurisdictions actually
levied, not from a model treaty, which is why `branch` and `directors` are in
the list: Namibia and Bangladesh both turn on them and neither is a classic
category.

FIRST DRAW OFF THE QUEUE

64 of 142 jurisdictions named only classic heads. Kenya was taken first, for
readership rather than for anything the output said about it, and it carried one
stale rate and six missing heads:

  * Dividends to non-residents were stated at 10%. They are 15%, and have been
    since the Finance Act 2023. Five points, and the payer carries a shortfall.
  * Management and professional fees: 5% resident, 20% non-resident. Absent.
  * Training fees: 5% resident, 20% non-resident. Absent.
  * Contractual fees: 3% resident, 20% non-resident. Absent.
  * Rent to non-residents: 30% on immovable property, 15% on other property.
    Absent -- and 30% is the HIGHEST rate in Kenya's withholding table. A guide
    that stops after royalties leaves its reader treating a non-resident
    landlord as a 15% case, or as no case at all.
  * Insurance and reinsurance premiums: 5% resident. Absent.
  * Interest sub-rates by instrument (bearer instruments 25%, government bonds
    of two years or more 15%, bearer bonds of ten years or more 10%). Absent;
    the guide carried only the 15% general rate.

That is the shape the queue is for. Kenya's three stated rates were two right
and one stale, and the damage was mostly in what was not there.

WHY 64 JURISDICTIONS LOOK THE SAME

Turkey and Thailand were taken next, both from the classic-only list and both
already worked on this branch for their rates. Neither guide was careless. PwC's
`corporate/withholding-taxes` page -- the page both guides cite, and the page
most of this corpus was built from -- carries, for these two countries,
dividends, interest, royalties and a treaty matrix. Nothing else. The other
heads are real and are somewhere else entirely.

  * Turkey also withholds 20% on professional services (17% on certain
    copyright work), 20% on commercial rent computed on the GROSS rent, and 5%
    on progress payments to contractors on construction spanning more than one
    calendar year, with 1% for certain long-term projects. Its 30% on payments
    to harmful-tax-competition jurisdictions IS on the PwC page, and the guide
    did not carry that either.
  * Thailand also withholds 15% under Section 70 on service income,
    professional services and rentals paid to a foreign company not carrying on
    business there, and domestically 3% on professional and service fees, 5% on
    rent, 2% on advertising and 1% on transport.

So the classic-only shape is not sloppiness. It is faithful reproduction of a
source that is itself three-headed for that country, and the corpus inherited
its scope along with its numbers. Two things follow.

First, this queue is systematically incomplete rather than randomly so, which
makes it worth working all the way down rather than sampling.

Second, and more useful: RE-READING THE PAGE THE GUIDE CITES WILL NEVER FIND
THIS. Every other check on this branch was satisfied by going back to the
authority the guide named. Here the guide named its source faithfully and the
source does not answer the question. Coverage varies by country and cannot be
assumed either way -- PwC's Kenya page does carry the full table, which is how
Kenya's six missing heads were found in one fetch. When a jurisdiction appears
below with three heads, the next step is a different page or the statute, not
the one in the citation.

A CAVEAT ABOUT THE THIN END

Jurisdiction keys come from the third path segment, so `us`, `im`, `in` and `nc`
are Isle of Man, the United States, Indiana and North Carolina, and the
single-head rows are mostly guides shaped differently rather than jurisdictions
withholding on one thing. Read the classic-only list, which is the real queue;
treat the 1- and 2-head rows as a note about guide structure.

Usage: python3 scripts/list-withholding-scope.py [--selftest] [--classic-only]
"""
import os, re, sys, collections

# Ordered for reading, not for precedence: a label matching several heads
# records all of them, because "interest and royalties" is two heads and
# recording only the first is how a guide comes to look complete.
HEADS = (
    ('dividends', r'dividend'),
    ('interest', r'\binterest\b'),
    ('royalties', r'royalt'),
    ('services', r'\bservices?\b|\btechnical\b|\bmanagement\b|\bconsultanc|'
                 r'\bconsulting\b|\bprofessional fees?\b|\bcontractor'),
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
ROW = re.compile(r'^\s*\|\s*([^|]{4,90}?)\s*\|\s*([^|]+?)\s*\|')
LABEL = re.compile(r'\b(?:WHT|withholding(?:\s+tax)?|NRST|'
                   r'non[- ]?residents?.{0,12}tax)\b', re.I)
# A head is only a head if the label commits to a rate or an exemption. "See
# the withholding section" is a cross-reference, not a charge.
VALUE = re.compile(r'\d|\bexempt\b|\bnil\b|\bno\b|\bzero\b', re.I)

SKIP_DIRS = ('orchestrator', 'cross-border', 'verticals', 'integrations')


def heads_in(line):
    """Return the set of withholding heads a labelled line names, else None."""
    m = BULL.match(line) or ROW.match(line)
    if not m:
        return None
    label, value = m.group(1), m.group(2)
    if not LABEL.search(label):
        return None
    if not VALUE.search(value):
        return None
    found = {name for name, pat in HEADS if re.search(pat, label, re.I)}
    return found or None


def scan(root='skills'):
    out = collections.defaultdict(set)
    for dp, _, fns in os.walk(root):
        parts = dp.split(os.sep)
        jur = parts[2] if len(parts) >= 3 else ''
        if not jur or jur in SKIP_DIRS:
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            with open(os.path.join(dp, fn), encoding='utf-8', errors='replace') as fh:
                for line in fh:
                    got = heads_in(line)
                    if got:
                        out[jur] |= got
    return out


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
    print('selftest: %d cases pass' % len(cases))


def main(classic_only=False):
    found = scan()
    rows = []
    for jur, heads in found.items():
        extras = sorted(heads - set(CLASSIC))
        rows.append((len(heads), jur, sorted(heads), extras))
    rows.sort(key=lambda r: (r[0], r[1]))

    classic = [r for r in rows if not r[3]]
    if classic_only:
        for _, jur, heads, _ in classic:
            print('%-26s %s' % (jur, ', '.join(heads)))
        print('\n%d of %d jurisdictions name only dividends, interest and/or '
              'royalties.' % (len(classic), len(rows)))
        return 1 if classic else 0

    for n, jur, heads, _ in rows:
        print('%2d  %-26s %s' % (n, jur, ', '.join(heads)))
    print()
    print('jurisdictions naming a withholding head:', len(rows))
    print('naming only classic heads (the queue):', len(classic))
    for _, jur, heads, _ in classic:
        print('   classic-only: %-24s %s' % (jur, ', '.join(heads)))
    spread = collections.Counter(n for n, _, _, _ in rows)
    print('heads named per jurisdiction:', ', '.join(
        '%d:%d' % (k, spread[k]) for k in sorted(spread)))
    return 1 if classic else 0


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        sys.exit(main('--classic-only' in sys.argv))
