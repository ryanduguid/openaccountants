# Coverage

**This file is the record of this repository's coverage numbers, derived from
`index.json`.** Every other surface that states a count (the README headline,
`llms.txt`, `docs/QUALITY-TIERS.md`, the generated `PARTNERS.md`) is checked
against the same index by `scripts/check-coverage-claims.py`, a CI gate; when a
document and the tree disagree, the tree wins and the document is fixed.

Upstream's own figures (openaccountants.com's production database: "1,000+
skills across 192 jurisdictions", 85 accountant-reviewed) described a different
corpus and sat in this file as a frozen June 2026 snapshot until 2026-09-28.
They are not restated: this fork does not operate the platform, and git history
holds the old tables.

## This repository (derived from `index.json`)

Regenerate with `python3 scripts/build-index.py`; the `counts` block at the top
of `index.json` carries the first three rows, and the gate checks every row.

| Measure | This tree |
|---|---|
| Guide files indexed | **1,865** |
| Distinct `jurisdiction` codes | **243** |
| `tier: 1` (accountant-reviewed) | **164** |
| `tier: 2` (source-cited draft) | **1,701** |
| Distinct `reviewed_by` values | **29** (one spelling each; Aryee, Amiridze and Mat Hussin were previously recorded two ways and are now normalised to `Name, Credential`) |
| Country directories under `skills/international/` | **184** |
| US jurisdiction codes (`US` + 50 states + DC) | **52** |
| Generated bundles under `packages/` | **255** |

US coverage is complete at state level: all 50 states plus DC are present.
Accountant-reviewed guides exist in 24 of the 243 jurisdiction codes;
[PARTNERS.md](../PARTNERS.md), generated from the index with the one counting
rule (`tier: 1` plus a named reviewer), lists them per reviewer and per
jurisdiction.

### Guides two tax years behind

Seven guides carry `tax_year: 2024`, the oldest in the corpus. They are correctly
labelled — the spec defines `tax_year` as the coverage *start* year, so 2024 is
right for a 2024-25 or 2024/25 guide — and each states the year it covers in its
own quick-reference table, so nothing in them is presented as current when it is
not. They are a coverage gap, not an error:

| Guide | Covers | Current period as at this writing |
|---|---|---|
| `au-individual-return` | 1 Jul 2024 – 30 Jun 2025 | 2025-26 is the lodgment year |
| `au-medicare-levy` | 2024-25 | 2025-26 |
| `hk-salaries-tax` | YA 2024/25 | YA 2025/26 |
| `hk-mpf` | 2024 | 2026 |
| `bangladesh-pit` | 2024 (1 Jul – 30 Jun) | 2025-26 |
| `ghana-pit` | 2024 calendar year | 2026 |
| `thailand-pit` | 2024 calendar year | 2026 |

Regenerate this list with:

```
python3 -c "import json;d=json.load(open('index.json'));print(sorted(g['slug'] for g in d['guides'] if str(g.get('tax_year')) <= '2024' and g.get('tax_year')))"
```

Everything else in the corpus is on `tax_year` 2025 (1,665), 2026 (119), or is
year-agnostic and carries none (74).

> **One open maintainer call.** 99 guides carry a named `reviewed_by` while
> marked `tier: 2`. The enforced contract permits that, but 93 of them also
> carry `review_status: current`, which means `tier: 1` everywhere else, so a
> reader cannot tell from the frontmatter whether they were reviewed. None of
> them counts as reviewed anywhere in this repository until the call is made.
> See [QUALITY-TIERS.md](QUALITY-TIERS.md).

## Where the defects were

The branch-wide fact-check of September 2026 found that arithmetic and rate
tables held up and that identifiers, labels and citations did not: Malta's
numbers were never wrong while its form names, a deadline and its statutory
citations were. The account, and why a checker cannot close that gap, is the
verification-log entry
[Where the defects actually were](verification-log/2026-09-09-where-the-defects-actually-were.md);
[FORM-REGISTER.md](FORM-REGISTER.md) is the reading aid it recommends.

## How to update this file

The derived table is hand-written but machine-checked. When a change to
`skills/` moves the counts, `scripts/check-coverage-claims.py` names the row and
the tree's value: update the row, the headline line in `README.md`, `llms.txt`
and `docs/QUALITY-TIERS.md`, regenerate `PARTNERS.md` (`make build`), and run
the gate until it passes. The tax-year list and the maintainer-call figures are
not gated; the commands beside them re-derive them.
