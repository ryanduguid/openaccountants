---
name: es-corporate-tax
description: Use this skill whenever asked about Spanish corporate income tax (Impuesto sobre Sociedades, IS), Modelo 200, Modelo 202 (pagos fraccionados), corporate tax rates in Spain, SL tax obligations, company formation tax, deducciones empresariales, bases imponibles negativas (BINs), reserva de capitalizacion, reserva de nivelacion, or foral corporate tax. Trigger on phrases like "Impuesto de Sociedades", "Modelo 200", "Modelo 202", "IS Spain", "corporate tax Spain", "tipo gravamen sociedades", "SL taxes", "nueva creacion", "empresa reducida dimension", "microempresa fiscal", "BINs", "compensacion perdidas sociedad", "pago fraccionado empresa", "ZEC Canarias", "bonificacion Ceuta Melilla sociedades", "I+D deduccion sociedades", "donativos sociedad", "resultado contable", or any question about computing or filing corporate income tax in Spain. ALWAYS read this skill before touching any Spanish corporate tax work.
version: 1.2
jurisdiction: ES
tax_year: 2025
last_updated: 2026-11-11
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ES Corporate Tax

## Spain Corporate Income Tax (Impuesto sobre Sociedades) Skill v1.2

> **Based on work by [Nambu89 (Impuestify)](https://github.com/Nambu89/Impuestify)** and **[Pau March (larenta)](https://github.com/paumrch/larenta)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Estado Español) |
| Tax | Impuesto sobre Sociedades (IS) |
| Currency | EUR only |
| Fiscal year | Generally calendar year (can differ) |
| Primary legislation | Ley 27/2014 (LIS); Ley 7/2024 — **not only an IS reform: it also creates the Impuesto Complementario**, a separate Pillar Two charge, see Section 2A |
| Supporting legislation | RDL 4/2024 (microempresa); Art. 25-26 LIS (reserves/BINs) |
| Tax authority | AEAT (common territory); Haciendas Forales (Basque/Navarra) |
| Filing form | Modelo 200 (annual) |
| Quarterly payments | Modelo 202 (pagos fraccionados) |
| Filing deadline | 25 days after 6 months from fiscal year-end (July 25 for calendar year) |
| Modelo 202 deadlines | 1-20 April, 1-20 October, 1-20 December |

## Section 2 -- Tax Rates (Tipos de Gravamen) 2025

> **This guide cites Ley 7/2024 twice below, and took only one thing from it.**
> The same Act that changed the microempresa and ERD rates also created a second
> Spanish corporate tax — the **Impuesto Complementario**, Spain's Pillar Two
> charge — and this guide was silent on it. The statute was already in hand.
> Set out in *Section 2A* immediately below, read from the consolidated text at
> [BOE-A-2024-26694](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26694).
>
> It does **not** replace the Impuesto sobre Sociedades. The two run alongside
> each other, so every rate in this section still governs the ordinary charge.

### Section 2A -- Impuesto Complementario (Ley 7/2024, Pillar Two)

*Ley 7/2024, de 20 de diciembre*, BOE 307 of 21 December 2024, ELI
[boe.es/eli/es/l/2024/12/20/7/con](https://www.boe.es/eli/es/l/2024/12/20/7/con).
Its full title establishes three taxes at once, of which this is the first:
*«un Impuesto Complementario para garantizar un nivel mínimo global de imposición
para los grupos multinacionales y los grupos nacionales de gran magnitud, un
Impuesto sobre el margen de intereses y comisiones de determinadas entidades
financieras y un Impuesto sobre los líquidos para cigarrillos electrónicos…»*

**Effective dates and scope**

- Ley 7/2024 entered into force on 22 December 2024 and generally applies to tax periods beginning on or after 31 December 2023. The undertaxed profits rule (UTPR) generally applies to periods beginning on or after 31 December 2024. The earlier date applies to the Article 28(3) case where the ultimate parent is in an EU Member State that elected to defer the income inclusion and undertaxed profits rules under Article 50 of Directive (EU) 2022/2523. [Ley 7/2024, art 28(3) and final provision 22](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26694&p=20261003&tn=1)
- The general scope test covers a Spanish constituent entity of a multinational or large domestic group whose consolidated net turnover, including excluded entities, reaches EUR 750 million or more in at least 2 of the 4 tax periods immediately preceding the period under review. The measure uses the ultimate parent's consolidated financial statements. Adjust the threshold proportionally for any tested period longer or shorter than 12 months. [Ley 7/2024, art 6(1)](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26694&p=20261003&tn=1)
- The top-up percentage is the positive difference between the 15% minimum and the applicable jurisdiction's effective tax rate. [Ley 7/2024, arts 5(43), 22 and 23](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26694&p=20261003&tn=1)

| Charge | General application |
| --- | --- |
| Domestic top-up tax (*Impuesto Complementario nacional*) | Spanish constituent entities of groups in scope where the Spanish effective rate is below the minimum |
| Primary top-up tax (*Impuesto Complementario primario*) | Income inclusion rule for eligible Spanish parent entities in relation to low-taxed foreign constituent entities |
| Secondary top-up tax (*Impuesto Complementario secundario*) | UTPR for the share allocated to Spain under the statutory conditions |

[Ley 7/2024, arts 6(2)–(4), 27–29 and 32–36](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26694&p=20261003&tn=1)

**State filing and payment**

| Form | Ordinary period | Transition |
| --- | --- | --- |
| Modelo 240, notification of who files the information return | Before the final 3 months of the applicable information-return filing period. One notification can cover the group's Spanish constituent entities if it includes the required details. | For periods ending before 31 March 2025, within the 2 months before 30 June 2026 |
| Modelo 241, top-up tax information return | By the last day of month 15 after the tax period ends | For the transition period, within the 2 months before the last day of month 18 after period end. For periods ending before 31 March 2025, within the 2 months before 30 June 2026 |
| Modelo 242, self-assessment and payment | Within 25 calendar days after the end of month 15 following the tax period. Pay when filing. | Within 25 calendar days after the end of month 18 following the transition period. No filing before 30 June 2026. If the 25-day window would begin earlier, count it from that date |

[Ley 7/2024, arts 47 and 50–51 and transitional provision 5](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26694&p=20261003&tn=1) · [Royal Decree 252/2025, arts 18 and 32 and transitional provision 3](https://www.boe.es/buscar/act.php?id=BOE-A-2025-6598) · [Order HAC/1198/2025, arts 2, 4, 9, 13 and 15 and transitional provisions 1–2](https://www.boe.es/buscar/act.php?id=BOE-A-2025-21727&p=20260529&tn=1)

For the state regime, the qualifying foreign filing rules in Article 47 can relieve local Modelo 241 filing. Check the actual filer, the effective exchange arrangements and any additional information Spain requires. Modelo 240 and any Modelo 242 obligation must be considered separately. [Ley 7/2024, arts 6(5), 47(2)–(5) and 50–51](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26694&p=20261003&tn=1)

This section covers the state regime. Foral territories have their own instruments, including Navarra's [Ley Foral 18/2025](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-3911). Confirm the applicable territorial rules, electronic filing procedure and payment method before filing. Check the detailed computation and safe-harbour conditions separately.

### Common Territory (Territorio Común) -- Ley 7/2024

**Common Territory Rates**  _(Ley 7/2024)_

| Entity Type | INCN (Facturación) | Rate | Notes |
| --- | --- | --- | --- |
| Microempresa | < EUR 1,000,000 | 2025: 21% (first EUR 50,000) + 22% (rest); 2026: 19% + 21%; 2027 onwards: 17% + 20% | Ley 7/2024 Disp. Final 8ª / LIS DT 44ª |
| ERD (Empresa Reducida Dimensión) | EUR 1M - 10M | 24% | Transitional: drops 1pp/year to 20% by 2029 |
| General | ≥ EUR 10,000,000 | 25% | Standard rate |
| Nueva creación | Any (first 2 years with BI > 0) | 15% | First 2 fiscal years with positive base imponible |

### ERD Transitional Calendar (Ley 7/2024)

**ERD Transitional Calendar**  _(Ley 7/2024)_

| Fiscal Year | ERD Rate |
| --- | --- |
| 2025 | 24% |
| 2026 | 23% |
| 2027 | 22% |
| 2028 | 21% |
| 2029+ | 20% |

### Foral Territories

**Foral Territories Rates**

| Territory | General Rate | Microempresa | Nueva Creación |
| --- | --- | --- | --- |
| Álava (NF 37/2013) | 24% | 20%/24% (EUR 50k tramo) | 19%/24% |
| Bizkaia (NF 11/2013) | 24% | 20%/24% (EUR 50k tramo) | 19%/24% |
| Gipuzkoa (NF 1/2025) | 19% | 15%/17% (EUR 50k tramo) | 15%/19% |
| Navarra (LF 26/2016) | 28% | 23%/28% (EUR 50k tramo) | 15%/28% |

### Special Regimes

**Special Regimes Rates**

| Regime | Rate | Applicable |
| --- | --- | --- |
| ZEC Canarias | 4% (up to employment-based ceiling) | Entities in Zona Especial Canaria |
| Ceuta/Melilla | 25% with 50% bonificación on qualifying income | Income generated in Ceuta/Melilla |
| Cooperativas fiscalmente protegidas | 20% | Ley 20/1990 |
| Cooperativas especialmente protegidas | 20% + 50% bonificación cuota | Art. 34.2 Ley 20/1990 |

### Payments to Non-Residents (IRNR Withholding)

**Domestic rates on payments to non-residents without a permanent establishment**  _(TRLIRNR, RDLeg 5/2004, arts 25.1 and 31.2: https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527)_

| Payment | Rate | Reference |
| --- | --- | --- |
| Dividends | 19% | Art. 25.1.f).1.º |
| Interest | 19% | Art. 25.1.f).2.º |
| Gains on transfers of assets | 19% | Art. 25.1.f).3.º |
| Royalties (cánones) and other income taxed at the general rate | 24% general; 19% for residents of an EU or EEA state with effective exchange of tax information | Art. 25.1.a) |

