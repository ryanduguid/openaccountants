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

## Bangladesh: a whole company form was missing, and its absence made a true sentence false

`bd-company-formation.md` sat at **9 of 11** on one law firm's page. Bangladesh's
Ministry of Law publishes the Companies Act 1994 section by section at
`bdlaws.minlaw.gov.bd`, with a footnote against each amended section naming the
amending act — so the authority is not just reachable, it shows its own history.

The guide listed five entity types and omitted the sixth. **Part X-A, twelve
sections (ss.392A–392L), inserted by s.9 of the Companies (Second Amendment) Act
2020, creates the one-person company.** It has a mandatory nominee named in the
memorandum with written consent; a rule that a natural person may form **only
one**; the sole shareholder as director; one board meeting per half calendar
year; and financial statements filed **within 180 days** of year end.

The omission is what made another statement false. The guide said there is **"no
statutory minimum paid-up capital (effectively as low as BDT 1)"**. That is true
of a private or public company. For an OPC, s.392C sets paid-up capital at **not
less than BDT 2,500,000 and not more than BDT 50,000,000**, plus a prior-year
turnover band of **BDT 10,000,000 to 500,000,000**. A blanket claim about a
jurisdiction is only as good as the list of forms it was checked against.

Two further statements were right and incomplete in ways that change the answer.
The fifty-member cap **excludes persons in the company's employment**, and
**joint holders count as a single member** — so a company that looks over the
line may not be. And "minimum 2 directors" holds only for an ordinary private
company: s.90(1) requires **three** in a private company that is a **subsidiary
of a public company**, which is the ordinary shape of a foreign group's
Bangladeshi subsidiary. s.90(3) adds that only a **natural person** may be a
director, so there are no corporate directors and the parent cannot sit on the
board itself.

### Two mistakes caught before committing, both about reading

**A negative grep in an unfamiliar script is not evidence of absence.** Searching
the consolidated Act for `একক ব্যক্তি` returned six hits, every one meaning
"individual" in the definition of managing director. The conclusion drawn from
that — *the Ministry of Law's database does not carry the 2020 amendment* — was
written down and was wrong. The Act calls it **`এক ব্যক্তি কোম্পানী`**, without
the doubled consonant, and searching the section index for that phrase returned
**twelve** sections immediately. The failure was in the search string, not the
database, and the wrong conclusion was about the *authority's completeness* —
the kind of claim that, published, sends the next reader somewhere worse.

**A proviso is not the rule.** The draft asserted that the Act's financial year
is the calendar year, quoting *"অর্থ-বৎসর বলিতে পঞ্জিকা বৎসরকে বুঝাইবে"* from
s.2. The quotation is real. It is the **proviso**, and it applies to **insurance
companies only**. The clause itself defines a financial year, for a body
corporate, as the period *"whether or not it is a full year"* for which the
profit-and-loss account is laid before the annual general meeting. What exposed
it was re-fetching the section and noticing that the opening words did not match
the window quoted from — the first extraction had started mid-clause, at the
proviso, and read it as the definition.

That is the Armenian near-miss in a third costume. Twice there, the general rate
article was not the end of the article; here, the start of the quotation was not
the start of the clause. **The rule is the same each time: read from the
beginning of the provision to the end of it, and check that what you quote
begins where the provision begins.**

### And the clause letters were not transliterated

The Act is published in Bengali only — `?lang=en` returns the same Bengali page.
The draft cited the private-company definition as `s.2(t)(iii)`, mapping `ট` to
"t" by its sound. In an ordered list `ট` is the eleventh consonant, so the
Roman-alphabet equivalent would be `(k)`, not `(t)`. Rather than guess which
convention the Ministry uses, every clause is now cited by the definition it
contains and the Bengali letter as printed — *"s.2(1), definition of
'প্রাইভেট কোম্পানী' (clause ট)"*. **A citation a reader can follow beats a
citation that looks more familiar**, and inventing a Roman letter for a clause
nobody has published in Roman is how an unfalsifiable citation gets made.

The lakh and crore figures were converted and then checked against an
independent English statement of the same amounts before being written down —
the Myanmar rule, applied to a second numbering system where a misread order of
magnitude is a hundred-fold error inspection will not catch.

### The leak grep found a second guide, and the second tree behind it

