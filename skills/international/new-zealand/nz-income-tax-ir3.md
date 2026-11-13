---
name: nz-income-tax-ir3
description: Reconcile a full-year New Zealand resident individual’s 2025-26 IR3 return with a 31 March balance date. Covers ordinary salary, sole-trader and schedular income, New Zealand bank interest and ordinary New Zealand dividends. Aggregate supported income and deductions, calculate annual income tax and IETC, separate ACC from PAYE and apply imputation limits before refundable credits. Reconcile residual income tax, provisional payments and the terminal balance. Use for IR3, annual income tax, mixed salary and business income, withholding credits, IETC or provisional tax handoff. Refer complex income, residence, deductions and other assessments for separate review.
version: 2.2
jurisdiction: NZ
tax_year: 2026
tax_year_notes: "2025-26 annual return; separate handoff for 2026-27 provisional tax"
last_updated: 2026-11-13
review_status: pending_review
verified_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand annual individual income tax, IR3

## Scope and filing requirements

This workflow covers **1 April 2025 to 31 March 2026**, using the 2026 IR3 form (July 2026) and IR3G (August 2026). It assumes a confirmed full-year NZ resident individual with a 31 March balance date. It reconciles ordinary salary, separate sole-trader/schedular income, NZ bank interest and ordinary NZ dividends. It does not establish residence or whether a particular receipt or deduction qualifies. [S1][S1] [S2][S2]

An IR3 is required when IRD tells the person to file and for relevant income outside the automatic assessment system. Salary and interest alone do not necessarily require an IR3. Confirm the filing obligation before using this return workflow. [S2, pp 5–6][S2]

| 2025-26 obligation | Ordinary date and condition |
|---|---|
| IR3 without an extension | 7 July 2026 |
| Tax-agent extension of time | Up to 31 March 2027, only where the extension actually applies |
| Terminal income tax | 9 February 2027 after the nominal 7 February Sunday and the 8 February observed public holiday; confirm myIR |
| Tax-agent terminal date | 7 April 2027 where the relevant agent/extension conditions apply; confirm the account’s date |

RA 13(2) and (4) require notification that the return will be filed by a tax agent who has a section 37(4) extension; merely hiring an agent does not establish the April terminal date. [S10][S10]

The current IRD extension page says 31 March of the following filing year. The IR3G p 7 reference to 31 March 2026 is inconsistent with that rule and the return period; do not use it as the extension date. IR3G p 54 confirms the nominal February/April 2027 payment dates. The 9 February date above is derived from that rule and the government’s 2027 holiday calendar. [S9][S9] Payment dates falling on a weekend or public holiday move under IRD’s payment-day rule; provincial anniversary days have a separate electronic-payment rule. [S2, pp 7,54][S2] [S6][S6] [S7][S7] [S8][S8]

Earlier tax years need their own form, rates and credit rules. The 2024-25 composite rates and IETC transition must not be replaced with this full-year schedule. [S3][S3]

## Required inputs and stops

A bank statement alone is insufficient. Obtain the following reconciled records before calculating. Use synthetic information in demonstrations.

| Input | Required distinction |
|---|---|
| Period, residence and filing | Confirmed full-year residence, balance date, IR3 obligation and any extension |
| Salary summary | Gross salary, reconciled SOI income-tax credit or employer PAYE before payroll-giving credits, any extinguished credit, ACC-liable/nonliable amounts and annual ACC levy; exclude KiwiSaver, student-loan or other deductions from the income-tax credit |
| Business/schedular records | Gross income, GST status and treatment, actual withholding, allowable expenses and proof that income appears in only 1 category |
| NZ bank interest | Gross interest, actual RWT, any negative interest repaid and whether/when a term deposit was broken in full, including all accounts and the supported ownership share |
| Ordinary NZ dividends | Net dividend, NZ imputation credits and dividend RWT, with gross income reconciled to the statement |
| Losses and other expenses | Supported loss balance/amount claimable and deductions not already included in business or schedular net income |
| IETC | Net income before brought-forward losses and a month-by-month eligibility record, including benefit, pension and WFF facts |
| Imputation brought forward | IRD’s confirmed excess-credit balance, distinct from a brought-forward income loss |
| Payments | Income-tax account showing provisional payments actually allocated to this tax year, separately from income-tax withholding credits |

