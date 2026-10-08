---
name: venezuela-income-tax
description: Use this skill whenever asked about Venezuela personal income tax (ISLR — Impuesto Sobre la Renta) for resident or non-resident individuals, self-employed professionals, and contractors. Trigger on phrases like "how much ISLR do I pay", "Venezuela income tax", "declaración definitiva de rentas", "Unidad Tributaria", "UT", "tarifa 1", "sustraendo", "desgravamen único", "rebajas personales", "RIF", "SENIAT", "estimated return", "declaración estimada", "retención ISLR", "self-employed tax Venezuela", "bonos vs salario", or any question about filing or computing ISLR for an individual in Venezuela. Also trigger when preparing or reviewing a Venezuelan annual income tax return, computing deductions in Tax Units, or advising on withholding and social-security parafiscal contributions. This skill covers the UT mechanism, the Tarifa Nº 1 graduated schedule, sustraendos, standard vs itemized deductions, personal credits, the 31 March deadline, social-security/parafiscal regimes, and the hyperinflationary dual-track measurement reality. ALWAYS read this skill before touching any Venezuela income tax work.
version: 0.1
jurisdiction: VE
tax_year: 2025
last_updated: 2026-10-08
reviewed_by: Jose Padilla
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Venezuelan Income Tax (ISLR) — Individual

## Venezuelan Income Tax (ISLR) — Individual Skill v0.1

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Jose Padilla** on 2026-06-21; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.
>
> **Edited since review (2026-10-08).** Citations now point to the statutes instead of a secondary tax summary: the Ley de Impuesto Sobre la Renta as reprinted by Decreto N° 2.163 (Gaceta Oficial N° 6.210 Extraordinario, 30 December 2015; [National Assembly copy](https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-n0-2163-mediante-el-cual-se-dicta-el-decreto-con-rango-valor-y-fuerza-de-ley-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-de-impuesto-sobre-la-renta-20211019151632.pdf); "LISLR" below), its Reglamento (Decreto N° 2.507, Gaceta Oficial N° 5.662 Extraordinario, 24 September 2003; "Reglamento" below) and Decreto N° 1.808 on withholding (Gaceta Oficial N° 36.203, 12 May 1997). The statutes changed four statements: the insurance desgravamen covers hospitalisation, surgery and maternity premiums only, not life insurance (LISLR art. 57(2)); the Reglamento lets the Executive extend the 31 March deadline (arts. 146, 149); the estimated-tax rules are stated from Reglamento arts. 156 and 164; and resident professional fees paid by a company are withheld at 3%, not ~10% (Decreto 1.808 art. 9(1)(b)). These edits are not covered by the 2026-06-21 sign-off.

## Critical Structural Warning — Read First

Venezuela is a **hyperinflationary economy with a dual-track measurement system**. Three caveats govern everything below:

1. **ISLR brackets, deductions and credits are denominated in Tax Units (Unidad Tributaria / UT)**, not in bolívares directly. You must convert UT → VES using the current UT value before quoting any bolívar figure. (LISLR arts. 50, 57-59.)
2. **Penalties are NO LONGER in UT.** Since the 2020 reform of the Código Orgánico Tributario (COT Art. 91), pecuniary fines stated as a multiple are calculated using the **official exchange rate of the highest-value currency published by the BCV** (effectively the USD rate) on the **date of payment**. (COT Art. 91, 2020 reform.)
3. **The legal minimum wage (Bs. 130/month, frozen since 15 March 2022, Decreto 4.653) is economically negligible** (~USD 0.50/month by Dec 2025). The real income floor is delivered via **non-salary "bonos"** (the "ingreso mínimo integral indexado" of ~USD 160/month, announced 30 April 2025). Do NOT treat the legal minimum wage as the economic minimum, and note that bonos are excluded from the salary base for social security and largely from the ISLR salary base. (Decreto 4.653; executive announcement 30 April 2025.)

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Venezuela (Bolivarian Republic of Venezuela) |
| Tax | ISLR — Impuesto Sobre la Renta (personal income tax) |
| Currency | Bolívar (VES / Bs.) — brackets denominated in Tax Units (UT) |
| Tax year | Calendar year (1 January – 31 December) for wage earners; individuals carrying on commercial, industrial or service activities may elect another 12-month period (Reglamento art. 148) |
| Primary legislation | Ley de Impuesto Sobre la Renta (LISLR), as reprinted by Decreto N° 2.163, Gaceta Oficial N° 6.210 Extraordinario, 30 December 2015 |
| Supporting legislation | Reglamento de la LISLR (Decreto N° 2.507, 2003); Código Orgánico Tributario (COT); Decreto 1.808 (ISLR withholdings, 1997); SNAT/2025/000048 (UT value) |
| Tax authority | SENIAT — Servicio Nacional Integrado de Administración Aduanera y Tributaria |
| Social security authority | IVSS — Instituto Venezolano de los Seguros Sociales (plus parafiscal regimes) |
| Tax ID | RIF — Registro Único de Información Fiscal (issued by SENIAT, no fee) |
| Filing deadline | 31 March of the following year: three months after the end of the tax year (Reglamento art. 146); the Ministry of Finance may extend it by resolution (art. 149) |
| Tax Unit (UT) value | VES 43.00 per UT (SNAT/2025/000048, Official Gazette 2 June 2025) |
| Top marginal rate (residents) | 34% (Tarifa Nº 1, LISLR) |
| Non-resident flat rate | 34% on Venezuelan-source income (LISLR art. 50, Parágrafo Único) |
| Validated by | Verified by Jose Padilla (CPA) on 2026-06-21 |
| Validation date | Verified by Jose Padilla (CPA) on 2026-06-21 |
| Skill version | 0.1 |

### Tax Unit (UT) — the master variable

**Tax Unit (UT) — the master variable**

