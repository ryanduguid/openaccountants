---
name: pg-income-tax
description: Use this skill whenever asked about Papua New Guinea (PNG) personal income tax for employees and self-employed individuals. Trigger on phrases like "how much tax do I pay in PNG", "salary or wages tax", "SWT", "PAYE Papua New Guinea", "Kina income tax", "provisional tax", "annual income tax return", "IRC return", "fortnightly tax", "superannuation contribution", "Nambawan Super", "Nasfund", "GST registration", "self-employed tax PNG", or any question about filing or computing income tax for an employee or sole trader in Papua New Guinea. Also trigger when computing fortnightly salary/wages tax, provisional tax instalments, or superannuation, and when reading a PNG bank statement to classify business income and expenses. This skill covers resident and non-resident rate brackets, SWT/PAYE mechanics, provisional tax, superannuation, GST interaction, filing deadlines, penalties, and the new Income Tax Act 2025 regime effective 1 January 2026. ALWAYS read this skill before touching any PNG income tax work.
jurisdiction: PG
category: international
tax_year: 2025
last_updated: 2026-10-11
version: 0.2
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# papua-new-guinea-income-tax

## Papua New Guinean Income Tax -- Employee & Self-Employed Skill v0.2

## REGIME-CHANGE WARNING -- two regimes in play

REGIME-CHANGE WARNING -- two regimes in play.
- The 2025 tax year is governed by the Income Tax Act 1959 (as amended), with rates set by the Income Tax, Dividend (Withholding) Tax and Interest (Withholding) Tax Rates Act 1984 and, for salary or wages tax, the Income Tax (Salary or Wages Tax) (Rates) Act 1979, each as amended by the 2024 Budget Acts of 2023 and the 2025 Budget Acts of 2024 (Nos. 17 and 18 of 2024).
- The Income Tax Act 2025 commenced on 1 January 2026 and applies to tax years starting on or after that date (s 165); it repeals the 1959 Act and the Rates Acts for those years (s 163), while the repealed law continues to govern 2025 and earlier years (s 164). It introduces a narrow 15% CGT, a 30% assessment regime for non-residents with a PNG permanent establishment, and new benefit valuation rules. Schedule 1 of the Act keeps the resident brackets below unchanged for 2026, restores the 22% band on a non-resident's first K20,000 that the 2025 Budget had removed, and keeps a dependant tax credit (s 56).
- The bracket figures in this skill are taken from the Acts as certified: the 2024 Budget Act (No. 25 of 2023) for residents from 1 January 2024, Table 2A of Act No. 18 of 2024 for non-residents in 2025, and Schedule 1 of the Income Tax Act 2025 for 2026. The IRC's salary and wages tax page still shows the 2024 non-resident table.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Papua New Guinea (Independent State of Papua New Guinea) |
| Tax | Personal Income Tax / Salary or Wages Tax (SWT) |
| Currency | Papua New Guinea Kina (PGK / K) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation (2025) | Income Tax Act 1959 (as amended); Income Tax (Salary or Wages Tax)(Rates)(2025 Budget) Act 2024 |
| New legislation (from 2026) | Income Tax Act 2025 (in force 1 January 2026) |
| Tax authority | Internal Revenue Commission (IRC) — irc.gov.pg |
| Tax-free threshold (residents) | PGK 20,000 (permanent from 1 Jan 2024) — Income Tax (Salary or Wages Tax) (Rates) (2024 Budget) (Amendment) Act 2023, Part 7 Table 1; IRC Salary and Wages Tax page; Income Tax Act 2025 Sch 1 Part I cl (1) |
| Top marginal rate | 42% on income over PGK 250,000 — same Acts |
| Non-resident first band | 2025: 30% from the first kina (Act No. 18 of 2024, Table 2A); 2026: 22% on the first PGK 20,000 (Income Tax Act 2025 Sch 1 Part I cl (2)) |
| SWT remittance | Withheld fortnightly; remitted monthly to IRC by the 7th of the following month — IRC Key Tax Dates; IRC Salary and Wages Tax page |
| Annual return deadline (2024 returns, lodged in 2025) | 28 February 2025, or a later date under the tax agent lodgement extension program — National Gazette G7 of 7 January 2025 (Income Tax Act 1959 s 223); the notice for 2025 returns is gazetted each January |
| Annual return deadline (2026 and later tax years) | Individuals: within 3 months after year end (31 March); companies 6 months, or 9 months with a registered tax agent — Income Tax Act 2025 s 135 |
| Validated by | Pending — requires sign-off by a PNG-registered tax agent / CPA PNG |
| Validation date | Pending |
| Skill version | 0.2 |

### Resident Tax Rate Brackets (2024 onward; applies to 2025)

