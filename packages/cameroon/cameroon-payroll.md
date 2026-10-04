---
name: cameroon-payroll
description: Use this skill whenever asked about Cameroon payroll processing for employed persons. Trigger on phrases like "Cameroon payroll", "IRPP withholding", "PAYE Cameroon", "CNPS contribution", "CFC housing fund", "FNE employment fund", "CAC surcharge", "centimes additionnels", "DIPE", "payslip Cameroon", "bulletin de paie", "net salary Cameroon", "salaire net", "tax withholding Cameroon", "employer social security Cameroon", "SMIG Cameroon", "minimum wage Cameroon", "gross to net Cameroon", "XAF salary calculation", or any question about computing employee pay, withholding tax (IRPP/PAYE), or social security (CNPS) for Cameroon-based employees. This skill covers IRPP progressive withholding with the 10% Additional Council Tax (CAC), CNPS pension/family-allowance/accident contributions, the CFC housing fund and FNE employment fund payroll levies, council tax and audiovisual royalty, minimum wage (SMIG), monthly DIPE filing, and remittance deadlines. ALWAYS read this skill before processing any Cameroon payroll.
version: 0.3
jurisdiction: CM
tax_year: 2025
last_updated: 2026-10-04
reviewed_by: Nkinyam Courage Ndasi
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cameroon Payroll

## Cameroon Payroll Skill v0.3

**Tier 2 — Research-verified.** Figures are sourced from PwC Worldwide Tax Summaries (Cameroon) and the CNPS official site, corroborated by Employer-of-Record guides. This skill has **not** yet been section-by-section verified by a licensed Cameroon accountant (`verified_by: pending`). Treat all outputs as estimates pending professional sign-off. Where a figure could not be sourced to a primary authority it is flagged **[RESEARCH GAP — reviewer to confirm]**.

> **Source-cited draft (tier 2), not accountant-reviewed.** On 2026-06-21 Nkinyam Courage Ndasi checked the rates, thresholds and deadlines listed for this guide against the cited authorities; the corrections of that fact check are in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). It was a check of listed facts, not a sign-off on the guide: no reviewer sign-off is recorded in the frontmatter, the guide is not on the roster in `PARTNERS.md`, and `review_status` is `pending_review`. Items the check flagged for clarification remain marked in the text.

## Section 1 — Quick Reference

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Republic of Cameroon |
| Currency | Central African CFA franc (XAF) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January – 31 December) |
| Tax withholding system | Monthly PAYE — Impôt sur le Revenu des Personnes Physiques (IRPP), withheld via the DIPE declaration |
| Tax authority | Direction Générale des Impôts (DGI), Ministry of Finance |
| Social security authority | Caisse Nationale de Prévoyance Sociale (CNPS) |
| Key legislation | Code Général des Impôts (CGI); Code du Travail; CNPS social security regulations; annual Finance Law |
| Monthly employer return | DIPE — Déclaration des Impôts et des Prélèvements sur les Salaires (PAYE + salary levies), due 15th of following month [PwC, Tax administration] |
| CNPS contribution ceiling | XAF 750,000/month (XAF 9,000,000/year) [PwC, Other taxes; CNPS] |
| Personal income tax | **Yes** — Cameroon levies IRPP (progressive 11%–38.5% incl. CAC) |
| Validated by | Verified by Nkinyam Courage Ndasi (3472800) on 2026-06-21 |
| Skill version | 0.3 |

**No-PIT note:** This is **not** a no-PIT jurisdiction. Cameroon levies a progressive personal income tax (IRPP) on employment income, withheld monthly. Treat IRPP as a core employer withholding obligation.

## Section 2 — Income Tax Withholding (IRPP / PAYE)

- **IRPP withholding basis** — The employer withholds IRPP monthly under the PAYE system. IRPP is progressive and applied to annual net taxable salary (the brackets below are annual; the monthly withholding is the annual liability divided by 12 for a stable salary).  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income)_

### 2.1 IRPP Brackets (FY2025 — effective rates incl. 10% CAC)

- **CAC surcharge incorporation** — The published bracket rates already incorporate the Additional Council Tax (Centimes Additionnels Communaux, CAC) surcharge of 10% added to base IRPP. Base IRPP rates are 10% / 15% / 25% / 35%; × 1.10 CAC gives the effective rates below.