| Field | Value | Source |
| --- | --- | --- |
| Current UT value | VES 43.00 | SNAT/2025/000048, Official Gazette 2 June 2025, effective same date |
| Previous UT value | VES 9.00 | SNAT (prior ruling) |
| Increase | ~377.8% | Derived from VES 9.00 → VES 43.00 |

- **UT setting mechanism and conversion** — The UT is set by SENIAT administrative ruling on no fixed schedule. ISLR brackets, deductions, credits and filing thresholds are all expressed in UT. Convert UT → VES at VES 43.00/UT for the 2025 reporting cycle.

### Resident Graduated Rate Schedule (Tarifa Nº 1)

**Resident Graduated Rate Schedule (Tarifa Nº 1)**  _(LISLR art. 50, Tarifa Nº 1; sustraendos derived from the bands)_

| Taxable income (UT) | Rate | Sustraendo (UT) | Cumulative tax at top of band (UT) |
| --- | --- | --- | --- |
| 0 – 1,000 | 6% | 0 | 60 |
| 1,000 – 1,500 | 9% | 30 | 105 |
| 1,500 – 2,000 | 12% | 75 | 165 |
| 2,000 – 2,500 | 16% | 155 | 245 |
| 2,500 – 3,000 | 20% | 255 | 345 |
| 3,000 – 4,000 | 24% | 375 | 585 |
| 4,000 – 6,000 | 29% | 575 | 1,165 |
| Over 6,000 | 34% | 875 | — |

- **Tax formula and continuity note** — Tax = (rate × taxable income in UT) − sustraendo, then × UT value for the VES figure. The sustraendos make the schedule continuous (each band's cumulative tax at its ceiling equals the next band's value at the same point — verified).  _(LISLR art. 50 taxes each fraction at its band rate; the sustraendo restates that as one rate less a fixed amount)_

### Non-Resident Rates (flat, withheld at source)

**Non-Resident Rates (flat, withheld at source)**  _(LISLR arts. 39, 50; Decreto 1.808 arts. 3, 9)_

| Income type | Rate | Effective rate | Source |
| --- | --- | --- | --- |
| Salary / services performed in Venezuela | 34% flat | 34% of gross | LISLR art. 50, Parágrafo Único; Decreto 1.808 art. 3 (34% of the total paid) |
| Professional non-business activities | 34% on 90% of gross | ~30.6% of gross | LISLR art. 39 (net income is 90% of gross); Decreto 1.808 art. 9(1)(a) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP — do not apply a rate basis without residency (worldwide vs Venezuelan-source) |
| Unknown deduction method | Standard deduction (desgravamen único 774 UT) — blocks itemized |
| Unknown whether income is salary or non-salary bono | Treat as bono (excluded from salary base) only if explicitly confirmed; otherwise treat as salary |
| Unknown UT value for a prior year | STOP — confirm the UT ruling in force for that tax year |
| Unknown business-use % | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown taxpayer marital/dependant status | Apply taxpayer credit (10 UT) only; do not assume spouse/dependant credits |
| Unknown VES amount where only UT is given | Convert at VES 43.00/UT (2025) and flag the UT value used |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable / Recommended / Ideal inputs and refusal** — **Minimum viable** — bank statement(s) for the full tax year (PDF, CSV, or pasted text), confirmation of residency status (resident worldwide / non-resident Venezuelan-source), and the RIF status of the individual. **Recommended** — invoices issued and received, ISLR withholding certificates (comprobantes de retención), prior-year declaración definitiva de rentas, confirmation of marital/dependant status for credits, and the UT value in force for the year. **Ideal** — complete income and expenditure record, documentation for any itemized desgravámenes (education, insurance, medical, mortgage interest, rent), social-security/parafiscal payment records, and any estimated-return (declaración estimada) filings. **Refusal if minimum is missing — SOFT WARN.** No bank statement at all = hard stop. Bank statement without supporting documents = proceed with reviewer warning: "This ISLR computation was produced from bank statement alone. The reviewer must verify residency basis, that any itemized desgravámenes are documented and paid to Venezuelan entities where required, and that bonos vs salary classification is correct."

### Refusal Catalogue

- **R-VE-1 — Residency unknown** — Residency determines whether worldwide or only Venezuelan-source income is taxed. This skill cannot compute ISLR without it. Please confirm resident vs non-resident status before proceeding.
- **R-VE-2 — Companies / partnerships / group structures** — This skill covers individuals (including self-employed professionals and contractors) only. Companies and other entities follow corporate ISLR rules. Escalate to a Venezuelan licensed tax professional.
- **R-VE-3 — Prior-year or future-year UT value not confirmed** — ISLR brackets are denominated in Tax Units. Without the UT value in force for the relevant tax year, no bolívar figure can be produced. Confirm the SENIAT UT ruling for that year before proceeding.
- **R-VE-4 — Penalties / SENIAT enforcement** — COT penalties are calculated in multiples of the BCV highest-value-currency exchange rate at the date of payment and can be severe (150–300×). Do not advise on penalty exposure. Escalate to a Venezuelan licensed tax professional immediately.
- **R-VE-5 — Hyperinflation / inflationary-adjustment accounting** — Inflationary adjustment (ajuste por inflación) and multi-currency measurement issues require specialised analysis. Out of scope for individual salary/professional ISLR. Escalate.
- **R-VE-6 — VAT (IVA) return requested** — This skill covers ISLR (income tax) only. Venezuelan IVA is a separate 16% regime; use a dedicated VAT skill or escalate.

## Section 3 — Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5. Match by case-insensitive substring on the counterparty name or description as it appears in the statement. If multiple patterns match, use the most specific.

Note: Venezuelan bank statements are typically in **bolívares (VES / Bs.)**; some accounts and payments operate in **USD**. Always record the currency and convert USD lines to VES at the applicable BCV rate before aggregating.

