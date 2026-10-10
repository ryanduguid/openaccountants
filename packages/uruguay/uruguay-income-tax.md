---
name: uruguay-income-tax
description: Use this skill whenever asked about Uruguay personal income tax (IRPF) for resident individuals, employees, and the self-employed. Trigger on phrases like "how much IRPF do I pay", "Impuesto a la Renta de las Personas Físicas", "Categoría I", "Categoría II", "rentas del trabajo", "rentas del capital", "declaración jurada IRPF", "Formulario 1102", "Formulario 1103", "núcleo familiar", "deducciones IRPF", "aportes BPS", "FONASA", "monotributo", "unipersonal", "servicios personales", "IRNR", "non-resident Uruguay tax", or any question about computing or filing income tax for a Uruguayan-resident individual. Also trigger when preparing or reviewing an IRPF annual return, computing the deduction credit, or advising on BPS social-security contributions. This skill covers the IRPF dual scheme (Category I capital income at 12% flat; Category II labour income on a 0%–36% progressive scale), the deduction-credit mechanic, BPS contributions, monotributo, filing forms/deadlines, and DGI penalties. ALWAYS read this skill before touching any Uruguay income tax work.
version: 0.3
jurisdiction: UY
tax_year: 2025
tax_year_notes: "2025 (2026 scale, BPC and filing calendar stated alongside)"
last_updated: 2026-10-10
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uruguay Income Tax (IRPF) -- Resident Individual

> **The retirement contribution ceiling changes in February, not January.** BPS's historical values table ("Topes Art. 7º y 8º (Ley 16713) - C") gives UYU 288,836 from February 2026, UYU 272,564 from February 2025 and UYU 256,821 from February 2024. A January pay period therefore uses the previous year's ceiling while the BPC has already moved on 1 January. Confirm the ceiling for the pay month before using any retirement calculation below.

> **Edited 2026-10-10 (v0.3).** Citations moved from PwC Worldwide Tax Summaries to the statutes (Texto Ordenado 2023 Título 7 and Título 8, Decreto 148/007, Ley 16.713, Ley 18.211, Ley 19.689, Ley 19.690, the Código Tributario and the BPC, minimum-wage and penalty decrees) and to BPS and DGI publications. Corrections: the housing-rent relief is an 8% credit against the Category II tax, not a 6% deductible item; the mortgage relief is for loan instalments on a home costing up to UI 1,000,000, capped at 36 BPC a year; Category I interest rates follow the 2023 table (0.5% to 12%), not 3%/5%/7%; the núcleo familiar option needs no 12-minimum-salary test (that test picks the scale); the unipersonal ficto is 11 BFC (about UYU 20,328 a month in 2026), not 11 BPC; aguinaldo and salario vacacional are taxed at the top marginal rate instead of entering the scale; the FY2025 balance instalments and the 2026 penalty amounts are filled in; Ley 20.446 (Budget 2025-2029) is enacted.

## Uruguay Income Tax (IRPF) -- Resident Individual Skill v0.3

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Uruguay (República Oriental del Uruguay) |
| Tax | IRPF -- Impuesto a la Renta de las Personas Físicas |
| Currency | UYU (Uruguayan peso, $U) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Reference unit | BPC (Base de Prestaciones y Contribuciones) = **UYU 6,576/month for 2025** (Decreto N° 5/025, 10 Jan 2025) and **UYU 6,864/month for 2026** (+4.38%, from 1 Jan 2026, Decreto N° 11/026). Every peso figure in this skill is a BPC multiple — take it from the BPC of the year being taxed |
| Tax authority (income tax) | DGI -- Dirección General Impositiva |
| Social security authority | BPS -- Banco de Previsión Social |
| Basis of taxation | Territorial with an extension for capital: Uruguayan-source income (activities carried on, assets located or rights used in Uruguay) plus capital yields and the related capital gains from non-resident entities, as the Budget law rewrote that extension from 2026 (Texto Ordenado 2023, Título 7, art. 6, as amended by Ley 20.446 art. 653) |
| System | Dual / scheduler -- Category I (capital) and Category II (labour) taxed separately |
| Filing portal | DGI servicios en línea |
| Annual return forms | Formulario 1102 (individual); Formulario 1103 (núcleo familiar) (EY UY, May 2025) |
| Filing window (FY2025 filed 2026) | 29 June -- 31 August 2026, one range for every taxpayer: DGI dropped the last-digit staggering for the 2026 campaign; refunds from 28 July 2026. (FY2024 filed 2025 ran 7 July -- 28 August 2025, staggered by RUT/CI ending.) (DGI, "Calendario de la Campaña 2026 de IRPF"; EY UY) |
| Validated by | Pending -- requires sign-off by a Uruguayan contador público |
| Validation date | Pending |
| Skill version | 0.3 |

### IRPF Category II -- Labour Income (Rentas del Trabajo) -- Resident, Individual Filing

**The band widths are fixed in BPC and only the BPC moves.** The multiples
84/120/180/360/600/900/1,380 and the rates 0/10/15/24/25/27/31/36 are unchanged
for 2026; the peso columns below are those multiples times the BPC of the year.
Both years are live in the second half of 2026: the FY2025 return is filed on
the 2025 scale, and current-year withholding runs on the 2026 scale.

**Category II resident individual progressive scale -- 2026 (BPC = UYU 6,864)**

| Annual taxable income (UYU) | BPC multiple | Rate | Cumulative tax at top of band (UYU) |
| --- | --- | --- | --- |
| 0 -- 576,576 | 0 -- 84 | 0% | 0.00 |
| 576,576 -- 823,680 | 84 -- 120 | 10% | 24,710.40 |
| 823,680 -- 1,235,520 | 120 -- 180 | 15% | 86,486.40 |
| 1,235,520 -- 2,471,040 | 180 -- 360 | 24% | 383,011.20 |
| 2,471,040 -- 4,118,400 | 360 -- 600 | 25% | 794,851.20 |
| 4,118,400 -- 6,177,600 | 600 -- 900 | 27% | 1,350,835.20 |
| 6,177,600 -- 9,472,320 | 900 -- 1,380 | 31% | 2,372,198.40 |
| Over 9,472,320 | > 1,380 | 36% | -- |

