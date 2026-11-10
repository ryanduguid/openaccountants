---
name: fj-payroll-social
description: Use this skill whenever asked about Fiji payroll processing for employed persons. Trigger on phrases like "Fiji payroll", "PAYE Fiji", "FNPF contribution", "Fiji National Provident Fund", "SRT Fiji", "Social Responsibility Tax", "ECAL Fiji", "Environment Climate Adaptation Levy", "FRCS PAYE", "tax withholding Fiji", "employer FNPF", "net salary Fiji", "minimum wage Fiji", "salary calculation Fiji", "gross to net Fiji", "TPOS Fiji", "FJD payroll", or any question about computing employee pay, withholding tax (PAYE/SRT/ECAL), or FNPF social contributions for Fiji-based employees. This skill covers PAYE income tax withholding (a final tax for employment-only income), Social Responsibility Tax, the Environment & Climate Adaptation Levy, FNPF employee and employer contributions, the national minimum wage, non-resident taxation, and FRCS/FNPF filing obligations. ALWAYS read this skill before processing any Fiji payroll.
jurisdiction: FJ
category: payroll
tax_year: 2025
last_updated: 2026-11-10
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# fiji-payroll

## Fiji Payroll Skill v0.1

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Fiji |
| Currency | FJD only (Fijian Dollar, $) |
| Standard pay frequency | Monthly or fortnightly (weekly permitted) |
| Tax year | Calendar year (1 January -- 31 December) [FRCS] |
| Tax withholding system | PAYE -- final withholding tax for employment-only income [FRCS, "New PAYE Structure" public notice] |
| Income tax authority | Fiji Revenue & Customs Service (FRCS) -- https://frcs.org.fj |
| Social contribution authority | Fiji National Provident Fund (FNPF) -- https://myfnpf.com.fj |
| Labour authority | Ministry of Employment, Productivity & Industrial Relations (MEPIR) |
| Key legislation | Income Tax Act 2015; Tax Administration Act 2009; Fiji National Provident Fund Act 2011; Employment Relations Act 2007 |
| Filing portal | FRCS Taxpayer Online Services (TPOS) |
| Has personal income tax? | YES -- collected via PAYE as a final tax |
| Validated by | Pending -- requires sign-off by a Fiji-licensed accountant |
| Skill version | 0.1 |

### Statutory Payroll Components at a Glance (resident employee)

**Statutory Payroll Components at a Glance**

| Component | Employee | Employer | Base / threshold |
| --- | --- | --- | --- |
| Income tax (PAYE) | 0% -- 39% progressive | withhold & remit | tax-free to $30,000; 20% to $270,000, then 33% -- 39% [FRCS Tax Rates, 2024 onwards] |
| Social Responsibility Tax (SRT) | integrated into PAYE brackets from 1 Jan 2024 | none separately | not charged on top [FRCS "New PAYE Structure" notice] |
| Environment & Climate Adaptation Levy (ECAL) on income | not charged from 2024 | none | 2024 PAYE template excludes ECAL [FRCS "New PAYE Structure" notice] |
| FNPF | 8% | 10% | gross ordinary wages, no cap [FNPF Employers, eff. 1 Jan 2024] |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP -- ask. Non-residents have NO tax-free threshold (20% from the first dollar to $270,000) |
| Unknown whether income exceeds $270,000 | Treat as below $270,000 (20% marginal) and flag to reviewer if near threshold |
| Unknown FNPF membership / age | Treat employee aged 15+ as FNPF-mandatory; STOP if under 15 |
| Unknown whether figure is "ordinary wages" vs total remuneration | Use ordinary/gross wages for FNPF; STOP if composition unclear |
| Unknown pay frequency | Assume monthly; annualise for bracket computation |
| Voluntary FNPF top-ups | Assume none unless evidenced |
| Sector minimum wage applies | STOP -- check for a Wages Regulation Order before assuming national minimum |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — gross (ordinary) wages for the period, pay frequency, residency status (resident / non-resident), and confirmation the employee is an FNPF member (or eligible, aged 15+).
- **Recommended inputs** — annualised gross, FNPF member number, FRCS Tax Identification Number (TIN), employment start date, age, and any voluntary FNPF election.
- **Ideal inputs** — full payslip history for the year (for cumulative PAYE reconciliation), employment contract showing ordinary wage vs allowances, sector/industry (to check Wages Regulation Orders), and bank statements showing salary credits and statutory remittances.

