---
name: uruguay-social-contributions
description: "Use this skill whenever asked about Uruguay social-security (BPS) contributions for employed persons. Trigger on phrases like \"BPS contributions\", \"BPS Uruguay\", \"Banco de Previsión Social\", \"aporte jubilatorio\", \"montepío\", \"15% BPS\", \"7.5% patronal\", \"FONASA Uruguay\", \"FONASA rate\", \"FRL\", \"Fondo de Reconversión Laboral\", \"FGCL\", \"social security Uruguay\", \"aportes a la seguridad social\", \"employer contribution Uruguay\", \"tope de cotización\", \"retirement contribution ceiling\", \"how much BPS do I pay\", \"Uruguay social contributions calculation\", \"Formulario 1102 BPS\", or any question about computing the BPS social-security burden (employee and employer shares) for Uruguay-based employees. CRITICAL STRUCTURAL FACT: BPS social contributions (jubilatorio/montepío, FONASA, FRL, FGCL) are SEPARATE from IRPF. IRPF (Impuesto a la Renta de las Personas Físicas, Categoría II) is a distinct DGI progressive income tax expressed in BPC units — it is NOT a social contribution. This skill computes ONLY the BPS contribution layer; IRPF withholding lives in the uruguay-payroll / uruguay-income-tax skills. This skill covers the jubilatorio/montepío rates, the FONASA health matrix (3%–8% by income and dependants), FRL, FGCL, the retirement contribution ceiling, the minimum wage, classification of BPS-related bank transactions, and the boundary with IRPF. ALWAYS read this skill before computing any Uruguay social contribution."
version: 0.2
jurisdiction: UY
tax_year: 2025
tax_year_notes: "2025 (2026 BPC, FONASA split, retirement ceiling and minimum wage stated alongside)"
last_updated: 2026-10-10
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uruguay Social Contributions (BPS) Skill v0.2 (Tier 2 — research-verified, reviewer sign-off pending)

> **The retirement contribution ceiling changes in February, not January.** BPS's historical values table ("Topes Art. 7º y 8º (Ley 16713) - C") gives UYU 288,836 from February 2026, UYU 272,564 from February 2025 and UYU 256,821 from February 2024, while the BPC moves on 1 January. A January 2026 pay period caps retirement contributions at UYU 272,564 and a January 2025 period at UYU 256,821. Read the ceiling for the pay month off BPS's values table before using any retirement calculation or template below.

> **Edited 2026-10-10 (v0.2).** Citations moved from PwC Worldwide Tax Summaries to the statutes (Ley 16.713, Ley 18.083, Ley 18.211, Ley 19.689, Ley 19.690, Ley 20.130, the Código Tributario, Texto Ordenado 2023 Título 7 and Decreto 148/007) and to BPS and DGI publications. The AFAP allocation levels, the socio vitalicio FONASA rates, the aguinaldo treatment, the CCM formula, the BPS payment calendar and the BPS mora fines and surcharge are filled in from BPS pages and the laws; the ceiling's February vigencia is recorded.

> **Tier 2 status.** Every rate, threshold, and value below is sourced to a statute or decree (Ley 16.713 and later laws, the Código Tributario, Texto Ordenado 2023 and Decreto 148/007, published by IMPO) or to a BPS or DGI publication and cited inline. It has **not** yet been section-by-section verified by a licensed Uruguayan accountant (contador público). Items marked **[RESEARCH GAP — reviewer to confirm]** carry residual uncertainty and must be confirmed against primary sources before reliance.

> **READ THIS FIRST — the single most important structural fact.** This skill computes **BPS social-security contributions only** — the retirement (jubilatorio/montepío), health (FONASA), labour-reconversion (FRL), and labour-credit-guarantee (FGCL) layers. **IRPF (Impuesto a la Renta de las Personas Físicas, Categoría II — rentas de trabajo) is a SEPARATE tax**, administered by **DGI** (not BPS), levied progressively (0%–36%) and expressed in **BPC units**. Do **not** treat IRPF as a social contribution, and do not bundle the two layers into one rate. Almost every Uruguayan threshold is expressed in units of the **BPC** (Base de Prestaciones y Contribuciones): **BPC = UYU 6,864/month for 2026** (Decreto N° 11/026) and **UYU 6,576/month for 2025** (Decreto N° 5/025; BPS Comunicado R 2/2025). Use one BPC value **consistently** within a computation, and take it from the year of the pay period. See Section 1 and the BPC integrity note below.

> **BPC integrity note (resolving the "115 BPC" confusion).** A prior version of this file conflated the IRPF bracket boundary **115 BPC** with a general monthly contribution threshold, producing a self-contradiction. There is no contradiction: 115 BPC is the top of the IRPF 31% bracket (start of 36%) — **UYU 789,360/month in 2026** and **UYU 756,240/month in 2025**. It is an **IRPF** boundary, not a BPS contribution threshold. The only BPS thresholds that matter in this skill are the **FONASA 2.5 BPC band split** (UYU 17,160 in 2026, UYU 16,440 in 2025) and the **retirement ceiling** (UYU 288,836 from February 2026, UYU 272,564 from February 2025). Note that the ceiling is *not* a BPC multiple — it is the indexed top of the second level of Ley 16.713 art. 7, published by BPS — so it is the one figure here you cannot derive from the BPC.