**Category II resident individual progressive scale -- 2025 (BPC = UYU 6,576)**  _(Texto Ordenado 2023, Título 7, art. 48 lit. A sets the annual scale in BPC (84/120/180/360/600/900/1,380 BPC); the peso columns multiply those by Decreto N° 5/025's BPC of UYU 6,576. The monthly twelfths are in BPS Comunicado R 2/2025.)_

| Annual taxable income (UYU) | BPC multiple | Rate | Cumulative tax at top of band (UYU) |
| --- | --- | --- | --- |
| 0 -- 552,384 | 0 -- 84 | 0% | 0.00 |
| 552,384 -- 789,120 | 84 -- 120 | 10% | 23,673.60 |
| 789,120 -- 1,183,680 | 120 -- 180 | 15% | 82,857.60 |
| 1,183,680 -- 2,367,360 | 180 -- 360 | 24% | 366,940.80 |
| 2,367,360 -- 3,945,600 | 360 -- 600 | 25% | 761,500.80 |
| 3,945,600 -- 5,918,400 | 600 -- 900 | 27% | 1,294,156.80 |
| 5,918,400 -- 9,074,880 | 900 -- 1,380 | 31% | 2,272,665.60 |
| Over 9,074,880 | > 1,380 | 36% | -- |

Progressive scale, 8 brackets, 0%–36%, in both years. Cumulative figures recomputed band-by-band from the BPC multiples (see Section 5.1); each 2026 figure is the 2025 figure times 6,864/6,576.

> **A warning about secondary tables for 2026.** At least one Uruguayan advisory
> site publishes a 2026 Category II scale with nine bands and new 20% and 22%
> rates at boundaries of 24, 36, 54 and 80 BPC. That structure could not be
> traced to any statute, the Ley de Presupuesto Nacional 2025-2029 (Ley 20.446)
> made no change to the labour-income scale, and its own peso columns do not
> reconcile to its own BPC multiples. DGI-sourced tables for 2026 carry the eight
> bands above. Do not adopt the nine-band scale.

### IRPF Category II -- Núcleo Familiar (Family-Unit Filing)

**Núcleo familiar scale B: each member's Category II income in the year exceeds 12 Salarios Mínimos Nacionales (SMN)**  _(Texto Ordenado 2023, Título 7, art. 48 lit. B.)_

| BPC multiple | Rate | Annual taxable income, 2026 (BPC 6,864) | Annual taxable income, 2025 (BPC 6,576) |
| --- | --- | --- | --- |
| 0 -- 168 | 0% | 0 -- 1,153,152 | 0 -- 1,104,768 |
| 168 -- 180 | 15% | 1,153,152 -- 1,235,520 | 1,104,768 -- 1,183,680 |
| 180 -- 360 | 24% | 1,235,520 -- 2,471,040 | 1,183,680 -- 2,367,360 |
| 360 -- 600 | 25% | 2,471,040 -- 4,118,400 | 2,367,360 -- 3,945,600 |
| 600 -- 900 | 27% | 4,118,400 -- 6,177,600 | 3,945,600 -- 5,918,400 |
| 900 -- 1,380 | 31% | 6,177,600 -- 9,472,320 | 5,918,400 -- 9,074,880 |
| > 1,380 | 36% | Over 9,472,320 | Over 9,074,880 |

**Núcleo familiar scale C: one member's Category II income in the year does not exceed 12 SMN**  _(Texto Ordenado 2023, Título 7, art. 48 lit. C.)_

| BPC multiple | Rate | Annual taxable income, 2026 (BPC 6,864) | Annual taxable income, 2025 (BPC 6,576) |
| --- | --- | --- | --- |
| 0 -- 96 | 0% | 0 -- 658,944 | 0 -- 631,296 |
| 96 -- 144 | 10% | 658,944 -- 988,416 | 631,296 -- 946,944 |
| 144 -- 180 | 15% | 988,416 -- 1,235,520 | 946,944 -- 1,183,680 |
| 180 -- 360 | 24% | 1,235,520 -- 2,471,040 | 1,183,680 -- 2,367,360 |
| 360 -- 600 | 25% | 2,471,040 -- 4,118,400 | 2,367,360 -- 3,945,600 |
| 600 -- 900 | 27% | 4,118,400 -- 6,177,600 | 3,945,600 -- 5,918,400 |
| 900 -- 1,380 | 31% | 6,177,600 -- 9,472,320 | 5,918,400 -- 9,074,880 |
| > 1,380 | 36% | Over 9,472,320 | Over 9,074,880 |

Who may opt: spouses under the sociedad conyugal regime and judicially recognised concubinos (Ley 18.246 art. 4), both resident, for Category II income only, once per calendar year and not in a year in which the marriage or union is created or dissolved; they are jointly liable (Título 7, art. 8 lit. B). The 12-SMN test is not an eligibility condition: it selects scale B or scale C. Above 180 BPC both scales rejoin the individual scale. A couple that opts must file the annual return even if each has a single employer (Decreto 148/007 art. 64), and may ask the employers to cut the monthly withholding by 5% during the year (Decreto 148/007 art. 63; BPS Comunicado 24/2023 ítem 5). The SMN is UYU 23,604 for 2025 and UYU 24,572 from 1 January 2026 then UYU 25,383 from 1 July 2026 (Decretos 369/024 and 319/025), so "12 SMN" is UYU 283,248 for 2025.

### IRPF Category I -- Capital Income (Rentas del Capital)

**Category I rates**  _(Texto Ordenado 2023, Título 7, art. 37, in the wording of Ley 20.075 art. 485 (from 1 January 2023) and Ley 20.446 art. 653 (from 2026); Decreto 148/007 art. 33.)_

| Item | Rate |
| --- | --- |
| Residual rate: rents, royalties, capital gains, interest not listed below | 12% |
| Interest on deposits with local financial institutions, and on publicly issued, exchange-listed bonds, debt securities and financial-trust certificates of resident issuers, in pesos at a fixed nominal rate: one year or less / more than one and up to three years / more than three years | 5.5% / 2.5% / 0.5% |
| The same instruments in pesos with an indexation clause (UI): one year or less / more than one and up to three years / more than three years | 10% / 7% / 5% |
| The same instruments in foreign currency: one year or less / more than three years | 12% / 7% |
| Dividends and profits paid or credited by IRAE taxpayers, and deemed (ficto) dividends under art. 19 | 7% |
| Copyright royalties on literary, artistic or scientific works | 7% |
| Capital yields from non-resident entities earned by a new resident who took the art. 24 lit. b) option | 7% |