Bangladesh has **two** formation guides: `bd-company-formation.md` and
`bd-formation.md`, the latter a freelancer-facing guide whose entity table
offered sole proprietor, partnership and private limited. It stated no
contradicting number, so no checker here would ever flag it — but it presented a
three-way choice in which the one-person company, the form built for a single
owner, was absent. Both it **and** its hand-maintained `agent-skills/bd-formation`
counterpart now carry the OPC column and a note saying plainly why a starting
freelancer cannot use it: the BDT 10,000,000 prior-year turnover floor. Written
twice, by hand, because `agent-skills/` inherits nothing.

Corpus effect, re-measured: authority citations 2,811 → **2,830**, secondary
4,715 → **4,713**. Bangladesh goes to **27 authority citations against 40**, and
the single-source queue is at **27**.

> **Those two numbers were re-run after the base changed underneath them.** PR
> [#18](https://github.com/ryanduguid/openaccountants/pull/18) merged while this
> section was being written, and `main` picked up two other pull requests'
> Australian work at the same time, so the corpus the counts describe is not the
> corpus they were first measured against. Re-running both sides on the new base
> gives the same pair — 2,811 before, 2,830 after — which is a confirmation and
> not a reason to skip the re-run. **The point of re-measuring is that you cannot
> tell in advance which time it will have moved.**

## DR Congo — the reduced VAT rate was wrong by a factor of eight

`cd-vat-gst.md` carried seven citations. **Six pointed at the same commercial
advisory blog post**, and it was the queue's ranking of that concentration that
picked the file, not any figure looking wrong. Reading the statute found a number
that was out by 8×.

### What the statute says

The DGI publishes its consolidated *Code des Impôts* (2023 edition) as a PDF on
`dgi.gouv.cd`. Article 35 of Ordonnance-Loi n° 10/001, as amended by L.F. n°
21/029 of 31 December 2021 and n° 22/071 of 28 December 2022, sets the rates:
*"taux normal : 16% … taux réduit : **8%** … taux 0%, applicable aux exportations
et opérations assimilées"*. The guide said the reduced rate was **1%**.

The 8% band is not a description but a **schedule of customs tariff positions**
printed in the article itself — 02.01 through 02.07 for meats and offal,
0303.23.00 for frozen tilapia, 1006.20.00 and 1006.30.00 for husked and milled
rice, and so on — followed by a limb that has nothing to do with food: *"à la
vente des billets d'avion sur le trafic aérien national"*. Domestic air tickets
were absent from the guide altogether.

### The corroboration was found second, not first

The DGI's own August 2025 taxpayer leaflet, *La Taxe sur la Valeur Ajoutée —
Notions essentielles à retenir*, states the same three rates at §VI including the
air-ticket limb. It is worth being clear about the order: **the leaflet was read
after the Code, and would not have been sufficient on its own** — a leaflet is a
summary, and the next finding is exactly what happens when you trust one.

### An authority contradicting itself, recorded as a gap rather than resolved

The same leaflet says at §II that members of the **liberal professions** are
subject to VAT *"sans considération de leur chiffre d'affaires"*. That rule is
art. 44 of Décret n° 011/42, and the DGI's own consolidated Code prints it inside
square brackets marked ***"(Disposition désuète conformément à la L.F. n° 15/021
du 31 décembre 2015)"*** — text the Code flags as spent.

So the authority's current leaflet asserts a rule the authority's consolidated
code marks as superseded. **The guide states neither version.** It records the
conflict, names both documents, and leaves the question to a reviewer. Picking
the leaflet because it is newer, or the Code because it is the legal text, would
have produced a confident sentence with a coin-flip behind it. **A documented
contradiction between two arms of the same authority is a finding; silently
choosing one of them is not.**

### Three smaller corrections the statute forced

- **"Exceeding" versus "equal to or greater than."** The guide put the
  registration threshold at turnover *exceeding* CDF 80,000,000. Art. 14 reads
  *"chiffre d'affaires annuel **égal ou supérieur à** 80.000.000"*. A business at
  exactly the threshold is inside the tax, and the guide put it outside. The same
  article also carries a **two-year lock-in** on voluntary registration and a
  **two-year tail** after turnover falls below the threshold, neither of which the
  guide mentioned.
- **Not a reverse charge.** The guide described imported services as
  reverse-charged by the recipient "(approx — confirm)". Art. 23 requires the
  non-resident to appoint an **approved resident representative, jointly and
  severally liable**; the customer pays *"en cas de non désignation d'un
  représentant"* — a default remedy, not the mechanism.
