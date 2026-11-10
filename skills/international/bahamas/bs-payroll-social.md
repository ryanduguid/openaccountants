---
name: bs-payroll-social
description: "Bahamas payroll and National Insurance contributions. Covers ordinary rates, the July 2026 wage ceiling change, employer statements, self-employment and arrears. Pending practitioner review."
jurisdiction: BS
category: payroll
tax_year: 2026
tax_year_notes: "Includes the 1 July 2024 rate change and the July 2026 ceiling transition. Source position checked through 10 November 2026."
last_updated: 2026-11-10
version: 1.2
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahamas Payroll & Social Contributions

## Payroll scope

Bahamian domestic personal income tax withholding is inapplicable for the period checked through 10 November 2026. Employers account for National Insurance Board (NIB) contributions on insurable wages. Apply the worker's contribution class and pay period before calculating a deduction. [Ministry of Finance guidance, ‘Scope of the MAP “Limitations”’](https://cdn.bahamas.gov.bs/tenant/tenantministryoffinance/documents/All%20Documents/BAHAMAS-JAPANMAPGUIDANCEDOCUMENT-20240718120503.pdf) · [National Insurance Act, ss 18–19](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/1972/1972-0021/1972-0021.pdf)

The Industrial Tribunal applied the BSD 260 weekly minimum wage from 1 January 2023 in its decision concerning a private employer. Check the applicable wage order, class of worker and pay basis before applying a floor. Under the ordinary Employment Act rules, standard hours are 8 a day and 40 a week. Overtime ordinarily attracts at least 1.5 times the regular rate, or twice the regular rate for overtime on a public holiday or day off. Check ss 8–10 for averaging, industry and managerial exceptions and the separate rule for tipped tourism and hospitality workers. [Industrial Tribunal, NR/NES/041, paras 124–125](https://www.industrialtribunal.bs/wp-content/uploads/2026/03/NR24-041-DEC.pdf) · [Employment Act, ss 8–10](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/2001/2001-0027/2001-0027_2.pdf)

## National Insurance rates and ceilings

The ordinary employee rate is 4.65% and the employer rate is 6.65%, a combined 11.3% of insurable wages from 1 July 2024. Ordinary self-employed contributors under 65 without retirement benefit pay 10.3% of insurable income. The voluntary rate is 6.5% for a person eligible for voluntary insurance. The NIB's July 2026 update confirms unchanged contribution rates. [S.I. 37 of 2024, regs 1, 4–7 and 9](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf) · [NIB rates sheet](https://www.nib-bahamas.com/UserFiles/HTMLEditor/Contribution-Rates-and-Insurable-Ceilings-2024.pdf) · [NIB July 2026 notice](https://www.nib-bahamas.com/uploads/2026_biennial_adjustments_f9ad1d917d.pdf)

| Period | Weekly ceiling | Monthly ceiling |
| --- | ---: | ---: |
| July 2024 schedule through June 2026 | BSD 810 | BSD 3,510 |
| From 1 July 2026 | BSD 830 | BSD 3,597 |

A contribution week runs Monday to Sunday. For weekly payroll use BSD 810 for the week beginning 29 June 2026 and BSD 830 beginning with the week of 6 July. NIB illustrates the increase for an ordinary employee who earns at least the new ceiling. The extra BSD 20 of insurable wages adds BSD 0.93 to the employee share and BSD 1.33 to the employer share for a week at the new ceiling. [Contributions Regulations, regs 2 and 52](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/SUBORDINATE/1984/1984-0068/1984-0068_2.pdf) · [NIB July 2026 notice](https://www.nib-bahamas.com/uploads/2026_biennial_adjustments_f9ad1d917d.pdf)

```oa-check
name: BS ordinary weekly payroll ceiling transition from 29 June to 6 July 2026
inputs:
  wages: 900
  old_ceiling: 810
  new_ceiling: 830
  employee_rate: 4.65
  employer_rate: 6.65
steps:
  - increase: min(wages, new_ceiling) - min(wages, old_ceiling)
  - employee_increase: pct(increase, employee_rate)
  - employer_increase: pct(increase, employer_rate)
expected:
  increase: 20
  employee_increase: 0.93
  employer_increase: 1.33
```

For an ordinary employee paid BSD 3,600 in qualifying basic wages for July 2026, the monthly insurable wages are BSD 3,597. The cap for June was BSD 3,510. [NIB July 2026 notice](https://www.nib-bahamas.com/uploads/2026_biennial_adjustments_f9ad1d917d.pdf)

```oa-check
name: BS monthly payroll ceilings for June and July 2026
inputs:
  monthly_wages: 3600
  june_ceiling: 3510
  july_ceiling: 3597
steps:
  - june_insurable: min(monthly_wages, june_ceiling)
  - july_insurable: min(monthly_wages, july_ceiling)
expected:
  june_insurable: 3510
  july_insurable: 3597
```

For an ordinary employee entitled to at least one week's notice of termination and paid a fixed salary or wage, use basic wages excluding any housing allowance, up to the applicable ceiling. Regulation 23(2) gives separate bases for employees paid wholly or partly by commission, fees or a share of sales or results and for other workers. Where reg 43 applies, count basic wages before qualifying gratuities within the combined ceiling. Check the NIB class and operative schedule before calculating contributions for retirement benefit recipients, workers aged 65 or older, summer workers, gratuities, concurrent jobs or other special cases. The NIB rates sheet and published schedule require reconciliation for some of these classes. [Contributions Regulations, regs 2, 23, 42–43 and Seventh Schedule](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/SUBORDINATE/1984/1984-0068/1984-0068_2.pdf) · [S.I. 37 of 2024](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf) · [NIB rates sheet](https://www.nib-bahamas.com/UserFiles/HTMLEditor/Contribution-Rates-and-Insurable-Ceilings-2024.pdf)

For continuing self-employment, reg 30 uses the income from the year ending 31 December before the contribution week. Regulation 2 and the First Schedule define the qualifying profit and restricted deductions. Check the separate transition rules that can apply up to the end of the first full calendar year of self-employment. They depend on whether the person was previously employed. Regulation 42(6)–(8) addresses a week with both employment and self-employment. [Contributions Regulations, regs 2, 30 and 42 and First Schedule](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/SUBORDINATE/1984/1984-0068/1984-0068_2.pdf)

## Registration, statements and payment

- NIB's employer guidance gives employers and self-employed people 10 working days from commencing operations to register with the Board. Employers submit Form R1. The Employer Self Service portal supports employee registration, contribution statements and payments. [NIB employer guidance](https://www.nib-bahamas.com/_m1758/Employers) · [NIB portals](https://www.nib-bahamas.com/portals)
- Under reg 26, employers normally pay both shares and file a monthly statement for each employee within 15 days after the month in which the wages are paid. Check the specific rules for advance wages, termination and approved arrangements. Regulation 32 gives the separate self-employed rule, normally payment by 15 days after month end. [Contributions Regulations, regs 25–26 and 32](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/SUBORDINATE/1984/1984-0068/1984-0068_2.pdf)
- The NIB's C10(A) instructions use the actual 4 or 5 contribution weeks according to the number of Mondays in the month for weekly paid employees. For monthly paid employees use the month's insurable wages. Use the ceiling and rates for the period concerned and check the current NIB filing route and rounding method. [NIB C10(A) instructions, points 6, 7 and 11](https://www.nib-bahamas.com/wp-content/uploads/2025/05/C10-A-INSTRUCTIONS-FOR-COMPLETING-C10-A-FORM-Revised-August-2015.pdf)

## Arrears

Section 55(1) provides for interest compounded annually at the prime rate, subject to regulations and any other prescribed rate and start date. Act 27 of 2024 added a discretionary ministerial waiver after consultation with the Board, addressed interest on employer recovery under s 54 and added the s 55A garnishee procedure from 1 July 2024. For an actual arrears balance, obtain the NIB's statement and confirm the applicable rate, dates and any waiver. [National Insurance Act, ss 2 and 54–55](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/1972/1972-0021/1972-0021.pdf) · [Act 27 of 2024, ss 1 and 5–7](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0027A/2024-0027A.pdf)

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
