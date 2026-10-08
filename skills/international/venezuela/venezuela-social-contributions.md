---
name: venezuela-social-contributions
description: "Use this skill whenever asked about Venezuela social security and payroll contributions (IVSS, Paro Forzoso, FAOV, INCES, LOPCYMAT) for employers or employees. Trigger on phrases like \"how much social security do I pay in Venezuela\", \"IVSS contribution\", \"Seguro Social Obligatorio\", \"Paro Forzoso\", \"régimen prestacional de empleo\", \"FAOV housing contribution\", \"INCES training levy\", \"LOPCYMAT\", \"aporte patronal\", \"deducción IVSS\", \"salario mínimo VES 130\", \"cestaticket\", \"bono de guerra\", \"ISLR withholding on salary\", \"Venezuela payroll tax\", or any question about Venezuelan employer/employee statutory contributions. Also trigger when classifying bank statement transactions that relate to IVSS, FAOV/BANAVIH, INCES, or SENIAT debits from Banco de Venezuela, Banesco, Mercantil, or other Venezuelan banks. CRITICAL: Venezuela's legal minimum wage has been frozen at VES 130 since March 2022 and real pay is delivered through NON-salary bonuses (Cestaticket, Bono de Guerra) that are EXCLUDED from the IVSS, Paro Forzoso, FAOV and INCES bases — never apply those rates to total pay; the 9% pension protection contribution paid by companies is the exception, because its base includes those bonuses. This skill covers contribution rates and splits, the salary vs. non-salary base distinction, contributory ceilings expressed in minimum salaries, the ISLR personal income tax brackets, the Tax Unit (UT) value, filing deadlines, penalties, bank statement classification, and edge cases. ALWAYS read this skill before touching any Venezuelan payroll/social-contribution work."
version: 0.1
jurisdiction: VE
tax_year: 2025
last_updated: 2026-10-08
reviewed_by: Jose Padilla
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Venezuela Social Security & Payroll Contributions

