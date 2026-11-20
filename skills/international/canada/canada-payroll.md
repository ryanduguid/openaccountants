---
name: canada-payroll
description: Use this skill whenever asked about Canadian payroll, source deductions, CPP contributions, EI premiums, or employer obligations in Canada. Trigger on phrases like "source deductions", "CPP", "Canada Pension Plan", "CPP2", "EI", "employment insurance", "T4", "TD1", "payroll deductions", "CRA payroll", "remittance", "ROE", "record of employment", "statutory holiday pay", "vacation pay Canada", "minimum wage Canada", "provincial tax", "payroll Canada", "PD7A", "remitter type", or any question about running payroll in Canada. This skill covers federal rules; Quebec (QPP/QPIP) differences are noted but not fully detailed. ALWAYS read this skill before processing any Canadian payroll work.
version: 1.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-21
reviewed_by: Edgar Lautsyus
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada Payroll

## Canada -- Payroll Skill v1.1

> **Review history.** Nathan Wiebe reviewed the earlier rates and thresholds on 21 June 2026. Edgar Lautsyus signed off the earlier guide, as recorded in the frontmatter and on the roster in `PARTNERS.md`. This version updates selected contributions, pay examples, minimum wage rates and EI benefits from the cited authorities. It awaits renewed practitioner review.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD ($) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (federal); Canada Pension Plan Act; Employment Insurance Act; Canada Labour Code (federal employees) |
| Tax authority | Canada Revenue Agency (CRA) |
| Reporting system | T4/T4A information returns; PD7A remittance voucher |
| Pay frequency | Biweekly (most common), semi-monthly, monthly, weekly |
| Employer registration | Business Number (BN) + payroll program account (RP) via CRA |
| Provincial variation | Each province/territory has its own income tax brackets, ESA, and minimum wage |
| Practitioner review | Prior rates review on 21 June 2026. This version awaits renewed review. |
| Skill version | 1.1 |

## Section 2 -- Income Tax Withholding (Source Deductions)

Employers withhold both federal and provincial/territorial income tax from each pay. CRA publishes payroll deduction tables (T4032) and formulas (T4127) annually.

### Federal Tax Brackets (2026)

**Federal Tax Brackets (2026)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 58,523 | 14% |
| 58,523 -- 117,045 | 20.5% |
| 117,045 -- 181,440 | 26% |
| 181,440 -- 258,482 | 29% |
| 258,482+ | 33% |

- **Lowest bracket rate change** — The lowest bracket rate was reduced from 15% to 14% effective for the 2026 tax year (enacted via 2025 tax reform).

### Federal Basic Personal Amount (BPA) -- 2026

**Federal Basic Personal Amount (BPA) -- 2026**

| Income Level | BPA (CAD) |
| --- | --- |
| Up to $181,440 | $16,452 |
| $181,440 -- $258,482 | Claws back to $14,829 |
| Above $258,482 | $14,829 |

### Provincial/Territorial Tax

Each province has its own tax brackets applied on top of federal tax. The employer determines the applicable province based on the employee's **province of employment** (where they physically report to work). Employees complete a federal TD1 and a provincial TD1 form.

### Key Provincial Top Marginal Rates (Combined Federal + Provincial, 2026)

**Key Provincial Top Marginal Rates (Combined Federal + Provincial, 2026)**

| Province | Top Combined Rate (approx.) |
| --- | --- |
| Ontario | ~53.5% |
| British Columbia | ~53.5% |
| Alberta | ~48.0% |
| Quebec | ~53.3% |
| Manitoba | ~50.4% |
| Saskatchewan | ~47.5% |

## Section 3 -- Social Security: Employee Deductions

### Canada Pension Plan (CPP) -- 2026

**Canada Pension Plan (CPP) -- 2026**

| Component | Rate (Employee) | Ceiling | Maximum Contribution |
| --- | --- | --- | --- |
| CPP base + first additional | 5.95% | YMPE $74,600 (less $3,500 basic exemption) | $4,230.45 |
| CPP2 (second additional) | 4.00% | Earnings between YMPE $74,600 and YAMPE $85,000 | $416.00 |

- **Basic exemption** — $3,500 a year, allocated by pay period. For 26 biweekly pays, use the CRA exemption of $134.61. [CRA contribution rates, maximums and exemptions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums.html)
- **CPP age eligibility** — CPP applies to employees aged 18--69 (mandatory 18--65; elective 65--70)
- **CPP2** — CPP2 is a second tier introduced in 2024 on earnings between the first and second ceilings

### Employment Insurance (EI) -- 2026

**Employment Insurance (EI) -- 2026**