The payer withholds the amount of the tax due under these rates or the applicable tax treaty (art. 31.2). No withholding applies to income exempt under art. 14 or a treaty (art. 31.4.a). Check the treaty rate before withholding.

## Section 3 -- Liquidation Pipeline (Modelo 200)

The IS computation follows this pipeline:

```
1. Resultado contable (accounting profit)
   + Ajustes positivos (non-deductible expenses, amortization differences)
   - Ajustes negativos (exempt income, timing differences)
   - Reserva de capitalización (Art. 25 LIS)
   = Base imponible previa
   - Reserva de nivelación (Art. 105 LIS, ERD only)
   - Compensación BINs (Art. 26 LIS)
   - RIC Canarias (if applicable)
   = Base imponible (floor: EUR 0)
   × Tipo de gravamen (rate table above)
   = Cuota íntegra
   - Deducciones (I+D, IT, donativos, empleo, cine...)
   - Bonificaciones (Ceuta/Melilla, cooperativas)
   = Cuota líquida (with tributación mínima floor if applicable)
   - Retenciones e ingresos a cuenta
   - Pagos fraccionados (Modelo 202)
   = Resultado liquidación (a ingresar / a devolver)
```

## Section 4 -- Key Computations

### 4.1 Reserva de Capitalización (Art. 25 LIS)