## Section 1 — Quick Reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Uruguay (Oriental Republic of Uruguay) |
| Currency | **peso uruguayo — $U / UYU** only |
| Social-security authority | **BPS** — Banco de Previsión Social (collects social contributions) |
| Income-tax authority (separate) | **DGI** — Dirección General Impositiva (administers IRPF) |
| Primary scheme | BPS — Industria y Comercio (general private sector) |
| Reference unit | **BPC = UYU 6,864/month** for 2026 (Decreto N° 11/026); **UYU 6,576/month** for 2025 (Decreto N° 5/025; BPS Comunicado R 2/2025) |
| Employee retirement (jubilatorio / montepío) | **15%** of nominal salary, up to the retirement ceiling (Ley 16.713 art. 181; BPS Tasas) |
| Employer retirement (patronal) | **7.5%** of nominal salary, up to the retirement ceiling (Ley 18.083 art. 87; BPS Tasas) |
| Employee FONASA (health) | **3% / 4.5% / 5% / 6% / 6.5% / 8%** by income band & family situation (Ley 18.211 arts. 61 and 66; BPS Tasas Fonasa) |
| Employer FONASA | **5%** of remuneration subject to montepío (+ CCM where applicable) (Ley 18.211 art. 61; BPS Tasas Fonasa) |
| Employee FRL (Fondo de Reconversión Laboral) | **0.1%** of nominal salary (Ley 19.689 art. 17; BPS FRL page) |
| Employer FRL | **0.1%** of nominal salary (Ley 19.689 art. 17; BPS FRL page) |
| Employer FGCL (labour-credit guarantee) | **0.025%** of nominal salary (employer only) (Ley 19.690 art. 10; BPS FGCL page) |
| **Employer total** | **12.625%** (7.5 + 5 + 0.1 + 0.025) before BSE/CCM (sum of the statutory rates) |
| FONASA band split | **2.5 BPC** = UYU 17,160/month in 2026; UYU 16,440/month in 2025, on the month's remuneration excluding the aguinaldo (Ley 18.211 art. 61; BPS Tasas Fonasa) |
| Retirement contribution ceiling | **UYU 288,836/month** from February 2026; **UYU 272,564/month** from February 2025 to January 2026; UYU 256,821 from February 2024. The indexed top of the second level of Ley 16.713 art. 7, not a BPC multiple: it rose 5.97% in February 2026 against the BPC's 4.38% in January, so read it off BPS's values table (Ley 16.713 art. 7; BPS Valores actuales and Valores históricos) |
| Minimum wage | **UYU 25,383/month** from 1 Jul 2026 (+3.3%); **UYU 24,572/month** from 1 Jan 2026 (+4.1%, Decreto N° 319/025); **UYU 23,604/month** from 1 Jan 2025 (+6%, Decreto N° 369/024). The 2026 rise came in two steps, so the figure changes mid-year (IMPO) |
| IRPF (separate DGI tax) | Progressive 0%–36% in BPC units — **NOT a social contribution** (Section 7) |
| Monthly filing | BPS **nómina** (declaración nominada) and payment by the BPS calendar date of the following month, keyed to the last digit of the company number (BPS, Vencimientos 2026; Section 12) |
| Validated by | Pending — requires sign-off by a licensed Uruguayan accountant (contador público) |
| Skill version | 0.2 (Tier 2) |

**Contribution overview (Industria y Comercio / general private sector)**

| Component | Employee | Employer | Base |
| --- | --- | --- | --- |
| Jubilatorio / montepío (retirement) | **15%** | **7.5%** | Nominal salary up to the ceiling (UYU 288,836 from February 2026; UYU 272,564 from February 2025) |
| FONASA (health) | **3%–8%** (matrix, Section 3) | **5%** (+ CCM) | Full nominal salary |
| FRL (Fondo de Reconversión Laboral) | **0.1%** | **0.1%** | Full nominal salary |
| FGCL (Fondo de Garantía de Créditos Laborales) | 0% | **0.025%** | Full nominal salary |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Family / FONASA situation unknown | Assume **single, no dependents**; flag the assumption |
| Sector unknown | Assume **general private sector (Industria y Comercio)** — employer retirement 7.5% |
| Salary stated in USD or other currency | **STOP** — refuse; ask for the UYU nominal amount |
| Pay period in 2027 or later | Apply the **2026** values (BPC 6,864; ceiling 288,836) and flag that they are last year's, until the 2027 BPC decree and BPS values table are published; do not invent them |
| Asked about IRPF | IRPF is a **separate DGI tax** (Section 7) — do not fold it into the BPS rate |
| Salary above the retirement ceiling | Cap retirement (15%/7.5%) at the ceiling for the pay month (288,836 from February 2026; 272,564 from February 2025 to January 2026); keep FONASA/FRL/FGCL on full nominal |
| AFAP split of the 15% retirement requested | State total 15% and the BPS/AFAP allocation by the BPS levels for the worker's regime (Section 4.5); ask whether the worker's first job began before or from 1 December 2023 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — monthly **nominal** salary in **UYU**, and the employee's **FONASA family situation** (single / single with children / with spouse without own SNIS cover / with spouse + children). Without these, STOP.

**Recommended** — employer sector (general private vs civil/public organism), pay period (month/year, to confirm FY2025 constants), and number of dependents (for the FONASA band only — child *IRPF* deductions are out of scope here).

**Ideal** — BPS nómina (Formulario 1102), payslip showing the nominal salary and each contribution line, and confirmation of the employer's BPS registration.

### Refusal catalogue

- **R-UY-BPS-1 — Currency not UYU** — Trigger: salary stated in USD or any non-UYU currency. Message: "Uruguay social contributions are computed on the UYU nominal salary. Provide the UYU nominal amount (or the FX basis used). Cannot proceed in another currency."
- **R-UY-BPS-2 — FONASA family situation unknown** — Trigger: family/dependant status not provided. Message: "The employee FONASA rate ranges 3%–8% depending on income band and family situation. Defaulting to single / no dependents and flagging the assumption — confirm before reliance."
- **R-UY-BPS-3 — IRPF treated as a contribution** — Trigger: user asks to bundle IRPF into the BPS rate or treats IRPF as social security. Message: "IRPF is a separate DGI income tax (progressive 0%–36% in BPC units), not a BPS social contribution. This skill computes BPS only. Route IRPF withholding to the uruguay-payroll / uruguay-income-tax skill."
- **R-UY-BPS-4 — AFAP allocation for an unusual record** — Trigger: user asks for the split of the 15% retirement between BPS and the private AFAP for a worker with several employers, an art. 8 option or a regime change. Message: "The total employee retirement withholding is 15%. The BPS/AFAP allocation follows the BPS levels in Section 4.5 (UYU 96,279 / 144,418 / 288,836 from February 2026), but a worker's option under Ley 16.713 art. 8, a multi-employer aggregation or a change of regime needs the worker's BPS record. Escalate to a licensed Uruguayan accountant."
- **R-UY-BPS-5 — Civil/public-organism patronal rate** — Trigger: employer is a civil or public organism. Message: "Civil/public-organism patronal rates differ from the 7.5% general private-sector rate. Confirm the applicable patronal rate before computing; do not apply 7.5% blindly."
- **R-UY-BPS-6 — Recargo for a specific month** — Trigger: request for the exact surcharge on a late BPS payment. Message: "The mora fine tiers are fixed by the Código Tributario (Section 14 of this guide gives them), but the monthly recargo moves with the BCU averages and is capitalised every four months. Read the rate for the payment month off BPS's values page or its simulator before quoting a total."

## Section 3 — FONASA employee rate matrix

Employee FONASA is **3%–8%**, selected by income band and family situation. The band split is **2.5 BPC**: UYU 17,160/month in 2026 (2.5 × 6,864) and UYU 16,440/month in 2025 (2.5 × 6,576), tested on all remuneration subject to contributions in the month with the aguinaldo excluded. The 3%, 4.5% and 6% rates are in Ley 18.211 art. 61 and the 2% spouse or partner surcharge in art. 66. (Sources: Ley 18.211 arts. 61 and 66; BPS Tasas Fonasa.)

