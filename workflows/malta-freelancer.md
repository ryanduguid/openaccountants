# Malta Freelancer / Self-Employed Tax Workflow

> This revision includes changes made after the recorded verification and awaits a new verification.

**MCP prompt name:** `malta-freelancer`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/MT`

## Trigger phrases

- "self-employed Malta"
- "freelancer Malta"
- "part-time work Malta"
- "FS5 Malta"
- "SSC Malta"
- "Malta VAT registration"
- "malta-income-tax"
- "Malta sole trader"
- "tax Malta"

## What it produces

- Part-time regime (TA22) vs progressive rate comparison
- SSC Class 2 contribution computation (self-occupied)
- VAT return working paper (if VAT-registered)
- Provisional tax schedule
- Annual income tax return working paper

## Skills to load

From the MT bundle:
- `malta-income-tax` — tax rates, brackets, single/married/parent computation, part-time TA22 regime
- `malta-ssc` — Social Security Contributions (Class 2 self-occupied rates)
- `malta-vat-return` — VAT return periods, thresholds, deductible input VAT
- `mt-estimated-tax` — provisional tax due dates

Rates and thresholds in the phases below come from these guides. The hosted bundle does not carry them all: if one is not loaded, fetch it from `packages/malta/` in this repository before computing, and never fall back on a remembered figure.

## 6-phase structure

### Phase 1 — Intake
Confirm: employment status (full-time employed + part-time self-employed, or full-time self-employed), type of income (service, product, rental), annual gross revenue, major expenses, VAT registration status, marital status (affects rate structure).

### Phase 2 — Part-time vs standard rate decision
If the taxpayer is also in full-time employment, a pensioner or a full-time student or apprentice, and meets the other conditions in the part-time section of `malta-income-tax`: eligible for the optional TA22 regime, a flat rate on net part-time profit up to a cap, with any excess declared in the return. Take the rate, cap and conditions from there. Compare to declaring under the progressive rates with deductions — run both and show which is lower.

### Phase 3 — SSC computation
Class 2 (self-occupied): take the category for the person's net income and birth year from `malta-ssc`, which pays a percentage between a weekly minimum and maximum. Compute annual SSC liability. Note: do not assume TA22 removes Class 2. It depends on the person's contribution status, so flag it for review in every TA22 case.

### Phase 4 — VAT position
If annual turnover exceeds the Malta VAT registration threshold: mandatory VAT registration. Take the threshold, the registration type (Article 10, 11 or 12), the return frequency and the deadlines from `malta-vat-return`. Compute output VAT (sales × applicable rate) less deductible input VAT (business purchases).

### Phase 5 — Provisional tax
Self-employed taxpayers pay provisional tax separately from FS5, which is an employer's monthly payment advice under the FSS. Take the instalments, due dates and benchmark from `mt-estimated-tax`.

### Phase 6 — Handoff
Recommend review by a Malta-qualified CPA or warranted accountant. Route to: https://www.openaccountants.com

## Verifier

For the revision of 2026-06-09 (commit 47b8f2fa): Verified by **Michael Cutajar CPA (Malta)** — [openaccountants.com/network](https://www.openaccountants.com/network)

Skills signed off by Michael are Tier 1 (accountant-verified). Use the MCP server or bundle API to access the verified versions.
