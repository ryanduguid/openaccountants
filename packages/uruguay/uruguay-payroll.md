---
name: uruguay-payroll
description: "Use this skill whenever asked about Uruguay payroll processing for employed persons. Trigger on phrases like \"Uruguay payroll\", \"Uruguayan payroll\", \"nómina Uruguay\", \"planilla de trabajo\", \"BPS Uruguay\", \"Banco de Previsión Social\", \"aporte jubilatorio\", \"montepío\", \"15% BPS\", \"7.5% patronal\", \"FONASA Uruguay\", \"FRL Uruguay\", \"Fondo de Reconversión Laboral\", \"IRPF Uruguay\", \"IRPF Categoría II\", \"rentas de trabajo\", \"retención IRPF\", \"BPC Uruguay\", \"Base de Prestaciones y Contribuciones\", \"mínimo no imponible\", \"MNIG\", \"salario mínimo nacional Uruguay\", \"minimum wage Uruguay\", \"aguinaldo Uruguay\", \"ajuste anual IRPF\", \"DGI Uruguay\", \"net salary Uruguay\", \"salario líquido\", \"salario nominal\", \"gross to net Uruguay\", \"employer contribution Uruguay\", \"tope de cotización\", \"Formulario 1102\", or any question about computing employee pay, IRPF withholding, or social-security (BPS) contributions for Uruguay-based employees. CRITICAL STRUCTURAL FACT: unlike many Latin-American jurisdictions, in Uruguay the employer IS an IRPF withholding agent on dependent salaries — IRPF (Categoría II) is withheld monthly on a progressive scale and reconciled by a year-end ajuste anual, on top of mandatory BPS contributions. This skill covers IRPF withholding, BPS contributions (jubilatorio, FONASA, FRL, FGCL), the retirement contribution ceiling, the minimum wage, the IRPF annual sworn declaration, and filing/payslip obligations. ALWAYS read this skill before processing any Uruguay payroll."
version: 0.2
jurisdiction: UY
tax_year: 2025
tax_year_notes: "2025 (full 2026 scale and BPS constants stated alongside, at BPC 6,864)"
last_updated: 2026-10-10
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uruguay Payroll Skill v0.2 (Tier 2 — research-verified, reviewer sign-off pending)

> **The retirement contribution ceiling changes in February, not January.** BPS's historical values table ("Topes Art. 7º y 8º (Ley 16713) - C") gives UYU 288,836 from February 2026, UYU 272,564 from February 2025 and UYU 256,821 from February 2024, while the BPC moves on 1 January. A January 2026 payroll therefore caps retirement contributions at UYU 272,564 and a January 2025 payroll at UYU 256,821. Read the ceiling for the pay month off BPS's values table before using any retirement calculation or template below.

> **Edited 2026-10-10 (v0.2).** Citations moved from PwC Worldwide Tax Summaries to the statutes (Texto Ordenado 2023 Título 7, Decreto 148/007, Ley 16.713, Ley 18.083, Ley 18.211, Ley 19.689, Ley 19.690, the Código Tributario and the BPC, minimum-wage and penalty decrees) and to BPS and DGI publications. Corrections: the monthly IRPF withholding base is increased by 6% when the month's income exceeds 10 BPC (Decreto 148/007 art. 63), which changes Examples C, D and E; the aguinaldo and the salario vacacional are withheld at the top marginal rate instead of entering the scale; the AFAP split, the BPS payment calendar, the penalty amounts and the 2026 Fondo de Solidaridad values are filled in.

## Uruguay Payroll Skill v0.2 (Tier 2 — research-verified, reviewer sign-off pending)

> **Tier 2 status.** Every rate, threshold, and deadline below is sourced to a statute or decree (Texto Ordenado 2023, Decreto 148/007, Ley 16.713 and later laws, published by IMPO) or to a BPS or DGI publication, with EY Uruguay cited for the 2025 filing campaign, and cited inline. It has **not** yet been section-by-section verified by a licensed Uruguayan accountant (contador público). Items marked **[RESEARCH GAP — reviewer to confirm]** carry residual uncertainty and must be confirmed against primary sources before reliance.

> **READ THIS FIRST — the single most important structural fact.** Uruguay **does** levy a personal income tax on labour income (**IRPF — Impuesto a la Renta de las Personas Físicas, Categoría II / rentas de trabajo**), and — unlike Paraguay or many other LATAM jurisdictions — **the employer IS the withholding agent.** IRPF is **withheld monthly** on a progressive 0%–36% scale and reconciled at year end via the **ajuste anual** performed through BPS. On top of IRPF the employer also withholds and pays **BPS** social-security contributions (retirement/montepío, FONASA, FRL). Almost every IRPF threshold is expressed in units of the **BPC** (Base de Prestaciones y Contribuciones): **BPC = UYU 6,864/month for 2026** and **UYU 6,576/month for 2025**. The BPC changes every 1 January, and every peso threshold in this skill changes with it, so take the BPC from the pay period you are running. See Section 2.

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Uruguay (Oriental Republic of Uruguay) |
| Currency | UYU (Uruguayan peso, "$") only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Income-tax withholding on salaries | **Yes — employer withholds IRPF Categoría II monthly** on a progressive scale, with a year-end ajuste anual (Decreto 148/007 arts. 62 to 64; BPS Comunicados R 2/2025 and R 5/2026) |
| Reference unit | **BPC = UYU 6,864/month** for 2026 (+4.38%, from 1 Jan 2026, Decreto N° 11/026); **UYU 6,576/month** for 2025 (Decreto N° 5/025; BPS Comunicado R 2/2025) |
| IRPF non-taxable minimum (MNIG) | = 7 BPC: **UYU 48,048/month** in 2026, **UYU 46,032/month** in 2025; first peso above this is taxed (Decreto 148/007 art. 63; BPS Comunicados R 2/2025 and R 5/2026) |
| IRPF scale | Progressive **0% – 36%** across 8 monthly brackets, the twelfths of the annual scale of Texto Ordenado 2023 Título 7 art. 48 (Decreto 148/007 art. 63) |
| IRPF withholding base above 10 BPC | When the month's income (excluding aguinaldo) exceeds 10 BPC (UYU 68,640 in 2026; UYU 65,760 in 2025), the part subject to personal contributions is **increased by 6%** before the scale is applied; the ajuste anual drops the uplift (Decreto 148/007 arts. 60 and 63; BPS Comunicado 24/2023) |
| Aguinaldo and salario vacacional | Not entered into the scale: withheld at the **top marginal rate** reached by the month's other income (Título 7 arts. 47 and 48; Decreto 148/007 art. 63; BPS Comunicado 24/2023 ítem 3.2) |
| Employee retirement (jubilatorio/montepío) | **15%** of nominal salary, withheld by employer (Ley 16.713 art. 181; BPS Tasas) |
| Employer retirement (patronal) | **7.5%** of nominal salary (general private-sector rate) (Ley 18.083 art. 87; BPS Tasas) |
| FONASA (health) | Employer **5%** plus the Complemento de Cuota Mutual where it applies; employee **3%–8%** by income & family situation (Ley 18.211 arts. 61 and 66; BPS Tasas Fonasa) |
| FRL (Fondo de Reconversión Laboral) | **0.1%** employee + **0.1%** employer (Ley 19.689 art. 17; BPS FRL page) |
| FGCL (labour-credit guarantee) | **0.025%** employer only (Ley 19.690 art. 10; BPS FGCL page) |
| Retirement contribution ceiling | Retirement contributions apply only up to **UYU 288,836/month** from February 2026 and **UYU 272,564/month** from February 2025 (UYU 256,821 from February 2024). It is the indexed top of the second level of Ley 16.713 art. 7, not a BPC multiple: it rose 5.97% in February 2026 against the BPC's 4.38% in January, so read it off BPS's values table (BPS, Valores actuales and Valores históricos) |
| Minimum wage | **UYU 25,383/month** from 1 Jul 2026 (+3.3%); **UYU 24,572/month** from 1 Jan 2026 (+4.1%, Decreto N° 319/025 of 26 Dec 2025); **UYU 23,604/month** from 1 Jan 2025 (+6%, Decreto N° 369/024). The 2026 rise was decreed in two steps, so the figure changes mid-year (IMPO) |
| Tax authority (IRPF) | **DGI** — Dirección General Impositiva |
| Social-security authority | **BPS** — Banco de Previsión Social (receives the IRPF withholding declaration with the nómina and computes the withholdings: Decreto 148/007 art. 65) |
| BPS nómina and payment | Monthly, by the BPS calendar date for the last digit of the company number: the January 2026 nómina and payment by 18 February (digits 0 to 4) or 19 February (5 to 9) (BPS, Vencimientos 2026) |
| IRPF annual sworn declaration | **Form 1102** (individual) / **Form 1103** (family unit) — most single-employer employees do NOT file (employer ajuste anual instead) (Decreto 148/007 art. 64; DGI) |
| Filing portals | DGI (servicios en línea); BPS (nómina / GAFI) |
| Validated by | Pending — requires sign-off by a licensed Uruguayan accountant (contador público) |
| Skill version | 0.2 (Tier 2) |

## Section 2 -- Income Tax Withholding (IRPF Categoría II — employer-withheld)

Uruguay levies **IRPF (Impuesto a la Renta de las Personas Físicas), Categoría II — rentas de trabajo**, on labour income (Texto Ordenado 2023, Título 7, arts. 5, 11 and 42). The employer **IS** the withholding agent (responsable sustituto) and withholds IRPF **monthly** on the progressive scale below, reconciling over the year via the **ajuste anual** at 31 December, declared through BPS (Decreto 148/007 arts. 62 to 65). The peso values of the monthly scale are published each year by BPS: Comunicado R 2/2025 for 2025 and Comunicado R 5/2026 for 2026.

### 2.1 Monthly progressive income scale (escala mensual progresional de rentas)

The bracket boundaries are fixed at 7/10/15/30/50/75/115 BPC and the rates at
0/10/15/24/25/27/31/36. Neither changed for 2026. Only the BPC changed, and
every peso column below is a BPC multiple, so **run the scale for the year of
the pay period** rather than carrying peso figures forward.

