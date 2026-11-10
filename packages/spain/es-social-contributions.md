---
name: es-social-contributions
description: Use this skill whenever asked about Spanish self-employed social contributions (cuota de autonomos / RETA). Trigger on phrases like "cuota autonomos", "RETA", "social contributions Spain", "autónomo contributions", "how much do I pay as autonomo", "tarifa plana", "cese de actividad", "regularizacion cuotas", "base de cotización", "TGSS direct debit", "cuota mensual", or any question about Spanish self-employed social security. Also trigger when classifying bank statement transactions showing TGSS direct debits, cuota autonomos debits, or Seguridad Social payments. ALWAYS read this skill before touching any Spanish social contributions work.
version: 2.2
jurisdiction: ES
tax_year: 2025
last_updated: 2026-11-11
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ES Social Contributions

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Spain |
| Primary Legislation | LGSS; Real Decreto-ley 13/2022 (income-based system) |
| Supporting Legislation | Orden PJC/178/2025 (2025 rates); Orden PJC/297/2026 (2026 rates); Ley 20/2007 (Estatuto Trabajo Autonomo); Ley 35/2006 IRPF |
| Tax Authority | Tesoreria General de la Seguridad Social (TGSS) |
| Currency | EUR only |
| Total contribution rate (2025) | 31.40% |
| Total contribution rate (2026) | 31.50% (MEI 0.90%) |
| Ordinary tarifa plana | EUR 80/month before MEI in 2023–2025. For 2026, Importass shows EUR 88.64 including MEI. Reconcile the assessment under Rule 5. |
| Payment frequency | Monthly (last business day of current month) |
| Payment method | Domiciliacion bancaria (direct debit) -- mandatory |
| 15 income tranches | Tranche 1 (<=EUR 670/mo) to Tranche 15 (>EUR 6,000/mo) |
| Maximum base (2025) | EUR 4,909.50/month |
| Maximum base (2026) | EUR 5,101.20/month |
| Autonomo societario ordinary minimum base | Period and category specific. See Rule 6. |
| Base change windows | 6 per year (Feb, Apr, Jun, Aug, Oct, Dec) |
| Regularisation | Automatic after IRPF filing |
| Contributor | Open Accountants |
| Validated by | Pending -- requires sign-off by qualified asesor fiscal |
| Validation date | Pending |

**Read this whole section before computing or classifying anything.**

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown persona fisica vs societario | Ask -- minimum base rules differ |
| Unknown net income estimate | STOP -- income estimate required for tranche |
| Unknown whether first-time autonomo | Ask -- tarifa plana eligibility |
| Unknown 7% vs 3% deduction | Establish the statutory category and days in RETA. See Rule 1. |

### Required inputs

**Minimum viable** -- type (persona fisica or societario), estimated monthly net income (rendimientos netos), and whether first registration.

**Recommended** -- bank statements showing TGSS debits, date of alta, prior RETA registration history, IRPF declaration.

**Ideal** -- complete IRPF data, TGSS Informe de Bases de Cotizacion, alta/baja history.

### Refusal catalogue

- **R-ES-SC-1 -- Disability regimes** — Trigger: client has disability affecting contribution rates. Message: "Disability contribution regimes require case-specific TGSS assessment. Escalate."
- **R-ES-SC-2 -- Cross-border posted workers** — Trigger: client posted from another EU country. Message: "EU social security coordination applies. Escalate."
- **R-ES-SC-3 -- Mutuas MATEPSS specifics** — Trigger: client asks about specific Mutua benefits or coverage details. Message: "Mutua-specific benefit calculations are out of scope. Contact the relevant Mutua."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to RETA contributions.

### 3.1 TGSS direct debits (monthly cuota)

**TGSS direct debits (monthly cuota)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TGSS, TESORERIA GENERAL | EXCLUDE -- RETA cuota | Monthly autonomo contribution |
| SEGURIDAD SOCIAL, SS | EXCLUDE -- RETA cuota | Alternative description |
| CUOTA AUTONOMOS | EXCLUDE -- RETA cuota | Explicit cuota reference |
| RETA, REG ESP TRAB AUTONOMOS | EXCLUDE -- RETA cuota | Regime name reference |
| DOMICILIACION TGSS | EXCLUDE -- RETA cuota | Direct debit description |

### 3.2 Regularisation payments (TGSS demands additional cuotas)

**Regularisation payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TGSS REGULARIZACION | EXCLUDE -- RETA regularisation | Additional cuotas demanded after IRPF filing |
| TGSS COMPLEMENTO | EXCLUDE -- RETA adjustment | Adjustment to provisional base |

