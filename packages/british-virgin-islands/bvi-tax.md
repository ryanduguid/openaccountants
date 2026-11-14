---
name: bvi-tax
description: British Virgin Islands tax reference for payroll, ordinary income tax, social contributions, customs and business company obligations. Read the linked guides for the applicable period.
version: 2.1
jurisdiction: VG
tax_year: 2025
last_updated: 2026-11-11
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bvi Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | British Virgin Islands (BVI) |
| Tax | Payroll tax (primary), customs duties, property tax, social security, NHI |
| Currency | USD |
| Tax year | Calendar year |
| Primary legislation | Payroll Taxes Act, 2004 (as amended); Customs Management and Duties Act |
| Supporting legislation | BVI Business Companies Act, 2004; Economic Substance Act, 2018 |
| Tax authority | Inland Revenue Department (IRD) |
| Filing portal | [eTax](https://efiling.gov.vg/) from 2 November 2026. [Ministry of Finance release](https://www.gov.vg/news/ministry-finance-launches-enhanced-etax-portal-and-online-tax-payments) |
| Filing deadline | See the [payroll guide](vg-payroll-social.md) for the monthly and annual rules and their effective periods. |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a licensed BVI practitioner |
| Skill version | 2.1 |

### Tax Landscape

**Tax Landscape**

| Tax Type | Status |
| --- | --- |
| Ordinary income tax | Zero-rated from 1 January 2005 according to the FSC. See the [income tax guide](vg-corporate-income-tax.md) for the retained Ordinance and company exemption. |
| Gains on BVI business company securities | Section 242 exempts these gains from the Income Tax Ordinance. See the [income tax guide](vg-corporate-income-tax.md). |
| VAT / Sales Tax | None |
| BVI business company payments | Section 242 exempts payments by companies within its scope from the Income Tax Ordinance. Check foreign withholding separately. |
| Payroll Tax | Yes |
| Customs Duties | Yes |
| Property Tax | Yes |
| Social Security (SSB) | Private sector 4% employee and 4.5% employer. See the [Social Security Board](https://www.vissb.vg/contributions/) for other categories. |
| National Health Insurance (NHI) | For employees, 3.75% each for employer and employee. See the [contributions guide](vg-payroll-social.md). |

### Payroll Tax Rates

See the [payroll guide](vg-payroll-social.md) for the class rates, employer liability, employee deductions and the annual exemption.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown employer class | Confirm the class with Inland Revenue before calculating the liability. |
| Unknown duty rate | General merchandise |
| Unknown economic substance | Assume relevant activity applies |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- payroll records, employee count, employer classification.

**Recommended** -- remuneration breakdown by employee, BVI BC registration, prior returns.

**Ideal** -- complete payroll export, economic substance filings, customs records.

### Refusal Catalogue

- **R-VG-1 — Income tax** — Check the [ordinary zero rate and company exemption](vg-corporate-income-tax.md). Confirm the applicable entity, period and any earlier assessment or top-up tax before giving a conclusion.
- **R-VG-2 -- VAT/sales tax** — BVI has no VAT or sales tax.  _(R-VG-2)_
- **R-VG-3 -- Economic substance detail** — Escalate to specialist.  _(R-VG-3)_
- **R-VG-4 -- CRS/FATCA compliance** — Escalate to specialist.  _(R-VG-4)_

## Section 3 -- Compliance Pattern Library

### 3.1 Employer Payment Patterns

**Employer Payment Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, BONUS, COMMISSION | Payroll tax base | Include in taxable remuneration |
| BENEFITS IN KIND | Payroll tax base | Include |
| CONTRACTOR | Check status | Determine whether the person is an employee, deemed employee or self-employed. |
| SSB CONTRIBUTION | Social Security | Private sector 4% employee and 4.5% employer. [Social Security Board](https://www.vissb.vg/contributions/) |
| NHI CONTRIBUTION | Health insurance | For employees, 3.75% each. See the [contributions guide](vg-payroll-social.md). |

### 3.2 Customs Duty Categories

**Customs Duty Categories**

| Category | Rate |
| --- | --- |
| General merchandise | 5% -- 20% |
| Food/essential goods | Lower or exempt |
| Motor vehicles | 20% + environmental levy |
| Building materials | 5% -- 10% |

### 3.3 BVI BC Annual Fees

See the [company formation guide](vg-company-formation.md) for the fee categories and annual due dates.

## Section 4 -- Worked Examples

### Example 1 -- Payroll Tax (Class 2)

If Inland Revenue confirms a Class 2 employer has US$50,000 of taxable remuneration after applying the exemption, the total at 14% is US$7,000. Apply any permitted recovery from employees to their individual taxable amounts. Calculate Social Security and NHI separately. [Payroll and social contributions](vg-payroll-social.md)
### Example 2 -- BVI BC Annual Obligations

**Input:** BVI BC with 10,000 no-par shares, no employees.

**Classification:** Check the [annual fee and financial return](vg-company-formation.md) and the [section 242 exemption](vg-corporate-income-tax.md). Check whether there is any deemed remuneration and whether economic substance reporting applies.

### Example 3 -- Import Duty

**Input:** Office equipment USD 10,000.

**Computation:** Duty ~15%: USD 1,500. No VAT. No sales tax.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Ordinary Income Tax and VAT

- See [corporate income tax](vg-corporate-income-tax.md) for the ordinary zero rate and section 242 exemption. See the [VAT and customs guide](vg-vat-gst.md) for indirect taxes.

### 5.2 Payroll Tax Filing

- See the [payroll guide](vg-payroll-social.md) for the 2007 change to monthly filing, the annual return and the 2026 eTax route.

### 5.3 Social Security and NHI

- See the [payroll guide](vg-payroll-social.md) for the different contribution categories and earnings caps.
## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Payroll Tax Exemptions

- **Payroll tax exemptions** — Small business concessions may apply. Flag for practitioner.

### 6.2 Economic Substance

- **Economic substance** — Entities conducting relevant activities must demonstrate adequate substance in BVI. Flag for specialist.

### 6.3 Stamp Duty

- **Stamp duty on real estate** — Real estate: 4% buyer + 4% seller. Belonger concessions may apply.

## Section 7 -- Excel Working Paper Template

```
BVI TAX -- Working Paper

A. PAYROLL TAX
  A1. Total remuneration          ___________
  A2. Employer class              ___________
  A3. Employer payroll tax        ___________
  A4. Employee payroll tax        ___________

B. SOCIAL SECURITY & NHI
  B1. SSB employer (4.5%)         ___________
  B2. NHI employer (3.75%)        ___________

C. BVI BC FEES
  C1. Annual government fee       ___________

REVIEWER FLAGS:
  [ ] Employer classification confirmed?
  [ ] Employee exemption applied?
  [ ] Economic substance filing required?
```

## Section 8 -- Bank Statement Reading Guide

**Bank Statement Reading Guide**

| Bank | Format | Key Fields |
| --- | --- | --- |
| VP Bank, First Caribbean | PDF, CSV | Date, Description, Debit, Credit, Balance |
| Scotiabank BVI | CSV | Date, Narrative, Amount |

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- BVI TAX
1. Do you have employees in BVI?
2. How many employees?
3. Total payroll?
4. Employer class (1 or 2)?
5. Do you import goods?
6. BVI Business Company held?
7. Relevant activities for economic substance?
8. Non-Belonger employees (work permits)?
9. Property in BVI?
10. Prior returns available?
```

## Section 10 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| Payroll tax | Payroll Taxes Act, 2004 |
| Customs | Customs Management and Duties Act |
| BVI BCs | BVI Business Companies Act, 2004 |
| Economic substance | Economic Substance Act, 2018 |
| Social security | Social Security Act |
| Health insurance | National Health Insurance Act |

## PROHIBITIONS

- Confirm the applicable income tax period, entity and provision before applying the ordinary zero rate or a company exemption.
- NEVER state BVI has VAT or sales tax -- it does not
- Check the relevant guide before calculating a tax on a BVI transaction.
- NEVER ignore payroll tax obligations
- NEVER confuse government fees with taxes
- NEVER ignore economic substance requirements
- NEVER ignore SSB and NHI contributions
- NEVER present calculations as definitive

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
