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
| VAT/GST registration threshold | 20 jurisdictions | 2 | Albania, France. Egypt was **not** an error — see "Corrections made during PR review" |
| Withholding rate on dividends, interest, royalties | 10 of the 118 stating one | 3 | Ethiopia, Trinidad and Tobago, Belize. Iceland was **not** an error — see "Corrections made during PR review" |
| Payroll and social contribution rates | Morocco, Egypt | 0 | — |
| Personal income tax bands and exemptions | Egypt | 0 | — |
| Micro-regime threshold and dividend WHT | Romania | 2 | Romania |
| Minimum wage feeding contribution bases | Albania | 1 | Albania |
| Social contribution ceilings | Slovakia | 1 | Slovakia |
| Alternative minimum tax status | Taiwan | 0 | Taiwan — reverted, see "Corrections made during PR review" |
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

### Corrections made during PR review

The September 2026 review found errors in both proposed corrections and their
supporting narrative. The current guides incorporate these changes:

- Egypt's general VAT threshold remains EGP 500,000. ETA Decision 281/2025
  concerns an e-receipt rollout and does not establish a halved threshold.
- Fiji's exempt dividends do not carry the historical 15% withholding rate.
  FRCS Practice Statement 39/2017 and section 115 identify the exemption.
- Nigeria's National Assembly copy of the NTA defines a small company by
  turnover no greater than NGN 100 million and fixed assets no greater than
  NGN 250 million. The prior NGN 50 million correction was removed. Other
  companies pay 30%; the guide no longer uses a 20% medium band for 2026.
- Australia's permanent AUD 20,000 write-off was enacted on 26 August 2026.
  Schedule 2 commences on 1 October and applies to qualifying assets from
  1 July 2026. Enactment, commencement and application are separate dates.
- Kazakhstan's 2026 basic deduction uses 30 MCI, not the former 14 MCI.
- Ireland's 2026 lower employer PRSI band ends at EUR 552 weekly. The roadmap
  adds 0.15 percentage points in 2026 and 2027, then 0.20 in 2028.
- Liechtenstein's 2026 unemployment contribution is 0.5% per side on covered
  annual salary up to CHF 126,000. The borrowed Swiss estimates were removed.
- The Scottish 2026-27 band table states income including the standard
  personal allowance, rather than labelling its endpoints taxable income
  after that allowance. Uruguay's 2026 BPC is confirmed by Decreto 11/026.

Primary-source links appear beside the corrected guide statements. These are
targeted checks of changed claims, not a fresh professional sign-off on each
guide. Existing reviewer metadata records historical upstream review.

The register and rate extractors also needed fixes: federal guides now share
one jurisdiction group, identifiable direct-tax thresholds are omitted from
the VAT/GST list, and withholding tables can supply their heading context.
Shared single rates are listed for each payment type named. Regression tests
cover these cases. The expiry checker waits until the named month has ended.

### Limits of the review aids

The scripts produce leads for source review. They do not establish that a rate
has been enacted, that matching copies are correct, or that a missing entry
means a jurisdiction has no rule. Multi-rate labels, staggered deadlines,
unusual currencies and unlabelled facts can be missed or simplified.

Taiwan's proposed AMT start date is a review lead, not proof of enactment.
The guide requires confirmation of the current instrument before computing
a liability for an in-scope group. A higher-rate scenario is not tax due.
Iceland's disputed interest withholding claim was restored rather than
treated as a confirmed correction.

The coverage counts above are historical branch reports. They have not been
independently reproduced as an exhaustive source audit. Unit tests and guide
validation do not certify the legal content. Remaining research gaps require
review by a qualified practitioner before the guides support a filing.

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

### A "last verified" date is a falsifiable claim

