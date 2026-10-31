---
name: in-pf-esi-employer
description: Use this skill whenever asked about Indian EPF (Employees' Provident Fund), ESI (Employees' State Insurance), or employer social security obligations. Trigger on phrases like "PF contribution India", "EPF employer", "ESI contribution", "provident fund India", "PF admin charges", "EDLI", "EPS pension", "ECR filing", "PF return", "ESI threshold", "PF applicability", "12% PF", "employer PF obligation", or any question about computing, depositing, or filing EPF/ESI in India. This skill covers EPF contribution rates, EPS, EDLI, ESI rates and thresholds, applicability criteria, monthly filing (ECR), and compliance deadlines. ALWAYS read this skill before touching any Indian PF/ESI employer work.
version: "1.0"
jurisdiction: IN
tax_year: 2025
last_updated: 2026-10-31
reviewed_by: Mayur Deokar
review_status: pending_review
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IN Pf Esi Employer

## India EPF & ESI -- Employer Obligations Skill v1.0

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Mayur Deokar** on 2026-06-06; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text. Figures changed on 2026-10-31 for the EPF wage ceiling postdate that sign-off and await review.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Tax/Contribution | EPF (Provident Fund) + ESI (State Insurance) |
| Currency | INR only |
| Applicable period | FY 2025-26 (April 2025 -- March 2026); EPF wage ceiling as revised from 17 September 2026 (FY 2026-27) |
| EPF legislation | Employees' Provident Funds and Miscellaneous Provisions Act, 1952 |
| ESI legislation | Employees' State Insurance Act, 1948 |
| Administering bodies | EPFO (Employees' Provident Fund Organisation); ESIC (ESI Corporation) |
| Filing portal (EPF) | Unified Portal (unifiedportal-emp.epfindia.gov.in) |
| Filing portal (ESI) | ESIC Portal (esic.gov.in) |
| Skill version | 1.0 |

### EPF Contribution Summary

**EPF Contribution Summary**

| Component | Employer (%) | Employee (%) | On |
| --- | --- | --- | --- |
| EPF (Provident Fund) | 3.67% | 12% | Basic + DA |
| EPS (Employee Pension Scheme) | 8.33% | Nil | Basic + DA (capped at ₹25,000/month from 17 September 2026; ₹15,000 before) |
| **Total employer contribution** | **12%** | -- | Basic + DA |
| **Total employee contribution** | -- | **12%** | Basic + DA |

### Employer Administrative Charges

**Employer Administrative Charges**

| Charge | Rate | On |
| --- | --- | --- |
| EPF Admin charges | 0.50% | Total EPF wages (minimum ₹500/month if >20 employees) |
| EDLI (Employees' Deposit Linked Insurance) | 0.50% | Basic + DA (capped at ₹25,000/month from 17 September 2026; ₹15,000 before) |
| EDLI Admin charges | Nil (removed w.e.f. 01-04-2017) | -- |

### ESI Contribution Summary

**ESI Contribution Summary**

| Component | Rate | On |
| --- | --- | --- |
| Employer ESI | 3.25% | Gross wages (all components except certain exclusions) |
| Employee ESI | 0.75% | Gross wages |
| **Total ESI** | **4%** | Gross wages |

### ESI Wage Ceiling

**ESI Wage Ceiling**

| Threshold | Amount |
| --- | --- |
| ESI applicability (employee) | Gross wages ≤ ₹21,000/month |
| ESI applicability (disability employee) | Gross wages ≤ ₹25,000/month |

### Applicability Thresholds

**Applicability Thresholds**

| Scheme | Applies When |
| --- | --- |
| EPF | Establishment employs 20 or more persons |
| ESI | Establishment employs 10 or more persons (in notified areas) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether establishment is covered | Verify employee count -- do not assume |
| Unknown wage components | Include all regular earnings as PF wages unless specifically excluded |
| Unknown ESI area notification | Check ESIC notification for the area |

## Section 2 -- EPF Detailed Rules

### 2.1 Wage Components for PF

**Wage Components for PF**

| Included in Basic + DA (PF Wages) | Excluded from PF Wages |
| --- | --- |
| Basic salary | House Rent Allowance (HRA) |
| Dearness Allowance (DA) | Overtime allowance |
| Retaining allowance | Bonus (statutory or otherwise) |
| Cash value of food concession (if not provided) | Commission |
|  | Conveyance allowance |
|  | Retrenchment compensation |
|  | Gratuity |

- **PF wage ceiling (voluntary cap)** — ₹25,000/month is the statutory wage ceiling from 17 September 2026; ₹15,000 applied before that date. Authority: S.O. 5109(E) of 17 September 2026, made under section 2(89) of the Code on Social Security, 2020 for its Chapter III, in force on Gazette publication (Gazette of India, Extraordinary, Part II, Section 3(ii), No. 4918, https://egazette.gov.in/WriteReadData/2026/276299.pdf). Contributions run on ₹25,000 or actual wages if lower (PIB release 2314111). Employers may choose to contribute on actual Basic + DA even if above ₹25,000 (most large employers do this). EPS is always capped at ₹25,000/month.
- **Enrolment from 17 September 2026:** Employees excluded until now because their wages exceeded ₹15,000, and whose EPF wages do not exceed ₹25,000, must be made members of EPF, EPS and EDLI from 17 September 2026. Enrolling them is the employer's duty; no application is needed (EPFO FAQs Q29 to Q31; PIB release 2313790). An EPF member outside EPS with wages in that band joins EPS from the same date (FAQs Q9). EPF wages above ₹25,000 at joining or on 17 September 2026 fall outside mandatory coverage and EPS membership (FAQs Q13 note, Q26), so a voluntary member in that position has no EPS share and the full employer 12% goes to EPF.
- **September 2026 wage month:** File one ECR. EPFO FAQs Q8 give 15 October 2026 as the ordinary due date. Secondary reports describe an EPFO circular of 13 October 2026 extending filing and remittance for this wage month only; no EPFO or government copy could be opened, so confirm the due date against EPFO before computing interest or damages. Later wage months keep the normal due date in section 4.1. Compute 1 to 16 September under the ₹15,000 ceiling and 17 to 30 September under ₹25,000, using 16/30 and 14/30 of the monthly wage (EPFO FAQs Q7 to Q9, Q46). Wage of ₹20,000, member previously capped at ₹15,000: EPF wage = ₹8,000.00 + ₹9,333.33 = ₹17,333.33; employee ₹2,080.00; employer EPF ₹636.13; EPS ₹1,443.87; EDLI ₹86.67; admin ₹86.67. Same wage, previously excluded employee: EPF wage = ₹9,333.33; employee ₹1,120.00; employer EPF ₹342.53; EPS ₹777.47; EDLI ₹46.67; admin ₹46.67.
- **Status of these sources:** The Gazette text sets only the ceiling and its date. The enrolment duty and the September split rest on the EPFO FAQs, read from a copy on a third-party host (https://www.staffnews.in/wp-content/uploads/2026/10/EPFO_Wage_Ceiling_FAQs.pdf) because the EPFO site refused the request. PIB releases 2313790 and 2314111 support the ceiling, the 8.33% of ₹25,000 EPS maximum and enrolment, not the split. Confirm the split against an EPFO circular.

### 2.2 Employer 12% Breakup

**Employer 12% Breakup**

| Component | Rate | Cap |
| --- | --- | --- |
| EPF account (employee's individual PF) | 3.67% | On full PF wages |
| EPS (Pension fund) | 8.33% | Capped at ₹25,000/month from 17 September 2026 (max ₹2,083/month to EPS: 8.33% is ₹2,082.50, shown as ₹2,083 in EPFO FAQs Q13) |
| If PF wages > ₹25,000 | Balance of 8.33% above cap goes to EPF | Employer's full 12% is still paid, split between EPF and EPS |

**Example (wage months from October 2026):** EPS member contributing on actual Basic + DA = ₹30,000/month:
- Employer EPF = ₹30,000 × 3.67% = ₹1,101
- Employer EPS = ₹25,000 × 8.33% = ₹2,083 (capped)
- Remaining to EPF = (₹30,000 × 8.33%) − ₹2,083 = ₹2,499 − ₹2,083 = ₹416
- Total employer to EPF account = ₹1,101 + ₹416 = ₹1,517
- Total employer contribution = ₹30,000 × 12% = ₹3,600 (split between EPF and EPS)

### 2.3 EDLI (Employees' Deposit Linked Insurance)

**EDLI Details**

| Item | Detail |
| --- | --- |
| Purpose | Life insurance for EPF members |
| Employer contribution | 0.50% of Basic + DA (capped at ₹25,000/month from 17 September 2026; ₹15,000 before) |
| Maximum EDLI contribution | ₹125/month per employee from 17 September 2026 (₹75 before) |
| Benefit on death | Up to ₹7,00,000 (₹7 lakh), unchanged by the higher ceiling (EPFO FAQs Q38) |
| Employee contribution | Nil |

### 2.4 International Workers

**International Workers PF Treatment**

| Scenario | PF Treatment |
| --- | --- |
| Indian employee sent abroad (no SSA country) | PF continues on Indian salary |
| Foreign national working in India (from SSA country) | Exempt from PF if covered in home country |
| Foreign national from non-SSA country | PF mandatory at full rate |

- **SSA** — Social Security Agreement (India has SSAs with ~20 countries).

## Section 3 -- ESI Detailed Rules

### 3.1 Wage Components for ESI

- **Basis of ESI calculation** — ESI is calculated on **gross wages** (broader than PF wages)

**Wage Components for ESI**

| Included | Excluded |
| --- | --- |
| Basic salary | Annual bonus (statutory) |
| DA | Retrenchment compensation |
| HRA | Encashment of leave on superannuation |
| City Compensatory Allowance | Gratuity |
| Overtime (for contribution purposes) |  |
| All other regular cash payments |  |

### 3.2 Contribution Period and Benefit Period

**Contribution and Benefit Periods**

| Contribution Period | Benefit Period |
| --- | --- |
| 1 April -- 30 September | 1 January -- 30 June (following) |
| 1 October -- 31 March | 1 July -- 31 December (following) |

### 3.3 ESI Benefits

**ESI Benefits**

| Benefit | Coverage |
| --- | --- |
| Medical benefit | Full medical care for employee and family |
| Sickness benefit | 70% of wages for up to 91 days |
| Maternity benefit | Full wages for 26 weeks |
| Disablement benefit | 90% of wages (temporary); pension (permanent) |
| Dependants' benefit | 90% of wages as pension to dependants |
| Funeral expenses | ₹15,000 |

### 3.4 Crossing the ESI Threshold

- **Crossing the ESI threshold mid-period** — If an employee's wages exceed ₹21,000/month mid-contribution period: - ESI contributions continue for the remainder of that contribution period - Employee ceases to be covered from the next contribution period - Employer must ensure coverage for the full 6-month period once started

## Section 4 -- Filing and Payment

### 4.1 EPF -- ECR (Electronic Challan cum Return)

**ECR Details**

| Item | Detail |
| --- | --- |
| What is ECR | Monthly return declaring employee-wise PF contributions |
| Due date | 15th of the following month |
| Payment mode | Online through EPFO Unified Portal |
| Format | Upload employee data (UAN, name, wages, contribution breakup) |
| Late payment penalty (interest, EPF Act s 7Q) | Simple interest at 12% per annum on delayed deposits |
| Damages (EPF Act s 14B) | 1% per month or part of a month of the arrears, whatever the length of delay, from 14 June 2024 (EPF Scheme para 32A as amended by the EPF (Amendment) Scheme 2024, in force from its Gazette publication on 14 June 2024; 5% to 25% per annum by length of delay before that) |

### 4.2 ESI -- Monthly Contribution

**ESI Monthly Contribution Details**

| Item | Detail |
| --- | --- |
| Due date | 15th of the following month |
| Payment mode | Online through ESIC portal |
| Return | Half-yearly return (now largely subsumed in monthly online filing) |
| Late payment penalty (interest, ESI Act s 39(5)(a)) | Simple interest at 12% per annum |
| Damages (ESI (General) Regulations reg 31C) | 5% to 25% per annum of the arrears by length of delay (under 2 months 5%; 2 to 4 months 10%; 4 to 6 months 15%; over 6 months 25%) |

### 4.3 Annual Returns

**Annual Returns**

| Return | Due Date | Covers |
| --- | --- | --- |
| EPF Annual Return (Form 3A/6A) | Now via monthly ECR (no separate annual) | Automated through monthly ECR |
| ESI Return (Form 5) | Half-yearly (11 May and 11 November) | Contribution register |

## Section 5 -- Computation Examples

### Example 1: Standard Employee (PF + ESI applicable)

Employee: Basic = ₹12,000/month, DA = ₹3,000/month, HRA = ₹5,000/month
Gross = ₹20,000/month (below ₹21,000 ESI threshold)

**Example 1 Calculation Table**

| Component | Employer | Employee |
| --- | --- | --- |
| EPF (on Basic + DA = ₹15,000) | ₹15,000 × 3.67% = ₹550.50 | ₹15,000 × 12% = ₹1,800 |
| EPS (₹15,000 is below the ₹25,000 ceiling) | ₹15,000 × 8.33% = ₹1,249.50 | Nil |
| Total PF employer | ₹1,800 (12% of ₹15,000) | ₹1,800 |
| EDLI | ₹15,000 × 0.50% = ₹75 | Nil |
| PF Admin | ₹15,000 × 0.50% = ₹75 | Nil |
| ESI (on gross ₹20,000) | ₹20,000 × 3.25% = ₹650 | ₹20,000 × 0.75% = ₹150 |
| **Total employer cost** | **₹2,600** | -- |
| **Total employee deduction** | -- | **₹1,950** |

### Example 2: Higher Salary (PF only, ESI not applicable)

Employee: EPS member, wage months from October 2026, Basic + DA = ₹40,000/month, Gross = ₹65,000/month (above ₹21,000 ESI threshold)

**Example 2 Calculation Table**

| Component | Employer | Employee |
| --- | --- | --- |
| EPF (on ₹40,000, if contributing on actual) | ₹40,000 × 3.67% = ₹1,468 | ₹40,000 × 12% = ₹4,800 |
| EPS (capped at ₹25,000) | ₹25,000 × 8.33% = ₹2,083 | Nil |
| Remaining to EPF | ₹40,000 × 8.33% − ₹2,083 = ₹1,249 | Nil |
| Total PF employer | ₹4,800 (12% of ₹40,000) | ₹4,800 |
| EDLI | ₹25,000 × 0.50% = ₹125 | Nil |
| PF Admin | ₹40,000 × 0.50% = ₹200 | Nil |
| ESI | Not applicable (gross > ₹21,000) | Not applicable |
| **Total employer cost** | **₹5,125** | -- |

## Section 6 -- Edge Cases

### 6.1 Establishments with < 20 Employees

- **EPF applicability for small establishments** — EPF is mandatory for establishments with 20+ employees. Establishments with fewer may voluntarily register. Once registered, coverage continues even if numbers drop below 20.

### 6.2 Contract Labour

- **Contract labour PF/ESI responsibility** — The principal employer is responsible for PF/ESI of contract workers if the contractor fails to deposit. Both principal employer and contractor must be registered.

### 6.3 Fixed-Term Employees

- **Fixed-term employee coverage** — Fixed-term employees are entitled to same PF/ESI benefits as regular employees from day one. No waiting period.

### 6.4 Exempted Establishments (PF Trust)

- **PF Trust exemption** — Large employers may apply for EPF exemption to manage their own PF trust. Must provide equal or better benefits. Trust must maintain accounts as per EPFO norms.

### 6.5 VPF (Voluntary Provident Fund)

- **VPF rules** — Employee may contribute above 12% voluntarily (up to 100% of Basic + DA). Employer contribution remains at 12% -- no additional employer obligation for VPF.

### 6.6 New Establishments

- **New establishment registration deadlines** — A new establishment must register with EPFO within one month of employing 20 persons. ESI registration within 15 days of applicability.

## Section 7 -- Prohibitions

- NEVER compute PF on gross salary -- PF is on Basic + DA only
- NEVER exceed the EPS ceiling (₹25,000/month from 17 September 2026; ₹15,000 before) for pension calculation
- NEVER apply ESI to employees earning above ₹21,000/month gross (unless mid-period crossing)
- NEVER miss the 15th of the month deadline without accounting for interest/damages
- NEVER assume all establishments are covered -- verify employee count threshold
- NEVER confuse employer contribution rate (12%) with employee rate (12%) -- they are separate obligations
- NEVER ignore admin charges and EDLI when computing total employer cost
- NEVER present calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CA, CMA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
