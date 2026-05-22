---
name: ph-sss-philhealth
description: >
  Use this skill whenever asked about Philippines SSS, PhilHealth, or Pag-IBIG contributions. Trigger on phrases like "SSS contribution", "Social Security System", "PhilHealth", "Philippine Health Insurance", "Pag-IBIG", "HDMF", "Home Development Mutual Fund", "self-employed SSS", "voluntary SSS", "monthly salary credit", "social security Philippines", or any question about mandatory government contributions in the Philippines for self-employed individuals. Covers SSS, PhilHealth, and Pag-IBIG rates, thresholds, registration, and payment. ALWAYS read this skill before advising on Philippine social security contributions.
version: 1.0
jurisdiction: PH
tax_year: 2025
category: international
depends_on:
  - ph-income-tax
verified_by: pending
---

# Philippines SSS, PhilHealth & Pag-IBIG Contributions Skill v1.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Philippines |
| Systems | SSS, PhilHealth, Pag-IBIG (HDMF) |
| Currency | PHP (₱) only |
| Contribution year | Calendar month |
| Primary legislation | RA 11199 (Social Security Act of 2018); RA 11223 (Universal Health Care Act of 2019); RA 9679 (Pag-IBIG Fund Law) |
| Validated by | Pending |
| Validation date | Pending |
| Skill version | 1.0 |

### Summary Table (2025)

| Agency | Total Rate | Floor | Ceiling | Employer Share | Employee Share |
|---|---|---|---|---|---|
| SSS | 15% | ₱5,000 MSC | ₱35,000 MSC | 10% + EC | 5% |
| PhilHealth | 5% | ₱10,000 MBS | ₱100,000 MBS | 2.5% | 2.5% |
| Pag-IBIG | 2% + 2% | -- | ₱10,000 MFS | ₱200 max | ₱200 max |

Self-employed pay the full contribution for SSS (15%) and PhilHealth (5%). Pag-IBIG is voluntary for self-employed.

---

## Section 2 -- SSS (Social Security System)

### 2.1 Overview

The SSS provides social insurance for private sector workers and self-employed persons, covering sickness, maternity, disability, retirement, death, and funeral benefits.

### 2.2 Contribution Rate (2025)

| Component | Rate |
|---|---|
| Total contribution | 15% of Monthly Salary Credit (MSC) |
| Employer share (employed) | 10% |
| Employee share (employed) | 5% |
| Self-employed / voluntary | 15% (full amount) |
| Employees' Compensation (EC) | ₱10 or ₱30/month (employer only; added on top) |

### 2.3 Monthly Salary Credit (MSC) Range

| Item | Amount |
|---|---|
| Minimum MSC | ₱5,000 |
| Maximum MSC | ₱35,000 |
| Minimum monthly contribution (self-employed) | ₱750 (15% × ₱5,000) |
| Maximum monthly contribution (self-employed) | ₱5,250 (15% × ₱35,000) |

### 2.4 MSC Bracket Examples (Self-Employed)

| Monthly Compensation Range | MSC | Total Contribution (15%) |
|---|---|---|
| Below ₱5,250 | ₱5,000 | ₱750 |
| ₱5,250 -- ₱5,749.99 | ₱5,500 | ₱825 |
| ₱9,750 -- ₱10,249.99 | ₱10,000 | ₱1,500 |
| ₱14,750 -- ₱15,249.99 | ₱15,000 | ₱2,250 |
| ₱19,750 -- ₱20,249.99 | ₱20,000 | ₱3,000 |
| ₱24,750 -- ₱25,249.99 | ₱25,000 | ₱3,750 |
| ₱29,750 -- ₱30,249.99 | ₱30,000 | ₱4,500 |
| ₱34,750 and above | ₱35,000 | ₱5,250 |

Note: For MSC above ₱20,000, contributions are split between Regular SS and Mandatory Provident Fund (MPF).

### 2.5 Self-Employed Registration and Payment

