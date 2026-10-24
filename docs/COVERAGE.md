# Coverage

Country and territory guide presence is tracked separately in
[COUNTRY-COVERAGE.md](COUNTRY-COVERAGE.md), against a dated authoritative
geographical catalogue. The jurisdiction totals below include US states and
global or cross-border labels and do not establish comprehensive country coverage.

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
| Guide files indexed | **1,949** |
| Distinct `jurisdiction` codes | **251** |
| `tier: 1` (accountant-reviewed) | **164** |
| `tier: 2` (source-cited draft) | **1,785** |
| Distinct `reviewed_by` values | **29** (one spelling each; Aryee, Amiridze and Mat Hussin were previously recorded two ways and are now normalised to `Name, Credential`) |
| Country directories under `skills/international/` | **192** |
| US jurisdiction codes (`US` + 50 states + DC) | **52** |
| Generated bundles under `packages/` | **263** |

Guides are present for all 50 US states and DC.
Accountant-reviewed guides exist in 24 of the 251 jurisdiction codes;
[PARTNERS.md](../PARTNERS.md), generated from the index with the one counting
rule (`tier: 1` plus a named reviewer), lists them per reviewer and per
jurisdiction.

### Guides with earlier period labels

Five guides carry a `tax_year` of 2024 or earlier. These are the indexed
period labels; they do not establish current law or complete topic coverage.
The Anguilla payroll draft explicitly requires verification of the applicable
law before calculating an engagement liability from its 2022 baseline.

| Guide | Indexed `tax_year` | Reference scope |
|---|---|---|
| `ai-payroll` | 2022 | Statutory consolidation as at 31 December 2022 |
| `bangladesh-pit` | 2024 | Personal income tax |
| `hk-mpf` | 2024 | Mandatory Provident Fund |
| `hk-salaries-tax` | 2024 | Salaries tax |
| `thailand-pit` | 2024 | Personal income tax |

Regenerate this list with:

```
python3 -c "import json;d=json.load(open('index.json'));print(sorted(g['slug'] for g in d['guides'] if str(g.get('tax_year')) <= '2024' and g.get('tax_year')))"
```

The other guides carry `tax_year` 2025 (1,591), 2026 (278), or no year (75).

> **Names on tier-2 guides.** 99 guides carry a named `reviewed_by` while
> marked `tier: 2`. The name records corrections an accountant contributed
> without signing the whole guide off, and none of them counts as reviewed
> anywhere in this repository. Since 2026-09-29 every one of them carries
> `review_status: pending_review`, and the validator rejects `current` on a
> tier-2 guide: `review_status` is review freshness, `tier` is the quality
> state. See [QUALITY-TIERS.md](QUALITY-TIERS.md). Regenerate the count with:
>
> ```
> python3 -c "import json;d=json.load(open('index.json'));print(sum(1 for g in d['guides'] if str(g.get('tier'))=='2' and g.get('reviewed_by') and g['reviewed_by'].strip().lower() not in ('pending','none','no','false','-','n/a','tbd')))"
> ```

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
the gate until it passes. The tax-year list and the tier-2 names figure are
not gated; the commands beside them re-derive them.
