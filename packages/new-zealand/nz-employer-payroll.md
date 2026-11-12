---
name: nz-employer-payroll
description: >
  Use this guide for ordinary New Zealand employer payroll paid from 1 April
  2026 to 31 March 2027. Covers ordinary and selected extra-pay PAYE and
  student-loan calculations, tailored certificates, recovery notices, child support
  and selected court-attachment calculations,
  the ACC earners' levy, selected KiwiSaver enrolment, base, notice and refund administration, employer contributions, ESCT,
  payday filing, payment schedules and payroll records. Trigger on NZ payroll,
  PAYE, payday filing, KiwiSaver employer contributions, ESCT and employer
  deductions. Distinguishes the electronic filing threshold from the large
  employer payment threshold. Requires actual pay dates, employee declarations
  and notices. Unresolved special payments, cross-border employment, leave entitlements
  and employer ACC invoice calculations require separate checks.
jurisdiction: NZ
category: payroll
tax_year: 2026
tax_year_notes: "Ordinary payroll paid 1 April 2026 to 31 March 2027; separate filing and payment rules checked 12 November 2026"
tier: 2
last_updated: 2026-11-12
version: 0.5
verified_by: pending
review_status: pending_review
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand employer payroll v0.5

> **General reference only.** This is a source-cited draft awaiting qualified review. Confirm the employee's facts and the rules for the actual payday before filing, paying or relying on a calculation.

## Section 1 -- Scope and required inputs