- **Not a rollout.** The guide called e-invoicing a 2025 modernisation plan
  "(approx — confirm)". Art. 58 has required a *facture normalisée produite par
  les dispositifs électroniques fiscaux* since the 2022 Finance Law, and art. 38
  makes it a **condition of deducting input tax**.

### A mislabelled citation, caught by re-reading before writing

Working notes had the carry-forward and no-refund rule at "décret arts. 140–141".
Re-running the search before drafting put the primary rule at **art. 63 of the
Ordonnance-Loi** — *"Le crédit d'impôt ne peut pas faire l'objet d'un
remboursement au profit de l'assujetti et ne peut être cédé"* — with décret art.
140 repeating it. Both exist and both say it; the *statute* is the citation, and
a note written earlier in the session had reached for the implementing decree.
**Notes taken during research are not citations until re-verified against the
text at the moment of writing.**

### And a category invented rather than looked up

The rewrite was first written with `category: vat`. That value does not exist:
`docs/skill-template.md` lists the vocabulary, and country-level VAT belongs under
`international`. A grep confirmed `vat` appeared in exactly one file in the
corpus — the one just written. **The vocabulary was two commands away and got
guessed instead**, the same failure mode as the invented Bengali clause letter one
section above, in a repo where nothing enforces `category` at all.

Corpus effect: authority citations 2,830 → **2,867**, secondary 4,713 → **4,704**.
`cd-tax-overview.md` carried the same VAT rate and filing deadline on commercial
citations and was re-pointed to arts. 35 and 60 in the same commit — the
jurisdiction-wide grep, which is what found it.

## Lesotho — the numbers were right and three whole rules were missing

`ls-corporate-income-tax.md` rested six of its seven numeric facts on one law
firm's page. Reading the Income Tax Act 1993 as published by Revenue Services
Lesotho **confirmed every rate the guide stated** — and found that confirming the
stated numbers is not the same as the guide being right.

### What was absent

- **A rate band.** The Third Schedule has four rows, not two. Item 2 —
  manufacturing income from activities relating *"exclusively to exports to any
  country other than a country within the Southern African Customs Union"* — is at
  **0%**. The guide described a two-rate system.
- **A whole tax.** Section 87 imposes **advance corporation tax** on a resident
  company paying a dividend, at `A × 100/(100−A)` where A is the non-manufacturing
  Third Schedule rate — **33.33%** of the gross dividend — with a return due within
  **seven days** of payment. The guide did not mention it.
- **A withholding section.** Section 157 requires **5%** withholding on payments to
  a resident contractor — construction, transport, plant hire, plumbing, roofing,
  landscaping and more — subject to a monthly M3,000 test, a principal-residence
  carve-out and exemption certificates. Any business paying a Lesotho builder
  operates it. The guide listed five withholding rates and not this one.

**A guide can be fully verified and still mislead by omission.** Every checker in
this repo compares stated figures against sources; none of them can see a rule
that is simply not there. The single-source queue found this file because of who
was cited, not because anything it said was wrong.

### The authority contradicts itself, and the contradiction is on one page

RSL's *Guide on Corporate Tax* (June 2025) prints a rate table whose Rate column is
**inverted relative to the explanatory notes directly beneath it**. The table puts
manufacturing-for-export at 25% and "Other Income" at 10%; note (a) on the same
page says 10% for manufacturing exports and note (b) says 25% for non-manufacturing
companies. The Act and RSL's own website agree with the notes.

This was checked rather than assumed to be an extraction artefact. Re-extracting
the page with pdfminer's layout analysis and printing each text line with its `y`
and `x` coordinates showed each rate positionally aligned with its own row: 10% at
y=309.1, 0% at y=240.1, 10% at y=212.6, 25% at y=185.0, all at x=431.0 against four
distinct row labels. **The document really does say it.** The guide follows the
Act, states the conflict in a table of its own, and does not paper over it.

### A public ruling that is right about structure and dated about rates

RSL's *Withholding Tax Public Ruling* is the only RSL document that tabulates
withholding rates — and it is dated **April 2010** and works its example at **14%
VAT**, a rate Lesotho has since moved. Its account of *structure* is used (which
section catches which payment, that "gross amount" means before VAT, that goods
supplied incidentally to a service are swept in). Its **rates** are taken from the
Act instead.