The reduced rates are instrument-specific; everything else in Category I is 12%. Public-debt interest is exempt (art. 38 lit. A). The foreign-currency row for terms of more than one and up to three years is printed without a rate in every official text read (IMPO's Título 7 and Título 8 and Decreto 148/007 art. 33). [RESEARCH GAP — reviewer to confirm the foreign-currency rate for one-to-three-year terms against the gazette text of Ley 20.075 art. 485.]

### Conservative Defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown filing unit (individual vs núcleo familiar) | Individual (Formulario 1102) |
| Unknown residency | STOP -- do not apply resident scale without confirming tax residency |
| Unknown income category | STOP -- Category I (capital) and Category II (labour) use different scales |
| Unknown deduction-credit rate (14% vs 8%) | 8% (higher-income default; less favourable to taxpayer) |
| Unknown dependent-child status | 0 children (no fictitious child deduction) |
| Unknown self-employment regime | IRPF general (servicios personales), NOT monotributo |
| Unknown business-use % (vehicle, phone, home) | 0% |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- confirmation of tax residency, income category (labour Category II and/or capital Category I), filing unit (individual vs núcleo familiar), and either payroll/recibos de sueldo or a bank statement for the full tax year (CSV, PDF, or pasted text).

**Recommended** -- BPS contribution records (aportes), FONASA family situation, number of dependent children (and disability status), housing rent or mortgage-interest documentation, prior-year IRPF declaración jurada.

**Ideal** -- complete income statement, full BPS aportes detail by month, prior-year Formulario 1102/1103, withholding certificates from employers (retenciones), and any IRNR / foreign-income documentation.

**Refusal if minimum is missing -- SOFT WARN.** No income data at all = hard stop. Bank statement without payroll records = proceed with reviewer warning: "This IRPF computation was produced from a bank statement alone. The reviewer must confirm that BPS aportes, FONASA family situation, and the deduction credit are correctly captured, and that nothing belongs to Category I vs Category II in error."

### Refusal Catalogue

- **R-UY-1** — Tax residency unknown. (Residency determines whether the resident IRPF scale or the non-resident IRNR regime applies. This skill cannot compute tax without confirming the client is a Uruguayan tax resident. Please confirm before proceeding.)
- **R-UY-2** — Non-resident income (IRNR). (Non-resident taxation under IRNR (general rates 7%–25%; 25% for low/no-tax jurisdiction residents) has different rules and is out of scope. Escalate to a contador público.)
- **R-UY-3** — Companies / corporate income (IRAE). (Corporate and business income under IRAE is a separate tax and is out of scope. This skill covers individuals only. Escalate to a contador público.)
- **R-UY-4** — Capital gains on real estate / complex disposals. (Property and complex capital-gains computations under Category I require specialised analysis. Escalate to a contador público.)
- **R-UY-5** — New-resident tax holiday / global mobility. (The options to pay IRNR or a 7% IRPF rate on foreign capital income after a change of residence (Título 7 art. 24) are fact-specific and were rewritten by Ley 20.446 with effect from 2026. Out of scope. Escalate to a contador público.)
- **R-UY-6** — IASS (pension income tax) requested. (IASS (Impuesto de Asistencia a la Seguridad Social) on pensions/retirement income is a separate tax from IRPF and is out of scope for this skill.)
- **R-UY-7** — Arrears / DGI enforcement. (Client has outstanding tax arrears or is subject to DGI enforcement. Mora and recargos compound and are severe. Do not advise. Escalate to a contador público immediately.)

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement (Spanish terms common in Uruguayan statements). If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits / Créditos)

**Income patterns table**

| Pattern | IRPF Category | Treatment | Notes |
| --- | --- | --- | --- |
| SUELDO, HABERES, NÓMINA, REMUNERACIÓN, EMPLEADOR [name] | Category II | Labour income | Employee salary -- normally withheld at source |
| HONORARIOS, FACTURA, SERVICIOS PROFESIONALES | Category II | Labour income (servicios personales) | Independent professional fees |
| AGUINALDO, SALARIO VACACIONAL | Category II | Labour income | 13th-salary / holiday salary -- taxable |
| ALQUILER COBRADO, RENTA INMUEBLE | Category I | Capital income (rents) | 12% (Título 7 art. 37; Section 1) |
| INTERESES, INTERÉS GANADO | Category I | Capital income (interest) | 12% unless the deposit or listed bond qualifies for a rate between 0.5% and 10% by currency and term (Section 1) |
| DIVIDENDOS, UTILIDADES | Category I | Capital income (dividends) | 7% (Título 7 art. 37; Section 1) |
| DEVOLUCIÓN DGI, REINTEGRO IRPF | EXCLUDE | Not income | Prior-year tax refund |
| TRANSFERENCIA PROPIA, CUENTA PROPIA | EXCLUDE | Own-account transfer | Not income |

### 3.2 Deductible / Credit Items (Debits feeding the deduction credit)

The Uruguayan IRPF does NOT subtract deductions from the base; allowable deductions are summed and multiplied by the deduction rate (14% or 8%), and that credit reduces gross tax (Section 5.3; Título 7 art. 49). Housing rent is different: 8% of the rent paid is credited directly against the Category II tax without passing through the 14%/8% rate (Título 7 art. 51; Section 5.4). Capture these for the credit calculations, not as base reductions.

**Deductible/credit items table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| BPS, APORTE JUBILATORIO, MONTEPÍO | Deduction credit | Personal BPS pension contribution | 15% jubilatorio (Section 4; Título 7 art. 49 lit. A) |
| FONASA, APORTE FONASA | Deduction credit | Personal health contribution | Rate depends on income / family (Section 4; art. 49 lit. B) |
| FRL, FONDO RECONVERSIÓN LABORAL | Deduction credit | 0.10% employee FRL | Component of personal aportes (art. 49 lit. B) |
| FONDO DE SOLIDARIDAD | Deduction credit | Fondo de Solidaridad levy and its adicional | University graduates' levy (art. 49 lit. C) |
| ALQUILER VIVIENDA, ARRENDAMIENTO (housing) | Direct tax credit | 8% of the rent paid on the permanent home | Credited against the Category II tax, not multiplied by 14%/8%; written contract and identified landlord required (art. 51; Section 5.4) |
| HIPOTECA, CUOTA PRÉSTAMO VIVIENDA | Deduction credit | Mortgage loan instalments paid in the year (capped) | Sole permanent home costing up to UI 1,000,000; 36 BPC a year cap (art. 49 lit. E; Section 5.4) |

### 3.3 Non-Deductible / Personal (Debits)

**Non-deductible items table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SUPERMERCADO, TIENDA INGLESA, DISCO, DEVOTO | NOT deductible | Personal groceries |
| MULTA, SANCIÓN, RECARGO | NOT deductible | Fines/penalties |
| IRPF, PAGO DGI, DECLARACIÓN JURADA | NOT deductible | Tax payment is not an expense |
| RETIRO PERSONAL, CAJERO (personal), ATM | NOT deductible | Personal drawings |

### 3.4 Exclusions (Neither Income nor Deduction)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA ENTRE CUENTAS, CUENTA PROPIA | EXCLUDE | Own-account transfer |
| PRÉSTAMO, CUOTA PRÉSTAMO, AMORTIZACIÓN | EXCLUDE | Loan principal movement |
| IVA, PAGO IVA | EXCLUDE | VAT liability, not income/expense |
| PAGO A CUENTA IRPF, ANTICIPO | Credit against liability | Advance/withholding -- credit, not expense |

### 3.5 Uruguayan Banks -- Statement Format Reference