**Monthly progressive IRPF scale 2026 (BPC = UYU 6,864)**

| Bracket (BPC) | Desde (UYU/month) | Hasta (UYU/month) | Rate | Cumulative tax at top of bracket (UYU) |
| --- | --- | --- | --- | --- |
| Up to 7 BPC | 0 | 48,048 | 0% | 0.00 |
| Over 7–10 BPC | 48,049 | 68,640 | 10% | 2,059.20 |
| Over 10–15 BPC | 68,641 | 102,960 | 15% | 7,207.20 |
| Over 15–30 BPC | 102,961 | 205,920 | 24% | 31,917.60 |
| Over 30–50 BPC | 205,921 | 343,200 | 25% | 66,237.60 |
| Over 50–75 BPC | 343,201 | 514,800 | 27% | 112,569.60 |
| Over 75–115 BPC | 514,801 | 789,360 | 31% | 197,683.20 |
| Over 115 BPC | 789,361 | — | 36% | — |

**Monthly progressive IRPF scale 2025 (BPC = UYU 6,576)**  _(Decreto 148/007 art. 63 for the BPC brackets; BPS Comunicado R 2/2025 and DGI, IRPF categoría 2 escalas y alícuotas, for the peso values)_

| Bracket (BPC) | Desde (UYU/month) | Hasta (UYU/month) | Rate | Cumulative tax at top of bracket (UYU) |
| --- | --- | --- | --- | --- |
| Up to 7 BPC | 0 | 46,032 | 0% | 0.00 |
| Over 7–10 BPC | 46,033 | 65,760 | 10% | 1,972.80 |
| Over 10–15 BPC | 65,761 | 98,640 | 15% | 6,904.80 |
| Over 15–30 BPC | 98,641 | 197,280 | 24% | 30,578.40 |
| Over 30–50 BPC | 197,281 | 328,800 | 25% | 63,458.40 |
| Over 50–75 BPC | 328,801 | 493,200 | 27% | 107,846.40 |
| Over 75–115 BPC | 493,201 | 756,240 | 31% | 189,388.80 |
| Over 115 BPC | 756,241 | — | 36% | — |

- **Tax computed bracket-by-bracket** — Tax is computed bracket-by-bracket (progressive marginal), NOT flat.  _(Título 7 art. 47; Decreto 148/007 art. 63)_
- **General non-taxable minimum (MNIG)** — = 7 BPC: UYU 48,048/month in 2026, UYU 46,032/month in 2025. Below this, no IRPF.  _(Decreto 148/007 art. 63; BPS Comunicados R 2/2025 and R 5/2026; Decreto N° 11/026)_
- **6% uplift above 10 BPC** — When the month's income excluding the aguinaldo exceeds 10 BPC (UYU 68,640 in 2026; UYU 65,760 in 2025), the computable income subject to personal social-security contributions is increased by 6% before the scale is applied, and the contribution ceilings of the AFAP regime are ignored when fixing that base: a UYU 120,000 salary enters the 2025 scale as 127,200. The uplift applies only to the monthly advances and withholding; the ajuste anual and the annual return recompute on actual income without it, which is why most employees above 10 BPC are refunded part of the year's withholding in December.  _(Decreto 148/007 arts. 60 and 63 num. 1; BPS Comunicado 24/2023 ítem 1.1)_
- **Aguinaldo and salario vacacional** — The sueldo anual complementario and the statutory suma para el mejor goce de la licencia do not enter the monthly scale and do not count towards the 10 BPC or 15 BPC tests. They are withheld at a proportional rate equal to the highest marginal rate reached by the month's other income, without the 6% uplift. The personal contributions withheld on them are deductible items at the ajuste anual.  _(Título 7 arts. 47 and 48; Decreto 148/007 art. 63; BPS Comunicado 24/2023 ítems 2.1 and 3.2)_

**Cumulative-tax check (recomputed bracket by bracket):**
- 10% × (65,760 − 46,032) = 10% × 19,728 = **1,972.80** ✓
- + 15% × (98,640 − 65,760) = 15% × 32,880 = 4,932.00 → **6,904.80** ✓
- + 24% × (197,280 − 98,640) = 24% × 98,640 = 23,673.60 → **30,578.40** ✓
- + 25% × (328,800 − 197,280) = 25% × 131,520 = 32,880.00 → **63,458.40** ✓
- + 27% × (493,200 − 328,800) = 27% × 164,400 = 44,388.00 → **107,846.40** ✓
- + 31% × (756,240 − 493,200) = 31% × 263,040 = 81,542.40 → **189,388.80** ✓ (Self-verified.)

**Cumulative-tax check, 2026:**
- 10% × (68,640 − 48,048) = 10% × 20,592 = **2,059.20** ✓
- + 15% × (102,960 − 68,640) = 15% × 34,320 = 5,148.00 → **7,207.20** ✓
- + 24% × (205,920 − 102,960) = 24% × 102,960 = 24,710.40 → **31,917.60** ✓
- + 25% × (343,200 − 205,920) = 25% × 137,280 = 34,320.00 → **66,237.60** ✓
- + 27% × (514,800 − 343,200) = 27% × 171,600 = 46,332.00 → **112,569.60** ✓
- + 31% × (789,360 − 514,800) = 31% × 274,560 = 85,113.60 → **197,683.20** ✓ (Self-verified.)
- Cross-check: each 2026 cumulative is its 2025 counterpart × 6,864/6,576. 189,388.80 × 1.043796 = 197,683.20 ✓

- **Annual scale figures** — The statute sets the scale annually in BPC (84/120/180/360/600/900/1,380) and the monthly scale is its twelfth. 2026: 0% to 576,576; 10% 576,576–823,680; 15% 823,680–1,235,520; 24% 1,235,520–2,471,040; 25% 2,471,040–4,118,400; 27% 4,118,400–6,177,600; 31% 6,177,600–9,472,320; 36% above 9,472,320. 2025: 0% to 552,384; 10% 552,384–789,120; 15% 789,120–1,183,680; 24% 1,183,680–2,367,360; 25% 2,367,360–3,945,600; 27% 3,945,600–5,918,400; 31% 5,918,400–9,074,880; 36% above 9,074,880.  _(Texto Ordenado 2023, Título 7, art. 48 lit. A; Decreto 148/007 art. 60)_

The BPC values are **UYU 6,864** for 2026 (Decreto N° 11/026) and **UYU 6,576** for 2025 (Decreto N° 5/025); never use a converted or foreign-currency figure for the BPC.

### 2.2 Deductions mechanism (escala de deducciones)

- **Deductions mechanism overview** — IRPF allows specified deductions, but they are not subtracted from the income base: their sum is multiplied by a flat rate (14% or 8%) and the result is subtracted from the gross IRPF on income.  _(Título 7 art. 49; Decreto 148/007 art. 58 (annual) and art. 63 num. 2 (monthly))_

**Fixed monthly deduction-credit rate table**  _(Decreto 148/007 art. 63 num. 2; BPS Comunicados R 2/2025 and R 5/2026)_

| Nominal IRPF income in the month (excluding aguinaldo and salario vacacional) | Deduction credit rate | Source |
| --- | --- | --- |
| ≤ 15 BPC (≤ UYU 102,960 in 2026; ≤ UYU 98,640 in 2025) | **14%** | Decreto 148/007 art. 63; BPS Comunicados |
| > 15 BPC (> UYU 102,960 in 2026; > UYU 98,640 in 2025) | **8%** | Decreto 148/007 art. 63; BPS Comunicados |

The annual test is 180 BPC of nominal income (Título 7 art. 49; Decreto 148/007 art. 58). The 14% rate replaced 10% from FY2023 under Ley 20.124.

**Deductible items (monthly values) table**  _(Título 7 art. 49; Decreto 148/007 arts. 56 and 63; BPS Comunicados R 2/2025 (2025 values) and R 5/2026 (2026 values))_

The child deductions below are BPC multiples. The Fondo de Solidaridad, Caja de Profesionales and withholding-option figures are published in pesos by BPS each year; both years are shown. Proportional deductions (contributions) are taken at the month's actual amounts; non-proportional ones (children, Fondo de Solidaridad, mortgage instalments) at one twelfth of the annual figure (Decreto 148/007 art. 63).

| Item | Monthly value (UYU) | Source |
| --- | --- | --- |
| Personal social-security contributions (montepío 15% + FONASA + FRL employee shares) | actual amounts withheld | Título 7 art. 49 lits. A and B |
| Dependent minor child | = 20 BPC annual / 12: **11,440** per child in 2026; **10,960** in 2025 | Título 7 art. 49 lit. D; BPS Comunicados R 5/2026 and R 2/2025 |
| Dependent child with disability | = 40 BPC annual / 12: **22,880** per child in 2026; **21,920** in 2025 | Título 7 art. 49 lit. D; BPS Comunicados R 5/2026 and R 2/2025 |
| Fondo de Solidaridad — Cat.1 / Cat.2 / Cat.3 / Cat.4 / Cat.5 | 2026: 286 / 572 / 1,144 / 1,049 / 1,621; 2025: 274 / 548 / 1,096 / 1,005 / 1,553 | Título 7 art. 49 lit. C; BPS Comunicados R 5/2026 and R 2/2025 |
| Caja de Profesionales Universitarios (Ley 17.738 ten-category scale) | 2026: 7,566 (1st) to 39,734 (10th), 1st especial bonificada 3,802; 2025: 6,447 (1st) to 33,855 (10th), 11th/especial 3,241. BPS R 5/2026 also prints the Ley 20.410 reduced-ficto scale and the fifteen-category scale | Título 7 art. 49 lit. A; BPS Comunicados R 5/2026 and R 2/2025 |
| Mortgage loan instalments on the sole permanent home (cost up to UI 1,000,000) | one twelfth of the annual instalments, capped at 36 BPC a year | Título 7 art. 49 lit. E; Decreto 148/007 art. 56 bis |
| Option to exclude from withholding regime — importe límite (monthly) | **68,300** in 2026; **65,400** in 2025 | Decreto 148/007 art. 64 bis; BPS Comunicados R 5/2026 and R 2/2025 |

