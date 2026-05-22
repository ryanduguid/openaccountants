---
name: tw-income-tax
description: >
  Use this skill whenever asked about Taiwan (ROC) individual income tax for self-employed or professional individuals. Trigger on phrases like "Taiwan income tax", "ROC income tax", "consolidated income tax", "Taiwan tax return", "eFiling Taiwan", "etax.nat.gov.tw", "執行業務所得", "其他所得", "standard deduction Taiwan", "special deduction Taiwan", "National Taxation Bureau", "withholding tax Taiwan", or any question about Taiwanese income tax rates, deductions, exemptions, or filing for individuals. Covers progressive rates, standard and itemized deductions, special deductions, self-employed income categories, withholding, and May filing. ALWAYS read this skill before touching any Taiwan income tax work.
version: 1.0
jurisdiction: TW
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
verified_by: pending
---

# Taiwan (ROC) Income Tax -- Self-Employed Skill v1.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Taiwan (Republic of China / 中華民國) |
| Tax | Individual Consolidated Income Tax (綜合所得稅) |
| Currency | TWD / NT$ (New Taiwan Dollar) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (所得稅法) |
| Tax authority | National Taxation Bureau (國稅局) under the Ministry of Finance |
| Filing portal | eFiling (https://tax.nat.gov.tw) |
| Filing deadline | 1 -- 31 May of the following year |
| Validated by | Pending -- requires sign-off by a Taiwan CPA (會計師) |
| Validation date | Pending |
| Skill version | 1.0 |

### Progressive Tax Rates (2025)

| Net Taxable Income (NT$) | Rate | Progressive Difference | Tax Formula |
|---|---|---|---|
| 0 -- 590,000 | 5% | NT$0 | Income × 5% |
| 590,001 -- 1,330,000 | 12% | NT$41,300 | Income × 12% - 41,300 |
| 1,330,001 -- 2,660,000 | 20% | NT$147,700 | Income × 20% - 147,700 |
| 2,660,001 -- 4,980,000 | 30% | NT$413,700 | Income × 30% - 413,700 |
| 4,980,001+ | 40% | NT$911,700 | Income × 40% - 911,700 |

### Exemption (2025)

| Item | Amount (NT$) |
|---|---|
| Personal exemption (per taxpayer, spouse, dependant) | NT$97,000 |
| Personal exemption (aged 70+) | NT$145,500 |

### Standard Deduction (2025)

| Filing Status | Amount (NT$) |
|---|---|
| Single | NT$131,000 |
| Married filing jointly | NT$262,000 |

### Non-Resident Tax

| Income Type | Rate |
|---|---|
| Wages/salary (residing <183 days) | 18% withholding (or 6% for ≤1.5× minimum wage) |
| Professional fees | 20% withholding |
| Other income | 20% withholding |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown residency status | Non-resident (higher withholding) until confirmed |
| Unknown deduction preference | Standard deduction |
| Unknown special deduction eligibility | Do not claim |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- total income for the year, residency status (≥183 days in Taiwan), marital status, number of dependants.

**Recommended** -- withholding tax statements (扣繳憑單), prior year tax filing, professional income records, insurance premium records.

**Ideal** -- complete income and expense records for professional practice, NHI premium statements, rental contract (if claiming rent deduction), donation receipts.

### Refusal Catalogue

**R-TW-1 -- Corporate income.** "This skill covers individuals only. Companies (公司) file corporate income tax. Escalate to a Taiwan CPA."

**R-TW-2 -- Non-resident complex income.** "Non-residents with multiple Taiwan-sourced income types require specialist analysis on withholding and treaty application."

**R-TW-3 -- Alternative Minimum Tax (AMT).** "High-income individuals may be subject to the Income Basic Tax (基本所得額). This requires separate computation under the Income Basic Tax Act."

---

## Section 3 -- Income Categories for Self-Employed

### 3.1 Category 2 -- Professional Practice Income (執行業務所得)

| Item | Detail |
|---|---|
| Who | Licensed professionals practicing independently: lawyers, CPAs, architects, doctors, engineers, artists |
| Gross income | Total fees received |
| Deductions | Actual expenses (with receipts and books) OR deemed expense ratios set by the National Taxation Bureau (varies by profession, typically 20-50% of gross) |
| Net income | Gross - deductions = taxable professional income |
| Withholding | Payor withholds 10% on professional fees paid to residents |

### 3.2 Category 6 -- Other Income (其他所得)

| Item | Detail |
|---|---|
| Who | Freelancers, consultants, independent workers not in regulated professions |
| Gross income | Total income from activities |
| Deductions | Actual costs and necessary expenses (with documentation) |
| Net income | Gross - documented expenses = taxable other income |

### 3.3 Category 1 -- Employment Income (薪資所得)

| Item | Detail |
|---|---|
| Who | Employees |
| Special deduction | NT$218,000 per person (2025) |
| Withholding | Employer withholds per tax withholding table |

---

## Section 4 -- Deductions

### 4.1 Standard vs Itemized

Taxpayers choose EITHER standard deduction OR itemized deductions (cannot combine).

### 4.2 Itemized Deductions

| Deduction | Limit (NT$) |
|---|---|
| Donations (to government, defence, education) | No limit |
| Donations (to approved charities) | 20% of consolidated income |
| Insurance premiums (per person, excluding NHI) | NT$24,000/year |
| NHI premiums | No limit (fully deductible) |
| Medical expenses (unreimbursed) | No limit |
| Disaster losses | Actual loss (verified) |
| Mortgage interest (principal residence) | NT$300,000/year |
| Political donations | NT$200,000/year |

### 4.3 Special Deductions (2025)

| Special Deduction | Amount (NT$) | Notes |
|---|---|---|
| Wage/salary income (薪資所得特別扣除額) | NT$218,000 per person | Employees and self-employed with salary income |
| Savings and investment interest (儲蓄投資特別扣除額) | NT$270,000 per household | Interest and dividend income |
| Disabled persons (身心障礙特別扣除額) | NT$218,000 per person | Registered disabled |
| Preschool children (幼兒學前特別扣除額) | NT$150,000 for first child; NT$225,000 for second+ | Children under 6 |
| Long-term care (長期照顧特別扣除額) | NT$120,000 per person | Qualifying care recipients |
| Housing rent (房屋租金支出特別扣除額) | NT$180,000 per household | From 2024; replaces former itemized deduction |

Note: The preschool child and long-term care special deductions are subject to income thresholds (not available if applicable tax rate exceeds 20% or if claiming standard rate on certain income).

---

## Section 5 -- Tax Computation

### 5.1 Formula

```
Consolidated Income
  - Exemptions (NT$97,000 × number of persons)
  - Deductions (standard OR itemized)
  - Special Deductions
  - Basic Living Expense Difference (if applicable)
= Net Taxable Income
  → Apply progressive rates
= Tax Payable
  - Withholding tax already paid
  - Investment tax credits (if any)
= Tax Due / Refund
```

### 5.2 Basic Living Expense (基本生活費差額)

If (exemptions + deductions + special deductions) < (basic living expense × number of persons in household), the difference is additionally deducted. For 2025, basic living expense per person is approximately NT$210,000 (verify with annual announcement).

---

## Section 6 -- Worked Examples

### Example 1 -- Freelance Designer (Category 6), Single

**Input:** Gross income NT$1,500,000. Documented expenses NT$400,000. No other income.

**Computation:**
- Net Category 6 income: NT$1,500,000 - NT$400,000 = NT$1,100,000
- Exemption: NT$97,000
- Standard deduction: NT$131,000
- No special deductions applicable (no salary, not disabled)
- Net taxable income: NT$1,100,000 - NT$97,000 - NT$131,000 = NT$872,000

**Tax:** NT$872,000 × 12% - NT$41,300 = NT$63,340

**Less withholding:** If payors withheld 10% on some payments, credit those amounts.

### Example 2 -- CPA (Category 2), Married, One Child Under 6

**Input:** Professional fees NT$3,000,000. Deemed expense ratio 30%. Spouse has salary income NT$800,000. One child aged 4.

**Computation:**
- CPA net income: NT$3,000,000 × 70% = NT$2,100,000
- Spouse salary income: NT$800,000
- Consolidated income: NT$2,900,000
- Exemptions: 3 × NT$97,000 = NT$291,000
- Standard deduction (married): NT$262,000
- Spouse salary special deduction: NT$218,000
- Preschool child: NT$150,000
- Net taxable income: NT$2,900,000 - NT$291,000 - NT$262,000 - NT$218,000 - NT$150,000 = NT$1,979,000

**Tax:** NT$1,979,000 × 20% - NT$147,700 = NT$248,100

---

## Section 7 -- Filing

### 7.1 Filing Period and Methods

| Item | Detail |
|---|---|
| Filing period | 1 May -- 31 May |
| eFiling | Via https://tax.nat.gov.tw using Citizen Digital Certificate, Health IC Card, or registered phone |
| Paper filing | At local National Taxation Bureau offices |
| Extension | Generally not available; special circumstances may qualify |
| Amended return | Can be filed within 5 years if overpaid; penalties apply if underpaid |

### 7.2 Withholding on Self-Employed Income

| Income Type | Withholding Rate (Resident) |
|---|---|
| Professional fees (Category 2) | 10% |
| Salary/wages (Category 1) | Per withholding table |
| Rent (Category 5) | 10% |
| Royalties | 10% |

### 7.3 Penalties

| Offence | Penalty |
|---|---|
| Late filing | Surcharge: up to 15% of tax underpaid (sliding scale by delay) |
| Failure to file | Estimated assessment + penalty up to 3× tax evaded |
| Negligent understatement | 10% of additional tax |
| Intentional evasion | Fine + potential criminal prosecution |

---

## Section 8 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Income tax rates | Income Tax Act (所得稅法), Article 5 |
| Exemptions | Article 17-1 |
| Deductions | Article 17 |
| Professional income | Article 14, Category 2 |
| Other income | Article 14, Category 6 |
| Filing | Articles 71-75 |
| Withholding | Articles 88-92 |

### Key Resources

| Resource | URL |
|---|---|
| eFiling portal | https://tax.nat.gov.tw |
| National Taxation Bureau of Taipei | https://www.ntbt.gov.tw/English |
| Taxation Administration, MOF | https://www.dot.gov.tw/eng |
| Tax rate table | https://www.ntbt.gov.tw/English/multiplehtml/3f18d2625aea4187b0d90e9b929afe4c |

---

## Prohibitions

- NEVER ignore the choice between standard and itemized deductions -- compute both and recommend the more beneficial
- NEVER apply resident rates to individuals present in Taiwan <183 days
- NEVER claim both standard deduction and itemized deductions
- NEVER forget to account for withholding tax already paid on professional fees
- NEVER use deemed expense ratios without checking the current year's published rates for the profession
- NEVER present calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