**Bank statement format reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BROU (Banco República) | TRANSFERENCIA, DÉBITO, CRÉDITO, SUELDO | PDF/CSV; date format DD/MM/YYYY |
| Itaú Uruguay | TRANSF, DÉBITO AUTOMÁTICO, COMPRA | PDF/CSV; merchant in description |
| Santander Uruguay | TRANSFERENCIA, PAGO, COBRO | PDF; counterparty in description |
| BBVA Uruguay | TRANSF, DÉBITO, ABONO | PDF/CSV |
| Scotiabank Uruguay | TRANSFER, DEBIT, PAYMENT | PDF/CSV; some English labels |
| Prex / Mi Dinero (wallets) | RECARGA, PAGO, TRANSFERENCIA | CSV export; clean counterparty names |

## Section 4 -- BPS Social Security Contributions (Industria y Comercio, dependent workers, 2025)

These are NOT income tax but are deductible items feeding the IRPF deduction credit (Section 5.3) and must be captured.

### 4.1 Jubilatorio (Pension)

**Jubilatorio rates table**  _(Ley 16.713 art. 181 (personal 15%); Ley 18.083 art. 87 (employer 7.5% generic rate, Industria y Comercio); BPS, Tasas de aportación (bps.gub.uy/835/tasas.html).)_

| Party | Rate |
| --- | --- |
| Employee (personal) | 15% |
| Employer (patronal) | 7.5% |

### 4.2 FONASA (Health) -- Employee Personal Rate

**FONASA employee rate table**  _(Ley 18.211 art. 61 (3% / 4.5% / 6%) and art. 66 (2% spouse or partner surcharge); BPS, Tasas FONASA (bps.gub.uy/10314/tasas-fonasa.html).)_

| Monthly income | Family situation | Employee rate |
| --- | --- | --- |
| ≤ 2.5 BPC | single, no children | 3% |
| ≤ 2.5 BPC | single, with children | 3% |
| ≤ 2.5 BPC | with spouse (no SNIS cover), ± children | 5% |
| > 2.5 BPC | single, no children | 4.5% |
| > 2.5 BPC | single, with children | 6% |
| > 2.5 BPC | with spouse, no children | 6.5% |
| > 2.5 BPC | with spouse, with children | 8% |

- **Employer FONASA rate** — 5% of remuneration subject to montepío, plus the Complemento de Cuota Mutual (CCM) where the 3% basic personal and 5% employer contributions fall short of the cuota mutual for the covered workers  _(Ley 18.211 art. 61 first paragraph; BPS, Tasas FONASA, which prints the CCM formula.)_
- **2.5 BPC monthly threshold value** — UYU 17,160/month in 2026 (at BPC 6,864) and UYU 16,440/month in 2025 (at BPC 6,576); the test uses all remuneration subject to contributions in the month, excluding the aguinaldo  _(Ley 18.211 art. 61; BPS, Tasas FONASA; Decreto N° 11/026 for the 2026 BPC.)_

### 4.3 Other BPS Funds

**Other BPS funds table**  _(FRL: Ley 19.689 art. 17 (0.10% for employers, workers and the State from 1 January 2019, previously 0.125%) and BPS, Fondo de Reconversión Laboral page. FGCL: Ley 19.690 art. 10 (0.025% on the materia gravada of Ley 16.713 art. 153) and BPS, Fondo de Garantía de Créditos Laborales page (employer-only, from 1 January 2019).)_

| Fund | Employee | Employer |
| --- | --- | --- |
| FRL (Fondo de Reconversión Laboral) | 0.10% | 0.10% |
| FGCL (Fondo de Garantía de Créditos Laborales) | -- | 0.025% |

The Executive may raise the FRL rate back to 0.125% after consulting the employer and worker organisations (Ley 19.689 art. 17), and may cut or suspend the FGCL contribution when the fund is sufficient (Ley 19.690 art. 10). Neither had happened on 10 October 2026 (BPS pages last updated 15 January 2019 and 12 December 2019).

### 4.4 Approximate Totals (Industria y Comercio)

**Approximate totals table**

| Party | Component breakdown | Approx. total |
| --- | --- | --- |
| Employee (personal) | 15% jubilatorio + 3%–8% FONASA + 0.10% FRL | 18.10% – 23.10% |
| Employer (patronal) | 7.5% jubilatorio + 5% FONASA + 0.10% FRL + 0.025% FGCL | 12.625% |

Employee total range arithmetic: minimum = 15 + 3 + 0.10 = 18.10%; maximum = 15 + 8 + 0.10 = 23.10%. Employer total = 7.5 + 5 + 0.10 + 0.025 = 12.625%. Employer figure excludes BSE (accident insurance), which varies by activity, and the CCM. Sources: the statutes and BPS pages cited in 4.1 to 4.3. [RESEARCH GAP — reviewer to confirm the BSE rate by activity.]

### 4.5 Contribution Ceiling (Tope de Cotización)

**Contribution ceiling table**  _(Ley 16.713 art. 7 (the three income levels, indexed); BPS, Valores actuales and Valores históricos, "Topes Art. 7º y 8º (Ley 16713) - C".)_

| Item | Value |
| --- | --- |
| Max nominal monthly income subject to jubilatorio | UYU 288,836/month from February 2026; UYU 272,564/month from February 2025 to January 2026; UYU 256,821/month from February 2024 to January 2025 |
| Max personal jubilatorio contribution | 15% of the applicable monthly ceiling: UYU 43,325.40 at 288,836; UYU 40,884.60 at 272,564 |

The ceiling is the top of the second level of Ley 16.713 art. 7 (UYU 15,000 in 1995 pesos, indexed), not a BPC multiple: it rose 5.97% in February 2026 against 4.38% for the BPC on 1 January 2026, and BPS changes it with effect from February each year. Read it off BPS's values table for the pay month. The lower levels on the same table are UYU 96,279 (level A) and UYU 144,418 (level B) from February 2026; they govern how the 15% is split between BPS and an AFAP (Ley 16.713 arts. 7 and 8 for affiliates of the mixed regime before 1 December 2023; Ley 20.130 art. 22 for later entrants), and do not change the total.

### 4.6 Minimum Wage

- **Salario Mínimo Nacional** — UYU 23,604/month from 1 Jan 2025 (+6%); UYU 24,572/month from 1 Jan 2026 (+4.1%) and UYU 25,383/month from 1 Jul 2026 (+3.3%), a 7.54% rise decreed in two steps. Used as the reference for the '12 minimum salaries' núcleo-familiar eligibility test, so the test moves mid-year in 2026 UYU  _(MTSS, "Salario Mínimo Nacional: $ 24.572 desde el 1.º de enero de 2026"; Decreto N° 319/025 of 26 Dec 2025)_

### 5.1 Category II Progressive Tax -- Cumulative Computation

**Cumulative computation table**  _(Texto Ordenado 2023, Título 7, art. 48 lit. A; band widths from BPC multiples at the 2025 BPC.)_

