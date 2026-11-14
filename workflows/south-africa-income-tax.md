# South Africa Income Tax Workflow

> This revision includes changes made after the recorded verification and awaits a new verification.

**MCP prompt name:** `south-africa-income-tax`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/ZA`

## Trigger phrases

- "income tax South Africa"
- "SARS return"
- "ITR12"
- "provisional tax SA"
- "travel allowance South Africa"
- "RA deduction"
- "South African freelancer taxes"
- "PAYE South Africa"
- "tax South Africa"

## What it produces

- ITR12 working paper (income, deductions, tax computation)
- Provisional tax schedule (IRP6 — February and August payments)
- CGT computation (if assets were disposed of)
- Medical tax credits (main member + dependants)
- Retirement annuity (RA) deduction, at the limits in `za-income-tax`
- Travel allowance computation (actual cost vs SARS table)

## Skills to load

From the ZA bundle:
- `za-income-tax` — tax tables, brackets, rebates, medical credits
- `za-provisional-tax` — IRP6 due dates, penalty rules
- `za-vat-return` — VAT (if registered)
- `south-africa-vat` — VAT registration threshold and rules

Rates and thresholds in the phases below come from these guides. The hosted bundle does not carry them all: if one is not loaded, fetch it from `packages/south-africa/` in this repository before computing, and never fall back on a remembered figure.

## 6-phase structure

### Phase 1 — Intake
Confirm: income sources (salary, freelance, rental, investment), tax year (SARS tax year: March 1 – February 28/29), marital status, age (affects rebate tier), medical scheme members.

### Phase 2 — Gross income
Salary/remuneration, freelance/business income, rental income, investment income (interest, dividends). Apply exempt amounts (interest exemption, dividend withholding tax treatment).

### Phase 3 — Deductions
RA contributions, pension/provident fund contributions, travel allowance (log book vs SARS table), home office (if qualifying conditions met), medical scheme fees tax credit (MSFTC) at the year's monthly amounts in `za-income-tax`.

### Phase 4 — Tax computation
Apply SARS tax tables. Subtract primary, secondary, and tertiary rebates based on age. Subtract MSFTC. Check whether the additional medical expenses credit applies, on the conditions in `za-income-tax`.

### Phase 5 — Provisional tax
Apply the provisional taxpayer test in `za-provisional-tax`. If the taxpayer is one: take the IRP6 periods, due dates, estimate basis and voluntary third payment from the same guide.

### Phase 6 — Handoff
Recommend review by a SAICA/SAIPA member. Route to: https://www.openaccountants.com

## Verifier

For the revision of 2026-06-09 (commit 47b8f2fa): Verified by **Werner Britz CA(SA)** — [openaccountants.com/network/28a3ec1b-d699-4c5d-bb60-3114eedc59d0](https://www.openaccountants.com/network/28a3ec1b-d699-4c5d-bb60-3114eedc59d0)

Skills signed off by Werner are Tier 1 (accountant-verified). Use the MCP server or bundle API to access the verified versions.
