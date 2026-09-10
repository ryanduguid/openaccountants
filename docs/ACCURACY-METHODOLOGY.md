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

### Most of the corpus's citations are secondary, and it shows

`scripts/list-source-mix.py` classifies every external link by whether it points
at a tax authority or at a secondary source, ignoring the CTA block each guide
ends with. The measurement:

Run it rather than trusting the numbers below:

```
python3 scripts/list-source-mix.py
```

**As at 10 September 2026: 66% of citations were secondary — 4,844 against 2,540
authority links, with 18 of 189 jurisdictions citing no authority domain at
all.** One publisher, PwC's Worldwide Tax Summaries, carries about a third of
all external citations on its own; the next largest is the IRS at 140, then
Estonia's tax board at 82.

Those counts are a dated snapshot and are quoted for the argument, not as a
current figure. They drifted **six times** while this section was being
written — adding `lex.uz` to the classifier moved the zero-authority count by
one, correcting Uzbekistan moved the citation totals, auditing the statute-link
queue found nine more revenue authorities and statutory funds the classifier
had been calling marketing sites, and then a code review found four domains on
the allowlist that were not authorities at all. That is the same defect
`scripts/check-coverage-claims.py` exists to catch in `COVERAGE.md`: a derived
number copied into prose is stale the moment the thing it describes changes.
The command is the durable statement; the numbers are an illustration of it.
The heading above used to say "three quarters", which was true of the first
measurement and of no measurement since; a fraction in a heading is prose that
nobody re-runs.

> **The first version of this measurement was wrong, and the way it was wrong is
> the point.** It reported 76% secondary and 41 zero-authority jurisdictions,
> because its authority test was a government-domain pattern and a great many
> revenue authorities are not on government domains. Botswana headed the
> zero-authority list while citing `burs.org.bw`, its own revenue service.
> Estonia's tax board, the corpus's most-cited authority after the IRS, scored
> as secondary. The allowlist is now built from measurement — every entry is a
> domain the corpus actually cites — and `--unclassified` prints the remaining
> authority-shaped candidates so the omission stays visible rather than silent.
> Read the authority count as a **floor**, never a ceiling — with the caveat in
> the next section, which is that an allowlist can also be wrong upwards.

The list still earns its place. **Slovakia, Laos and Libya** are on it, and all
three produced defects on this branch: Slovakia's minimum-tax band (the
Financial Administration says EUR 960 on taxable *revenues*, not EUR 940 on
taxable income), Laos naming three of six withholding heads, Libya's three
hedged near-denials where its source states plainly that the country levies no
withholding at all.

**Iceland and Mauritius were on the list and are no longer**, which is the
measurement working as intended: Iceland's guide now cites Skatturinn because
correcting its interest rate meant going there (12%, against a 13% that was a
2024-only figure), and Mauritius's now cites the MRA because that is where the
missing eight withholding heads were found. Fixing a jurisdiction by reading its
authority takes it off this list.

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

### An allowlist can be wrong upwards, and that error never reports itself

Every correction recorded above ran one way: the checker could not see authority
the corpus was citing, someone noticed, the count went up. Six passes, always
the same direction. A code review on the pull request found the opposite, and it
is the more dangerous shape.

`manao.mg` was on the allowlist, commented "Madagascar tax portal". Manao sells
accounting and payroll software. It went on the list from its name, in a batch
where the surrounding entries were revenue authorities, and nothing afterwards
looked at it again. It was the **only** domain scoring as an authority for
Madagascar, so one unchecked entry took a jurisdiction off the zero-authority
queue — the queue this script exists to produce. Three more went the same way:
`startup.sm` ("© San Marino Management Srl"), `camcom.sm` (a *società a capitale
misto pubblico-privato*, an economic development agency and not the Ufficio
Tributario) and `palgakalkulaator.ee`, a salary calculator naming no publisher,
cited as the source for Estonia's statutory minimum wage.

The two errors are not symmetric, and the asymmetry is the whole lesson:

- A **missing** entry over-reports risk. The jurisdiction stays on a list
  somebody reads, and the next person to read it removes it. That is how six of
  these corrections happened.
