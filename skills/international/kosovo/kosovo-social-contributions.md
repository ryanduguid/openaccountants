---
name: kosovo-social-contributions
description: Use this skill whenever asked about Kosovo payroll social contributions and wage taxation for employees and employers. Trigger on phrases like "how much pension contribution in Kosovo", "Kosovo payroll tax", "mandatory pension Trusti", "KPST contribution", "5% pension Kosovo", "Kosovo social security", "do I pay health insurance in Kosovo", "Kosovo PIT on salary", "withholding tax wages Kosovo", "WM declaration", "CM pension form", "secondary employer 10%", or any question about Kosovo employment-tax obligations. Also trigger when classifying bank statement transactions that relate to TAK/ATK tax payments, Trusti/KPST pension transfers, or salary debits from Kosovan banks (BKT, ProCredit, Raiffeisen Kosovo, TEB, NLB, Banka Ekonomike). Also trigger when preparing a monthly WM (wage withholding) or CM (pension contribution) declaration, or the annual PD personal income tax return. This skill covers the mandatory 10% pension split (5% employee + 5% employer), the 0%/8%/10% progressive personal income tax, the flat 10% secondary-employer withholding, the enacted-but-dormant health insurance regime, minimum wage, benefit-in-kind thresholds, payment schedule, penalties, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Kosovo payroll or social-contribution work.
version: 0.2
jurisdiction: XK
tax_year: 2025
last_updated: 2026-10-08
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kosovo Social Contributions & Wage Taxation

## Kosovo Social Contributions & Wage Taxation Skill v0.2

