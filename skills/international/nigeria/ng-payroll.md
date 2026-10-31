---
name: ng-payroll
description: Use this skill whenever asked to compute, review, or advise on end-to-end Nigerian monthly payroll for employees — gross-to-net calculation, payslip generation, statutory deduction sequencing (Pension, NHF, NHIS, rent relief, PAYE), employer remittance scheduling (PAYE to SIRS, Pension to PFC/PFA, NHF to FMBN, NSITF to NSITF), and year-end Form H1 reconciliation. Trigger on phrases like "Nigeria payroll", "compute Nigerian payroll", "Nigerian pay slip", "payslip Nigeria", "monthly payroll Nigeria", "payroll computation Nigeria", "PAYE and pension together", "deductions Nigeria", "gross to net Nigeria", "Lagos payroll", "LIRS payroll", "FIRS payroll", "Form H1 Nigeria", "annual payroll reconciliation Nigeria", or any request involving running monthly payroll for one or more employees in Nigeria. This skill is the ORCHESTRATOR — it pulls PAYE rules from `ng-paye` and statutory employer/employee contributions (Pension, NHF, NSITF, ITF, NHIS, EDT) from `ng-statutory-deductions` and sequences them into the correct computation order. ALWAYS read this skill before touching Nigerian payroll computation.
jurisdiction: NG
category: payroll
tax_year: 2026
last_updated: 2026-10-31
reviewed_by: Omolola Fasasi
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NG Payroll

## Nigeria — Payroll Computation (End-to-End) — Skill v1.0

> **Scope note:** This skill is the **end-to-end monthly payroll orchestrator**. It does NOT redefine pension percentages, or NHF thresholds — those live in the dependency skills (`ng-paye`, `ng-statutory-deductions`). This skill defines the **sequence**, the **payslip layout**, the **remittance calendar**, and the **year-end reconciliation workflow**.
>
> **Law by date:** Pay periods from 1 January 2026 fall under the Nigeria Tax Act 2025 (NTA), which commenced on that date and repealed the Personal Income Tax Act (PITA) (NTA s 195(g)), and the Nigeria Tax Administration Act 2025 (NTAA), which covers deduction, employer returns and penalties. Earlier pay periods keep the PITA method in Section 3A. Neither Act mentions the FIRS Tax Pro-Max payroll module that earlier versions of this guide described, so that module is unconfirmed. See Section 5 for remittance routing. [NTA](https://nass.gov.ng/documents/download/11249); [NTAA](https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf)

> **Source-cited draft (tier 2), not accountant-reviewed.** On 2026-06-21 Omolola Fasasi checked the rates, thresholds and deadlines listed for this guide against the cited authorities; the corrections of that fact check are in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). It was a check of listed facts, not a sign-off on the guide: no reviewer sign-off is recorded in the frontmatter, the guide is not on the roster in `PARTNERS.md`, and `review_status` is `pending_review`. Items the check flagged for clarification remain marked in the text.

## Section 1 — Quick reference: payroll component order

**Payroll component order table**

| Step | Component | Effect on employee PAYE base | Paid by |
| --- | --- | --- | --- |
| 1 | **Gross monthly emolument** (basic + housing + transport + other taxable allowances + BIK) | Starting point | — |
| 2 | − Employee Pension contribution (8% of BHT, see `ng-statutory-deductions`) | **Reduces** PAYE base | Employee |
| 3 | − Employee NHF contribution (2.5% of basic, if applicable) | **Reduces** PAYE base | Employee |
| 4 | − Employee NHIS contribution (if scheme operated; varies) | **Reduces** PAYE base | Employee |
| 5 | − Other eligible deductions claimed: rent relief (20% of annual rent paid, maximum NGN 500,000), owner-occupied house loan interest, life insurance or deferred annuity premiums (NTA s 30(2)(a)) | **Reduces** PAYE base | Employee |
| 6 | = Chargeable income (NTA s 30(1)) | — | — |
| 7 | Apply NTA Fourth Schedule rates (Section 3, Step 5) | → PAYE liability | — |
| 8 | = **PAYE for the month** | — | Employee (withheld) |
| 9 | Net pay = Gross − Employee Pension − Employee NHF − Employee NHIS − PAYE − any voluntary deductions | — | — |

