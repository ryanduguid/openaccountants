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

The checks in `scripts/` compare the corpus against **itself** — across the three
trees, across siblings inside a jurisdiction, and against its own arithmetic.
They cannot see a figure that every copy agrees on and that is simply wrong.
Closing that gap means asking a source outside the repository, field by field and
jurisdiction by jurisdiction. This records how far that has got, so it is not
re-derived or over-claimed.

### Checked against an outside source

| Field | Coverage | Errors found | Notes |
|---|---|---|---|
| Standard VAT / GST rate | 157 of 157 jurisdictions stating one | 6 | Fiji, India, Kazakhstan, Zimbabwe, Malawi, Maldives |
| Headline corporate rate | ~135 jurisdictions | 3 | Lithuania, Cyprus, Portugal |

Everything else — payroll rates and thresholds, registration and filing
thresholds, filing deadlines, penalty and interest rates, social-contribution
bands, capital allowances, withholding rates, and every form name and statutory
citation — has had **no** external verification pass. Those change on the same
annual cycle as the rates above, and the rates above turned up nine errors.

### What the six VAT errors had in common

Every one was a jurisdiction where an overview or income-tax guide carried the
correct current rate while the **dedicated indirect-tax guide** — the file an
agent loads to prepare a return — did not. Overviews get refreshed from summary
sources; the deep guides do not. `scripts/check-superseded-rates.py` sweeps for
that shape, but two of the six would still have escaped it: Malawi labelled the
stale rate "(2025)" rather than asserting it bare, and Maldives' correct sibling
was an income-tax guide, which its tax-family filter rejects. Both were found by
reading. Treat a clean run as evidence about the checker as much as the corpus.

### What "verified" means here, and what it does not

It means the corpus agrees with a reputable secondary source — usually PwC's
Worldwide Tax Summaries. It does **not** mean a licensed practitioner in that
jurisdiction has confirmed it, and the difference is not theoretical. Twice the
corpus was right and the chart was stale:

- **Eswatini** — PwC lists 27.5%. It is 25% for year-ends after 31 December 2024,
  which both Eswatini guides state, with the date.
- **Nigeria** — PwC gives "30% (large companies)". `ng-cit` carries the whole
  NTA 2025 regime including the abolition of the medium-company band, the 4%
  development levy, and an AUDIT FLASH POINT on the NGN 50M / NGN 100M statutory
  conflict.

- **Fiji** — a chart gave 20%. It is 25% (15% for South Pacific Stock Exchange
  listings), which is what the guide says.
- **Tajikistan** — a chart gave 13% as the rate. 13% applies to
  production-of-goods activities; the standard rate is 18%, and the guide carries
  both with the distinction.
- **Somalia** — a chart gave a flat 15%. It is progressive from 9% to a 30% top
  rate above USD 30,000, cited to the Investment Promotion Office.
- **Sudan** — a chart gave 35%. The guide has 15% standard with 30% for banks,
  tobacco and petroleum, which matches neither half of the chart's figure.

The corporate pass makes the point sharper than the VAT pass did. Its last
tranche of ~35 jurisdictions produced zero corpus errors and six cases where the
aggregator was wrong. Beyond the well-covered jurisdictions, a chart comparison
stops finding defects and starts manufacturing false ones, and each is a chance
to "correct" a right answer into a wrong one. Every hit needs reading before it
is acted on.

A chart comparison is a lead generator, not an assurance mechanism. Only the
Tier 1 route — a named practitioner signing the guide — carries an assurance
claim. Nothing in this section changes a guide's tier.
