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

**As at 10 September 2026: 65% of citations were secondary — 4,804 against 2,608
authority links, with 14 of 189 jurisdictions citing no authority domain at
all.** One publisher, PwC's Worldwide Tax Summaries, carries about a third of
all external citations on its own; the next largest is the IRS at 140, then
Estonia's tax board at 82.

That last figure moved from 18 to 14 in a single afternoon, and none of the four
gained a verified rate. Iraq, DR Congo, Suriname and Libya each had a live,
reachable revenue authority the corpus had simply never linked to: Iraq cited
PwC 55 times and an incorporation firm 14 times while `tax.mof.gov.iq` published
guides to income, property, corporate and withholding tax. Three of the four
needed no allowlist entry at all — their domains already matched the government
pattern. The only thing missing was a link.

Which is worth stating plainly, because the queue is easy to misread: leaving
the zero-authority list means *a citation now points at the authority*, not that
anything it says has been checked against it.

Those counts are a dated snapshot and are quoted for the argument, not as a
current figure. They drifted **eleven times** while this section was being
written — adding `lex.uz` to the classifier moved the zero-authority count by
one, correcting Uzbekistan moved the citation totals, auditing the statute-link
queue found nine more revenue authorities and statutory funds the classifier
had been calling marketing sites, then a code review found four domains on
the allowlist that were not authorities at all, then reading the statute-link
queue's *destinations* found four more (`u.ae`, `nssfug.org`, EswatiniLII,
NamibLII), then `belastingdienst.sr`, and then four jurisdictions were linked to
authorities that had been reachable the whole time. That is the same defect
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

### A cited domain can stop being what the citation says it is

Benin's tax overview cited its tax year to
`https://finances.bj/wp-content/uploads/2025/01/Benin-Code-General-des-Impots-2025.pdf`.
That was the Ministry of Finance. The domain is now an Indonesian online-casino
site. The Direction Générale des Impôts has moved to
`www.impots.finances.gouv.bj` and still lists `cdgi@finances.bj` as its own
contact address, which is how you can tell the domain was theirs and was lost
rather than never having been theirs.

**A status code would not have found it.** `finances.bj` answers HTTP 200. Not
down, not a 404, not a redirect. Every check that asks "does this link resolve"
passes it. The domain is alive and answering; it just is not the ministry any
more. So `scripts/list-citation-rot.py` reads the body, not only the code.

The harm is sharper than a misdescribed source. A citation that names a statute
and lands on tax commentary sends a reader to tax commentary. This sends a
reader who is following a government citation to a gambling site, from a file
that names a Ministry of Finance beside the link.

Two hosts across 1,256 checked:

| Host | Citations | Jurisdiction | What it serves now |
|---|---|---|---|
| `zambiaprice.com` | 7 | Zambia | Indonesian slot-gambling SEO |
| `finances.bj` | 1 | Benin | an online casino, or a 500 |
| `doingbusiness.co.bw` | 1 | Botswana | "Under Construction" and a shopping cart |
| `obr.bi` | 1 | Burundi | HTTP 200 and a Joomla fatal error |

Zambia's is the worse of the two by consequence: those seven citations are the
*entire* NAPSA and NHIMA contribution table — both rates, both splits and the
monthly ceiling. Every figure in that block rested on one page that no longer
exists.

There is a third case that is not link rot at all. `www.impots.finances.gouv.bj`
— Benin's real, live, correct tax authority — is itself serving injected casino
spam ("Melbet Jordan", "Mol Casino", "ronybet"), the signature of a compromised
WordPress install. The citation is right and the authority is right; the
authority's site is hacked. Nothing the corpus can fix, and worth knowing.

#### The exemption that would have hidden it

The first draft of the checker **suppressed** a squatter match when the page
also read institutional — on the reasonable theory that a gaming regulator
cited for betting duty legitimately uses those words. That rule was replaced,
before the first real run, with a demotion: such a page goes to its own printed
bucket instead of disappearing. The reasoning was the one this document keeps
arriving at — *a wrong exemption is the error that never reports itself.*

On the first real run that decision paid for itself immediately. Benin's DGI is
institutional **and** compromised. The suppressing version would have shown
nothing.

#### And the bucket that was not measured at all

The same run put **github.com at the top of the dead list, with 169 citations**,
and `canada.ca` just below it. Neither is dead.

The selftest covers `judge()`, which decides what a response *means*. It could
not cover `fetch()`, which decides what response you *get*. So the classifier
was measured and the fetcher was not, and one whole bucket of 186 hosts and 654
citations came back unvalidated — reported with the same confidence as the two
real findings.

**First diagnosis, wrong.** Under fourteen-way concurrency a busy host times out,
and a timeout is indistinguishable from a domain that no longer exists. So a
serial re-check was added: anything the concurrent pass would call dead is tried
again, minutes later, with no contention.

The next sweep put github.com at the top of the dead list again. **Three of 171
hosts cleared.** The fix had addressed a hypothesis that was never tested — which
is the same error as the bucket it was meant to repair, committed while repairing
it.

**Second diagnosis, and the actual one: the environment.** These sweeps run
behind a policy-enforcing egress proxy. It answers 400 for github.com over both
schemes while `curl` reaches it perfectly well, and its own status endpoint
reports `gateway answered 502 to CONNECT (policy denial or upstream failure)`
for host after host sitting in the dead list — `minfin.gov.tm`, `mof.gov.er`,
`finances.gov.td` among them.

From inside the sandbox, **a policy denial and a dead domain are the same
event.** 592 citations were reported dead on the strength of neither, twice.

The script now proves it can reach the network before it is allowed to call
anything unreachable: a handful of control hosts are fetched first, and if any
fails the dead bucket is not printed at all and the summary says why. The serial
re-check stays — contention is real and the check is cheap — but it is no longer
mistaken for a fix.

That the loudest false positive was github.com, **both times**, is luck. A false
positive that obvious gets fixed within the hour. Had the same flaw produced a
plausible-looking list of small foreign tax authorities, it would have been
believed on both occasions, and a batch of working citations would have been
"fixed" away from sources that were fine.

There is a general form of this worth keeping: **a checker that depends on the
network cannot tell you the network is broken.** It will report the shape of its
own environment as a property of the thing it is measuring, and it will do so
with a plausible number attached.

#### What it cannot see

Hosts, not documents. A ministry whose site is healthy but whose 2019 PDF has
been reorganised away passes here, and that is the commoner kind of link rot by
a wide margin. Host-level is what catches the class above — and that is the
class that misleads rather than merely disappoints.

It also does not judge WAF rejections. A live authority behind a firewall
answers a script with 403 or 406 — `impots.finances.gouv.bj` itself does, and so
do `onrc.ro` and `registrucentras.lt` — and calling those dead would bury two
real findings under 364 citations to sites that are perfectly fine.

### Legal information institutes are not a class

Reading the statute-link queue's destinations turned out to be a way of asking
the authority allowlist what it was missing, and it named four: `u.ae` ("The
Official Platform of the UAE Government"), `nssfug.org` (Uganda's NSSF, the
statutory fund that collects the charge), `eswatinilii.org` and `namiblii.org`.

The last two are the interesting ones, because the obvious move — treat LIIs as
a class — is wrong in both directions. The test this repo uses is whether the
domain belongs to the body that makes, administers or collects the charge, *or
publishes the official text of the law*. Applied to three LIIs:

| Site | Run by | On the list? |
|---|---|---|
| EswatiniLII | "the Judiciary of eSwatini" | yes |
| NamibLII | "the Law Reform and Development Commission" | yes |
| ZambiaLII | SAIPAR, "an independent, educational and development oriented research centre", collecting cases "indirectly from the Zambian judiciary" | **no** |

Three sites, near-identical front pages, same software, same movement — and the
test splits them. Adding them wholesale would have credited a research centre's
republication as the official law; skipping them wholesale would have kept two
state publishers scored as marketing sites.

`onrc.ro` and `registrucentras.lt` are almost certainly authorities too. Both
were left off, because both answer a script with a rejection and neither could
actually be read. Adding a domain because its name and reputation fit is exactly
how `manao.mg` got onto this list in the first place.

### The article you find first may not be the article that governs

Benin states a top personal rate of 30%. Art. 136 of its Code Général des Impôts
sets a progressive barème topping out at **40%**. That looks like a clean
correction, and it is wrong.

Art. 137 gives the game away: its minimum tax applies to taxpayers with
"revenus industriels, commerciaux et non commerciaux, artisanaux et agricoles".
Art. 136 is the *business* scale. Salaries run on their own scale under art. 142
— 0/10/15/20/30% in monthly slices — and art. 181(3) makes the salary
withholding *libératoire*, final, so salary income never reaches art. 136 at all.

Both figures are right. Neither is the whole answer, and the guide's unqualified
"30 percent" was half of it. This is the third time on this branch that reading
further has stopped a correct figure from being "corrected" — after Armenia's
art. 125 and Ethiopia's accounting periods — and the first time where the trap
was not a later paragraph of the same article but *a different article
altogether*.

The same page produced a smaller version of the same lesson. Benin's employer
payroll tax is 4%, and the surrounding text made arts. 211–212 look like the
citation. Checking rather than inferring: 211 is the charge, 212 the exemptions,
**214** the rate — which also carries a 2% reduced rate for private schools that
no summary of it mentioned.

---

Use a chart to generate leads. Only the Tier 1 route, where a named practitioner
signs the guide, supports an assurance claim, and nothing in this section changes
any guide's tier.

### Why so much of this corpus cites PwC: some authorities cannot be read

The section above reports that 65% of the corpus's citations are secondary, and
treats that as exposure. Part of it is not a sourcing choice at all.

Trying to check three jurisdictions off the zero-authority list against their own
authorities, in one sitting:

| Jurisdiction | Authority | What a fetch gets |
|---|---|---|
| Madagascar | `impots.mg` | 503 on every attempt, two days apart; five other Malagasy government hosts refuse the connection outright |
| Myanmar | `ird.gov.mm` | Loads, and is entirely in Burmese; the rate tables sit behind further navigation |
| Azerbaijan | `taxes.gov.az` | Loads. The Tax Code page is 451 KB of HTML that yields 7.7 KB of text — the Code itself is rendered by a JavaScript viewer |
| Cape Verde | `mf.gov.cv` | Loads; the ministry portal does not link the tax content from its front page |
| Zambia | `napsa.co.zm` | Answers 200 with twelve characters of text |

Only Benin's DGI handed over a 269-page PDF that could be read end to end, and
that pass found five wrong band boundaries, a wrong minimum-tax floor, a rate
given as flat when it is split, and a tax system described as using a mechanism
it does not use.

So the honest reading of the 65% is two things at once. Some of it is a corpus
that reached for the easy summary. Some of it is a jurisdiction whose law is
genuinely not machine-readable from outside the country, where PwC is the best
available source and saying so is the accurate thing to do. The two look
identical in the citation count, and this document has been treating them as one
number.

What separates them is not guessable from the corpus: it takes trying to fetch
the authority. `scripts/list-citation-rot.py` now records which hosts answer,
which refuse a script, and which are gone, and that is the beginning of telling
the two apart.

Note in passing, from two of those authorities' own front pages. Myanmar's IRD
carries a standing warning that fraudsters clone its site and states its official
URL to guard against it; Azerbaijan's State Tax Service prints "Official websites
of the Republic of Azerbaijan end with .gov.az" beside a list of trusted sites.
Both are the Benin problem seen from the other side, by the institutions it
happens to.

### When every number in a guide comes from one place

Three jurisdictions failed the same way, and it was the same shape each time: an
entire table of rates and thresholds resting on a single non-authority page.

| Jurisdiction | Source carrying the table | What was wrong |
|---|---|---|
| Benin | one HR-platform page | every IRPP band boundary, and band 4's rate |
| Zambia | one page on `zambiaprice.com` | unknowable — the domain now serves gambling SEO |
| Burundi | one HR-platform page | unknowable — `obr.bi` answers with a crash |

Benin is the one that makes the case. Those figures were not hedged and not
marked uncertain. They were simply wrong, and the shared source is the thing a
reader could have noticed *without knowing any Beninese tax law*.

`scripts/list-single-source-blocks.py` measures it: of the bullets in a guide
that state a number **and** carry a citation, what share point at one host.

The split matters more than the count. Concentration on a revenue service is a
guide doing it right. Concentration on PwC is weaker but honest, and is how much
of this corpus is necessarily built — see the section above on authorities that
cannot be read. Reported first is the Benin case, where the one host is neither.

```
other  38 guides    publisher  181    authority  79      (of 515 with 4+ facts)
```

`remotepeople.com` carries four of those 38 outright, `taxatlas.io` three,
`remotesolutionsafrica.com` two. The Benin fix shows up where it should: its two
guides moved out of `other` and into `authority`.

This is not a defect detector and never gates CI. A single-sourced guide is not
a wrong guide; it is one with no internal corroboration, which is a statement
about what a mistake would cost, not evidence that one was made.

### A total and its parts, asserted twice, in the shape nothing was reading

`check-total-rows.py` had found real errors — Sweden's 31.42%, Mexico's IMSS
Modalidad 40 understated by a quarter — by checking a table's Total row against
the rows above it. It read **tables**. The corpus's generated fact blocks are
bullet lists making exactly the same double assertion:

```
- **Total employer social-security contribution** - 27.4%
- **Employer - pension (first pillar)** - 16.6%
- **Employer - Fondiss** - 2.0%   ...
```

25.5% against a stated 27.4%, invisible because no pipe character appears
anywhere in it. Note the order is reversed from the table convention: the total
**leads** its components rather than closing them.

Thirteen bullet totals check out. Four do not, and all four are real: San Marino
(employer 27.4 vs 25.5 — the 1.9-point gap is exactly the unemployment figure, so
a branch is missing or double-counted; and employee 8.3 vs 8.4), the Central
African Republic (19% against the 4+11+2 its own bullet names as its parts) and
Mauritania (15% against 5+4+5+2).

None is resolvable from outside. `iss.sm` is genuinely the ISS and publishes
health services, not a contribution schedule. So each guide states the
contradiction and says explicitly **not** to adjust a branch to make the addition
work — which side is wrong is not determinable from the file.

#### Three false starts, which is the point

The first grouping rule flagged **45 of 61** groups, with "totals" of 100% and
86%. That is not a finding that the corpus is 74% wrong; it is the measuring
instrument failing. Requiring a shared topic word between the total and each
component cut it to 34 groups and 16 flags. Then two of those 16 were the
checker's own fault, and one was a shape it had no rule for:

- **Togo and Djibouti** are internally consistent (17.5 = 12.5+3+2). They were
  flagged only because the *employee* row was being summed into an *employer*
  total. A component naming the opposite side of the payroll now ends the group.