### Refusal Catalogue

- **R-FJ-1 -- Residency unknown** — Resident employees get a $30,000 tax-free threshold; non-residents are taxed at 20% from the first dollar up to $270,000, then 33% to 39% (2024 non-resident table) [FRCS]. Confirm residency status before computing PAYE.  _(FRCS)_
- **R-FJ-2 -- High-earner thresholds** — Chargeable income above $270,000 falls in the 33% to 39% PAYE bands, which integrate SRT from 1 January 2024; no separate SRT or ECAL is withheld. If annual chargeable income is at or near $270,000, escalate to a licensed accountant for review.  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ (resident table "from the 2024 tax year onwards"; SRT row "Till 31st December 2023"); FRCS "New PAYE Structure" notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ (SRT integrated into the PAYE brackets from 1 January 2024; 2024 template excludes SRT and ECAL))_
- **R-FJ-3 -- ECAL on income** — Not charged from 2024: FRCS's 2024 PAYE template excludes SRT and ECAL. Do not withhold ECAL on income.  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ (resident table "from the 2024 tax year onwards"; SRT row "Till 31st December 2023"); FRCS "New PAYE Structure" notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ (SRT integrated into the PAYE brackets from 1 January 2024; 2024 template excludes SRT and ECAL))_
- **R-FJ-4 -- Penalty figures** — Specific FRCS PAYE penalties and the FNPF late-payment penalty rate were not confirmed from primary sources [RESEARCH GAP]. Do not state exact penalty amounts — refer to 'penalties under the Tax Administration Act 2009 / FNPF Act 2011' and escalate.
- **R-FJ-5 -- Termination / final pay / redundancy** — Termination pay, redundancy, and leave-on-termination computations are outside this skill's scope. Escalate to a licensed accountant.
- **R-FJ-6 -- Fringe benefits / non-cash remuneration** — Fringe benefit tax and the taxation of non-cash benefits are outside this skill's scope. Escalate to a licensed accountant.

## Section 3 -- PAYE Income Tax Withholding (Residents)

- **PAYE deduction and final tax rule** — The employer deducts PAYE each pay period using the FRCS tax tables / the 2024 PAYE Regulation 6 formula and an approved calculator/Excel filing template [FRCS]. PAYE is a final tax for employees whose only income is employment income — those employees do not file an annual return [FRCS, "New PAYE Structure" notice].  _(FRCS, "New PAYE Structure" notice)_

### 3.1 Resident PAYE Brackets (tax year 2024 onwards; current for 2025) [FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/]

**Resident PAYE Brackets**  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ (resident table "from the 2024 tax year onwards"; SRT row "Till 31st December 2023"); FRCS "New PAYE Structure" notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ (SRT integrated into the PAYE brackets from 1 January 2024; 2024 template excludes SRT and ECAL))_

| Chargeable income (FJD) | Income tax |
| --- | --- |
| 0 -- 30,000 | Nil (tax-free threshold = $30,000) |
| 30,001 -- 50,000 | 18% of excess over $30,000 |
| 50,001 -- 270,000 | $3,600 + 20% of excess over $50,000 |
| 270,001 -- 300,000 | $47,600 + 33% of excess over $270,000 |
| 300,001 -- 350,000 | $57,500 + 34% of excess over $300,000 |
| 350,001 -- 400,000 | $74,500 + 35% of excess over $350,000 |
| 400,001 -- 450,000 | $92,000 + 36% of excess over $400,000 |
| 450,001 -- 500,000 | $110,000 + 37% of excess over $450,000 |
| 500,001 -- 1,000,000 | $128,500 + 38% of excess over $500,000 |
| 1,000,001+ | $318,500 + 39% of excess over $1,000,000 |

