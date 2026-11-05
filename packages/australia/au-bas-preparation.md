---
name: au-bas-preparation
description: >
  Use this skill to prepare, review or check an Australian business activity statement (BAS) from
  end to end, for any entity type. It covers the preparation workflow: gathering records,
  reconciling the accounts to the ledger, confirming the reporting cycle and accounting basis,
  mapping amounts to BAS labels, separating PAYG withholding from PAYG instalments, handling
  adjustments and corrections, calculating the net amount, and lodging and paying. Trigger on
  phrases like "prepare BAS", "BAS preparation", "how do I do my BAS", "Business Activity
  Statements preparation Australia GST PAYG", "BAS checklist", "reconcile BAS", "BAS labels",
  "1A 1B W1 W2 T7 5A", "net amount on BAS", "fix a BAS", "BAS due date". For the GST
  classification rules behind the labels see australia-gst; for the label-level PAYG detail see
  au-gst-bas.
version: 0.8
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-05
review_status: pending_review
depends_on:
  - australia-gst
  - au-gst-bas
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia BAS Preparation v0.8

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### Australia BAS Preparation v0.8

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

### What this file is

**Obligation category:** CT (consumption tax), WHT (withholding tax), ET (estimated tax)
**Functional role:** Preparation workflow, spanning every role reported on one activity statement
**Status:** Source-cited draft, pending accountant review

This is the end-to-end preparation workflow. It sequences the work and tells you which guide owns
each rule. It does not restate the classification rules:

- GST classification of sales and purchases, the supplier pattern library and the refusal
  catalogue live in `australia-gst.md`.
- Label-level PAYG withholding, PAYG instalment and FBT instalment mechanics live in
  `au-gst-bas.md`.
- Property transactions, including the margin scheme and GST at settlement, live in
  `au-gst-property.md`.
- Lodgment dates, penalties, interest and remission live in `au-lodgment-deadlines-penalties.md`.

### Section 1 - Scope statement

This skill covers:

- The preparation sequence for a business activity statement, from source records to lodgment.
- Reconciling the GST and PAYG withholding control accounts to the ledger before any label is
  filled in.
- Choosing between Simpler BAS and full reporting, and between cash and non-cash (accruals)
  accounting for GST.
- Mapping ledger balances to the GST labels (G1, 1A, 1B), the PAYG withholding labels
  (W1 to W5, label 4), the PAYG instalment labels (T1 to T9, 5A, 5B) and the summary
  (8A, 8B, 9).
- Distinguishing PAYG withholding from PAYG instalments, which are different obligations that
  share one form.
- Adjustments, corrections of earlier errors, and when a revision is required instead.
- The lodgment and payment step, including the electronic lodgment concession.

This skill does NOT cover:

- Whether a particular supply is taxable, GST-free or input taxed. See `australia-gst.md`.
- Registration, cancellation or turnover tests. See `australia-gst.md`.
- Payroll calculation, award interpretation, superannuation guarantee or Single Touch Payroll
  reporting. See `australia-payroll.md` and `au-super-guarantee.md`.
- Fuel tax credits, wine equalisation tax and luxury car tax computation. Those labels appear on
  the BAS but their rules are outside this file.
- Income tax return preparation. PAYG instalments are prepayments only, and the return is where
  they are reconciled.

## Ask the client first

### Section 2 - Establish the facts before you calculate

**Facts to establish before calculating**

| Fact to establish | Why it changes the answer |
| --- | --- |
| Entity and ABN | Determines who lodges and which roles are registered |
| GST registration status and date of effect | An unregistered period has no GST labels at all |
| Reporting cycle: monthly, quarterly, annual or quarterly GST instalments | Sets the period, the due date and the GST labels used |
| Simpler BAS or full reporting | Simpler BAS reports only G1, 1A and 1B for GST |
| Accounting basis: cash or non-cash (accruals) | Sets the period an amount is attributed to |
| Whether G1 is reported GST-inclusive or GST-exclusive | The BAS requires the choice to be indicated |
| PAYG withholding registration and withholder class (small, medium or large) | Determines the W labels and the reporting and payment cycle |
| PAYG instalment role, and option 1 or option 2 | Determines whether T7 or T1 and T2 are used |
| FBT instalment role | Determines whether F1 applies |
| Any prior period error not yet corrected | Determines whether a correction or a revision is needed |