### 3.3 TGSS refunds (overpayment)

**TGSS refunds**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TGSS DEVOLUCION | EXCLUDE -- RETA refund | Refund of excess cuotas |
| TGSS REINTEGRO | EXCLUDE -- RETA refund | Same |

### 3.4 Tarifa plana payments

**Tarifa plana payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TGSS with a verified reduced-contribution notice | EXCLUDE -- tarifa plana cuota | Match the payment to the TGSS assessment and contribution period. Use the amount only as a search clue. |

### 3.5 Tax authority (NOT RETA)

**Tax authority patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AEAT, AGENCIA TRIBUTARIA | EXCLUDE -- income tax/VAT | Not social contributions |
| HACIENDA | EXCLUDE -- tax | Not RETA |
| IVA, IRPF (tax reference) | EXCLUDE -- tax | Not RETA |

### 3.6 Employee social security (employer obligations)

**Employee social security patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TGSS REGIMEN GENERAL | EXCLUDE -- employee SS | Employer's obligation for employees, not the autonomo's own RETA |
| TC1, TC2 (payroll references) | EXCLUDE -- payroll SS | Employer obligations |

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical Spanish self-employed web developer.

### Example 1 -- Standard monthly RETA cuota (TGSS direct debit)

**Input line:**
`30.04.2025 ; TGSS TESORERIA GENERAL ; ADEUDO ; CUOTA AUTONOMOS ABR 2025 ; -425.85 ; EUR`

**Reasoning:**
Matches "TGSS" + "CUOTA AUTONOMOS" (pattern 3.1). The fictional April 2025 assessment confirms a base of EUR 1,356.21, the minimum for band 10. At 31.40% this gives EUR 425.85. Exclude from VAT.

**Classification:** EXCLUDE -- RETA cuota. 100% deductible as gasto deducible in IRPF.

### Example 2 -- Tarifa plana cuota (new autonomo)

**Input line:**
`31.03.2026 ; TGSS ; ADEUDO ; CUOTA TARIFA PLANA MAR ; -88.64 ; EUR`

**Reasoning:**
The fictional March 2026 TGSS assessment identifies a full month in the initial reduced-contribution period and confirms the debit. Article 38 ter(1) covers common and occupational contingencies and exempts contributions for cessation of activity and vocational training. See Rule 5 for the MEI and the difference between the published total and the calculation.

**Classification:** EXCLUDE -- tarifa plana RETA cuota. Verify the actual paid amounts and applicable tax treatment before deducting them.

### Example 3 -- Regularisation demand from TGSS

**Input line:**
`25.09.2025 ; TGSS REGULARIZACION ; ADEUDO ; COMPLEMENTO CUOTAS 2024 ; -2,413.54 ; EUR`

**Reasoning:**
Matches "TGSS REGULARIZACION" (pattern 3.2). After 2024 IRPF filing, TGSS determined actual income placed the autonomo in a higher tranche than the provisional base used. This is the additional cuotas demanded. Due by last day of month following notification.

**Classification:** EXCLUDE -- RETA regularisation demand. Deductible in 2025 (year paid, not 2024).

### Example 4 -- TGSS refund (overpaid cuotas)

**Input line:**
`15.10.2025 ; TGSS DEVOLUCION ; ABONO ; DEVOLUCION CUOTAS 2024 ; +1,907.45 ; EUR`

**Reasoning:**
Matches "TGSS DEVOLUCION" (pattern 3.3). TGSS refunding excess cuotas because actual income was in a lower tranche. This is a CREDIT. Taxable as income in the IRPF year received (2025).

**Classification:** EXCLUDE from VAT. Taxable income in 2025 IRPF (refund of previously deducted cuotas).

### Example 5 -- AEAT tax payment (NOT RETA)

**Input line:**
`20.04.2025 ; AGENCIA TRIBUTARIA ; ADEUDO ; PAGO FRACCIONADO IRPF ; -1,500.00 ; EUR`

**Reasoning:**
Matches "AGENCIA TRIBUTARIA" (pattern 3.5). This is a quarterly IRPF instalment (pago fraccionado), NOT a social contribution. Do not classify as RETA.

**Classification:** EXCLUDE -- income tax. NOT RETA.

### Example 6 -- Employer TGSS payment (not autonomo's own RETA)