**FONASA employee rate matrix**  _(Ley 18.211 arts. 61 and 66; BPS Tasas Fonasa)_

| Monthly income | Single, no children | Single, with children | With spouse*, no children | With spouse*, with children |
| --- | --- | --- | --- | --- |
| ≤ 2.5 BPC (≤ UYU 17,160 in 2026; ≤ UYU 16,440 in 2025) | **3%** | **3%** | **5%** | **5%** |
| > 2.5 BPC (> UYU 17,160 in 2026; > UYU 16,440 in 2025) | **4.5%** | **6%** | **6.5%** | **8%** |

\* The spouse rates apply **only** when the spouse does **not** have independent SNIS coverage. "Socios vitalicios" (life members) of a mutual-aid institution pay no 3% basic contribution and only the additions: **0%** single without children, **3%** with children, **2%** with a spouse or partner without children, **5%** with both (BPS Tasas Fonasa).

- FONASA is **NOT** subject to the retirement ceiling — it applies to the **full** nominal salary (Ley 18.211 art. 61; BPS).
- **Band-split check:** 2.5 × 6,864 = **17,160** and 2.5 × 6,576 = **16,440** ✓ (Self-verified.)

## Section 4 — Contribution rates (Industria y Comercio / general private sector)

(Sources: Ley 16.713 arts. 153 and 181; Ley 18.083 art. 87; Ley 18.211 arts. 61 and 66; Ley 19.689 art. 17; Ley 19.690 art. 10; BPS Tasas; BPS Tasas Fonasa; BPS FRL and FGCL pages.)

### 4.1 Employee shares

**Employee shares table**  _(Ley 16.713 art. 181; Ley 18.211 arts. 61 and 66; Ley 19.689 art. 17)_

| Component | Employee rate | Base | Source |
| --- | --- | --- | --- |
| Jubilatorio / montepío (retirement) | **15%** | Nominal salary up to ceiling (Section 4.4) | Ley 16.713 art. 181; BPS Tasas |
| FONASA (health) | **3% / 4.5% / 5% / 6% / 6.5% / 8%** (Section 3) | Full nominal salary | Ley 18.211 arts. 61 and 66; BPS Tasas Fonasa |
| FRL | **0.1%** (0.125% until 31 December 2018) | Full nominal salary | Ley 19.689 art. 17; BPS FRL page |

**Illustrative employee total (single, no dependents, > 2.5 BPC, below ceiling):** 15 + 4.5 + 0.1 = **19.6%**. *Check:* 15 + 4.5 + 0.1 = **19.6** ✓ (Self-verified.) This total moves with the FONASA band/family situation.

### 4.2 Employer shares

**Employer shares table**  _(Ley 18.083 art. 87; Ley 18.211 art. 61; Ley 19.689 art. 17; Ley 19.690 art. 10)_

| Component | Employer rate | Base | Source |
| --- | --- | --- | --- |
| Jubilatorio / montepío (patronal) | **7.5%** | Nominal salary up to ceiling (Section 4.4) | Ley 18.083 art. 87 (generic rate from 1 July 2007); BPS Tasas |
| FONASA | **5%** (+ CCM where applicable) | Remuneration subject to montepío | Ley 18.211 art. 61; BPS Tasas Fonasa |
| FRL | **0.1%** | Full nominal salary | Ley 19.689 art. 17 |
| FGCL (Fondo de Garantía de Créditos Laborales) | **0.025%** | Full nominal salary (materia gravada of Ley 16.713 art. 153) | Ley 19.690 art. 10; BPS FGCL page (employer-only, from 1 January 2019) |

**Employer total:** 7.5 + 5 + 0.1 + 0.025 = **12.625%**, before BSE accident insurance and CCM. *Check:* 7.5 + 5 + 0.1 + 0.025 = **12.625** ✓ (Self-verified.)

> Civil/public organisms use different patronal rates (Ley 18.083 art. 87 leaves the aportación civil outside the unified rate); this skill applies the **general private-sector 7.5%** unless told otherwise (R-UY-BPS-5). Effective employer cost rises with the **CCM (Complemento de Cuota Mutual)**, which BPS computes as (number of covered workers × cuota mutual) − (3% basic personal contributions + 5% employer contributions), with the cuota mutual at UYU 1,880 in September and October 2026 (BPS Tasas Fonasa; BPS Valores actuales), and with the activity-specific **BSE (Banco de Seguros del Estado) workplace-accident premium** (mandatory, rate varies by risk class — **[RESEARCH GAP — reviewer to confirm]**, no single national rate).

### 4.3 Combined headline burden

**Combined headline burden table**

| Side | Components | Total |
| --- | --- | --- |
| Employee (single, > 2.5 BPC, below ceiling) | 15% + 4.5% + 0.1% | **19.6%** |
| Employer (general private sector) | 7.5% + 5% + 0.1% + 0.025% | **12.625%** |

*Check:* employee 15 + 4.5 + 0.1 = 19.6 ✓; employer 7.5 + 5 + 0.1 + 0.025 = 12.625 ✓ (Self-verified.)

### 4.4 Retirement contribution ceiling (tope de cotización)

**Retirement ceiling table**  _(Ley 16.713 art. 7; BPS, Valores actuales and Valores históricos, "Topes Art. 7º y 8º (Ley 16713) - C")_

| Item | Detail | Source |
| --- | --- | --- |
| Retirement ceiling | Retirement contributions (employee **15%** and employer **7.5%**) apply **only up to UYU 288,836/month from February 2026**, **UYU 272,564/month from February 2025 to January 2026** and UYU 256,821/month from February 2024 to January 2025; salary above the cap is exempt from retirement contribution | Ley 16.713 art. 7; BPS Valores históricos |
| FONASA / FRL / FGCL | **NOT** subject to the retirement cap — apply to the **full** nominal salary | Ley 18.211 art. 61; Ley 19.689 art. 17; Ley 19.690 art. 10 |

### 4.5 AFAP (private pension pillar)

The 15% employee retirement contribution is split between BPS's solidarity pillar and the worker's **AFAP** by income levels that BPS indexes together with the ceiling (values from February 2026: level A UYU 96,279, level B UYU 144,418, level C UYU 288,836; BPS Valores actuales). For affiliates of the Ley 16.713 mixed regime (first job before 1 December 2023), contributions on income up to level A go to BPS, or half of them to the AFAP under the art. 8 option, and contributions on income between level A and the ceiling go to the AFAP; level B governs the art. 8 option for incomes between A and B (Ley 16.713 arts. 7 and 8). For people whose first job began on or after 1 December 2023 (Sistema Previsional Común), 10% of income up to UYU 144,418 goes to BPS while 5% of that tranche and 15% of income between UYU 144,418 and 288,836 go to the AFAP (Ley 20.130 art. 22; BPS "Niveles Art. 22 (ley 20.130)"). The **total** 15% employee retirement withholding and the employer's 7.5% are unaffected — only the routing changes.

