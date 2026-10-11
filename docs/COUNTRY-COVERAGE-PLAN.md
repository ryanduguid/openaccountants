# Completing country and territory packs

Every country and territory in [the coverage inventory](COUNTRY-COVERAGE.md) needs a sourced pack that explains its applicable tax and accounting rules. The inventory reports guide presence. It does not certify that a pack is complete.

## What a complete pack must cover

A pack may combine related topics in one guide when that is clearer. Each applicable topic needs substantive rules, primary sources and operational limits:

| Topic | Required content |
|---|---|
| Tax-system scope | Territorial reach, tax residence, taxpayer types, currency, assessment period and responsible authorities |
| Individual income tax | Chargeable income, deductions, allowances, rates, residence and non-resident treatment |
| Corporate income tax | Residence, permanent establishment, profit base, rates, losses, distributions and applicable minimum taxes |
| Consumption and imports | VAT, GST or sales tax, registration, place of supply, exemptions, input recovery and customs interaction |
| Payroll | Employer registration, withholding, benefits, reporting, payment and reconciliation |
| Social contributions | Employee, employer and self-employed bases, caps, exemptions and contribution periods |
| Formation and reporting | Entity registration, ownership disclosures, recordkeeping, accounts, audit and annual filings |
| Withholding and cross-border rules | Relevant payment categories, source rules, domestic rates, treaty eligibility, relief procedure and transfer pricing |
| Capital and property | Capital gains, property taxes, transfers, inheritance or estate charges, and relevant transaction duties |
| Compliance | Registration, returns, deadlines, payments, corrections, appeals, penalties and records |
| Special regimes | Applicable industry rules, digital assets, incentives, economic substance and local exceptions |

An absent tax needs affirmative primary-source support. A shared regime needs a source establishing territorial application and any exceptions. Uninhabited areas and disputed or administratively divided territories need a scope guide; copying the administering state's tax tables does not settle application.

## Verification and review

Use the repository's existing [frontmatter and guide structure](skill-template.md), [quality tiers](QUALITY-TIERS.md) and [accuracy methodology](ACCURACY-METHODOLOGY.md). New material remains a source-cited draft pending professional review. Technical checks, a consultation or a merged pull request cannot confer an accountant's sign-off.

For each material claim, record the exact primary source, provision or guidance section, applicable period and the result of reading it in context. Recompute worked examples. Keep evidence gaps explicit; a portal link, search snippet, secondary summary or unreachable citation cannot close one.

Deliver one coherent jurisdiction or related regime batch per pull request. Regenerate derived files, update coverage counts, run the required checks and review new findings before publication. Record the accepted revision and verification limits in a dated entry under `verification-log/`. Recheck later source changes before carrying a verification result forward.

## Keeping the inventory current

The [catalogue](country-catalogue.json) captures the UN M49 table's country-or-area rows on its stated retrieval date. Taiwan and Kosovo retain their existing repository identifiers in a separate list. This geographical inventory makes no claim about sovereignty, recognition or uniform tax administration.

After regenerating `index.json`, run:

```sh
python3 scripts/check-country-coverage.py
python3 scripts/check-country-coverage.py --markdown > docs/COUNTRY-COVERAGE.md
python3 scripts/check-country-coverage.py --check-report
```

The default command lists areas with no indexed guide. `--json` emits each area's guide and accountant-review counts. `--check-report` checks the saved inventory's freshness; a successful result does not establish complete tax coverage. Refresh the authoritative geography source deliberately and review additions, removals and name changes before changing the catalogue.