- **IRPF due formula** — The deduction credit is computed as `credit rate × (sum of deductible items)`, then `IRPF due = max(0, gross IRPF on income − deduction credit)`. If the credit exceeds the gross IRPF, IRPF due is zero (it does not create a negative/refundable amount within the monthly withholding). The housing-rent credit (8% of rent paid, Título 7 art. 51) is not a payroll item: the employee claims it in the annual return.  _(Decreto 148/007 art. 63; BPS Comunicado 24/2023 ítem 3.1)_

### 2.3 IRPF annual sworn declaration (declaración jurada) and the ajuste anual

**Annual sworn declaration / ajuste anual table**  _(Decreto 148/007 art. 64; BPS Comunicado 24/2023; DGI, Calendario de la Campaña 2026 de IRPF and Vencimientos 2026 calendario general, ordinal 16; EY Uruguay for the 2025 campaign)_

| Item | Detail | Source |
| --- | --- | --- |
| Year-end mechanism for single-employer employees | In December the employer computes the year's tax on actual income (no 6% uplift), with the aguinaldo and salario vacacional at the top marginal rate, deducts the January-to-November withholdings and withholds or stops withholding accordingly; a negative result is settled by DGI, which pays automatic refunds from June of the following year. For a worker whose only labour income came from that employer the withholding is final | Decreto 148/007 art. 64; BPS Comunicado 24/2023 ítems 1 to 6 |
| Annual filing window (FY2025, filed 2026) | **29 June – 31 August 2026**, the same range for every taxpayer: DGI dropped the last-digit staggering for the 2026 campaign. Pre-filled online form from 26 June; refunds from 28 July 2026 for returns filed before the 15th of a month | DGI, "Calendario de la Campaña 2026 de IRPF" |
| Annual filing window (FY2024, for reference) | 7 July – 28 August 2025 | EY Uruguay |
| Forms | **Form 1102** (individual) / **Form 1103** (family unit / núcleo familiar) | DGI |
| Mandatory filers | Independent workers; employees with more than one employer whose nominal labour income exceeds 150,000 UI in the year; núcleo familiar electors and employees who asked for the 5% withholding reduction; employees not in employment on 31 December | Decreto 148/007 art. 64; DGI, Instructivo Formulario 1102 |
| Payment (if owed) | Up to 5 equal instalments: 31 August, 30 September, 30 October, 30 November and 30 December 2026 for the FY2025 balance (FY2024: first 29 Aug 2025, last 30 Dec 2025) | DGI, Vencimientos 2026, ordinal 16; EY Uruguay |

Most single-employer employees are **NOT** required to file — the employer's ajuste anual settles the year (Decreto 148/007 art. 64).

### 2.4 IRNR (non-resident income tax) — out of scope but flagged

- **IRNR regime for non-residents** — Non-residents are taxed under IRNR on Uruguayan-source income at 12% (residual rate), 7% on dividends, 25% on income of entities in low- or no-tax jurisdictions, and 0.5% to 12% on listed interest by currency and term; labour income is computed as for IRPF. IRNR is a distinct regime from the employer IRPF withholding covered here; route IRNR questions to a specialist.  _(Texto Ordenado 2023, Título 8, arts. 13 and 18)_

## Section 3 -- Social Security (BPS) -- Employee Deductions

Uruguay's mandatory social-security scheme is BPS (Banco de Previsión Social). The employer withholds the employee shares and remits them with the employer shares via the monthly BPS nómina. The contribution base (materia gravada) is every regular and permanent remuneration in cash or in kind for the worker's personal activity, including bonuses paid with regularity and the aguinaldo (Ley 16.713 arts. 153 and 158). (Sources: Ley 16.713 art. 181; Ley 18.211 arts. 61 and 66; Ley 19.689 art. 17; BPS Tasas; BPS Tasas Fonasa.)

### 3.1 Retirement / pension (Jubilatorio — "montepío")

**Retirement employee rate table**  _(Ley 16.713 art. 181; BPS Tasas)_

| Item | Employee rate | Base | Source |
| --- | --- | --- | --- |
| Retirement (montepío) | **15%** of nominal salary | Nominal salary up to the retirement ceiling (Section 4.4) | Ley 16.713 art. 181; BPS Tasas |

### 3.2 FONASA (national health fund) — variable employee rate

- **FONASA employee variability** — Employee FONASA is 3%–8% by income level and family situation. The band split is 2.5 BPC = UYU 17,160 in 2026 and UYU 16,440 in 2025, tested on all remuneration subject to contributions in the month excluding the aguinaldo.  _(Ley 18.211 art. 61; BPS Tasas Fonasa)_

**FONASA employee rate by income and family situation**  _(Ley 18.211 art. 61 (3% / 4.5% / 6%) and art. 66 (+2% spouse or partner); BPS Tasas Fonasa)_

| Monthly income | No dependents (single) | Single, with children | With spouse/partner, no children | With spouse/partner + children |
| --- | --- | --- | --- | --- |
| ≤ 2.5 BPC (≤ UYU 17,160 in 2026; ≤ UYU 16,440 in 2025) | 3% | 3% | 5% | 5% |
| > 2.5 BPC (> UYU 17,160 in 2026; > UYU 16,440 in 2025) | 4.5% | 6% | 6.5% | 8% |

- **Spouse surcharge condition** — The spouse/partner surcharge applies only if the spouse lacks own SNIS coverage.  _(Ley 18.211 art. 66; BPS Tasas Fonasa)_
- **Socios vitalicios** — Life members of a mutual-aid institution pay 0% basic FONASA, with the 3% child and 2% spouse additions only (0% / 3% / 2% / 5%).  _(BPS Tasas Fonasa)_
- **FONASA not subject to retirement ceiling** — FONASA is NOT subject to the retirement ceiling — it applies to the full nominal salary.  _(Ley 18.211 art. 61; BPS)_

### 3.3 FRL — Fondo de Reconversión Laboral

**FRL employee rate table**  _(Ley 19.689 art. 17; BPS FRL page)_

| Item | Employee rate | Source |
| --- | --- | --- |
| FRL | **0.1%** of nominal salary (0.125% until 31 December 2018) | Ley 19.689 art. 17; BPS FRL page |

- **FRL not subject to retirement ceiling** — FRL is NOT subject to the retirement ceiling — it applies to the full nominal salary.  _(Ley 19.689 art. 17: computed on the asignaciones computables subject to contributions)_

### 3.4 Employee total (illustrative, single, no dependents, > 2.5 BPC, below ceiling)

**Employee total illustrative table**  _(sum of the three rows)_

| Component | Rate | Source |
| --- | --- | --- |
| Retirement (montepío) | 15% | Ley 16.713 art. 181 |
| FONASA | 4.5% | Ley 18.211 art. 61 |
| FRL | 0.1% | Ley 19.689 art. 17 |
| **Employee BPS total (this case)** | **19.6%** | sum of the three rows |

**Total-row check (recomputed):** 15 + 4.5 + 0.1 = **19.6** ✓ (Self-verified.) Note the FONASA rate (and hence this total) changes with income band and family situation (Section 3.2).

## Section 4 -- Social Security (BPS) -- Employer Contributions

(Sources: Ley 18.083 art. 87; Ley 18.211 art. 61; Ley 19.689 art. 17; Ley 19.690 art. 10; BPS Tasas; BPS Tasas Fonasa; BPS FGCL page.)

### 4.1 Employer contribution rates (general private sector)

**Employer contribution rates table**  _(Ley 18.083 art. 87; Ley 18.211 art. 61; Ley 19.689 art. 17; Ley 19.690 art. 10; BPS Tasas; BPS Tasas Fonasa)_

| Component | Employer rate | Base | Source |
| --- | --- | --- | --- |
| Retirement (patronal/jubilatorio) | **7.5%** | Nominal salary up to the retirement ceiling (Section 4.4) | Ley 18.083 art. 87 (generic rate from 1 July 2007); BPS Tasas |
| FONASA | **5%** (+ CCM where applicable) | Remuneration subject to montepío | Ley 18.211 art. 61; BPS Tasas Fonasa |
| FRL | **0.1%** | Full nominal salary | Ley 19.689 art. 17 |
| FGCL (Fondo de Garantía de Créditos Laborales) | **0.025%** | Full nominal salary (materia gravada of Ley 16.713 art. 153) | Ley 19.690 art. 10; BPS FGCL page |

- **Civil/public organism note** — Civil/public organisms use different patronal rates (Ley 18.083 art. 87 keeps the aportación civil outside the unified rate); this skill applies the general private-sector 7.5% unless told otherwise.

### 4.2 Employer total

- **Employer total headline** — The employer total is 12.625% = 7.5% jubilatorio + 5% FONASA + 0.1% FRL + 0.025% FGCL, before BSE accident insurance and the CCM.  _(Sum of the rates in 4.1)_

**Total-row check (recomputed):** 7.5 + 5 + 0.1 + 0.025 = **12.625** ✓ (Self-verified.)

> This 12.625% bundles FONASA at the base 5%. Effective employer cost rises with the Complemento de Cuota Mutual (CCM = number of covered workers × cuota mutual − (3% basic personal contributions + 5% employer contributions); the cuota mutual was UYU 1,880 in September and October 2026 per BPS Valores actuales) and the activity-specific BSE (Banco de Seguros del Estado) workplace-accident premium (mandatory, rate varies by risk class — **[RESEARCH GAP — reviewer to confirm]**, no single national rate).

### 4.3 Combined headline burden (employee illustrative + employer)

**Combined headline burden table**

| Side | Components | Total |
| --- | --- | --- |
| Employee (single, >2.5 BPC, below ceiling) | 15% + 4.5% + 0.1% | **19.6%** |
| Employer (general private sector) | 7.5% + 5% + 0.1% + 0.025% | **12.625%** |

**Total-row check:** employee 15 + 4.5 + 0.1 = 19.6 ✓; employer 7.5 + 5 + 0.1 + 0.025 = 12.625 ✓ (Self-verified.) (Employee total varies with the FONASA band/family situation; this row shows the single, >2.5 BPC, no-dependents case.)

### 4.4 Retirement contribution ceiling (tope de cotización)

