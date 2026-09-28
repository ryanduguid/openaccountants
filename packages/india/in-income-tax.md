---
name: in-income-tax
description: >
  Indian income tax working papers for resident sole proprietors, freelancers and
  specified professionals for FY 2025-26 (AY 2026-27), under the Income-tax Act,
  1961. Covers new and old regime bands, Section 87A rebate and marginal relief,
  conditional Section 44AD and 44ADA limits, eligible receipts, advance tax and
  TDS credits. Use for India income tax, presumptive taxation, ITR-3, ITR-4,
  Section 44ADA, Section 44AD, Form 26AS or freelancer tax calculations. Includes
  bank narration examples and a working-paper template. Capital gains,
  non-residents, RNOR, firms, companies and international tax need separate review.
  FY 2026-27 requires the Income-tax Act, 2025.
version: 2.1
jurisdiction: IN
tax_year: 2025
tax_year_notes: "2025-26"
tier: 2
last_updated: 2026-09-11
review_status: pending_review
category: international
depends_on:
  - income-tax-workflow-base
---

# Indian Income Tax (आयकर) -- Self-Employed Skill v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> This guide covers FY 2025-26 (AY 2026-27) under the Income-tax Act, 1961.
> The Income-tax Act, 2025 commenced on 1 April 2026 and governs FY 2026-27.
> Confirm the income year before using these section references and deadlines.
> The later Act preserves the new-regime bands in section 202 and rebate in
> section 156, but other provisions are renumbered. Use the
> [Department's mapping utility](https://www.incometaxindia.gov.in/utility-to-check-provisions-of-income-tax-act-1961-vis-a-vis-income-tax-act-2025)
> for later-year work.

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | India (भारत) |
| Tax | Income Tax + Health & Education Cess (4%) + Surcharge (if applicable) |
| Currency | INR only |
| Tax year | Financial Year (FY): 1 April -- 31 March |
| Current year | **This guide covers FY 2025-26 (AY 2026-27)** — the last year under the Income-tax Act, 1961. The current financial year, FY 2026-27, is governed by the Income-tax Act, 2025. |
| Primary legislation | Income-tax Act, 1961 (as amended for AY 2026-27, including Finance Act, 2026 filing changes) **for FY 2025-26**. From FY 2026-27: **Income-tax Act, 2025 (30 of 2025)**, in force 1 April 2026, as amended by Finance Act, 2026 |
| Tax authority | Central Board of Direct Taxes (CBDT) / Income Tax Department |
| Filing portal | incometax.gov.in |
| Filing deadline | 31 August 2026 for ITR-4 and non-audit business/professional cases in AY 2026-27; check applicable extensions and the filing category |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Chartered Accountant (India) |
| Skill version | 2.1 |

### New Tax Regime Rate Table -- FY 2025-26 (Default) [T1]

| Total Income (INR) | Rate |
|---|---|
| 0 -- 4,00,000 | 0% |
| 4,00,001 -- 8,00,000 | 5% |
| 8,00,001 -- 12,00,000 | 10% |
| 12,00,001 -- 16,00,000 | 15% |
| 16,00,001 -- 20,00,000 | 20% |
| 20,00,001 -- 24,00,000 | 25% |
| Above 24,00,000 | 30% |

**Section 87A rebate (new regime):** for a resident individual whose income is
taxed entirely at ordinary slab rates, the rebate is the lower of slab tax and
Rs. 60,000 at total income up to Rs. 12,00,000. Above that income, marginal relief
reduces tax to the excess income where slab tax would be higher. Apply this
before cess. The rebate cannot offset tax charged at special rates; such income
needs separate review. For an eligible salaried individual, deduct up to
Rs. 75,000 from the salary component before testing total income. Self-employment
receipts do not receive a salary standard deduction. Section 87A of the 1961 Act
governs this guide's year; the equivalent is section 156 of the
[2025 Act, pp. 216–217](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf).

For ordinary slab income only, with `total_income` and `slab_tax` in rupees:

```python
if total_income <= 1_200_000:
    rebate = min(slab_tax, 60_000)
else:
    rebate = max(0, slab_tax - (total_income - 1_200_000))
tax_after_rebate = slab_tax - rebate
```

Checks before surcharge and credits: income of Rs. 12,00,000 gives slab tax
Rs. 60,000 and no tax after rebate; Rs. 12,10,000 gives slab tax Rs. 61,500,
rebate Rs. 51,500 and Rs. 10,400 including cess; Rs. 13,00,000 gives slab tax
Rs. 75,000, no rebate and Rs. 78,000 including cess.


**Cess:** Add 4% Health & Education Cess on all income tax computed (after rebate).

### Old Tax Regime Rate Table (Below 60) [T1]

| Total Income (INR) | Rate |
|---|---|
| 0 -- 2,50,000 | 0% |
| 2,50,001 -- 5,00,000 | 5% |
| 5,00,001 -- 10,00,000 | 20% |
| Above 10,00,000 | 30% |

**Section 87A Rebate (Old Regime):** If taxable income ≤ Rs. 5,00,000, rebate up to Rs. 12,500 applies.

### Surcharge (Both Regimes) [T1]

| Total Income (INR) | Surcharge Rate |
|---|---|
| Up to 50,00,000 | Nil |
| 50,00,001 -- 1,00,00,000 | 10% of income tax |
| 1,00,00,001 -- 2,00,00,000 | 15% of income tax |
| 2,00,00,001 -- 5,00,00,000 | 25% of income tax (new regime only 25%) |
| Above 5,00,00,000 | 37% (old regime); 25% (new regime cap) |

### Presumptive Taxation Rates [T1]

| Section | Who | Presumptive Rate | Threshold |
|---|---|---|---|
| 44ADA | Specified professionals (doctors, lawyers, CAs, architects, consultants, etc.) | 50% of gross receipts = deemed profit | Rs. 50,00,000; Rs. 75,00,000 only if cash receipts are no more than 5% |
| 44AD | Business owners (non-professionals) | 8% of turnover (6% if digital receipts) = deemed profit | Rs. 2,00,00,000; Rs. 3,00,00,000 only if cash receipts are no more than 5% |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Regime not specified | New tax regime |
| Nature of income unclear (professional vs business) | Confirm the activity and statutory eligibility before selecting 44ADA or 44AD |
| Digital vs cash receipt mix unknown | 100% cash (8% rate under 44AD, not 6%) |
| Filing status unknown | Individual below 60 |
| TDS credits not confirmed | Exclude until Form 26AS verified |
| Advance tax paid unknown | Nil advance tax paid |

### Red Flag Thresholds [T1]

| Flag | Threshold |
|---|---|
| 44ADA limit exceeded | Gross receipts above Rs. 50,00,000, or Rs. 75,00,000 where the 5% cash test is met; assess regular accounts and audit requirements |
| 44AD limit exceeded | Turnover above Rs. 2,00,00,000, or Rs. 3,00,00,000 where the 5% cash test is met |
| Advance tax mandatory | Estimated tax payable after relevant credits is Rs. 10,000 or more (s. 208) |
| TAN and payer withholding duties | Check the applicable TDS section, payer eligibility and threshold; payment type alone does not establish a withholding duty |
| Tax audit (professional) | Assess s. 44AB separately, including gross receipts above Rs. 50,00,000 unless the applicable presumptive exception is met |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full financial year (1 April -- 31 March) in PDF, CSV, or pasted text. Confirmation of whether income is professional or business, and whether new or old regime applies.

**Recommended:** Form 26AS / Annual Information Statement (AIS) for TDS credits, advance tax challans (ITNS 280), all client invoices, Form 16A (TDS certificates from clients), PAN.

**Ideal:** Complete books of accounts (if not presumptive), all receipts for deductions under 80C/80D (old regime only), GST returns (if GST-registered).

### Refusal Catalogue

**R-IN-1 -- Non-Resident Indians (NRI) and RNOR.** "This skill covers Resident individuals only. NRI/RNOR taxation involves different income sourcing rules, DTAA analysis, and TRC requirements. Escalate."

**R-IN-2 -- Firms, Companies, LLPs.** "This skill covers individuals (sole proprietors/freelancers) only. Partnership firms, private limited companies, and LLPs file separate returns with different rates. Out of scope."

**R-IN-3 -- Capital Gains.** "Capital gains on shares, mutual funds, property, or other assets require detailed computation under Sections 111A, 112, and 112A. Escalate."

**R-IN-4 -- International Transactions / DTAA.** "Double taxation treaty analysis, foreign tax credits, and transfer pricing are out of scope. Escalate."

**R-IN-5 -- Tax Audit Cases (non-presumptive).** "If gross receipts exceed the presumptive threshold and a tax audit is required under Section 44AB, this skill cannot replace a statutory audit. Escalate."

---

## Section 3 -- Transaction Pattern Library

Use these patterns to identify transactions for review. Before applying any row, verify the invoice, payee, business purpose and whether the amount is income, a loan, an own-account transfer or a reimbursement. The narration alone cannot establish tax treatment, a gross amount, a deduction or eligibility for a presumptive scheme.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| NEFT CR / RTGS CR / IMPS CR [client name] | Gross receipts (44ADA/44AD) | Business income | Professional service fee received -- add to gross receipts |
| UPI [client name] / UPI CREDIT | Gross receipts | Business income | Digital receipt -- counts as electronic for 44AD 6% rate |
| RAZORPAY SETTLEMENT / RAZORPAY TRANSFER | Gross receipts | Business income | Payment gateway payout -- match to invoices |
| PAYTM PAYOUT / PAYTM SETTLEMENT | Gross receipts | Business income | Digital payment payout -- electronic for 44AD |
| CASHFREE SETTLEMENT / CASHFREE PAYOUT | Gross receipts | Business income | Payment aggregator payout |
| STRIPE PAYOUT INDIA / STRIPE TRANSFER | Gross receipts | Business income | International invoicing via Stripe India |
| PAYPAL TRANSFER / PAYPAL PAYOUT | Foreign income (Gross receipts) | Business income in INR | Apply the income-category and date checks in Section 6.4 |
| SALARY CREDIT / SAL ADV [employer] | Salary income (Section 17) | NOT professional income | Employment income -- separate head, Form 16 required |
| INTEREST CREDIT / INT CREDIT / FD INTEREST | Income from Other Sources | NOT business income | Bank interest taxable; FD interest TDS may apply |
| DIVIDEND CREDIT / DIV [company] | Income from Other Sources | Taxable dividends | Domestic dividends taxable since FY 2020-21 |
| REFUND FROM INCOMETAX / IT REFUND | EXCLUDE | Not income | Separate the non-income tax refund principal from taxable refund interest |
| LOAN DISBURSEMENT / LOAN CREDIT | EXCLUDE | Not income | Loan principal is liability, not income |
| GST REFUND / IGST REFUND | Review | Reconcile to the GST ledger | Determine whether the refund reverses a tax asset or an amount previously deducted; do not exclude it automatically |

### 3.2 Expense Patterns (Debits -- for ITR-3 filers; ITR-4 presumptive filers do not itemise)

| Pattern | Schedule C Category | Treatment | Notes |
|---|---|---|---|
| OFFICE RENT / COMMERCIAL RENT [landlord] | Rent | Assess business deduction | Check whether section 194-I or 194-IB applies to this payer, the threshold and current rate; do not infer the TDS rate from the narration |
| ELECTRICITY [BESCOM/MSEDCL/TATA POWER/TNEB] | Utilities | Deductible (business portion) | Home office: apportion by usage |
| BROADBAND / JIOFIBER / ACT / AIRTEL BROADBAND | Communication | Deductible (business portion) | Mixed use: apportion |
| MOBILE RECHARGE / AIRTEL / JIO / VI | Communication | Deductible (business portion) | Business calls only |
| SWIGGY BUSINESS / ZOMATO FOR BUSINESS | Meals/entertainment | Deductible if business | Document business purpose |
| AMAZON BUSINESS / FLIPKART BUSINESS | Review invoice | Expense, asset or private use | A business account does not establish deductibility; capital assets may require depreciation |
| ZOHO SUBSCRIPTION / FRESHBOOKS / TALLY | Software | Fully deductible | Business software |
| GOOGLE ADS / META ADS / LINKEDIN ADS | Advertising | Fully deductible | Digital marketing |
| CA FEES / LEGAL FEES / CONSULTANT FEES | Professional charges | Fully deductible | TDS may be required (Section 194J) |
| LIC PREMIUM / TERM INSURANCE | NOT business expense | Section 80C deduction (old regime) | Personal insurance = not a business expense |
| HEALTH INSURANCE / MEDICLAIM [Star/HDFC Ergo/Bajaj] | NOT business expense | Section 80D deduction (old regime) | NOT deductible as business expense |
| PPF DEPOSIT / ELSS PURCHASE / NSC | NOT business expense | Section 80C deduction (old regime) | Investment deductions |
| ADVANCE TAX CHALLAN / ITNS 280 | EXCLUDE | Prepaid tax | Not a business expense; credit against liability |
| TDS TO GOVT / TDS CHALLAN | Withholding liability payment | Reconcile the deductor ledger | Tax withheld from suppliers or employees is not the payer's own income-tax credit |
| GST PAYMENT / GST CHALLAN | EXCLUDE | Indirect tax | Not deductible as income tax expense |
| SWIPE / POS [vendor] | Mixed -- check | Identify payee | Could be office supply, travel, entertainment |
| PROFESSIONAL TAX [state] | Deductible | Fully deductible | State professional tax paid |
| BANK CHARGES / ACCOUNT MAINTENANCE / NEFT CHARGES | Bank charges | Fully deductible | Business account only |

### 3.3 UPI and Digital Platform Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| UPI/CR/[amount]/[client name] | Gross receipts | Electronic -- qualifies for 6% deemed profit under 44AD |
| PHONEPE CR / GPAY CREDIT / PAYTM CREDIT | Gross receipts | Digital receipt |
| BHIM UPI / BHIM CREDIT | Gross receipts | Digital receipt |
| NEFT/RTGS credits | Gross receipts | Electronic -- qualifies for 6% under 44AD |
| CHEQUE DEPOSIT / CHQ DEP | Potential gross receipts | Confirm account-payee status and timing before applying 6%; a narration alone does not establish either |
| CASH DEPOSIT / CASH / CDM | Gross receipts | CASH -- applies 8% under 44AD, not 6% |

### 3.4 TDS Deductions (Credits on Statement = Tax Credits)

| Pattern | Treatment | Notes |
|---|---|---|
| TDS BY [client name] / TDS DEDUCTED | Tax credit -- do NOT reduce income | Gross up income; claim TDS as credit on Form 26AS |
| 194J TDS / TDS 194J | Reconcile withholding | Verify the payment category, applicable rate and certificate; not every section 194J payment uses 10% |
| 194C TDS | Contractor TDS at 1%/2% | Contract payment TDS |

---

## Section 4 -- Worked Examples

### Example 1 -- UPI Payment from Client

**Input line (HDFC Bank statement):**
`15-Jun-2025 | UPI/CR/250615123456/ALPHA TECH SOLUTIONS | 85,000.00 CR | Bal 3,42,500.00`

**Reasoning:**
Credit via UPI from a business client. This is a professional fee receipt. Under Section 44ADA (professional), 50% of gross receipts = deemed profit. Under 44AD (business), 6% applies as UPI is digital/electronic. Confirm whether taxpayer is a specified professional. Receipt is electronic -- qualifies for the 6% rate if under 44AD.

**Classification:** Gross receipts Rs. 85,000. Add to annual total.

### Example 2 -- Razorpay Settlement

**Input line (ICICI Bank statement):**
`22-Aug-2025 | RAZORPAY SOFTWARE PVT LTD | 1,24,650.00 CR | Ref: RPY2025082211234`

**Reasoning:**
Razorpay collects payments on behalf of the seller, deducts their fee, and pays out net amount. Assume the settlement report confirms customer receipts of Rs. 1,25,000 and fees of Rs. 350, with no other adjustments. Reconcile the net Rs. 1,24,650 to that report; the bank line alone cannot supply the fee. Record gross business receipts of Rs. 1,25,000 before computing profit. Eligible fees are assessed separately under regular computation; presumptive filers cannot deduct them again.

**Classification:** Gross receipts Rs. 1,25,000. Razorpay fee Rs. 350 is deductible for non-presumptive filers only.

### Example 3 -- LIC Premium Payment

**Input line (SBI Bank statement):**
`01-Apr-2025 | LIC PREMIUM/OTH/NEFT | 45,000.00 DR | Balance 2,85,000.00`

**Reasoning:**
Life insurance premium. This is NOT a business expense. Under the old regime, LIC premium qualifies for Section 80C deduction up to Rs. 1,50,000 combined limit. Under the new regime, 80C deductions are not available. Cannot be classified as a deductible business expense in either regime.

**Classification:** EXCLUDE from business expenses. Old regime: add to 80C pool (max Rs. 1,50,000 combined). New regime: no deduction.

### Example 4 -- TDS Deducted by Client

**Input line (Axis Bank statement):**
`10-Jul-2025 | NEFT CR/MNRVA CONSULTING/INV0042 LESS TDS | 90,000.00 CR`

**Reasoning:**
Assume the invoice and TDS certificate confirm that the client paid Rs. 90,000 after deducting 10% TDS on a Rs. 1,00,000 invoice. The gross income is Rs. 1,00,000 (not Rs. 90,000). The TDS of Rs. 10,000 is a tax credit visible in Form 26AS. Report Rs. 1,00,000 as gross receipt and claim Rs. 10,000 TDS as credit.

**Classification:** Gross receipts Rs. 1,00,000. TDS credit Rs. 10,000 (verify in Form 26AS).

### Example 5 -- Cash Deposit

**Input line (Kotak Bank statement):**
`05-Sep-2025 | CASH DEPOSIT / CDM / BRANCH | 30,000.00 CR`

**Reasoning:**
Cash deposit. For 44AD taxpayers, cash receipts are taxed at 8% deemed profit (not the 6% digital rate). For 44ADA professionals, cash and digital are both 50% deemed -- no distinction. Cannot treat as digital receipt. Ask: was this cash collected from a client for a business service?

**Classification:** pending confirmation of the source. If the deposit represents business receipts not already recorded, add Rs. 30,000 to cash receipts; otherwise record the supported transfer, loan or other treatment.

### Example 6 -- Advance Tax Challan Payment

**Input line (HDFC Bank statement):**
`14-Sep-2025 | INCOMETAX DEPT/ITNS 280/ADVANCE TAX | 25,000.00 DR`

**Reasoning:**
Advance tax payment to the Income Tax Department. This is NOT a business expense -- it is a prepayment of income tax liability. Record as advance tax paid (to be credited against final liability). Check Section 5.4: eligible 44AD/44ADA filers pay the whole advance tax by 15 March; other covered taxpayers use the instalment schedule when the statutory Rs. 10,000 test is met.

**Classification:** EXCLUDE from income/expenses. Record: advance tax paid Rs. 25,000; apply it to the taxpayer's applicable instalment schedule.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Presumptive Taxation -- Section 44ADA (Professionals)

**Legislation:** Section 44ADA, Income Tax Act, 1961

Applicable to specified professionals: legal, medical, engineering, architecture, accountancy, technical consultancy, interior decoration, and any other profession notified by CBDT.

- Gross receipts up to Rs. 50,00,000: apply the ordinary ceiling. The ceiling rises to Rs. 75,00,000 only where cash receipts are no more than 5% of total gross receipts. Non-account-payee cheques and drafts count as cash for this test.
- Deemed profit = 50% of gross receipts (taxpayer may declare higher)
- Maintain evidence of gross receipts, cash receipts and scheme eligibility. The presumptive books exemption does not dispense with records needed for other taxes or obligations.
- Use ITR-4 only if its separate total-income and other eligibility tests are met; otherwise use the applicable ITR-3 schedules.
- No deduction for actual expenses allowed -- 50% covers all

### 5.2 Presumptive Taxation -- Section 44AD (Business)

**Legislation:** Section 44AD, Income Tax Act, 1961

Applies to an eligible resident business with turnover up to Rs. 2,00,00,000, rising to Rs. 3,00,00,000 only where cash receipts are no more than 5% of turnover. Non-account-payee cheques and drafts count as cash for this test. Exclude agency business, commission or brokerage income, specified professions and goods-carriage businesses covered by section 44AE. Check the section 44AD(4) five-year exclusion where the taxpayer previously left the scheme.

- Deemed profit = 8% of gross turnover (cash receipts)
- Deemed profit = 6% on qualifying receipts through an account-payee cheque or draft, electronic clearing through a bank account, or a prescribed electronic mode, received during the year or by the section 139(1) return due date. Apply 8% to the remaining turnover.
- Mixed receipts: apply 6%/8% pro-rata
- Use ITR-4 only if its separate total-income and other eligibility tests are met; otherwise use the applicable ITR-3 schedules.

The Department's [ITR-4 FAQs, questions 9–16](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs)
explain the cash conditions, excluded activities and 15 March rule. The linked page covers AY 2026-27. Verify the assessment year when using a
different form or an archived FAQ.

### 5.3 Tax Computation Flow (New Regime)

```
Gross receipts / turnover
- Presumptive expenses (44ADA: 50% of gross; 44AD: 92-94% of gross)
= Presumptive profit (Business Income)
+ Other income (interest, dividends, salary)
= Gross Total Income
- Standard deduction for salaried component (if any)
= Total Income
Apply rate table (Section 1)
= Slab tax
- Section 87A rebate, including marginal relief (Section 1)
= Tax after rebate
+ Applicable surcharge after surcharge marginal relief
x 1.04 (add 4% cess)
= Total Tax Payable
- TDS credits (from Form 26AS)
- Advance tax paid
= Tax due / refund
```

Apply the statutory rounding of total income under section 288A and the final
payable or refundable amount under section 288B. The examples above show the
calculation before that rounding.

### 5.4 Advance Tax Schedule

**Legislation:** Sections 208 and 211, Income-tax Act, 1961.

An eligible taxpayer declaring profits under section 44AD or 44ADA pays **100%
by 15 March**. The table below applies to other taxpayers within this guide's
scope. Check estimated tax payable after relevant TDS/TCS and other statutory
credits; advance tax applies at **Rs. 10,000 or more**.

| Instalment | Due Date | Cumulative % of Liability |
|---|---|---|
| 1st | 15 June | 15% |
| 2nd | 15 September | 45% |
| 3rd | 15 December | 75% |
| 4th (final) | 15 March | 100% |

Assess sections 234B and 234C separately for any shortfall. A payment by 31 March is advance tax for that year, but does not retrospectively meet an earlier instalment deadline.

### 5.5 Interest for Late Payment / Default

| Situation | Interest | Section |
|---|---|---|
| Instalment shortfall | Apply the statutory instalment base and periods, including the single 15 March instalment for 44AD/44ADA | 234C |
| Advance tax below 90% of assessed tax | 1% per month or part from 1 April on the statutory shortfall, subject to payments and statutory adjustments | 234B |
| Return after the applicable due date | 1% per month or part on the statutory unpaid-tax base; use the applicable notified due date | 234A |

### 5.6 Filing Deadlines

| Scenario | Deadline |
|---|---|
| Non-audit business/professional cases, including ITR-4 | 31 August 2026 (AY 2026-27) |
| Tax audit cases (Section 44AB) | 31 October 2026 |
| Belated return | 31 December 2026, or completion of assessment if earlier; applicable late fee and interest |
| Revised return | 31 March 2027, or completion of assessment if earlier; section 234-I fee applies after 31 December 2026 |

Check notified extensions and the taxpayer's filing category before using these
dates. The Department's [ITR-4 FAQ, question 22](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs)
states 31 August 2026. Its [ITR-1 FAQs, questions 19–20](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ITR1-FAQ)
explain the AY 2026-27 extension of the revised-return period to 31 March and
the additional section 234-I fee. The revised-return extension does not extend
the original or belated-return deadline.

### 5.7 Non-Deductible Items (Both Regimes)

| Item | Reason |
|---|---|
| Income tax itself (advance tax, self-assessment tax) | Not deductible |
| LIC premiums, PPF, ELSS | Personal investments (80C in old regime only) |
| Mediclaim/health insurance | Section 80D (old regime only) |
| Personal drawings / withdrawals | Not a business expense |
| GST paid on sales | Indirect tax, not income tax deduction |
| Fines and penalties | Not incurred for business |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Regime Selection Optimisation

For business or professional income, a preference alone does not elect the old
regime. Verify Form 10-IEA was filed by the applicable section 139(1) due date,
and check the taxpayer's earlier elections and the restricted return to the new
regime. See the Department's ITR-4 FAQs, questions 4–6.

Compute the tax under both available regimes using each regime's deductions, exemptions, rebates, surcharge and cess. Compare the final tax amounts. A deduction amount cannot be compared directly with a tax saving.

### 6.2 Mixed Professional and Business Income

Do not automatically combine 44ADA with 44AD. Section 44AD(6) excludes a person
carrying on a profession referred to in section 44AA(1). Establish eligibility
for each activity and whether regular computation is required before combining
the resulting income. Refer mixed professional and business cases for review.

### 6.3 Home Office Deduction (ITR-3 filers only)

Self-employed persons maintaining regular books (ITR-3) may claim proportionate rent, electricity, and internet for a home office. Acceptable apportionment: floor area ratio or dedicated usage hours. 44ADA/44AD presumptive filers cannot claim this separately -- covered by deemed profit.

### 6.4 PayPal / Foreign Client Receipts

Apply Income-tax Rule 115 using the income category and specified conversion date; an RBI rate or receipt-date rate is not an interchangeable default. Reconcile any different accounting conversion and obtain review of foreign receipts and related GST obligations.

### 6.5 Clubbing of Income (Spouse / Minor)

If income earned by a spouse or minor child is attributable to the taxpayer's assets or business, it may be clubbed with the taxpayer's income. Flag for reviewer if transfers to spouse or minor detected.

---

## Section 7 -- Excel Working Paper Template

```
INDIA INCOME TAX WORKING PAPER -- FY 2025-26
Taxpayer name: _______________  PAN: ___________
Filing form: ITR-4 / ITR-3 after eligibility review [circle one]
Regime: New / Old [circle one]

A. GROSS RECEIPTS / TURNOVER
  A1. Receipts qualifying for the 44AD 6% rate   ___________
  A2. Remaining receipts                                  ___________
  A3. Total gross receipts (A1 + A2)                ___________

B. BUSINESS / PROFESSIONAL PROFIT
  B1. 44ADA: A3 x 50%                               ___________
  B2. 44AD qualifying receipts: A1 x 6%                         ___________
  B3. 44AD remaining receipts: A2 x 8%                            ___________
  B4. Profit: eligible presumptive amount above,
      or regular profit from supporting schedule              ___________

C. OTHER INCOME
  C1. Interest income                                ___________
  C2. Dividend income                                ___________
  C3. Taxable salary / pension after its permitted
      standard deduction                            ___________
  C4. Total other income                             ___________

D. GROSS TOTAL INCOME (B4 + C4)                     ___________

E. DEDUCTIONS (check eligibility for the selected regime)
  E1. Section 80C (LIC, PPF, ELSS, tuition, etc.)  ___________
  E2. Section 80D (health insurance)                ___________
  E3. Section 80G (donations)                       ___________
  E4. Total permitted deductions (80C cap: 1,50,000)          ___________

F. TOTAL INCOME (D - E)                              ___________

G. TAX COMPUTATION
  G1. Income tax (per rate table)                    ___________
  G2. Less: Section 87A rebate and marginal relief
      from Section 1 (ordinary slab income only)      ___________
  G3. Surcharge (if applicable)                      ___________
  G4. Health & Education Cess (4% of G1+G3-G2)     ___________
  G5. Total tax payable                              ___________

H. TAX CREDITS
  H1. TDS (from Form 26AS)                          ___________
  H2. Advance tax paid                               ___________
  H3. Total credits                                  ___________

I. NET TAX DUE / REFUND (G5 - H3)                  ___________

REVIEWER FLAGS:
  [ ] Form 26AS verified against bank statement?
  [ ] Regime choice confirmed?
  [ ] Cash vs digital receipt split confirmed?
  [ ] TDS certificates received for all credits?
  [ ] Advance tax interest computed (234B/234C)?
```

---

## Section 8 -- Bank Statement Reading Guide

### Indian Bank Statement Formats

| Bank | Key Format | Key Fields |
|---|---|---|
| HDFC Bank | CSV / PDF | Date, Narration, Value Date, Debit, Credit, Closing Balance |
| ICICI Bank | CSV / Excel | S.No, Value Date, Transaction Date, Cheque/Ref No, Transaction Remarks, Withdrawal (Dr), Deposit (Cr), Balance |
| SBI | CSV / PDF | Txn Date, Value Date, Description, Ref No/Cheque No, Debit, Credit, Balance |
| Axis Bank | CSV | Tran Date, CHQNO, Particulars, Debit, Credit, Balance |
| Kotak Mahindra | XLS | Date, Description, Chq/Ref No, Debit(INR), Credit(INR), Bal(INR) |

### Key Narration Patterns

| Narration | Meaning | Tax Action |
|---|---|---|
| NEFT/CR/[ref]/[sender] | Electronic credit via NEFT | Business income |
| UPI/CR/[date]/[ref]/[sender] | UPI credit | Business income (digital) |
| CASH DEP / CDM | Cash deposit | Business income (cash) |
| TRF TO [own account] | Internal transfer | Exclude |
| IMPS/[ref]/[name] | IMPS credit | Business income (digital) |
| ATW/[ATM ref]/[branch] | ATM withdrawal | Investigate -- personal or business? |
| INT PD / INTEREST CREDIT | Bank interest | Other income |
| SALARY/SAL | Salary credit | Employment income |
| ADVNC TAX / ITNS 280 | Advance tax payment | Tax prepayment (credit) |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Identify UPI/NEFT/RTGS/cheque credits as potential receipts; verify source and, for cheques, account-payee status before assigning a presumptive rate
2. Classify all CDM/cash deposits as potential gross receipts (cash)
3. Use the new regime by default; leave presumptive profit pending until the activity, scheme eligibility and cash-limit tests are confirmed
4. Mark all salary credits and interest separately
5. Flag advance tax challans as prepaid tax credits
6. Generate working paper with clear PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- INDIA INCOME TAX
1. Are you a specified professional (doctor, CA, lawyer, architect, etc.) or a general business?
2. New or old tax regime? (Default: new)
3. Total gross receipts for FY 2025-26?
4. What % of receipts were received via UPI/NEFT/RTGS/cheque (vs cash)?
5. TDS deducted by clients -- do you have Form 26AS / AIS downloaded?
6. Advance tax paid -- any ITNS 280 challans this year?
7. Old regime only: any LIC, PPF, ELSS, health insurance, home loan repayments?
8. Is your PAN linked to your bank account?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Section |
|---|---|
| Presumptive taxation (professionals) | Section 44ADA |
| Presumptive taxation (business) | Section 44AD |
| New tax regime | Section 115BAC |
| Advance tax | Sections 207-219 |
| Interest for default | Sections 234A, 234B, 234C |
| TDS on professional fees | Section 194J |
| TDS on rent | Section 194I |
| Section 80C deductions | Section 80C |
| Health insurance deduction | Section 80D |

### ITR Form Guide

| Form | Who Uses It |
|---|---|
| ITR-4 (Sugam) | Eligible presumptive income, total income ≤ Rs. 50,00,000, and all other AY 2026-27 form conditions met |
| ITR-3 | Business/professional income, including presumptive income where ITR-4 is unavailable |
| ITR-1 (Sahaj) | Salaried individuals only, no business income |

### Known Gaps / Out of Scope

- Capital gains (Sections 111A, 112, 112A)
- NRI / RNOR taxation
- Partnership firms, companies, LLPs
- DTAA / double taxation relief
- Cryptocurrency taxation (VDA -- Section 115BBH)

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.1 | 2026-09-11 | Rebate flow, conditional presumptive limits, return eligibility and advance-tax schedule corrected |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; transaction pattern library; local bank formats; worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] New regime applied by default unless old regime confirmed?
- [ ] 4% cess applied after rebate?
- [ ] Surcharge checked for income > Rs. 50,00,000?
- [ ] Cash vs digital receipts split verified for 44AD?
- [ ] TDS credits verified against Form 26AS, not just bank statement?
- [ ] Correct advance-tax schedule selected and sections 234B/234C checked on their statutory bases?

---

## PROHIBITIONS

- NEVER apply old regime without explicit confirmation from client
- NEVER allow LIC/PPF/health insurance premiums as business expenses (they are 80C/80D items in old regime only)
- NEVER use net bank receipt as gross income when TDS was deducted -- always gross up
- NEVER allow income tax (advance tax, self-assessment tax) as a business deduction
- NEVER apply the 6% deemed profit rate to cash receipts under 44AD (8% applies)
- NEVER advise NRI clients using this skill -- escalate
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Chartered Accountant for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant or equivalent licensed practitioner in India) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
