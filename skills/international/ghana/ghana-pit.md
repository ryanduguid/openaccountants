---
name: ghana-pit
description: Use this skill whenever asked to prepare, review, or classify transactions for Ghana Personal Income Tax (PAYE), annual tax return, or advise on GRA income tax brackets and SSNIT contributions. Trigger on phrases like "Ghana income tax", "PAYE Ghana", "GRA", "SSNIT", "Ghana tax return", or any Ghana personal tax request. ALWAYS read this skill before touching any Ghana PIT work.
version: 1.1
jurisdiction: GH
tax_year: 2026
last_updated: 2026-10-06
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana Pit

## Section 1 — Quick reference

**Section 1 — Quick reference table**

| Field | Value |
| --- | --- |
| Country | Ghana (Republic of Ghana) |
| Tax | Personal Income Tax / PAYE (Pay As You Earn) |
| Currency | GHS (Ghana Cedi / ₵) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Current tax year | 2026 |
| Tax authority | Ghana Revenue Authority (GRA) |
| Return form | Self-Assessment Return |
| Filing portal | https://tpsweb.gra.gov.gh |
| Filing deadline | 30 April of following year |
| SSNIT rate (employee) | 5.5% of basic salary |
| SSNIT rate (employer) | 13% of basic salary |
| Source credit | `Kessir/taxcalculatorgh` (32 stars) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Ghanaian Chartered Accountant |
| Skill version | 1.1 |

## Section 2 — Monthly PAYE tax brackets (effective 1 Sep 2026)

The Income Tax (Amendment) Act, 2026 (Act 1178) replaced the resident individual bands from 1 September 2026. Source: GRA, Pay As You Earn (PAYE), https://gra.gov.gh/domestic-tax/tax-types/paye/ , and GRA notice "Amendments - Income Tax Act, 2026 (Act 1178)", https://gra.gov.gh/wp-content/uploads/2026/09/Amendments-To-The-Income-Tax-2015-Act-896_Updated-1.pdf (both read 6 October 2026).

**Monthly PAYE tax brackets**

| Monthly chargeable income (GHS) | Rate | Cumulative income | Cumulative tax |
| --- | --- | --- | --- |
| First 588 | 0% | 588 | 0 |
| Next 80 | 5% | 668 | 4.00 |
| Next 100 | 10% | 768 | 14.00 |
| Next 2,900 | 17.5% | 3,668 | 521.50 |
| Next 16,000 | 25% | 19,668 | 4,521.50 |
| Next 30,332 | 30% | 50,000 | 13,621.10 |
| Exceeding 50,000 | 35% | — | — |

### Annual equivalent

**Annual equivalent brackets**

| Annual chargeable income (GHS) | Rate |
| --- | --- |
| First 7,056 | 0% |
| Next 960 | 5% |
| Next 1,200 | 10% |
| Next 34,800 | 17.5% |
| Next 192,000 | 25% |
| Next 363,984 | 30% |
| Over 600,000 | 35% |

### Bands before 1 September 2026

PAYE for months up to August 2026 used the bands effective 1 January 2024, as previously recorded in this guide: first GHS 490 at 0%, next 110 at 5%, next 130 at 10%, next 3,166.67 at 17.5%, next 16,000 at 25%, next 30,520 at 30%, and 35% above that. GRA's PIT page still states the GHS 490 monthly tax-free amount (https://gra.gov.gh/domestic-tax/personal-income-tax/, read 6 October 2026). How the two scales combine in the annual assessment for the 2026 year of assessment is not stated on the GRA pages; flag 2026 annual returns for review.

Non-resident individuals: chargeable income is generally taxed at a flat 25% (GRA PAYE page).

## Section 3 — Social security (SSNIT / Tier 1 & 2)

**SSNIT contributions**

| Contribution | Rate | Base |
| --- | --- | --- |
| Employee contribution | 5.5% | Basic salary |
| Employer contribution | 13% | Basic salary |
| Remitted to SSNIT (Tier 1) | 13.5% of the 18.5% total | Basic salary |
| Remitted to the Tier 2 occupational scheme | 5% of the 18.5% total | Basic salary |
| Tier 3 (voluntary provident) | Variable; deductible up to 16.5% of basic salary | Basic salary |