- **Gabon** sums exactly right and was flagged at 16% against 20.1%, because one
  branch reads `4.1% total (0.6% + 2% + 1.5%)`. Several percentages, so the run
  stopped short and reported the partial sum. A component whose value is not a
  single percentage now abandons the group outright: reporting nothing beats
  reporting a partial sum.
- **Belize's** two components each restate the 10% total rather than partition
  it, summing to double. Components that all equal the total are not a partition.

Final: 13 checked, 4 flagged, no false positives. Every step of that tightening
*removed* findings, and every removal was correct — which is the opposite of the
usual direction in this document and worth noticing.

#### The annotation that hid the defect it documented

The first version of the CAR and Mauritania notes put the explanation **inside**
the total bullet — "…listed below as 4% + 11% + 2% = 17%, not 19%". That added
more percentages to the bullet's value, so it stopped parsing as a total, and the
checker's own count fell silently from 4 to 2.

An annotation that documents a defect must not also hide it from the check that
found it. Both are blockquotes above the bullet now, and all four still report.

### A blind spot fixed, that turned out to be empty

`list-statute-links.py` required `skills/<tree>/<jurisdiction>/file.md` and so
never opened the **168 files that sit directly in a tree** — every US federal
guide, every cross-border guide, all the orchestrators. Same shape as the
trailer bug: for those files the queue was not low, it was uncomputed.

Fixed, and the honest result is that it found **nothing**. Zero rows in all 168.
The federal guides cite `[§1202](law.cornell.edu/uscode/text/26/1202)`, which
lands the reader on 26 U.S.C. §1202 itself — a citation doing its job.

Recording a fix that found nothing, because the alternative is leaving an
impression that it found something. It did surface one real false positive:
`law.cornell.edu` was top of the single-source queue at 52/62. Cornell's LII is
a Cornell Law School programme, not the official publisher — the OLRC publishes
the US Code — so it is a republisher, in ZambiaLII's position. But it
republishes the *section* rather than a summary of it, so it belongs with the
recognised publishers in both checkers, and flagging it would have been the
error.

### Togo: five guides, one PDF, and eleven figures that did not survive it

The single-source queue named `tg-income-tax.md` at 35/35 — every numeric fact
in the guide resting on one commercial summary site. Togo is a WAEMU state
sharing Benin's code structure, and unlike most of the queue its authority is
reachable: `www.otr.tg` serves the consolidated **Code Général des Impôts et
Livre des Procédures Fiscales, mis à jour 2025** as a 361-page PDF.

Read with `scripts/read-tax-pdf.py`, in both 1-column and 2-column modes so
that no figure was quoted unless the two passes agreed. Eleven figures across
five guides did not survive the reading:

| Guide said | The code says |
|---|---|
| IRPP band 1 taxed at 0.5% | **exonéré** (CGI art. 74) |
| band 2 at 7% | **3%** |
| band 3 at 15% to XOF 5,500,000 | **10%** to **6,000,000** |
| five bands, top rate from 15,000,000 | **eight** bands, 35% from **20,000,000** |
| "family quotient (parts)" | a fixed **XOF 10,000 per dependant per month**, capped at six, employment income only (arts. 72–73) |
| *(missing)* | a **28% standard deduction** on employment income up to XOF 10,000,000 (art. 26) |
| *(missing)* | business income is **off the scale at a flat 30%** (art. 78) |
| VAT reduced rate 10% | a **single rate of 18%**; the reduced-rate paragraph is *Abrogé* (art. 195) |
| VAT threshold XOF 60,000,000 | **XOF 100,000,000** (art. 177) |
| minimum tax "commonly cited XOF 3,000" | **MFP: 1% of turnover excl. VAT, floor XOF 20,000** (art. 120) |
| employer *taxe sur les salaires* 3% | **no such tax in the code**; only the vehicle tax and TETTIC are assimilated to direct taxes |
| registration duty on contributions 2% | formation and capital increases are **registered *gratis*** (art. 464(21)) |

Three of those deserve separate notes, because each is a different failure mode
and only one is "the summary was wrong".

**A real number, filed under the wrong tax.** XOF 60,000,000 is in the code —
art. 130, as the ceiling of the *taxe professionnelle unique* for individuals.
The VAT threshold is art. 177's 100,000,000. Same for the 2% registration duty:
art. 436 charges 2%, but on acts **extending a company's term**, and company
formation is on the *gratis* list. Both figures would survive a spot-check
against the statute by anyone who searched for the number rather than for the
rule — which is the search a reviewer under time pressure actually runs.

**Two books, one PDF, one article number.** The download binds the CGI and the
Livre des Procédures Fiscales together, each numbering its articles from 1. The
annual return deadline is **LPF art. 20**. CGI art. 20 is about benefits in
kind, and CGI art. 83 — which a search for the deadline surfaces — sits under
*Chapitre XIII : La Patente*, a different tax entirely. Every citation added
here names its book for that reason.

**The claim that was right, stated wrongly.** The guide gave the withholding
remittance deadline as "within 15 days of the end of the pay month". LPF art. 27
says *le 15 du mois suivant* — a fixed calendar date, not a rolling window. In
most months these coincide, which is exactly why the wrong form of the rule
survives: it is never visibly wrong. Two nearby articles use the same words for
other taxes (LPF art. 59 for TETTIC, art. 60 for VAT), and quoting either of
those would have "confirmed" the salary rule from a provision that has nothing
to do with salaries.

Also worth stating: the non-resident 20% withholding at LPF art. 98 is credited
against the year's tax and **is not refundable**. The guide called it a final
withholding. A non-refundable credit and a *libératoire* final tax behave the
same way in the common case and differently whenever there is other income —
the kind of distinction a summary flattens.

### And the checker called the revenue authority a commercial host

Rewriting the five guides moved every citation onto `www.otr.tg`. The
single-source queue then reported all five under its own heading: *"one host
carries the numbers, and it is neither an authority nor a recognised
publisher."* The host was the **Office Togolais des Recettes** — the body that
assesses and collects the taxes and publishes the code.

`otr.tg` is a bare ccTLD with no `gov` label, so the government-domain pattern
cannot see it, and the allowlist had never been asked about Togo. This is the
same error as `u.ae`, `belastingdienst.sr` and `andoz.tj` before it, and it
keeps recurring for the same structural reason: **the allowlist only learns
about an authority when somebody cites it**, so improving a jurisdiction's
sourcing is what exposes the gap, and the gap always reads as though the new
sourcing were worse.

Fixed by adding `otr.tg` with the test it satisfies, and by pinning three of
these bare-ccTLD authorities in the selftest so the class stops being
re-discovered one jurisdiction at a time. Secondary share **65% → 64%**
(2,697 authority against 4,768 secondary); hedged figures **845 → 837**.

The asymmetry recorded earlier in this document holds here in its sharpest
form. A missing allowlist entry over-reports risk, and the artefact it leaves —
a jurisdiction sitting on a queue somebody reads — is what eventually gets it
fixed. This one took a rewrite of five guides to surface. The entries that are
wrong in the other direction leave no artefact at all.

### The reader that said a document was empty when it had not read it

Chasing the same single-source queue into Cote d'Ivoire, `scripts/read-tax-pdf.py`
was pointed at the *annexe fiscale* to the 2025 budget law. It printed one blank
line and exited 0.

That is not "the document contains no text". Every page in that file declares
its content as `/Contents [672 0 R]` -- a one-element **array** -- and the
reader's regex matched only the bare `/Contents 672 0 R` form. It found 150
pages, extracted none of them, and reported the result as though it had looked.
An hour later the same output would have read as evidence that Cote d'Ivoire
publishes nothing useful.

Three fixes, and the second matters more than the first:

1. Accept the array form, joining the parts before tokenising (a split
   `/Contents` is one stream cut at an arbitrary byte, so the pieces cannot be
   tokenised separately).
2. **Exit non-zero with a diagnostic when no page yields content**, naming how
   many objects were seen and how many were marked `/Type /Page`, and saying in
   terms that the document was not read. A tool that cannot read something must
   say so rather than return nothing.
3. Report the observed `/MediaBox` width when it disagrees with the
   `PAGE_WIDTH` argument. Passing the wrong width silently drops everything
   past the first column band -- another way to get a confident empty answer.

The Togo extraction is byte-identical after the change, which is the only
evidence that the fix is a fix and not a rewrite.

Two limits stay, and both are now visible rather than silent. Pages come out in
object order, not reading order, so the 2025 annexe interleaves pages 33-39;
the page footers make the true order recoverable. And the annexe's subset fonts
carry no usable `/ToUnicode`, so accented Latin letters map wrongly
(`p`->`e-acute`, `j`->`a-grave`, `r`->`e-circumflex`). **Digits, punctuation and
article numbers come through intact**, which is what made the figures below
quotable; the French prose around them had to be read through the substitution.

### Cote d'Ivoire: the same levy, counted at two levels of the same tax

`ivory-coast-payroll.md` is one of the better-built guides in this corpus. It
computes cumulative tax at each band, marks ten open research gaps by section,
and carries a step-by-step computation order. Its step 7 charges the employer
2.8% (local) or 12% (expatriate) of gross. Its step 8 then charges 1.6% for the
FDFP training levies -- 0.4% apprenticeship plus 1.2% continuing training.

Article 16 of the *annexe fiscale* to Loi de Finances n deg 2024-1109 du 18
decembre 2024 re-presents the table at CGI art. 146 as four components:

| Component | Local | Expatriate |
|---|---|---|
| Contribution employeur proprement dite | -- | 9.2% |
| Contribution nationale pour le developpement economique, culturel et social | 1.2% | 1.2% |
| Taxe d'apprentissage | 0.4% | 0.4% |
| Taxe additionnelle pour la formation professionnelle continue | 1.2% | 1.2% |
| **Total** | **2.8%** | **12%** |

1.2 + 0.4 + 1.2 = 2.8. 9.2 + 1.2 + 0.4 + 1.2 = 12.0. Both columns close
exactly, which is what settles it: there is no room inside 2.8% for a further
1.6%. The guide charged a local employer 4.4% where the statute charges 2.8% --
**a 57% overstatement**, carried into all six worked examples, the spreadsheet
template, and a Tier 1 rule that told the reader never to omit the second
charge.

The arithmetic mattered here for a second reason. The table extracted with its
columns scrambled: the header row read "Personnel expatrie | Budget
beneficiaire | Personnel local" while the data rows ran the other way. Rather
than trust the header, the assignment was settled by which column each set of
components sums to. That is the guard the reader's own docstring asks for,
applied to a case where the layout was actively misleading.

**Why the error was invisible.** Nothing in the guide contradicted anything else
in it, and no checker in this repo could see it: the two figures are correct
individually, sit in different sections, and cite different sources -- PwC for
the 2.8%/12%, the FDFP's own site for the 1.6%. Both sources are right about
their half. PwC describes the employer contribution and does not mention the
training levies; the FDFP says it *manages* the two levies and does not say who
collects them or inside what. Neither is wrong. The error lives in the join,
and only the statute shows the join.

That is the general shape: **a summary describes one level of a tax, and
another summary describes a component of it, and adding them double-counts.**
It survives cross-checking two sources against each other, because each is
faithful to what it covers.

**Three more findings from the same document**, all things the guide either
hedged or lacked:

- **The 20% professional abatement is abolished.** The guide assumed this from
  PwC and marked it an open research gap. Art. 16 says it in terms: Ordonnance
  n deg 2023-719 *supprime* it and the base is now gross taxable income. Gap
  closed against the statute -- and the same article explains why the employer
  totals did not move: the component rates were re-set so that 2.8% and 12%
  are maintained on the now-unabated base.
- **Dockers and transit dockers pay a flat 1.5%**, off the progressive scale
  entirely (new CGI art. 120 bis). Applying the barème to a docker overstates
  the tax.
- **CGI art. 263 is repealed** and the taxe d'apprentissage was cut from 0.50%
  to 0.40% (CGI art. 143). The guide's 0.4% was right, sourced to a portal.

And the classifier repeated its Togo trick one commit later: citing `dgbf.ci`,
the Ivorian Ministry of Finance directorate that publishes the enacted annexe,
moved Cote d'Ivoire off the single-source queue and the corpus's secondary
count **up** by seven. Bare ccTLD, no `gov` label, invisible to the pattern.
Twice in one session, both francophone African ministries: added, with the
comment saying so, because the next one will arrive the same way.

---

## The same checker, tried a second time, discarded a second time

An outside review of PR #16 returned fourteen bugs, and **five were one defect**:
a figure corrected in one place and left standing in another. Paraguay's decreed
minimum wage against a prohibitions section still calling it unconfirmed; the
UK's enacted Scottish bands against a section still saying to use last year's;
Uruguay's 14% deduction credit against a working paper still offering 10%;
Liechtenstein's 2026 rates in a 2025 guide; Nigeria's education tax charged
beside the levy that replaced it.

This is the defect class the section above records a discarded checker for. The
review is independent evidence that the class is real, common, and not caught by
anything here.

### Reviewing for the defect, and committing it

Six of the seven were already fixed. The seventh, Nigeria, was recorded in a
pull-request comment as **"Fixed. 'There is no medium-company 20% band from 1
January 2026'"** — and it was not. That quotation is real and the rate bullet
was correct. What the check missed is that the correction's *consequences* were
still standing three sections away:

- a `CIT — large company` band at turnover > NGN 50B, in the bullet **directly
  after** the one saying NTA 2025 has two bands and no third;
- Plc obligations and the mandatory-filings list both charging tertiary
  education tax beside the 4% development levy that replaced it under s.59 —
  ten lines below a bullet already saying "do not add 3% tertiary education
  tax";
- a comparison table offering small companies an "education tax exempt" that is
  not a separate exemption to claim.

The check asked *did someone write the correction* and answered yes. The defect
is *did the correction reach everything it contradicts*. **Reviewing for this
class while committing it** is the most direct evidence available that it is
hard for a person, which is what makes automating it attractive — and the rest
of this section is why that remains unearned.

NGN 50 billion is real, and belongs to a different charge: the domestic turnover
limb of the 15% Minimum Effective Tax Rate in s.57(2)(b), which tops an
effective rate up rather than setting a CIT rate. Togo's XOF 60,000,000 again —
a real number filed under the wrong tax survives a spot-check, because anyone
searching for the number finds it.

### The second attempt, and what was new about it

The first attempt seeded from **denial sentences**. This one seeded from
**authorial retirement notes** — "previously stated 10%", "the earlier figure of
about 10.6%", "the old EGP 500,000 figure is superseded" — a narrower class,
because a denial is something a guide writes constantly and a retirement note is
something an author writes deliberately.

It also had a discriminator the first attempt lacked, and this one is worth
keeping even though the script is not:

> **A line carrying both the retired value and its replacement is a before/after
> statement, not a stale copy.** "The pension rate doubled from 6% to 12%",
> "EUR 550.66/month to 31 Jul; EUR 620.20 from 1 Aug". A genuinely stale copy
> carries the old value **alone** — that is what makes it stale.

That single rule removed Rwanda, Bulgaria and the US 1099-K guide from the top
of the output, where all three had filled it with lines that state their change
correctly.

### It found two real defects

**Sri Lanka's capital gains guide** — Tier 1, accountant-reviewed, marked
current — put its headline rate at 10% when no taxpayer it names pays 10%. Act
No. 11 of 2026, enacted 3 June 2026, is recorded three bullets below:
individuals and partnerships 15%, trusts and unit trusts and mutual funds and
NGOs 30%, companies 30% at the CIT rate. Every class covered, none left at 10%.
Reading the first rate bullet understates an individual by a third and a trust
by two thirds. The same file called the CSE withholding 10% in one bullet and
"now 15% post-amendment" in another — not settleable from the file, since a
withholding rate need not track the final rate it collects against, so it is
recorded as a gap naming both readings.

And Nigeria, above. Both fixes stand on their own evidence — the statute, and
the file's own other bullets — not on the script.

### And it was discarded anyway

Three tokeniser and regex defects, each found only by reading the output:

| defect | what it did |
| --- | --- |
| `band` matched inside the compound *four-band* | retired 0%, 8% and 10% from Kosovo's **current** schedule — 25 false hits, ranked first |
| the adjective-to-noun gap crossed a comma | bound "the **prior** year, the **floor**" and retired $1,000 and 50%, California's correct prepayment rule |
| any three-letter uppercase prefix read as a currency | **`ASC 805` became an amount**, and the US GAAP business-combinations guide arrived at the top with 53 false hits, because the standard's own number is on every line of it |

And three mutually incompatible rankings in one sitting, volume swinging
**60 → 29 → 94** files as each replaced the last. The middle one halved the
output and killed a true positive. Each new ranking broke a selftest written to
pin the previous one — which is the honest signal that the design was being
changed faster than it was being understood.

**Precision was never measured on a random sample.** Under every ranking that
was sampled, the top of the corpus-wide output was dominated by false positives
of a new kind. That is the bar the first attempt was discarded against —
*each tightening cut the volume and none of them improved precision* — and
applying a softer bar to the second attempt because it is newer would be the
double standard the rest of this document exists to avoid.

### Two lessons that cost more than they should have

**The sub-lesson recorded above was rediscovered, not remembered.** This
document already said, in the first attempt's write-up, that *a denial
sentence's figures split by which side of the marker they sit on*. The second
attempt assumed the retired value always **follows** the trigger, failed two
real cases, and relearned the rule from a failing selftest. It was written down,
in prose, in the right file — and prose in a methodology document did not stop
it being re-derived the hard way. A lesson lives where it executes: in a
selftest, not in a paragraph.

**A claim was published from a case that had already been fixed.** The second
attempt replaced distance-based ranking with subject-based ranking, and the
change was written up — in this document and in a pull-request description — as
a measured lesson: *"a stale copy is missed BECAUSE it is far from the note, so
proximity cannot be the evidence."* It is not supported. The Uruguay guide it
was measured against had already been repaired at the commit examined, so the
"false positives" it was tuned away from were the only thing left in the file.
Distance ranking is what surfaced Sri Lanka's stale headline; subject ranking
demoted it and promoted the two **correct** bullets in its place, because they
share "amendment" and "enactment" with the note and the stale line shares
nothing. **A stale copy is stale precisely because nobody rewrote it to match
the note, so requiring it to echo the note's wording selects against the thing
being looked for.**

Both errors have the same root as the defect class itself: something was
established in one place and its consequences were not carried to the others.

### What is actually left

The human control, unchanged and now twice-earned: **when a correction
contradicts something the guide already says, search the file for the number
before writing the new row, and again after** — and then check what the
corrected figure *implies* elsewhere, not merely whether the correction is
present. The Nigeria review above failed the second half of that sentence, which
is why it is now in it.

The replacement-value rule in the box above is the one mechanical piece worth
carrying into any third attempt. It is not enough on its own.

---

## Guinea-Bissau: a guide filed under a tax the country does not have

`gw-income-tax.md` sat at the very top of the single-source queue — **10 of 10**
numeric facts on one HR blog, every band marked "(approx — confirm)". It was
titled "Personal income tax (IRPS)" and cited an "Imposto sobre o Rendimento das
Pessoas Singulares (IRPS) statute" nine times.

Guinea-Bissau has no IRPS. The word appears **nowhere** in the tax authority's
own consolidated legislation. Income from work is taxed by the **Imposto
Profissional**, Código approved by Decreto nº 23/83 de 6 de Agosto; business
profit by the **Contribuição Industrial**; sales by the **IGV**. IRPS is the
Cabo Verde, Mozambique and São Tomé name, applied here by analogy — the same
shape as Kosovo citing its accreditation statute as its income tax law, and
harder to see, because the invented name is a real tax somewhere else.

### The bands were right, and almost nothing around them was

The nine bands and their rates — 1 / 6 / 8 / 10 / 12 / 14 / 16 / 18 / 20 per
cent — match art. 27º nº 1 exactly, as worded by Lei nº 1/2021 art. 10º. The
commercial source got them right, which is worth stating plainly: concentration
is exposure, not error. What it did not carry:

- **That the rates are marginal.** Art. 27º nº 3 says the percentages
  *"representam **taxas marginais**"* and art. 28º repeats it. The guide gave
  nine bare bands and no application rule. Applying 20% to a whole salary
  overstates the tax several times over.
- **A second schedule entirely.** Art. 27º nº 2 puts the self-employed and
  holders of copyright income on three bands — 10 / 20 / 25 — starting at 10%
  where an employee starts at 1%. The guide presented the employee table as *the*
  personal income tax.
- Occasional income at 10% (nº 4); pensions of XOF 200,000/month or less exempt;
  employer remittance within **10 days** of month end (art. 29º), where the guide
  gave no remittance deadline at all; the XOF 2,000 de minimis on assessment.

And the hedge the guide flagged against itself — *"some sources cite a 0% first
band"* — is settled: there is no 0% band, 1% applies from the first franc.

### Nine article numbers were wrong before they were checked

The first draft of the rewrite cited arts. 4º, 22º, 25º-A, 26º and 32º from
context — the shape of where such provisions usually sit. Resolving each against
the nearest preceding heading in the consolidated text gave arts. **1º, 2º, 13º,
31º-A and 37º**. Only art. 18º was right by guess. This is the Togo lesson
arriving in a new costume: there, two books bound in one PDF each numbered from
1; here, plausible article numbers written from habit. **A citation is a claim,
and the cost of checking it is one search.**

### The arithmetic found a defect in the statute

The schedule ships a *parcela a abater* — the amount subtracted from rate ×
income, the standard lusophone shortcut for a marginal computation. Testing it
at all eight band boundaries, it reproduces the marginal result exactly at seven.
At the fifth-to-sixth it does not:

| | monthly | annual |
| --- | ---: | ---: |
| band 5 at its top (12%, parcela 13,917 / 167,004) | 34,143 | 409,716 |
| band 6 at its start at the **current 14%** (parcela 37,947 / 455,364) | **18,123** | **217,478** |
| band 6 at its start at the **superseded 18%** | 34,143 | 409,718 |

The parcela is continuous **at 18%** — the rate the band carried under Lei nº
8/2020 — and not at the 14% substituted by Lei nº 1/2021. On its face the rate
was cut and the parcela derived for the old rate was left behind, so applying
the published figure literally makes tax **fall by 16,020 a month** as income
rises through XOF 400,501.

That is the Côte d'Ivoire lesson generalised. There, arithmetic settled which
column was which when a table extracted scrambled. Here it found something no
reading would: **the schedule is internally consistent everywhere except at the
one boundary an amending law moved.** It is recorded as a research gap naming
both methods, not "corrected" to the 21,927 that continuity would require —
that is a value the arithmetic implies, not one the statute states, and writing
it in would be inventing law to make a sum close.

### The classifier gap, predicted and then observed

The comment beside `dgbf.ci` in `list-source-mix.py` ended: *"the next one will
arrive the same way."* It did, on the next jurisdiction opened. `mef.gw`,
`dgci.mef.gw` and `kontaktu.mef.gw` — a finance ministry, its tax directorate,
and the portal serving the consolidated codes with superseded wording struck
through — all classified as commercial. Bare ccTLD, no `gov` label.

One thing was different this time, and it is the point of writing predictions
down: the allowlist entry went in **with** the citation change rather than after
it. Togo and Côte d'Ivoire each pushed the corpus's secondary count *up* by
citing their own revenue authority, and the fix trailed the finding by a commit.
Guinea-Bissau did not: authority citations rose 2,705 → 2,724 and secondary fell
4,767 → 4,757 in the same change. The shape is a bare ccTLD, not a language —
Togo and Côte d'Ivoire were francophone, this one is lusophone.

### The same jurisdiction's VAT guide: every figure right, and the tax half-described

`gw-vat-gst.md` was the next guide on the queue — **9 of 9** facts on one
commercial host. Unlike the income-tax guide, its framing was correct and so was
every number: 19% standard, 10% reduced, 0% exports, thresholds of FCFA
40,000,000 and 10,000,000. All confirmed against arts. 18.º, 37.º and 38.º of the
Código do IVA (Lei nº 4/2022, Boletim Oficial nº 8, 4th supplement, 25 February
2022). **Concentration is exposure, not error**, and this is the second guide in
one jurisdiction to prove it.

What a rate table cannot tell you is how the tax operates, and that is what was
missing:

- **The simplified regime is a turnover tax, not a reduced VAT.** 5% of the value
  of supplies with **no input deduction at all**, and its invoices give the buyer
  **no right of deduction**, which the invoice must say (arts. 38.º nos 2–3,
  39.º). The guide called it "a simplified VAT scheme".
- **A domestic withholding with no trace in the guide.** A normal-regime buyer
  must withhold **the entire IVA** charged on an invoice from a simplified-regime
  supplier, or from a normal-regime supplier the director-general has designated
  a *contribuinte de risco* (art. 7.º nº 3). A buyer who pays such an invoice
  gross has underpaid the state.
- **Non-residents must appoint a fiscal representative**, who is the debtor for
  the tax and must be named to the counterparty *before* the operation, with the
  represented person jointly and severally liable (art. 33.º).
- **Filing**: normal regime monthly by the **15th**, nil returns mandatory
  (art. 31.º); simplified regime **quarterly**, last working day of April, July,
  October and January (art. 42.º). The guide had "monthly ((approx — confirm))"
  and nothing at all for the simplified regime — right for one regime, silent for
  the other.
- **A 30% flat surcharge** on imports by anyone on the monthly list of IVA
  non-declarants (Lei nº 4/2022 art. 6.º).
- Below FCFA 10,000,000 a person is exempt from IVA **and** subject to a single
  small-taxpayer tax *"em termos a fixar por lei"* (art. 45.º) — not simply
  outside the system.

Two smaller things the reading settled. The IGV it replaced also stood at 19%, so
the guide's "replaced the former 19% general sales tax" was right — but the IGV
carried a **15% band on electricity and water** that the IVA does not, so it is
not a like-for-like swap. And the Code's own art. 37.º nº 6 points to *"o regime
de pequenos contribuintes previstos no artigo 46º"* when that regime is art. 45.º
and art. 46.º is *Garantias* — recorded as a gap against the Boletim Oficial
text rather than silently renumbered.

**The citation discipline held better the second time, and still not well
enough.** Writing the guide, seven article numbers were again put down from
context; resolving each against the nearest heading corrected **three** — the
partial-deduction rule is art. 23.º not 27.º, taxpayer-initiated payment is
art. 25.º not 29.º, administration-initiated payment art. 26.º not 30.º — and one
number I could not confirm was softened rather than asserted. Three wrong out of
seven, against eight out of nine an hour earlier, because this time some headings
had been read directly rather than inferred. The rule that works is not "be more
careful"; it is **resolve every article number mechanically before writing it
down**.

Guinea-Bissau's secondary share moved the corpus across a boundary: authority
citations 2,724 → **2,746**, secondary 4,757 → **4,750**, and the corpus's
secondary share from 64% to **63%**. Only `gw-payroll-social.md` is left on the
single-source queue for this jurisdiction.

---

## Myanmar: the bands were right and three whole charges were missing

`mm-income-tax.md` sat on the single-source queue at **11 of 14** on
`taxatlas.io`, citing "Union Taxation Law 2025" for every band while linking to a
commercial summary. The Internal Revenue Department publishes its own statement
of that law, in Burmese, citing it **section by section**.

**All fourteen figures survived.** The six bands (0/5/10/15/20/25 with
thresholds at 2m, 10m, 30m, 50m, 70m), the four s.6 reliefs (20% capped at
10,000,000; spouse 1,000,000; child 500,000; parent 1,000,000) and the
MMK 4,800,000 salary exemption all match, and are now cited to UTL 2025
ss.19(c), 19(a) and Income Tax Law s.6 rather than to a summary. That is the
third guide in two jurisdictions where the commercial source got the numbers
right — **concentration is exposure, not error**, and the value of reading the
statute is rarely that the headline rate is wrong.

The value is what a rate table cannot contain. Three charges were absent
entirely:

- **Capital gains at 10%** (s.27(b)), **exempt where the total does not exceed
  MMK 10,000,000** (s.28), return due **within 30 days** of the sale. A
  non-resident foreigner pays in the currency the proceeds were received in.
- **Rental income is taxed separately at 10%** after the s.6 reliefs — not on the
  progressive scale. A reader applying §1's bands to rent computes the wrong
  number, and commercial tax at 5% arrives on top once gross rent passes
  MMK 50,000,000 (ss.14(e), 15(b)).
- **A second rate scale, 3 / 5 / 10 / 15 / 30 per cent**, for income whose source
  cannot be shown when buying or building immovable property, a vehicle, a vessel
  or shares (s.25). Its bands run from MMK 300,000,000 to MMK 3,000,000,000 — two
  orders of magnitude above the ordinary ones, which is exactly why nobody
  transcribing a "personal income tax rates" table would notice it is missing.

One hedge was also settled rather than carried: the guide said non-residents were
on the same bands "(approx — confirm; some guides cite a 25% flat treatment in
earlier years)". The IRD states it plainly — same bands, **no reliefs** (s.24).
The rate was never the difference.

### Reading a source in a script you cannot read