## Section 5 — Payment / bank-statement pattern library (deterministic)

Apply these rules mechanically when classifying BPS-related transactions. Match by case-insensitive substring on the uppercased description. BPS contributions are **statutory obligations**, not business supplies — always EXCLUDE from any IVA (VAT) return. All amounts in UYU.

### 5.1 BPS contribution remittances (employer → State)

**BPS contribution remittances table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| `BPS`, `BANCO DE PREVISION SOCIAL`, `APORTES BPS` | EXCLUDE — BPS remittance | Employee + employer shares, monthly nómina |
| `MONTEPIO`, `JUBILATORIO`, `APORTE PERSONAL` | EXCLUDE — retirement share | Part of the BPS nómina |
| `FONASA` | EXCLUDE — health-fund contribution | Subject to no retirement ceiling |
| `FRL`, `FONDO DE RECONVERSION` | EXCLUDE — FRL contribution | — |
| `FGCL`, `GARANTIA DE CREDITOS LABORALES` | EXCLUDE — FGCL (employer only) | — |
| `FORMULARIO 1102`, `NOMINA BPS` | EXCLUDE — BPS payroll declaration/payment | — |

### 5.2 IRPF / DGI payments (NOT BPS — do not confuse)

**IRPF / DGI payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| `DGI`, `DIRECCION GENERAL IMPOSITIVA` | EXCLUDE — DGI tax, NOT BPS | Separate authority |
| `IRPF`, `RETENCION IRPF` | EXCLUDE — income tax, NOT a social contribution | Section 7 |
| `IRAE`, `IVA`, `IMESI` | EXCLUDE — other DGI taxes | Not social security |

### 5.3 BSE workplace-accident premium

**BSE workplace-accident premium table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| `BSE`, `BANCO DE SEGUROS`, `SEGURO DE ACCIDENTES` | EXCLUDE — BSE premium | Mandatory; rate varies by risk class — research gap (Section 4.2) |

### 5.4 Salary credits (to employees — not a contribution)

**Salary credits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| `SUELDO`, `SALARIO`, `HABERES`, `LIQUIDO` | EXCLUDE — net salary payment | Not a BPS contribution |
| `PAGO NOMINA`, `ACREDITACION SUELDO` | EXCLUDE — net salary payment | Not a BPS contribution |
| `AGUINALDO`, `SAC` | EXCLUDE — 13th salary | Materia gravada: BPS contributions apply at the ordinary rates (Ley 16.713 art. 153); only the FONASA 2.5 BPC band test ignores it (BPS Tasas Fonasa). IRPF on it is a payroll-guide matter |

### 5.5 Benefits received from BPS (not contributions paid)

**Benefits received from BPS table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| `BPS PENSION`, `JUBILACION`, `PENSION` (incoming) | EXCLUDE — benefit received | Not a contribution paid |
| `SUBSIDIO`, `ASIGNACION FAMILIAR` (incoming) | EXCLUDE — benefit received | Not a contribution paid |

## Section 6 — Worked examples

All figures in UYU. Every example below is a **2025 pay period (February to December 2025)**, **general private sector (Industria y Comercio)**, on the 2025 constants: BPC = 6,576; FONASA band split = 16,440; retirement ceiling = 272,564 (January 2025 used 256,821). Unless stated, the employee is **single, no dependents**. Each line reconciles to the cent. **These examples compute the BPS layer only — IRPF (Section 7) is excluded by design.**

The rates are the same for a 2026 period and only the thresholds move: FONASA band split 17,160, retirement ceiling 288,836 from February 2026 (272,564 in January). Rerun the comparison rather than reusing a peso figure from below.

### Example A — Minimum wage, nominal UYU 23,604/month

23,604 > 16,440 → FONASA 4.5% (single). Below the retirement ceiling.

**Example A table**

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 23,604.00 |
| Employee retirement | 15% × 23,604 | 3,540.60 |
| Employee FONASA | 4.5% × 23,604 | 1,062.18 |
| Employee FRL | 0.1% × 23,604 | 23.60 |
| **Employee BPS total** | 3,540.60 + 1,062.18 + 23.60 | **4,626.38** |
| **Net of BPS** | 23,604 − 4,626.38 | **18,977.62** |
| Employer retirement | 7.5% × 23,604 | 1,770.30 |
| Employer FONASA | 5% × 23,604 | 1,180.20 |
| Employer FRL | 0.1% × 23,604 | 23.60 |
| Employer FGCL | 0.025% × 23,604 | 5.90 |
| **Employer BPS total** | 1,770.30 + 1,180.20 + 23.60 + 5.90 | **2,980.00** |
| **Total employer cost** | 23,604 + 2,980.00 | **26,584.00** |
| **Total BPS remittance** | 4,626.38 + 2,980.00 | **7,606.38** |

### Example B — Below the FONASA band split, nominal UYU 15,000/month

15,000 ≤ 16,440 → FONASA 3% (single).

**Example B table**

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 15,000.00 |
| Employee retirement | 15% × 15,000 | 2,250.00 |
| Employee FONASA | 3% × 15,000 | 450.00 |
| Employee FRL | 0.1% × 15,000 | 15.00 |
| **Employee BPS total** | 2,250 + 450 + 15 | **2,715.00** |
| **Net of BPS** | 15,000 − 2,715 | **12,285.00** |
| Employer retirement | 7.5% × 15,000 | 1,125.00 |
| Employer FONASA | 5% × 15,000 | 750.00 |
| Employer FRL | 0.1% × 15,000 | 15.00 |
| Employer FGCL | 0.025% × 15,000 | 3.75 |
| **Employer BPS total** | 1,125 + 750 + 15 + 3.75 | **1,893.75** |
| **Total employer cost** | 15,000 + 1,893.75 | **16,893.75** |

### Example C — Mid-range, nominal UYU 120,000/month, single no dependents

120,000 > 16,440 → FONASA 4.5%. Below the retirement ceiling.

**Example C table**

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 120,000.00 |
| Employee retirement | 15% × 120,000 | 18,000.00 |
| Employee FONASA | 4.5% × 120,000 | 5,400.00 |
| Employee FRL | 0.1% × 120,000 | 120.00 |
| **Employee BPS total** | 18,000 + 5,400 + 120 | **23,520.00** |
| **Net of BPS** | 120,000 − 23,520 | **96,480.00** |
| Employer BPS total | 12.625% × 120,000 | 15,150.00 |
| **Total employer cost** | 120,000 + 15,150 | **135,150.00** |
| **Total BPS remittance** | 23,520 + 15,150 | **38,670.00** |

