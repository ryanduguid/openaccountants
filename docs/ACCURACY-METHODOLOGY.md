# Accuracy methodology

How OpenAccountants skills are built, reviewed, and corrected — and, just as importantly, what "reviewed" does **not** mean.

## The problem we're solving

General-purpose LLMs hallucinate tax law: they invent rates, misremember thresholds, cite forms that don't exist, and apply last year's rules to this year. OpenAccountants skills replace the model's guesswork with content drafted from authoritative sources and, where possible, signed off by a licensed practitioner.

## Two quality tiers

See [QUALITY-TIERS.md](QUALITY-TIERS.md) for the full definitions. In short:

| Tier | Standard | Who |
|---|---|---|
| **Source-cited draft** (Tier 2) | Every rate, threshold, form, and deadline drafted from authoritative sources (tax-authority publications and primary legislation) | Drafted + cross-checked, awaiting a full accountant review |
| **Accountant-reviewed** (Tier 1) | A licensed practitioner has reviewed the skill, tested it against representative data, and put their name + credential on it | Named CPA / CA / EA / Steuerberater / local equivalent |

This historical fork contains both tiers. Its metadata records upstream review
status; this fork does not operate the hosted MCP service or commission fresh
accountant reviews. See [COVERAGE.md](COVERAGE.md) for the recorded split and
[README.md](../README.md) for the fork's maintenance status.

## Sources

Skills are drafted from, and cite, primary sources only:
- Tax-authority publications (IRS, HMRC, CRA, ATO, etc.)
- Primary legislation and statutory instruments
- Official forms and their instructions

Training-data recall and unsourced web results are **not** acceptable sources for a rate or threshold.

## Conservative by design

When the correct treatment is genuinely uncertain, skills are written to **assume the higher-tax / more-compliant position** and to flag the uncertainty rather than guess in the taxpayer's favour. Every skill surfaces **audit flash points** — the specific spots where a real practitioner should look before anything is filed.

## The correction feedback loop

Accuracy improves in the open. When a skill produces something wrong:
1. Anyone can open an issue or PR with the correct figure and a source, or email a correction (see [CORRECTION-FEEDBACK-LOOP-SPEC.md](CORRECTION-FEEDBACK-LOOP-SPEC.md)).
2. The fix is applied and the contributor gets public credit.
3. With a credentialed practitioner's full review and sign-off, the skill moves from source-cited draft to accountant-reviewed.

## What "reviewed" does NOT mean

- It is **not** tax advice and **not** a filed return — every output is a **working paper** for a human to check.
- A source-cited draft has **not** been reviewed by a credentialed practitioner.
- A review reflects the rules **as of the skill's stated date**; tax law changes — check the date.
- Coverage of a jurisdiction does not imply coverage of every edge case within it.

The product is designed around this honesty: the AI produces a working paper and routes you to a real accountant for sign-off via `request_accountant_review`.

## External verification status

The scripts in `scripts/` compare the corpus against itself: across the three
trees, across sibling guides in one jurisdiction, and against its own arithmetic.
Agreement between copies does not establish that a tax rule is correct. That
requires checking an external source for the relevant jurisdiction and period.
The results below record earlier branch work; they are not a fresh independent
verification of every guide.

The `check-*.py` review aids generally exit zero even when they report leads.
Read their output and distinguish confirmed defects from parser limitations,
different tax periods and different regimes. Guide validation and unit tests
check software and metadata; neither certifies the tax content. The
percentage-conflict checker previously skipped table rows and all Windows
paths, so its earlier results did not cover those inputs.

### Checked against an outside source

| Field | Coverage | Errors found | Notes |
|---|---|---|---|
| Standard VAT / GST rate | 157 of 157 jurisdictions stating one | 6 | Fiji, India, Kazakhstan, Zimbabwe, Malawi, Maldives |
| Headline corporate rate | ~135 jurisdictions | 3 | Lithuania, Cyprus, Portugal |
| Annual return filing deadline | 24 jurisdictions | 8 | Italy, Greece, Armenia, Cyprus, Finland, Australia, Norway, Brazil |
| VAT/GST registration threshold | 20 jurisdictions | 2 | Albania, France. Egypt was **not** an error — see "Three corrections that were the opposite of corrections" |
| Withholding rate on dividends, interest, royalties | 10 of the 118 stating one | 3 | Ethiopia, Trinidad and Tobago, Belize. Iceland was **not** an error — see "Three corrections that were the opposite of corrections" |
| Payroll and social contribution rates | Morocco, Egypt | 0 | — |
| Personal income tax bands and exemptions | Egypt | 0 | — |
| Micro-regime threshold and dividend WHT | Romania | 2 | Romania |
| Minimum wage feeding contribution bases | Albania | 1 | Albania |
| Social contribution ceilings | Slovakia | 1 | Slovakia |
| Alternative minimum tax status | Taiwan | 0 | Taiwan — reverted, see "Three corrections that were the opposite of corrections" |
| Penalty and interest on overdue tax | Cyprus | 0, one conflict recorded | — |
| Minimum corporate tax bands | Slovakia | 1 | Slovakia |
| Statutory citations | Pakistan, Ireland (partial) | 0, one unverified | — |
| Forthcoming rate steps | Ireland | 1 gap filled | Ireland |
| Capital allowances | Australia | 1 | Australia |
| Personal allowances and bands | Liechtenstein | 0 | — |
| Social insurance rates | Liechtenstein | 3 | Liechtenstein |
| Self-employed contribution caps | Russia | 0 | — |
| Penalty rates | Russia | 0 | — |
| Medicare levy surcharge thresholds | Australia | 1 | Australia |
| Late payment interest | UK | 0, restated | — |
| High-income surcharge | Pakistan | 0, self-contradiction fixed | — |
| Loss carryforward caps | Dominican Republic | 0 | — |
| Indexation units (MCI, minimum wage) | Kazakhstan | 1 | Kazakhstan |
| Indexation units (UIT, IAS) | Peru, Portugal | 2 | Peru, Portugal |