| Item | Detail |
|---|---|
| Registration | SSS office, SSS website (sss.gov.ph), or SSS mobile app |
| Declaration | Self-employed declare their monthly earnings to determine MSC |
| Payment | Monthly; via SSS portal, banks, GCash, Maya, bayad centres, 7-Eleven |
| Deadline | Last day of the month for current month's contribution; or per schedule by surname |
| Can change MSC | Request MSC change via SSS; must be consistent with actual income |

### 2.6 SSS Benefits Summary

| Benefit | Key Detail |
|---|---|
| Sickness | Up to 120 days/year; daily cash allowance based on MSC |
| Maternity | 105 days (live birth), 60 days (miscarriage); cash allowance |
| Disability | Monthly pension based on credited years and MSC |
| Retirement | Monthly pension starting at age 60 (with 120 monthly contributions) |
| Death | Lump sum or monthly pension to beneficiaries |
| Funeral | ₱40,000 lump sum |
| Unemployment (WISP-Plus) | For involuntary separation; requires 36 contributions in last 48 months |

---

## Section 3 -- PhilHealth (Philippine Health Insurance Corporation)

### 3.1 Overview

PhilHealth provides mandatory national health insurance to all Filipino citizens under the Universal Health Care Act (RA 11223).

### 3.2 Contribution Rate (2025)

| Item | Value |
|---|---|
| Premium rate | 5% of Monthly Basic Salary (MBS) |
| Floor salary | ₱10,000 |
| Ceiling salary | ₱100,000 |
| Minimum monthly premium | ₱500 (5% × ₱10,000) |
| Maximum monthly premium | ₱5,000 (5% × ₱100,000) |
| Employer share (employed) | 2.5% |
| Employee share (employed) | 2.5% |
| Self-employed / voluntary / direct contributor | 5% (full amount) |

### 3.3 Self-Employed PhilHealth

| Item | Detail |
|---|---|
| Basis | Declared monthly income |
| Minimum income | ₱10,000 (premium = ₱500/month) |
| Maximum income | ₱100,000 (premium = ₱5,000/month) |
| Payment | Monthly, quarterly, semi-annual, or annual |
| Channels | PhilHealth office, online (member.philhealth.gov.ph), GCash, Maya, bayad centres |
| Benefits | Inpatient/outpatient coverage, Z benefits for catastrophic conditions |

### 3.4 PhilHealth Benefits Summary

| Benefit | Detail |
|---|---|
| Inpatient | Room and board, drugs, lab, professional fees (case rates) |
| Outpatient | Primary care, outpatient drugs, lab (in accredited facilities) |
| Z Benefits | Catastrophic conditions (cancer, etc.) |
| Maternity | Normal delivery and caesarean section packages |
| Day surgery | Covered under case rates |

---

## Section 4 -- Pag-IBIG (HDMF -- Home Development Mutual Fund)

### 4.1 Overview

Pag-IBIG is a savings programme that provides members access to housing loans, multi-purpose loans, and calamity loans.

### 4.2 Contribution Rates

| Monthly Salary | Employee Rate | Employer Rate |
|---|---|---|
| ≤₱1,500 | 1% | 2% |
| >₱1,500 | 2% | 2% |

| Item | Amount |
|---|---|
| Maximum Monthly Fund Salary (MFS) | ₱10,000 |
| Maximum employee contribution | ₱200/month (2% × ₱10,000) |
| Maximum employer contribution | ₱200/month |
| Maximum total contribution | ₱400/month |

### 4.3 Self-Employed Pag-IBIG

| Item | Detail |
|---|---|
| Status | Voluntary for self-employed |
| Minimum contribution | ₱200/month |
| Registration | Pag-IBIG Fund office or online (pagibigfund.gov.ph) |
| Payment | Monthly via Pag-IBIG portal, banks, bayad centres |
| Benefits | Housing loan (after 24 monthly contributions), multi-purpose loan (after 24 contributions), calamity loan |