The IRD page is Burmese, and its numerals are Burmese too (၀၁၂၃၄၅၆၇၈၉). Figures
were transliterated digit-by-digit before use, and the unit ***သိန်း*** (*lakh*,
100,000) applied — "ကျပ်သိန်း ၁၀၀" is MMK 10,000,000, not 100. Getting that unit
wrong in either direction is a hundred-fold error, and it is the kind a reader
who does not know the script cannot catch by eye. The cross-check that made it
safe was that every transliterated figure had to match the guide's existing
number, which came from an independent English source; where the two agreed, the
reading was sound. **A source in an unfamiliar script is usable, but only with an
independent check on the arithmetic, not on the words.**

### The leak was checked for this time

Guinea-Bissau's correction leaked into three sibling guides because nothing was
grepped. Here the jurisdiction was searched for the same figures **before**
committing: `mm-tax-overview.md` carried "Progressive 0% to 25%" and a bare
"Capital gains tax 10%", both sourced to PwC. Both were repointed at the statute
and given what the headline hides — that "0% to 25%" is not the whole scale, and
that the 10% gain is exempt below MMK 10,000,000. Two commits earlier that would
have been found a day later by an outside reviewer.

Corpus effect: authority citations 2,750 → **2,765**, secondary 4,747 →
**4,733**. Both `mm-income-tax.md` and `mm-tax-overview.md` are off the
single-source queue; `mm-company-formation.md` (8/10 on a law firm) remains.

> **Two corrections to the paragraph above, and both are the defect this
> document is about.** It first read "2,763 / 4,735" and "`mm-tax-overview.md`
> remains" — the citation pair carried forward from the previous measurement
> rather than re-run, and the queue membership asserted from memory of what had
> been on it rather than from the listing. Re-running `list-source-mix.py` gives
> 2,765 / 4,733, three times in a row; re-running `list-single-source-blocks.py`
> shows Myanmar's overview gone from the queue, because repointing its two
> headline figures at the statute is exactly what takes a guide off it. **Two
> citations and one filename is not a material error. Needing the re-run to find
> out is the point** — a derived number written into prose is a copy, and this
> file's whole argument is that copies go stale silently.

## Armenia, again: the second reviewer finding that was wrong

An outside review of PR #18 raised ten findings. Eight were already fixed at
head. One was a real leak (below). One was **wrong, and its recommended fix
would have broken a correct rule** — the second time in this branch that has
happened, and on the very article the near-miss section above is about.

The finding said the micro-business regime charges **AMD 5,000 of income tax per
employee**, not ordinary withholding, citing a law firm's page that says exactly
that. The guide says the opposite. The guide is right:

- **Art. 269(2)(2)** — the micro exemption does not reach "the obligation to
  compute and pay income tax **in the manner established by the Code**
  (*Օրենսգրքով սահմանված կարգով*) on taxable amounts paid to individuals who are
  not individual entrepreneurs or notaries". *In the manner established by the
  Code* is the ordinary rule. It names no rate and no per-head amount.
- **Art. 125(3)** — where the AMD 5,000 actually lives — charges individual
  entrepreneurs **in the turnover-tax system** (Chapter 55, not the micro
  chapter) **profit tax** (*շահութահարկ*, not *եկամտային հարկ*) of "five
  thousand drams per month, **regardless of the number of activity types**",
  and makes it their **final** profit-tax liability. Per entrepreneur, per
  month, for their own profit tax. Not per employee, not income tax, not micro.
- **Art. 270(2)** has micro-business subjects file the ordinary art. 156(1)
  income-tax calculation monthly — which is what ordinary withholding requires.
- **Art. 271**, "Payment of taxes and fees by micro-business subjects", is
  **repealed** (ՀՕ-450-Ն, 24 November 2022). Searching the Code for any amount
  attached to the micro provisions returns nothing.

So the secondary source is describing a regime that was repealed at the end of
2022, and the two AMD 5,000 charges — one real, one abolished — are close enough
to swap without anyone noticing. That is the same shape as the art. 125(3.1)
near-miss recorded above, where 18% was right for the article's first part and
23% for a subparagraph three down. **Both times the guide was already correct and
the proposed fix would have broken it.** Both times what settled it was opening
the Code and reading the whole article, including which tax the article is about.

One further note on that finding's evidence. It also said the guide contradicted
itself — that §5.10 still carried the per-employee treatment. At the commit it
reviewed that may have held; at head it does not. §5.10, the rate table, the
reviewer checklist and the prohibitions list all say the same thing. **A review
runs against a commit, not against your branch**, and a finding whose evidence is
an in-file contradiction is the kind most likely to have been overtaken.

### And one that was right, where the reviewer named one file and three were wrong

The same review found that Pakistan's Finance Act correction — read every "verify
against FA 2025" marker as naming the Act in force for the year being computed —
had been written into four `skills/` guides and into `agent-skills/pk-income-tax`,
but not into `agent-skills/pk-freelance-intake`. It was right, and the source
guide **said so in its own text**: a trailing note recorded that the counterpart
"has not been updated here". Writing down that a correction has not propagated is
not the same as propagating it.

Grepping the tree for the stale markers rather than fixing the file named found
**three**, not one: `pk-freelance-intake`, `pk-formation` and `pk-return-assembly`
all still told a reader to verify a current-year computation against FA 2025. All
three now carry the block. `agent-skills/` inherits nothing from `skills/` — it is
hand-maintained — so every correction that touches a jurisdiction with an
`agent-skills/` counterpart has to be written twice, and the grep is the only
thing that catches the second one.

## Vietnam: the guide named a ministry that had been abolished

The single-source queue put `vn-company-formation.md` near the top — 11 of its 12
citations went to one commercial host, with the underlying laws named but not
read. Vietnam is not a thin jurisdiction where nobody has checked; it is one of
the most-read pages in the corpus. That is what made it worth opening.

Three of its statements had stopped being true, and one whole regime was missing.

**The registration authority.** The guide said the Enterprise Registration
Certificate is "issued by the provincial Department of Planning and Investment".
The Ministry of Planning and Investment was merged into the Ministry of Finance
in 2025 and the provincial departments went with it. Decree 168/2025/NĐ-CP art.
20(1) puts the Business Registration Authority in the **Sở Tài chính**, the
Department of Finance. The National Business Registration Portal settles it
without needing the decree at all: its own footer reads *"Bản quyền thuộc Bộ Tài
chính"*. A reader following the old guide is looking for a building that is not
there.

**The annual business licence fee.** The guide listed the *lệ phí môn bài* at
"VND 1,000,000 to VND 3,000,000 per year based on registered charter capital" as
a live recurring cost. Resolution 198/2025/QH15 art. 10(7) is one sentence long:
*"Chấm dứt việc thu, nộp lệ phí môn bài từ ngày 01 tháng 01 năm 2026."* The
charge ended, and with it the declaration. The band description was also wrong on
its own terms — VND 1,000,000 was never a charter-capital band, it was the rate
for branches, representative offices and business locations.

**The 90-day capital rule.** Correct as far as it went, and it did not go far
enough: art. 47(2) excludes the time spent transporting or importing contributed
assets and completing ownership-transfer formalities. For a contribution in cash
the guide was right; for imported plant or real property it understated the
deadline.

**The regime that was missing.** Law No. 76/2025/QH15, in force 1 July 2025,
built a beneficial-owner register into Vietnamese company law: a definition
(art. 4(35)), a standing duty to collect and update (art. 8(5a)), a dossier item
for every company form (arts. 20–22), required fields down to ethnicity and
gender (art. 25(5)), notifiable changes (art. 31(1)(c)), anti-money-laundering
access (art. 33(1a)) and five-year retention past dissolution (art. 216(1)(h)).
The guide had no trace of any of it. Its transitional rule is the practical
point: a company registered before 1 July 2025 files the information at its
**next** registration change, so the obligation arrives silently, attached to
whatever routine filing comes first.

### What the fetching cost, and why it is worth writing down

Three of the four government hosts holding the primary texts were awkward in a
different way, and the workarounds are reusable:

- **The relay closes long transfers mid-flight.** A 626 KB `.doc` arrived in
  four truncated pieces. Resuming with `curl -C -` finished it — and *corrupted*
  it, because the server ignores `Range` and restarts from zero, so the resumed
  bytes appended a second copy. The file that ended up 650 KB against an
  expected 627 KB was the tell. A single unresumed request with a long timeout
  is the fix; a resumed file that is *larger* than expected is never complete.
- **Signed PDFs are scans.** `datafiles.chinhphu.vn` serves the official signed
  text of both the Law on Enterprises 2020 and Decree 362/2025 — as images.
  4.4 MB in, 70 characters of text out. The gazette's own DOCX would have
  answered, but its CDN host is not in the TLS bundle.
- **`vbpl.vn`, the Ministry of Justice's national legal database, returns 403 to
  everything**, root and file paths alike. So does `ssa.gov`, which matters
  beyond Vietnam: `gw-payroll-social.md` cites the SSA's *Social Security
  Programs Throughout the World* for Guinea-Bissau's contribution ceiling, and
  that citation cannot be checked from this network at all.

The consequence is recorded in the guide rather than hidden: arts. 46(1) and
47(2) were read in an English translation, not in Vietnamese, and arts. 111(1),
113(1) and 188 were not re-read at all. They stay marked, with a research gap
naming exactly which articles a reviewer still has to confirm. **Getting three
things right and saying plainly which fourth thing you could not reach beats
quietly promoting all four.**

Corpus effect, re-measured rather than carried forward: authority citations
2,765 → **2,787**, secondary 4,733 → **4,728**. `vn-company-formation.md` is off
the single-source queue; `vn-tax-overview.md` and `vn-payroll-social.md` remain
on it, both concentrated on PwC, which is a recognised publisher rather than an
unknown one.

## San Marino: the file said its own totals were wrong, and it was right

`sm-payroll-social.md` was the worst concentration on the single-source queue —
**11 of 11** numeric facts on one HR platform. It also carried an unusually good
note, written by an earlier pass: the stated employer total of 27.4% did not
equal its own components (16.6 + 2.0 + 1.9 + 4.0 + 1.0 = 25.5), the employee
total of 8.3% did not equal its components either, and the note said plainly
**"do not reconcile these by adjusting a component to make the arithmetic
work"**, because which number was wrong could not be determined from the file.

That instruction was correct, and following it is what made the finding
possible. The cause is not a typo in any component. **San Marino legislated a
seven-year ramp**, so there is no single current rate to reconcile to. Legge 29
novembre 2022 n.157 art. 21(4) prints the whole progression:

| Primo pilastro | 2023 | 2024 | 2025 | 2026 | 2027–2029 |
| --- | ---: | ---: | ---: | ---: | ---: |
| employee | 5.90% | 6.40% | 6.90% | 6.90% | 6.90% |
| employer | 16.60% | 17.10% | 17.60% | 17.60% | 17.60% |

The guide's 5.90% and 16.60% are the **2023 column**. Both had moved twice by
2025. FONDISS, the mandatory second pillar, is flat at 2.00% each side through
2025 and then rises from 1 January 2026 — to 2.50% each side, and on to 4.00%
employee against 3.00% employer by 2029, so the two sides stop being equal.

**The clean demonstration is the employee total.** At 2025 rates the two pillars
alone are 6.90 + 2.00 = **8.90%**, against a stated total of "approximately
8.3%" — the total is smaller than the sum of two of its own components, before
any unemployment or family-allowance contribution is added. In 2026 the pillars
are 9.40%. That is not rounding, and no adjustment to a component could have
produced it: the components and the total were describing **different years**.

So the guide now prints the statutory table in full, 2023 to 2029, rather than
picking a year and calling it current. A rate that is legislated to change every
January is a table, and flattening it to one number guarantees the guide is
wrong for six years out of seven.

### Checking that the table had not itself been superseded

Quoting a 2022 rate schedule in 2026 is precisely the defect this document is
about, so before the table was copied, two instruments that amend Legge 157/2022
were opened and read against art. 21. The **errata corrige** of 1 December 2022
substitutes one office's name and nothing else. **Decreto Delegato 28 marzo 2024
n.76** abrogates art. 23(4), replaces art. 27 and reduces the art. 31 rate for
working pensioners to 25% split 18/7 — and leaves art. 21 and its progression
intact. **Two negative results are worth as much as the table**, and both are
recorded in the guide so the next reader does not have to repeat them.

### What could not be read, and the shape of the obstacle

The remaining branches — unemployment, health and accident, the Social Services
Fund — are not in Legge 157/2022. The ISS, which collects them, publishes an
annual circular that sets them. Every ISS circular fetched for this pass is a
**scanned PDF with no text layer**: the 2026 one is 2.2 MB and yields eight
characters. No OCR was available. So those four figures stay on the commercial
source, marked, and **the guide now states no employer or employee total at
all** — because stating one would mean adding statutory figures to unverified
ones and presenting the sum as a single number, which is exactly how the
totals came to disagree with their components in the first place. Refusing to
state a total is the honest output when half the addends are unknown.

Two things the statute gave that a rate table could not: art. 21(2) cuts the
employer's Fondo malattie contribution by **0.40%** from 2023 and the Fondo
Assegni Familiari by **0.60%** from 2024, so any pre-2023 figure for those
branches is too high — which bears directly on the four unverified numbers. And
art. 22(3) zeroes artisans' family-allowance contribution from 2029 **while
abolishing the family-allowance and short-sickness entitlements for that
category**: a benefit change disguised as a rate change, invisible to anyone
reading only percentages.

### The bare-ccTLD gap, fourth occurrence — and checked before citing

`iss.sm`, `consigliograndeegenerale.sm` and `bollettinoufficiale.sm` all
classified as commercial, the same shape as `otr.tg`, `dgbf.ci` and `mef.gw`
before them: a bare country-code TLD with no `gov` label. This time the
allowlist entries went in **before** the citations rather than after, so the
secondary count never rose. `gov.sm` already passed, on the label.

The entries carry a warning for the next reader, because San Marino is the one
jurisdiction where this list has already been wrong in the other direction:
`startup.sm` ("© San Marino Management Srl") and `camcom.sm` (mixed
public-private capital) were **removed** from it by an earlier pass. Both
removals were right. The test is not the `.sm` suffix — it is whether the body
collects the charge or publishes the law. The Istituto per la Sicurezza Sociale
collects it; the Consiglio Grande e Generale enacts it; the Bollettino Ufficiale
publishes it. All three are pinned in the selftest **alongside** assertions that
`startup.sm` and `camcom.sm` stay out, so a future pass cannot widen the rule to
the whole TLD without a test failing.

Corpus effect, re-measured: authority citations 2,787 → **2,797**, secondary
4,728 → **4,722**. San Marino goes from 0 authority citations to **11**.
`sm-payroll-social.md` is off the single-source queue; `sm-vat-gst.md` remains on
it at 6/6.

## San Marino again: the framing was right, the tax was half-described, and the citations pointed at a law that does not set the rates