| Band top (UYU) | Band rate | Band width (UYU) | Tax on band (UYU) | Cumulative (UYU) |
| --- | --- | --- | --- | --- |
| 552,384 | 0% | 552,384 | 0.00 | 0.00 |
| 789,120 | 10% | 236,736 | 23,673.60 | 23,673.60 |
| 1,183,680 | 15% | 394,560 | 59,184.00 | 82,857.60 |
| 2,367,360 | 24% | 1,183,680 | 284,083.20 | 366,940.80 |
| 3,945,600 | 25% | 1,578,240 | 394,560.00 | 761,500.80 |
| 5,918,400 | 27% | 1,972,800 | 532,656.00 | 1,294,156.80 |
| 9,074,880 | 31% | 3,156,480 | 978,508.80 | 2,272,665.60 |
| above | 36% | -- | -- | -- |

- **Band tax computation formula** — tax = cumulative-at-previous-band-top + (X − previous-band-top) × band-n-rate  _(Texto Ordenado 2023, Título 7, art. 47: the sum of computable income enters the scale and each tranche bears its own rate.)_
- **Aguinaldo and salario vacacional do not enter the scale** — The sueldo anual complementario and the statutory suma para el mejor goce de la licencia are excluded from the progressive computation and taxed at a proportional rate equal to the highest marginal rate reached by the taxpayer's other labour income. Example: annual computable income of UYU 1,000,000 on the 2025 scale tops out in the 15% band, so an aguinaldo of UYU 80,000 bears 15% × 80,000 = 12,000.00.  _(Título 7 arts. 47 and 48, last paragraph; BPS Comunicado 24/2023 ítem 3.2.)_
- **Monthly withholding differs from the annual computation** — Employers withhold on a monthly twelfth of the scale and, when the month's income exceeds 10 BPC, on the part subject to personal contributions increased by 6%; the annual settlement drops that 6% and recomputes on actual income, which is why most employees above 10 BPC a month receive a refund in the ajuste anual or the annual return.  _(Decreto 148/007 arts. 60, 63 and 64; BPS Comunicado 24/2023 ítem 1.1. The payroll guide covers the monthly mechanics.)_

### 5.2 Category I Capital Income

- **Category I taxed separately** — Capital income is taxed separately at the proportional rates in Section 1 (12% residual, 7% dividends, 0.5% to 12% on listed interest by currency and term). It is NOT pooled with Category II labour income; each category is settled on its own, and losses stay within their category.  _(Texto Ordenado 2023, Título 7, arts. 11 and 37.)_

### 5.3 The Deduction Credit Mechanic (Key Uruguayan Specificity)

- **Deduction credit mechanic** — Uruguayan IRPF does NOT subtract deductions from the taxable base. Instead: 1. Sum all allowable deductions (personal pension contributions; FONASA and FRL contributions; Fondo de Solidaridad; the fictitious child deduction; capped mortgage loan instalments; CJPB health payments). 2. Multiply that sum by the deduction rate: **14%** if annual nominal income is at or below 180 BPC (the 15 BPC/month equivalent, measured without aguinaldo and salario vacacional); **8%** above that threshold. 3. Subtract the resulting credit from the gross Category II tax (from Section 5.1). The housing-rent credit (Section 5.4) is then taken against what remains.  _(Texto Ordenado 2023, Título 7, art. 49, in the wording of Ley 20.124 art. 1; Decreto 148/007 art. 58; BPS Comunicados R 2/2025 and R 5/2026. This guide previously stated 10% for the lower band; see the note below.)_

> **Corrected: the low-income deduction rate is 14%, not 10%.** Earlier versions of this file put the lower rate at 10%. Ley 20.124 (24 March 2023) raised the rate from 10% to 14% for hechos generadores from 31 December 2023, and Título 7 art. 49 and Decreto 148/007 art. 58 now read 14% and 8%. A 10% rate understates the credit by four points of the deduction sum and so overstates the tax.
- **180 BPC annual threshold (15 BPC/month equivalent)** — UYU 1,235,520 a year or UYU 102,960/month in 2026 (at BPC 6,864) and UYU 1,183,680 a year or UYU 98,640/month in 2025 (at BPC 6,576); the BPC used is the one in force on 31 December of the year  _(Título 7 art. 49; Decreto 148/007 art. 58; BPS Comunicados R 2/2025 and R 5/2026.)_

The rates are **14%** at or below 180 BPC a year (15 BPC/month, excluding aguinaldo and salario vacacional) and **8%** above it, consistent with `uruguay-payroll` and `uruguay-social-contributions`.

### 5.4 Deductible Items (for the credit) and the Rent Credit

**Deductible items table**  _(Texto Ordenado 2023, Título 7, art. 49 lits. A to F; Decreto 148/007 arts. 56 and 56 bis; DGI, "Deducciones admitidas en la liquidación del IRPF" (28 April 2023).)_

| Item | Amount |
| --- | --- |
| Personal BPS jubilatorio contribution (or CJPPU, Caja Notarial, Caja Bancaria, military and police funds, complementary pension funds) | Actual (lit. A) |
| FONASA + FRL personal contributions (and Fondo Sistema Notarial de Salud, cajas de auxilio) | Actual (lit. B) |
| Fondo de Solidaridad and its adicional | Actual (lit. C) |
| Fictitious deduction per dependent minor child (also children held under judicial custody for adoption, from 2026) | 20 BPC/year (UYU 137,280 at BPC 6,864 for 2026; UYU 131,520 at BPC 6,576 for 2025); split 100/0 or 50/50 between the parents by agreement, otherwise 50/50 (lit. D; Decreto 148/007 art. 57) |
| Fictitious deduction per child with a disability, minor or adult | 40 BPC/year (UYU 274,560 at BPC 6,864 for 2026; UYU 263,040 at BPC 6,576 for 2025) (lit. D) |
| Mortgage loan instalments (cuotas, not only interest) paid in the year on the sole permanent home, including ANV, MVOT and MEVIR promissory purchases | Actual, provided the home cost no more than UI 1,000,000 (UI 794,000 before FY2023), capped at 36 BPC a year (UYU 247,104 for 2026; UYU 236,736 for 2025); claimed in the annual return (lit. E; Decreto 148/007 art. 56 bis) |

**Housing-rent credit (not a deductible item).** A tenant of a permanent home may credit 8% of the rent actually paid and accrued in the year against the Category II tax, provided the lease is written and the landlord is identified. The credit is capped at the Category II tax of the year; any excess is neither carried forward nor refunded. Co-tenants split it by agreement, otherwise equally. The rate was 6% until FY2022 and 8% from FY2023 (Ley 20.124 art. 2).  _(Título 7 art. 51; Decreto 148/007 art. 77 bis.)_

### 5.5 Self-Employed / Independent Regimes

**Self-employed regimes table**  _(Texto Ordenado 2023, Título 7, art. 45; Ley 18.211 arts. 70 and 71; Ley 16.713 art. 173; Ley 18.083 arts. 70 to 72; BPS, Aportes mínimos: Industria y Comercio (vigencia enero 2026) and Aportación de monotributo pages.)_

