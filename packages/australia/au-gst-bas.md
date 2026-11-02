---
name: au-gst-bas
description: >
  Use this guide for the non-GST sections of an Australian Business Activity
  Statement. It covers PAYG withholding labels W1-W5, PAYG income tax instalment
  labels T1-T9, FBT instalment label F1 and PAYG withholding reconciliation. Read
  it with australia-gst for the GST labels and with the relevant workflow base
  for the complete reviewer package. Trigger on BAS withholding, instalments,
  reconciliation or preparation questions. Establish the selected period,
  reported amounts and source conditions before applying the instructions.
  Preserve exceptions and self-checks, and refer unresolved classifications or
  filing procedures for professional review.
version: 1.8
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-02
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU GST Bas v1.8

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### What this file is

**Obligation category:** CT (Consumption Tax) / ET (Estimated Tax) / WHT (Withholding Tax)
**Functional role:** Return — complementary to `australia-gst.md`
**Status:** Source-cited draft — pending accountant review

This file covers the non-GST sections of the Business Activity Statement. For GST labels (1A through 9), see `australia-gst.md` in this directory.

**Tax year coverage.** This skill targets the **2026-27 income year** (1 July 2026 to 30 June 2027). Figures still needed for 2025-26 statements are labelled with their year.

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

### Section 1 — Scope statement

This skill covers:

- **PAYG withholding labels** (W1 through W5) — amounts withheld from payments to employees and contractors
- **PAYG income tax instalment labels** (T1 through T11, 5A and 5B): quarterly pre-payments of income tax
- **FBT instalment label** (F1) — fringe benefits tax quarterly instalments
- **Fuel tax credits** (7C, 7D) — overview only
- **BAS lodgement and payment deadlines**
- **Entity types:** Sole proprietors and individual taxpayers who lodge BAS

This skill does NOT cover:

- GST labels (1A through 9) — see `australia-gst.md`
- Partnerships, companies, trusts, or superannuation funds
- Wine equalisation tax (WET) or luxury car tax (LCT)
- Detailed fuel tax credit calculations

## Ask the client first

- What taxpayer or entity, jurisdiction and reporting capacity are in scope?
- Which income year or transaction period applies?
- What records support the amounts, dates and classifications?
- Which residence, election, exception or eligibility conditions in this guide affect the answer?
- What facts or source conditions remain unresolved?

## The method, step by step

### Australia BAS: Non-GST Sections v1.8

### Section 3 — Rates and thresholds

#### 3.1 PAYG withholding

**PAYG withholding rates and rules**  _(TAA 1953 Sch 1 Div 12)_

| Item | Detail | Source |
| --- | --- | --- |
| Withholding obligation trigger | Making payments to employees, directors, or contractors who do not quote an ABN | TAA 1953 Sch 1 Div 12 |
| No-ABN withholding rate | 47% of the payment amount | TAA 1953 Sch 1 s 12-190 |
| Voluntary agreement rate | As per the ATO tax tables or agreed rate | TAA 1953 Sch 1 s 12-55 |
| Labour hire withholding | As per ATO tax tables | TAA 1953 Sch 1 s 12-60 |

#### 3.2 PAYG income tax instalments

**PAYG income tax instalment rates and thresholds**  _(TAA 1953 Sch 1 s 45-5)_