### 3.1 Income Patterns (Credits / Abonos)

**3.1 Income Patterns (Credits / Abonos)**

| Pattern | ISLR Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFERENCIA, ABONO, PAGO RECIBIDO, DEPÓSITO | Gross income (ingreso bruto) | Business/professional income | If IVA charged, extract net of 16% IVA |
| HONORARIOS, HONORARIOS PROFESIONALES, SERVICIOS | Gross income | Professional fees | Typical self-employed income |
| FACTURA, COBRO FACTURA | Gross income | Business income | Match to issued invoice |
| STRIPE, PAYPAL, WISE, BINANCE PAYOUT | Gross income | Platform/remittance payout | Verify USD vs VES; convert at BCV rate |
| SALARIO, NÓMINA, SUELDO, [employer name] | Salary income | Employment income | Resident salary base; subject to withholding |
| CESTATICKET, BONO, BONO CONTRA LA GUERRA ECONÓMICA | Review — likely EXCLUDE from salary base | Non-salary bono | Excluded from SS base and largely from ISLR salary base — flag for reviewer |
| ALQUILER, CANON DE ARRENDAMIENTO (received) | Other income | Rental income | Subject to estimated-return threshold test |
| INTERESES, RENDIMIENTOS (received) | Other income | Investment income | Investment income |
| DIVIDENDOS | Other income | Investment income | Dividend income |
| DEVOLUCIÓN ISLR, REINTEGRO SENIAT | EXCLUDE | Not income | Tax refund from prior year |

### 3.2 Expense Patterns (Debits / Cargos) — Self-Employed Business Expenses

Self-employed business expenses are deductible **under the same LISLR art. 27 deduction rules that companies use** and only against business/professional income, NOT against salary income: LISLR art. 31 treats employment remuneration itself as net income, so no deduction reduces it.

**3.2 Expense Patterns (Debits / Cargos) — Self-Employed Business Expenses**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, ARRENDAMIENTO LOCAL | Office rent | Deductible (business) | Dedicated business premises |
| HONORARIOS CONTADOR, ASESORÍA, AUDITORÍA | Professional fees paid | Deductible (business) |  |
| HONORARIOS ABOGADO, LEGAL (business) | Legal fees | Deductible (business) | Must be business-related |
| PAPELERÍA, MATERIALES DE OFICINA | Office supplies | Deductible (business) |  |
| PUBLICIDAD, MARKETING, GOOGLE ADS, META | Advertising | Deductible (business) |  |
| COMISIÓN BANCARIA, MANTENIMIENTO CUENTA | Bank charges | Deductible (business) | Business account only |
| SOFTWARE, SUSCRIPCIÓN, HOSTING, DOMINIO | Software / IT | Deductible (business) | Recurring = expense; capitalise large perpetual items per corporate rules |
| INTERNET, TELÉFONO (business %) | Telecoms | T2 — business % only | Default 0% if mixed |

### 3.3 Itemized Personal Desgravámenes (only if NOT using the 774 UT standard)

**3.3 Itemized Personal Desgravámenes (only if NOT using the 774 UT standard)**

| Pattern | Category | Treatment | Cap | Source |
| --- | --- | --- | --- | --- |
| COLEGIO, UNIVERSIDAD, MATRÍCULA (taxpayer/children <26) | Education | Itemized desgravamen | No stated cap; paid to Venezuelan educational institutes; descendants not older than 25 (no age limit for special education) | LISLR art. 57(1) |
| SEGURO HCM, HOSPITALIZACIÓN, CIRUGÍA, MATERNIDAD | Insurance premiums | Itemized desgravamen | No stated cap; hospitalisation, surgery and maternity cover only, paid to companies domiciled in Venezuela. Life insurance (SEGURO DE VIDA) is NOT a desgravamen | LISLR art. 57(2) |
| MÉDICO, ODONTÓLOGO, CLÍNICA, HOSPITAL | Medical/dental | Itemized desgravamen | No stated cap; services provided in Venezuela to the taxpayer and dependants | LISLR art. 57(3) |
| HIPOTECA, INTERESES HIPOTECARIOS (primary home) | Mortgage interest | Itemized desgravamen | 1,000 UT/year | LISLR art. 57(4) |
| ALQUILER VIVIENDA (primary/permanent home) | Rent | Itemized desgravamen | 800 UT/year | LISLR art. 57(4) |

### 3.4 Expense Patterns — NOT Deductible

**3.4 Expense Patterns — NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, COMIDA, ENTRETENIMIENTO (personal) | Personal | NOT deductible | Private living costs |
| MERCADO, SUPERMERCADO, FARMACIA (personal) | Personal | NOT deductible | Private living costs |
| MULTA, SANCIÓN, INTERESES MORATORIOS | Fines/penalties | NOT deductible | Public policy |
| PAGO ISLR, IMPUESTO SOBRE LA RENTA | Tax payments | NOT deductible | Income tax cannot reduce income |
| RETIRO PERSONAL, CONSUMO PROPIO | Drawings | NOT deductible | Not an expense |
| GASTOS DE EMPLEO (salaried) | Employment expenses | NOT deductible | No employment expenses recognised: employment remuneration is net income (LISLR art. 31) |

### 3.5 Exclusions / Tax-Account Movements

**3.5 Exclusions / Tax-Account Movements**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, ENTRE CUENTAS | EXCLUDE | Own-account transfer |
| PRÉSTAMO, ABONO A PRÉSTAMO, CAPITAL | EXCLUDE | Loan principal movement |
| RETENCIÓN ISLR, COMPROBANTE DE RETENCIÓN | Credit against liability | Withholding suffered — offsets final tax, not an expense |
| PAGO IVA, SENIAT IVA | EXCLUDE | VAT liability payment, not an expense |
| IVSS, SEGURO SOCIAL, FAOV, INCES (employee share) | Parafiscal contribution | Withheld from salary — see Section 5 |
| DECLARACIÓN ESTIMADA, ANTICIPO ISLR | Credit against liability | Estimated-tax advance, not an expense |