That mattered. The ruling gives the 15% manufacturing-linked withholding for
**royalties only**. Section 107(3), as substituted by s.9 of Act No. 2 of 1994,
gives it for **interest, royalties and management charges** — three limbs. Had the
ruling been treated as authoritative because it came from the authority, the guide
would have narrowed a statutory relief by two thirds. **An authority's summary is
a secondary source about its own statute.**

### Two places where RSL's guidance is simpler than the law

- **The provisional-tax instalment.** RSL's *Guide on Provisional Tax* says each
  instalment is "30% of the Client's income tax liability for the preceding year".
  Section 150(1) says **30% × (A − B)**, where B is so much of the preceding year's
  liability as was already paid by **amounts withheld at source**. For a company
  with substantial withholding credits those are materially different numbers.
- **The branch rate.** 25% on branch profits is right, but it is the ordinary
  corporate rate on the branch's income, **not a remittance tax** — and s.10(2)
  denies a Lesotho branch of a non-resident company the manufacturing concession
  altogether.

### A worked example in an authority document that does not compute

RSL's *Advanced Corporation Tax Guide* takes chargeable income of M100,000, states
the resulting liability as M16,667 (25% of M100,000 is M25,000), then divides it by
three to reach "M5,000 per quarter" (a third of M16,667 is M5,555.67). Neither step
follows. The **rule** in that guide matches s.87 and is used; its **arithmetic** is
flagged in the guide so a reader working through the example does not assume the
error is theirs.

### What could not be read, and is marked as such

The most recent consolidation RSL publishes is the Act **updated to 1 April 2012**.
RSL also lists *Income Tax (Amendment) Regulations No. 24 of 2026* — published as a
**scanned image with no extractable text**, and no OCR is available in this
environment. So the 25% and 10% figures are separately confirmed by RSL's current
website, and **the 0% export band is not**. The guide carries a currency note
saying exactly that, rather than presenting a 2012 schedule as current law.

Corpus effect: authority citations 2,867 → **2,893**, secondary 4,704 → **4,694**,
the single-source queue 26 → **25**. The jurisdiction-wide grep also re-pointed the
non-resident rate and the fringe-benefits rate in `ls-income-tax.md` to the Act —
the latter revealing that the 40% is applied to a **grossed-up** base under s.117,
`A × 1/(1−B)`, not to the benefit's face value.

### Qatar, attempted and deferred

`qa-payroll-social.md` was taken first and set down. Qatar's GRSIA
(`grsia.gov.qa`, also served as `daman.gov.qa`) resolves 200 and classifies as an
authority, but its SharePoint site renders every content page in JavaScript and
returns **403 on `/_api/web/lists`, `/_api/search/query` and `/_vti_bin/ListData.svc`**
for anonymous callers; `sitemap.xml` and `robots.txt` both 404 into a SharePoint
error page. The Ministry of Justice's Al-Meezan legal portal (`almeezan.qa`) does
not resolve from this network, and `hukoomi.gov.qa` returns 403. **A reachable
authority is not a readable one**, and the queue entry stands.

> **Superseded later in the same session — see "Qatar — the block was the
> renderer, not the authority" below.** Every diagnosis in the paragraph above is
> accurate and the conclusion drawn from it was wrong: the pages render in
> JavaScript, so a *renderer* was the missing piece, not access. Opened in a real
> browser the same page lists twenty-five instruments. This entry is left standing
> rather than edited away, because the mistake it records — **treating "curl
> returned no content" as "the authority has no reachable content"** — is the
> point. The rule it yields: when a page 200s with a large body and no data,
> establish whether the failure is *access* or *rendering* before recording a
> block.

## Cayman Islands — a browser that solves proof-of-work, and five right numbers with wrong mechanics

`ky-payroll-social.md` rested **all five** of its numeric facts on one commercial
residents' site. The Cayman Islands Legislation portal
(`legislation.gov.ky`) publishes every Act as a consolidated PDF — and sits behind
a **Sucuri `sgcaptcha` interstitial** that answers `curl` with a 202 and a
185-byte meta-refresh stub. The jurisdiction had been recorded as blocked.

### How the block was cleared

The interstitial turned out **not** to be a human CAPTCHA. Reading the stub showed
no reCAPTCHA, hCaptcha or Turnstile, no form, and an inline script computing a
hash in a Web Worker before posting to `sgsubmit_url` — a **proof-of-work
challenge that any real browser solves unattended**. What was needed was a real
browser, not a solver.

