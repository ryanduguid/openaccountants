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

The honest headline is **"source-cited drafts here, accountant-reviewed via MCP"** — never a blanket "reviewed by accountants." Most skills in this repo are Tier 2. See [COVERAGE.md](COVERAGE.md) for the exact split.

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
None of them can see a figure that every copy agrees on and that is wrong. To
close that gap you have to ask a source outside the repository, one field and one
jurisdiction at a time. This section records how far that has got.

### Checked against an outside source

| Field | Coverage | Errors found | Notes |
|---|---|---|---|
| Standard VAT / GST rate | 157 of 157 jurisdictions stating one | 6 | Fiji, India, Kazakhstan, Zimbabwe, Malawi, Maldives |
| Headline corporate rate | ~135 jurisdictions | 3 | Lithuania, Cyprus, Portugal |
| Annual return filing deadline | 24 jurisdictions | 8 | Italy, Greece, Armenia, Cyprus, Finland, Australia, Norway, Brazil |
| VAT/GST registration threshold | 20 jurisdictions | 3 | Egypt, Albania, France |
| Withholding rate on dividends, interest, royalties | 10 of the 118 stating one | 4 | Ethiopia, Iceland, Trinidad and Tobago, Belize |
| Payroll and social contribution rates | Morocco, Egypt | 0 | — |
| Personal income tax bands and exemptions | Egypt | 0 | — |
| Micro-regime threshold and dividend WHT | Romania | 2 | Romania |
| Minimum wage feeding contribution bases | Albania | 1 | Albania |
| Social contribution ceilings | Slovakia | 1 | Slovakia |
| Alternative minimum tax status | Taiwan | 1 | Taiwan |
| Penalty and interest on overdue tax | Cyprus | 0, one conflict recorded | — |
| Minimum corporate tax bands | Slovakia | 1 | Slovakia |
| Statutory citations | Pakistan, Ireland (partial) | 0, one unverified | — |
| Forthcoming rate steps | Ireland | 1 gap filled | Ireland |
| Capital allowances | Australia | 1 | Australia |

The deadline pass has covered 24 jurisdictions of 200. Nobody has run an external
pass over anything else. That leaves payroll rates and thresholds, registration
and filing thresholds, penalty and interest rates, social-contribution bands,
capital allowances, withholding rates, form names and statutory citations. All
of them move on the same annual cycle as the fields above.

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