| Regime | Treatment |
| --- | --- |
| Servicios personales (independent professionals and other non-dependent services outside IRAE) | IRPF Category II on 70% of gross fees: a flat 30% notional expense deduction, plus bad debts (Título 7 art. 45). FONASA is also charged at the employee rates on 70% of fees (Ley 18.211 art. 70), with monthly advances; pension contributions follow the fund (CJPPU for university professionals, BPS fictos for unipersonales) |
| Unipersonal owner without employees | Minimum fictitious base = 11 BFC (Base Ficta de Contribución, not BPC), the first of the ten categories of Ley 16.713 art. 173 (11 to 60 BFC): UYU 20,328 a month from January 2026 at BFC 1,847.96. FONASA for a unipersonal with at most five employees is charged on a 6.5 BPC ficto (Ley 18.211 art. 71) |
| Monotributo (micro-business simplified) | One payment replacing the owner's social contributions and all national taxes except import duties (Ley 18.083 art. 70). Open to unipersonales with at most one employee, two-partner de facto companies and family companies of up to three partners, selling only to final consumers from one small outlet; excluded if the owner also holds a partnership or directorship, and for personal services (arts. 70 to 72). Revenue cap: 60% of the small-enterprise IRAE limit (Título 4 art. 52 lit. E) for unipersonales, 100% for the others (art. 71 lit. A). BPS charges jubilatorio and FRL on 5 BFC, health cover optionally on 6.5 BPC, and 8% of 1 BPC when no health cover is taken; companies registered since 2021 pay 25% / 50% / 100% in their first three years |

The earlier "11 BPC" figure in this guide was a unit error: Ley 16.713 art. 173 sets the categories in Bases Fictas de Contribución, and BPS's January 2026 table shows the first category at UYU 20,328 (11 × 1,847.96). The monotributo revenue caps in pesos and the current monotributo amounts are published by BPS; read them off the BPS pages for the year.

### 5.6 Non-Resident Income (IRNR) -- Reference Only

- **IRNR rates, out of scope** — Non-residents pay IRNR on gross Uruguayan-source income at 12% (residual rate), 7% on dividends and profits from IRAE taxpayers, 25% on income of entities resident in low- or no-tax jurisdictions (other than such dividends), and the same 0.5% to 12% currency-and-term table as Category I on listed interest. Labour income is computed as for IRPF. Out of scope (see R-UY-2).  _(Texto Ordenado 2023, Título 8, arts. 13 and 18.)_

### 5.7 Filing and Payment

**Filing and payment table**  _(Texto Ordenado 2023, Título 7, art. 50; Decreto 148/007 art. 64; DGI, "Calendario de la Campaña 2026 de IRPF" (1 June 2026) and "Vencimientos 2026. Calendario general actualizado", ordinal 16; EY UY (May 2025) for the 2025 campaign.)_

| Item | Detail |
| --- | --- |
| Forms | Formulario 1102 (individual); Formulario 1103 (núcleo familiar); Formulario 1302 for the IVA servicios personales return of independent workers, same window |
| Filing window (FY2025 / 2026) | 29 June -- 31 August 2026 for every taxpayer; the pre-filled online form and the appointment agenda opened on 26 June (FY2024 / 2025 ran 7 July -- 28 August 2025, staggered by RUT/CI ending) |
| Refunds | From 28 July 2026 for returns filed before the 15th of a month, otherwise within the following month; automatic refunds for non-filers were checked from June |
| Balance payment | Up to 5 equal instalments: 31 August, 30 September, 30 October, 30 November and 30 December 2026 for the FY2025 balance (DGI 2026 calendar, ordinal 16; IASS balances may run to 7 instalments under Resolución DGI 750/2026) |
| Pure-wage single-employer earners | NOT required to file: the employer's December ajuste anual makes the withholding final (Decreto 148/007 art. 64). Filing becomes mandatory for núcleo familiar electors, for employees who asked for the 5% withholding cut, for employees with more than one employer whose nominal labour income exceeds 150,000 UI in the year, for employees not in employment on 31 December, and for independent workers (DGI, Instructivo Formulario 1102; DGI campaign notices) |

### 5.8 Penalties (DGI)

**Penalties table**  _(Código Tributario (Decreto-Ley 14.306) arts. 94 and 95; Decreto 344/025; Resolución DGI 097/026; Decreto 274/008 as amended by Decreto 23/020; BPS, Valores actuales.)_

| Item | Detail |
| --- | --- |
| Late filing of a sworn return (contravención, art. 95) | UYU 910 per late return in 2026, and at most UYU 2,730 when a taxpayer with no activity in the period files several returns at once (Resolución DGI 097/026 of 14 January 2026); applies even with zero balance. The art. 95 range for 2026 is UYU 680 to UYU 13,220 (Decreto 344/025) |
| Mora (late payment, art. 94) | Fine of 5% of the unpaid tax if paid within five business days of the due date, 10% if paid later but within 90 calendar days, 20% after 90 days; 10% when a payment plan is requested in time |
| Recargos (interest, art. 94) | Monthly surcharge set by the Executive, calculated day by day and capitalised every four months: 110% of a 70/30 blend of the BCU's latest quarterly average lending rates for large and medium companies (Decreto 274/008 art. 1). BPS published 0.80% a month for September and October 2026 |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Individual vs Núcleo Familiar Election

- Núcleo familiar filing is optional for spouses under the sociedad conyugal regime and judicially recognised concubinos, for Category II income only (Título 7 art. 8 lit. B). It is beneficial only in specific income splits.
- When each member's Category II income exceeds 12 SMN in the year, scale B applies (0% to 168 BPC, then 15% from 168 to 180 BPC); otherwise scale C applies (0% to 96 BPC, 10% to 144 BPC, 15% to 180 BPC). Both rejoin the individual scale above 180 BPC (art. 48 lits. B and C).
- The option makes the annual return mandatory for both (Decreto 148/007 art. 64).
- **Conservative default:** individual filing (Formulario 1102) until reviewer models both.
- **Flag for reviewer:** run both computations and elect the lower total.

### 6.2 Deduction-Credit Rate (14% vs 8%)

- The rate depends on whether annual labour income exceeds the 15 BPC/month equivalent.
- **Conservative default:** 8% (less favourable) until income level confirmed.
- **Flag for reviewer:** confirm the threshold crossing and applicable rate.

### 6.3 FONASA Family Situation

- The personal FONASA rate (3%–8%) depends on income relative to 2.5 BPC and on spouse/child coverage.
- **Conservative default:** confirm family situation before applying any rate above 3%.
- **Flag for reviewer:** confirm spouse SNIS coverage and number of covered children.

### 6.4 Dependent-Child Fictitious Deduction

- 20 BPC/child/year (40 BPC if disabled), splittable between parents.
- **Flag for reviewer:** confirm number of children, disability status, and any split with the other parent.

