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

TWO TRUE NEGATIVES, AND THE RULE THEY SUGGEST

Ukraine and Kazakhstan came off the queue next and were both thin -- Ukraine
missing engineering, agency and brokerage, freight at 6%, real-estate and
securities disposals, Eurobond and government-bond treatment and deemed
dividends; Kazakhstan missing services at 20%, the 20% residual, insurance at
15%, reinsurance and international transport at 5% and constructive dividends,
and attributing its reduced 5% dividend rate to a holding-period test when the
real test is a 230,000 MCI distribution ceiling.

Switzerland and Hong Kong were then checked expecting the same, and both were
entirely correct. Switzerland charges 35% on dividends and on interest from
bonds and bank deposits, nothing on ordinary loan interest, and nothing at all
on royalties. Hong Kong charges nothing on dividends or interest and taxes
royalties through deemed assessable profits, 4.95% to an unassociated
non-resident and up to 16.5% to an associate. Three heads each, because three
heads is what those two jurisdictions have.

So the queue has real true negatives, and the two of them share the property
that makes them verifiable in a minute rather than an hour: THEY STATE THE ZERO.
Switzerland's guide says "0% -- Switzerland levies no withholding tax on royalty
payments". Hong Kong's says "0% (no withholding tax on dividends)". Neither
leaves the reader inferring an absence from a silence.

That is the cheap resolution for much of this queue. A guide that omits a head
is indistinguishable from a jurisdiction that does not charge it, and the
distinction cannot be recovered from the guide -- which is why 64 entries needed
a statute lookup each. A guide that writes the zero down converts itself from a
question into an answer, and the next reader spends no time on it at all. Where
a jurisdiction genuinely charges nothing on services or rent, saying so is worth
as much as a rate.

THE REMITTANCE RETURN IS THE COMPLETENESS SOURCE

Zimbabwe produced the best answer yet to "how do you find out what a statute
charges when the summary page only carries three heads". PwC has no Zimbabwe
withholding page at all -- it 404s. ZIMRA's rate schedule was not readily
retrievable either. But ZIMRA publishes REV 5, the return a payer files to REMIT
withholding taxes, and a remittance return has to enumerate every head, because
each one needs a line for the payer to write a figure on.

REV 5 lists fourteen: resident shareholders' tax, non-resident shareholders'
tax, resident tax on interest, non-residents' tax on fees, on remittances and on
royalties, tax on non-executive directors' fees, the automated financial
transaction tax, tax on the exercise of share options granted before 1 February
2009, capital gains withholding tax on immovable property and on marketable
securities as two separate heads, withholding tax on tenders, value added
withholding tax, and the tobacco levy.

The guide carried five. Nothing about the form gives a rate, and that is fine:
the form answers the question this script asks, which is what heads exist. Rates
can then be chased one at a time, and the ones that cannot be settled get said
so -- Zimbabwe's tender and no-tax-clearance withholding is stated as a live
conflict between a 30% and a 10% source, with the instruction to withhold the
higher where no ITF263 is produced, because an under-deduction is the payer's.

So the order of search for a queue entry is: the authority's remittance or
declaration form first, its rate schedule second, a summary page third. The
form is the only one of the three that is structurally obliged to be complete.

THE QUEUE OVER-REPORTED BY 30%, AND NOW SPLITS ITSELF

After ten jurisdictions had been worked off the list by hand it was worth
asking how many of the rest were real. This script indexes the heads named in a
bullet's LABEL, because labels are where the corpus states facts and bodies are
prose. That is the right primary signal and it has a predictable blind spot: a
guide that names five heads inside one bullet's body reads here as naming none
of them.

Measured, 15 of the 50 classic-only entries name an extra head in a body. Some
are real coverage the label does not advertise; some are a word like "insurance"
appearing in a sentence about something else; and a few are this branch's own
work, where a fix was written as one headline bullet rather than one bullet per
head. All three cases share the useful property that they are cheaper to triage
by eye than to research from a statute.

So the output now splits. `queue` is the 35 that name nothing beyond the classic
three anywhere -- those need the statute. `triage` is the 15 whose bodies mention
a service, rent, insurance or similar head -- read those first, and most will
either already be covered or need only restructuring so the head sits in a label
where it can be found. The exit code follows `queue`, not the total, so a run
that leaves only triage entries is a clean run.

The lesson is narrower than it looks and worth keeping: a checker's blind spot
is measurable, and measuring it before working its output is cheaper than
working the output. Thirty per cent of this queue was the tool, not the corpus.

ELEVEN OF THE QUEUE WITHHELD NOTHING AT ALL

The second measured blind spot, found the same way as the first. A jurisdiction
that levies no withholding tax names no service, rent or insurance head because
there is nothing to name, so it is indistinguishable here from a guide that
forgot them. Eleven were sitting on the queue for that reason: the British
Virgin Islands, Cayman, Bermuda, the Bahamas, Vanuatu, Bahrain, Monaco, Macau,
Curacao, the Isle of Man and Liechtenstein.

All eleven already state their zeros plainly -- "0% (no withholding tax on
dividends)", "None" -- which is exactly the habit recommended above, and it is
what makes them mechanically separable. `is_zero` reads the rate out of the
value: if every rate a jurisdiction states is zero, or the value says none or
nil, the guide is complete rather than thin and it is reported as `zero-wht`
instead of queued.

That is 11 removed on top of the 15 the body-mention split removed. Between
them the queue has gone from 64 to 24 without a single statute being opened,
because both were the tool describing itself rather than the corpus. It is
worth stating the ratio plainly: of the 64 entries this script originally
produced, roughly 40% were artefacts of how it measures. A checker that has not
been measured against its own blind spots is reporting its shape as much as the
corpus's.

A CAVEAT ABOUT THE THIN END

Jurisdiction keys come from the third path segment, so `us`, `im`, `in` and `nc`
are Isle of Man, the United States, Indiana and North Carolina, and the
single-head rows are mostly guides shaped differently rather than jurisdictions
withholding on one thing. Read the classic-only list, which is the real queue;
treat the 1- and 2-head rows as a note about guide structure.

Usage: python3 scripts/list-withholding-scope.py [--selftest] [--classic-only]
       python3 scripts/list-withholding-scope.py --show <jurisdiction>

Run --show before editing a jurisdiction. It prints every withholding-labelled
line the jurisdiction has, with file and line number, so a claim about what a
guide omits can be checked against the guide rather than against this script's
summary. Three wrong claims on this branch came from skipping that step.
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
ROW = re.compile(r'^\s*\|\s*([^|]{4,90}?)\s*\|\s*([^|]+?)\s*\|')
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
    """
    rates = PCT.findall(value)
    if rates:
        return all(float(r) == 0 for r in rates)
    return bool(NIL.search(value))

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


def body_heads_in(line):
    """Heads named in a withholding line's BODY rather than its label.

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
             if name not in CLASSIC and re.search(pat, value, re.I)}
    return found or None


def scan(root='skills'):
    """Return {jurisdiction: (label_heads, body_only_extras, all_rates_zero)}."""
    labels = collections.defaultdict(set)
    bodies = collections.defaultdict(set)
    nonzero = collections.defaultdict(bool)
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
