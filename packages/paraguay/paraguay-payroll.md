---
name: paraguay-payroll
description: "Use this skill whenever asked about Paraguay payroll processing for employed persons. Trigger on phrases like \"Paraguay payroll\", \"Paraguayan payroll\", \"planilla de sueldos\", \"planilla de aporte obrero-patronal\", \"IPS Paraguay\", \"aporte obrero\", \"aporte patronal\", \"Instituto de Previsión Social\", \"social security Paraguay\", \"9% IPS\", \"16.5% IPS\", \"IRP Paraguay\", \"Impuesto a la Renta Personal\", \"renta de servicios personales\", \"Formulario 515\", \"Marangatú\", \"salario mínimo Paraguay\", \"minimum wage Paraguay\", \"aguinaldo\", \"13th salary Paraguay\", \"net salary Paraguay\", \"salario neto\", \"gross to net Paraguay\", \"employer contribution Paraguay\", \"DNIT payroll\", \"REI Paraguay\", or any question about computing employee pay, social security contributions, or the income-tax position for Paraguay-based employees. CRITICAL STRUCTURAL FACT: in Paraguay the employer is generally NOT an income-tax (IRP) withholding agent on dependent salaries — IRP is self-assessed annually by the individual. The employer's mandatory payroll burden is IPS social security (employee 9% + employer 16.5% commercial). This skill covers IPS contributions, the minimum wage, the mandatory aguinaldo (13th salary), the IRP self-assessment position, monthly IPS filing, and payslip/income-certificate obligations. ALWAYS read this skill before processing any Paraguay payroll."
version: 0.2
jurisdiction: PY
tax_year: 2025
tax_year_notes: "2025 (minimum-wage floor also stated at the 1 July 2026 level of PYG 3,044,000)"
last_updated: 2026-10-11
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Paraguay Payroll Skill v0.2 (Tier 2 — research-verified, reviewer sign-off pending)

## Paraguay Payroll Skill v0.2 (Tier 2 — research-verified, reviewer sign-off pending)

> **Tier 2 status.** Every rate, threshold, and deadline below is sourced to a named authority (DNIT, IPS, MTESS) or to the statute (Ley N° 6380/2019; the consolidated IPS charter, Decreto-Ley N° 1.860/1950 as amended by Ley N° 98/1992) and cited inline. It has **not** yet been section-by-section verified by a licensed Paraguayan accountant (contador público). Items marked **[RESEARCH GAP — reviewer to confirm]** carry residual uncertainty and must be confirmed against primary sources before reliance.

> **READ THIS FIRST — the single most important structural fact.** Paraguay levies a personal income tax (**IRP — Impuesto a la Renta Personal**), but for salaried (dependent) employees **IRP is NOT withheld at source by the employer.** It is a **self-assessed annual tax** filed by the individual taxpayer (Form 515 via Marangatú). The employer's mandatory monthly payroll burden is therefore primarily **IPS social security** (employee withholding + employer contribution). Do not "withhold IRP from a salary" — that is wrong for Paraguay. See Section 2.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Paraguay (Republic of Paraguay) |
| Currency | PYG (Paraguayan Guaraní) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Income-tax withholding on salaries | **None by the employer** — IRP is self-assessed annually by the individual (Ley N° 6380/2019; DNIT) |
| Employee IPS contribution (general regime) | **9.0%** of salary, withheld by the employer (IPS charter art. 17(a), as replaced by Ley N° 98/1992; IPS contribution table) |
| Employer IPS contribution (general regime) | **16.5%** of salary: 14% under art. 17(b) of the IPS charter plus the employer levies the IPS collects on the same planilla: 1% for the SNPP (Ley N° 253/1971 art. 28), 0.50% for the malaria campaign (Ley N° 432/1973) and 1% for the Ministry of Public Health (Ley N° 446/1957), as the IPS contribution table applies (IPS) |
| Combined IPS (general regime) | **25.5%** (IPS contribution table) |
| Bank and finance employees | Not IPS: affiliated to the Caja de Jubilaciones y Pensiones de Empleados de Bancos y Afines, where Ley N° 2856/2005 art. 9 sets **13% employee / 19% employer** on total remuneration until the fund reaches financial balance (Ley N° 73/1991 had set 10% / 16%); confirm the rate the Caja currently applies |
| IPS base | "Salario": the total remuneration in cash, kind or royalties, including overtime, piece-work, commissions, bonuses, severance pay, premiums and fees, EXCEPT aguinaldo (IPS charter art. 76(a)) and the family allowance (Ley N° 430/1973 art. 4(c)); floor = minimum wage (art. 20) |
| IPS ceiling | None: the charter sets a floor (art. 20) and no ceiling on the contribution base |
| IRP registration/filing threshold | Gross personal-service income **> PYG 80,000,000** counted from 1 January of the year (Ley N° 6380/2019 arts. 62 and 69; DNIT) |
| IRP rates (net taxable income) | 8% up to 50,000,000; 9% on 50,000,001–150,000,000; 10% from 150,000,001 (Ley N° 6380/2019 art. 69; DNIT) |
| Minimum wage | **PYG 3,044,000/month** (general) from 1 Jul 2026 (+5%); **PYG 2,899,048/month** from 1 Jul 2025. Paraguay adjusts in July, so a calendar year spans two floors (Decreto N° 6225 of 17 Jun 2026, reglamentado by MTESS Resolución N° 670/2026; MTESS Resolución N° 677/2025) |
| Aguinaldo (13th salary) | Mandatory; 1/12 of annual remuneration; payable before 31 Dec; **exempt from IPS and IRP** (Ley N° 417/73) |
| Tax authority | DNIT — Dirección Nacional de Ingresos Tributarios (absorbed the former SET in 2023) |
| Social-security authority | IPS — Instituto de Previsión Social |
| Labour authority (minimum wage) | MTESS — Ministerio de Trabajo, Empleo y Seguridad Social |
| Key legislation | Ley N° 6380/2019 (IRP) + Decreto N° 3184/2019; Ley N° 98/92 & Ley N° 213/93 (Código del Trabajo, IPS), reformed by Ley N° 7446/2024; Ley N° 417/73 (aguinaldo) |
| Filing portals | IPS: **REI** (Registro del Empleador por Internet); DNIT/IRP: **Marangatú** |
| Validated by | Pending — requires sign-off by a licensed Paraguayan accountant |
| Skill version | 0.2 (Tier 2) |