### 6.5 Servicios Personales vs Monotributo vs IRPF

- The optimal regime depends on revenue, whether the client has employees, and revenue caps.
- **Conservative default:** IRPF general (servicios personales).
- **Flag for reviewer:** confirm monotributo eligibility against current revenue caps.

### 6.6 Foreign Capital Income (Residents)

- Uruguay's quasi-territorial system taxes certain foreign capital income for residents.
- **Flag for reviewer:** confirm scope of any foreign interest/dividend income and available foreign-tax credits.

### 6.7 Housing Rent Credit / Mortgage Instalment Deduction

- 8% of the rent paid on the permanent home is a direct credit against the Category II tax, capped at that tax (Título 7 art. 51). Mortgage loan instalments on the sole permanent home (cost up to UI 1,000,000) are a deductible item capped at 36 BPC a year and feed the 14%/8% credit (art. 49 lit. E).
- **Flag for reviewer:** confirm the written lease and landlord identification for the rent credit, and the home's UI cost and the instalments paid for the mortgage deduction.

## Section 7 -- Excel Working Paper Template

URUGUAY IRPF -- WORKING PAPER
Tax Year: ______  Fill the BPC from the year being taxed:
  2026 (BPC = UYU 6,864/month)   2025 (BPC = UYU 6,576/month)
Client: ___________________________
Filing unit: Individual (F.1102) / Núcleo Familiar (F.1103)

A. CATEGORY II -- LABOUR INCOME (annual, UYU)
  A1. Salary / haberes                            ___________
  A2. Aguinaldo / salario vacacional              ___________
  A3. Honorarios / servicios personales           ___________
  A4. TOTAL gross Category II                      ___________

B. TAXABLE BASE (Category II)
  B1. Less: items excluded from base (per DGI)     ___________
  B2. Category II taxable income                   ___________

C. GROSS CATEGORY II TAX (pass to deterministic engine, Section 5.1)
  C1. Gross tax on B2                              ___________

D. DEDUCTION CREDIT (Section 5.3)
  D1. Personal BPS jubilatorio (15%)              ___________
  D2. FONASA + FRL personal                        ___________
  D3. Fictitious child deduction (20/40 BPC each)  ___________
  D4. Fondo de Solidaridad                         ___________
  D5. Mortgage loan instalments (36 BPC cap)       ___________
  D6. SUM of deductions (D1..D5)                   ___________
  D7. Deduction rate (14% at or below 180 BPC, else 8%) ___________
  D8. Deduction credit (D6 x D7)                   ___________

E. CATEGORY II TAX
  E1. Tax after deduction credit (C1 - D8, floored at 0) ___________
  E2. Less: rent credit, 8% of rent paid, capped at E1   ___________
  E3. CATEGORY II TAX DUE (E1 - E2)                      ___________

F. CATEGORY I -- CAPITAL INCOME (separate)
  F1. Rents / interest / capital gains             ___________
  F2. Rate (12% / 7% / listed-interest table)      ___________
  F3. Category I tax                               ___________

G. CREDITS
  G1. Less: withholdings / anticipos (retenciones) ___________
  G2. TOTAL IRPF DUE / REFUND (E3 + F3 - G1)       ___________

REVIEWER FLAGS:
  [ ] Tax residency confirmed?
  [ ] Filing unit modelled both ways (1102 vs 1103)?
  [ ] Deduction rate (14% vs 8%) confirmed against income?
  [ ] FONASA family situation confirmed?
  [ ] Dependent-child deduction confirmed?
  [ ] Category I vs Category II split correct?
  [ ] Tope jubilatorio applied if income > ceiling?
  [ ] Monotributo eligibility checked (self-employed)?

## Section 8 -- Bank Statement Reading Guide

### Uruguayan Bank Statement Formats

**Bank statement formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BROU (Banco República) | PDF, CSV | Fecha, Concepto/Detalle, Débito, Crédito, Saldo | Most common; description holds counterparty + reference |
| Itaú Uruguay | PDF, CSV | Fecha, Descripción, Importe, Saldo | Card transactions show merchant |
| Santander Uruguay | PDF | Fecha, Concepto, Débito, Crédito, Saldo | Counterparty in concepto field |
| BBVA Uruguay | PDF, CSV | Fecha, Movimiento, Importe, Saldo |  |
| Scotiabank Uruguay | PDF, CSV | Date/Fecha, Description, Amount | Some English labels |
| Prex / Mi Dinero | CSV | Fecha, Detalle, Monto | Wallet exports; clean names |

### Key Uruguayan Banking / Tax Terms

**Banking/tax terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| SUELDO / HABERES | Salary / wages | Category II income |
| HONORARIOS | Professional fees | Category II (servicios personales) |
| AGUINALDO | 13th-month salary | Category II income |
| ALQUILER | Rent | Category I if received; deduction-credit item if housing paid |
| INTERESES | Interest | Category I income |
| DIVIDENDOS / UTILIDADES | Dividends | Category I income (7%) |
| APORTE / MONTEPÍO | BPS contribution | Deduction-credit item (Box D) |
| FONASA | Health contribution | Deduction-credit item |
| DÉBITO AUTOMÁTICO | Direct debit | Regular expense -- check counterparty |
| TRANSFERENCIA | Transfer | Check direction for income/expense |
| RETENCIÓN | Withholding | Credit against IRPF liability |
| DEVOLUCIÓN DGI | Tax refund | Exclude -- not income |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3), separating Category I from Category II.
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1) -- individual filing, 8% deduction rate, 0 children, FONASA 3% floor.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

ONBOARDING QUESTIONS -- URUGUAY IRPF
1. Are you a Uruguayan tax resident for the full year?
2. Filing unit: individual or núcleo familiar (and does your spouse earn >= 12 minimum salaries)?
3. Income types: salary, professional fees (honorarios), rents, interest, dividends?
4. Do you have a single employer who withholds IRPF, or multiple income sources?
5. Number of dependent children (and any with a disability)?
6. FONASA family situation: single or with spouse? Does your spouse have their own SNIS coverage?
7. Do you pay housing rent or a mortgage? Amounts?
8. Self-employed? If so: servicios personales, unipersonal, or monotributo?
9. Any foreign capital income (interest/dividends abroad)?
10. Total BPS aportes and any withholdings (retenciones) for the year?

## Section 10 -- Reference Material

### Key References

**Key references table**