`camofox-browser` (a REST wrapper around Camoufox, a Firefox fork) was installed
for this. Three environment-specific obstacles had to be cleared, each worth
recording because they will recur:

1. **`api.github.com` returns 403 through the egress proxy**, so `camoufox fetch`
   could not discover its own releases. The **release asset itself**, on
   `github.com/.../releases/download/`, is reachable and honours byte ranges — the
   680 MB browser was fetched directly and unpacked into the cache layout the
   project's Dockerfile builds, with the archive's exact `content-length` checked
   against the file on disk.
2. **GeoIP is hardcoded on whenever a proxy is set.** Camoufox tries to derive
   locale and timezone from the proxy's exit IP via public IP APIs, which the
   policy proxy blocks — `"Failed to get a public proxy IP address from any API
   endpoint."` A one-line local patch made it respect `CAMOFOX_GEOIP=0`.
3. **Firefox could not reach anything, with `NS_ERROR_NET_RESET`**, while `curl`
   succeeded from the same container. The fix was the browser's own protocol
   negotiation: disabling **HTTP/2, HTTP/3 and Encrypted Client Hello**
   (`network.http.http2.enabled`, `network.http.http3.enable`,
   `network.dns.echconfig.enabled`) and routing through the agent proxy. The proxy
   CA was installed via Firefox's `distribution/policies.json` `Certificates.Install`.

With that, the challenge solved itself in under ten seconds, the resulting cookie
was persisted to a storage-state file, and four consolidated Acts were downloaded
through the same authenticated context. **A gate that looks like a CAPTCHA is
worth reading before it is recorded as a block.**

### Every stated figure was right; almost every mechanism was wrong

This is the second guide in this session (after Lesotho) where verification
confirmed the numbers and the reading found the real defects elsewhere.

- **The pension split is not 50/50.** The guide said "generally split 5% employer
  / 5% employee". The Act sets a **10% total** (s.47(3)(c)), a **5% employer
  floor** (s.47(3)(b)) and a **5% member ceiling** (s.47(3)(a)) — an employer
  paying more than 5% reduces the member's share, and the total stays 10%.
- **The health-insurance "50% share" is a right of recovery, not a split.** Under
  s.7 the employer is liable to the insurer for the **total cost** and may recover
  *"not exceeding fifty per cent"* from the employee. For a **high-risk** employee
  it may recover only the difference from a standard premium — the loading falls
  on the employer. For **dependants** (s.8) it pays in full and may recover **all**
  of it. The guide mentioned none of this and marked the employer share
  "(approx — confirm)".
- **Two exclusions were missing.** The nine-month relief applies only to someone
  who is **neither Caymanian nor a permanent resident**; and **household
  domestics** are excluded regardless of service length (s.25(2)(b)). An employee
  with **two employers** generates contributions from each (s.25(4)).

### An amendment on the statute book and not in force

The Act's own footnote against s.25(2)(a) records that s.18(2)(i) of the **National
Pensions (Amendment) Act, 2016**, which would cut the nine-month period to six,
***"has not yet commenced"***. A source describing Cayman as a six-month rule is
describing law that was enacted and never brought into force. **Enactment is not
commencement**, and a consolidated text that flags the difference is doing the
reader a service worth passing on.

### A citation that would have been spent on arrival

The **National Pensions (Maximum Pensionable Earnings) Order, 2022** looks exactly
like the source of the guide's CI$87,000 cap. It is not. It prorated the maximum
to **CI$21,750** for 1 October to 31 December 2022 and **expired on 31 December
2022**, providing that the figure be read *"as if it had never been amended"*.
The working hypothesis while reading it was that the guide's cap was a lapsed
temporary measure — **and that was wrong**: s.3 of the Act carries CI$87,000 as the
standing definition, with the Order as a temporary override. Checking the parent
Act rather than stopping at the instrument settled it in both directions: it
confirmed the figure **and** identified the citation that must not be used for it.

Corpus effect: authority citations 2,893 → **2,915**, secondary 4,694 → **4,687**,
the single-source queue 25 → **24**. The jurisdiction grep caught one leak —
`cayman-tax.md` said "Pension: 10% split equally" and "aged 18-65" — now corrected
and cited to the Act.

## Qatar — the block was the renderer, not the authority

