---
name: au-payg-instalments
description: Use this skill whenever asked about Australian PAYG Instalments for sole traders. Trigger on phrases like "PAYG instalments", "BAS T1 T2 T7 T9", "instalment rate", "instalment amount", "ATO instalment", "GDP uplift", "GIC", "variation of instalments", or any question about income tax prepayments through the Business Activity Statement. Covers entry/exit thresholds, instalment rate method (T1/T2), instalment amount method (T7), GDP uplift factor, voluntary variation, GIC exposure on under-estimation, and quarterly, two-instalment and annual payment. ALWAYS read this skill before touching any PAYG instalment work for Australia.
version: 2.8
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-02
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Payg Instalments v2.8

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this skill whenever asked about Australian PAYG Instalments for sole traders. Trigger on phrases like "PAYG instalments", "BAS T1 T2 T7 T9", "instalment rate", "instalment amount", "ATO instalment", "GDP uplift", "GIC", "variation of instalments", or any question about income tax prepayments through the Business Activity Statement. Covers entry/exit thresholds, instalment rate method (T1/T2), instalment amount method (T7), GDP uplift factor, voluntary variation, GIC exposure on under-estimation, and quarterly, two-instalment and annual payment. ALWAYS read this skill before touching any PAYG instalment work for Australia.

## Ask the client first

Confirm these facts before reporting an amount or choosing a variation:

1. The income year, residence, entity type and balancing date; the examples assume a resident sole trader and a 30 June year end. Confirm other cases separately.
2. The current ATO notice, offered method, notified rate or amount, cycle and exact due date, including any prior variation.
3. Gross ordinary business and investment income reconciled to source records, GST and other excluded receipts; do not substitute net profit or the bank balance.
4. The first quarter for which instalments became payable this year, earlier instalments and credits, and their entitlement and claim history.
5. For a variation, a documented full-year benchmark-tax forecast, assumptions and appropriate reason code; a cash shortage alone does not change the tax estimate.
6. The lodged activity statements, ATO account allocations and bank evidence needed to separate PAYG instalments, other BAS obligations, credits, unpaid debt and cash.

### Section 2 -- Required inputs and refusal catalogue

#### Required inputs

- **Minimum viable inputs**: the current ATO notification of instalment rate (T2) or instalment amount (T7). The rate method also needs instalment income for the period; an unchanged notified amount does not require an income calculation.
- **Recommended inputs** — prior year income tax assessment, BAS due dates, current year income projections if varying.
- **Ideal inputs** — complete ATO notification, prior year assessment, quarterly P&L, BAS history.
- **If minimum inputs are missing**: return Needs Input for the amount to report or pay. An income reconciliation may be prepared provisionally, but a historical percentage or a bank debit cannot establish the current notice.

#### Refusal catalogue

- **R-AU-PI-1 -- Companies/trusts/partnerships** — Trigger: client is not a sole trader. Message: "This skill covers sole trader PAYG instalments only."  _(Refusal catalogue)_
- **R-AU-PI-2 -- PAYG withholding** — Trigger: client asks about PAYG withholding (W labels). Message: "PAYG withholding is a separate obligation. See au-gst-bas."  _(Refusal catalogue)_
- **R-AU-PI-3 -- GST computation** — Trigger: client asks about GST. Message: "GST computation is handled by the GST skill. This skill covers PAYG instalments only."  _(Refusal catalogue)_

## The method, step by step

### Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Tax | PAYG income tax instalments (via BAS) |
| Primary legislation | TAA 1953 Sch 1 Div 45 |
| Authority | Australian Taxation Office (ATO) |
| Portal | Online services for business, or ATO online services through myGov for sole traders |
| Currency | AUD only |
| Resident individual entry thresholds | All 3: instalment income at least $4,000, latest assessed tax payable at least $1,000 and estimated notional tax at least $500; confirm the ATO notification and SAPTO status. [ATO starting instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments) |
| Resident individual exit | The ATO lists alternative exit grounds, including income below $4,000, adjusted assessment debt below $1,000, notional tax below $500 or a 0.0% calculated rate; SAPTO, age and final-return grounds also apply. Confirm exit rather than simply stopping payment. [ATO stopping instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments) |
| Methods | Rate: T1 x pre-filled T2 or current varied T3 gives T11, with the instalment reported at 5A under the detailed statement instructions. Amount: notified T7 or varied T8/T9/5A |
| GDP adjustment factor | 5% for 2026-27; 4% for 2025-26 and SAP years starting 1 January, 1 February or 1 March 2026; 6% for 2024-25. Applies to the amount method, not the rate method or annual payers. [ATO current calculation](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/how-we-calculate-your-payg-instalment-amount-or-rate), [2026-27 SAP dates](https://softwaredevelopers.ato.gov.au/GDPupliftfactor) and [2025-26 history](https://softwaredevelopers.ato.gov.au/gdp-adjustment-2025-26-gst-and-payg-instalments) |
| Variation GIC threshold | Rate method: compare the varied rate with 85% of the benchmark rate. Amount method: compare the annual estimate used with 85% of benchmark tax. A year-end aggregate alone does not prove that every earlier quarter is protected. [TAA Sch 1 ss 45-230, 45-232 and 45-233](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| GIC rate | The quarterly base interest rate plus 7 percentage points; use the applicable daily rate and statutory period, not a flat percentage of the year-end balance. [TAA s 8AAD](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) and [ATO GIC rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Australian CPA/CA |
| Validation date | Pending |

**BAS label summary**

| Label | Description |
| --- | --- |
| T1 | Instalment income for the quarter |
| T2 | Pre-filled instalment rate, including a previous quarter's varied rate where applicable |
| T3 | Varied instalment rate |
| T4 | Reason code for variation |
| T7 | ATO-notified instalment amount |
| T8 | Estimated annual tax for an amount variation |
| T9 | Varied instalment amount |
| T11 | Rate-method amount: T1 x T2, or T1 x T3 when currently varying; carried to 5A |
| 5A | PAYG instalment payable |
| 5B | Credit claimed from a PAYG instalment variation |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Method unclear | Check ATO notification -- they determine the method |
| Instalment income components uncertain | Trace legal character and the period before including or excluding the receipt. Unresolved classification is Needs Input. Gross ordinary income, not net profit, is the starting point |
| Variation considered | Check 85% safe harbour before varying |
| First year of business | Check ATO notification, including any voluntary entry; the first year is not an exemption |
| Annual election eligibility | Notional tax under $8,000, first instalment quarter not yet lodged, and not required to be registered for GST, or voluntarily registered and remitting GST annually; confirm the choice by the 28th after the first quarter |

### Section 3 -- Payment pattern library

These descriptions identify candidates for reconciliation. A bank descriptor or payment date alone cannot establish that an amount is PAYG instalments, which period it belongs to or how a combined payment was allocated. Match the activity statement or instalment notice and ATO account before assigning a tax component.

#### 3.1 ATO PAYG instalment debits

**ATO PAYG instalment debits pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO, AUSTRALIAN TAXATION OFFICE | Unresolved ATO payment | Match the notice, tax account, period and allocation |
| BAS PAYMENT, BAS DEBIT | Unresolved activity-statement payment | It may combine obligations and credits; do not assume both GST and PAYG |
| PAYG INSTALMENT, PAYG INST | Candidate PAYG instalment payment | Confirm the notice, period and allocation |
| ATO DIRECT DEBIT | Unresolved ATO payment | A collection method does not identify the tax |

#### 3.2 Timing-based identification (quarterly BAS, standard)

**Nominal quarterly timing hints, not proof of classification**

| Debit date range | BAS quarter | Confidence |
| --- | --- | --- |
| 20 October -- 5 November | Q1 (Jul-Sep) due 28 Oct | Timing hint only |
| 20 February -- 10 March | Q2 (Oct-Dec) due 28 Feb | Timing hint only |
| 20 April -- 10 May | Q3 (Jan-Mar) due 28 Apr | Timing hint only |
| 20 July -- 10 August | Q4 (Apr-Jun) due 28 Jul | Timing hint only |

Note: BAS payments typically combine GST and PAYG amounts. Use the PAYG amount at 5A and any variation credit at 5B; T2 is a rate, not an amount.

These windows also catch 2 other cycles (Section 7). A two-instalment payer's debits fall due on 28 April (75%) and 28 July (the remainder), and an annual payer using a tax agent pays by 21 October. Check the notice before treating a debit as a quarterly instalment.

#### 3.3 Related but NOT PAYG instalments

**Related but not PAYG instalments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO PAYG WITHHOLDING, W1-W5 | EXCLUDE | Employer withholding (separate) |
| ATO GST ONLY | EXCLUDE | GST-only payment |
| ATO SUPER, SUPER GUARANTEE | EXCLUDE | Superannuation guarantee |
| ATO PENALTY, ATO GIC | EXCLUDE | Penalty/interest |
| ATO REFUND | Flag for reviewer | Tax refund |
| ATO ACTIVITY STATEMENT | Unresolved statement payment | Match the lodged statement and account allocation before identifying obligations or a split |

#### 3.4 BAS combined payment identification

A single activity-statement payment can include several obligations and credits. Identify the PAYG instalment assessed at 5A and any eligible 5B variation credit from the lodged statement, then reconcile the ATO account and cash allocation. A net bank payment does not by itself identify either label. Use the actual notice due date, including applicable extensions or holiday adjustments, rather than the timing windows above.

### Section 5 -- Computation rules

#### 5.1 Entry into PAYG instalment system

- **Resident individual entry:** The ATO applies three entry thresholds together: instalment income of at least $4,000, tax payable on the latest notice of assessment of at least $1,000, and estimated current-year tax of at least $500, with the SAPTO qualification. Confirm the ATO notification before treating instalments as payable. A resident with $10,000 instalment income, $1,200 assessed tax, $750 estimated tax and no SAPTO meets these thresholds. Voluntary entry is available below them. (TAA 1953 Sch 1 s 45-15; [ATO, Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments).)
- **Method choice** — The ATO notifies an instalment amount, an instalment rate, or a choice between them. When a choice is offered, the method selected on the first activity statement applies for the rest of that income year. The notified figures come from the latest return with the ATO's adjustments; use the notice, not a historical uplift percentage.  _([ATO, Calculate your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments))_

#### 5.2 Instalment rate method (T1, T2/T3, T11 and 5A)

- **Instalment rate method:** T1 is quarterly instalment income (business and investment income, excluding salary/wages covered by PAYG withholding, sole-trader capital gains and GST). The detailed activity-statement instructions calculate T11 from T1 x T2, or T1 x T3 when currently varying, and carry that amount to 5A; a paper statement requires manual entry at 5A. T2 can contain the prior quarter's varied rate. The shorter calculation page summarises reporting at 5A; its omission of T11 does not exclude the detailed T11 step. For a current variation, enter T3, the reason at T4 and any eligible prior-instalment credit claimed at 5B. Follow the issued statement's layout. [ATO detailed statement instructions](https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement); [ATO calculation summary](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments); [ATO variation instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments).
- **What counts as instalment income**: start with gross ordinary business and investment income for the period, excluding GST. Business deductions do not reduce T1. Ordinary dividends are included without franking credits; deemed dividends are excluded. Salary and wages from which PAYG withholding was or should have been made are excluded, whilst non-quotation TFN/ABN withholding is not a general reason to exclude ordinary income. A sole trader excludes capital gains from T1, but must consider their effect on the whole-year tax forecast. Trace unusual receipts, farm management deposits and partnership/trust amounts separately. [ATO instalment income](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/instalment-income).
- **Zero instalment rate** — If the notified rate is zero, still report instalment income at T1 and retain the statement and the reconciliation behind it.

#### 5.3 Instalment amount method (T7)

- **Instalment amount method**: use the current amount notified at T7, unless making a valid variation. It is not generally prior notional tax multiplied by the GDP factor and divided by 4. GDP-adjusted notional tax is worked out through the statutory notional-tax calculation, with increases to adjusted taxable income and adjusted withholding income, rather than a flat uplift of the old tax bill. The amount for a four-instalment payer uses the cumulative 25%, 50%, 75% or 100% of GDP-adjusted notional tax for the relevant instalment number, less earlier instalments, with nil if the result is not positive and any applicable statutory adjustments. A later return or variation can change the notified amount. Reconstructing it needs the complete statutory inputs; an unadjusted prior-tax figure and one percentage are insufficient. [TAA Sch 1 ss 45-325, 45-400 and 45-405](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO calculation](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments).

#### 5.4 GDP adjustment factor

- **GDP adjustment factor 2026-27**: 5% for taxpayers whose relevant income year starts on or after 1 April 2026. SAP income years starting 1 January, 1 February or 1 March 2026 retain 4%. The historical factors are 4% for 2025-26 and 6% for 2024-25. The factor is set each year from ABS data or by legislation and does not affect the rate method or annual payers. See the current and historical ATO developer sources in the quick reference.  _([ATO, How we calculate your PAYG instalment amount or rate](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/how-we-calculate-your-payg-instalment-amount-or-rate))_

#### 5.5 Variation

- **Variation rule:** For a rate variation, enter the new rate at T3 and the reason at T4; the result goes to T11 and 5A. For an amount variation, enter estimated annual tax at T8 and the varied instalment at T9 and 5A, with the reason at T4. For a four-instalment payer, use cumulative 25%, 50%, 75% or 100% according to the number of instalments for which the taxpayer has been liable this income year, less earlier instalments and plus the applicable earlier credits. Count from the first liable instalment, not automatically from July-September. The third and fourth computations restore relevant earlier credit entitlements under s 45-410; the examples below stipulate that those credits were entitled and claimed. If the calculation is nil or negative, enter zero at T9/5A; an eligible credit may be claimed as a positive amount at 5B. If the annual estimate used is below 85% of benchmark tax, calculate any variation GIC under the statutory quarter-by-quarter rules. Benchmark tax excludes capital gains except for superannuation funds and disregards certain offsets; it is not total assessed tax.

For example, the third liable instalment, with estimated annual benchmark tax of $12,000, earlier instalments of $8,000 and no earlier credits, gives $12,000 x 75% - $8,000 = $1,000 at T9/5A. With $500 of applicable earlier credit entitlements, all claimed in this example, it gives $1,500. A new entrant first liable in January-March instead starts at 25%, not 75%; confirm the notice and first liable instalment before selecting the percentage. See [ATO: how to vary PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments).

- **Varied rate formula** — Varied rate = estimated annual tax on instalment income divided by estimated annual instalment income, multiplied by 100. Apply the varied percentage to actual instalment income for the period. If estimated annual instalment income is zero, the rate or amount can be varied to zero without estimating tax. Select the reason code that matches the circumstances.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Estimate the whole year, not turnover times a rate** — A variation changes prepayments without changing the final liability. Estimate the tax attributable to instalment income from a current full-year forecast that includes other income, deductions and offsets. Under the rate method the instalment already rises and falls with income; a changed profit margin can justify a variation, a temporary cash shortage does not. If payment is difficult, lodge the statement and discuss a payment arrangement with the ATO.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_
- **Timing and records** — Lodge the variation on or before the instalment due date and before the income tax return for that year is lodged; it applies to later instalments until a valid new estimate for a later quarter or the end of the year. Do not replace the estimate already used for the same instalment under s 45-415(2). Keep the forecast, assumptions, calculation, reason code and lodged statement, review the forecast when conditions change, and match instalment credits on the assessment to the instalment account before treating an expected credit as cash.  _([ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_

#### 5.6 Year-end credit

- **Year-end credit rule** — Total PAYG instalments credited against annual income tax assessment. Overpayment: refund or offset. Underpayment: balance due with assessment.

### Section 6 -- Penalties and interest

#### 6.1 General Interest Charge (GIC)

- **GIC rate and period**: use the published quarterly base rate plus 7 percentage points and the applicable daily rate. For a rate variation, s 45-230 tests the varied rate against 85% of the benchmark instalment rate. For an amount variation, s 45-232 tests the annual benchmark-tax estimate used against 85% of benchmark tax. Work out the statutory charge amount and period separately; a year-end balance or comparison with total assessed tax is insufficient. [TAA Sch 1 ss 45-230 and 45-232](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [TAA s 8AAD](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) and [ATO GIC rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates).
- **GIC/SIC deductibility:** The denial applies to GIC and SIC incurred on or after 1 July 2025 for income years starting on or after that date, regardless of the debt's year. For a substituted accounting period, check the next income year starting on or after 1 July 2025. A later remission of interest denied under this rule is not assessable; remission of previously deducted interest can be assessable. [ATO, Denying deductions for ATO interest charges](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/deny-deductions-for-ato-interest-charges).

#### 6.2 Late BAS lodgement penalty

- **Late BAS lodgement penalty:** For a small entity, the base is one penalty unit per 28 days or part, up to five units, subject to the statutory conditions, adjustments and remission. Date the applicable unit: $313 from 1 July 2023 to 6 November 2024, $330 from 7 November 2024 to 30 June 2026, and $364 from 1 July 2026. Five units are respectively $1,565, $1,650 and $1,820. Do not apply one rate across every period. (TAA 1953 Sch 1 s 286-80; Crimes Act 1914 s 4AA.) A multiplier of 2, 5 or 500 can apply. The withholder, assessable income and GST turnover tests are alternatives, so a small withholder can still attract a higher multiplier: see the table in `au-lodgment-deadlines-penalties.md` Section 6.

#### 6.3 Safe harbour

- **Apply the correct 85% test**: compare rates for a rate variation and the annual estimate used for an amount variation. Exactly 85% does not meet the statutory condition of being less than 85%; it is not a general exemption from interest on late payment or other liabilities. Do not certify all earlier quarters by checking the final annual total. Under s 45-233, a later top-up can reduce an amount-method variation shortfall from the later instalment due date; it does not retrospectively remove the earlier charging period. [TAA Sch 1 ss 45-230, 45-232 and 45-233](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).
- **85% is a floor, not a target:** Use a supportable full-year forecast and the method-specific test above. The threshold is not licence to understate deliberately and does not remove other interest or penalties. [ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments).

### Section 7 -- Annual instalment election and two-instalment option

- **Annual election eligibility:** The most recently notified notional tax must be below $8,000 and the remaining conditions and choice must be satisfied. The basic path in s 45-140(1) requires no GST registration or requirement for the taxpayer or a partnership in which they are a partner. The alternative in s 45-140(1A) covers an annual GST election in force for the taxpayer, or an unregistered taxpayer not required to register who is a partner in a registered partnership. Each registered partnership must have an annual GST election in force and none may be required to register. Do not apply a blanket exclusion to every GST-registered partnership. A company must also satisfy the GST joint-venture and instalment-group restrictions and must not be the head company of a consolidated group to which Subdivision 45-Q applies. Low turnover alone is insufficient: a voluntarily GST-registered sole trader who reports GST quarterly with $60,000 income and $5,000 notional tax fails the GST condition. The first instalment quarter must not yet have been lodged. Confirm the choice by the 28th day of the month after the end of the first instalment quarter (the next 28 February where December ends that quarter). [TAA Sch 1 s 45-140](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO, When are PAYG instalments due](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due).
- **Election and timing:** Confirm the annual election on the ATO notice and retain its confirmation; eligibility alone does not make the election. For an income year ending 30 June, the annual instalment is due by the next 21 October. A taxpayer using a tax agent should pay the annual instalment before the return is lodged and by 21 October. If the agent has already lodged before 21 October, the ATO instructs payment by 21 October without lodging or varying the instalment notice. A self-preparer need not pay the annual instalment or lodge the instalment notice, and instead lodges the tax return by 31 October, when the instalments are worked out. Check first-entry and loss-of-eligibility timing separately. (Taxation Administration Act 1953 (Cth) sch 1 ss 45-70(2), 45-140; [ATO, When are PAYG instalments due](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due).)
- **Two-instalment option:** A quarterly payer on the instalment amount may be offered 2 instalments if an individual carrying on a primary production business or a special professional (such as an author, inventor, performing artist, production associate or sportsperson), where the latest return shows gross income from that source above the related deductions. Pay 75% of the year's instalments by 28 April and the remainder by 28 July, using the instalment amount. To return to quarterly instalments, lodge the activity statement by the first instalment's due date using the instalment rate. _([ATO, When are PAYG instalments due](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due))_

## Boundary and exception table

### Section 8 -- Edge cases

**New business.** A new business without an ATO instalment notification will commonly have no first-year instalments. Voluntary entry is available. Once notified, follow the instalment obligations even before the first return is assessed; allow for the eventual tax balance.

**Seasonal income.** The instalment rate method adjusts with income each quarter. Under the amount method, consider a variation in low-income quarters.

**Several activities.** Instalment income is the total across all business and investment activities, and a single rate applies to the aggregate.

**Investment income.** Interest, dividends and rent are instalment income. Employees with significant investment income may enter the PAYG instalment system.

**Medicare levy.** The ATO-notified rate already includes the Medicare levy (2%) and any surcharge. No separate adjustment is needed.

**Exit.** Check the ATO stopping-instalments conditions and confirmation. For a resident individual, the listed automatic grounds include notional tax below $500, income below $4,000, adjusted assessment debt below $1,000, a 0.0% calculated rate and SAPTO or specified age/final-return conditions. A non-resident income threshold differs. If income ceases, request exit rather than assuming a bank pattern or a changed forecast has cancelled the obligation. [ATO stopping instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments).

## Worked cases

### Section 4 -- Worked examples

#### Example 1 -- Instalment rate method

A resident sole trader has gross business receipts of $46,200 including separately reconciled GST of $4,200, and ordinary bank interest of $800. Salary of $10,000 subject to PAYG withholding and a $3,000 net capital gain are excluded from T1; their final-assessment effects are outside this instalment illustration. Business deductions of $9,000 do not reduce T1. The current notice confirms T2 of 8.50%. Income character and timing are stipulated as resolved. [ATO instalment income](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/instalment-income).

**BAS label value table**

| BAS label | Value |
| --- | --- |
| T1 (instalment income) | $42,800 |
| T2 (instalment rate) | 8.50% |
| T11 and 5A (instalment payable using the pre-filled T2) | $3,638 |

```oa-check
name: Sole-trader gross instalment income excludes GST and not business deductions
tolerance: 0.000001
inputs:
  business_receipts_including_gst: 46200
  reconciled_gst: 4200
  bank_interest: 800
  business_deductions: 9000
  notified_rate_percent: 8.5
steps:
  - business_income_excluding_gst: business_receipts_including_gst - reconciled_gst
  - instalment_income: business_income_excluding_gst + bank_interest
  - incorrect_net_income: instalment_income - business_deductions
  - reported_instalment: pct(instalment_income, notified_rate_percent)
  - understatement_if_net_profit_used: reported_instalment - pct(incorrect_net_income, notified_rate_percent)
expected:
  business_income_excluding_gst: 42000
  instalment_income: 42800
  incorrect_net_income: 33800
  reported_instalment: 3638
  understatement_if_net_profit_used: 765
```


#### Example 2 -- Instalment amount method

Input: ATO-notified instalment amount (T7) = $3,150 per quarter.

Output: Enter the notified $3,150 at 5A (T7 is pre-filled) and pay by the notice due date. No income calculation is needed. Four unchanged notices would total $12,600, but neither figure can be inferred simply by uplifting an unadjusted prior notional tax of $12,000 by 5%. Obtain the current notice or complete statutory workings; otherwise return Needs Input.

#### Example 3 -- Variation of instalment rate

Input: ATO rate = 12%. A supportable full-year tax and instalment-income forecast establishes an estimated rate of 8%, with a changed taxable proportion rather than just lower gross income. Varied rate = 8%.

Computation: enter 8% at T3 and the variation reason at T4. T11 and 5A = T1 x 8%. For this rate-method variation, compare the varied rate with the Commissioner's eventual benchmark instalment rate, not the old notified 12% or total assessed tax. Confirm a changed taxable proportion; lower gross income alone already lowers the rate-method instalment. See Example 6 for the 85% boundary.

#### Example 3A -- Amount variation and an earlier credit

Two established four-instalment payers are at their third liable instalment. Each has earlier instalments of $8,000 and applicable earlier credit entitlements of $500, all claimed. Payer A has a supported annual benchmark-tax estimate of $12,000: $12,000 x 75% - $8,000 + $500 = $1,500. Payer B has a supported annual estimate of $8,000: the result is -$1,500, so report zero at T9/5A and, if claimed in the approved form by the due date, $1,500 at 5B. Payer B has $6,000 net after both credits. These are separate taxpayers with different supported forecasts, not successive estimates for one instalment or a choice of the more convenient payment. Section 45-415(2) prevents a later replacement estimate for the same instalment. Neither case establishes a GIC exemption. [ATO variation instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments); [TAA Sch 1 ss 45-410, 45-415 and 45-420](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

```oa-check
name: Third liable instalment restores earlier credit and separates a negative result
tolerance: 0.000001
inputs:
  higher_annual_estimate: 12000
  lower_annual_estimate: 8000
  cumulative_percent: 75
  earlier_instalments: 8000
  earlier_credit_entitlements_claimed: 500
steps:
  - higher_result_without_earlier_credit: pct(higher_annual_estimate, cumulative_percent) - earlier_instalments
  - higher_reported_instalment: higher_result_without_earlier_credit + earlier_credit_entitlements_claimed
  - lower_variation_result: pct(lower_annual_estimate, cumulative_percent) - earlier_instalments + earlier_credit_entitlements_claimed
  - lower_t9_and_5a: max(lower_variation_result, 0)
  - eligible_5b_if_claimed: max(0 - lower_variation_result, 0)
  - net_instalments_after_new_credit: earlier_instalments - earlier_credit_entitlements_claimed - eligible_5b_if_claimed
expected:
  higher_result_without_earlier_credit: 1000
  higher_reported_instalment: 1500
  lower_variation_result: -1500
  lower_t9_and_5a: 0
  eligible_5b_if_claimed: 1500
  net_instalments_after_new_credit: 6000
```

#### Example 3B -- A new payer first liable in income-year Q3

A resident sole trader's notice confirms the four-instalment cycle and their first liable instalment in January-March. A supportable annual estimate is $12,000, with no earlier instalments or credits. The first liable instalment uses 25%, giving $3,000; the next uses cumulative 50% less the earlier $3,000, giving another $3,000. The first year's two payments total $6,000, so plan for the assessment balance. Selecting 75% merely because January-March is income-year Q3 would overstate the first payment by $6,000. If the liable sequence or cycle is unconfirmed, return Needs Input. [ATO variation instructions for new instalment payers](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments); [TAA Sch 1 s 45-410](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

```oa-check
name: New payer counts from the first liable instalment rather than income-year quarter
tolerance: 0.000001
inputs:
  annual_estimate: 12000
  first_cumulative_percent: 25
  second_cumulative_percent: 50
  incorrect_income_year_quarter_percent: 75
steps:
  - first_instalment: pct(annual_estimate, first_cumulative_percent)
  - second_instalment: pct(annual_estimate, second_cumulative_percent) - first_instalment
  - first_year_total: first_instalment + second_instalment
  - incorrect_first_instalment: pct(annual_estimate, incorrect_income_year_quarter_percent)
  - first_payment_overstatement: incorrect_first_instalment - first_instalment
expected:
  first_instalment: 3000
  second_instalment: 3000
  first_year_total: 6000
  incorrect_first_instalment: 9000
  first_payment_overstatement: 6000
```

#### Example 4 -- Below entry threshold

Input: Instalment income = $3,500. Notional tax = $800.

Output: These figures do not trigger automatic individual entry. Check the ATO notification and voluntary-entry status before concluding that no instalments are due.

#### Example 5 -- Bank statement classification

Input line: `28.10.2026 ; ATO ACTIVITY STATEMENT ; DEBIT ; BAS JUL-SEP 2026 ; -5,800.00 ; AUD`

Classification: an unresolved activity-statement payment. The $5,800 debit does not establish GST, PAYG instalments or their split. Obtain the lodged statement, 5A/5B and the ATO account allocation; return Needs Input for the PAYG cash component until reconciled. The PAYG amount assessed, any variation credit and cash paid are separate facts.

#### Example 6 -- Rate variation at the 85% boundary

Assume the eventual benchmark instalment rate is 10% and this period's instalment income is $42,800. A varied rate of 8% is 80% of benchmark and meets the less-than-85% rate condition; 8.5% is exactly 85% and does not meet that condition. The corresponding payments are $3,424 and $3,638. This comparison does not calculate a GIC amount, resolve earlier variations or excuse late payment. [TAA Sch 1 s 45-230](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

```oa-check
name: Rate variation distinguishes below 85 percent from exactly 85 percent
tolerance: 0.000001
inputs:
  benchmark_rate_percent: 10
  lower_rate_percent: 8
  boundary_rate_percent: 8.5
  instalment_income: 42800
steps:
  - lower_benchmark_share_percent: lower_rate_percent / benchmark_rate_percent * 100
  - boundary_benchmark_share_percent: boundary_rate_percent / benchmark_rate_percent * 100
  - lower_payment: pct(instalment_income, lower_rate_percent)
  - boundary_payment: pct(instalment_income, boundary_rate_percent)
  - payment_difference: boundary_payment - lower_payment
expected:
  lower_benchmark_share_percent: 80
  boundary_benchmark_share_percent: 85
  lower_payment: 3424
  boundary_payment: 3638
  payment_difference: 214
```

## When to refuse or refer

### Prohibitions

- Exclude GST, sole-trader capital gains and salary/wages covered by PAYG withholding from T1; trace other receipts against the instalment-income definition rather than applying a blanket bank-description rule
- NEVER vary the instalment rate or amount without checking the 85% safe harbour
- Check the ATO notification and voluntary-entry status before deciding whether first-year instalments are payable
- Check the current notice and the applicable GDP year when reconciling T7; never replace the statutory income-based calculation with a flat uplift of old tax, and never uplift the instalment rate
- NEVER conflate PAYG instalments (T labels) with PAYG withholding (W labels)
- NEVER present instalment figures as definitive -- the ATO notification is authoritative


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.



## Completion checklist

### Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Entry thresholds checked ($4,000 instalment income, $1,000 tax payable, $500 notional tax)
- [ ] Correct method identified (rate vs amount)
- [ ] T1 includes gross instalment income, excluding GST, sole-trader capital gains and salary/wages covered by PAYG withholding
- [ ] T2 matches the notice; any varied rate is at T3, reason at T4, and result at T11/5A
- [ ] Any amount variation uses T8/T9, cumulative quarter percentages and applicable earlier credits
- [ ] Correct rate/annual-estimate 85% test and each relevant quarter checked; no blanket year-end GIC clearance
- [ ] GDP year/SAP qualification checked; current notice used, not prior tax multiplied by 1.05
- [ ] BAS due dates correct
- [ ] Year-end credit against annual assessment noted
- [ ] First-year ATO notification and voluntary-entry status checked
- [ ] Output labelled as estimated until Australian CPA/CA confirms

#### Test 1 -- Instalment rate method

Input: T1 = $42,800. T2 = 8.50%.
Expected: T11 and 5A = $3,638 using the pre-filled T2 under the detailed statement instructions.

#### Test 2 -- Instalment amount method

Input: Four unchanged ATO notices each show T7 of $3,150.
Expected: Report each notified amount; total $12,600. An unadjusted prior notional tax of $12,000 and the 5% factor alone do not establish those notices.

#### Test 3 -- Below entry threshold

Input: Instalment income = $3,500.
Expected: Below the automatic individual entry-income threshold; check the notice and voluntary-entry status before concluding that no instalments are due.

#### Test 4 -- Variation with safe harbour check

Input: ATO rate 12%. Varied to 8%. Actual correct rate = 10%.
Expected: The varied rate is 80% of the benchmark rate. The less-than-85% rate condition is met; work out any charge under s 45-230 rather than asserting its amount or clearing it from year-end totals.

#### Test 5 -- First year

Input: New sole trader, no prior assessment and no ATO instalment notification.
Expected: No instalments yet; plan for the tax balance.
Counterexample: the same trader voluntarily enters and receives an ATO instalment notice.
Expected: follow that notice; the first year is not an exemption.

#### Test 6 -- Year-end credit (overpayment)

Input: Total instalments paid = $15,000. Actual tax = $12,000.
Expected: $3,000 overpayment refunded or offset.

## Sources

| Source | URL | Read on |
|---|---|---|
| ATO, Starting PAYG instalments: individual entry, notification and voluntary entry sections | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments> | 2 November 2026; page updated 17 December 2024 |
| ATO, Calculate your PAYG instalments: method selection, notified amount and rate steps | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments> | 2 November 2026; page updated 9 March 2022 |
| ATO, PAYG instalments: how to complete your activity statement, option 2 T2/T3/T11/5A and unvaried-rate example | <https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement> | 2 November 2026; page updated 9 January 2023; saved same-day primary capture reused |
| ATO, How we calculate your PAYG instalment amount or rate: GDP and notified-rate explanation | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/how-we-calculate-your-payg-instalment-amount-or-rate> | 2 November 2026; displayed update 20 May 2025, body states 5% for 2026-27 |
| ATO, How to vary your PAYG instalments: amount/rate steps, new-payer sequence, credits and forecast/timing warnings | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments> | 2 November 2026; page updated 23 June 2026 |
| ATO, Instalment income: included and excluded income sections | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/instalment-income> | 2 November 2026; page updated 9 March 2022 |
| ATO, When are PAYG instalments due: quarterly, twice-yearly and annual sections | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due> | 2 November 2026; page updated 3 March 2026; actual notice/extensions still required |
| ATO, Stopping PAYG instalments: individual exit and request sections | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments> | 2 November 2026; page updated 18 December 2024 |
| Taxation Administration Act 1953, compilation 227: selected Sch 1 ss 45-120, 45-140, 45-230, 45-232, 45-233, 45-325, 45-335, 45-400, 45-405, 45-410, 45-415 and 45-420 | <https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html> | 2 November 2026; effective 1 October, registered 19 October 2026 as C2026C00468; current identity checked through the register API |
| Taxation Administration Act 1953, compilation 227: s 8AAD ordinary GIC daily rate, base-rate quarters and rounding | <https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html> | 2 November 2026; ordinary PAYG GIC base plus 7 percentage points, not the separate Division 296 rate |
| ATO developer GDP uplift factor: current version 2027 description and SAP qualification | <https://softwaredevelopers.ato.gov.au/GDPupliftfactor> | 2 November 2026; published 11 June 2026 |
| ATO developer GDP adjustment 2025-26: version 2026 description, prior 4%/6% and SAP qualification | <https://softwaredevelopers.ato.gov.au/gdp-adjustment-2025-26-gst-and-payg-instalments> | 2 November 2026; published 2 April 2025 |
| ATO, Denying deductions for ATO interest charges: standard/SAP application and remission sections | <https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/deny-deductions-for-ato-interest-charges> | 2 November 2026; page updated 8 June 2026 |
| ATO, General interest charge rates: introductory quarterly/daily-rate instructions | <https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates> | 2 November 2026; page updated 4 September 2026; historical rate table not audited here |

Not yet confirmed: This source check covers the selected sections above and 4 executable arithmetic cases under stated facts. It does not certify all retained penalty-unit/multiplier figures, historical claims, special regimes, foreign-resident treatment or the complete portal/form/software workflow. Full notional/benchmark-tax reconstruction and a particular debt's GIC amount, dates and daily rates remain unverified; formula images in the statutory extraction were not read as a complete calculation engine. Current approved reporting instructions must resolve fractional precision; the cases produce whole-dollar payments. Obtain the current notice, liable instalment sequence, income character/timing, prior instalments and credit entitlements or return Needs Input. Earlier credits in Example 3A are stipulated entitled and claimed; unclaimed-credit cases need separate review. Tier 2 remains pending review and qualified Australian sign-off is required. Historical provenance retains its original scope.

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