**IRPP Brackets**  _(Source (brackets): https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income ; Source (10% CAC): https://rivermate.com/guides/cameroon/taxes ; https://remotepeople.com/countries/cameroon/hire-employees/payroll-tax/)_

| Annual net taxable income (XAF) | Base rate | Effective rate (incl. 10% CAC) |
| --- | --- | --- |
| 0 – 2,000,000 | 10% | **11%** |
| 2,000,001 – 3,000,000 | 15% | **16.5%** |
| 3,000,001 – 5,000,000 | 25% | **27.5%** |
| Over 5,000,000 | 35% | **38.5%** |

**Cumulative tax at each bracket ceiling (effective, incl. CAC)**

| At annual net income (XAF) | Cumulative IRPP (XAF) |
| --- | --- |
| 2,000,000 | 220,000 |
| 3,000,000 | 385,000 |
| 5,000,000 | 935,000 |

*Check:* 2,000,000 × 11% = 220,000; + 1,000,000 × 16.5% = 165,000 → 385,000; + 2,000,000 × 27.5% = 550,000 → 935,000. Above 5,000,000 add 38.5% of the excess.

### 2.2 Net Taxable Salary — Computation Order

- **Computation order intro** — Apply in this exact order:
- **Step 1 — Gross taxable salary** — All wages, salaries, cash and benefits in kind. Certain special-duty allowances and statutory family allowances are exempt.  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/income-determination)_
- **Step 2 — Less employee CNPS pension contribution** — The 4.2% pension contribution is a deductible charge.  _(https://remotepeople.com/countries/cameroon/hire-employees/payroll-tax/)_
- **Step 3 — Less 30% lump-sum professional/business expense allowance** — Computed on the post-CNPS taxable salary.  _(https://rivermate.com/guides/cameroon/taxes ; https://remotepeople.com/countries/cameroon/hire-employees/payroll-tax/)_
- **Step 4 — Less standard abatement of XAF 500,000** — Annual abatement on employment income.  _(https://remotepeople.com/countries/cameroon/hire-employees/payroll-tax/)_
- **Step 5 — Round down to nearest XAF 1,000** — Then apply the progressive scale (result already includes the 10% CAC).  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income)_

> **Benefit-in-kind valuation** (% of taxable income): housing 15%, electricity 4%, water 2%, per the income-determination rules. **[RESEARCH GAP — reviewer to confirm full BIK schedule and per-item caps from the CGI.]**
> Source: https://taxsummaries.pwc.com/republic-of-cameroon/individual/income-determination

- **Other income note (not employment PAYE)** — Net income from "other activities" is taxed at 33%; income from stocks/shares at 16.5% overall.  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income)_

## Section 3 — Salary-based Local Taxes (withheld with PAYE)

These flat local levies are withheld alongside IRPP on the DIPE declaration.

Each levy is a flat monthly amount read from a band table by monthly salary. The two tables below are those of the 2026-06-21 fact check (Nkinyam Courage Ndasi), which carried them without an article citation; PwC (Other taxes) confirms the top bands: the council tax above XAF 500,000 (PwC's rounded ~XAF 2,520, where the reviewed table says 2,500) and the CRTV royalty of XAF 13,000 above XAF 1,000,000. Until 2026-09-29 this guide stated only those top bands and treated every lower band as a research gap.

**Council tax (taxe de développement local, TDL, withheld on salaries) — monthly bands**

| Monthly salary (XAF) | Council tax (XAF/month) |
| --- | --- |
| Below 62,000 | 0 |
| 62,000 – 75,000 | 250 |
| 75,001 – 100,000 | 500 |
| 100,001 – 125,000 | 750 |
| 125,001 – 150,000 | 1,000 |
| 150,001 – 200,000 | 1,250 |
| 200,001 – 250,000 | 1,500 |
| 250,001 – 300,000 | 2,000 |
| 300,001 – 500,000 | 2,250 |
| Above 500,000 | 2,500 |

**Audiovisual royalty (CRTV, redevance audiovisuelle) — monthly bands**

| Monthly salary (XAF) | CRTV (XAF/month) |
| --- | --- |
| 0 – 50,000 | 0 |
| 50,001 – 100,000 | 750 |
| 100,001 – 200,000 | 1,950 |
| 200,001 – 300,000 | 3,250 |
| 300,001 – 400,000 | 4,550 |
| 400,001 – 500,000 | 5,850 |
| 500,001 – 600,000 | 7,150 |
| 600,001 – 700,000 | 8,450 |
| 700,001 – 800,000 | 9,750 |
| 800,001 – 900,000 | 11,050 |
| 900,001 – 1,000,000 | 12,350 |
| Above 1,000,000 | 13,000 |

> **Base and citation.** The reviewed tables are headed "monthly salary" (council tax) and "monthly taxable income" (CRTV); this guide, like PwC, bands both on the gross monthly salary, which overstates the CRTV by at most one band where exempt allowances are large. **[RESEARCH GAP — reviewer to confirm]** the Code Général des Impôts article of each scale (the taxe de développement local on salaried employees; the redevance audiovisuelle) and the exact base, before a band amount is relied on in a filing.

## Section 4 — Social Security (CNPS) — Contribution Rates

- **CNPS contribution ceiling rule** — All CNPS branches are capped at a monthly contribution ceiling of XAF 750,000 (XAF 9,000,000/year). Salary above the ceiling is not subject to CNPS.  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/other-taxes ; https://www.cnps.cm/en/assures/assure-e.html)_

**CNPS contribution rates**  _(Source (employer 11.2% + accident 1.75/2.5/5%, employee 4.2%): https://taxsummaries.pwc.com/republic-of-cameroon/corporate/other-taxes ; Source (family allowance 7% / pension 4.2% / accident bands): https://rivermate.com/guides/cameroon/taxes ; https://remotepeople.com/countries/cameroon/hire-employees/payroll-tax/ ; Source (CNPS authority): https://www.cnps.cm/en/assures/assure-e.html)_

| Branch | Employee | Employer | Base / ceiling |
| --- | --- | --- | --- |
| Old-age / disability / survivor **pension** | **4.2%** | **4.2%** | salary capped at XAF 750,000/mo |
| **Family allowances** (general private sector) | 0% | **7.0%** | capped at XAF 750,000/mo |
| **Occupational accident** insurance (by risk class) | 0% | **1.75% / 2.5% / 5%** | capped at XAF 750,000/mo |
| **Total CNPS (excl. accident)** | **4.2%** | **11.2%** |  |
| **Total CNPS (incl. accident)** | **4.2%** | **12.95% – 16.2%** | depends on risk class |

*Arithmetic check (employer, excl. accident):* 4.2% + 7.0% = **11.2%** ✓ (matches PwC's stated 11.2% employer figure).
*Incl. accident:* 11.2% + 1.75% = 12.95% (low risk); 11.2% + 5% = 16.2% (high risk). ✓

- **Maximum monthly CNPS contributions (at/above the XAF 750,000 ceiling)** — Employee pension: 4.2% × 750,000 = XAF 31,500/mo Employer pension: 4.2% × 750,000 = XAF 31,500/mo Employer family allowance: 7.0% × 750,000 = XAF 52,500/mo Employer accident (low/mid/high): 1.75% / 2.5% / 5% × 750,000 = XAF 13,125 / 18,750 / 37,500/mo

> **Reduced family-allowance rates:** 5.65% for workers in the agricultural and assimilated scheme and 3.70% for private education staff, against 7% in the general scheme, all on the XAF 750,000 monthly ceiling, per CLEISS's table of contributions at 1 January 2024 ([CLEISS, Les cotisations au Cameroun](https://www.cleiss.fr/docs/cotisations/cameroun.html)).
> Source (secondary): https://www.playroll.com/global-hiring-guides/cameroon

- **Voluntary / self-insured contribution** — 8.4% of declared income (pension branch only); declared income range XAF 36,270–750,000/month.  _(https://www.cnps.cm/en/assures/assure-e.html ; https://taxsummaries.pwc.com/republic-of-cameroon/individual/other-taxes)_

## Section 5 — Other Payroll Levies (CFC + FNE)

**CFC + FNE levies**  _(Source (CFC 1.5% employer / 1% employee, FNE 1% employer): https://taxsummaries.pwc.com/republic-of-cameroon/individual/other-taxes ; Source (combined 2.5% employer payroll tax): https://taxsummaries.pwc.com/republic-of-cameroon/corporate/other-taxes ; Source (CFC 1.5%/1% corroboration): https://remotepeople.com/countries/cameroon/employer-of-record/)_

| Levy | Employee | Employer | Base | Source |
| --- | --- | --- | --- | --- |
| **Housing Fund** — Crédit Foncier du Cameroun (CFC) | **1.0%** | **1.5%** | taxable salary | PwC, Other taxes |
| **National Employment Fund** (Fonds National de l'Emploi, FNE) | 0% | **1.0%** | taxable salary | PwC, Other taxes |
| **Total CFC + FNE** | **1.0%** | **2.5%** |  |  |

*Arithmetic check (employer):* 1.5% + 1.0% = **2.5%** ✓. PwC's corporate page describes the combined CFC + FNE as a **"payroll tax of 2.5% of total salaries and fringe benefits"** funding the Housing Loan and Employment Fund. The employee adds a separate 1.0% CFC.

> Unlike CNPS, the CFC and FNE are levied on **taxable salary** (no XAF 750,000 cap stated). **[RESEARCH GAP — reviewer to confirm]** whether any ceiling applies to CFC/FNE; PwC states no cap. The worked examples below assume CFC/FNE apply to the full taxable salary.

## Section 6 — Minimum Wage (SMIG) and Working Time

### 6.1 Minimum Wage (SMIG)

**SMIG rates**  _([CLEISS, Les cotisations au Cameroun](https://www.cleiss.fr/docs/cotisations/cameroun.html); EOR guides for cross-checks)_

| Category | Monthly SMIG | Source |
| --- | --- | --- |
| Private sector (non-agricultural) | XAF 60,000 from 21 March 2023 (40-hour week) | CLEISS |
| Private sector (agricultural and assimilated) | XAF 45,000 from 21 March 2023 | CLEISS |
| State employees under the Labour Code | XAF 43,969 from 23 February 2024 | CLEISS |

> **SMIG sources.** CLEISS states the SMIG for a 40-hour week at XAF 60,000 in the private sector and XAF 45,000 in the agricultural and assimilated sector from 21 March 2023, and XAF 43,969 for state employees under the Labour Code from 23 February 2024; the XAF 41,875 that some guides still quote was the earlier state-employee figure. Check the Ministry of Labour decree when a later revision is announced.

### 6.2 Working Time

> **[RESEARCH GAP — reviewer to confirm]** Standard hours (commonly cited 40 hours/week under the Code du Travail), overtime multipliers, and weekly rest were not sourced to a primary authority in this pass. Confirm against the Code du Travail before computing overtime.

## Section 7 — Conservative Defaults

When an input is missing or ambiguous, apply the **most conservative defensible assumption** and flag it for the reviewer. Never silently guess.

**Conservative defaults**

| Unknown / ambiguous input | Conservative default | Rationale |
| --- | --- | --- |
| CNPS occupational-accident risk class unknown | Use **2.5%** (mid band) and flag | Avoids understating employer cost; mid band is a defensible neutral |
| Family-allowance sector unclear | Use **7.0%** (general private sector) | Highest standard rate; reduced rates unconfirmed |
| Benefit-in-kind valuation uncertain | Include BIK at stated %s (housing 15%, electricity 4%, water 2%) and flag | Excluding BIK understates taxable salary |
| Council tax / CRTV base uncertain (allowances of unknown taxability) | Band on the **gross monthly salary** and flag | The §3 tables are read on the monthly salary; an overstated base overstates a levy by at most one band |
| Pay frequency unstated | Assume **monthly** | Standard Cameroon practice |
| Marital/dependant status (IRPP) | IRPP scale is **not** status-banded (single national scale) | Cameroon uses one progressive scale; no S/M codes |
| CFC/FNE ceiling uncertain | Apply to **full taxable salary** (no cap) | PwC states 2.5% on total salaries; no cap mentioned |
| SMIG value disputed | **Do not assume** — request confirmation | Sources disagree; flag as research gap |

Every default applied **must** be surfaced in the output as an explicit assumption line.

## Section 8 — Required Inputs and Refusal Catalogue

### 8.1 Required Inputs

- **Required inputs before computing Cameroon payroll** — Before computing Cameroon payroll, you MUST have: 1. Gross monthly salary in XAF (and frequency, if not monthly). 2. Components of pay — basic, allowances, cash/in-kind benefits (to determine taxable vs exempt). 3. CNPS occupational-accident risk class (low 1.75% / mid 2.5% / high 5%) — or accept the 2.5% default with a flag. 4. Whether any sector-specific reduced family-allowance rate applies (default 7%). 5. Whether the employer/employee are CNPS- and DGI-registered (NIU and CNPS employer number).

### 8.2 Refusal Catalogue — STOP and request input if:

**Refusal catalogue**

| Condition | Action |
| --- | --- |
| No gross salary figure provided | **Refuse** — cannot compute anything |
| Salary given in a currency other than XAF | **Refuse** — convert/confirm XAF first; never assume FX |
| Asked to compute SMIG-compliance as definitive | **Refuse to certify** — SMIG figure is a research gap; provide ranges only with disclaimer |
| Asked to file or sign a DIPE / tax return | **Refuse** — only a registered party / licensed professional may file |
| Asked to certify a council-tax / CRTV band amount for a filing | **Flag** — the §3 band tables are the reviewer's, not yet cited to a CGI article; compute, and label the amount as pending primary citation |
| Asked to treat output as professional advice | **Refuse** — outputs are estimates pending accountant sign-off |

## Section 9 — Transaction / Payment Pattern Library

Deterministic mapping of Cameroon bank-statement narratives (French/English) to payroll classifications. Match case-insensitively.

### 9.1 Salary Credits (employee side)

**Salary credit narrative patterns**

| Narrative pattern | Classification |
| --- | --- |
| `SALAIRE`, `PAIE`, `VIREMENT SALAIRE`, `NET A PAYER` | Net salary payment |
| `VIREMENT [employer]`, `REMUNERATION` | Net salary payment |
| `PRIME`, `BONUS`, `GRATIFICATION`, `13E MOIS` | Bonus / gratuity (taxable) |
| `INDEMNITE` | Allowance — check exempt vs taxable per CGI |
| `REMB CNPS`, `REMBOURSEMENT CNPS` | CNPS refund — not income |

### 9.2 Employer Debits (employer side)

**Employer debit narrative patterns**

| Narrative pattern | Classification |
| --- | --- |
| `DGI`, `IMPOT`, `IRPP`, `DIPE`, `PRECOMPTE` | IRPP + salary-levy remittance to DGI |
| `CAC`, `CENTIMES ADDITIONNELS` | Additional Council Tax (within IRPP block) |
| `CNPS`, `COTISATION CNPS`, `PREVOYANCE SOCIALE` | CNPS contribution remittance |
| `CFC`, `CREDIT FONCIER` | Housing Fund (Crédit Foncier) levy |
| `FNE`, `FONDS NATIONAL EMPLOI` | National Employment Fund levy |
| `CRTV`, `REDEVANCE AUDIOVISUELLE` | Audiovisual royalty |
| `TAXE COMMUNALE`, `TDL`, `TAXE DE DEVELOPPEMENT LOCAL` | Council tax (taxe de développement local) |
| `VIREMENT SALAIRES`, `PAIE DU MOIS`, `MASSE SALARIALE` | Net wages disbursement to employees |

## Section 10 — Worked Examples

All examples use **FY2025** rates. CNPS ceiling XAF 750,000/mo. IRPP computed on annual net taxable salary then ÷12. Accident class assumed **mid (2.5%)** unless stated. Figures recomputed end-to-end.

### Example A — Junior employee, gross XAF 250,000/month (annual 3,000,000)

**Example A calculation table**

| Step | Calc | XAF |
| --- | --- | --- |
| Gross taxable (annual) | 250,000 × 12 | 3,000,000 |
| Less CNPS pension EE (4.2%, ≤ ceiling) | 4.2% × 250,000 × 12 | (126,000) |
| Post-CNPS |  | 2,874,000 |
| Less 30% professional allowance | 30% × 2,874,000 | (862,200) |
| Less standard abatement |  | (500,000) |
| Net taxable (rounded down to 1,000) | 1,511,800 → | **1,511,000** |
| IRPP (within 0–2m band @ 11%) | 11% × 1,511,000 | **166,210/yr** |
| Monthly IRPP | ÷ 12 | **13,851/mo** |

Bank line: `VIREMENT SALAIRE — JEAN M. — XAF 2xx,xxx`

Monthly deductions (employee): CNPS pension 10,500 + CFC 1% (1% × 250,000 = 2,500) + IRPP 13,851 + council tax 1,500 (band 200,001 – 250,000) + CRTV 3,250 (band 200,001 – 300,000) = **31,601**.
Net pay ≈ 250,000 − 31,601 = **XAF 218,399/mo**.
*Council/CRTV check:* 250,000 falls in the 200,001 – 250,000 council-tax band → 1,500, and in the 200,001 – 300,000 CRTV band → 3,250 (§3 tables).

### Example B — Mid employee, gross XAF 800,000/month (annual 9,600,000)

**Example B calculation table**

| Step | Calc | XAF |
| --- | --- | --- |
| Gross taxable (annual) | 800,000 × 12 | 9,600,000 |
| Less CNPS pension EE (capped at ceiling) | 4.2% × 750,000 × 12 = 31,500 × 12 | (378,000) |
| Post-CNPS |  | 9,222,000 |
| Less 30% professional allowance | 30% × 9,222,000 | (2,766,600) |
| Less standard abatement |  | (500,000) |
| Net taxable (rounded to 1,000) | 5,955,400 → | **5,955,000** |
| IRPP — to 5,000,000 (cumulative) |  | 935,000 |
| IRPP — excess @ 38.5% | 38.5% × (5,955,000 − 5,000,000) = 38.5% × 955,000 | 367,675 |
| Total IRPP |  | **1,302,675/yr** |
| Monthly IRPP | ÷ 12 | **108,556/mo** |

Bank line: `PAIE DU MOIS — A. NGUEMA — VIREMENT`

Monthly employee deductions: CNPS pension **31,500** (capped) + CFC 1% (1% × 800,000 = 8,000) + IRPP 108,556 + council tax (above 500,000) **2,500** + CRTV (band 700,001 – 800,000) **9,750** = **160,306**.
*CRTV:* 800,000 is the top of the 700,001 – 800,000 band → 9,750 (§3 table).
Net pay ≈ 800,000 − 160,306 = **XAF 639,694/mo**.

### Example C — Employer monthly cost for Example B employee (gross 800,000)

**Example C employer cost table**

| Employer levy | Calc | XAF/mo |
| --- | --- | --- |
| CNPS pension (4.2%, capped) | 4.2% × 750,000 | 31,500 |
| CNPS family allowance (7%, capped) | 7% × 750,000 | 52,500 |
| CNPS accident (mid 2.5%, capped) | 2.5% × 750,000 | 18,750 |
| CFC employer (1.5% of taxable salary) | 1.5% × 800,000 | 12,000 |
| FNE employer (1.0% of taxable salary) | 1.0% × 800,000 | 8,000 |
| **Total employer on-costs** |  | **122,750** |

Fully-loaded employer cost = 800,000 + 122,750 = **XAF 922,750/mo**.
*Check:* CNPS subtotal 31,500 + 52,500 + 18,750 = 102,750; CFC+FNE 12,000 + 8,000 = 20,000; total 122,750 ✓.

### Example D — High earner, gross XAF 1,500,000/month (annual 18,000,000)

**Example D calculation table**

| Step | Calc | XAF |
| --- | --- | --- |
| Gross taxable (annual) | 1,500,000 × 12 | 18,000,000 |
| Less CNPS pension EE (capped) | 31,500 × 12 | (378,000) |
| Post-CNPS |  | 17,622,000 |
| Less 30% professional allowance | 30% × 17,622,000 | (5,286,600) |
| Less standard abatement |  | (500,000) |
| Net taxable (rounded to 1,000) | 11,835,400 → | **11,835,000** |
| IRPP — to 5,000,000 (cumulative) |  | 935,000 |
| IRPP — excess @ 38.5% | 38.5% × (11,835,000 − 5,000,000) = 38.5% × 6,835,000 | 2,631,475 |
| Total IRPP |  | **3,566,475/yr** |
| Monthly IRPP | ÷ 12 | **297,206/mo** |

Monthly employee deductions: CNPS pension 31,500 + CFC 1% (1% × 1,500,000 = 15,000) + IRPP 297,206 + council tax 2,500 (>500,000) + CRTV 13,000 (>1,000,000 → top band) = **359,206**.
Net pay ≈ 1,500,000 − 359,206 = **XAF 1,140,794/mo**.

### Example E — Worker at SMIG (illustrative only)

> SMIG is a **[RESEARCH GAP]**. Using the secondary figure XAF 60,000/month **for illustration only**: gross 60,000 is below the first council-tax band (62,000) → no council tax, and in the 50,001 – 100,000 CRTV band → 750; below the first IRPP band after deductions the net taxable is likely **nil** (post-CNPS 60,000 − 2,520 = 57,480; less 30% and the 500,000 abatement → negative → IRPP = 0). Employee still bears CNPS pension 4.2% × 60,000 = **2,520**, CFC 1% = **600** and CRTV **750**. **Do not certify SMIG compliance** until the official figure is confirmed.

## Section 11 — Tier 1 Rules (deterministic — always apply)

- **IRPP brackets basis** — IRPP brackets are annual net taxable income; the published 11%/16.5%/27.5%/38.5% rates already include the 10% CAC — never add CAC again.  _(Section 11 — Tier 1 Rules)_
- **CNPS contribution cap** — CNPS contributions are capped at XAF 750,000/month per branch; never apply CNPS to salary above the ceiling.  _(Section 11 — Tier 1 Rules)_
- **CNPS pension deductibility order** — The 4.2% employee CNPS pension is deductible before the 30% professional allowance and the 500,000 abatement.  _(Section 11 — Tier 1 Rules)_
- **Net-taxable computation order** — gross → less CNPS pension → less 30% → less 500,000 → round down to 1,000 → apply scale  _(Section 11 — Tier 1 Rules)_
- **CFC and FNE levy basis** — CFC (1.5% employer / 1% employee) and FNE (1% employer) are levied on taxable salary; PwC states no ceiling.  _(Section 11 — Tier 1 Rules)_
- **Council tax and CRTV bands** — Council tax is banded on the monthly salary from XAF 62,000 (250/month) to above 500,000 (2,500/month); CRTV from XAF 50,001 (750/month) to above 1,000,000 (13,000/month). Read the §3 tables; never apply a top-band amount to a salary in a lower band, and never a flat threshold.  _(Section 11 — Tier 1 Rules)_
- **CNPS total employer rate excluding occupational accident** — 11.2%  _(PwC Worldwide Tax Summaries — Cameroon, Corporate/Other taxes)_
- **DIPE deadline** — Monthly DIPE return + remittance is due by the 15th of the following month.  _(Section 11 — Tier 1 Rules)_
- **Currency assumption** — All amounts are XAF; never assume a different currency or apply FX without explicit input.  _(Section 11 — Tier 1 Rules)_

## Section 12 — Tier 2 Catalogue (reviewer judgement required)

**Tier 2 catalogue**

| Item | Why it needs judgement |
| --- | --- |
| Benefit-in-kind valuation and caps | Full CGI BIK schedule is a research gap; housing/electricity/water %s confirmed but caps unconfirmed |
| Exempt allowances (special-duty, statutory family) | Exemption scope is fact-specific per CGI |
| Council tax / CRTV band tables | Reviewer-supplied (2026-06-21) without a CGI article citation; PwC confirms the top bands only |
| Sector-reduced family-allowance rates (agriculture/teachers) | Secondary-sourced only |
| Operative SMIG | Sources disagree; needs the labour decree |
| Occupational-accident risk classification | Class assignment is employer/sector-specific |
| Working time / overtime multipliers | Not sourced to the Code du Travail this pass |
| Annual recapitulative tier (DIPE) by taxpayer office | Depends on DGE / CIME / CDI classification |
| Expatriate / non-resident treatment, tax treaties | Out of scope of this base skill |

## Section 13 — Excel Working Paper Template

**Excel working paper columns**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | NIU / CNPS no. | input |
| C | Gross monthly salary | input |
| D | Exempt allowances | input (per CGI) |
| E | Taxable monthly salary | =C−D |
| F | CNPS-able base (capped) | =MIN(E, 750000) |
| G | CNPS pension EE (4.2%) | =0.042*F |
| H | Annual taxable | =E*12 |
| I | Less CNPS pension EE (annual) | =G*12 |
| J | Less 30% professional | =0.30*(H−I) |
| K | Less abatement | =500000 |
| L | Net taxable (rounded) | =FLOOR(H−I−J−K, 1000) |
| M | Annual IRPP (incl. CAC) | progressive on L (see §2.1) |
| N | Monthly IRPP | =M/12 |
| O | CFC EE (1%) | =0.01*E |
| P | Council tax | =IF(C<62000, 0, LOOKUP(C, {62000;75001;100001;125001;150001;200001;250001;300001;500001}, {250;500;750;1000;1250;1500;2000;2250;2500}))  *(§3 band table)* |
| Q | CRTV royalty | =LOOKUP(C, {0;50001;100001;200001;300001;400001;500001;600001;700001;800001;900001;1000001}, {0;750;1950;3250;4550;5850;7150;8450;9750;11050;12350;13000})  *(§3 band table)* |
| R | Net pay | =C−G−N−O−P−Q |
| S | CNPS pension ER (4.2%) | =0.042*F |
| T | CNPS family allowance ER (7%) | =0.07*F |
| U | CNPS accident ER | =riskrate*F  (1.75%/2.5%/5%) |
| V | CFC ER (1.5%) | =0.015*E |
| W | FNE ER (1%) | =0.01*E |
| X | Employer on-cost total | =S+T+U+V+W |
| Y | Fully-loaded cost | =C+X |

## Section 14 — Bank Statement / Terminology Reading Guide

**Terminology reading guide**

| French / local term | Meaning |
| --- | --- |
| Salaire brut | Gross salary |
| Salaire net / Net à payer | Net pay |
| Bulletin de paie | Payslip |
| IRPP (Impôt sur le Revenu des Personnes Physiques) | Personal income tax |
| CAC (Centimes Additionnels Communaux) | Additional Council Tax (10% surcharge on IRPP) |
| Précompte / Retenue à la source | Withholding at source |
| DIPE | Monthly employer salary-tax declaration |
| CNPS | National Social Insurance Fund |
| CFC (Crédit Foncier du Cameroun) | Housing Fund levy |
| FNE (Fonds National de l'Emploi) | National Employment Fund levy |
| CRTV / Redevance audiovisuelle | Audiovisual royalty |
| Taxe communale | Council tax |
| Prime / Gratification | Bonus / gratuity |
| Indemnité | Allowance |
| NIU (Numéro Identifiant Unique) | Taxpayer Identification Number |
| DGI | Tax authority (Directorate General of Taxation) |

Cameroon is bilingual (French / English); statements are usually in French.

## Section 15 — Onboarding Fallback

- **Minimum to start** — Minimum to start: gross monthly salary in XAF + pay frequency. Without these, refuse (see §8.2).  _(Section 15 — Onboarding Fallback)_
- **Unknown risk class default** — If risk class is unknown, apply the 2.5% mid-band accident default and flag.  _(Section 15 — Onboarding Fallback)_
- **Missing benefit-in-kind details** — If benefit-in-kind details are missing, compute on cash salary only and flag that BIK may increase the taxable base.  _(Section 15 — Onboarding Fallback)_
- **Unknown registration status** — If registration status (NIU / CNPS number) is unknown, note that the employer must register with DGI and CNPS before lawful operation (§17) and proceed with computations marked "subject to registration."  _(Section 15 — Onboarding Fallback)_
- **Assumptions block requirement** — Always output an assumptions block listing every default applied.  _(Section 15 — Onboarding Fallback)_

## Section 16 — Filing, Remittance Deadlines and Penalties

### 16.1 Deadlines

**Deadlines table**  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/tax-administration)_

| Obligation | Deadline | Source |
| --- | --- | --- |
| Monthly DIPE return + PAYE/IRPP + salary levies remittance | **15th of the following month** | PwC, Tax administration |
| CNPS monthly contributions | Monthly, by the 15th of the following month (aligned with payroll) | PwC, Other taxes / CNPS |
| Annual individual tax return | **15 March** following year-end (fiscal year = calendar year) | PwC, Tax administration |
| Annual payroll-tax adjustment (DIPE recapitulative) — DGE | **15 March** | PwC, Tax administration |
| — Medium & Specialized Tax Centres (CIME/CSI) | **15 April** | PwC, Tax administration |
| — Divisional Tax Centres (CDI) | **15 May** | PwC, Tax administration |
| Annual recapitulative (employees) — senior citizens / public & semi-public | **31 July** (revised by 2025 Finance Act) | PwC, Tax administration |
| — private-sector under DGE / Medium / Specialized | **30 September** | PwC, Tax administration |
| — other individual taxpayers | **31 October** | PwC, Tax administration |
| Record retention | **10 years** | PwC, Tax administration |

Source (all deadlines): https://taxsummaries.pwc.com/republic-of-cameroon/individual/tax-administration

### 16.2 Penalties

**Penalties table**  _(https://taxsummaries.pwc.com/republic-of-cameroon/corporate/tax-administration ; https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income)_

| Breach | Penalty | Source |
| --- | --- | --- |
| Late monthly declaration | **10% per month, capped at 30%** of tax due (Finance Law 2010) | PwC |
| Late payment interest | **1.5% per month, capped at 50%**, from 30 days after the deadline (since 1 Jan 2018) | PwC |
| Assessment — good faith | **30%** | PwC |
| Assessment — bad faith | **100%** | PwC |
| Assessment — fraud | **150%** | PwC |

Source: https://taxsummaries.pwc.com/republic-of-cameroon/corporate/tax-administration ; https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income

## Section 17 — Registration

- **Employer registration requirement** — Employers must register with the DGI to obtain a Numéro Identifiant Unique (NIU) and with CNPS for an employer registration number before hiring.  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income ; https://www.cnps.cm/en/assures/assure-e.html)_
- **CNPS affiliation mandatory** — CNPS affiliation is mandatory for all salaried workers from the first employee — no headcount threshold.  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income ; https://www.cnps.cm/en/assures/assure-e.html)_
- **Self-employed/business minimum-tax note (not salaried employees)** — 2.2% or 5.5% of turnover (depending on regime; not salaried employees)  _(https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income ; https://www.cnps.cm/en/assures/assure-e.html)_

## Section 18 — Reference Material

**Reference material table**

| Item | Value | Source |
| --- | --- | --- |
| Currency | XAF | — |
| Tax year | Calendar year | PwC |
| IRPP effective brackets (incl. CAC) | 11% / 16.5% / 27.5% / 38.5% | PwC, Taxes on personal income |
| CAC surcharge | 10% on base IRPP | Rivermate; RemotePeople |
| 30% professional allowance | 30% | RemotePeople; Rivermate |
| Standard abatement | XAF 500,000/yr | RemotePeople |
| CNPS ceiling | XAF 750,000/mo (9,000,000/yr) | PwC; CNPS |
| CNPS pension | 4.2% EE / 4.2% ER | PwC corporate |
| CNPS family allowance | 7.0% ER | PwC corporate; Rivermate |
| CNPS accident | 1.75% / 2.5% / 5% ER | PwC corporate |
| CNPS employer total (excl. accident) | 11.2% | PwC corporate |
| CFC housing fund | 1.5% ER / 1.0% EE | PwC, Other taxes |
| FNE employment fund | 1.0% ER | PwC, Other taxes |
| CFC+FNE combined employer | 2.5% | PwC corporate |
| Council tax | XAF 250 – 2,500/mo by salary band (§3) | Reviewed table (2026-06-21); PwC for the top band |
| CRTV royalty | XAF 750 – 13,000/mo by salary band (§3) | Reviewed table (2026-06-21); PwC for the top band |
| SMIG (non-agri, secondary) | XAF 60,000/mo **[GAP]** | Playroll; RemotePeople |
| Monthly DIPE deadline | 15th of following month | PwC, Tax administration |
| Record retention | 10 years | PwC, Tax administration |

**Primary sources:** PwC Worldwide Tax Summaries — Cameroon (individual & corporate); CNPS official site (cnps.cm).
**Secondary (corroboration only):** Rivermate, RemotePeople, Playroll EOR guides — flagged inline.

## Section 19 — Test Suite

Each test states inputs → expected output. Recompute to confirm before relying on the skill.

1. **CNPS pension cap.** Gross 800,000/mo. Expected employee pension = 4.2% × 750,000 = **31,500/mo** (capped, not 4.2% × 800,000). ✓
2. **Employer CNPS (excl. accident) at cap.** Expected 11.2% × 750,000 = pension 31,500 + family 52,500 = **84,000/mo**. ✓
3. **IRPP cumulative checkpoints.** At net taxable 2,000,000 → **220,000**; 3,000,000 → **385,000**; 5,000,000 → **935,000**. ✓
4. **Example A net taxable.** Gross 250,000/mo → net taxable **1,511,000**; annual IRPP **166,210**; monthly **13,851**. ✓
5. **Example B net taxable.** Gross 800,000/mo → net taxable **5,955,000**; annual IRPP **1,302,675**; monthly **108,556**. ✓
6. **Example B net pay.** 800,000 − (31,500 + 8,000 + 108,556 + 2,500 + 9,750) = **639,694/mo**. ✓
7. **Example C employer on-cost.** Gross 800,000, mid accident → **122,750/mo**; fully loaded **922,750/mo**. ✓
8. **Council-tax bands.** Gross 60,000 (below 62,000) → council tax **0**; gross 250,000 (200,001 – 250,000) → **1,500**; gross 800,000 (above 500,000) → **2,500**. ✓
9. **CRTV bands.** Gross 250,000 (200,001 – 300,000) → **3,250**; gross 800,000 (700,001 – 800,000) → **9,750**; gross 1,500,000 (above 1,000,000) → **13,000**. ✓
10. **Example D high earner.** Gross 1,500,000/mo → net taxable **11,835,000**; annual IRPP **3,566,475**; monthly **297,206**; net pay **1,140,794**. ✓
11. **CFC+FNE employer.** Gross 800,000 → CFC 12,000 + FNE 8,000 = **20,000/mo** (2.5% × 800,000 = 20,000). ✓
12. **CAC not double-counted.** Net taxable 1,000,000 → IRPP = 11% × 1,000,000 = **110,000** (using effective rate; do NOT add a further 10%). ✓
13. **Late-declaration penalty cap.** 10%/month capped at **30%**; late-payment interest 1.5%/month capped at **50%**. ✓
14. **SMIG refusal.** Asked to certify SMIG compliance → **flag research gap, do not certify**. ✓

## PROHIBITIONS

- NEVER add the 10% CAC again — the 11%/16.5%/27.5%/38.5% rates already include it.
- NEVER apply CNPS contributions to salary above the XAF 750,000/month ceiling.
- NEVER omit the employer family-allowance contribution (7%) or the CFC/FNE levies (2.5% combined employer) from employer cost.
- NEVER compute IRPP on gross salary — always run the full net-taxable order (CNPS pension → 30% → 500,000 abatement → round down).
- NEVER apply council tax below XAF 62,000/month or CRTV at or below XAF 50,000/month, and NEVER apply a top-band amount to a salary in a lower band — read the §3 tables.
- NEVER present a SMIG figure as definitive — it is an unresolved research gap.
- NEVER present the §3 band tables as cited to the CGI — they are the reviewer's figures pending a primary citation; PwC confirms the top bands only.
- NEVER assume a currency other than XAF, or apply an FX rate without explicit input.
- NEVER miss the 15th-of-following-month DIPE deadline — penalties (10%/month up to 30%, plus interest) apply.
- NEVER file or sign a DIPE / tax return on the client's behalf.
- NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Cameroon accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Cameroon) before implementation. This is a Tier 2 (research-verified) skill that has not yet received section-by-section verification by a licensed Cameroon accountant; several figures are flagged as research gaps pending confirmation against the Code Général des Impôts and official decrees.

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