**Input line:**
`30.04.2025 ; TGSS REGIMEN GENERAL ; ADEUDO ; SS EMPLEADOS ABR ; -2,800.00 ; EUR`

**Reasoning:**
Matches "TGSS REGIMEN GENERAL" (pattern 3.6). This is the employer's social security obligation for their employees under the General Regime. It is NOT the autonomo's own RETA cuota.

**Classification:** EXCLUDE -- employer SS for employees. Not the autonomo's personal RETA contribution.

### Rule 1 -- Net income formula for tranche determination

For direct estimation, add back the owner's Social Security contributions and payments to alternative mutual schemes to the activity's net IRPF earnings. Combine the applicable earnings across activities and apply the 7% general expense deduction. Use 3% for the specified company categories when the 90-day condition is met. The statute specifies separate inputs for objective estimation, attributed income and company earnings. Use the expected monthly average for provisional band selection and the applicable regularisable period for the final calculation. [LGSS art. 308(1)(a) and (c)](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308)

### Rule 2 -- 2025 and 2026 tranche table (15 tranches)

**Tabla Reducida (Tranches 1-3)** and **Tabla General (Tranches 4-15)**.

**Tabla Reducida (Tranches 1-3)**

| Tranche | Monthly Net (EUR) | Min. Base (EUR) | Min. Cuota 2025 at 31.40% (EUR/month) | Min. Cuota 2026 at 31.50% (EUR/month) |
| --- | --- | --- | --- | --- |
| 1 | <= 670 | 653.59 | 205.23 | 205.88 |
| 2 | 670.01-900.00 | 718.95 | 225.75 | 226.47 |
| 3 | 900.01 to under 1,166.70 | 849.67 | 266.80 | 267.65 |

**Tabla General (Tranches 4-15)**

| Tranche | Monthly Net (EUR) | Min. Base (EUR) | Min. Cuota 2025 at 31.40% (EUR/month) | Min. Cuota 2026 at 31.50% (EUR/month) |
| --- | --- | --- | --- | --- |
| 4 | 1,166.70-1,300.00 | 950.98 | 298.61 | 299.56 |
| 5 | 1,300.01-1,500.00 | 960.78 | 301.68 | 302.65 |
| 6 | 1,500.01-1,700.00 | 960.78 | 301.68 | 302.65 |
| 7 | 1,700.01-1,850.00 | 1,143.79 | 359.15 | 360.29 |
| 8 | 1,850.01-2,030.00 | 1,209.15 | 379.67 | 380.88 |
| 9 | 2,030.01-2,330.00 | 1,274.51 | 400.20 | 401.47 |
| 10 | 2,330.01-2,760.00 | 1,356.21 | 425.85 | 427.21 |
| 11 | 2,760.01-3,190.00 | 1,437.91 | 451.50 | 452.94 |
| 12 | 3,190.01-3,620.00 | 1,519.61 | 477.16 | 478.68 |
| 13 | 3,620.01-4,050.00 | 1,601.31 | 502.81 | 504.41 |
| 14 | 4,050.01-6,000.00 | 1,732.03 | 543.86 | 545.59 |
| 15 | > 6,000.00 | 1,928.10 | 605.42 | 607.35 |