**Retirement contribution ceiling table**  _(Ley 16.713 art. 7; BPS, Valores actuales and Valores históricos, "Topes Art. 7º y 8º (Ley 16713) - C")_

| Item | Detail | Source |
| --- | --- | --- |
| Retirement ceiling | Retirement contributions (employee 15% **and** employer 7.5%) apply **only up to UYU 288,836/month from February 2026**, **UYU 272,564/month from February 2025 to January 2026** and UYU 256,821/month from February 2024 to January 2025; salary above the cap is exempt from retirement contribution | Ley 16.713 art. 7; BPS Valores históricos |
| FONASA / FRL / FGCL | **NOT** subject to the retirement cap — apply to the full nominal salary | Ley 18.211 art. 61; Ley 19.689 art. 17; Ley 19.690 art. 10 |

### 4.5 AFAP (private pension pillar)

- **AFAP mixed regime description** — The 15% employee retirement contribution is split between BPS's solidarity pillar and the worker's AFAP by income levels that BPS indexes with the ceiling. For affiliates of the Ley 16.713 mixed regime (first job before 1 December 2023): contributions on income up to level A (UYU 96,279 from February 2026) go to BPS, or half of them to the AFAP under the art. 8 option, and contributions on income between level A and the ceiling (level C, UYU 288,836) go to the AFAP; level B (UYU 144,418) governs the art. 8 option for incomes between A and B. For people whose first job started on or after 1 December 2023 (Sistema Previsional Común, Ley 20.130 art. 22): 10% of income up to UYU 144,418 goes to BPS, 5% of that same tranche and 15% of income between UYU 144,418 and 288,836 go to the AFAP. Income above the ceiling bears no retirement contribution (voluntary savings only).  _(Ley 16.713 arts. 7 and 8; Ley 20.130 art. 22; BPS Valores actuales, "Topes Art. 7º y 8º (Ley 16713)" and "Niveles Art. 22 (ley 20.130)", values for February to October 2026)_

The split never changes the **total** 15% employee retirement withholding or the employer's 7.5%; it matters only for the BPS versus AFAP allocation shown on the nómina.

### 4.6 Payment / filing

**Payment/filing table**  _(Decreto 148/007 art. 65; BPS, Vencimientos 2026; BPS, Tributación régimen general)_

| Item | Detail | Source |
| --- | --- | --- |
| Monthly | BPS **nómina** (payroll declaration): employee + employer BPS shares + IRPF withheld, which BPS computes from the declared data and collects with the contributions | Decreto 148/007 art. 65 |
| Due date | By the BPS calendar date of the month after the payroll month, keyed to the last digit of the company number. 2026 dates for digits 0 to 4: 19 Jan, 18 Feb, 16 Mar, 20 Apr, 19 May, 15 Jun, 15 Jul, 17 Aug, 15 Sep, 16 Oct, 17 Nov, 15 Dec; for digits 5 to 9: 20 Jan, 19 Feb, 17 Mar, 21 Apr, 20 May, 16 Jun, 16 Jul, 18 Aug, 16 Sep, 19 Oct, 18 Nov, 16 Dec. Example: the January 2026 nómina of company 3421234 is due by 18 February 2026 | BPS, Vencimientos 2026 (updated 30 April 2026) |
| Registration | Any dependent worker triggers mandatory BPS employer registration; no income floor exempts the employer | BPS |

## Section 5 -- Minimum Wage (Salario Mínimo Nacional)

- **Minimum wage authority** — Authority: Executive (Decreto), after consulting the Consejo Superior Tripartito (Decreto-Ley 14.791 art. 1 lit. e; Ley 18.566 art. 10). 2025: Decreto N° 369/024 (+6% from 1 January 2025). 2026: Decreto N° 319/025 (+4.1% from 1 January and +3.3% from 1 July 2026). The daily wage is the monthly figure divided by 25 and the hourly wage divided by 200.  _(Decreto N° 369/024 and Decreto N° 319/025 (IMPO))_

**Minimum wage table**  _(Decreto N° 369/024; Decreto N° 319/025 (IMPO))_

| Item | Value by effective date | Source |
| --- | --- | --- |
| Monthly national minimum wage | **UYU 25,383** from 1 Jul 2026; **UYU 24,572** from 1 Jan 2026; **UYU 23,604** from 1 Jan 2025 | Decreto N° 319/025 (26 Dec 2025); Decreto N° 369/024 (IMPO) |

- **Minimum wage below IRPF threshold** — The minimum wage sits well below the MNIG in both years (UYU 25,383 against 48,048 in 2026; UYU 23,604 against 46,032 in 2025), so a minimum-wage earner pays no IRPF but still pays BPS contributions (Section 3).

> The 2026 adjustment came in two steps under Decreto N° 319/025 of 26 December 2025: **UYU 24,572** from 1 January 2026 (+4.1%) and **UYU 25,383** from 1 July 2026 (+3.3%), 7.54% for the year. A 2026 payroll therefore uses a different minimum wage in the first half of the year than in the second — check the month, not just the year.

## Section 6 -- Conservative Defaults

When inputs are ambiguous, apply these defaults and flag the assumption to the user:

1. **Employer withholds IRPF.** Uruguay's employer IS an IRPF withholding agent — compute monthly IRPF on the progressive scale (Section 2) AND BPS contributions (Sections 3–4). Do not skip IRPF as if it were self-assessed.
2. **Family/FONASA situation = single, no dependents.** Apply FONASA at 3% (≤ 2.5 BPC) or 4.5% (> 2.5 BPC) unless the user states children/spouse (which change the FONASA band and add child deductions). Flag the assumption.
3. **Sector = general private sector.** Employer retirement 7.5%; do not apply civil/public-organism rates without confirmation.
4. **Retirement ceiling applied** at UYU 288,836/month for 2026 periods (UYU 272,564 for 2025) to the 15% employee and 7.5% employer retirement only; FONASA/FRL/FGCL on full nominal salary (Section 4.4).
5. **No deductions beyond personal BPS contributions** unless the user provides them. Apply the deduction-credit rate (14% if nominal income is at or below 15 BPC — UYU 102,960 in 2026, UYU 98,640 in 2025 — else 8%) to the sum of deductible items (Section 2.2). Do not invent Fondo de Solidaridad / Caja Profesional / mortgage figures.
6. **Currency:** all amounts in **UYU**. Never assume USD or any other currency.
7. **Pay period:** take the constants from the month being run. **2026**: BPC 6,864; MNIG 48,048; 10 BPC uplift threshold 68,640; retirement ceiling 288,836 from February (272,564 in January); minimum wage 24,572 to 30 June and 25,383 from 1 July. **2025**: BPC 6,576; MNIG 46,032; uplift threshold 65,760; ceiling 272,564 from February (256,821 in January); minimum wage 23,604. If the pay period is unknown, ask — never assume the earlier year.
8. **6% uplift:** apply it whenever the month's income excluding the aguinaldo exceeds 10 BPC (Section 2.1); it is part of the withholding the employer must make, and the ajuste anual gives it back.
9. **Aguinaldo:** withhold at the top marginal rate of the month's other income, never through the scale (Section 2.1).
10. **AFAP split:** state the total 15% and, if asked, the BPS/AFAP allocation by the BPS levels (Section 4.5); it does not change the withholding.

### 7.1 Required inputs (must have before computing payroll)

**Required inputs table**

| Input | Why needed |
| --- | --- |
| Monthly **nominal** salary in UYU | Drives the IRPF scale, BPS bases, and both contribution sides |
| Family / FONASA situation (single / with children / with spouse w/o SNIS cover) | Selects the FONASA employee band (3%–8%) and child deductions |
| Number of dependent minor children (and any with disability) | Each adds a monthly IRPF deduction (11,440 / 22,880 in 2026; 10,960 / 21,920 in 2025) |
| Employer sector (general private vs civil/public organism) | Confirms the 7.5% patronal rate |
| Pay period (month/year) | Selects the BPC, MNIG, minimum wage and retirement ceiling. The month matters as well as the year: the 2026 minimum wage rises on 1 July |
| Whether the employee has multiple employers / elects family-unit regime | Affects annual filing obligation and withholding option |
| Employer registration with BPS | Must be registered before running payroll |

### 7.2 Refusal catalogue — STOP and ask rather than guess

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| Salary stated in USD or another currency | **Refuse to compute.** Ask for the UYU nominal amount (or the FX basis used). |
| User asks to skip IRPF withholding ("they self-assess") | Do **not** skip. Explain Uruguay's employer IS an IRPF withholding agent (Section 2); compute monthly IRPF and the year-end ajuste anual. |
| FONASA family situation not stated | Default to single/no-dependents and **flag it** — do not silently apply a spouse/children band. |
| Pay period in 2027 or later | Apply the 2026 constants (BPC 6,864, ceiling 288,836) and flag that they are last year's until the 2027 BPC decree and BPS values table are published; do not invent them. |
| Civil/public-organism employer | Confirm the patronal rate; do not apply 7.5% blindly. |
| Request for the AFAP split of the 15% retirement | State the total 15% withholding and the BPS/AFAP allocation by the BPS levels in force for the month (Section 4.5); confirm whether the worker entered the labour market before or from 1 December 2023. |
| Request for exact DGI/BPS penalty amounts | Use the Código Tributario and BPS figures in Section 13; the recargo rate moves monthly, so read the current one off BPS or DGI. |
| Non-resident employee | IRNR regime (Section 2.4) — out of scope for this employer-withholding skill; route to a specialist. |
| Salary above the retirement ceiling (UYU 288,836 from February 2026; UYU 272,564 from February 2025) | Apply the ceiling to the 15%/7.5% retirement only; keep FONASA/FRL/FGCL on the full nominal, and apply the 6% uplift to the full nominal. |

## Section 8 -- Transaction / Payment Pattern Library (deterministic)

**Transaction/payment pattern library table**

