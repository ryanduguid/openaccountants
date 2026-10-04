---
name: turkey-pit
description: Use this skill whenever asked to prepare, review, or classify transactions for Turkey Personal Income Tax (Gelir Vergisi), annual tax return (Yıllık Gelir Vergisi Beyannamesi / 0001 kodu), or advise on Turkish PIT deductions and filing. Trigger on phrases like "gelir vergisi", "Turkish income tax", "yıllık beyanname", "GİB", "vergi dairesi", or any Turkey personal income tax request. ALWAYS read this skill before touching any Turkey PIT work.
version: 1.1
jurisdiction: TR
tax_year: 2026
last_updated: 2026-10-04
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Turkey Pit

## Turkey Personal Income Tax (Gelir Vergisi) Skill v1.1

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Türkiye (Republic of Türkiye) |
| Tax | Gelir Vergisi (Personal Income Tax) |
| Currency | TRY (Turkish Lira / ₺) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Current tax year | 2026 |
| Tax authority | Gelir İdaresi Başkanlığı (GİB — Revenue Administration) |
| Return code | 0001 — Yıllık Gelir Vergisi Beyannamesi |
| Filing portal | https://ivd.gib.gov.tr (İnteraktif Vergi Dairesi) |
| Filing deadline | 1–25 March of following year |
| Payment | 2 equal instalments: March and July |
| Source credit | `ozgurg/vergihesaplayici.com` (AGPL-3.0) + `berkaygure/gelir-vergisi-kesintisi-hesaplama` |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Turkish SMMM or YMM |
| Skill version | 1.1 |

## Section 2 — Progressive tax brackets (Vergi dilimleri) — 2026 and 2025