The return and worksheets require these separate categories and credit fields. [S1, Questions 11–14,21,24,28–36][S1] [S2, pp 11–17,38–45][S2]

Stop the affected calculation when evidence is missing or inconsistent. Do not invent a schedular withholding rate, vehicle percentage, processor fee, expense allowance or IETC eligibility. A narration such as ‘transfer’, ‘salary’, ‘tax’ or ‘ACC’ is a reconciliation lead, not sufficient tax classification. Do not infer a filing extension from an accountant payment in a bank statement.

Route nonresident, part-year or transitional residence; foreign income/foreign tax credits; FIF/CFC; PIE outcomes; trusts/partnership allocations; rental/property-sale regimes; WFF calculations; student-loan assessments and disputed losses or deductions to their own supported review. Ordinary company turnover is not the individual’s sole-trader income. Do not certify an overall refund until any separate assessment or offset has been reconciled. The IR3 form expressly warns that WFF can change the final balance. [S1, Questions 16–23,35,38,41][S1] [S2, pp 40,42–46,54][S2]

## Build the annual income and credit schedule

1. **Salary, Question 11.** Include gross salary once. For ordinary salary, IR3G’s annual worksheet takes the ACC-liable part of salary, caps it at **$152,790** and applies **1.67%**. The guide gives a maximum levy of **$2,551.59**. Use the reconciled SOI Box 11E where available. When deriving it from employer records, start with PAYE **before** payroll donation tax credits, subtract any extinguished donation credit to reach Box 11A, then subtract the annual ACC levy to get Box 11E. A payroll cash deduction after donation credits is not that starting figure. Reconcile nonliable income and any unusual employment amounts separately; do not subtract the whole payroll net-pay deduction total. [S2, pp 11–13][S2]
2. **Schedular income, Question 12.** Use the payer’s gross amount and actual tax withheld. Deduct related allowable expenses at 12C to reach 12D. If the gross schedular amount includes GST and the person is GST registered, reconcile the GST-exclusive income entry. Do not report the same Summary of Income receipt again at Question 24 or claim its expenses again at 29. A known net receipt plus evidenced withholding can reconcile to gross; a guessed percentage cannot. [S1, Questions 12,24,29][S1] [S2, p 15][S2]
3. **Interest, Question 13.** Report gross NZ interest and keep RWT separately. Net bank interest is not the gross income entry. If a term deposit was broken **in full**, the IR3G worksheet subtracts evidenced negative interest repaid from certificate gross interest for 13B. In other cases, that negative-interest deduction is deferred to the return when the deposit matures. Keep actual RWT separate and resolve a negative overall entry or financial-arrangement adjustment before continuing. [S1, Question 13][S1] [S2, pp 15–17][S2]
4. **Dividends, Question 14.** For supported ordinary NZ dividends, gross income equals net dividend received plus NZ imputation credits plus dividend RWT. Record the 2 credits separately. This is not a rule for PIE, FIF or foreign franking credits. [S2, p 17][S2]
5. **Sole trader, Question 24.** Enter supported net self-employment income that is not already included from the Summary of Income. Classify expenses using their evidence and applicable deduction rules; this annual reconciliation does not authorise an expense merely because its narration resembles a business purchase. [S1, Question 24][S1] [S2, pp 34,38–39][S2]
6. **Total and losses.** Reconcile supported categories through 21B and 28, deduct other allowable expenses once at 29 and reach **net income at 30**. Deduct only the supported current claim of brought-forward losses at 31B to reach **taxable income at 32**. Net income at 30, not taxable income after those brought-forward losses, controls IETC. If the overall result is a loss or the loss balance/availability is unresolved, obtain a separate loss reconciliation. [S1, Questions 21,28–33][S1] [S2, pp 39–40][S2]

For GST-registered amounts, use the appropriate GST-exclusive entries; do not strip GST indiscriminately from salary, interest or every bank receipt. Schedular and other deductions already claimed elsewhere must not be deducted twice. Self-employed ACC invoices remain a separate levy reconciliation; do not add them to RIT or use them as withholding credits. Any deduction for an invoice component needs its own substantiated treatment. [S2, pp 15,38–39][S2]