The table does not establish a complete external review of payroll rates and
thresholds, registration and filing thresholds, filing deadlines, penalties,
interest, social-contribution bands, capital allowances, withholding rates,
form names or statutory citations. Earlier individual corrections do not
establish that every guide covering those topics has been checked.

To put a number on it: the deadline pass has covered 24 of the 201 jurisdictions that state a deadline,
and the fields just listed move on the same annual cycle as the ones in the
table above.

The threshold column is the newest and has the same split as the deadline one.
Reading it for odd rows found Egypt and Albania; a random draw of ten found only
Albania. Both errors were a guide stating a figure the jurisdiction had already
changed, and in both a sibling guide in the same pack had it right.

Looking at what a column does not contain became the most productive lead of
all, and it works on any field. In the deadline column it found Brazil, whose
guide leads with a flat "30 de maio" while its own citation says the date is
set annually, and South Africa, whose guide names the ITR12 and never says when
it is due. The South African case is the one to remember: a missing figure
passes every check ever written here, because nothing contradicts it.

So all 30 jurisdictions absent from the deadline column were read. Exactly one
was genuinely silent, and that was South Africa. Vanuatu is silent on purpose,
since individuals there file no annual return. The other 28 state a deadline
the script cannot represent, and almost always because the deadline is not a
single date: Ecuador staggers it by the ninth digit of the RUC, Colombia by the
NIT, Uruguay by the RUT, and Hong Kong counts a month from the day the return
is issued. Treat an absence as a question rather than a gap. Asking it found
Brazil, France and South Africa; answering it thirty times found one hole.

France came from looking at what the column does not contain. Only eight EU
states appear in it, so the obvious question was whether the rest have no
threshold or no wording the script recognises. Germany, the Netherlands and
France all state one under their own name for it, and France's was four years
out of date in fourteen places. A coverage number counts the phrasing a script
knows, and the gap between that and the field is where this error was sitting.

### The first payroll figures checked outside the repo

Morocco, chosen because the hedge queue is dominated by contribution rates and
Morocco sits near the top of it. Every figure checked was right.

CNSS totals of 21.09% employer and 6.74% employee match the 2026 rate table, as
do the MAD 6,000 monthly ceiling on the two prestations sociales branches, AMO
at 4.11% employer and 2.26% employee, family allowances at 6.40% and the
vocational training tax at 1.60%, both uncapped. The auto-entrepreneur regime
checks out too: MAD 500,000 for commercial, industrial and artisanal activity,
MAD 200,000 for services, 0.5% and 1% of collected turnover, and the rule that
service income above MAD 80,000 from a single client is withheld at 30% instead.

One thing the check could not settle, recorded rather than smoothed over. The
guide puts the employee capped branches at 4.48%, and the published component
breakdown gives 0.33% plus 3.96%, which is 4.29%. The published components do
not sum to the published employee total either, 6.55% against 6.74%. The same
0.19% is missing from both, so the guide agrees with the total and disagrees
with the parts. Its hedge on the component split stays.

Egypt came next, for the same reason and with the same result. The annual
personal exemption of EGP 20,000, raised from EGP 15,000 on 21 February 2024,
matches the ETA schedule, and so does the whole seven-band scale: 0% to 40,000,
then 10, 15, 20, 22.5 and 25%, with 27.5% above EGP 1,200,000. The bands and
the rates both check out, which is worth stating separately, because a rate
schedule can be right in its rates and wrong in its boundaries.

Egypt's VAT threshold hedges also close, and this is the kind that expires on
its own. The guide said "lowered to EGP 250,000 effective 1 Jan 2026 — verify
current value". That date has passed, the change is in force, and a hedge
written before a commencement date should be revisited after it rather than
carried forward. Its prohibition now reads "do NOT state the threshold as
EGP 500,000" rather than "do not present either figure as settled".

### One stale unit moves everything denominated in it

Searching for the Kazakh shape across the corpus found it in three more places.
A guide that converts an indexation unit to currency and stores the result is
correct on the day and wrong the following January, and 36 lines in six
jurisdictions do that conversion.

  * Peru. The UIT is S/ 5,500 for 2026, up from S/ 5,350, under Supreme Decree
    301-2025-EF. peru-income-tax knew both values and still expressed all five
    income tax bands at the 2025 rate, so the 45-UIT top band read S/ 240,750
    where it is S/ 247,500.
  * Portugal. The IAS is EUR 537.13 for 2026, up from EUR 522.50.
    portugal-tax-optimization labelled the old value as the new one, reading
    "IAS 2026 = EUR 522,50", and pt-social-contributions expressed the 4-IAS
    exemption as EUR 2,090 where it is EUR 2,148.52.
  * Kazakhstan. A second guide, kz-income-tax, had banked the standard personal
    deduction as 14 MCI = KZT 55,048 at the 2025 index. It is KZT 60,550.

Every one of those guides names the unit correctly. What ages is the currency
figure beside it, and the arithmetic that produced it was right. Where a
jurisdiction indexes, keep the unit and recompute; that instruction is now in
each of the lines.

