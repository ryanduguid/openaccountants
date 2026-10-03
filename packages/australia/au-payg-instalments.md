---
name: au-payg-instalments
description: Use this skill whenever asked about Australian PAYG Instalments for sole traders. Trigger on phrases like "PAYG instalments", "BAS T1 T2 T7 T9", "instalment rate", "instalment amount", "ATO instalment", "GDP uplift", "GIC", "variation of instalments", or any question about income tax prepayments through the Business Activity Statement. Covers entry/exit thresholds, instalment rate method (T1/T2), instalment amount method (T7), GDP uplift factor, voluntary variation, GIC exposure on under-estimation, and quarterly/annual election. ALWAYS read this skill before touching any PAYG instalment work for Australia.
version: 2.4
jurisdiction: AU
tax_year: 2026
last_updated: 2026-10-04
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Payg Instalments

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Tax | PAYG income tax instalments (via BAS) |
| Primary legislation | TAA 1953 Sch 1 Div 45 |
| Authority | Australian Taxation Office (ATO) |
| Portal | Online services for business, or ATO online services through myGov for sole traders |
| Currency | AUD only |
| Entry thresholds | Instalment income of $4,000 or more, tax payable on the latest assessment of $1,000 or more, and notional tax of $500 or more (individuals and trusts) |
| Exit threshold | Automatic exit when notional tax is under $500, instalment income is under $4,000, the tax debt on assessment is under $1,000 or the calculated rate is 0.0% |
| Methods | Rate: T1, T2 or varied T3, result T11/5A. Amount: notified T7 or varied T8/T9/5A |
| GDP adjustment factor | 5% for 2026-27 (6% in 2024-25); set each year and applied to the instalment amount method only |
| Variation safe harbour | 85% of correct instalment amount |
| GIC rate | Base rate + 7% (updated quarterly) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Australian CPA/CA |
| Validation date | Pending |

**BAS label summary**

| Label | Description |
| --- | --- |
| T1 | Instalment income for the quarter |
| T2 | ATO-notified instalment rate |
| T3 | Varied instalment rate |
| T4 | Reason code for variation |
| T7 | ATO-notified instalment amount |
| T8 | Estimated annual tax for an amount variation |
| T9 | Varied instalment amount |
| T11 | Rate-method amount: T1 x T2, or T1 x T3 when varied |
| 5A | PAYG instalment payable |
| 5B | Credit claimed from a PAYG instalment variation |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Method unclear | Check ATO notification -- they determine the method |
| Instalment income components uncertain | Include all business + investment income; exclude salary, CGT, exempt |
| Variation considered | Check 85% safe harbour before varying |
| First year of business | Check ATO notification, including any voluntary entry; the first year is not an exemption |
| Annual election eligibility | Notional tax under $8,000 and not required to be registered for GST, or voluntarily registered and remitting GST annually; confirm the choice by the 28th after the first quarter |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — ATO notification of instalment rate (T2) or instalment amount (T7), quarterly instalment income figure.
- **Recommended inputs** — prior year income tax assessment, BAS due dates, current year income projections if varying.
- **Ideal inputs** — complete ATO notification, prior year assessment, quarterly P&L, BAS history.
- **Refusal policy if minimum is missing** — SOFT WARN. Without the ATO notification, the instalment rate or amount cannot be confirmed.

### Refusal catalogue

- **R-AU-PI-1 -- Companies/trusts/partnerships** — Trigger: client is not a sole trader. Message: "This skill covers sole trader PAYG instalments only."  _(Refusal catalogue)_
- **R-AU-PI-2 -- PAYG withholding** — Trigger: client asks about PAYG withholding (W labels). Message: "PAYG withholding is a separate obligation. See au-gst-bas."  _(Refusal catalogue)_
- **R-AU-PI-3 -- GST computation** — Trigger: client asks about GST. Message: "GST computation is handled by the GST skill. This skill covers PAYG instalments only."  _(Refusal catalogue)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a PAYG instalment payment.

### 3.1 ATO PAYG instalment debits

**ATO PAYG instalment debits pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO, AUSTRALIAN TAXATION OFFICE | PAYG instalment | Match with BAS quarterly timing |
| BAS PAYMENT, BAS DEBIT | PAYG instalment (combined with GST) | BAS payment includes both GST and PAYG |
| PAYG INSTALMENT, PAYG INST | PAYG instalment | Explicit description |
| ATO DIRECT DEBIT | PAYG instalment | Automatic payment |

