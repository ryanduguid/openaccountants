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
10% on unlisted, Hong Kong 4.95% on royalties to unassociated non-residents,
Peru 4.99% on accredited unrelated-party loans against 30% generally, Mongolia
5% on interest from bonds issued by Mongolian commercial banks against 20%,
Rwanda 5% on listed securities against 15%, Bosnia 5% in FBiH and 10% in RS
because withholding there is set by entity and not federally.

That is all ten disagreeing rows triaged, and none of them was a wrong rate.
The column has now earned the reading the paragraph above gives it: on this
field a disagreement is the corpus carrying a real distinction, not a defect.

But it is still worth chasing, because of what Bosnia turned up. The row
disagreed because ba-corporate-income-tax.md splits the dividend rate three
ways by entity, correctly and with both PwC and the Eurofast tax card behind
it. The defect was in a file this script cannot see disagreeing with anything:
bosnia-tax-optimization.md said "0% dividends" four times, unqualified, and
built its Company Extraction section on it. The 0% is right for a resident
individual -- dividends are exempt personal income in all three entities --
and wrong for the foreign owner that section is written for, who is withheld
5% or 10%. A guide that states one side of a distinction is invisible here;
only the guide that states both shows up. So the row points at the guide that
got it right, and the one to open is its neighbour that stayed silent.

Its own consistency rule had the same hole. The guide's header and its
Prohibition 4 both listed the three files it must agree with, and neither
listed the corporate income tax guide -- the one file carrying the rates its
extraction maths depends on. Both lists now include it.

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

  * Monaco    CORRECT on all three, hedges resolved. Monaco levies no
              withholding tax on outbound dividends, interest or royalties.
              Worth stating the limit as well, which the guide did not: a zero
              rate in Monaco is not a zero rate on the payment, because income
              arriving from abroad is still withheld at source.
  * Fiji      GENUINELY UNRESOLVED, and now says so precisely. The guide read
              "position uncertain: some sources cite 0% (dividend WHT removed
              effective 1 August 2017), others cite 15%". Checked, and the
              conflict is real: dividends were exempted from 1 August 2017 and
              the Income Tax Act still carries a 15% non-resident dividend
              withholding tax, with neither source retracting the other. The
              guide now defaults to withholding 15% and says to ask FRCS before
              paying gross, because an under-deduction is the payer's liability
              while an over-deduction is the recipient's to reclaim.

Fiji is the shape to copy when a field cannot be settled. "Position uncertain"
tells a reader nothing they can act on; naming both sources, both dates and
which way to err tells them what to do this afternoon.

  * Trinidad and Tobago  WRONG on two of three, and the guide had the dividend
              rates transposed onto interest. It read dividends at a flat 10%
              and interest at "10% to non-resident individuals; 8% to
              non-resident companies". The Board of Inland Revenue's own guide
              gives distributions at 3% to a non-resident parent company and 8%
              to any other non-resident, and puts interest with royalties and
              other payments at 15% for individuals and companies alike. So
              interest was understated by 5 to 7 points and the payer carries
              that.
  * Turkey    A CORRECTION THAT MADE THE GUIDE WORSE, now reversed. The entry
              that stood here said the guide was "CORRECT at 10% on interest to
              non-residents, and now says what decides it: 10% where the loan
              runs more than two years, 15% otherwise". The 10% is right. The
              rest was read off the wrong column. That two-year split is a
              footnote in PwC's TREATY table, hanging off Austria, Luxembourg,
              Portugal and Korea; it is not domestic law, and a payer applying
              15% to a lender outside those four treaties over-deducts by five
              points. The same entry then wrote that "treaty rates are mostly
              equal to or above the domestic rate, so a treaty rarely helps
              here", which inverts the very rule it had just quoted. What main
              had said was "10% ... (varies by instrument; treaty rates may
              reduce) (approx -- confirm)": vague, hedged and right. The guide
              now states the 10%, says the two-year split is a treaty rule,
              warns that Turkish rates live in Presidential Decrees and change
              often, and carries the 0% for licensed non-resident banks under
              Decree 2009/14593 art. 1/5-a as a rate to confirm per lender
              rather than to assume.
  * Andorra   CORRECT, hedge resolved. Royalties to non-residents are withheld
              at 5% under Llei 94/2010, and dividends and interest at 0%. The
              hedge said "confirm treaty rates", which is not something a guide
              can settle once for every counterparty. What was missing is the
              frame: 5% is a REDUCED rate against a general IRNR rate of 10%,
              so a payment that is not a royalty does not get it. Andorra's
              treaty network is small enough that the guide now says to check
              whether a treaty exists rather than to assume one does.