`sm-vat-gst.md` was the jurisdiction's second entry on the single-source queue,
**6 of 6** on one commercial blog. Its headline claim was correct — San Marino
has no VAT, it has the *imposta monofase*, a tax charged once on entry into the
territory — and neither Legge 157/2022 nor Legge 3 marzo 2025 n.30 legislates a
VAT, so the framing holds. That is the fourth guide in this branch whose numbers
and framing survived the statute. **Concentration is exposure, not error.**

What the statute added is the half of the tax the guide did not describe.

**The monofase is refunded on export.** The second sentence of art. 1 of Legge 22
dicembre 1972 n.40: *"È previsto il rimborso dell'imposta quando i beni, anche
dopo la loro trasformazione, vengono esportati."* This is the provision that lets
a San Marino manufacturer import inputs, process them and export without the tax
sticking. The guide said nothing about refunds at all — and a widely repeated
commercial description of the monofase calls it *"non detraibile e non
rimborsabile"*. The first half is right: it is not deducted up the chain, which
is what "single-stage" means. The second half is contradicted by the statute's
opening article, and the case it gets wrong is the one exporters are in. The
machinery is real and visible: the Ufficio Tributario publishes an annual refund
declaration that derives an **aliquota media** from the year's purchases, so an
exporter's recovery depends on the mix of rates on what it bought rather than on
any headline percentage.

**And every rate citation pointed at the wrong instrument.** The guide cited
"Imposta Monofase (single-phase import tax) legislation" beside each of its six
rates. Art. 26 of the same law: *"Le eventuali variazioni delle aliquote,
l'introduzione di esenzioni, la variazione dei beni soggetti alle diverse
aliquote… possono essere disposte con decreto della Reggenza."* Rate changes, new
exemptions **and the movement of goods between bands** are all decree matters.
The law demonstrates this against itself: as enacted its art. 4 ordinary rate is
**7%**, with annexed tables at 2, 3, 8, 9, 14 and 15 per cent, every one long
superseded. So a rate quoted against Legge 40/1972 is quoted against a document
that has not set it for fifty years, and the six figures stay marked with a
research gap naming what a reviewer has to find: the decree in force.

This is a different failure from a wrong number. The rates may well all be right.
**The citation was unfalsifiable** — pointing at a document that could never
confirm or deny it — and that is worth catching on its own, because a reader who
checks the cited source finds a real law, sees nothing contradicting the figure,
and concludes it is verified.

Three smaller things the statute gave that the guide had none of: the taxable
base is converted at the official rate **of the day the tax is paid**, not the
invoice date (art. 3); barter is taxed on the value of **all** goods imported
(art. 3); and art. 2 excludes money and money claims, foreign currency, postal
values and stamps, securities not representing goods, daily newspapers, and
**imports by State bodies** — the guide listed no exclusions whatsoever. From
Legge 30/2025: postal imports may now be settled **on collection of the goods**
through Poste San Marino (art. 33), and supplier credit notes issued within a
year are **refunded in full** on top of the export refund (art. 34).

### The leak grep earned its place again

Rewriting the VAT guide left `sm-tax-overview.md` asserting "standard rate 17%"
against the same "Imposta Monofase legislation" citation — the exact defect just
documented, one file away. Found by grepping the corpus for *monofase* before
committing, not after. That is now the fourth jurisdiction where a rewrite leaked
into a sibling, and the second where grepping first caught it in the same commit
rather than an hour later.

Corpus effect, re-measured: authority citations 2,797 → **2,811**, secondary
4,722 → **4,715**. San Marino ends the pass at **25 authority citations against
50 secondary**, having started at zero, and **both** its guides are off the
single-source queue — which is now at **28**.

## Six-jurisdiction source review, September 2026

This pass replaces secondary citations with primary provisions in Bangladesh,
DR Congo, Lesotho, Cayman Islands, Qatar and Burundi. Source access and statutory
interpretation were checked separately. All affected guides remain drafts pending
local-accountant review; a reachable authority website does not establish that
every rule in its documents is current.

### Bangladesh company formation

The Ministry of Law publishes the Companies Act 1994 section by section.
Part X-A, inserted in 2020, provides for a one-person company. Sections 392B–392J
cover its single natural-person owner, nominee, capital and prior-year turnover
bands, director, meetings, accounts and audit. The ordinary private-company
capital statement cannot be applied to an OPC.

The private-company member limit excludes employees and counts joint holders
once. Section 90 requires three directors for a public company and a private
subsidiary of a public company, and two for other private companies. The Act's
domestic definition does not, by itself, settle a foreign parent's classification.
The financial-year definition permits a period shorter than a full year; the
calendar-year proviso concerns insurance companies.

Two reading errors informed the review. Searching for the wrong Bengali spelling
missed the OPC provisions, and extracting only a proviso misrepresented the
financial-year definition. Citations retain the Bengali definition names and
clause letters instead of inventing Roman equivalents. Lakh and crore amounts
were converted explicitly: 25 lakh is BDT 2,500,000 and five crore is BDT 50,000,000.
The OPC conditions and filing references were also added to the existing
freelancer formation guide and its hand-maintained agent skill.

