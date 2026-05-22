---
name: hk-salaries-tax
description: >
  Use this skill whenever asked about Hong Kong salaries tax for employees or individuals with mixed employment/self-employment income. Trigger on phrases like "Hong Kong salaries tax", "HK tax", "IRD", "Inland Revenue Department Hong Kong", "BIR60", "tax return Hong Kong", "provisional salaries tax", "standard rate Hong Kong", "progressive rate Hong Kong", "personal assessment Hong Kong", "allowances Hong Kong", "ird.gov.hk", or any question about Hong Kong salaries tax rates, allowances, deductions, or filing. Covers progressive rates, standard rate, allowances, deductions, provisional tax, and filing. ALWAYS read this skill before touching any Hong Kong salaries tax work.
version: 1.0
jurisdiction: HK
tax_year: 2024-25
category: international
depends_on:
  - income-tax-workflow-base
verified_by: pending
---

# Hong Kong Salaries Tax Skill v1.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Hong Kong SAR, China |
| Tax | Salaries Tax (薪俸稅) |
| Currency | HKD (Hong Kong Dollar / HK$) only |
| Tax year | 1 April -- 31 March (e.g., 2024/25 = 1 April 2024 -- 31 March 2025) |
| Primary legislation | Inland Revenue Ordinance (Cap. 112) |
| Tax authority | Inland Revenue Department (IRD) |
| Filing portal | eTAX (https://www.gov.hk/en/residents/taxes/etax/) |
| Filing deadline | Typically 1 month from date of issue of tax return (BIR60); usually due in June-July |
| Validated by | Pending -- requires sign-off by a Hong Kong CPA |
| Validation date | Pending |
| Skill version | 1.0 |

### Progressive Tax Rates on Net Chargeable Income (2024/25 onwards)

| Net Chargeable Income (HK$) | Rate | Tax on Band | Cumulative Tax |
|---|---|---|---|
| First 50,000 | 2% | $1,000 | $1,000 |
| Next 50,000 | 6% | $3,000 | $4,000 |
| Next 50,000 | 10% | $5,000 | $9,000 |
| Next 50,000 | 14% | $7,000 | $16,000 |
| Remainder | 17% | -- | -- |

### Two-Tiered Standard Rate (from 2024/25)

| Net Income (HK$) | Rate |
|---|---|
| First $5,000,000 | 15% |
| Remainder | 16% |

Tax payable is the LOWER of: (a) progressive rates on net chargeable income, or (b) standard rate on net income.

**Net chargeable income** = Assessable income - Deductions - Allowances
**Net income** = Assessable income - Deductions (before allowances)

### Allowances (2024/25)

| Allowance | Amount (HK$) |
|---|---|
| Basic allowance | $132,000 |
| Married person's allowance | $264,000 |
| Child allowance (per child) | $130,000 |
| Additional child allowance (year of birth) | $130,000 |
| Dependent parent/grandparent (aged 60+) | $50,000 |
| Dependent parent/grandparent (aged 55-59) | $25,000 |
| Additional dependent parent/grandparent (residing together, 60+) | $50,000 |
| Additional dependent parent/grandparent (residing together, 55-59) | $25,000 |
| Single parent allowance | $132,000 |
| Disabled dependant allowance | $75,000 |
| Personal disability allowance | $75,000 |

### Tax Reduction (2024/25)

100% reduction of final tax, subject to a ceiling of HK$1,500 per case.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown marital status | Single (basic allowance only) |
| Unknown number of children | Zero |
| Unknown deduction eligibility | No deductions claimed |
| Unknown whether standard or progressive | Compute both; apply lower |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- total assessable income for the year, marital status, and number of children.

**Recommended** -- employer's Form IR56B, MPF contribution records, charitable donation receipts, self-education expense records, prior year tax assessment.

**Ideal** -- complete BIR60 data, all supporting documents for deductions and allowances, employment contracts.

### Refusal Catalogue

**R-HK-1 -- Profits tax matters.** "Self-employed persons with sole proprietorship income are assessed under Profits Tax, not Salaries Tax (unless electing Personal Assessment). For Profits Tax on business income, use the Hong Kong Profits Tax skill."

**R-HK-2 -- Non-Hong Kong income.** "Hong Kong taxes on a territorial basis. Income not arising in or derived from Hong Kong is generally not taxable. Determining source of income requires specialist analysis."

**R-HK-3 -- Tax treaty claims.** "Hong Kong has Comprehensive Avoidance of Double Taxation Agreements (CDTAs) with multiple jurisdictions. Treaty claim analysis is out of scope."

---

## Section 3 -- Deductions (Allowable from Assessable Income)

### 3.1 Statutory Deductions

| Deduction | Limit (HK$) |
|---|---|
| MPF mandatory contributions | $18,000/year |
| Approved charitable donations | 35% of assessable income (after other deductions) |
| Self-education expenses | $100,000/year |
| Elderly residential care expenses | $100,000/year |
| Home loan interest | $100,000/year (max 20 years of assessment) |
| Qualifying annuity premiums + voluntary MPF contributions | $60,000/year (combined) |
| Domestic rent deduction (from 2022/23) | $100,000/year |

### 3.2 Key Rules

- MPF voluntary contributions (Tax Deductible Voluntary Contributions / TVC) are deductible up to $60,000 combined with qualifying annuity premiums
- Self-education must be for a prescribed course of education
- Home loan interest deduction requires the property to be the taxpayer's principal residence
- Domestic rent deduction: the taxpayer must not own any domestic property in HK at any time during the year

---

## Section 4 -- Provisional Salaries Tax

### 4.1 How It Works

| Item | Detail |
|---|---|
| What | Advance payment of next year's tax, based on current year's assessment |
| Amount | 100% of the current year's net tax payable (after tax reduction) |
| Payment | Typically in two instalments: 75% (January) and 25% (April) |
| Credit | Provisional tax paid is credited against the following year's final assessment |

### 4.2 Applying for Holdover

If you expect next year's income to be substantially lower, you can apply to hold over (reduce) provisional tax.

| Condition | Detail |
|---|---|
| Income drop ≥10% | Can apply for holdover |
| Cessation of employment | Can apply for holdover |
| Increased allowances/deductions | Can apply for holdover |
| Application deadline | 28 days before the due date of the instalment, or 14 days after the notice date (whichever is later) |

---

## Section 5 -- Personal Assessment

### 5.1 What Is Personal Assessment

Personal Assessment aggregates ALL income (salaries, profits, rental) of an individual and applies progressive rates and allowances. It can reduce total tax for individuals with multiple income sources.

### 5.2 Eligibility

| Condition | Requirement |
|---|---|
| Residency | Must be a Hong Kong permanent resident, or a temporary resident in HK for the full year, or a temporary resident married to a permanent resident |
| Application | Must elect annually (Section 41 of the IRO) |

### 5.3 When Beneficial

- Individual has rental losses to set off against salaries income
- Individual has both profits tax and salaries tax liabilities
- Total tax under Personal Assessment is lower than separate assessments

---

## Section 6 -- Worked Examples

### Example 1 -- Single Employee, Moderate Income

**Input:** Annual salary HK$600,000. Single, no children. MPF mandatory contribution HK$18,000.

**Progressive method:**
- Assessable income: $600,000
- Less deductions: MPF $18,000
- Net income: $582,000
- Less basic allowance: $132,000
- Net chargeable income: $450,000

Tax:
- First $50,000 at 2% = $1,000
- Next $50,000 at 6% = $3,000
- Next $50,000 at 10% = $5,000
- Next $50,000 at 14% = $7,000
- Remaining $250,000 at 17% = $42,500
- Total: $58,500

**Standard rate method:**
- Net income: $582,000 × 15% = $87,300

**Tax payable:** Lower amount = $58,500 (progressive). Less tax reduction (100%, max $1,500) = **$57,000**.

### Example 2 -- Married, Two Children

**Input:** Annual salary HK$1,200,000. Married (spouse no income), 2 children. MPF $18,000.

**Net income:** $1,200,000 - $18,000 = $1,182,000
**Net chargeable income:** $1,182,000 - $264,000 (married) - $260,000 (2 × $130,000 children) = $658,000

**Progressive tax:** $16,000 + ($658,000 - $200,000) × 17% = $16,000 + $77,860 = $93,860
**Standard rate:** $1,182,000 × 15% = $177,300

**Tax payable:** $93,860 - $1,500 reduction = **$92,360**.

---

## Section 7 -- Filing

### 7.1 Timeline

| Event | Typical Date |
|---|---|
| BIR60 issued by IRD | Early May |
| Filing deadline | 1 month from issue (typically early June; extension to early August for eTAX filers) |
| Assessment notice | September -- November |
| Provisional tax 1st instalment (75%) | January |
| Provisional tax 2nd instalment (25%) | April |

### 7.2 Filing Methods

| Method | Detail |
|---|---|
| eTAX | Online filing at https://www.gov.hk/en/residents/taxes/etax/ |
| Paper BIR60 | Post to IRD |
| Tax representative | Authorised tax agent can file on behalf |

### 7.3 Penalties

| Offence | Penalty |
|---|---|
| Failure to file return | Fine up to HK$10,000 + 3× tax undercharged |
| Late filing | Estimated assessment; penalty proceedings |
| Incorrect return | Fine up to HK$10,000 + 3× tax undercharged |
| Wilful evasion | Fine up to HK$50,000 + imprisonment up to 3 years + 3× tax evaded |

---

## Section 8 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Salaries tax | IRO Sections 8-13 |
| Allowances | IRO Sections 28-33 |
| Deductions | IRO Sections 12(1), 26C-26N |
| Provisional tax | IRO Section 63H |
| Personal Assessment | IRO Sections 41-43 |
| Standard rate | IRO Section 12B (two-tiered from 2024/25) |
| Tax reduction | IRO Section 20AR |

### Key IRD Resources

| Resource | URL |
|---|---|
| eTAX portal | https://www.gov.hk/en/residents/taxes/etax/ |
| Tax calculator | https://www.gov.hk/en/residents/taxes/taxfiling/taxrates/salariesrates.htm |
| IRD main site | https://www.ird.gov.hk |
| Allowances table | https://www.ird.gov.hk/eng/pdf/pam61e.pdf |

---

## Prohibitions

- NEVER apply standard rate without comparing to progressive rate -- always use the LOWER amount
- NEVER claim both basic allowance and married person's allowance for the same taxpayer
- NEVER claim child allowance for both spouses -- must be claimed en bloc by one parent
- NEVER ignore provisional salaries tax -- it is mandatory and based on 100% of current year tax
- NEVER treat Hong Kong profits tax (self-employed) as salaries tax -- different regime
- NEVER advise on source of income issues -- territorial basis determination requires specialist analysis
- NEVER present calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