## Tax and credit calculation

### Annual income tax for 2025-26

Use the whole-dollar taxable-income entry required by the IR3 worksheet, supported by the return records. Preserve source statement precision and resolve any entry-rounding discrepancy before filing. The examples below use whole-dollar income and expense entries and separately stated credit amounts. [S1, Box 32][S1] [S2, p 44][S2]

| Taxable income | Rate on the part in this band | Tax at lower threshold |
|---|---|---|
| $0 to $15,600 | 10.5% | $0 |
| Over $15,600 to $53,500 | 17.5% | $1,638.00 |
| Over $53,500 to $78,100 | 30% | $8,270.50 |
| Over $78,100 to $180,000 | 33% | $15,650.50 |
| Over $180,000 | 39% | $49,277.50 |

Tax equals the lower-threshold tax plus the marginal rate on the excess above that threshold. The 33% band starts above **$78,100**. IR3G p 43 prints $78,101 in its subtraction-threshold column; that would understate this band’s tax by $0.33. Use the published rate boundaries above, not that printed subtraction figure. Schedule 1 part A table 1 confirms the bands and its history records the 1 April 2025 replacement. [S11][S11] [S3][S3] [S2, pp 43–44][S2]

### Annual IETC

Use **net income at Box 30**, before brought-forward losses. For each whole month, establish all LC 13(1) conditions. In particular, the person must be resident and not receive a main benefit, NZ Super, veteran’s pension or an overseas equivalent. The person must not be both entitled to and receiving WFF; the same entitlement-and-receipt test applies to the spouse/civil union/de facto partner. The overseas-equivalent tax-credit conditions also apply. A disqualifying day removes that whole month. Read LC 13’s exact conditions when entitlement and receipt differ; do not replace them with an assumption based on income alone. [S4][S4] [S2, pp 40–41][S2]

If net income is below **$24,000**, IETC is zero. Otherwise, calculate the positive part of **$520 minus $0.13 for each complete dollar of net income above $66,000**, then multiply by qualifying whole months/12. It reaches zero at **$70,000**. A credit already reflected in ME payroll deductions is reconciled through the actual annual PAYE income-tax credit; do not add a second payroll IETC claim. [S4, LC 13(2)–(6)][S4] [S2, pp 40–45][S2]

### Credit order and final balance

For this supported slice, there is no foreign-tax-credit or PIE adjustment. Follow the Question 36 worksheet in this order. [S2, pp 44–45][S2]

1. Calculate tax on taxable income, then subtract annual IETC with a floor of zero.
2. Add current NZ imputation credits to the confirmed imputation balance brought forward. Apply them up to the remaining tax. Excess imputation is **carried forward, not refunded**; reconcile IRD’s confirmation.
3. Separately total refundable income-tax credits: Box 11E PAYE income tax, actual schedular withholding, NZ interest RWT and ordinary dividend RWT. Subtract these from the tax remaining after imputation. This **signed amount is RIT**, Box 36A. A negative result is a credit, not an extra imputation refund.
4. Subtract provisional income-tax payments allocated to **2025-26**. The result is **Question 36B before any Question 37 early payment discount**: positive means tax to pay, negative means an income-tax refund before other assessments/offsets. Provisional payments reduce the balance, not RIT and not business profit.
5. Check Question 37 before treating 36B as the final amount payable. A possible early payment discount needs a separate eligibility/payment-history/election review under IR3G pp 47–49. This guide does not calculate it; all worked balances below assume no such discount and no other assessment or offset.
6. Pass the **2026 RIT**, not the post-payment balance, to [NZ provisional tax](nz-provisional-tax.md). Prior-year RIT above **$5,000** ordinarily creates a following-year provisional obligation; exactly $5,000 does not under the prior-year rule. The companion checks the standard method’s filing timing, uplift and instalment exceptions. [S5][S5]

Eligible donation credits outside payroll giving are claimed separately through IR526/myIR. Payroll giving is handled through the correct PAYE input above; do not add the same credit again. A donation credit is not an extra business deduction or one of this worksheet’s refundable withholding inputs. [S2, p 40][S2]

## Worked examples and executable self-checks

