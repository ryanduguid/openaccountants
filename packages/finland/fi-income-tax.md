---
name: fi-income-tax
description: Use this skill whenever asked about Finland income tax for self-employed individuals or freelancers. Trigger on phrases like "Finland income tax", "Finnish tax", "Verohallinto", "OmaVero", "vero.fi", "elinkeinotulo", "pääomatulo", "ansiotulo", "Finnish tax return", "ennakkoperintä", "municipal tax Finland", "capital income Finland", "state tax Finland", or any question about Finnish income tax filing, rates, or deductions for self-employed persons. Covers progressive state tax, municipal tax, capital income tax, church tax, deductions, and filing via OmaVero. ALWAYS read this skill before touching any Finland income tax work.
version: 1.2
jurisdiction: FI
tax_year: 2025
last_updated: 2026-10-16
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FI Income Tax

This Tier 2 draft retains 2025 rate, deduction and calculation material that
still needs period-specific verification before a complete financial output.
Version 1.2 corrects the church-membership default and the natural-person
filing-penalty framework using the cited primary rules. It does not verify the
remaining income-tax examples or supply final annual rounding. Hold dependent
amounts under the income-tax workflow base until their rules and inputs are proved.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Finland (Republic of Finland / Suomen tasavalta) |
| Tax | Income Tax (tulovero) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (tuloverolaki 1535/1992); Act on Tax Prepayments (ennakkoperintälaki 1118/1996) |
| Supporting legislation | Business Income Tax Act (laki elinkeinotulon verottamisesta 360/1968); Municipal Tax Act |
| Tax authority | Finnish Tax Administration (Verohallinto / Vero) |
| Filing portal | OmaVero (https://www.vero.fi/omavero) |
| Filing deadline | Self-employed: 1 April of the following year. Employees: one of several April dates, assigned per taxpayer and printed on the return and in MyTax -- **1, 14, 21 or 28 April 2026** for tax year 2025 (they were 15, 22 and 29 April in the previous season, so do not carry a year forward) |
| Validated by | Pending -- requires sign-off by a Finnish KHT/HT auditor or tax adviser |
| Validation date | Pending |
| Skill version | 1.2 |

### Earned Income -- State Tax Brackets (2025)

**Earned Income -- State Tax Brackets (2025)**

| Taxable Earned Income (EUR) | Tax at Lower Limit | Rate on Excess |
| --- | --- | --- |
| 0 -- 21,200 | €0 | 12.64% |
| 21,200 -- 31,500 | €2,679.68 | 19.00% |
| 31,500 -- 52,100 | €4,636.68 | 30.25% |
| 52,100 -- 88,200 | €10,868.18 | 34.00% |
| 88,200 -- 150,000 | €23,142.18 | 41.75% |
| 150,000+ | €48,943.68 | 44.25% |

- **Solidarity tax top bracket** — The top bracket (44.25%) includes a 2 percentage point "solidarity tax" (solidaarisuusvero) on income above €150,000.

### Municipal Tax (kunnallisvero)

- **Municipal tax rate range** — 4.73% -- 10.86% percent (Flat rate set by each municipality, mainland Finland 2025. Average approximately 7.5%. Applied to taxable earned income after municipal deductions (which differ from state deductions).)

### Church Tax (kirkollisvero)

- **Church tax rate range** — 1.0% -- 2.2% (Applicable only to members of the Evangelical Lutheran Church or Orthodox Church, depending on parish)

Establish the church, parish and legally effective membership at the end of
the preceding year before selecting a parish rate. [Act 1013/2012, section 1](https://www.finlex.fi/sv/lagstiftning/2012/1013)
provides the Lutheran membership test and municipal taxable-income base;
[Vero's general church-tax guidance](https://www.vero.fi/sv/skatteforvaltningen/nyhetsrummet/presentations_och_undervisningsmateria/kyrkoskat/)
uses the preceding-year-end test for Lutheran and Orthodox members. Special
parishes, foreign membership, estates and disputed effective dates need their
own checks. An unknown membership status does not establish zero church tax.
The 2025 parish-rate range above was not reverified in this correction.

### Capital Income Tax (pääomatulovero)

**Capital Income Tax (pääomatulovero)**

| Capital Income (EUR) | Rate |
| --- | --- |
| 0 -- 30,000 | 30% |
| 30,000+ | 34% |

### Health Insurance Contributions (2025)

**Health Insurance Contributions (2025)**

| Component | Rate | Applies To |
| --- | --- | --- |
| Medical care contribution | 0.51% | All earned income |
| Daily allowance contribution (employee) | 0.88% | Earned income ≥€17,255/year |
| Daily allowance contribution (self-employed) | 1.11% | Earned income ≥€17,255/year |
| Daily allowance (self-employed, low income) | 0.23% | Earned income <€17,255/year |

### Self-Employed Business Income Split

- **Self-Employed Business Income Split** — For self-employed (sole traders / toiminimiyrittäjä), business income is split between earned income and capital income: Capital income portion: 20% of the net assets of the business at the end of the prior year (default). The taxpayer may elect 10% or 0% instead. Earned income portion: The remainder is taxed as earned income at progressive rates plus municipal tax.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown municipality | STOP -- municipal tax rate required |
| Unknown church membership | Needs Input; hold church tax and any dependent credit allocation or total until membership, parish and effective dates are established |
| Unknown capital income split election | 20% of net assets (statutory default) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration | Assume not VAT-registered |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, municipality of residence, and confirmation of whether self-employed (elinkeinonharjoittaja) or freelancer (ammatinharjoittaja).

**Recommended** -- all sales invoices, purchase invoices/receipts, YEL pension insurance payment confirmations, prior year OmaVero tax decision, asset register for business.

**Ideal** -- complete bookkeeping (single-entry or double-entry), balance sheet if double-entry, prepayment tax (ennakkovero) payment confirmations, travel expense records.

For church tax, obtain the applicable church/parish, effective membership dates
and the relevant prefilled or authority record. Resolve conflicting information
before choosing a zero charge or parish rate.

### Refusal Catalogue

- **R-FI-1 -- Municipality unknown** — "Municipal tax rate varies from 4.73% to 10.86%. Cannot compute total tax without knowing the client's municipality. Please confirm."
- **R-FI-2 -- Company or partnership** — "This skill covers sole traders (toiminimi) and freelancers (ammatinharjoittaja) only. Oy (osakeyhtiö), Ky (kommandiittiyhtiö), and Ay (avoin yhtiö) have different rules. Escalate to a Finnish tax adviser."
- **R-FI-3 -- Non-resident taxation** — "Non-resident and dual-resident taxation has separate rules (e.g., flat 35% withholding on employment income). Out of scope."
- **R-FI-4 -- International income / tax treaty** — "Cross-border income subject to Finland's extensive double tax treaty network requires specialist analysis. Escalate."
- **R-FI-CHURCH -- Membership or parish unresolved**: "I need the applicable church, parish and effective membership status at the end of the preceding year. Church tax and dependent credit allocations or totals remain held until these are established."

## Section 3 -- Deductions

### 3.1 Earned Income Deductions (from State Tax)

**3.1 Earned Income Deductions (from State Tax)**

| Deduction | Detail |
| --- | --- |
| Työtulovähennys (earned income deduction) | Granted automatically on wages/business earned income; max ~€2,140 (2025); phases out at higher income |
| Perusvähennys (basic deduction) | Granted on municipal tax; max ~€3,870 (2025); phases out as income rises |
| YEL pension insurance | Fully deductible from personal taxation |

### 3.2 Business Deductions (Self-Employed)

**3.2 Business Deductions (Self-Employed)**

| Category | Treatment |
| --- | --- |
| Office rent (dedicated business premises) | Fully deductible |
| Home office (työhuonevähennys) | Fixed deduction: €940/year if primary workplace; €470/year if secondary; or actual costs pro-rated by area |
| Professional literature, tools | Fully deductible |
| Travel expenses (business trips) | Actual costs or per diem (päiväraha): full day (>10h) €51, partial (>6h) €24 (2025 domestic rates) |
| Kilometre allowance | €0.30/km for own car on business trips (2025) |
| Training and CPD | Deductible if related to current profession |
| Telephone / internet (business portion) | Deductible for documented business use portion |
| Professional memberships | Fully deductible |
| Accounting and legal fees | Fully deductible |
| Marketing, advertising | Fully deductible |
| Bank charges (business account) | Fully deductible |
| Bad debts | Deductible if previously declared as income and irrecoverable |
| Representation / entertainment | 50% deductible (food and beverages for client entertainment) |
| Depreciation | Machinery/equipment: max 25% declining balance; IT equipment: max 25%; Furniture: max 25%; Buildings: 4-7% straight-line |

### 3.3 Non-Deductible Expenses

**3.3 Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Personal living costs | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Commuting (home to permanent workplace) | Personal; separate commuting deduction exists for employees |
| Clothing (unless protective/uniform) | Personal |
| Donations (except to approved universities/research) | Not deductible for self-employed |

## Section 4 -- Worked Examples

### Example 1 -- Freelance Developer, Single, Helsinki

**Input:** Gross business revenue €65,000, allowable expenses €12,000, net business income €53,000. No significant business assets. Municipality: Helsinki (municipal tax 8.50% for 2025). Church member (Evangelical Lutheran, church tax ~1.0%).

**Capital income split:** Net business assets ~€5,000. Capital income = 20% × €5,000 = €1,000 at 30% = €300. Earned income = €53,000 - €1,000 = €52,000.

**State tax on €52,000 earned income:**
Tax at €31,500 limit = €4,636.68
Excess: (€52,000 - €31,500) × 30.25% = €6,201.25
State tax = €10,837.93

**Municipal tax on €52,000:** €52,000 × 8.50% = €4,420 (before municipal deductions; actual will be lower after perusvähennys and other deductions).

**Health insurance:** ~€52,000 × (0.51% + 1.11%) = ~€842.

**Capital income tax:** €1,000 × 30% = €300.

**Approximate total tax:** ~€15,000--€16,000 (effective rate ~28-30%).

### Example 2 -- Capital Income Only

**Input:** Investment income €45,000 (dividends, rental, interest).

**Tax:** First €30,000 at 30% = €9,000. Remaining €15,000 at 34% = €5,100. Total = €14,100.

## Section 5 -- Filing and Payment

### 5.1 Filing

**5.1 Filing**

| Item | Detail |
| --- | --- |
| Self-employed filing deadline | 1 April of the following year (from 2025 onwards) |
| Employee filing deadline | An April date assigned per taxpayer, printed on the return and in MyTax. **1, 14, 21 or 28 April 2026** for tax year 2025 |
| Portal | OmaVero (omavero.fi) |
| Pre-populated return | Verohallinto pre-fills income from employers, banks, pension companies |
| Self-employed attachment | Income statement (tuloslaskelma) and balance sheet (tase) if double-entry bookkeeping |
| Record retention | 6 years |

### 5.2 Prepayment Tax (Ennakkovero)

Self-employed persons must pay prepayment tax during the tax year. See the **fi-prepayments** skill for full details.

- Based on estimated income or prior year assessment
- The ordinary schedule has 2, 3, 6 or 12 instalments according to the assessed advance; see the source-linked bands in **fi-prepayments**
- Adjustable during the year through OmaVero
- Residual tax (jäännösvero) due if prepayments insufficient

### 5.3 Penalties

[Assessment Procedure Act 1558/1995, sections 32–33](https://www.finlex.fi/sv/lagstiftning/1995/1558),
introduced by [15/2018](https://www.finlex.fi/sv/lagstiftning/forfattningssamling/2018/15)
from tax year 2018, distinguishes a natural person's EUR 50 annual late-filing
fee from a tax increase. An individual sole trader uses this branch. A complete
required main return filed late before assessment ends comes within the fee
branch even after a request. A correction of an existing or deemed prefilled
return uses that substitution only on the taxpayer's own initiative before
completion. Separate errors can still attract an increase. The fee is once
per tax year, not EUR 50 plus a percentage of tax.

First establish the disclosure failure and any non-imposition ground. The
statute addresses minor failures, valid reasons and the applicable
unreasonableness test; the fee has additional outside-control and special-reason
grounds. A missing taxpayer-favourable item normally attracts neither charge,
subject to the repeated-failure/clear-indifference exception. That does not
excuse an entirely late required return or an unfounded deduction.

| Qualifying increase branch | Percentage of added income | Percentage of increased tax where section 32b applies |
|---|---|---|
| Ordinary | 2% | 10% |
| Repeated failure or clear indifference | 3% to 10% | 15% to 50% |
| Estimated assessment | 5% | 25% |
| Statutory interpretive uncertainty or qualifying unreasonableness | 1% | 5% |
| Foreign income satisfying section 32a(5), excluding the aggravated branch | 1% | 5% |
| Own-initiative correction after completion with the explanation duty fulfilled | 0.5% | 2% |

Added income is the primary base, including a qualifying reduction of an
assessed loss. Increased tax is the alternative base when the income base
cannot be used or income was placed in the wrong category. The natural-person
minimum is EUR 75 when an increase is imposed, after non-imposition grounds
have been considered. Do not apply an income percentage to additional tax or
classify a failure from an informal label such as 'negligent' alone.

[Vero's guidance dated 20 May 2026](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/anvisningar/66816/pofoljdsavgifter-for-inkomstbeskattningen/)
contains apparent wording conflicts in sections 3.2.5 and 3.2.12: the former
uses added-income wording for the 15% to 50% increased-tax branch; the latter
states a EUR 150 minimum without qualifying the taxpayer category. Sections
32a–32b and the guidance's section 3.2.9 support the natural-person base and
EUR 75 minimum above. The 2026 guidance is interpretive material, not a change
of this guide's 2025 tax year. Disputed facts, special formal failures, foreign
credits, criminal-process safeguards and remedies need their complete rules.

Payment interest is separate. Use **fi-prepayments** for reduced settlement
interest and interest starting the day after an overdue amount's due date;
an honest shortfall in advances alone does not establish a disclosure penalty.

## Section 6 -- Interaction with Other Finnish Taxes

**Section 6 -- Interaction with Other Finnish Taxes**

| Tax | Interaction |
| --- | --- |
| VAT (ALV) | Separate system; see Finland VAT skill if applicable. VAT collected is not income; input VAT recovered is not expense. |
| YEL pension insurance | Mandatory for self-employed; deductible from personal income. See **fi-yel-social** skill. |
| Prepayment tax (ennakkovero) | Not an expense; credit against final liability. See **fi-prepayments** skill. |

## Section 7 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Income tax rates | Income Tax Act (tuloverolaki) 1535/1992 |
| Business income | Business Income Tax Act (EVL) 360/1968 |
| Capital income split | Income Tax Act §38 |
| Deductions | Income Tax Act §29-§31, §93-§95; EVL §7-§18 |
| Prepayments | Prepayment Act (ennakkoperintälaki) 1118/1996 |
| Filing deadlines | Verohallinto annual announcement |

### Key Verohallinto Resources

**Key Verohallinto Resources**

| Resource | URL |
| --- | --- |
| OmaVero portal | https://www.vero.fi/omavero |
| Self-employed guide | https://www.vero.fi/en/businesses-and-corporations/about-corporate-taxes/sole-traders/ |
| Tax rates on pay | https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/income/earned-income/tax-rates-on-pay-pensions-and-benefits/ |
| Per diem rates | https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/income/earned-income/work-related-travel/ |

## Prohibitions

- NEVER compute total tax without knowing the client's municipality of residence
- NEVER ignore the earned income / capital income split for self-employed
- NEVER apply employee-specific deductions (e.g., commuting deduction) to self-employed income
- NEVER treat YEL insurance as a business expense -- it is a personal tax deduction
- NEVER treat prepayment tax (ennakkovero) as an expense -- it is a credit against final tax
- NEVER present calculations as definitive -- always label as estimated
- NEVER advise on non-resident, dual-resident, or cross-border tax situations

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