### 4.4 Modified Pag-IBIG 2 (MP2)

| Item | Detail |
|---|---|
| What | Voluntary savings programme with higher dividends |
| Minimum | ₱500 per contribution |
| Term | 5 years |
| Tax | Dividends are tax-exempt |

---

## Section 5 -- Combined Monthly Cost for Self-Employed

### 5.1 Example: Self-Employed Earning ₱25,000/month

| System | Monthly Contribution |
|---|---|
| SSS (MSC ₱25,000 × 15%) | ₱3,750 |
| PhilHealth (₱25,000 × 5%) | ₱1,250 |
| Pag-IBIG (voluntary, ₱200) | ₱200 |
| **Total** | **₱5,200** |

### 5.2 Example: Self-Employed Earning ₱50,000/month

| System | Monthly Contribution |
|---|---|
| SSS (capped at MSC ₱35,000 × 15%) | ₱5,250 |
| PhilHealth (₱50,000 × 5%) | ₱2,500 |
| Pag-IBIG (voluntary, ₱200) | ₱200 |
| **Total** | **₱7,950** |

---

## Section 6 -- Payment Deadlines and Channels

### 6.1 Deadlines

| System | Employed | Self-Employed |
|---|---|---|
| SSS | By last day of month following salary month | By last day of applicable month (or per SSS schedule) |
| PhilHealth | By last day of month following salary month | Monthly/quarterly/semi-annual/annual |
| Pag-IBIG | By last day of month following salary month | Monthly |

### 6.2 Online Payment Channels

| Channel | SSS | PhilHealth | Pag-IBIG |
|---|---|---|---|
| SSS website/app | Yes | No | No |
| PhilHealth portal | No | Yes | No |
| Pag-IBIG portal | No | No | Yes |
| GCash | Yes | Yes | Yes |
| Maya | Yes | Yes | Yes |
| Bayad Centre / 7-Eleven | Yes | Yes | Yes |
| Banks (BDO, BPI, etc.) | Yes | Yes | Yes |

---

## Section 7 -- Penalties

| System | Penalty for Late/Non-Payment |
|---|---|
| SSS | 2% monthly penalty on unpaid contributions |
| PhilHealth | 2% monthly penalty; loss of benefits if contributions not up to date |
| Pag-IBIG | Membership benefits suspended until arrears are settled |

---

## Section 8 -- Tax Treatment

| Contribution | Tax Treatment |
|---|---|
| SSS (self-employed) | Not deductible as business expense; however, reduces taxable income effectively through the contribution structure |
| PhilHealth (self-employed) | Not directly deductible; part of personal obligations |
| Pag-IBIG (self-employed) | Not deductible |
| SSS (employee share) | Not subject to income tax (exempt from withholding) |
| Employer SSS/PhilHealth/Pag-IBIG | Deductible business expense for employer |

---

## Section 9 -- Reference Material

### Key Portals

| System | URL |
|---|---|
| SSS | https://www.sss.gov.ph |
| PhilHealth | https://www.philhealth.gov.ph |
| Pag-IBIG | https://www.pagibigfund.gov.ph |

### Key Legislation

| System | Act |
|---|---|
| SSS | RA 11199 (Social Security Act of 2018) |
| PhilHealth | RA 11223 (Universal Health Care Act of 2019) |
| Pag-IBIG | RA 9679 (Home Development Mutual Fund Law of 2009) |

---

## Prohibitions

- NEVER advise self-employed persons to skip SSS or PhilHealth -- both are mandatory
- NEVER use employer/employee split rates for self-employed -- self-employed pay the full rate
- NEVER exceed the MSC ceiling (₱35,000 for SSS) or MBS ceiling (₱100,000 for PhilHealth) in calculations
- NEVER assume Pag-IBIG is mandatory for self-employed -- it is voluntary
- NEVER present contribution amounts without checking the current year's official tables
- NEVER present calculations as definitive -- always verify against official SSS/PhilHealth tables

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