| Trigger | Deterministic action |
| --- | --- |
| Nominal salary ≤ MNIG = 7 BPC (48,048 in 2026; 46,032 in 2025) | IRPF = 0. Still compute BPS (retirement 15%, FONASA per band, FRL 0.1%). |
| Nominal salary above the MNIG but ≤ 10 BPC (68,640 in 2026; 65,760 in 2025) | Compute gross IRPF bracket-by-bracket on the nominal (Section 2.1), then subtract the deduction credit (Section 2.2); IRPF due = max(0, gross IRPF − credit). |
| Nominal salary above 10 BPC | IRPF computable income = part subject to personal contributions × 1.06 (the ceiling is ignored for this step); compute gross IRPF on that figure, then subtract the deduction credit. |
| Nominal income ≤ 15 BPC (102,960 in 2026; 98,640 in 2025) | Deduction credit rate = 14%. |
| Nominal income above 15 BPC | Deduction credit rate = 8%. |
| Nominal income ≤ 2.5 BPC (17,160 in 2026; 16,440 in 2025) | FONASA employee = 3% (single) / 5% (with spouse w/o SNIS). |
| Nominal income above 2.5 BPC | FONASA employee = 4.5% / 6% / 6.5% / 8% per family situation (Section 3.2). |
| Nominal salary ≤ retirement ceiling (288,836 from February 2026; 272,564 from February 2025) | Retirement base = full nominal (15% employee, 7.5% employer). |
| Nominal salary above the ceiling | Retirement base = the ceiling; FONASA/FRL/FGCL still on full nominal. |
| Each dependent minor child | Add 11,440 in 2026 (10,960 in 2025) to the deductible-items sum; 22,880 in 2026 (21,920 in 2025) if disabled. |
| Aguinaldo / sueldo anual complementario (and the statutory salario vacacional) | BPS: materia gravada at the ordinary rates (Ley 16.713 art. 153); excluded only from the FONASA 2.5 BPC band test. IRPF: withhold at the top marginal rate reached by the month's other income, without the uplift and outside the scale; the personal contributions on it are deductible at the ajuste anual (Section 2.1). |
| Bank credit `SUELDO`/`SALARIO` to an employee | Net salary payment. |
| Bank debit to `BPS`/`DGI` | BPS contribution remittance / IRPF remittance. |

## Section 9 -- Worked Examples

All figures in UYU. Every example below is a **2025 pay period (February to December 2025)** and uses the 2025 constants: BPC = 6,576; MNIG = 46,032; 10 BPC uplift threshold = 65,760; retirement ceiling = 272,564 (February 2025 onward; January 2025 used 256,821); FONASA split 16,440; child deduction 10,960. **General private sector**. Employer withholds IRPF and BPS. Unless stated, the employee is **single, no dependents**. Each line is recomputed end-to-end.

The mechanics are identical for a 2026 period and only the constants move: BPC 6,864, MNIG 48,048, uplift threshold 68,640, ceiling 288,836 from February 2026, FONASA split 17,160, child deduction 11,440, and the band tops in Section 2.1. Do not lift a peso figure out of these examples into a 2026 payroll — rerun it on the 2026 scale.

### Example A — Minimum wage, nominal UYU 23,604/month (below MNIG)

23,604 < 46,032 → IRPF = 0. 23,604 > 16,440 → FONASA 4.5% (single).