All cases are synthetic, conditional on the evidence and scope above. Their arithmetic checks do not establish deduction eligibility, residence, IETC facts or filing readiness. Cases 1–7 exercise annual reconciliation; the IETC boundary cases exercise their stated eligibility branch.

### Case 1: sole trader, annual balance due

Confirmed sole-trader receipts of $90,000 less $30,000 of allowable expenses give $60,000 net income. All 12 months qualify for IETC. There are no withholding or imputation credits. Allocated provisional payments are $8,000. The balance is $1,700.50.

```oa-check
name: nz-2026-ir3-sole-trader-balance
tolerance: 0
inputs:
  receipts: 90000
  expenses: 30000
  qualifying_months: 12
  provisional_paid: 8000
steps:
  net_income: receipts - expenses
  taxable_income: net_income
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  ietc: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0) * qualifying_months / 12
  rit: max(income_tax - ietc, 0)
  balance: rit - provisional_paid
expected:
  net_income: 60000
  income_tax: 10220.5
  ietc: 520
  rit: 9700.5
  balance: 1700.5
```

### Case 2: salary plus self-employment, ACC separated

Salary is $60,000 and net self-employment income is $20,000. Total PAYE is $11,222.50, including $1,002 ACC earners’ levy. Only $10,220.50 is an income-tax credit. Taxable income is $80,000, IETC is nil and RIT is $6,057. No provisional payments have been made.

```oa-check
name: nz-2026-ir3-salary-plus-business
tolerance: 0
inputs:
  salary: 60000
  business_net: 20000
  total_paye: 11222.5
  acc_levy: 1002
steps:
  taxable_income: salary + business_net
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  paye_tax_credit: total_paye - acc_levy
  rit: income_tax - paye_tax_credit
expected:
  taxable_income: 80000
  income_tax: 16277.5
  paye_tax_credit: 10220.5
  rit: 6057
```

### Case 3: salary and gross bank interest, refund

Salary is $50,000 and gross NZ bank interest is $2,000. Salary PAYE is $8,493 including $835 ACC; interest RWT is $660. The taxpayer qualifies for IETC for all 12 months. RIT is a credit of $830 before any provisional payments.

```oa-check
name: nz-2026-ir3-interest-and-paye-refund
tolerance: 0
inputs:
  salary: 50000
  gross_interest: 2000
  total_paye: 8493
  acc_levy: 835
  interest_rwt: 660
  qualifying_months: 12
steps:
  net_income: salary + gross_interest
  taxable_income: net_income
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  ietc: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0) * qualifying_months / 12
  paye_tax_credit: total_paye - acc_levy
  rit: max(income_tax - ietc, 0) - paye_tax_credit - interest_rwt
expected:
  net_income: 52000
  income_tax: 8008
  ietc: 520
  paye_tax_credit: 7658
  rit: -830
```

### Case 4: schedular gross income and actual withholding

The payer’s statement confirms gross schedular income of $40,000 and $8,000 tax withheld; bank receipts are $32,000. Confirmed related expenses are $5,000. This income is entered once, at Question 12. With 12 qualifying IETC months, RIT is a credit of $3,487. No withholding rate is inferred from a narration.

```oa-check
name: nz-2026-ir3-schedular-gross-and-credit
tolerance: 0
inputs:
  bank_received: 32000
  withheld_tax: 8000
  related_expenses: 5000
  qualifying_months: 12
steps:
  gross_schedular: bank_received + withheld_tax
  net_income: gross_schedular - related_expenses
  taxable_income: net_income
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  ietc: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0) * qualifying_months / 12
  rit: max(income_tax - ietc, 0) - withheld_tax
expected:
  gross_schedular: 40000
  net_income: 35000
  income_tax: 5033
  ietc: 520
  rit: -3487
```

### Case 5: dividend imputation is not a cash refund

An ordinary NZ dividend statement shows $6,700 net cash, $2,800 imputation and $500 RWT. Gross dividend income is $10,000. Income tax is $1,050 and no IETC is available. Imputation used is $1,050, excess imputation carried forward is $1,750 and RIT is a credit of $500, solely from RWT.