The last two of the six were Bolivia and Uruguay, and both turned out larger
than a line.

  * Bolivia. The SMN rose from Bs 2,750 to Bs 3,300 on 1 January 2026, twenty
    per cent, the largest rise in a decade. Every RC-IVA threshold is an SMN
    multiple: the 2-SMN non-taxable minimum, the presumed VAT credit at 13% of
    1 SMN, the 60-SMN pension ceiling. bolivia-payroll carried both years
    correctly and told the reader never to mix them. bolivia-income-tax, which
    is the guide an agent loads to compute the tax, had only 2025 in its key
    thresholds table and in its conservative defaults.
  * Uruguay. The BPC rose from UYU 6,576 to UYU 6,864, 4.38%, on 1 January 2026.
    Nearly every Uruguayan threshold is a BPC multiple: the whole IRPF Category
    II scale, the non-taxable minimum, the FONASA band split, the deduction
    credit threshold, the child deductions. uy-tax-overview named both values.
    uruguay-payroll, uruguay-social-contributions and uruguay-income-tax — the
    three that actually compute anything — banked every peso figure at 6,576.

That is the reference-guide-current, working-guide-stale split again, for the
ninth time on this branch, and it is worth stating as a rule: when an
indexation unit moves, check the guides that *use* it before the guide that
*defines* it.

One figure in the Uruguayan set is not a BPC multiple and cannot be derived.
The BPS retirement contribution ceiling went from UYU 272,564 to UYU 288,836,
a rise of 5.97% against the BPC's 4.38%, because BPS sets it separately. A
sweep that recomputes everything from the new unit would have got that one
wrong in the confident direction. The guides now say which figures are
multiples and which have to be read off the BPS table.



Kazakhstan states many of its thresholds in MCI, the monthly calculation index,
which the budget law resets each year. It went from KZT 3,932 for 2025 to
KZT 4,325 for 2026, about 10%. Three of the four guides carrying it already had
4,325 and hedged it; kz-company-formation had converted 100 MCI to tenge at the
2025 rate and stored the tenge figure, so its minimum charter capital read
KZT 393,200 where it is now KZT 432,500.

That is the shape to watch in any jurisdiction with an indexation unit. The
guide that keeps the unit stays right for free and the guide that converts once
goes stale silently, because the arithmetic it did was correct on the day. The
line now says to recompute from MCI rather than carry the tenge forward.

The minimum wage in the same law did not move, staying at KZT 85,000 for both
years, which is worth stating beside the MCI so a reader does not assume
everything indexes together.

### Four corrections that were the opposite of corrections

A code review on the pull request read the diff against outside sources and
found that three of the changes on this branch had made a correct guide wrong.
All three failed the same way, and it is the way this document already warns
about: I took a secondary source over the authority, on a field where the
authority is one page away. A fourth turned up later, from the other direction:
the right source, read off the wrong column.

**Egypt.** The guide said the VAT registration threshold is EGP 500,000 and
hedged it. Advisory write-ups say in chorus that "Resolution No. 281 of 2025
halved the threshold from EGP 500,000 to EGP 250,000", so I changed it, removed
the hedge, and added a prohibition reading "Do NOT state the VAT threshold as
EGP 500,000." ETA's own VAT page says: the mandatory registration threshold is
500 thousand pounds. Decision No. 281 is the second sub-phase of the eighth main
phase of the **e-receipt** rollout, obliging the taxpayers on its attached list
to issue B2C electronic receipts from 15 September 2025. The EGP 250,000 in
those write-ups is an e-invoicing enrolment criterion that has been repeated
until it reads like a VAT threshold. So the guide was right, I overwrote it, and
the prohibition I wrote pointed the reader away from the correct figure.

**Iceland.** The guide gave 12% on interest to non-residents and noted that PwC
publishes 13%. I resolved that by deducting at 13%, on this document's own rule
of taking the higher-tax position where a rate is unsettled. Skatturinn states:
"interest income tax rate is 12% except for 2024, then it is 13%." The rate was
never unsettled. It was dated, PwC's page had not caught up, and the
higher-tax rule is for genuine disputes rather than for a stale secondary source.
Applying a conservative default to a question that has an answer is not caution.

**Taiwan.** The guide called the 15% enterprise Income Basic Tax rate for large
MNE groups "proposed". I changed it to "in force since 1 January 2025 — not a
proposal". PwC, which the guide cites, says "currently there are draft
proposals"; Taiwan's Ministry of Finance calls it a draft amendment. The
complication is real — the Executive Yuan can set the IBT rate within statutory
limits without a Legislative Yuan amendment, so "announced and effective" and
"still a draft" can both be said honestly — but that is an argument for the
Fiji treatment, naming both positions and which way to err, not for asserting
one of them.

**Turkey.** This one the review did not catch, and it is the worst of the four.
The guide on main read: 10% on interest paid to non-residents under domestic law
*(varies by instrument; treaty rates may reduce)*, hedged *(approx — rate varies
by interest type; confirm)*. Vague, and right. I replaced it with a confident
specific — "the instrument decides it: 10% where the loan or debt claim runs
more than two years, **15%** otherwise" — and added that "treaty rates are
mostly equal to or above the domestic rate, so a treaty rarely reduces this
one". The two-year split is real, and it is a footnote in PwC's **treaty**
table, hanging off Austria, Luxembourg, Portugal and Korea. It is not domestic
law. So the sentence asserted a treaty rule as domestic law and then, in its
next clause, told the reader treaties do not matter here. A Turkish payer
following it would deduct 15% from a lender under any of the other treaties and
over-deduct by five points.

The mechanism is different from the first three and worth separating. Egypt,
Iceland and Taiwan came from preferring a chorus of secondary sources to the
authority. Turkey came from the right source — the page the guide itself cites —
read off the wrong column. A rate table with a treaty matrix beside it will hand
you a number that is accurate about something you did not ask. So checking that
the source is authoritative is not the whole check; you also have to establish
which question the number answers. And the damage was larger here than in the
other three, because the line I overwrote was already correctly hedged: I traded
a true vague statement for a false precise one, which is the only trade in this
work that is strictly negative.