### 3.6 Venezuelan Banks — Statement Format Reference

**3.6 Venezuelan Banks — Statement Format Reference**

| Bank | Common patterns | Notes |
| --- | --- | --- |
| Banesco | TRANSFERENCIA, PAGO MÓVIL, COMPRA, CARGO | PDF/CSV; description holds counterparty + reference |
| Banco de Venezuela (BDV) | ABONO, CARGO, PAGO MÓVIL, COMISIÓN | PDF; date format DD/MM/AAAA |
| Mercantil | TRANSF, DÉBITO, CRÉDITO, COMISIÓN | PDF/CSV |
| BBVA Provincial | MOVIMIENTO, CARGO, ABONO | PDF |
| Zelle / USD accounts | RECEIVED, SENT | USD — convert at BCV rate before aggregating |

## Section 4 — Worked Examples

All examples use **UT value = VES 43.00** (SNAT/2025/000048).

### Example 1 — Professional fee received (resident self-employed)

**Input line:**
`15/03/2025 ; BANESCO ; ABONO TRANSFERENCIA ; CLIENTE ACME C.A. ; HONORARIOS FACTURA 0012 ; +860.000,00 ; VES`

**Reasoning:**
Professional fee for services rendered in Venezuela. If IVA was charged, the gross includes 16% IVA which is a liability to SENIAT, not income. Assuming no IVA charged here (e.g. below threshold / exempt), the full VES 860,000 is gross professional income. Convert to UT for the bracket computation: 860,000 ÷ 43 = 20,000.00 UT.

**Classification:** Gross income = VES 860,000 (20,000 UT).

### Example 2 — Standard deduction and full ISLR computation (resident)

**Input:** Resident individual, gross income 20,000 UT (VES 860,000), elects the standard deduction (desgravamen único 774 UT), married with two qualifying children.

**Reasoning (recomputed end-to-end):**
- Gross income: 20,000 UT
- Less desgravamen único: 774 UT
- Taxable income: 20,000 − 774 = 19,226 UT
- Taxable income is in the "Over 6,000" band → rate 34%, sustraendo 875 UT
- Tax = (0.34 × 19,226) − 875 = 6,536.84 − 875 = **5,661.84 UT**
- In VES: 5,661.84 × 43 = **VES 243,459.12**
- Credits (rebajas): taxpayer 10 UT + spouse 10 UT + 2 children × 10 UT = 40 UT = 40 × 43 = VES 1,720
- Tax after credits: 243,459.12 − 1,720 = **VES 241,739.12**
- Less withholdings suffered during the year: VES 5,300
- **Amount due: 241,739.12 − 5,300 = VES 236,439.12**

**Classification:** Tax due = VES 236,439.12. (Recomputed from LISLR arts. 50, 58 and 59.)

### Example 3 — Itemized desgravámenes with rent cap

**Input:** Resident, gross 8,000 UT. Documented rent on primary home VES 50,000/month × 12 = VES 600,000 = 13,953.49 UT. Education VES 86,000 = 2,000 UT. Elects itemized.

**Reasoning:**
- Rent desgravamen is **capped at 800 UT/year** (LISLR art. 57(4)). Documented rent of 13,953.49 UT exceeds the cap → allow **800 UT only**.
- Education: no stated cap → allow 2,000 UT.
- Total itemized desgravámenes: 800 + 2,000 = 2,800 UT.
- Taxable income: 8,000 − 2,800 = 5,200 UT.
- Band 4,000–6,000 → rate 29%, sustraendo 575 UT.
- Tax = (0.29 × 5,200) − 575 = 1,508 − 575 = **933 UT** = 933 × 43 = **VES 40,119.00** (before credits).

**Classification:** Rent capped at 800 UT; taxable 5,200 UT; tax 933 UT (VES 40,119.00) before rebajas.

### Example 4 — Non-resident professional fee (flat rate, withheld)

**Input line:**
`10/05/2025 ; MERCANTIL ; PAGO HONORARIOS ; CONSULTOR NO RESIDENTE ; SERVICIOS PROFESIONALES ; +200.000,00 ; VES`

**Reasoning:**
Non-resident performing professional non-business activity. Rate is 34% applied to **90% of gross** (LISLR arts. 39, 50; Decreto 1.808 art. 9(1)(a)), withheld at source.
- Base: 90% × 200,000 = VES 180,000
- Withholding: 34% × 180,000 = **VES 61,200** (effective 30.6% of gross)

**Classification:** Withholding tax = VES 61,200 (34% on 90% of gross).

### Example 5 — Cestaticket / bono received (non-salary)

**Input line:**
`28/04/2025 ; BDV ; ABONO ; CESTATICKET SOCIALISTA ; ABRIL 2025 ; +XXX,XX ; VES`

**Reasoning:**
Cestaticket and the "Bono contra la Guerra Económica" are **non-salary bonos** (ingreso mínimo integral indexado, ~USD 160/month, executive announcement 30 April 2025). They are excluded from the social-security base and largely from the ISLR salary base. Flag for reviewer — do not include in the salary base without confirmation.

**Classification:** EXCLUDE from salary base (reviewer to confirm). Not severance/aguinaldo/pension base.

### Example 6 — ISLR withholding suffered (credit, not expense)

**Input line:**
`30/06/2025 ; BANESCO ; RETENCIÓN ISLR ; CLIENTE BETA C.A. ; COMPROBANTE 2025-44 ; -X.XXX,XX ; VES`