| Topic | Reference |
| --- | --- |
| IRPF statute (residence, scope, categories, Category I rates, Category II scales, deductions, rent credit) | Texto Ordenado 2023 (Decreto 101/024), Título 7, arts. 2, 5, 6, 8, 11, 37, 45, 47 to 51, as updated through Ley 20.446 (IMPO: impo.com.uy/bases/todgi-2023/7-2024) |
| IRPF regulations (deductions, deduction rate, advances, employer withholding, ajuste anual, rent credit) | Decreto 148/007, arts. 56, 56 bis, 57, 58, 60, 63, 64, 64 bis, 65 and 77 bis (IMPO: impo.com.uy/bases/decretos/148-2007) |
| 2023 relief law (14% deduction rate, 20 BPC per child, 8% rent credit, UI 1,000,000 home cost) | Ley 20.124 (24 March 2023) and Decreto 118/023 |
| IRPF monthly scale and values (official) | BPS Comunicado R 2/2025 (2025) and BPS Comunicado R 5/2026 (2026): valores escalas IRPF |
| DGI guidance on deductions | DGI, "Deducciones admitidas en la liquidación del IRPF" (28 April 2023) |
| BPC values | Ley 17.856; Decreto N° 5/025 (UYU 6,576); Decreto N° 11/026 (UYU 6,864); DGI, Base de Prestaciones y Contribuciones (BPC) |
| BPS contribution rates | Ley 16.713 arts. 7, 153, 173 and 181; Ley 18.083 art. 87; Ley 18.211 arts. 61, 66, 70 and 71; Ley 19.689 art. 17; Ley 19.690 art. 10; BPS Tasas, Tasas Fonasa, FRL and FGCL pages; BPS Valores actuales and Valores históricos |
| Monotributo | Ley 18.083 arts. 70 to 72; BPS (bps.gub.uy/4659, /10444, /844) |
| Minimum wage | Decreto N° 369/024 (2025); Decreto N° 319/025 (2026) |
| Filing forms / deadlines | DGI, Calendario de la Campaña 2026 de IRPF; DGI, Vencimientos 2026 calendario general, ordinal 16; EY UY (May 2025) for the 2025 campaign |
| Penalties | Código Tributario arts. 94 and 95; Decreto 344/025; Resolución DGI 097/026; Decreto 274/008 |
| Non-resident (IRNR) | Texto Ordenado 2023, Título 8, arts. 13 and 18 |

### BPC Reference Values

**BPC reference values table**

| Year | BPC (UYU/month) | Source |
| --- | --- | --- |
| 2024 | 6,177 | Decreto N° 7/024 (16 Jan 2024), per DGI's BPC table |
| 2025 | 6,576 | Decreto N° 5/025 (primary) |
| 2026 | 6,864 | Decreto N° 11/026; +4.38%, from 1 Jan 2026 |

The 2025 and 2026 values are decree-confirmed. [Decreto 11/026](https://www.impo.com.uy/bases/decretos/11-2026) sets the 2026 BPC at UYU 6,864 from 1 January, a 4.38% rise on the 2025 value fixed by Decreto 5/025. DGI's BPC table also lists UYU 6,177 for 2024 under Decreto 7/024 of 16 January 2024.

### Changes enacted for 2026 (NOT 2025-effective)

Ley 20.446 of 16 December 2025 (Presupuesto Nacional 2025-2029) rewrote the foreign-capital extension of Título 7 art. 6, added a 7% Category I rate for new residents who tax such income under the art. 24 lit. b) option, limited the original new-resident IRNR option to changes of residence up to 31 December 2025 (art. 649), and extended the child deduction to minors held under judicial custody for adoption (art. 650); DGI Resolución 665/026 of 10 March 2026 regulates the new foreign-income rules. These apply to hechos generadores from 2026. The FY2025 return is unaffected; new-resident and foreign-capital questions stay out of scope (R-UY-5 and Section 6.6).

### Test Suite

Input: Resident, individual, Category II taxable income UYU 552,384.
Expected: Gross tax = 0.00 (top of 0% band).

Input: Resident, individual, Category II taxable income UYU 1,000,000.
Expected: Cumulative to 789,120 = 23,673.60; plus (1,000,000 − 789,120 = 210,880) × 15% = 31,632.00. Gross tax = 55,305.60.

Input: Category II taxable income UYU 1,500,000.
Expected: Cumulative to 1,183,680 = 82,857.60; plus (1,500,000 − 1,183,680 = 316,320) × 24% = 75,916.80. Gross tax = 158,774.40.

Input: Gross Category II tax = 55,305.60 (from Test 2); allowable deductions sum = 180,000; deduction rate = 8%.
Expected: Credit = 180,000 × 8% = 14,400.00. Tax due = 55,305.60 − 14,400.00 = 40,905.60.

Input: Rental income UYU 240,000 (Category I, general 12%).
Expected: Category I tax = 240,000 × 12% = 28,800.00. Taxed separately from Category II.

Input: Dividends UYU 100,000 (Category I).
Expected: Tax = 100,000 × 7% = 7,000.00.

Input: Núcleo familiar, each member above 12 SMN, combined Category II taxable income UYU 1,104,768.
Expected: Gross tax = 0.00 (top of the scale B 0% band, 168 BPC).

Input: Núcleo familiar, one member at or below 12 SMN (scale C), combined Category II taxable income UYU 1,000,000 (2025).
Expected: 10% × (946,944 − 631,296 = 315,648) = 31,564.80; plus 15% × (1,000,000 − 946,944 = 53,056) = 7,958.40. Gross tax = 39,523.20.

Input: Resident, individual, Category II taxable income UYU 1,000,000 plus a statutory aguinaldo of UYU 80,000 (2025).
Expected: Gross tax on the scale = 55,305.60 (Test 2); the aguinaldo bears the top marginal rate reached, 15% × 80,000 = 12,000.00; total gross tax = 67,305.60.

Input: Category II tax after the deduction credit = 40,905.60 (Test 4); housing rent paid in the year UYU 300,000 under a written lease with the landlord identified.
Expected: Rent credit = 8% × 300,000 = 24,000.00, below the 40,905.60 cap. Category II tax due = 16,905.60.

Input: Industria y Comercio employer rates.
Expected: 7.5% + 5% + 0.10% + 0.025% = 12.625%.

## PROHIBITIONS

- NEVER apply the resident IRPF scale without confirming tax residency
- NEVER pool Category I (capital) and Category II (labour) income -- they are taxed separately
- NEVER subtract deductions from the IRPF base -- deductions feed a credit (sum × 14% or 8%) against gross tax
- NEVER multiply the housing-rent credit by the 14%/8% rate -- 8% of the rent is credited directly against the Category II tax and capped at it
- NEVER enter the aguinaldo or the salario vacacional into the progressive scale -- they bear the top marginal rate of the other labour income
- NEVER assume the 14% deduction rate -- default to 8% until the income is confirmed to be at or below the 15 BPC/month equivalent
- NEVER apply a FONASA rate above 3% without confirming income level and family situation
- NEVER apply monotributo without confirming revenue-cap eligibility
- NEVER treat IRNR (non-resident) or IRAE (corporate) income with this skill -- escalate
- NEVER treat a BPS or FONASA payment as a base reduction -- it is a deduction-credit item
- NEVER rely on a [RESEARCH GAP] figure without reviewer confirmation
- NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, contador público, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