The pattern across all four: each began as a hedged line, and a hedged line is
where this branch has found most of its real errors. That made me quick to
resolve one, and resolving a hedge in the wrong direction is worse than leaving
it, because the hedge told the reader to check and the resolution tells them not
to. The rule that would have caught all four is already in `scripts/
list-withholding-rates.py`: read the guide, and read what it cites, before you
change a number. I wrote that after nearly breaking Barbados. Then I broke
Egypt.

Worth recording the mechanism as well as the lesson. The first three survived my
own verification because I checked them the way I had found errors — search, read
the consensus of secondary sources, act — rather than the way the corpus is
supposed to be checked, which is to open the authority's page. Consensus among
advisory write-ups is not corroboration; they copy each other. Turkey survived
because opening the authority's page felt like the whole job, and it is only
half: a source can be the right one and still be answering a different question
than the one in front of you.

There is a defensive habit in all of this that costs nothing. Before changing a
hedged line, read what the line says on `main`. If the version you are replacing
is vaguer than yours but not wrong, you are not correcting it — you are betting
that your new precision is right, against a line that could not be wrong because
it did not commit. That bet has now lost once out of four.

### Three ways the Bolivia and Uruguay pass nearly went wrong

Restating a whole bracket table from an outside source is a bigger move than
correcting one number, and this pass produced three near-misses worth keeping.

**An outside source published a different scale, and it was the source that was
wrong.** A Uruguayan advisory site gives a 2026 IRPF Category II scale with nine
bands and new rates of 20% and 22% at boundaries of 24, 36, 54 and 80 BPC,
against the eight bands and 0/10/15/24/25/27/31/36 the corpus carries. Three
things settled it. The Ley de Presupuesto Nacional 2025-2029 (Ley 20.446)
changed IRPF for foreign-source income, the tax-holiday election and FONASA
credit offset, and four law firms writing it up mention no change to the labour
scale. A DGI-sourced 2026 table carries the eight bands. And the advisory
table does not reconcile to itself: it labels a band top of 80 BPC and prints
553,920, where 80 BPC at the 2026 BPC is 549,120. That last check cost nothing
and would have caught it alone. The corpus was right and the guide now carries
a note naming the wrong scale, because the next person to search will find the
same page.

**The right number from a decree that no longer exists.**
bolivia-social-contributions credited the 2026 SMN of Bs 3,300 to DS 5503, and
Bs 3,300 is correct. DS 5503, of 17 December 2025, was abrogated after union
mobilisation and replaced by DS 5516, published in the Gaceta Oficial on
13 January 2026, which set the same figure. The file cited DS 5516 correctly one
row below its own DS 5503 citation. A checker comparing numbers between sibling
guides sees nothing here, because the numbers agree; what disagrees is the
authority, and defects keep clustering in the nouns rather than the digits.

**A rate where two siblings outvoted the third, and the third's own citation
agreed with them.** uruguay-income-tax put the IRPF deduction credit at 10% for
income below the 15 BPC threshold, while uruguay-payroll and
uruguay-social-contributions both said 14% and cited the BPS comunicado.
Outside sources give 14% and 8%. The source uruguay-income-tax named as
corroboration says "8% o 14%" on its own page. So the citation was checkable
against itself, and a 10% rate understates the credit by four points of the
deduction sum, which overstates the tax. Reading what a guide cites is the
cheapest check available and it keeps paying.

### The same Act, two commencement dates, and a guide that read one

Working the expired-rule queue into the UK pack turned up the sharpest instance
yet of a class this document has recorded twice before: an announcement is not a
law, and a law is not in force on the day it is announced.

The Finance Bill following the Autumn Budget of 26 November 2025 received Royal
Assent on 18 March 2026 as Finance Act 2026 (c. 11). It raises three sets of
rates by two percentage points, and it commences them on **two different dates**:

  * s.4  dividends -- ordinary 8.75% to 10.75%, upper 33.75% to 35.75%, from
         **6 April 2026**, so it bites on a 2026-27 return.
  * s.5  savings -- basic 22%, higher 42%, additional 47%, from **6 April 2027**.
  * s.7  property, as a new rate category of its own -- the same 22/42/47, also
         from **6 April 2027**.

`uk-income-tax-sa100` had the dividend half exactly right and read the savings
half a year early. Its Scottish worked example applied "expected 42%" to a
higher-rate taxpayer's bank interest in 2026-27, where the rate is still 40%,
and its legislation table carried both changes as "TBC pending Finance Bill
enactment" five months after Royal Assent. Its prohibitions told the reader not
to finalise a 2026-27 return before an enactment that had already happened.

Two details make this worth recording rather than just fixing.

The first is that the sibling guide had it right and said so loudly.
`uk-rental-sa105` states the 2027-28 commencement, restates the 2026-27 rates as
20/40/45, and warns in as many words that a Scottish taxpayer's 42% is a
residence rate on non-savings income and that "the coincidence of the number is
a trap". `uk-income-tax-sa100` then walked into precisely that trap, writing 42%
into a Scottish example. Nine times on this branch the reference guide has been
current while the working guide was stale; this is the first time one sibling
documented the exact error another sibling was making.

The second is what the placeholder cost. "TBC pending enactment" reads as
caution, and caution is normally free. Here it was not: while the guide waited
for an enactment that had happened, it also carried a provisional figure derived
from the announcement, and that figure applied a 2027-28 rate to a 2026-27
return and overstated the example by GBP 50. A hedge that carries a working
estimate is not a refusal to answer. It is an answer, with a disclaimer attached.