| Item | Amount / Rate | Source |
| --- | --- | --- |
| Automatic entry — individuals (including sole traders) | The ATO uses the latest tax return. Automatic entry requires all of: instalment income of $4,000 or more; tax payable on the latest notice of assessment of $1,000 or more; and estimated (notional) tax of $500 or more. | [ATO — Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments) |
| Instalment rate | As notified by the ATO (varies per taxpayer) | ATO instalment rate notice |
| GDP-adjusted amount | GDP adjustment is part of the notified instalment-amount calculation, not an automatic increase in T2 | [ATO PAYG variation instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments) |
| GDP uplift factor | 5% for 2026-27; 4% for 2025-26, and for a substituted accounting period whose income year started on 1 January, 1 February or 1 March 2026; 6% for 2024-25 | [ATO — GDP adjustment for 2025-26 GST and PAYG instalments](https://softwaredevelopers.ato.gov.au/gdp-adjustment-2025-26-gst-and-payg-instalments); [2026-27](https://softwaredevelopers.ato.gov.au/GDPupliftfactor) |
| Voluntary entry | A person new to business, or expecting business and investment income over the threshold, can request voluntary entry to PAYG instalments. | [ATO — Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments) |

#### 3.3 FBT instalments

**FBT instalment rates and thresholds**  _(FBTAA 1986 Pt VII Div 2)_

| Item | Amount / Rate | Source |
| --- | --- | --- |
| FBT instalment threshold | Notional FBT amount >= $3,000 in prior FBT year | FBTAA 1986 s 111(2), (3); [ATO, FBT instalment](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/fringe-benefits-tax-fbt-instalment) |
| FBT year | 1 April to 31 March | FBTAA 1986 s 136(1) ('year of tax') |
| Instalment rate | 25% of prior year FBT liability each quarter | FBTAA 1986 ss 110, 111; [ATO, FBT instalment](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/fringe-benefits-tax-fbt-instalment) |

### Section 4 — Computation rules

#### 4.1 PAYG withholding (labels W1-W5)

- **PAYG withholding computation steps** — **Step 1.** Identify the payments and withholding labels that apply during the period: - W1 — total salary, wages and other payments subject to withholding, where W1 must be completed; - W2 — amounts withheld from the payments shown at W1; - W3 — other amounts withheld; - W4 — amounts withheld where an ABN was not quoted; and - W5 — total amounts withheld: W2 + W3 + W4. **Step 2.** Reconcile the labels that the entity must report on its issued activity statement with payroll records, STP data and any ATO pre-fill. The ATO uses STP amounts to pre-fill W1 and W2 on activity statements; verify them, and complete W3, W4 and W5 where applicable. Whether a small or medium withholder reporting through STP may leave W1 out is not confirmed: the ATO's labels page states that relief only for large withholders, so complete W1 where the issued statement asks for it and confirm with the ATO before omitting it. A large withholder that does not report through STP completes only W1; a large withholder reporting through STP does not report PAYG withholding on its activity statement. Large withholders do not complete W2, W3, W4, W5 or label 4 and must pay withheld amounts electronically on the applicable large-withholder schedule. **Step 3.** Where W2 applies, cross-check it against ATO PAYG withholding tax tables for each employee's earnings level. **Step 4.** If the entity makes payments to a supplier without an ABN, withhold 47% and account for that amount under the reporting and payment rules for the entity's withholding class. **Step 5.** Where W5 applies, report the W2 + W3 + W4 total and pay the amount due by the applicable due date.  _([ATO — PAYG withholding](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding); [ATO, Employees menu in Online services for business](https://www.ato.gov.au/online-services/businesses-and-organisations-online-services/employees-in-online-services-for-business); [ATO, Changing a withholding cycle](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/changing-a-withholding-cycle))_

#### 4.2 PAYG income tax instalments (T labels, 5A and 5B)

Two methods are available:

##### Method A — Instalment amount method (label T7)

- **Instalment amount method:** The notice shows the amount at T7; if unchanged, report it at 5A. For a variation, estimate annual benchmark tax at T8. A four-instalment payer counts cumulative 25%, 50%, 75% or 100% from the first liable instalment, subtracts earlier instalments and restores applicable earlier credit entitlements. Report T9 and 5A, with the reason at T4. A nil or negative result gives zero T9/5A; an eligible credit may be claimed as a positive amount at 5B. At the third liable instalment, $12,000 annual estimated tax and $8,000 earlier instalments, with no earlier credits, give $12,000 x 75% - $8,000 = $1,000. A new payer first liable in January-March instead starts at 25%. For variation GIC, compare the annual benchmark-tax estimate used with 85% of benchmark tax; do not clear earlier periods from a final payment total. See [the PAYG guide](au-payg-instalments.md), [ATO variation instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments) and [TAA Sch 1 ss 45-232, 45-233, 45-410 and 45-415](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

##### Method B — Instalment rate method (labels T1-T2)

- **Instalment rate method:** Calculate gross quarterly instalment income at T1 under the applicable definition, excluding GST and salary/wages covered by PAYG withholding. Business deductions do not reduce T1; confirm special-regime treatment, including superannuation-fund capital gains, separately. Multiply by the pre-filled percentage at T2 and report T11 and 5A under the detailed statement instructions. To vary, enter T3 and the reason at T4; T1 x T3 gives T11 and 5A. Any eligible earlier-instalment credit claimed goes at 5B. For variation GIC, compare the varied rate with 85% of the benchmark rate, rather than comparing aggregate payments with total assessed tax. See [the PAYG guide](au-payg-instalments.md), [ATO instalment income](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/instalment-income) and [TAA Sch 1 s 45-230](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).
- **Rate-method amount:** T1 x T2, or T1 x varied T3, gives the amount at T11 and 5A.

#### 4.3 FBT instalment (label F1)

- **FBT instalment computation steps** — **Step 1.** If the taxpayer has an FBT instalment obligation, the ATO pre-fills label F1 with 25% of the prior year FBT liability. **Step 2.** The taxpayer may vary the instalment if F1 would produce more or less than the expected FBT liability for the year, using labels F2, F3 and F4 (mechanics in `au-fbt-year.md`). If the estimate used is less than 90% of the tax assessed for the year, GIC can apply (FBTAA 1986 s 112B); the ATO also warns that a penalty may apply where total instalments, or the estimates behind them, are less than 90% of actual liability. **Step 3.** Report at F1, or F3 if varied, and copy the amount to 6A. The annual FBT return (due 21 May for non-tax-agent lodgement or 25 June for tax agents) reconciles the actual liability.  _(FBTAA 1986 ss 103, 110 to 112B; [ATO, FBT instalment](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/fringe-benefits-tax-fbt-instalment))_

#### 4.4 Net BAS payable / refundable

- **Net BAS payable or refundable:** Use the amounts reported in the issued statement's summary: total liabilities at 8A less total credits at 8B gives the net amount at 9. Include every applicable tax role. Where only GST, PAYG withholding, PAYG instalments and FBT instalments apply, the components are `(1A - 1B) + 4 + 5A + 6A - 5B - 6B`, using only labels applicable to that statement. Other liabilities and credits must also enter the summary when present. A positive result is payable; a negative result is a credit before any ATO account offsets. W5 transfers to 4 where required; large withholders pay withholding separately and do not add it to this BAS. Use F1 at 6A if unchanged, or the reportable varied F3 at 6A. For a negative FBT variation calculation, F3 and 6A are zero and an eligible credit may be claimed as a positive amount at 6B. Do not add F1 again after using 6A, or treat annual estimates at T8 or F2 as payments. ([ATO, FBT instalment](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/fringe-benefits-tax-fbt-instalment); [ATO, PAYG withholding](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding); [ATO, PAYG activity statement labels](https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement).)

## Boundary and exception table

### Section 5 — Edge cases and special rules

#### 5.1 Variation of PAYG instalments

- **PAYG instalment variation and GIC** — Apply the ATO’s method-specific 85% shortfall test to a variation using expected full-year income and tax. Document the estimate and review it as circumstances change. Repeated variations do not themselves change the published GDP adjustment factor.  _([ATO PAYG variation instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments))_

#### 5.2 First year of business

- **Starting PAYG instalments / first-year businesses** — The ATO works out automatic entry from information in the latest tax return. It notifies the taxpayer when they enter the PAYG instalments system, and payments start once it sends an activity statement or instalment notice. A person new to business can request voluntary entry. Under Schedule 1 section 45-15 of the Taxation Administration Act 1953, an entity is liable to pay instalments if the Commissioner has given it an instalment rate in writing.  _([ATO — Starting PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments); [TAA 1953 Sch 1 s 45-15](https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html#_Toc235715860))_

#### 5.3 STP and BAS alignment

- **STP and BAS labels** — Reporting through STP does not cancel activity-statement obligations arising from GST, PAYG instalments or other tax roles. Complete the PAYG-withholding labels required by the issued activity statement; Section 4.1 records that W1 relief is unconfirmed for small and medium withholders. Different reporting and payment rules apply to large withholders. ATO Online Services may pre-fill W1 and W2 from STP information for eligible electronic activity statements; use payroll records as the primary source, then verify and correct any pre-filled figures. For a small employer with 19 or fewer payees, in-scope payments to closely held payees may be reported through STP quarterly, but arm's-length payees must still be reported on or before payday. That timing concession does not itself remove BAS obligations.  _([ATO — PAYG withholding](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding); [ATO, Employees menu in Online services for business](https://www.ato.gov.au/online-services/businesses-and-organisations-online-services/employees-in-online-services-for-business); [ATO, Changing a withholding cycle](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/changing-a-withholding-cycle); [ATO, STP concessional reporting](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/concessional-reporting))_

- **Award transport transition:** For payments on or after 1 October 2026, the special nil withholding variation ends. Include payments at W1 where required and actual withholding at W2. Use the appropriate STP allowance classification. Under cutover, stop adding new AD amounts before the first payment on or after 1 October and retain earlier AD year-to-date amounts. The zeroing-out method transfers AD year-to-date amounts by an Update Event and may be used before 31 December 2026 if withholding is correct from 1 October. AD cannot be included for payments made on or after 1 July 2027. Reconcile payment totals and withholding separately from classification changes. See the [ATO transition methods](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/in-detail/single-touch-payroll-phase-2-employer-reporting-guidelines/changes-to-award-transport-payments) and [W1/W2 instructions](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding).

#### 5.4 Ceasing PAYG instalments

- **Stopping PAYG instalments** — For individuals, the ATO will automatically remove a taxpayer if one of its published automatic-exit conditions is met; this includes an estimated (notional) tax liability of less than $500. That threshold is an automatic-exit condition, not a standalone self-exit test. An individual who is no longer earning business or investment income may request to exit, subject to the ATO's eligibility requirements and listed exclusions. Individuals can request exit through myGov: **Tax > Manage > Tax registrations > Cancel** (the option is available only when eligible), through a registered tax agent, or by contacting the ATO. If the Commissioner withdraws the instalment rate, the entity ceases to be liable to pay further instalments.  _([ATO — Stopping PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments); [TAA 1953 Sch 1 s 45-90](https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html#_Toc235715874))_

#### 5.5 Nil BAS / activity statement

- **Nil lodgment and FTL exposure** — If an entity has nothing to report for a BAS period but is required to lodge the BAS, it must lodge it as nil by the due date. A business that has paused trading but keeps its GST registration continues to receive a BAS and must lodge it as nil. Do not assume every zero-value activity-statement notice has that obligation: the ATO says quarterly Forms R (PAYG instalment), S (GST instalment) and T (PAYG and GST instalment) generally need only be lodged when varying the instalment amount. If a required BAS is not given to the Commissioner in approved form by its due date, the entity may be liable to an FTL administrative penalty. The base amount is one penalty unit for each 28-day period (or part) for which it remains outstanding, capped at five units; statutory multipliers apply to specified medium, large and significant-global entities. The Commissioner may remit all or part of the penalty. Use the applicable penalty-unit value for the relevant period, rather than a static tax-year dollar figure.  _([ATO — nil activity-statement guidance](https://www.ato.gov.au/api/public/content/0-0b929c4e-ddac-4b4f-a627-7427575b94a2); [ATO — paused business and nil BAS](https://www.ato.gov.au/api/public/content/0-8551e46a-7b10-44c9-b5b4-7fc8bd0c32d5); [TAA 1953 Sch 1 ss 286-75, 286-80 and 298-20](https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html); [Crimes (Amount of a Penalty Unit) Instrument 2026](https://www.legislation.gov.au/F2026N00424/asmade/2026-06-16/text/original/epub/OEBPS/document_1/document_1.html))_

## Worked cases

### Case 1: varied FBT replaces the pre-filled instalment

For the quarter ending 31 December 2026, F1 is $10,000, estimated annual FBT at F2 is $28,000 and previous instalment liabilities are $20,000 with no previous credits. The ATO formula gives F3 and 6A of $1,000. The independently reconciled GST labels are 1A $40,500 and 1B $26,900, withholding at 4 is $5,400 and unchanged PAYG instalments at 5A are $6,200. No other liabilities, credits or account offsets apply. The BAS is $26,200 payable. Adding F1 instead would produce $35,200 and overstate it by $9,000.

```oa-check
name: AU BAS uses varied FBT at 6A
inputs:
  f1: 10000
  f2: 28000
  quarter_fraction: 0.75
  prior_fbt_liabilities: 20000
  prior_fbt_credits: 0
  gst_1a: 40500
  gst_1b: 26900
  paygw_4: 5400
  paygi_5a: 6200
steps:
  - varied_fbt: f2 * quarter_fraction - (prior_fbt_liabilities - prior_fbt_credits)
  - fbt_6a: max(0, varied_fbt)
  - total_8a: gst_1a + paygw_4 + paygi_5a + fbt_6a
  - total_8b: gst_1b
  - net_9: total_8a - total_8b
  - using_f1_instead: gst_1a + paygw_4 + paygi_5a + f1 - total_8b
  - overstatement: using_f1_instead - net_9
expected:
  varied_fbt: 1000
  fbt_6a: 1000
  total_8a: 53100
  total_8b: 26900
  net_9: 26200
  using_f1_instead: 35200
  overstatement: 9000
```

### Case 2: negative PAYG variation is a positive credit

The taxpayer has paid quarterly PAYG instalments from the first quarter of 2026-27. At the third quarter it estimates annual instalment tax of $6,000 and has paid $8,000 in the first 2 quarters, with no earlier credits. The variation calculation is negative $3,500. T9 and 5A are zero; entitlement to claim the full $3,500 credit at 5B is stipulated and the taxpayer chooses to claim it. Separately established labels are 1A $1,000, 1B $500 and 4 $2,000. No FBT, other tax roles or account offsets apply. The BAS result is a $1,000 credit. This illustration assumes current rules continue through the March 2027 quarter.

```oa-check
name: AU BAS negative PAYG variation labels
inputs:
  estimated_annual_tax: 6000
  quarter_fraction: 0.75
  earlier_instalments: 8000
  earlier_credits: 0
  gst_1a: 1000
  gst_1b: 500
  paygw_4: 2000
steps:
  - varied_paygi: estimated_annual_tax * quarter_fraction - earlier_instalments + earlier_credits
  - t9: max(0, varied_paygi)
  - paygi_5a: t9
  - paygi_5b: max(0, -varied_paygi)
  - total_8a: gst_1a + paygw_4 + paygi_5a
  - total_8b: gst_1b + paygi_5b
  - net_9: total_8a - total_8b
expected:
  varied_paygi: -3500
  t9: 0
  paygi_5a: 0
  paygi_5b: 3500
  total_8a: 3000
  total_8b: 4000
  net_9: -1000
```

Recompute with `python3 scripts/check-examples.py --require skills/international/australia/au-gst-bas.md`. These synthetic cases check label arithmetic for stipulated entitlements, not variation reason codes, estimates, GIC, taxpayer eligibility or a final ATO account refund.

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


### Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.



## Filing and payment

### Section 2 — Filing requirements

#### 2.1 Who must lodge a BAS

- **Activity-statement lodgement obligation** — Lodgement depends on the entity's tax roles, reporting method and the form the ATO issues. Lodge each required BAS or activity statement by its due date. Quarterly Forms R (PAYG instalment), S (GST instalment) and T (PAYG and GST instalment) generally need only be lodged when varying the instalment amount.  _([ATO — activity statements and nil lodgments](https://www.ato.gov.au/api/public/content/0-0b929c4e-ddac-4b4f-a627-7427575b94a2))_

#### 2.2 Lodgement frequency

**Lodgement frequency**  _(GST Act Div 27 and s 31-5; TAA 1953 Sch 1 Subdiv 16-B)_

| Situation | BAS frequency | Source |
| --- | --- | --- |
| GST turnover < $20M, no monthly election or ATO direction to report monthly, and no annual reporting arrangement | Quarterly | [ATO, BAS reporting cycles](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas) |
| GST turnover >= $20M | Monthly | GST Act s 27-15 and s 31-5 |
| Voluntary monthly reporter | Monthly | ATO election |
| PAYG withholding (with or without GST) | Set by the withholder class below, not by GST turnover | TAA 1953 Sch 1 ss 16-75, 16-95 to 16-105 |

**PAYG withholder classes**  _([ATO, Paying and reporting PAYG withholding amounts for small and medium withholders](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/when-to-pay-and-report-on-activity-statements); [ATO, Changing a withholding cycle](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/changing-a-withholding-cycle))_

| Class | Test for a particular month | Report and pay | Source |
| --- | --- | --- | --- |
| Small | Withheld at least one amount in the month and is neither large nor medium | Quarterly, by the date on the issued activity statement (a deferred BAS payer uses the dates in 2.3). Monthly statements can be arranged with the ATO | TAA 1953 Sch 1 ss 16-75(3), (4), 16-105 |
| Medium | Not large, and withheld more than $25,000 in a financial year ending before that month, or so determined by the Commissioner | Monthly, by the 21st of the next month (a deferred BAS payer has the 28th, and 28 February for December amounts) | TAA 1953 Sch 1 ss 16-75(2), (2A), 16-100 |
| Large | Withheld more than $1 million in a financial year ending at least 2 months before that month (for a company, alone or across its wholly-owned group at the end of that year), or so determined by the Commissioner | Pay electronically. Withheld on Saturday or Sunday: by the second Monday after. Monday or Tuesday: by the first Monday after. Wednesday: by the second Thursday after. Thursday or Friday: by the first Thursday after. See 4.1 for the labels | TAA 1953 Sch 1 ss 16-75(1), 16-95 |

- **Class follows earlier financial years and determinations, not one statement** — The tests look back to completed financial years, not only the latest one. One quarter's withholding does not decide the class, and a fall in withholding does not lower it by itself: $40,000 withheld in 2024-25 and $20,000 in 2025-26 leaves an entity medium in 2026-27 unless the Commissioner determines otherwise. A downward determination needs written notice given before the month, and the entity may apply for one in writing (s 16-110). An upward determination can have regard to the amounts likely to be withheld in the following 12 months (s 16-115). The ATO describes the classes by annual amount ($25,000 or less; $25,001 to $1 million; more than $1 million), reviews withholding each financial year and writes when a cycle is to change; for 2026-27 it wrote in April for changes from 1 July 2026. An entity can ask to stay on a lower cycle if its estimated withholding for the coming year is within the threshold. Where a quarter's amount would exceed $25,000 if repeated across the year, check earlier years' amounts, any ATO notice and the issued statement.
- **Large withholder dates** — The ATO summarises the schedule as 6 to 8 days, but the statutory table can give 9: an amount withheld on Saturday 3 October 2026 is due by Monday 12 October 2026.  _([ATO, Changing a withholding cycle](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/changing-a-withholding-cycle); [ATO, Changes to your PAYG withholding cycle](https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/changes-to-your-payg-withholding-cycle); TAA 1953 Sch 1 ss 16-75(1), 16-95 to 16-115)_

#### 2.3 Due dates (quarterly)

**Due dates (quarterly)**  _(ATO lodgement programme)_

| Quarter | Period | Due date |
| --- | --- | --- |
| Q1 | 1 Jul – 30 Sep | 28 October |
| Q2 | 1 Oct – 31 Dec | 28 February |
| Q3 | 1 Jan – 31 Mar | 28 April |
| Q4 | 1 Apr – 30 Jun | 28 July (registered tax and BAS agents lodging electronically generally have 25 August; online self-lodgers may get 2 extra weeks) |

- **Weekend/holiday due date rule** — If the due date falls on a weekend or public holiday, the due date is the next business day. Tax agents may have extended lodgement programmes.  _(ATO lodgement programme)_

## Completion checklist

### Section 6 — Self-checks

Before delivering output, verify:

- [ ] Applicable PAYG withholding labels agree with payroll records, STP data and any ATO pre-fill
- [ ] PAYG instalment income (T1) excludes salary, GST, and capital gains
- [ ] The notified rate remains at T2; any varied rate is at T3, the reason at T4 and the rate-method amount at T11/5A
- [ ] An amount variation uses T8/T9 and the cumulative quarterly calculation
- [ ] FBT instalment (F1) is 25% of prior year FBT liability or validly varied
- [ ] Lodgement due date has been correctly identified (including any tax agent extensions)
- [ ] GST section cross-references to australia-gst.md output
- [ ] Rates and thresholds match the income year of the statement, including the GDP adjustment factor (5% for 2026-27; 4% for 2025-26 and the substituted accounting periods in Section 3.2)
- [ ] Withholder class is checked against earlier financial years' withholding, any Commissioner determination and any ATO notice, not one quarter
- [ ] Output format matches the base skill spec

## Sources

| Source | URL | Read on |
|---|---|---|
| TAA 1953 compilation 227, selected Sch 1 ss 45-230, 45-232, 45-233, 45-410 and 45-415: rate/annual-estimate tests and liable-instalment sequence | <https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html> | 2026-11-02; effective 1 October, registered 19 October 2026; selected PAYG provisions only |
| ATO instalment income, included/excluded income sections | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/calculate-your-payg-instalments/instalment-income> | 2026-11-02; page updated 9 March 2022 |
| ATO BAS due dates, updated 17 September 2026 | <https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas> | 2026-11-02; monthly direction, quarterly and annual conditions |
| ATO PAYG activity statement, updated 9 January 2023 | <https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement> | 2026-11-02; option 1 labels and option 2 T1/T2/T3/T11/5A |
| Retained citation | <https://www.ato.gov.au/api/public/content/0-0b929c4e-ddac-4b4f-a627-7427575b94a2> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/when-to-pay-and-report-on-activity-statements> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/changing-a-withholding-cycle> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/changes-to-your-payg-withholding-cycle> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments> | Not re-read for this format update; see retained provenance |
| ATO PAYG variations, updated 23 June 2026 | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments> | 2026-11-02; amount-method steps 3-5, quarterly formula, zero T9/5A and positive 5B |
| Retained citation | <https://softwaredevelopers.ato.gov.au/gdp-adjustment-2025-26-gst-and-payg-instalments> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://softwaredevelopers.ato.gov.au/GDPupliftfactor> | Not re-read for this format update; see retained provenance |
| ATO FBT instalment, updated 1 May 2025 | <https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/fringe-benefits-tax-fbt-instalment> | 2026-11-02; F3 formula, zero floor, 6A/6B and December example |
| ATO PAYG withholding, updated 1 May 2025 | <https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding> | 2026-11-02; W5 to 4 and large-withholder exception |
| Retained citation | <https://www.ato.gov.au/online-services/businesses-and-organisations-online-services/employees-in-online-services-for-business> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html#_Toc235715860> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/concessional-reporting> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/in-detail/single-touch-payroll-phase-2-employer-reporting-guidelines/changes-to-award-transport-payments> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html#_Toc235715874> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/api/public/content/0-8551e46a-7b10-44c9-b5b4-7fc8bd0c32d5> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C1953A00001/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/F2026N00424/asmade/2026-06-16/text/original/epub/OEBPS/document_1/document_1.html> | Not re-read for this format update; see retained provenance |

Not yet confirmed: The 2 executable cases check the selected BAS label arithmetic only. A complete page-level source/read-date audit and independent legal review have not been performed for this guide. Retained dates, thresholds, variation eligibility, GIC and annual FBT procedures outside the selected reads remain subject to their original qualifications and qualified review.

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