Trinidad is the case for going to the authority rather than to a chart. A first
search returned 15% for interest, which is right, and 15% for royalties, which
is also right, from a page summarising both. PwC's table renders the corporate
distribution rate as "3/8%", which extraction turns into something that reads
like three-eighths of one per cent and is really "3% or 8%". Neither reading
settles anything. The IRD's own withholding guide settles all three in one
page.

  * Belize    WRONG on two of three, understated by ten points each. The guide
              gave 15% for all three and hedged interest and royalties with
              "sources vary 15%/25%, confirm". Interest and royalties to
              non-residents are 25%, as are fees for services such as
              consultancy; only dividends are 15%. Grandfathered international
              business companies are exempt from withholding on payments to
              non-residents.
  * Zimbabwe  CORRECT on the rate, and the line around it was thin. The 15%
              non-residents' tax on interest was reintroduced with effect from
              1 January 2026 by the 2026 national budget, so the payment date
              still decides it. What the entry had added and could not support
              was "payable in US dollars"; no source found for it, so it is
              gone. What no source had been read for, and matters more, is in:
              withhold and remit the return within 30 days of payment, a payer
              who fails to withhold is personally liable for the tax plus a
              further 15% of it, and two exemptions -- interest payable by
              licensed investors on their special economic zone business, and
              interest payable by the Infrastructure Development Bank of
              Zimbabwe to non-resident institutional shareholders.
  * Romania   CORRECT at 16% from 1 January 2026 under Law 141/2025 (Official
              Gazette 699/2025), and missing the rule that decides most of the
              answers being asked in 2026. Interim dividends distributed during
              2025 out of the 31 March, 30 June or 30 September 2025 interim
              statements stay at 10%, including on regularisation in 2026; a
              distribution out of the 31 December 2025 annual statements is
              16%, because those statements cannot be approved until after
              1 January. So the question to ask is which financial statements
              the distribution sits on, not which year it is paid in. The line
              also cited a KPMG note from February 2025 for a law published in
              July 2025, which cannot support it; the citation now names the
              Gazette.

  * Argentina  RIGHT MECHANISM, WRONG BANDS. Dividends at 7% are correct and
              the 35%-on-a-presumed-margin machinery is correctly described.
              The hedged royalty line then said "~31.5% software, ~28%
              trademark/technical assistance, reducible to ~21% in certain
              cases". PwC's 28% band is "cessation of rights or licences for
              invention patents exploitation and technical assistance
              obtainable in Argentina" -- patents, not trademarks; PwC does not
              enumerate trademarks at all. The 21% is not a reduction anyone
              applies for, it is the rate for technical assistance, technology
              and engineering NOT obtainable in Argentina under a registered
              agreement, and registration is the condition the line never
              mentioned. The enumerated scale was missing entirely: copyright
              12.25%, motion picture, video and sound 17.5%, real estate rental
              21%, other Argentine-source income 31.5%, unregistered agreements
              31.5% or 35%. Software was asserted at 31.5% with no reasoning;
              31.5% is the residual, and a copyright characterisation would put
              it at 12.25%, a nineteen-point spread the guide closed by fiat.
              The interest line was the larger exposure: it gave "commonly
              15.05% (or 35% in some cases)" without either condition. 15.05%
              needs a local bank debtor, or a foreign creditor that is a
              supervised financial institution in a non-low-tax country with
              information exchange and no bank secrecy -- cumulative. Everyone
              else is at 35%. Assuming the exception under-deducts by twenty
              points.
  * Malawi    THE SPLIT WAS BACKWARDS. The line read "20% (non-resident);
              resident royalties also subject to WHT (approx -- confirm
              resident vs non-resident split)". It is 20% for RESIDENTS, as an
              advance tax, and 15% for non-residents, as a final tax under the
              general rule that Malawi-source income paid to a non-resident
              bears a final 15% of the gross. Same inversion on interest, where
              the guide's hedge "commonly cited around 20% on bank interest"
              had the right figure attached to the wrong payee. The structure
              explains itself once stated: the resident rate is higher because
              it is an advance against a later assessment, while the
              non-resident rate is the whole tax. MRA's own Fourteenth Schedule
              page would not render on either attempt, so this rests on
              secondary sources and says so in the guide.
  * Seychelles CORRECT on all three, hedges replaced rather than deleted. 15%
              on dividends, on interest from a non-banking company and on
              royalties for rights used in Seychelles. SRC's page was
              unreachable twice, so the guide now states the rates and records
              that they rest on secondary reporting -- which is more useful
              than the bare "(approx -- confirm)" it replaced, and more honest
              than deleting the hedge.