- **GST reporting cycle** — Quarterly applies where GST turnover is less than $20 million and the ATO has not directed monthly reporting. Monthly is compulsory at $20 million or more, and is available by choice below that. Annual reporting is available only to an entity that is voluntarily registered, that is, turnover under $75,000, or under $150,000 for a not-for-profit body.  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas))_
- **GST instalments** — A quarterly GST instalment payer reports at 1A the instalment pre-filled at G21, or the varied amount at G23. It does not complete 1B on the quarterly statement, and it lodges an annual GST return.  _([ATO, Complete your BAS: Step 5 summary](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/complete-your-bas/step-5-summary))_
- **PAYG withholding cycle** — Set by withholder class, not GST turnover. Large: more than $1 million withheld in a financial year ending at least 2 months before the month; pay electronically on the weekday schedule in s 16-75(1). Medium: more than $25,000 withheld in a financial year ending before the month; report and pay monthly. Otherwise small: report and pay quarterly. The tests are not limited to the latest year, and a Commissioner determination can override them. One quarter's withholding does not decide the class; see `au-gst-bas.md` Section 2.2.  _([ATO, Changing a withholding cycle](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/changing-a-withholding-cycle); TAA 1953 Sch 1 ss 16-75, 16-95 to 16-105)_
- **Accounting basis** — On a cash basis, an amount is attributed to the period in which payment was received or made, and may be part of the sale price. On a non-cash (accruals) basis, an amount is attributed to the earlier of the period in which any payment is received or made and the period in which an invoice is issued or received.  _([ATO, Identify your accounting basis; GST Act ss 29-5, 29-10](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/identify-your-accounting-basis))_

**Do not assume the basis from the accounting file.** A file set to accrual reporting for management accounts can still be registered to report GST on a cash basis, and the reverse is common after a change of adviser. Confirm the registered basis, not the software setting.

## The method, step by step

### Section 3 - Step 1: Gather the records

Collect, for the exact period being reported:

1. The trial balance and general ledger for the period, after the period is closed to new entries.
2. Bank statements for every business account, including credit cards and loan accounts, covering
   the full period.
3. Sales records: invoices issued, point-of-sale summaries, platform settlement reports.
4. Purchase records: tax invoices for acquisitions where a credit will be claimed.
5. Payroll records for the period: the payroll register and the Single Touch Payroll year-to-date
   figures at the period end.
6. Any ATO correspondence for the period, including the pre-filled instalment amount or rate.
7. Any adjustment notes issued or received, and any credit notes.
8. Records of assets bought or sold, including trade-ins.

- **Evidence rule for credits** — A GST credit generally requires a valid tax invoice held at the time the claim is made. The exception applies to acquisitions of $82.50 including GST or less. The four-year credit time limit is not permission to claim before the required evidence exists.  _([GST Act ss 11-5, 29-10, 29-70, 93-5](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-10))_

### Section 4 - Step 2: Reconcile before you report

Reconciliation is what turns the ledger into evidence. The ATO reports that incorrect timing, miscalculation and transcription errors, unsubstantiated credit claims, credits on private-use purchases and missed registration thresholds together make up more than half of all GST corrections, and a reconciliation catches most of them. Complete all five before filling in a label.

1. **Bank reconciliation.** Every business account reconciled to the statement closing balance at the period end, with the unpresented items listed.
2. **GST control accounts.** The GST collected and GST paid control account balances at the period end must agree with the GST calculated from the transaction listing for the period. An unexplained difference is an error, not a rounding item.
3. **PAYG withholding liability account.** The balance must agree with amounts withheld per the payroll register for the period, less amounts already remitted.
4. **Sales reconciliation.** Total sales per the profit and loss for the period must agree with G1, after allowing for the reporting basis and for items excluded from G1.
5. **Balance sheet sanity check.** Clearing and suspense accounts must be zero or fully explained. A transaction sitting in suspense has no GST classification, so it cannot have been reported correctly.

**Common source of a false reconciliation.** Transactions processed outside accounts payable or accounts receivable, such as a direct bank entry or a journal, are often classified incorrectly and never reach the GST control accounts. Review journals posted to revenue, expense and asset accounts for the period before signing off the reconciliation.

### Section 5 - Step 3: Map GST amounts to labels

Classify every transaction first, using `australia-gst.md`. Then map.

#### 5.1 Simpler BAS

**Simpler BAS GST labels**  _([ATO, Simpler BAS GST bookkeeping guide](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/simpler-bas-gst-bookkeeping-guide))_

