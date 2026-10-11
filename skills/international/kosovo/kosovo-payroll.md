---
name: kosovo-payroll
description: Use this skill whenever asked about Kosovo payroll processing for employed persons. Trigger on phrases like "Kosovo payroll", "Kosova paga", "tatimi mbi pagat", "personal income tax Kosovo", "tatimi në të ardhura personale", "withholding tax Kosovo", "mbajtja në burim", "pension contribution Kosovo", "kontributi pensional", "KPST", "Trusti pensional", "ATK", "TAK", "Administrata Tatimore e Kosovës", "EDI declaration", "WM form Kosovo", "net salary Kosovo", "paga neto", "gross to net Kosovo", "PAYE Kosovo", "employer contributions Kosovo", "minimum wage Kosovo", "paga minimale", "secondary employer Kosovo", "benefit in kind Kosovo", or any question about computing employee pay, withholding personal income tax, or mandatory pension contributions for Kosovo-based employees. This skill covers PIT monthly withholding (progressive 0%/8%/10% bands for the primary employer, flat 10% for secondary employers), mandatory pension contributions (5% employee + 5% employer to KPST), voluntary supplementary pension, benefit-in-kind thresholds, minimum wage, new-hire reporting, and the monthly WM declaration and annual reconciliation. ALWAYS read this skill before processing any Kosovo payroll.
version: 0.3
jurisdiction: XK
tax_year: 2025
last_updated: 2026-10-11
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kosovo Payroll

## Kosovo Payroll Skill v0.3