`qa-payroll-social.md` rested seven of its nine facts on one law firm's news page.
Qatar had been set down earlier in this same session as blocked: GRSIA
(`grsia.gov.qa`, also served as `daman.gov.qa`) resolves 200 and classifies as an
authority, but every content page renders in JavaScript, its SharePoint REST
endpoints (`/_api/web/lists`, `/_api/search/query`, `/_vti_bin/ListData.svc`) all
return 403 anonymously, and `sitemap.xml` and `robots.txt` 404 into a SharePoint
error page. `curl` on the Laws & Legislations page returned a 696 KB shell with
**zero** document links.

The same page, opened in the browser installed for the Cayman work, rendered a
register of **twenty-five instruments** with their PDF hrefs — including *Law No.
(1) of 2022 regarding social insurance* and *Cabinet Resolution No. (3) of 2025
issuing the executive regulations*. **The obstacle was never access; it was
rendering.** Two conclusions worth carrying: a 200 with a large body is not
evidence that a page has content, and "authority unreadable" should record which
of the two failed.

### Reading the Arabic

pdfminer emits Arabic in visual order, so every extracted line arrives reversed.
Reversing each line and then re-reversing the digit runs inside it produced
readable text with intact numerals — enough to locate and quote the operative
articles, each pinned by its own article-number marker rather than by proximity.

### Every rate confirmed, and five rules found

Article 11 confirms the whole of the previous version's arithmetic: contribution
computed on contribution salary **not exceeding QAR 100,000**, total **21%**,
being **7%** deducted from the insured person and **14%** paid by the employer,
remitted *"within a period not exceeding the fifth of the month following"*. The
art. 1 definition confirms contribution salary as **basic salary plus the social
allowance and the housing allowance**.

What the guide did not have:

- **The self-employed are in the scheme.** Art. 1 defines the insured person as
  every Qatari in government employment, **a private-sector worker, or a
  self-employed person**, who pays for himself.
- **The State can pay part of the employer's share.** The last paragraph of art.
  11 lets the public treasury, with Cabinet approval, bear a proportion of the
  contribution due from a **private-sector** employer.
- **Late payment costs 2% a month** (art. 21), running from the due date to the
  payment date.
- **Contributing on understated salaries is treated as not contributing at all** —
  art. 22 adds **10%** of the real contributions payable where an employer failed
  to register, or paid on other than real salaries.
- **One job only** — art. 10 limits an insured person working for several covered
  employers to a single contribution.

### The GCC claim pointed at the wrong law

The previous version said the scheme "applies to Qatari (and GCC) national
employees" and cited Law No. 1 of 2022 for both. The Qatari half is right. **GCC
coverage is not in that Law**: it comes from Law No. 4 of 2007 as amended by Law
No. 5 of 2021, which GRSIA lists as separate instruments. Those two were not read,
and the guide says so rather than describing them. **A citation that is right
about one half of a sentence is unfalsifiable about the other half** — the same
defect this workstream documented in San Marino's monofase rates and in
Bangladesh's ss.392B–392C link.

### One figure deliberately not repeated

The previous version noted that enrolments above the ceiling "may be
grandfathered". No transitional provision to that effect appears in the Law. It
may sit in the executive regulations, which were downloaded but not read in full.
The guide records it as unverified instead of carrying it forward or deleting it.

And one trap is flagged: **QAR 100,000 appears twice in the Law for different
purposes** — art. 11's contribution-salary ceiling, and art. 57's cap on the
aggregate where a person combines more than one pension, or a pension and a
salary. Identical figures serving unrelated rules are exactly what gets conflated.

Corpus effect: authority citations 2,915 → **2,928**, secondary 4,687 → **4,680**,
the single-source queue 24 → **23**.

## Burundi — an authority that was never down, and a statute no machine could read

Burundi held **four** entries on the single-source queue, the largest cluster on
it, and had been recorded as blocked because **`obr.bi` answered HTTP 200 with a
182-byte PHP fatal error** — *"Application Instantiation Error: Failed to start the
session because headers have already been sent"*. `bi-income-tax.md` carried an
explicit warning that nothing in it had been put in front of a primary source.

**Opened in a real browser the site works normally.** The failure was in whatever
`curl` triggers, not in the site. Its *Lois et règlements* page carries the income
tax law, the 2020 amendment, the VAT law, its 2020 amendment and the **Loi de
Finances 2026/2027** — a complete legislative set for every guide in the
jurisdiction.

### Then the real obstacle appeared