### 3.2 Timing-based identification (quarterly BAS, standard)

**Timing-based identification table**

| Debit date range | BAS quarter | Confidence |
| --- | --- | --- |
| 20 October -- 5 November | Q1 (Jul-Sep) due 28 Oct | High |
| 20 February -- 10 March | Q2 (Oct-Dec) due 28 Feb | High |
| 20 April -- 10 May | Q3 (Jan-Mar) due 28 Apr | High |
| 20 July -- 10 August | Q4 (Apr-Jun) due 28 Jul | High |

Note: BAS payments typically combine GST and PAYG amounts. Use the PAYG amount at 5A and any variation credit at 5B; T2 is a rate, not an amount.

### 3.3 Related but NOT PAYG instalments

**Related but not PAYG instalments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO PAYG WITHHOLDING, W1-W5 | EXCLUDE | Employer withholding (separate) |
| ATO GST ONLY | EXCLUDE | GST-only payment |
| ATO SUPER, SUPER GUARANTEE | EXCLUDE | Superannuation guarantee |
| ATO PENALTY, ATO GIC | EXCLUDE | Penalty/interest |
| ATO REFUND | Flag for reviewer | Tax refund |
| ATO ACTIVITY STATEMENT | Combined payment | Includes GST + PAYG -- split for classification |

### 3.4 BAS combined payment identification

A single BAS payment typically includes GST payable/refundable + PAYG instalment + PAYG withholding. To isolate the PAYG instalment component, the BAS PAYG amounts (5A and any 5B credit) are needed.

## Section 4 -- Worked examples

### Example 1 -- Instalment rate method

Q1 business income = $42,000. Interest income = $800. ATO rate (T2) = 8.50%.

**BAS label value table**

| BAS label | Value |
| --- | --- |
| T1 (instalment income) | $42,800 |
| T2 (instalment rate) | 8.50% |
| T11 and 5A (instalment payable) | $3,638 |

### Example 2 -- Instalment amount method

Input: ATO-notified instalment amount (T7) = $3,150 per quarter.

Output: The notified T7 amount is $3,180. Enter $3,180 at 5A and pay by the notice due date.

### Example 3 -- Variation of instalment rate

Input: ATO rate = 12%. Taxpayer estimates current year rate should be 8% (income dropped). Varied rate = 8%.

Computation: enter 8% at T3 and the variation reason at T4. T11 and 5A = T1 x 8%. Assess variation interest against benchmark tax, not total assessed tax; below 85% may attract GIC.

### Example 4 -- Below entry threshold

Input: Instalment income = $3,500. Notional tax = $800.

Output: Instalment income < $4,000. Not entered into PAYG instalment system.

### Example 5 -- Bank statement classification

Input line: `28.10.2026 ; ATO ACTIVITY STATEMENT ; DEBIT ; BAS JUL-SEP 2026 ; -5,800.00 ; AUD`

Classification: Combined BAS payment (GST + PAYG). PAYG instalment component = 5A, adjusted for any 5B variation credit. Flag for reviewer to split.

## Section 5 -- Computation rules

### 5.1 Entry into PAYG instalment system

- **Resident individual entry:** The Library gives three thresholds: instalment income of at least $4,000, tax payable on the latest notice of assessment of at least $1,000, and estimated current-year tax of at least $500, with the SAPTO qualification. Confirm the ATO notification before treating instalments as payable. A resident with $10,000 instalment income, $1,200 assessed tax, $750 estimated tax and no SAPTO meets these thresholds. Voluntary entry is available below them. (Library, Tax/Administration and Assessment.)
- **Method choice** — The ATO notifies an instalment amount, an instalment rate, or a choice between them. When a choice is offered, the method selected on the first activity statement applies for the rest of that income year. The notified figures come from the latest return with the ATO's adjustments; use the notice, not a historical uplift percentage.  _([ATO, Calculate your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments))_

### 5.2 Instalment rate method (T1, T2/T3, T11 and 5A)