`emerging-market-corridors` — the cross-border guide and its `agent-skills/`
mirror — stamped its Turkey → Germany block **Last verified: May 2026** and said
underneath it that "Turkey domestic WHT on dividends is 10% (recently increased
from 7.5%)". Turkey's dividend withholding went to **15%** on 22 December 2024,
by Presidential Decree No. 9286, which reversed the cut from 15% to 10% made on
22 December 2021. So the block understated the rate by five points, had the
direction of the last change backwards, and carried a verification date sixteen
months after the change it missed.

That combination is checkable without knowing any tax law. A guide asserting it
was verified on a date, while stating a value that a different guide in the same
corpus says was superseded before that date, has told you the verification did
not cover that field. `tr-corporate-income-tax` had "15% ... raised from 10% by
Presidential Decree No. 9286, 22 Dec 2024" the whole time, in the same
repository, four directories away. The corpus contained its own refutation.

Two smaller habits follow from it. A file-level "Last Verified" row above
per-section verification dates is the oldest of them, not the newest, and should
say so, or a reader takes the header as covering the section. And a verification
note is worth more when it says what was checked: this pass re-verified Turkey's
domestic rates and did not re-check the German side or the treaty articles, so
the block now says exactly that rather than restamping the whole thing.

The correction also moved the advice, which is the part a summary would lose. At
10% domestic the Turkey-Germany treaty's 15% portfolio dividend rate was worse
than domestic law. At 15% it merely matches, so a portfolio shareholder gets
nothing from the treaty and only the 5% substantial-holding rate is worth
claiming. A stale rate does not just misstate a number; it can invert whether
claiming treaty relief is worth doing at all.

### A guide can cite its source faithfully and still be incomplete

Every other correction on this branch was found by going back to the authority
the guide named. Egypt, Iceland, Taiwan, Turkey's interest rate, Bosnia, Kenya —
in each case the guide's own citation contained the answer, and the failure was
that nobody had opened it, or had opened it and read the wrong column.

The withholding-scope pass found the case where that method cannot work.

`list-withholding-scope.py` reports which heads of withholding each
jurisdiction's guides actually name. Sixty-four of 142 named only dividends,
interest and royalties. Turkey and Thailand were taken from that list, both
already worked on this branch for their rates. Neither guide was careless. PwC's
`corporate/withholding-taxes` page — the page both cite, and the page much of
this corpus was built from — carries, for those two countries, dividends,
interest, royalties and a treaty matrix, and nothing else.

The other heads are real and substantial. Turkey withholds 20% on professional
services, 20% on commercial rent computed on the gross, and 5% on progress
payments to contractors on multi-year construction. Thailand withholds 15% under
Section 70 on services, professional fees and rentals paid abroad, and
domestically 3% on professional fees, 5% on rent, 2% on advertising and 1% on
transport. None of it was on the cited page.

So the classic-only shape is not sloppiness. It is faithful reproduction of a
source that is itself three-headed for that country. The corpus inherited its
scope along with its numbers, and a guide built that way looks complete, cites
correctly, and verifies clean against its own source forever.

The rule this adds is narrow and worth stating on its own: **checking a figure
against the source the guide cites cannot tell you about a figure the guide does
not state.** Absence has no citation to check. The only defence is to ask what
the statute charges rather than what the page lists — and coverage varies, so it
cannot be assumed either way. PwC's Kenya page does carry the full withholding
table, which is how Kenya's six missing heads and one stale rate came out of a
single fetch. Its Turkey and Thailand pages do not.

That is also why the scope checker prints what each jurisdiction *does* name
rather than trying to detect what it should. Nothing in this repo knows what a
given statute charges. What it can know is that a guide naming three heads sits
oddly beside one naming eight, and that the difference is worth an hour.

### Three quarters of the corpus's citations are secondary, and it shows

`scripts/list-source-mix.py` classifies every external link by whether it points
at a tax authority or at a secondary source, ignoring the CTA block each guide
ends with. The measurement:

- **76% of citations are secondary** — 5,638 against 1,733 authority links.
- One publisher, PwC's Worldwide Tax Summaries, carries about a third of all
  external citations on its own. No authority comes close; the next largest is
  the IRS at 140.
