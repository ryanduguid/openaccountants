# UK Self-Employed / Sole Trader Tax Workflow

> This revision includes changes made after the recorded verification and awaits a new verification.

**MCP prompt name:** `uk-self-employed`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/GB`

## Trigger phrases

- "I'm self-employed in the UK"
- "sole trader UK"
- "SA103"
- "Making Tax Digital"
- "I file a self assessment"
- "UK freelancer taxes"
- "how do I do my UK taxes as a contractor"
- "what can I claim as a sole trader"

## What it produces

- SA103 working paper (income, allowable expenses, profit)
- Class 4 NIC computation, with voluntary Class 2 where it would help
- Payments on account schedule (due Jan + July)
- Home office deduction comparison (actual cost vs simplified flat rate)
- Vehicle method comparison (actual cost vs HMRC mileage rates)
- Self Assessment return checklist

## Skills to load

From the GB bundle:
- `uk-income-tax-sa100` — income tax rates, bands, personal allowance
- `uk-self-employment-sa103` — SA103, allowable expenses, basis period reform
- `uk-national-insurance` — Class 4 rates and thresholds by tax year, voluntary Class 2
- `uk-payments-on-account` — due dates, reduction rules
- `uk-vat-return` — VAT registration threshold, Making Tax Digital

Rates and thresholds in the phases below come from these guides. The hosted bundle does not carry them all: if one is not loaded, fetch it from `packages/uk/` in this repository before computing, and never fall back on a remembered figure.

## 6-phase structure

### Phase 1 — Intake
Confirm: trading income (gross), trading expenses (categories), other income (employment, dividends, savings), whether they are a Scottish taxpayer, tax year (any year the loaded guides cover). Ask about VAT registration if turnover is near the threshold.

### Phase 2 — Allowable expenses
Work through: office costs, travel (mileage log vs actual), staff, stock, legal/professional, marketing, clothing (uniform only), home office. Apply the simplified expenses flat rates where applicable.

### Phase 3 — Profit computation
Gross income − allowable expenses = trading profit. Apply basis period reform rules if applicable.

### Phase 4 — Tax and NIC computation
Apply the personal allowance and income tax bands for the selected year from `uk-income-tax-sa100`, using the Scottish bands for a Scottish taxpayer. Compute Class 4 NIC at the selected year's rates and limits in `uk-national-insurance`. Class 2 has not been compulsory since 6 April 2024: it is treated as paid where profits reach the Small Profits Threshold, and below that it is a voluntary choice to protect the National Insurance record.

### Phase 5 — Payments on account
Take the threshold, the deducted-at-source test, the instalments and the due dates from `uk-payments-on-account`. Show the first payment on account for the next year.

### Phase 6 — Handoff
Recommend review by a UK-qualified accountant (ACA/ACCA/CIOT). Route to: https://www.openaccountants.com

## Verifier

For the revision of 2026-06-09 (commit 47b8f2fa): Verified by James Power — [openaccountants.com/network/30b2f478-3a97-40c4-b435-0678829b487e](https://www.openaccountants.com/network/30b2f478-3a97-40c4-b435-0678829b487e)