- A **wrong** entry under-reports risk, silently, with no artefact left behind.
  The jurisdiction leaves the queue and nothing ever looks at it again. There is
  no output anywhere that says "Madagascar's entire score rests on one domain
  nobody checked."

So the allowlist now states its test — *the domain belongs to the body that
makes, administers or collects the charge, or publishes the official text of the
law* — and `--load-bearing` prints the entries a jurisdiction's whole authority
score depends on:

```
python3 scripts/list-source-mix.py --load-bearing
```

Eleven entries currently hold a jurisdiction off the queue on their own. Those
are the ones to check hardest, because those are the ones where a mistake is
invisible. The removals put Madagascar back on the list and moved the secondary
share from 65% to 66%; San Marino stayed off it, correctly, because it cites
`gov.sm` once.

The same review found the matching bug in `scripts/list-withholding-scope.py`.
Its `--show` mode exists precisely so that nobody writes "this guide omits X"
without reading every line; its docstring says so. When `heads_in()` learned
that a dedicated withholding guide does not repeat the word in every row label,
`--show` kept the old label-only test. `--show israel` printed **7** lines where
the scan counted **44**, dropping the entire rate table — services, rent,
royalties, interest, dividends — that the fix had been written to surface. A
diagnostic that under-reports against its own checker is worse than no
diagnostic: it reads as proof the rows are absent.

Both are the same defect in different clothes. **Anything that removes an item
from a review queue needs more scrutiny than anything that adds one**, because
only one of those two mistakes leaves something behind for a person to find.

### A citation can name the right statute and still mislead

`scripts/list-statute-links.py` looks at markdown links whose **clickable text**
names an instrument. The corpus writes `[Instrument name](where I read about
it)`, which is honest as far as it goes — 944 links do it — but it means the
anchor text describes the law and the destination is something else entirely.