```oa-check
name: nz-2026-ir3-imputation-carryforward
tolerance: 0
inputs:
  net_dividend: 6700
  imputation_current: 2800
  dividend_rwt: 500
steps:
  taxable_income: net_dividend + imputation_current + dividend_rwt
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  imputation_used: min(imputation_current, income_tax)
  imputation_carried: max(imputation_current - income_tax, 0)
  rit: max(income_tax - imputation_current, 0) - dividend_rwt
expected:
  taxable_income: 10000
  income_tax: 1050
  imputation_used: 1050
  imputation_carried: 1750
  rit: -500
```

### Case 6: all supported income categories, no double counting

Confirmed salary is $40,000, separate sole-trader profit is $25,000, gross schedular income is $12,000 with $2,000 related expenses, interest is $2,000 and gross ordinary NZ dividends are $3,000. Other allowable expenses of $1,000 have not been claimed elsewhere. Dividend imputation is $840; refundable credits are $5,908 salary income tax, $2,400 schedular tax, $660 interest RWT and $150 dividend RWT. After $6,000 allocated provisional payments, the result is a $10.50 refund. IETC is nil.

```oa-check
name: nz-2026-ir3-all-supported-categories
tolerance: 0
inputs:
  salary: 40000
  business_net: 25000
  schedular_gross: 12000
  schedular_expenses: 2000
  gross_interest: 2000
  gross_dividends: 3000
  other_expenses: 1000
  imputation: 840
  paye_income_tax: 5908
  schedular_tax: 2400
  interest_rwt: 660
  dividend_rwt: 150
  provisional_paid: 6000
steps:
  schedular_net: schedular_gross - schedular_expenses
  taxable_income: salary + business_net + schedular_net + gross_interest + gross_dividends - other_expenses
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  tax_after_imputation: max(income_tax - imputation, 0)
  refundable_credits: paye_income_tax + schedular_tax + interest_rwt + dividend_rwt
  rit: tax_after_imputation - refundable_credits
  balance: rit - provisional_paid
expected:
  schedular_net: 10000
  taxable_income: 79000
  income_tax: 15947.5
  tax_after_imputation: 15107.5
  refundable_credits: 9118
  rit: 5989.5
  balance: -10.5
```

### Case 7: IETC uses net income before a brought-forward loss

Net income before brought-forward losses is $67,000. A supported $3,000 loss claim reduces taxable income to $64,000. IETC still abates on $67,000, giving $390 for 12 qualifying months. With no other credits, RIT is $11,030.50.

```oa-check
name: nz-2026-ir3-loss-does-not-reset-ietc
tolerance: 0
inputs:
  net_income: 67000
  loss_claim: 3000
  qualifying_months: 12
steps:
  taxable_income: net_income - loss_claim
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  ietc: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0) * qualifying_months / 12
  rit: max(income_tax - ietc, 0)
expected:
  taxable_income: 64000
  income_tax: 11420.5
  ietc: 390
  rit: 11030.5
```

### IETC boundary: lower-ineligible

Confirmed net income before brought-forward losses is $23,999, with 12 qualifying whole months. The lower-income eligibility branch is selected before abatement. The credit is $0.00. These are annual credits, not additional weekly payroll credits.

```oa-check
name: nz-2026-ir3-ietc-lower-ineligible
tolerance: 0
inputs:
  net_income: 23999
  qualifying_months: 12
steps:
  full_year_entitlement: 0 * net_income
  ietc: full_year_entitlement * qualifying_months / 12
expected:
  full_year_entitlement: 0
  ietc: 0
```

### IETC boundary: lower-eligible

Confirmed net income before brought-forward losses is $24,000, with 12 qualifying whole months. The lower-income eligibility branch is selected before abatement. The credit is $520.00. These are annual credits, not additional weekly payroll credits.

```oa-check
name: nz-2026-ir3-ietc-lower-eligible
tolerance: 0
inputs:
  net_income: 24000
  qualifying_months: 12
steps:
  full_year_entitlement: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0)
  ietc: full_year_entitlement * qualifying_months / 12
expected:
  full_year_entitlement: 520
  ietc: 520
```

### IETC boundary: abatement-start

Confirmed net income before brought-forward losses is $66,000, with 6 qualifying whole months. The lower-income eligibility branch is selected before abatement. The credit is $260.00. These are annual credits, not additional weekly payroll credits.