This order applies to pay periods from 1 January 2026. For earlier periods use Section 3A.

The order of deductions matters because **Pension and NHF reduce the chargeable income** before PAYE is computed, while **NSITF, ITF, EDT and the employer pension share are employer costs** that do NOT affect the employee's PAYE base.

**Employer-side costs (parallel, do NOT affect employee net)**

| Component | Rate / amount | Notes |
| --- | --- | --- |
| Employer Pension | 10% of BHT | Remitted to employee's PFA via PFC |
| NSITF (ECS) | 1% of total payroll | Employer-only |
| ITF | 1% of total payroll (employers with ≥ 5 staff OR turnover ≥ NGN 50m) | Annual return |
| EDT (Tertiary Education Tax) | Not employer payroll cost — corporate tax on assessable profits |  |
| NHIS employer share | If group scheme operated; varies |  |

> **Conservative default:** When in doubt whether a deduction reduces the PAYE base, treat it as **non-deductible** (i.e. PAYE is computed on the higher figure) and flag for reviewer. Over-withholding can be refunded via year-end reconciliation; under-withholding triggers SIRS penalties and interest.

## Section 2 — Required inputs & refusal catalogue

### 2.1 Inputs required to run a payroll

**Inputs required to run a payroll table**

| Input | Source | Notes |
| --- | --- | --- |
| TIN (Tax Identification Number) | Employee record / JTB | Required for PAYE filing; flag if missing |
| State of tax residence | Employee record | Determines which SIRS receives PAYE (per PITA §2(2)) |
| Gross monthly emolument breakdown | Contract / HR | Must split Basic / Housing / Transport / Other |
| Pension scheme status | RSA + PFA details | Confirm employee has RSA opened |
| NHF applicability | Salary ≥ NGN 3,000/month and Nigerian citizen | See `ng-statutory-deductions` |
| NHIS scheme details | If operated by employer | Optional except for federal MDAs |
| Annual rent paid | Employee declaration | Needed for rent relief; the employee must declare the actual rent and the claim must be in writing (NTA ss 30(2)(a)(vi), 31 and 32) |
| Marital / dependent status | Not relevant to the PAYE deductions in NTA s 30(2) | Retained only for HR records |
| Benefits in Kind (BIK) for the month | HR / accounts payable | Must be quantified before PAYE |

### 2.2 Refusal catalogue — out of scope for this skill

**Refusal catalogue table**

| Scenario | Action |
| --- | --- |
| Cross-border employment (employee tax-resident outside Nigeria, employer in Nigeria) | Refer to a qualified Nigerian tax consultant — treaty analysis required |
| Expatriates with split-pay arrangements (home-country + Nigeria) | Out of scope; refer to specialist |
| Directors' fees not paid through payroll | Out of scope — covered by WHT under `ng-paye` |
| Employee stock options / share-based payments | Out of scope — bespoke valuation and CGT interaction |
| Salary sacrifice into pension above 8% statutory | Permitted under PRA 2014 §11(7) but flag for reviewer — quantum and PAYE-deductibility need confirmation |
| Termination payments / gratuity > NGN 10m | Flag — exemption thresholds and tax treatment require legal review |
| Backdated salary adjustments spanning > 1 tax year | Refer to specialist — re-opening of prior-year H1 may be required |

## Section 3 — Step-by-step payroll computation

The procedure below is the **canonical monthly run**. Apply per employee.

### Step 1 — Build the gross emolument

- **Gross monthly emolument formula** — Basic salary                          B + Housing allowance                   H + Transport allowance                 T + Other taxable allowances            O   (utility, meal, leave, entertainment, etc.) + Cash bonus paid in month            X + Benefits in Kind (BIK)              K = Gross monthly emolument             G = B + H + T + O + X + K
- **Note on BHT** — Pension contributions are computed on **Basic + Housing + Transport** (BHT), not on G. See `ng-statutory-deductions` for the legislative basis (PRA 2014 §4(3)).  _(PRA 2014 §4(3))_

### Step 2 — Compute statutory deductions that reduce PAYE base

**Statutory deductions reducing PAYE base table**