| Item | Rate | Maximum Insurable Earnings | Maximum Annual Premium |
| --- | --- | --- | --- |
| Employee (Canada except Quebec) | 1.63% | $68,900 | $1,123.07 |
| Employee (Quebec -- reduced for QPIP) | 1.30% | $68,900 | $895.70 |

Use the 2026 rows for insurable earnings paid in 2026. [CRA Employment Insurance premium rates and maximums](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rate-maximum.html)

### Quebec Differences

For 2026, the employee and employer each pay Quebec Pension Plan (QPP) base and first additional contributions at 6.30%, subject to the $3,500 exemption, $74,600 earnings ceiling and $4,479.30 annual maximum. The second additional contribution is 4.00% each on pensionable earnings between $74,600 and $85,000, capped at $416.00 each. Quebec Parental Insurance Plan (QPIP) premiums are separate. Use 0.430% and a $442.90 maximum for employees, and 0.602% and a $620.06 maximum for employers, on up to $103,000 of insurable earnings. [Revenu Québec 2026 employer changes](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/)

## Section 4 -- Social Security: Employer Contributions

### CPP Employer Contributions -- 2026

**CPP Employer Contributions -- 2026**

| Component | Rate | Maximum |
| --- | --- | --- |
| CPP base + first additional | 5.95% (matches employee) | $4,230.45 |
| CPP2 | 4.00% (matches employee) | $416.00 |

- **Employer CPP matching** — Employer CPP contributions mirror the employee amount exactly (1:1 match).

### EI Employer Contributions -- 2026

**EI Employer Contributions -- 2026**

| Item | Rate | Maximum |
| --- | --- | --- |
| Employer (Canada except Quebec) | 2.282% (1.4× employee rate) | $1,572.30 |
| Employer (Quebec) | 1.820% (1.4× employee rate) | $1,253.98 |

[CRA Employment Insurance premium rates and maximums](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rate-maximum.html)

- **Employer EI multiplier** — The employer pays 1.4 times the employee EI premium. Employers may apply for an EI premium reduction if they have a qualifying short-term disability plan.

### Workers' Compensation

Provincial/territorial requirement. Premiums vary by industry classification and province. Typically $0.50--$3.00 per $100 of insurable earnings for office workers; higher for construction/manufacturing.

### Employer Health Tax (Select Provinces)

**Employer Health Tax (Select Provinces)**

| Province | Threshold | Rate |
| --- | --- | --- |
| Ontario (EHT) | $1,000,000 | 0.98%--1.95% |
| British Columbia (EHT) | $1,000,000 | 1.95% (above $1,500,000); 5.85% of remuneration exceeding $1,000,000 (between $1M–$1.5M) |
| Manitoba (HE levy) | $2,250,000 | 2.15%--4.3% |
| Quebec (HSF) | All payroll | 1.65%--4.26% |

## Section 5 -- Minimum Wage and Overtime

### Federal Minimum Wage