```oa-check
name: nz-2026-ir3-ietc-abatement-start
tolerance: 0
inputs:
  net_income: 66000
  qualifying_months: 6
steps:
  full_year_entitlement: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0)
  ietc: full_year_entitlement * qualifying_months / 12
expected:
  full_year_entitlement: 520
  ietc: 260
```

### IETC boundary: first-complete-dollar

Confirmed net income before brought-forward losses is $66,001, with 12 qualifying whole months. The lower-income eligibility branch is selected before abatement. The credit is $519.87. These are annual credits, not additional weekly payroll credits.

```oa-check
name: nz-2026-ir3-ietc-first-complete-dollar
tolerance: 0
inputs:
  net_income: 66001
  qualifying_months: 12
steps:
  full_year_entitlement: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0)
  ietc: full_year_entitlement * qualifying_months / 12
expected:
  full_year_entitlement: 519.87
  ietc: 519.87
```

### IETC boundary: last-positive

Confirmed net income before brought-forward losses is $69,999, with 12 qualifying whole months. The lower-income eligibility branch is selected before abatement. The credit is $0.13. These are annual credits, not additional weekly payroll credits.

```oa-check
name: nz-2026-ir3-ietc-last-positive
tolerance: 0
inputs:
  net_income: 69999
  qualifying_months: 12
steps:
  full_year_entitlement: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0)
  ietc: full_year_entitlement * qualifying_months / 12
expected:
  full_year_entitlement: 0.13
  ietc: 0.13
```

### IETC boundary: upper-zero

Confirmed net income before brought-forward losses is $70,000, with 12 qualifying whole months. The lower-income eligibility branch is selected before abatement. The credit is $0.00. These are annual credits, not additional weekly payroll credits.

```oa-check
name: nz-2026-ir3-ietc-upper-zero
tolerance: 0
inputs:
  net_income: 70000
  qualifying_months: 12
steps:
  full_year_entitlement: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0)
  ietc: full_year_entitlement * qualifying_months / 12
expected:
  full_year_entitlement: 0
  ietc: 0
```

### IETC boundary: no-qualifying-months

Confirmed net income before brought-forward losses is $60,000, with 0 qualifying whole months. The lower-income eligibility branch is selected before abatement. The credit is $0.00. These are annual credits, not additional weekly payroll credits.

```oa-check
name: nz-2026-ir3-ietc-no-qualifying-months
tolerance: 0
inputs:
  net_income: 60000
  qualifying_months: 0
steps:
  full_year_entitlement: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0)
  ietc: full_year_entitlement * qualifying_months / 12
expected:
  full_year_entitlement: 520
  ietc: 0
```

### Case 15: income above the top threshold and capped salary levy

For salary of $180,001, the recorded total PAYE is $40,000 and the annual ACC levy is the IR3G published maximum of $2,551.59. Income tax is $49,277.89. Separating the ACC component leaves $37,448.41 income-tax credit and $11,829.48 RIT. The supplied withholding is a synthetic underpayment, not a payroll-table prediction.

```oa-check
name: nz-2026-ir3-top-rate-capped-acc
tolerance: 0
inputs:
  taxable_income: 180001
  total_paye: 40000
  acc_levy: 2551.59
steps:
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  paye_tax_credit: total_paye - acc_levy
  rit: income_tax - paye_tax_credit
expected:
  income_tax: 49277.89
  paye_tax_credit: 37448.41
  rit: 11829.48
```

### Case 16: payroll giving and an extinguished credit

Salary is $60,000. Employer records show $10,000 PAYE before payroll donation tax credits and an extinguished donation credit of $100. Adjusted Box 11A is $9,900. After the $1,002 ACC levy, Box 11E is $8,898. With 12 qualifying IETC months, RIT is $802.50. No further payroll-giving credit is added.

```oa-check
name: nz-2026-ir3-payroll-giving-adjustment
tolerance: 0
inputs:
  salary: 60000
  paye_before_donation_credit: 10000
  extinguished_credit: 100
  acc_levy: 1002
  qualifying_months: 12
steps:
  net_income: salary
  taxable_income: net_income
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  ietc: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0) * qualifying_months / 12
  box_11a: paye_before_donation_credit - extinguished_credit
  paye_tax_credit: box_11a - acc_levy
  rit: max(income_tax - ietc, 0) - paye_tax_credit
expected:
  income_tax: 10220.5
  ietc: 520
  box_11a: 9900
  paye_tax_credit: 8898
  rit: 802.5
```