| Label | What goes in it |
| --- | --- |
| G1 | Total sales for the period. Indicate whether the figure includes or excludes GST |
| 1A | Total GST payable on sales for the period, including GST adjustments |
| 1B | Total GST credits on purchases for the period, including credit adjustments |

#### 5.2 Full reporting

- **Full reporting methods** — Full reporting adds the G labels. Two methods are available and both are acceptable: - **Accounts method.** Take 1A and 1B directly from the GST control accounts, which requires GST to be separately recorded for supplies and acquisitions. - **Calculation worksheet method.** Complete the ATO GST calculation worksheet and transfer G9 to 1A and G20 to 1B. The worksheet is not lodged.  _([ATO, Complete your BAS: Step 5 summary](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/complete-your-bas/step-5-summary))_

#### 5.3 What is excluded from the GST labels entirely

- **Items excluded from GST labels** — Wages and salaries, superannuation contributions, drawings and owner contributions, loan principal, dividends, internal transfers between the entity's own accounts, and stamp duty. These have no GST classification. Reporting them as purchases at G11 is a recurring error.

### Section 6 - Step 4: PAYG withholding is not PAYG instalments

**PAYG withholding vs PAYG instalments**

| Feature | PAYG withholding | PAYG instalments |
| --- | --- | --- |
| Whose tax is it | The payee's (employee, contractor without an ABN, some investors) | The entity's own income tax |
| What triggers it | Making a payment from which the law requires withholding | The ATO entering the entity into the instalment system |
| Labels | W1, W2, W3, W4, W5, then label 4 | T1 to T9, then 5A or 5B |
| Effect on the entity | The entity holds and remits someone else's money | A prepayment of the entity's own tax |
| Where it is reconciled | The payee's tax return, and the entity's STP finalisation | The entity's own income tax return |
| Consequence of underpaying | Withheld amounts not remitted can attract director penalties | A shortfall is payable on assessment, with possible interest |

#### 6.1 PAYG withholding labels

**PAYG withholding labels**

| Label | Content |
| --- | --- |
| W1 | Gross salary, wages and other payments subject to withholding, including payments with no amount withheld; exclusions below |
| W2 | Amounts withheld from the payments shown at W1 |
| W3 | Other amounts withheld that do not belong at W2 or W4 |
| W4 | Amounts withheld from invoices where no ABN was quoted |
| W5 | Total amounts withheld, being W2 plus W3 plus W4 |
| 4 | The W5 total, transferred to the summary |

- **W1 gross payments detail** — W1 is a gross payments figure. Exclude salary sacrifice amounts, superannuation contributions and payments whose withholding belongs at W3 or W4. Include wages below the withholding threshold even when no tax was withheld.
- **W3 inclusions** — W3 includes withholding from investment distributions where no TFN was quoted, interest, dividends and royalties paid to foreign residents, departing Australia superannuation payments, and payments to foreign residents for entertainment, sports, construction and casino gaming junket activities.
- **Large withholders** — complete only W1, and omit W1 as well if reporting through Single Touch Payroll (STP). Leave W2, W3, W4, W5 and label 4 blank; remit withheld amounts electronically. For other withholders, reconcile W1 and W2 to the payroll register and relevant STP figures for the period, and investigate any difference before lodging.  _([ATO, PAYG withholding: activity statement labels and large withholders](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding))_

#### 6.2 PAYG instalment labels

**PAYG instalment options**  _([ATO, PAYG instalments: how to complete your activity statement](https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement))_

| Option | Labels used | How it works |
| --- | --- | --- |
| Option 1, instalment amount | T7; T8, T9, T4 and eligible 5B if varying | If unchanged, copy T7 to 5A. If varying, use T9 at 5A, subject to the zero-floor and credit rules below |
| Option 2, instalment rate | T1, T2, T11; T3, T4 and eligible 5B if varying | Multiply T1 by T2, or varied T3. Report the result at T11 and 5A. Check any separate credit entitlement at 5B |