- **41 of 189 jurisdictions cite no authority domain at all.** Every figure they
  carry rests on a summary.

That list is not a coincidence. Iceland, Slovakia, Mauritius, Laos and Libya are
all on it, and all five produced defects on this branch that only an authority
settled: Iceland's non-resident interest rate (Skatturinn says 12%, and 13% was
a 2024-only figure), Slovakia's minimum-tax band (the Financial Administration
says EUR 960 on taxable *revenues*, not EUR 940 on taxable income), Mauritius
naming three of eleven withholding heads, Laos three of six.

Two distinct failure modes sit behind this, both found on this branch:

- **The summary's scope becomes the corpus's scope.** PwC's withholding page for
  Turkey, Thailand and Austria is three-headed, so guides built from it are
  three-headed, however faithfully they cite it. Austria's entire §99 EStG
  charge — consultancy, hiring-out of labour, supervisory fees, performers, all
  at 20% — is absent from the page.
- **The summary's prose is not the collection agent's table.** Pakistan's
  securities CGT is computed and deducted by NCCPL, whose TY 2026 notification
  gives non-ATL rates as exactly double the ATL rates below 1 July 2025 and
  equal to them above it. PwC describes a "not less than 15%" floor and KPMG a
  normal-slab/29% treatment. Both describe the statute; neither is what gets
  deducted. Three successive versions of that table in this repo were wrong,
  two of them written during this very pass.

The rule that follows is narrow enough to apply: **for a tax collected at
source, read the collection agent's own notification before any summary of it.**
NCCPL, ZIMRA's REV 5 remittance return and Trinidad's Board of Inland Revenue
guide all publish the table they actually operate, and in each case it carried
something no summary did.

The checker ranks and never gates CI, because citing a summary is not a defect
and an authority link does not prove the figures came from it. It measures
exposure, not diligence.

### Three ways a guide comes to name three heads, and what each costs to fix

The withholding-scope queue turned out to hold three distinct defects wearing
the same shape, plus a fourth thing that is not a defect at all. They are worth
separating, because the cost of fixing them differs by an order of magnitude.

**The source has the rows; the guide took three.** Laos cites PwC's Lao PDR
withholding page and reproduced its first three rows. The same page carries six
domestic heads — adding service fees at 10%, rent at 10%, artist and athlete
income at 10% and share transfers at 2% — plus the Foreign Withholding Tax
table, a separate deemed-profit regime charging 1.4% to 6% by activity with 10%
VAT bundled in on services, and *final* on the foreign supplier. Kenya was the
same. **Cost: one fetch.** These are the cheapest findings in the corpus and
they should be exhausted first.

**The source does not have the head.** Austria's guide was faithful to its
source, every figure verified, and still missed the whole §99 EStG charge —
because PwC's Austria withholding-taxes page does not mention §99. Section 99
catches commercial or technical consultancy performed in Austria at 20%, the
hiring-out of labour at 20% with the *Austrian recipient* obliged to withhold,
supervisory board fees at 20%, and artists, entertainers, sportspeople,
lecturers, authors and architects at 20% where the activity happens in Austria.
Turkey and Thailand were the same. **Cost: knowing to doubt a clean
verification**, which no check can supply.

**The structure is wrong, not the list.** Trinidad and Tobago named three heads
because the guide enumerated where the statute has a catch-all. Sections 50–51
sort everything into two boxes: distributions at 3% to a parent and 8%
otherwise, branch profits included whether remitted or not; and *payments* at a
flat 15%, defined to cover rentals, management charges, personal services,
technical and managerial skills, annuities, discounts, premiums, commissions,
fees and licences. The fix is not six more rows — it is stating the rule, so a
head nobody thought to list still lands in the right box.