The Scottish half of the same example was simply out of date rather than wrong
in kind. The 2026-27 Scottish Budget widened the starter band 7.4% to GBP 16,537
and the basic band 7.4% to GBP 29,526 while freezing the higher, advanced and
top thresholds. On the example's GBP 50,000 that makes the Scottish tax GBP
8,982.05 rather than the GBP 9,013.80 the guide carried forward from 2025-26 --
lower, not higher, which is the direction a "working estimate" is least likely
to guess.

### Nigeria: two Acts, two thresholds, and the majority of sources wrong

The best find on this branch came from checking a number the corpus already
disagreed with itself about, and it is the seventh time an outside source
contradicted the corpus and the corpus turned out right — this time against
almost every outside source.

`ng-return-assembly` put the Nigeria Tax Act 2025 small-company threshold for 0%
companies income tax at turnover of ₦50M with fixed assets under ₦250M.
`ng-formation` put it at ₦100M, and built a worked example on it. A first search
returned ₦100M from six sources including two accounting firms, which made
`ng-return-assembly` look like the error.

It is not. The 2025 reform enacted two Acts that define overlapping terms
differently and has not reconciled them:

  * **NTA 2025 s.202** — "small company": turnover ≤ **₦50M** and fixed assets
    ≤ ₦250M, professional services excluded. This drives the 0% CIT rate at
    s.56(a), and the education-tax and development-levy exemptions.
  * **NTAA 2025 s.147** — "small business": turnover ≤ **₦100M**. This is a VAT
    and withholding test.

Between ₦50M and ₦100M the two labels come apart: a company can be a small
*business* for VAT and a medium *company* paying 20% CIT at the same time. Most
secondary coverage flattens both to "₦100 million", which is how six sources
agreed on the wrong answer for CIT. A Nigerian law firm and a Nigerian
publication both name the sections and the conflict.

What it cost. `ng-formation`'s worked example put a Lagos software developer on
₦60M turnover into the 0% band and concluded that incorporating "wins decisively"
against a business name. On the correct test she is a medium company: 20% CIT on
₦45M assessable profit is ₦9,000,000, against the guide's own indicative
₦9,280,000 of personal income tax as a sole trader. The recommendation was not
just mis-costed by ₦9M; the reason for it evaporated. The example now says the
tax case is roughly neutral and that the case for incorporating is structural,
and names ₦50M as where the 0% band actually bites.

Two smaller things in the same pack, both nouns rather than numbers. The Federal
Inland Revenue Service was renamed and re-established as the **Nigeria Revenue
Service** on 1 January 2026 under its own Act; two guides in the pack knew, and
five still named FIRS flatly as the tax authority. And four guides held figures
open pending implementing regulations "late 2025 / early 2026" that the Federal
Ministry of Finance published on 18 June 2026 — with the sting that "the
regulations are pending" had become a reason to fall back on a repealed statute
for a period the new one governs.

The rule this reinforces, for the seventh time: read the guide, and read what it
cites, before you change a number. A count of agreeing sources is not evidence
when they are all copying the same simplification.

### Morocco: the guide was right, and that was not the end of the job

Two Moroccan leads came out of the expired-rule queue and neither produced a
correction. Both produced an improvement, which is worth separating.

The e-invoicing decree under CGI art. 145-IX was still unpublished when
re-checked in September 2026 — the draft sits with the Secrétariat Général du
Gouvernement and nothing has reached the Bulletin Officiel. Law 42.25 on
crypto-assets is still an avant-projet, dated 5 August 2025 and made public that
November, not adopted; Bank Al-Maghrib's governor said in July 2026 only that
adoption was in progress, so the widely-reported "mid-2026 adoption" did not
happen. The guides said both positions were unsettled and they were right.

So the finding is not that anything was wrong. It is that "the decree is
pending" was doing less work than it looked like it was doing.

Search for Moroccan e-invoicing and you get a detailed calendar from a dozen
advisory sites and vendors: 1 January 2026 for large IS taxpayers, 1 July 2026
for medium enterprises, 1 January 2027 for PME/TPE, sometimes a MAD 200M
threshold for the first wave. None of it comes from a published DGI document.
One of the firms publishing a calendar says so on its own page. And the calendar
fails two internal checks: a mandate said to have started on 1 January 2026
cannot be squared with the Directeur Général des Impôts saying in April 2026
that launch was planned for later in the year, and the first date has now passed
with no decree, so anyone who followed it was told to comply with a rule that
does not exist.

An agent reading "the decree is pending" and then searching will find that
calendar and believe it, because it is specific, confident and repeated. The
guide now names the calendar, says where it does not come from, and says why it
does not hold together. That is the Fiji treatment applied to a pending rule
rather than to a conflicting rate: naming both positions and which way to err
beats recording that the position is uncertain.

Both files also now carry the date they were re-checked rather than the date
they were written. "As of April 2026" in a September file tells a reader the
position is five months old and nothing else. "Re-checked September 2026 and
unchanged" tells them somebody looked. It is the same sentence's worth of
characters and a different amount of information.

### Work the queue by who reads it, not by who hedges most

The hedge queue sorted by count puts Central African Republic first with 27 and
Australia nowhere. Sorted by pack size it puts Australia first with 37 guides
and 3 hedges. The second ordering found an error in the file whose whole job is
to be right.

`au-rates-2026-27` gave the Medicare levy surcharge base tier as $101,000
single and $202,000 family. Those are the 2025-26 figures; for 2026-27 they are
$105,000 and $210,000, with the family threshold rising $1,500 for each MLS
dependent child after the first. A guide named for a year, carrying the
previous year's numbers, is the worst version of this error, because the name
is the reason a reader trusts it.