- **Negative instalment-amount variation:** If the option 1 calculation is nil or negative, enter zero at T9 and 5A. A negative calculation may support a credit for earlier PAYG instalments in the same income year; claim the eligible amount as a positive number at 5B. Do not enter the negative calculation at T9 or add both it and the 5B credit to the summary. A credit need not be claimed on the activity statement. ([ATO, How to vary your PAYG instalments, amount method steps 4-5](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments).)
- **Varying carries a risk:** For rate-method GIC, compare the varied rate with 85% of the benchmark rate. For amount-method GIC, compare the annual benchmark-tax estimate used with 85% of benchmark tax. For a four-instalment payer, count cumulative amount variations from the first liable instalment and include applicable earlier credit entitlements. A final payment total does not clear every earlier estimate, and later top-ups reduce an amount-method shortfall from their due date. Work out the statutory amount and period separately; penalties may also apply. See [the PAYG guide](au-payg-instalments.md), [ATO variation instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments) and [TAA Sch 1 ss 45-230, 45-232, 45-233 and 45-410](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).
- **Instalment notices** — **Instalment notices.** Where the entity receives an instalment notice rather than an activity statement, and does not wish to vary, the amount can simply be paid. No lodgment is required.

### Section 7 - Step 5: Adjustments and corrections

These are three different things. Treat them separately.

#### 7.1 Adjustments

- **Adjustments** — An adjustment arises because circumstances changed after the original reporting, not because the original reporting was wrong. Examples: a price change, a cancelled supply, a bad debt written off, a change in the extent of creditable purpose, goods applied to private use. Adjustments belong in the period in which the adjustment event is accounted for, and they flow into 1A or 1B. An adjustment note is generally required before a decreasing adjustment on a supply is claimed.  _([GST Act Div 19, Div 21, Div 129](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/19-10))_

#### 7.2 Correcting an earlier GST error on a later BAS