**Reasoning:**
ISLR withheld by a client on professional fees is **not an expense** — it is a prepayment of the individual's final tax. It offsets the final liability (as in Example 2's "withholdings suffered" line). Retain the comprobante de retención.

**Classification:** Credit against final ISLR liability. NOT a deductible expense.

## Section 5 — Tier 1 Rules (When Data Is Clear)

### 5.1 Residency basis

**5.1 Residency basis**

| Status | Tax base | Source |
| --- | --- | --- |
| Resident individual | Worldwide income | LISLR art. 1 |
| Non-resident individual | Venezuelan-source income only | LISLR art. 1 |
| Foreign resident with a fixed base in Venezuela | National- and foreign-source income attributable to that base | LISLR art. 1 |

A person is non-resident if their stay does not exceed 183 days in a calendar year and they are not domiciled under the COT; a continuous stay of more than 183 days in the previous calendar year makes them resident (LISLR art. 51).

### 5.2 The graduated computation (residents)

- **Computation steps** — 1. Aggregate worldwide taxable income; convert to UT at the year's UT value (VES 43.00 for 2025). 2. Subtract deductions (standard 774 UT **or** itemized desgravámenes — not both). 3. Apply the Tarifa Nº 1 band: tax (UT) = (rate × taxable UT) − sustraendo. 4. Convert tax to VES (× 43.00). 5. Subtract personal credits (rebajas) in VES. 6. Subtract ISLR withheld and estimated-tax advances paid. 7. Result = amount due (or refund).

### 5.3 Deductions — standard vs itemized

- **Standard deduction** — Standard (desgravamen único): 774 UT/year, no documentation required. Electing it blocks itemized deductions.  _(LISLR art. 58)_
- **Itemized desgravámenes** — Itemized desgravámenes (Section 3.3): education at Venezuelan institutes (taxpayer + descendants not older than 25, no age limit for special education); hospitalisation, surgery and maternity insurance premiums paid to companies domiciled in Venezuela; medical, dental and hospital services provided in Venezuela; mortgage interest on primary home capped at 1,000 UT/year; rent on primary/permanent home capped at 800 UT/year. Payments must fall in the tax year, receipts go with the return, and amounts reimbursed by an employer or insurer, or already deducted as business costs, do not qualify.  _(LISLR art. 57 and its Parágrafos Primero and Segundo)_
- **Employment expenses and business expenses** — Employment expenses: none recognised, because employment remuneration is net income. Self-employed business expenses use the art. 27 deduction rules and offset only business income, not salary.  _(LISLR arts. 27, 31)_
- **Loss carryforward** — Up to 3 years; annual offset limited to 25% of the year's income; foreign losses offset only foreign-source income.  _(LISLR art. 55)_

### 5.4 Personal credits (rebajas) — applied after tax is computed

**5.4 Personal credits (rebajas) — applied after tax is computed**

| Credit | Amount | Source |
| --- | --- | --- |
| Taxpayer | 10 UT | LISLR art. 59 |
| Spouse not separated of property (not available when the spouses file separately) | 10 UT | LISLR art. 59(1) and Parágrafo Primero |
| Per resident ascendant or descendant (adult descendants only if unable to work, or studying and under 25) | 10 UT each | LISLR art. 59(2) |

- **VES value of each credit** — At UT = VES 43.00, each 10 UT credit = VES 430.

### 5.5 Non-resident flat rates

- **Non-resident flat rates** — Salary/services performed in Venezuela: 34% flat, withheld at source. Professional non-business activities: 34% on 90% of gross (effective ~30.6%).  _(LISLR arts. 39, 50; Decreto 1.808 arts. 3, 9(1)(a))_

### 5.6 Filing and administration

**5.6 Filing and administration**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year (wage earners); alternative 12-month period for individuals carrying on commercial, industrial or service activities | Reglamento art. 148 |
| Who must file | Resident individuals with net annual income above 1,000 UT or gross income above 1,500 UT; non-residents whatever the amount of their Venezuelan income | Reglamento art. 138; LISLR art. 79 |
| Annual return | Declaración definitiva de rentas | Reglamento art. 146 |
| Deadline | **31 March** of the following year (three months after the tax year ends); the Ministry of Finance may grant more time by resolution; special calendar for contribuyentes especiales | Reglamento arts. 146, 149 |
| Spouses | Spouses not separated of property are one taxpayer, but a married woman may file separately for employment income and professional fees; spouses with a marriage settlement or judicial separation of property file separately | LISLR art. 54; Reglamento art. 145 |
| Estimated-tax threshold (business and professional activity) | Required if prior-year net taxable income exceeded **1,500 UT**; the advance is computed on 80% of the prior year's net income | LISLR art. 80; Reglamento art. 156 |
| Estimated tax payment | 75% of the resulting tax, paid from the sixth month after the year-end in up to 6 equal monthly instalments; special taxpayers pay advances under SENIAT's separate rules for them (not traced here) | LISLR art. 85, Parágrafo Segundo; Reglamento art. 164 |
| Tax ID | RIF — issued by SENIAT, no fee, available online; required to invoice/receive payment | SENIAT registration practice (not traced to a statute here) |

### 5.7 Withholding on self-employed / professional income (Decreto 1.808)

**5.7 Withholding on self-employed / professional income (Decreto 1.808)**

| Item | Rate | Source |
| --- | --- | --- |
| Professional non-business fees paid by a company to a resident individual | 3% of the amount paid | Decreto 1.808 art. 9(1)(b) |
| Professional non-business fees paid to a company domiciled in Venezuela | 5% | Decreto 1.808 art. 9(1)(b) |
| Professional fees paid to a non-resident individual | 34% on 90% of the amount paid | Decreto 1.808 art. 9(1)(a) |
| Invalid/missing RIF | Decreto 1.808 sets no separate rate for it; any surcharge rule is unconfirmed | [RESEARCH GAP — reviewer to confirm] |
| IVA (VAT) on services | 16% standard | See the `venezuela-iva` guide, which flags the rate for confirmation |