**And the fourth thing: the source does not cover the jurisdiction.** Of the
twelve small jurisdictions left on the queue — Andorra, Belarus, Benin, Bhutan,
Cuba, Eritrea, Iran, Libya, São Tomé and Príncipe, Suriname, Tajikistan and Togo
— PwC's withholding page exists for exactly one. Eleven return 404, Belarus
included; PwC no longer covers it. And Libya, the one with a page, levies no
withholding tax at all, so working it added no head — it converted three hedged
near-denials into a stated zero, plus the warning that matters more than the
zero: a foreign contractor is still assessed on **deemed profit at contract
registration**, so "0% withholding" answers the payer's question and misses the
contractor's liability entirely.

That last group is why the queue stops shrinking. It is not a backlog of unread
pages; it is the set of jurisdictions the corpus's main source does not have.
Closing them means national gazettes, regional tax cards or a paid database.
Saying so is more useful than leaving the number to look like inattention.

### Fixing a figure once is not fixing it

The most reliable way to introduce a contradiction into this corpus is to
correct something. A guide states the same figure in the frontmatter
description, a quick-reference table, a narrative section, a worked example, a
prohibition and a provenance note. The table is the part you are looking at when
you decide the figure is wrong. The other five are not.

Three cases on this branch, in order of discovery.

Pakistan's income tax guide had the wrong top salaried rate. Correcting the
table left **nine** other places saying the old thing, three of them operative,
including the section heading directly above the corrected table.

`pk-cgt` was then rewritten for the Section 37A cohorts, and four satellites
kept the superseded non-filer wording. Worse, the rewrite itself was wrong: it
moved the acquisition-date boundary from 1 July 2024 to 1 July 2025, invented a
cohort that does not exist, and deleted the statutory "not less than 15%"
non-ATL floor as an error. The mechanism is worth naming because it is not
carelessness and it will recur — **the year of the Act is not the year of the
cohort.** The Finance Act 2025 governed the tax year, so the cohort it governs
was assumed to start in July 2025. FA 2024 set the boundary; FA 2025 left it
alone. Read a boundary date out of the rate schedule, never off the Act's name.

Three Bulgaria guides described the 2026 State Social Security Budget Act as an
unadopted draft in fourteen places, quoting a proposed ceiling of EUR 2,352 that
never passed, while the prohibitions section of one of those same files already
recorded the Act as gazetted on 28 July 2026 with a ceiling of EUR 2,300. The
file contradicted itself, and the stale half was the half an agent computing
contributions would reach first.

That last shape is the dangerous one. A guide with an old figure is wrong. A
guide with a corrected table and an uncorrected satellite is wrong *and* looks
authoritative on both sides, with nothing to tell a reader which is current.

`scripts/list-incomplete-fixes.py` catches it mechanically. It reads your own
diff, collects the values you removed and did not re-add, and looks for them in
the parts of the file you did not touch. Unlike everything else in `scripts/`,
it is an author's pre-push check rather than a corpus check, and like
`list-solo-citations.py` it ranks rather than accuses and never gates CI.

It has to rank, because three legitimate shapes look identical to it. A **dated
worked example** keeps its own year's figures — Bolivia's Form 610 example is
computed at the 2025 minimum wage of Bs 2,750 and says so, and re-rating it at
2026 figures would make a correct example wrong. The **other side of a
supersession** survives legitimately — the UK guide's GBP 9,013.80 belongs in
the 2025-26 computation it was computed for, even though a speculative 2026-27
projection that had copied it was deleted. And a figure can be **right in one
cohort and wrong in another**: Pakistan charges 45% at the top of the
non-salaried slab and 35% at the top of the salaried one, so removing 45% from
one row says nothing about the row below.

One thing it cannot see, recorded in its own selftest as a known miss: a value
restated in different **units**. Removing "BGN 4,130" while the file still says
"EUR 2,111.64" is the same figure at the fixed conversion rate. Bulgaria needed
that caught and it was caught by hand.

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
