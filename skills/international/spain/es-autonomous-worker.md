---
name: es-autonomous-worker
description: Use this skill whenever asked about Spanish self-employed (autónomo) tax and social security obligations beyond IRPF computation. Trigger on phrases like "autonomo", "autónomo", "cuota de autonomos", "cuota seguridad social autonomo", "RETA", "tarifa plana", "alta autonomo", "baja autonomo", "cotizacion por ingresos reales", "obligaciones fiscales autonomo", "modelos autonomo", "Modelo 303", "Modelo 130", "Modelo 390", "Modelo 349", "calendario fiscal autonomo", "pluriactividad", "autonomo societario", "facturacion autonomo", "estimacion directa", "libro registro", "IGIC autonomo", "IPSI autonomo", "autonomo Canarias", "autonomo Ceuta Melilla", "cuanto paga un autonomo", or any question about the complete fiscal and social security picture for a self-employed worker in Spain. ALWAYS read this skill before advising on autónomo setup, ongoing obligations, or take-home pay calculations.
version: 1.2
jurisdiction: ES
tax_year: 2025
last_updated: 2026-11-11
review_status: pending_review
depends_on:
  - es-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ES Autonomous Worker

## Spain Autónomo (Self-Employed Worker) Complete Obligations Skill v1.2

> **Based on work by [Nambu89 (Impuestify)](https://github.com/Nambu89/Impuestify)** and **[Pau March (larenta)](https://github.com/paumrch/larenta)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Estado Español) |
| Subject | Trabajador Autónomo (Self-Employed Worker / Sole Trader) |
| Currency | EUR only |
| Legal framework | Ley 20/2007 (Estatuto del Trabajo Autónomo); RDL 13/2022 (cotización por ingresos reales) |
| Social Security regime | RETA (Régimen Especial de Trabajadores Autónomos) |
| Tax regime | IRPF (estimación directa simplificada by default) |
| Tax authority | AEAT (tax) + Tesorería General de la Seguridad Social (TGSS) (social security) |
| Key filing forms | Modelo 036/037 (census), Modelo 130 (quarterly IRPF), Modelo 303 (quarterly IVA), Modelo 100 (annual IRPF) |

## Section 2 -- Cuota de Autónomos 2025 and 2026

Since January 2023, self-employed workers pay Social Security (cuota de autónomos) based on actual income (rendimientos netos). The system has 15 brackets deployed gradually until 2032.

### The 15 Contribution Brackets (Tramos) -- 2025 and 2026

**The 15 Contribution Brackets (Tramos) -- 2025 and 2026**  _(Orden PJC/297/2026 art. 18: minimum bases unchanged from 2025; https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296)_

| Tramo | Net Monthly Income (EUR) | Minimum Base (EUR/month) | Minimum Contribution 2025 at 31.40% (EUR/month) | Minimum Contribution 2026 at 31.50% (EUR/month) |
| --- | --- | --- | --- | --- |
| 1 | ≤ 670 | 653.59 | 205.23 | 205.88 |
| 2 | 670.01 - 900 | 718.95 | 225.75 | 226.47 |
| 3 | 900.01 - under 1,166.70 | 849.67 | 266.80 | 267.65 |
| 4 | 1,166.70 - 1,300 | 950.98 | 298.61 | 299.56 |
| 5 | 1,300.01 - 1,500 | 960.78 | 301.68 | 302.65 |
| 6 | 1,500.01 - 1,700 | 960.78 | 301.68 | 302.65 |
| 7 | 1,700.01 - 1,850 | 1,143.79 | 359.15 | 360.29 |
| 8 | 1,850.01 - 2,030 | 1,209.15 | 379.67 | 380.88 |
| 9 | 2,030.01 - 2,330 | 1,274.51 | 400.20 | 401.47 |
| 10 | 2,330.01 - 2,760 | 1,356.21 | 425.85 | 427.21 |
| 11 | 2,760.01 - 3,190 | 1,437.91 | 451.50 | 452.94 |
| 12 | 3,190.01 - 3,620 | 1,519.61 | 477.16 | 478.68 |
| 13 | 3,620.01 - 4,050 | 1,601.31 | 502.81 | 504.41 |
| 14 | 4,050.01 - 6,000 | 1,732.03 | 543.86 | 545.59 |
| 15 | > 6,000 | 1,928.10 | 605.42 | 607.35 |

- **Contribution rate** — 31.40% of chosen base de cotización for 2025; 31.50% for 2026 (MEI rises from 0.80% to 0.90%). Maximum base EUR 4,909.50/month for 2025 and EUR 5,101.20/month for 2026 (the contribution amounts above are the minimums -- workers can choose higher bases within their bracket for better future pensions)

### How to Calculate Net Monthly Income (Rendimiento Neto)

Use [es-social-contributions, Rule 1](es-social-contributions.md#rule-1----net-income-formula-for-tranche-determination) to convert IRPF earnings to RETA net earnings. Direct estimation adds back the owner's contributions before the general expense deduction. Use the expected monthly average for provisional band selection.

### Key Rules

- **6 changes per year** — You can change your contribution base up to 6 times annually to match income fluctuations
- **Annual regularisation** — TGSS determines the definitive contribution from the applicable earnings and periods. Rule 5 of the social contributions guide covers the initial reduction and extension.
- **Autónomos societarios minimum** — Check the period and category under [es-social-contributions, Rule 6](es-social-contributions.md#rule-6----autonomo-societario-minimum).

## Section 3 -- Tarifa Plana (Flat Rate for New Autónomos)

Use [es-social-contributions, Rule 5](es-social-contributions.md#rule-5----tarifa-plana) for eligibility, application timing, extension and eligible company partners. The statutory EUR 80 base amount applies to 2023–2025 before MEI. For 2026, Importass shows EUR 88.64 including MEI. Reconcile the actual amount and period on the TGSS assessment.

Check eligibility and the request at registration, plus any separate extension request. Review debt, overlapping relief and concurrent employment where relevant before applying the reduction.

## Section 4 -- Complete Fiscal Calendar for Autónomos

### Quarterly Obligations

**Quarterly Obligations**

| Quarter | Period | Deadline | Models to File |
| --- | --- | --- | --- |
| Q1 | Jan-Mar | 1-20 April | 130 (IRPF) + 303 (IVA) |
| Q2 | Apr-Jun | 1-20 July | 130 + 303 |
| Q3 | Jul-Sep | 1-20 October | 130 + 303 |
| Q4 | Oct-Dec | 1-30 January | 130 + 303 |

### Annual Obligations

**Annual Obligations**

| Model | Description | Deadline |
| --- | --- | --- |
| 100 | Declaración de la Renta (IRPF annual) | April-June (campaign dates vary) |
| 390 | Annual IVA summary | 1-30 January |
| 347 | Operations with third parties > EUR 3,005.06 | February |
| 349 | Intra-EU operations (if applicable) | Monthly or quarterly |

### Additional Models (if applicable)

**Additional Models (if applicable)**

| Model | Who | When |
| --- | --- | --- |
| 111 | If you have employees (retenciones nóminas) | Quarterly |
| 115 | If you rent premises (retenciones alquileres) | Quarterly |
| 131 | Instead of 130, if in estimación objetiva (módulos) | Quarterly |
| 720 | Assets abroad > EUR 50,000 | March |

## Section 5 -- Indirect Tax by Territory

### IVA (Common Territory + Baleares)

**IVA (Common Territory + Baleares)**

| Item | Value |
| --- | --- |
| General rate | 21% |
| Reduced rate | 10% (food, transport, hotels) |
| Super-reduced rate | 4% (bread, milk, medicines, books) |
| Filed via | Modelo 303 (quarterly) + Modelo 390 (annual summary) |

### IGIC (Canarias)

**IGIC (Canarias)**

| Item | Value |
| --- | --- |
| General rate | 7% |
| Reduced | 3% |
| Zero rate | 0% (certain essential goods) |
| Incrementado | 9.5%, 15% |
| Filed via | Modelo 420 (quarterly) to Hacienda Canaria |

### IPSI (Ceuta and Melilla)

**IPSI (Ceuta and Melilla)**

| Item | Value |
| --- | --- |
| General rate (services) | 4% |
| Other rates | 0.5% - 10% depending on goods/services |
| Filed via | Local IPSI models to Ciudad Autónoma |

## Section 6 -- Net Take-Home Calculation (Sueldo Neto Autónomo)

### Monthly Calculation Formula

- **Monthly calculation formula** — Facturación bruta (without IVA) + IVA/IGIC/IPSI repercutido (charged to client) = Total factura (amount on invoice) - Retención IRPF (15% or 7% withheld by client, if applicable) = Cobro efectivo (cash received) - Cuota autónomos (Social Security) - Gastos deducibles = Neto mensual aproximado IVA/IGIC/IPSI a pagar Hacienda = repercutido - soportado (on purchases)

### Annual Calculation Formula

- **Annual calculation formula** — Facturación bruta anual - Gastos deducibles anuales - Cuota autónomos anual - 5% gastos difícil justificación (max EUR 2,000, if simplificada) = Base imponible IRPF IRPF anual = Apply progressive brackets to base imponible Neto anual = Facturación bruta - IRPF - Cuota SS - Gastos

### Worked Example: 2025 IT Freelancer, Madrid, EUR 3,000/month billing

Assume monthly RETA net earnings in band 10 and an assessed standard contribution at the minimum base. The annual illustration uses a stipulated EUR 5,318 IRPF liability. Compute the actual liability separately using the relevant state and regional rules.

Monthly:
  Facturación bruta:            EUR 3,000
  + IVA 21%:                    EUR 630
  = Total factura:              EUR 3,630
  - Retención IRPF 15%:        EUR 450
  = Cobro efectivo:             EUR 3,180
  - Cuota autónomos (Tramo 10): EUR 425.85 (minimum base 1,356.21 × 31.40%, 2025)
  - Gastos deducibles:          EUR 200
  = Cash before IVA settlement: EUR 2,554.15

Annual:
  Facturación bruta:            EUR 36,000
  - Gastos deducibles:          EUR 2,400
  - Cuota autónomos:            EUR 5,110.20 (425.85 × 12)
  - Stipulated IRPF liability:  EUR 5,318.00
  Neto anual:                   EUR 36,000 - 5,318 - 5,110.20 - 2,400 = EUR 23,171.80
  Monthly average:              EUR 1,930.98
  Net as a share of billings:    64.37%

Monthly cash includes IVA collected and is reduced by IRPF withholding. The annual calculation excludes IVA and uses the full stipulated IRPF liability.

## Section 7 -- Territorial Regime Classification

**Territorial Regime Classification**

| Fiscal Residence | IRPF Scale | Indirect Tax | SS Bonification |
| --- | --- | --- | --- |
| Common territory (15 CCAA) | State + Regional (50/50) | IVA 21% | None |
| Canarias | State + Regional | IGIC 7% | None |
| Ceuta | State + Regional, 60% deduction cuota | IPSI 4% | 50% cuota SS (certain sectors) |
| Melilla | State + Regional, 60% deduction cuota | IPSI 4% | 50% cuota SS (certain sectors) |
| País Vasco (Álava/Bizkaia/Gipuzkoa) | Foral (own scale, 23%-49%) | IVA 21% | None |
| Navarra | Foral (own scale, 13%-52.8%) | IVA 21% | None |

### Ceuta/Melilla Sectors with 50% SS Bonification

- **Eligible sectors** — Agriculture, fishing, aquaculture; Industry (except energy and water); Commerce, tourism, hospitality; Other services (excluding air transport, building construction, financial/real estate activities)

## Section 8 -- Types of Autónomo

### 8.1 Autónomo Persona Física (Standard)

- **Autónomo Persona Física** — Most common: freelancer or sole trader; Filed as individual IRPF taxpayer; Can choose estimación directa simplificada (default) or normal; Retención 15% (7% first 3 years) on professional invoices (Sección 2 IAE only)

### 8.2 Autónomo Societario

- **Autónomo Societario** — Check the services and effective-control tests under [LGSS art. 305(2)(b) and (e)](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a305). Use Rules 1, 5 and 6 of the social contributions guide for the earnings calculation, reduced contribution and ordinary minimum base. Determine the IRPF treatment of each source of remuneration separately.

### 8.3 Autónomo Colaborador (Family Member)

- **Autónomo Colaborador** — Check the family category and the period-specific base under Rule 6 of the social contributions guide. Eligible new collaborating relatives receive a common-contingency contribution credit of 50% for 18 months and 25% for the next 6 months, measured against the minimum base of the first general income band. The rule requires 5 years out of the relevant regimes before registration. Check any tax filing obligations by activity. [Ley 20/2007, art. 35](https://www.boe.es/eli/es/l/2007/07/11/20/con/20260902)

### 8.4 Autónomo Económicamente Dependiente (TRADE)

- **TRADE** — Derives ≥75% of income from a single client; Must formalize the relationship with a written contract; Specific protections under Estatuto del Trabajo Autónomo; Tax obligations are the same as standard autónomo

## Section 9 -- Registration Process (Alta de Autónomo)

### Steps

- **Step 1: Alta en Hacienda** — Alta en Hacienda (Modelo 036 or 037): Register for tax obligations, select IAE epígrafe, choose estimation regime
- **Step 2: Alta en RETA** — Alta en RETA (Modelo TA.0521): Register with Social Security within 60 days before starting activity (or same day)
- **Step 3: Licencia de actividad** — Licencia de actividad (if applicable): Some activities require local permits
- **Step 4: Libro registro** — Libro registro: Start maintaining income and expense records from day one

### Key Decisions at Registration

**Key Decisions at Registration**

| Decision | Options | Default |
| --- | --- | --- |
| Estimation regime | Directa simplificada / Directa normal / Objetiva (módulos) | Simplificada |
| IAE epígrafe | Section 1 (business) or Section 2 (professional) | Determines if retención applies |
| IVA regime | General / Simplified / Recargo equivalencia | General |
| Tarifa plana | Apply or not | Apply if eligible |
| Contribution base | Minimum of bracket or higher | Minimum |

## Section 10 -- Deductible Expenses for Autónomos

### Fully Deductible (with proper invoice)

**Fully Deductible (with proper invoice)**

| Expense | Notes |
| --- | --- |
| Cuota autónomos (RETA) | Monthly SS contribution |
| Office rent (local de negocio) | Fully deductible with factura |
| Professional services (gestoría, abogado) | Fully deductible |
| Software and subscriptions | Business use |
| Advertising and marketing | Fully deductible |
| Professional training | Related to activity |
| Professional insurance | Liability, etc. |
| Bank fees (business account) | Fully deductible |
| Payment processor fees (Stripe, PayPal) | Fully deductible |
| Depreciation (amortización) | Per simplified table |
| Business travel (transport) | Documented trips |
| Travel meals (dietas) | Max EUR 26.67/day domestic, EUR 48.08/day international |

### Partially Deductible (Special Rules)

**Partially Deductible (Special Rules)**

| Expense | Rule | Reference |
| --- | --- | --- |
| Home office supplies (luz, gas, agua) | (office area / total area) × 30% of supply costs | LIRPF Art. 30.2.5.b |
| Vehicle expenses | Business portion only (default: 50% IVA, IRPF needs logbook) | Art. 95 LIVA |
| Mobile phone | Business portion only (default 0% if not documented) |  |
| Meals not during travel | NOT deductible | Client entertainment excluded |
| Personal insurance | NOT deductible |  |
| IRPF payments (Modelo 130) | NOT deductible (prepayment of tax, not expense) |  |

### Gastos de Difícil Justificación (Simplificada only)

- **Gastos de difícil justificación** — 5% of rendimiento neto previo, maximum EUR 2,000/year; Automatic reduction under estimación directa simplificada; Covers expenses that are difficult to document but clearly business-related

## Section 11 -- Obligación de Declarar (Filing Obligation)

Not all autónomos are obligated to file the annual Renta if their income is very low:

## Section 11 -- Obligación de Declarar (Filing Obligation)

**Obligación de Declarar thresholds**

| Situation | Limit |
| --- | --- |
| Single payer, employment income only | EUR 22,000 |
| Multiple payers (2nd+ pays > EUR 1,500) | EUR 15,876 |
| Capital income | > EUR 1,600 |
| Real estate income | > EUR 1,000 |
| Any business/professional income | Always obligated to file |

## Section 11 -- Obligación de Declarar (Filing Obligation)

- **Always obligated to file** — Autónomos are ALWAYS obligated to file Modelo 100 regardless of income level (Art. 96 LIRPF exception for rendimientos de actividades económicas)  _(Art. 96 LIRPF)_

## Section 12 -- Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown estimation regime | Directa simplificada |
| Unknown cuota autónomos | Obtain the TGSS assessment or calculate a provisional amount from the verified period, earnings and chosen base |
| Unknown tarifa plana eligibility | Hold the contribution estimate and establish eligibility |
| Unknown if new autónomo | NOT new (15% retención, not 7%) |
| Unknown Sección IAE | Sección 2 (professional -- retención applies) |
| Unknown business-use % | 0% for mixed-use items |
| Unknown territory | Common territory with IVA 21% |
| Unknown effective registration date | Hold the reduced contribution until the date is established |

## PROHIBITIONS

- **Prohibition 1** — NEVER tell someone they can avoid paying cuota de autónomos if they are actively self-employed
- **Prohibition 2** — Verify Article 38 ter(9) status and the other eligibility conditions for a company partner
- **Prohibition 3** — NEVER deduct client entertainment meals from IRPF
- **Prohibition 4** — Apply the RETA general expense deduction by statutory category and period under Rule 1 of the social contributions guide
- **Prohibition 5** — NEVER confuse retenciones (tax prepayments) with expenses -- they are NOT deductible business expenses
- **Prohibition 6** — NEVER apply IVA to an autónomo in Canarias (they use IGIC) or Ceuta/Melilla (IPSI)
- **Prohibition 7** — NEVER forget that Modelo 130 is cumulative year-to-date (not just the quarter's income)
- **Prohibition 8** — Before extending the reduced contribution, verify the request, the applicable amount and the annual SMI conditions for each affected calendar year
- **Prohibition 9** — NEVER present cuota estimates as exact -- actual regularization happens the following year
- **Prohibition 10** — NEVER advise on baja (deregistration) without noting that this affects future tarifa plana eligibility

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