- **Threshold elimination rule** — Tax-free threshold: PGK 20,000. The former 22% first band was eliminated for residents when the threshold rose to PGK 20,000 (temporarily from 1 January 2023, permanently from 1 January 2024). Do not use older tables showing a 22% resident first bracket. The Income Tax Act 2025 keeps the same five resident bands for 2026 and sets the fortnightly equivalents at K770, K1,270, K2,693 and K9,615.  _(Income Tax (Salary or Wages Tax) (Rates) (2024 Budget) (Amendment) Act 2023 (No. 25 of 2023), Schedule 1 Part 7 Table 1, PacLII — https://www.paclii.org/pg/legis/num_act/itowt2024ba2023500/ ; Internal Revenue Commission, Public Notice: 2024 Budget - Employee Tax-Free Threshold and Dependant Rebate, 19 January 2024, linked from https://irc.gov.pg/pages/know-your-taxes/salary-wages-tax ; Income Tax Act 2025, Schedule 1 Part I cl (1) and (3), IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

**Resident Tax Rate Brackets (2024 onward; applies to 2025 and 2026)**  _(Income Tax (Salary or Wages Tax) (Rates) (2024 Budget) (Amendment) Act 2023, Part 7 Table 1; Internal Revenue Commission, Salary and Wages Tax (rates from 1 January 2024) — https://irc.gov.pg/pages/know-your-taxes/salary-wages-tax ; Income Tax Act 2025, Schedule 1 Part I cl (1))_

| Taxable income (PGK) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 -- 20,000 | 0% (nil) | K 0 |
| 20,001 -- 33,000 | 30% | K 3,900 |
| 33,001 -- 70,000 | 35% | K 16,850 |
| 70,001 -- 250,000 | 40% | K 88,850 |
| Over 250,000 | 42% | -- |

### Non-Resident Tax Rate Brackets

- **Non-resident threshold rule** — Non-residents do not receive the tax-free threshold. For the 2025 tax year the first kina is taxed at 30%: the 2025 Budget Acts replaced the 22% band on the first K20,000 with a single 30% band to K33,000 for both salary or wages tax (Table 2A) and income tax on other income (Schedule 1A Table 5), both for the period from 1 January 2025. For the 2026 tax year the Income Tax Act 2025 restores the 22% band on the first K20,000.  _(Income Tax (Salary or Wages Tax) (Rates) (2025 Budget) (Amendment) Act 2024 (No. 18 of 2024), s 2 and Table 2A, IRC copy — https://static.irc.gov.pg/2025/January/9RMCiB-media-incometax-salaryorwagestaxratesact2024.pdf ; Income Tax, Dividend (Withholding) Tax and Interest (Withholding) Tax Rates (2025 Budget) (Amendment) Act 2024 (No. 17 of 2024), s 1 and Table 5, PacLII — https://www.paclii.org/pg/legis/num_act/itdtaitr2025ba2024808/ ; Income Tax Act 2025, Schedule 1 Part I cl (2) and (4), IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

**Non-Resident Tax Rate Brackets (2025 tax year)**  _(Act No. 18 of 2024, Table 2A; Act No. 17 of 2024, Schedule 1A Table 5)_

| Taxable income (PGK) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 -- 33,000 | 30% | K 9,900 |
| 33,001 -- 70,000 | 35% | K 22,850 |
| 70,001 -- 250,000 | 40% | K 94,850 |
| Over 250,000 | 42% | -- |

**Non-Resident Tax Rate Brackets (2026 tax year onwards)**  _(Income Tax Act 2025, Schedule 1 Part I cl (2); the fortnightly table in cl (4) applies 22% to the first K770)_

| Taxable income (PGK) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 -- 20,000 | 22% | K 4,400 |
| 20,001 -- 33,000 | 30% | K 8,300 |
| 33,001 -- 70,000 | 35% | K 21,250 |
| 70,001 -- 250,000 | 40% | K 93,250 |
| Over 250,000 | 42% | -- |

### Superannuation (Compulsory) — Contribution Rates

**Superannuation (Compulsory) — Contribution Rates**  _(Superannuation (General Provisions) Act 2000, ss 3, 76 and 77 (rates prescribed by regulation), PacLII — https://www.paclii.org/pg/legis/num_act/spa2000396/ ; Bank of Papua New Guinea, Public Notice: Employer and Employee Superannuation Contributions, 21 February 2025 — https://bankpng.gov.pg/sites/default/files/2025-02/20250221%20-%20Public%20Notice%20to%20Employer%20and%20Employee%20Superannuation%20Contribution.pdf)_

| Party | Rate | Base |
| --- | --- | --- |
| Employee | 6.0% | Gross basic salary (after-tax) |
| Employer | 8.4% | Gross basic salary (pre-tax) |
| **Combined** | **14.4%** | Gross basic salary excl. overtime, bonus, commission |

No published Kina floor/ceiling on the contribution base was found. [RESEARCH GAP — reviewer to confirm: treat as "no stated contribution cap" rather than assuming one.]

### Other Key Rates

**Other Key Rates**

| Item | Rate / Threshold | Source |
| --- | --- | --- |
| GST | 10% on most goods and services | Goods and Services Tax Act 2003, s 8; IRC GST page |
| GST registration threshold | Annual turnover PGK 250,000 (voluntary below) | Goods and Services Tax Act 2003, s 43; IRC GST page |
| Corporate income tax | 30% for resident companies (2025 and 2026); non-resident companies 48% in 2025, and from 2026 a PNG permanent establishment pays 30% plus 15% non-resident tax on repatriated profit | IRC Corporate Tax Rates page; Income Tax Act 2025, ss 14 and 71 and Sch 1 Part I cl (5) and (9) |
| Capital gains tax (from 1 Jan 2026) | 15% — narrow; resource rights and interests deriving more than 50% of their value from them | Income Tax Act 2025, ss 16 and 83 and Sch 1 Part I cl (21) |
| Minimum wage (2025) | PGK 3.50 / hour | ILO; WageIndicator |
| Minimum wage (from 1 Jan 2026) | PGK 5.00 / hour (K5.25 in 2027; K5.50 in 2028) | ILO; WageIndicator |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | STOP — residency determines whether the K20,000 threshold applies |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether income already SWT-taxed at source | Treat as final-taxed employment income (no return) until confirmed |
| Unknown whether superannuation applies | Apply 6%/8.4% only for PNG-citizen employees of an employer with 15 or more employees who have been continuously employed for three months or more |
| Unknown asset / depreciation life | Flag for reviewer — capital allowance rates not set in this skill |
| Unknown GST registration status | Assume not registered (turnover below PGK 250,000) until confirmed |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable — bank statement (and/or payslips) for the full tax year in CSV, PDF, or pasted text, plus confirmation of residency status (resident / non-resident) and income type (employment only / self-employment / mixed).

Recommended — payslips showing fortnightly SWT withheld, superannuation statements (Nambawan Super / Nasfund), sales and purchase invoices, prior year assessment or return, GST registration status.

Ideal — complete income and expenditure account, asset register, provisional tax payment confirmations, employer SWT remittance records, full payroll detail.

Refusal if minimum is missing — SOFT WARN. No bank statement or payslip at all = hard stop. Bank statement alone (no payslips/invoices) = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that SWT was correctly withheld at source and that all deductions claimed are supported by valid documentation."

### Refusal Catalogue

- **R-PG-1 — Residency unknown** — Residency determines whether the PGK 20,000 tax-free threshold applies (residents) or whether the first Kina is taxed at 22% (non-residents). This skill cannot compute tax without confirmed residency status. Please confirm before proceeding.
- **R-PG-2 — Companies, partnerships, trusts** — This skill covers individuals (employees and sole traders) only. Companies (30% CIT), partnerships, and trusts file separate returns. Escalate to a PNG-registered tax agent.
- **R-PG-3 — Extractive / resource interests and CGT** — Disposals of taxable assets tied to mining, petroleum, or resource rights — including indirect disposals via a 10% or greater beneficial-ownership change — fall under the new 15% CGT regime (from 1 Jan 2026) and are out of scope. Escalate to a PNG-registered tax agent.
- **R-PG-4 — Mixed expatriate / foreign-source income** — Expatriate packages, double-tax-treaty relief, and foreign-source income require specialised analysis. Out of scope. Escalate to a PNG-registered tax agent.
- **R-PG-5 — Arrears / IRC enforcement** — Client has outstanding tax arrears or is subject to IRC enforcement. Late-payment penalties (20% p.a.) and additional tax for failure to furnish (up to 100% of tax) are severe. Do not advise. Escalate to a PNG-registered tax agent immediately.
- **R-PG-6 — GST return requested** — This skill covers income tax / salary or wages tax only. PNG GST (10%) is a separate return. Escalate or use a dedicated PNG GST skill.
- **R-PG-7 — 2026 return under the new Act** — Returns for the 2026 tax year are governed by the Income Tax Act 2025 (in force 1 Jan 2026, first returns due 2027), which may change benefit valuations, salary-packaging limits, and introduces CGT. Do not finalise a 2026 computation from this 2025-based skill without reviewer confirmation against the Act text.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. Many PNG employees are taxed entirely at source under SWT (final tax) — for those, no income tax return is required and the patterns are used only to confirm there is no untaxed side income.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Business income (self-employment) | If GST-registered, extract net (excl. 10% GST) |
| FEES, PROFESSIONAL FEES, CONSULTANCY, SERVICES | Business income | Typical sole-trader income |
| SALARY, WAGES, PAY, [employer name], FORTNIGHT | Employment income — SWT at source | Usually final-taxed; confirm SWT withheld |
| RENT RECEIVED, RENTAL | Rental income | Non-employment income — annual return required |
| INTEREST, INTERESSI | Investment income | Non-employment income — annual return required |
| DIVIDEND | Investment income | Non-employment income — annual return required |
| IRC REFUND, TAX REFUND | EXCLUDE | Tax refund from prior year |
| GOVERNMENT GRANT, CAPITAL GRANT | EXCLUDE unless revenue grant | Capital grants EXCLUDE; revenue grants = business income |
| SUPER WITHDRAWAL, NAMBAWAN, NASFUND (credit in) | EXCLUDE / flag | Super distribution — taxed under withdrawal-tax table, not ordinary income |

### 3.2 Expense Patterns (Debits) — Deductible Business Expenses (self-employed only)

**3.2 Expense Patterns (Debits) — Deductible Business Expenses (self-employed only)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, RENT [commercial address] | Office rent | Deductible | Dedicated business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible |  |
| ACCOUNTANT, AUDITOR, BOOKKEEP, CPA, TAX AGENT | Accountancy fees | Deductible |  |
| LAWYER, LEGAL, NOTARY (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, ADVERTISING, GOOGLE ADS, FACEBOOK ADS | Marketing/advertising | Deductible |  |
| TRAINING, COURSE, SEMINAR, CONFERENCE | Training | Deductible | Must relate to current business |
| BANK FEE, SERVICE FEE, BSP CHARGE, KINA BANK CHARGE | Bank charges | Deductible | Business account only |
| INTERNET, DIGICEL DATA, TELIKOM, HOSTING, DOMAIN | IT / communications | Deductible (business %) | Apportion if mixed use |

### 3.3 Expense Patterns (Debits) — Utilities (may need apportionment)

**3.3 Expense Patterns (Debits) — Utilities (may need apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| PNG POWER, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| WATER PNG, EDA RANU, WATER | Water | T2 if home office | Apportion |
| DIGICEL, BMOBILE, VODAFONE, TELIKOM | Telecoms/phone | T2 | Business use portion only; default 0% if mixed |

### 3.4 Expense Patterns (Debits) — Travel

**3.4 Expense Patterns (Debits) — Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR NIUGINI, PNG AIR, FLIGHT | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, LODGE, GUESTHOUSE, BOOKING.COM | Accommodation | Deductible if business travel |  |
| TAXI, PMV, HIRE CAR | Local transport | Deductible if business purpose |  |
| FUEL, PETROL, DIESEL, PUMA, MOBIL | Vehicle fuel | T2 — business % only | Requires mileage log |

### 3.5 Expense Patterns (Debits) — NOT Deductible

**3.5 Expense Patterns (Debits) — NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINNER, ENTERTAINMENT, CLIENT MEAL | Entertainment | Generally not deductible | Flag for reviewer |
| GROCERIES, SUPERMARKET, STOP N SHOP, RH, PERSONAL | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, INFRINGEMENT | Fines/penalties | NOT deductible | Public policy |
| IRC PAYMENT, INCOME TAX, SWT PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.6 Exclusions (Neither Income nor Expense)

**3.6 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, LOAN PRINCIPAL | EXCLUDE | Loan principal movement |
| SUPER CONTRIBUTION, NAMBAWAN, NASFUND (debit out) | Superannuation | 6% employee contribution — not a business expense |
| GST PAYMENT, IRC GST | EXCLUDE | GST liability payment, not expense |
| PROVISIONAL TAX, PT INSTALMENT | Credit against liability | Not an expense — offset against assessed tax |

### 3.7 PNG Banks — Statement Format Reference

**3.7 PNG Banks — Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BSP (Bank South Pacific) | TRANSFER, EFT, DD, SO, FEE | PDF/CSV; largest PNG bank; description holds counterparty + reference |
| Kina Bank | PAYMENT, TRF, CARD, CHARGE | PDF/CSV |
| Westpac PNG | TRANSFER, DIRECT DEBIT, FEE | PDF; date format DD/MM/YYYY |
| ANZ PNG | PAYMENT, EFTPOS, TRF, CHARGE | PDF/CSV |

## Section 4 -- Worked Examples

All amounts in Papua New Guinea Kina (PGK / K).

### Example 1 -- Salary credit (employee, SWT final tax)

**Input line:**
`14/03/2025 ; BSP EFT CREDIT ; HIGHLANDS COFFEE LTD ; FORTNIGHT PAY ENDING 13/03 ; +2,450.00 ; PGK`

**Reasoning:**
Net fortnightly salary already taxed under SWT at source. SWT is a final tax for an employee whose only income is fully-taxed employment income — no annual income tax return is required. The K2,450 is net pay; gross and SWT appear on the payslip, not the bank statement.

**Classification:** Employment income, SWT final tax. No further income tax due. EXCLUDE from any self-employment computation.

### Example 2 -- Sole-trader client payment (GST-registered)

**Input line:**
`20/03/2025 ; KINA BANK TRANSFER IN ; MOROBE TRADING LTD ; INV-0042 ; +1,100.00 ; PGK`

**Reasoning:**
Payment for services. Client is GST-registered (turnover over PGK 250,000), so K1,100 includes 10% GST. Net business income = K1,000 (K1,100 ÷ 1.10). K100 is GST collected — a liability to IRC, excluded from income.

**Classification:** Business income = K1,000. GST K100 excluded.

### Example 3 -- Superannuation contribution (employee 6%)

**Input line:**
`14/03/2025 ; BSP DD ; NAMBAWAN SUPER ; MEMBER CONTRIBUTION ; -147.00 ; PGK`

**Reasoning:**
Employee superannuation contribution is 6.0% of gross basic salary. For a fortnight where gross basic salary is K2,450, the employee contribution is 6% × 2,450 = K147.00 (the employer separately contributes 8.4% × 2,450 = K205.80). Source: Superannuation (General Provisions) Act 2000, ss 76 and 77, and the Bank of Papua New Guinea's public notice of 21 February 2025. The employee contribution is not a business expense.

**Classification:** Superannuation (employee 6%). Confirm gross basic salary excludes overtime/bonus/commission.

### Example 4 -- Fuel (mixed-use vehicle)

**Input line:**
`02/04/2025 ; ANZ CARD ; PUMA ENERGY WAIGANI ; FUEL ; -180.00 ; PGK`

**Reasoning:**
Vehicle fuel for a sole trader. Only the business-use percentage is deductible, and only with a mileage log. Tier 2 — conservative default is 0% deduction until the business percentage is documented.

**Classification:** T2. Default K0 deductible until mileage log confirms business %.

### Example 5 -- Income tax / provisional tax payment (not deductible)

**Input line:**
`28/09/2025 ; BSP TRANSFER ; INTERNAL REVENUE COMMISSION ; PROVISIONAL TAX 2025 ; -3,000.00 ; PGK`

**Reasoning:**
Provisional tax is a payment on account against the year's assessed income tax — it is not a business expense. It is credited against the final assessed liability, not deducted from income. For 2025 the IRC raises the provisional tax assessment from the last return lodged and the notice sets the due date; from the 2026 tax year three instalments fall due on 30 April, 31 July and 31 October (Income Tax Act 2025 s 138).

**Classification:** Provisional tax paid (credit against assessed tax). NOT a deduction.

### Example 6 -- Resident sole trader, full-year tax computation

**Inputs:** Resident sole trader. Gross business income K120,000; allowable expenses K35,000 → taxable income K85,000.

**Reasoning (resident brackets):**
- 0 – 20,000 at 0% = K0
- 20,001 – 33,000 at 30% = 30% × 13,000 = K3,900
- 33,001 – 70,000 at 35% = 35% × 37,000 = K12,950
- 70,001 – 85,000 at 40% = 40% × 15,000 = K6,000
- Total income tax = 0 + 3,900 + 12,950 + 6,000 = K22,850

If K3,000 provisional tax was already paid (Example 5), balance due on assessment = 22,850 − 3,000 = K19,850.

**Classification:** Income tax K22,850; balance due K19,850 after provisional tax credit.

### Example 7 -- Internal transfer (exclude)

**Input line:**
`15/05/2025 ; BSP TRANSFER ; OWN ACCOUNT - SAVINGS ; ; -2,000.00 ; PGK`

**Reasoning:**
Transfer between the client's own accounts. Neither income nor expense.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency and the Tax-Free Threshold

- **Residency threshold rule** — Residents receive a PGK 20,000 tax-free threshold (effective 1 Jan 2024). Non-residents receive no threshold: in 2025 the first kina is taxed at 30%, and from 2026 at 22%. Residency must be confirmed before any rate table is applied (see R-PG-1). The IRC treats an individual as resident when they spend more than six months in PNG in the year, continuously or not, subject to any treaty; the Income Tax Act 2025 makes an individual resident if they reside in PNG, are domiciled there without a permanent place of abode elsewhere, or are present for 183 days or more in the tax year (unless their usual abode is abroad and they do not intend to take up residence).  _(Internal Revenue Commission, Taxation of Individuals — https://irc.gov.pg/pages/taxes/individuals/taxation-of-individuals ; Income Tax (Salary or Wages Tax) (Rates) (2025 Budget) (Amendment) Act 2024 (No. 18 of 2024), Table 2A, IRC copy — https://static.irc.gov.pg/2025/January/9RMCiB-media-incometax-salaryorwagestaxratesact2024.pdf ; Income Tax Act 2025, s 10(2) and Schedule 1 Part I cl (1) and (2), IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

### 5.2 Salary or Wages Tax (SWT / PAYE)

- **SWT mechanics** — SWT is assessed fortnightly using the fortnightly tax tables, regardless of actual pay frequency (pay for other periods is converted to a fortnightly equivalent). It operates as a final tax for employees whose only income is fully-taxed employment income — those employees do not lodge an annual return, and no refund arises even where only one fortnight was worked. The employer withholds SWT each fortnight and remits it monthly to the IRC by the 7th day of the following month; an employer who fails to remit pays 20% of the amount plus 20% a year calculated daily. The Income Tax Act 2025 keeps this design: salary and wages tax is a fortnightly tax withheld by the employer (ss 13 and 149, Schedule 6) and is final where the employee is not required to lodge a return (s 13(6)).  _(Internal Revenue Commission, Salary and Wages Tax — https://irc.gov.pg/pages/know-your-taxes/salary-wages-tax ; Internal Revenue Commission, Taxation of Individuals — https://irc.gov.pg/pages/taxes/individuals/taxation-of-individuals ; Internal Revenue Commission, Key Tax Dates — https://irc.gov.pg/key-tax-dates ; Income Tax Act 2025, ss 13, 136 and 149, IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

### 5.3 Who Must Lodge an Annual Return

- **Annual return requirement** — A salary or wage earner lodges a return only where they earn other income above K100 in the year, or where they choose to lodge to claim the 25% rebate on work expenses above K200; everyone else with non-salary income must lodge, including the self-employed and anyone with interest, rental, trust or partnership income (the gazette lists the categories each year; gross investment income of K100 or less is excused unless the Commissioner General asks). Under the Income Tax Act 2025 an individual whose only assessable income is employment income taxed under s 149 need not lodge, as may a non-resident whose only PNG income bore non-resident tax (s 136).  _(Internal Revenue Commission, Taxation of Individuals — https://irc.gov.pg/pages/taxes/individuals/taxation-of-individuals ; National Gazette No. G7 of 7 January 2025, Lodgement of 2024 Income Tax Returns, Part A, PacLII — http://www.paclii.org/pg/other/PGGovGaz/2025/7.pdf ; Income Tax Act 2025, s 136, IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

### 5.4 Provisional Tax (self-employed / non-salary income)

- **Provisional tax, 2025 (Income Tax Act 1959)** — The Commissioner General issues a provisional tax assessment based on the last income tax return lodged so that tax on the year's non-salary income is collected during the year; companies pay three equal instalments on or before 30 April, 31 July and 31 October, and a taxpayer who expects a lower liability may apply to vary the assessment before the due date. The payments are credited against the assessed tax when the return is lodged. The due date for an individual's provisional tax is the date on the notice; this guide no longer carries an unsourced "not before 30 September" rule.  _(Internal Revenue Commission, Taxation of Companies (Provisional Tax) — https://irc.gov.pg/pages/taxes/businesses-and-employers/taxation-of-companies)_
- **Provisional tax, 2026 onwards (Income Tax Act 2025, s 138)** — An income taxpayer pays three instalments by the last day of the month after the end of the third, sixth and ninth months of the tax year (30 April, 31 July and 31 October for a calendar year), each one third of the most recent assessed liability (after foreign tax credits, multiplied by the uplift factor in the Regulations) less tax withheld under Part X. An individual whose taxable income is reasonably expected to stay below the K20,000 tax-free threshold pays no instalments.  _(Income Tax Act 2025, s 138, IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_
- **Assessment payment due date** — Personal and company income tax shown on a notice of assessment is due 30 days after the notice, or as the IRC directs. From the 2026 tax year income tax on a self-assessment return is due on the return due date, and tax on any other return on the date in the notice of assessment (s 137).  _(Internal Revenue Commission, Tax Information — https://irc.gov.pg/pages/know-your-taxes/tax-information ; Income Tax Act 2025, s 137, IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

### 5.5 Filing Deadlines (individuals)

**5.5 Filing Deadlines (individuals)**  _(National Gazette No. G7 of 7 January 2025, Lodgement of 2024 Income Tax Returns, Part E (Income Tax Act 1959 s 223), PacLII — http://www.paclii.org/pg/other/PGGovGaz/2025/7.pdf ; Income Tax Act 2025, s 135, IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

| Tax year and lodgement method | Deadline |
| --- | --- |
| 2024 returns, self-lodged (no tax agent) | On or by 28 February 2025 (the Commissioner General gazettes the same notice each January; the 2025 return notice is published in January 2026) |
| 2024 returns, through a registered tax agent | Such later date as the tax agent lodgement extension program provides; the gazette sets no fixed 30 June date |
| 2026 and later tax years, individuals and partnerships | Within 3 months after the end of the tax year (31 March for a calendar year) |
| 2026 and later tax years, companies | Within 6 months after year end, or 9 months where a registered tax agent prepares the return |

### 5.6 Dependant Rebates — NOT REPEALED

- **Dependant rebate repeal put on hold** — The 2024 Budget announced the repeal of the dependant rebate, but the IRC's public notice of 19 January 2024 records that the Government put the repeal on hold, the amendment was not certified and the IRC does not administer it: employers were told to keep applying the dependant columns of the fortnightly tables (Tables A, B and C) and to reverse any removal already made. The IRC's table text effective 1 January 2024 repeats that the Government decided not to proceed. Nothing in the 2025 Budget Acts repealed the rebate, so it applies to 2025 declarations. Secondary summaries that report the rebate as repealed are wrong on this point.  _(Internal Revenue Commission, Public Notice: 2024 Budget - Employee Tax-Free Threshold and Dependant Rebate, 19 January 2024, and Salary and Wages Tax Table Text Effective 1 January 2024, both linked from https://irc.gov.pg/pages/know-your-taxes/salary-wages-tax)_
- **Dependant tax credit from 2026 (Income Tax Act 2025, s 56)** — A resident individual who maintains a dependant (a spouse, an unmarried child under 16, a student child aged 16 to 24 in full-time education, an invalid relative, or a resident parent of either spouse, whose own income does not exceed K1,040 a year or K40 a fortnight) receives a credit of the lesser of 15% of the tax before credits or K450 for the first dependant, and the lesser of 10% or K300 for each other dependant, capped at the greater of 35% of the tax or K1,050 a year (so three dependants exhaust it); it cannot create a refund and is apportioned for part-year or shared maintenance. The fortnightly withholding formula deducts one twenty-sixth of the credit where the employee has lodged a declaration.  _(Income Tax Act 2025, s 56, Schedule 1 Part II cl (8) to (12) and Schedule 6 cl 2(3), IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

### 5.7 Superannuation

**5.7 Superannuation rules**

| Rule | Detail |
| --- | --- |
| Employer obligation | Mandatory for employers employing or engaging **15 or more** employees (s 4(1)(a) with the Superannuation (Amendment) Regulation 2004); smaller employers may elect to contribute |
| Employee coverage | Compulsory for **PNG-citizen** employees **continuously employed for three months or more**; mandatory contributions do not apply to non-citizens (ss 76(6) and 77(6), inserted 2013), who may contribute voluntarily |
| Employee contribution | **6.0%** of base salary, deducted from pay (s 77) |
| Employer contribution | **8.4%** of base salary from the employer's own funds (s 76) |
| Contribution base | "Pay": gross salary, wages and commission earned on duty or paid leave and paid in cash — excludes overtime, allowances, bonuses, compensation and gifts (s 3) |
| Contribution ceiling | None: the Act and the Bank's notice set no cap on the base |
| Remittance | Employer contributions within 14 days of the end of each calendar month; employee deductions within 14 days of the deduction (s 78) |

- **Superannuation legislation and funds** — Legislation: Superannuation (General Provisions) Act 2000, as amended in 2001, 2002, 2004, 2007 and 2013, with the Bank of Papua New Guinea as regulator. Main authorised funds: Nambawan Super (public sector), Nasfund (private sector). Employer contributions to an approved fund are exempt from salary or wages tax up to 15% of the employee's fully taxable salary, and from 2026 are deductible to the employer up to 15% of the employee's taxed employment income (ITA 2025 s 117).  _(Superannuation (General Provisions) Act 2000, ss 3, 4, 76 to 79, PacLII — https://www.paclii.org/pg/legis/num_act/spa2000396/ ; Superannuation (General Provisions) (Amendment) Act 2013, ss 6 and 7, PacLII — https://www.paclii.org/pg/legis/num_act/spa2013476/ ; Bank of Papua New Guinea, Public Notice: Employer and Employee Superannuation Contributions, 21 February 2025 — https://bankpng.gov.pg/sites/default/files/2025-02/20250221%20-%20Public%20Notice%20to%20Employer%20and%20Employee%20Superannuation%20Contribution.pdf ; Internal Revenue Commission, Taxation of Individuals (Exempt income) — https://irc.gov.pg/pages/taxes/individuals/taxation-of-individuals ; Income Tax Act 2025, s 117, IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

**Superannuation withdrawal/distribution tax (concessional, by years of contributions)**  _(Internal Revenue Commission, Salary and Wages Tax (Superannuation) — https://irc.gov.pg/pages/know-your-taxes/salary-wages-tax ; Income Tax Act 2025, s 119 and Schedule 1 Part I cl (12), IRC certified copy — https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf)_

| Years of contributions | Withdrawal tax (2025 IRC table; the same rates in the 2025 Act from 2026) |
| --- | --- |
| Under 5 years | Marginal rate |
| 5 – 9 years | Lesser of 15% or marginal rate |
| 9 – 15 years | Lesser of 8% or marginal rate |
| 15 years or more | 2% |
| Any period: 7 years or more of contributions and the member is over 50 or subject to enforced early retirement; death or permanent disability of the member | 2% |

The 2025 Act taxes only the part of a pay-out not representing the member's own taxed contributions (s 119(2)); a lump sum rolled into a retirement savings account with an approved fund is not taxed (s 119(3)).

### 5.8 GST Interaction

**5.8 GST Interaction**  _(Goods and Services Tax Act 2003, ss 8 and 43, PacLII — https://www.paclii.org/pg/legis/num_act/gasta2003226/ ; Internal Revenue Commission, Goods and Services Tax — https://irc.gov.pg/pages/taxes/businesses-and-employers/goods-services-tax)_

| Scenario | Income Tax Treatment |
| --- | --- |
| GST-registered, GST collected on sales | NOT income — exclude from business income |
| GST-registered, input GST recovered | NOT an expense — exclude |
| Not GST-registered (turnover < PGK 250,000) | All GST paid on purchases is part of the gross cost (deductible as expense) |

- **GST rate and registration threshold** — GST is charged at 10% on taxable supplies and imports (GST Act 2003 s 8); registration is compulsory where annual turnover exceeds, or is expected to exceed, K250,000 (s 43), voluntary below; monthly returns and payment are due by the 21st of the following month.  _(Goods and Services Tax Act 2003, ss 8 and 43, PacLII — https://www.paclii.org/pg/legis/num_act/gasta2003226/ ; Internal Revenue Commission, Goods and Services Tax — https://irc.gov.pg/pages/taxes/businesses-and-employers/goods-services-tax ; Internal Revenue Commission, Key Tax Dates — https://irc.gov.pg/key-tax-dates)_

### 5.9 Non-Deductible Expenses

**5.9 Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Entertainment (client meals, events) | Generally blocked — flag for reviewer |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax / SWT itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |
| Superannuation employee contribution | Personal contribution, not a business expense |
| Provisional tax | Credit against assessed tax, not a deduction |

### 5.10 Penalties

**5.10 Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| Late lodgement of income tax return | Additional tax up to **100% of the tax** for failure to furnish | KPMG PNG Tax Profile; IRC practice |
| Late payment of income tax / provisional tax | **20% per annum** late-payment penalty | KPMG PNG Tax Profile |
| SWT (PAYE) non-compliance | An employer who fails to remit pays a penalty of **20% of the amount not paid plus 20% a year calculated daily** from the due date, and may be fined K500 to K5,000; failing to deduct attracts the same fine and liability for the undeducted amount; remittance is due by the 7th of the following month | IRC, Salary and Wages Tax — https://irc.gov.pg/pages/know-your-taxes/salary-wages-tax |
| Failure to lodge a gazetted return (2024 and earlier years) | Offence under s 313 of the Income Tax Act 1959: court penalty of **K500 to K5,000 plus K50 for each day** the return is outstanding | National Gazette No. G7 of 7 January 2025, Part F — http://www.paclii.org/pg/other/PGGovGaz/2025/7.pdf |

Caveat: the first two rows come from a Big-4 profile, not a directly-parsed IRC penalty schedule. [RESEARCH GAP — reviewer to re-confirm the late-lodgement and late-payment percentages against the Tax Administration Act 2017, which the Income Tax Act 2025 applies to income tax procedure (s 133).]

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (self-employed)

- Calculate the proportion of the home used for business (dedicated room(s) as a percentage of total rooms or floor area).
- Apply that percentage to rent, electricity (PNG Power), water (Water PNG / Eda Ranu), and internet.
- A dual-use room does not qualify.

Conservative default: 0% deduction until reviewer confirms the room arrangement.
Flag for reviewer: Confirm room count, floor-area basis, and that the workspace is genuinely dedicated.

### 6.2 Motor Vehicle Business Use (self-employed)

- Only the business-use percentage of fuel, insurance, and running costs is deductible.
- Client must maintain a mileage log (business vs total mileage).

Conservative default: 0% business use until a mileage log is provided.
Flag for reviewer: Confirm the business percentage is documented and reasonable.

### 6.3 Phone / Internet Mixed Use

- Business-use portion only (Digicel, bmobile, Telikom).

Conservative default: 0% deduction until the business percentage is confirmed.

### 6.4 Capital Allowances / Depreciation

- Business assets are depreciated, not expensed. This skill does not set PNG capital-allowance rates.

Conservative default: flag any asset purchase for the reviewer.
Flag for reviewer: [RESEARCH GAP — PNG depreciation/capital-allowance rates not captured in this skill; reviewer to apply the correct Income Tax Act schedule.]

### 6.5 Entertainment

- Generally non-deductible; reviewer to confirm whether any narrow business exception applies.

### 6.6 Residency Edge Cases

- Part-year residents, expatriates, and those present under specific day-count tests require reviewer judgement on which threshold/rate table applies.

## Section 7 -- Excel Working Paper Template

```
PAPUA NEW GUINEA INCOME TAX -- WORKING PAPER
Tax Year: 2025  (Income Tax Act 1959 regime)
Client: ___________________________
Residency: Resident / Non-resident
Income type: Employment only / Self-employed / Mixed
Currency: PGK (Kina)

A. EMPLOYMENT INCOME (SWT at source)
  A1. Gross salary/wages (per payslips)          ___________
  A2. SWT withheld (fortnightly, final tax)      ___________
  A3. Net employment income                       ___________
  (If A1 is the ONLY income and fully SWT-taxed -> no annual return required)

B. SELF-EMPLOYMENT / BUSINESS INCOME
  B1. Gross business income (net of GST if reg.) ___________
  B2. Rental income                               ___________
  B3. Interest / dividends                        ___________
  B4. TOTAL non-employment income                 ___________

C. ALLOWABLE BUSINESS DEDUCTIONS (self-employed)
  C1. Office rent                                 ___________
  C2. Professional insurance                      ___________
  C3. Accountancy / legal / tax-agent fees        ___________
  C4. Office supplies                             ___________
  C5. Marketing / advertising                     ___________
  C6. Training                                    ___________
  C7. Bank charges                                ___________
  C8. Telecoms (business %)                       ___________
  C9. Travel (flights, accommodation, transport)  ___________
  C10. Home office (% of utilities/rent)          ___________
  C11. Vehicle (business %)                       ___________
  C12. Capital allowances (reviewer-set rates)    ___________
  C13. TOTAL deductions                           ___________

D. TAXABLE INCOME (B4 - C13; add A1 if return required) ___________

E. TAX COMPUTATION (pass to deterministic engine)
  E1. Income tax (resident or non-resident table) ___________
  E2. Less: provisional tax paid                  ___________
  E3. Balance due / refund (E1 - E2)              ___________

F. SUPERANNUATION (if applicable)
  F1. Gross basic salary (excl. OT/bonus/comm.)   ___________
  F2. Employee contribution 6.0%                  ___________
  F3. Employer contribution 8.4%                  ___________

REVIEWER FLAGS:
  [ ] Residency confirmed (threshold applies?)?
  [ ] Income fully SWT-taxed at source (no return)?
  [ ] GST registration status confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] Capital-allowance rates applied correctly?
  [ ] Provisional tax credited (not deducted)?
  [ ] Superannuation base excludes OT/bonus/commission?
  [ ] 2026 work: re-checked against Income Tax Act 2025?
```

## Section 8 -- Bank Statement Reading Guide

### PNG Bank Statement Formats

**PNG Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BSP (Bank South Pacific) | PDF, CSV | Date, Description, Debit, Credit, Balance | Largest PNG bank; description holds counterparty + reference |
| Kina Bank | PDF, CSV | Date, Narrative, Amount, Balance | Card transactions show merchant |
| Westpac PNG | PDF | Date, Particulars, Withdrawals, Deposits | Date format DD/MM/YYYY |
| ANZ PNG | PDF, CSV | Value Date, Description, Amount, Balance | EFTPOS shows merchant name |

### Key PNG Banking / Payroll Terms

**Key PNG Banking / Payroll Terms**

| Term | Meaning | Classification Hint |
| --- | --- | --- |
| SWT | Salary or Wages Tax | PAYE withheld at source — final tax |
| EFT / TRF | Electronic transfer | Check direction for income/expense |
| DD | Direct debit | Regular expense (utility, subscription, super) |
| SO | Standing order | Regular expense (rent, loan) |
| PMV | Public Motor Vehicle | Local transport fare — possible business travel |
| EFTPOS | Card payment at terminal | Expense — check merchant |
| FORTNIGHT / FN | Two-week pay period | Salary credit — employment income |
| Nambawan / Nasfund | Superannuation funds | Super contribution (6%) or withdrawal |
| IRC | Internal Revenue Commission | Tax payment — not deductible |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- PAPUA NEW GUINEA INCOME TAX
1. Residency: are you a PNG resident or non-resident for tax?
2. Income type: employment only, self-employed, or mixed?
3. If employed: is all your salary taxed under SWT at source (payslips show SWT)?
4. Do you have any non-salary income (business, rental, interest, dividends)?
5. GST: is your business turnover over PGK 250,000 / are you GST-registered?
6. Home office: dedicated room or shared space? If dedicated, what % of floor area?
7. Vehicle: do you use a car for business? What % is business use? Mileage log?
8. Phone/internet: what % is business use?
9. Superannuation: which fund (Nambawan/Nasfund) and your gross basic salary?
10. Provisional tax: total amount paid in the tax year?
11. Will the return be lodged via a registered tax agent (under the IRC's lodgement extension program) or self-lodged (28 Feb for 2024 and earlier years; 31 March from the 2026 tax year)?
```

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References**

| Topic | Reference |
| --- | --- |
| Income tax (2025) | Income Tax Act 1959 (as amended) and Income Tax, Dividend (Withholding) Tax and Interest (Withholding) Tax Rates Act 1984, as amended by Act No. 17 of 2024 — IRC Legislation Home; PacLII |
| Salary/wages tax rates (2025) | Income Tax (Salary or Wages Tax) (Rates) Act 1979, as amended by Act No. 25 of 2023 (2024 Budget) and Act No. 18 of 2024 (2025 Budget) — IRC copy; PacLII |
| New regime (from 2026) | Income Tax Act 2025 — IRC certified copy (ss 10, 13, 56, 119, 135 to 138, 149, 165; Schedules 1 and 6) |
| Rate brackets / thresholds | The Acts above; IRC Salary and Wages Tax page and public notice of 19 January 2024 |
| SWT, provisional tax, deadlines | IRC Salary and Wages Tax, Taxation of Individuals, Taxation of Companies, Tax Information and Key Tax Dates pages; National Gazette G7 of 7 January 2025; Income Tax Act 2025 ss 135 to 138 |
| Superannuation | Superannuation (General Provisions) Act 2000 and 2013 Amendment Act (PacLII); Bank of Papua New Guinea public notice of 21 February 2025; IRC Salary and Wages Tax page (pay-out rates); Income Tax Act 2025 ss 117 and 119 |
| GST | Goods and Services Tax Act 2003 (PacLII); IRC GST page |
| CGT (from 2026) | Income Tax Act 2025, Part V and Schedule 1 |
| Penalties | IRC Salary and Wages Tax page; National Gazette G7 of 2025; KPMG PNG Tax Profile for the unverified rows |
| Tax authority | Internal Revenue Commission (IRC) — irc.gov.pg |

### Source URLs

- Income Tax Act 2025, IRC certified copy: https://static.irc.gov.pg/2025/October/0uvVvY-media-certifiedincometaxact2025.pdf
- Income Tax (Salary or Wages Tax) (Rates) (2024 Budget) (Amendment) Act 2023 (No. 25 of 2023), PacLII: https://www.paclii.org/pg/legis/num_act/itowt2024ba2023500/
- Income Tax (Salary or Wages Tax) (Rates) (2025 Budget) (Amendment) Act 2024 (No. 18 of 2024), IRC copy: https://static.irc.gov.pg/2025/January/9RMCiB-media-incometax-salaryorwagestaxratesact2024.pdf
- Income Tax, Dividend (Withholding) Tax and Interest (Withholding) Tax Rates (2025 Budget) (Amendment) Act 2024 (No. 17 of 2024), PacLII: https://www.paclii.org/pg/legis/num_act/itdtaitr2025ba2024808/
- IRC Legislation Home (consolidated Acts to 2021 and the certified 2025 Act): https://irc.gov.pg/pages/know-your-taxes/legislation-home
- IRC Salary and Wages Tax (rates, allowances, superannuation and long service leave tables, penalties; links to the 19 January 2024 public notice and the 2024 table text): https://irc.gov.pg/pages/know-your-taxes/salary-wages-tax
- IRC Taxation of Individuals: https://irc.gov.pg/pages/taxes/individuals/taxation-of-individuals
- IRC Taxation of Companies (provisional tax): https://irc.gov.pg/pages/taxes/businesses-and-employers/taxation-of-companies
- IRC Tax Information (payment due dates): https://irc.gov.pg/pages/know-your-taxes/tax-information
- IRC Key Tax Dates: https://irc.gov.pg/key-tax-dates
- IRC Goods and Services Tax: https://irc.gov.pg/pages/taxes/businesses-and-employers/goods-services-tax
- National Gazette No. G7 of 7 January 2025, Lodgement of 2024 Income Tax Returns, PacLII: http://www.paclii.org/pg/other/PGGovGaz/2025/7.pdf
- Superannuation (General Provisions) Act 2000, PacLII: https://www.paclii.org/pg/legis/num_act/spa2000396/
- Superannuation (General Provisions) (Amendment) Act 2013, PacLII: https://www.paclii.org/pg/legis/num_act/spa2013476/
- Bank of Papua New Guinea, Public Notice: Employer and Employee Superannuation Contributions, 21 February 2025: https://bankpng.gov.pg/sites/default/files/2025-02/20250221%20-%20Public%20Notice%20to%20Employer%20and%20Employee%20Superannuation%20Contribution.pdf
- Goods and Services Tax Act 2003, PacLII: https://www.paclii.org/pg/legis/num_act/gasta2003226/
- ILO — new national minimum wage for PNG: https://www.ilo.org/resource/news/ilo-welcomes-new-national-minimum-wage-papua-new-guinea

### Test Suite

All figures recomputed end-to-end against the resident/non-resident bracket tables in Section 1.

Input: Resident, taxable income K85,000.
Expected: 0 (first 20,000) + 3,900 (30% × 13,000) + 12,950 (35% × 37,000) + 6,000 (40% × 15,000) = income tax K22,850.

Input: Resident, taxable income K33,000.
Expected: 0 + 30% × 13,000 = K3,900 (matches cumulative-tax column).

Input: Resident, taxable income K70,000.
Expected: 3,900 + 12,950 = K16,850 (matches cumulative-tax column).

Input: Resident, taxable income K300,000.
Expected: 88,850 (cumulative at 250,000) + 42% × 50,000 = 88,850 + 21,000 = K109,850.

Input: Non-resident, taxable income K85,000, 2025 tax year.
Expected: 9,900 (30% × 33,000) + 12,950 (35% × 37,000) + 6,000 (40% × 15,000) = K28,850 (= resident K22,850 + 30% × 20,000 lost threshold).

Input: Non-resident, taxable income K85,000, 2026 tax year.
Expected: 4,400 (22% × 20,000) + 3,900 (30% × 13,000) + 12,950 (35% × 37,000) + 6,000 (40% × 15,000) = K27,250 (= resident K22,850 + K4,400 lost threshold).

Input: Resident employee, 2026 tax year, fortnightly employment income K1,000, one dependant declared (illustrative application of the Schedule 6 formula; use the IRC's published 2026 tables once issued).
Expected: Schedule 6 formula (A × B) − C/26: tax on K1,000 at the fortnightly table = 30% × (1,000 − 770) = K69.00; dependant credit is the lesser of 15% of annual tax (26 × 69.00 = 1,794.00; 15% = K269.10) or K450, so C = K269.10 and C/26 = K10.35; SWT withheld = 69.00 − 10.35 = K58.65.

Input: Gross basic fortnight salary K2,450 (excl. OT/bonus/commission).
Expected: Employee 6% = K147.00; Employer 8.4% = K205.80; combined 14.4% = K352.80.

Input: Employee, only income is salary fully taxed under SWT at source.
Expected: No annual income tax return required; SWT is the final tax.

Input: Resident sole trader, income tax K22,850, provisional tax paid K3,000.
Expected: Provisional tax credited against assessed tax → balance due 22,850 − 3,000 = K19,850. Provisional tax is NOT deducted from income.

## PROHIBITIONS

- NEVER apply a rate table without knowing residency (residents get the K20,000 threshold; non-residents do not)
- NEVER apply the eliminated 22% first band to a resident
- NEVER apply the 22% non-resident first band to a 2025 computation (it is 30% from the first kina in 2025 and returns at 22% only from the 2026 tax year)
- NEVER drop the dependant rebate on the strength of the 2024 Budget announcement: the repeal was put on hold and the 2025 Act keeps the credit
- NEVER treat provisional tax as a deduction — it is a credit against assessed tax
- NEVER treat the employee superannuation contribution as a business expense
- NEVER allow income tax or SWT itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER include GST collected on sales in business income for a GST-registered client
- NEVER require an annual return from an employee whose only income is fully SWT-taxed at source
- NEVER finalise a 2026 computation from this 2025-based skill without reviewer confirmation against the Income Tax Act 2025
- NEVER present tax calculations as definitive — always label as estimated and pass to the deterministic engine

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