### Case 17: term deposit broken in full

Case 3 also has a documented $500 negative-interest repayment on a term deposit broken in full during 2025-26. The certificate gross interest is $2,000; the adjusted 13B interest entry is $1,500. RWT remains the evidenced $660. With the same salary, PAYE/ACC split and 12 IETC months, RIT is a credit of $917.50. A partial break does not receive this same timing treatment.

```oa-check
name: nz-2026-ir3-fully-broken-term-deposit
tolerance: 0
inputs:
  salary: 50000
  certificate_interest: 2000
  negative_interest_repaid: 500
  total_paye: 8493
  acc_levy: 835
  interest_rwt: 660
  qualifying_months: 12
steps:
  interest_entry: certificate_interest - negative_interest_repaid
  net_income: salary + interest_entry
  taxable_income: net_income
  income_tax: pct(min(taxable_income, 15600), 10.5) + pct(min(max(taxable_income - 15600, 0), 37900), 17.5) + pct(min(max(taxable_income - 53500, 0), 24600), 30) + pct(min(max(taxable_income - 78100, 0), 101900), 33) + pct(max(taxable_income - 180000, 0), 39)
  ietc: max(520 - pct(floor(max(net_income - 66000, 0)), 13), 0) * qualifying_months / 12
  paye_tax_credit: total_paye - acc_levy
  rit: max(income_tax - ietc, 0) - paye_tax_credit - interest_rwt
expected:
  interest_entry: 1500
  taxable_income: 51500
  income_tax: 7920.5
  ietc: 520
  paye_tax_credit: 7658
  rit: -917.5
```

## Working paper and reviewer checks

Retain a schedule with these separate rows: salary gross/total PAYE/ACC/Box 11E; schedular gross/expenses/net/withholding; other sole-trader net income; gross interest/RWT; gross dividends/imputation/RWT; total income; other expenses once; Box 30 net income; supported loss claim; Box 32 taxable income; tax; qualifying IETC months/credit; imputation used/carried; refundable credits; signed RIT; allocated provisional payments; terminal balance. Tie each row to its statement, return box or supported adjustment.

Before release, reconcile every income category to the annual records, exclude duplicate Summary of Income receipts, prove the withholding/ACC split, retain IETC eligibility dates and keep imputation/loss balances distinct. Resolve missing statements, unexplained account differences and separate assessment effects. This guide does not compute penalties, UOMI, student loans, WFF or ACC invoices.

## Primary sources and verification limits

Checked 13 November 2026. The source form/guide identity and selected worksheets were checked by native extraction and visual inspection; this is not a visual review of every IR3G page. The statute capture is the version as at 4 September 2026. The dated [verification entry](../../../docs/verification-log/2026-11-13-new-zealand-annual-ir3-provisional.md) records source discrepancies, amendment-check limits and regression evidence. Tier 2/pending status remains.

[S1]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3/ir3-2026.pdf?modified=20260728214111
[S2]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf?modified=20260821041603
[S3]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals
[S4]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1949201/
[S5]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519805/
[S6]: https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements
[S7]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/income-tax-assessments/refunds-and-tax-bills
[S8]: https://www.ird.govt.nz/managing-my-tax/make-a-payment/when-to-pay

[S9]: https://www.govt.nz/browse/work/public-holidays-and-work/public-holidays-and-anniversary-dates/
[S10]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1519723/#DLM1519757
[S11]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/#DLM1523192

## Prohibitions

Do not calculate an annual return from business profit alone when salary or investment income exists. Do not use total PAYE including ACC as income-tax credit, treat imputation as refundable, deduct provisional payments from RIT or infer eligibility from bank narrations. Do not use this year’s rates for a different year. Missing evidence stops the affected calculation.

## Disclaimer

General reference and conditional computation only. A qualified New Zealand practitioner must review the facts, applicable rules, source discrepancies and completed return before filing or acting. This source-cited draft has no recorded practitioner sign-off.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