Three hedges in the same five packs came back correct and were restated rather
than removed. Australia's private hospital excess of $750 single and $1,500
family has been unchanged since 1 April 2019. The UK's late payment interest is
Bank Rate plus 4 points, which happens to be the 7.75% the guide already showed,
though the guide dated it to 2024 and the number is right for a different
reason: it is 7.75% from 9 January 2026 on a Bank Rate of 3.75%. That line also
gained the part that changes an answer, that the margin was 2.5 points before
6 April 2025, so interest running across that date is charged at two margins.

### The file that disagrees is usually the file that is right

`list-withholding-rates.py` prints a `guides disagree` marker when two guides in
one jurisdiction state different rates for the same payment. Ten jurisdictions
carried the marker. All ten have now been read, and none of them was a wrong
rate. Every one was a real distinction the corpus was carrying properly: Peru's
4.99% on accredited unrelated-party loans against 30% generally, Mongolia's 5%
on bank bond interest against 20%, Rwanda's 5% on listed securities against 15%,
Bosnia's 5% in the Federation against 10% in Republika Srpska.

The useful part is what chasing Bosnia found anyway. `ba-corporate-income-tax.md`
splits the dividend rate three ways by entity — 5% FBiH, 10% RS, 0% Brcko — and
both PwC and the Eurofast tax card confirm it line for line. The defect was in
`bosnia-tax-optimization.md`, which disagreed with nothing because it stated only
one side. It said "0% dividends" four times, unqualified, and built its Company
Extraction section on it: *10% CIT on profit; 0% dividend tax on distribution → a
very efficient extraction*. The 0% is right — dividends are exempt personal
income in all three entities — for a **resident individual**. Section 4 is
written for the owner of a d.o.o. deciding how to take profit out, and a foreign
owner reading it would understate the cost of extraction by 5 points in the
Federation and 10 in Republika Srpska.

So the marker is not a defect report, and it is not noise either. It is a pointer
to a jurisdiction where a distinction exists, and the file to open is not the one
that flagged — it is the neighbour that never mentions the distinction at all. A
guide stating one side of a split is invisible to every consistency check the
repo has, because a check needs two claims to compare and a silent guide only
offers one. That is the same shape as the pattern that keeps recurring here: the
reference guide is current, and the guide an agent actually loads to do the work
is the one that is wrong.

The optimisation guide's own consistency rule had the hole in the same place. Its
header and its Prohibition 4 both named the three files it must agree with, and
neither named the corporate income tax guide — the single file carrying the rates
its extraction arithmetic depends on. A rule that lists which siblings to check
is worth reading as carefully as a rate, because a sibling missing from that list
is a contradiction the guide is licensed to make.

### A guide that borrows another country's rates says so

Liechtenstein's payroll guide gave AHV/IV as "approx 10.6% of gross salary,
split equally employer/employee", and its own note explained where that came
from: "figure follows Swiss model". It had no Liechtenstein source, so it used
Switzerland's and said so.

The real figures are 12.285% in total, split 7.385% employer against 4.900%
employee, so the split is not equal and the employer share was understated by
about two points. Its sources were an HR services blog rather than the
AHV-IV-FAK contribution table, which is the other half of the same problem.

The same pack's income tax figures, cited to PwC, are exactly right: bands at
CHF 21,140 and CHF 211,401, allowances of CHF 15,855, CHF 31,710 and CHF 23,783.
Five hedges resolved and three rates corrected, in one jurisdiction, from two
sources.

The lesson is in what the guide admitted. "Follows the Swiss model" is a
confession, and a corpus that writes those down can be searched for them. It is
a better lead than any disagreement, because it names both the doubt and its
cause.

### An announcement is not a law, in either direction

Two errors this session are the same mistake pointing opposite ways, and a
reader is misled by both.

Taiwan called its 15% alternative minimum tax for large multinational groups
"proposed" after it had been law for a year, and a reader does not apply a
proposed rate. Australia's bookkeeping guide did the reverse: it listed the
instant asset write-off as "Permanent (from 1 Jul 2026) — announced in 2026
Budget — made permanent". The 2026-27 Budget of 12 May 2026 did announce it,
the enabling legislation has not passed, and the standing legislated threshold
for assets first used from 1 July 2026 is $1,000. A small business told it can
immediately deduct a $15,000 asset would instead be pooling it at 15% and 30%.

Both guides had the fact and the date right. What they got wrong was the
status, and no rate check, arithmetic check or cross-tree comparison in
`scripts/` can see that, because there is no wrong number to find.

Australia is also the eighth instance of the pattern that runs through every
field here. `au-rates-2026-27` states it exactly right, as "legislated to
30 Jun 2026; permanence from 1 Jul 2026 announced, confirm enactment", and
`au-rd-incentive` and `australia-tax-optimization` bound their claims to
30 June 2026 too. The guide an agent loads to write up a set of books did not.

### A hedge attached to a future date expires on that date

Fourteen of the 900 hedged figures name a commencement date that has since
arrived. That is a small category and it was worth measuring rather than
assuming, but it produced three errors from the first four worked, because a
guide written before a change takes effect states the old figure first and
nothing brings it back afterwards.

Romania gave the micro-enterprise ceiling as "EUR 250,000 for 2025; lowered to
EUR 100,000 from 2026", dated correctly and led by the superseded half. Read in
2026 it is simply wrong, and the same guide put the non-resident dividend
withholding rate at "10% (2025)" where Law 141/2025 raised it to 16% for
dividends distributed from 1 January 2026. Albania's payroll guide gave the
minimum wage as "40,000 ALL (2025)" while its own income tax guide already
carried the 50,000 that took effect on 1 January 2026, which matters because
that figure is the floor for social contributions.