- **Ordinary income tables** — The 2025 and 2026 schedules use the same minimum bases and bands. The reduced table ends below EUR 1,166.70 and the general table starts at EUR 1,166.70. The orders number the 12 general bands separately. The amounts above are minimum base × standard total rate, rounded to cents. Special floors and cover can change the assessment. [2025 order, arts 18 and 37](https://www.boe.es/eli/es/o/2025/02/25/pjc178) · [2026 order, arts 18 and 37](https://www.boe.es/eli/es/o/2026/03/30/pjc297)

- **Maximum base** — Each tranche has its own maximum base (for example EUR 718.94 in tranche 1). The overall maximum, EUR 4,909.50/month (2025) and EUR 5,101.20/month (2026), applies only in tranches 14 and 15. Top cuota 2026 (tranches 14 and 15): 5,101.20 x 31.50% = EUR 1,606.88/month  _(Orden PJC/297/2026, arts 18 and 37)_

### Rule 3 -- Contribution rate breakdown (2025 and 2026)

**Contribution rate breakdown (2025 and 2026)**  _(Orden PJC/178/2025; Orden PJC/297/2026, arts 18 and 37)_

| Concept | 2025 | 2026 |
| --- | --- | --- |
| Contingencias comunes | 28.30% | 28.30% |
| Contingencias profesionales | 1.30% | 1.30% |
| Cese de actividad | 0.90% | 0.90% |
| Formacion profesional | 0.10% | 0.10% |
| MEI | 0.80% | 0.90% |
| **Total** | **31.40%** | **31.50%** |

### Rule 4 -- Cuota formula

- **Cuota mensual formula** — Cuota mensual = Base de cotizacion elegida x 31.40% (2025) or 31.50% (2026)

### Rule 5 -- Tarifa plana

Article 38 ter covers initial registration or return after at least 2 years without registration. A person who used the reduction during their earlier period needs 3 years out of the regime. Request the reduction in the registration procedure. It starts on the effective registration date and runs through the next 12 complete calendar months. Importass also instructs applicants to be current with Social Security and tax authorities and to check which benefit applies if registered in several regimes. [Ley 20/2007, art. 38 ter(1), (3) and (4)](https://www.boe.es/eli/es/l/2007/07/11/20/con/20260902#a3-5) · [Importass guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia?changeLanguage=es)

The ordinary extension covers the following 12 complete calendar months. Apply before it starts and declare expected annual net earnings below the annual minimum wage (SMI), EUR 17,094 for 2026. Test each calendar year covered by the extension. The initial period is exempt from regularisation. During the extension, the statute provides for regularisation in the affected year when earnings exceed the SMI. TGSS guidance also treats equality as loss of the extension for that year. Check the notice and the months affected. [Art. 38 ter(2), (3) and (6)](https://www.boe.es/eli/es/l/2007/07/11/20/con/20260902#a3-5) · [2026 SMI, RD 126/2026 art. 3](https://www.boe.es/eli/es/rd/2026/02/18/126) · [TGSS, Prórroga Tarifa Plana](https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24/44b5f09d-6c25-4dcd-8210-c21700c67096?changeLanguage=es)

Paragraph 9 includes qualifying partners in capital companies and worker-owned companies and worker-members of associated-work cooperatives. Check their statutory category and contribution regime. Paragraph 10 sets an initial period of 24 complete calendar months and a 36-month extension for people with disability of at least 33%, victims of gender violence and victims of terrorism. Paragraph 11 excludes the specified relatives up to the second degree and members of Catholic institutes of consecrated life in the stated regimes. [Art. 38 ter(9)–(11)](https://www.boe.es/eli/es/l/2007/07/11/20/con/20260902#a3-5)

- **2023–2025 statutory amounts before MEI** — EUR 80 per month for the ordinary reduction. For eligible paragraph 10 cases, EUR 80 through the first 24 complete calendar months and EUR 160 from month 25 while the reduction continues. The provision assigns amounts from 2026 to each year's State Budget Act. [RDL 13/2022, transitional provision 5](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482#dt-5)
- **2026 administrative guidance** — Importass shows EUR 80 plus 0.90% MEI, totalling EUR 88.64 for the ordinary initial period. The 2026 order's general-table minimum for band 1 is EUR 950.98. Applying 0.90% to that base gives EUR 8.56, whilst Importass's total implies EUR 8.64. The basis for the difference and the statutory continuation of the reduced amount remain open. RDL 3/2026 art. 3(4) carries forward the ordinary income tables. Confirm the rate, base and total on the TGSS assessment, including for cross-year or special-category periods. [Importass guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia?changeLanguage=es) · [2026 order, art. 18](https://www.boe.es/eli/es/o/2026/03/30/pjc297) · [RDL 3/2026](https://www.boe.es/eli/es/rdl/2026/02/03/3/con)

### Rule 6 -- Autonomo societario minimum

Check ordinary provisional and definitive bases separately for the covered company and family categories. The 2025 order set a EUR 1,000 monthly floor once the 90-day condition was met. In 2026 the order allows the covered worker to retain the 2025 provisional base or apply the statutory group 7 minimum, EUR 1,424.40 for 2026. The definitive floor on regularisation follows LGSS art. 308(1)(c), rule 5, with the applicable 90-day condition. Use the TGSS notice for the worker's category and period. Check Article 38 ter separately for a reduced contribution. [2025 order, art. 18(4)](https://www.boe.es/eli/es/o/2025/02/25/pjc178) · [2026 order, arts 3 and 18(4)](https://www.boe.es/eli/es/o/2026/03/30/pjc297) · [LGSS art. 308](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308)

### Rule 7 -- Payment schedule

- **Payment schedule** — Monthly. Due: last business day of current month. Mandatory domiciliacion bancaria. Late surcharge: 10% first month, 20% thereafter.

### Rule 8 -- Base change windows (6 per year)

- **Base change windows** — Submit by: end Feb (effective 1 Mar), end Apr (1 May), end Jun (1 Jul), end Aug (1 Sep), end Oct (1 Nov), end Dec (1 Jan).

### Rule 9 -- Annual regularisation (automatic)

- **Annual regularisation** — After IRPF filed, TGSS compares actual vs provisional. Underpayment: TGSS demands additional cuotas. Overpayment: TGSS refunds automatically. Additional cuotas deductible in year paid. Refunds taxable in year received.

### Rule 10 -- Tax deductibility

- **Tax deductibility** — RETA cuotas: 100% deductible as gasto deducible in IRPF. Tarifa plana cuotas: also deductible. Late surcharges and penalties: NOT deductible.

### T2-1 -- Pluriactividad (simultaneous employment + RETA)

**Trigger:** Client works as employee (Regimen General) and self-employed (RETA) simultaneously.
**Issue:** For 2026, the refund is 50% of qualifying common-contingency contributions above EUR 17,323.68, limited to 50% of the RETA common-contingency contributions paid. Count the relevant employer and worker contributions from employment. TGSS pays after regularisation within the statutory timing, subject to calculation or data exceptions. [2026 order, art. 18(8)](https://www.boe.es/eli/es/o/2026/03/30/pjc297)
**Action:** Check the calculation, actual assessment and any concurrent relief under Rule 5.

### T2-2 -- Autonomo over age 47

**Trigger:** Client aged 47+ wants specific base election.
**Issue:** Transitional provisions from pre-2023 system may restrict base choice.
**Action:** Flag for reviewer.

### T2-3 -- Large regularisation demand

**Trigger:** TGSS demands significant additional cuotas (estimated tranche far below actual).
**Issue:** Payment due by last day of month following notification. Aplazamiento possible.
**Action:** Flag for reviewer to advise on aplazamiento and whether income estimate was reasonable.

### T2-4 -- Mid-year alta (pro-rata)

**Trigger:** Client registers mid-month.
**Issue:** The reduction runs from the effective registration date. A mid-month activity start can have a different effective date, depending on the registration history and timing.
**Action:** Confirm the effective date and first month's assessed amount. [Art. 38 ter(1)](https://www.boe.es/eli/es/l/2007/07/11/20/con/20260902#a3-5) · [Importass guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia?changeLanguage=es)

### T2-5 -- Tarifa plana extension rejected

**Trigger:** Expected or actual annual net earnings reach or exceed the annual SMI in a calendar year of the extension.
**Issue:** TGSS guidance includes earnings at equality in the regularisation of the affected year. See Rule 5.
**Action:** Check the extension request, annual earnings, calendar-year overlap and assessment before selecting the contribution or adjustment.

## Section 7 -- Excel working paper template

SPAIN RETA CONTRIBUTIONS -- WORKING PAPER
Client: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Type:                          [Persona fisica / Autonomo societario]
  Gross annual revenue:          EUR [____]
  Deductible expenses:           EUR [____]
  Contributions to add back:     EUR [____]
  Net income before deduction:   EUR [____]
  Generic deduction (7%/3%):     EUR [____]
  Net income for RETA:           EUR [____]
  Monthly net:                   EUR [____]
  Applicable tranche:            [____]
  Tarifa plana eligible:         [YES/NO]
  Date of alta:                  [____]

CUOTA COMPUTATION
  Chosen base (min of tranche):  EUR [____]
  Rate:                          31.40% (2025) / 31.50% (2026)
  Monthly cuota:                 EUR [____]
  Annual cuota (12 months):      EUR [____]

OR TARIFA PLANA
  Verified period and instrument: [____]
  TGSS decision and amount:       [____]
  Total for covered payments:     EUR [____]

REGULARISATION ESTIMATE
  Actual tranche (post-IRPF):    [____]
  Actual min base:               EUR [____]
  Difference per month:          EUR [____]
  Annual adjustment:             EUR [____]
  Direction: [DEMAND / REFUND]

IRPF DEDUCTIBILITY
  Total cuotas paid:             EUR [____]
  Deductible as gasto deducible: EUR [____]

REVIEWER FLAGS
  [List any Tier 2 flags]

## Section 8 -- Bank statement reading guide

### How RETA payments appear on Spanish bank statements

**TGSS direct debits:**
- Description: "TGSS", "TESORERIA GENERAL", "SEGURIDAD SOCIAL", "CUOTA AUTONOMOS"
- Timing: Last business day of each month (current month payment)
- Amount: Consistent monthly amount (unless base changed)
- Reduced contribution: match the amount to the TGSS assessment and period

**Regularisation payments:**
- Description: "TGSS REGULARIZACION", "COMPLEMENTO CUOTAS"
- Timing: After IRPF filing (typically Sep-Dec)
- Amount: Can be large if tranche mismatch

**Refunds:**
- Description: "TGSS DEVOLUCION", "TGSS REINTEGRO"
- Direction: CREDIT (incoming)
- Amount: Varies

**Key identification tips:**
1. RETA is MONTHLY, not quarterly -- look for consistent end-of-month debits
2. Match possible reduced contributions to the relevant TGSS assessment.
3. Check the contribution period, basis and chosen base on the assessment.
4. AEAT debits are tax, not social security
5. "REGIMEN GENERAL" debits are employer SS for employees, not the autonomo's RETA

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Scan for TGSS debits** -- identify monthly pattern and amount
2. **Identify possible tarifa plana** — obtain the TGSS assessment before confirming status or amount
3. **Establish the tranche** — get the assessment, earnings and chosen base. Ordinary income bands permit overlapping base ranges.
4. **Look for regularisation** -- large TGSS debit or credit mid-year
5. **Flag missing records** — ask the reviewer to resolve any unmatched payment before filing.

## Section 10 -- Reference material

### Net income example

**2025 net income example** — A full year under direct estimation, with EUR 4,800 of owner's contributions included in deductible expenses and no other adjustment under Rule 1.

| Item | EUR |
| --- | --- |
| Gross annual revenue | 48,000 |
| Deductible expenses | 12,000 |
| Net IRPF earnings | 36,000 |
| Add back contributions | 4,800 |
| 7% general expense deduction on 40,800 | 2,856 |
| Net for RETA | 37,944 |
| Monthly | 3,162 |
| Tranche | 11 (over EUR 2,760 up to EUR 3,190) |
| Min base | EUR 1,437.91 |
| Min cuota at 31.40% | EUR 451.50/month |

### Cese de actividad (cessation benefit)

- **Cese de actividad benefit** — 70% of average contribution base of last 12 months. 4-24 months duration. Must have 12 months continuous contribution in prior 24. Voluntary cessation does NOT qualify.

### IT (sick leave) coverage

- **IT coverage** — Days 4-20: 60% of regulatory base. Day 21+: 75%. Days 1-3 not covered. Higher chosen base = higher daily benefit.

### Test suite

In 2025, persona física with monthly RETA net earnings of EUR 2,100. Band 9 minimum base EUR 1,274.51 gives EUR 400.20/month.

Use the fictional March 2026 assessment in Example 2 to reconcile EUR 88.64. A bank debit alone leaves the contribution type and period unverified.

In 2025, a covered company worker with monthly RETA net earnings of EUR 800 meets the 90-day condition and has standard cover. The EUR 1,000 floor gives EUR 314.00/month. For 2026, apply Rule 6.

In 2025, monthly RETA net earnings of EUR 8,000 fall in band 15. The EUR 1,928.10 minimum base gives EUR 605.42/month.

In a 2025 illustration with 12 identical regularisable months, a EUR 960.78 provisional base gives EUR 301.68/month. The EUR 1,601.31 definitive base gives EUR 502.81/month. The rounded monthly difference is EUR 201.13, or EUR 2,413.56 for 12 months.

In a 2025 illustration with 12 identical regularisable months, a EUR 1,356.21 provisional base gives EUR 425.85/month. If TGSS sets the definitive base at EUR 1,166.70, the maximum for reduced band 3, the illustrative contribution is EUR 366.34/month. The rounded difference is EUR 59.51, or EUR 714.12 for 12 months. Check the TGSS notice and any option to retain a higher base.

Deductibility: paid EUR 4,800 cuotas. -> 100% deductible in IRPF.

### Prohibitions

- NEVER compute without knowing persona fisica vs societario
- Determine the band's net earnings under Rule 1.
- NEVER tell client they can avoid RETA once registered
- NEVER present tarifa plana as automatic -- must apply at alta
- NEVER ignore regularisation
- NEVER advise on pluriactividad without reviewer
- NEVER present cuotas as exact without specifying chosen base
- NEVER confuse monthly payment with quarterly
- NEVER advise late surcharges are deductible
- NEVER compute IT benefits without knowing actual base of month prior to baja

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in Spain) before filing or acting upon.

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
