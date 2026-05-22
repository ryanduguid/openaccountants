---
name: hk-mpf
description: >
  Use this skill whenever asked about Hong Kong Mandatory Provident Fund (MPF) contributions. Trigger on phrases like "MPF", "Mandatory Provident Fund", "MPF contribution", "MPFA", "retirement Hong Kong", "pension Hong Kong", "MPF self-employed", "voluntary MPF", "TVC", "tax deductible voluntary contributions", "MPF maximum", "MPF exemption", or any question about MPF obligations, rates, caps, and tax treatment in Hong Kong. Covers mandatory contributions, self-employed MPF, voluntary contributions, tax deductions, and exemptions. ALWAYS read this skill before advising on Hong Kong MPF matters.
version: 1.0
jurisdiction: HK
tax_year: 2024-25
category: international
depends_on:
  - hk-salaries-tax
verified_by: pending
---

# Hong Kong Mandatory Provident Fund (MPF) Skill v1.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Hong Kong SAR, China |
| System | Mandatory Provident Fund (MPF / 強制性公積金) |
| Currency | HKD (HK$) only |
| Contribution period | Monthly (for employees); monthly or yearly (for self-employed) |
| Primary legislation | Mandatory Provident Fund Schemes Ordinance (Cap. 485) |
| Regulator | Mandatory Provident Fund Schemes Authority (MPFA / 積金局) |
| Portal | eMPF Platform (https://www.empf.org.hk) |
| Validated by | Pending |
| Validation date | Pending |
| Skill version | 1.0 |

### Mandatory Contribution Summary

| Item | Employee | Employer | Self-Employed |
|---|---|---|---|
| Rate | 5% | 5% | 5% |
| Minimum relevant income | HK$7,100/month | -- | HK$7,100/month (or HK$85,200/year) |
| Maximum relevant income | HK$30,000/month | HK$30,000/month | HK$30,000/month (or HK$360,000/year) |
| Maximum monthly contribution | HK$1,500 | HK$1,500 | HK$1,500 |
| Maximum annual contribution | HK$18,000 | HK$18,000 | HK$18,000 |

### Below Minimum Income

| Relevant Income | Employee Contribution | Employer Contribution |
|---|---|---|
| <HK$7,100/month | HK$0 (not required) | 5% of relevant income (employer still pays) |

---

## Section 2 -- Who Must Join MPF

### 2.1 Mandatory Coverage

| Category | Requirement |
|---|---|
| Employees aged 18-64 | Employer must enrol within 60 days of employment start |
| Self-employed aged 18-64 | Must self-enrol within 60 days of becoming self-employed |
| Casual employees (construction/catering) | Covered under industry schemes |

### 2.2 Exempt Persons

| Category | Exemption |
|---|---|
| Domestic helpers | Exempt from MPF |
| Self-employed hawkers | Exempt |
| Persons covered by statutory pension/provident fund schemes | Exempt (e.g., civil servants under old pension scheme) |
| Employees from overseas temporarily in HK (<13 months) | Exempt |
| Members of ORSO-exempted schemes | May be exempt from MPF |
| Persons under 18 or over 64 | Exempt (but may contribute voluntarily) |

---

## Section 3 -- Contribution Rates and Caps

### 3.1 Employee Contributions

| Monthly Relevant Income | Employee Rate | Monthly Contribution |
|---|---|---|
| Less than HK$7,100 | 0% | HK$0 |
| HK$7,100 -- HK$30,000 | 5% | HK$355 -- HK$1,500 |
| Above HK$30,000 | 5% (capped) | HK$1,500 |

### 3.2 Employer Contributions

| Monthly Relevant Income | Employer Rate | Monthly Contribution |
|---|---|---|
| Less than HK$7,100 | 5% | Income × 5% |
| HK$7,100 -- HK$30,000 | 5% | HK$355 -- HK$1,500 |
| Above HK$30,000 | 5% (capped) | HK$1,500 |

Employer ALWAYS contributes 5%, even when employee's income is below HK$7,100.

### 3.3 Self-Employed Contributions

| Relevant Income | Contribution |
|---|---|
| Less than HK$7,100/month (or HK$85,200/year) | Not required |
| HK$7,100 -- HK$30,000/month | 5% of relevant income |
| Above HK$30,000/month (or HK$360,000/year) | HK$1,500/month (or HK$18,000/year) |

Self-employed must enrol regardless of income level but contribution is not required if below the minimum.

### 3.4 Contribution Frequency (Self-Employed)

| Option | Detail |
|---|---|
| Monthly | Contribute on a chosen day each month |
| Yearly | Contribute by the last day of the scheme's financial year |
| Income declaration | Self-employed declare relevant income to the eMPF Platform |

---

## Section 4 -- Relevant Income

### 4.1 What Counts as Relevant Income

| Included | Excluded |
|---|---|
| Wages / salary | Severance payments |
| Commissions | Long service payments |
| Bonuses | Jury duty fees |
| Allowances (housing, transport, etc.) | Benefits in kind (non-cash) |
| Tips (if paid through employer) | |

### 4.2 Self-Employed Relevant Income

For self-employed persons, relevant income is the net assessable profits for Profits Tax purposes (assessable profits less allowable deductions).

---

## Section 5 -- Tax Treatment

### 5.1 Mandatory Contributions

| Item | Tax Treatment |
|---|---|
| Employee mandatory contribution | Deductible from salaries tax; max HK$18,000/year |
| Employer mandatory contribution | Deductible business expense; max HK$18,000 per employee/year |
| Self-employed mandatory contribution | Deductible from profits tax; max HK$18,000/year |

### 5.2 Voluntary Contributions

| Type | Tax Treatment |
|---|---|
| Standard voluntary contributions | NOT tax deductible |
| Tax Deductible Voluntary Contributions (TVC) | Deductible up to HK$60,000/year (combined with qualifying annuity premiums) |

### 5.3 TVC (Tax Deductible Voluntary Contributions)

| Item | Detail |
|---|---|
| Max deduction | HK$60,000/year (combined with qualifying annuity premiums) |
| Eligible schemes | Special TVC account within an MPFA-approved MPF scheme |
| Who can claim | Any taxpayer (employee, self-employed, or non-working spouse) |
| Claim on | Salaries tax, Profits Tax, or Personal Assessment return |
| Preservation | Same rules as mandatory -- cannot withdraw until age 65 |

---

## Section 6 -- Payment and Compliance

### 6.1 Payment Deadlines

| Contributor | Deadline |
|---|---|
| Employer (for employees) | Within 10 days after month end (contribution day) |
| Self-employed (monthly) | On the chosen contribution day each month |
| Self-employed (yearly) | Last day of the scheme's financial year |

### 6.2 Abolition of MPF Offsetting (from 25 May 2025)

| Item | Detail |
|---|---|
| Previous rule | Employers could offset severance/long service payments against their MPF contributions |
| New rule | From 25 May 2025, employer mandatory contributions on or after this date can NO longer be used to offset severance/long service payments |
| Transitional | Contributions made before 25 May 2025 can still be used for offsetting under grandfathering rules |

### 6.3 Penalties

| Offence | Penalty |
|---|---|
| Failure to enrol employee | Fine up to HK$350,000 + imprisonment up to 3 years |
| Late contribution | 5% surcharge on outstanding amount |
| Failure to contribute | Fine up to HK$350,000 + imprisonment up to 3 years |
| Self-employed failure to enrol | Fine up to HK$50,000 |

---

## Section 7 -- Withdrawal of MPF Benefits

### 7.1 Permitted Withdrawal Events

| Event | Condition |
|---|---|
| Retirement | Aged 65 |
| Early retirement | Aged 60 with permanent departure from workforce |
| Permanent departure from HK | Statutory declaration + evidence |
| Total incapacity | Medical certification |
| Terminal illness | Medical certification |
| Small balance | Account balance ≤HK$5,000 + no contributions for 12 months |
| Death | Payment to personal representative / nominee |

### 7.2 Tax on Withdrawal

MPF benefits withdrawn are generally NOT subject to salaries tax or profits tax.

---

## Section 8 -- Worked Examples

### Example 1 -- Employee Earning HK$25,000/month

| | Employee | Employer |
|---|---|---|
| Relevant income | $25,000 | $25,000 |
| Rate | 5% | 5% |
| Monthly contribution | $1,250 | $1,250 |
| Annual contribution | $15,000 | $15,000 |
| Tax deduction (employee) | $15,000 (within $18,000 cap) | -- |

### Example 2 -- Employee Earning HK$50,000/month

| | Employee | Employer |
|---|---|---|
| Relevant income | $50,000 (capped at $30,000) | $50,000 (capped at $30,000) |
| Monthly contribution | $1,500 | $1,500 |
| Annual contribution | $18,000 | $18,000 |

### Example 3 -- Self-Employed, Annual Income HK$400,000

| Item | Amount |
|---|---|
| Relevant income | $400,000 (capped at $360,000) |
| Annual contribution | $18,000 |
| Additional TVC | $42,000 (to reach $60,000 total deduction with annuity) |
| Total tax deduction | $18,000 (mandatory) + $42,000 (TVC) = $60,000 |

---

## Section 9 -- MPFA-Approved Schemes

| Provider Type | Examples |
|---|---|
| Major trustees | HSBC, Manulife, AIA, Sun Life, BCT, BEA |
| eMPF Platform | Centralized platform for all MPF management (launched 2025) |
| Default Investment Strategy (DIS) | Standardised low-fee option in every scheme |

Self-employed persons can choose any MPFA-approved scheme.

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| MPF Ordinance | Cap. 485, Mandatory Provident Fund Schemes Ordinance |
| Contribution rates | MPF General Regulation (Cap. 485A) |
| Tax deduction (mandatory) | IRO Section 12(1)(e) |
| Tax deduction (TVC) | IRO Section 26N |
| Offsetting abolition | Employment and Retirement Schemes Legislation (Offsetting Arrangement) (Amendment) Ordinance 2022 |

### Key Resources

| Resource | URL |
|---|---|
| MPFA | https://www.mpfa.org.hk |
| eMPF Platform | https://www.empf.org.hk |
| IRD MPF FAQ | https://www.ird.gov.hk/eng/faq/mpf.htm |
| Contribution calculator | https://www.mpfa.org.hk/en/mpf-system/contribution-calculator |

---

## Prohibitions

- NEVER calculate employee contributions on income below HK$7,100/month -- employee contributes $0
- NEVER forget that employers MUST contribute 5% even when employee income is below HK$7,100
- NEVER exceed the HK$30,000/month (HK$360,000/year) cap in contribution calculations
- NEVER claim standard voluntary contributions as tax deductible -- only TVC qualifies
- NEVER combine mandatory and TVC deductions -- they have separate caps ($18,000 and $60,000 respectively)
- NEVER advise on MPF offsetting without considering the 25 May 2025 abolition date
- NEVER present calculations as definitive -- always verify against official MPFA guidelines

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