| Deduction | Formula | Notes |
| --- | --- | --- |
| Employee Pension | 8% × (B + H + T) | Per PRA 2014 |
| Employee NHF | 2.5% × B | Only if Nigerian citizen AND monthly basic ≥ NGN 3,000 |
| Employee NHIS | Per scheme rules (commonly 1.75% × B for federal MDAs) | Skip if no scheme |

Call these collectively `D_pre`.

### Step 3: Other eligible deductions (pay periods from 1 January 2026)

- **Other eligible deductions**: Add each item the employee claims in writing and can evidence: rent relief of 20% of annual rent paid, up to NGN 500,000, on an accurate declaration of rent; interest on loans for developing an owner-occupied residential house; and annuity or life insurance premiums for the employee or spouse paid in the year before the year of assessment. Call the annual total `D_other`. There is no Consolidated Relief Allowance from 2026.  _(NTA 2025 ss 30(2)(a), 31 and 32)_

### Step 4 — Chargeable income

- **Chargeable income formula**: Chargeable_annual = (G × 12) − (D_pre × 12) − D_other  _(NTA 2025 s 30(1))_

### Step 5: Apply the NTA Fourth Schedule rates

**Fourth Schedule rates, year of assessment 2026 onward**

| Chargeable income band (NGN) | Slice | Rate |
| --- | --- | --- |
| 0 – 800,000 | First 800,000 | 0% |
| 800,001 – 3,000,000 | Next 2,200,000 | 15% |
| 3,000,001 – 12,000,000 | Next 9,000,000 | 18% |
| 12,000,001 – 25,000,000 | Next 13,000,000 | 21% |
| 25,000,001 – 50,000,000 | Next 25,000,000 | 23% |
| Above 50,000,000 | Remainder | 25% |

_(NTA 2025 s 58 and Fourth Schedule)_

- **Annualization method**: Apply the rates to `Chargeable_annual` and divide by 12 to get **monthly PAYE**. Deductions across the year must equal the income tax chargeable on the employee's emoluments for that year.  _(NTAA 2025 s 51(6) and (7))_

### Step 6: Minimum wage exemption; no 1% minimum tax

- **Minimum wage**: Employment income of a person whose gross income from that employment is the national minimum wage or less is exempt.  _(NTA 2025 ss 58 and 162(1)(t))_
- **No 1% minimum tax from 2026**: PITA §37 is repealed with the rest of PITA, and NTA s 58 and the Fourth Schedule set no individual minimum tax. Do not substitute 1% of gross income for a 2026 pay period.  _(NTA 2025 ss 58 and 195(g))_

### Step 7 — Net pay

- **Net pay formula** — Net pay = G − Employee Pension − Employee NHF − Employee NHIS − PAYE − Voluntary deductions (loan repayments, salary advance recoveries, union dues, etc.)

### Step 8 — Employer-side accruals (parallel posting)

**Employer-side accruals table**

| Item | Posted to |
| --- | --- |
| Employer Pension 10% × BHT | DR Payroll expense, CR Pension payable |
| NSITF 1% × total payroll | DR Payroll expense, CR NSITF payable |
| ITF 1% × total payroll (qualifying employers) | DR Payroll expense, CR ITF payable (accrued monthly, paid annually) |

### Section 3A: Pay periods before 1 January 2026 (repealed PITA method)

Use these steps in place of Steps 3 to 6 only when the pay period ended before 1 January 2026, for example a late correction of a 2025 payroll.

#### Pre-2026 Step 3 — Compute CRA gross income and CRA

- **CRA computation formula** — Gross_for_CRA = G − D_pre CRA = max(NGN 200,000 annual / NGN 16,666.67 monthly, 1% × Gross_for_CRA) + 20% × Gross_for_CRA

**Monthly application:** Divide annual CRA components by 12, OR — recommended approach — compute on annualized gross and divide the result by 12. The annualized approach is more accurate when income varies month-to-month and matches the year-end reconciliation.

#### Pre-2026 Step 4 — Chargeable income

- **Chargeable income formula** — Chargeable_monthly = Gross_for_CRA − CRA_monthly

#### Pre-2026 Step 5 — Apply PITA Sixth Schedule progressive brackets

- **Annualization method** — Annualize `Chargeable_monthly × 12`, apply the brackets in Section 7, part I, divide the result by 12 to get **monthly PAYE**. The annualized method avoids the regressive distortion that occurs when applying brackets directly to monthly income.