- **Instalment rate method:** T1 is quarterly instalment income (business and investment income, excluding salary, capital gains and GST). Use the notified rate at T2, or enter a varied rate at T3. Multiply T1 by the applicable percentage rate and report the whole-dollar amount at T11 and 5A. For a variation, enter the reason at T4 and any eligible prior-instalment credit claimed at 5B.
- **What counts as instalment income** — Instalment income is gross business and investment income for the period, excluding GST. It is not net profit, so business deductions do not reduce T1. Salary subject to PAYG withholding and net capital gains are excluded, but a capital gain still creates a final income tax liability, so include it in the whole-year cash forecast. Review unusual receipts against the ATO definition.  _([ATO, Calculate your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments))_
- **Zero instalment rate** — If the notified rate is zero, still report instalment income at T1 and retain the statement and the reconciliation behind it.

### 5.3 Instalment amount method (T7)

- **Instalment amount method formula** — T7 = notional tax x (1 + GDP adjustment factor) / 4 No income calculation needed. ATO pre-fills the amount.

### 5.4 GDP adjustment factor

- **GDP adjustment factor 2026-27** — 5%, applied to the instalment amount (T7) for quarters starting on or after 1 April 2026; it was 6% in 2024-25. The factor is set each year from ABS data or by legislation and does not affect the rate method or annual payers. %  _([ATO, How we calculate your PAYG instalment amount or rate](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/how-we-calculate-your-payg-instalment-amount-or-rate))_

### 5.5 Variation

- **Variation rule:** For a rate variation, enter the new rate at T3 and the reason at T4; the result goes to T11 and 5A. For an amount variation, enter estimated annual tax at T8 and the varied instalment at T9 and 5A, with the reason at T4. For four quarterly instalments, use 25%, 50%, 75% or 100% of estimated annual benchmark tax, less earlier instalments and plus applicable earlier credits. If the calculation is nil or negative, enter zero at T9/5A; an eligible credit may be claimed as a positive amount at 5B. Below 85% of benchmark tax may attract variation GIC. Benchmark tax excludes capital gains except for superannuation funds and disregards certain offsets; it is not total assessed tax.

For example, Q3 estimated annual tax of $12,000, earlier instalments of $8,000 and no earlier credits gives $12,000 x 75% - $8,000 = $1,000 at T9/5A. With $500 earlier applicable credits, it gives $1,500. See [ATO: how to vary PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments).

- **Varied rate formula** — Varied rate = estimated annual tax on instalment income divided by estimated annual instalment income, multiplied by 100. Apply the varied percentage to actual instalment income for the period. If estimated annual instalment income is zero, the rate or amount can be varied to zero without estimating tax. Select the reason code that matches the circumstances.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Estimate the whole year, not turnover times a rate** — A variation changes prepayments without changing the final liability. Estimate the tax attributable to instalment income from a current full-year forecast that includes other income, deductions and offsets. Under the rate method the instalment already rises and falls with income; a changed profit margin can justify a variation, a temporary cash shortage does not. If payment is difficult, lodge the statement and discuss a payment arrangement with the ATO.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Timing and records** — Lodge the variation on or before the instalment due date and before the income tax return for that year is lodged; it applies to the remaining instalments until another variation or the end of the year. Keep the forecast, assumptions, calculation, reason code and lodged statement, review the forecast when conditions change, and match instalment credits on the assessment to the instalment account before treating an expected credit as cash.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_

### 5.6 Year-end credit

- **Year-end credit rule** — Total PAYG instalments credited against annual income tax assessment. Overpayment: refund or offset. Underpayment: balance due with assessment.

## Section 6 -- Penalties and interest

### 6.1 General Interest Charge (GIC)

- **GIC rate** — base rate (90-day bank bill rate) + 7%  _(Updated quarterly. Applies from instalment due date if variation results in < 85% of correct amount.)_
- **GIC is no longer deductible** — General interest charge and shortfall interest charge incurred on or after 1 July 2025 cannot be deducted, whatever year the debt relates to, and a later remission of that interest is not assessable.  _([ATO, Denying deductions for ATO interest charges](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/deny-deductions-for-ato-interest-charges))_

### 6.2 Late BAS lodgement penalty

- **Late BAS lodgement penalty:** For a small entity, the base is one penalty unit per 28 days or part, up to five units, subject to the statutory conditions, adjustments and remission. Date the applicable unit: $313 from 1 July 2023 to 6 November 2024, $330 from 7 November 2024 to 30 June 2026, and $364 from 1 July 2026. Five units are respectively $1,565, $1,650 and $1,820. Do not apply one rate across every period. (Library, Tax/Administration and Assessment.) Medium withholders pay twice and large withholders five times the base amount.