**Correcting an earlier GST error on a later BAS**  _([ATO, Types of GST errors; LI 2023/32, Correcting GST Errors Determination 2023](https://www.legislation.gov.au/F2023L01284/latest))_

| Condition | Credit error (too much GST reported) | Debit error (too little GST reported) |
| --- | --- | --- |
| Time limit | Correct on a later BAS lodged within the period of review for the earlier period, being 4 years and one day from the day the earlier BAS was lodged | Turnover under $20 million: within 18 months of the due date of the BAS containing the error. Turnover $20 million or more: within 12 months |
| Value limit | None | Under $20m: less than $12,500. $20m to under $100m: less than $25,000. $100m to under $500m: less than $50,000. $500m to under $1b: less than $100,000. $1b and over: less than $560,000 |
| Other conditions | Cannot claim additional GST credits after the four-year credit time limit has ended | Must not result from recklessness or intentional disregard of a GST law |

- **Common conditions:** Section 6 of the determination requires the earlier tax period to start on or after 1 July 2012 and the later return to be lodged within the earlier assessment's period of review. The error must not already have been corrected to any extent in another tax period. The compliance exclusion covers an error relating to a matter under notified compliance activity or made in a period under that activity, unless the Commissioner has given written permission to correct it under the instrument. These conditions apply to credit and debit errors; debit errors also need every section 7 condition. ([Determination 2023, sections 4 and 6-8](https://www.legislation.gov.au/F2023L01284/latest).)
- **Net sum and unresolved value-limit boundary:** The value limit applies to debit errors less credit errors included on the same BAS. Section 7(c) requires that net sum to be **less than** the limit. The ATO table agrees, but its partial-correction wording says 'up to' the limit and its Greg's Garage and Serge's Auto examples permit exactly $12,500. This source conflict remains unresolved. Return **Needs Input** for an exact-limit or partial-at-limit correction and obtain qualified review or ATO clarification; do not automatically accept equality or choose a partial amount from this guide. Revising the original period, where permitted, remains an alternative. The ATO also says excess amounts cannot be rolled into another later BAS. ([Determination 2023, section 7(c)](https://www.legislation.gov.au/F2023L01284/latest); [ATO, Types of GST errors](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/correcting-gst-errors/types-of-gst-errors), updated 14 September 2026, read 2 November 2026.)

#### 7.3 Revising an earlier BAS

- **Revising an earlier BAS** — Where the correction rules do not permit a later-BAS correction, revise the earlier activity statement. The ATO treats a revised BAS as an application to amend an assessment. If the revision increases tax or reduces a credit, it is generally treated as a voluntary disclosure, which usually attracts concessional treatment of penalties and interest.  _([ATO, Revising an earlier business activity statement](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/fix-a-mistake-or-amend-your-tax-return/correct-an-activity-statement/revising-an-earlier-activity-statement))_

### Section 8 - Step 6: Calculate the result

- **BAS summary calculation** — ``` 8A  Total amounts you owe the ATO   = 1A + 4 + 5A + 6A + 7 (+ other liability labels) 8B  Total the ATO owes you          = 1B + 5B + 6B (+ other credit labels) 9   Net amount                      = 8A - 8B ``` If 9 is positive it is payable. If negative it is refundable, subject to offsetting against other ATO debts.
- **Nil BAS still required** — A registered entity must give a GST return for each tax period, even where the net amount is nil and no GST was payable on any supply. Quarterly instalment Forms R, S and T differ: they generally need only be lodged when varying the instalment amount.  _([GST Act s 31-5](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/31-5); [ATO, activity statements and nil lodgments](https://www.ato.gov.au/api/public/content/0-0b929c4e-ddac-4b4f-a627-7427575b94a2))_

## Boundary and exception table

### Section 11 - Common errors

Drawn from the ATO's published analysis of GST corrections and from recurring practice issues.

**Classification errors**

- Claiming GST credits on GST-free purchases such as basic food, most exports and some health services, and on bank fees, stamp duty and third party insurance levies.
- Claiming a credit on a purchase for private use, or failing to apportion a mixed-use purchase.
- Treating a government fee or charge as a taxable purchase.
- Claiming a full credit on a car costing more than the car limit, where the credit is capped. Confirm the car limit for the relevant income year on ato.gov.au before claiming.

**Timing errors**

- Reporting in the wrong period for the registered accounting basis.
- Claiming the whole credit on a lease or hire agreement in the period the goods are delivered rather than as payments become due.
- Claiming a credit on a real estate purchase at contract date rather than at settlement.

**Evidence errors**

- Claiming a credit with no valid tax invoice held, where the $82.50 exception does not apply.
- Tax invoices made out to the wrong entity, which is common in group structures.

**Process errors**

- Transactions processed outside accounts payable or accounts receivable and never captured in the GST control accounts.
- Incorrect default GST codes in the accounting file after a chart of accounts change.
- Not reconciling the GST control accounts to the BAS at all.
- Failing to recognise an adjustment event, such as a settlement discount taken by a customer.

**Threshold and registration errors**

- Not noticing that GST turnover has met the $75,000 registration threshold: current turnover at or above it, unless the Commissioner is satisfied projected turnover is below it, or projected turnover at or above it (GST Act ss 23-5, 188-10(1)). The application is due within 21 days after becoming required to be registered (s 25-1).
- Changing from monthly to quarterly reporting in the first 12 months of operation without ATO approval.

**PAYG errors**

- Reporting superannuation contributions at W1.
- Entering the instalment rate at 5A instead of the calculated instalment.
- Varying an instalment down without support, then falling under the 85% threshold.

[ATO, GST](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst); [ATO, Types of GST errors](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/correcting-gst-errors/types-of-gst-errors)

## Worked cases

### Section 10 - Worked example

**Facts.** Coastline Joinery Pty Ltd is a quarterly GST lodger. Its issued statement uses Simpler BAS; eligibility for that method is stipulated rather than inferred from a turnover figure without a measurement period. It accounts for GST on a non-cash (accruals) basis and reports G1 including GST. It has two part-time employees and is registered for PAYG withholding as a small withholder: it has not withheld more than $25,000 in any earlier financial year, and no Commissioner determination applies. One quarter does not itself set the class (see `au-gst-bas.md` Section 2.2). It pays PAYG instalments using option 1. The period is the quarter ended 30 September 2026. All figures are synthetic.

The export independently satisfies the GST-free export conditions. All listed taxable sales and wholly creditable acquisitions are attributable to this quarter, with valid tax invoices held when required and no special valuation, private-use or credit-limit rules. The bad debt relates to an earlier taxable sale whose GST was already attributed; the unpaid debt is written off in this quarter and qualifies for the $500 decreasing adjustment. The supplier credit note relates to an earlier fully credited acquisition; the $100 increasing adjustment is attributable this quarter. The $1,200 bank fee carries no GST. These classifications and adjustment entitlements are stipulated, not determined by the arithmetic. No FBT, other tax-role liabilities or credits, or ATO account offsets apply.

**Transactions for the quarter**

| Item | Amount | GST treatment |
| --- | --- | --- |
| Taxable sales, including GST | $451,000 | Taxable, 1/11 is GST |
| Export of a custom joinery unit | $22,000 | GST-free, in G1, no GST |
| CNC router purchased and installed | $88,000 incl GST | Creditable acquisition |
| Other taxable purchases and expenses | $209,000 incl GST | Creditable acquisitions |
| Salaries and wages paid | $36,000 | No GST, excluded from GST labels |
| Bank account fees | $1,200 | Input taxed supply to the entity, no credit |
| Customer debt written off as bad | $5,500 incl GST | Decreasing adjustment |
| Supplier credit note received for returned goods | $1,100 incl GST | Increasing adjustment, reduces credits |
| Amounts withheld from wages | $5,400 | PAYG withholding |
| ATO instalment amount at T7 | $6,200 | PAYG instalment |

**Step 1, GST on sales.**

```
GST on taxable sales          451,000 / 11    =  41,000
Less decreasing adjustment (bad debt)
                                5,500 / 11    =    (500)
1A GST on sales                               =  40,500
```

**Step 2, GST credits.**

```
Capital acquisition            88,000 / 11    =   8,000
Other acquisitions            209,000 / 11    =  19,000
Less increasing adjustment (credit note)
                                1,100 / 11    =    (100)
1B GST on purchases                           =  26,900
```

**Step 3, G1 total sales.**

```
Taxable sales including GST                   = 451,000
GST-free export                               =  22,000
G1 Total sales (GST-inclusive basis indicated)= 473,000
```

**Step 4, PAYG withholding.** The example shows W1 because the issued statement asks for it.

```
W1 Total salary, wages and other payments     =  36,000
W2 Amounts withheld from W1                   =   5,400
W3 and W4                                     =       0
W5 Total amounts withheld                     =   5,400
4  PAYG tax withheld                          =   5,400
```

**Step 5, PAYG instalment.**

```
T7 ATO instalment amount                      =   6,200
5A PAYG income tax instalment                 =   6,200
```

**Step 6, summary.**

```
8A = 1A 40,500 + 4 5,400 + 5A 6,200           =  52,100
8B = 1B 26,900                                =  26,900
9  = 8A - 8B                                  =  25,200 payable
```

**Step 7, lodgment.** The quarter ended 30 September 2026, so the standard due date is 28 October 2026. If the company lodges online it may be entitled to an extra two weeks, and its registered agent may have a different lodgment program date. The $25,200 must be paid by the applicable due date, whether or not the statement is lodged on time.

**What the example shows.** Net GST of $13,600 is just over half of the amount payable. The company must fund $5,400 of employees' withheld tax and $6,200 of its own income tax prepayment out of the same quarter's cash. A business that budgets for net GST alone will be short on the due date.

### Case 1 arithmetic: Coastline label reconciliation

The executable case below recomputes the retained illustration using its stated classifications and adjustments. It does not establish export status, credit entitlement or adjustment timing. The standard taxable-price arithmetic uses GST Act sections 9-70 and 9-75; credit amounts use sections 11-20 and 11-25.

```oa-check
name: AU Coastline BAS reconciles GST and income tax prepayments
inputs:
  taxable_sales_including_gst: 451000
  gst_free_export: 22000
  capital_purchase_including_gst: 88000
  other_purchases_including_gst: 209000
  bad_debt_including_gst: 5500
  supplier_credit_including_gst: 1100
  paygw_4: 5400
  paygi_5a: 6200
steps:
  - sales_gst: taxable_sales_including_gst / 11
  - bad_debt_adjustment: bad_debt_including_gst / 11
  - gst_1a: sales_gst - bad_debt_adjustment
  - capital_credit: capital_purchase_including_gst / 11
  - other_credit: other_purchases_including_gst / 11
  - supplier_adjustment: supplier_credit_including_gst / 11
  - gst_1b: capital_credit + other_credit - supplier_adjustment
  - total_sales_g1: taxable_sales_including_gst + gst_free_export
  - net_gst: gst_1a - gst_1b
  - total_8a: gst_1a + paygw_4 + paygi_5a
  - total_8b: gst_1b
  - net_9: total_8a - total_8b
expected:
  sales_gst: 41000
  bad_debt_adjustment: 500
  gst_1a: 40500
  capital_credit: 8000
  other_credit: 19000
  supplier_adjustment: 100
  gst_1b: 26900
  total_sales_g1: 473000
  net_gst: 13600
  total_8a: 52100
  total_8b: 26900
  net_9: 25200
```

### Case 2: a GST credit can still leave a BAS payable

For a synthetic 2026-27 period, independently reconciled labels are 1A $1,000, 1B $4,000, 4 $2,500 and 5A $2,000. No variations, other tax roles or account offsets apply. Net GST is a $3,000 credit, but the full BAS is $1,500 payable. Do not describe the GST component as the total refund.

```oa-check
name: AU GST credit does not determine whole BAS result
inputs:
  gst_1a: 1000
  gst_1b: 4000
  paygw_4: 2500
  paygi_5a: 2000
steps:
  - net_gst: gst_1a - gst_1b
  - total_8a: gst_1a + paygw_4 + paygi_5a
  - total_8b: gst_1b
  - net_9: total_8a - total_8b
expected:
  net_gst: -3000
  total_8a: 5500
  total_8b: 4000
  net_9: 1500
```

### Case 3: the GST error limit is a net amount with an unresolved equality boundary

Current GST turnover is below $20 million. All section 6 conditions, the debit-error time limit and the absence of recklessness or intentional disregard are stipulated. Debit errors total $14,000. If eligible credit errors included on the same BAS total $1,501, the net debit errors are $12,499, $1 below the statutory cap. If those credits are $1,500, the net is exactly $12,500: return Needs Input under section 7.2 because the statutory wording and ATO partial-correction examples conflict. Do not infer that an error can be split across later returns. This arithmetic checks the net amounts and distance from the cap; it does not execute legal eligibility or resolve the source conflict.

```oa-check
name: AU GST debit error net amounts at value boundary
inputs:
  debit_errors: 14000
  credits_below: 1501
  credits_at: 1500
  value_limit: 12500
steps:
  - net_below: debit_errors - credits_below
  - headroom_below: value_limit - net_below
  - net_at: debit_errors - credits_at
  - headroom_at: value_limit - net_at
expected:
  net_below: 12499
  headroom_below: 1
  net_at: 12500
  headroom_at: 0
```

Recompute with `python3 scripts/check-examples.py --require skills/international/australia/au-bas-preparation.md`. The checker verifies the displayed arithmetic, not the stipulated classifications, source accuracy or the rest of this guide.

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


### Section 14 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional in the relevant jurisdiction before lodging or acting upon them.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).

> Contributed by Ryan Duguid.



## Filing and payment

### Section 9 - Step 7: Lodge and pay

**Due dates by cycle**  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas))_

| Cycle | Due date | Notes |
| --- | --- | --- |
| Monthly | 21st day of the month after the period ends | No electronic lodgment concession |
| Quarter 1, July to September | 28 October | Online lodgment may allow an extra 2 weeks |
| Quarter 2, October to December | 28 February | No further extension, the date already includes one month |
| Quarter 3, January to March | 28 April | Online lodgment may allow an extra 2 weeks |
| Quarter 4, April to June | 28 July | Online lodgment may allow an extra 2 weeks |

- **Weekend/holiday and agent program** — A due date falling on a weekend or public holiday moves to the next business day. A registered tax or BAS agent may have a different lodgment program date, which is a concession attached to the agent's client list and is not an automatic right of the taxpayer.  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas))_
- **Electronic lodgment threshold** — Entities with GST turnover of $20 million or more must lodge electronically.  _([GST Act s 31-25](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/31-25))_

**Lodgment and payment are separate obligations.** Lodging on time does not stop general interest charge accruing on an unpaid amount. If the amount cannot be paid, lodge anyway and contact the ATO about a payment arrangement before the due date. See `au-lodgment-deadlines-penalties.md`.

## Completion checklist

### Section 12 - Self-checks

Before lodging, confirm:

- [ ] The period, the entity and the ABN on the statement match the records used.
- [ ] Every business bank account is reconciled to the period end.
- [ ] The GST control account balances agree with the transaction listing for the period.
- [ ] G1 agrees with total sales per the profit and loss, after basis and exclusion differences.
- [ ] The G1 GST-inclusive or GST-exclusive choice is indicated and matches the figure entered.
- [ ] 1A and 1B include every adjustment for the period and no corrections that are out of time.
- [ ] Where W1 and W2 reporting is required, the amounts reconcile to the payroll register and relevant STP figures for the period.
- [ ] Where these labels apply, W5 equals W2 plus W3 plus W4, and label 4 equals W5. Large withholders follow Section 6.1 instead.
- [ ] 5A comes from T7 for an unchanged amount, T9 for an amount variation, or T11 calculated as T1 x T2 for the pre-filled rate or T1 x T3 for a current rate variation.
- [ ] 8A less 8B equals label 9, recalculated independently.
- [ ] Any correction of a prior period error is within its time and value limits.
- [ ] Suspense and clearing accounts are nil or fully explained.
- [ ] The due date has been identified, including any electronic or agent concession.

## Sources

| Source | URL | Read on |
|---|---|---|
| TAA 1953 compilation 227, selected Sch 1 ss 45-230, 45-232, 45-233 and 45-410: method-specific GIC and liable-instalment sequence | <https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html> | 2026-11-02; effective 1 October, registered 19 October 2026; selected PAYG provisions only |
| GST Act, compilation 96 effective 1 January 2026 | <https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-02; selected sections 9-70, 9-75(1) including formula alternative text, 11-20, 11-25, 21-5 and 29-5/29-10; other sections not newly audited |
| ATO BAS due dates, updated 17 September 2026 | <https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas> | 2026-11-02; monthly direction, quarterly dates and extensions |
| ATO GST summary, updated 9 September 2026 | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/complete-your-bas/step-5-summary> | 2026-11-02; 1A/1B and quarterly-instalment exception |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/changing-a-withholding-cycle> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/identify-your-accounting-basis> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-10> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/simpler-bas-gst-bookkeeping-guide> | Not re-read for this format update; see retained provenance |
| ATO PAYG withholding, updated 1 May 2025 | <https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding> | 2026-11-02; W5 to 4 and large-withholder exception |
| ATO PAYG activity statement, updated 9 January 2023 | <https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement> | 2026-11-02; option 1 labels and option 2 T1/T2/T3/T11/5A |
| ATO PAYG variations, updated 23 June 2026 | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments> | 2026-11-02; amount-method steps 3-5, zero T9/5A and positive 5B |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/19-10> | Not re-read for this format update; see retained provenance |
| GST error Determination 2023, in force | <https://www.legislation.gov.au/F2023L01284/latest> | 2026-11-02; sections 4 and 6-8; strict section 7(c) conflicts with ATO partial-correction examples |
| ATO Types of GST errors, updated 14 September 2026 | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/correcting-gst-errors/types-of-gst-errors> | 2026-11-02; time limits, net sum, value table and partial-correction examples |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/fix-a-mistake-or-amend-your-tax-return/correct-an-activity-statement/revising-an-earlier-activity-statement> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/31-5> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/api/public/content/0-0b929c4e-ddac-4b4f-a627-7427575b94a2> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/31-25> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst> | Not re-read for this format update; see retained provenance |

### Section 13 - Sources

- A New Tax System (Goods and Services Tax) Act 1999, especially ss 11-5, 29-5, 29-10, 29-70, 31-5, 31-25, 93-5, and Divisions 19, 21 and 129.
- Taxation Administration Act 1953, Schedule 1, Parts 2-5 (PAYG withholding) and 2-10 (PAYG instalments).
- LI 2023/32, A New Tax System (Goods and Services Tax) (Correcting GST Errors) Determination 2023, https://www.legislation.gov.au/F2023L01284/latest
- ATO, Due dates for lodging and paying your BAS, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas
- ATO, Identify your accounting basis, https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/identify-your-accounting-basis
- ATO, Simpler BAS GST bookkeeping guide, https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/simpler-bas-gst-bookkeeping-guide
- ATO, Types of GST errors, https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/correcting-gst-errors/types-of-gst-errors
- ATO, PAYG instalments: how to complete your activity statement, https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement
- ATO, How to vary your PAYG instalments, https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments
- ATO, Changing a withholding cycle, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/changing-a-withholding-cycle
- ATO, Complete your BAS: Step 5 summary, https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/complete-your-bas/step-5-summary

Sources were checked on 16 September 2026; the GST error time and value limits were rechecked against the ATO page (updated 14 September 2026) on 11 October 2026; withholder classes, GST instalments and the instalment-form lodgment rule were checked on 31 October 2026. Rates, thresholds and administrative processes change; confirm each figure against the cited page for the period being reported.

Not yet confirmed: The 3 executable cases check selected BAS arithmetic only. The exact GST debit-error cap and partial-at-cap source conflict in section 7.2 remains unresolved and must be referred. Coastline's classifications, GST-free export, credit entitlement and adjustment timing are stipulated, not established by the checker. A complete source/read-date audit, other retained claims and illustrations, and independent legal review remain outstanding.

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
