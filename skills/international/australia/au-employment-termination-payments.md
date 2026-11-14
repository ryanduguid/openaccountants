---
name: au-employment-termination-payments
description: >
  Use this skill for any Australian employment termination question: employment
  termination payments (ETPs), genuine redundancy, the tax-free redundancy limit,
  the ETP cap and whole-of-income cap, unused annual and long service leave on
  termination, payment in lieu of notice, ETP codes and STP reporting, delayed
  termination payments and death benefit ETPs. Trigger on "ETP", "redundancy
  payment", "genuine redundancy tax-free", "lump sum D", "Schedule 11",
  "Schedule 7", "termination pay withholding", "golden handshake", "payment in
  lieu of notice", "preservation age ETP", "whole-of-income cap", "ETP code R",
  "ETP code O". Covers 2026-27 figures for employers, payroll staff and advisers.
version: 1.5
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-05
review_status: pending_review
depends_on:
  - australia-payroll
  - au-super-guarantee
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Employment Termination Payments v1.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

> Use this skill for any Australian employment termination question: employment termination payments (ETPs), genuine redundancy, the tax-free redundancy limit, the ETP cap and whole-of-income cap, unused annual and long service leave on termination, payment in lieu of notice, ETP codes and STP reporting, delayed termination payments and death benefit ETPs. Trigger on "ETP", "redundancy payment", "genuine redundancy tax-free", "lump sum D", "Schedule 11", "Schedule 7", "termination pay withholding", "golden handshake", "payment in lieu of notice", "preservation age ETP", "whole-of-income cap", "ETP code R", "ETP code O". Covers 2026-27 figures for employers, payroll staff and advisers.

## Ask the client first

- What are the termination and payment dates, birth date, residence, visa status and effective TFN declaration? Check age at dismissal separately from preservation age at the payment year's end.
- What contract, award, dismissal evidence and voluntary-termination entitlement support each component? Identify any required retirement date, non-arm's-length dealing, re-employment arrangement or approved early retirement scheme.
- Which whole periods of service does the payment recognise, including documented transferred or discontinuous service? What earlier redundancy payments used the tax-free limit?
- What earlier life benefit ETPs were received in this income year or for this termination in any year, and what amounts counted towards their caps? Keep death benefit recipient history separate.
- What other taxable income, deductions and later income affect the employee's final whole-of-income cap? Separate that assessment from the employer's Schedule 11 withholding calculation.
- What leave types, accrual dates, normal pay period, tax-table lookups, SG eligibility, year-to-date qualifying earnings and member fund-receipt records support the payment and reporting? Return Needs Input for missing facts.

## The method, step by step

### Australia Employment Termination Payments and Redundancy v1.5

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

### Section 1 - Quick Reference

**Quick reference table**

| Field | Value | Source |
| --- | --- | --- |
| Country | Australia | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Income year covered | 2026-27 (1 July 2026 to 30 June 2027) | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| ETP cap | $270,000, indexed annually | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Whole-of-income cap | $180,000, not indexed, reduced by the employee's other taxable payments in the year | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Genuine redundancy tax-free limit | $13,598 plus $6,801 for each completed year of service | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Withholding on the taxable component within the cap | 32% under preservation age, 17% at or above preservation age | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Withholding above the cap | 47% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Preservation age | 60 for anyone born after 30 June 1964 | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Age-pension age | 67 for anyone born on or after 1 January 1957 | [DSS, pension age tables](https://guides.dss.gov.au/social-security-guide/3/4/1/10) |
| ETP timing rule | Generally within 12 months; statutory genuine redundancy/early retirement and applicable determination exceptions require separate checks (Section 3) | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Withholding tables | Schedule 11 for ETPs and Schedule 7 for unused leave, both applying from 1 July 2026 | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Reporting | STP pay event with an ETP code, or an ETP payment summary within 14 days | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Primary legislation | ITAA 1997 Divisions 82 and 83; TAA 1953 Schedule 1 sections 12-85 and 12-90 | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Tax authority | Australian Taxation Office | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Reviewed by | Pending. Australian CPA or CA review required | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |

### Section 2 - The calculation workflow

Work through these steps for every termination. Each component of the package gets its own
treatment, and the order matters because the code R part reduces the cap left for the code O part.

**Step 1. Split the package into components.**
Salary and wages owed, unused leave, the genuine redundancy or early retirement scheme amount,
the ETP components, and anything that is not an ETP at all (superannuation, foreign termination
payments, employee share scheme amounts, some restraint of trade payments). See Section 3.

**Step 2. Test whether the redundancy is genuine.**
The position must genuinely be redundant and the employee dismissed before the earlier of pension age and any applicable mandatory retirement or service-completion date. Check the voluntary-termination amount, any non-arm's-length amount limit, re-employment arrangements and statutory exclusions. A label or bank description does not establish these conditions. See Section 4 and [ITAA 1997 s 83-175](https://www.legislation.gov.au/C2026C00471/latest/text).

**Step 3. Work out the tax-free limit.**
$13,598 plus $6,801 for each completed year of service in 2026-27. The genuine redundancy amount
up to the limit is tax-free, is reported at lump sum D and is not an ETP.

**Step 4. Treat any excess as an ETP.**
Identify a tax-free component (service before 1 July 1983 or an invalidity segment); the rest is
the taxable component. See Section 5.

**Step 5. Choose the cap.**
Classify excluded and non-excluded life benefit payments under s 82-10(6) before choosing the cap and reporting code. Excluded payments use the ETP cap; non-excluded payments use the smaller applicable cap. Reconcile earlier payments and keep the employer's withholding calculation separate from the employee's final assessment. See Section 6.

**Step 6. Withhold from the taxable component.**
32% or 17% up to the cap, depending on the employee's age at the end of the income year, and 47%
above it. See Section 7.

**Step 7. Withhold from unused leave under Schedule 7.**
The rate depends on the reason for termination and when the leave accrued. See Section 8.

**Step 8. Report each component in its own place.**
Each ETP carries a code, and a redundancy excess and a golden handshake from the same termination
are reported as two ETPs. See Section 9.

### Section 3 - What is and is not an ETP

**Payments in and out of the ETP**