#### Pre-2026 Step 6 — Minimum tax check

- **Minimum tax check** — If the computed PAYE is less than **1% of gross income** (minimum tax under PITA §37), substitute the minimum tax. Common for low earners; rare for the salary range typically processed via formal payroll.  _(PITA §37)_

## Section 4 — Payslip components & sample

A **conforming Nigerian payslip** must show, at minimum:

1. Employer name, address, employer TIN
2. Employee name, employee TIN, RSA PIN, state of tax residence
3. Pay period and pay date
4. Gross emolument breakdown (basic, housing, transport, other allowances, BIK)
5. Statutory deductions, **itemized** (Pension, NHF, NHIS, PAYE)
6. Voluntary deductions
7. Net pay
8. Employer contributions (for transparency — Pension 10%, NSITF, ITF)
9. YTD totals (cumulative gross, cumulative PAYE, cumulative pension)

### Sample payslip — Lagos employee, NGN 500,000 gross monthly (May 2026)

> Full worked numbers are in Section 7. The layout below is the recommended template.

```
+-----------------------------------------------------------------+
|  ACME NIGERIA LTD                       PAYSLIP — MAY 2026      |
|  12 Awolowo Road, Ikoyi, Lagos                                  |
|  Employer TIN: 12345678-0001                                    |
+-----------------------------------------------------------------+
|  Employee: Adaeze Okafor       TIN: 98765432-0001               |
|  RSA PIN: PEN100123456789      State of residence: LAGOS        |
|  Pay date: 28 May 2026         Period: 01-31 May 2026           |
+-----------------------------------------------------------------+
|  EARNINGS                              NGN                      |
|    Basic salary                        250,000.00               |
|    Housing allowance                   100,000.00               |
|    Transport allowance                  50,000.00               |
|    Utility allowance                    50,000.00               |
|    Meal allowance                       50,000.00               |
|    Gross emolument                     500,000.00               |
+-----------------------------------------------------------------+
|  DEDUCTIONS                            NGN                      |
|    Employee Pension (8% × BHT)          32,000.00               |
|    NHF (2.5% × Basic)                    6,250.00               |
|    PAYE                                 62,015.00               |
|    Total deductions                    100,265.00               |
+-----------------------------------------------------------------+
|  NET PAY                               NGN 399,735.00           |
+-----------------------------------------------------------------+
|  EMPLOYER CONTRIBUTIONS (info only)    NGN                      |
|    Employer Pension (10% × BHT)         40,000.00               |
|    NSITF (1% × Gross)                    5,000.00               |
|    ITF (1% × Gross, accrued)             5,000.00               |
+-----------------------------------------------------------------+
|  YTD TOTALS (Jan–May 2026)              NGN                     |
|    Gross YTD                          2,500,000.00              |
|    PAYE YTD                             [auto]                  |
|    Pension YTD (employee)              160,000.00               |
+-----------------------------------------------------------------+
```

## Section 5 — Monthly remittance calendar

**Monthly remittance calendar table**