## Venezuela Social Security & Payroll Contributions Skill v0.1

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Jose Padilla** on 2026-06-21; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.
>
> **Edited since review (2026-10-08).** Rates and bases now cite the statutes listed under "Primary legislation" below instead of a secondary tax summary. The statutes required three corrections that the 2026-06-21 sign-off does not cover: FAOV has no ceiling (Ley del Régimen Prestacional de Vivienda y Hábitat art. 33 sets 3% of integral salary with no cap); the INCES employer 2% is on monthly normal salary and applies to employers with five or more workers (Ley del INCES art. 49); and the 9% pension protection contribution in force since May 2024 is added, the one charge whose base includes non-salary bonuses (Ley de Protección de las Pensiones de Seguridad Social art. 7; Decreto N° 4.952).

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Venezuela (Bolivarian Republic of Venezuela) |
| Currency | Venezuelan bolívar (VES, "bolívar digital") |
| Social security authority | IVSS — Instituto Venezolano de los Seguros Sociales |
| Tax authority | SENIAT — Servicio Nacional Integrado de Administración Aduanera y Tributaria |
| Housing fund authority | BANAVIH (administers FAOV — Fondo de Ahorro Obligatorio para la Vivienda) |
| Training authority | INCES — Instituto Nacional de Capacitación y Educación Socialista |
| Primary legislation | Ley del Seguro Social and its Reglamento General (Decreto N° 8.922, Gaceta Oficial N° 39.912, 30 April 2012; [text](http://mundotributariovzla.blogspot.com/2012/05/reforma-parcial-del-reglamento-general.html)); Ley del Régimen Prestacional de Empleo (Gaceta Oficial N° 38.281, 2005; [text](https://venezuela.justia.com/federales/leyes/ley-del-regimen-prestacional-de-empleo/gdoc)); Ley del Régimen Prestacional de Vivienda y Hábitat as reprinted in Gaceta Oficial N° 6.805 Extraordinario, 1 May 2024 ([gazette](https://www.traviesoevans.com/travieso/wp-content/uploads/gacetas/2024/05-mayo/2024-05-01-6805-extraordinario.pdf)); Ley del INCES (Decreto N° 1.414, Gaceta Oficial N° 6.155 Extraordinario, 19 November 2014; [text](https://pandectasdigital.blogspot.com/2017/02/ley-del-instituto-nacional-de.html)); LOPCYMAT (Gaceta Oficial N° 38.236, 26 July 2005); Ley de Protección de las Pensiones de Seguridad Social (Gaceta Oficial N° 6.806 Extraordinario, 8 May 2024) and Decreto N° 4.952 (Gaceta Oficial N° 42.880, 16 May 2024); Ley de Impuesto Sobre la Renta (Gaceta Oficial N° 6.210 Extraordinario, 30 December 2015; [National Assembly copy](https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-n0-2163-mediante-el-cual-se-dicta-el-decreto-con-rango-valor-y-fuerza-de-ley-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-de-impuesto-sobre-la-renta-20211019151632.pdf)) and its Reglamento (Decreto N° 2.507, 2003) |
| Tax year | Calendar year |
| Legal minimum monthly wage (salario mínimo) | **VES 130** since 15 March 2022 (Decreto N° 4.653 art. 1, Gaceta Oficial N° 6.691 Extraordinario); unchanged through 2025 per CloudPay; no later decree was traced here |
| Tax Unit (UT/TU) value 2025 | **VES 43** per Administrative Ruling SNAT/2025/000048, Official Gazette 2 June 2025 (Orbitax) |
| Annual ISLR (personal income tax) return deadline | **31 March** following the tax year (ISLR Reglamento art. 146); the Ministry of Finance may extend it by resolution (art. 149) |
| Validated by | Verified by Jose Padilla (CPA) on 2026-06-21 |
| Validation date | Verified by Jose Padilla (CPA) on 2026-06-21 |

### CRITICAL Venezuela-specific caveat — read FIRST

The **legal monthly minimum wage (salario mínimo) has been frozen at VES 130 since 15 March 2022** (Decreto N° 4.653 art. 1; CloudPay). Almost all social-security and payroll contributions are legally computed on the **salary** base, which in practice is tiny. Real worker compensation is delivered through **non-salary bonuses** — the *Bono contra la Guerra Económica* ("Bono de Guerra") and the *Cestaticket Socialista* — which the government explicitly classifies as **non-salary** so they are **EXCLUDED** from the IVSS, Paro Forzoso, FAOV and INCES bases. The exception is the **pension protection contribution** (9%, companies only), whose base is total salary **plus** non-salary bonuses (Ley de Protección de las Pensiones de Seguridad Social art. 7). As of 30 April 2025 the indexed minimum income totalled ~US$160/month (Cestaticket ~$40 + Bono de Guerra ~$120, paid in VES at the BCV rate), while the underlying VES 130 minimum wage is worth only ~US$2.50.

**You MUST account for the salary vs. non-salary distinction. Mechanically applying rates to "total pay" will be wrong.** See Section 5, Rule 1.

### Contribution overview (2025)

Sources: the statutes listed under "Primary legislation" in the quick reference, article by article in the table; CloudPay (cloudpay.com/payroll-guide/venezuela-payroll-and-benefits-guide) for current practice.

**Contribution overview table**

| Regime | Employer | Employee | Base / Ceiling | Source |
| --- | --- | --- | --- | --- |
| **IVSS** — Seguro Social Obligatorio (mandatory social security) | 9% / 10% / 11% (by risk class: minimum, medium, maximum) | 4% | Salary, capped at **5 urban minimum salaries** | Reglamento General de la Ley del Seguro Social arts. 98, 108, 109 |
| **Paro Forzoso** — Régimen Prestacional de Empleo (unemployment) | 2% | 0.5% | Normal salary of the previous month; floor **1**, ceiling **10 urban minimum salaries** | Ley del Régimen Prestacional de Empleo art. 46 (2.5% split 80/20) |
| **FAOV** — Régimen Prestacional de Vivienda y Hábitat (housing) | 2% | 1% | **Integral salary, no ceiling** | Ley del Régimen Prestacional de Vivienda y Hábitat art. 33 (3% split two-thirds/one-third) |
| **INCES** — training levy | 2% of monthly normal salary paid (employers with 5 or more workers) | 0.5% of annual *utilidades*, aguinaldos or year-end bonuses | No cap | Ley del INCES arts. 49, 50 |
| **LOPCYMAT** — workplace prevention/safety | 0.75% – 10% (risk-dependent) | 0% | Salary of each worker; the law sets no cap | LOPCYMAT art. 7 |
| **Pension protection contribution** (contribución especial) | 9% (companies and other private entities; not individuals) | 0% | Total **salary and non-salary bonuses** paid; per-worker base not below the indexed integral minimum income; no cap | Ley de Protección de las Pensiones de Seguridad Social arts. 6, 7, 9; Decreto N° 4.952 art. 1 |

- The **IVSS** and **Paro Forzoso** ceilings are expressed in *minimum salaries*. With the frozen VES 130 minimum wage, the contributory ceilings are extremely low in absolute terms (IVSS cap = 5 × VES 130 = VES 650/month; Paro Forzoso cap = 10 × VES 130 = VES 1,300/month).
- **FAOV** uses the *integral salary* (salario integral) with **no ceiling** in the law — integral salary includes commissions, gratifications, profit sharing, bonuses, vacation bonus, and shift premiums. The employer withholds the worker's 1%, adds its 2% and deposits both within the first five business days of each month (art. 34).
- **Paro Forzoso** is withheld when salary is paid and paid to the Tesorería de Seguridad Social within the first five business days of each month (Ley del Régimen Prestacional de Empleo art. 47).
- **INCES**: the employer's 2% is due within five days after each quarter ends; the worker's 0.5% is withheld from the utilidades payment and paid within ten days (Ley del INCES arts. 49, 50).
- **Pension protection contribution**: declared and paid monthly to SENIAT (art. 9). The law allows up to 15% (art. 7); Decreto N° 4.952 fixed 9% from 16 May 2024 and exempted enterprises registered in the Registro Nacional de Emprendimientos for at most one year from publication (arts. 2-4). Whether that exemption was extended after May 2025 is unconfirmed [RESEARCH GAP].
- IVSS announced contribution-rate administration changes in Feb 2025 (secondary EOR sources, e.g. Rivermate). The Reglamento General (art. 109) still sets the 4% employee / 9–11% employer split — **treat 4% / 9–11% as authoritative**. [RESEARCH GAP — reviewer to confirm whether the Feb-2025 IVSS administrative change altered the split, against ivss.gob.ve.]

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown occupational-risk class (IVSS) | Use the **lowest** employer rate 9% for estimates; flag for reviewer to confirm class |
| Unknown LOPCYMAT risk rate | STOP — do not estimate; range is 0.75%–10% and is too wide to default safely. Flag for reviewer |
| Pay described only as "total pay" or "total income" | STOP — split into salary vs. non-salary (Cestaticket / Bono de Guerra) before applying ANY rate |
| Unknown whether bonus is salary or non-salary | Treat Cestaticket and Bono de Guerra as **non-salary (EXCLUDED)**; flag everything else for reviewer |
| Unknown whether worker is "urban" | Assume urban-worker ceilings (5 / 10 minimum salaries); flag for reviewer |
| Unknown UT for a year other than 2025 | STOP — UT changes by Administrative Ruling; do not assume |
| Unknown whether the employer is a company or an individual | Assume a company: apply the 9% pension protection contribution and flag for reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — the worker's **salary** base (the legally-classified *salario*, NOT total compensation) and whether the payment items are salary or non-salary. Without the salary/non-salary split, STOP.

**Recommended** — occupational-risk class (for IVSS 9/10/11%), LOPCYMAT risk rate, integral-salary components (for FAOV), and the annual *utilidades* profit-share figure (for the INCES employee 0.5%).

**Ideal** — the IVSS/BANAVIH/INCES registration records, the payroll register showing salary vs. non-salary line items, and bank statements showing the monthly statutory debits.

### Refusal catalogue

- **R-VE-SC-1 — Salary vs. non-salary split unknown** — Trigger: only "total pay" is provided, with no breakdown of salary vs. Cestaticket / Bono de Guerra. Message: "Venezuelan contributions are computed on the *salary* base only. The Cestaticket Socialista and Bono contra la Guerra Económica are legally non-salary and are excluded. Applying rates to total pay overstates contributions massively. Provide the salary component before I can compute anything."
- **R-VE-SC-2 — LOPCYMAT risk rate unknown** — Trigger: LOPCYMAT computation requested without the assigned risk percentage. Message: "LOPCYMAT employer contributions range 0.75%–10% depending on the assigned occupational-risk rate (INPSASEL classification). I cannot default across a 13× range. Provide the assigned rate or escalate to a licensed accountant."
- **R-VE-SC-3 — IVSS Feb-2025 rate-change query** — Trigger: client asks whether IVSS rates changed in 2025. Message: "Secondary EOR sources reference a Feb-2025 IVSS administrative change, but the Reglamento General de la Ley del Seguro Social (art. 109) still sets the 4% employee / 9–11% employer split. [RESEARCH GAP] This must be confirmed directly against ivss.gob.ve before relying on it. Escalate to a licensed accountant."
- **R-VE-SC-4 — Penalty / arrears quantification** — Trigger: client asks to quantify contribution arrears or COT penalties. Message: "COT penalties are FX-indexed to the BCV highest-value-currency rate and special-taxpayer penalties increase by 200%. Do not estimate arrears or penalties without authority statements. Escalate to a licensed accountant immediately."
- **R-VE-SC-5 — Exact SENIAT/IVSS form code as load-bearing** — Trigger: output depends on naming the exact 2025 ISLR individual form code. Message: "The individual ISLR form is DPN-99025, an electronic form also known informally as 'Forma 25' among accountants. If the exact form code is load-bearing, confirm directly against seniat.gob.ve."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Venezuelan statutory contributions and taxes. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Statutory contributions and tax payments always EXCLUDE from any revenue/expense VAT (IVA) classification — they are statutory obligations, not business supplies. Amounts are in VES.

### 3.1 IVSS / social-security debits

**IVSS / social-security debits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IVSS, SEGURO SOCIAL, SEGURO SOCIAL OBLIGATORIO | EXCLUDE — IVSS contribution | Monthly employer + employee IVSS |
| INSTITUTO VENEZOLANO DE LOS SEGUROS SOCIALES | EXCLUDE — IVSS contribution | Full authority name |
| TIUNA, SISTEMA TIUNA | EXCLUDE — IVSS contribution | IVSS online payment system reference |

### 3.2 Other statutory regimes

**Other statutory regimes table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PARO FORZOSO, REGIMEN PRESTACIONAL DE EMPLEO, RPE | EXCLUDE — unemployment (Paro Forzoso) | Employer 2% / employee 0.5% |
| FAOV, BANAVIH, VIVIENDA Y HABITAT, AHORRO HABITACIONAL | EXCLUDE — housing (FAOV) | Employer 2% / employee 1%, integral salary, no cap |
| INCES, INCE | EXCLUDE — training levy | Employer 2% (quarterly) / employee 0.5% on utilidades |
| LOPCYMAT, INPSASEL | EXCLUDE — workplace-safety (LOPCYMAT) | Employer-only 0.75%–10% |
| CONTRIBUCION ESPECIAL, PROTECCION DE LAS PENSIONES, LPPSS | EXCLUDE — pension protection contribution (paid to SENIAT) | Employer-only 9% of salary plus non-salary bonuses; companies only |

### 3.3 SENIAT / tax payments (NOT social contributions — do not confuse)

**SENIAT / tax payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SENIAT | EXCLUDE — tax payment, not a contribution | ISLR, IVA or other SENIAT tax |
| ISLR, IMPUESTO SOBRE LA RENTA | EXCLUDE — income tax | Not a social contribution |
| IVA, IMPUESTO AL VALOR AGREGADO | EXCLUDE — VAT | Not a social contribution |
| RETENCION, RETENCION ISLR | EXCLUDE — withholding tax | Salary/professional-fee withholding |

### 3.4 Salary and non-salary payroll (exclude from contribution classification)

**Salary and non-salary payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NOMINA, SUELDO, SALARIO (outgoing) | EXCLUDE — payroll (salary) | Salary base; contributions computed separately |
| CESTATICKET, CESTA TICKET, CESTATICKET SOCIALISTA | EXCLUDE — **non-salary** benefit | NOT in the contribution base |
| BONO DE GUERRA, BONO CONTRA LA GUERRA ECONOMICA | EXCLUDE — **non-salary** benefit | NOT in the contribution base |
| UTILIDADES (outgoing) | EXCLUDE — profit-share bonus | INCES employee 0.5% applies to this figure |

### 3.5 Benefit payments received (not contributions paid)

**Benefit payments received table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IVSS PENSION, PENSION DE VEJEZ | EXCLUDE — pension income received | Not a contribution payment |
| PARO FORZOSO PAGO, PRESTACION DESEMPLEO | EXCLUDE — unemployment benefit received | Not a contribution payment |

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical small employer in Caracas. All amounts in VES. Because the minimum wage is frozen at VES 130, salary-base contributions are tiny in absolute terms; FAOV (no cap, integral salary) is usually the largest line.

> Throughout: the **salary base** used for IVSS/Paro Forzoso is the legally-classified *salario*, which for a minimum-wage worker is VES 130/month, subject to the minimum-salary ceilings. Cestaticket and Bono de Guerra are **excluded**.

### Example 1 — IVSS monthly contribution, single minimum-wage worker

**Input line:**
`05.02.2025 ; IVSS SEGURO SOCIAL OBLIGATORIO ; DEBITO ; ENERO 2025 ; -16,90 ; VES`

**Reasoning:**
Matches "IVSS / SEGURO SOCIAL OBLIGATORIO" (pattern 3.1). Salary base = VES 130 (minimum wage, below the 5-minimum-salary IVSS ceiling of VES 650). Employer 9% (lowest risk class default) + employee 4% = 13% of VES 130 = **VES 16.90**. Excludes from IVA.

Check: 130 × 0.09 = 11.70 (employer); 130 × 0.04 = 5.20 (employee); 11.70 + 5.20 = **16.90**. ✓

**Classification:** EXCLUDE — IVSS contribution (employer VES 11.70 + employee VES 5.20).

### Example 2 — FAOV housing contribution (integral salary, no cap)

**Input line:**
`07.02.2025 ; BANAVIH FAOV AHORRO HABITACIONAL ; DEBITO ; ENERO 2025 ; -3,90 ; VES`

**Reasoning:**
Matches "BANAVIH / FAOV" (pattern 3.2). FAOV uses the **integral salary** with **no ceiling**: employer 2% + employee 1% = 3%. On a VES 130 integral salary (no other integral components present), 3% × 130 = **VES 3.90**. If integral-salary components (commissions, bonuses classified as salary) existed, the base would be higher.

Check: 130 × 0.02 = 2.60 (employer); 130 × 0.01 = 1.30 (employee); 2.60 + 1.30 = **3.90**. ✓

**Classification:** EXCLUDE — FAOV housing contribution (employer VES 2.60 + employee VES 1.30).

### Example 3 — Paro Forzoso (unemployment)

**Input line:**
`07.02.2025 ; PARO FORZOSO REGIMEN PRESTACIONAL EMPLEO ; DEBITO ; ENERO 2025 ; -3,25 ; VES`

**Reasoning:**
Matches "PARO FORZOSO / RPE" (pattern 3.2). Salary base VES 130 (below the 10-minimum-salary ceiling of VES 1,300). Employer 2% + employee 0.5% = 2.5% × 130 = **VES 3.25**.

Check: 130 × 0.02 = 2.60 (employer); 130 × 0.005 = 0.65 (employee); 2.60 + 0.65 = **3.25**. ✓

**Classification:** EXCLUDE — Paro Forzoso (employer VES 2.60 + employee VES 0.65).

### Example 4 — Cestaticket paid (non-salary, NOT a contribution and NOT in the base)

**Input line:**
`10.02.2025 ; CESTATICKET SOCIALISTA ; DEBITO ; FEBRERO 2025 ; -2.080,00 ; VES`

**Reasoning:**
Matches "CESTATICKET" (pattern 3.4). This is a **non-salary** benefit paid to the worker. It is the dominant part of real take-home pay (here ~VES 2,080, far above the VES 130 salary), but it is **EXCLUDED from every contribution base**. Do NOT add it to the salary base when computing IVSS/Paro Forzoso/FAOV. It is also not itself a statutory contribution debit.

**Classification:** EXCLUDE — non-salary benefit. NOT in any contribution base.

### Example 5 — SENIAT ISLR payment (tax, NOT a social contribution)

**Input line:**
`28.03.2025 ; SENIAT ISLR DECLARACION ANUAL ; DEBITO ; EJERCICIO 2024 ; -45.000,00 ; VES`

**Reasoning:**
Matches "SENIAT / ISLR" (pattern 3.3). This is an annual income-tax (ISLR) payment, due by **31 March** following the tax year (ISLR Reglamento art. 146). It is NOT a social-security contribution — do not classify it as IVSS/FAOV/etc.

**Classification:** EXCLUDE — ISLR income tax payment. NOT a social contribution.

### Example 6 — Ambiguous IVSS lump sum (possible arrears/penalty)

**Input line:**
`15.06.2025 ; IVSS ; DEBITO ; AJUSTE/RECARGO ; -1.250,00 ; VES`

**Reasoning:**
Matches "IVSS" (pattern 3.1) but the amount is irregular and the reference says "AJUSTE/RECARGO" (adjustment/surcharge). This may include arrears plus COT-indexed penalties (FX-indexed to the BCV highest-value-currency rate; +200% for special taxpayers). Principal cannot be separated from penalty without an IVSS statement.

**Classification:** EXCLUDE from IVA. Flag for reviewer — request the IVSS breakdown to split contribution principal from penalty.

## Section 5 -- Tier 1 rules

These rules apply when payroll data is clear and the salary/non-salary split is available. Apply exactly as written. Sources are the statutes named in each rule.

### Rule 1 — Contributions are computed on the SALARY base, NOT total pay

- **Rule 1** — The Cestaticket Socialista and Bono contra la Guerra Económica are non-salary and are EXCLUDED from the IVSS, Paro Forzoso, FAOV and INCES bases. Always strip these out before applying those rates. This is the single most important rule for Venezuela. The one exception is the pension protection contribution (Rule 6A), whose base adds non-salary bonuses back.  _(the government's explicit non-salary classification; Ley de Protección de las Pensiones de Seguridad Social art. 7 for the exception)_

### Rule 2 — IVSS (Seguro Social Obligatorio)

- **Rule 2** — Employer 9% / 10% / 11% by risk class (minimum / medium / maximum); employee 4%. Base capped at 5 urban minimum salaries = 5 × VES 130 = VES 650/month.  _(Reglamento General de la Ley del Seguro Social arts. 98, 108, 109)_

### Rule 3 — Paro Forzoso (Régimen Prestacional de Empleo)

- **Rule 3** — Total 2.5% of the previous month's normal salary, 80% (2%) employer and 20% (0.5%) employee. Base between 1 and 10 urban minimum salaries = up to 10 × VES 130 = VES 1,300/month.  _(Ley del Régimen Prestacional de Empleo art. 46)_

### Rule 4 — FAOV (housing) uses integral salary with no ceiling

- **Rule 4** — Total 3% of integral salary: employer two-thirds (2%), employee one-third (1%). Base = total monthly integral salary (commissions, gratifications, profit sharing, bonuses, vacation bonus, shift premiums), with no ceiling in the law. This is usually the largest contribution line for anyone earning above the salary minimum. Deposit within the first five business days of each month.  _(Ley del Régimen Prestacional de Vivienda y Hábitat arts. 33, 34, Gaceta Oficial N° 6.805 Extraordinario)_

### Rule 5 — INCES (training levy)

- **Rule 5** — Employers with five or more workers pay 2% of the monthly normal salary paid, within five days after each quarter ends; workers pay 0.5% of annual utilidades, aguinaldos or year-end bonuses — no cap. The employee component is NOT a monthly salary deduction; the employer withholds it from the utilidades payment and pays it within ten days.  _(Ley del INCES arts. 49, 50)_

### Rule 6 — LOPCYMAT (workplace prevention) is employer-only

- **Rule 6** — Employer 0.75%–10% of each worker's salary depending on assigned occupational-risk rate; no employee contribution. Do not default the rate — see R-VE-SC-2.  _(LOPCYMAT art. 7)_

### Rule 6A — Pension protection contribution (companies only)

- **Rule 6A** — Companies and other private entities (not individual employers) pay 9% of total payments to workers for salary and non-salary bonuses, so Cestaticket and Bono de Guerra ARE in this base. The base for each worker may not be lower than the indexed integral minimum income set by the Executive. Declared and paid monthly to SENIAT; no employee share. Enterprises registered in the Registro Nacional de Emprendimientos were exempt for at most one year from 16 May 2024.  _(Ley de Protección de las Pensiones de Seguridad Social arts. 6, 7, 9, Gaceta Oficial N° 6.806 Extraordinario; Decreto N° 4.952 arts. 1-4, Gaceta Oficial N° 42.880)_

### Rule 7 — Ceilings are expressed in minimum salaries

- **Rule 7** — IVSS = 5 minimum salaries; Paro Forzoso = 10 minimum salaries. With the frozen VES 130 minimum wage, recompute the absolute cap as (multiple × VES 130) whenever the minimum wage figure is current. If the minimum wage changes, the absolute ceilings move with it.

### Rule 8 — ISLR (personal income tax) is separate from contributions

- **Rule 8** — ISLR is progressive 6%–34% on a Tax-Unit (TU) basis for residents (worldwide income); non-residents pay flat 34% on 90% of gross for non-business professional income. The UT value for 2025 is VES 43 (SNAT/2025/000048, Gazette 2 June 2025). See Section 10 for the bracket table.  _(LISLR arts. 1, 39, 50)_

### Rule 9 — ISLR filing deadline is 31 March

- **Rule 9** — The annual ISLR return is due 31 March following the calendar tax year (three months after the year ends); the Ministry of Finance may grant more time by resolution. Late filing triggers penalties plus interest. Major/"special" taxpayers file on SENIAT-set dates.  _(ISLR Reglamento arts. 146, 149)_

### Rule 10 — Estimated-tax return threshold

- **Rule 10** — An advance (anticipo) is required from taxpayers with business or professional activity whose prior-year net taxable income exceeded 1,500 TU. It is computed on 80% of the prior year's net income; only 75% of the resulting tax is paid, from the sixth month after the year-end in up to six equal monthly instalments. For 2025, 1,500 TU = 1,500 × VES 43 = VES 64,500.  _(LISLR arts. 80, 85; ISLR Reglamento arts. 156, 164)_

## Section 6 -- Tier 2 catalogue

When data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 — Occupational-risk class for IVSS (9% vs 10% vs 11%)

**Trigger:** employer IVSS rate must be applied but the risk class is not documented.
**Issue:** the employer rate is 9%, 10%, or 11% depending on the IVSS-assigned occupational-risk class.
**Action:** flag for reviewer. Use 9% only as a provisional estimate and label it as such.

### T2-2 — LOPCYMAT risk rate (0.75%–10%)

**Trigger:** LOPCYMAT contribution must be computed.
**Issue:** the rate spans a 13× range and is assigned per the INPSASEL classification (LOPCYMAT art. 7); whether it is collected in practice is unconfirmed.
**Action:** flag for reviewer. Do not estimate without the assigned rate.

### T2-3 — Integral-salary composition for FAOV

**Trigger:** worker has commissions, bonuses, or shift premiums that may be salary or non-salary.
**Issue:** FAOV uses the integral salary (no cap), so misclassifying a component changes the base directly. Cestaticket and Bono de Guerra are non-salary; other items require judgement.
**Action:** flag for reviewer to confirm which components are integral salary.

### T2-4 — IVSS Feb-2025 administrative change

**Trigger:** client relies on a 2025 IVSS rate.
**Issue:** secondary EOR sources cite a Feb-2025 IVSS administrative change; the Reglamento General (art. 109) still sets 4%/9–11%. [RESEARCH GAP]
**Action:** flag for reviewer to confirm against ivss.gob.ve before filing.

### T2-5 — Special-taxpayer (contribuyente especial) status

**Trigger:** client is or may be a SENIAT-designated special taxpayer.
**Issue:** special taxpayers file ISLR on SENIAT-set dates, may make bi-weekly advance payments, and face penalties increased by 200% (COT Art. 108).
**Action:** flag for reviewer to confirm special-taxpayer designation and the applicable calendar.

### T2-6 — Contribution arrears and FX-indexed penalties

**Trigger:** unpaid contributions or COT penalties.
**Issue:** COT-2020 penalties are FX-indexed to the BCV highest-value-currency rate, not UT-indexed; quantification requires authority statements.
**Action:** do not estimate; escalate to a licensed accountant (see R-VE-SC-4).

## Section 7 -- Excel working paper template

When producing a Venezuelan contribution computation, structure the working paper as follows:

```
VENEZUELA SOCIAL CONTRIBUTIONS -- WORKING PAPER
Employer / Client: [name]
Tax Year: [year]            Month: [____]
Prepared: [date]

INPUT DATA
  Salary base (salario, VES):          [____]
  Integral salary (FAOV base, VES):    [____]
  Non-salary excluded items:
     Cestaticket (VES):                [____]  (EXCLUDED)
     Bono de Guerra (VES):             [____]  (EXCLUDED)
  Occupational-risk class (IVSS):      [9% / 10% / 11%]
  LOPCYMAT assigned rate:              [0.75%–10% — confirm]
  Annual utilidades (VES):             [____]  (INCES employee base)
  Minimum wage in force (VES):         130  (since 15 Mar 2022)

CEILINGS (recompute from minimum wage)
  IVSS cap (5 x min wage, VES):        650
  Paro Forzoso cap (10 x min wage):    1,300
  FAOV cap:                            none (integral salary)

PENSION PROTECTION BASE (companies only)
  Salary + non-salary bonuses (VES):   [____]  (each worker at least the indexed integral minimum income)

CONTRIBUTIONS                           Employer        Employee
  IVSS    (9–11% / 4%):                 [____]          [____]
  Paro Forzoso (2% / 0.5%):            [____]          [____]
  FAOV    (2% / 1%, integral):         [____]          [____]
  INCES   (2% salaries / 0.5% util.):  [____]          [____]
  LOPCYMAT (0.75–10% / nil):           [____]            nil
  Pension protection (9% / nil):       [____]            nil
  ------------------------------------------------------------
  TOTAL:                               [____]          [____]

ISLR (if computing income tax)
  Taxable income (TU = VES / 43):      [____] TU
  Bracket rate:                        [____]%
  Subtraction (TU):                    [____]
  Tax (TU):                            [____]
  Tax (VES = TU x 43):                 [____]

REVIEWER FLAGS
  [List any Tier 2 / RESEARCH GAP flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How statutory debits appear on Venezuelan bank statements

**Banco de Venezuela:**
- Description: "IVSS", "SEGURO SOCIAL OBLIGATORIO", "BANAVIH FAOV", "INCES", "SENIAT"
- Timing: monthly (contributions); ISLR annually around March
- Amount: small in VES for salary-base contributions (minimum wage frozen at VES 130)

**Banesco:**
- Description: "IVSS SEGURO SOCIAL", "FAOV AHORRO HABITACIONAL", "PARO FORZOSO", "RETENCION ISLR"
- Timing: same monthly cycle

**Mercantil / BBVA Provincial / Banco Mercantil:**
- Description: "INSTITUTO VENEZOLANO DE LOS SEGUROS SOCIALES", "BANAVIH", "INCES", "SENIAT"
- Timing: same monthly cycle

**Key identification tips:**
1. Statutory contributions are always outgoing (DEBITO), never credits.
2. Salary-base contributions (IVSS, Paro Forzoso) are tiny in VES because the salary minimum is frozen at VES 130 — do not assume a small debit is an error.
3. FAOV (integral salary, no ceiling) is usually the largest salary-base contribution line for higher earners; for a company the 9% pension protection contribution paid to SENIAT is usually larger still, because its base includes the bonuses.
4. **Cestaticket** and **Bono de Guerra** debits are large non-salary payments — they are NOT contributions and NOT in the IVSS, Paro Forzoso, FAOV or INCES bases (they are in the pension protection base).
5. Do not confuse SENIAT (ISLR/IVA tax) debits with IVSS/FAOV/INCES (social contribution) debits.
6. Irregular IVSS/SENIAT lump sums with "RECARGO", "AJUSTE", or "MULTA" may include FX-indexed penalties — flag for reviewer.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for statutory debits** — identify all outgoing payments matching Section 3 patterns (IVSS, FAOV/BANAVIH, Paro Forzoso, INCES, LOPCYMAT, SENIAT).
2. **Separate contributions from tax** — IVSS/FAOV/INCES/Paro Forzoso/LOPCYMAT are social contributions; SENIAT/ISLR/IVA are taxes.
3. **Identify the salary base** — look for NOMINA/SUELDO/SALARIO outgoing lines. Treat CESTATICKET and BONO DE GUERRA as non-salary (excluded from the base).
4. **Reverse-check IVSS:** if you can see the salary base, employer+employee IVSS ≈ 13% (9% + 4%) of the capped salary base. A monthly IVSS debit far above 13% of (5 × minimum wage) suggests arrears or a non-default risk class.
5. **Flag for reviewer:** "Contribution classification derived from bank statement amounts only. Salary vs. non-salary split, occupational-risk class, LOPCYMAT rate, and special-taxpayer status have not been independently verified. Reviewer must confirm before filing."

## Section 10 -- Reference material

### ISLR personal income tax brackets — residents (2025)

**ISLR personal income tax brackets — residents (2025)**  _(LISLR art. 50, Tarifa Nº 1; subtraction amounts derived from the bands)_

| Taxable income (TU) | Rate | Subtraction (TU) |
| --- | --- | --- |
| 0 – 1,000 | 6% | 0 |
| 1,000 – 1,500 | 9% | 30 |
| 1,500 – 2,000 | 12% | 75 |
| 2,000 – 2,500 | 16% | 155 |
| 2,500 – 3,000 | 20% | 255 |
| 3,000 – 4,000 | 24% | 375 |
| 4,000 – 6,000 | 29% | 575 |
| Over 6,000 | 34% | 875 |

- **Non-residents ISLR rate** — flat 34% on 90% of gross for non-business professional income  _(LISLR arts. 39, 50)_

### Corporate income tax (context)

**Corporate income tax (context)**  _(LISLR art. 52, Tarifa Nº 2; banking, financial, insurance and reinsurance income of domiciled companies is taxed at a flat 40%, Parágrafo Primero)_

| Bracket | Rate |
| --- | --- |
| 0–2,000 TU | 15% |
| 2,000–3,000 TU | 22% |
| over 3,000 TU | 34% |

### Filing & registration thresholds

**Filing & registration thresholds table**

| Item | Value | Source |
| --- | --- | --- |
| Annual ISLR return deadline | 31 March; the Ministry of Finance may extend it by resolution | ISLR Reglamento arts. 146, 149 |
| Estimated-tax threshold | prior-year net taxable income > 1,500 TU (= VES 64,500 at UT 43) | LISLR art. 80; ISLR Reglamento art. 156 |
| Estimated tax formula | 75% of tax on 80% of prior-year net income; paid from the sixth month after the year-end in up to 6 equal monthly instalments. Special taxpayers: advances on gross sales under a separate SENIAT ruling (secondary sources give 1% per fortnight; not traced) | LISLR art. 85; ISLR Reglamento arts. 156, 164 |
| Individual ISLR form (2025) | DPN-99025 (electronic form, also historically called "Forma 25" among accountants; as an electronic form it is not commonly referred to by a form name) | Practitioner usage; not confirmed on seniat.gob.ve |
| Spouses | Spouses not separated of property file as one taxpayer, but a married woman may file separately for employment income and professional fees; spouses with a marriage settlement or judicial separation of property file separately | LISLR art. 54; ISLR Reglamento art. 145 |

### Penalties (Código Orgánico Tributario / COT, 2020 reform)

**Penalties table**  _(Grant Thornton Venezuela penalty schedule; Justia COT)_

| Penalty | Rate / basis |
| --- | --- |
| Omitting income / underpaying ISLR | fine 100%–300% of the omitted tax |
| Failure to file a declaration | 10-day closure of the establishment **plus** fine 150× the BCV highest-value-currency rate |
| Incomplete declaration or delay up to one year | fine 100× the BCV highest-value-currency rate |
| Special taxpayers (COT Art. 108) | penalties increased by **200%** |
| Indexation | pecuniary sanctions indexed to the **BCV official rate of the highest-value foreign currency** (FX-indexed, not UT-indexed) |

### Worked ISLR bracket check (for the test suite)

For taxable income of 5,000 TU (falls in the 4,000–6,000 band): tax = 5,000 × 29% − 575 = 1,450 − 575 = **875 TU**. In VES at UT 43: 875 × 43 = **VES 37,625**.

### Test suite

**Test 1 — IVSS, minimum-wage worker.** Salary base VES 130, risk class lowest (9%). Employer = 130 × 9% = VES 11.70; employee = 130 × 4% = VES 5.20; total = **VES 16.90**.

**Test 2 — FAOV, integral salary VES 130.** Employer = 130 × 2% = VES 2.60; employee = 130 × 1% = VES 1.30; total = **VES 3.90**.

**Test 3 — Paro Forzoso, salary base VES 130.** Employer = 130 × 2% = VES 2.60; employee = 130 × 0.5% = VES 0.65; total = **VES 3.25**.

**Test 4 — IVSS ceiling.** Salary base = VES 2,000 (above the 5-minimum-salary cap). Capped base = 5 × 130 = VES 650. Employer (9%) = VES 58.50; employee (4%) = VES 26.00; total = **VES 84.50** (NOT computed on the uncapped VES 2,000).

**Test 5 — Cestaticket exclusion.** Worker receives salary VES 130 + Cestaticket VES 2,080. Contribution base = **VES 130 only**; Cestaticket VES 2,080 is excluded. IVSS total (per Test 1) = VES 16.90.

**Test 6 — INCES employee on utilidades.** Annual utilidades VES 4,000. Employee INCES = 4,000 × 0.5% = **VES 20.00** (attaches to the utilidades payment, not the monthly salary).

**Test 7 — ISLR resident, taxable income 5,000 TU (2025).** Tax = 5,000 × 29% − 575 = **875 TU** = 875 × VES 43 = **VES 37,625**.

**Test 8 — ISLR resident, taxable income 1,000 TU.** Falls at the top of the 6% band: 1,000 × 6% − 0 = **60 TU** = 60 × VES 43 = **VES 2,580**.

**Test 9 — Estimated-tax threshold (2025).** Prior-year qualifying income of VES 70,000 = 70,000 / 43 = 1,627.9 TU > 1,500 TU → estimated-tax return **required**.

**Test 10 — Non-resident professional fee.** Gross VES 100,000 non-business professional income: tax = 34% × (90% × 100,000) = 34% × 90,000 = **VES 30,600** withheld.

**Test 11 — Pension protection contribution (company employer).** Salary VES 130 + Cestaticket VES 2,080 = VES 2,210 paid in the month; assume the indexed integral minimum income for the month, in VES, is not above VES 2,210. Employer contribution = 2,210 × 9% = **VES 198.90**, paid to SENIAT; no employee share. If the indexed minimum is higher, use it as the base instead.

### Prohibitions

- NEVER apply IVSS, Paro Forzoso, FAOV or INCES rates to total pay — strip out Cestaticket and Bono de Guerra (non-salary) first. The 9% pension protection contribution is the exception: its base includes them.
- NEVER cap FAOV — the law sets no ceiling on the integral-salary base.
- NEVER assume the minimum wage has changed — it has been frozen at VES 130 since 15 March 2022; confirm before relying on a different figure.
- NEVER default the LOPCYMAT rate — it spans 0.75%–10%; flag for reviewer.
- NEVER apply IVSS/Paro Forzoso rates to an uncapped base — the ceilings are 5 and 10 minimum salaries respectively.
- NEVER use a UT value other than VES 43 for 2025 without an Administrative Ruling reference.
- NEVER conflate SENIAT (ISLR/IVA tax) debits with IVSS/FAOV/INCES (social contribution) debits.
- NEVER quantify arrears or COT penalties without authority statements — they are FX-indexed and special-taxpayer penalties rise 200%.
- NEVER rely on the IVSS Feb-2025 rate-change claim without confirming against ivss.gob.ve [RESEARCH GAP].
- NEVER cite an exact 2025 ISLR form code as definitive without confirming against seniat.gob.ve [RESEARCH GAP].
- NEVER present contribution or tax figures as definitive — always label as estimated and direct the client to their IVSS/SENIAT statements.

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
