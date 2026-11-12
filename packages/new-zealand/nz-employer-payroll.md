---
name: nz-employer-payroll
description: >
  Use this guide for ordinary New Zealand employer payroll paid from 1 April
  2026 to 31 March 2027. Covers PAYE tax-code inputs, the ACC earners' levy,
  KiwiSaver employee deductions and compulsory employer contributions, ESCT,
  payday filing, payment schedules and payroll records. Trigger on NZ payroll,
  PAYE, payday filing, KiwiSaver employer contributions, ESCT and employer
  deductions. Distinguishes the electronic filing threshold from the large
  employer payment threshold. Requires actual pay dates, employee declarations
  and notices. Special payments, cross-border employment, leave entitlements
  and employer ACC invoice calculations require separate checks.
jurisdiction: NZ
category: payroll
tax_year: 2026
tax_year_notes: "Ordinary payroll paid 1 April 2026 to 31 March 2027; separate filing and payment rules checked 12 November 2026"
tier: 2
last_updated: 2026-11-12
version: 0.1
verified_by: pending
review_status: pending_review
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand employer payroll v0.1

> **General reference only.** This is a source-cited draft awaiting qualified review. Confirm the employee's facts and the rules for the actual payday before filing, paying or relying on a calculation.

## Section 1 -- Scope and required inputs