- **Top income-tax marginal rate** — The top income-tax marginal rate is 39% above $1,000,000. SRT is integrated into these brackets from 1 January 2024 (Section 4) and ECAL on income is not charged (Section 5); nothing stacks on top.  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ (resident table "from the 2024 tax year onwards"; SRT row "Till 31st December 2023"); FRCS "New PAYE Structure" notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ (SRT integrated into the PAYE brackets from 1 January 2024; 2024 template excludes SRT and ECAL))_

Bracket note: The FRCS Tax Rates page's "Year of Assessment 2022 Onwards" table (20% income tax plus a separate 18% -- 24% SRT column) covers 2022 and 2023 only; FRCS's SRT rate table ends "Till 31st December 2023". Do not use it for 2024 or later.

### 3.2 Computation Method

- **PAYE computation method** — Annual income tax = bracket base + (rate × (chargeable income − bracket floor)) Period PAYE        = annual income tax ÷ number of pay periods (cumulatively adjusted)  _(FRCS)_
- **Tax-free threshold as personal allowance** — PAYE is computed on annualised chargeable income, divided across pay periods, and trued up cumulatively over the year via the FRCS PAYE formula. The $30,000 tax-free threshold IS the personal allowance — there is no separate allowance.  _(FRCS)_

## Section 4 -- Social Responsibility Tax (SRT) -- Integrated into PAYE from 2024

- **SRT integrated** — From 1 January 2024 SRT is integrated into the PAYE brackets above $270,000 (Section 3.1). Do not compute or withhold SRT separately for 2024 or later. The separate SRT schedule (18% -- 24% above $270,000) applied to 2022 and 2023 only.  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ (resident table "from the 2024 tax year onwards"; SRT row "Till 31st December 2023"); FRCS "New PAYE Structure" notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ (SRT integrated into the PAYE brackets from 1 January 2024; 2024 template excludes SRT and ECAL))_

## Section 5 -- Environment & Climate Adaptation Levy (ECAL) on Income

- **ECAL on income not charged** — FRCS's 2024 PAYE template excludes ECAL, and FRCS's last income table with an ECAL column is Year of Assessment 2020 and 2021 (5% of excess over $270,000). Do not withhold ECAL on income for 2024 or later.  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ (resident table "from the 2024 tax year onwards"; SRT row "Till 31st December 2023"); FRCS "New PAYE Structure" notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ (SRT integrated into the PAYE brackets from 1 January 2024; 2024 template excludes SRT and ECAL))_

Note: ECAL also applies separately to prescribed services and certain luxury items — these are not payroll-relevant and are out of scope here.

## Section 6 -- Non-Resident Employees

**Non-resident rules table**

| Rule | Detail | Source |
| --- | --- | --- |
| PAYE rate | **20% from the first dollar** to $270,000 — NO $30,000 tax-free threshold. Above $270,000: $54,000 + 33% of excess, rising to $324,900 + 39% of excess over $1,000,000 | FRCS Tax Rates (non-resident table, 2024 onwards) |
| SRT | Integrated into the non-resident PAYE brackets from 2024; not charged separately | FRCS "New PAYE Structure" notice |
| ECAL on income | Not charged from 2024 | FRCS "New PAYE Structure" notice |
| FNPF | FNPF covers employees working in Fiji; applicability to short-term non-resident assignees **[RESEARCH GAP — reviewer to confirm coverage rules for non-residents]** | FNPF Act 2011 |

## Section 7 -- FNPF -- Mandatory Social / Pension Contributions