**Reserva de Capitalización table**  _(Art. 25 LIS)_

| Fiscal Year | Reduction % | Limit (% of base previa) |
| --- | --- | --- |
| Pre-2025 | 10% of equity increase | 10% |
| 2025 (Ley 7/2024) | 20% base (up to 30% with workforce growth) | 20% |

- **2025 scale by workforce growth** — 0% workforce increase: 20% reduction; 2%+ workforce increase: 23% reduction; 5%+ workforce increase: 26.5% reduction; 8%+ workforce increase: 30% reduction  _(Art. 25 LIS)_

### 4.2 Compensación de Bases Imponibles Negativas (BINs) -- Art. 26 LIS

**BIN Compensation Limit table**  _(Art. 26 LIS)_

| INCN (Annual Revenue) | BIN Compensation Limit |
| --- | --- |
| < EUR 20M | 100% (with EUR 1M free floor) |
| EUR 20M - 60M | 70% of base imponible previa |
| ≥ EUR 60M | 50% of base imponible previa |

- **BINs expiry** — BINs never expire (no time limit since 2015 reform).  _(Art. 26 LIS)_

### 4.3 Reserva de Nivelación (Art. 105 LIS) -- ERD Only

- **Reserva de Nivelación** — Only for companies with INCN < EUR 10M: Reduces base imponible by up to 10% (max EUR 1,000,000); must be added back within 5 years if not offset by future losses; effectively allows 'advance' loss compensation.  _(Art. 105 LIS)_

### 4.4 Deducciones en Cuota