**[RESEARCH GAP — reviewer to confirm]** The art. 9 table was read from the Pandectas Digital transcription of Decreto 1.808, not the Gazette image, and SENIAT's practice of deducting a sustraendo from resident individuals' withholding was not traced to the decree's text.

### 5.8 Social security and parafiscal contributions

Sources for the table: Reglamento General de la Ley del Seguro Social arts. 98, 109 (Decreto N° 8.922, Gaceta Oficial N° 39.912, 30 April 2012); Ley del Régimen Prestacional de Empleo art. 46 (Gaceta Oficial N° 38.281, 2005); Ley del Régimen Prestacional de Vivienda y Hábitat art. 33 as reprinted in Gaceta Oficial N° 6.805 Extraordinario, 1 May 2024; Ley del INCES arts. 49-50 (Decreto N° 1.414, Gaceta Oficial N° 6.155 Extraordinario, 19 November 2014); LOPCYMAT art. 7 (Gaceta Oficial N° 38.236, 2005); Ley de Protección de las Pensiones de Seguridad Social arts. 6-9 (Gaceta Oficial N° 6.806 Extraordinario, 8 May 2024) and Decreto N° 4.952 (Gaceta Oficial N° 42.880, 16 May 2024). The `venezuela-social-contributions` guide gives the detail.

**5.8 Social security and parafiscal contributions**

| Regime | Employee | Employer | Base | Cap |
| --- | --- | --- | --- | --- |
| Social Security (IVSS / Seguro Social Obligatorio) | 4% | 9% / 10% / 11% (by risk class) | Salary | Up to 5 urban minimum salaries |
| Unemployment (Régimen Prestacional de Empleo) | 0.5% | 2% | Normal salary of the previous month | Floor 1, ceiling 10 urban minimum salaries |
| Housing (FAOV / Ley de Vivienda y Hábitat) | 1% | 2% | Integral salary | None in the law |
| Worker training (INCES) | 0.5% (of annual utilidades, aguinaldos or year-end bonuses) | 2% of monthly normal salary paid | Employers with 5 or more workers | None |
| LOPCYMAT (workplace risk) | — (employer only) | 0.75% – 10% (risk-dependent) | Salary of each worker | Whether it is collected in practice is unconfirmed [RESEARCH GAP] |
| Pension protection contribution | — | 9% (companies and other private entities, not individuals) | Total salary and non-salary bonuses paid; per-worker base not below the indexed integral minimum income | None |

- **Employee-side total on normal wages** — Employee-side total (on normal wages): 4% + 0.5% + 1% + 0.5% = 6.0% (IVSS + unemployment + FAOV + INCES employee shares; note INCES employee share is on utilidades, not normal wages). Verify each base separately before summing — bases differ.

**Minimum-salary reference for caps:** VES 130/month since 15 March 2022 (Decreto N° 4.653 art. 1, Gaceta Oficial N° 6.691 Extraordinario). **[RESEARCH GAP — reviewer to confirm]** whether caps are administratively indexed to the USD-160 integral income in practice.

### 5.9 Penalties (COT)

- **Mechanism (confirmed)** — Pecuniary fines stated as a multiple are calculated using the official exchange rate of the highest-value currency published by the BCV (effectively USD) at the date of payment (COT Art. 91, 2020 reform). Late payment accrues interest at the active market rate × 1.2.  _(COT Art. 91, 2020 reform)_

**Penalties (COT) table**

| Infraction | Order of magnitude | Source |
| --- | --- | --- |
| Late filing of a return / withholding declaration | ~100–150× the highest-value-currency rate (ISLR withholding declarations cited at 150×) | Grant Thornton COT schedule; TSJ case law |
| Failure to file declarations (formal duty, COT Art. 103/155) | 150–300× the rate | TSJ decisions |
| Underpayment (material) + interest | Applies in addition | COT |

**[RESEARCH GAP — reviewer to confirm]** The full line-by-line COT penalty table was not extracted from a single primary source this session; mechanism and order of magnitude are confirmed. Parse the Grant Thornton COT PDF in full before quoting exact per-infraction multiples.

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Bono vs salary classification

- **Bono vs salary classification** — - Non-salary bonos (Cestaticket, Bono contra la Guerra Económica) are excluded from the SS base, severance, aguinaldos, vacations, pensions and largely from the ISLR salary base. - **Flag for reviewer:** confirm each credit's legal character before including/excluding from the salary base. - **Conservative default:** treat ambiguous amounts as salary unless documented as a bono.

### 6.2 Standard vs itemized deduction election

- **Standard vs itemized deduction election** — - 774 UT standard requires no documents; itemized may exceed it but needs documentation, HCM premiums paid to insurers domiciled in Venezuela and medical services provided in Venezuela. - **Flag for reviewer:** confirm which election minimises tax and that itemized support exists.

### 6.3 Home/office and mixed-use apportionment

- **Home/office and mixed-use apportionment** — - Only the business-use portion of telecoms, internet and similar mixed costs is deductible against business income. - **Conservative default:** 0% until a documented business percentage is provided.

### 6.4 Currency and BCV conversion

- **Currency and BCV conversion** — - USD-denominated income/expenses must be converted at the applicable BCV rate; the rate and date drive both the ISLR figure and any penalty exposure. - **Flag for reviewer:** confirm the conversion rate and date applied to each foreign-currency line.

### 6.5 Estimated-return obligation

- **Estimated-return obligation** — - Required only if prior-year commercial/professional/leasing income exceeded 1,500 UT. - **Flag for reviewer:** confirm prior-year activity income against the 1,500 UT threshold.

### 6.6 Self-employed expense deductibility (corporate rules)