### 6.3 Safe harbour

- **Safe harbour rule** — If varied instalments total >= 85% of the benchmark instalment, no GIC.
- **85% is a floor, not a target** — Where varied instalments fall below 85% of the tax payable on instalment income, general interest charge applies to the difference and penalties can follow. The figure is not licence to understate tax deliberately, and it does not remove other interest charges.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_

## Section 7 -- Annual instalment election

- **Annual election eligibility:** The most recently notified notional tax must be below $8,000. The taxpayer must be neither registered nor required to register for GST, or be voluntarily registered and report and pay GST annually, and must not be a partner in a partnership that is registered or required to register. A company must also satisfy the GST joint-venture and instalment-group restrictions. Low turnover alone is insufficient: a voluntarily GST-registered sole trader who reports GST quarterly with $60,000 income and $5,000 notional tax fails the GST condition. Confirm the choice by the 28th day after the end of the first instalment quarter. _([ATO, Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments))_
- **Election and timing:** Confirm the annual election on the ATO notice and retain its confirmation; eligibility alone does not make the election. Use the applicable notified due date. An annual instalment is generally due at the end of the first quarter of the following income year. Check first-entry and loss-of-eligibility timing separately. (Taxation Administration Act 1953 (Cth) sch 1 s 45-140; Library, Tax/Individuals.)

## Section 8 -- Edge cases

A new business without an ATO instalment notification will commonly have no first-year instalments. Voluntary entry is available. Once notified, follow the instalment obligations even before the first return is assessed; allow for the eventual tax balance.

Instalment rate method auto-adjusts. If using amount method, consider variation in low-income quarters.

Instalment income = total across all activities. Single rate applies to aggregate.

Interest, dividends, rent are instalment income. Employees with significant investment income may enter PAYG system.

ATO-notified rate already includes Medicare levy (2%) and any surcharge. No separate adjustment needed.

Apply if notional tax drops below $500 or instalment income ceases.

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Entry thresholds checked ($4,000 instalment income, $1,000 tax payable, $500 notional tax)
- [ ] Correct method identified (rate vs amount)
- [ ] T1 includes only correct components (no salary, no CGT, no GST)
- [ ] T2 matches the notice; any varied rate is at T3, reason at T4, and result at T11/5A
- [ ] Any amount variation uses T8/T9, cumulative quarter percentages and applicable earlier credits
- [ ] 85% safe harbour checked if variation applied
- [ ] GDP adjustment factor current (5% for 2026-27)
- [ ] BAS due dates correct
- [ ] Year-end credit against annual assessment noted
- [ ] First-year ATO notification and voluntary-entry status checked
- [ ] Output labelled as estimated until Australian CPA/CA confirms

### Test 1 -- Instalment rate method

Input: T1 = $42,800. T2 = 8.50%.
Expected: T11 and 5A = $3,638.

### Test 2 -- Instalment amount method

Input: Prior year notional tax = $12,000. GDP adjustment = 5%.
Expected: Annual = $12,600. T7 = $3,150/quarter.

### Test 3 -- Below entry threshold

Input: Instalment income = $3,500.
Expected: Not entered into system.

### Test 4 -- Variation with safe harbour check

Input: ATO rate 12%. Varied to 8%. Actual correct rate = 10%.
Expected: Varied total = 80% of correct. Below 85%. GIC applies.

### Test 5 -- First year

Input: New sole trader, no prior assessment and no ATO instalment notification.
Expected: No instalments yet; plan for the tax balance.
Counterexample: the same trader voluntarily enters and receives an ATO instalment notice.
Expected: follow that notice; the first year is not an exemption.

### Test 6 -- Year-end credit (overpayment)

Input: Total instalments paid = $15,000. Actual tax = $12,000.
Expected: $3,000 overpayment refunded or offset.

## Prohibitions

- NEVER include salary, net capital gains, or GST in instalment income (T1)
- NEVER vary the instalment rate or amount without checking the 85% safe harbour
- Check the ATO notification and voluntary-entry status before deciding whether first-year instalments are payable
- NEVER ignore the GDP adjustment factor when checking T7, and NEVER apply it to the instalment rate
- NEVER conflate PAYG instalments (T labels) with PAYG withholding (W labels)
- NEVER present instalment figures as definitive -- the ATO notification is authoritative

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