This guide covers ordinary salary and wages and selected extra-pay calculations for a New Zealand employer in NZD during **1 April 2026 to 31 March 2027**. It provides selected tax, contribution and filing rules, not complete employment-law or whole-topic coverage. Start with [Inland Revenue's salary and wage deduction instructions][S1] and its [2026-27 payroll calculation specification][S2].

Obtain the following before calculating:

- Employer registration, actual payday, pay frequency and period covered. [Register as an employer as soon as you start employing staff][S3].
- Employee classification, completed IR330 tax-code declaration and any Inland Revenue tax-code, tailored-rate, student-loan, child-support or arrears notice. Resolve conflicting instructions before using a rate.
- Gross pay and each payment's character. Determine PAYE income and KiwiSaver gross salary or wages separately; allowances, reimbursements and special payments need their own treatment.
- KiwiSaver membership and eligibility, valid deduction-rate instruction, employer contribution agreement (including whether it promises a gross or net-of-ESCT amount) and any valid opt-out, savings-suspension or temporary-rate-reduction notice.
- For ESCT, employment start date, whether the employee worked for this employer throughout the preceding tax year and the relevant salary/wages plus gross employer superannuation contributions.
- Annual PAYE and ESCT figures, any connected employers and the established filing and payment schedules. The $50,000 electronic filing test and $500,000 remittance test serve different purposes.

An unknown classification, contribution base or notice is an input gap. Do not invent a resident tax code, a pension exemption or a flat PAYE percentage. Ordinary salary rules do not establish the treatment of contractors, non-residents, offshore employers, IR56 workers, benefits or paid parental leave. The selected extra-pay methods below require an established payment classification; they do not determine employment-law entitlements.

## Section 2 -- PAYE and the employee ACC levy

Use the employee's IR330 code and any applicable Inland Revenue instruction. [Inland Revenue][S1] requires **ND at 45% plus the applicable ACC earners' levy** when no completed tax-code declaration is supplied. Do not use a zero rate or guess a standard code. Contractor schedular payments use a separate IR330C process; they are not automatically salary payroll. [S1], [S4]

Use the official PAYE calculator or actual-period deduction tables linked from [the salary/wage deductions page][S1], with the correct payday, tax code and pay frequency. PAYE calculation includes ACC earners' levy where applicable. **Do not add another ACC levy to a PAYE result that already includes it.** Annual income-tax brackets alone do not reproduce every payroll code, frequency, levy cap or rounding rule. [S1], [S2]

| Employee earners' levy period | GST-inclusive rate | Maximum annual liable earnings | Maximum annual levy |
|---|---:|---:|---:|
| 1 April 2026 to 31 March 2027 | 1.75% | $156,641 | $2,741.22 |

Source: [Inland Revenue's earners' levy table][S5]. Apply the actual payroll calculation and its cap rules; this annual table is not an instruction to charge 1.75% on uncapped pay or to combine multiple employments without checking their treatment.

Student-loan and child-support deductions need the actual code or notice and applicable calculation. Ordinary employee child support is limited to 40% of gross salary/wages less the PAYE income-tax component, excluding ACC earners' levy from that tax component. It does not cap every other deduction at 40%. The notice, protected-earnings and shortfall methods are set out below. [S1], [S2, section 5.15][S2], [S13, PDF page 24][S13]

The employee earners' levy comes from the employee's income through PAYE. The employer's **Work and Working Safer levies** are separately invoiced by ACC and require the business's classification, liable payroll and current invoice/rates. Do not add them as another generic employee deduction. This guide does not calculate those invoices. [ACC's explanation of levy responsibilities][S6] supports that distinction; use [S5] for the dated employee rate.

### Ordinary M and ME calculations

For regular positive salary or wages under **M, M SL, ME or ME SL**, use the sequence in [S2, sections 5.2-5.4][S2]. Confirm the declaration and notices first. The specification calls for 6 decimal places during calculations unless a stated truncation applies.

1. Multiply taxable period pay **including cents** by 52 for weekly pay, 26 for fortnightly, 13 for every 4 weeks or 12 for monthly. Then drop the annual amount's cents to obtain whole-dollar annual income A. Do not drop period cents before annualising M/ME pay.
2. Calculate annual income tax from the following table. Keep the result unrounded.

| Whole-dollar annual income A | Annual income tax |
|---|---|
| $1 to $15,600 | A × 10.5% |
| $15,601 to $53,500 | A × 17.5% − $1,092.00 |
| $53,501 to $78,100 | A × 30% − $7,779.50 |
| $78,101 to $180,000 | A × 33% − $10,122.50 |
| Above $180,000 | A × 39% − $20,922.50 |

3. Calculate the annual ACC component: **A × 1.75% where A < $156,641; otherwise $2,741.22**. Keep this component unrounded. Use the specification's stated maximum rather than multiplying the capped earnings and rounding independently.
4. For M/M SL, add annual tax and ACC. For ME/ME SL, subtract the applicable annual IETC from that sum. On the whole-dollar A, the payroll IETC is $0 below $24,000; **$520 from $24,000 to $66,000 inclusive**; **$520 − 13% × (A − $66,000)** from $66,001 to $69,999; and $0 from $70,000. Keep the credit unrounded.
5. Divide the annual total by **52**, then **truncate to cents**. For fortnightly, 4-weekly or monthly pay, multiply that already-truncated weekly amount by 52 and divide by 26, 13 or 12 respectively, then **truncate to cents again**. Dividing the annual total directly by 12 can give a different monthly deduction. This result is PAYE including ACC; student loans and other deductions remain separate.

The payroll credit formula does not establish IETC eligibility. Check NZ tax residence, total annual income and the exclusion where the employee or partner is entitled to and receives Working for Families, and the exclusions for income-tested benefits, NZ Superannuation, Veteran's Pension and overseas equivalents. Entitlement is tested by whole months. Use ME/ME SL only under the appropriate declaration; a main job below $24,000 with total income in the eligible range may need a tailored code or year-end credit. A year-end assessment may correct too much or too little credit. [IETC eligibility][S18], [salary/wage instructions][S19]

### Ordinary secondary codes and ND

A secondary code is chosen using **estimated annual total income from all sources**, rather than the second job alone. Follow the employee's IR330 and any Inland Revenue direction. For ordinary liable salary/wages, [S2, section 5.6][S2] gives these standard deductions, each already including the 1.75% ACC levy:

| Estimated annual total income | Secondary code, with SL where required | Standard PAYE including ACC |
|---|---|---:|
| Up to $15,600 | SB / SB SL | 12.25% |
| $15,601 to $53,500 | S / S SL | 19.25% |
| $53,501 to $78,100 | SH / SH SL | 31.75% |
| $78,101 to $180,000 | ST / ST SL | 34.75% |
| Above $180,000 | SA / SA SL | 40.75% |

Drop period pay's cents **before** multiplying by the applicable standard secondary rate, then truncate the deduction to cents. The whole payment uses that code's flat rate; these are not progressive bands within the second job. Do not add ACC again or import the M/ME annualisation algorithm. [S2, sections 5.1 and 5.6][S2], [tax-code instructions][S20]

For ordinary ND salary/wages, drop period cents, multiply by **46.75%** (45% tax plus 1.75% ACC) and truncate to cents. [S2, section 5.8][S2] These standard-code algorithms do not determine an individual's final annual ACC liability across multiple employments. Resolve a valid tailored tax code, levy adjustment or other exceptional instruction separately; do not remove ACC from a standard secondary or ND rate merely by applying the M-code cap formula.

### Ordinary student-loan deductions

For the 2026-27 period, the specification's annual repayment threshold is **$24,128**, with these primary-job period thresholds: weekly **$464**, fortnightly **$928**, every 4 weeks **$1,856** and monthly **$2,010.66**. Use the stated monthly amount rather than rounding it to $2,010.67. [S2, sections 2.2 and 5.4][S2]

For **M SL or ME SL**, drop gross period pay's cents, subtract the applicable period threshold and deduct **12% of a positive excess**, truncating the result to cents. The deduction is zero where there is no excess. For an ordinary **secondary SL code**, drop period cents and deduct **12% of that whole-dollar pay**, truncating to cents; there is **no second ordinary repayment threshold**. A valid special-deduction-rate certificate substitutes its specified percentage in the relevant algorithm. Keep the student-loan result separate from PAYE, and do not reduce taxable pay by it. [S2, sections 5.4 and 5.6][S2]

Check the actual SL declaration and any repayment exemption, special rate or extra-deduction notice before using these ordinary rules. An unused primary-job threshold does not automatically transfer to a second job; apply for the appropriate special rate. Inland Revenue's [salary/wage student-loan page][S21] explains that distinction but labels its annual threshold as the **2026 tax year**; the dated 2026-27 specification supplies this guide's period-specific figures. Exemptions, recovery deductions and irregular or special payments need their own checks.

### Tailored tax codes and student-loan certificates

Use an actual Inland Revenue certificate covering the payday. Record its PAYE rate, separate student-loan rate, whether the loan threshold applies and each start/end date. For ordinary salary or wages, truncate period pay to whole dollars, multiply by the certificate's PAYE rate and truncate the deduction to cents. The quoted salary/wage PAYE rate already includes the 1.75% earners' levy; do not add it again. Calculate the loan deduction separately on the whole-dollar base: apply the certificate rate to positive income above the period threshold for main employment, or to every dollar for secondary employment, as the certificate directs. [S2, section 5.9, PDF pages 32–33][S2]

A student-loan special deduction rate changes the loan calculation, not the PAYE tax code unless the certificate says so. It may allocate unused main-job threshold through a reduced secondary-job rate; the employer cannot invent that allocation. Follow each dated rate period. Do not backdate a special deduction rate or a repayment exemption. On expiry, follow the certificate's return-to-standard instructions. If a tailored PAYE certificate expires without a replacement or new declaration, revert to the previous IR330/IR330C code; if there was none, use ND until a valid declaration or certificate arrives. [S2, section 5.9.2, PDF pages 34–37][S2]

A full-time student expecting income below the annual repayment threshold may qualify for a repayment deduction exemption even when an individual pay exceeds its threshold. Require the IRD exemption certificate, use its specified non-SL code only for its valid period and restore its instructed SL code when it ends. Student status alone does not authorise stopping deductions. A special loan rate does not absorb voluntary SLBOR deductions; keep them separate. IRD says it cancels SLCIR notices when granting an SDR: reconcile the actual notice trail rather than silently retaining or cancelling a recovery instruction yourself. [S2, sections 5.9.2–5.9.3][S2]

### Extra pay: choose the calculation before choosing a rate

Annual or special bonuses, cashed-up leave, back pay and redundancy/retiring payments can be extra pay. Overtime and regular payments are not automatically lump sums. First establish the payment's legal character, whether it relates to ending employment, the employee's code and any election for a higher rate. NSW, ND and tailored-code payments use their applicable special rate rather than the ordinary extra-pay rate table; CAE/EDW extra pay follows the primary-income method. This guide does not establish entitlement to a termination payment, ESS treatment or a contractor's schedular-payment treatment. [S22], [S23], [S24]

For a **non-termination** extra payment under an ordinary primary or secondary code:

1. Total regular PAYE income payments in the 4 weeks ending on the payment date, including that date but excluding all extra pays. Annualise by 13 for weekly, fortnightly or four-weekly payments and by 12 for monthly payments. An off-cycle extra payment still uses a window ending on its actual payment date. No regular payment in that window means a zero historical amount, not an assumed annual salary. Where only one prior pay period exists, use its pay amount annualised for its frequency. [S2, section 5.11][S2], [S22]
2. For a secondary code, add the low threshold below to that annualised amount. Add zero for a primary code. Call this combined amount **B**. Add the extra pay **E** to B and truncate that grossed-up total to whole dollars **G** solely to select the tax band. Retain cents in E and B for the deduction and levy calculations. [S2, sections 5.11.1–5.11.2][S2]
3. Select the income-tax rate below, or the employee's valid election for a higher permitted rate. Multiply the **whole extra payment**, with its cents, by that single rate. This is withholding on the extra pay, not a progressive allocation of the extra pay amongst annual bands. Do not truncate that tax component before adding the levy. [S2, section 5.11][S2], [S22]

| Secondary code, with or without SL | Amount added to annualised income |
|---|---:|
| SB | $0 |
| S | $15,601 |
| SH | $53,501 |
| ST | $78,101 |
| SA | $180,001 |

| Whole-dollar G | Income-tax rate, excluding ACC |
|---|---:|
| Up to $15,600 | 10.5% |
| $15,601–$53,500 | 17.5% |
| $53,501–$78,100 | 30% |
| $78,101–$180,000 | 33% |
| Above $180,000 | 39% |

Sources: [S22], [S24] and [S2, section 5.11][S2]. The web tables explicitly include the first dollar of each band. Do not copy the specification's inconsistent 'greater than $15,601/$53,501/$78,101' wording and leave those boundary amounts unassigned. An employee can elect a higher 17.5%, 30%, 33% or 39% income-tax rate where applicable; establish the instruction before using it. [S2, section 5.11][S2]

Calculate ACC separately. For an ordinary levy-liable extra payment, the levy base is the lesser of E and the positive amount remaining from **$156,641 minus B**. Multiply that base by **1.75%**. Thus a payment crossing the cap has levy only on the part below the cap; do not simply levy all or none because G crosses it. Redundancy payments, retiring allowances and ESS benefits are not liable for this earners' levy; establishing an ESS benefit's other treatment is outside this guide. Add the unrounded income-tax and levy components, then truncate the total to cents. These are the specified withholding calculations; they do not determine the employee's final multi-employer annual ACC position. [S2, sections 5.11–5.12][S2], [S22], [S24]

For a tailored code, follow the certificate rather than the table. For a confirmed redundancy payment or retiring allowance, remove the earners' levy included in that rate and mark the earnings as not liable for ACC on the employment information. For example, a 24% certificate rate less the 2026-27 levy of 1.75 percentage points is **22.25%**. The specification's printed 22.58% example is an arithmetic error; do not use it. Resolve the actual certificate and payment classification before applying this adjustment. [S2, section 5.11, PDF pages 45 and 51][S2], [S22]

### Extra pay when employment ends

For payments arising from the end of employment, use the **last 2 paid regular pay periods before the period containing the extra payment**, excluding other extra pays. Skip unpaid periods and out-of-cycle payments. Do not annualise the current termination-period wage or automatically use the last 4 calendar weeks. Total the 2 paid periods and multiply by 26 for weekly, 13 for fortnightly, 6.5 for four-weekly or 6 for monthly pay. When those 2 periods have different frequencies, annualise each at its own frequency and average the 2 annual values. With only one earlier paid period, annualise that period at its frequency. If no prior period exists, resolve the applicable employee instruction and IRD method before calculating. [S2, section 5.12, PDF pages 55–64][S2], [S24]

Add the secondary low threshold where applicable, then the extra payment, and use the same rate/levy steps above. Combine other extra pay paid together with termination extra pay for this calculation; do not calculate each under a different annualisation method. Keep each component's ACC character: a normal bonus does not become levy-exempt merely because it accompanies redundancy pay. These end-of-employment instructions apply to payments on or after 1 April 2025; the rates and levy amounts here are for 2026-27. [S2, section 5.12][S2], [S24]

### Student loans, regular bonuses and reporting

For primary M SL/ME SL extra pay, combine regular and extra taxable pay for the pay period, truncate that combined pay to whole dollars, subtract the period repayment threshold once and apply 12% to any positive excess, or the valid certificate rate. Truncate the loan deduction to cents. Do not give a second threshold if wages have already used it. When the extra pay is separate and total period pay cannot be established, apply the appropriate loan rate to the entire extra pay. Secondary SL extra pay has no ordinary threshold: truncate the relevant pay to whole dollars, apply 12% or the certificate rate and truncate to cents. Tailored codes follow the certificate's threshold instruction. Keep PAYE and loan deductions separate. [S2, sections 5.11–5.12][S2], [S23]

Regular incentive/production bonuses paid with normal wages are included in normal period pay. For a monthly bonus covering several pay periods, calculate monthly PAYE on that month's wages with and without the bonus and deduct the difference. For a bonus covering several months, divide it by those months, calculate the difference between monthly PAYE with and without that monthly share, then multiply the difference by the number of months. Apply the corresponding loan method for an SL code. This is the regular-bonus method, not an annual/special lump-sum rate selection. [S2, section 5.13][S2]

For an enrolled KiwiSaver employee, a confirmed redundancy payment is excluded from employee KiwiSaver deductions; do not assume the same exclusion for every other extra payment. Check the contribution base and notices separately. Report a lowest-rate extra payment using the low-rate indicator. For separate extra-pay reporting, file within 2 working days electronically or 10 working days on paper. IRD permits inclusion in the next regular electronic schedule only when reported before the relevant deduction-payment end date: month-end for monthly remitters, or the 15th/month-end for twice-monthly remitters. Record which permitted reporting route was used. [S23], [S2, section 5.11.3][S2]

### Student-loan recovery and voluntary extra deductions

Keep ordinary student-loan deductions, **SLCIR** recovery and **SLBOR** voluntary deductions separate. An IRD SLCIR notice states the amount to recover and the percentage to deduct until that amount has been reached. Use that notice, not an automatic extra 5% on every SL employee. For ordinary primary employment, the maximum recovery rate is **5% of gross pay above the pay-period repayment threshold**; for secondary employment it is **5% of gross pay without that threshold**. Truncate gross pay to whole dollars for this calculation and truncate the deduction to cents. For 2026-27 the weekly primary threshold is **$464**; use the corresponding period threshold already set out above. Do not recover more than the remaining amount required by the notice. [S2, section 3, PDF pages 9–10][S2], [S25]

A voluntary SLBOR deduction uses the employee's actual requested amount or percentage. Report ordinary loan deductions, SLCIR and SLBOR in their respective employment-information fields. These are additional loan deductions, not PAYE income tax. Keep the notice balance, effective dates, actual deduction and any cancellation or certificate change together; an SDR and its cancellation trail require the separate checks above. [S2, sections 3 and 5.9.2][S2], [S13, PDF page 22][S13]

### Employee child-support notices and protected earnings

Use the actual employee deduction notice, its start/amend/stop date, pay frequency and amount. Do not start early. Ask IRD to correct an incorrect payday or frequency rather than silently converting the notice yourself. The employee cannot instruct the employer to start or stop these deductions. The contractor/schedular-payment notice has a different payment and employment-information route; the employee instructions here do not establish that route. [S2, section 5.15][S2], [S13, PDF page 23][S13]

For the ordinary employee child-support calculation, let **G** be gross salary/wages, **P** PAYE including the employee ACC earners' levy and **A** that levy component. The protected-earnings calculation uses **N = G − (P − A)**, so its income-tax deduction excludes ACC. The normal maximum child-support deduction is **40% of N**: deduct the lesser of the notice amount and that capacity. The remaining 60% is protected for this purpose, not a guaranteed final take-home amount after student loans, ACC, KiwiSaver and other lawful deductions. Establish special payment bases separately; this formula does not resolve ESS or schedular payments. [S2, section 5.15.1, PDF pages 71–72][S2], [S13, PDF page 24 worked example][S13]

Where protected earnings prevent the full deduction, report variation **P** and the amount actually deducted. Do not make up the difference in a later pay; IRD arranges it with the employee. Other variation codes are A for advance payment, D for previously deducted, S for a short unpaid absence preventing any deduction and O for other reasons. If employment has ceased, **C takes priority even when P would otherwise apply**; record the employee finish date as well. Include employee child support in employment information and pay it with the ordinary employer deductions. Protect the employee's child-support information. [S1], [S13, PDF pages 24–25][S13]

### District Court attachment orders

Identify the statute and actual order. **Section 157 of the District Court Act 2016** governs these court attachments; **section 157 of the Tax Administration Act 1994** below is a different notice. The court order specifies the earnings period, deduction amount or percentage and minimum earnings to retain. For an ordinary District Court attachment, the protected floor is the **higher of 60% of statutory net earnings and the actual order's minimum**. Use the PAYE income-tax component for the net-earnings base, with the ACC distinction above. Confirm which payments are salary/wages for the order: the statutory definition is broader than ordinary basic pay. [S27], [S28], [S29], [S2, section 5.15.2][S2]

Section 157(3) requires the court attachment to be reduced or cancelled as necessary when it alone, or together with the listed other notices/orders, would take earnings below that floor. For a single ordinary court order with established prior deductions, its available capacity is **max(0, N − protected floor − applicable prior deductions)**; deduct the lesser of that capacity and the amount required by the order. Child support has priority. Section 157(2) also makes the ordinary court charge subject to the specified Family Proceedings/Summary Proceedings attachments and statutory deduction notices. Do not invent priority amongst competing orders or reduce a different statutory notice merely by applying this court formula; obtain the actual instruments and resolve their priority with the issuer/court or IRD. [S27], [S13, PDF page 23][S13]

The specification's page 72 step 5 prints the full other-attachment amount even when it exceeds remaining capacity. That instruction conflicts with section 157(3)'s protection. Apply the statutory reduction instead of copying the printed branch. The worked checks below assume the stated order, base and prior deductions are already valid; they do not determine every competing-notice combination. [S27], [S2, PDF page 72][S2]

### IRD tax-arrears notices

A Tax Administration Act section 157 notice for salary/wage arrears is separate from a student-loan SLCIR recovery notice. Obtain its required amount, instalment period, initial notified debt, payment deadline, tax reference and any notified interest. For the ordinary statutory salary/wage ceiling, compare **10% per week of the debt due at the notice date** with **20% of gross salary/wages payable**. Take the lesser, then compare it with **$10 per week** and take the greater. For non-weekly pay, scale the weekly debt instalment and minimum to the pay period; the 20% limb already uses that period's actual gross pay. This is a ceiling, not an instruction to deduct it when the actual notice requires less. Limit the deduction to the amount actually payable and required under the notice. [S30, subsections (1)–(3)][S30], [S26], [S32, paragraphs 26–28][S32]

IRD's SPS 21/01 says no extra deduction is required where weekly earnings are **less than $10**. It also addresses an employee request for a higher deduction. Follow the applicable notice and actual request; resolve an apparent conflict with IRD rather than creating a deduction that exceeds the wages available. The specification's page 75 flowchart shortcut of $10 when weekly gross is below $100 does not reproduce the general statutory formula: for example, 20% of $80 is $16. Other fixed-amount notices may be issued. [S32, paragraphs 27–28][S32], [S2, section 5.17][S2]

Child-support arrears use a different notice and calculation, and child support takes priority over other tax arrears. Check that actual instrument separately; the ordinary employee child-support formula above does not establish all arrears or contractor cases. Do not merge different notices into one generic 40% cap. [S26], [S32, paragraphs 29–30][S32]

Do not put these tax-arrears deductions in employment information or the SLCIR field. Pay them separately from PAYE using the employee's IRD number, tax type, period and amount. The general payroll instructions say by calendar month-end; the Act and SPS require payment within the time in the actual notice, so establish that deadline before processing. Notify the employee of the deduction and its purpose. The amount withheld is held in trust for the Crown. Keep the notice until the required amount is paid or IRD changes/revokes it in writing; the employee cannot cancel it. [S2, section 5.17][S2], [S26], [S30, subsections (1), (4), (6) and (8)][S30], [S32, paragraphs 33–36][S32]

## Section 3 -- KiwiSaver from 1 April 2026

For ordinary post-2009 default cases, the employee deduction and minimum compulsory employer contribution increased from 3% to **3.5% for paydays on or after 1 April 2026**. The payday determines the rate for the whole payment when a period straddles 1 April; do not prorate by days worked. A surviving historical 4% employee default is addressed below. Existing valid elections of 4%, 6%, 8% or 10% remain available. [S7], [S45, subsection (3B)][S45], [S50, subsection (4B)][S50]

### Establish membership and automatic-enrolment eligibility

Membership, automatic enrolment and compulsory employer-contribution eligibility are separate questions. For the ordinary case, establish that the person normally lives in New Zealand and is a citizen or entitled to remain indefinitely, and that the employer is within the Act. A temporary visitor, student or work permit does not establish indefinite entitlement. The State services overseas exception and other cross-border cases need their own checks. [S41], [KS4, PDF page 6][S33]

Automatic enrolment ordinarily concerns a new employee aged **18 or older and under 65** at the start of employment, with a non-exempt employer and no applicable exception. It does not automatically enrol a 16- or 17-year-old. An under-18 person joins through a provider; an existing member supplies their membership and deduction information rather than being enrolled again. Membership can continue beyond 65 even where compulsory employer contributions cease. [S42], [S44], [KS4, PDF pages 6–11][S33]

Check the exceptions before treating any new starter as automatically enrolled. A contract for no more than 28 continuous days is temporary for this purpose; count calendar days of employment, not shifts. If that employment continues, the temporary exclusion ends on day 29, described in section 12(2)(b) as the 28th day after employment started. Casual agricultural employment and qualifying irregular/intermittent employment with holiday pay have separate statutory tests. Section 14 also excludes existing members and specified situations such as private domestic service, election-day work and employment without required PAYE withholding. This is not an exhaustive classification checklist; resolve the actual section 12/14 exception, secondment or exempt-employer status first. [S43], [S44], [KS4, PDF page 7][S33]

Give a person who is automatically enrolled the KiwiSaver information pack within **7 days** of starting. Collect the applicable KS2 deduction information and retain it; do not send KS2 to IRD. Give IRD the applicable new-employee KiwiSaver details using IR346K/myIR or payroll software no later than the first employment-information return is due. Coordinate this with the separate new-employee information deadline in Section 5. Start required deductions from the first payment for an automatically enrolled employee; for an existing member or an IRD direction, section 60 applies to payments calculated after the employer receives the relevant notice. Obtain a valid savings-suspension notice before omitting otherwise required deductions. [S34], [S35], [S49], [KS4, PDF pages 8–11][S33]

### Employee rates, changes and temporary reductions

Use the valid KS2, written rate instruction or IRD notice. The ordinary elected choices are **3.5%, 4%, 6%, 8% and 10%** of KiwiSaver gross salary or wages. Apply a valid change to the first payment calculated after receipt; ordinary changes must be at least **92 days** apart unless the employer agrees to a shorter interval. Do not backdate missed employee deductions when acting on IRD's start instruction. A possible employer-contribution arrears obligation is a separate question and is not cancelled by that employee-deduction instruction. [S8], [S45, subsections (2)–(4)][S45], [KS4, PDF page 14][S33]

Do not assume every employee without a new election defaults to 3.5%. Section 64(1)(ab) retains a **4% default** where section 60(1)(a), (b) or (c) first applied to this employer in respect of this employee before 1 April 2009, subject to the statutory alternatives and any overriding election or valid temporary reduction. Section 64(1)(a) also preserves separate treatment for former section 66A transitional cases and certain pre-April-2013 2% elections. Check historical employment and rate records; the member's original joining date alone does not establish a legacy 4% case. The general IRD web/KS4 default summaries omit this surviving statutory limb. [S45, subsections (1)–(2)][S45], [S49]

A valid IRD temporary rate reduction permits **3%**. The requested approval period must be **at least 92 days and no more than 1 year**; further reductions can follow. Use the actual approval's start/end dates and the notice for the relevant employer, rather than treating one employer's notification as an instruction for every job. Track expiry and any renewed approval. A person cannot use a temporary reduction whilst on a savings suspension. An informal request does not replace approval. [S39], [S46], [S47]

An employee may revoke the temporary reduction for an employer and resume the applicable ordinary/default/elected rate. Using it for fewer than **92 days requires that employer's agreement**. Retain that agreement; a request alone does not prove consent. The payroll specification's PDF page 13 sample letter says a reduction cannot end in its first 3 months, but omits the statutory agreement exception. Follow section 101S and the consistent KS4 instruction rather than implementing an absolute ban. A later reduction for that employer requires a new application. [S48], [S39], [KS4, PDF page 18][S33]

### Identify the contribution base

Classify each payment before applying a rate. The following are selected ordinary inclusions/exclusions, not a complete ruling on an actual payment. [S38], [KS4, PDF page 12][S33], [S2, section 4.5][S2]

| Payment already correctly classified | KiwiSaver gross salary or wages | Complying-fund gross base salary or wages |
|---|---|---|
| Ordinary salary, wages and overtime | Included | Included, subject to the fund's applicable definition |
| Bonus and commission | Included | Excluded |
| Redundancy payment | Excluded | Excluded |
| Board/lodging, use of a house or an allowance instead | Excluded | Excluded |
| Overseas accommodation/living-cost allowance or reimbursement within the stated exclusion | Excluded | Excluded |
| Qualifying voluntary bonding payment or employee-share-scheme shares within the stated exclusion | Excluded | Excluded |

Check the complying fund's trust deed for other excluded amounts. KiwiSaver also excludes the specified Fire and Emergency New Zealand volunteer honoraria. Keep evidence supporting an exclusion. These exclusions do not determine PAYE, FBT, ESS, employment-law or cross-border treatment. For a person contributing to both KiwiSaver and a complying fund, establish each employee deduction rate and its own base; do not silently reuse one base for both. [S38], [KS4, PDF pages 12 and 23][S33]

### Compulsory employer contributions

The ordinary minimum is 3.5% of qualifying gross salary or wages for an eligible contributing member. From 1 April 2026 this includes eligible **16- and 17-year-old members**. The ordinary conditions include age 16 to under 65, membership, required employee deductions and no disqualifying defined-benefit arrangement. Check the actual circumstances; membership alone does not establish liability. [S7], [S9]

If an employee has an approved temporary 3% deduction rate, the employer **may choose** the 3% employer rate; it need not reduce its contribution. Record its choice and any contract requiring more. The statutory CEC rate is otherwise 3.5%. Reaching 65 may end the statutory obligation, but an agreement or voluntary contribution can continue and ESCT may still apply. Use the applicable stop instruction and evidence rather than assuming a birthday cancels all contractual obligations. [S9], [S50, subsection (4)][S50]

For a person contributing to both a KiwiSaver scheme and a complying fund, the ordinary employer minimum is shared between the funds, not an additional 3.5% minimum for each. Establish the relevant bases and agreed allocation. Do not deduct an unrelated superannuation contribution as an automatic credit: section 101D's other-contribution and hybrid-scheme offsets have detailed scheme, employment/agreement and vesting conditions. Their application remains an actual-case check here. [S9], [S50]

Employer contributions are normally additional to salary or wages. An agreed total-remuneration arrangement needs a genuine agreement and must still satisfy minimum-wage requirements excluding the employer contribution. Do not reduce contracted pay automatically. Deduct ESCT from the gross employer contribution unless employer and employee have agreed to the separate PAYE treatment. The employee's own KiwiSaver deduction is not subject to ESCT. KiwiSaver employer contributions go through IRD; complying-fund contributions go directly to that fund. [S9], [S10]

Check whether an agreed employer contribution is gross or net of ESCT. A promised net contribution requires grossing up under IR335's method before the ordinary ESCT calculation. Reconcile the promised net after the required truncation; do not treat a contractual net percentage as the gross statutory minimum. This guide does not work a contractual gross-up example. [IR335, page 27][S13]

### Savings suspensions, ACC and leave

Require a valid savings-suspension notice and track its dates. An unsupported statement that the employee is on a suspension does not justify stopping deductions. Apply IRD's restart instruction when it ends. A suspension ordinarily stops required employee deductions and compulsory employer contributions, but an agreement or voluntary employer contribution can continue; apply the appropriate ESCT or agreed PAYE treatment. Approval eligibility, including early hardship applications, is not determined here. [S8], [S9], [S2, section 4.1][S2], [KS4, PDF page 18][S33]

If the employer continues paying under an ACC partnership programme or employer reimbursement agreement, continue employee KiwiSaver deductions unless a valid suspension applies; employer contributions in that situation are voluntary. When ACC pays weekly compensation directly, the employer can stop its own deductions and contributions. If the employer continues salary or wages during parental leave, continue required employee and employer contributions unless a valid suspension applies. This does not determine deductions from government parental-leave payments or leave entitlements. [S40], [S2, section 4.5.3][S2]

Contributions normally stop on unpaid leave, but the employer may contribute voluntarily. IRD's current instructions permit including the contribution in employment information with **zero gross earnings**, or paying a lump sum through IRD after the employee returns. ESCT still applies unless the agreed salary/wages treatment applies. For a voluntary $52.50 contribution with an established 30% ESCT rate, the whole-dollar base is $52, tax is $15.60 and the fund receives $36.90. The specification's page 19 table wrongly switches its tax base to $45; use the current dedicated web example and Section 4's algorithm. [S40], [S2, section 4.5.4][S2]

### Opt-outs and separate refund streams

Only an automatically enrolled employee can use the ordinary opt-out process. A timely request is made on **days 14 to 56 inclusive** after starting employment, using KS10. Send the request/details to IRD and stop deductions/contributions under the valid opt-out instruction. A voluntary joiner or existing member cannot use KS10 merely because they started a new job. A qualifying later withdrawal or KS51 stop instruction is a separate process. [S36], [KS4, PDF page 18][S33]

After day 56, IRD decides whether to accept a late request. Its stated window is up to 3 months **after IRD received the first contribution**, subject to its specified reasons; it is not a blanket 3-month extension from employment commencement. Continue employee deductions, employer contributions and ESCT until IRD's acceptance/stop instruction applies. Do not approve the late request yourself. [S37]

Reconcile each stream before refunding. If employee deductions have not been filed and paid to IRD, the employer may refund them and report the amounts actually deducted/retained. If they have already been sent, IRD refunds the employee; avoid a second employer refund. Reconcile mixed or partly forwarded amounts with IRD before acting. Employer contributions already sent are refunded to the employer subject to amounts owing to IRD. **ESCT is a separate refund request**, using the applicable IR344 amendment/contact route; do not assume an automatic employer-contribution refund also refunds ESCT. Retain the accepted request, filing amendments, employee refund and employer/ESCT reconciliation. [S36], [S2, section 5.21.5][S2]

The announced 4% ordinary default from 1 April 2028 is a future change, not the ordinary new-default rate for 2026-27 payroll. [S7]

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

These fictional cases assume the stated code, eligibility, contribution base and notices have already been established. They check the selected contribution, PAYE and student-loan arithmetic, not an actual person's liability. Cases 1 and 2 use the ordinary ESCT method rather than an agreed PAYE alternative. Set tolerance to zero so a cent error fails.

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

**Case 3: M monthly, annualise before dropping cents.** Confirmed ordinary M pay of $5,000.99 a month gives annual whole-dollar income $60,011. Annual tax is $10,223.80 and ACC is $1,050.1925. Weekly truncation gives $216.80, then monthly PAYE **$939.46**. Direct annual-to-monthly truncation would give $939.49 and skips the required weekly step. [S2, section 5.2][S2]

```oa-check
name: nz-2026-m-monthly-two-stage-truncation
tolerance: 0
inputs:
  period_pay: 5000.99
  pays: 12
steps:
  annual_income: floor(period_pay * pays)
  annual_tax: pct(annual_income, 30) - 7779.50
  annual_acc: pct(annual_income, 1.75)
  weekly_paye: floor((annual_tax + annual_acc) / 52 * 100) / 100
  period_paye: floor(weekly_paye * 52 / pays * 100) / 100
expected:
  annual_income: 60011
  annual_tax: 10223.80
  annual_acc: 1050.1925
  weekly_paye: 216.80
  period_paye: 939.46
```

**Case 4: M monthly with capped ACC.** Confirmed ordinary M pay of $15,000 a month annualises to $180,000. The annual ACC component is the stated **$2,741.22** maximum. PAYE including that component is **$4,334.89** a month. [S2, section 5.2][S2]

```oa-check
name: nz-2026-m-monthly-capped-acc
tolerance: 0
inputs:
  period_pay: 15000
  pays: 12
  annual_acc_cap: 2741.22
steps:
  annual_income: floor(period_pay * pays)
  annual_tax: pct(annual_income, 33) - 10122.50
  weekly_paye: floor((annual_tax + annual_acc_cap) / 52 * 100) / 100
  period_paye: floor(weekly_paye * 52 / pays * 100) / 100
expected:
  annual_income: 180000
  annual_tax: 49277.50
  weekly_paye: 1000.36
  period_paye: 4334.89
```

**Case 5: ME weekly with IETC abatement.** An employee with a confirmed ME declaration and IETC eligibility earns $1,300 weekly. Annualised income is $67,600, so the payroll credit is **$312** after abatement. Weekly PAYE including ACC and that credit is **$257.14**. This example assumes eligibility; salary alone does not establish it. [S2, section 5.3][S2], [S18]

```oa-check
name: nz-2026-me-weekly-ietc-abatement
tolerance: 0
inputs:
  period_pay: 1300
  pays: 52
steps:
  annual_income: floor(period_pay * pays)
  annual_tax: pct(annual_income, 30) - 7779.50
  annual_acc: pct(annual_income, 1.75)
  annual_credit: 520 - pct(annual_income - 66000, 13)
  period_paye: floor((annual_tax + annual_acc - annual_credit) / 52 * 100) / 100
expected:
  annual_income: 67600
  annual_tax: 12500.50
  annual_acc: 1183
  annual_credit: 312
  period_paye: 257.14
```

**Case 6: primary monthly SL near the threshold.** Ordinary M SL monthly gross pay of $2,011.99 becomes $2,011 for the loan calculation. Subtracting the **$2,010.66** threshold leaves $0.34; 12% truncated to cents is **$0.04**. There is no exemption or special-rate notice in this example. [S2, section 5.4][S2]

```oa-check
name: nz-2026-primary-sl-monthly-threshold
tolerance: 0
inputs:
  period_pay: 2011.99
  threshold: 2010.66
steps:
  loan_pay: floor(period_pay)
  loan_deduction: floor(pct(max(loan_pay - threshold, 0), 12) * 100) / 100
expected:
  loan_pay: 2011
  loan_deduction: 0.04
```

**Case 7: primary weekly SL with no positive excess.** Ordinary M SL weekly pay of $464.99 becomes $464, matching the threshold, so the loan deduction is **$0.00**. [S2, section 5.4][S2]

```oa-check
name: nz-2026-primary-sl-weekly-no-excess
tolerance: 0
inputs:
  period_pay: 464.99
  threshold: 464
steps:
  loan_pay: floor(period_pay)
  loan_deduction: floor(pct(max(loan_pay - threshold, 0), 12) * 100) / 100
expected:
  loan_pay: 464
  loan_deduction: 0
```

**Case 8: secondary SH SL has no ordinary loan threshold.** An employee's declared total annual income is $75,000 and the confirmed code for this second job is SH SL. Ordinary weekly pay of $300.99 becomes $300 for these calculations. PAYE including ACC is **$95.25** and the separate loan deduction is **$36.00**. Being below the main-job weekly threshold does not make this secondary loan deduction zero. No special rate or exemption applies here. [S2, section 5.6][S2], [S21]

```oa-check
name: nz-2026-secondary-sh-sl-no-threshold
tolerance: 0
inputs:
  period_pay: 300.99
steps:
  whole_pay: floor(period_pay)
  period_paye: floor(pct(whole_pay, 31.75) * 100) / 100
  loan_deduction: floor(pct(whole_pay, 12) * 100) / 100
expected:
  whole_pay: 300
  period_paye: 95.25
  loan_deduction: 36
```

**Case 9: ordinary ND includes ACC.** Without a completed declaration or superseding Inland Revenue instruction, ordinary ND pay of $457.89 becomes $457. The combined 46.75% deduction truncates to **$213.64**; adding ACC again overstates the deduction. [S2, section 5.8][S2]

```oa-check
name: nz-2026-nd-whole-dollar-pay
tolerance: 0
inputs:
  period_pay: 457.89
steps:
  whole_pay: floor(period_pay)
  period_paye: floor(pct(whole_pay, 46.75) * 100) / 100
expected:
  whole_pay: 457
  period_paye: 213.64
```

**Case 10: main-job tailored certificate.** Assume a valid weekly certificate requires 20% PAYE including ACC and 8% loan deductions above $464. On $1,000.99, use the $1,000 whole-dollar base: **$200.00 PAYE** and a separate **$42.88 loan deduction**. [S2, section 5.9][S2]

```oa-check
name: nz-2026-stc-primary
tolerance: 0
inputs:
  pay: 1000.99
  paye_rate: 20
  sl_rate: 8
  threshold: 464
steps:
  base: floor(pay)
  paye: floor(pct(base, paye_rate) * 100) / 100
  loan: floor(pct(base - threshold, sl_rate) * 100) / 100
expected:
  paye: 200
  loan: 42.88
```

**Case 11: secondary certificate has no threshold.** Assume a valid secondary certificate requires 18% PAYE including ACC and 8% loan deductions on every dollar. Weekly pay of $300.99 gives **$54.00 PAYE** and **$24.00 loan deductions** on $300. Do not subtract the primary $464 threshold. [S2, section 5.9][S2]

```oa-check
name: nz-2026-stc-secondary
tolerance: 0
inputs:
  pay: 300.99
  paye_rate: 18
  sl_rate: 8
steps:
  base: floor(pay)
  paye: floor(pct(base, paye_rate) * 100) / 100
  loan: floor(pct(base, sl_rate) * 100) / 100
expected:
  paye: 54
  loan: 24
```

**Case 12: one loan threshold for combined pay.** An M SL employee receives $400 regular weekly pay and $200.99 extra pay together. Combined pay truncates to $600; subtract $464 once. The total loan deduction for this pay is **$16.32**. No special certificate applies. [S2, section 5.11][S2], [S23]

```oa-check
name: nz-2026-extra-pay-single-sl-threshold
tolerance: 0
inputs:
  wages: 400
  extra: 200.99
  threshold: 464
  sl_rate: 12
steps:
  base: floor(wages + extra)
  loan: floor(pct(base - threshold, sl_rate) * 100) / 100
expected:
  base: 600
  loan: 16.32
```

**Case 13: bonus crosses the ACC cap.** An ordinary primary-code bonus of $30,000.56 follows $10,000 of regular payments in the relevant 4-week window. Annualised pay is $130,000; G is $160,000, selecting 33%. Only $26,641 of the bonus attracts 1.75% ACC. Retain $9,900.1848 tax and $466.2175 levy until the final cent truncation: **$10,366.40 PAYE**. The specification example prints $10,366.39 after prematurely shortening components; this case follows its explicit calculation sequence. [S2, section 5.11.1, PDF pages 47–48][S2], [S22]

```oa-check
name: nz-2026-bonus-crosses-acc-cap
tolerance: 0
inputs:
  prior_four_weeks: 10000
  extra: 30000.56
  cap: 156641
  tax_rate: 33
  levy_rate: 1.75
steps:
  annual: prior_four_weeks * 13
  grossed: floor(annual + extra)
  levy_base: cap - annual
  income_tax: pct(extra, tax_rate)
  levy: pct(levy_base, levy_rate)
  paye: floor((income_tax + levy) * 100) / 100
expected:
  annual: 130000
  grossed: 160000
  levy_base: 26641
  paye: 10366.4
```

**Case 14: secondary threshold affects the cap.** An ST-code bonus of $40,000 follows $4,695 regular pay in the relevant 4 weeks. Annualised pay $61,035 plus the ST low threshold $78,101 gives B of $139,136 and G of $179,136. Tax is 33% of the bonus; ACC applies to only $17,505. Total PAYE is **$13,506.33**, leaving **$26,493.67** before other deductions. [S2, section 5.11.2, PDF pages 52–55][S2], [S22]

```oa-check
name: nz-2026-secondary-bonus-cap
tolerance: 0
inputs:
  prior_four_weeks: 4695
  low_threshold: 78101
  extra: 40000
  cap: 156641
  tax_rate: 33
  levy_rate: 1.75
steps:
  annual: prior_four_weeks * 13
  base: annual + low_threshold
  grossed: floor(base + extra)
  levy_base: cap - base
  paye: floor((pct(extra, tax_rate) + pct(levy_base, levy_rate)) * 100) / 100
  net_before_other_deductions: extra - paye
expected:
  base: 139136
  grossed: 179136
  levy_base: 17505
  paye: 13506.33
  net_before_other_deductions: 26493.67
```

**Case 15: signing bonus before any regular payment.** An M-code employee receives a $10,000 levy-liable signing bonus with no earlier regular pay in the window and no higher-rate election. Annualised pay is zero, so the 10.5% income-tax rate and 1.75% levy give **$1,225.00 PAYE**. Set the low-rate extra-pay indicator. A future contractual salary is not substituted for historical payments. [S2, section 5.11.1, PDF page 49][S2], [S22]

```oa-check
name: nz-2026-signing-bonus-low-rate
tolerance: 0
inputs:
  extra: 10000
  tax_rate: 10.5
  levy_rate: 1.75
steps:
  paye: floor((pct(extra, tax_rate) + pct(extra, levy_rate)) * 100) / 100
expected:
  paye: 1225
```

**Case 16: first dollar of a new extra-pay band.** With $52,000 annualised regular pay, a $1,500 primary bonus gives G of $53,500 and **$288.75 PAYE** at 17.5% plus levy. A $1,501 bonus gives G of $53,501 and **$476.56 PAYE** at 30% plus levy. The higher rate applies to the whole bonus, not just its last dollar. [S2, section 5.11][S2], [S22]

```oa-check
name: nz-2026-extra-pay-band-boundary
tolerance: 0
inputs:
  annual: 52000
  extra_lower: 1500
  extra_upper: 1501
  lower_rate: 17.5
  upper_rate: 30
  levy_rate: 1.75
steps:
  g_lower: floor(annual + extra_lower)
  g_upper: floor(annual + extra_upper)
  paye_lower: floor((pct(extra_lower, lower_rate) + pct(extra_lower, levy_rate)) * 100) / 100
  paye_upper: floor((pct(extra_upper, upper_rate) + pct(extra_upper, levy_rate)) * 100) / 100
expected:
  g_lower: 53500
  g_upper: 53501
  paye_lower: 288.75
  paye_upper: 476.56
```

**Case 17: termination skips unpaid and current periods.** The last 2 paid weekly periods before the termination period contain $550 and $650, with an intervening unpaid week. Ignore that unpaid week and the current $500 wage. A confirmed $1,000 redundancy payment gives annualised pay $31,200 and G $32,200: **$175.00 PAYE**, with no earners' levy on redundancy. [S2, section 5.12][S2], [S24]

```oa-check
name: nz-2026-termination-paid-periods
tolerance: 0
inputs:
  paid_older: 550
  paid_recent: 650
  extra: 1000
  tax_rate: 17.5
steps:
  annual: (paid_older + paid_recent) * 26
  grossed: floor(annual + extra)
  paye: floor(pct(extra, tax_rate) * 100) / 100
expected:
  annual: 31200
  grossed: 32200
  paye: 175
```

**Case 18: termination after a frequency change.** The last 2 paid periods before termination are $800 weekly and $1,720 fortnightly. Average their annualised values to get $43,160. A separate $1,000 levy-liable bonus paid because employment ends gives G of $44,160 and **$192.50 PAYE**. Assume no secondary code or higher-rate election. [S2, section 5.12, PDF page 64][S2], [S24]

```oa-check
name: nz-2026-termination-mixed-frequencies
tolerance: 0
inputs:
  weekly: 800
  fortnightly: 1720
  extra: 1000
  tax_rate: 17.5
  levy_rate: 1.75
steps:
  annual: (weekly * 52 + fortnightly * 26) / 2
  grossed: floor(annual + extra)
  paye: floor((pct(extra, tax_rate) + pct(extra, levy_rate)) * 100) / 100
expected:
  annual: 43160
  grossed: 44160
  paye: 192.5
```

**Case 19: combined termination payments keep their levy character.** The last 2 paid monthly periods before termination are $5,500 and $7,600; ignore a later unpaid month and the current termination-period wage. A confirmed $15,000 redundancy payment and $500 ordinary bonus are paid together. Annualised pay is $78,600; G $94,100 selects 33% on all $15,500. Only the $500 bonus attracts ACC: total **$5,123.75 PAYE**, leaving **$10,376.25** before other deductions. [S2, section 5.12, PDF pages 62–63][S2], [S24]

```oa-check
name: nz-2026-combined-termination-extra-pay
tolerance: 0
inputs:
  older_month: 7600
  recent_month: 5500
  redundancy: 15000
  bonus: 500
  tax_rate: 33
  levy_rate: 1.75
steps:
  annual: (older_month + recent_month) * 6
  extra: redundancy + bonus
  grossed: floor(annual + extra)
  paye: floor((pct(extra, tax_rate) + pct(bonus, levy_rate)) * 100) / 100
  net_before_other_deductions: extra - paye
expected:
  annual: 78600
  grossed: 94100
  paye: 5123.75
  net_before_other_deductions: 10376.25
```

**Case 20: remove the levy from a tailored redundancy rate.** Assume a valid 24% salary/wage certificate rate includes 1.75% ACC and the $1,000 payment is confirmed redundancy. The applicable rate excluding levy is **22.25%**, giving **$222.50**. Mark the earnings not liable for ACC. This is conditional arithmetic, not a determination that any actual payment qualifies. [S2, section 5.11][S2]

```oa-check
name: nz-2026-tailored-redundancy-levy-exclusion
tolerance: 0
inputs:
  extra: 1000
  certificate_rate: 24
  levy_rate: 1.75
steps:
  rate_excluding_levy: certificate_rate - levy_rate
  paye: floor(pct(extra, rate_excluding_levy) * 100) / 100
expected:
  rate_excluding_levy: 22.25
  paye: 222.5
```

**Case 21: regular bonus covering 3 months.** An ordinary M-code employee earns $5,000 monthly and receives a $1,200 regular bonus covering 3 months. The $400 monthly share gives monthly PAYE of $1,066.17 on $5,400 versus $939.20 on $5,000, using the weekly-first truncation method above. The bonus PAYE is **$380.91**: 3 times the $126.97 monthly difference. Assume the same facts for the covered months and no SL code, tailored certificate or other adjustment. [S2, sections 5.1 and 5.13][S2]

```oa-check
name: nz-2026-regular-bonus-multiple-months
tolerance: 0
inputs:
  monthly_wages: 5000
  bonus: 1200
  months: 3
steps:
  share: bonus / months
  annual_base: floor(monthly_wages * 12)
  annual_with: floor((monthly_wages + share) * 12)
  tax_base: pct(annual_base, 30) - 7779.50
  tax_with: pct(annual_with, 30) - 7779.50
  weekly_base: floor(((tax_base + pct(annual_base, 1.75)) / 52) * 100) / 100
  weekly_with: floor(((tax_with + pct(annual_with, 1.75)) / 52) * 100) / 100
  paye_base: floor((weekly_base * 52 / 12) * 100) / 100
  paye_with: floor((weekly_with * 52 / 12) * 100) / 100
  bonus_paye: (paye_with - paye_base) * months
expected:
  paye_base: 939.2
  paye_with: 1066.17
  bonus_paye: 380.91
```

Before release also check an exactly $50,000 electronic-filing case, an exactly $500,000 large-employer case, the December 15 January exception and a pay period straddling 1 April. A temporary 3% employee rate does not by itself force the employer to reduce its rate.

**Case 22: primary SLCIR and separate voluntary repayment.** Assume weekly M SL pay of $875.90, a valid 5% SLCIR notice with sufficient balance and a $20 SLBOR request. Whole-dollar gross is $875; ordinary SL is $49.32, SLCIR $20.55 and SLBOR $20, totalling $89.87. [S2, section 3][S2]

```oa-check
name: nz-2026-slcir-primary-separate
tolerance: 0
inputs:
  gross: 875.9
  threshold: 464
  ordinary_rate: 0.12
  recovery_rate: 0.05
  voluntary: 20
steps:
  whole: floor(gross)
  base: max(0, whole - threshold)
  ordinary: floor(base * ordinary_rate * 100) / 100
  recovery: floor(base * recovery_rate * 100) / 100
  total: ordinary + recovery + voluntary
expected:
  whole: 875
  ordinary: 49.32
  recovery: 20.55
  total: 89.87
```

**Case 23: primary recovery below the threshold.** Weekly M SL pay of $425.35 is below $464. Assume no different certificate: ordinary SL and SLCIR are zero. [S2, section 3][S2]

```oa-check
name: nz-2026-slcir-below-threshold
tolerance: 0
inputs:
  gross: 425.35
  threshold: 464
steps:
  base: max(0, floor(gross) - threshold)
  ordinary: floor(base * 0.12 * 100) / 100
  recovery: floor(base * 0.05 * 100) / 100
expected:
  base: 0
  ordinary: 0
  recovery: 0
```

**Case 24: secondary recovery has no ordinary threshold.** Assume $300.99 secondary SL pay and a valid 5% recovery notice with sufficient balance. On $300 whole-dollar gross, ordinary SL is $36 and SLCIR $15. [S2, section 3][S2]

```oa-check
name: nz-2026-slcir-secondary
tolerance: 0
inputs:
  gross: 300.99
steps:
  whole: floor(gross)
  ordinary: floor(whole * 0.12 * 100) / 100
  recovery: floor(whole * 0.05 * 100) / 100
  total: ordinary + recovery
expected:
  ordinary: 36
  recovery: 15
  total: 51
```

**Case 25: use the actual recovery percentage.** Assume weekly M SL pay of $900 and a valid notice requiring 3% above $464. Ordinary SL is $52.32 and recovery $13.08, not an assumed 5% deduction. [S2, section 3][S2]

```oa-check
name: nz-2026-slcir-actual-rate
tolerance: 0
inputs:
  gross: 900
  threshold: 464
  notice_rate: 0.03
steps:
  base: max(0, floor(gross) - threshold)
  ordinary: floor(base * 0.12 * 100) / 100
  recovery: floor(base * notice_rate * 100) / 100
  total: ordinary + recovery
expected:
  ordinary: 52.32
  recovery: 13.08
  total: 65.4
```

**Case 26: stop at the required recovery balance.** Assume the first case has only $7 left to recover under the notice. Deduct $7 SLCIR and reconcile the completed recovery amount; do not take $20.55. [S2, section 3][S2]

```oa-check
name: nz-2026-slcir-final-balance
tolerance: 0
inputs:
  gross: 875.9
  threshold: 464
  remaining: 7
steps:
  calculated: floor(max(0, floor(gross) - threshold) * 0.05 * 100) / 100
  recovery: min(calculated, remaining)
  balance: remaining - recovery
expected:
  calculated: 20.55
  recovery: 7
  balance: 0
```

**Case 27: child support protects the tax-only net base.** Assume ordinary weekly pay $600, PAYE including ACC $94.50, its ACC component $10.50, a $230 employee child-support notice, ordinary SL $16.32 and an eligible 3.5% KiwiSaver deduction. N is $516 and child support is $206.40. Take-home after those stated deductions is $261.78; the 60% child-support protection is not a final take-home guarantee. [S13, PDF page 24][S13], [S8]

```oa-check
name: nz-2026-child-support-tax-only-base
tolerance: 0
inputs:
  gross: 600
  paye: 94.5
  acc: 10.5
  notice: 230
  student: 16.32
  kiwi_rate: 0.035
steps:
  income_tax: paye - acc
  net_base: gross - income_tax
  capacity: net_base * 0.40
  support: min(notice, capacity)
  kiwi: gross * kiwi_rate
  takehome: gross - paye - support - student - kiwi
expected:
  net_base: 516
  support: 206.4
  kiwi: 21
  takehome: 261.78
```

**Case 28: reduce the ordinary court attachment.** Assume N=$516, prior valid child support $120 and a single ordinary court order requesting $100 with no higher minimum. The remaining court capacity is $86.40, so the court deduction must be reduced. [S27]

```oa-check
name: nz-2026-court-residual-capacity
tolerance: 0
inputs:
  net_base: 516
  child_support: 120
  requested: 100
  notice_floor: 0
steps:
  floor: max(net_base * 0.60, notice_floor)
  capacity: max(0, net_base - floor - child_support)
  court: min(requested, capacity)
expected:
  floor: 309.6
  capacity: 86.4
  court: 86.4
```

**Case 29: the order can specify a higher protected minimum.** Assume N=$500, an actual court minimum of $400, prior valid child support $80 and an ordinary court request of $100. Court capacity is $20. [S27], [S28]

```oa-check
name: nz-2026-court-higher-minimum
tolerance: 0
inputs:
  net_base: 500
  notice_floor: 400
  child_support: 80
  requested: 100
steps:
  floor: max(net_base * 0.60, notice_floor)
  capacity: max(0, net_base - floor - child_support)
  court: min(requested, capacity)
expected:
  floor: 400
  capacity: 20
  court: 20
```

**Case 30: court capacity cannot be negative.** Assume N=$300 and a court-order minimum of $350. The ordinary court request of $100 reduces to zero, rather than producing a negative deduction. [S27]

```oa-check
name: nz-2026-court-zero-capacity
tolerance: 0
inputs:
  net_base: 300
  notice_floor: 350
  requested: 100
steps:
  floor: max(net_base * 0.60, notice_floor)
  capacity: max(0, net_base - floor)
  court: min(requested, capacity)
expected:
  floor: 350
  capacity: 0
  court: 0
```

**Case 31: ordinary weekly arrears ceiling.** Assume a valid income-tax arrears notice with initial debt $3,000 requires the standard salary/wage formula, with sufficient balance. On weekly gross $900, the ceiling and required deduction are $180. This does not select the amount for a different actual notice. [S30], [S32, paragraph 28][S32]

```oa-check
name: nz-2026-arrears-weekly-ceiling
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 900
steps:
  debt_limb: initial_debt * 0.10
  wage_limb: gross * 0.20
  ceiling: max(10, min(debt_limb, wage_limb))
expected:
  debt_limb: 300
  wage_limb: 180
  ceiling: 180
```

**Case 32: low pay does not automatically mean a $10 deduction.** Under the same assumed standard notice and sufficient balance, weekly gross $80 gives a $16 ceiling and deduction. Do not copy the specification flowchart shortcut. [S30], [S32, paragraphs 26–27][S32]

```oa-check
name: nz-2026-arrears-low-pay-sixteen
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 80
steps:
  ceiling: max(10, min(initial_debt * 0.10, gross * 0.20))
expected:
  ceiling: 16
```

**Case 33: the weekly minimum limb.** Assume the standard notice, sufficient balance and weekly gross $30. The lesser percentage limb is $6, so the weekly minimum limb gives $10. [S30], [S32, paragraph 27.2][S32]

```oa-check
name: nz-2026-arrears-weekly-minimum
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 30
steps:
  lesser: min(initial_debt * 0.10, gross * 0.20)
  ceiling: max(10, lesser)
expected:
  lesser: 6
  ceiling: 10
```

**Case 34: reconcile the remaining amount required.** Assume weekly gross $900 and a fixed arrears instalment of $40, but only $5 remains required under the actual notice and no further notified interest is due. The deduction is $5, not a fresh $40 or $180 ceiling. [S30, subsection (1)][S30]

```oa-check
name: nz-2026-arrears-final-amount
tolerance: 0
inputs:
  gross: 900
  initial_debt: 3000
  notice: 40
  remaining_required: 5
steps:
  ceiling: max(10, min(initial_debt * 0.10, gross * 0.20))
  deduction: min(notice, ceiling, remaining_required, gross)
expected:
  ceiling: 180
  deduction: 5
```

**Case 35: a ceiling does not replace a lower notice amount.** Assume weekly gross $900, initial debt $3,000 and a valid fixed notice requiring $40, with sufficient balance. The standard ceiling is $180; the actual required deduction remains $40. [S30, subsections (1)–(3)][S30]

```oa-check
name: nz-2026-arrears-actual-notice
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 900
  notice: 40
steps:
  ceiling: max(10, min(initial_debt * 0.10, gross * 0.20))
  deduction: min(notice, ceiling)
expected:
  ceiling: 180
  deduction: 40
```

**Case 36: scale weekly limbs once for fortnightly pay.** Assume fortnightly gross $1,800, initial debt $3,000 and the standard notice with sufficient balance. Scale the weekly debt limb and $10 minimum by 2; the 20% limb already applies to fortnightly gross. The ceiling is $360. [S32, paragraph 27.1][S32], [S30]

```oa-check
name: nz-2026-arrears-fortnightly
tolerance: 0
inputs:
  initial_debt: 3000
  gross: 1800
  weeks: 2
steps:
  debt_limb: initial_debt * 0.10 * weeks
  wage_limb: gross * 0.20
  minimum: 10 * weeks
  ceiling: max(minimum, min(debt_limb, wage_limb))
expected:
  debt_limb: 600
  wage_limb: 360
  minimum: 20
  ceiling: 360
```

**Case 37: different contribution bases.** Assume $1,000 ordinary wages, $50 overtime, $200 bonus, $100 commission, $300 redundancy and $100 accommodation all validly classified as above. At a stated 3.5% employee rate, the KiwiSaver base is $1,350 and the complying-fund base is $1,050. The complying fund has no additional deed exclusions. These are alternative base calculations, not an instruction to enrol in both funds. [S38], [S33]

```oa-check
name: nz-2026-kiwisaver-distinct-bases
tolerance: 0
inputs:
  ordinary: 1000
  overtime: 50
  bonus: 200
  commission: 100
  redundancy: 300
  accommodation: 100
  rate: 0.035
steps:
  total_pay: ordinary + overtime + bonus + commission + redundancy + accommodation
  kiwisaver_base: total_pay - redundancy - accommodation
  complying_base: kiwisaver_base - bonus - commission
  kiwisaver_deduction: pct(kiwisaver_base, rate)
  complying_deduction: pct(complying_base, rate)
expected:
  total_pay: 1750
  kiwisaver_base: 1350
  complying_base: 1050
  kiwisaver_deduction: 47.25
  complying_deduction: 36.75
```

**Case 38: established historical default.** Assume records establish a surviving section 64(1)(ab) case for this employer/employee, with no overriding election or temporary reduction. The $1,000 KiwiSaver base produces a $40 employee deduction, not $35. The example does not infer eligibility from a joining date alone. [S45], [S49]

```oa-check
name: nz-2026-kiwisaver-legacy-default
tolerance: 0
inputs:
  base: 1000
  rate: 0.04
steps:
  employee: pct(base, rate)
expected:
  employee: 40
```

**Case 39: valid election overrides the legacy default.** For the same established historical case, assume the employer has received a valid election of 3.5% applying to this calculated payment. On a $1,000 base, deduct $35. [S45, subsections (2)–(3)][S45]

```oa-check
name: nz-2026-kiwisaver-legacy-election
tolerance: 0
inputs:
  base: 1000
  rate: 0.035
steps:
  employee: pct(base, rate)
expected:
  employee: 35
```

**Case 40: temporary reduction with unchanged employer rate.** Assume an approved 3% employee reduction applies and the employer retains 3.5%, with a shared $1,000 base and an established 17.5% ESCT rate. Employee $30, gross employer $35, ESCT $6.12 and net employer $28.88 remain separate amounts. [S9], [S50], [S12]

```oa-check
name: nz-2026-kiwisaver-trr-employer-unchanged
tolerance: 0
inputs:
  base: 1000
  employee_rate: 0.03
  employer_rate: 0.035
  esct_rate: 0.175
steps:
  employee: pct(base, employee_rate)
  employer_gross: pct(base, employer_rate)
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employee: 30
  employer_gross: 35
  esct: 6.12
  employer_net: 28.88
```

**Case 41: employer chooses the permitted reduced rate.** Assume the same valid temporary reduction and base, but the employer chooses 3% and no agreement requires more. At 17.5% ESCT, gross employer $30 becomes $24.75 net after $5.25 ESCT. [S50], [S12]

```oa-check
name: nz-2026-kiwisaver-trr-employer-reduced
tolerance: 0
inputs:
  base: 1000
  employer_rate: 0.03
  esct_rate: 0.175
steps:
  employer_gross: pct(base, employer_rate)
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employer_gross: 30
  esct: 5.25
  employer_net: 24.75
```

**Case 42: shared employer minimum across 2 funds.** Assume both funds qualify, each relevant base is $1,000, the ordinary minimum is 3.5% and a valid allocation contributes 2.5% to one fund and 1% to the other. Gross contributions of $25 and $10 meet the $35 aggregate minimum. This does not establish the employee deduction rates or any legacy offset. [S9], [S50]

```oa-check
name: nz-2026-kiwisaver-two-fund-minimum
tolerance: 0
inputs:
  base: 1000
  minimum_rate: 0.035
  first_rate: 0.025
  second_rate: 0.01
steps:
  minimum: pct(base, minimum_rate)
  first: pct(base, first_rate)
  second: pct(base, second_rate)
  total: first + second
  shortfall: max(0, minimum - total)
expected:
  minimum: 35
  first: 25
  second: 10
  total: 35
  shortfall: 0
```

**Case 43: voluntary unpaid-leave contribution.** Assume zero actual wages, a voluntary employer contribution of 3.5% of usual weekly pay of $1,500 and an established 30% ESCT rate. The $52.50 contribution uses a $52 ESCT base, producing $15.60 tax and $36.90 net. Usual pay is not reported as actual gross earnings. [S40], [S12]

```oa-check
name: nz-2026-kiwisaver-unpaid-leave
tolerance: 0
inputs:
  usual_pay: 1500
  contribution_rate: 0.035
  esct_rate: 0.3
steps:
  employer_gross: pct(usual_pay, contribution_rate)
  esct_base: floor(employer_gross)
  esct: floor(esct_base * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employer_gross: 52.5
  esct_base: 52
  esct: 15.6
  employer_net: 36.9
```

**Case 44: voluntary employer contribution during a suspension.** Assume an approved suspension stops required employee deductions and the employer voluntarily contributes $30. With an established 17.5% ESCT rate and no agreed PAYE treatment, tax is $5.25 and net employer contribution $24.75. Suspension does not make the voluntary contribution tax free. [S9], [S33], [S12]

```oa-check
name: nz-2026-kiwisaver-suspension-voluntary
tolerance: 0
inputs:
  employer_gross: 30
  esct_rate: 0.175
steps:
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  esct: 5.25
  employer_net: 24.75
```

**Case 45: unforwarded employee deductions refunded once.** Assume a valid timely opt-out and 2 employee deductions of $35 each, neither filed nor paid to IRD. An employer refund of $70 clears this employee-deduction balance. It does not give the employee the employer contribution or ESCT. [S36]

```oa-check
name: nz-2026-kiwisaver-optout-unforwarded
tolerance: 0
inputs:
  first: 35
  second: 35
  refund: 70
steps:
  held: first + second
  remaining: held - refund
expected:
  held: 70
  remaining: 0
```

**Case 46: reconcile employer contribution and ESCT separately.** Assume an accepted opt-out and 2 previously remitted gross employer contributions of $35, each with $6.12 ESCT and $28.88 net to the fund. The employer-side gross total $70 reconciles to $57.76 fund contributions plus $12.24 ESCT. These are separate refund/amendment streams, subject to IRD processing and debts; they are not an employee refund and no automatic ESCT refund is assumed. [S36], [S12]

```oa-check
name: nz-2026-kiwisaver-optout-employer-streams
tolerance: 0
inputs:
  count: 2
  per_contribution: 35
  per_esct: 6.12
  per_net: 28.88
steps:
  gross_total: count * per_contribution
  fund_total: count * per_net
  esct_total: count * per_esct
  reconciled: fund_total + esct_total
expected:
  gross_total: 70
  fund_total: 57.76
  esct_total: 12.24
  reconciled: 70
```

## Section 7 -- Limits and sources

Still requiring separate actual-case checks: special PAYE codes beyond the selected certificate/extra-pay methods; exemption eligibility, recovery notices beyond the selected methods, other irregular pays and unresolved competing-notice/attachment cases; ESS, schedular payments and payment classification; enrolment exceptions and mixed/late refund cases beyond the selected administration; historical-rate evidence, contribution classifications and legacy scheme offsets; cross-border employment and treaty/social-security questions; FBT; leave, holiday pay, minimum wage and termination entitlements; employer ACC invoices; records retention and penalties. No whole payroll, social-contribution or compliance topic is certified complete by this guide. It remains tier 2 and pending qualified review.

Sources checked 12 November 2026. Selected District Court Act sections use the current copy dated 17 February 2026; Tax Administration Act section 157 uses the current copy dated 1 October 2026. SPS 21/01 is dated 12 April 2021 and remains linked by IRD's arrears page updated 16 April 2026. Extra-pay and deduction examples are recalculated from the stated rules; known inconsistent printed examples and boundary wording are recorded in the verification log. The technical specification is dated 24 March 2026, version 1.0, and expressly covers 1 April 2026 to 31 March 2027. IR335's cover says September 2026. KS4's cover says April 2026. Selected KiwiSaver Act provisions use the current copy dated 1 April 2026. The verification log records the selected native/image page scope, the surviving legacy default and conflicting sample-letter/example wording. These checks do not claim full PDF or statute review.

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

[S18]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc "ietc-eligibility"
[S19]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc/getting-the-independent-earner-tax-credit-if-you-earn-salary-or-wages "ietc-salary"
[S20]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/about-tax-codes "about-tax-codes"
[S21]: https://www.ird.govt.nz/repaying-my-student-loan-when-i-earn-salary-or-wages "student-loan-salary"

[S22]: https://www.ird.govt.nz/calculate-lump-sum-paye "Non-termination lump-sum PAYE, updated 18 May 2026"
[S23]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments "Lump-sum deductions and reporting, updated 27 January 2026"
[S24]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment "End-of-employment lump-sum PAYE, updated 20 April 2026"

[S25]: https://www.ird.govt.nz/student-loans/living-in-new-zealand-with-a-student-loan/repaying-my-student-loan-when-i-earn-salary-or-wages/student-loan-underpayments "Student-loan underpayments, updated 3 April 2024; dated specification supplies 2026-27 period"
[S26]: https://www.ird.govt.nz/employing-staff/deductions-from-income/deduction-notices-collecting-taxes-from-taxpayers-who-refuse-to-pay "IRD deduction notices, updated 16 April 2026"
[S27]: https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942502/ "District Court Act 2016, section 157, as at 17 February 2026"
[S28]: https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942500/ "District Court Act 2016, section 156, as at 17 February 2026"
[S29]: https://www.legislation.govt.nz/act/public/2016/49/en/latest/sections/DLM6942492/ "District Court Act 2016, section 154, as at 17 February 2026"
[S30]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/DLM356984/ "Tax Administration Act 1994, section 157, as at 1 October 2026"
[S31]: https://www.taxtechnical.ird.govt.nz/standard-practice-statements/processing/sps-21-01 "SPS 21/01 issuer index, issued 12 April 2021"
[S32]: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/standard-practice-statements/processing/sps-21-01.pdf?modified=20210420044632 "SPS 21/01 Deduction notices, paragraphs 26–36, 12 April 2021"

<!-- openaccountants-cta-block -->

---

[S33]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326 "KS4 employer guide, cover April 2026, selected pages"
[S34]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver "Starting employees, updated 21 October 2026"
[S35]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver/auto-enrol-employees-into-kiwisaver "Automatic enrolment, updated 21 October 2026"
[S36]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver "Employee opt-outs, updated 28 July 2026"
[S37]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver/employees-who-opt-out-late-from-kiwisaver "Late opt-outs, updated 28 April 2021"
[S38]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds "KiwiSaver and complying-fund gross pay, updated 28 April 2021"
[S39]: https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/making-changes-to-my-kiwisaver/changing-my-kiwisaver-contribution-rate/temporary-rate-reduction "Temporary rate reduction, updated 1 April 2026"
[S40]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employees-with-special-circumstances "Special employee circumstances, updated 1 October 2026"
[S41]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378821/ "6 Application, current copy 1 April 2026"
[S42]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378830/ "10 Who automatic enrolment rules apply to, current copy 1 April 2026"
[S43]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378834/ "12 Temporary employment, current copy 1 April 2026"
[S44]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378843/ "14 Other situations when automatic enrolment rules do not apply, current copy 1 April 2026"
[S45]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/ "64 Contribution rate, current copy 1 April 2026"
[S46]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569986/ "101L How to apply for rate reduction, current copy 1 April 2026"
[S47]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569987/ "101M Grant of rate reduction, current copy 1 April 2026"
[S48]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569995/ "101S Revocation of rate reduction, current copy 1 April 2026"
[S49]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379032/ "KiwiSaver Act section 60, current copy 1 April 2026"
[S50]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/ "KiwiSaver Act section 101D, current copy 1 April 2026"

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