This guide covers ordinary salary and wages paid by a New Zealand employer in NZD during **1 April 2026 to 31 March 2027**. It provides selected tax, contribution and filing rules, not complete employment-law or whole-topic coverage. Start with [Inland Revenue's salary and wage deduction instructions][S1] and its [2026-27 payroll calculation specification][S2].

Obtain the following before calculating:

- Employer registration, actual payday, pay frequency and period covered. [Register as an employer as soon as you start employing staff][S3].
- Employee classification, completed IR330 tax-code declaration and any Inland Revenue tax-code, tailored-rate, student-loan, child-support or arrears notice. Resolve conflicting instructions before using a rate.
- Gross pay and each payment's character. Determine PAYE income and KiwiSaver gross salary or wages separately; allowances, reimbursements and special payments need their own treatment.
- KiwiSaver membership and eligibility, valid deduction-rate instruction, employer contribution agreement (including whether it promises a gross or net-of-ESCT amount) and any valid opt-out, savings-suspension or temporary-rate-reduction notice.
- For ESCT, employment start date, whether the employee worked for this employer throughout the preceding tax year and the relevant salary/wages plus gross employer superannuation contributions.
- Annual PAYE and ESCT figures, any connected employers and the established filing and payment schedules. The $50,000 electronic filing test and $500,000 remittance test serve different purposes.

An unknown classification, contribution base or notice is an input gap. Do not invent a resident tax code, a pension exemption or a flat PAYE percentage. Ordinary salary rules do not establish the treatment of contractors, non-residents, offshore employers, IR56 workers, benefits, termination/lump-sum payments or paid parental leave.

## Section 2 -- PAYE and the employee ACC levy

Use the employee's IR330 code and any applicable Inland Revenue instruction. [Inland Revenue][S1] requires **ND at 45% plus the applicable ACC earners' levy** when no completed tax-code declaration is supplied. Do not use a zero rate or guess a standard code. Contractor schedular payments use a separate IR330C process; they are not automatically salary payroll. [S1], [S4]

Use the official PAYE calculator or actual-period deduction tables linked from [the salary/wage deductions page][S1], with the correct payday, tax code and pay frequency. PAYE calculation includes ACC earners' levy where applicable. **Do not add another ACC levy to a PAYE result that already includes it.** Annual income-tax brackets alone do not reproduce every payroll code, frequency, levy cap or rounding rule. [S1], [S2]

| Employee earners' levy period | GST-inclusive rate | Maximum annual liable earnings | Maximum annual levy |
|---|---:|---:|---:|
| 1 April 2026 to 31 March 2027 | 1.75% | $156,641 | $2,741.22 |

Source: [Inland Revenue's earners' levy table][S5]. Apply the actual payroll calculation and its cap rules; this annual table is not an instruction to charge 1.75% on uncapped pay or to combine multiple employments without checking their treatment.

Student-loan and child-support deductions need the actual code or notice and applicable calculation. Child-support deductions have a 40% net-after-tax protected-earnings limit; it does not cap every other deduction at 40%. Follow Inland Revenue's reporting instructions for any shortfall rather than automatically recovering it in a later pay. [S1]

The employee earners' levy comes from the employee's income through PAYE. The employer's **Work and Working Safer levies** are separately invoiced by ACC and require the business's classification, liable payroll and current invoice/rates. Do not add them as another generic employee deduction. This guide does not calculate those invoices. [ACC's explanation of levy responsibilities][S6] supports that distinction; use [S5] for the dated employee rate.

## Section 3 -- KiwiSaver from 1 April 2026

The default employee deduction and minimum compulsory employer contribution increased from 3% to **3.5% for paydays on or after 1 April 2026**. Where a pay period straddles 1 April, the payday determines the rate for the whole payment. Existing employee elections of 4%, 6%, 8% or 10% remain available. Do not prorate the April change by days worked. [S7], [S8]

### Employee deductions

Use the employee's valid rate instruction, including KS2, a written request or an Inland Revenue rate-change notice, or the 3.5% default where deductions are required. The ordinary choices are **3.5%, 4%, 6%, 8% and 10%** of KiwiSaver gross salary or wages. A valid temporary rate reduction permits **3%** for its approved period of **3 to 12 months** and can be renewed. Apply the approved notice; do not substitute 3% merely because an employee asks informally. Savings suspensions and opt-outs require the appropriate evidence. [S7], [S8]

### Compulsory employer contributions

The ordinary minimum is 3.5% of qualifying gross salary or wages for an eligible contributing member. From 1 April 2026, this includes eligible **16- and 17-year-old members**; the ordinary eligibility conditions include age 16 to under 65, membership of KiwiSaver or a complying fund, employee deductions and no disqualifying defined-benefit arrangement. Membership and employer-contribution eligibility do not mean every 16-year-old is automatically enrolled. Check the actual employee's circumstances. [S7], [S9]

If an employee has an approved temporary 3% deduction rate, the employer **may choose** to reduce its matching contribution to 3%; it need not do so. Record the choice and any contract requiring more. Start and stop contributions under Inland Revenue's membership, opt-out and suspension instructions. Reaching 65 may end the statutory obligation, but an agreement or voluntary contribution can continue and ESCT may still apply. [S9]

Employer contributions are normally additional to salary or wages. An agreed total-remuneration arrangement needs a genuine agreement and must still satisfy minimum-wage requirements excluding the employer contribution. Do not reduce contracted pay automatically. Deduct ESCT from the gross employer contribution unless employer and employee have agreed to the separate PAYE treatment. The employee's own KiwiSaver deduction is not subject to ESCT. KiwiSaver employer contributions go through Inland Revenue; complying-fund contributions go directly to that fund. [S9], [S10]

Check whether an agreed employer contribution is gross or net of ESCT. A promised net contribution requires grossing up under IR335's method before the ordinary ESCT calculation. Reconcile the promised net after the required truncation; do not treat a contractual net percentage as the gross statutory minimum. This guide does not work a contractual gross-up example. [IR335, page 27][S13]

The announced 4% default from 1 April 2028 is a future change, not the rate for 2026-27 payroll. [S7]

## Section 4 -- ESCT rate and calculation

### Set the employee's rate

If the employee worked for this employer for the whole preceding tax year, use that year's salary/wages **plus gross employer superannuation contributions before ESCT**. Otherwise estimate both amounts for the **current tax year**. A part-year new starter is not automatically assigned a full 12 months of earnings beyond 31 March. Recalculate for the next tax year; ordinary salary changes during the year do not reset the rate. [S2, sections 5.20.4-5.20.5][S2]

| ESCT rate threshold amount, last whole dollar | ESCT rate |
|---|---:|
| $0 to $18,720 | 10.5% |
| $18,721 to $64,200 | 17.5% |
| $64,201 to $93,720 | 30% |
| $93,721 to $216,000 | 33% |
| $216,001 upwards | 39% |

These are single rates on the relevant employer contribution, not progressive bands applied to salary. [Income Tax Act 2007, Schedule 1 Part D][S11] says to select the band for the **last dollar** of the threshold amount. Do not round a fractional dollar up into the next band. The current technical specification reproduces the table in section 5.20.4. Defined-benefit funds and certain past-employee contributions have separate rules and are outside the ordinary case here. [S2], [S11]

### Calculate each contribution

Under [the 2026-27 specification, sections 5.20.6 and 5.21.3][S2], and [Inland Revenue's deduction instructions][S12]:

1. Calculate the gross employer contribution using dollars and cents.
2. Drop cents from that contribution to obtain the whole-dollar ESCT base. **Do not round up.**
3. Multiply that whole-dollar base by the employee's ESCT rate.
4. Truncate the tax to cents, rather than rounding it to the nearest cent.
5. Subtract that tax from the **original contribution including cents** to obtain the net employer contribution.

The September 2026 IR335 employer guide's page 27 Matthew example taxes $204.17 directly at 17.5%, despite its page 26 whole-dollar instruction. Do not copy that example's $35.73 tax. The technical algorithm and [the dedicated deduction page][S12] require a whole-dollar base; $204.17 at 17.5% gives **$35.70 ESCT and $168.47 net contribution**. This is a recorded source discrepancy, not an alternative method. [IR335, pages 26-27][S13]

## Section 5 -- Filing, remitting and records

### Employment information

File employment information for every payday using the actual pay date, not the end of the work period. Electronic filing is due within **2 working days** of payday. Allowed paper filing is due within **10 working days** of each payday, or under the permitted twice-monthly grouping within 10 working days of the 15th and month end. Filing and payment deadlines are separate; file on time even if unable to pay. [S14]

New employers may file on paper during their first 6 months. After that, electronic filing is required where annual PAYE and ESCT is **$50,000 or more**. Smaller employers can choose electronic filing. Tell Inland Revenue the required new-employee information on or before the first payday; for electronic filing this includes the employee's address and, if supplied, date of birth. Tell Inland Revenue the leaver's end date on or before their last day. Advise Inland Revenue when no wages will be paid for a month or more, including an irregular or stopped payroll. [S14], [S15]

### Paying deductions

| Gross annual PAYE and ESCT payment category | Paydays covered | Ordinary payment deadline |
|---|---|---|
| Less than $500,000 | Whole month | 20th of the following month |
| $500,000 or more | 1st to 15th | 20th of the same month |
| $500,000 or more | 16th to month end, except December | 5th of the following month |
| $500,000 or more | 16 to 31 December | **15 January** |

For established employers the large-employer test uses the preceding year's gross PAYE and ESCT. New employers pay monthly until reaching $500,000. Gross PAYE for this test includes ESCT but excludes ACC earners' levy, student loans, KiwiSaver and child support. Check connected-employer aggregation rather than treating each entity as independent. If a payment deadline falls on a weekend or public holiday, the next working day applies. [IR335, pages 71-72][S13]

The [payment web page][S16] says 'more than' $500,000, leaving equality unclear; IR335 explicitly says **$500,000 or more**. Use the latter boundary rather than classifying exactly $500,000 as a small employer. This threshold does not replace the separate $50,000 filing threshold.

Reconcile PAYE, student loans, child support, employee KiwiSaver, net employer KiwiSaver and ESCT separately before making the combined **EMP** payment. Confirm the employer account, period and reference. Other arrears notices can require a separate payment process; do not assume every withheld amount belongs in ordinary employment information or the same payment. Filing an employment-information return does not itself pay the liability. [S12], [S13], [S16]

Keep wagebook information, PAYE payment records, employee declarations and applicable Inland Revenue notices/certificates. [The PAYE records page][S17] identifies the required record types. This guide does not establish all employment-record retention periods, payslip obligations or employment-law records.

## Section 6 -- Conditional worked checks

These fictional cases assume membership, contribution bases and rates have already been established. They verify contribution arithmetic, not PAYE, eligibility or an actual person's liability. Both use the ordinary ESCT method, not an agreed PAYE alternative. Set tolerance to zero so a cent error fails.

**Case 1: truncating a half-cent tax result.** Qualifying gross salary of $3,000 at 3.5% gives a $105.00 gross employer contribution. At a confirmed 17.5% ESCT rate, $18.375 truncates to **$18.37** and the fund receives **$86.63**.

```oa-check
name: nz-2026-employer-esct-half-cent
tolerance: 0
inputs:
  salary: 3000
  contribution_rate: 3.5
  esct_rate: 17.5
steps:
  gross_contribution: pct(salary, contribution_rate)
  esct_base: floor(gross_contribution)
  esct: floor(pct(esct_base, esct_rate) * 100) / 100
  net_contribution: gross_contribution - esct
expected:
  gross_contribution: 105
  esct: 18.37
  net_contribution: 86.63
```

**Case 2: retaining contribution cents.** A confirmed $204.17 gross employer contribution at 17.5% uses a $204 ESCT base. Tax is **$35.70**, leaving **$168.47**. Dropping the contribution's cents from the amount paid to the fund would also be wrong.

```oa-check
name: nz-2026-employer-esct-whole-dollar-base
tolerance: 0
inputs:
  gross_contribution: 204.17
  esct_rate: 17.5
steps:
  esct_base: floor(gross_contribution)
  esct: floor(pct(esct_base, esct_rate) * 100) / 100
  net_contribution: gross_contribution - esct
expected:
  esct_base: 204
  esct: 35.70
  net_contribution: 168.47
```

Before release also check an exactly $50,000 electronic-filing case, an exactly $500,000 large-employer case, the December 15 January exception and a pay period straddling 1 April. A temporary 3% employee rate does not by itself force the employer to reduce its rate.

## Section 7 -- Limits and sources

Still requiring separate actual-case checks: complete PAYE code algorithms and extra-pay rules; student-loan and attachment calculations; automatic-enrolment, opt-out and refund administration; full definitions of contribution bases; cross-border employment and treaty/social-security questions; FBT; leave, holiday pay, minimum wage and termination entitlements; employer ACC invoices; records retention and penalties. No whole payroll, social-contribution or compliance topic is certified complete by this guide. It remains tier 2 and pending qualified review.

Sources checked 12 November 2026. The technical specification is dated 24 March 2026, version 1.0, and expressly covers 1 April 2026 to 31 March 2027. IR335's cover says September 2026. Selected PDF pages were read as native text and images; this does not claim full review of either PDF or the complete statute.

[S1]: https://www.ird.govt.nz/deductions "Salary and wage deductions"
[S2]: https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 "2026-27 payroll specification, selected sections"
[S3]: https://www.ird.govt.nz/setting-up-a-business-or-organisation "Registering as an employer"
[S4]: https://www.ird.govt.nz/employing-staff/deductions-from-income "Deductions from income"
[S5]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates "ACC earners' levy rates"
[S6]: https://www.acc.co.nz/for-business/understanding-levies-if-you-work-or-own-a-business "Levy responsibilities; not the source for dated rates"
[S7]: https://www.ird.govt.nz/kiwisaver-changes "KiwiSaver changes"
[S8]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay "Employee KiwiSaver deductions"
[S9]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds "Employer contributions"
[S10]: https://www.ird.govt.nz/esct "ESCT scope and methods"
[S11]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/ "Income Tax Act 2007, Schedule 1 Part D, current copy dated 4 September 2026"
[S12]: https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution "Deducting ESCT"
[S13]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131 "IR335 employer guide, September 2026, selected pages"
[S14]: https://www.ird.govt.nz/payday "Payday filing"
[S15]: https://www.ird.govt.nz/employing-staff/payday-filing/filing-employment-information-electronically "Electronic employment information"
[S16]: https://www.ird.govt.nz/employing-staff/payday-filing/paying-deductions-to-inland-revenue "Paying deductions"
[S17]: https://www.ird.govt.nz/employing-staff/deductions-from-income/paye-records "PAYE records"

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