**Deducciones en Cuota table**

| Deduction | Rate | Limit (% of cuota) | Reference |
| --- | --- | --- | --- |
| I+D (Investigación y Desarrollo) | 25% of expenditure | 25% of cuota íntegra | Art. 35.1 LIS |
| I+D (exceso sobre media 2 años) | 42% of excess | Included in 25% limit | Art. 35.1.b LIS |
| I+D personal investigador | +17% of researcher costs | Included | Art. 35.1.b LIS |
| I+D inmovilizado afecto | +8% of dedicated assets | Included | Art. 35.1.b LIS |
| IT (Innovación Tecnológica) | 12% of expenditure | 25% of cuota íntegra | Art. 35.2 LIS |
| Donativos mecenazgo | 40% (sociedades) | 10% of base imponible | Art. 20 Ley 49/2002 |
| Empleo discapacitados 33-65% | EUR 9,000 per person/year of increase in average workforce with that disability | No limit | Art. 38 LIS |
| Empleo discapacitados ≥65% | EUR 12,000/employee | No limit | Art. 38 LIS |
| Producción cinematográfica española | 30%/25% (first EUR 1.5M/rest) | EUR 20M | Art. 36.1 LIS |
| Producción cinematográfica extranjera | 30% | EUR 20M (EUR 40M CSI) | Art. 36.2 LIS |

### 4.5 Bonificación Ceuta y Melilla (Art. 33.6 LIS)

- **Bonificación Ceuta y Melilla** — 50% bonificación on the cuota íntegra proportional to income generated in Ceuta/Melilla. Proportion = rentas Ceuta-Melilla / resultado contable total. Combined with 25% rate = effective ~12.5% on Ceuta/Melilla income.  _(Art. 33.6 LIS)_

### 4.6 Tributación Mínima (Art. 30 bis LIS)

**Tributación Mínima table**  _(Art. 30 bis LIS)_

| Situation | Minimum Rate (on base imponible) |
| --- | --- |
| General | 15% |
| Nueva creación (first 2 years BI+) | 10% |
| Banking/hydrocarbon entities | 18% |

- **Applicability and floor mechanism** — Applies to entities with INCN ≥ EUR 20M or in consolidated group. If cuota líquida (after deductions) < minimum, it is raised to the minimum.  _(Art. 30 bis LIS)_

## Section 5 -- Modelo 202: Pagos Fraccionados

### Two Modalities

**Two Modalities table**

| Modality | Calculation | When Used |
| --- | --- | --- |
| Art. 40.2 | 18% × (cuota íntegra - deducciones - bonificaciones - retenciones) del último ejercicio | Default for most companies |
| Art. 40.3 | 17% × base imponible del período (24% if INCN > EUR 10M) | Mandatory if INCN > EUR 6M; optional otherwise |

### Calendar

**Calendar table**

| Period | Deadline |
| --- | --- |
| 1P (Jan-Mar) | 1-20 April |
| 2P (Jan-Sep) | 1-20 October |
| 3P (Jan-Nov) | 1-20 December |

### Pago Fraccionado Mínimo (DA 14ª LIS)

- **Pago Fraccionado Mínimo** — For entities with INCN ≥ EUR 10M in modality Art. 40.3: Minimum payment: 23% of (resultado contable positivo + ajustes positivos) for the period. Banking/hydrocarbon: 25%. If calculated payment < minimum, minimum applies.  _(DA 14ª LIS)_

## Section 6 -- Non-Deductible Expenses (Gastos No Deducibles)

**Non-Deductible Expenses table**

| Expense | Art. LIS | Treatment |
| --- | --- | --- |
| Resultado contable del propio IS | Art. 15.b | Ajuste positivo |
| Multas y sanciones | Art. 15.c | Never deductible |
| Donativos y liberalidades | Art. 15.e | Generally not deductible (exceptions for promotion) |
| Retribución fondos propios | Art. 15.a | Dividends are not expense |
| Pérdidas por deterioro de participaciones | Art. 15.k | Not deductible (since 2013) |
| Gastos financieros > 30% EBITDA or EUR 1M | Art. 16 | Excess is non-deductible (carry forward) |
| Atenciones a clientes > EUR 1/1000 INCN | Art. 15.e | Excess is non-deductible, max EUR 1% of INCN |

## Section 7 -- ZEC Canarias (Zona Especial Canaria)