## Section 2 -- Income Tax Position (IRP — self-assessed, NOT employer-withheld)

Paraguay **does** levy a personal income tax — **IRP (Impuesto a la Renta Personal), Rentas de Servicios Personales** — under **Ley N° 6380/2019 ("Modernización Tributaria")** and **Decreto N° 3184/2019** (DNIT). The crucial payroll consequence: for **dependent (salaried) employees the employer is generally NOT an IRP withholding agent.** IRP is **self-assessed and filed annually by the individual** taxpayer.

### 2.1 What the employer does (and does not) do

- **Employer role for IRP vs IPS** — The employer does NOT withhold IRP from monthly salaries. The employer's role for IRP is to issue payslips / income certificates that the employee uses to prepare their own annual Form 515 (DNIT — IRP portal). The employer DOES withhold and remit IPS (Sections 3–4) — that is the mandatory monthly payroll burden.  _(DNIT — IRP portal)_

### 2.2 IRP registration / filing threshold (the employee's own obligation)

- **Register & pay IRP only if gross personal-service income exceeds** — PYG 80,000,000, counted from 1 January of the year. A person becomes a taxpayer once their gross taxable personal-service income passes that figure; in that first year the tax is computed on the gross income less the deductible outgoings from the day after the threshold is crossed, and in later years on the whole year  _(Ley N° 6380/2019, art. 62 — https://www.bacn.gov.py/archivos/9332/Ley+6380.pdf ; DNIT — IRP portal — https://www.dnit.gov.py/web/portal-institucional/irp)_

> Ley N° 6380/2019 art. 69: where the taxpayer's gross personal-service income does not exceed PYG 80,000,000 in the fiscal year, they must meet the formal obligations the regulations set but are **not obliged to pay the tax**. Below the threshold, **no IRP is due**.

### 2.3 IRP progressive rate scale (on NET taxable income, FY2025)

**IRP progressive rate scale**  _(Ley N° 6380/2019, art. 69 — https://www.bacn.gov.py/archivos/9332/Ley+6380.pdf ; DNIT — IRP portal — https://www.dnit.gov.py/web/portal-institucional/irp)_

| Net taxable income (PYG) | Rate | Source |
| --- | --- | --- |
| Up to 50,000,000 | 8% | Ley 6380/2019 art. 69; DNIT |
| 50,000,001 – 150,000,000 | 9% (on the slice in this band) | Ley 6380/2019 art. 69; DNIT |
| 150,000,001 and above | 10% (on the slice from 150,000,001) | Ley 6380/2019 art. 69; DNIT |

Applied to **net taxable income** (gross less the deductions in art. 64), not gross; the rate for each band applies to the slice of net income within it and the tax is the sum of the slices (art. 69).

**Cumulative-tax check (recomputed):**
- At exactly 50,000,000 net: 8% × 50,000,000 = **4,000,000**.
- At exactly 150,000,000 net: 4,000,000 + 9% × (150,000,000 − 50,000,000) = 4,000,000 + 9,000,000 = **13,000,000**.
- At 200,000,000 net: 13,000,000 + 10% × (200,000,000 − 150,000,000) = 13,000,000 + 5,000,000 = **18,000,000**. (Self-verified — see Section 9, IRP illustration.)

> A secondary search summary cited a "9% at PYG 100M" break-point; art. 69 of the law sets the bands at 50,000,000 and 150,000,000. The flat **8%** rate on capital income and gains, including rental income, is in art. 60.

### 2.4 IRP deductions

IRP-RSP allows deduction of documented personal/family expenses and investments (the DNIT "net income scale"), governed by **Decreto N° 3184/2019**.

> **[RESEARCH GAP — reviewer to confirm]** The exact deductible categories and any caps were not quoted from an authoritative figure-level source. A licensed Paraguayan accountant must confirm the deductible-expense rules and caps against Decreto N° 3184/2019 and current DNIT guidance before computing any employee's net taxable income.

### 2.5 IRP forms, system and deadline

**IRP forms, system and deadline**  _(DNIT)_

| Item | Detail | Source |
| --- | --- | --- |
| Form | **Formulario 515** — Declaración Jurada IRP Rentas de Servicios Personales | DNIT — Instructivo Formulario 515 |
| System | **Marangatú** (electronic) | DNIT |
| Obligation codes | Form 715-IRP RSP / Form 716-IRP RGC referenced on the DNIT institutional page | DNIT |
| Deadline | Annually in **March**, per the "calendario perpetuo" keyed to the taxpayer's RUC ending digit | DNIT — IRP portal |

### 2.6 Aguinaldo is IRP-exempt

- **Aguinaldo IRP exemption** — The mandatory aguinaldo (13th salary) is exempt from IRP — it does not enter the taxable base. See Section 6.  _(Ley N° 417/73)_

## Section 3 -- Social Security (IPS) -- Employee Deductions

Paraguay's mandatory social-security scheme is **IPS (Instituto de Previsión Social)** (Ley N° 98/92; Ley N° 213/93 Código del Trabajo; reformed by Ley N° 7446/2024). The employer **withholds** the employee share and remits it together with the employer share via the **REI** online system.

### 3.1 Employee contribution (Aporte Obrero)

**Employee IPS contribution rates**  _(Decreto-Ley N° 1.860/1950, Carta Orgánica del IPS (consolidated), art. 17(a) as replaced by Ley N° 98/1992, arts. 20 and 76(a) — https://informacionpublica.paraguay.gov.py/public/241273-CartaOrgnicadelIPSpdf-CartaOrgnicadelIPS.pdf ; IPS, Tabla de bases mínimas imponibles y porcentajes de aportes — https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?c=315)_

| Regime | Employee rate | Base | Source |
| --- | --- | --- | --- |
| IPS general regime (private-sector employees, including domestic workers since Ley N° 6.338/2019) | **9.0%** of salary | Total remuneration in cash, kind or royalties, including overtime, commissions, bonuses, premiums and fees, EXCEPT aguinaldo (art. 76(a)) and the family allowance (Ley N° 430/1973 art. 4(c)); floor = minimum wage (art. 20) | IPS charter arts. 17(a), 20, 76(a); IPS |
| Bank and finance employees (Caja de Jubilaciones y Pensiones de Empleados de Bancos y Afines, not IPS) | **13%** of total remuneration under Ley N° 2856/2005 art. 9(b), the rate that applies until the Caja reaches financial balance (Ley N° 73/1991 had 10%); confirm the Caja's current rate | Total remuneration without deduction except the family allowance and the legal aguinaldo; floor = the bank employees' minimum wage (art. 10) | Ley N° 2856/2005 arts. 9 and 10 — https://paraguay.justia.com/nacionales/leyes/ley-2856-jan-3-2006/gdoc |

- **Floor, ceiling, and illegal over-deduction** — Floor: no contribution may be lower than the one due on the legal minimum wage, even for apprentices (charter art. 20; Section 5). Ceiling: the charter sets none, so IPS applies to the full salary. The deduction from the worker may not exceed 9% of the salary actually paid; the employer bears any difference needed to reach the minimum (art. 20), and the 16.5% employer share must be paid from the employer's own funds.  _(IPS charter art. 20 — https://informacionpublica.paraguay.gov.py/public/241273-CartaOrgnicadelIPSpdf-CartaOrgnicadelIPS.pdf ; MTESS)_

## Section 4 -- Social Security (IPS) -- Employer Contributions

### 4.1 Employer contribution (Aporte Patronal)

**Employer IPS contribution rates**  _(Decreto-Ley N° 1.860/1950, Carta Orgánica del IPS (consolidated), art. 17(b) as replaced by Ley N° 98/1992 — https://informacionpublica.paraguay.gov.py/public/241273-CartaOrgnicadelIPSpdf-CartaOrgnicadelIPS.pdf ; Ley N° 432/1973 — https://paraguay.justia.com/nacionales/leyes/ley-432-dec-28-1973/gdoc ; IPS, Tabla de bases mínimas imponibles y porcentajes de aportes — https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?c=315)_

| Regime | Employer rate | Base | Source |
| --- | --- | --- | --- |
| IPS general regime | **16.5%** of salary: 14% under charter art. 17(b), plus the employer levies the IPS collects on the same planilla: 1% of total salaries for the SNPP (Ley N° 253/1971 art. 28, deposited with the IPS under art. 29), 0.50% for the malaria campaign (Ley N° 432/1973) and 1% for the Ministry of Public Health (Ley N° 446/1957), as the IPS contribution table applies | Same base as the employee | IPS charter art. 17(b); Ley N° 253/1971 — https://paraguay.justia.com/nacionales/leyes/ley-253-jul-2-1971/gdoc ; Ley N° 432/1973; IPS |
| Bank and finance employers (Caja de Jubilaciones y Pensiones de Empleados de Bancos y Afines) | **19%** of total remuneration under Ley N° 2856/2005 art. 9(a), until the Caja reaches financial balance (Ley N° 73/1991 had 16%); confirm the Caja's current rate | Same base as the employee (art. 10) | Ley N° 2856/2005 arts. 9 and 10 |

### 4.2 Combined IPS burden

**Combined IPS burden table**  _(IPS contribution table; Ley N° 2856/2005 art. 9)_

| Regime | Employee | Employer | Combined |
| --- | --- | --- | --- |
| IPS general regime | 9.0% | 16.5% | **25.5%** |
| Caja Bancaria (statutory rates until financial balance) | 13% | 19% | **32%** |

**Total-row check (recomputed):** general 9.0 + 16.5 = **25.5** ✓; Caja Bancaria 13 + 19 = **32** ✓. The 11% / 17% (28%) pair that some summaries print for the financial sector matches neither Ley N° 73/1991 (10% / 16%) nor Ley N° 2856/2005 (13% / 19%); do not use it without the Caja's own confirmation.

### 4.3 Aguinaldo is IPS-exempt

- **Aguinaldo IPS exemption** — The aguinaldo is NOT subject to IPS contributions: the charter's definition of salary excludes aguinaldos (art. 76(a)), and the family allowance is likewise excluded (Ley N° 430/1973 art. 4(c), as the IPS states). It is unembargable (no deductions permitted). See Section 6.  _(IPS charter art. 76(a) — https://informacionpublica.paraguay.gov.py/public/241273-CartaOrgnicadelIPSpdf-CartaOrgnicadelIPS.pdf ; IPS — https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?c=315)_

### 4.4 Payment deadline and penalties

**Payment deadline and penalties table**  _(IPS portal; Vouga; Ley N° 7446/2024; worki360/Deel (secondary))_

| Item | Detail | Source |
| --- | --- | --- |
| Monthly filing | "Planilla de aporte obrero-patronal" via the **REI** system | IPS portal |
| Payment deadline | Per the IPS **"Calendario de Pago"** (Resolución C.A. N° 066/2022); **"Mora Patronal"** (employer default) arises the day after the due date | Vouga / IPS |
| Administrative component | Reduced to **1%** by Ley N° 7446/2024 | Ley N° 7446/2024 |
| Late-payment surcharges (recargos) | The Consejo de Administración may impose surcharges on contributions paid after the 10th day of the month following the month the salaries were paid; the surcharge may not exceed **2% of the contributions for each month of delay, capped at 50%** (IPS charter art. 71). The exact schedule is in the Consejo's resolutions | IPS charter art. 71 — https://informacionpublica.paraguay.gov.py/public/241273-CartaOrgnicadelIPSpdf-CartaOrgnicadelIPS.pdf |

## Section 5 -- Minimum Wage (Salario Mínimo)

**Minimum wage table**  _(MTESS Resolución N° 677/2025)_

| Item | Value | Source |
| --- | --- | --- |
| Monthly minimum (general/unspecified activities), from 1 Jul 2026 | **PYG 3,044,000** (jornal mínimo PYG 117,077; daily rate for monthly-paid staff PYG 101,467; hourly PYG 12,683) | Decreto N° 6225 (17 Jun 2026); MTESS Resolución N° 670/2026 |
| Monthly minimum (general/unspecified activities), 1 Jul 2025 to 30 Jun 2026 | **PYG 2,899,048** | MTESS Resolución N° 677/2025 |
| Daily wage (jornaleros) | PYG 117,077 from 1 Jul 2026; PYG 111,502 from 1 Jul 2025 to 30 Jun 2026 | MTESS Res. 670/2026; Res. 677/2025 |
| Daily rate (mensualizados) | PYG 101,467 from 1 Jul 2026; PYG 96,635 before | MTESS Res. 670/2026; Res. 677/2025 |
| Hourly rate (mensualizados) | PYG 12,683 from 1 Jul 2026; PYG 12,080 before | MTESS Res. 670/2026; Res. 677/2025 |
| Night-shift monthly (with +30%) | PYG 3,957,200 from 1 Jul 2026; PYG 3,768,763 before | Derived: minimum wage x 1.30 |

**Authority:** MTESS. Resolución N° 670/2026 applies from 1 July 2026; Resolución N° 677/2025 applies from 1 July 2025 to 30 June 2026.

- The minimum wage also functions as the **IPS contribution floor** (Section 3).

> **The July 2026 adjustment happened.** Decreto N° 6225 of 17 June 2026 raised the
> minimum wage by 5% from 1 July 2026, and MTESS Resolución N° 670/2026 published
> the regulated table: **PYG 3,044,000/month**, jornal mínimo PYG 117,077, daily
> rate for monthly-paid staff PYG 101,467, hourly PYG 12,683. The rise checks
> against the prior floor: 2,899,048 x 1.05 = 3,044,000. Paraguay adjusts in July,
> so a calendar year straddles two floors and the **month** decides which applies,
> not the year.

## Section 6 -- Aguinaldo (13th-month salary) — mandatory

**Aguinaldo table**  _(Ley N° 417/73)_

| Item | Detail | Source |
| --- | --- | --- |
| Legal basis | Código del Trabajo + **Ley N° 417/73** | Ley N° 417/73 |
| Amount | **1/12 of total remuneration earned during the calendar year** | Ley N° 417/73 |
| Payment deadline | **Before 31 December** | Ley N° 417/73 |
| IPS treatment | **Exempt** — not in the IPS base | IPS charter art. 76(a); IPS |
| IRP treatment | **Exempt** — not in the IRP taxable base | Ley N° 417/73 |
| Other | Unembargable; no deductions permitted | finiquitojusto (secondary) |

## Section 7 -- Conservative Defaults

- **Conservative defaults list** — When inputs are ambiguous, apply these defaults and flag the assumption to the user: 1. No employer IRP withholding. Never withhold IRP from a monthly salary. Compute IPS only; treat IRP as the employee's own annual self-assessment (Section 2). If asked to "withhold income tax from the salary", explain that Paraguay does not do this for dependent employees. 2. Regime = IPS general. Apply the general IPS rates (employee 9.0% / employer 16.5%) unless the employer is a bank or finance entity, whose staff belong to the Caja Bancaria (statutory 13% / 19% under Ley N° 2856/2005; confirm the Caja's current rate before computing) (Section 4). 3. IPS base = full salary (every cash, in-kind or royalty item) excluding aguinaldo and the family allowance, with the minimum-wage floor applied and no ceiling (Section 3). 4. Currency: all amounts in PYG. Never assume USD or any other currency. 5. Pay period: take the minimum-wage floor from the month, since Paraguay adjusts in July rather than January — PYG 3,044,000 from 1 Jul 2026, PYG 2,899,048 from 1 Jul 2025 to 30 Jun 2026. If the month is unknown, ask; never assume the earlier floor. 6. Aguinaldo: compute as 1/12 of annual remuneration, exempt from both IPS and IRP (Section 6). 7. IRP deductions: do not assume any deduction figures — they are a research gap (Section 2.4). Compute IRP illustrations on stated net taxable income only, and label them estimates.

### 8.1 Required inputs (must have before computing IPS payroll)

**Required inputs table**

| Input | Why needed |
| --- | --- |
| Monthly **gross** wage in PYG (cash + in kind) | Drives the IPS base and both contribution shares |
| Employer sector (IPS general regime vs bank or finance entity) | Selects the 9%/16.5% IPS rates or the Caja Bancaria regime (Section 4) |
| Pay period (month/year) | Selects the minimum-wage floor. The floor changes on 1 July, not 1 January: PYG 3,044,000 from 1 Jul 2026, PYG 2,899,048 from 1 Jul 2025 to 30 Jun 2026 |
| Whether the wage includes aguinaldo or family allowance | Those are excluded from the IPS base |
| Employer registration with IPS (REI) | Must be registered before running payroll |

### 8.2 Refusal catalogue — STOP and ask rather than guess

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| Wage stated in USD or another currency | **Refuse to compute.** Ask for the PYG gross amount (or the FX basis the employer uses). |
| User asks the employer to "withhold income tax (IRP) from the salary" | Do **not** do it. Explain Paraguay does not withhold IRP on dependent salaries — IRP is the employee's annual self-assessment (Section 2). Offer to compute IPS instead. |
| User asks for the employee's exact IRP liability | Compute only on a stated **net taxable income**, label it an estimate, and flag that deductible categories/caps are a research gap (Section 2.4) and that the PYG 80M registration threshold applies. |
| Pay period after 30 Jun 2027 | Flag that the July-2026 floor (PYG 3,044,000) is the last confirmed one until the next July adjustment is decreed; do not invent a figure. |
| Financial-sector employer not confirmed | Confirm the sector; do not silently apply 11%/17% to a commercial employer or vice versa. |
| Request for exact IPS late-payment surcharge amount | State the reported 1%–50% range and flag it as a research gap (Section 4.4) — do not present a precise figure as confirmed. |
| Self-employed / sole trader, not an employee | Out of scope for employer payroll — direct to the IRP self-assessment / income-tax skill. |

## Section 9 -- Worked Examples

All figures in PYG. Every example below is a **pay period between 1 July 2025 and 30 June 2026**, **commercial sector** unless stated. IPS base = full gross (no aguinaldo/family allowance), floored at the minimum wage in force for that window (PYG 2,899,048), **no ceiling** applied. For a period from 1 July 2026 the mechanics are identical and only the floor moves, to PYG 3,044,000 — at which the employee 9% is PYG 273,960, the employer 16.5% is PYG 502,260 and the combined 25.5% is PYG 776,220. **No IRP is withheld by the employer** in any example. Each line is recomputed end-to-end.

### Example A — Minimum wage, gross PYG 2,899,048/month (floor edge)

**Example A table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Gross | — | 2,899,048.00 |
| IPS base | = minimum-wage floor | 2,899,048.00 |
| Employee IPS | 9.0% × 2,899,048 | 260,914.32 |
| IRP withheld | none — self-assessed | 0.00 |
| **Net pay** | 2,899,048 − 260,914.32 | **2,638,133.68** |
| Employer IPS | 16.5% × 2,899,048 | 478,342.92 |
| **Total employer cost** | 2,899,048 + 478,342.92 | **3,377,390.92** |

### Example B — Gross PYG 5,000,000/month (typical mid salary)

**Example B table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Gross | — | 5,000,000.00 |
| IPS base | 5,000,000 ≥ floor | 5,000,000.00 |
| Employee IPS | 9.0% × 5,000,000 | 450,000.00 |
| IRP withheld | none — self-assessed | 0.00 |
| **Net pay** | 5,000,000 − 450,000 | **4,550,000.00** |
| Employer IPS | 16.5% × 5,000,000 | 825,000.00 |
| **Total employer cost** | 5,000,000 + 825,000 | **5,825,000.00** |

### Example C — Gross PYG 8,000,000/month (higher salary; annualised crosses IRP threshold)

Annualised gross = 8,000,000 × 12 = 96,000,000 > PYG 80,000,000 → the **employee** must register and self-assess IRP (Section 2.2). The **employer still withholds no IRP** — only IPS.

**Example C table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Gross | — | 8,000,000.00 |
| IPS base | 8,000,000 ≥ floor | 8,000,000.00 |
| Employee IPS | 9.0% × 8,000,000 | 720,000.00 |
| IRP withheld | none — employee self-assesses annually | 0.00 |
| **Net pay** | 8,000,000 − 720,000 | **7,280,000.00** |
| Employer IPS | 16.5% × 8,000,000 | 1,320,000.00 |
| **Total employer cost** | 8,000,000 + 1,320,000 | **9,320,000.00** |

### Example D — Financial sector, gross PYG 12,000,000/month (11% / 17%)

**Example D table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Gross | — | 12,000,000.00 |
| IPS base | 12,000,000 ≥ floor | 12,000,000.00 |
| Employee IPS | 11% × 12,000,000 | 1,320,000.00 |
| IRP withheld | none — self-assessed | 0.00 |
| **Net pay** | 12,000,000 − 1,320,000 | **10,680,000.00** |
| Employer IPS | 17% × 12,000,000 | 2,040,000.00 |
| **Total employer cost** | 12,000,000 + 2,040,000 | **14,040,000.00** |

### Example E — Aguinaldo (13th salary), employee on PYG 5,000,000/month all year

Total remuneration in the calendar year = 5,000,000 × 12 = 60,000,000. Aguinaldo = 1/12 × 60,000,000.

> The aguinaldo is paid in full (no IPS, no IRP, unembargable) before 31 December (Section 6).

**Example E table**

| Line | Computation | Amount (PYG) |
| --- | --- | --- |
| Annual remuneration | 5,000,000 × 12 | 60,000,000.00 |
| Aguinaldo | 1/12 × 60,000,000 | 5,000,000.00 |
| IPS on aguinaldo | exempt | 0.00 |
| IRP on aguinaldo | exempt | 0.00 |
| **Aguinaldo paid (net)** | no deductions | **5,000,000.00** |

### Example F — IRP illustration (employee self-assessment, NOT payroll)

Reference only — the employer does not compute this. Employee with **net taxable income** of PYG 200,000,000 (after confirmed deductions — see the Section 2.4 research gap).

**Cumulative check:** matches Section 2.3 (18,000,000 at 200,000,000 net). (Self-verified.) Filed by the individual on Form 515 via Marangatú in March.

**Example F table**

| Band | Computation | Tax (PYG) |
| --- | --- | --- |
| Up to 50,000,000 @ 8% | 0.08 × 50,000,000 | 4,000,000.00 |
| 50,000,001–150,000,000 @ 9% | 0.09 × 100,000,000 | 9,000,000.00 |
| 150,000,001–200,000,000 @ 10% | 0.10 × 50,000,000 | 5,000,000.00 |
| **Total IRP** | 4,000,000 + 9,000,000 + 5,000,000 | **18,000,000.00** |

## Section 10 -- Tier 1 Rules (deterministic — apply mechanically)

- **Tier 1 rules list** — 1. The employer does NOT withhold IRP from dependent salaries — IRP is the employee's annual self-assessment (Ley N° 6380/2019; DNIT). 2. IPS general regime: employee 9.0%, employer 16.5%, combined 25.5% (IPS charter art. 17 as replaced by Ley N° 98/1992; Ley N° 432/1973; IPS contribution table). 3. Bank and finance employees are in the Caja de Jubilaciones y Pensiones de Empleados de Bancos y Afines, not IPS: Ley N° 2856/2005 art. 9 sets 13% employee / 19% employer until the Caja reaches financial balance; confirm the current rate with the Caja. 4. IPS base = every cash, in-kind or royalty remuneration item EXCEPT aguinaldo (charter art. 76(a)) and the family allowance (Ley N° 430/1973 art. 4(c)). 5. IPS contribution base cannot fall below the minimum wage in force for the period (PYG 3,044,000 from 1 Jul 2026; PYG 2,899,048 from 1 Jul 2025) (charter art. 20; MTESS). 6. The charter sets no IPS salary ceiling (Section 3). 7. The deduction from the worker may not exceed 9% of the salary actually paid; the employer bears the difference to the minimum and pays the 16.5% employer share from its own funds (charter art. 20; MTESS). 8. IRP applies only where the individual's gross personal-service income exceeds PYG 80,000,000 counted from 1 January (Ley N° 6380/2019 arts. 62 and 69; DNIT). 9. IRP rates on net taxable income: 8% up to 50,000,000; 9% on 50,000,001–150,000,000; 10% from 150,000,001 (Ley N° 6380/2019 art. 69; DNIT). 10. Aguinaldo = 1/12 of annual remuneration, payable before 31 December, exempt from both IPS and IRP (Ley N° 417/73). 11. Minimum wage = PYG 3,044,000/month from 1 July 2026 (Decreto N° 6225; MTESS Res. 670/2026); PYG 2,899,048/month from 1 July 2025 (MTESS Res. 677/2025). 12. Monthly IPS planilla filed and paid via REI per the IPS "Calendario de Pago"; Mora Patronal arises the day after the due date (IPS; Vouga). 13. IRP Form 515 filed by the individual via Marangatú annually in March, keyed to the RUC ending digit (DNIT). 14. All payroll amounts in PYG (Guaraní) — never another currency.

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

These items require a licensed Paraguayan accountant's judgement and/or confirmation against primary sources before reliance.

1. IRP itemized deductions / caps (Section 2.4) — governed by Decreto N° 3184/2019; exact deductible categories and caps not quoted from a figure-level source. Confirm before computing any employee's net taxable income.
2. Caja Bancaria rates (Section 4) — Ley N° 2856/2005 art. 9 sets 13% / 19% "for the time needed to reach the Caja's financial balance", falling back towards the earlier percentages afterwards; confirm the rate the Caja applies today before computing a bank employee's payroll.
3. IPS late-payment surcharge schedule (Section 4.4) — the charter caps surcharges at 2% of the contributions per month of delay and 50% overall (art. 71); confirm the current Consejo de Administración resolution for the exact schedule.
4. IRP changes for 2026 (Section 2) — no IRP rate or threshold change has been confirmed for 2026; confirm against DNIT before applying one. The **minimum wage is no longer a research gap**: Decreto N° 6225 of 17 June 2026 raised it 5% to PYG 3,044,000 from 1 July 2026, regulated by MTESS Resolución N° 670/2026.
5. IRP rate break-point (Section 2.3) — one secondary summary cited a "9% at PYG 100M" break-point; this skill uses the 50M/150M bands in art. 69 of Ley N° 6380/2019, which DNIT's IRP page repeats.
6. In-kind wage valuation for the IPS base — confirm how in-kind remuneration is valued for contribution purposes.

### 12.1 Monthly — IPS planilla de aporte obrero-patronal

**Monthly filing table**  _(IPS portal; Vouga)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Monthly contribution payroll ("planilla de aporte obrero-patronal") | Declare and pay the employee (9%) + employer (16.5%) IPS contributions, filed via the **REI** system | Per the IPS **"Calendario de Pago"** (Resolución C.A. N° 066/2022); Mora Patronal arises the day after the due date | IPS portal; Vouga |

### 12.2 Annual — IRP (the employee's own filing, NOT the employer's)

**Annual filing table**  _(DNIT — IRP portal; Instructivo Form 515)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **Formulario 515** — Declaración Jurada IRP Rentas de Servicios Personales | The individual's annual self-assessment of IRP (only if gross personal-service income > PYG 80M/year) | Annually in **March**, per the "calendario perpetuo" keyed to the RUC ending digit | DNIT — IRP portal; Instructivo Form 515 |

**IRP filing triggers** (the employee's obligation, not the employer's): gross personal-service income exceeding **PYG 80,000,000** counted from 1 January (Ley N° 6380/2019 arts. 62 and 69; DNIT). The return for fiscal year 2025 fell due in March 2026 on the day set by the last digit of the RUC under the calendario perpetuo (DNIT notice of 5 March 2026; RG N° 01/2007 and 38/2020). The employer's only IRP role is to issue the payslip/income certificate the employee uses for Form 515.

## Section 13 -- Thresholds Reference Table

**Thresholds Reference Table**

| Threshold | Value | Source |
| --- | --- | --- |
| IPS employee rate (general regime) | 9.0% of salary | IPS charter art. 17(a); IPS |
| IPS employer rate (general regime) | 16.5% of salary (14% charter art. 17(b) plus 1% SNPP, 0.50% malaria campaign and 1% Ministry of Public Health levies) | IPS charter art. 17(b); Leyes N° 253/1971, 432/1973 and 446/1957; IPS |
| IPS combined (general regime) | 25.5% | IPS contribution table |
| Caja Bancaria employee / employer (bank and finance staff, not IPS) | 13% / 19% by statute until financial balance; confirm the current rate | Ley N° 2856/2005 art. 9 |
| IPS base floor | Minimum wage: PYG 3,044,000 from 1 Jul 2026; PYG 2,899,048 from 1 Jul 2025 | IPS charter art. 20; MTESS |
| IPS ceiling | None in the charter | IPS charter arts. 17 and 20 |
| IRP registration/filing threshold | Gross personal-service income > PYG 80,000,000 counted from 1 January | Ley N° 6380/2019 arts. 62 and 69; DNIT |
| IRP rate band 1 | 8% on net taxable income up to 50,000,000 | Ley N° 6380/2019 art. 69; DNIT |
| IRP rate band 2 | 9% on net taxable income 50,000,001–150,000,000 | Ley N° 6380/2019 art. 69; DNIT |
| IRP rate band 3 | 10% on net taxable income from 150,000,001 | Ley N° 6380/2019 art. 69; DNIT |
| Minimum wage | PYG 3,044,000/month from 1 Jul 2026; PYG 2,899,048/month from 1 Jul 2025 | Decreto N° 6225; MTESS Resoluciones N° 670/2026 and N° 677/2025 |
| Aguinaldo | 1/12 of annual remuneration; before 31 Dec; IPS & IRP exempt | Ley N° 417/73 |
| IPS administrative component | 1% (post Ley N° 7446/2024) | Ley N° 7446/2024 |
| IRP filing deadline | March (per RUC ending digit) | DNIT |

**Sanity check:** IRP bands 50M < 150M (ordered) ✓; IPS combined 25.5% (commercial) and 28% (financial) are plausible payroll percentages ✓; minimum-wage floor is a positive amount ✓. No confirmed ceiling, so the floor-≤-ceiling check is N/A and flagged as a research gap. (Self-verified.)

## Section 14 -- Penalties

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| IPS Mora Patronal (employer default) | Arises the day after the contribution due date | IPS; Vouga |
| IPS late-payment surcharges (recargos moratorios) | Reported **1% up to 50%** depending on months of delay, plus interest — **[RESEARCH GAP — reviewer to confirm]** (secondary aggregators; confirm against the IPS resolution) | worki360/Deel (secondary) |
| Over-deduction from worker's pay | Deducting more than the 9% employee share is a misappropriation offence | MTESS |
| IRP late filing/payment | Administrative penalties apply to the individual taxpayer — **[RESEARCH GAP — reviewer to confirm]** exact figures not quoted from a primary source | DNIT |

## Section 15 -- Excel Working Paper Template

**Excel working paper template**

| Row | Label | Formula / source |
| --- | --- | --- |
| 1 | Employee name | input |
| 2 | Pay period (month/year) | input |
| 3 | Sector (C = commercial / F = financial) | input |
| 4 | **Gross wage (cash + in kind, excl. aguinaldo/family allowance)** | input |
| 5 | Minimum-wage floor | `3044000` from 1 Jul 2026; `2899048` for 1 Jul 2025 to 30 Jun 2026. Pick from B2, the pay period |
| 6 | IPS base | `=MAX(B4,B5)` (floor; no ceiling) |
| 7 | Employee IPS rate | `=IF(B3="F",0.11,0.09)` |
| 8 | **Employee IPS** | `=B6*B7` |
| 9 | IRP withheld | `=0` (employer never withholds IRP) |
| 10 | **Net pay** | `=B4-B8-B9` |
| 11 | Employer IPS rate | `=IF(B3="F",0.17,0.165)` |
| 12 | **Employer IPS** | `=B6*B11` |
| 13 | **Total employer cost** | `=B4+B12` |
| 14 | Monthly IPS remittance to IPS | `=B8+B12` (employee + employer shares) |
| 15 | Aguinaldo accrual (memo) | `=B4` per month → 1/12 of annual; IPS & IRP exempt |

Reproduce this layout in a single worksheet (one column per employee, or one row per employee for a register). All cells in PYG. **No IRP row** — the employer does not withhold IRP.

**Cross-check against Example B (commercial, gross 5,000,000):** row 6 = 5,000,000; row 8 = 5,000,000 × 0.09 = 450,000; row 10 = 5,000,000 − 450,000 = 4,550,000; row 12 = 5,000,000 × 0.165 = 825,000; row 13 = 5,825,000; row 14 = 450,000 + 825,000 = 1,275,000. ✓ Matches Example B exactly.

## Section 16 -- Bank Statement / Terminology Reading Guide

Common Paraguayan payroll terms (Spanish → English) and typical bank-statement patterns. Match on the **uppercased** description.

### 16.1 Salary credits (to employees)

**Salary credits table**

| Pattern (PYG bank statement) | Classification |
| --- | --- |
| `SUELDO`, `SALARIO`, `PAGO DE SUELDO`, `HABERES` | Net salary payment |
| `PAGO NOMINA`, `PLANILLA DE SUELDOS`, `TRANSFERENCIA SUELDO` | Net salary payment |
| `AGUINALDO`, `13ER SUELDO`, `DECIMO TERCER` | Aguinaldo (13th salary, IPS & IRP exempt) |
| `ANTICIPO`, `ADELANTO DE SUELDO` | Salary advance — reconcile against month-end net |
| `BONIFICACION`, `GRATIFICACION` | Bonus — wage item (review IPS-base inclusion) |

### 16.2 Employer debits to the State (IPS / DNIT)

**Employer debits table**

| Pattern | Classification |
| --- | --- |
| `IPS`, `INSTITUTO DE PREVISION SOCIAL`, `APORTE OBRERO PATRONAL` | IPS contribution (employee + employer shares remitted together) |
| `APORTE PATRONAL`, `APORTE OBRERO` | IPS contribution share |
| `PLANILLA IPS`, `REI` | Monthly IPS payroll-list payment |
| `DNIT`, `IRP`, `MARANGATU` | DNIT / IRP payment (normally the individual's own IRP, not employer payroll) |

### 16.3 Non-payroll / not income

**Non-payroll table**

| Pattern | Classification |
| --- | --- |
| `REEMBOLSO`, `REINTEGRO` | Reimbursement / refund — not salary |
| `VIATICOS`, `GASTOS DE VIAJE` | Travel allowance/expense — review for treatment |
| `CUOTA PRESTAMO`, `DESCUENTO PRESTAMO` | Loan deduction — not an employer cost |

## Section 17 -- Onboarding Fallback

If the user has not provided enough to run payroll, collect in this order:
1. Monthly gross wage in PYG (cash + in kind) — refuse if given in USD or another currency (Section 8.2).
2. Employer sector — commercial (9%/16.5%) or financial (11%/17%).
3. Pay period (month + year) — selects the minimum-wage floor, which changes on 1 July: PYG 3,044,000 from 1 Jul 2026, PYG 2,899,048 before that.
4. Whether the wage includes aguinaldo or family allowance (excluded from the IPS base).
5. Confirm the employer is registered with IPS (REI).
6. Clarify if the user is asking about the employee's IRP self-assessment (annual, individual) rather than employer payroll — the employer does not withhold IRP.

If any required input is missing, state what is missing and do not fabricate a figure.

## Section 18 -- Interaction with Other Skills

**Interaction with other skills table**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (IPS contributions) | **This skill (paraguay-payroll.md)** |
| Individual IRP self-assessment (Form 515) | paraguay-income-tax.md (employee's own annual filing) |
| Paraguay VAT (IVA) returns | paraguay-vat-return.md |
| Paraguay corporate income tax (IRE) | paraguay-corporate-tax.md |
| Paraguay bookkeeping | paraguay-bookkeeping.md |

### Key handoff points

- **Payroll → Bookkeeping:** gross wages and the 16.5% employer IPS are expenses; the 9% employee IPS withheld is a liability until remitted via REI. There is **no IRP withholding liability** on salaries.
- **Payroll → IRP:** the employer issues the payslip/income certificate; the employee uses it for their own Form 515 (only if gross personal-service income > PYG 80M/year). The two are separate filings.

### 19.1 Sources

**Sources table**

| # | Title | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Ley N° 6380/2019 "De Modernización y Simplificación del Sistema Tributario Nacional" (IRP arts. 47-70; IVA art. 90) | BACN (Biblioteca y Archivo Central del Congreso) | https://www.bacn.gov.py/archivos/9332/Ley+6380.pdf |
| 2 | Decreto-Ley N° 1.860/1950, Carta Orgánica del IPS, consolidated with Ley N° 98/1992 and later amendments (arts. 17, 20, 71, 76) | Portal Unificado de Información Pública | https://informacionpublica.paraguay.gov.py/public/241273-CartaOrgnicadelIPSpdf-CartaOrgnicadelIPS.pdf |
| 2a | Tabla de bases mínimas imponibles y porcentajes de aportes al IPS | IPS | https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?c=315 |
| 2b | Ley N° 432/1973 (0.50% additional employer contribution collected by the IPS) | Justia Paraguay (transcription) | https://paraguay.justia.com/nacionales/leyes/ley-432-dec-28-1973/gdoc |
| 2b-i | Ley N° 253/1971 (SNPP), arts. 28-29: 1% of total salaries, deposited with the IPS together with the social-security contributions | Justia Paraguay (transcription) | https://paraguay.justia.com/nacionales/leyes/ley-253-jul-2-1971/gdoc |
| 2c | Ley N° 2856/2005 (Caja de Jubilaciones y Pensiones de Empleados de Bancos y Afines), arts. 9 and 10; Ley N° 73/1991 for the earlier rates | Justia Paraguay (transcription) | https://paraguay.justia.com/nacionales/leyes/ley-2856-jan-3-2006/gdoc |
| 2d | Calendario Perpetuo de Vencimientos (RG N° 01/2007 and 38/2020), DNIT notice of 26 March 2025 | DNIT | https://www.dnit.gov.py/web/portal-institucional/w/calendario-perpetuo-continua-vigente-para-el-iva-irp-y-rentas |
| 3 | IRP — Impuesto a la Renta Personal (institutional portal) | DNIT | https://www.dnit.gov.py/en/web/portal-institucional/irp |
| 4 | IRP Cartilla (al 30.07.24) | DNIT | https://www.dnit.gov.py/documents/20123/233435/IRP+Cartilla+al+30.07.24.pdf |
| 5 | Instructivo del Formulario N° 515 (IRP RSP) | DNIT | https://www.dnit.gov.py/documents/47797/47809/ |
| 6 | IPS — contribución obrero-patronal | Instituto de Previsión Social (IPS) | https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?c=315 |
| 7 | REI — Registro del Empleador por Internet | IPS | https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?e=12 |
| 8 | Resolución MTESS N° 677/2025 — salario mínimo (1 Jul 2025) | MTESS | https://www.mtess.gov.py/?p=30682 |
| 8a | Decreto N° 6225 (17 Jun 2026) + Resolución MTESS N° 670/2026 — salario mínimo (1 Jul 2026) | MTESS | https://www.mtess.gov.py/wp-content/uploads/2026/07/Resolucion-MTESS-N%C2%B0-670-REGLAMENTACION-SALARIO-2026.pdf |
| 9 | El MTESS reglamenta los nuevos salarios mínimos | Vouga Abogados | https://www.vouga.com.py/en/el-mtess-reglamenta-los-nuevos-salarios-minimos/ |
| 10 | El IPS estableció nuevos criterios (Calendario de Pago / Mora Patronal) | Vouga Abogados | https://www.vouga.com.py/en/el-instituto-de-prevision-social-ips-establecio-nuevos-criterios/ |
| 11 | Ley N° 417/73 (aguinaldo) | BACN | https://www.bacn.gov.py/leyes-paraguayas/2518/ |

### 19.2 Test Suite (numbered — recompute to confirm any change)

**Test suite table**

| # | Input | Expected output | Recomputation |
| --- | --- | --- | --- |
| 1 | Commercial, gross 2,899,048 (min wage) | Net 2,638,133.68; employer cost 3,377,390.92 | Ex. A — employee IPS 9% × 2,899,048 = 260,914.32; employer 16.5% = 478,342.92 |
| 2 | Commercial, gross 5,000,000 | Net 4,550,000; employer cost 5,825,000 | Ex. B — employee IPS 450,000; employer 825,000 |
| 3 | Commercial, gross 8,000,000 | Net 7,280,000; employer cost 9,320,000; employee must self-assess IRP (annual 96M > 80M) | Ex. C — employee IPS 720,000; employer 1,320,000; no IRP withheld |
| 4 | Financial, gross 12,000,000 | Net 10,680,000; employer cost 14,040,000 | Ex. D — 11% = 1,320,000; 17% = 2,040,000 |
| 5 | Aguinaldo, 5,000,000/month all year | Aguinaldo 5,000,000 paid in full; IPS 0; IRP 0 | Ex. E — 1/12 × 60,000,000; both exempt |
| 6 | IRP on net taxable 200,000,000 (employee filing) | IRP 18,000,000 | Ex. F — 8%×50M + 9%×100M + 10%×50M = 4M + 9M + 5M |
| 7 | Any salary, employer IRP withholding | 0 — employer never withholds IRP on dependent salaries | Section 2.1 |
| 8 | IPS rate totals | Commercial 25.5%; financial 28% | Section 4.2 — both additions reconcile |
| 9 | Monthly IPS remittance, commercial gross 5,000,000 | 450,000 + 825,000 = 1,275,000 to IPS | Template row 14 |
| 10 | Deadlines | IPS monthly per Calendario de Pago; IRP Form 515 in March | Section 12 |

## PROHIBITIONS

- NEVER withhold IRP from a dependent salary — Paraguay does not withhold income tax on employee wages; IRP is the employee's annual self-assessment (Form 515).
- NEVER compute Paraguayan payroll in USD or any non-PYG currency — refuse and ask for the PYG gross.
- NEVER apply commercial IPS rates (9%/16.5%) to a financial-sector employer, or financial rates (11%/17%) to a commercial employer, without confirming the sector.
- NEVER include the aguinaldo or family allowance in the IPS contribution base.
- NEVER apply IPS contributions to the aguinaldo, and never deduct IPS or IRP from it — it is exempt and unembargable.
- NEVER deduct more than the 9% employee IPS share from the worker's pay — the 16.5% employer share is paid from employer funds (misappropriation offence otherwise).
- NEVER compute the IPS base below the minimum-wage floor in force for the pay period (PYG 3,044,000 from 1 Jul 2026; PYG 2,899,048 from 1 Jul 2025 to 30 Jun 2026).
- NEVER assert an IPS salary ceiling as confirmed — none is confirmed (research gap); treat IPS as uncapped.
- NEVER state exact IPS late-payment surcharges or IRP penalty amounts as confirmed — they are research gaps pending primary-source confirmation.
- NEVER quote IRP deduction figures/caps as confirmed — the deductible categories are a research gap pending Decreto N° 3184/2019 confirmation.
- NEVER apply a minimum wage from the wrong side of 1 July. The floor changes mid-year, not on 1 January: PYG 3,044,000 from 1 Jul 2026 (Decreto N° 6225; MTESS Res. 670/2026), PYG 2,899,048 from 1 Jul 2025 to 30 Jun 2026.
- NEVER present payroll computations as definitive — label them estimated and direct the user to a licensed Paraguayan accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Paraguay) before implementation. This is a Tier 2 (research-verified) skill: figures are sourced to named authorities (DNIT, IPS, MTESS) and Big-4 summaries but have not yet been verified section-by-section by a licensed Paraguayan accountant, and items marked "[RESEARCH GAP — reviewer to confirm]" carry residual uncertainty.

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