**Annual income tax brackets for yıllık gelir vergisi — 2026 income other than wages**  _(Income Tax Law No. 193 (Gelir Vergisi Kanunu, consolidated text with the 2026 amounts, mevzuat.gov.tr), art. 103 — https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf ; Income Tax General Communiqué Seri No. 332, Resmî Gazete 31 December 2025, No. 33124 (5th repeated edition), art. 3(3) — https://www.resmigazete.gov.tr/eskiler/2025/12/20251231M5-30.pdf)_

| Taxable Income (TRY) | Rate | Max tax in bracket |
| --- | --- | --- |
| 0 – 190,000 | 15% | 28,500 |
| 190,001 – 400,000 | 20% | 42,000 |
| 400,001 – 1,000,000 | 27% | 162,000 |
| 1,000,001 – 5,300,000 | 35% | 1,505,000 |
| 5,300,001 + | 40% | — |

**Wage income (ücret) brackets — 2026; employers apply this table to cumulative wages for the year**  _(Income Tax Law No. 193 (Gelir Vergisi Kanunu, consolidated text with the 2026 amounts, mevzuat.gov.tr), arts. 103 and 104 — https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf ; Income Tax General Communiqué Seri No. 332, Resmî Gazete 31 December 2025, No. 33124 (5th repeated edition), art. 3(3) — https://www.resmigazete.gov.tr/eskiler/2025/12/20251231M5-30.pdf)_

| Taxable wages (TRY) | Rate | Max tax in bracket |
| --- | --- | --- |
| 0 – 190,000 | 15% | 28,500 |
| 190,001 – 400,000 | 20% | 42,000 |
| 400,001 – 1,500,000 | 27% | 297,000 |
| 1,500,001 – 5,300,000 | 35% | 1,330,000 |
| 5,300,001 + | 40% | — |

**2025 income other than wages (returns filed 1 to 25 March 2026)**  _(Income Tax General Communiqué Seri No. 329, Resmî Gazete 30 December 2024 (2nd repeated edition), art. 3 — https://www.resmigazete.gov.tr/eskiler/2024/12/20241230M2-12.htm)_

| Taxable Income (TRY) | Rate | Max tax in bracket |
| --- | --- | --- |
| 0 – 158,000 | 15% | 23,700 |
| 158,001 – 330,000 | 20% | 34,400 |
| 330,001 – 800,000 | 27% | 126,900 |
| 800,001 – 4,300,000 | 35% | 1,225,000 |
| 4,300,001 + | 40% | — |

For 2025 wages the 27% band runs to 1,200,000 TRY and the 35% band from there to 4,300,000 TRY. Until October 2026 this guide applied the wage ceiling of 1,200,000 TRY to all 2025 income and showed a separate "cumulative withholding" table whose thresholds (24,000 to 650,000 TRY) are not in the law; art. 104 computes the monthly wage tax from the annual tariff.

## Section 3 — Income categories (Gelir türleri)

**7 income categories per GVK**  _(Gelir Vergisi Kanunu (GVK))_

| # | Turkish | English | GVK Section |
| --- | --- | --- | --- |
| 1 | Ticarî kazançlar | Business income | §37–51 |
| 2 | Ziraî kazançlar | Agricultural income | §52–59 |
| 3 | Ücretler | Employment income (wages) | §61–64 |
| 4 | Serbest meslek kazançları | Self-employment / professional income | §65–68 |
| 5 | Gayrimenkul sermaye iratları (GMSİ) | Rental income | §70–74 |
| 6 | Menkul sermaye iratları | Investment income (interest, dividends) | §75–80 |
| 7 | Diğer kazanç ve iratlar | Other income (capital gains etc.) | §80–82 |

## Section 4 — Key exemptions and deductions (İstisnalar ve indirimler)

### Exemptions (2026)

**Exemptions (2026, with 2025 in brackets)**  _(Income Tax Law No. 193 (Gelir Vergisi Kanunu, consolidated text with the 2026 amounts, mevzuat.gov.tr), arts. 21 and mükerrer 20 — https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf ; Income Tax General Communiqué Seri No. 332, Resmî Gazete 31 December 2025, No. 33124 (5th repeated edition), art. 3(2)(b) and the art. 103 tariff — https://www.resmigazete.gov.tr/eskiler/2025/12/20251231M5-30.pdf ; Income Tax General Communiqué Seri No. 329, Resmî Gazete 30 December 2024 (2nd repeated edition), art. 3 — https://www.resmigazete.gov.tr/eskiler/2024/12/20241230M2-12.htm)_

| Item | Amount (TRY) | Notes |
| --- | --- | --- |
| Residential rental income exemption (mesken kira geliri istisnası, art. 21) | 58,000 (2025: 47,000) | Annual; lost if the income is not declared or is under-declared; not available when gross wages, investment income, rental income and other gains together exceed the wage ceiling of the third tariff bracket |
| Young entrepreneur exemption (genç girişimci kazanç istisnası, mükerrer art. 20) | 400,000 (2025: 330,000) | Equal to the second bracket of the art. 103 tariff; first registration before age 29; first three tax periods |
| Severance pay (kıdem tazminatı) | Exempt | Within legal limits |

Until October 2026 this guide showed the 2024 amounts (33,000 and 230,000 TRY) as the 2025 exemptions.

### Deductions from income

**Deductions from income**  _(Income Tax Law No. 193 (Gelir Vergisi Kanunu, consolidated text with the 2026 amounts, mevzuat.gov.tr), art. 89 — https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf)_

| Deduction | Limit |
| --- | --- |
| Education and health expenses (art. 89(2)) | 10% of declared income; spent in Türkiye and documented by invoices from Turkish taxpayers |
| Personal insurance premiums (art. 89(1)) | 50% of life insurance premiums plus other personal insurance premiums (death, accident, health, disability, maternity, birth, education), together within 15% of declared income and the annual gross minimum wage |
| Private pension (BES) contributions | State matches 30%, employer deductible |
| Donations to public bodies, public-benefit associations and tax-exempt foundations (art. 89(4)) | Up to 5% of declared income (10% in priority development regions), against a receipt |
| Sponsorship expenses | Per related legislation |
| Social security premiums (SGK) | Actual amount paid |

## Section 5 — Filing rules

### Who must file annually?

- **Who must file annually** — Self-employed (serbest meslek erbabı); Business owners (ticari kazanç); Residential rental income above the art. 21 exemption (58,000 TRY for 2026; 47,000 TRY for 2025); Investment income above thresholds; Capital gains (değer artışı kazancı); Wages from more than one employer where the wages after the first employer exceed the second tariff bracket (400,000 TRY for 2026) or total wages exceed the fourth bracket (5,300,000 TRY for 2026) (art. 86(1)(b))  _(Income Tax Law No. 193 (Gelir Vergisi Kanunu, consolidated text with the 2026 amounts, mevzuat.gov.tr), arts. 85, 86 and 21 — https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf ; Income Tax General Communiqué Seri No. 332, Resmî Gazete 31 December 2025, No. 33124 (5th repeated edition), art. 3 — https://www.resmigazete.gov.tr/eskiler/2025/12/20251231M5-30.pdf)_

### Who does NOT file?

- **Who does not file** — Wage earners with a single employer whose wages were taxed by withholding and do not exceed the fourth tariff bracket (5,300,000 TRY for 2026); income that stays within exemption limits or the art. 86 declaration thresholds  _(Income Tax Law No. 193 (Gelir Vergisi Kanunu, consolidated text with the 2026 amounts, mevzuat.gov.tr), art. 86(1)(a) and (b) — https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf)_

### Provisional tax (Geçici vergi)

**Provisional tax quarterly due dates (payment; the statutory filing day is the 14th of the same month)**  _(Income Tax Law No. 193 (Gelir Vergisi Kanunu, consolidated text with the 2026 amounts, mevzuat.gov.tr), mükerrer art. 120 — https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf)_

| Quarter | Period | Due date |
| --- | --- | --- |
| Q1 | Jan–Mar | 17 May |
| Q2 | Apr–Jun | 17 August |
| Q3 | Jul–Sep | 17 November |
| Q4 | Oct–Dec | 17 February |

- **Provisional tax rate and offset** — Business and professional income earners pay provisional tax on each quarter's profit at the rate of the first tariff bracket (15%), declared by the 14th and paid by the 17th of the second month after the quarter; income tax withheld in the period is credited against it, and the provisional tax is credited against the annual liability. Law 7566 (Resmî Gazete 19 December 2025) removed the nine-month limit that Law 7338 had applied from 2022, so the fourth-quarter return applies again from the 2025 period. This guide said 'same brackets as annual' until October 2026  _(Income Tax Law No. 193 (Gelir Vergisi Kanunu, consolidated text with the 2026 amounts, mevzuat.gov.tr), mükerrer art. 120 and the Law 7566 application table — https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf)_

## Section 6 — Computation method

Step 1: Total assessable income (all 7 categories)
Step 2: − Exempt income (kira istisnası, genç girişimci, etc.)
Step 3: − Allowable expenses per category
Step 4: = Net taxable income (safi gelir)
Step 5: − Deductions (insurance, donations, BES)
Step 6: = Taxable base (vergi matrahı)
Step 7: Apply progressive brackets (Section 2)
Step 8: = Gross tax
Step 9: − Provisional tax paid (geçici vergi)
Step 10: − Withholding tax (stopaj / tevkifat)
Step 11: = Net tax payable or refund

## Section 7 — Worked example

**Scenario (2025 tariff):** Freelance software developer, 2025 annual income 600,000 TRY, allowable expenses 30,000 TRY, no other deductions. No provisional tax paid.

**Taxable base computation**  _(§40(4))_

| Step | Description | Amount (TRY) |
| --- | --- | --- |
| Gross income | Professional income §40(4) | 600,000 |
| − Expenses | Documented business costs | (30,000) |
| **Taxable base** |  | **570,000** |

**Tax computation on 570,000 TRY**

| Bracket | Taxable in bracket | Rate | Tax |
| --- | --- | --- | --- |
| 0 – 158,000 | 158,000 | 15% | 23,700 |
| 158,001 – 330,000 | 172,000 | 20% | 34,400 |
| 330,001 – 570,000 | 240,000 | 27% | 64,800 |
| **Total tax** |  |  | **122,900 TRY** |

If 50,000 TRY provisional tax was paid during the year:
**122,900 − 50,000 = 72,900 TRY** payable at filing (2 instalments: 36,450 March + 36,450 July).

## Section 8 — Conservative defaults

**Conservative defaults table**

| Situation | Conservative position |
| --- | --- |
| Income category unclear | Classify as taxable; flag for reviewer |
| Expense documentation incomplete | Do NOT deduct; flag |
| Rental income — mixed use | Apply exemption only to clearly residential portion |
| Foreign income | Include if Turkish resident; flag treaty applicability |
| Crypto / digital asset gains | Classify as "diğer kazanç"; flag pending legislation |

## Section 9 — Classification rules for bank statements

**Classification rules for bank statements**

| Pattern / Keyword | Classification | Category |
| --- | --- | --- |
| Maaş / Ücret / Salary | Employment income | Ücret §61 |
| Kira / Rent | Rental income | GMSİ §70 |
| Faiz / Interest | Investment income | Menkul sermaye §75 |
| Temettü / Dividend | Investment income | Menkul sermaye §75 |
| Serbest meslek / Freelance | Professional income | Serbest meslek §65 |
| Satış / E-ticaret | Business income | Ticarî kazanç §37 |
| Komisyon / Commission | Professional income | §65 or §37 |
| SGK / Social security | Deductible expense | — |
| BES / Pension contribution | Deductible | — |

## Section 10 — Sources

**Sources table**

| Source | URL |
| --- | --- |
| GİB (Revenue Administration) | https://www.gib.gov.tr |
| İnteraktif Vergi Dairesi | https://ivd.gib.gov.tr |
| `ozgurg/vergihesaplayici.com` (AGPL-3.0) | https://github.com/ozgurg/vergihesaplayici.com |
| `berkaygure/gelir-vergisi-kesintisi-hesaplama` | https://github.com/berkaygure/gelir-vergisi-kesintisi-hesaplama |
| Gelir Vergisi Kanunu No. 193 (consolidated text, mevzuat.gov.tr) | https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf |
| Gelir Vergisi Genel Tebliği Seri No. 332 (2026 amounts and tariff) | https://www.resmigazete.gov.tr/eskiler/2025/12/20251231M5-30.pdf |
| Gelir Vergisi Genel Tebliği Seri No. 329 (2025 amounts and tariff) | https://www.resmigazete.gov.tr/eskiler/2024/12/20241230M2-12.htm |

## *OpenAccountants — open-source accounting skills for AI*

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