*Employer cross-check:* 7.5% × 120,000 = 9,000; 5% × 120,000 = 6,000; 0.1% × 120,000 = 120; 0.025% × 120,000 = 30 → 9,000 + 6,000 + 120 + 30 = **15,150.00** ✓

### Example D — Nominal UYU 120,000/month, single with 1 minor child

Single with children, > 2.5 BPC → FONASA **6%**. (Child *IRPF* deductions are out of scope — this is the BPS layer only.)

**Example D table**

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 120,000.00 |
| Employee retirement | 15% × 120,000 | 18,000.00 |
| Employee FONASA | 6% × 120,000 | 7,200.00 |
| Employee FRL | 0.1% × 120,000 | 120.00 |
| **Employee BPS total** | 18,000 + 7,200 + 120 | **25,320.00** |
| **Net of BPS** | 120,000 − 25,320 | **94,680.00** |
| Employer BPS total | 12.625% × 120,000 | 15,150.00 |
| **Total employer cost** | 120,000 + 15,150 | **135,150.00** |

> Versus Example C (same salary, FONASA 4.5%): the higher FONASA band (6% vs 4.5%) raises the employee BPS by 1.5% × 120,000 = 1,800, reducing net-of-BPS from 96,480.00 to 94,680.00. The employer side is unchanged.

### Example E — Above the retirement ceiling, nominal UYU 300,000/month

300,000 > 272,564 → retirement on 272,564; FONASA/FRL/FGCL on full 300,000. FONASA 4.5% (single).

**Example E table**

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 300,000.00 |
| Retirement base (capped) | min(300,000, 272,564) | 272,564.00 |
| Employee retirement | 15% × 272,564 | 40,884.60 |
| Employee FONASA | 4.5% × 300,000 | 13,500.00 |
| Employee FRL | 0.1% × 300,000 | 300.00 |
| **Employee BPS total** | 40,884.60 + 13,500 + 300 | **54,684.60** |
| **Net of BPS** | 300,000 − 54,684.60 | **245,315.40** |
| Employer retirement | 7.5% × 272,564 | 20,442.30 |
| Employer FONASA | 5% × 300,000 | 15,000.00 |
| Employer FRL | 0.1% × 300,000 | 300.00 |
| Employer FGCL | 0.025% × 300,000 | 75.00 |
| **Employer BPS total** | 20,442.30 + 15,000 + 300 + 75 | **35,817.30** |
| **Total employer cost** | 300,000 + 35,817.30 | **335,817.30** |
| **Total BPS remittance** | 54,684.60 + 35,817.30 | **90,501.90** |

### Example F — With spouse (no own SNIS cover) + children, nominal UYU 80,000/month

> 2.5 BPC, spouse without SNIS cover + children → FONASA **8%** (top of the matrix). Below the retirement ceiling.

**Example F table**

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 80,000.00 |
| Employee retirement | 15% × 80,000 | 12,000.00 |
| Employee FONASA | 8% × 80,000 | 6,400.00 |
| Employee FRL | 0.1% × 80,000 | 80.00 |
| **Employee BPS total** | 12,000 + 6,400 + 80 | **18,480.00** |
| **Net of BPS** | 80,000 − 18,480 | **61,520.00** |
| Employer BPS total | 12.625% × 80,000 | 10,100.00 |
| **Total employer cost** | 80,000 + 10,100 | **90,100.00** |

*Employer cross-check:* 7.5% × 80,000 = 6,000; 5% × 80,000 = 4,000; 0.1% × 80,000 = 80; 0.025% × 80,000 = 20 → 6,000 + 4,000 + 80 + 20 = **10,100.00** ✓

## Section 7 — Boundary with IRPF (separate DGI income tax — NOT a contribution)

- **IRPF scope note** — IRPF is not computed by this skill. It is documented here only so the boundary is unambiguous and so that the "115 BPC" value is correctly understood as an IRPF bracket boundary, never a BPS threshold. IRPF (Impuesto a la Renta de las Personas Físicas, Categoría II — rentas de trabajo) is a DGI progressive income tax in BPC units. BPC = UYU 6,864 (2026); UYU 6,576 (2025).  _(Texto Ordenado 2023, Título 7, art. 48; Decreto 148/007 art. 63; BPS Comunicados R 2/2025 and R 5/2026; Decreto N° 11/026)_

**IRPF Category II brackets (BPC)**  _(Decreto 148/007 art. 63 (monthly twelfths of Título 7 art. 48); BPS Comunicados R 2/2025 and R 5/2026)_

| Bracket (BPC) | Rate | Hasta (UYU/month), 2026 | Hasta (UYU/month), 2025 |
| --- | --- | --- | --- |
| Up to 7 BPC | **0%** (MNIG) | 48,048 | 46,032 |
| Over 7–10 BPC | **10%** | 68,640 | 65,760 |
| Over 10–15 BPC | **15%** | 102,960 | 98,640 |
| Over 15–30 BPC | **24%** | 205,920 | 197,280 |
| Over 30–50 BPC | **25%** | 343,200 | 328,800 |
| Over 50–75 BPC | **27%** | 514,800 | 493,200 |
| Over 75–115 BPC | **31%** | 789,360 | 756,240 |
| Over 115 BPC | **36%** | — | — |

- **Non-taxable minimum (MNIG)** — 7 BPC: UYU 48,048/month in 2026; UYU 46,032/month in 2025  _(Section 7)_
- **115 BPC meaning** — 115 BPC = UYU 789,360/month in 2026 (115 × 6,864) and UYU 756,240/month in 2025 (115 × 6,576) — the top of the 31% bracket / start of 36%. This is the only meaning of "115 BPC"; it is an IRPF boundary, never a BPS contribution threshold.  _(Section 7)_

The authoritative BPC values are UYU 6,864 for 2026 (Decreto N° 11/026) and UYU 6,576 for 2025 (Decreto N° 5/025); never use a converted or foreign-currency figure.

- **IRPF deduction credit rates** — IRPF deductions are taken as a credit at 14% (income at or below the 15 BPC equivalent: UYU 102,960/month in 2026, UYU 98,640/month in 2025) or 8% above; child deductions are UYU 11,440/month in 2026 (disabled child UYU 22,880) and UYU 10,960/month in 2025 (disabled child UYU 21,920); BPS contributions themselves feed the deductible base. The monthly withholding base is increased by 6% when the month's income exceeds 10 BPC. Compute IRPF in the uruguay-payroll / uruguay-income-tax skill — not here.  _(Título 7 art. 49; Decreto 148/007 art. 63; BPS Comunicados R 2/2025 and R 5/2026)_