Slovakia and Taiwan then made it five of six. Slovakia's maximum monthly
employee social contribution was EUR 1,478.62, derived from the 2025 assessment
base of EUR 15,730 and labelled as derived. The 2026 base is EUR 16,764, so the
ceiling is EUR 1,575.82 and a figure carried over understates it by about
EUR 97 a month. Taiwan called the 15% alternative minimum tax rate for large
multinational groups "proposed"; it was announced in August 2024, took effect
on 1 January 2025 and first showed up in returns filed in 2026.

Taiwan is the variant worth watching for. Nothing there is a number: the rate
and the date were both right, and the word "proposed" was the error. A reader
told a rate is proposed does not apply it.

The lesson is about how these guides are written rather than about any of the
six. A figure labelled with its year is honest and ages badly, and every
"lowered to X from 2026" written in 2025 becomes a wrong headline in 2026
unless someone turns it around. Lead with the rule in force and keep the
superseded figure behind it.

All fourteen dated hedges have now been worked. Six were wrong: Romania twice,
Albania, Slovakia twice and Taiwan. Latvia, Cyprus, Russia, Seychelles and
Egypt's remaining lines were right, though Cyprus does not resolve and says so.
Six in fourteen is the densest seam this branch found, against four in ten for
hedges generally and zero in ten for a random draw.

### A refusal rule expires the same way a figure does

The Uruguayan pass turned up a variant that is worse than a stale number,
because it is an instruction and an agent will follow it. Both BPS guides
carried a conservative-defaults row reading, in substance, "pay period in 2026
or later: apply the FY2025 values and flag; do not invent 2026 figures", and
uruguay-payroll's prohibitions ended with "NEVER apply unconfirmed 2026 figures
— use FY2025 values until 2026 values are published".

Every word of that was right when it was written. The 2026 BPC was not yet
decreed, and telling an agent to hold the old value and say so is exactly the
conservative behaviour this corpus wants. The values were published on
20 January 2026. From that morning the rule stopped protecting anyone and
started causing the error it was written to prevent, and nothing in the file
knew.

A figure labelled with its year at least tells a reader it is dated. A refusal
rule reads as current policy however old it is, so it is the more dangerous of
the two. The rows now point forward — "pay period in 2027 or later: apply the
2026 constants and flag" — which will age in its turn, but ages into caution
rather than into a wrong answer.

The general form: any guidance conditioned on "until X is published" needs a
check that fires when X is published. That search is now
`scripts/check-expired-rules.py`, and writing it was more instructive than
running it.

The first pattern returned 286 hits, the second 63, the third 45. None of those
numbers was about the corpus. "TBC" is the Transfer Balance Cap through the
whole Australian pack. "As of May 2026" is Morocco dating a research position
honestly, which is the behaviour this repo wants rather than a defect. "Until
2035" is Bermuda's tax assurance and "until 2029" Albania's zero band, both
statements of law. Latvia's "do NOT use the 2026 figure for a 2025 computation"
is the *opposite* of the defect. Reading a whole line for a date let "ITAA 1997"
supply the year for unrelated text, so one rule was reported as waiting on 1997.

Tightening cost recall, and the docstring says where. Uruguay's conservative
default -- "apply FY2025 values and flag; do not invent 2026 figures" -- is a
real expired rule that the finished check does not catch, because every phrasing
that would catch it also catches Latvia. The file still surfaces on a different
line, which is the right way to read the output: a hit points at a file worth
reading, not at the only bad line in it.

Two things the check found immediately. Paraguay's minimum wage had moved on
1 July 2026 (Decreto 6225, +5% to PYG 3,044,000) under a guide still saying the
July-2026 adjustment was expected but unconfirmed, and the minimum wage is the
IPS contribution floor, so the rule understated contributions on every wage at
or near it. And the UK student loan guide's 2026-27 threshold column was still
five cells of "TBC -- HMRC publishes annually" five months into the 2026-27 tax
year, in a tier 1 guide whose recorded accountant review is dated 3 June 2026 --
two months after that year began. A human sign-off passed over it, which is the
argument for checking this by date rather than by reading.

Then it caught a fix of mine. Run against the UK guide immediately after that
guide was corrected, it found a second copy of the same threshold table two
hundred lines further down, still TBC in all five cells, plus a refusal code and
a three-year sensitivity test built on the same placeholder. The first fix had
been to the table a reader sees first. That is the ninth time on this branch
that a checker has been evidence about the checker, and the first time one has
been evidence about me.

### The best lead in the corpus is the corpus's own doubt

Ten withholding rates were checked against outside sources and four were wrong.
Every one of the four sat on a line where the guide had already written
"approx — confirm" or "sources vary". Belize said "sources vary 15%/25%" and
they vary because interest and royalties are 25%. Trinidad and Tobago hedged
its interest rate and had the dividend rates transposed onto it. Iceland led
with 12% while its own hedge said PwC cites 13%. Ethiopia hedged the royalty
split as residency when the split is by kind of royalty.

A guide that doubts itself beats two guides that disagree, because someone has
already done the work of noticing, and until now nothing acted on it.
`scripts/list-hedged-claims.py` turns that into a queue. The corpus carries
about 3,500 self-hedged lines; 907 of them attach a figure to a labelled fact,
across 180 jurisdictions, and those are the ones a reader will act on.

Volume there is not severity. Central African Republic tops the list because
its pack was drafted from thin sources and says so on nearly every line, which
is the guide behaving correctly. One hedge on a headline rate in a
well-covered jurisdiction is worth more than twenty in a pack that hedges
everything.