- **SSNIT deduction timing** — Employee's 5.5% SSNIT is deducted before tax calculation (reduces chargeable income).  _(GRA, Pay As You Earn (PAYE) — https://gra.gov.gh/domestic-tax/tax-types/paye/)_
- **Insurable earnings for 2026** — From 1 January 2026 the maximum insurable earnings are GHS 69,000 a month (up from GHS 61,000) and the minimum GHS 587.80, so the maximum and minimum monthly contributions payable to SSNIT are GHS 9,315.00 and GHS 79.40  _(SSNIT, Public Notice "Maximum and Minimum Insurable Earnings for 2026", under s 63(3) of the National Pensions Act, 2008 (Act 766) — https://www.ssnit.org.gh/wp-content/uploads/2026/01/Public-Notice-Min-Max-Insurable.pdf)_

## Section 4 — Chargeable income calculation

- **Chargeable income calculation steps** — Step 1: Gross monthly salary (basic + allowances) Step 2: − Exempt allowances (if applicable) Step 3: = Assessable income Step 4: − SSNIT employee contribution (5.5% of basic) Step 5: − Tier 3 voluntary contribution (if any) Step 6: − Other reliefs (see Section 5) Step 7: = Chargeable income Step 8: Apply PAYE brackets (Section 2) Step 9: = Monthly tax

## Section 5 — Reliefs and deductions

**Reliefs and deductions**

| Relief | Amount / Rule |
| --- | --- |
| Marriage/responsibility relief | GHS 1,200 a year, for a resident who maintains a spouse or at least two children |
| Child education relief | GHS 600 a year per child, up to three children at a recognised registered educational institution in Ghana; both parents cannot claim for the same child |
| Disability relief | 25% of the disabled person's income from business or employment |
| Old age relief (60 and over) | GHS 1,500 a year |
| Aged dependent relative relief | GHS 1,000 a year per relative aged 60 or over, up to two relatives (not a spouse or child) |
| Educational relief | GHS 2,000 a year for training to update professional, technical or vocational skills |
| Mortgage interest relief | Qualifying mortgage interest on one principal private residence |

Reliefs are granted on application to the Commissioner-General on the prescribed form. Source: GRA, Personal Tax Relief, https://gra.gov.gh/domestic-tax/personal-tax-relief/ (read 6 October 2026). The previous life insurance premium row is removed: the GRA page lists no such relief.

## Section 6 — Self-employed / Business income

Self-employed individuals pay tax on annual profits at the annual rates GRA publishes for the 2026 year of assessment (GRA PAYE page and Act 1178 notice above):

**Self-employed annual tax brackets**

| Annual chargeable income (GHS) | Rate |
| --- | --- |
| First 7,056 | 0% |
| 7,057 – 8,016 | 5% |
| 8,017 – 9,216 | 10% |
| 9,217 – 44,016 | 17.5% |
| 44,017 – 236,016 | 25% |
| 236,017 – 600,000 | 30% |
| Over 600,000 | 35% |

- **Modified Taxation Scheme** — From 1 September 2026, individuals whose annual business turnover is more than GHS 20,000 but not more than GHS 750,000 pay a presumptive tax of 3% of annual turnover under the Modified Taxation Scheme  _(GRA notice "Amendments - Income Tax Act, 2026 (Act 1178)" — https://gra.gov.gh/wp-content/uploads/2026/09/Amendments-To-The-Income-Tax-2015-Act-896_Updated-1.pdf)_

- **Quarterly instalments** — Quarterly instalment payments required (25% of estimated annual tax per quarter).

## Section 7 — Worked example

**Scenario:** Employed professional, monthly basic GHS 8,000, monthly allowances GHS 4,000. Total gross = GHS 12,000/month. No Tier 3.

**Chargeable income calculation table**

| Step | Description | Amount (GHS) |
| --- | --- | --- |
| Gross salary | Basic + allowances | 12,000 |
| − SSNIT (5.5% of basic) | 5.5% × 8,000 | (440) |
| **Chargeable income** |  | **11,560** |

Monthly PAYE on GHS 11,560 for a month from September 2026:

**Monthly PAYE bracket breakdown**

| Bracket | Income in bracket | Rate | Tax |
| --- | --- | --- | --- |
| First 588 | 588 | 0% | 0 |
| Next 80 | 80 | 5% | 4.00 |
| Next 100 | 100 | 10% | 10.00 |
| Next 2,900 | 2,900 | 17.5% | 507.50 |
| Remaining 7,892 | 7,892 | 25% | 1,973.00 |
| **Monthly tax** |  |  | **2,494.50** |

Annualised at the September 2026 bands: GHS 2,494.50 × 12 = **GHS 29,934**. For the 2026 calendar year the months from January to August were taxed at the earlier bands (GHS 2,488.50 a month on the same pay), so the actual 2026 total differs.

### Who must file?

- All employees (employer withholds PAYE monthly)
- Self-employed persons
- Persons with income from multiple sources
- Rental income recipients

### Key dates

**Key dates table**

| Event | Deadline |
| --- | --- |
| Tax year end | 31 December |
| PAYE monthly remittance | 15th of following month |
| Annual return (employees) | 30 April |
| Self-employed quarterly payments | End of each quarter |
| Annual return (self-employed) | 30 April |

## Section 9 — Conservative defaults

**Conservative defaults table**

| Situation | Conservative position |
| --- | --- |
| Allowance taxability unclear | Include as chargeable; flag for reviewer |
| SSNIT contribution not documented | Use 5.5% of stated basic; flag |
| Business expense documentation weak | Do not deduct; flag |
| Foreign income | Include if Ghana resident; flag treaty applicability |
| Rental income (undeclared) | Classify as chargeable; flag |

## Section 10 — Sources

**Sources table**

| Source | URL |
| --- | --- |
| Ghana Revenue Authority (GRA) | https://gra.gov.gh |
| GRA, Pay As You Earn (PAYE) | https://gra.gov.gh/domestic-tax/tax-types/paye/ |
| GRA notice, Income Tax (Amendment) Act, 2026 (Act 1178) | https://gra.gov.gh/wp-content/uploads/2026/09/Amendments-To-The-Income-Tax-2015-Act-896_Updated-1.pdf |
| GRA, Personal Tax Relief | https://gra.gov.gh/domestic-tax/personal-tax-relief/ |
| SSNIT, Maximum and Minimum Insurable Earnings for 2026 | https://www.ssnit.org.gh/wp-content/uploads/2026/01/Public-Notice-Min-Max-Insurable.pdf |
| Income Tax Act, 2015 (Act 896) | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf |
| Revenue Administration Act, 2016 (Act 915) | — |
| `Kessir/taxcalculatorgh` | https://github.com/Kessir/taxcalculatorgh |

## Footer disclaimer

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed by a qualified professional before filing.*

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