**Example A table**  _(23,604.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 23,604.00 |
| Employee retirement | 15% × 23,604 | 3,540.60 |
| Employee FONASA | 4.5% × 23,604 | 1,062.18 |
| Employee FRL | 0.1% × 23,604 | 23.60 |
| Employee BPS total | 3,540.60 + 1,062.18 + 23.60 | 4,626.38 |
| IRPF withheld | nominal < MNIG | 0.00 |
| **Net pay** | 23,604 − 4,626.38 − 0 | **18,977.62** |
| Employer retirement | 7.5% × 23,604 | 1,770.30 |
| Employer FONASA | 5% × 23,604 | 1,180.20 |
| Employer FRL | 0.1% × 23,604 | 23.60 |
| Employer FGCL | 0.025% × 23,604 | 5.90 |
| Employer BPS total | 1,770.30 + 1,180.20 + 23.60 + 5.90 | 2,980.00 |
| **Total employer cost** | 23,604 + 2,980.00 | **26,584.00** |

### Example B — Nominal UYU 60,000/month (just into the 10% IRPF band)

60,000 in 10% band; 60,000 ≤ 65,760 → no 6% uplift; nominal ≤ 98,640 → deduction credit rate 14%. FONASA 4.5%.

**Example B table**  _(60,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 60,000.00 |
| Employee retirement | 15% × 60,000 | 9,000.00 |
| Employee FONASA | 4.5% × 60,000 | 2,700.00 |
| Employee FRL | 0.1% × 60,000 | 60.00 |
| Employee BPS total (deductible) | 9,000 + 2,700 + 60 | 11,760.00 |
| Gross IRPF on income | 10% × (60,000 − 46,032) = 10% × 13,968 | 1,396.80 |
| Deduction credit | 14% × 11,760 | 1,646.40 |
| IRPF due | max(0, 1,396.80 − 1,646.40) | 0.00 |
| **Net pay** | 60,000 − 11,760 − 0 | **48,240.00** |
| Employer BPS | 12.625% × 60,000 | 7,575.00 |
| **Total employer cost** | 60,000 + 7,575.00 | **67,575.00** |

The deduction credit (1,646.40) exceeds the gross IRPF (1,396.80), so IRPF due is 0 (no negative/refund within monthly withholding).

### Example C — Nominal UYU 120,000/month (24% band, non-zero IRPF)

120,000 > 65,760 → the IRPF computable income is 120,000 × 1.06 = 127,200, in the 24% band; nominal > 98,640 → deduction credit rate 8%. FONASA 4.5%.

**Example C table**  _(120,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 120,000.00 |
| Employee retirement | 15% × 120,000 | 18,000.00 |
| Employee FONASA | 4.5% × 120,000 | 5,400.00 |
| Employee FRL | 0.1% × 120,000 | 120.00 |
| Employee BPS total (deductible) | 18,000 + 5,400 + 120 | 23,520.00 |
| IRPF computable income (6% uplift) | 120,000 × 1.06 | 127,200.00 |
| Gross IRPF on income | 6,904.80 + 24% × (127,200 − 98,640) = 6,904.80 + 24% × 28,560 | 13,759.20 |
| Deduction credit | 8% × 23,520 | 1,881.60 |
| IRPF withheld | 13,759.20 − 1,881.60 | 11,877.60 |
| **Net pay** | 120,000 − 23,520 − 11,877.60 | **84,602.40** |
| Employer BPS | 12.625% × 120,000 | 15,150.00 |
| **Total employer cost** | 120,000 + 15,150.00 | **135,150.00** |

Without the uplift the gross IRPF would be 12,031.20 and the withholding 10,149.60; the extra 1,728.00 a month is what the December ajuste anual returns to a single-employer worker whose actual income is 120,000 every month (Decreto 148/007 art. 64; BPS Comunicado 24/2023).

### Example D — Nominal UYU 300,000/month (retirement ceiling bites; 25% band)

300,000 > 272,564 → retirement on 272,564; FONASA/FRL/FGCL on full 300,000. IRPF computable income = 300,000 × 1.06 = 318,000 (the uplift applies to the whole salary subject to personal contributions; the ceiling is ignored for this step). 25% IRPF band; credit rate 8%.

**Example D table**  _(300,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 300,000.00 |
| Retirement base (capped) | min(300,000, 272,564) | 272,564.00 |
| Employee retirement | 15% × 272,564 | 40,884.60 |
| Employee FONASA | 4.5% × 300,000 | 13,500.00 |
| Employee FRL | 0.1% × 300,000 | 300.00 |
| Employee BPS total (deductible) | 40,884.60 + 13,500 + 300 | 54,684.60 |
| IRPF computable income (6% uplift) | 300,000 × 1.06 | 318,000.00 |
| Gross IRPF on income | 30,578.40 + 25% × (318,000 − 197,280) = 30,578.40 + 25% × 120,720 | 60,758.40 |
| Deduction credit | 8% × 54,684.60 | 4,374.77 |
| IRPF withheld | 60,758.40 − 4,374.77 | 56,383.63 |
| **Net pay** | 300,000 − 54,684.60 − 56,383.63 | **188,931.77** |
| Employer retirement | 7.5% × 272,564 | 20,442.30 |
| Employer FONASA | 5% × 300,000 | 15,000.00 |
| Employer FRL | 0.1% × 300,000 | 300.00 |
| Employer FGCL | 0.025% × 300,000 | 75.00 |
| Employer BPS total | 20,442.30 + 15,000 + 300 + 75 | 35,817.30 |
| **Total employer cost** | 300,000 + 35,817.30 | **335,817.30** |

### Example E — Nominal UYU 120,000/month, single with 1 minor child

Single with children, > 2.5 BPC → FONASA 6%. One child deduction = 10,960. Computable income 127,200 (uplift). Credit rate 8% (income > 98,640).

**Example E table**  _(120,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 120,000.00 |
| Employee retirement | 15% × 120,000 | 18,000.00 |
| Employee FONASA | 6% × 120,000 | 7,200.00 |
| Employee FRL | 0.1% × 120,000 | 120.00 |
| Employee BPS total | 18,000 + 7,200 + 120 | 25,320.00 |
| Deductible-items sum | 25,320 (BPS) + 10,960 (1 child) | 36,280.00 |
| IRPF computable income (6% uplift) | 120,000 × 1.06 | 127,200.00 |
| Gross IRPF on income | 6,904.80 + 24% × (127,200 − 98,640) | 13,759.20 |
| Deduction credit | 8% × 36,280 | 2,902.40 |
| IRPF withheld | 13,759.20 − 2,902.40 | 10,856.80 |
| **Net pay** | 120,000 − 25,320 − 10,856.80 | **83,823.20** |
| Employer BPS | 12.625% × 120,000 | 15,150.00 |
| **Total employer cost** | 120,000 + 15,150.00 | **135,150.00** |

Versus Example C (same salary, no child, FONASA 4.5%): the child deduction and FONASA band change net pay from 84,602.40 to 83,823.20 — the higher FONASA (6% vs 4.5%) outweighs the extra child deduction at this income.

### Example G — June aguinaldo for the Example C employee

Aguinaldo for December 2024 to May 2025 on a constant UYU 120,000 salary = 6 × 120,000 / 12 = 60,000 (Ley 12.840: one twelfth of the remuneration of the period). BPS contributions apply at the ordinary rates; the aguinaldo does not enter the IRPF scale and bears the top marginal rate of the June salary, 24% (Example C), with no uplift.

**Example G table**  _(60,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Aguinaldo | 6 × 120,000 / 12 | 60,000.00 |
| Employee retirement | 15% × 60,000 | 9,000.00 |
| Employee FONASA | 4.5% × 60,000 | 2,700.00 |
| Employee FRL | 0.1% × 60,000 | 60.00 |
| Employee BPS total | 9,000 + 2,700 + 60 | 11,760.00 |
| IRPF withheld on the aguinaldo | 24% × 60,000 (top marginal rate of the June salary; no scale, no uplift, no monthly deduction credit) | 14,400.00 |
| **Net aguinaldo** | 60,000 − 11,760 − 14,400 | **33,840.00** |
| Employer BPS | 12.625% × 60,000 | 7,575.00 |

At the ajuste anual the 11,760.00 of contributions on the aguinaldo join the deductible items (8% × 11,760 = 940.80 of credit) and the aguinaldo is taxed at the top marginal rate of the annual scale (BPS Comunicado 24/2023 ítems 2.1 and 3.2).

### Example F — IRPF scale verification (reference)

Gross IRPF on income only (before deduction credit), at each **2025** bracket top, must match the 2025 scale in Section 2.1. The 2026 equivalents are the cumulative column of the 2026 table there:

**Example F table**

| Nominal income | Gross IRPF | Recomputation |
| --- | --- | --- |
| 65,760 | 1,972.80 | 10% × (65,760 − 46,032) |
| 98,640 | 6,904.80 | 1,972.80 + 15% × 32,880 |
| 197,280 | 30,578.40 | 6,904.80 + 24% × 98,640 |
| 328,800 | 63,458.40 | 30,578.40 + 25% × 131,520 |
| 493,200 | 107,846.40 | 63,458.40 + 27% × 164,400 |
| 756,240 | 189,388.80 | 107,846.40 + 31% × 263,040 |

(Self-verified — matches the cumulative column in Section 2.1.)

## Section 10 -- Tier 1 Rules (deterministic — apply mechanically)

- **Employer as IRPF withholding agent** — The employer IS an IRPF withholding agent on dependent salaries — withhold IRPF monthly on the progressive scale and reconcile via the ajuste anual  _(Decreto 148/007 arts. 62 to 64)_
- **BPC** — UYU 6,864/month in 2026 (Decreto N° 11/026); UYU 6,576/month in 2025  _(Decreto N° 5/025)_
- **MNIG** — 7 BPC: UYU 48,048/month in 2026, UYU 46,032/month in 2025; first peso above MNIG is taxed  _(Decreto 148/007 art. 63; BPS Comunicados R 5/2026 and R 2/2025)_
- **6% uplift** — Income above 10 BPC in the month (68,640 in 2026; 65,760 in 2025): the part subject to personal contributions × 1.06 is the IRPF computable income for the month  _(Decreto 148/007 arts. 60 and 63)_
- **Aguinaldo and salario vacacional** — Withheld at the top marginal rate of the month's other income; never entered in the scale; excluded from the 10 BPC and 15 BPC tests  _(Título 7 arts. 47 and 48; Decreto 148/007 art. 63)_

**IRPF scale (monthly)**  _(Decreto 148/007 art. 63; BPS Comunicados R 2/2025 and R 5/2026)_

| Band (BPC) | Rate | Band top, 2026 | Band top, 2025 |
| --- | --- | --- | --- |
| to 7 | 0% | 48,048 | 46,032 |
| to 10 | 10% | 68,640 | 65,760 |
| to 15 | 15% | 102,960 | 98,640 |
| to 30 | 24% | 205,920 | 197,280 |
| to 50 | 25% | 343,200 | 328,800 |
| to 75 | 27% | 514,800 | 493,200 |
| to 115 | 31% | 789,360 | 756,240 |
| above 115 | 36% | — | — |

- **IRPF due formula** — IRPF due = max(0, gross IRPF on income − deduction credit). Credit rate = 14% if nominal income (excluding aguinaldo and salario vacacional) is at or below 15 BPC (102,960 in 2026; 98,640 in 2025), else 8%  _(Decreto 148/007 art. 63 num. 2)_
- **Deductible items** — Deductible items include personal BPS contributions plus the child deduction — 11,440/child in 2026 (22,880 if disabled), 10,960 and 21,920 in 2025 — and other listed items (Section 2.2)  _(Título 7 art. 49; BPS Comunicados R 5/2026 and R 2/2025)_
- **Employee BPS rates** — retirement 15% + FONASA 3%–8% (by income band & family) + FRL 0.1%  _(Ley 16.713 art. 181; Ley 18.211 arts. 61 and 66; Ley 19.689 art. 17)_
- **Employer BPS rates (general private)** — retirement 7.5% + FONASA 5% + FRL 0.1% + FGCL 0.025% = 12.625% before BSE/CCM  _(Ley 18.083 art. 87; Ley 18.211 art. 61; Ley 19.689 art. 17; Ley 19.690 art. 10)_
- **Retirement contribution ceiling** — Retirement contributions (15% + 7.5%) apply only up to UYU 288,836/month from February 2026 and UYU 272,564/month from February 2025 (256,821 from February 2024); FONASA/FRL/FGCL on full nominal  _(Ley 16.713 art. 7; BPS Valores históricos)_
- **Minimum wage** — UYU 23,604/month from 1 Jan 2025; UYU 24,572 from 1 Jan 2026 and UYU 25,383 from 1 Jul 2026. A min-wage earner pays no IRPF but pays BPS.  _(Decreto N° 369/024; Decreto N° 319/025)_
- **Year-end ajuste anual** — Year-end: employer ajuste anual on actual income (no uplift) settles most single-employer employees; Form 1102/1103 filed only by mandatory filers  _(Decreto 148/007 art. 64; BPS Comunicado 24/2023)_
- **BPS nómina due date** — The month after the payroll month, by the BPS calendar date for the last digit of the company number (Section 4.6)  _(BPS, Vencimientos 2026)_
- **Currency requirement** — All payroll amounts in UYU — never another currency.
- **Total employee retirement withholding** — The total employee retirement withholding is 15% regardless of the BPS/AFAP split (Section 4.5).

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

These items require a licensed Uruguayan accountant's judgement and/or confirmation against primary sources before reliance.
1. **BSE workplace-accident insurance premium** (Section 4.2) — varies by activity/risk class; no single national rate.
2. **CCM (Complemento de Cuota Mutual)** (Section 4.2) — the formula and the cuota mutual value are published by BPS, but whether a given workforce triggers it depends on the mix of covered workers and their basic contributions; confirm from the BPS factura.
3. **Civil/public-organism patronal rates** — differ from the 7.5% general private-sector rate used here.
4. **AFAP allocation for workers who changed regime or hold several jobs** (Section 4.5) — the BPS levels are confirmed, but the art. 8 option and multi-employer aggregation need the worker's BPS record.
5. **Recargo por mora rate for the payment month** (Section 13) — it moves with the BCU averages; the figure here is for September and October 2026.

## Section 12 -- Filing Obligations

### 12.1 Monthly — BPS nómina + IRPF remittance

**BPS nómina table**  _(Decreto 148/007 art. 65; BPS, Vencimientos 2026)_

| Item | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| BPS **nómina** (payroll declaration) | Declare and pay employee + employer BPS shares and IRPF withheld | The month after the payroll month, by the calendar date for the last digit of the company number: 2026 dates 19/18/16/20/19/15/15/17/15/16/17/15 (digits 0 to 4) and 20/19/17/21/20/16/16/18/16/19/18/16 (digits 5 to 9) for January to December; e.g. the January 2026 nómina by 18 or 19 February (Section 4.6) | BPS, Vencimientos 2026 |

### 12.2 Annual — IRPF declaración jurada (employee's own filing, where required)

**Annual IRPF declaración jurada table**  _(Decreto 148/007 art. 64; DGI, Calendario de la Campaña 2026 de IRPF; DGI, Vencimientos 2026, ordinal 16)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **Form 1102** (individual) / **Form 1103** (family unit) | Annual IRPF sworn declaration for mandatory filers | FY2025: **29 Jun – 31 Aug 2026**, one range for all taxpayers — DGI dropped the last-digit staggering for the 2026 campaign; refunds from 28 Jul 2026; balance in up to 5 instalments on 31 Aug, 30 Sep, 30 Oct, 30 Nov and 30 Dec 2026 | DGI, "Calendario de la Campaña 2026 de IRPF"; DGI, Vencimientos 2026, ordinal 16 |

Most single-employer employees do NOT file — the employer's ajuste anual settles the year, and DGI pays automatic refunds from June (Decreto 148/007 art. 64; DGI campaign calendar).
Mandatory filers: independent workers; employees with more than one employer whose nominal labour income exceeds 150,000 UI; núcleo familiar electors and employees who asked for the 5% withholding reduction; employees not in employment on 31 December (Decreto 148/007 art. 64; DGI, Instructivo Formulario 1102).

## Section 13 -- Penalties

**Penalties table**  _(Código Tributario (Decreto-Ley 14.306) arts. 94 and 95; Decreto 274/008 as amended by Decreto 23/020; Decreto 344/025; Resolución DGI 097/026; BPS, Multas y recargos por mora; BPS, Valores actuales)_

| Penalty | Detail | Source |
| --- | --- | --- |
| Multa por mora (DGI, unpaid IRPF withholdings) | 5% of the unpaid tax if paid within five business days of the due date; 10% if paid later but within 90 calendar days; 20% after 90 days; 10% when a payment plan is requested in time | Código Tributario art. 94 |
| Recargo por mora (DGI and BPS) | Monthly surcharge, calculated day by day and capitalised every four months, set by the Executive at 110% of a 70/30 blend of the BCU's latest quarterly average lending rates for large and medium companies; BPS published 0.80% a month for September and October 2026 | Código Tributario art. 94; Decreto 274/008 art. 1; BPS Valores actuales |
| Multa por mora (BPS contributions) | Same 5% / 10% / 20% tiers, halved to 2.5% / 5% / 10% when the nómina was filed on time with a declaration of non-payment | BPS, Multas y recargos por mora |
| Contravención (late or omitted sworn returns, formal duties) | Fine within the art. 95 range, UYU 680 to UYU 13,220 for 2026; a late sworn return costs UYU 910 each (at most UYU 2,730 per filing for taxpayers with no activity in the period) | Código Tributario art. 95; Decreto 344/025; Resolución DGI 097/026 |

Defraudación (art. 96) and omisión de pago (art. 97) carry their own multiples of the tax; escalate those to a contador público.

## Section 14 -- Excel Working Paper Template

Reproduce this layout in a single worksheet (one column per employee, or one row per employee for a register). All cells in UYU. Enter the constants for the year of the pay period. **2026**: BPC 6,864; MNIG 48,048; uplift threshold 68,640; retirement ceiling 288,836 (272,564 in January); FONASA split 17,160. **2025**: BPC 6,576; MNIG 46,032; uplift threshold 65,760; ceiling 272,564 (256,821 in January); FONASA split 16,440. The formulas below carry the 2025 constants for a February-to-December 2025 period.

**Excel working paper template table**

| Row | Label | Formula / source |
| --- | --- | --- |
| 1 | Employee name | input |
| 2 | Pay period (month/year) | input |
| 3 | Nominal salary | input |
| 4 | FONASA employee rate (decimal) | input (0.03 / 0.045 / 0.05 / 0.06 / 0.065 / 0.08 per Section 3.2) |
| 5 | Dependent minor children (count) | input |
| 6 | Children with disability (count) | input |
| 7 | Retirement base (capped) | `=MIN(B3,272564)` |
| 8 | Employee retirement | `=B7*0.15` |
| 9 | Employee FONASA | `=B3*B4` |
| 10 | Employee FRL | `=B3*0.001` |
| 11 | **Employee BPS total (deductible)** | `=B8+B9+B10` |
| 12 | IRPF computable income (6% uplift above 10 BPC) | `=IF(B3>65760,B3*1.06,B3)` |
| 13 | Gross IRPF on income | progressive on B12 per Section 2.1 (see note) |
| 14 | Deductible-items sum | `=B11 + B5*10960 + B6*21920` |
| 15 | Deduction credit rate | `=IF(B3<=98640,0.14,0.08)` |
| 16 | Deduction credit | `=B14*B15` |
| 17 | **IRPF withheld** | `=MAX(0,B13-B16)` |
| 18 | **Net pay** | `=B3-B11-B17` |
| 19 | Employer retirement | `=B7*0.075` |
| 20 | Employer FONASA | `=B3*0.05` |
| 21 | Employer FRL | `=B3*0.001` |
| 22 | Employer FGCL | `=B3*0.00025` |
| 23 | **Employer BPS total** | `=B19+B20+B21+B22` |
| 24 | **Total employer cost** | `=B3+B23` |
| 25 | Monthly BPS remittance | `=B11+B23` (employee + employer BPS) |

- **Row 13 gross IRPF helper formula** — =IF(B12<=46032,0, IF(B12<=65760,(B12-46032)*0.1, IF(B12<=98640,1972.8+(B12-65760)*0.15, IF(B12<=197280,6904.8+(B12-98640)*0.24, IF(B12<=328800,30578.4+(B12-197280)*0.25, IF(B12<=493200,63458.4+(B12-328800)*0.27, IF(B12<=756240,107846.4+(B12-493200)*0.31, 189388.8+(B12-756240)*0.36)))))))
- **Aguinaldo month** — add a row for the aguinaldo with BPS at the row 8 to 10 rates and IRPF = aguinaldo × the top marginal rate reached by B12 (Example G); do not add the aguinaldo to B3.

Cross-check against Example C (nominal 120,000, FONASA 4.5%, no children): row 7 = 120,000; row 8 = 18,000; row 9 = 5,400; row 10 = 120; row 11 = 23,520; row 12 = 127,200; row 13 = 13,759.20; row 14 = 23,520; row 15 = 0.08; row 16 = 1,881.60; row 17 = 11,877.60; row 18 = 84,602.40; row 23 = 15,150; row 24 = 135,150. ✓ Matches Example C exactly.

## Section 15 -- Bank Statement / Terminology Reading Guide

Common Uruguayan payroll terms (Spanish → English) and typical bank-statement patterns. Match on the **uppercased** description.

### 15.1 Salary credits (to employees)

**Salary credits table**

| Pattern (UYU bank statement) | Classification |
| --- | --- |
| `SUELDO`, `SALARIO`, `HABERES`, `LIQUIDO` | Net salary payment (salario líquido) |
| `PAGO NOMINA`, `TRANSFERENCIA SUELDO`, `ACREDITACION SUELDO` | Net salary payment |
| `AGUINALDO`, `SUELDO ANUAL COMPLEMENTARIO`, `SAC` | Aguinaldo / 13th salary: BPS at ordinary rates, IRPF at the top marginal rate (Section 8; Example G) |
| `ADELANTO`, `ANTICIPO DE SUELDO` | Salary advance — reconcile against month-end net |
| `PARTIDA`, `PRIMA`, `INCENTIVO` | Bonus / allowance — review IRPF & BPS-base inclusion |
| `DEVOLUCION IRPF`, `AJUSTE ANUAL` | IRPF year-end refund/adjustment — not new income |

### 15.2 Employer debits to the State (BPS / DGI)

**Employer debits to the state table**

| Pattern | Classification |
| --- | --- |
| `BPS`, `BANCO DE PREVISION SOCIAL`, `APORTES BPS` | BPS contribution remittance (employee + employer shares) |
| `MONTEPIO`, `JUBILATORIO`, `APORTE PERSONAL` | Retirement contribution share |
| `FONASA` | Health-fund contribution |
| `FRL`, `FONDO DE RECONVERSION` | FRL contribution |
| `DGI`, `IRPF`, `RETENCION IRPF` | DGI / IRPF remittance |
| `BSE`, `SEGURO DE ACCIDENTES` | BSE workplace-accident premium (varies by risk class — research gap) |

### 15.3 Non-payroll / not income

**Non-payroll table**

| Pattern | Classification |
| --- | --- |
| `REINTEGRO`, `REEMBOLSO` | Reimbursement / refund — not salary |
| `VIATICOS`, `GASTOS DE VIAJE` | Travel allowance/expense — review for treatment |
| `CUOTA PRESTAMO`, `DESCUENTO PRESTAMO` | Loan deduction — not an employer cost |

## Section 16 -- Onboarding Fallback

If the user has not provided enough to run payroll, collect in this order:
1. Monthly **nominal** salary in UYU — refuse if given in USD or another currency (Section 7.2).
2. **Family / FONASA situation** — single / single with children / with spouse (own SNIS cover or not) — selects the FONASA band.
3. Number of dependent **minor children** (and any with disability) — for the IRPF deduction.
4. Employer **sector** — general private (7.5% patronal) or civil/public organism.
5. **Pay period** (month + year) — selects the constants: 2026 (BPC 6,864; MNIG 48,048; ceiling 288,836) or 2025 (BPC 6,576; MNIG 46,032; ceiling 272,564). The month matters too, because the 2026 minimum wage rises on 1 July.
6. Whether the employee has **multiple employers** or elects the family-unit regime — affects annual filing.
7. Confirm the employer is **registered with BPS**.

If any required input is missing, state what is missing and **do not** fabricate a figure.

## Section 17 -- Interaction with Other Skills

**Interaction with other skills table**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (IRPF + BPS) | **This skill (uruguay-payroll.md)** |
| Uruguay VAT (IVA) returns | uruguay-iva.md |
| Individual IRPF annual return (Form 1102/1103) | uruguay-income-tax.md (employee's own filing, where required) |
| Uruguay corporate income tax (IRAE) | uruguay-corporate-tax.md |
| Uruguay bookkeeping | uruguay-bookkeeping.md |

### Key handoff points

**Payroll → Bookkeeping:** nominal wages and the 12.625% employer BPS are expenses; the employee BPS (~19.6%) and IRPF withheld are liabilities until remitted to BPS/DGI.
**Payroll → IRPF return:** the employer's ajuste anual settles most single-employer employees; the employee files Form 1102/1103 only if a mandatory filer (Section 2.3).

### 18.1 Sources

**Sources**  _(see individual rows)_

| # | Title | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Texto Ordenado 2023 (Decreto 101/024), Título 7 — IRPF (arts. 42, 47 to 49, 51) | IMPO (DGI text) | https://www.impo.com.uy/bases/todgi-2023/7-2024 |
| 2 | Texto Ordenado 2023, Título 8 — IRNR (arts. 13 and 18) | IMPO (DGI text) | https://www.impo.com.uy/bases/todgi-2023/8-2024 |
| 3 | Decreto 148/007 — IRPF regulations (arts. 56 to 58, 60, 62 to 65, 64 bis, 77 bis) | IMPO | https://www.impo.com.uy/bases/decretos/148-2007 |
| 4 | Ley 16.713 — social security reform (arts. 7, 8, 153, 158, 181) | IMPO | https://www.impo.com.uy/bases/leyes/16713-1995 |
| 5 | Ley 18.083 art. 87 — employer pension contribution 7.5% | IMPO | https://www.impo.com.uy/bases/leyes/18083-2006 |
| 6 | Ley 18.211 arts. 61 and 66 — FONASA contributions | IMPO | https://www.impo.com.uy/bases/leyes/18211-2007 |
| 7 | Ley 19.689 art. 17 — FRL 0.10% | IMPO | https://www.impo.com.uy/bases/leyes/19689-2018/17 |
| 8 | Ley 19.690 art. 10 — FGCL 0.025% | IMPO | https://www.impo.com.uy/bases/leyes/19690-2018 |
| 9 | Ley 20.130 art. 22 — contribution levels of the Sistema Previsional Común | IMPO | https://www.impo.com.uy/bases/leyes/20130-2023 |
| 10 | Código Tributario (Decreto-Ley 14.306) arts. 94 and 95 | IMPO | https://www.impo.com.uy/bases/codigo-tributario/14306-1974/94 |
| 11 | Decreto 274/008 — recargo por mora formula; Decreto 344/025 — 2026 contravención range | IMPO | https://www.impo.com.uy/bases/decretos/274-2008 ; https://www.impo.com.uy/bases/decretos/344-2025 |
| 12 | Decreto N° 5/025 and Decreto N° 11/026 — BPC 2025 and 2026 | IMPO | https://www.impo.com.uy/bases/decretos/5-2025 ; https://www.impo.com.uy/bases/decretos/11-2026 |
| 13 | Decreto N° 369/024 and Decreto N° 319/025 — salario mínimo nacional 2025 and 2026 | IMPO | https://www.impo.com.uy/bases/decretos/369-2024 ; https://www.impo.com.uy/bases/decretos/319-2025 |
| 14 | BPS Comunicado R 2/2025 — IRPF 2025 monthly values (escalas) | Banco de Previsión Social (BPS) | https://www.bps.gub.uy/bps/file/22584/2/2025---comunicado-r-2---valores-escalas-irpf-2025.pdf |
| 15 | BPS Comunicado R 5/2026 — IRPF 2026 monthly values (escalas) | BPS | https://www.bps.gub.uy/bps/file/23860/3/2026---comunicado-r-5---valores-escalas-irpf-2026.pdf |
| 16 | BPS Comunicado 24/2023 — ajuste anual IRPF trabajadores dependientes | BPS | https://www.bps.gub.uy/bps/file/21231/1/2023---comunicado-24---ajuste-anual-irpf-2023-trabajadores-dependientes.pdf |
| 17 | BPS — Tasas (contribution rates) | BPS | https://www.bps.gub.uy/835/tasas.html |
| 18 | BPS — Tasas Fonasa | BPS | https://www.bps.gub.uy/10314/tasas-fonasa.html |
| 19 | BPS — Fondo de Reconversión Laboral (FRL); Fondo de Garantía de Créditos Laborales | BPS | https://www.bps.gub.uy/10322/fondo-reconversion-laboral-frl.html ; https://www.bps.gub.uy/15668/fondo-de-garantia-de-creditos-laborales.html |
| 20 | BPS — Valores actuales and Valores históricos (topes, niveles, cuota mutual, recargo) | BPS | https://www.bps.gub.uy/5478/valores-actuales.html ; https://www.bps.gub.uy/5479/valores-historicos.html |
| 21 | BPS — Vencimientos 2026 (nómina and payment calendar); Multas y recargos por mora | BPS | https://www.bps.gub.uy/24165/vencimientos-de-monotributo.html ; https://www.bps.gub.uy/18132/multas-y-recargos-por-mora.html |
| 22 | DGI — IRPF Categoría 2 escalas y alícuotas | DGI (gub.uy) | https://www.gub.uy/direccion-general-impositiva/politicas-y-gestion/irpf-categoria-2-escalas-alicuotas |
| 23 | DGI — Calendario de la Campaña 2026 de IRPF; Vencimientos 2026 calendario general | DGI (gub.uy) | https://www.gub.uy/direccion-general-impositiva/comunicacion/noticias/calendario-campana-2026-irpf ; https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/vencimientos-2025-calendario-general-actualizado |
| 24 | DGI — Sanciones 2026 (contravención por presentación fuera de plazo; multa por contravención) | DGI (gub.uy) | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/sanciones-2 |
| 25 | IRPF — vencimiento declaración jurada 2025 | EY Uruguay | https://www.ey.com/es_uy/newsroom/2025/05/irpf-vencimiento-para-la-presentacion-de-la-declaracion-jurada-en-2025 |

### 18.2 Test Suite (numbered — recompute to confirm any change)

**Test Suite**  _(see individual rows)_

| # | Input | Expected output | Recomputation |
| --- | --- | --- | --- |
| 1 | Min wage, nominal 23,604, single | IRPF 0; net 18,977.62; employer cost 26,584.00 | Ex. A — employee BPS 4,626.38; employer BPS 2,980.00 |
| 2 | Nominal 60,000, single | IRPF 0 (credit > gross); net 48,240.00; employer cost 67,575.00 | Ex. B — gross IRPF 1,396.80 < credit 1,646.40 |
| 3 | Nominal 120,000, single | IRPF 11,877.60; net 84,602.40; employer cost 135,150.00 | Ex. C — computable 127,200; gross IRPF 13,759.20; credit 1,881.60 |
| 4 | Nominal 300,000, single (ceiling) | IRPF 56,383.63; net 188,931.77; employer cost 335,817.30 | Ex. D — retirement on 272,564; computable 318,000; gross IRPF 60,758.40 |
| 5 | Nominal 120,000, single + 1 child | IRPF 10,856.80; net 83,823.20; employer cost 135,150.00 | Ex. E — FONASA 6%; child deduction 10,960 |
| 6 | IRPF scale cumulative | 1,972.80 / 6,904.80 / 30,578.40 / 63,458.40 / 107,846.40 / 189,388.80 | Ex. F — bracket tops match Section 2.1 |
| 7 | Employer total rate | 12.625% (7.5 + 5 + 0.1 + 0.025) | Section 4.2 |
| 8 | Employee total rate (single, >2.5 BPC, below ceiling) | 19.6% (15 + 4.5 + 0.1) | Section 3.4 |
| 9 | Monthly BPS remittance, nominal 120,000 (Ex. C) | 23,520 + 15,150 = 38,670 | Template row 25 |
| 10 | Deadlines | BPS nómina by the calendar date of the following month (January 2026 nómina by 18 or 19 February); IRPF DJ 1102/1103 29 Jun–31 Aug 2026 (mandatory filers only) | Section 12 |
| 11 | Below MNIG (≤ 48,048 in 2026; ≤ 46,032 in 2025) | IRPF = 0, BPS still due | Tier 1 rule 2; Ex. A |
| 12 | Above retirement ceiling (> 288,836 from February 2026; > 272,564 from February 2025) | Retirement capped; FONASA/FRL/FGCL on full nominal; uplift on the full nominal | Tier 1 rule 10; Ex. D |
| 13 | Uplift threshold: nominal 65,760 versus 65,761 (2025) | 65,760 enters the scale as 65,760; 65,761 enters as 65,761 × 1.06 = 69,706.66 | Section 2.1; Decreto 148/007 art. 63 |
| 14 | June aguinaldo 60,000 for the Ex. C employee | BPS 11,760.00; IRPF 24% × 60,000 = 14,400.00; net aguinaldo 33,840.00; employer BPS 7,575.00 | Ex. G |

## PROHIBITIONS

- **Never skip IRPF withholding** — NEVER skip IRPF withholding — Uruguay's employer IS an IRPF withholding agent on dependent salaries; compute monthly IRPF and the year-end ajuste anual.  _(PROHIBITIONS section)_
- **Never compute payroll in non-UYU currency** — NEVER compute Uruguayan payroll in USD or any non-UYU currency — refuse and ask for the UYU nominal salary.  _(PROHIBITIONS section)_
- **Never apply IRPF as flat rate** — NEVER apply IRPF as a flat rate — it is progressive bracket-by-bracket (Section 2.1).  _(PROHIBITIONS section)_
- **Never skip the 6% uplift** — NEVER withhold on the bare nominal when the month's income exceeds 10 BPC; the computable income is the part subject to personal contributions × 1.06 (Decreto 148/007 art. 63). Equally, never carry the uplift into the ajuste anual or the annual return.  _(PROHIBITIONS section)_
- **Never run the aguinaldo through the scale** — NEVER enter the aguinaldo or the statutory salario vacacional into the progressive scale or the 10 BPC and 15 BPC tests; withhold on them at the top marginal rate of the month's other income (Título 7 arts. 47 and 48).  _(PROHIBITIONS section)_
- **Never forget deduction credit** — NEVER forget the deduction credit (14% / 8%) — IRPF due = max(0, gross IRPF − credit), and it can drive IRPF to zero.  _(PROHIBITIONS section)_
- **Never apply retirement contributions above ceiling** — NEVER apply retirement contributions (15% / 7.5%) above the ceiling for the pay month (UYU 288,836 from February 2026; UYU 272,564 from February 2025 to January 2026), and never cap FONASA/FRL/FGCL — those apply to the full nominal salary.  _(PROHIBITIONS section)_
- **Never assume FONASA employee rate** — NEVER assume the FONASA employee rate — it varies 3%–8% by income band and family situation; ask if unknown.  _(PROHIBITIONS section)_
- **Never tax minimum-wage earner under IRPF** — NEVER tax a minimum-wage earner under IRPF; the minimum wage is far below the MNIG in both years (25,383 against 48,048 in 2026; 23,604 against 46,032 in 2025). Always still compute BPS.  _(PROHIBITIONS section)_
- **Never let the AFAP split change the withholding** — NEVER vary the 15% employee or 7.5% employer retirement contribution by the BPS/AFAP allocation; the levels in Section 4.5 only route the money.  _(PROHIBITIONS section)_
- **Never invent a BSE premium or a recargo rate** — NEVER state a BSE accident premium (it varies by risk class) or a recargo por mora rate for a month you have not read off BPS or DGI.  _(PROHIBITIONS section)_
- **Never mix years** — NEVER run a pay period on another year's constants. The 2026 values are published: BPC 6,864 (Decreto N° 11/026), MNIG 48,048, uplift threshold 68,640, retirement ceiling 288,836 from February, minimum wage 24,572 to 30 June and 25,383 from 1 July (Decreto N° 319/025). Applying the 2025 set to a 2026 period understates the MNIG and every band top by 4.38% and overstates the tax.  _(PROHIBITIONS section)_
- **Never present computations as definitive** — NEVER present payroll computations as definitive — label them estimated and direct the user to a licensed Uruguayan accountant (contador público).  _(PROHIBITIONS section)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Uruguay) before implementation. This is a Tier 2 (research-verified) skill: figures are sourced to the statutes and decrees published by IMPO and to BPS and DGI publications (EY Uruguay for the 2025 filing campaign) but have not yet been verified section-by-section by a licensed Uruguayan accountant, and items marked "[RESEARCH GAP — reviewer to confirm]" carry residual uncertainty.

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