Seychelles also produced the mistake worth writing down. Working from the three
lines this script prints, I drafted a bullet saying the guide "lists only the
classic three" and omits service fees and the BAS remittance mechanism. Both
were already in the file, three and five bullets further down, one still hedged.
The rule above -- read the guide, and read what it cites, before you change a
number -- has a sibling: read the whole guide before you claim it omits
something. This script prints lines, not files, and a line is not a guide.

Zimbabwe and Romania are the same shape as Bosnia from the other direction. In
Bosnia a guide stated one side of a split. Here each stated a correct headline
rate and stopped before the transitional rule, the exemption and the penalty,
which are the parts that change what a reader does this week. A rate is the
cheapest thing on the line to get right and the least of what the line owes.

Still open: 124 jurisdictions state a rate, 25 hedge at least one of their own,
and 17 have been checked. Six were wrong outright and every one of the six had
hedged itself, which is the argument for working this column by its own doubts
rather than by a random draw. Five more were right at the headline and
incomplete underneath, which no hedge flags at all.

Two of the six wrong ones -- Trinidad and Malawi -- were wrong the same way: a
correct pair of rates with the resident and non-resident labels swapped. That is
worth looking for directly. It survives every check the repo has, because both
numbers are real, both appear in the authority's own table, and nothing in the
line contradicts anything else in the corpus. Only reading the source settles it.

THE FOURTH COLUMN THIS SCRIPT CANNOT SEE

KIND below covers dividends, interest and royalties. Withholding on SERVICE and
TECHNICAL FEES is a fourth head that most jurisdictions levy separately, and no
checker in this repo touches it. Five were read on the first pass, chosen
because their own hedges mentioned residency, and three were wrong:

  * Greece    WRONG, and backwards. The line read "20% ... paid to certain
              non-residents / domestic recipients". Those are the two groups
              that are EXEMPT. A Greek tax-resident legal entity is not subject
              to it, and neither is a non-resident with no Greek PE. It catches
              a NON-EU entity with a PE in Greece; an EU entity receiving the
              same fees through a Greek PE is exempt. So the ordinary case, a
              Greek company paying an EU consultancy with no Greek presence,
              bears no Greek withholding at all and the guide would have had
              20% deducted from the whole invoice.
  * Croatia   WRONG list against the wrong rate. Market research, tax
              consulting, business consulting and audit services are the 25%
              categories, and only for a payee in an EU non-cooperative
              jurisdiction with no treaty. The general 15% is IP-right fees and
              interest. The guide had the four advisory categories at 15%,
              which over-withholds on an ordinary adviser and under-withholds
              by ten points on a blacklisted one.
  * Qatar     WRONG TEST. The line said "services performed wholly or partly in
              Qatar". The rule is where the service is USED: 5% on all services
              used, utilised or benefited in Qatar even if carried out wholly
              outside it. A foreign adviser working entirely abroad on a Qatari
              matter is inside the charge and the guide put them outside it.
              Also added: the 5% applies only where the non-resident has no
              Qatari PE, remittance is by the 16th of the following month, and
              the Trusted Entity regime from 16 March 2026 gives treaty relief
              at source instead of pay-and-reclaim.
  * Malaysia  CORRECT at 10%, and missing a limb. Section 4A also covers rental
              of movable property, and the scope question the hedge asked is
              answered by the territorial test: services performed in Malaysia.
  * Estonia   CORRECT at 10% for services provided in Estonia, and missing the
              22% that applies where the recipient is a tax-haven entity. Its
              royalty definition also reaches payments for the use of
              industrial, commercial or scientific equipment, so an equipment
              rental is a royalty there rather than an untaxed service fee.

Three of five wrong is the worst hit rate of any field checked so far, and it is
the field with no checker. The pattern is not bad rates but bad SCOPE: who is
caught, where the service must happen, which list the category belongs to. A
rate can be verified against a chart; a scope has to be read.

Two recall limits the PR #16 review found, both still open and worth knowing
before reading a zero in this output as an absence:

  * A table whose HEADING establishes the withholding context, with plain row
    labels like "Dividends", "Interest", "Royalties", is skipped entirely,
    because the label test runs per row. Nigeria's quick-look WHT table is the
    example, and every rate in it is discarded.
  * A line that gives one rate for all three payment types is recorded only
    under the first. The Bahamas states a single zero for dividends, interest
    and royalties and appears here as dividends alone.

Both need the reader, not the parser, so they are documented rather than
guessed at. A jurisdiction missing from this list has not been shown to be
silent.

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