**Tier 2 — research-verified. Figures below are sourced from the Tax Administration of Kosovo (Administrata Tatimore e Kosovës — TAK/ATK), Law No. 05/L-028 on Personal Income Tax as amended by Law No. 08/L-142 (effective 23 August 2024), Law No. 04/L-101 on Pension Funds (as amended by Laws No. 04/L-168 and 05/L-116), TAK Public Explanatory Decision No. 01/2013 on pension contributions, Law No. 08/L-257 on the Administration of Tax Procedures (which repealed Law No. 03/L-222), and the Kosovo Pension Savings Trust (Trusti i Kursimeve Pensionale të Kosovës — KPST). a secondary practitioner summary remains the source only for the benefit-in-kind threshold, which the law leaves to a sub-legal act not read for this guide. NOT yet signed off by a licensed Kosovo accountant or tax adviser. Treat every computation as an estimate pending professional review.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Kosovo (Republic of Kosovo / Republika e Kosovës) |
| Currency | EUR only (Kosovo uses the euro despite not being a eurozone member) |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) ([Law No. 05/L-028](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) art. 2(1.27)) |
| Tax withholding system | Monthly PIT withholding by the employer for each payroll period; the principal employer reduces each month's tentative tax by the tax withheld in the previous month of the year (Law No. 05/L-028 art. 38(1) and (2)) |
| Income tax authority | Tax Administration of Kosovo (Administrata Tatimore e Kosovës — TAK/ATK), portal atk-ks.org, filing via the EDI electronic declaration system |
| Pension authority | Kosovo Pension Savings Trust (Trusti i Kursimeve Pensionale të Kosovës — KPST); contributions collected via TAK; supervised by the Central Bank of Kosovo (BQK) |
| Key legislation | [Law No. 05/L-028](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) on Personal Income Tax (as amended by Law No. 08/L-142, eff. 23 Aug 2024); [Law No. 04/L-101](https://www.atk-ks.org/wp-content/uploads/2017/07/Law-No.-04-L-101.pdf) on Pension Funds (as amended by Laws No. 04/L-115, 04/L-168 and 05/L-116); [Law No. 08/L-257](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) on the Administration of Tax Procedures (adopted 14 December 2023; art. 122 repeals Law No. 03/L-222) |
| Filing portal | TAK EDI electronic declaration system (via atk-ks.org) |
| Validated by | Pending -- requires sign-off by a licensed Kosovo accountant / tax adviser |
| Skill version | 0.3 |

**Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` — follow that runbook with this skill supplying the Kosovo-specific content.**

### The single most important Kosovo fact

- **Primary vs secondary employer PIT treatment** — The PIT bands an employer applies depend on whether it is the employee's PRIMARY or SECONDARY employer. The primary (main) employer withholds on the progressive monthly bands 0% / 8% / 10%. A secondary employer withholds a flat 10% on all wage income it pays, with no 0% or 8% band — the employee then reconciles on the annual return. If you do not know the employee's status, default to primary (progressive) only if you have confirmed there is no other employer; otherwise treat the second job as secondary and apply the flat 10%. The employee designates the principal employer (art. 2(1.7)).  _(Law No. 05/L-028 art. 38(2) and (3))_

## Section 2 -- Income Tax Withholding (tatimi mbi pagat)

The employer withholds personal income tax (PIT) monthly. The 4% band was removed and the brackets reset by Law No. 08/L-142, effective 23 August 2024; TAK's laws page (read 8 October 2026) lists no later personal income tax law, so the same brackets apply for 2025 and 2026. ([TAK notice of 27 August 2024 quoting Law No. 08/L-142 art. 5](https://www.atk-ks.org/en/notice-to-taxpayers-personal-income-tax-rates-are-changed/))

### Monthly Wage Bands — PRIMARY employer (2025)

**Monthly Wage Bands — PRIMARY employer (2025)**  _(TAK notice of 27 August 2024, which gives these monthly bands beside the annual ones in Law No. 05/L-028 art. 6 as replaced by Law No. 08/L-142 art. 5)_

| Band | Monthly PIT base (EUR) | Rate |
| --- | --- | --- |
| 1 | 0.00 -- 250.00 | 0% |
| 2 | 250.01 -- 450.00 | 8% |
| 3 | above 450.00 | 10% |

- **Maximum tax in 8% band** — The maximum tax in the 8% band is EUR 16.00 (8% × the EUR 200.00 width of the 250.01–450.00 band; verify: 0.08 × 200 = 16.00 ✓). Everything above EUR 450.00 of base is taxed at 10%.  _(TAK notice of 27 August 2024)_

### Secondary employer — flat 10%

- **Secondary employer flat rate** — A secondary employer withholds a flat 10% on all wage income it pays — no 0% or 8% band is applied. The employee may reconcile the total across all employers on the annual PIT return; one with wages only is not required to file (art. 48(2) and (3)).  _(Law No. 05/L-028 art. 38(3))_

### Annual Bands — reconciliation / equivalent (2025)

**Annual Bands — reconciliation / equivalent (2025)**  _(Law No. 05/L-028 art. 6, as replaced by Law No. 08/L-142 art. 5)_

| Band | Annual income (EUR) | Rate |
| --- | --- | --- |
| 1 | 0.00 -- 3,000.00 | 0% |
| 2 | 3,000.01 -- 5,400.00 | 8% |
| 3 | above 5,400.00 | 10% |

- **Annual bands derivation and usage** — The annual bands are the monthly bands × 12 (250 × 12 = 3,000 ✓; 450 × 12 = 5,400 ✓) and drive the annual reconciliation, not each individual pay run. Each pay run uses the MONTHLY bands.  _(Law No. 05/L-028 arts. 6 and 38(2); TAK notice of 27 August 2024)_

### Monthly Withholding Method (primary employer)

- **Deterministic withholding order** — 1. Start with gross salary (paga bruto). 2. Subtract the employee's pension contribution (Section 3): the mandatory 5% plus any voluntary employee contribution, up to 15% of gross in total, reduces the PIT base. 3. Add any taxable benefit in kind to the extent it exceeds EUR 65/month (Section 5). 4. The result is the monthly PIT base. 5. Apply the monthly bands: 0% on the first EUR 250.00, 8% on EUR 250.01–450.00, 10% on the portion above EUR 450.00. 6. The sum is the withheld PIT for the month. The employer then adds the 5% employer pension contribution on top of gross (an employer cost, not a deduction — see Section 4).  _([TAK Public Explanatory Decision No. 01/2013](https://www.atk-ks.org/wp-content/uploads/2017/08/Vendim-Shpjegues-Publik-NR-01-2013Anglisht.pdf) art. 6; Law No. 04/L-101 art. 37.2, as replaced by [Law No. 05/L-116 art. 10](https://bqk-kos.org/wp-content/uploads/2024/10/Ligji-05L116-per-ndryshimin-e-fondeve-pensionale.pdf); Law No. 05/L-028 art. 9(1.8) for benefits in kind)_

TAK states the base directly: "The bases for calculation of Personal Income Tax for employees will be considered gross salary after deduction of Pension Contribution (employee's share)" (TAK Decision 01/2013 art. 6). **[T2-1 — reviewer to confirm]** how the EDI WM form applies the art. 38(2) prior-month reduction when pay changes during the year.

## Section 3 -- Contributions: Employee Deductions (Pension)

- **No employee social security beyond pension** — Kosovo has no employee social-security tax beyond the mandatory pension. The employee pays a 5% mandatory pension contribution, withheld from gross and remitted to the Kosovo Pension Savings Trust (KPST) via TAK.  _([Law No. 04/L-101](https://www.atk-ks.org/wp-content/uploads/2017/07/Law-No.-04-L-101.pdf) art. 6.2(b) and 6.3)_

**Employee pension contributions table**  _(Law No. 04/L-101 art. 6.2; TAK Decision 01/2013 arts. 4 and 5)_

| Contribution | Rate | Payer | Authority | Note |
| --- | --- | --- | --- | --- |
| Mandatory pension — employee share | 5% of gross salary | Employee (withheld) | KPST (collected via TAK) | The only mandatory employee deduction besides PIT |
| Voluntary supplementary pension — employee | up to a further 10%, 15% of gross salary in total | Employee (elective) | KPST or a supplementary fund | Optional; deductible with the mandatory share up to 15% of gross |

### Total mandatory employee deductions

**Total mandatory employee deductions**  _(Law No. 05/L-028 art. 38; Law No. 04/L-101 art. 6.2(b))_

| Item | Rate / basis |
| --- | --- |
| PIT | 0% / 8% / 10% monthly bands (primary) or flat 10% (secondary) on the PIT base |
| Mandatory pension | 5% of gross salary |

Both are withheld from gross wage. (Law No. 05/L-028 art. 38(1); Law No. 04/L-101 art. 6.3)

## Section 4 -- Contributions: Employer Contributions (Pension)

- **Employer pension contribution and PIT not employer cost** — The employer pays a 5% mandatory pension contribution on top of gross salary, remitted to KPST via TAK. There is no employer social-security, health, or unemployment levy beyond the mandatory pension. PIT is fully employee-borne (withheld), not an employer cost.  _(Law No. 04/L-101 art. 6.2(a) and 37.1)_

**Employer pension contributions table**

| Contribution | Rate | Payer | Authority | Ceiling | Note |
| --- | --- | --- | --- | --- | --- |
| Mandatory pension — employer share | 5% of gross salary | Employer (on top of gross) | KPST (via TAK) | None (art. 6.2) | Sole mandatory employer-borne contribution |
| Voluntary supplementary pension — employer | up to a further 10%, 15% of gross salary in total | Employer (elective) | KPST or a supplementary fund | — | Optional |

### Combined mandatory pension

**Combined mandatory pension**  _(Law No. 04/L-101 art. 6.2(a) and (b))_

| Share | Rate of gross |
| --- | --- |
| Employee | 5% |
| Employer | 5% |
| **Total mandatory pension** | **10%** |

(verify: 5% + 5% = 10% ✓) (Law No. 04/L-101 art. 6.2; TAK Decision 01/2013 art. 4)

### Voluntary supplementary pension

- **Total employer cost formula** — Total employer cost = gross salary + (5% × gross salary) = gross × 1.05. PIT does not appear in employer cost because it is withheld from the employee's gross, not added on top.  _(Law No. 04/L-101 art. 6.2(a); Law No. 05/L-028 art. 38(1))_
- **Voluntary contribution limits and deductibility** — Voluntary contributions may take each side to 15% of gross salary (30% combined). The employee's share up to 15% of gross reduces the employee's PIT base, and the employer's share up to 15% is a deductible expense for the employer; contributions to KPST or a supplementary fund are not subject to PIT.  _(Law No. 04/L-101 arts. 6.2(c) and 37.1 to 37.2, as replaced by Law No. 05/L-116 art. 10; TAK Decision 01/2013 arts. 5 and 6)_

### Pension contribution base: minimum-wage floor, no ceiling

- **Floor** — Where a full-time employee is paid less than the minimum wage, the employer pays 5% of the minimum wage and the employee 5% of the actual wage. A secondary employer, or a primary employer of a part-time employee, uses the actual gross wage even below the minimum wage.  _(Law No. 04/L-101 art. 6.6; TAK Decision 01/2013 art. 7)_
- **No ceiling** — Art. 6.2 levies 5% + 5% on total wages with no upper limit; Law No. 04/L-168 amended only art. 6.12 (self-employed) and Law No. 05/L-116 did not amend art. 6. Version 0.1 left a possible cap open as a research gap; there is none to apply.  _(Law No. 04/L-101 art. 6.2)_

### Benefit-in-kind threshold

- **BIK tax-free threshold** — Benefits in kind are taxable as wages to the extent they exceed EUR 65 per month. The first EUR 65/month of benefits in kind is tax-free; only the excess is added to the PIT base. Meals and transport provided in kind, actual business travel reimbursed within ministerial limits and work-accident indemnity are not wages.  _(Law No. 05/L-028 art. 9(1.8) and (2) leaves the threshold to a sub-legal act of the Minister, which was not read; the EUR 65 figure is from a secondary summary. **[RESEARCH GAP — confirm the figure in the current administrative instruction.]**)_

### National Minimum Gross Wage (paga minimale)

**National Minimum Gross Wage (paga minimale)**

| Period | Monthly gross (EUR) | Note |
| --- | --- | --- |
| Through 2025 | 350.00 | In force during 2025 (Balkanweb / WageIndicator, reporting Government decision) |
| From 1 January 2026 | 425.00 | Government decision 10/273, 31 Oct 2025 (Balkanweb; WageIndicator) |
| From 1 July 2026 | 500.00 | Government decision 10/273 (Balkanweb) |

- **Apply EUR 350 to 2025 only** — Apply EUR 350 to 2025 pay periods only. The EUR 425 and EUR 500 figures take effect in 2026 and must NOT be applied to 2025 runs.  _(Balkanweb; WageIndicator)_

### Working hours and overtime

**[RESEARCH GAP — reviewer to confirm]** Statutory overtime multipliers, maximum weekly hours, and night/weekend/holiday premiums under the Kosovo Labour Law were not part of this research dataset. A reviewer should populate these from the Labour Law (Ligji i Punës) and any applicable collective agreement before relying on overtime figures.

## Section 6 -- Conservative Defaults

When an input is unknown, the skill MUST apply the conservative default below and flag the assumption in its output rather than guessing a more favourable figure.

**Conservative Defaults table**

| Field | Default | Rationale |
| --- | --- | --- |
| Employer status (primary vs secondary) | **Primary** ONLY if it is confirmed the employee has no other employer; otherwise treat a second job as **secondary** (flat 10%) | Secondary employment is withheld at a flat 10% with no 0%/8% band; defaulting wrongly to primary would under-withhold. (Law No. 05/L-028 art. 38(2) and (3)) |
| Mandatory pension | **5% employee + 5% employer, no voluntary top-up** | Voluntary contributions are optional and not assumed unless elected. (Law No. 04/L-101 art. 6.2) |
| PIT base | **Gross − employee pension (+ BIK above EUR 65)** | TAK Decision 01/2013 art. 6 sets the base as gross after the employee's pension share. |
| Minimum wage | **EUR 350/month for 2025 pay periods; EUR 425 from 1 Jan 2026** | EUR 350 was the rate in force during 2025; the increase takes effect 1 Jan 2026. (Balkanweb; WageIndicator) |
| Benefit in kind | **Tax-free only up to EUR 65/month; excess added to PIT base** | Threshold set by sub-legal act under art. 9(1.8); figure from practitioner summaries. **[RESEARCH GAP]** |
| Pension base cap | **None** | Law No. 04/L-101 art. 6.2 sets no ceiling. |
| Employer cost estimate | **Gross × 1.05** (add 5% employer pension) | Single mandatory employer-borne contribution; PIT is not an employer cost. (Law No. 04/L-101 art. 6.2(a)) |
| Remittance timing | **15th of the following month** for the monthly WM declaration and payment | Within 15 days after the end of each month. (Law No. 05/L-028 art. 38(5)) |

## Section 7 -- Required Inputs and Refusal Catalogue

### Required inputs before any computation

- **Required inputs list** — 1. Gross monthly salary (paga bruto) in EUR. 2. Employer status — is this the employee's PRIMARY or SECONDARY employer? (Drives progressive bands vs flat 10%.) 3. Pay period (month and year) — to pick the correct minimum wage and band figures (2025 vs 2026). 4. Whether any benefit in kind is provided, and its monthly value (taxable above EUR 65). 5. Whether any voluntary supplementary pension is elected (and by whom) — otherwise mandatory 5% + 5% only. 6. Whether the employee is a new hire this period — triggers TAK notification one day before the start date.

### Refusal Catalogue — DO NOT attempt; route to a licensed accountant

**Refusal Catalogue table**

| Scenario | Why it is out of scope |
| --- | --- |
| Posted workers / cross-border social-security coordination / totalization | Requires treaty and KPST/TAK determinations — see `cross-border-payroll-coordination`. |
| Non-resident employees, double-tax-treaty relief, expat tax-equalisation | Treaty residency and tie-breaker analysis is beyond a domestic payroll run. |
| Severance / termination payment taxation | Not in scope; route to a reviewer. |
| Self-employed / sole-trader contributions | Different regime — out of scope for employer payroll. |
| Overtime / night / holiday premium computation | Labour Law multipliers not in this research dataset. **[RESEARCH GAP]** |

## Section 8 -- Transaction / Payment Pattern Library

Deterministic classification of Kosovo bank-statement lines for payroll. Match on the uppercased description fragment. Descriptions appear in Albanian (sq), Serbian (sr) and English.

### Salary credits (what lands in the employee's account)

**Salary credits table**

| Bank statement text (SQ / EN) | Classification |
| --- | --- |
| `PAGA`, `PAGA NETO`, `PAGESA E PAGES` | Net salary payment |
| `SALARY`, `WAGES`, `NET SALARY` | Net salary payment (English variant) |
| `PARADHENIE`, `AVANS` | Salary advance (not final pay) |
| `SHTESA`, `BONUS`, `KOMPENSIM` | Allowance / bonus (check taxability) |
| `MEDITJE`, `PER DIEM` | Per-diem / travel allowance (may be tax-exempt up to limits — verify) |
| `KTHIM TATIMI`, `TAX REFUND` | PIT refund — NOT income |

### Employer debits (what leaves the employer's account)

**Employer debits table**

| Bank statement text (SQ / EN) | Classification |
| --- | --- |
| `TATIMI NE BURIM`, `TATIMI MBI PAGAT`, `ATK`, `TAK` | PIT withheld, remitted to the Tax Administration |
| `KONTRIBUTI PENSIONAL`, `PENSION`, `KPST`, `TRUSTI` | Mandatory pension contribution remittance (employee 5% + employer 5%) to KPST |
| `WM`, `EDI` | Reference tag for the monthly WM declaration / EDI payment batch |
| `PAGESA E PAGAVE`, `PAYROLL`, `LISTA E PAGAVE` | Net wages disbursed to employees |

PIT is remitted to TAK; the mandatory pension (5% + 5%) is collected by TAK and routed to KPST. Both are declared together on the monthly WM declaration via the EDI system (Section 12). **[T2-3 — the exact WM form code was not verified against a live TAK/EDI page; treat the WM label as the commonly used wage/withholding form and confirm on the EDI portal.]**

## Section 9 -- Worked Examples

All examples use 2025 figures. The mandatory pension is 5% employee + 5% employer. The PIT base is gross less the 5% employee pension (plus any BIK above EUR 65) per the Section 2 method **[T2-1]**. Primary-employer examples use the progressive monthly bands (0% / 8% / 10%); the secondary-employer example uses the flat 10%. Every line below was recomputed end-to-end.

### Example 1 — Standard primary-employer employee, EUR 500 gross/month

Bank statement context: `PAGA NETO … 456,50 EUR` credited to the employee; `ATK … 18,50 EUR` (PIT) and `KPST … 50,00 EUR` (pension, 5%+5%) debited from the employer.

**Example 1 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 500.00 |
| Employee pension (5% of 500) | — | 25.00 |
| PIT base | 500 − 25 | 475.00 |
| PIT — band 1 (0% on first 250) | 250 × 0% | 0.00 |
| PIT — band 2 (8% on 250.01–450) | 200 × 8% | 16.00 |
| PIT — band 3 (10% on 450.01–475) | 25 × 10% | 2.50 |
| Total PIT | 0 + 16 + 2.50 | 18.50 |
| **Net pay** | 500 − 25 − 18.50 | **456.50** |
| Employer pension (5% of 500) | on top of gross | 25.00 |
| **Total employer cost** | 500 + 25 | **525.00** |

### Example 2 — Minimum-wage worker (2025), EUR 350 gross/month, primary

**Example 2 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 350.00 |
| Employee pension (5% of 350) | — | 17.50 |
| PIT base | 350 − 17.50 | 332.50 |
| PIT — band 1 (0% on first 250) | 250 × 0% | 0.00 |
| PIT — band 2 (8% on 250.01–332.50) | 82.50 × 8% | 6.60 |
| PIT — band 3 (10% above 450) | none | 0.00 |
| Total PIT | — | 6.60 |
| **Net pay** | 350 − 17.50 − 6.60 | **325.90** |
| Employer pension (5% of 350) | on top | 17.50 |
| **Total employer cost** | 350 + 17.50 | **367.50** |

### Example 3 — Part-time employee inside the 0% band, EUR 250 gross/month, primary

**Example 3 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 250.00 |
| Employee pension (5% of 250) | — | 12.50 |
| PIT base | 250 − 12.50 | 237.50 |
| PIT — band 1 (0% — base ≤ 250) | 237.50 × 0% | 0.00 |
| Total PIT | — | 0.00 |
| **Net pay** | 250 − 12.50 − 0 | **237.50** |
| Employer pension (5% of 250) | on top | 12.50 |
| **Total employer cost** | 250 + 12.50 | **262.50** |

EUR 250 is below the 2025 minimum wage of EUR 350, so this works only for a part-time employee, whose pension is computed on the actual gross (TAK Decision 01/2013 art. 7). For a full-time employee paid EUR 250, the employer's 5% would be computed on the EUR 350 minimum wage (EUR 17.50) while the employee's stays at 5% of EUR 250 (Law No. 04/L-101 art. 6.6); a full-time employee may not lawfully be paid below the minimum wage in any case.

### Example 4 — Mid earner across all three bands, EUR 1,000 gross/month, primary

**Example 4 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 1,000.00 |
| Employee pension (5% of 1,000) | — | 50.00 |
| PIT base | 1,000 − 50 | 950.00 |
| PIT — band 1 (0% on first 250) | 250 × 0% | 0.00 |
| PIT — band 2 (8% on 250.01–450) | 200 × 8% | 16.00 |
| PIT — band 3 (10% on 450.01–950) | 500 × 10% | 50.00 |
| Total PIT | 0 + 16 + 50 | 66.00 |
| **Net pay** | 1,000 − 50 − 66 | **884.00** |
| Employer pension (5% of 1,000) | on top | 50.00 |
| **Total employer cost** | 1,000 + 50 | **1,050.00** |

### Example 5 — Secondary employer, EUR 800 gross/month, FLAT 10%

**Example 5 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary (from this secondary job) | — | 800.00 |
| Employee pension (5% of 800) | — | 40.00 |
| PIT base | 800 − 40 | 760.00 |
| PIT — flat 10% (no 0%/8% band) | 760 × 10% | 76.00 |
| **Net pay** | 800 − 40 − 76 | **684.00** |
| Employer pension (5% of 800) | on top | 40.00 |
| **Total employer cost** | 800 + 40 | **840.00** |

A secondary employer applies a flat 10% to all wage income — no 0% or 8% band. The employee may reconcile the combined income across all employers on the annual PIT return (where the progressive annual bands apply). (Law No. 05/L-028 arts. 38(3) and 48(3)) **[T2-4 — art. 38(3) says "ten percent (10%) of the wages"; this example applies it to wages after the employee's pension share, following TAK Decision 01/2013 art. 6, and flags it for review.]**

### Example 6 — Primary employee with a benefit in kind, EUR 600 gross + EUR 100/month BIK

**Example 6 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Cash gross salary | — | 600.00 |
| Employee pension (5% of 600) | — | 30.00 |
| Cash base after pension | 600 − 30 | 570.00 |
| Taxable BIK (excess over 65) | 100 − 65 | 35.00 |
| PIT base | 570 + 35 | 605.00 |
| PIT — band 1 (0% on first 250) | 250 × 0% | 0.00 |
| PIT — band 2 (8% on 250.01–450) | 200 × 8% | 16.00 |
| PIT — band 3 (10% on 450.01–605) | 155 × 10% | 15.50 |
| Total PIT | 0 + 16 + 15.50 | 31.50 |
| **Net cash pay** | 600 − 30 − 31.50 | **538.50** |
| Employer pension (5% of cash gross 600) | on top | 30.00 |
| **Total employer cash cost** | 600 + 30 | **630.00** (plus the cost of providing the EUR 100 benefit) |

Only the EUR 35 BIK excess over the EUR 65/month threshold enters the PIT base; the first EUR 65 is tax-free. (Law No. 05/L-028 art. 9(1.8); EUR 65 figure from a secondary summary) **[T2-5 — whether the taxable BIK also enters the pension base was not resolved; this example applies the 5% pension to cash gross only and flags it.]**

## Section 10 -- Tier 1 Rules (deterministic — the skill applies these directly)

- **T1-1 Monthly wage PIT primary** — Monthly wage PIT (PRIMARY employer): 0% on the first EUR 250, 8% on EUR 250.01–450.00, 10% above EUR 450.00. The 4% band was removed and brackets reset by Law No. 08/L-142, effective 23 Aug 2024.  _(TAK notice of 27 August 2024)_
- **T1-2 Secondary employer flat rate** — SECONDARY employers withhold a flat 10% on all wage income they pay; no 0%/8% band. The employee may reconcile on the annual return.  _(Law No. 05/L-028 arts. 38(3) and 48(3))_
- **T1-3 Annual PIT bands** — Annual PIT bands (reconciliation/equivalent): 0% to EUR 3,000; 8% on EUR 3,000.01–5,400; 10% above EUR 5,400 (= monthly bands × 12). Each pay run uses the MONTHLY bands, not the annual bands.  _(Law No. 05/L-028 art. 6, as replaced by Law No. 08/L-142 art. 5)_
- **T1-4 Mandatory pension** — Mandatory pension: 5% withheld from the employee + 5% paid by the employer = 10% of gross salary, remitted to KPST via TAK.  _(Law No. 04/L-101 art. 6.2 and 6.3)_
- **T1-5 Voluntary supplementary pension** — Voluntary supplementary pension up to 15% each (employer + employee, 30% combined) is permitted; the employee's share up to 15% of gross reduces the PIT base and the employer's share up to 15% is deductible for the employer.  _(Law No. 04/L-101 art. 6.2(c); TAK Decision 01/2013 arts. 5 and 6)_
- **T1-6 Employer cost formula** — Employer cost = gross salary + 5% employer pension (gross × 1.05). PIT is fully employee-borne via withholding and is NOT an employer cost.  _(Law No. 04/L-101 art. 6.2(a))_
- **T1-7 Monthly computation** — Withholding on wages is computed monthly to match the pay period; the monthly bands drive each pay run.  _(Law No. 05/L-028 art. 38(1) and (2))_
- **T1-8 BIK threshold** — Benefits in kind are taxable as wages to the extent they exceed EUR 65/month; the first EUR 65/month is tax-free.  _(Law No. 05/L-028 art. 9(1.8); figure from a secondary summary)_
- **T1-9 Monthly WM deadline** — Monthly WM declaration and payment of withheld PIT and pension contributions is due by the 15th of the following month via the TAK EDI system.  _(Law No. 05/L-028 art. 38(5))_
- **T1-10 Annual PIT return deadline** — The annual individual PIT return is due 31 March of the following year; the tax period is the calendar year.  _(Law No. 05/L-028 arts. 2(1.27) and 48(1))_
- **T1-11 New-hire notification** — The employer must notify TAK of each new employment contract one day before the employee starts work; the fine is EUR 500 for each undeclared worker.  _([Law No. 08/L-257](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) arts. 43(5) and 102(3))_
- **T1-12 Minimum gross wage** — Minimum gross wage (full-time): EUR 350/month during 2025; EUR 425 from 1 Jan 2026 and EUR 500 from 1 Jul 2026 (Government decision 10/273). Apply EUR 350 to 2025 pay periods only.  _(Balkanweb; WageIndicator)_
- **T1-13 Currency** — Currency is the euro (EUR); Kosovo uses the euro despite not being a eurozone member.

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue table**

| Ref | Issue | What the reviewer must resolve |
| --- | --- | --- |
| **[T2-1]** | Prior-month reduction on the WM form | Confirm how the EDI WM form applies the art. 38(2) reduction for tax withheld in the previous month when pay changes during the year. |
| **[T2-3]** | Exact WM form code / EDI form name | The 'WM' label was not verified against a live TAK page; confirm the precise wage-withholding declaration code on the EDI portal. |
| **[T2-4]** | Secondary-employer 10% base | Whether the flat 10% applies to gross or gross-less-pension was not verified. |
| **[T2-5]** | Pension base for benefits in kind | Whether the taxable BIK excess enters the 5% pension base was not resolved. |
| **[T2-6]** | Benefit-in-kind threshold | Confirm the EUR 65 figure in the current ministerial instruction under art. 9(1.8). |
| **[T2-7]** | Overtime / night / holiday premiums under the Labour Law | Not researched here — confirm from the Kosovo Labour Law (Ligji i Punës) and any collective agreement. |
| **[T2-9]** | Per-diem / travel-allowance and severance tax limits | Not in this research dataset — reviewer to populate. |

## Section 12 -- Filing Obligations

### Monthly — WM declaration

**Monthly WM declaration table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| **WM** — Statement of Tax Withheld on Wages and Pension Contributions | Monthly declaration and payment of PIT withheld on wages plus the mandatory (5% + 5%) pension contributions; filed electronically via the TAK EDI system. | By the **15th** day of the month following the pay period. (Law No. 05/L-028 art. 38(5)) **[T2-3 — exact WM form code unverified.]** |
| Payment of PIT + pension contributions | Remittance of withheld PIT and pension contributions to TAK (pension routed to KPST) | Same as the WM deadline — the 15th of the following month. (Law No. 05/L-028 art. 38(5); Law No. 04/L-101 art. 6.3) |
| Withholding statement (interest, royalties, rent, other withholdings) | Statement and payment of other amounts withheld | Within 15 days after the end of the month. (Law No. 05/L-028 arts. 39(3) and (4) and 40(2)) |
| Annual withholding certificate to each employee | Certificate of tax withheld for the year | By **1 March** of the following year. (Law No. 05/L-028 art. 38(6)) |

### Annual

**Annual filing table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Annual Personal Income Tax Return (individual) | Annual reconciliation of PIT, including where the taxpayer had multiple employers (primary + secondary); optional where wages are the only income | **31 March** of the following year. (Law No. 05/L-028 art. 48(1) to (3)) |

### Employee registration

**Employee registration table**

| Item | Requirement | Timing |
| --- | --- | --- |
| New-hire notification to TAK | Employer must notify TAK of each new employment contract | **One day before** the employee starts work. (Law No. 08/L-257 art. 43(5)) |

## Section 13 -- Penalties

[Law No. 08/L-257 on the Administration of Tax Procedures](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf), adopted 14 December 2023, repealed Law No. 03/L-222 (art. 122). Its fines:

**Penalties table**

| Trigger | Consequence |
| --- | --- |
| Failure to file a declaration that results in a liability (incl. the WM declaration) | **EUR 50** per declaration for a business natural person, **EUR 150** for a legal entity, **EUR 20** for a non-business natural person. (Law No. 08/L-257 art. 99) |
| Understatement / under-declaration of tax | **15%** of the shortfall where it is 10% or less of the correct tax; **25%** where it is more. (Law No. 08/L-257 art. 100(1)) |
| Failure to withhold or pay over wage tax or pension contributions | **25%** of the amount not paid over. (Law No. 08/L-257 art. 103) |
| New employee not notified to TAK | **EUR 500** for each undeclared worker. (Law No. 08/L-257 art. 102(3)) |
| Late payment of tax / contributions | **Interest accrues monthly** (per month or part-month) at a rate the Minister sets at least once a year above the commercial bank lending rate; calculated for up to 10 years from the due date. (Law No. 08/L-257 art. 24) |
| Fine reductions | 75% off for voluntary disclosure before notice of an investigation; 50% off a fine paid within 15 days of notice, except art. 103 fines. (Law No. 08/L-257 art. 110(1) and (7)) |
| Record-keeping | Keep records for at least **six years** after the end of the tax period. (Law No. 08/L-257 art. 6(3.1)) |

## Section 14 -- Excel Working Paper Template

**Excel Working Paper Template**

| Col | Heading | Type | Formula / source |
| --- | --- | --- | --- |
| A | Employee name | Input | — |
| B | Fiscal/personal number | Input | TAK / employee ID |
| C | Employer status (P/S) | Input | P = primary (progressive), S = secondary (flat 10%) |
| D | Gross salary (EUR) | Input | paga bruto |
| E | Employee pension (5%) | Computed | `D * 5%` |
| F | Taxable BIK (excess over 65) | Input/Computed | `MAX(bik - 65, 0)` |
| G | PIT base | Computed | `D - E + F` |
| H | PIT — band 1 (0%) | Computed | `0` |
| I | PIT — band 2 (8%) | Computed | `IF(C="S", 0, MAX(MIN(G,450)-250,0) * 8%)` |
| J | PIT — band 3 (10%) | Computed | `IF(C="S", G*10%, MAX(G-450,0) * 10%)` |
| K | PIT withheld | Computed | `H + I + J` |
| L | Net pay | Computed | `D - E - K` |
| M | Employer pension (5%) | Computed | `D * 5%` |
| N | Total employer cost | Computed | `D + M` |

Footer checks: sum of column K ties to the WM declaration PIT line; sum of (E + M) ties to the KPST pension remittance (10% of total gross); sum of L ties to the total net wages disbursed; sum of N ties to total employer cost. For a secondary employer (C="S"), the flat 10% applies to the whole PIT base (column J), and columns H and I are zero. **[T2-4]**

## Section 15 -- Kosovo Bank Statement & Terminology Reading Guide

**Terminology Reading Guide**

| Albanian / term | English | Relevance |
| --- | --- | --- |
| Paga bruto | Gross salary | Starting figure for all computations |
| Paga neto | Net salary | What the employee receives |
| Tatimi mbi pagat / tatimi në burim | Wage tax / withholding tax | PIT withheld monthly |
| Tatimi në të ardhura personale | Personal income tax (PIT) | The tax being withheld |
| Kontributi pensional | Pension contribution | 5% employee + 5% employer |
| KPST / Trusti i Kursimeve Pensionale | Kosovo Pension Savings Trust | Receives the mandatory pension |
| ATK / TAK / Administrata Tatimore e Kosovës | Tax Administration of Kosovo | Receives PIT; runs the EDI system |
| EDI | Electronic declaration system | Electronic filing of the WM declaration |
| WM | Wage / withholding declaration | Monthly PIT + pension declaration **[T2-3]** |
| Paga minimale | Minimum wage | EUR 350 (2025) / EUR 425 (Jan 2026) / EUR 500 (Jul 2026) |
| Përfitim në natyrë | Benefit in kind | Taxable above EUR 65/month |
| Punëdhënësi parësor | Primary employer | Applies progressive 0%/8%/10% bands |
| Punëdhënësi dytësor | Secondary employer | Applies flat 10% |
| Meditje | Per diem / travel allowance | May be tax-exempt up to limits (verify) |
| BQK | Central Bank of Kosovo | Supervises KPST |

## Section 16 -- Onboarding Fallback

When key facts are missing, ask the user these questions before computing. If a question is unanswered, apply the Section 6 conservative default and clearly flag the assumption. 1. What is the employee's gross monthly salary in EUR? 2. Is this the employee's primary or secondary employer? (Primary → progressive 0%/8%/10%; secondary → flat 10%.) 3. Which month and year is this pay run for? (Determines minimum wage and band figures — 2025 vs 2026.) 4. Is any benefit in kind provided, and what is its monthly value? (Taxable above EUR 65/month.) 5. Is any voluntary supplementary pension elected, and by whom? (If none → mandatory 5% + 5% only.) 6. Is the employee a new hire this period? (Triggers TAK notification one day before the start date.)

## Section 17 -- Interaction with Other Skills

**Interaction with Other Skills table**

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (PIT + mandatory pension) | **This skill (kosovo-payroll.md)** |
| Kosovo personal income tax (annual / self-employment) | kosovo-income-tax.md |
| Kosovo VAT (TVSH) returns | kosovo-vat.md |
| Cross-border / posted workers / coordination | cross-border-payroll-coordination.md |
| Shared workflow runbook | payroll-workflow-base.md |

### Key handoff points

- Payroll → Bookkeeping: Gross wages and the 5% employer pension are expenses; withheld PIT and the 5% employee pension are liabilities until remitted via the monthly WM declaration.
- Payroll → Income tax: Employees with more than one employer (primary + secondary, the latter withheld at flat 10%) reconcile on the annual PIT return due 31 March.
- Payroll → Pension: Mandatory contributions (5% + 5%) paid through payroll build the employee's KPST pension entitlement.

## Section 18 -- Reference Material

**Reference Material table**

| # | Source | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Law No. 05/L-028 on Personal Income Tax (English) | Tax Administration of Kosovo (ATK) | https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf |
| 2 | Law No. 04/L-101 on Pension Funds of Kosovo (English) | Tax Administration of Kosovo (ATK) | https://www.atk-ks.org/wp-content/uploads/2017/07/Law-No.-04-L-101.pdf |
| 3 | Law No. 04/L-168 amending Law No. 04/L-101 (English; art. 3 caps the self-employed obligatory contribution) | Central Bank of Kosovo (BQK) | https://bqk-kos.org/wp-content/uploads/2024/11/Ligji-fondet-pensionale-te-Kosoves-anglisht.pdf |
| 4 | Law No. 05/L-116 amending Law No. 04/L-101 (Albanian; Official Gazette 3/2017) | Central Bank of Kosovo (BQK) | https://bqk-kos.org/wp-content/uploads/2024/10/Ligji-05L116-per-ndryshimin-e-fondeve-pensionale.pdf |
| 5 | TAK Public Explanatory Decision No. 01/2013 on the pension law (rates, PIT base, minimum-wage base) | Tax Administration of Kosovo (ATK) | https://www.atk-ks.org/wp-content/uploads/2017/08/Vendim-Shpjegues-Publik-NR-01-2013Anglisht.pdf |
| 6 | Law No. 08/L-257 on the Administration of Tax Procedures (fines, interest, new-hire notice, records) | Tax Administration of Kosovo (ATK) | https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf |
| 7 | Kosovo — Individual — Income determination (BIK EUR 65 threshold only) | secondary practitioner summary (link removed) | n/a |
| 8 | Notice to taxpayers — Personal Income Tax rates are changed (Law No. 08/L-142, eff. 23 Aug 2024) | Tax Administration of Kosovo (ATK) | https://www.atk-ks.org/en/notice-to-taxpayers-personal-income-tax-rates-are-changed/ |
| 9 | Kosovo minimum wage decision — EUR 425 (Jan 2026) / EUR 500 (Jul 2026), prior EUR 350 | Balkanweb / News24 (reporting Government decision 10/273) | https://www.balkanweb.com/en/425-euro-nga-janari-dhe-500-nga-korriku-hyn-ne-fuqi-vendimi-per-pagen-minimale-ne-kosove/ |
| 10 | Minimum Wage Updated in Kosovo from 01 January 2026 | WageIndicator.org | https://wageindicator.org/salary/minimum-wage/minimum-wages-news/2026/minimum-wage-updated-in-kosovo-from-01-january-2026-january-01-2026 |

Primary authorities: Tax Administration of Kosovo — TAK/ATK (https://www.atk-ks.org); Kosovo Pension Savings Trust — KPST (https://www.trusti.org); Central Bank of Kosovo — BQK (https://www.bqk-kos.org); filing via the TAK EDI electronic declaration system. **Research note (8 October 2026):** atk-ks.org answered normally and the rates, pension rules, deadlines and fines above were checked against the law texts it publishes. The WM form code and the BIK threshold were not verified against a primary text and remain flagged above.

### Test Suite

Run these to validate any implementation of this skill. Expected results use 2025 figures, mandatory pension 5% + 5%, and the Section 2 PIT-base method (gross − employee pension + BIK above 65).
1. Standard primary earner. EUR 500 gross, primary, no BIK. Expect: pension EUR 25.00, PIT base EUR 475.00, PIT EUR 18.50 (0 + 16.00 + 2.50), net EUR 456.50, employer pension EUR 25.00, total employer cost EUR 525.00.
2. Minimum-wage worker (2025). EUR 350 gross, primary. Expect: pension EUR 17.50, PIT base EUR 332.50, PIT EUR 6.60, net EUR 325.90, employer cost EUR 367.50.
3. 0% band only. EUR 250 gross, primary, part-time. Expect: pension EUR 12.50, PIT base EUR 237.50, PIT EUR 0.00, net EUR 237.50, employer cost EUR 262.50.
4. All three bands. EUR 1,000 gross, primary. Expect: pension EUR 50.00, PIT base EUR 950.00, PIT EUR 66.00 (0 + 16.00 + 50.00), net EUR 884.00, employer cost EUR 1,050.00.
5. Secondary employer flat rate. EUR 800 gross, secondary. Expect: pension EUR 40.00, PIT base EUR 760.00, PIT EUR 76.00 (flat 10%, no 0%/8% band), net EUR 684.00, employer cost EUR 840.00.
6. Benefit in kind. EUR 600 cash gross + EUR 100/month BIK, primary. Expect: taxable BIK EUR 35.00 (100 − 65), pension EUR 30.00, PIT base EUR 605.00, PIT EUR 31.50 (0 + 16.00 + 15.50), net cash EUR 538.50, employer cash cost EUR 630.00.
7. 8%-band ceiling check. Confirm the maximum tax in the 8% band is EUR 16.00 (8% × the EUR 200 band width) for any primary employee whose base reaches EUR 450.
8. Annual = monthly × 12 check. Confirm the annual bands (3,000 / 5,400) equal the monthly bands (250 / 450) × 12, and that each pay run uses the MONTHLY bands.
9. Employer-cost-only check. Confirm the 5% employer pension is added on top of gross, is NEVER deducted from the employee's net pay, and that PIT is NOT an employer cost.
10. Pension split check. Confirm the mandatory pension is exactly 5% employee + 5% employer = 10% of gross, with no voluntary top-up assumed.
11. Filing check. Confirm PIT AND pension contributions are declared together on the monthly WM declaration via the TAK EDI system, due the 15th of the following month, with the annual PIT return due 31 March.
12. Primary/secondary fallback. Status unknown — confirm the skill treats a known second job as secondary (flat 10%) and flags the assumption, rather than defaulting to the progressive bands.

## PROHIBITIONS

- **Prohibitions list** — - NEVER apply the progressive 0%/8%/10% bands at a SECONDARY employer — a secondary employer withholds a flat 10%. - NEVER reintroduce the 4% band — it was removed by Law No. 08/L-142, effective 23 August 2024. - NEVER deduct the 5% employer pension contribution from the employee's net pay — it is an employer cost paid on top of gross. - NEVER treat PIT as an employer cost — PIT is fully employee-borne via withholding. - NEVER apply the ANNUAL bands (3,000 / 5,400) to a single pay run — each pay run uses the MONTHLY bands (250 / 450). - NEVER tax the first EUR 65/month of benefits in kind — only the excess above EUR 65 enters the PIT base. - NEVER assume voluntary supplementary pension — apply the mandatory 5% + 5% only unless an election is confirmed; only the mandatory amount is tax-deductible. - NEVER apply a pension base cap with an invented EUR maximum — the EUR cap figure is an unconfirmed RESEARCH GAP; route high earners to a reviewer. - NEVER run a full-time employee below the statutory minimum wage (EUR 350 in 2025; EUR 425 from 1 Jan 2026). - NEVER apply the EUR 425 or EUR 500 minimum wage to a 2025 pay period — those take effect in 2026. - NEVER miss the monthly WM deadline (15th of the following month) or the annual PIT return deadline (31 March). - NEVER quote a specific late-filing fine amount or pension base cap — those are unconfirmed RESEARCH GAPS pending reviewer confirmation. - NEVER present payroll computations as definitive — always label them as estimated and direct the user to a licensed Kosovo accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax adviser in Kosovo) before implementation.

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