| Item | Recipient | Deadline | Channel |
| --- | --- | --- | --- |
| **PAYE** | Relevant State IRS (state of employee's tax residence) | **10th of the following month** | LIRS e-tax (Lagos); FCT-IRS portal (FCT); other state IRS portals or bank Pay-Direct |
| **Employee + Employer Pension** | Pension Fund Custodian (PFC) for credit to employee's PFA | **Within 7 working days** of salary payment date | PFA transfer via PFC; PenCom RSA Multifund schedule |
| **NHF** | Federal Mortgage Bank of Nigeria (FMBN) | **Within 1 month** of deduction | FMBN-designated commercial banks |
| **NSITF (ECS)** | Nigeria Social Insurance Trust Fund | **Monthly, by the last day of the following month** | NSITF e-portal / designated banks |
| **NHIS (if operated)** | NHIS / HMO | Per scheme rules — typically monthly | HMO direct |
| **ITF (employer only)** | Industrial Training Fund | **Annual** — by 1 April of following year | ITF portal |

- **PAYE due date from 2026**: LIRS's FAQ, which treats the NTA and NTAA 2025 as the governing law, says 'on or before the 10th day of the following month'; FCT-IRS's due date page says '10th of every month'. Both pages are undated. For any other state, confirm with its IRS. NTAA s 107(1) applies its penalty when deducted tax is not remitted by the 21st day of the following month, and s 28 leaves monthly deduction returns to regulations. No regulation was read, and the Joint Revenue Board's Personal Income Tax Guidelines 2026 could not be opened, so do not treat the 21st as a later due date.  _(https://lirs.gov.ng/faq; https://fctirs.gov.ng/due-date/; NTAA 2025 ss 28 and 107(1))_

### FIRS Tax Pro-Max payroll module (status note)

- **Module status**: Earlier versions of this guide described a phased unified payroll module under FIRS Tax Pro-Max, attributed to the 2025 Acts. Neither the NTA nor the NTAA mentions it, so the rollout phases are unconfirmed. **Conservative default:** continue with the current state IRS portal until that IRS publishes an onboarding notice.

### Late-payment penalties (summary — full detail in `ng-paye` and `ng-statutory-deductions`)

**Late-payment penalties table**

| Item | Penalty |
| --- | --- |
| PAYE not deducted (from 2026) | 40% of the amount not deducted (NTAA 2025 s 105) |
| PAYE deducted but not remitted by the 21st day of the following month (from 2026) | The amount, plus 10% per annum of it, plus interest at the prevailing CBN monetary policy rate (NTAA 2025 s 107(1)) |
| PAYE late remittance (before 2026) | 10% of unremitted tax + interest at CBN MPR + 5% (PITA §82) |
| Pension late remittance | 2% per month of unremitted amount (PRA 2014 §11(7)) |
| NHF late remittance | NGN 50,000 (individual) / NGN 100,000 (body corporate) + recovery |
| NSITF late remittance | 10% of contribution + interest |

## Section 6 — Year-end activities

### 6.1 Form H1 — Annual Employer's Return

- **Form H1 filing requirement** — Every employer must file **Form H1 (Annual Employer's Return of all emoluments paid to employees)** with the relevant State IRS by **31 January** of the following year, covering the preceding tax year (1 January – 31 December).  _(NTAA 2025 s 14(1) and (2))_

**Form H1 field table**

| Field | Content |
| --- | --- |
| Employer details | Name, TIN, address |
| Schedule of employees | Name, TIN, RSA PIN, total gross emolument, total deductions, net emoluments, chargeable income, total PAYE remitted by month |
| Reconciliation | Sum of monthly PAYE remitted must equal computed annual PAYE per employee |
| Variance | Any under-remittance is payable; over-remittance is offsetable against the next year (refund procedurally difficult) |

### 6.2 Employee tax deduction certificate (informal "P9A/P9B equivalent")

Nigeria has no single statutory equivalent of the Kenyan P9A/P9B form, but employers customarily issue an **"Employee Tax Deduction Certificate"** at year-end showing:

- Gross emolument per month and YTD
- Statutory deductions (Pension, NHF, NHIS) per month and YTD
- PAYE deducted per month and YTD
- Receipt numbers / SIRS PAYE schedule references

This certificate enables the employee to claim WHT credits, file self-assessment if they have other income sources, or substantiate income for credit/visa applications.

### 6.3 Reconciliation checklist

**Reconciliation checklist table**

| Check | Pass criterion |
| --- | --- |
| Sum of monthly Form A (PAYE schedule) = Form H1 total | ✓ |
| Pension contributions remitted = 18% × annual BHT for each employee | ✓ |
| NHF contributions remitted = 2.5% × annual basic for each qualifying employee | ✓ |
| NSITF remitted = 1% × annual total payroll | ✓ |
| ITF annual return filed (if applicable) | ✓ |
| Any retroactive bonuses / 13th-month spread per `ng-paye` rules | ✓ |
| BIK valuations consistent across months | ✓ |

## Section 7 — Worked example

**Scenario:** Software developer, **Lagos resident**, NGN **500,000 gross monthly**, employed full-time at a private fintech. No BIK. Nigerian citizen. Has RSA, TIN, and is NHF-eligible. Employer operates no NHIS group scheme. Annual rent paid NGN 1,200,000, declared and claimed in writing. Pay period: **May 2026**.

### A — Gross emolument breakdown

**Gross emolument breakdown table**

| Component | NGN |
| --- | --- |
| Basic (50% of gross) | 250,000 |
| Housing (20%) | 100,000 |
| Transport (10%) | 50,000 |
| Utility allowance | 50,000 |
| Meal allowance | 50,000 |
| **Gross monthly (G)** | **500,000** |

BHT = 250,000 + 100,000 + 50,000 = **400,000**

### B — Statutory deductions reducing PAYE base

**Statutory deductions reducing PAYE base table**

| Item | Formula | NGN |
| --- | --- | --- |
| Employee Pension | 8% × 400,000 | 32,000 |
| NHF | 2.5% × 250,000 | 6,250 |
| NHIS | n/a (no scheme) | 0 |
| **D_pre total** |  | **38,250** |

### C: Other eligible deductions (annual)

**Other eligible deductions table**

| Item | Formula | NGN |
| --- | --- | --- |
| Rent relief | 20% × 1,200,000 = 240,000, below the 500,000 maximum | 240,000 |
| **D_other total** |  | **240,000** |

### D — Chargeable income

- **Chargeable income worked example**: Annual gross = 500,000 × 12 = 6,000,000 Annual D_pre = 38,250 × 12 = 459,000 Chargeable_annual = 6,000,000 − 459,000 − 240,000 = 5,301,000

### E: PAYE (NTA Fourth Schedule, 2026 rates, applied annually then divided by 12)

**PAYE bracket table**

| Bracket | Slice | Rate | Tax (annual) |
| --- | --- | --- | --- |
| 0 – 800,000 | 800,000 | 0% | 0 |
| 800,001 – 3,000,000 | 2,200,000 | 15% | 330,000 |
| 3,000,001 – 5,301,000 | 2,301,000 | 18% | 414,180 |
| **Annual PAYE** |  |  | **744,180** |
| **Monthly PAYE** | 744,180 / 12 |  | **62,015.00** |

### F — Net pay

**Net pay table**

| Item | NGN |
| --- | --- |
| Gross | 500,000.00 |
| − Employee Pension | (32,000.00) |
| − NHF | (6,250.00) |
| − PAYE | (62,015.00) |
| **Net pay** | **399,735.00** |

### G — Employer cost ledger (monthly)

**Employer cost ledger table**

| Item | NGN |
| --- | --- |
| Gross emolument | 500,000.00 |
| Employer Pension (10% × BHT) | 40,000.00 |
| NSITF (1% × Gross) | 5,000.00 |
| ITF accrual (1% × Gross) | 5,000.00 |
| **Total employer cost** | **550,000.00** |

### H — Remittances arising from this payslip

**Remittances arising from this payslip table**

| Recipient | Amount NGN | Deadline |
| --- | --- | --- |
| LIRS (PAYE) | 62,015.00 | 10 Jun 2026 (see Section 5) |
| PFC → PFA (Pension total) | 72,000.00 | within 7 working days of pay date |
| FMBN (NHF) | 6,250.00 | within 1 month |
| NSITF | 5,000.00 | last day of following month |
| ITF | 5,000.00 (accrued; paid annually by 1 Apr 2027) | annual |

### I: Same salary in May 2025 (repealed PITA method, for comparison only)

No rent relief applied before 2026. This part must not be used for a 2026 pay period.

#### CRA computation (monthly basis using annualization)

- **CRA computation worked example** — Gross_for_CRA (monthly)   = 500,000 − 38,250        = 461,750 Gross_for_CRA (annualized)                          = 5,541,000 CRA (annual) = max(200,000, 1% × 5,541,000) + 20% × 5,541,000 = max(200,000, 55,410)        + 1,108,200 = 200,000                     + 1,108,200 = 1,308,200 CRA (monthly) = 1,308,200 / 12 = 109,016.67

#### Chargeable income

- **Chargeable income worked example** — Chargeable_monthly  = 461,750 − 109,016.67 = 352,733.33 Chargeable_annual   = 4,232,800

#### PAYE (PITA Sixth Schedule, applied annually then divided by 12)

**PAYE bracket table**

| Bracket | Slice | Rate | Tax (annual) |
| --- | --- | --- | --- |
| 0 – 300,000 | 300,000 | 7% | 21,000 |
| 300,001 – 600,000 | 300,000 | 11% | 33,000 |
| 600,001 – 1,100,000 | 500,000 | 15% | 75,000 |
| 1,100,001 – 1,600,000 | 500,000 | 19% | 95,000 |
| 1,600,001 – 3,200,000 | 1,600,000 | 21% | 336,000 |
| 3,200,001 – 4,232,800 | 1,032,800 | 24% | 247,872 |
| **Annual PAYE** |  |  | **807,872** |
| **Monthly PAYE** | 807,872 / 12 |  | **67,322.67** |

Minimum tax check: 1% × 500,000 = 5,000 → not binding (computed PAYE is higher).

#### Net pay

**Net pay table**

| Item | NGN |
| --- | --- |
| Gross | 500,000.00 |
| − Employee Pension | (32,000.00) |
| − NHF | (6,250.00) |
| − PAYE | (67,322.67) |
| **Net pay** | **394,427.33** |

## Section 8 — Conservative defaults

**Conservative defaults table**

| Situation | Conservative position |
| --- | --- |
| Pension status unclear (RSA exists?) | Assume RSA exists and deduct 8% / pay employer 10% — flag for HR; under-remittance triggers 2%/month penalty |
| NHF applicability unclear | If Nigerian citizen and basic ≥ NGN 3,000, deduct 2.5% — flag for reviewer if foreign national |
| BIK valuation uncertain | Use higher of cost-to-employer or open-market value — flag |
| Bonus / 13th-month timing | **Spread evenly across the 12 months of the period it relates to** for PAYE smoothing; flag if employer prefers month-paid taxation (allowed but produces a higher PAYE spike that month) |
| Multi-state employee (works across states) | Use the state where employee is **principally resident** per PITA §2(2); flag for reviewer |
| Mid-month joiner / leaver | Pro-rate gross emolument, pro-rate annual deductions on annualized basis (CRA for pay periods before 2026), full statutory deductions on actual paid amounts |
| Employee TIN missing | Compute PAYE normally but **flag immediately** — SIRS reconciliation will reject schedule without TIN |
| Salary advance / loan recovery | Show as voluntary deduction below the line; does NOT reduce PAYE base |
| Pay in foreign currency | Convert to NGN at CBN official rate on pay date; document the rate used |
| Late hire — backdated salary | Apply current-month PAYE on full amount paid; do NOT spread retroactively without reviewer sign-off |

## Section 9 — Sources

**Sources table**

| Source | Reference |
| --- | --- |
| Nigeria Tax Act 2025 ss 30, 31, 32, 58, 162 and 195 and Fourth Schedule (from 1 January 2026) | [National Assembly copy](https://nass.gov.ng/documents/download/11249) |
| Personal Income Tax Act (PITA) Cap P8 LFN 2004, as amended by Finance Acts 2019–2023 (pay periods before 1 January 2026; repealed by NTA s 195(g)) | Federal Inland Revenue Service |
| Pension Reform Act 2014 (PRA 2014) | National Pension Commission (PenCom) |
| National Housing Fund Act, Cap N45 LFN 2004 | Federal Mortgage Bank of Nigeria (FMBN) |
| Employees Compensation Act 2010 (NSITF) | Nigeria Social Insurance Trust Fund |
| Industrial Training Fund Act, Cap I9 LFN 2004 (as amended 2011) | Industrial Training Fund |
| National Health Insurance Authority Act 2022 | NHIA (formerly NHIS) |
| Nigeria Tax Administration Act 2025 ss 14, 28, 51, 105 and 107 | [Tax Appeal Tribunal copy](https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf) |
| Lagos State Internal Revenue Service e-tax portal | https://etax.lirs.net |
| FCT Internal Revenue Service portal | https://fctirs.gov.ng |
| FIRS Tax Pro-Max | https://taxpromax.firs.gov.ng |
| Companion skill — PAYE rules | `ng-paye` |
| Companion skill — Statutory deductions | `ng-statutory-deductions` |
| Companion skill — Income tax (self-employed) | `ng-income-tax` |

## *OpenAccountants — open-source accounting skills for AI*

*All outputs must be reviewed by a qualified Nigerian payroll professional or tax consultant before any payslip is issued or any remittance is made.*

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