- **Self-employed expense deductibility (corporate rules)** — - Business expenses follow corporate-tax rules and offset only business income, not salary. - **Flag for reviewer:** confirm each expense meets the corporate-deduction test and is matched to business income.

### 6.7 Loss carryforward limits

- **Loss carryforward limits** — - 3-year carryforward; annual offset capped at 25% of current-year taxable income; foreign losses offset only foreign income. - **Flag for reviewer:** confirm prior-year losses and the 25% annual cap.

## Section 7 — Excel Working Paper Template

```
VENEZUELA ISLR — INDIVIDUAL WORKING PAPER
Tax Year: 2025          UT value used: VES 43.00 (SNAT/2025/000048)
Client: ___________________________   RIF: __________________
Residency: Resident (worldwide) / Non-resident (VE-source) / Fixed base
Deduction method: Standard (774 UT) / Itemized

A. GROSS INCOME (convert all to UT)
  A1. Professional / business income (net of 16% IVA)   ______ VES  ______ UT
  A2. Salary income (excl. non-salary bonos)            ______ VES  ______ UT
  A3. Rental income                                     ______ VES  ______ UT
  A4. Investment income (interest, dividends)           ______ VES  ______ UT
  A5. TOTAL GROSS (UT)                                              ______ UT

B. DEDUCTIONS (choose ONE method)
  B1. Standard desgravamen único                                   774 UT
   -- OR itemized --
  B2. Education                                                    ______ UT
  B3. HCM insurance premiums (VE insurers)                         ______ UT
  B4. Medical / dental (services in VE)                            ______ UT
  B5. Mortgage interest (cap 1,000 UT)                             ______ UT
  B6. Rent — primary home (cap 800 UT)                             ______ UT
  B7. TOTAL DEDUCTIONS                                             ______ UT

C. TAXABLE INCOME (A5 - B)                                         ______ UT

D. TAX (Tarifa Nº 1)
  D1. Band rate ____%   Sustraendo ______ UT
  D2. Tax (UT) = (rate x C) - sustraendo                           ______ UT
  D3. Tax (VES) = D2 x 43.00                                       ______ VES

E. CREDITS (rebajas)
  E1. Taxpayer                                                     10 UT
  E2. Spouse                                                       ______ UT
  E3. Dependants ( __ x 10 UT )                                    ______ UT
  E4. TOTAL credits (UT)                            ______ UT  =  ______ VES

F. FINAL
  F1. Tax after credits (D3 - E4 in VES)                           ______ VES
  F2. Less ISLR withheld (comprobantes)                            ______ VES
  F3. Less estimated-tax advances                                  ______ VES
  F4. AMOUNT DUE / (REFUND)                                        ______ VES

REVIEWER FLAGS:
  [ ] Residency basis confirmed?
  [ ] UT value for the year confirmed (VES 43.00 for 2025)?
  [ ] Bonos vs salary classification confirmed?
  [ ] Standard vs itemized election optimal and documented?
  [ ] Itemized caps applied (mortgage 1,000 UT / rent 800 UT)?
  [ ] USD lines converted at correct BCV rate/date?
  [ ] Estimated-return threshold (1,500 UT) tested?
  [ ] Withholding (Decreto 1.808 art. 9) rate and any sustraendo confirmed?
```

## Section 8 — Bank Statement Reading Guide

### Venezuelan Bank Statement Formats

**Venezuelan Bank Statement Formats**

| Bank | Format | Key fields | Notes |
| --- | --- | --- | --- |
| Banesco | PDF, CSV | Fecha, Descripción, Débito, Crédito, Saldo | Most common; description holds counterparty + reference |
| Banco de Venezuela (BDV) | PDF | Fecha, Concepto, Monto, Saldo | State bank; pago móvil common |
| Mercantil | PDF, CSV | Fecha valor, Descripción, Débito, Crédito |  |
| BBVA Provincial | PDF | Fecha, Movimiento, Monto, Saldo |  |
| USD / Zelle accounts | varies | Date, Counterparty, Amount (USD) | Convert at BCV rate before aggregating |

### Key Venezuelan Banking / Tax Terms

**Key Venezuelan Banking / Tax Terms**

| Term | English | Classification hint |
| --- | --- | --- |
| ABONO | Credit / deposit | Potential income |
| CARGO / DÉBITO | Debit | Expense — check counterparty |
| TRANSFERENCIA | Transfer | Check direction and whether own-account |
| PAGO MÓVIL | Mobile payment | Common in VE; income or expense by direction |
| HONORARIOS | Professional fees | Income (received) or expense (paid) |
| RETENCIÓN | Withholding | ISLR withheld — credit against liability |
| COMISIÓN / MANTENIMIENTO | Bank charge | Deductible (business account) |
| CESTATICKET / BONO | Food ticket / bonus | Non-salary bono — flag for reviewer |
| SALARIO / NÓMINA / SUELDO | Salary / payroll | Salary income |
| IVA | VAT | Liability movement — exclude from income |
| RIF | Tax ID | Registration reference |

## Section 9 — Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS — VENEZUELA ISLR
1. Residency: resident (taxed on worldwide income), non-resident (VE-source only),
   or foreign resident with a fixed base in Venezuela?
2. Do you have an active RIF? (Required to invoice/receive payment.)
3. Deduction method: standard 774 UT, or do you want to itemize?
4. If itemizing: education, insurance, medical, mortgage interest, rent paid?
   (Only hospitalisation/surgery/maternity cover from Venezuelan insurers and
   medical services provided in Venezuela qualify; life insurance does not.)
5. Marital/dependant status: spouse? how many qualifying dependants?
6. Any non-salary bonos received (Cestaticket, Bono contra la Guerra Económica)?
7. ISLR withheld during the year (do you have comprobantes de retención)?
8. Did prior-year commercial/professional/leasing income exceed 1,500 UT?
   (Determines estimated-return obligation.)