Some will not settle, and Fiji shows what that should look like. Its dividend
rate is 0% under a 2017 exemption and 15% under the Income Tax Act, with
neither source retracting the other. The guide now names both, dates both, and
says which way to err, because an under-deduction is the payer's liability
while an over-deduction is the recipient's to reclaim.

### What the deadline pass has found so far

Five of the first eight jurisdictions were wrong, and a reader had picked those
eight because their rows looked odd. The next ten came from a random draw over
the 149 international jurisdictions with a row, and every one was right:
Afghanistan, Bhutan, Burundi, Costa Rica, El Salvador, Indonesia, Lesotho,
Sierra Leone, Tunisia, and Andorra's personal filing window.

Five in eight and zero in ten are both worth keeping. The first says the leads
were good. The second says the field is in better shape than the first number
implied, and it is the one to quote.

A fourth lead turned one of these findings into a script.
`scripts/check-deadline-rules.py` does the arithmetic that Greece and Andorra
failed: a guide states the rule and then what the rule works out to for a
calendar-year taxpayer, so the two halves can be compared. It found Norway,
where the accounts are approved within six months and filed by a fixed
31 July, and the six-month rule had been attached to the filing.

Its first run returned 43 hits and about 40 were the same mistake on the
checker's part: it assumed a 31 December year-end where the line named a
different one. Ethiopia counts four months from 7 July, Australian trusts two
months from 30 June, and Hong Kong's BIR60 is due a month after the return is
issued rather than after any year-end. Gated on a stated calendar year, it
returns two, and one of them is the open Andorra case.

A third lead found the sixth error without comparing any column. Armenia and
Finland had each frozen one filing season into a standing rule, so the next
step was to grep the deadline lines for any that name no year later than 2025.
That caught Australia, where `au-return-assembly` declares tax year 2025, dates
its BAS quarters correctly for the year ended 30 June 2026, and then gives the
return lodgement date for 2024-25. Look for the shape of an error you have
already found, not only for the field it appeared in.

The errors divide in a way the rate hides. Italy and Greece named a real date
belonging to a different obligation: Italy filed the Modello Redditi PF on
30 June, which is when IRPEF is paid, and gave the Modello 730 the second
acconto's date. Armenia and Finland froze one filing season into a standing
rule, so both read correctly this year and go wrong next year. Cyprus was not a
date at all, but a threshold stated two ways in one file.

Only the first kind is visible to a reader who knows the jurisdiction. The
second kind looks right until the calendar turns, and no check in `scripts/`
can see it, because a date that is correct for one year and presented without
one is not a contradiction. Prefer a guide that states the rule and gives this
year as an example.

### What the six VAT errors had in common

In every case a jurisdiction's overview or income-tax guide carried the correct
current rate, and its dedicated indirect-tax guide did not. That second file is
the one an agent loads to prepare a return. Maintainers refresh overviews from
summary sources and leave the deep guides alone.

`scripts/check-superseded-rates.py` sweeps for that shape. Two of the six would
still have escaped it. Malawi labelled its stale rate "(2025)" instead of
asserting it bare, and Maldives kept the correct figure in an income-tax guide,
which the script's tax-family filter throws out. A reader found both. So when
that script reports zero, you have learned something about the script as well as
about the corpus.

### What "verified" means here, and what it does not

It means the corpus agrees with a reputable secondary source, usually PwC's
Worldwide Tax Summaries. It does not mean a licensed practitioner in that
jurisdiction has confirmed it. Six times the corpus was right and the chart was
wrong:

- **Eswatini** — PwC lists 27.5%. It is 25% for year-ends after 31 December 2024,
  which both Eswatini guides state, with the date.
- **Nigeria** — PwC gives "30% (large companies)". `ng-cit` carries the whole
  NTA 2025 regime: the abolition of the medium-company band, the 4% development
  levy, and an AUDIT FLASH POINT on the NGN 50M / NGN 100M statutory conflict.
- **Fiji** — a chart gave 20%. It is 25%, or 15% for South Pacific Stock Exchange
  listings, which is what the guide says.
- **Tajikistan** — a chart gave 13%. That rate applies to production-of-goods
  activities; the standard rate is 18%. The guide carries both.
- **Somalia** — a chart gave a flat 15%. The rate runs progressively from 9% to a
  30% top rate above USD 30,000, cited to the Investment Promotion Office.
- **Sudan** — a chart gave 35%. The guide has 15% standard with 30% for banks,
  tobacco and petroleum, matching neither half of that figure.

Four of those six sit in the corporate pass, and its last tranche of about 35
jurisdictions turned up no corpus errors at all. Past the well-covered
jurisdictions, comparing against a chart stops finding defects and starts
inventing them, and each invented one invites you to break a guide that was
already right. Read the guide before you act on a hit.

### One defect that needs no script

`australia-payroll` once carried two headings over a single table, "### Resident
Individual Tax Rates (2026--27)" directly above "**Resident Individual Tax Rates
(2025--26)**". Every figure under them was right and the arithmetic checked out,
so no value check could see it. Only the year above the numbers was wrong, and a
reader who trusted the bold line dated a current table a year early.

That happened once in the whole corpus. This finds it:

```
grep -Pzo '(?m)^#{1,6} +([^\n]*?\b20\d\d\b[^\n]*)\n\n?\*\*([^\n]*?\b20\d\d\b[^\n]*)\*\*\n' skills/**/*.md
```

An 83-line checker for this used to live in `scripts/`. It was deleted: one
instance, already fixed, and a grep reproduces it.

Use a chart to generate leads. Only the Tier 1 route, where a named practitioner
signs the guide, supports an assurance claim, and nothing in this section changes
any guide's tier.