BPC bracket cross-check (× 12 = annual). 2025: 552,384 / 789,120 / 1,183,680 / 2,367,360 / 3,945,600 / 5,918,400 / 9,074,880 ✓ consistent with BPC 6,576. 2026: 576,576 / 823,680 / 1,235,520 / 2,471,040 / 4,118,400 / 6,177,600 / 9,472,320 ✓ consistent with BPC 6,864.

## Section 8 — Tier 1 rules (deterministic — apply mechanically)

- **BPC value** — UYU 6,864/month for 2026 and UYU 6,576/month for 2025; use one value consistently within a computation, chosen by the pay period  _(Decreto N° 11/026; Decreto N° 5/025)_
- **Employee BPS composition** — retirement 15% + FONASA 3%–8% (Section 3 matrix) + FRL 0.1%  _(Ley 16.713 art. 181; Ley 18.211 arts. 61 and 66; Ley 19.689 art. 17)_
- **Employer BPS composition (general private)** — retirement 7.5% + FONASA 5% + FRL 0.1% + FGCL 0.025% = 12.625% before BSE/CCM  _(Ley 18.083 art. 87; Ley 18.211 art. 61; Ley 19.689 art. 17; Ley 19.690 art. 10)_
- **FONASA band split** — 2.5 BPC = UYU 17,160 in 2026 and UYU 16,440 in 2025, tested on the month's remuneration excluding the aguinaldo. At or below the split → 3% (single) / 5% (spouse w/o SNIS). Above it → 4.5% / 6% / 6.5% / 8% per family situation (Section 3).  _(Ley 18.211 arts. 61 and 66; BPS Tasas Fonasa)_
- **Retirement contribution ceiling** — UYU 288,836/month from February 2026; UYU 272,564/month from February 2025 to January 2026. Salary above the ceiling is exempt from retirement only  _(Ley 16.713 art. 7; BPS Valores históricos)_
- **FONASA, FRL, FGCL not capped** — FONASA, FRL, and FGCL are NOT capped — they apply to the full nominal salary regardless of the retirement ceiling.  _(Ley 18.211 art. 61; Ley 19.689 art. 17; Ley 19.690 art. 10)_
- **FGCL employer-only** — FGCL is employer-only (0.025%); never charge it to the employee.  _(Ley 19.690 art. 10; BPS FGCL page)_
- **Aguinaldo** — The aguinaldo is materia gravada: charge retirement, FONASA, FRL and FGCL on it at the ordinary rates.  _(Ley 16.713 art. 153; BPS Tasas Fonasa)_
- **Minimum wage** — UYU 25,383/month from 1 Jul 2026; UYU 24,572/month from 1 Jan 2026; UYU 23,604/month from 1 Jan 2025. A minimum-wage earner still pays full BPS.  _(Decreto N° 319/025; Decreto N° 369/024)_
- **IRPF separate tax** — IRPF is a separate DGI tax (Section 7) — never bundle it into the BPS rate; route IRPF to the payroll/income-tax skill.  _(Texto Ordenado 2023, Título 7)_
- **Total employee retirement withholding** — The total employee retirement withholding is 15% regardless of the BPS/AFAP allocation (Section 4.5).  _(Ley 16.713 art. 181; Ley 20.130 art. 22)_
- **Currency requirement** — All amounts in UYU ($U) — never another currency.  _(Section 8, rule 12)_
- **Total monthly BPS remittance** — Total monthly BPS remittance = employee BPS shares + employer BPS shares, declared in the BPS nómina and paid by the BPS calendar date of the following month (Section 12).  _(BPS, Vencimientos 2026)_

## Section 9 — Tier 2 catalogue (reviewer judgement required)

These items require a licensed Uruguayan accountant's judgement and/or confirmation against primary sources before reliance.

### T2-UY-1 — AFAP allocation for an unusual record

Trigger: request for the split of the 15% retirement between BPS and the private AFAP for a worker with several employers, an art. 8 option or a change of regime. Issue: the BPS levels are confirmed (Section 4.5), but the worker's option under Ley 16.713 art. 8, multi-employer aggregation (each entity considers its own assignments, Ley 20.130 art. 22 num. 5) and regime changes need the worker's BPS record. Action: state the total 15%; give the allocation only for a plain single-employer case. Flag for reviewer.

### T2-UY-2 — BSE workplace-accident premium

Trigger: employer wants total labour cost including accident insurance. Issue: the BSE premium varies by activity/risk class; no single national rate (Section 4.2). Action: flag as a research gap; do not invent a rate.

### T2-UY-3 — CCM (Complemento de Cuota Mutual)

Trigger: employer FONASA cost appears higher than 5%. Issue: the CCM formula is published (Section 4.2) but whether it bites depends on the number of covered workers and their basic contributions in the month, and the cuota mutual changes. Action: compute it only from the BPS factura or with the cuota mutual for the month; otherwise flag for reviewer.

### T2-UY-4 — Civil/public-organism patronal rates

Trigger: employer is a civil or public organism. Issue: patronal rates differ from the 7.5% general private rate (Section 4.2). Action: confirm the applicable rate before computing.

### T2-UY-5 — Recargo por mora for a given month

Trigger: request for the total cost of a late BPS payment. Issue: the mora fine tiers are statutory (Section 14), but the monthly recargo follows the BCU averages and is capitalised every four months; 0.80% a month was the September and October 2026 rate. Action: read the rate for the payment month off BPS's values page or its simulator.

## Section 10 — Excel working paper template

Reproduce this layout in a single worksheet (one column per employee, or one row per employee for a register). All cells in UYU. Enter the constants for the year of the pay period — **2026**: BPC 6,864; FONASA band split 17,160; retirement ceiling 288,836. **2025**: BPC 6,576; band split 16,440; ceiling 272,564. This template computes the BPS layer only — IRPF is computed in the payroll/income-tax skill.

**Excel working paper template rows**

| Row | Label | Formula / source |
| --- | --- | --- |
| 1 | Employee name | input |
| 2 | Pay period (month/year) | input |
| 3 | Nominal salary | input |
| 4 | FONASA employee rate (decimal) | input (0.03 / 0.045 / 0.05 / 0.06 / 0.065 / 0.08 per Section 3) |
| 5 | Sector (general private?) | input (Y/N — if N, confirm patronal rate) |
| 6 | Retirement base (capped) | `=MIN(B3,272564)` |
| 7 | Employee retirement | `=B6*0.15` |
| 8 | Employee FONASA | `=B3*B4` |
| 9 | Employee FRL | `=B3*0.001` |
| 10 | **Employee BPS total** | `=B7+B8+B9` |
| 11 | **Net of BPS** | `=B3-B10` |
| 12 | Employer retirement | `=B6*0.075` |
| 13 | Employer FONASA | `=B3*0.05` |
| 14 | Employer FRL | `=B3*0.001` |
| 15 | Employer FGCL | `=B3*0.00025` |
| 16 | **Employer BPS total** | `=B12+B13+B14+B15` |
| 17 | **Total employer cost** | `=B3+B16` |
| 18 | **Total BPS remittance** | `=B10+B16` |