Sources: [section 2](http://bdlaws.minlaw.gov.bd/act-788/section-32006.html),
[section 90](http://bdlaws.minlaw.gov.bd/act-788/section-32914.html),
[section 392B](http://bdlaws.minlaw.gov.bd/act-788/section-50102.html),
[section 392C](http://bdlaws.minlaw.gov.bd/act-788/section-50103.html),
[section 392I](http://bdlaws.minlaw.gov.bd/act-788/section-50109.html) and
[section 392J](http://bdlaws.minlaw.gov.bd/act-788/section-50110.html).

RJSC administrative deadlines, BIDA conditions, fees and a new venture's treatment
under the prior-year turnover requirement still need confirmation.

### DR Congo VAT

Article 35 of Ordonnance-Loi n° 10/001 sets an 8% reduced rate for the listed
tariff positions and domestic air tickets. The previous guide gave 1%. Article 14
includes turnover exactly equal to CDF 80,000,000, permits a two-year registration
option below the threshold and retains registration for the two years following
a turnover decline. Article 23 requires an approved representative for a
non-established supplier and makes the customer liable if none is appointed.

The review corrected three further distinctions. Article 59 makes an issuer
liable for VAT stated on an invoice; its denial of recipient deductions concerns
fictitious supplies or prices not actually payable, rather than all VAT invoices.
Article 62 provides separate treatment for mining-company imports other than
petroleum products. The 2022 normalised-invoice amendment did not establish its
operational rollout date: DGI's November 2025 announcement specifies 1 December
2025. Earlier transactions need the applicable transitional directions.

Sources: [DGI Code des Impôts, 2023 edition](https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf),
[DGI August 2025 VAT leaflet](https://dgi.gouv.cd/wp-content/uploads/2025/10/TVA-CORRIGE.pdf)
and [DGI rollout announcement](https://dgi.gouv.cd/carnaval-de-sensibilisation-sur-lexigence-et-lemission-obligatoire-de-la-facture-normalisee-a-partir-du-1er-decembre-2025/).

The leaflet imposes VAT on liberal professions regardless of turnover, while the
2023 Code marks the corresponding implementing-decree provision as spent. That
conflict remains unresolved. Later ministerial changes to the threshold also need
confirmation before use.

### Lesotho income tax

The RSL consolidation ends at 1 April 2012. Its Third Schedule prints a 0%
export-manufacturing rate, while the 2025 corporate-tax guide's explanatory notes
give 10%. The guide also contains an internal rate-table conflict: PDF page 2
shows export manufacturing at 25% and other income at 10%; page 3 states 10%
and 25% respectively. The page images confirm that this is not caused by text
extraction. Coordinates from the Act's table must not be presented as evidence
about the separate guidance PDF.

That correction was right, and the coordinates have since been re-run against the
guidance PDF itself. On its **page 2** the rate column sits at x=304.2 against
four row labels: *export of manufactured goods outside* SACU at y=242.9 → **25%**;
*manufacturing activity or enterprise* at y=187.2 → **25%**; *farming* at y=131.5
→ **25%**; *Other Income* at y=103.3 → **10%**. On **page 3** the notes read
*"Corporate tax rate of 10% is levied on income from exporting manufactured
goods"* and *"A corporate tax rate of 25% is imposed on profits of a resident
non-manufacturing"* company.

So the conflict is wider than first recorded on either side. It is not one
inverted row: **the 10/25 pairing is inverted on every row of the page-2 table**,
which gives ordinary manufacturing and farming 25% where the Act gives 10%, and
Other Income 10% where the Act gives 25%. The earlier write-up also placed the
table and the notes on the same page; they are a page apart, which is part of why
the inversion survives into a published guide — **nothing puts the two readings in
the same eyeful**.

The original error is worth naming exactly, because the numbers looked like
corroboration. The four rates first cited with coordinates — 10%, 0%, 10%, 25% —
are the **Act's Third Schedule items 1 to 4**, not the guidance table at all. They
were offered as proof that the guidance PDF really printed what it appeared to
print, and they proved something about a different document. **Layout coordinates
answer "did this document say it"; they are only evidence about the document they
were extracted from**, and a plausible set of numbers is the easiest place to stop
checking which file the extractor was pointed at.

The operational guides now mark the 0% provision as historical and unresolved.
Legislation governs as amended, but a 2012 consolidation cannot settle a current
conflict without checking intervening amendments. RSL guidance independently
supports the ordinary 25% company rate and 10% manufacturing and farming rates.

Sections 85 and 87 establish advance corporation tax on distributions outside
qualified income, at 25/75 of the taxable dividend when the standard rate is 25%.
That is exactly one-third, rather than a rounded 33.33% computation. The seven-day
return period runs from dividend payment. Sections 107–109 distinguish gross
withholding from an elective net assessment; choosing the latter requires a
calculation using actual deductible expenses. Section 150 instalments use
30% × (A − B), accounting for prior-year withholding.

Sources: [Income Tax Act, consolidation to April 2012](https://www.rsl.org.ls/sites/default/files/2024-05/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012_0.pdf),
[corporate-tax guide](https://www.rsl.org.ls/sites/default/files/2025-06/Guide%20on%20Corporate%20Tax.pdf),
[ACT guide](https://www.rsl.org.ls/sites/default/files/2024-07/Advanced%20Corporation%20Tax%20Guide.pdf)
and [provisional-tax guide](https://www.rsl.org.ls/sites/default/files/2025-06/Guide%20of%20Provisional%20Tax.pdf).

Post-2012 amendments, the export rate and the prescribed penalty rates remain
review gaps. The different penalty percentages in RSL guides are not sufficient
to reconcile their application.

### Cayman pension and health insurance

The legislation portal returned documents in a browser after direct requests had
failed. That access failure did not establish that the authority was unavailable.
The National Pensions Act separates the required defined-contribution total from
the employer floor and the employee limit without express consent. Additional
voluntary contributions are allowed. Defined-benefit funding has separate
actuarial requirements. Household-domestic exclusions carry a status condition;
they do not exclude every domestic worker.

Health Insurance Act section 7 makes the employer liable for the premium and
permits recovery from the employee. For standard cover, recovery cannot exceed
50%. For a high-risk employee, section 7(ii) uses the difference between the
actual premium and the employer's liability under a standard contract if the
employee were not high risk. It does not establish that the employer bears the
whole loading. Section 8 separately permits recovery of the total dependant
premium for cover effected under section 5(2).

Sources: [National Pensions Act, 2024 Revision](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1996/1996-0010/1996-0010_2024%20Revision.pdf)
and [Health Insurance Act, 2021 Revision](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1997/1997-0015/1997-0015_2021%20Revision.pdf).

The 2024 consolidation marks the six-month pension amendment as uncommenced.
Later commencement orders, current health premium amounts and work-permit fee
scales were not exhaustively verified.

### Qatar social insurance

Law No. 1 of 2022 confirms the 21% total contribution, split 7% employee and
14% employer, with a general QAR 100,000 contribution-salary ceiling. Article 12
adds a QAR 6,000 monthly cap on the housing allowance included in that salary.
Article 13 expressly preserves existing contribution salaries above the general
ceiling until actual termination of service. A claim that grandfathering could
not be found in the law was incorrect.

Article 4 makes self-employed participation optional and provides for income
bands and full payment by the participant. Employee eligibility under articles
2–3 and exclusions under article 5 must be checked separately. GCC coverage
rests on Law No. 4 of 2007 as amended by Law No. 5 of 2021. It prevents a blanket
statement that every non-Qatari employee has no social-insurance obligation.

The Gazette header identifies issue 7 dated 3 July 2022. The issuing law's
article 4 provides commencement six months after publication, with specified
exceptions. Article 11 authorises a Cabinet-approved State contribution towards
private-sector employer costs; no implemented subsidy was verified.

Source: [GRSIA, Law No. 1 of 2022](https://www.grsia.gov.qa/Regulations%20and%20Policies/Law-1-2022.pdf).
The GCC system, detailed housing settlements, executive regulations and
expatriate end-of-service treatment still require further review.

### Burundi income tax and VAT

The OBR website and legislation register returned in the browser. Its tax laws
are scans, so OCR helped locate passages and page images supplied the check.
Agreement between words and digits can expose an OCR error, but does not prove
that a rate applies to the right taxpayer. Arithmetic checks cannot establish
the legal scope either.

The review found that article 23's 15% capital-income rate belongs to individuals.
Company capital income and gains fall within article 98 and the article 103
company rules, subject to their exceptions. Article 102 governs final corporate
non-resident withholding under articles 122–125. Article 130, legible on PDF
page 42, provides three 25% provisional instalments with withholding credits.

Article 21 contains annual employment and rental-income bands. Article 117
expressly sets monthly payroll bands, including exceptional payments. The monthly
thresholds are not conditional on equal pay across twelve months. Articles 118
and 119 address non-principal and occasional employers separately. The upper-band
calculation must include the tax from the preceding band.

Finance Act 2026/2027 article 190 applies quarterly 1% turnover tax to qualifying
natural persons with annual turnover up to BIF 25,000,000. Article 271 makes VAT
registration compulsory at taxable turnover of BIF 25,000,000 or more and has
separate purchases, imports and stock tests. At the exact threshold the income-tax
and VAT regimes may overlap; they do not switch together. The guides label these
Finance Act provisions as 2026/2027 rules rather than applying them to 2025.

The VAT law sets ordinary, intermediate and zero rates of 18%, 10% and 0%.
Specified categories depend on ministerial lists. Articles 52 and 54 govern
monthly filing and payment, and article 67 addresses deregistration. The
100% and 200% penalties in articles 55–56 concern specified electronic-invoicing
breaches and must not be presented as a universal VAT penalty.

Sources: [income tax law amended in December 2020](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf),
[VAT law amended in November 2020](https://www.obr.bi/images/LOI_N1_10_DU_16_NOVEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_12_DU_29_JUILLET_2013_PORTANT_REVISION_DE_LA_LOI_N1_02_DU_17_FEVRIER_2009_PORTANT_INSTITUTION_DE_LA_TAXE_SUR_LA_VALEUR_AJOUTEE_TVA_.pdf)
and [Finance Act 2026/2027](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf).

INSS contribution rates and caps, the ministerial VAT lists and the detailed
penalty ladder remain unverified. The payroll guide retains explicit warnings
for conflicting secondary-source social-contribution figures.

#### Re-reading the withholding chapter at page-image quality

The article 117 correction above was checked rather than accepted, and it holds:
the article sits under the heading *"Du taux mensuel de la retenue à la source sur
les revenus d'emploi"* and sets its own monthly table. The earlier claim that the
monthly figures were a derivation from article 21 valid only for **even pay across
twelve months** was wrong twice over — the bands are statutory in their own right,
and article 117 expressly extends them to *"les paiements exceptionnels"*, which is
precisely the uneven case the caveat said they could not reach.

Verifying it meant reading the surrounding pages at 300 dpi instead of by OCR, and
that turned up five provisions no version of these guides carried:

- **Article 113** — where tax is not withheld, *"l'employeur est obligé de payer
  l'impôt non retenu ainsi que les amendes et pénalités y afférentes"*. The failure
  to operate PAYE lands on the employer **with the penalties**, not on the employee.
- **Article 116** — where the employer is not obliged to withhold, the employee
  must file monthly *"sous peine de sanction"*. Its deadline is the **15th of the
  following month**, where article 115 gives the employer **fifteen calendar days
  after the end of each month**. Two deadlines, two taxpayers, one number.
- **Article 117, second table** — *indemnités de licenciement, de perte d'emploi,
  de fin de carrière, de départ à la retraite ou de résiliation du contrat* are on
  a separate progressive scale of **5% / 10% / 15%** at BIF 10,000,000 and
  30,000,000. Severance was being answered off a scale topping out at 30%.
- **Article 117 also names political and public office-holders** and recipients of
  *indemnités de fin de mandat*, so that case is settled expressly rather than
  argued from the definition of employment.
- **Article 22:** withholding under articles 119 and 120 is final for non-residents' Burundi-source income not attributable to a Burundi permanent establishment. This conclusion is limited to those withholding provisions. Ordinary employment and rental income remain subject to article 21's rules. [Income tax law, arts. 21–22](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

Article 24 sets the annual individual deadline at the end of the third month after the accounting year closes, excluding the employer's article 115 recapitulative. Article 25 exempts people receiving only salary withheld under article 113, income withheld under articles 119–120, or both. Article 26 permits voluntary filing, including for refunds. The guide now includes those conditions. [Income tax law, arts. 24–26](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

One correction here ran the other way. Article 115 was doubted on the strength of
an OCR fragment reading *"au plus tard le quinze (15) du mois suivant"*, which
looked like the wrong formulation for the article cited. The page image showed the
fragment belonged to **article 116** and that article 115 says exactly what the
review claimed. The OCR line belonged to the adjacent article. The page image resolved the attribution.

## Sierra Leone concurrent update and review

A concurrent commit added Sierra Leone while this review was underway. It was
preserved and reviewed against the NRA's Finance Acts. Finance Act 2026 section
13 changes the resident company rate from 25% to 30%, effective 1 January 2026.
Section 14 raises the non-resident contractor, dividend, interest and
management/professional fee withholding rates to 20%. These changes must remain
separate from the 2025 columns and the non-resident ordinary income rate.

The concurrent draft said the section 97 amendment could not be read. It is
printed on page 7, on the right of the PDF spread whose left side is page 42.
Section 8 replaces section 97(3) with prescribed return requirements and adds
section 97(6)(d) for related-party files. The 2017 certified-accounts provision
must not be presented as the current subsection. Section 97(1)'s 120-day rule
is not amended by section 8.

The master file is due within one month after filing in the parent's residence
country, the local file within two months after the annual return, and the
country-by-country report within one year after the relevant tax year ends.
Applicable Gazette directions and reporting scope still need confirmation.

The draft also inferred currency units from counts of `Le` and `NLe`. Those
labels do not establish that every 2024 amount is in old leones. Monetary
thresholds remain unconverted until their units are verified.

Source: [NRA Finance Act 2026](http://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2026_121df05d9b.pdf),
sections 1, 8 and 12–14. The three Sierra Leone guides remain pending review.

The minimum-tax review also checked the provisions left in force. Finance Act
2025 section 8 preserves initial incorporation and liquidation exemptions and
protection for existing investment agreements until expiry or review. Finance
Act 2024 section 8 supplies turnover exclusions and non-refundable credits for
the following ten years. Removing the loss condition in 2026 does not remove
those other provisions.
[Finance Act 2024](http://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2024_0d6d83e684.pdf),
[Finance Act 2025](http://webtestcms.nra.gov.sl/uploads/The_Finance_Act_2025_beb680faed.pdf).

## Armenia — the authority was one form submission away

`am-company-formation.md` sat at **5 of 5** on `armenian-lawyer.com`. The queue had
carried a note that `arlis.am` "returns 200", which is the weakest possible reason
to leave a jurisdiction on commercial sources: a 200 says the server answered, not
that anything was read.

Opened in a browser, `arlis.am` is the Ministry of Justice's legal information
system and it publishes **the consolidated Tax Code and the LLC Law in full text**
— 1.45 million characters for the Tax Code alone, current consolidation, status
*Գործում է*. Nothing about it was hard except finding the search box.

**The search is a POST form whose text input has no `name` attribute.** A GET with
a query string silently returns the home page — same byte length, HTTP 200, no
error — so the obvious first attempt looks like a working request that finds
nothing. The field had to be addressed by its placeholder text and the form
submitted in the page. **A site is not "unsearchable" until you have looked at how
its search actually posts**, and the failure mode here was a 200 with plausible
content, the same trap the DR Congo leaflet set.

### What the Tax Code said

Two of the guide's numbers were right and thinly sourced, and now carry the
statute: **profit tax 18%** (art. 125(1)) and **VAT 20%** (art. 63(1)). Three were
approximations that the statute states exactly, and three whole mechanisms were
missing:

- **"Within about 20 days of incorporation"** is, precisely, *by the 20th day
  following the day of state registration, inclusive* — arts. 254(1)(2) and
  267(1)(2). An existing company elects by **20 February**.
- **"Turnover tax" is not a rate.** Article 258(1) prints a ten-row schedule from
  **1%** (Government-listed high technology) to **20%**, under an **AMD
  115,000,000** previous-year ceiling (art. 254(2)). Eligibility also depends on the activity, related-party and contractual exclusions in article 254(3). The guide now includes the expense reductions and floors in article 258(2)–(7): trading 9.5% of qualifying expenses with a 1% turnover floor; production 5% with a 3% floor; catering 9% with a 3.5% floor; other activity 6% with a 4.5% floor. Unused reductions carry forward by activity. [Tax Code, arts. 258 and 260](https://www.arlis.am/en/acts/230455/latest).
- **Micro-business** has an **AMD 24,000,000** ceiling (art. 267(3)) and an
  exemption whose exceptions are the operative part: a micro-business is still
  liable for import taxes, excise, environmental and road tax, and **still
  withholds income tax on employees** (art. 269). The article 267(5) exclusions must be checked before electing; accounting and advisory activities are excluded even below the ceiling.
- **The 16.67% embedded-VAT rate** (art. 63(2)) applies in four invoicing-failure
  cases and appears nowhere in the corpus.
- **Charter capital**: art. 28(1) sets no minimum — and its *next sentence* lets
  other laws set minimums by sector, which the flat "no statutory minimum" claim
  concealed.
- **Approving annual results** must happen *"ոչ շուտ, քան 2 ամիս և ոչ ուշ, քան 6
  ամիս"* after year end — **not earlier than two months** and not later than six.
  The guide gave the ceiling and dropped the floor. **A one-sided window reads as
  complete**, which is why the omission survives review.

### One check paid for four files

The flat **20% personal income tax** appears across `armenia-payroll.md`,
`armenia-social-contributions.md` and their triggers, cited to PwC throughout.
Article 150(1) confirms it and shows the phase-down that produced it — 23% from
2020, 22%, 21%, then 20% from 1 January 2023. `armenia-payroll.md` said the rate
"reached 20% from **1 July 2023**"; the statute says **1 January**.

Article 150(1.1) sets a 10% rate for qualifying R&D salary, subject to the Government-listed occupation, qualifying work, commission opinion and residence conditions. Those conditions now feed the required inputs, calculation rules and templates in both payroll guides. A verified AMD 600,000 R&D salary produces AMD 60,000 PIT; the general rate produces AMD 120,000. Unresolved eligibility stops the final calculation. If the commission opinion is revoked, the general rules govern recalculation. [Tax Code, art. 150](https://www.arlis.am/en/acts/230455/latest).

Corpus effect: authority citations 3,010 → measured after commit; Armenia moves off
zero authority citations. The registration fee, incorporation timeline and
e-invoicing mandate stay on commercial sources and are marked as such — the Law on
State Registration of Legal Entities and the Law on State Duty are both on
`arlis.am` and would settle them.

## Guinea — reaching the authority and finding it does not publish the law

`gn-income-tax.md` was **6 of 6** on `taxatlas.io`, every row marked "(approx —
confirm)". The outcome here is not a correction: it is a **negative result,
established rather than assumed**, and it is worth recording because "we used a
commercial source" and "the authority does not publish this" are very different
statements to leave in front of a reviewer.

### Clearing a bot challenge, and why the obvious fix fails

`dgi.gov.gn` answers a plain HTTP client with **202 and a 169-byte body** — an
interstitial challenge, not a page. In a browser the home page renders normally.

The trap is one layer down. A browser automation library gives you two ways to
fetch: navigate a **page**, which runs JavaScript, or call the context's
**request** API, which does not. Binary downloads naturally reach for the request
API — and it **cannot clear a JavaScript challenge**, so it returns the same
248-byte interstitial while the browser sitting next to it loads the site fine.
Two download strategies failed this way before the shape of the problem was clear.

What works is to **warm the context with a real page navigation first**, let the
challenge resolve, and only then call the request API — the clearance cookie is
set on the context, so the subsequent fetch inherits it. One further detail
mattered: the warm-up must **wait for the network to settle** before its title is
checked. Checking at `domcontentloaded` read an empty title, concluded the page had
not rendered, and skipped the wait, so no cookie was ever obtained. With a
`networkidle` wait and a short settle, the same code returned **5,214,544 bytes of
`application/pdf`**.

**A challenge is cleared per browsing context, not per request**, and the fix is
ordering rather than cleverness.

### And then the document was the wrong kind of document

The DGI's *Bibliothèque de documents* was read in full. Its "Loi et règlements"
section lists finance laws for 2016–2021 and 2025, arrêtés, décisions, taxpayer
charter and mission reports. **There is no Code Général des Impôts on the site at
all.**

The newest instrument, **Loi ordinaire L/2024/023/CNT portant loi de finances pour
l'année 2025**, is a 22-page scan with no text layer. OCR shows what it is: a
**budget appropriation law** — total revenue estimated at GNF 35,176,145,730,740,
split between the general budget and special-allocation budgets, then allocations,
closing at article 37 with the standard repeal-and-publication clause. **No IRPP
scale appears in it**, so it cannot confirm or contradict any row of the guide.

**A finance law is not always a tax law.** In several jurisdictions already worked
here — Burundi, Sierra Leone — the annual finance act is where the operative rates
and thresholds live, and that pattern invites the assumption that reaching a
finance act means reaching the rates. Guinea's is a pure appropriation act. The
guide's bands stay marked, the research gap now names the exact missing document,
and the reviewer is told where the search already went so they do not repeat it.

### A source-availability register for the rest of the queue

Having built a browser that clears bot challenges, the sensible next step was to
point it at every remaining queue jurisdiction at once rather than discover the
same dead ends one file at a time. The results below are **evidence about this
environment on 2026-09-10**, not a verdict on the sites themselves — a host that
does not answer here may be geo-restricted, may be blocking the egress proxy, or
may simply have been down. Recorded so the next person does not repeat the search.

**Live, and the authority publishes usable law**

- **Armenia** — `arlis.am` serves the consolidated Tax Code and the LLC Law in
  full text. Worked through above; the guide is rewritten on it.

**Live, but not the document the guide needs**

- **Guinea** — `dgi.gov.gn` clears its challenge in a browser and its library was
  read in full. It publishes finance laws, arrêtés and reports; **no Code Général
  des Impôts**. Covered above.
- **Nicaragua** (`dgi.gob.ni`), **Myanmar IRD** (`ird.gov.mm`), **Cape Verde
  Finance Ministry** (`mf.gov.cv`) — all answer HTTP 200 with real pages. Each is
  a *tax* authority, and each jurisdiction's queue entry is a **company formation**
  guide, whose authority is a companies registry or a commercial code. **Reaching
  an authority is not the same as reaching the right authority**, and these three
  are the best remaining leads precisely because the obstacle is now knowing which
  instrument to ask for rather than whether anyone will answer.

**Reached, and empty**

- **São Tomé and Príncipe** — `mf.gov.st` answers, with the title *"Under
  construction - Awesome site in the making!"* and **91 characters of body text**.
  Three guides sit on the queue behind a ministry site that has not been built.
  `impostos.st`, `minfinancas.st`, `mpf.gov.st` and `impostos.gov.st` have no DNS.

**Resolve but never serve — the browser failed too, so this is not a challenge**

- **Gabon** `dgi.ga` → 197.231.72.25; **Eritrea** `mof.gov.er` → 196.200.102.238;
  **Myanmar DICA** `dica.gov.mm` → 103.89.50.27. Each resolves, each refuses the
  connection to both a plain client and the browser. Note the split in Myanmar:
  the **tax** authority answers and the **companies registry** does not, and the
  registry is the one the formation guide needs.

**No DNS at all**

- Cuba `onat.gob.cu`; Djibouti `impots.dj` and `impots.gouv.dj`; Vanuatu
  `customsinlandrevenue.gov.vu`; Central African Republic `impots.cf`;
  Turkmenistan `minfin.gov.tm`.

**Deliberately not pursued**

- **Iraq** — a Cloudflare WAF deny, which is a firewall rule someone configured on
  purpose. It is left alone. The guide stays marked, and 13 of its 14 citations
  stay on one commercial host, because the alternative is evading a control the
  site owner chose to apply.

The distinction worth keeping is between the three states above: **no DNS** is a
dead address, **resolves-but-refuses** is a live address behind something, and
**answers-with-a-placeholder** is a live site with nothing in it. Only the first
is safely permanent; the other two are worth retrying from a different network
before a guide is written off, and none of the three is a reason to present a
commercial figure as though it were checked.

### Cape Verde — the operator contradicts the summary, and the code stays out of reach

Following the register's own advice — go to the legal gazette, not the tax
authority, when the guide is about company formation — Cape Verde produced one
correction and one well-mapped dead end.

**The Imprensa Nacional de Cabo Verde**, the state gazette publisher, describes
*Empresa no Dia* itself: incorporation of Sociedades Anónimas and Sociedades por
Quotas *"de forma imediata, no próprio dia"* at a staffed Casa do Cidadão counter,
with **eight separate interactions with the administration** — legal, fiscal,
social and labour — collapsed into one. The guide said the timeline was
"approximately 1 to 2 weeks (faster via the one-stop shop)", on a commercial host.
**The body that runs the service says same day.** The row now cites INCV and says
so, with the caveat that a longer estimate may be describing steps outside the
service rather than the incorporation.

The *Código das Empresas Comerciais* is another matter, and the search is recorded
because it went four layers deep and still failed:

- `casadocidadao.cv` — the operator's own domain — answers **200 with a 17-byte
  body**. Live, and empty.
- There is **no `boe.cv` or `bo.cv`**, despite INCV describing an electronic
  Boletim Oficial as a free and universal public service. *(This bullet was a
  false negative produced by guessing at hostnames. The gazette is at
  **`boe.incv.cv`** and is open, complete and free. See "Cape Verde, resolved"
  below.)*
- INCV's Boletim Oficial page **displays its own feed error**: *"SSL certificate …
  has expired"*. The publisher cannot reach its own gazette feed.
- `legis-palop.org`, the Portuguese-speaking African countries' legal database, is
  live but serves through an opaque `?load=NNNNN` application loader.

So the capital figures stay marked, with one addition a reviewer can act on
immediately: **the guide gives a Sociedade Anónima the same CVE 1 minimum capital
as a Sociedade por Quotas**. A public limited company sharing a private one's
statutory floor is unusual enough that the claim should not be relied on without
an article number. **Noticing that a figure is implausible is not the same as
knowing it is wrong** — it is flagged, not corrected, because the code that would
settle it could not be opened. *(It was opened later, and the flag was right for
the wrong reason — see "Cape Verde, resolved" below.)*

### Two ways to manufacture a false "unreachable", both hit in one sitting

The register above is only worth having if its verdicts are about the sites rather
than about this environment's configuration. Two faults found immediately after
publishing it would each have produced convincing, entirely false entries. Both
are recorded because **a tooling failure and a dead host look identical from the
outside** — an empty page and a note saying it could not be loaded.

**1. The proxy port moved and the drivers hardcoded the old one.** The container
restarted; the egress proxy came back on a different port. Every browser driver
carried the previous port as a literal, so each fetch returned *"Problem loading
page"* — the exact signature recorded for Gabon, Eritrea and Myanmar's registry.
Nicaragua's National Assembly was written off on that basis and is, in fact, fine.

The tell was a **contradiction between two tools**: `curl` reached the host and
returned a Cloudflare challenge while the browser could not reach it at all. That
is backwards — the browser is the more capable client. **When the weaker tool
succeeds where the stronger one fails, suspect the stronger one's configuration
before you conclude anything about the host.** Every driver now reads
`process.env.HTTPS_PROXY` instead of a literal.

The register's own entries survive this, because those tests ran **before** the
restart, on the port that was then correct. That is a fact about timing rather
than a defence of the method: had the restart come an hour earlier, three
jurisdictions would have been recorded as dead on the strength of a stale port.

**So they were re-tested rather than left resting on that.** With the corrected
proxy and `https://` throughout: Gabon `dgi.ga` and Myanmar's `dica.gov.mm` still
never load; Eritrea's `mof.gov.er` still returns *"Problem loading page"*; and São
Tomé's `mf.gov.st` still answers **202** with *"Under construction - Awesome site
in the making!"* and 91 characters of body. Every entry holds. **Publishing a
claim, finding two ways it could have been wrong, and then re-running it is the
cheap half of the work** — the expensive half was noticing the tools disagreed.

**2. The proxy tunnels HTTPS only, and government sites still link `http://`.**
`digesto.asamblea.gob.ni` returned **405 with a 465-byte body** through the
browser. The body is not from the site — it is the proxy saying *"this proxy only
accepts HTTPS CONNECT tunnels."* Every link to the Digesto on the Assembly's own
home page is `http://`, so following the site's own navigation produces a
plausible-looking failure at the first hop. **The same URL over `https://` returns
200 and 46 KB.**

So a scheme the site itself publishes is enough to make a live authority look
dead. **Rewrite `http://` to `https://` before recording any failure**, and read
the error body rather than the status code — a 405 that explains itself is not a
site rejecting you.

### Nicaragua — the legal database is live, and it is not the one the links point at

Correcting the register entry above: the useful Nicaraguan authority is not the
tax administration but the **Digesto Jurídico Nicaragüense**
(`https://digesto.asamblea.gob.ni/`), the official consolidated legal digest,
which answers **200** and offers *Normas Jurídicas*, *Digestos Jurídicos* and a
documentary collection running from 1821.

`legislacion.asamblea.gob.ni` looks like the database and is not one. Over `http`
its `normaweb.nsf` is a Lotus Domino stub whose entire body is
`onload="window.location.href='http://www.asamblea.gob.ni'"` — a redirect with no
content; over `https` the connection resets. **A URL that looks like a database
endpoint can be a redirect with a database's name on it.**

The norms themselves sit behind `/consultas/normas/`, whose search is
JavaScript-driven — the static form exposes only a norm number and date ranges —
and whose documents are addressed as `shownorms.php?idnorm=<base64 of a numeric
id>`. `ni-company-formation.md` therefore stays on its commercial source for now,
but the gap is narrowed to **locating one code inside a working official database**
rather than finding an authority at all.

### Nicaragua — five layers to the text, and the Code contradicts the guide

The Digesto entry above said the database was live and the code was not yet
located. It is now, and the route is worth writing down because none of the five
steps was guessable from the one before it.

1. The search is a **POST to `/consultas/util/ws/proxy.php`** with
   `hddQueryType=getJuridicNorms` and the serialised form, returning JSON. The
   visible form offers only a norm number and date ranges — there is **no title
   field** — so the way in is a **date range**: the Código de Comercio is 1916 law,
   and 1914–1918 returns 1,219 records, among them *Código de Comercio de
   Nicaragua*, `registro` **"Vigente"**, published 20/10/1916.
2. Each record carries an `iunpid`, base64 of a numeric id — `MjkyOTI=` is 29292.
3. `shownorms.php?idnorm=…` renders the record: *Código N°. s/n*, materia *Empresa,
   Industria y Comercio*. It shows a TEXTO panel and a Download button.
4. **Both are empty.** `hasfileNorm` returns **false** for every `valordominio`,
   and `getVersionHtmlAccordion` returns nothing. The Digesto catalogues this code
   without attaching its text. **A record is not a document**, and stopping here
   would have produced a perfectly defensible "the database has it but does not
   serve it".
5. The text is in the **documentary collection**, reached by a different query —
   `getRddsByIunp` — which returns an `rddid` and a starting page, and
   `pdf.php?type=rdd&rdd=…` then serves **13.7 MB, 323 pages** with an OCR text
   layer. The Code begins at page 35.

### What the Code says that the guide did not

`ni-company-formation.md` was **4 of 5** on one commercial host. Reading arts.
201–207 confirmed one claim and contradicted another.

- **Two founders is right** — art. 202, *"puede constituirse por dos o más
  personas"*. Confirmed, and now cited to the Code.
- **"Capital need not be deposited at incorporation" is wrong where it matters.**
  Article 206: *"Ninguna compañía anónima podrá comenzar sus operaciones mientras no
  tuviere suscrita siquiera **la mitad del capital social**, y en dinero efectivo, el
  **10%** del capital que consista en numerario."* The Code does not gate
  incorporation on paying capital; it gates **commencing operations** — which is
  what a founder is actually asking about. **A claim can be technically defensible
  and still answer the wrong question.**
- **Three rules were simply absent**: art. 204, no legal personality until the
  escritura and Estatutos are registered, and both must then be **published**;
  art. 205, five grounds on which a judge **refuses** registration; art. 203, the
  prescribed content of the Estatutos.
- **And one of those grounds qualifies a headline claim.** The guide said
  "Foreigners may fully own a Nicaraguan company". Art. 205's first ground refuses
  registration where the founders are not *"naturales del país o extranjeros
  **domiciliados en el mismo**"*. Ownership after formation and eligibility to be a
  founder are different questions. **This is 1916 law** and later investment
  legislation may displace it, so it is **flagged, not resolved** — the guide now
  puts the two side by side and says which is unsettled.

Article 206 was read from the **page image** at 300 dpi rather than the OCR layer,
which renders the surrounding text as *"R sus habitantes"* and *"dctretan"*. The
figures survive the words-and-digits rule only on the image: *"la mitad"* is words,
*"el 10%"* is digits alone, and the image is what confirms it.

`incv.cv` was added to the `list-source-mix.py` allowlist in the same commit — the
Imprensa Nacional de Cabo Verde publishes the Boletim Oficial and was scoring as
secondary, the same blind spot that once had Botswana citing its own revenue
service and counting as unsourced. `digesto.asamblea.gob.ni` already scored as
authority through the `gob` pattern; a selftest now pins both.

### OHADA — the queue was treating one law as two problems, and they disagree

Burkina Faso and Gabon sit on the queue as separate entries. They are not separate
problems: both are **OHADA** member states, so their company law is not national
law but the same *Acte uniforme relatif au droit des sociétés commerciales et du
groupement d'intérêt économique*, shared across seventeen countries. Noticing that
was the whole finding, because it puts two guides that never reference each other
into direct comparison.

**They disagree, while citing the same instrument.** `bf-company-formation` gives
the SARL minimum capital as *"freely set by the partners but at least the par value
of one share (5,000 FCFA)"*, cited to the AUSCGIE. `ga-company-formation` gives
**XAF 1,000,000**, cited to the AUSCGIE. **A single uniform text cannot say both.**
At least one attribution is wrong, and the corpus contained the contradiction with
nothing to surface it: no checker compares two jurisdictions' citations of a shared
supranational instrument, because nothing knows the instrument is shared.

The likely resolution, **flagged as a hypothesis rather than asserted**: the 2014
revision left the SARL minimum to each member state, so both states may genuinely
differ while **neither figure belongs to the uniform act**. On that reading Burkina
Faso's 5,000 FCFA par value is **pre-2014** — a rule right for the wrong year, the
Sierra Leone shape again. The two guides *agree* that the SA minimum is 10,000,000,
which is the figure usually attributed to the Act, and that agreement is the only
corroborating part.

It stays a hypothesis because **the Act could not be read**. `ohada.org` answers
`curl` with 200 and 408 KB, but its *Actes uniformes* and *Droit des sociétés
commerciales et du GIE* pages carry **no PDF link and no inline text** — zero
matches for "Article N" — and both fail in the browser while succeeding under
`curl`, the reverse pattern that earlier exposed the stale proxy port and this time
did not. `droit-afrique.com`, the usual mirror, returns a hard **403 Forbidden** to
`curl` and browser alike: 260 bytes, a real refusal rather than a challenge.

**A shared legal instrument is a checkable cross-jurisdiction invariant**, and this
corpus has more of them than the queue can see: OHADA covers seventeen states, and
the same logic applies to CEMAC, UEMOA, the EAC and the GCC. Where two guides cite
one supranational text for the same rule and give different numbers, one of them is
wrong **without anyone needing to open the text**.

### Myanmar — three sources, all dead, so the entry is closed rather than open

`mm-company-formation.md` is the largest non-Iraq entry on the queue at 8 of 10.
Its authority is the companies registry, and the register already recorded
`dica.gov.mm` as resolving but never serving. Two further routes were tried with
the corrected proxy and `https://` throughout: the **Myanmar Law Information
System** (`mlis.gov.mm`) and the **Myanmar Law Library**
(`myanmar-law-library.org`). Both resolve; **both fail in the browser as well as
`curl`**.

So the split noted earlier holds and is now complete: Myanmar's **tax** authority
answers and **every route to its company law does not**. The entry stays on the
queue, but as a documented dead end rather than an unexplored one.

### Two countries were being governed by a treaty they never joined

The OHADA comparison above suggested a check nothing in this repo performs: for a
**supranational instrument**, membership is a fact with an authoritative register,
and every guide citing the instrument can be tested against it in one pass.

Sixteen jurisdictions in this corpus cite OHADA or the AUSCGIE. OHADA's own page,
*Les Etats membres de l'OHADA*, lists **seventeen**: Bénin, Burkina Faso, Cameroun,
Centrafrique, Comores, Congo, Côte d'Ivoire, Gabon, Guinée, Guinée Bissau, Guinée
Équatoriale, Mali, Niger, RDC, Sénégal, Tchad, Togo.

**Two of the sixteen are not on it: Djibouti and Burundi.**

Djibouti is the serious one. `dj-company-formation.md` opened with *"Company law in
Djibouti follows the OHADA Uniform Act on Commercial Companies"* and cited the
AUSCGIE **nine times** — for entity types, minimum capital, the 1-to-50 shareholder
range, the RCCM and the registration steps. `dj-tax-overview.md` stated it outright:
*"OHADA Uniform Acts apply **(Djibouti is an OHADA member state)**"*, and added that
*"OHADA accounting rules govern the books"*; `dj-corporate-income-tax.md` had the tax
base *"prepared under OHADA accounting"*. **Three guides, resting on a premise that
is false.**

The row asserting membership was already marked **"(approx — confirm)"**. The
confirmation was a single page on the treaty organisation's own site. **A marker is
not a substitute for the check it asks for**, and this one sat unread while nine
citations were built on what it flagged.

Burundi's is the gentler version: *"company law based on the OHADA-style commercial
framework"*. The hedge **"-style"** makes it not quite a false statement, which is
exactly why it survived — but a reader takes from it that the Uniform Acts apply,
and they do not.

**What was and was not fixed.** The false attributions are corrected and the guides
now cite OHADA's member register for the correction. **The figures underneath were
not replaced**, because nothing was found to replace them with: the entity names
(SARL, SA, RCCM) are shared across francophone civil-law systems and may well be
right for Djibouti. **A figure can survive its citation being wrong.** What is now
recorded is that they are **unsourced** rather than OHADA law, with Djibouti's own
*Code de commerce* named as the missing document.

The mirror-image gap exists too and is milder: **Cameroon is an OHADA member whose
four guides never mention OHADA at all.** Under-citing the instrument that governs
you is a smaller fault than citing one that does not, but it comes from the same
blind spot.

**This check generalises.** Membership of a supranational régime is verifiable
against the régime's own register, and the corpus leans on several: OHADA,
CEMAC, UEMOA, the EAC, the GCC, the EU. Any guide that names one is asserting a
membership fact, and that fact is cheap to test — **two false claims out of sixteen,
found in a single pass, none of which any figure-level checker could ever see**.

### The membership check, run against every other régime — and what it turned up instead

The OHADA result made the check worth generalising, so every supranational régime
this corpus names was tested the same way: list the jurisdictions citing it, compare
against the régime's membership.

**Four came back clean.** CEMAC is cited by exactly its six members; UEMOA and its
English name WAEMU are cited, between them, by exactly the eight; SACU by Lesotho
and South Africa; CARICOM by Jamaica and Trinidad and Tobago. The UK's single "GCC"
hit is a UAE-relocation day-count test, not a membership claim. **A check that finds
nothing is still worth running once** — it is the difference between "no other
régime is misattributed" and "nobody looked".

Two things fell out of the scan that it was not looking for.

**A jurisdiction's own name is a weaker key than it looks.** Five jurisdiction codes
map to more than one directory: `AE` (`uae`, `united-arab-emirates`), `CA`
(`canada`, `ca-chartered-accountant`), `IM` (`im`, `isle-of-man`), `VG` (`bvi`,
`british-virgin-islands`) and `VN`. The first four are a naming split, not an error —
`ca-chartered-accountant` holds sixteen **Canadian provincial** guides, all correctly
tagged `CA`, behind a directory name that suggests a profession. But **anything that
groups by directory sees eight jurisdictions where there are four**, and this repo's
own per-jurisdiction reporting does exactly that. The "jurisdictions with any
external citation" and "citing no authority domain at all" figures are computed
per directory, so those four are each counted twice.

**The real Argentine content was never lost, and I did not look for it.** It
survived intact in `agent-skills/argentina-references/` — the hand-maintained tree
CLAUDE.md describes as inheriting nothing from `skills/`. That description was read
as "the trees are independent, so a fix here will not propagate there", and the
converse went unconsidered: **a tree that does not receive corrections also does
not receive corruptions.** When one copy of a file is wrong, the parallel tree is
the first place to look, not an afterthought. The Argentine entry there lists
**pyafipws** (LGPL-3.0, the definitive AFIP e-invoicing library) and **PyARCA**,
whose own scope line reads *"Monotributo (ARCA/ex-AFIP)"* — corroborating the
authority's rename from a source independent of the authority. Those projects are
now restored to `skills/` rather than replaced with a thinner file written from
scratch, which is what happened on the first pass.

**And the fifth was a real error.** `argentina/references.md` carried
`jurisdiction: VN` and, under the heading *"Vietnam — Related Open-Source
Projects"*, listed two Vietnamese personal-income-tax repositories and cited *Luật
số 109/2025/QH15*, *Luật Thuế TNCN No. 04/2007/QH12* and *Thông tư
111/2013/TT-BTC*. It was a stray copy of `vietnam/references.md`. **Argentina did
not have a thin references file; it had Vietnam's.** All 32 other `references.md`
files match their directory. The file is now an Argentine one, naming **ARCA** —
verified from the authority's own portal, which uses that name throughout and none
of "AFIP" — with the legislative list left as a marked gap rather than invented.

**The Argentina pack was already right about the thing that looked wrong.** ARCA
replaced AFIP under Decreto 953/2024, and 70 "AFIP" mentions across seven files
looked like stale naming until they were read: the guides say *"ARCA (formerly
AFIP)"* and cite the decree. **Confirming that a suspicion is unfounded is part of
the check, not a wasted step** — and the alternative, a bulk rename of a term the
corpus was using correctly and deliberately, would have destroyed real information.

### The corpus contains its VAT guides twice, and three of the copies disagree about who reviewed them

Chasing the Argentina misfiling turned up a cheaper detector than the frontmatter
scan that found it: **compare a file's `name:` against the `# H1` in its body.**
It needs no external source, runs in a second, and the signal is strong because a
duplicated file usually keeps the original's heading.

It returned **41 files**. Most are benign in themselves — `se-vat-return.md` with
the H1 `sweden-vat-return`, `dk-vat-return.md` with `denmark-vat-return` — but the
pattern they reveal is not.

**Nearly every jurisdiction's VAT or GST return guide exists twice**, under two
naming conventions: an ISO-prefixed `xx-vat-return.md` and a country-named
`country-vat-return.md` / `-iva` / `-mva` / `-gst`. A body-similarity scan over
1,373 substantial guides found **33 near-duplicate pairs, 20 of them byte-identical
below the frontmatter** — Spain, Netherlands, Poland, Portugal, Romania, Sweden,
Denmark, Greece, Hungary, Ireland, Norway, Mexico, Colombia, Chile, Switzerland,
Singapore, India, Japan, Czechia, the UAE and the EU base file among them.

**A correction applied to one copy does not reach the other**, and nothing in either
file says a twin exists. That is the `agent-skills/` problem — a tree that inherits
nothing — reproduced inside `skills/` where nobody has flagged it.

**Three pairs are worse than a maintenance hazard.** The two copies carry different
tiers and different reviewers:

| Jurisdiction | Tier 1, reviewed | Tier 2, unreviewed |
| --- | --- | --- |
| **UAE** | `uae/uae-vat.md` — **Mehran Habib** | `united-arab-emirates/ae-vat-return.md` |
| **Portugal** | `portugal/portugal-vat-return.md` — **Mário Jorge da costa Vale** | `portugal/pt-vat-return.md` |
| **India** | `india/india-gst.md` — **Mayur Deokar** | `india/in-gst-return.md` |

The bodies are identical and **the trigger descriptions are identical word for
word**, so a model selecting a skill by description can load either. Which copy it
happens to load decides whether the answer is presented as accountant-reviewed and
signed by a named Partner, or as an unreviewed draft. **The review attaches to a
file, and the content it reviewed exists in two.** That is a question about what a
Partner's name is warranting, and it is the maintainers' to answer, not this
branch's — the pairs are recorded, not merged.

### Delaware's income tax guide was the gross receipts guide

One of the 41 was not a naming artefact. **`us-states/de/de-income-tax.md` had a
body byte-identical to `de-gross-receipts-tax.md`** — same H1, same headings,
throughout. Its frontmatter described something else entirely: the Delaware
individual income tax return on Form PIT-RES, seven graduated brackets, the state
standard deduction, modifications to federal AGI, personal credits.

**A guide that does not exist gets written; a guide that reads as coverage does
not.** Nothing inside the file contradicted its description, because the
frontmatter was the only part that mentioned income tax. Anyone asking about
Delaware income tax — a person skimming the inventory or a model matching on the
description — would have been handed rules for a different tax under a heading
naming that different tax.

The file is now a stub that says so. **The income tax content was not written from
memory**: the bracket table, thresholds, deduction and credits named in the old
description were never in the corpus, and inventing them to fill the hole would
have repeated the original fault in a more confident voice. `de-gross-receipts-tax`
is correct and unaffected.

**When a file's body names a different subject than its frontmatter, the body is
usually telling the truth** — it is the part that was copied, and the frontmatter is
the part someone edited and did not finish.

### Reading article 24 without articles 25 to 28

A review pass corrected two things in the Burundi filing section, and both were
mine. They are recorded because they are the same fault in two costumes.

**Article 22 was over-read.** The claim was that for a non-resident with no
permanent establishment the withholding is final, so "the scale above never
applies". Article 22 makes final the withholding under **articles 119 and 120** —
which are the *occasional employee* rate and the *public-procurement* deduction.
**Ordinary salary from a principal employer is article 117**, and nothing about
lacking an establishment converts it into an article 119 or 120 payment. A
non-resident on ordinary salary is still on the monthly scale.

**Article 24 was quoted without article 25.** The guide said article 24 requires
*"toute personne physique percevant un revenu"* to file annually. Article 25
**dispenses** with that return for a taxpayer receiving only employment income
withheld under article 113, only income withheld under articles 119 and 120, or
both — which is most employees. Article 26 then lets those taxpayers file
voluntarily to reclaim an overpayment under article 29. Stating the general rule
without the exemption told every Burundian employee to file a return they do not
owe.

**Both errors are the same error**: reading a provision without the ones next to
it. Articles 21 to 24 were read carefully and 25 onwards were not opened, and the
page break is the only reason.

Re-reading that page at 300 dpi produced four more provisions absent from every
version so far:

- **Employment income tax is monthly**, not annual — the tail of article 24 fixes
  the taxable period at one month and the deadline at the **15th of the following
  month**, without prejudice to the article 115 recapitulative.
- **A second quarterly threshold**, also in article 24: natural persons with
  turnover **≤ BIF 100,000,000** declare and pay quarterly. That is a
  *filing-frequency* rule, and it is not the Finance Act's **BIF 25,000,000**
  quarterly 1%-of-turnover regime. **Two quarterly tests, two thresholds, two
  purposes** — and a taxpayer between the figures files quarterly without being on
  the 1% regime.
- **Article 27**: medium and large taxpayers must have the annual declaration
  **and each annex** certified by a professional approved by the Ordre des
  Professionnels Comptables.
- **Article 28**: the annual liability is reduced by withholding under articles
  112–116 and 119–120, and by the quarterly provisional instalments under article
  126.

The same review also corrected Armenia, more consequentially. The turnover-tax
table here presented **article 258(1)'s rates as the tax payable**. They are gross
rates, reduced by a documented-expense allowance under article 258(2)–(7) and
floored at a minimum share of turnover under article 260 — so the guide overstated
the tax for any business with costs. The exclusions in article 254(3) and the
related-party tests in article 30 were missing too. **A rate table read out of its
chapter is a plausible-looking answer with the mechanism removed.**

### Cape Verde, resolved — the missing document was a repealed one

The Cape Verde entry above recorded a four-layer dead end and left the
implausible CVE 1 minimum capital flagged rather than fixed. Both halves were
wrong, and the way they were wrong is the transferable part.

**The gazette was never missing.** The register bullet said there is "no `boe.cv`
or `bo.cv`". Those were guesses at a hostname. The Cape Verdean electronic gazette
is **`boe.incv.cv`** — open, free, no login, with a full-text search over every
Boletim Oficial and a `/Bulletins/Download/<id>` endpoint that returns the
complete signed PDF. **A hostname guess that fails is not evidence that a service
does not exist**, and writing one into a register turns a failed guess into a
recorded fact. The rule the register already had — *resolves-but-refuses is not
the same as no DNS* — needs a third case in front of it: **never-asked**.

**The code was not unreachable; it was repealed.** Every search was for the
*Código das Empresas Comerciais*, because that is what the guide cited. That code
— Decreto-Legislativo n.º 3/99, de 29 de março — had its Books II and III revoked
in 2019. The current instrument is the **Código das Sociedades Comerciais**,
Decreto-Legislativo n.º 2/2019, in Boletim Oficial n.º 80, I Série, de 23 de julho
de 2019, alongside a new Código Comercial in the same bulletin. Searching for the
*subject* found it immediately; searching for the *code by name* could only ever
have found a dead document.

This is a check the corpus was not making at all. Every figure-level checker asks
*is this number right?*; none asks *is the instrument this number is attributed to
still in force?* A repealed code fails silently, because the citation stays
well-formed and the figures stay plausible.

**And the flag was right for the wrong reason.** "CVE 1 statutory minimum" for a
Sociedade Anónima was suspicious because a public company should not share a
private one's floor. The real answer is that **neither has a statutory floor**:
article 172(2) and article 237(1) both fix capital freely in the articles, and the
same enacting decree that approved the code expressly revoked **Portaria n.º
17/2013, "que fixa os montantes mínimos do capital social"** — the instrument that
set minimum amounts. The floors that do exist are indirect and were absent from
the guide entirely: a quota may not have a nominal value below CVE 100, a share
below CVE 1,000, an SA formed by public subscription needs CVE 2,500,000 fully
paid, and an SA may not distribute a single escudo of profit until its legal
reserve reaches CVE 2,500,000. **The guide's one suspicious number was less
misleading than the four real constraints it omitted.**

The pay-up split it could not verify — 50% for an Lda, 30% for an SA — turned out
to be right, from articles 176(2) and 238(2). A commercial source being unverified
is not a reason to expect it to be wrong.

### The gazette can be wrong, and the digits-and-words rule caught it first

Cape Verde also produced the cleanest possible vindication of the rule that a
figure is only accepted where **digits and words state it together**.

The Código das Sociedades Comerciais "saiu de forma inexata" and was formally
corrected by **Retificação n.º 133/2019** (Boletim Oficial n.º 101, 1.º
Suplemento, I Série, de 30 de setembro de 2019). Five articles were corrected, two
by an order of magnitude:

- **Article 222(2)** — the audit trigger for an Lda with no supervisory body. The
  gazette printed **CVE 10,000,000 "e/ou"** more than **ten** employees. The
  correction reads **CVE 100,000,000 "ou"** more than **fifty**. Both figures and
  the conjunction were wrong: a factor of ten, a factor of five, and *and/or*
  narrowed to *or*.
- **Article 342(5)** — the large-SA test. The gazette printed **"200.000$00
  (duzentos milhões de escudos)"**. The digits say two hundred thousand; the words
  say two hundred million. **A self-contradicting figure, in the official text.**
  The correction resolves it in favour of the words — CVE 200,000,000 — and lifts
  the net-asset limb from CVE 15,000,000 to CVE 150,000,000.

The lesson runs the other way from the usual one. The digits-and-words rule was
adopted to defend against **OCR**, on the theory that the document is right and
the reading of it may be wrong. Article 342(5) is a case where **the document is
wrong and the rule catches it anyway** — because a figure whose two statements of
itself disagree is unusable whatever the cause, and the only safe response is to
go looking for why. Here, looking found a rectification.

Two smaller habits earned their keep on the same page:

- **Treat structural anomalies in extracted text as signal.** Articles 253 and 254
  begin at paragraph 2 and article 255 at subparagraph b), with no paragraph 1 or
  subparagraph a). The first assumption was a text-extraction artefact. Rendering
  the page at 200 dpi and reading the image showed the printed gazette does this
  too. It is not in the rectification, so it stands: **cite article 254(2), and
  expect no article 254(1) to exist.**
- **A rectification is a separate document with its own gazette entry.** Nothing
  in the 130-page bulletin points forward to it. It was found by searching the
  gazette for the code's name and reading the summaries, and the search returned it
  above the code itself. **After finding a primary text, search the gazette again
  for later acts naming it** — that same search is what confirmed there have been
  no amendments since.