- **FNPF effective date** — FNPF is the primary mandatory social contribution. Rates are effective 1 January 2024 and confirmed current for 2025.  _(FNPF "Employers" -- https://myfnpf.com.fj/employers/)_

### 7.1 Contribution Rates

**Contribution Rates table**

| Party | Rate | Base |
| --- | --- | --- |
| Employee | 8% | gross / ordinary wages |
| Employer | 10% | gross / ordinary wages |
| **Total compulsory** | **18%** |  |

Arithmetic check: 8% (employee) + 10% (employer) = 18% total. ✓

### 7.2 Rules

**FNPF Rules table**

| Rule | Detail | Source |
| --- | --- | --- |
| Ceiling / cap | NONE — contributions on full ordinary wages | FNPF Employers |
| Minimum floor | None stated by FNPF — contributions on actual wages | FNPF Employers |
| Voluntary top-ups | Employer may pay voluntary additional contributions above the mandated 10% | FNPF Employers |
| Coverage | Employers must register all employees aged 15+ not already members (Registration of Employee Form) | FNPF Employers |
| Remittance frequency | Monthly | FNPF Employers |
| Schedule / payment deadline | Schedule due by the **14th**; payment by end of month / last working day following the contribution month | **[RESEARCH GAP — secondary employer guides; FNPF page states only "payable monthly"]** |
| Late-payment penalty | Reported at **10% per month** on the outstanding amount | **[RESEARCH GAP — reviewer to confirm against FNPF Act 2011]** |

## Section 8 -- PAYE Employer Obligations, Filing & Remittance

**PAYE Employer Obligations table**  _(FRCS PAYE structure notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/; corroborated by employer guides)_

| Obligation | Detail |
| --- | --- |
| Registration | Employer must register with FRCS for PAYE and hold a TIN; employees must have TINs |
| Deduction | Deduct PAYE (SRT integrated from 2024; no ECAL on income) each pay period using FRCS tax tables / 2024 PAYE Regulation 6 formula |
| Final tax | PAYE is a final tax for employees with employment income only — no annual return required |
| Filing portal | FRCS Taxpayer Online Services (TPOS) |
| Monthly return + remittance | By the **15th of the following month** **[RESEARCH GAP — from employer guides; not captured verbatim from a primary FRCS page]** |
| Penalties | Penalties and interest for late filing/payment under the Tax Administration Act 2009; exact amounts vary **[RESEARCH GAP — no specific statutory figure confirmed from a primary source]** |

## Section 9 -- Minimum Wage

**Minimum Wage table**

| Item | Value | Source |
| --- | --- | --- |
| National minimum wage | **FJD $5.00 per hour**, effective 1 April 2025 | Fiji Govt -- https://www.fiji.gov.fj/Media-Centre/News/MINIMUM-WAGE-INCREASE-TO-$5-00-AN-HOUR-BY-1ST-APRI |
| Phasing | $4.00 → $4.50 (1 Aug 2024) → $5.00 (1 Apr 2025) | WageIndicator |
| Sector minimums | Wages Regulation Orders apply on top in certain industries (e.g. construction foreman ~$7.54/hr from Apr 2025) | WageIndicator |
| Governing law | Employment Relations Act 2007; underpayment is a criminal offence | MEPIR |

## Section 10 -- Corporate Income Tax (Context -- Not Payroll)

**Corporate Income Tax table**

| Item | Value | Source |
| --- | --- | --- |
| Standard corporate income tax rate | **25%** (2024) | FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ |
| Concessions | E.g. 15% for up to 7 years for qualifying entities; reduced rate for new South Pacific Stock Exchange listings | FRCS Tax Rates |

Note: One aggregator cited 20%; the FRCS Tax Rates page states 25%. Use the FRCS figure (25%).

## Section 11 -- Transaction / Payment Pattern Library

### 11.1 Salary Credits (employee bank statement -- credits)

**Salary Credits table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| SALARY, PAY, WAGES, NET PAY | Net salary payment | After PAYE + 8% FNPF withheld |
| FORTNIGHT PAY, MONTHLY SALARY | Net salary payment | Confirm pay frequency for annualisation |
| BACK PAY, ARREARS | Net salary (catch-up) | May straddle periods — re-annualise PAYE |
| FNPF REFUND, FNPF ADJUSTMENT | Contribution adjustment | NOT income |

### 11.2 Employer Debit Patterns (employer bank statement -- debits)

**Employer Debit Patterns table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| FRCS, PAYE, TAX REMITTANCE, TPOS | PAYE remittance to FRCS | Liability until remitted |
| FNPF, FNPF CONTRIBUTION, FNPF EMPLOYER | FNPF contribution (8% employee + 10% employer) | Employer 10% is an expense; employee 8% is withheld |
| NET WAGES, PAYROLL RUN, SALARY DISBURSEMENT | Net salary disbursement to employees |  |
| FNPF VOLUNTARY | Voluntary FNPF top-up | Confirm policy/contract |

### 11.3 Exclusions

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Not a payroll transaction |
| LOAN, ADVANCE REPAYMENT | EXCLUDE from PAYE base | Not remuneration unless contractually pay |
| EXPENSE REIMBURSEMENT | EXCLUDE | Reimbursement, not wages (confirm composition) |

## Section 12 -- Worked Examples

All figures in FJD. PAYE per Section 3.1; FNPF per Section 7.1 (employee 8%, employer 10%). Examples assume employment income only and full-year employment unless stated.

### Example 1 -- Resident below the tax-free threshold ($20,000/yr)

**Input:** Resident, annual gross ordinary wages $20,000.

```
PAYE: $20,000 < $30,000 threshold              = $0
FNPF (employee 8%): 0.08 × 20,000              = $1,600.00
Total employee deductions                       = $1,600.00
Net pay                                          = 20,000 − 1,600 = $18,400.00
Employer FNPF (10%): 0.10 × 20,000             = $2,000.00
Total employer cost                              = 20,000 + 2,000 = $22,000.00
```

### Example 2 -- Resident in the 18% band ($45,000/yr)

**Input:** Resident, annual gross $45,000. Monthly pay.

```
PAYE: 18% × (45,000 − 30,000) = 0.18 × 15,000  = $2,700.00
FNPF (employee 8%): 0.08 × 45,000              = $3,600.00
Total employee deductions                       = 2,700 + 3,600 = $6,300.00
Net pay (annual)                                = 45,000 − 6,300 = $38,700.00
Employer FNPF (10%): 0.10 × 45,000             = $4,500.00
─ Monthly view ─
Gross 45,000/12                                 = $3,750.00
PAYE 2,700/12                                   = $225.00
FNPF 3,600/12                                   = $300.00
Net monthly = 3,750 − 225 − 300                 = $3,225.00
```

### Example 3 -- Resident in the 20% band ($80,000/yr)

**Input:** Resident, annual gross $80,000.

```
PAYE: 3,600 + 20% × (80,000 − 50,000)
     = 3,600 + 0.20 × 30,000 = 3,600 + 6,000   = $9,600.00
Below $270,000: 33% -- 39% bands not reached
FNPF (employee 8%): 0.08 × 80,000              = $6,400.00
Total employee deductions                       = 9,600 + 6,400 = $16,000.00
Net pay                                          = 80,000 − 16,000 = $64,000.00
Employer FNPF (10%): 0.10 × 80,000             = $8,000.00
```

### Example 4 -- High earner above $270,000 ($320,000/yr)

**Input:** Resident, annual chargeable income $320,000.

```
Income tax (PAYE): 57,500 + 34% × (320,000 − 300,000)
     = 57,500 + 0.34 × 20,000 = 57,500 + 6,800  = $64,300.00
SRT / ECAL on income: not charged from 2024     = $0
FNPF (employee 8%): 0.08 × 320,000              = $25,600.00
Total employee deductions
     = 64,300 + 25,600                           = $89,900.00
Net pay = 320,000 − 89,900                       = $230,100.00
Employer FNPF (10%): 0.10 × 320,000             = $32,000.00
```

### Example 5 -- Non-resident employee ($60,000/yr)

**Input:** Non-resident, annual gross $60,000. No tax-free threshold (Section 6).

```
PAYE: flat 20% × 60,000                          = $12,000.00
Below $270,000: 33% -- 39% bands not reached
FNPF (employee 8%): 0.08 × 60,000               = $4,800.00   [RESEARCH GAP — confirm FNPF coverage for non-residents]
Total employee deductions                        = 12,000 + 4,800 = $16,800.00
Net pay = 60,000 − 16,800                        = $43,200.00
Employer FNPF (10%): 0.10 × 60,000              = $6,000.00
```

### Example 6 -- Minimum-wage worker ($5.00/hr, 40 hrs/wk)

**Input:** Resident, $5.00/hr × 40 hrs × 52 weeks = $10,400/yr.

```
Annual gross: 5.00 × 40 × 52                     = $10,400.00
PAYE: $10,400 < $30,000 threshold                = $0
FNPF (employee 8%): 0.08 × 10,400               = $832.00
Net pay = 10,400 − 832                           = $9,568.00
Employer FNPF (10%): 0.10 × 10,400              = $1,040.00
```

## Section 13 -- Tier 1 Rules (Deterministic -- Apply Mechanically)

- **Tax-free threshold residents only** — Tax-free threshold $30,000 applies to residents ONLY. Non-residents pay 20% from $1 up to $270,000.  _(FRCS)_
- **Income tax marginal rates** — 20% up to $270,000, then 33% -- 39% (Section 3.1) for 2024 onwards.  _(FRCS Tax Rates)_
- **No separate SRT or ECAL** — SRT is integrated into the PAYE brackets from 1 January 2024 and ECAL on income is not charged — never add either on top.  _(FRCS "New PAYE Structure" notice)_
- **FNPF rate composition** — FNPF = 8% employee + 10% employer, no cap, on ordinary wages.  _(FNPF, eff. 1 Jan 2024)_
- **PAYE is final tax** — PAYE is a final tax for employment-only income — no annual return for those employees.  _(FRCS)_
- **Tax year definition** — Tax year = calendar year (1 Jan – 31 Dec).  _(FRCS)_
- **Employer withholding responsibility** — All employee deductions (PAYE + 8% FNPF) are withheld and remitted by the employer.
- **Annualisation requirement** — Annualise before applying brackets, then allocate to pay periods cumulatively.

## Section 14 -- Tier 2 Catalogue (Reviewer Judgement Required)

**Tier 2 Catalogue table**

| Issue | Why it needs judgement |
| --- | --- |
| Income at/near $270,000 | Marginal rate jumps from 20% to 33% above $270,000 |
| "Ordinary wages" definition for FNPF | Whether allowances/bonuses/overtime are inside the FNPF base affects the 18% total |
| Non-resident FNPF coverage | Applicability to short-term assignees is unconfirmed [RESEARCH GAP] |
| Mid-year start/leave | Cumulative PAYE true-up; annualisation assumptions break |
| Sector Wages Regulation Order | Sector minimum may exceed national $5.00/hr |
| Voluntary FNPF top-ups | Tax treatment and employer-policy interaction |
| Fringe benefits / non-cash pay | Out of scope — fringe benefit tax rules apply (escalate) |
| Penalty exposure | Exact FRCS/FNPF penalty figures unconfirmed [RESEARCH GAP] |

## Section 15 -- Excel Working Paper Template

Suggested columns for a per-employee monthly payroll working paper:

**Excel Working Paper Template columns**

| Column | Content |
| --- | --- |
| A | Employee name |
| B | TIN |
| C | FNPF member number |
| D | Residency (R / NR) |
| E | Pay period |
| F | Gross ordinary wages (period) |
| G | Annualised gross (=F × periods/year) |
| H | Annual income tax (PAYE) per Section 3.1 / Section 6 |
| I | Period PAYE (=H/periods) |
| J | FNPF employee (=F × 8%) |
| K | Net pay (=F − I − J) |
| L | FNPF employer (=F × 10%) |
| M | Total employer cost (=F + L) |

**Control totals (must reconcile):**
- Sum of column I = PAYE remitted to FRCS for the period.
- Sum of (J + L) = total FNPF remitted (employee 8% + employer 10% = 18%).
- Sum of column K = total net salary disbursed.

## Section 16 -- Bank Statement / Terminology Reading Guide

**Terminology Reading Guide table**

| Term / abbreviation | Meaning |
| --- | --- |
| FRCS | Fiji Revenue & Customs Service (income tax authority) |
| FNPF | Fiji National Provident Fund (mandatory pension/social fund) |
| PAYE | Pay As You Earn — employment income tax withholding |
| SRT | Social Responsibility Tax (integrated into PAYE brackets from 2024) |
| ECAL | Environment & Climate Adaptation Levy |
| TPOS | Taxpayer Online Services (FRCS filing portal) |
| TIN | Tax Identification Number |
| WRO | Wages Regulation Order (sector minimum wage instrument) |
| MEPIR | Ministry of Employment, Productivity & Industrial Relations |
| Ordinary wages | Base wages used for FNPF contribution calculation |
| $ / FJD | Fijian Dollar (the only currency in this skill) |

## Section 17 -- Onboarding Fallback

If the minimum viable inputs (Section 2) are not available:

1. Ask for **residency status** first — it changes the entire PAYE computation.
2. Ask for **annual or period gross ordinary wages** and **pay frequency**.
3. Confirm **FNPF membership / age 15+**.
4. If the employee may earn **> $270,000**, STOP and escalate (33% -- 39% bands).
5. If sector-specific (construction, hospitality, etc.), check for a **Wages Regulation Order** before assuming the national minimum wage.
6. Produce an **estimated** computation clearly labelled as draft, and route to a Fiji-licensed accountant for sign-off.

## Section 18 -- Reference Material and Test Suite

### Key Sources

**Key Sources table**

| Topic | Reference |
| --- | --- |
| Resident and non-resident PAYE brackets; SRT history; corporate 25% | FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ |
| PAYE as final tax; PAYE structure; SRT integrated and ECAL excluded from 2024 | FRCS public notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ |
| FNPF 8%/10%, coverage, monthly remittance | FNPF Employers -- https://myfnpf.com.fj/employers/ |
| Minimum wage $5.00/hr (1 Apr 2025) | Fiji Govt -- https://www.fiji.gov.fj/Media-Centre/News/MINIMUM-WAGE-INCREASE-TO-$5-00-AN-HOUR-BY-1ST-APRI |
| Governing legislation | Income Tax Act 2015; Tax Administration Act 2009; FNPF Act 2011; Employment Relations Act 2007 |

### Test Suite (recompute to the cent before relying on this skill)

1. **Resident $20,000:** PAYE $0; FNPF employee $1,600; net $18,400; employer FNPF $2,000. ✓
2. **Resident $45,000:** PAYE $2,700 (18% × 15,000); FNPF employee $3,600; net $38,700; employer FNPF $4,500. ✓
3. **Resident $80,000:** PAYE $9,600 (3,600 + 20% × 30,000); FNPF employee $6,400; net $64,000; employer FNPF $8,000. ✓
4. **Resident $320,000:** PAYE $64,300 (57,500 + 34% × 20,000); FNPF employee $25,600; total deductions $89,900; net $230,100; employer FNPF $32,000. ✓
5. **Non-resident $60,000:** PAYE $12,000 (flat 20%); FNPF employee $4,800; net $43,200; employer FNPF $6,000. ✓
6. **Minimum wage 40 hrs/wk:** annual $10,400; PAYE $0; FNPF employee $832; net $9,568; employer FNPF $1,040. ✓
7. **FNPF total check:** employee 8% + employer 10% = 18% on ordinary wages, no cap. ✓
8. **$270,000 boundary:** chargeable income of exactly $270,000 → PAYE $47,600; the 33% rate applies only to the *excess over* $270,000. ✓
9. **Bracket continuity:** income tax at $50,000 = $3,600; at $270,000 = $47,600; at $300,000 = $57,500; at $1,000,000 = $318,500. ✓

## PROHIBITIONS

- NEVER apply the $30,000 tax-free threshold to a non-resident — non-residents pay 20% from the first dollar (33% -- 39% above $270,000).
- NEVER add SRT or ECAL on income on top of the 2024 PAYE brackets — SRT is integrated into the 33% -- 39% bands.
- NEVER cap or floor FNPF — it is 8% employee + 10% employer on full ordinary wages with no ceiling.
- NEVER omit the employer's 10% FNPF when computing total employer cost.
- NEVER treat PAYE as non-final for an employment-only employee, nor force them to file an annual return.
- NEVER state exact FRCS or FNPF penalty figures — they are unconfirmed [RESEARCH GAP]; cite the governing Act and escalate.
- NEVER assume the national minimum wage applies where a sector Wages Regulation Order may set a higher rate.
- NEVER present payroll computations as definitive — always label as estimated and direct to a Fiji-licensed accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax practitioner in Fiji) before filing or acting upon.

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