Cross-check against Example C (nominal 120,000, FONASA 4.5%, single): row 6 = 120,000; row 7 = 18,000; row 8 = 5,400; row 9 = 120; row 10 = 23,520; row 11 = 96,480; row 16 = 15,150; row 17 = 135,150; row 18 = 38,670. ✓ Matches Example C exactly.

Cross-check against Example E (nominal 300,000, ceiling bites): row 6 = 272,564; row 7 = 40,884.60; row 8 = 13,500; row 9 = 300; row 10 = 54,684.60; row 11 = 245,315.40; row 12 = 20,442.30; row 16 = 35,817.30; row 17 = 335,817.30; row 18 = 90,501.90. ✓ Matches Example E exactly.

## Section 11 — Onboarding fallback

- **Onboarding order** — If the user has not provided enough to compute BPS, collect in this order: 1. Monthly nominal salary in UYU — refuse if given in USD or another currency (R-UY-BPS-1). 2. FONASA family situation — single / single with children / with spouse (own SNIS cover or not) / spouse + children — selects the FONASA band (Section 3). 3. Employer sector — general private (7.5% patronal) or civil/public organism (confirm rate). 4. Pay period (month + year) — selects the constants: 2026 (BPC 6,864; ceiling 288,836) or 2025 (BPC 6,576; ceiling 272,564). 5. Confirm the employer is registered with BPS.
- **Missing input handling** — If any required input is missing, state what is missing and do not fabricate a figure. If asked about IRPF, redirect to the payroll/income-tax skill (Section 7).

## Section 12 — Filing obligations

**Filing obligations**

| Item | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| BPS **nómina** (declaración nominada) and payment | Declare and pay employee + employer BPS shares (and the IRPF withheld, which BPS computes and collects with them) | The month after the payroll month, by the BPS calendar date for the last digit of the company number. 2026, digits 0 to 4: 19 Jan, 18 Feb, 16 Mar, 20 Apr, 19 May, 15 Jun, 15 Jul, 17 Aug, 15 Sep, 16 Oct, 17 Nov, 15 Dec; digits 5 to 9: 20 Jan, 19 Feb, 17 Mar, 21 Apr, 20 May, 16 Jun, 16 Jul, 18 Aug, 16 Sep, 19 Oct, 18 Nov, 16 Dec (the January 2026 nómina is due by 18 or 19 February). Companies without dependants pay by a separate calendar (22 October 2026 for September) | BPS, Vencimientos 2026 (updated 30 April 2026); Decreto 148/007 art. 65 |
| IRPF (separate, via DGI) | Annual declaración jurada (Form 1102/1103), 29 June to 31 August 2026 for FY2025 | See uruguay-payroll / uruguay-income-tax skill | DGI, Calendario de la Campaña 2026 de IRPF |

- **Mandatory BPS employer registration** — Any dependent worker triggers mandatory BPS employer registration; no income floor exempts the employer.
- **IRPF ajuste anual boundary** — The IRPF year-end ajuste anual and Form 1102/1103 income-tax declarations are a DGI matter handled in the payroll/income-tax skill — not a BPS contribution obligation.
- **Late payment** — Mora fine of 5% of the unpaid amount within five business days, 10% up to 90 calendar days and 20% beyond, halved to 2.5% / 5% / 10% when the nómina was filed on time with a declaration of non-payment, plus the monthly recargo (0.80% in September and October 2026), capitalised every four months (Código Tributario art. 94; BPS, Multas y recargos por mora; BPS Valores actuales).

## Section 13 — Interaction with other skills

**Interaction with other skills**

| Scenario | Skill to use |
| --- | --- |
| BPS social contributions only (employee + employer) | **This skill (uruguay-social-contributions.md)** |
| Full payroll incl. IRPF withholding + net pay | uruguay-payroll.md |
| Individual IRPF annual return (Form 1102/1103) | uruguay-income-tax.md |
| Uruguay VAT (IVA) returns | uruguay-iva.md |
| Uruguay corporate income tax (IRAE) | uruguay-corporate-tax.md |

### Key handoff points

Social contributions → Payroll: this skill produces the BPS layer (employee ~19.6% and employer 12.625%). The payroll skill layers IRPF on top to reach net pay. Social contributions → Bookkeeping: the 12.625% employer BPS is an expense; the employee BPS shares are a liability until remitted to BPS via Formulario 1102.

## Section 14 — Reference material

### 14.1 Test suite (numbered — recompute to confirm any change)

**Test suite**

| # | Input | Expected output | Recomputation |
| --- | --- | --- | --- |
| 1 | Min wage 23,604, single | Employee BPS 4,626.38; employer BPS 2,980.00; net-of-BPS 18,977.62; total cost 26,584.00 | Ex. A |
| 2 | Nominal 15,000, single (≤ band split) | FONASA 3%; employee BPS 2,715.00; employer BPS 1,893.75; total cost 16,893.75 | Ex. B |
| 3 | Nominal 120,000, single | FONASA 4.5%; employee BPS 23,520.00; employer BPS 15,150.00; remittance 38,670.00 | Ex. C |
| 4 | Nominal 120,000, single + 1 child | FONASA 6%; employee BPS 25,320.00; net-of-BPS 94,680.00 | Ex. D |
| 5 | Nominal 300,000, single (ceiling) | Retirement on 272,564; employee BPS 54,684.60; employer BPS 35,817.30; total cost 335,817.30 | Ex. E |
| 6 | Nominal 80,000, spouse w/o SNIS + children | FONASA 8%; employee BPS 18,480.00; employer BPS 10,100.00; total cost 90,100.00 | Ex. F |
| 7 | Employer total rate | 12.625% (7.5 + 5 + 0.1 + 0.025) | Section 4.2 |
| 8 | Employee total rate (single, > 2.5 BPC, below ceiling) | 19.6% (15 + 4.5 + 0.1) | Section 4.1 |
| 9 | FONASA band split | 2.5 BPC = 17,160 in 2026 (2.5 × 6,864); 16,440 in 2025 (2.5 × 6,576) | Section 3 |
| 10 | Retirement ceiling | 288,836/month in 2026; 272,564/month in 2025 (retirement capped; FONASA/FRL/FGCL on full nominal) | Section 4.4; Ex. E |
| 11 | "115 BPC" meaning | IRPF bracket boundary: 789,360 in 2026 (115 × 6,864), 756,240 in 2025 — NOT a BPS threshold | Section 7 |
| 12 | IRPF vs BPS | IRPF is a separate DGI tax — not computed here | Section 7 |