**ZEC Canarias table**  _(Art. 43 Ley 19/1994)_

| Feature | Value |
| --- | --- |
| Rate | 4% on base imponible up to ceiling |
| Ceiling by employees | 5 employees: EUR 1.8M; 6-10: EUR 2.7M; each +5: +EUR 1.8M |
| Minimum employees | 5 (3 in remote areas) |
| Excess above ceiling | 25% (general rate) |
| Eligible activities | Industrial, commercial, services (with exclusions) |
| Combining with RIC | Yes -- RIC further reduces base imponible |

## Section 8 -- Worked Example: Standard SL

**Input:** SL Consultora Digital, Madrid. Calendar year 2025. INCN EUR 500,000. Resultado contable EUR 80,000. Gastos no deducibles EUR 3,000. Incremento fondos propios EUR 20,000. BINs pendientes EUR 15,000. No I+D. Average workforce with a disability of 33% to under 65% rose by 1.0 person/year on 2024.

**Computation:**

```
1. Resultado contable:                        EUR 80,000
2. + Ajustes positivos (gastos no deducibles): EUR 3,000
3. - Ajustes negativos:                        EUR 0
4. - Reserva capitalización (20% × 20,000):   EUR 4,000
   = Base imponible previa:                    EUR 79,000
5. - Compensación BINs (100%, free floor 1M):  EUR 15,000
   = Base imponible:                           EUR 64,000
6. Tipo gravamen: Microempresa (INCN < 1M), period starting in 2025 (LIS DT 44ª.1)
   - First EUR 50,000 × 21% =                 EUR 10,500
   - Remaining EUR 14,000 × 22% =             EUR 3,080
   = Cuota íntegra:                            EUR 13,580
7. - Deducción empleo discapacidad (1 × 9,000): EUR 9,000
   = Cuota líquida:                            EUR 4,580
8. - Retenciones:                              EUR 0
   - Pagos fraccionados:                       EUR 0
   = Resultado liquidación:                    EUR 4,580 (a ingresar)

Tipo efectivo: 4,580 / 80,000 = 5.725%
```

Step 7 depends on the workforce increase: LIS art. 38.1 grants EUR 9,000 per person/year of increase on the prior period, not per employee. Without an increase the deduction is EUR 0, and EUR 13,580 is payable (16.975%).

## Section 9 -- Filing Obligations

**Filing Obligations table**

| Modelo | Who Must File | Deadline |
| --- | --- | --- |
| 200 | All entities subject to IS | 25 July (calendar year) |
| 202 | Entities with cuota líquida > 0 in prior year OR INCN > EUR 6M | April/October/December |
| 220 | Consolidated groups | 25 July |
| 232 | Related-party transactions > EUR 250K | November |

### Exempt from filing Modelo 200:

- Entities fully exempt (Art. 9.1 LIS): State, CCAA, local entities
- Partially exempt entities with income exclusively from exempt sources, no withholdings, and no non-exempt income

## Section 10 -- Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown territory | Common territory (Madrid) |
| Unknown INCN | General rate (25%) |
| Unknown entity type | SL (standard) |
| Unknown fiscal year | 2025 |
| Unknown BINs | EUR 0 (no compensation) |
| Amortización fiscal unknown | Same as contable (no adjustment) |
| Unknown if nueva creación | NOT nueva creación (higher rate) |
| ERD vs general unknown | General (higher rate) |

## PROHIBITIONS

- NEVER apply microempresa rates to entities with INCN ≥ EUR 1,000,000
- NEVER apply nueva creación rate beyond the first 2 fiscal years with positive base imponible
- NEVER compensate BINs beyond the percentage limit for the entity's INCN bracket
- NEVER exceed the 25% cuota íntegra limit for I+D/IT/donations combined
- NEVER forget tributación mínima for entities with INCN ≥ EUR 20M or consolidated groups
- NEVER apply ZEC 4% rate without verifying the employment ceiling
- NEVER deduct multas, sanciones, or retribución de fondos propios
- NEVER apply the microempresa rates of 17%/20% (LIS art. 29.1) to periods starting before 2027: periods starting in 2025 take 21%/22% and periods starting in 2026 take 19%/21% (LIS DT 44ª.1 and .2)
- NEVER apply common territory IS rates to entities fiscally domiciled in foral territories
- NEVER confuse IRPF (personal) with IS (corporate) -- completely different regimes

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