| Included in the ETP | Not an ETP |
| --- | --- |
| Gratuity or golden handshake | Unused annual leave and long service leave (Schedule 7 applies) |
| Genuine redundancy or early retirement scheme amount above the tax-free limit | Genuine redundancy or early retirement scheme amount up to the tax-free limit |
| Severance pay and a non-genuine redundancy payment | Salary, wages, allowances, bonuses and incentives owed for work done or leave taken |
| Payment in lieu of notice to the extent not included in the tax-free genuine redundancy or approved early retirement amount | Superannuation benefits |
| Unused sick leave and unused rostered days off | Foreign termination payments |
| Compensation for loss of job, and for wrongful dismissal paid within 12 months | Certain restraint of trade payments |
| Payments for loss of future super | Certain personal injury compensation for the inability to be employed |
| Payments on termination because of ill health, other than personal injury compensation | Employee share scheme payments, advances and loans |
| Lump sums paid on the death of an employee |  |

Use the full exclusions in [ITAA 1997 s 82-135](https://www.legislation.gov.au/C2026C00471/latest/text), rather than treating this summary as exhaustive. In particular, its advance/loan exclusion requires arm's-length terms; the personal-injury and restraint-of-trade exclusions have reasonableness conditions. Classify the substantiated legal character of each component, not its payroll label.

- **Definition**: An ETP is a lump sum paid in consequence of the termination of employment and received within 12 months of that termination, unless the ATO has determined otherwise. A payment from a super fund is never an ETP.  _([ITAA 1997 (Cth) s 82-130](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/82-130))_
- **The 12-month rule**: A payment outside 12 months is generally a delayed termination payment, rather than an ETP. Section 82-130(4) excepts genuine redundancy and approved early retirement scheme payments and recipients covered by a Commissioner determination. Check the operative class or individual determination and all its conditions; do not assume every late settlement qualifies. For a delayed termination payment with a valid TFN, Schedule 11 requires 32% withholding, rounded to the nearest dollar. Without a TFN, use 47% for a resident or 45% for a foreign resident and ignore cents. Report it as gross payments, not an ETP. The age-only non-genuine redundancy exception in s 82-10(6)(a) does not itself remove the 12-month condition. [ITAA 1997 s 82-130(4)-(8)](https://www.legislation.gov.au/C2026C00471/latest/text); [ATO, the 12-month rule](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/the-12-month-rule); [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments).
- **Life and death benefit ETPs**: A life benefit ETP is paid to the employee. A death benefit ETP is paid to a dependant, a non-dependant or the trustee of the estate because employment ended on death, and the withholding depends on who receives it. See Section 7.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Payments that are ETPs**: The ATO's lists of payments inside and outside an ETP are the starting point for Step 1, and compensation for wrongful dismissal counts only when paid within 12 months of the actual termination.  _([ATO, Payments that are ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/payments-that-are-etps))_

### Section 4 - Genuine redundancy and early retirement schemes

- **What makes a redundancy genuine**: The employer dismisses the employee because the position is genuinely redundant. Acceptance of an employer-decided package or an expression of interest does not by itself prevent dismissal. Only the amount above what could reasonably be expected on voluntary termination qualifies. Dismissal must precede the earlier of pension age and an applicable mandatory retirement or service-completion date. If the dismissal is not at arm's length, the payment must not exceed the reasonable arm's-length amount; non-arm's-length dealings alone do not disqualify it. An excessive payment fails that condition, rather than merely having the excess trimmed. At dismissal there must be no arrangement between the employee and employer, or employer and another person, to employ the employee afterwards. Payments in lieu of superannuation benefits and the other s 82-135 exclusions are not genuine redundancy amounts. [ITAA 1997 s 83-175](https://www.legislation.gov.au/C2026C00471/latest/text); [TR 2009/2, paragraphs 40-54](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001).
- **Non-genuine redundancy and dismissal evidence**: Voluntary departure, ordinary expiry of a fixed service term, retirement at the applicable age or dismissal principally for discipline or inefficiency do not establish genuine redundancy. The ATO's summary describes a pressured resignation as generally non-genuine, but TR 2009/2 paragraph 22 recognises constructive dismissal. Establish whether there was a dismissal and whether genuine redundancy was its prevailing cause; a pay cut, resignation or unsuitable alternative role alone does not decide both questions. Exceptional rolling-contract cases also require their actual employment evidence. Refer unresolved classification for review. [TR 2009/2, paragraphs 18-28 and 36-39](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001); [ATO summary](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement).
- **Failure only of the age/service limit**: A payment that would be genuine redundancy but for s 83-175(2)(a) is an excluded life benefit payment under s 82-10(6)(a). It has no genuine redundancy tax-free amount, but the whole-of-income cap does not apply. Do not automatically code every non-genuine redundancy as O or apply both caps. Confirm the applicable reporting code separately; the cap follows the statutory conditions. [ITAA 1997 ss 82-10(6)(a) and 83-175](https://www.legislation.gov.au/C2026C00471/latest/text); [ATO, applying the ETP caps](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps).
- **Notice pay and other component labels**: A payment in lieu of notice can form part of genuine redundancy if it would not reasonably be expected on voluntary termination and the other conditions hold. Conversely, a contractual payment payable on any departure may be a non-excluded ETP. Check the employment terms and redundancy element before assigning a cap or code. Its tax treatment does not decide its separate SG treatment. [TR 2009/2, paragraphs 55-65](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001); [ATO, categorising payments](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps).

**Age-pension age**

| Date of birth | Age-pension age | Source |
| --- | --- | --- |
| Before 1 July 1952 | Historical sex and birth-date rules apply; use the DSS tables | [DSS, pension age tables](https://guides.dss.gov.au/social-security-guide/3/4/1/10) |
| 1 July 1952 to 31 December 1953 | 65 and 6 months | [DSS, pension age tables](https://guides.dss.gov.au/social-security-guide/3/4/1/10) |
| 1 January 1954 to 30 June 1955 | 66 | [DSS, pension age tables](https://guides.dss.gov.au/social-security-guide/3/4/1/10) |
| 1 July 1955 to 31 December 1956 | 66 and 6 months | [DSS, pension age tables](https://guides.dss.gov.au/social-security-guide/3/4/1/10) |
| On or after 1 January 1957 | 67 | [DSS, pension age tables](https://guides.dss.gov.au/social-security-guide/3/4/1/10) |

- **The tax-free limit for 2026-27**: Base amount $13,598 plus $6,801 for each whole year in the period or sum of employment periods to which the payment relates. Do not count a part year as a whole year. Document recognised previous or discontinuous service; do not assume only the current uninterrupted start-to-dismissal period counts. Reconcile earlier payments for the redundancy before applying the limit to another instalment. The qualifying amount up to the limit is reported at lump sum D, is not an ETP and has no withholding; the qualifying excess is an excluded ETP. [ITAA 1997 s 83-170](https://www.legislation.gov.au/C2026C00471/latest/text); [TR 2009/2, paragraphs 69-75](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001); [Schedule 11, note 1](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments).
- **Early retirement schemes**: Obtain the ATO's written approval/class ruling before implementation and verify that the employee, retirement date and payment satisfy it and s 83-180. Normally the approved class and reorganisation conditions apply; s 83-180(4) permits approval in special circumstances. The age/service, arm's-length amount and no-re-employment conditions still matter. A qualifying payment uses the same s 83-170 tax-free limit as genuine redundancy. [ITAA 1997 ss 83-170 and 83-180](https://www.legislation.gov.au/C2026C00471/latest/text); [ATO, redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement).
- **Age limit since 2019**: Dismissals on or after 1 July 2019 use age-pension age rather than 65. An employer who withheld on the old basis can refund the excess and correct the STP report.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_
- **Ruling**: TR 2009/2 sets out the Commissioner's view on each condition, including dismissal, arm's length dealing and the exclusion of payments the employee would have received anyway.  _([TR 2009/2 Income tax: genuine redundancy payments](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001))_

### Section 5 - Tax-free and taxable components of an ETP

- **Tax-free component**: Only two things create a tax-free component: service before 1 July 1983 and an invalidity segment. Everything else is the taxable component. Do not withhold from the tax-free component, but report both.  _([ATO, Tax-free component of ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps))_
- **Pre-1 July 1983 segment**: Subtract any invalidity segment from the ETP, then multiply the result by the days of employment before 1 July 1983 divided by the total days of employment the ETP relates to.  _([ATO, Tax-free component of ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps))_
- **Invalidity segment**: The payment must be because the person stopped gainful employment due to physical or mental ill health before their statutory last retirement day. Two legally qualified medical practitioners must certify that, because of the ill health, the person is unlikely ever to be gainfully employed in a capacity for which they are reasonably qualified by education, experience or training. Multiply the ETP by days from termination to that last retirement day, divided by employment days plus days to retirement. Document the actual day, generally age 65 or the applicable service-completion day; do not substitute pension age or invent missing service days. A death benefit ETP cannot include an invalidity segment. Separately, s 82-10(6)(c) treats a payment that would include an invalidity segment but for the last-retirement-day condition in s 82-150(1)(c) as excluded for cap purposes; that exception does not create a tax-free invalidity segment. [ITAA 1997 s 82-150](https://www.legislation.gov.au/C2026C00471/latest/text); [ATO, tax-free component of ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps).

### Section 6 - Which cap applies

**ETP codes and caps**

| Code | Payment | Cap | Source |
| --- | --- | --- | --- |
| R | Excluded life benefit payment: qualifying early retirement scheme or genuine redundancy excess, invalidity or qualifying compensation; check s 82-10(6) and the applicable reporting specification | ETP cap only | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) |
| O | Non-excluded life benefit payment, such as a golden handshake, gratuity, non-genuine redundancy, severance, notice pay or unused sick leave/RDOs that does not satisfy an excluded-payment condition | Smaller of the ETP cap and the whole-of-income cap | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) |
| S | A code R payment where a code R, code O or transitional payment for the same termination was made in an earlier income year | ETP cap only | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) |
| P | A code O payment where a code R, code O or transitional payment for the same termination was made in an earlier income year | Smaller of the two caps | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) |
| D | Death benefit paid to a dependant | ETP cap | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) |
| N | Death benefit paid to a non-dependant | ETP cap | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) |
| B | Death benefit paid to a non-dependant where a payment to that non-dependant for the same termination was made in an earlier income year | ETP cap | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) |
| T | Death benefit paid to the trustee of the deceased estate | No withholding | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) |

- **Classify before using a code**: Section 82-10(6) determines excluded life benefit payments. Its compensation limb requires a genuine dispute, principally compensation for the listed matters and an amount exceeding what could reasonably be expected on voluntary termination. A description such as 'compensation', 'notice' or 'non-genuine redundancy' alone does not decide the cap. Check the age-only redundancy and invalidity exceptions and categorise each component from its actual conditions. [ITAA 1997 s 82-10(6)](https://www.legislation.gov.au/C2026C00471/latest/text); [ATO, applying the ETP caps](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps).
- **ETP cap and payment history**: The 2026-27 amount is $270,000, indexed annually. For life benefits, reconstruct both the current-income-year history, including other terminations, and the history for the same termination across income years. Section 82-10(4) uses amounts previously worked out under that subsection, with its excluded-payment distinctions; s 82-10(8) also limits the result by all earlier life benefit amounts counted towards the cap in each history. The two histories impose separate limits: do not add their totals into one union or count a payment twice. Keep tax-free amounts and amounts above the concession limit separate. Missing earlier-payment records mean Needs Input. [ITAA 1997 s 82-10(4) and (8)](https://www.legislation.gov.au/C2026C00471/latest/text); [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments).
- **Whole-of-income cap**: The $180,000 amount is not indexed and cannot be reduced below zero. For employer withholding, follow Schedule 11's payment-based steps and document which payments are known. For the employee's final assessment, s 82-10(4)(c), (5) and (7) use taxable income with their specific current/later ETP exclusions. Other taxable income, including later salary, interest and the taxable component of relevant earlier ETPs, can reduce the final cap; allowable deductions also affect taxable income. Only 5% of pre-16 August 1978 long service leave is assessable for this purpose. Tax-free redundancy does not reduce it. Do not treat withholding as the final income tax or assume all ETPs can be left out of the income reconciliation. For a non-excluded payment, compare the remaining applicable ETP cap with this cap; Schedule 11 uses the whole-of-income cap if equal. [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text); [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ATO, whole-of-income cap](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/working-out-the-whole-of-income-cap-amount).
- **A package with both kinds**: Process the excluded part first, then apply the remaining ETP cap and whole-of-income test to the non-excluded part. For the statutory final assessment, s 82-10(7) does not disregard the excluded taxable component when testing the non-excluded part. Schedule 11 example 4 instead illustrates employer withholding with a $397 redundancy excess withheld at 32%, a $17,678 gratuity, a $40,000 payment-based whole-of-income cap and a $269,603 ETP cap balance. Preserve that example's withholding scope; do not substitute its cap for the statutory assessment calculation. The ATO whole-of-income page's exclusion list also conflicts with its own mixed-payment explanation and examples. Follow the statute for assessment and obtain qualified review where that distinction affects reporting or final tax. [ITAA 1997 s 82-10(5) and (7)](https://www.legislation.gov.au/C2026C00471/latest/text); [Schedule 11, example 4](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ATO mixed-payment examples](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/working-out-the-whole-of-income-cap-amount).
- **Death benefits**: Keep life and death benefit caps separate. For a death benefit, reconcile the recipient's earlier death benefit payments for the same termination, including earlier income years; another recipient's payment does not automatically consume this recipient's cap. Nil withholding from a payment to the estate trustee does not establish that the estate or beneficiaries owe no tax. [ITAA 1997 ss 82-65 to 82-75](https://www.legislation.gov.au/C2026C00471/latest/text).
- **When other income is large**: If the paying employer has already made $200,000 of other taxable payments to the employee in the income year, its Schedule 11 whole-of-income cap is nil, so a golden handshake is withheld at 47% in full while the redundancy excess still gets the ETP cap. Income from other payers does not enter that withholding calculation; on assessment, taxable income of $180,000 or more under s 82-10(4)(c) and (5) still leaves a nil final whole-of-income cap.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_
- **Detail pages**: The ATO's cap pages walk through which cap applies and how to work out the whole-of-income cap with more than one payment in the year.  _([ATO, Applying the ETP caps](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps))_

### Section 7 - Withholding rates under Schedule 11 (from 1 July 2026)

**Table A summary**

These are 2026-27 Schedule 11 rates for the stated payment category. Confirm valid TFN, residence/treaty and working holiday maker status before applying them; the overrides below still apply.

| Payment | Age at the end of the income year | Amount | Rate | Source |
| --- | --- | --- | --- | --- |
| Life benefit, code R | Under preservation age | Up to the ETP cap | 32% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |
| Life benefit, code R | Preservation age or over | Up to the ETP cap | 17% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |
| Life benefit, code R | Any | Above the ETP cap | 47% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |
| Life benefit, code O | Under preservation age | Up to the smaller cap | 32% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |
| Life benefit, code O | Preservation age or over | Up to the smaller cap | 17% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |
| Life benefit, code O | Any | Above the smaller cap | 47% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |
| Death benefit to a non-dependant | Any | Up to the ETP cap, then above it | 32%, then 47% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |
| Death benefit to a dependant | Any | Up to the ETP cap, then above it | Nil, then 47% | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |
| Death benefit to the trustee of the estate | Any | All | Nil | [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments) |

- **Preservation age**: Test the employee's age at the end of the income year in which the payment is made, not at termination. Preservation age is 60 for anyone born after 30 June 1964, and everyone born earlier has already reached it.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **No TFN**: Withhold 47% from a resident and 45% from a foreign resident who has not quoted a TFN, ignoring cents. A TFN declaration stays effective for 12 months after the last payment.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Foreign residents**: Check the tax treaty first. If the ETP is assessable only in the other country, do not withhold. If it is assessable in Australia, use Table A less the 2% Medicare levy.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Rounding**: Round to the nearest dollar, with 50 cents rounding up.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Death benefit dependants**: A dependant includes a spouse, a child under 18, a person in an interdependency relationship and anyone who was a dependant of the deceased just before death. Nothing is withheld from a payment to the trustee of the estate.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_

### Section 8 - Unused leave on termination under Schedule 7 (from 1 July 2026)

**Withholding on unused annual leave, leave loading and long service leave**

| Leave | Reason for termination | Accrual period | Withholding | Reported at | Source |
| --- | --- | --- | --- | --- | --- |
| Annual leave and loading | Genuine redundancy, invalidity or early retirement scheme | Any | 32% | Lump sum A | [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Annual leave and loading | Any other reason | Before 18 August 1993 | 32% | Lump sum A | [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Annual leave and loading | Any other reason | On or after 18 August 1993 | Marginal rates | Salary and wages | [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Long service leave | Any reason | Before 16 August 1978 | 5% of the amount, taxed at marginal rates | Lump sum B | [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Long service leave | Any reason | 16 August 1978 to 17 August 1993 | 32% | Lump sum A | [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Long service leave | Genuine redundancy, invalidity or early retirement scheme | After 17 August 1993 | 32% | Lump sum A | [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |
| Long service leave | Any other reason | After 17 August 1993 | Marginal rates | Salary and wages | [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment) |

- **Marginal rate method**: For leave requiring the Schedule 7 marginal calculation, divide the relevant amount by the normal pay periods in 12 months and discard cents from that quotient before adding it to normal gross earnings. Use the applicable regular PAYG table for both the normal and increased pay, subtract the normal withholding and multiply the difference by the pay-period count. Normal gross earnings are generally the last full pay period, including taxable allowances, overtime and bonuses; significantly fluctuating pay can use the financial-year-to-date average. A withholding variation applies to unused leave only if its notice includes that leave; otherwise use Schedule 7, including the regular table rather than the varied rate. [ATO, Schedule 7, marginal rate calculation and variations](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment).
- **Small payments**: Where a post-17 August 1993 lump sum from normal termination is less than $300, withhold the lesser of the table amount and 32% of the payment.  _([ATO, Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment))_
- **No TFN**: If the employee has not provided a TFN before the payment, withhold 47%, or 45% for a foreign resident.  _([ATO, Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment))_
- **Leave is never an ETP**: Unused annual leave and long service leave sit outside the ETP caps, but a lump sum of leave counts as a taxable payment when the whole-of-income cap is reduced.  _([ATO, Accrued leave](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/accrued-leave))_
- **No study loan withholding**: Do not withhold for study and training support loans from lump sum termination payments.  _([ATO, Weekly tax table](https://www.ato.gov.au/tax-rates-and-codes/tax-table-weekly))_
- **Super guarantee**: From 1 July 2026 use qualifying earnings (QE), the applicable SG eligibility/rate and remaining annual maximum contribution base in `au-super-guarantee.md`. Notice pay is QE for all termination reasons, regardless of its tax treatment. Unused annual, long service, personal/carers leave, RDOs and overtime time off in lieu paid on termination are not QE; the ATO's other listed termination payments are also excluded. An ETP label alone does not establish that SG is nil. Verify the actual components, annual base and fund receipt. Historical periods retain their applicable OTE/quarterly rules. [ATO, qualifying earnings, Table 13 and example 7](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/what-payments-are-qualifying-earnings).

## Boundary and exception table

### Section 11 - Common errors

- Treating a resignation, the end of a fixed-term contract or a dismissal at age-pension age as a genuine redundancy.
- Counting part years of service in the tax-free limit.
- Applying the whole-of-income cap to a code R payment, or forgetting to reduce it by salary and unused leave already paid in the year.
- Testing preservation age at the termination date rather than at the end of the income year.
- Withholding from the tax-free component or from the lump sum D amount.
- Reporting a redundancy excess and a golden handshake under one ETP code.
- Using Schedule 11 for unused leave, or marginal rates for leave paid on a genuine redundancy.
- Withholding study loan amounts from a lump sum termination payment.
- Treating every payment outside 12 months as an ETP, or overlooking the statutory genuine redundancy/early retirement and operative determination exceptions.
- Deciding SG from the ETP code instead of QE components, or omitting notice pay from QE.
- Ignoring other terminations in the current-year cap history, subtracting both history totals as a single sum or applying a new cap to each instalment.
- Treating a non-arm's-length relationship, age-only failure or a notice-pay label as an automatic tax classification.
- Using a withholding example's cap or withheld amount as proof of the employee's final assessment.

## Worked cases

### Section 10 - Worked example

**Worked example facts**

| Item | Detail |
| --- | --- |
| Employee | Ana, aged 45, preservation age 60, Australian resident, TFN quoted |
| Service | Started 3 September 2018, dismissed on 30 October 2026 because her role was abolished, so 8 completed years |
| Salary and wages from 1 July to 30 October 2026 | $34,000 |
| Redundancy payment | $80,000, more than she would receive on resignation, at arm's length, with no arrangement to re-employ her |
| Payment in lieu of notice | $9,000; the verified workplace terms make this payable on any departure, including voluntary termination, so it is separately non-excluded |
| Unused annual leave | $6,000, all accrued after 17 August 1993 |

**Facts.** All figures are synthetic and fall in the 2026-27 income year. The $80,000 is the independently verified genuine redundancy element after excluding voluntary-termination entitlements; it is not in lieu of superannuation benefits. There is no earlier mandatory retirement/service date, earlier ETP, recognised prior service, earlier redundancy instalment, tax-free ETP component or other taxable payment in the employer's working paper. Ana is SG eligible under the general rate, with $34,000 QE already paid by this employer and no other QE before this package. The notice-pay classification is a stipulated contractual fact, not an inference from its label. See [TR 2009/2 paragraph 64](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001).

**Step 1, genuine redundancy test.** Ana is under age-pension age, the job no longer exists and the
employer made the decision. The $80,000 is a genuine redundancy payment.

**Step 2, tax-free limit.**

```
Base amount                                      13,598
Service amount 6,801 x 8 completed years         54,408
Tax-free limit                                   68,006
Genuine redundancy payment                       80,000
Tax-free, reported at lump sum D                 68,006
Excess, an ETP coded R                           11,994
```

**Step 3, the ETP coded R.** There is no tax-free component. Only the ETP cap of $270,000 applies,
and Ana is under preservation age.

```
Taxable component                                11,994
Withholding at 32%                                3,838
```

**Step 4, the payment in lieu of notice, an ETP coded O.**

This is the employer's Schedule 11 withholding illustration. For a final statutory assessment, the mixed-payment rule includes the $11,994 excluded taxable component in the income reconciliation, giving a whole-of-income cap of $128,006 before any other income or deductions. The $9,000 remains below either cap under these facts; do not infer that withholding equals final tax. [ITAA 1997 s 82-10(5) and (7)](https://www.legislation.gov.au/C2026C00471/latest/text).

```
Other taxable payments (salary 34,000 plus leave 6,000)    40,000
Whole-of-income cap: 180,000 less 40,000                  140,000
ETP cap balance: 270,000 less 11,994                      258,006
Smaller cap                                               140,000
Taxable component                                           9,000
Withholding at 32%                                          2,880
```

**Step 5, unused annual leave.** The termination is a genuine redundancy, so Schedule 7 applies 32%
whatever the accrual date.

```
Unused annual leave                               6,000
Withholding at 32%                                1,920
Reported at lump sum A
```

**Step 6, super.** Under the stipulated general SG eligibility and remaining annual base, 12% applies to the $9,000 notice-pay QE, giving $1,080. The salary is also QE; the separate redundancy element and unused leave are not. Notice pay remains QE despite being an ETP for tax. [ATO QE, Table 13 and example 7](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/what-payments-are-qualifying-earnings).

**Step 7, reporting.** The income statement shows lump sum D of $68,006 and lump sum A of $6,000.
Two ETP records follow: code R with a taxable component of $11,994 and tax of $3,838, and code O
with a taxable component of $9,000 and tax of $2,880. Total withholding on the package is $8,638.

**What changes with age.** If Ana were 62 at 30 June 2027, both ETPs would be withheld at 17%
($2,039 and $1,530) and the leave would stay at 32%. If she were 67 on the day of dismissal, there would be no genuine redundancy tax-free amount. If the age/service condition were the only failed genuine redundancy condition, s 82-10(6)(a) would preserve excluded-payment treatment for the $80,000, so the whole-of-income cap would not apply to it. Confirm the reporting code and apply Schedule 7's normal-termination treatment to leave rather than carrying forward the 32% genuine-redundancy leave rate. [ITAA 1997 ss 82-10(6)(a) and 83-175](https://www.legislation.gov.au/C2026C00471/latest/text).


### Checked case 1: Ana's verified package and notice-pay QE

Under the facts above, the genuine redundancy limit is $68,006 and its taxable excess is $11,994. Schedule 11 withholding is $3,838 on that excess and $2,880 on the separately non-excluded notice pay. Schedule 7 withholding on the leave is $1,920, giving package withholding of $8,638. The employer's payment-based whole-of-income cap is $140,000; the statutory mixed-payment assessment cap before any further income/deductions is $128,006. The $9,000 remains below both. Notice-pay QE is $9,000 and the remaining annual base accommodates all of it, giving employer SG of $1,080. The example checks these stipulated calculations, not Ana's final assessed tax. Sources: [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments), [Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment), [ITAA 1997 s 82-10](https://www.legislation.gov.au/C2026C00471/latest/text) and [ATO QE Table 13](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/what-payments-are-qualifying-earnings).

```oa-check
name: Ana verified redundancy and separately non-excluded notice (2026-27)
inputs:
  base: 13598
  service_amount: 6801
  service_years: 8
  redundancy: 80000
  notice: 9000
  leave: 6000
  salary: 34000
  etp_cap: 270000
  whole_income_limit: 180000
  mcb: 270830
steps:
  - redundancy_limit: base + service_amount * service_years
  - lump_sum_d: min(redundancy, redundancy_limit)
  - excluded_taxable: redundancy - lump_sum_d
  - excluded_withholding: round(excluded_taxable * 0.32)
  - etp_balance: max(0, etp_cap - excluded_taxable)
  - withholding_whole_income_cap: max(0, whole_income_limit - salary - leave)
  - assessment_whole_income_cap: max(0, whole_income_limit - salary - leave - excluded_taxable)
  - notice_cap: min(etp_balance, withholding_whole_income_cap)
  - notice_withholding: round(min(notice, notice_cap) * 0.32 + max(0, notice - notice_cap) * 0.47)
  - leave_withholding: round(leave * 0.32)
  - notice_qe: min(notice, max(0, mcb - salary))
  - notice_sg: notice_qe * 0.12
  - package_withholding: excluded_withholding + notice_withholding + leave_withholding
expected:
  redundancy_limit: 68006
  lump_sum_d: 68006
  excluded_taxable: 11994
  excluded_withholding: 3838
  etp_balance: 258006
  withholding_whole_income_cap: 140000
  assessment_whole_income_cap: 128006
  notice_withholding: 2880
  leave_withholding: 1920
  notice_qe: 9000
  notice_sg: 1080
  package_withholding: 8638
```

### Checked case 2: an age-only failure is different from a different dismissal cause

A synthetic resident employee is 67 at dismissal, has quoted a valid TFN and receives an $80,000 taxable life benefit within 12 months. Other taxable payments this employer already made to the employee in the income year are $200,000; there are no earlier ETPs or tax-free ETP components. If all genuine redundancy conditions hold except s 83-175(2)(a), the payment is excluded from the whole-of-income test and the full $80,000 is within the $270,000 ETP cap: Schedule 11 rate arithmetic at 17% gives $13,600. If instead the verified facts establish a non-excluded disciplinary termination with no other excluded-payment condition, the whole-of-income cap is zero and 47% gives $37,600. The $24,000 difference makes the missing classification material. This is a comparison of different established facts, not a choice of code; return Needs Input if the cause or conditions are unknown, and verify the age-only reporting code before submission. [ITAA 1997 s 82-10(6)(a)](https://www.legislation.gov.au/C2026C00471/latest/text); [ATO, applying the caps](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps); [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments).

```oa-check
name: Age-only excluded payment versus independently non-excluded termination (2026-27)
inputs:
  payment: 80000
  other_taxable_payments: 200000
  etp_cap: 270000
steps:
  - whole_income_cap: max(0, 180000 - other_taxable_payments)
  - age_only_withholding: round(min(payment, etp_cap) * 0.17 + max(0, payment - etp_cap) * 0.47)
  - non_excluded_cap: min(etp_cap, whole_income_cap)
  - non_excluded_withholding: round(min(payment, non_excluded_cap) * 0.17 + max(0, payment - non_excluded_cap) * 0.47)
  - difference: non_excluded_withholding - age_only_withholding
expected:
  whole_income_cap: 0
  age_only_withholding: 13600
  non_excluded_withholding: 37600
  difference: 24000
```

### Checked case 3: notice pay depends on the voluntary-termination entitlement

Use a synthetic employee aged 45 at the payment year's end, with a valid TFN, 8 whole recognised service years, no earlier ETPs/instalments or tax-free ETP components and every genuine redundancy condition verified. The package comprises $80,000 redundancy plus $9,000 notice pay. The same employer has already paid $200,000 salary/QE; no other amounts use the annual base. Where the workplace terms make notice pay payable on voluntary departure, it is non-excluded here: the redundancy excess gives $3,838 withholding and the notice gives $4,230, totalling $8,068. Where the facts instead establish that the $9,000 would not be expected on voluntary termination and it forms part of genuine redundancy, the genuine amount is $89,000 and its $20,994 taxable excess gives $6,718 withholding. The $1,350 difference requires the actual terms, not a label. In both branches the notice pay is $9,000 QE and employer SG is $1,080 under the stipulated general rate and remaining base. [TR 2009/2 paragraphs 55-65](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001); [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [ATO QE Table 13](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/what-payments-are-qualifying-earnings).

```oa-check
name: Contractual notice entitlement changes redundancy classification but not notice QE (2026-27)
inputs:
  redundancy: 80000
  notice: 9000
  salary: 200000
  service_years: 8
steps:
  - redundancy_limit: 13598 + 6801 * service_years
  - separate_redundancy_excess: max(0, redundancy - redundancy_limit)
  - whole_income_cap: max(0, 180000 - salary)
  - separate_notice_withholding: round(min(notice, whole_income_cap) * 0.32 + max(0, notice - whole_income_cap) * 0.47)
  - separate_total_withholding: round(separate_redundancy_excess * 0.32) + separate_notice_withholding
  - genuine_excess_with_notice: max(0, redundancy + notice - redundancy_limit)
  - genuine_total_withholding: round(genuine_excess_with_notice * 0.32)
  - difference: separate_total_withholding - genuine_total_withholding
  - notice_sg_both: min(notice, max(0, 270830 - salary)) * 0.12
expected:
  separate_redundancy_excess: 11994
  separate_notice_withholding: 4230
  separate_total_withholding: 8068
  genuine_excess_with_notice: 20994
  genuine_total_withholding: 6718
  difference: 1350
  notice_sg_both: 1080
```

### Checked case 4: keep the two earlier-payment histories separate

A synthetic resident employee under preservation age, with a valid TFN, receives a $50,000 non-excluded life benefit in 2026-27. Earlier amounts independently verified as counting towards the relevant concession limits are $250,000 for this same termination in 2025-26 and $30,000 for a different termination earlier in 2026-27. Both relevant terminations/payments satisfy the timing conditions. Other taxable income for this working paper is $100,000 salary plus that earlier $30,000 ETP, with no further income or deductions. The current-year ETP balance is $240,000 and the same-termination balance is $20,000. They are alternative limits, not a combined $280,000 subtraction. The whole-of-income cap is $50,000, so $20,000 is within the smallest cap and $30,000 above it. Schedule 11 rate arithmetic gives $20,500. The historic counted amounts are inputs from the verified history; this case does not recreate the earlier assessments. [ITAA 1997 s 82-10(4), (5) and (8)](https://www.legislation.gov.au/C2026C00471/latest/text); [ATO multiple ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/working-out-the-whole-of-income-cap-amount); [Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments).

```oa-check
name: Separate current-year and same-termination ETP limits (2026-27)
inputs:
  payment: 50000
  etp_cap: 270000
  prior_same_termination_counted: 250000
  earlier_current_year_counted: 30000
  earlier_current_year_taxable: 30000
  salary: 100000
steps:
  - current_year_balance: max(0, etp_cap - earlier_current_year_counted)
  - same_termination_balance: max(0, etp_cap - prior_same_termination_counted)
  - whole_income_cap: max(0, 180000 - salary - earlier_current_year_taxable)
  - available_cap: min(current_year_balance, same_termination_balance, whole_income_cap)
  - within_cap: min(payment, available_cap)
  - above_cap: max(0, payment - available_cap)
  - rate_illustration: round(within_cap * 0.32 + above_cap * 0.47)
expected:
  current_year_balance: 240000
  same_termination_balance: 20000
  whole_income_cap: 50000
  available_cap: 20000
  within_cap: 20000
  above_cap: 30000
  rate_illustration: 20500
```

### Checked case 5: Schedule 7 discards cents before the second table lookup

Recompute the ATO's 2026-27 Schedule 7 normal-retirement example: weekly normal gross $1,155, pre-16 August 1978 long service leave $780, middle-period leave $6,420 and post-17 August 1993 leave $14,820. The marginal calculation applies to $39 plus $14,820. Dividing $14,859 by 52 gives $285.75, but discard cents before adding $285 to normal pay: the second table lookup is at $1,440. The schedule supplies the verified weekly lookup amounts $188 and $279; this case does not independently implement the weekly tax table. The marginal withholding is $4,732, middle-period withholding rounds to $2,054, total leave withholding is $6,786 and the final week including ordinary pay withholding is $6,974. The employee has the schedule's valid TFN/threshold facts and no unused-leave variation. [Schedule 7, marginal calculation and long-service-leave example](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment).

```oa-check
name: Published Schedule 7 leave calculation and cents-discard step (2026-27)
inputs:
  normal_pay: 1155
  pre_1978_leave: 780
  middle_leave: 6420
  post_1993_leave: 14820
  pay_periods: 52
  normal_table_withholding: 188
  increased_table_withholding: 279
steps:
  - pre_1978_assessable: pre_1978_leave * 0.05
  - marginal_amount: pre_1978_assessable + post_1993_leave
  - whole_dollar_increment: floor(marginal_amount / pay_periods)
  - increased_pay: normal_pay + whole_dollar_increment
  - marginal_withholding: (increased_table_withholding - normal_table_withholding) * pay_periods
  - middle_withholding: round(middle_leave * 0.32)
  - leave_withholding: marginal_withholding + middle_withholding
  - final_week_withholding: leave_withholding + normal_table_withholding
expected:
  pre_1978_assessable: 39
  marginal_amount: 14859
  whole_dollar_increment: 285
  increased_pay: 1440
  marginal_withholding: 4732
  middle_withholding: 2054
  leave_withholding: 6786
  final_week_withholding: 6974
```

### Checked case 6: ordinary rounding and no-TFN truncation differ

For an Australian resident aged 60 or over at the end of 2026-27, a $50 non-excluded taxable ETP within both verified caps gives $8.50 at the Schedule 11 rate of 17%; a valid TFN means round up to $9. Without a TFN, the resident rate is 47% and cents are ignored, giving $23. A foreign resident without a TFN uses 45% and ignores cents, giving $22, subject to the guide's treaty and visa scope checks. These are different established TFN/residence facts; do not infer either from missing records. [Schedule 11, no TFN and rounding](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments).

```oa-check
name: ETP half-up rounding versus no-TFN cents truncation (2026-27)
inputs:
  taxable_etp: 50
steps:
  - valid_tfn_resident: round(taxable_etp * 0.17)
  - no_tfn_resident: floor(taxable_etp * 0.47)
  - no_tfn_foreign: floor(taxable_etp * 0.45)
expected:
  valid_tfn_resident: 9
  no_tfn_resident: 23
  no_tfn_foreign: 22
```

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.

## Filing and payment

### Section 9 - Reporting

- **STP**: Report each ETP in the pay event with its code, the tax-free and taxable components, the tax withheld and the payment date. An employer that is exempt from or deferred on STP gives the employee a PAYG payment summary for the ETP within 14 days.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **One package, several records**: Report the separately classified excluded and non-excluded parts with their verified ETP types and components; tax-free redundancy goes to lump sum D and leave to the applicable A/B or gross-payments fields. A genuine redundancy excess and a notice payment that is independently established as non-excluded need separate ETP records. Do not assign O to notice pay before testing its actual contractual and redundancy treatment. [ATO, Schedule 11 reporting and example 4](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments); [TR 2009/2 paragraph 64](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001).
- **Working holiday makers**: Use Schedule 15, not Schedule 11 or Schedule 7, for every payment to a working holiday maker, including the taxable component of an ETP and unused leave. See `au-working-holiday-makers.md`.  _([ATO, Schedule 15](https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers))_
- **Corrections**: Fix an STP error at the next pay event, or with an update event after finalisation. A payment summary already given to the employee cannot be changed; follow the ATO's amendment process instead.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_

## Completion checklist

### Section 12 - Self-checks

- [ ] Every component of the package is classified before any rate is applied.
- [ ] The genuine redundancy conditions, including age-pension age on the dismissal date, are documented.
- [ ] Whole service periods to which the payment relates, recognised earlier service and earlier redundancy instalments are documented; part years are not rounded up.
- [ ] The payment-based withholding cap is separated from final taxable-income reconciliation, including later income, relevant earlier ETPs and mixed-payment treatment.
- [ ] Both current-year life benefit history and same-termination history across years are checked, with counted concession amounts and death benefit recipient history kept separate.
- [ ] Preservation age is tested at 30 June of the payment year.
- [ ] Each ETP has its own code and record, and lump sums A, B and D sit on the income statement.
- [ ] Schedule 7 rates match the reason for termination and the accrual dates.
- [ ] Foreign resident and no-TFN adjustments have been considered.
- [ ] SG eligibility, notice-pay QE, remaining annual base and member fund receipt are verified independently of the ETP code; excluded termination leave is not treated as QE.

## Sources

| Source | URL | Read on |
|---|---|---|
| ATO, selected passages | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/82-130> | 2026-11-02; s 82-130 body; historical CCH determination notes not relied on as current instruments |
| ATO, selected passages | <https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments> | 2026-11-02; selected 2026-27 caps, categories, rates, timing, rounding and reporting passages |
| ATO, selected passages | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/payments-that-are-etps> | 2026-11-02; included/excluded payment lists; statutory qualifications checked separately |
| ATO, selected passages | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement> | 2026-11-02; selected dismissal, tax-free reporting and early retirement passages |
| TR 2009/2, selected passages | <https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001> | 2026-11-02; selected paragraphs 18-28, 36-54 and 55-75; not the full ruling |
| ATO, selected passages | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps> | 2026-11-02; tax-free components, service fraction and invalidity conditions |
| ATO, selected passages | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps> | 2026-11-02; cap histories, excluded-payment categories and classification passages |
| ATO, selected passages | <https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment> | 2026-11-02; leave table, marginal method, rounding, published example, variations and TFN |
| ATO, selected passages | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/accrued-leave> | 2026-11-02; unused annual/long-service leave scope and reporting overview |
| Retained citation | <https://www.ato.gov.au/tax-rates-and-codes/tax-table-weekly> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?DocID=SGR/SGR20092/NAT/ATO/00001> | Not re-read for this format update; see retained provenance |
| ATO, selected passages | <https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers> | 2026-11-02; selected visa, taxable termination payment and unused-leave scope passages |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments> | Not re-read for this format update; see retained provenance |
| ATO, selected passages | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/working-out-the-whole-of-income-cap-amount> | 2026-11-02; selected income, earlier-payment and mixed-payment passages; conflicting exclusion-list wording retained as a review gap |
| ATO, selected passages | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/the-12-month-rule> | 2026-11-02; statutory exceptions and determination overview; full operative instruments not reviewed |

| DSS, selected pension age tables | <https://guides.dss.gov.au/social-security-guide/3/4/1/10> | 2026-11-02; current and historical birth cohorts; Firecrawl after local browser challenge |
| Federal Register, ITAA 1997 compilation 268, Volume 3 | <https://www.legislation.gov.au/C2026C00471/latest/text> | 2026-11-02; selected ss 82-10, 82-65 to 82-75, 82-130 to 82-160 and 83-170 to 83-180; not the whole Act |
| ATO, qualifying earnings | <https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/what-payments-are-qualifying-earnings> | 2026-11-02; re-used current capture, Table 13 and example 7 re-read; historical OTE rules not re-audited |

### Section 13 - Sources

- Income Tax Assessment Act 1997, Division 82 (employment termination payments) and Division 83 (unused leave, genuine redundancy and early retirement scheme payments), https://www.ato.gov.au/law/view/document?docid=PAC/19970038/82-130
- Taxation Administration Act 1953, Schedule 1, sections 12-85 and 12-90 (withholding from ETPs and unused leave payments).
- ATO, Schedule 11 tax table for employment termination payments (from 1 July 2026), https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments
- ATO, Schedule 7 tax table for unused leave payments on termination of employment (from 1 July 2026), https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment
- ATO, Taxation of termination payments, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments
- ATO, Payments that are ETPs, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/payments-that-are-etps
- ATO, Tax-free component of ETPs, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps
- ATO, Redundancy and early retirement, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement
- ATO, Accrued leave, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/accrued-leave
- ATO, Applying the ETP caps, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps
- ATO, Working out the whole-of-income cap amount, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/working-out-the-whole-of-income-cap-amount
- ATO, The 12-month rule, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/the-12-month-rule
- ATO, TR 2009/2 Income tax: genuine redundancy payments, https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001
- ATO, SGR 2009/2 Superannuation guarantee: meaning of the terms ordinary time earnings and salary or wages, https://www.ato.gov.au/law/view/document?DocID=SGR/SGR20092/NAT/ATO/00001
- ATO, Schedule 15 tax table for working holiday makers, https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers

The retained guide recorded source checks on 27 September 2026. The selected current reads above have their own scope and date; that older statement does not establish a complete current source audit.

> **Working paper only, not a lodged return.** Have a qualified Australian CPA or CA review this before paying or reporting a termination package. Genuine redundancy status and early retirement scheme approval turn on the facts of the dismissal.
>
> Contributed by Ryan Duguid.

Not yet confirmed: Full-guide professional Australian review and the complete current STP/software submission, amendment, finalisation and payment workflow remain outstanding. The precise reporting code for an age-only excluded redundancy, the ATO mixed-payment wording conflict and affected approved-software behaviour require qualified reconciliation before an affected submission. Full operative late-payment determinations, historical commencement, all earlier cap assessments and tax-table lookup implementations have not been independently reconstructed. Current register compilation 268 is effective from 1 October 2026 and its metadata shows a next-version boundary on 1 December 2026; later statutory amendments and their relevance to this guide are not yet reconciled. Retained citations not re-read above keep their original provenance; structure and arithmetic checks do not establish every retained rule or actual taxpayer eligibility.

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