### 14.2 Sources

**Sources**

| # | Title | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Ley 16.713 — social security reform (arts. 7, 8, 153, 158, 181) | IMPO | https://www.impo.com.uy/bases/leyes/16713-1995 |
| 2 | Ley 18.083 art. 87 — employer pension contribution 7.5% | IMPO | https://www.impo.com.uy/bases/leyes/18083-2006 |
| 3 | Ley 18.211 arts. 61 and 66 — FONASA contributions | IMPO | https://www.impo.com.uy/bases/leyes/18211-2007 |
| 4 | Ley 19.689 art. 17 — FRL 0.10% from 1 January 2019 | IMPO | https://www.impo.com.uy/bases/leyes/19689-2018/17 |
| 5 | Ley 19.690 art. 10 — FGCL 0.025% | IMPO | https://www.impo.com.uy/bases/leyes/19690-2018 |
| 6 | Ley 20.130 art. 22 — contribution levels of the Sistema Previsional Común | IMPO | https://www.impo.com.uy/bases/leyes/20130-2023 |
| 7 | Código Tributario (Decreto-Ley 14.306) art. 94 — mora | IMPO | https://www.impo.com.uy/bases/codigo-tributario/14306-1974/94 |
| 8 | Texto Ordenado 2023, Título 7 — IRPF (arts. 48 and 49); Decreto 148/007 art. 63 | IMPO | https://www.impo.com.uy/bases/todgi-2023/7-2024 ; https://www.impo.com.uy/bases/decretos/148-2007 |
| 9 | BPS — Tasas (contribution rates) | Banco de Previsión Social (BPS) | https://www.bps.gub.uy/835/tasas.html |
| 10 | BPS — Tasas de Aportes Fonasa (matrix, socios vitalicios, CCM formula) | BPS | https://www.bps.gub.uy/10314/tasas-fonasa.html |
| 11 | BPS — Fondo de Reconversión Laboral (FRL); Fondo de Garantía de Créditos Laborales | BPS | https://www.bps.gub.uy/10322/fondo-reconversion-laboral-frl.html ; https://www.bps.gub.uy/15668/fondo-de-garantia-de-creditos-laborales.html |
| 12 | BPS — Valores actuales and Valores históricos (topes, niveles, cuota mutual, recargo por mora) | BPS | https://www.bps.gub.uy/5478/valores-actuales.html ; https://www.bps.gub.uy/5479/valores-historicos.html |
| 13 | BPS — Vencimientos 2026; Multas y recargos por mora | BPS | https://www.bps.gub.uy/24165/vencimientos-de-monotributo.html ; https://www.bps.gub.uy/18132/multas-y-recargos-por-mora.html |
| 14 | BPS — Comunicado R 2/2025 and Comunicado R 5/2026 (valores escalas IRPF) | BPS | https://www.bps.gub.uy/bps/file/22584/2/2025---comunicado-r-2---valores-escalas-irpf-2025.pdf ; https://www.bps.gub.uy/bps/file/23860/3/2026---comunicado-r-5---valores-escalas-irpf-2026.pdf |
| 15 | DGI — Base de Prestaciones y Contribuciones (BPC) | DGI (gub.uy) | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/base-prestaciones-contribuciones-bpc |
| 16 | DGI — IRPF Categoría 2 escalas y alícuotas | DGI (gub.uy) | https://www.gub.uy/direccion-general-impositiva/politicas-y-gestion/irpf-categoria-2-escalas-alicuotas |
| 17 | Decreto N° 5/025 — BPC 2025 (UYU 6,576) | IMPO | https://www.impo.com.uy/bases/decretos/5-2025 |
| 18 | Decreto N° 11/026 — BPC 2026 (UYU 6,864) | IMPO | https://www.impo.com.uy/bases/decretos/11-2026 |
| 19 | Decreto N° 369/024 — Salario Mínimo Nacional 2025 (UYU 23,604) | IMPO | https://www.impo.com.uy/bases/decretos/369-2024 |
| 20 | Decreto N° 319/025 — Salario Mínimo Nacional 2026 (UYU 24,572 from 1 Jan; UYU 25,383 from 1 Jul) | IMPO | https://www.impo.com.uy/bases/decretos/319-2025 |
| 21 | DGI — Calendario de la Campaña 2026 de IRPF | DGI (gub.uy) | https://www.gub.uy/direccion-general-impositiva/comunicacion/noticias/calendario-campana-2026-irpf |

## PROHIBITIONS

- **R-UY-BPS-1 (implied) and prohibitions list** — NEVER bundle IRPF into the BPS rate — IRPF is a SEPARATE DGI income tax (progressive 0%–36% in BPC units); this skill computes BPS social contributions only. NEVER mix BPC values within one computation — UYU 6,864 for 2026 and UYU 6,576 for 2025, applied consistently to the FONASA band split (17,160 / 16,440) and every other BPC-denominated figure. NEVER treat "115 BPC" as a BPS contribution threshold — it is an IRPF bracket boundary (789,360 in 2026, 756,240 in 2025). Confusing the two was the prior file's defect. NEVER compute Uruguayan contributions in USD or any non-UYU currency — refuse and ask for the UYU nominal salary. NEVER assume the FONASA employee rate — it varies 3%–8% by income band and family situation; ask if unknown. NEVER apply retirement contributions (15% / 7.5%) above the ceiling for the pay month (UYU 288,836 from February 2026; UYU 272,564 from February 2025 to January 2026), and NEVER cap FONASA/FRL/FGCL — those apply to the full nominal salary. NEVER charge FGCL (0.025%) to the employee — it is employer-only. NEVER let the BPS/AFAP allocation change the 15% employee or 7.5% employer contribution — the levels only route the money. NEVER exempt the aguinaldo from BPS contributions — it is materia gravada. NEVER state a BSE accident premium, or a CCM amount or recargo rate for a month you have not read off BPS — those depend on the risk class, the workforce and the BCU averages. NEVER run a pay period on another year's constants. The 2026 values are published: BPC 6,864 (Decreto N° 11/026), retirement ceiling 288,836 from February, minimum wage 24,572 to 30 June and 25,383 from 1 July (Decreto N° 319/025). NEVER present BPS computations as definitive — label them estimated and direct the user to a licensed Uruguayan accountant (contador público).  _(Section 8 (R-UY-BPS-1 referenced in Section 11))_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Uruguay) before implementation. This is a Tier 2 (research-verified) skill: figures are sourced to the statutes and decrees published by IMPO and to BPS and DGI publications but have not yet been verified section-by-section by a licensed Uruguayan accountant, and items marked "[RESEARCH GAP — reviewer to confirm]" carry residual uncertainty. The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