Most of the time that is harmless: a reader who clicks `[Income Tax Act]` and
lands on PwC can see immediately what they are looking at. The checker leaves
those alone. What it reports is the sharp end — links where the destination was
neither a tax authority nor a recognised tax publisher. `[Code Général des
Impôts (Bénin) — IRPP barème]` went to an HR platform's country page. `[OHADA
Uniform Act on Commercial Companies]` went to a corporate-services firm.
`[Civil Code of Curaçao, Book 2]` went to a law firm's marketing site.

The figures beside them may be perfectly correct. The citation is still telling
the reader something untrue about where it came from, and — like Portugal's
wrong Portaria — it survives every check that compares numbers, because there
is no number in it to compare.

The fix is presentational and safe: move the instrument name out of the anchor
so the link says where it goes. `[Code Général des Impôts (Bénin)](rivermate)`
becomes `Code Général des Impôts (Bénin) (as described at [rivermate.com](…))`.
Nothing about the tax changes; the reader stops being told they are clicking
through to a statute. Run `python3 scripts/list-statute-links.py` for the
current count; it was 305 across 53 jurisdictions when the queue opened.

**Two blind spots in that checker, found by testing it rather than reading it.**
Both were false negatives, which is the kind that survives — a checker that
under-reports looks clean.

The first was a one-word slip: on a line with several links, `return` where
`continue` belonged, so scanning stopped at the first link that did not name an
instrument. Thirty-nine lines in the corpus start with a plain link, and every
statute link after one was invisible. It happened to change no count on today's
corpus, which is exactly why it would have lasted.

The second was worse, because it was a gap in what the checker knew rather than
a slip in how it looped. The instrument vocabulary was `Act|Code|Law|Ordinance|
Decree|Loi|Código|Ley|…` — the words a common-law and francophone reader
reaches for. Ethiopia and Eritrea legislate by **Proclamation** and by nothing
else. Every statutory citation in both guides was therefore out of scope, and
Eritrea alone accounted for 18 of them, all pointing at commercial tax-data
sites. A vocabulary drawn from the legal systems you already know will silently
exempt the ones you do not. Adding `Proclamation`, `Regulation`, `Lei`, `Legge`
and `Resolution` found 27 more. `Order`, `Rules`, `Bill`, `Statute`,
`Constitution`, `Notification` and `Circular` were measured too and left out —
each is either ambiguous in English or absent from the corpus.

**And one false positive, which is the kind that gets caught.** The British
Virgin Islands' two `[National Health Insurance Regulations]` links go to
`vinhi.vg`, which the checker called a marketing site. It is the scheme itself:
its bulletin of 12 September 2024 sets the US$102,000 ceiling and the 3.75% +
3.75% split the guide quotes, over its own contact details. Same class as
NCCPL, FRCS and BURS — the body that computes and collects the charge,
publishing the table it collects under. BVI's two best citations were about to
be filed as defects. `vinhi.vg` is now a recognised authority in
`list-source-mix.py`, which also lifts BVI out of the zero-authority list.

**So the whole queue was audited destination by destination before a single
link was converted, and 45 of the 305 were wrong — 15%.** Nine were bodies
that compute and collect the charge the guide quotes: Burundi's `obr.bi`,
Curaçao's `svbcur.org`, the national insurance boards of Trinidad, the BVI and
the Bahamas, South Sudan's social insurance fund (on free hosting, which is
why it looked like a brochure), Liechtenstein's `llv.li`, Finland's `prh.fi`.
Two more were recognised publishers under another name — Legal 500 and
Bloomberg Tax.

Tonga is the one worth spelling out. Its links point at PDFs on a trade
portal, which reads like a brochure site. The PDF is the **Consumption Tax Act
CAP. 26.02, 2016 Revised Edition**, 31 pages, and s.5(3)(a) says "The rate of
Consumption Tax shall be 15 per cent" — the exact figure the guide cites. The
link was already doing what its anchor promised, and the checker was about to
recommend rewriting it.

**A heuristic was tried here and thrown away, which is worth recording.** The
idea was to exempt a link when the URL path echoes words from the anchor, on
the theory that the destination is then the instrument itself. It exempted
nine links and eight were wrong: a blog post *about* Ethiopia's amendment
Proclamation, a country page that happened to contain "tome" and "principe".
And it missed Tonga — the very case that prompted it — because the anchor was
short enough that only one word overlapped. String overlap between a label and
a URL does not test whether a document is a statute. It is the same mistake as
testing a file-level claim with a line-level pattern: **scope the test to the
claim.** Checking what the domain actually is does test it, and costs one
fetch.

### The queue read 1, and that was the strongest evidence it was broken

This section used to end by saying "the queue is now empty", after 260
conversions cleared it — with the caveat that this was no claim that every
citation in the corpus points somewhere good, since 66% of them still point at
commentary. The caveat was true and far too weak. The queue was empty because
the checker was looking at a shape the corpus mostly does not use.

There are two citation shapes here. The markdown link:

```
[Code Général des Impôts (Bénin)](https://www.rivermate.com/guides/benin)
```

and the trailer the generated fact blocks end almost every bullet with:

```
_(Code Général des Impôts (Madagascar) — TVA — https://manao.mg/fr/tva)_
```

Same claim, same harm, no markdown link in the second. Scanning only `[…](…)`
made **528 citations across 78 jurisdictions invisible** — under exactly the
test the markdown scan applies, that the destination is neither a tax authority
nor a recognised tax publisher. Madagascar names the Code Général des Impôts
sixty-five times, links to an authority zero times, and not one of those was in
the queue. The count is now **529**.

Two things about how that was found are worth keeping.

**It was found by disbelieving a clean result, not by a failure.** Nothing was
wrong with the output. The queue said 1, the selftest passed, the suite passed.
The prompt to look was a jurisdiction returning to the *other* queue — Madagascar,
after the `manao.mg` removal — and noticing that its citations all named the tax
code while none of them had ever appeared here.

**The first measurement of the blind spot was itself wrong, in the same
direction.** It returned **982**, because it exempted recognised publishers and
forgot to exempt authorities. `dgii.gov.do`, `gra.gm`, `src.gov.sc`, `ura.go.ug`
— the Dominican, Gambian, Seychellois and Ugandan revenue authorities — are
where a statute citation is *supposed* to land, and 454 of them did. Applying
the checker's real test gives 528. A measurement of a checker's blind spot is
itself a checker and needs the same scepticism.

Clearing the queue is a worklist of 529, not part of this change; the conversion
form is the one already used for the markdown shape, `Instrument name (as
described at [host](url))`, which keeps the instrument name — the true half of
the citation — and stops it claiming to be the destination.

### Reading the statute changes the answer, and twice it nearly changed it wrongly

The zero-authority list is where the corpus carries the most inherited risk, so
two of its jurisdictions were worked by reading their law rather than a summary
of it: Armenia (48 citations, none to an authority) and Kosovo (16).

Both produced real errors. Armenia's guide taxed a registered individual
entrepreneur's business income at the flat 20% income tax; art. 104(1)(1) makes
an IE a resident *profit* taxpayer and art. 125(3.1) sets that at 23%. Its
turnover-tax table was two regimes out of date, and it stated in three places
that the turnover tax allows no deductions — art. 258(2)–(5), from 1 January
2025, cuts the computed tax by up to 9.5% of documented expenses, so the
guide's worked example overstated the tax by as much as ten times. Kosovo cited
**Law No. 08/L-110** as its Personal Income Tax Act. That law establishes the
Kosovo Accreditation Agency. The tax law is 05/L-028 — as the guide's own
payroll and social-contributions files both correctly said.

**Two ways this could have gone wrong, and nearly did.**

*The general rate article is not the end of the article.* Armenia's art. 125(1)
says 18%, and two secondary sources agreed that an individual entrepreneur pays
18%. The corpus's own optimisation guide said 23%, which looked like a leftover
from the pre-2023 income tax and was queued for correction. Art. 125(3.1),
three subparagraphs further down, sets 23% for IEs specifically. The guide was
right; "correcting" it against the headline rate would have broken a correct
figure with a wrong one from the same statute.

*A search summary is not a source.* A search result reported Armenia's minimum
wage as having risen to AMD 75,000 in January 2025 from AMD 68,000, which would
have made the guide's "since 1 January 2023" wrong. The Law on Minimum Monthly
Salary on `arlis.am` shows the amendment dated 7 December 2022, effective the
following January — the guide was right. Separately, a news article the same
search surfaced as evidence of a 2026 increase turned out to be from **November
2021**, describing a five-year plan to reach AMD 85,000 by 2026. The year in
the target is not the year of the article.

Both near-misses share a shape with the Iceland interest rate a reviewer caught
earlier on this branch: the correction was the confident move, and the
confidence came from a source that was not the law.

**And the wrong citation propagates into the instructions for fixing it.**
Kosovo's guide flagged its own open question — is the gross-income-method
ceiling EUR 50,000 or EUR 30,000? — and told the reviewer to settle it "against
the consolidated text of PIT Law No. 08/L-110", which is the accreditation
statute. The answer is that Kosovo has three thresholds in three laws: EUR
50,000 for the personal gross-income method (05/L-028), EUR 30,000 for the
corporate small-taxpayer flat tax (06/L-105, which *reduced* it from 50,000 in
2019), and EUR 30,000 for VAT registration (05/L-037). The old corporate figure
and the current personal one are the same number, which is how they merge.

**Ethiopia: the citation named the right Proclamation and the wrong subject.**
`et-tax-overview.md` gave the VAT return deadline as "the 21st day (per local
practice; some sources cite end of the following month)", hedged "approx —
confirm", and cited VAT Proclamation No. 1341/2024 *as described at* an article
about VAT **registration** obligations. The article says nothing about filing.
Meanwhile `ethiopia-vat.md`, in the same repository, gave the last day of the
following month — so the corpus held both answers and pointed at neither.

Art. 58(1) of the Proclamation settles it: "A registered person shall file a VAT
return for each accounting period **on or before the last day of the calendar
month following the end of the period**." There is no 21st-day rule. Art. 58(2)
requires the return whether or not net VAT is payable, and art. 59(1) makes
payment due on the same date.

Reading art. 2 for the definition of the period then produced something neither
guide had: *"'Accounting Period' means each calendar month. The months of August
and Pagumen shall be aggregated and treated as One calendar month."* Pagumen is
the 5- or 6-day thirteenth month of the Ethiopian calendar, so the VAT year has
**twelve** filing periods, not thirteen. Nothing flagged that, because nothing
was wrong — the guides simply said "monthly" and stopped. **A hedge marks the
figures somebody doubted; it cannot mark the ones nobody thought to ask about.**

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

A second blind spot, found by the code review on the pull request and worth
stating because it is easy to walk into. The script works from **values you
removed**. A correction written *beside* the old claim rather than replacing it
removes nothing, so it is invisible.

Armenia's guide is the case. A research gap in §5.10 said "salaries paid to
employees still bear a fixed reduced income tax of ~AMD 5,000/employee/month".
Reading the Tax Code showed the micro regime does no such thing — art. 269(2)(2)
puts employee wages back under ordinary income tax withholding, and the AMD
5,000 belongs to art. 125(3), which charges an *individual entrepreneur in the
turnover-tax system* AMD 5,000 a month as their own final profit tax. That
correction went into the special-regime rate map as a new row. §5.10 was left
standing. The guide then asserted both, forty lines apart, and the checker had
nothing to report because nothing had been deleted.

So the rule the script cannot enforce: **when a correction contradicts something
the guide already says, the old sentence has to go, not merely be outvoted.**
Search the file for the number before writing the new row, and again after.

Reading the same article also turned up something the guide had been silent on
in both directions: art. 125(3) makes the AMD 5,000 a month a liability the
turnover tax does **not** absorb, so the turnover-tax worked example — which
computed the tax three ways against the art. 258(2) expense deduction — was
understating a quarter by AMD 15,000 the whole time.

### A second heuristic tried and discarded: denied-but-still-asserted

This shape turned out to be the single most common finding in outside review of
this branch. Of fifteen findings a code review raised against the merged work,
**seven** were a figure corrected in one place and left standing in another —
Paraguay's minimum wage, Scotland's 2026-27 bands, Uruguay's deduction credit,
Nigeria's abolished medium-company band, Egypt's VAT threshold, Portugal's
4×IAS ceiling, Pakistan's non-filer row. Two more on the following pull request
had the same shape. All were eventually fixed by a person reading both lines.

So it was worth trying to automate, and the attempt is worth recording because
it failed in an instructive way. The idea: a correction leaves a **denial
sentence** that names the figure it retires — "there is no medium-company 20%
band", "EGP 250,000 is not the VAT threshold", "previously stated 10%". Take the
figure out of the denial and look for it still being asserted, in a labelled
bullet or table row, elsewhere in the same file.

One sub-lesson from it is worth keeping even though the script is not. **A
denial sentence's figures split by which side of the marker they sit on.**

```
"25%, superseding the 20% that applied to 2025"   retires what FOLLOWS
"EGP 250,000 is not the VAT threshold"            retires what PRECEDES
```

Treating every figure in the sentence as retired gets the first case backwards
and flags 25% — the very rate the sentence exists to establish. The first
version did exactly that, and it was caught by a selftest case written to
*document a false positive*, which then failed because the rule was wrong in a
different way than expected. A test written to pin down a known weakness found
an unknown one.

The script still had to be discarded. Measured over the corpus:

| variant | rows | jurisdictions |
| --- | --- | --- |
| as first written | 7,942 | 118 |
| drop "rather than" / "instead of" as denials | 7,570 | 113 |
| + require a shared subject word between the two lines | 2,685 | 104 |
| + only figures appearing in ≤5 files corpus-wide | 472 | 50 |

Each tightening cut the volume and **none of them improved precision**: the
sample at 472 rows is as wrong as the sample at 7,942 — one denial line in
Iceland's payroll guide matching every legitimate mention of the rate it
discusses. It would have caught Armenia, the case that prompted it, and buried
it under hundreds of rows nobody would read.

The missing piece is the one that was hard from the start and got talked past:
linking the two lines to **the same subject**. A shared word is not that. In a
corpus where 15%, 20% and 30% each appear in hundreds of files against unrelated
heads of charge, a bare figure match carries almost no information, and the
denial vocabulary cannot tell "the guide retired this figure" from "the guide
discusses this figure".

Recorded as a negative result, on the same terms as the URL-overlap heuristic
above. The control that does work is the human rule already stated: **when a
correction contradicts something the guide already says, search the file for the
number before writing the new row, and again after.**

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