9. Any foreign-currency (USD) income or expenses to convert at the BCV rate?
10. Are you classified by SENIAT as a contribuyente especial (special calendar)?
```

## Section 10 — Reference Material

### Key References

**Key References**

| Topic | Reference |
| --- | --- |
| Tax Unit (UT) value | SNAT/2025/000048, Official Gazette 2 June 2025 — VES 43.00/UT |
| Graduated rates (Tarifa Nº 1) | Ley de Impuesto Sobre la Renta (LISLR) |
| Deductions / desgravámenes | LISLR arts. 57-58 |
| Personal credits (rebajas) | LISLR art. 59 |
| Filing / administration | LISLR arts. 54, 79-85; Reglamento arts. 138, 145-149, 156, 164 — 31 March deadline, 1,500 UT estimated threshold |
| ISLR withholdings | Decreto 1.808 arts. 2-3, 9 (Gaceta Oficial N° 36.203, 12 May 1997; [Pandectas Digital transcription](https://pandectasdigital.blogspot.com/2016/10/reglamento-parcial-de-la-ley-de.html)) |
| Social security / parafiscal | Reglamento General de la Ley del Seguro Social arts. 98, 109; Ley del Régimen Prestacional de Empleo art. 46; Ley del Régimen Prestacional de Vivienda y Hábitat art. 33; Ley del INCES arts. 49-50; LOPCYMAT art. 7; Ley de Protección de las Pensiones de Seguridad Social and Decreto N° 4.952 (Section 5.8) |
| Penalties | Código Orgánico Tributario (COT), Art. 91 (2020 reform); Grant Thornton COT schedule — **[RESEARCH GAP — full table]** |
| Minimum wage | Decreto 4.653 (15 March 2022) — VES 130/month |
| Income floor (bonos) | Executive announcement 30 April 2025 — "ingreso mínimo integral indexado" ~USD 160/month |
| VAT (IVA) | 16% standard (see the `venezuela-iva` guide) |

### UT → VES Conversion Reference (2025)

**UT → VES Conversion Reference (2025)**

| UT figure | VES at 43.00/UT |
| --- | --- |
| 1 UT | VES 43.00 |
| 10 UT (one credit) | VES 430.00 |
| 774 UT (standard deduction) | VES 33,282.00 |
| 800 UT (rent cap) | VES 34,400.00 |
| 1,000 UT (mortgage cap) | VES 43,000.00 |
| 1,500 UT (estimated threshold) | VES 64,500.00 |

### Test Suite

**Test 1 — Standard deduction, top band.**
Input: Resident, gross 20,000 UT, standard 774 UT, married + 2 children, withholding VES 5,300.
Expected: taxable 19,226 UT; tax = (0.34 × 19,226) − 875 = 5,661.84 UT = VES 243,459.12; credits 40 UT = VES 1,720; after credits VES 241,739.12; less VES 5,300 → **due VES 236,439.12**.

**Test 2 — Itemized with rent cap.**
Input: Resident, gross 8,000 UT, documented rent 13,953.49 UT, education 2,000 UT, itemized.
Expected: rent capped at 800 UT; deductions 2,800 UT; taxable 5,200 UT; band 4,000–6,000 (29%, sustraendo 575); tax = (0.29 × 5,200) − 575 = **933 UT = VES 40,119.00** before credits.

**Test 3 — Bottom band.**
Input: Resident, gross 1,500 UT, standard 774 UT.
Expected: taxable 726 UT; band 0–1,000 (6%, sustraendo 0); tax = 0.06 × 726 = **43.56 UT = VES 1,873.08** before credits.

**Test 4 — Non-resident professional fee.**
Input: Non-resident professional fee VES 200,000.
Expected: base 90% = VES 180,000; tax 34% = **VES 61,200** withheld (effective 30.6%).

**Test 5 — Non-resident salary.**
Input: Non-resident, salary for services in Venezuela VES 500,000.
Expected: flat 34% = **VES 170,000** withheld at source.

**Test 6 — Credits at exact band boundary.**
Input: Resident, taxable income exactly 6,000 UT, taxpayer-only credit.
Expected: use 29% band (4,000–6,000): tax = (0.29 × 6,000) − 575 = 1,165 UT; less taxpayer credit 10 UT = 1,155 UT = **VES 49,665.00**. (Confirms band continuity: the 34% band at 6,000 gives (0.34 × 6,000) − 875 = 1,165 UT — identical.)

**Test 7 — Estimated-return threshold.**
Input: Prior-year professional income 1,490 UT.
Expected: below 1,500 UT → **no estimated return required**.

## PROHIBITIONS

- NEVER quote a bolívar figure without stating the UT value used (VES 43.00 for 2025) and its source
- NEVER apply a rate basis without confirming residency (worldwide vs Venezuelan-source)
- NEVER combine the standard desgravamen (774 UT) with itemized deductions — they are mutually exclusive
- NEVER exceed the itemized caps: mortgage interest 1,000 UT, rent 800 UT
- NEVER treat the legal minimum wage (VES 130/month) as the economic income floor
- NEVER include non-salary bonos in the salary base without reviewer confirmation
- NEVER treat ISLR withheld (retención) or estimated-tax advances as deductible expenses — they are credits
- NEVER allow employment expenses as a deduction — none are recognised
- NEVER allow self-employed business expenses against salary income — only against business income
- NEVER express COT penalties in UT — they are multiples of the BCV highest-value-currency rate at the date of payment
- NEVER quote the full COT penalty table as authoritative — it is flagged [RESEARCH GAP]; quote Decreto 1.808 rates only with the sustraendo caveat in Section 5.7
- NEVER present tax calculations as definitive — always label as estimated and route to a licensed reviewer

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