> **Tier 2 (research-verified).** Figures are sourced from [Law No. 05/L-028](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) on Personal Income Tax as amended by Law No. 08/L-142 ([TAK notice of 27 August 2024 quoting Law No. 08/L-142 art. 5](https://www.atk-ks.org/en/notice-to-taxpayers-personal-income-tax-rates-are-changed/)), [Law No. 04/L-101](https://www.atk-ks.org/wp-content/uploads/2017/07/Law-No.-04-L-101.pdf) on Pension Funds as amended by Laws No. 04/L-168 and 05/L-116, [TAK Public Explanatory Decision No. 01/2013](https://www.atk-ks.org/wp-content/uploads/2017/08/Vendim-Shpjegues-Publik-NR-01-2013Anglisht.pdf), [Law No. 08/L-257](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) on the Administration of Tax Procedures and the TAK guidance portal. PwC is kept only for the benefit-in-kind threshold, and the health-insurance and minimum-wage rows keep their secondary sources. This skill has NOT yet been signed off by a Kosovo-warranted accountant (`verified_by: pending`). Treat every figure as estimated pending professional review.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**  _(Law No. 05/L-028 arts. 6 and 38; Law No. 04/L-101 art. 6; TAK Decision 01/2013; TAK CRM guidance portal for the form names)_

| Field | Value |
| --- | --- |
| Country | Kosovo (Republic of Kosovo) |
| Jurisdiction code | XK |
| Currency | EUR only |
| Primary social-contribution legislation | Law No. 04/L-101 on Pension Funds of Kosovo (mandatory pension) |
| Wage tax legislation | Law No. 05/L-028 on Personal Income Tax, as amended by Law No. 08/L-142 (Official Gazette, effective 23 Aug 2024) |
| Health insurance legislation | Law No. 04/L-249 on Health Insurance — enacted but NOT operational (no contributions collected as of 2025) |
| Tax authority | Tax Administration of Kosovo (TAK / Administrata Tatimore e Kosovës, ATK) — www.atk-ks.org / crmm.atk-ks.org |
| Pension administrator | Kosovo Pension Savings Trust (Trusti / KPST, www.trusti.org), supervised by Central Bank of Kosovo (BQK) |
| Mandatory pension — employee share | 5% of gross wages (withheld) |
| Mandatory pension — employer share | 5% of gross wages (employer cost) |
| Mandatory pension — total | 10% of gross wages |
| Voluntary additional pension | Up to a further 10% each, for a maximum of 15% employee and 15% employer (30% combined, including the mandatory 10%) |
| Health insurance contribution | 0% — NOT collected (regime dormant) |
| Unemployment / sickness contribution | 0% — none exists |
| Personal income tax on wages | Progressive 0% / 8% / 10% at the primary employer; flat 10% at any secondary employer; base is gross less the employee's pension contribution |
| Minimum wage | EUR 350.00/month gross (eff. 1 Oct 2024); rises to EUR 425.00 (1 Jan 2026) and EUR 500.00 (1 Jul 2026) |
| Tax year | Calendar year |
| Monthly forms | WM (wage withholding), CM (pension) — declare/pay by 15th of following month |
| Quarterly form | CI (individual pension contribution report) — 1st–15th of month after each quarter |
| Annual return | PD / PD24 (personal income tax) — due 31 March of following year |
| Validated by | Pending — requires sign-off by a Kosovo-warranted accountant |
| Validation date | Pending |

**Contribution overview (per EUR of gross wages)**  _(Law No. 04/L-101 art. 6.2; GrECo/Asinta (health insurance not implemented).)_

| Contribution | Employee | Employer | Total | Legal basis |
| --- | --- | --- | --- | --- |
| Mandatory pension (KPST/Trusti) | 5% | 5% | 10% | Law No. 04/L-101 |
| Health insurance | 0% | 0% | 0% | Law No. 04/L-249 (dormant) |
| Unemployment / sickness / other | 0% | 0% | 0% | none |
| **Total mandatory payroll contributions** | **5%** | **5%** | **10%** | — |

> **Arithmetic check:** employee column 5% + 0% + 0% = **5%**; employer column 5% + 0% + 0% = **5%**; total column 10% + 0% + 0% = **10%**, and 5% + 5% = **10%**. Rows reconcile.
> **Source:** Law No. 04/L-101 art. 6.2 (pension); GrECo/Asinta (health insurance not implemented).

**Personal income tax on employment income (primary employer — progressive)**  _(Law No. 05/L-028 art. 6, as replaced by Law No. 08/L-142 art. 5 from 23 Aug 2024; monthly bands from the TAK notice of 27 August 2024. The former schedule was 0%/4%/8%/10%.)_

| Band (annual) | Band (monthly) | Marginal rate | Tax within band | Cumulative tax at top of band |
| --- | --- | --- | --- | --- |
| Up to EUR 3,000.00 | Up to EUR 250.00 | 0% | EUR 0.00 | EUR 0.00 |
| EUR 3,000.01 – 5,400.00 | EUR 250.01 – 450.00 | 8% | 8% × 2,400 = EUR 192.00 | EUR 192.00 |
| EUR 5,400.01 and above | EUR 450.01 and above | 10% | 10% × (income − 5,400) | EUR 192.00 + 10% × excess |

> **Arithmetic check:** band 2 width = 5,400 − 3,000 = 2,400; 8% × 2,400 = **192.00**. Cumulative tax at EUR 5,400 = **192.00**. Band 3 starts from a cumulative base of EUR 192.00. Consistent.
> **Source:** Law No. 05/L-028 art. 6, as replaced by Law No. 08/L-142 art. 5 (TAK notice of 27 August 2024).

**Secondary-employer withholding**  _(Law No. 05/L-028 art. 38(2) and (3))_

| Situation | Treatment | Source |
| --- | --- | --- |
| Single (primary) employer | Progressive 0%/8%/10% bands above | Law No. 05/L-028 art. 38(2) |
| Each secondary employer (employee with >1 employer) | Flat 10% withholding on the wages it pays (no 0% band) | Law No. 05/L-028 art. 38(3): "An employer who is not the employee's principal employer shall withhold an amount equal to ten percent (10%) of the wages" |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether worker is employee or contractor | Treat as employee; apply 10% pension + PIT withholding; flag for reviewer |
| Unknown primary vs secondary employer | STOP — ask. Bands vs flat 10% depend entirely on this |
| Unknown gross vs net wage | Treat figure as GROSS; flag for reviewer |
| Employee pension and the PIT base | Deduct the employee's pension contribution before applying the bands (TAK Decision 01/2013 art. 6) |
| Health/unemployment contribution asked for | State 0% — not collected; cite dormant Law 04/L-249 |
| Minimum-wage figure for a payroll period | Use EUR 350.00 (2025); confirm against the operative Government Decision for the period |
| Pension contribution ceiling | None: compute on the full gross wage (Law No. 04/L-101 art. 6.2) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- gross monthly wage, and whether this is the employee's PRIMARY or SECONDARY employer. Without the primary/secondary flag, STOP — the PIT method changes entirely (progressive bands vs flat 10%).

**Recommended** -- pay period, whether the figure provided is gross or net, employer/employee names, and whether any benefits in kind exceed EUR 65/month.

**Ideal** -- the employer's TAK fiscal number, monthly WM and CM declarations, KPST/Trusti contribution statements, and the prior-year PD return.

### Refusal catalogue

- **R-XK-1 -- Primary/secondary employer unknown** — Cannot compute Kosovo wage tax without knowing whether this is the employee's primary or secondary employer. The primary employer applies progressive 0%/8%/10% bands; each secondary employer withholds a flat 10% with no 0% band. Designating primary vs secondary is a legal obligation of the employee. Please confirm before I proceed. (Trigger: employee may have more than one employer and the designation is unclear.)
- **R-XK-2 -- Health insurance contribution requested** — Kosovo's mandatory health-insurance system (Law No. 04/L-249) is enacted but NOT operational — no employer or employee health contributions are collected as of 2025; public healthcare is funded from general taxation. I will not compute a health contribution. Because this bill has repeatedly returned to the legislative agenda, confirm it has not commenced for the relevant payroll period. (Trigger: client asks to compute a Kosovo health-insurance payroll contribution.)
- **R-XK-4 -- Pension arrears / penalties** — Understatement fines (15% or 25% of the shortfall, Law No. 08/L-257 art. 100), a 25% fine on wage tax or pension contributions not withheld or not paid over (art. 103) and monthly late-payment interest (set above the commercial bank lending rate, accruing up to 10 years, art. 24) apply. Do not attempt to quantify arrears without a TAK statement. Escalate to a Kosovo-warranted accountant. (Trigger: client has undeclared or unpaid prior-period pension contributions or wage tax.)
- **R-XK-5 -- Voluntary / occupational pension structuring** — Voluntary contributions may take each side to 15% of gross (Law No. 04/L-101 art. 6.2(c)), and the employee's share up to 15% reduces the PIT base (TAK Decision 01/2013 art. 6), but supplementary-fund choice and scheme rules are case-specific. Escalate to a Kosovo-warranted accountant. (Trigger: client asks about the optional additional pension or scheme structuring.)

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Kosovo payroll, pension and wage tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Tax and pension remittances EXCLUDE from any VAT/revenue/expense recharacterisation — they are statutory payroll obligations, not business supplies. Kosovo uses EUR. Albanian-language terms appear alongside English on many statements.

### 3.1 Pension contribution remittances (KPST / Trusti)

**Pension contribution remittances table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRUSTI, KPST | EXCLUDE -- pension contribution | Mandatory 10% to Kosovo Pension Savings Trust |
| FONDI I KURSIMEVE PENSIONALE, KURSIMET PENSIONALE | EXCLUDE -- pension contribution | Albanian: "pension savings fund" |
| PENSION, PENSIONI | EXCLUDE -- pension contribution | Generic pension reference (outgoing) |
| KONTRIBUT PENSIONAL, KONTRIBUTI | EXCLUDE -- pension contribution | Albanian: "pension contribution" |
| CM, FORM CM | EXCLUDE -- pension contribution | TAK monthly pension form reference |

### 3.2 Wage tax / TAK remittances

**Wage tax / TAK remittances table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TAK, ATK, ADMINISTRATA TATIMORE | EXCLUDE -- wage withholding tax | Tax Administration of Kosovo |
| WM, FORM WM | EXCLUDE -- wage withholding tax | TAK monthly wage withholding form |
| TATIMI NE PAGA, TATIM PAGA | EXCLUDE -- wage withholding tax | Albanian: "tax on wages" |
| MBAJTJE NE BURIM, WITHHOLDING | EXCLUDE -- withholding tax | Albanian: "withheld at source" |

### 3.3 TAK debits appearing on specific Kosovan banks

**TAK debits by bank table**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| BKT (Banka Kombëtare Tregtare) | "TAK" / "ATK" / "PAGESA TATIMORE" | EXCLUDE -- tax/pension remittance |
| ProCredit Bank Kosovo | "ADMINISTRATA TATIMORE" / "TRUSTI" | EXCLUDE -- tax/pension remittance |
| Raiffeisen Bank Kosovo | "TAK PAYMENT" / "KPST" | EXCLUDE -- tax/pension remittance |
| TEB Sh.A. | "TATIMI NE PAGA" / "KONTRIBUT PENSIONAL" | EXCLUDE -- tax/pension remittance |
| NLB Banka / Banka Ekonomike | "TRUSTI" / "ATK" | EXCLUDE -- tax/pension remittance |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PAGA, PAGAT, ROGA (outgoing) | EXCLUDE -- payroll expense | Wage payment; not a contribution remittance |
| SALARY, NET PAY (outgoing) | EXCLUDE -- payroll expense | Net wage to employee |
| PAGA, SALARY (incoming) | EXCLUDE -- employment income received | Not a contribution payment |

### 3.5 Pension benefits received (NOT contributions)

**Pension benefits received table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSIONI BAZIK, BASIC PENSION (incoming) | EXCLUDE -- pension income received | Budget-funded basic state pension |
| TRUSTI WITHDRAWAL, TERHEQJE (incoming) | EXCLUDE -- pension withdrawal received | Not a contribution paid |

## Section 4 -- Worked examples

Six bank statement classifications and computations for a hypothetical Kosovan employer running monthly payroll (figures in EUR). All PIT figures use the monthly bands (0% up to 250, 8% on 250.01–450, 10% above 450). PIT is computed on gross wages less the employee's 5% pension contribution, the base TAK prescribes (TAK Decision 01/2013 art. 6). Version 0.1 computed PIT on full gross wages.

### Example 1 -- Minimum-wage employee, single employer (BKT)

**Inputs:** Gross monthly wage EUR 350.00 (the 2025 minimum wage); this is the employee's only (primary) employer.

**Computation:**
- Employee pension 5% × 350.00 = **EUR 17.50** (withheld).
- PIT base = 350.00 − 17.50 = 332.50. Monthly PIT: 0% on first 250.00 = 0.00; 8% on (332.50 − 250.00) = 8% × 82.50 = **EUR 6.60**.
- Employer pension 5% × 350.00 = **EUR 17.50** (employer cost on top of wage).
- Net pay = 350.00 − 6.60 (PIT) − 17.50 (employee pension) = **EUR 325.90**.
- Total employer outlay = 350.00 + 17.50 = **EUR 367.50**.

**Bank lines:**
`05.02.2025 ; PAGA SHKURT - ARDIAN K. ; DEBIT ; NET PAY ; -325.90 ; EUR` → EXCLUDE (payroll, 3.4)
`14.02.2025 ; ATK - WM ; DEBIT ; TATIMI NE PAGA 01/2025 ; -6.60 ; EUR` → EXCLUDE (wage tax, 3.2)
`14.02.2025 ; TRUSTI - CM ; DEBIT ; KONTRIBUT PENSIONAL 01/2025 ; -35.00 ; EUR` → EXCLUDE (pension, 3.1). EUR 35.00 = 17.50 employee + 17.50 employer.

**Source:** Law No. 05/L-028 arts. 6 and 38(2); Law No. 04/L-101 art. 6.2; TAK Decision 01/2013 art. 6; EY (minimum wage EUR 350 eff. 1 Oct 2024).

### Example 2 -- Mid-range employee, single employer (ProCredit)

**Inputs:** Gross monthly wage EUR 600.00; primary (only) employer.

**Computation:**
- Employee pension 5% × 600.00 = **EUR 30.00**.
- PIT base = 600.00 − 30.00 = 570.00. Monthly PIT: 0% on 250.00 = 0.00; 8% on (450.00 − 250.00) = 8% × 200.00 = 16.00; 10% on (570.00 − 450.00) = 10% × 120.00 = 12.00. Total PIT = 16.00 + 12.00 = **EUR 28.00**.
- Employer pension 5% × 600.00 = **EUR 30.00**.
- Net pay = 600.00 − 28.00 − 30.00 = **EUR 542.00**.

> **Annual cross-check:** PIT base EUR 570 × 12 = 6,840. Annual PIT: 0 + 192.00 (band 2) + 10% × (6,840 − 5,400) = 192.00 + 144.00 = 336.00; ÷ 12 = **EUR 28.00/month**. Reconciles.

**Source:** Law No. 05/L-028 art. 6; Law No. 04/L-101 art. 6.2; TAK Decision 01/2013 art. 6.

### Example 3 -- Higher earner, single employer (Raiffeisen)

**Inputs:** Gross monthly wage EUR 1,000.00; primary (only) employer.

**Computation:**
- Employee pension 5% × 1,000.00 = **EUR 50.00**.
- PIT base = 1,000.00 − 50.00 = 950.00. Monthly PIT: 0% on 250.00 = 0.00; 8% × (450.00 − 250.00) = 16.00; 10% × (950.00 − 450.00) = 10% × 500.00 = 50.00. Total PIT = 16.00 + 50.00 = **EUR 66.00**.
- Employer pension 5% × 1,000.00 = **EUR 50.00**.
- Net pay = 1,000.00 − 66.00 − 50.00 = **EUR 884.00**.
- Total employer outlay = 1,000.00 + 50.00 = **EUR 1,050.00**.

> **Annual cross-check:** PIT base EUR 950 × 12 = 11,400. Annual PIT: 0 + 192.00 + 10% × (11,400 − 5,400) = 192.00 + 600.00 = 792.00; ÷ 12 = **EUR 66.00**. Reconciles.

**Source:** Law No. 05/L-028 art. 6; Law No. 04/L-101 art. 6.2; TAK Decision 01/2013 art. 6.

### Example 4 -- Employee with a SECONDARY employer (flat 10%)

**Inputs:** Employee already has a primary employer elsewhere. This (secondary) employer pays EUR 400.00/month for part-time work.

**Computation (secondary employer):**
- Employee pension 5% × 400.00 = **EUR 20.00**.
- PIT: flat 10% on the wage after the employee pension, 10% × 380.00 (no 0% band at a secondary employer) = **EUR 38.00**.
- Employer pension 5% × 400.00 = **EUR 20.00**.
- Net from this employer = 400.00 − 38.00 − 20.00 = **EUR 342.00**.

> **Contrast:** had this been the primary employer, PIT would be 8% × (380.00 − 250.00) = **EUR 10.40**, not 38.00. The primary/secondary flag changes the tax by EUR 27.60/month here — hence R-XK-1.

**Source:** Law No. 05/L-028 art. 38(3). *[Art. 38(3) says "ten percent (10%) of the wages"; applying it after the employee pension follows TAK Decision 01/2013 art. 6 and matches kosovo-payroll T2-4. Reviewer to confirm.]*

### Example 5 -- Benefit in kind above the EUR 65 threshold

**Inputs:** Gross cash wage EUR 600.00 plus a EUR 100.00/month gym membership benefit (not business travel, not work-accident indemnity, not transport reimbursement); primary employer.

**Computation:**
- Benefit in kind exceeds EUR 65/month, so the full EUR 100.00 is treated as taxable employment income (conservative; kosovo-payroll adds only the EUR 35 excess, and art. 9(1.8), which taxes benefits "that exceed the minimum amount determined in a sub-legal act", does not settle which reading applies). PIT base = 600.00 − 30.00 (employee pension) + 100.00 = **EUR 670.00**.
- Monthly PIT on 670.00: 0% on 250.00 = 0.00; 8% × 200.00 = 16.00; 10% × (670.00 − 450.00) = 10% × 220.00 = 22.00. Total PIT = **EUR 38.00**.
- Pension contributions are computed on gross wages — *[RESEARCH GAP: whether the taxable BIK enters the pension base is not confirmed; reviewer to verify. Conservatively computed on cash wage EUR 600.]* Employee pension 5% × 600.00 = **EUR 30.00**; employer pension 5% × 600.00 = **EUR 30.00**.

**Source:** Law No. 05/L-028 art. 9(1.8) and (2) (benefits in kind; business travel, work-accident indemnity and transport exclusions); EUR 65 threshold from PwC, Income determination, because the sub-legal act that sets it was not read. *[RESEARCH GAP]*

### Example 6 -- Ambiguous TAK debit (understatement / interest)

**Input line:**
`20.06.2025 ; ADMINISTRATA TATIMORE E KOSOVES ; DEBIT ; RREGULLIM/INTERES ; -640.00 ; EUR`

**Reasoning:** Matches "ADMINISTRATA TATIMORE" (3.2/3.3) but the reference "RREGULLIM/INTERES" (adjustment/interest) and the irregular amount suggest an understatement fine (15% or 25% of the shortfall) and/or late-payment interest, not a routine WM remittance. Cannot split principal from penalty/interest without a TAK statement.

**Classification:** EXCLUDE from VAT. Flag for reviewer — request the TAK statement to separate principal wage tax (a payroll cost) from penalty/interest (non-deductible). Escalate per R-XK-4.

**Source:** Law No. 08/L-257 arts. 24 (interest) and 100 (understatement fines).

## Section 5 -- Tier 1 rules

These rules apply when bank statement data is clear and all required inputs are available. Apply exactly as written. Citations in parentheses.

### Rule 1 -- Mandatory pension formula

- **Mandatory pension formula** — Employee pension = 5% × gross_wages   (withheld) Employer pension = 5% × gross_wages   (employer cost) Total pension    = 10% × gross_wages  → remitted to KPST/Trusti  _(Law No. 04/L-101 art. 6.2 and 6.3; TAK Decision 01/2013 art. 4.)_

### Rule 2 -- No health, unemployment, or sickness payroll contribution

- **No health/unemployment/sickness contribution** — Health insurance (Law 04/L-249) is enacted but dormant — 0% collected. There is no separate unemployment, sickness, or general social-insurance payroll contribution. The basic state pension is budget-funded.  _(Law No. 04/L-101 arts. 2 and 3; GrECo/Asinta for the health-insurance status.)_

### Rule 3 -- PIT at the primary employer is progressive

- **PIT progressive bands formula** — 0%  on annual income up to EUR 3,000      (monthly up to EUR 250) 8%  on EUR 3,000.01 – 5,400               (monthly EUR 250.01 – 450) 10% on EUR 5,400.01 and above             (monthly EUR 450.01+), applied to gross wages less the employee's pension contribution  _(Law No. 05/L-028 art. 6, as replaced by Law No. 08/L-142 art. 5; TAK notice of 27 August 2024; TAK Decision 01/2013 art. 6.)_

### Rule 4 -- Current PIT schedule effective 23 August 2024

- **Current PIT schedule effective date** — The 0%/8%/10% structure was introduced by Law No. 08/L-142 (Official Gazette, effective 23 Aug 2024), replacing the former four-band 0%/4%/8%/10% schedule. The law entered into force on publication, 23 August 2024; for payroll periods before that date, the old schedule applied.  _(TAK notice of 27 August 2024.)_

### Rule 5 -- Secondary employer withholds flat 10%

- **Secondary employer flat 10%** — Where an employee has more than one employer, the primary employer applies the progressive bands and EACH secondary employer withholds a flat 10% on the wages it pays (no 0% band). The employee designates the principal employer in the way a ministerial sub-legal act sets.  _(Law No. 05/L-028 arts. 2(1.7) and 38(2) and (3).)_

### Rule 6 -- Employer withholds and remits

- **Employer withholds and remits** — The employer withholds PIT and the 5% employee pension contribution at the time of wage payment and remits both, together with the 5% employer pension share, to TAK by the 15th day of the following month.  _(Law No. 05/L-028 art. 38(1) and (5); Law No. 04/L-101 art. 6.3.)_

### Rule 7 -- Benefits in kind over EUR 65/month are taxable

- **Benefit in kind threshold** — EUR 65/month EUR (Benefits in kind exceeding this monthly amount are taxable employment income. Reimbursement of business travel, work-accident indemnity, and transport-cost reimbursement are excluded.)  _(Law No. 05/L-028 art. 9(1.8) and (2); EUR 65 figure from PwC, Income determination. *[RESEARCH GAP — confirm in the current sub-legal act.]*)_

### Rule 8 -- Voluntary additional pension

- **Voluntary additional pension** — Optional additional pension contributions are permitted: up to a further 10% by the employee and 10% by the employer, for a maximum of 15% each and 30% combined including the mandatory 10%. The employee's share up to 15% of gross reduces the PIT base.  _(Law No. 04/L-101 art. 6.2(c); TAK Decision 01/2013 arts. 5 and 6.)_

### Rule 9 -- Filing and payment schedule

**Filing and payment schedule table**  _(TAK CRM guidance portal for form names; Law No. 05/L-028 arts. 38(5) and 48(1) for the WM and PD dates.)_

| Form | Purpose | Deadline |
| --- | --- | --- |
| WM | Wage withholding tax declaration (monthly) | 1st–15th of following month; pay by the 15th |
| CM | Pension contribution declaration & payment (monthly) | 1st–15th of following month |
| CI | Quarterly individual pension contribution report | 1st–15th of month after each quarter |
| PD / PD24 | Annual personal income tax return | 31 March of the following year |

### Rule 10 -- Residence basis

- **Residence basis** — Residents are taxed on worldwide income; non-residents only on Kosovo-source income. A natural person is resident with a principal residence in Kosovo or 183 days' presence in any twelve-month period.  _(Law No. 05/L-028 arts. 2(1.18) and 4.)_

### Rule 11 -- New-employee reporting

- **New-employee reporting** — The employer must notify TAK of a new employment contract one day before that employee begins work; the fine is EUR 500 for each undeclared worker.  _([Law No. 08/L-257](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) arts. 43(5) and 102(3).)_

### Rule 12 -- No pension ceiling

- **No pension ceiling** — Art. 6.2 levies 5% + 5% on total wages without an upper limit. Law No. 04/L-168 amended only art. 6.12 (self-employed) and Law No. 05/L-116 did not amend art. 6. Compute on the full gross wage. A full-time wage below the minimum wage takes the minimum wage as the employer's base.  _(Law No. 04/L-101 art. 6.2 and 6.6; TAK Decision 01/2013 art. 7.)_

## Section 6 -- Tier 2 catalogue

When bank statement data is ambiguous or client circumstances are unclear, flag these for reviewer confirmation.

### T2-1 -- Employee pension and the PIT base (resolved)

**Trigger:** computing PIT where the employee 5% pension is withheld.

**Resolution:** TAK sets the base as "gross salary after deduction of Pension Contribution (employee's share)", deductible up to 15% of gross (TAK Decision 01/2013 art. 6), and employee contributions to KPST are not subject to PIT (Law No. 04/L-101 art. 37.2, as replaced by Law No. 05/L-116 art. 10). Version 0.1 computed PIT on full gross wages.

**Action:** None beyond confirming the employee's voluntary share, if any.

### T2-2 -- High earner / pension ceiling (resolved)

**Trigger:** gross wage high enough that a 10% pension is material.

**Resolution:** No ceiling exists (Rule 12). Compute on the full gross wage.

**Action:** None.

### T2-3 -- Primary vs secondary employer designation

**Trigger:** employee may have more than one employer; designation unclear or changed mid-period.

**Issue:** The progressive bands apply only at the primary employer; secondary employers withhold flat 10%. A wrong designation materially mis-states tax (see Example 4).

**Action:** STOP and confirm (R-XK-1). Flag any mid-period change of designation for reviewer.

### T2-4 -- Health-insurance regime status

**Trigger:** a new payroll period, or any client expectation that health contributions are due.

**Issue:** Law 04/L-249 is dormant but has repeatedly returned to the legislative agenda; it could commence.

**Action:** Confirm no mandatory health contribution has commenced for the relevant period before finalising. Flag for reviewer each new tax year.

### T2-5 -- Minimum wage in transition

**Trigger:** payroll period spanning a minimum-wage change date.

**Issue:** Minimum wage is EUR 350.00 in 2025, scheduled to rise to EUR 425.00 (1 Jan 2026) and EUR 500.00 (1 Jul 2026) per ministry/press reporting.

**Action:** Confirm the operative figure against the official Government Decision / Official Gazette for the period. Flag for reviewer.

### T2-6 -- Contractor vs employee classification

**Trigger:** payment to an individual that could be either employment or independent services.

**Issue:** Employment triggers 10% pension + wage withholding; independent services may fall under different rules. Mis-classification mis-states both contributions and tax.

**Action:** Flag for reviewer. Do not assume contractor status to avoid contributions.

### T2-7 -- Benefit-in-kind valuation

**Trigger:** non-cash benefits near or above the EUR 65/month threshold, or whether a BIK enters the pension base.

**Issue:** Valuation of BIKs and whether the taxable BIK is included in the pension base are not fully confirmed in the consulted sources.

**Action:** Flag for reviewer. *[RESEARCH GAP — pension base treatment of BIK.]*

## Section 7 -- Excel working paper template

When producing a Kosovo payroll/contribution computation, structure the working paper as follows:

```
KOSOVO PAYROLL & SOCIAL-CONTRIBUTION COMPUTATION -- WORKING PAPER
Employer: [name]            TAK fiscal no: [____]
Employee: [name]            Pay period:    [month/year]
Prepared: [date]

INPUT DATA
  Gross monthly wage (EUR):           [____]
  Figure is gross / net:              [GROSS / NET]
  Primary or secondary employer:      [PRIMARY / SECONDARY]   <- mandatory
  Benefits in kind > EUR 65/month:    [YES/NO]  amount: [____]
  Voluntary pension elected:          [YES/NO]  rates: [emp __% / empr __%]

PERSONAL INCOME TAX (monthly bands: 0% to 250 | 8% to 450 | 10% above)
  Taxable wage base (gross - employee pension + taxable BIK):  EUR [____]
  IF PRIMARY:
    0% on first 250.00:                     EUR 0.00
    8% on (min(base,450) - 250):            EUR [____]
    10% on (base - 450, if > 450):          EUR [____]
    PIT total:                              EUR [____]
  IF SECONDARY:
    10% x base (flat, no 0% band):          EUR [____]

MANDATORY PENSION (KPST / Trusti)
  Employee 5% x gross:                      EUR [____]
  Employer 5% x gross:                      EUR [____]
  Total 10% x gross:                        EUR [____]
  [No ceiling — Law No. 04/L-101 art. 6.2]

VOLUNTARY PENSION (optional, up to 15% / 15% in total)
  Employee voluntary:                       EUR [____]
  Employer voluntary:                       EUR [____]

NET PAY
  Net = gross - PIT - employee pension(s):  EUR [____]
  Total employer outlay = gross + employer pension(s): EUR [____]

FILING
  WM (wage tax) due:        15th of following month
  CM (pension) due:         15th of following month
  CI (quarterly):           1st-15th after quarter
  PD/PD24 (annual):         31 March following year

REVIEWER FLAGS
  [List any Tier 2 flags / RESEARCH GAP items here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their tax impact]
```

## Section 8 -- Bank statement reading guide

### How Kosovo payroll, tax and pension items appear on bank statements

**Currency:** EUR (Kosovo uses the euro unilaterally). Statements are commonly bilingual (Albanian / English); Serbian appears in some northern municipalities.

**Pension remittances (KPST / Trusti):**
- Descriptions: "TRUSTI", "KPST", "FONDI I KURSIMEVE PENSIONALE", "KONTRIBUT PENSIONAL", "CM".
- Timing: monthly, by the 15th of the following month.
- Amount: 10% of gross payroll (5% employee + 5% employer); always outgoing (DEBIT).

**Wage withholding tax (TAK / ATK):**
- Descriptions: "TAK", "ATK", "ADMINISTRATA TATIMORE", "TATIMI NE PAGA", "MBAJTJE NE BURIM", "WM".
- Timing: monthly, by the 15th of the following month.
- Amount: per the progressive bands (primary) or flat 10% (secondary).

**Salary (PAGA):**
- "PAGA", "PAGAT", "ROGA", "NET PAY" — outgoing net wages to employees. Not a contribution.

**Key identification tips:**
1. Pension and wage-tax remittances are always outgoing (DEBIT), recur monthly, and cluster around the 15th.
2. A pension remittance equal to exactly 10% of total gross payroll for the month is the mandatory KPST contribution.
3. Do NOT confuse "TATIMI NE PAGA" (wage tax → TAK) with "KONTRIBUT PENSIONAL" (pension → Trusti) — they are separate forms (WM vs CM).
4. Incoming "PENSIONI BAZIK" / "BASIC PENSION" or "TRUSTI" withdrawals are benefits received, not contributions.
5. Irregular TAK debits referencing "INTERES" or "RREGULLIM" may be interest/penalties — flag for reviewer.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for remittances** -- identify outgoing payments matching Section 3 (Trusti/KPST pension; TAK/ATK wage tax; PAGA salary).
2. **Reconstruct gross payroll** -- a pension remittance is 10% of gross payroll, so estimated monthly gross payroll ≈ pension remittance ÷ 0.10.
3. **Cross-check wage tax** -- the WM remittance should be consistent with the progressive bands on that gross (primary) or flat 10% (secondary).
4. **Flag the unknowns** -- "Computation derived from bank statement amounts only. Primary/secondary employer status, gross-vs-net basis and benefits in kind have NOT been independently verified. Health-insurance regime assumed dormant. Reviewer must confirm before filing WM/CM/PD."

### Quick computation table (single primary employer, 2025 bands, PIT on gross less employee pension)

**Quick computation table (single primary employer, 2025 bands, PIT on gross less employee pension)**  _(Law No. 05/L-028 art. 6; Law No. 04/L-101 art. 6.2; TAK Decision 01/2013 art. 6.)_

| Gross/month | Monthly PIT | Employee pension 5% | Employer pension 5% | Net pay |
| --- | --- | --- | --- | --- |
| EUR 250.00 | EUR 0.00 | EUR 12.50 | EUR 12.50 | EUR 237.50 |
| EUR 350.00 (min wage) | EUR 6.60 | EUR 17.50 | EUR 17.50 | EUR 325.90 |
| EUR 450.00 | EUR 14.20 | EUR 22.50 | EUR 22.50 | EUR 413.30 |
| EUR 600.00 | EUR 28.00 | EUR 30.00 | EUR 30.00 | EUR 542.00 |
| EUR 1,000.00 | EUR 66.00 | EUR 50.00 | EUR 50.00 | EUR 884.00 |

> **Arithmetic checks (PIT base = gross − employee pension; net = gross − PIT − employee pension):**
> - 250: base 237.50; PIT 0; net = 250 − 0 − 12.50 = 237.50 ✓
> - 350: base 332.50; PIT = 8% × 82.50 = 6.60; net = 350 − 6.60 − 17.50 = 325.90 ✓
> - 450: base 427.50; PIT = 8% × 177.50 = 14.20; net = 450 − 14.20 − 22.50 = 413.30 ✓
> - 600: base 570.00; PIT = 16.00 + 10% × 120 = 28.00; net = 600 − 28.00 − 30.00 = 542.00 ✓
> - 1,000: base 950.00; PIT = 16.00 + 10% × 500 = 66.00; net = 1,000 − 66.00 − 50.00 = 884.00 ✓
>
> **Source:** Law No. 05/L-028 art. 6; Law No. 04/L-101 art. 6.2; TAK Decision 01/2013 art. 6.

### Thresholds and key figures

**Thresholds and key figures**  _(Sources per row.)_

| Item | Value | Source |
| --- | --- | --- |
| PIT zero-rate threshold | EUR 3,000/year (EUR 250/month) | Law No. 05/L-028 art. 6, as replaced by Law No. 08/L-142 art. 5; TAK notice of 27 August 2024 |
| 8% band | EUR 3,000.01 – 5,400/year | Same |
| 10% band | EUR 5,400.01+/year | Same |
| Mandatory pension | 10% (5% employee + 5% employer) | Law No. 04/L-101 art. 6.2 |
| Voluntary pension | up to 15% employee / 15% employer in total | Law No. 04/L-101 art. 6.2(c); TAK Decision 01/2013 art. 5 |
| Health insurance | 0% (Law 04/L-249 dormant) | GrECo/Asinta |
| Taxable BIK threshold | EUR 65/month | PwC, Income determination (the law leaves it to a sub-legal act, art. 9(1.8)) *[RESEARCH GAP]* |
| Minimum wage (2025) | EUR 350.00/month gross | EY newsroom (eff. 1 Oct 2024) |
| Minimum wage (from 1 Jan 2026) | EUR 425.00/month | EY newsroom |
| Minimum wage (from 1 Jul 2026) | EUR 500.00/month | EY newsroom |
| Small business CIT exemption | gross income up to EUR 30,000 (quarterly 3% trade / 9% services of gross income, min EUR 37.50, and 10% of net rental income) | [Law No. 06/L-105](https://www.atk-ks.org/wp-content/uploads/2019/09/LAW_NO.06_L-105.pdf) art. 38(2.1) |
| Standard CIT rate | 10% | Law No. 06/L-105 art. 7 |
| Pension contribution ceiling | None | Law No. 04/L-101 art. 6.2 |

### Penalties

**Penalties**  _(Law No. 08/L-257 on the Administration of Tax Procedures)_

| Penalty | Amount | Source |
| --- | --- | --- |
| Understatement of tax | 15% of the shortfall where it is 10% or less of the correct tax; 25% where it is more | Law No. 08/L-257 art. 100(1) |
| Wage tax or pension contributions not withheld or not paid over | 25% of the amount not paid over | Law No. 08/L-257 art. 103 |
| Failure to file a declaration that results in a liability | EUR 50 (business natural person), EUR 150 (legal entity), EUR 20 (non-business natural person) per declaration | Law No. 08/L-257 art. 99 |
| Late-payment interest | Monthly interest, set at least annually above the commercial bank lending rate; accrues up to 10 years from due date | Law No. 08/L-257 art. 24 |

### Albanian-language glossary

**Albanian-language glossary**

| Albanian | English |
| --- | --- |
| Paga / Pagat | Wage / wages |
| Tatimi në paga | Tax on wages |
| Mbajtje në burim | Withholding at source |
| Kontribut pensional | Pension contribution |
| Fondi i Kursimeve Pensionale | Pension Savings Fund (Trusti/KPST) |
| Administrata Tatimore e Kosovës (ATK) | Tax Administration of Kosovo (TAK) |
| Pensioni bazik | Basic (state) pension |
| Rregullim / Interes | Adjustment / interest |

### Test suite

**Test 1:** Single (primary) employer, gross EUR 250.00/month. → PIT EUR 0.00; employee pension EUR 12.50; employer pension EUR 12.50; net EUR 237.50.

**Test 2:** Single employer, gross EUR 350.00 (min wage). → PIT base EUR 332.50; PIT 8% × 82.50 = EUR 6.60; employee pension EUR 17.50; net EUR 325.90; employer outlay EUR 367.50.

**Test 3:** Single employer, gross EUR 600.00. → PIT base EUR 570.00; PIT EUR 28.00 (16.00 + 12.00); employee pension EUR 30.00; employer pension EUR 30.00; net EUR 542.00.

**Test 4:** Single employer, gross EUR 1,000.00. → PIT base EUR 950.00; PIT EUR 66.00 (16.00 + 50.00); employee pension EUR 50.00; net EUR 884.00; employer outlay EUR 1,050.00.

**Test 5:** SECONDARY employer, gross EUR 400.00. → PIT flat 10% × 380.00 = EUR 38.00; employee pension EUR 20.00; net EUR 342.00. (Had it been primary: PIT 8% × 130 = EUR 10.40.)

**Test 6:** Gross EUR 600.00 + taxable BIK EUR 100.00 (over EUR 65), primary. → PIT base EUR 670.00 (600 − 30 + 100); PIT = 16.00 + 10% × 220 = EUR 38.00. Pension on cash wage EUR 600 = EUR 30.00 each side *[BIK-in-base RESEARCH GAP]*.

**Test 7:** Client asks for the Kosovo health-insurance contribution. → EUR 0.00; Law 04/L-249 dormant; no contribution collected (R-XK-2).

**Test 8:** Annual cross-check, gross EUR 1,000/month, PIT base EUR 950/month = EUR 11,400/year. → Annual PIT = 0 + 192.00 + 10% × (11,400 − 5,400) = EUR 792.00; ÷ 12 = EUR 66.00/month (matches Test 4).

### Prohibitions

- **Confirm employer status before computing wage tax** — NEVER compute Kosovo wage tax without confirming PRIMARY vs SECONDARY employer — bands vs flat 10% depend on it.
- **No health-insurance contribution** — NEVER add a health-insurance contribution — Law 04/L-249 is dormant; 0% is collected.
- **No invented social-insurance contributions** — NEVER invent an unemployment, sickness, or general social-insurance payroll contribution — none exists beyond pension.
- **No pension ceiling** — NEVER cap the 5% + 5% pension at a wage ceiling — Law No. 04/L-101 art. 6.2 sets none.
- **Deduct the employee pension before PIT** — NEVER compute wage PIT on full gross — TAK computes it on gross less the employee's pension share.
- **Do not apply old PIT schedule after 23 Aug 2024** — NEVER apply the old 0%/4%/8%/10% schedule to periods on/after 23 Aug 2024 — the current schedule is 0%/8%/10%.
- **Escalate arrears/penalties without TAK statement** — NEVER quantify pension/wage-tax arrears or penalties without a TAK statement — escalate (R-XK-4).
- **Do not confuse wage tax and pension contribution** — NEVER confuse "TATIMI NE PAGA" (wage tax → TAK, form WM) with "KONTRIBUT PENSIONAL" (pension → Trusti, form CM).
- **Do not treat Trusti withdrawals as contributions paid** — NEVER treat incoming "PENSIONI BAZIK" / Trusti withdrawals as contributions paid.
- **Label outputs as estimated (Tier 2)** — NEVER present figures as definitive — this skill is Tier 2 (`verified_by: pending`); label outputs as estimated and direct the client to TAK/KPST statements.
- **Surface research gaps to reviewer** — NEVER silently resolve a `[RESEARCH GAP]` item — surface it to the reviewer.

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