- **Federal minimum wage** — The general federal floor is $18.15 an hour from 1 April 2026. For federally regulated employment, use the higher of that floor and the applicable general provincial or territorial minimum under section 178(2). Check any separate category or exception. [Canada Labour Code, s 178](https://laws-lois.justice.gc.ca/eng/acts/L-2/section-178.html) · [Service Canada general minimum wages](https://minwage-salairemin.service.canada.ca/en/general.html?01cb4aff_page=1&1353fe24_page=3&50976b45_page=2&663d1f65_page=1&dbe437e9_page=2)

### Select Provincial Minimum Wages (2026)

**Select Provincial Minimum Wages (2026)**

| Province | General rate (CAD/hour) at 21 November 2026 | Effective from |
| --- | --- | --- |
| Ontario | $17.95 | 1 October 2026 |
| British Columbia | $18.25 | 1 June 2026 |
| Alberta | $15.00 | 26 June 2019 |
| Quebec | $16.60 | 1 May 2026 |
| Manitoba | $16.40 | 1 October 2026 |
| Saskatchewan | $15.70 | 1 October 2026 |

Check the pay date and any occupation or worker exceptions. [Service Canada general minimum wages](https://minwage-salairemin.service.canada.ca/en/general.html?01cb4aff_page=1&1353fe24_page=3&50976b45_page=2&663d1f65_page=1&dbe437e9_page=2)

### Overtime

**Overtime**

| Jurisdiction | Threshold | Rate |
| --- | --- | --- |
| Federal | 8 hrs/day or 40 hrs/week | 1.5× regular rate |
| Ontario | 44 hrs/week | 1.5× regular rate |
| British Columbia | > 8 hrs/day or > 40 hrs/week | 1.5×; > 12 hrs/day = 2× |
| Alberta | > 8 hrs/day or > 44 hrs/week | 1.5× regular rate |
| Quebec | > 40 hrs/week | 1.5× regular rate |

## Section 6 -- Mandatory Benefits

### Vacation Pay

**Vacation Pay**

| Jurisdiction | After 1 Year | After 5+ Years |
| --- | --- | --- |
| Federal | 4% (2 weeks) | 6% (3 weeks) |
| Ontario | 4% (2 weeks) | 6% (3 weeks after 5 years) |
| British Columbia | 4% (2 weeks) | 6% (3 weeks after 5 years) |
| Alberta | 4% (2 weeks) | 6% (3 weeks after 5 years) |
| Quebec | 4% (2 weeks) initially; 6% after 3 years | 6% (3 weeks) |
| Saskatchewan | 5.77% (3 weeks) | 7.69% (4 weeks after 10 years) |

### Statutory / Public Holidays

9 federal statutory holidays. Provincial holidays vary (6--10 per province). Employees are entitled to the statutory holiday with pay or premium pay (typically 1.5× or time off in lieu) if they work on the holiday.

### Sick Leave

**Sick Leave**

| Jurisdiction | Paid Days | Unpaid Days |
| --- | --- | --- |
| Federal | 10 paid (after 30 days of service) | -- |
| Ontario | 3 paid | -- |
| British Columbia | 5 paid | 3 unpaid |
| Quebec | 2 paid (after 3 months) | 24 unpaid |
| Alberta | 0 paid | 16 unpaid |

### Maternity / Parental Leave (EI Benefits)

**Maternity / Parental Leave (EI Benefits)**

| Benefit | Maximum weeks | Rate and 2026 weekly maximum |
| --- | --- | --- |
| Maternity (birth parent only) | 15 | 55% of average insurable weekly earnings, capped at $729 |
| Standard parental | 35 per parent, 40 shared | 55% of average insurable weekly earnings, capped at $729 |
| Extended parental | 61 per parent, 69 shared | 33% of average insurable weekly earnings, capped at $437 |

Quebec residents use Quebec's separate maternity and parental benefits programme. [Service Canada maternity and parental benefits](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental.html)

- **Top-up and waiting period** — Check the employment agreement for any employer top-up. Service Canada waives the usual one-week waiting period for new EI claims starting from 30 March 2025 to 9 October 2027. A claimant may serve it where a Supplemental Unemployment Benefit plan top-up makes that advantageous. [Service Canada temporary EI measures](https://www.canada.ca/en/services/benefits/ei/temporary-measures-for-major-economic-conditions.html)

### Group Benefits

Not legally mandated, but most Canadian employers provide extended health, dental, life insurance, and short/long-term disability as part of competitive compensation.

## Section 7 -- Payslip Requirements

The Canada Labour Code (federal) and provincial Employment Standards Acts require employers to provide a pay statement each pay period.

### Mandatory Payslip Contents

- Pay period dates
- Gross earnings
- All deductions itemised (CPP, EI, federal tax, provincial tax, other)
- Net pay
- Hours worked (if hourly)
- Rate of pay
- Overtime hours and pay (if applicable)
- Vacation pay (if applicable)

### Additional Requirements by Province

Ontario requires the employer's name and address, the employee's name, and the pay period. Quebec requires similar plus contribution details. Most provinces align with the above minimum.

## Section 8 -- Filing Obligations

### Remittance of Source Deductions

**Remittance of Source Deductions**

| Remitter Type | Threshold (Avg Monthly Withholding) | Due Date |
| --- | --- | --- |
| Quarterly | < $1,000 (new, perfect compliance) | 15th of month after quarter end |
| Regular | < $25,000 | 15th of following month |
| Threshold 1 accelerated | $25,000 -- $99,999.99 | Twice monthly (15th and month-end) |
| Threshold 2 accelerated | ≥ $100,000 | Up to 4 times per month (within 3 business days of pay date) |

### Year-End Filing (T4)

**Year-End Filing (T4)**

| Task | Deadline |
| --- | --- |
| T4 slips to employees | Last day of February (next business day if falls on weekend) |
| T4 Summary to CRA | Last day of February |
| T4A slips (contract/other income) | Last day of February |
| Quebec: RL-1 slips to employees and Revenu Québec | Last day of February |

### Record of Employment (ROE)

- **ROE issuance** — Must be issued within 5 calendar days of an interruption in earnings (layoff, leave, termination, etc.). Filed electronically via ROE Web.

### Penalties

**Penalties**

| Violation | Penalty |
| --- | --- |
| Late remittance | 3% (1--3 days late) to 10% (7+ days late) + arrears interest |
| Failure to deduct | Employer liable for undeducted amounts + 10% penalty |
| Late T4 filing | Min $100, max $7,500; daily penalty depends on number of slips filed late |
| Failure to issue ROE | Up to $2,000 fine and/or 6 months imprisonment |

## Section 9 -- Common Payroll Patterns

### Pattern 1 -- Biweekly Employee (Ontario)

Annual salary $75,000. Paid biweekly (26 pay periods).

1. Gross per period: $75,000 ÷ 26 = $2,884.62
2. CPP: ($2,884.62 - $134.61 exemption) × 5.95% = $163.63, assuming enough remaining annual CPP contribution room.
3. CPP2: apply 4.00% to the portion of the pay crossing the applicable year-to-date YMPE threshold, subject to remaining CPP2 room. The salary by itself does not establish the amount for this pay period.
4. EI: $2,884.62 × 1.63% = $47.02, assuming enough remaining annual EI premium room.
5. Federal tax: per T4032 table for biweekly pay.
6. Ontario provincial tax: per T4032-ON table.
7. Employer CPP: $163.63 (matches employee).
8. Employer EI at the standard multiplier: $47.02 × 1.4 = $65.83.

[CRA T4127, 122nd edition from 1 January 2026, chapter 6](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html). The [July 2026 edition](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jul-123rd-edition-effective-july-1-2026/t4127-jul-payroll-deductions-formulas.html) refers readers to the January edition for sections it omits.

```oa-check
name: Ontario biweekly CPP and EI with remaining contribution room
inputs:
  gross: 2884.62
  cpp_exemption: 134.61
  cpp_rate: 0.0595
  ei_rate: 0.0163
  ei_employer_multiple: 1.4
steps:
  - employee_cpp: round((gross - cpp_exemption) * cpp_rate, 2)
  - employee_ei: round(gross * ei_rate, 2)
  - employer_ei: round(employee_ei * ei_employer_multiple, 2)
expected:
  employee_cpp: 163.63
  employee_ei: 47.02
  employer_ei: 65.83
```

### Pattern 2 -- Employee Reaching CPP Maximum

An employee outside Quebec earns $80,000 of pensionable earnings from the same employer over 24 semi-monthly pays in 2026. Assume full-year CPP eligibility, with $3,333.33 in each of the first 23 pays and $3,333.41 in the last. Year-to-date pensionable earnings are $73,333.26 after pay 22 and $76,666.59 after pay 23. Pay 23 takes earnings above the $74,600 YMPE and reaches the $4,230.45 first-tier CPP maximum. CPP2 is $82.66 on pay 23 and $133.34 on pay 24, for $216.00 for the year. Earnings stay below the $85,000 YAMPE. [CRA T4127, 122nd edition from 1 January 2026, chapter 6 and appendix 1](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)

```oa-check
name: Semi-monthly CPP2 crossing and year-end top-up
inputs:
  standard_pay: 3333.33
  last_pay: 3333.41
  ympe: 74600
  cpp2_rate: 0.04
steps:
  - pay_22_earnings: standard_pay * 22
  - pay_23_earnings: standard_pay * 23
  - cpp2_pay_23: round((pay_23_earnings - ympe) * cpp2_rate, 2)
  - cpp2_pay_24: round(last_pay * cpp2_rate, 2)
  - cpp2_total: cpp2_pay_23 + cpp2_pay_24
expected:
  pay_22_earnings: 73333.26
  pay_23_earnings: 76666.59
  cpp2_pay_23: 82.66
  cpp2_pay_24: 133.34
  cpp2_total: 216
```

### Pattern 3 -- Vacation Pay Payout

Employee earning $52,000/year with 4% vacation pay. Vacation pay accrues: $52,000 × 4% = $2,080/year. Can be paid on each cheque (added to gross, subject to all deductions) or accrued and paid when vacation is taken.

### Pattern 4 -- Termination with ROE

Employee terminated without cause. Final pay includes:
- Outstanding regular wages through last day
- Accrued vacation pay (mandatory payout)
- Termination pay (if applicable under ESA -- typically 1 week per year of service)
- Severance (Ontario: 1 week per year if 5+ years and employer payroll ≥ $2.5M)

Issue ROE within 5 days via ROE Web. Code M (dismissal) or other applicable code.

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Skill | Interaction |
| --- | --- |
| payroll-workflow-base | Provides generic payroll processing steps; this skill adds Canadian-specific rules |
| canada-bookkeeping | Payroll journals: salaries + ER CPP/EI + ER EHT/WCB to P&L; net pay + source deductions payable to BS |
| canada-corporate-tax | Employer CPP/EI and provincial health taxes are deductible business expenses |
| canada-gst-hst | No GST/HST on wages; but taxable benefits may trigger GST/HST |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