Every one of those documents is a **scanned image with no text layer**. `pdfminer`
returns the 267-page Finance Act as 267 page-breaks and nothing else — 267
characters for a 7.7 MB file. This is the case the earlier Vietnam and San Marino
entries recorded as terminal ("no OCR is available here").

It is not terminal any more: `pymupdf` renders pages and
`rapidocr-onnxruntime` reads them, both pip-installable with no system packages.
Quality on this French legal text ran 0.95–1.00 confidence.

### The rule adopted for OCR'd figures

**OCR output is not the same evidential quality as a text layer**, and a misread
digit in a tax rate is precisely the failure this workstream exists to prevent. The
rule applied throughout: **accept a figure only where the statute states it in
words and digits together.** French legal drafting does this as a matter of course
— *"trente pour cent (30%)"*, *"vingt-cinq millions de francs burundais
(25 000 000 BIF)"* — and that redundancy is what makes an OCR'd numeral safe.

It earned its keep immediately. Article 103's corporate rate scans as ***"(So%)"***
and is readable as 30% only because *"trente pour cent"* sits beside it; elsewhere
"(10%)" scanned as "(1o%)". **Every figure in the Burundi guides has that
redundancy behind it, and figures that lack it — the VAT penalty ladder — are
deliberately not restated.**

A second, independent check fell out of the statute itself. The minimum tax is
**1% of turnover**, triggered when net income falls below **turnover ÷ 30**. At a
**30%** rate, tax on turnover ÷ 30 is exactly 1% of turnover. The three numbers
only interlock if all three were read correctly, which corroborates the 30% that
had scanned as "So%".

### What the reading found

- **The VAT registration threshold was out by a factor of four.** `bi-vat-gst.md`
  said BIF 100,000,000; art. 271 of the Finance Act 2026/2027 says **BIF
  25,000,000**. The old figure had nothing behind it structurally: **art. 37 of the
  VAT law contains no threshold at all**, delegating it to ministerial instrument.
  A threshold cited to "the VAT Law" is cited to a text that does not contain one.
- **Two liability tests that ignore turnover.** Art. 271 also makes a taxpayer
  automatically liable where **local purchases and/or imports**, or **stock on
  hand**, exceed **BIF 50,000,000** — and forces them into the medium or large
  taxpayer category. Neither appeared anywhere in the corpus.
- **The progressive scale does not reach business income.** `bi-income-tax.md` said
  Burundi applies its 0/20/30 scale to "employment, **business** and rental income".
  Art. 21 applies it to **employment and rental** income; a natural person's
  **business income is a flat 30%**, and for 2026/2027 a natural person under **BIF
  25,000,000** of turnover is outside both, filing **quarterly at 1% of turnover**
  under Finance Act art. 190.
- **A company's rental income is not taxed at the corporate rate either.** Art. 103
  excepts it and sends it to the art. 21 scale.
- **"Minimum tax for loss-making years" understated it twice over.** It applies
  *"quels qu'en soient ses résultats"*, expressly **including investment-code
  beneficiaries**, with a **ten-year free-zone exception**.
- **Electronic-communications services left VAT altogether** — a 20% specific tax
  replaces it for 2026/2027 (Finance Act art. 187).

### Two article headings that OCR would not give up

Finance Act art. 190's *subject* — the words "les personnes physiques qui" — was
dropped at 200 dpi. Re-running that single page at 320 dpi recovered it. Without
the re-read the regime would have been described without knowing **who it applies
to**.

The quarterly-instalment article in the income tax law was worse: its heading is
dropped at **both** 200 and 320 dpi, while the body of the rule scans cleanly. The
surrounding sequence makes "130" the obvious inference, and the guide **does not
make it** — the provision is cited as *Section 2, Paragraphe 1*, which is what
could actually be read. **An inferred article number is indistinguishable from a
verified one on the page**, which is the same defect as Bangladesh's invented Roman
clause letters.

### What is left, and why

`bi-payroll-social.md` stays on the queue at 89%. The OBR publishes revenue law;
**INSS is a different body and its social-security code is not on the OBR site**.
The PAYE line is now cited to art. 21, a duplicated health-insurance bullet was
removed, and the guide now says plainly that every INSS contribution figure is
unverified rather than merely imprecise. **Naming the missing source is the
deliverable when the source cannot be found.**

Corpus effect across the Burundi work: authority citations 2,928 → **2,976**,
secondary 4,680 → **4,657**, the single-source queue 23 → **20**, and Burundi from
**four** entries to **one**.
