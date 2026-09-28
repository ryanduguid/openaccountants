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

This fork carries both tiers. The reviewer names and tiers in the frontmatter
came with the guides from upstream; a guide becomes accountant-reviewed here
only when a named, licensed accountant signs it off in a pull request
([CONTRIBUTING.md → Review](../CONTRIBUTING.md#review)), and this fork does not
operate upstream's hosted MCP service. See [COVERAGE.md](COVERAGE.md) for the
counts derived from `index.json` and [PARTNERS.md](../PARTNERS.md), generated
from the same index, for who reviewed what.

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
1. Anyone can open an issue or pull request with the correct figure and a source. (The May 2026 proposal for capturing corrections as structured data was never implemented; it is kept in [archive/CORRECTION-FEEDBACK-LOOP-SPEC.md](archive/CORRECTION-FEEDBACK-LOOP-SPEC.md).)
2. The fix is applied and the contributor gets public credit.
3. With a credentialed practitioner's full review and sign-off, the skill moves from source-cited draft to accountant-reviewed.

## What "reviewed" does NOT mean

- It is **not** tax advice and **not** a filed return — every output is a **working paper** for a human to check.
- A source-cited draft has **not** been reviewed by a credentialed practitioner.
- A review reflects the rules **as of the skill's stated date**; tax law changes — check the date.
- Coverage of a jurisdiction does not imply coverage of every edge case within it.

The product is designed around this honesty: the AI produces a working paper and routes you to a real accountant for sign-off (upstream's hosted service does that through `request_accountant_review`; from this checkout, the working paper goes to the practitioner you choose).

## External verification status

The scripts in `scripts/` compare the corpus against itself: across sibling
guides in one jurisdiction, between the source tree and the generated packages,
and against its own arithmetic. Agreement between copies does not establish
that a tax rule is correct. That requires checking an external source for the
relevant jurisdiction and period. The results below record the September 2026
verification pass, whose dated entries are in the
[verification log](verification-log/README.md); they are not a fresh
independent verification of every guide.

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

## Verification log

The September 2026 pass produced a dated journal of what was checked, against
which source, and what turned out to be wrong: the six VAT errors and what they
had in common, the corporate-rate chart that invented defects, the citations
that named a statute and pointed at an HR platform, the authorities that could
be reached and the ones that could not, and the checkers that were built,
measured against real guides and sometimes discarded. It is
[docs/verification-log/](verification-log/README.md), one dated file per entry
(114 at the split on 2026-09-28), indexed by its README. An entry describes the
tree on its date and is not rewritten when the guides change; the guides and
`docs/guide-migrations.json` say what happened since. To add one, write a new
`YYYY-MM-DD-<topic>.md` there and list it in the README; a test fails on an
unlisted entry.
