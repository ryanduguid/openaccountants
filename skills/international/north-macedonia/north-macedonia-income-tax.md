---
name: north-macedonia-income-tax
description: Use this skill whenever asked about North Macedonia (Republic of North Macedonia) personal income tax for self-employed individuals and employees. Trigger on phrases like "how much tax do I pay in Macedonia", "Macedonian income tax", "personal income tax", "данок на личен доход", "MPIN salary declaration", "social contributions Macedonia", "denar payroll", "gross-to-net Macedonia", "self-employed tax Macedonia", "service contract tax", "UJP", "Public Revenue Office", "annual draft tax return", or any question about filing or computing personal income tax (PIT) for an employed or self-employed client in North Macedonia. Also trigger when preparing or reviewing a monthly salary calculation, a service-contract withholding, or an annual self-employed tax balance, computing the 28% social contributions, or advising on the MKD 10,270 monthly tax reduction. This skill covers the flat 10% PIT, the 15%/70% special rates, social-contribution rates and bases, the personal monthly exemption, registration thresholds, forms/deadlines, and interaction with VAT. ALWAYS read this skill before touching any North Macedonia income tax work.
version: 0.1
jurisdiction: MK
tax_year: 2025
last_updated: 2026-10-08
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# North Macedonia Personal Income Tax -- Individuals & Self-Employed

## North Macedonia Personal Income Tax -- Individuals & Self-Employed Skill v0.1

> **Tier 2 (research-verified) skill.** Rates, normative costs, deadlines and penalties cite the Law on Personal Income Tax (Official Gazette 241/2018, as amended to 274/2022; the Ministry of Finance's unofficial consolidated text) and the Law on Mandatory Social Insurance Contributions (Official Gazette 142/2008, as amended to 247/2018; the Public Revenue Office's unofficial consolidated text). Amendments after those consolidations were not traced. The yearly amounts the laws delegate (the MKD 10,270 monthly tax reduction, the MKD 63,154 average salary and the bases derived from it, the minimum wage) come from the Eurofast North Macedonia Tax Card 2025 / Payroll Guide 2025 and Bloomberg Tax reporting the Public Revenue Office's January 2025 clarification, and should be reconfirmed against the Ministry of Finance's annual tax-reduction notice and the State Statistical Office release before sign-off. Items marked **[RESEARCH GAP — reviewer to confirm]** are unresolved.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | North Macedonia (Republic of North Macedonia) |
| Tax | Personal Income Tax -- PIT (данок на личен доход) |
| Currency | MKD (Macedonian denar) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Law on Personal Income Tax (Закон за данокот на личен доход), Official Gazette 241/2018, 275/2019, 290/2020, 85/2021 and 274/2022 ("PIT Law" below) |
| Supporting legislation | Law on Mandatory Social Insurance Contributions (Official Gazette 142/2008 as amended to 247/2018; "Contributions Law" below); Law on Value Added Tax; Labour Relations Law (Official Gazette 62/05 and amendments) |
| Tax authority | Public Revenue Office (Управа за јавни приходи -- UJP / PRO), www.ujp.gov.mk; policy set by Ministry of Finance (finance.gov.mk) |
| Filing portal | UJP e-Services / e-Tax (e-Danoci); MPIN salary system for payroll |
| Annual draft return | PRO delivers draft by 30 April; taxpayer confirms/corrects by 31 May of the following year; tax due by 30 June [PIT Law arts. 96(2)-(3), 100(2)] |
| Self-employed annual return | Annual accounts and tax balance by 15 March of the following year; balance of tax due within 15 days after that deadline [PIT Law arts. 97, 100(1)] |
| Validated by | Pending — requires sign-off by a North Macedonia licensed accountant / tax advisor |
| Validation date | Pending |
| Skill version | 0.1 |

### PIT Rate Schedule (2025)

North Macedonia applies a **flat tax**, not progressive brackets. There is no cumulative-bracket table; each income type is taxed at a single rate.

### PIT Rate Schedule (2025)

**PIT Rate Schedule (2025)**

| Income type | Rate | Source |
| --- | --- | --- |
| Employment income | 10% | PIT Law art. 11(1) |
| Self-employment / business income | 10% | PIT Law art. 11(1) |
| Copyright royalties and industrial-property rights | 10% | PIT Law art. 11(1) |
| Sale of own agricultural products | 10% | PIT Law art. 11(1) |
| Rental income | 10% | PIT Law art. 11(1) |
| Income from capital (dividends, interest) | 10% | PIT Law arts. 11(1), 55 |
| Capital gains (taxable) | 10% | PIT Law art. 11(1) |
| Insurance income | 10% | PIT Law art. 11(1) |
| Other uncategorised taxable income | 10% | PIT Law art. 11(1) |
| Gains from games of chance | 15% | PIT Law art. 11(2) |
| Undeclared income (непријавен доход) | 70% | PIT Law art. 78 |
| Capital gains on securities / investment-fund shares held > 2 years | 0% (exempt); gains on securities and fund shares are taxable only for holdings acquired from 1 January 2023 | PIT Law art. 12(1)(39-а); Official Gazette 274/2022 art. 21 |
| Interest on term deposits | Not taxed until North Macedonia joins the EU (interest on sight deposits and transaction accounts is exempt outright) | PIT Law arts. 116, 12(1)(37) |

### PIT Rate Schedule (2025)

**There are no progressive bands. The flat 10% is the headline rate for almost all income.** The 2019 schedule's 18% band was suspended for 2020-2022 (Official Gazette 275/2019, art. 24), and art. 11 of the consolidated text to 274/2022 carries only the 10% and 15% rates. Personal relief takes the form of a fixed monthly tax reduction (see below), not a 0% band.

### Social Contribution Rates (2025) -- borne entirely by the employee on gross salary

**Social Contribution Rates (2025)**

| Class (Macedonian) | Employee rate | Employer rate | Source |
| --- | --- | --- | --- |
| Pension and disability insurance (Пензиско и инвалидско осигурување) | 18.8% | 0% | Contributions Law art. 25(1)(1) |
| Health insurance (Здравствено осигурување) | 7.5% | 0% | Contributions Law art. 25(1)(3) |
| Unemployment insurance (Осигурување во случај на невработеност) | 1.2% | 0% | Contributions Law art. 25(1)(8) |
| Additional health insurance for injury at work and occupational disease* | 0.5% | 0% | Contributions Law art. 25(1)(7) |
| **TOTAL mandatory social contributions** | **28.0%** | **0%** | Contributions Law art. 25(1) |

### Social Contribution Rates (2025) -- borne entirely by the employee on gross salary

*The statute calls the 0.5% component an additional contribution for mandatory health insurance in case of injury at work and occupational disease (Contributions Law art. 25(1)(7)); the Eurofast Tax Card labels it "disability". Both agree on the 0.5% rate and the 28% total.

**Arithmetic check:** 18.8 + 7.5 + 1.2 + 0.5 = **28.0%** (employee column). Employer column: 0 + 0 + 0 + 0 = **0%**. North Macedonia has **no separate employer-side social contribution** — the entire burden sits on the employee's gross salary and is withheld/remitted by the employer [Contributions Law art. 25(1); Eurofast Tax Card 2025].

### Contribution Bases (2025)

**Contribution Bases (2025)**

| Base | Amount (per month) | Basis | Source |
| --- | --- | --- | --- |
| National average gross salary (reference) | MKD 63,154 | State Statistical Office figure published in January 2025, the reference month the law fixes | Bloomberg Tax citing PRO; Contributions Law arts. 15(1), 16(5) |
| Minimum contribution base (floor) | MKD 31,577 | 50% of average gross salary (63,154 × 0.50) | Contributions Law art. 15(1); amount per Bloomberg Tax citing PRO |
| Maximum contribution base — employees (ceiling) | MKD 1,010,464 | 16 average gross salaries (63,154 × 16) | Contributions Law art. 16(1); amount per Bloomberg Tax citing PRO |
| Maximum contribution base — self-employed | MKD 757,848 | 12 average gross salaries (63,154 × 12) | Contributions Law art. 16(3); amount per Bloomberg Tax citing PRO |

### Contribution Bases (2025)

**Arithmetic check:** 63,154 × 0.50 = 31,577 ✓ · 63,154 × 16 = 1,010,464 ✓ · 63,154 × 12 = 757,848 ✓. Ceiling (1,010,464) ≥ floor (31,577) ✓.

### Tax Reduction & Wage Reference Figures (2025)

**Tax Reduction & Wage Reference Figures (2025)**

| Item | Amount | Source |
| --- | --- | --- |
| Monthly tax reduction (salary, wage compensation and pension only) | MKD 10,270 / month (one-twelfth of the annual amount the Minister of Finance publishes) | PIT Law arts. 10, 17(2); 2025 amount per Eurofast Tax Card 2025 |
| Minimum gross wage (effective March 2025) | MKD 36,037 / month (net ≈ MKD 24,379; hourly ≈ MKD 207) | Pepeljugoski law office |
| Registration threshold for sellers of own agricultural products | MKD 1,000,000 total annual income: register an activity by 15 January of the following year | PIT Law art. 45 |
| VAT registration threshold | MKD 2,000,000 turnover | Company Formation Macedonia |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown income type | Treat as "other income" at flat 10% — do NOT assume an exemption applies |
| Unknown whether income is salary | Do NOT apply the MKD 10,270 tax reduction (it applies only to salary, wage compensation and pension) |
| Unknown employment vs service-contract status | Service contract (PIT only, no social contributions on it) [Eurofast] |
| Unknown gross-vs-net of a salary figure | STOP — ask whether the figure is gross or net before computing |
| Unknown contribution base relief | Apply contributions on actual gross between the floor and ceiling |
| Unknown self-employed contribution ceiling | Use self-employed maximum base MKD 757,848/month |
| Unknown allowance-style base reduction | Do NOT apply (use full gross) until reviewer confirms the income category |
| Unknown VAT registration status | Assume not registered (no VAT split) until confirmed |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — for a salary computation: the gross monthly salary in MKD and confirmation that the figure is gross. For self-employment: the annual net business income (tax balance) or a full-year bank statement in CSV, PDF, or pasted text, plus confirmation of resident status.

**Recommended** — payslips / MPIN declarations for the year, the income category for each receipt (employment, service contract, rental, royalty, agricultural, capital, capital gain), SSC payment records, prior-year tax balance, VAT registration status.

**Ideal** — complete income and expenditure account for self-employed clients, asset register, prior-year annual accounts / tax balance, evidence supporting any base reductions (agricultural sales, IP rights, property lease deductions).

**Refusal if minimum is missing — SOFT WARN.** No salary figure / no bank statement at all = hard stop. A salary figure with no gross/net confirmation = hard stop (the entire computation hinges on it). A bank statement without supporting invoices for a self-employed client = proceed with reviewer warning: "This computation was produced from the bank statement alone. The reviewer must verify the income categorisation and that any base reductions or deductible contributions are supported."

### Refusal Catalogue

- **R-MK-1 — Gross/net of salary unknown** — "The whole gross-to-net calculation depends on whether the figure is the gross salary (бруто плата) or the net salary (нето плата). This skill cannot compute tax without that confirmation. Please confirm before proceeding."
- **R-MK-2 — Companies / legal entities** — "This skill covers individuals and sole self-employed persons only. Profit tax for companies (corporate income tax) is a separate regime. Escalate to a North Macedonia licensed accountant."
- **R-MK-3 — Non-resident / cross-border income** — "Non-resident taxation, double-tax-treaty relief, and foreign-salary positions require specialised analysis. Out of scope here (note: salary or pension received from abroad that was taxed abroad must be reported by 31 March of the following year [PIT Law art. 88(2)]). Escalate to a licensed accountant."  _(PIT Law art. 88(2))_
- **R-MK-4 — Undeclared income** — "Undeclared income is taxed at 70% (PIT Law art. 78) and triggers a formal PRO assessment. Do not self-classify. Escalate to a licensed accountant immediately."
- **R-MK-5 — Games of chance / gambling** — "Gains from games of chance are taxed at a special 15% rate with their own reporting. Confirm the exact nature before applying any rate. Escalate if material."
- **R-MK-6 — VAT return requested** — "This skill covers personal income tax and social contributions only. For North Macedonia VAT (DDV-04), use the dedicated VAT skill."
- **R-MK-7 — Arrears / enforcement** — "Client has outstanding tax arrears or is subject to PRO enforcement. Assessed tax under a Tax Assessment resolution must be paid within 15 days of delivery [PIT Law art. 100(3)]; failing to file a required calculation carries a fine of EUR 50-250 for an individual and EUR 100-250 for a sole trader or self-employed person [PIT Law art. 107]. Escalate to a licensed accountant."  _(PIT Law arts. 100(3), 107)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Macedonian terms are given alongside Latin transliterations and English. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Income category | Treatment | Notes |
| --- | --- | --- | --- |
| ПЛАТА, PLATA, SALARY, НЕТО ПЛАТА | Employment income | 10% PIT via MPIN | Gross-to-net already applied by employer; net hits account |
| ХОНОРАР, HONORAR, ДОГОВОР НА ДЕЛО, SERVICE CONTRACT, FEE | Service-contract income | 10% PIT, NO social contributions | Withheld/declared by payer if a legal entity [Eurofast] |
| ФАКТУРА, INVOICE, UPLATA OD KLIENT, CLIENT PAYMENT | Self-employment / business income | 10% on net income (tax balance) | If VAT-registered, extract net (excl. 18% VAT) |
| STRIPE PAYOUT, PAYPAL, WISE PAYOUT, REVOLUT | Business income | 10% on net income | Platform payout — match to invoices |
| UPWORK, FIVERR, TOPTAL | Business income | 10% on net income | Freelance platform — net of platform commission |
| КИРИЈА, KIRIJA, RENT RECEIVED, ЗАКУП | Rental income | 10% (after lease base reduction) | Unfurnished 10% deduction; furnished 15% deduction [PIT Law art. 53] |
| КАМАТА, KAMATA, INTEREST RECEIVED | Income from capital | 10% | Interest income |
| ДИВИДЕНДА, DIVIDENDA, DIVIDEND | Income from capital | 10% | Dividend income |
| АВТОРСКИ ПРАВА, ROYALTY | Copyright royalties | 10% on 50%-80% of gross | Normative costs of 50%, 40%, 30% or 20% by type of work [PIT Law art. 40] |
| ИНДУСТРИСКА СОПСТВЕНОСТ, PATENT, LICENCE FEE | Industrial-property rights | 10% on 90% of gross (base = 90%) | Normative costs of 10% [PIT Law art. 50] |
| ЗЕМЈОДЕЛСКИ ПРОИЗВОДИ, AGRICULTURAL SALE | Agricultural sales | 10% on 20% of gross (80% normative costs) | Own agricultural products: normative costs of 80% [PIT Law art. 44] |
| ИГРИ НА СРЕЌА, LOTARIJA, GAMES OF CHANCE, WINNINGS | Games of chance | 15% special rate | NOT 10% — special rate [PIT Law art. 11(2)] |
| ПОВРАТ НА ДАНОК, TAX REFUND | EXCLUDE | Not income | PRO refund from prior period |
| ГРАНТ, GRANT, SUBVENCIJA | Check nature | Capital grant EXCLUDE; revenue grant taxable | Confirm nature before classifying |

### 3.2 Expense / Deduction Patterns (Debits) -- Self-Employed Business Costs

For self-employed individuals taxed on net business income (tax balance), ordinary business costs reduce the net income before applying 10%. Match these as deductible business expenses.

### 3.2 Expense / Deduction Patterns (Debits) -- Self-Employed Business Costs

**3.2 Expense / Deduction Patterns (Debits) -- Self-Employed Business Costs**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| КАНЦЕЛАРИСКА КИРИЈА, OFFICE RENT | Office rent | Deductible business cost | Dedicated business premises |
| СМЕТКОВОДИТЕЛ, ACCOUNTANT, BOOKKEEP | Accountancy fees | Deductible business cost |  |
| АДВОКАТ, LAWYER, LEGAL (business) | Legal fees | Deductible business cost | Must be business-related |
| МАРКЕТИНГ, GOOGLE ADS, META ADS, ADVERTISING | Marketing/advertising | Deductible business cost |  |
| СОФТВЕР, SOFTWARE, GOOGLE WORKSPACE, MICROSOFT 365, ADOBE | Software subscription | Deductible business cost | Recurring subscription = operating expense |
| ANTHROPIC, OPENAI, GITHUB, AWS, HOSTING, DOMAIN | IT infrastructure | Deductible business cost |  |
| БАНКАРСКА ПРОВИЗИЈА, BANK FEE, CHARGE | Bank charges | Deductible business cost | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible business cost |  |
| ОБУКА, TRAINING, COURSE, SEMINAR, CONFERENCE | Training | Deductible business cost | Must relate to current business |

### 3.3 Expense Patterns (Debits) -- Mixed Use (Reviewer Judgement)

**3.3 Expense Patterns (Debits) -- Mixed Use (Reviewer Judgement)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ЕВН, EVN, ЕЛЕКТРИЧНА ЕНЕРГИЈА, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| МАКЕДОНСКИ ТЕЛЕКОМ, A1, TELEKOM, BROADBAND | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| МОБИЛЕН, MOBILE, A1 MOBILE | Phone | T2 | Business-use portion only |
| ГОРИВО, GORIVO, FUEL, OKTA, MAKPETROL, PETROL | Vehicle fuel | T2 — business % only | Requires mileage log |
| ПАРКИНГ, PARKING | Parking | T2 — business % only |  |

### 3.4 Expense Patterns (Debits) -- NOT Deductible / Not a Business Cost

**3.4 Expense Patterns (Debits) -- NOT Deductible / Not a Business Cost**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| РЕСТОРАН, RESTAURANT, ENTERTAINMENT, CLIENT MEAL | Entertainment | Reviewer judgement — default NOT deductible | Confirm wholly-and-exclusively basis |
| ЛИЧНО, PERSONAL, СУПЕРМАРКЕТ, SUPERMARKET, RAMSTORE | Personal expenses | NOT deductible | Private living costs |
| КАЗНА, KAZNA, FINE, PENALTY | Fines/penalties | NOT deductible | Public policy |
| ДАНОК, TAX PAYMENT, PIT PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| ПОДИГНУВАЊЕ, DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

### 3.5 Statutory Items (Neither ordinary income nor ordinary expense)

**3.5 Statutory Items (Neither ordinary income nor ordinary expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ПРИДОНЕСИ, PRIDONESI, SOCIAL CONTRIBUTIONS, ПИО, ФЗОМ | Social contributions (28%) | Deductible from the PIT base on employment income [Eurofast]; on salary, withheld via MPIN before PIT |
| INTERNAL TRANSFER, OWN ACCOUNT, СОПСТВЕНА СМЕТКА | EXCLUDE | Own-account transfer |
| КРЕДИТ, LOAN, ОТПЛАТА НА КРЕДИТ, LOAN REPAYMENT | EXCLUDE | Loan principal movement |
| ДДВ, DDV, VAT PAYMENT | EXCLUDE | VAT liability payment, not an income-tax expense |

### 3.6 Macedonian Banks -- Statement Format Reference

**3.6 Macedonian Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| NLB Banka | ТРАНСФЕР, УПЛАТА, ИСПЛАТА, ПРОВИЗИЈА | PDF/CSV; date format DD.MM.YYYY |
| Komercijalna Banka | TRANSFER, NALOG, NAKNADA | PDF; counterparty in description field |
| Stopanska Banka | УПЛАТА, ИСПЛАТА, ТРОШОК | PDF/CSV |
| Halkbank / Sparkasse / ProCredit | PAYMENT, TRANSFER, FEE | CSV available; clean counterparty names |
| Revolut / Wise (held by MK residents) | PAYMENT, TRANSFER, CONVERSION | CSV; multi-currency — use MKD-equivalent amounts |

## Section 4 -- Worked Examples

> All examples use the 2025 methodology: **monthly salary PIT = (gross − 28% social contributions − MKD 10,270 monthly tax reduction) × 10%** [Eurofast Payroll Guide 2025]. Each figure is recomputed end-to-end below.

### Example 1 -- Employee at the national average gross salary

**Input line:**
`25/03/2025 ; NLB PLATA ; DELOVNO DRUSTVO XYZ DOOEL ; PLATA MART ; +41,950.79 ; MKD`

**Reasoning:**
Gross salary MKD 63,154 (the 2025 average). Gross is above the floor (31,577) and below the ceiling (1,010,464), so contributions apply on the full gross.
- Social contributions: 63,154 × 28% = **MKD 17,683.12**
- After contributions: 63,154 − 17,683.12 = **MKD 45,470.88**
- Less tax reduction: 45,470.88 − 10,270 = **MKD 35,200.88** (PIT base)
- PIT at 10%: 35,200.88 × 0.10 = **MKD 3,520.09**
- Net pay: 45,470.88 − 3,520.09 = **MKD 41,950.79**

**Classification:** Contributions MKD 17,683.12; PIT MKD 3,520.09; net pay MKD 41,950.79. (Reconciles to the credit line.)

### Example 2 -- Minimum-wage employee

**Input line:**
`25/04/2025 ; KOMERCIJALNA ; FIRMA ABC ; NETO PLATA ; +24,378.98 ; MKD`

**Reasoning:**
Minimum gross wage MKD 36,037 (effective March 2025). Above the floor, below the ceiling.
- Social contributions: 36,037 × 28% = **MKD 10,090.36**
- After contributions: 36,037 − 10,090.36 = **MKD 25,946.64**
- Less tax reduction: 25,946.64 − 10,270 = **MKD 15,676.64** (PIT base)
- PIT at 10%: 15,676.64 × 0.10 = **MKD 1,567.66**
- Net pay: 25,946.64 − 1,567.66 = **MKD 24,378.98** ≈ MKD 24,379 (matches published minimum-wage net)

**Classification:** Contributions MKD 10,090.36; PIT MKD 1,567.66; net pay MKD 24,379.

### Example 3 -- Higher-paid employee (below the ceiling)

**Input line:**
`25/05/2025 ; STOPANSKA ; TECH DOO ; PLATA MAJ ; +78,787.00 ; MKD`

**Reasoning:**
Gross salary MKD 120,000. Still below the ceiling (1,010,464), so contributions on full gross.
- Social contributions: 120,000 × 28% = **MKD 33,600.00**
- After contributions: 120,000 − 33,600 = **MKD 86,400.00**
- Less tax reduction: 86,400 − 10,270 = **MKD 76,130.00** (PIT base)
- PIT at 10%: 76,130 × 0.10 = **MKD 7,613.00**
- Net pay: 86,400 − 7,613 = **MKD 78,787.00**

**Classification:** Contributions MKD 33,600; PIT MKD 7,613; net pay MKD 78,787.

### Example 4 -- Service-contract (договор на дело) income -- PIT only, no contributions

**Input line:**
`12/06/2025 ; NLB ; AGENCIJA MEDIA DOO ; HONORAR DOGOVOR NA DELO ; +45,000.00 ; MKD`

**Reasoning:**
Service-contract income paid by a legal entity to an individual is subject **only to PIT — no social contributions** [Eurofast Tax Card 2025]. The MKD 10,270 tax reduction does **not** apply (it covers only salary, wage compensation and pension; PIT Law art. 10(1)). The payer withholds/declares.
- PIT at 10%: 45,000 × 0.10 = **MKD 4,500.00**
- Net to individual: 45,000 − 4,500 = **MKD 40,500.00**

**Classification:** PIT MKD 4,500; no contributions; net MKD 40,500. A paying legal entity calculates, withholds and pays the PIT at each payment [PIT Law arts. 80, 92(1)]. Where the payer is a natural person, the recipient files a calculation by the 10th of the following month and pays by the 15th [PIT Law arts. 88(1)(7), 93(1)].

### Example 5 -- Self-employed annual net business income

**Input:** Self-employed individual keeping accounting records; annual net income (tax balance) for 2025 = MKD 800,000.

**Reasoning:**
Self-employment / business income is taxed at the flat 10% on net income from the tax balance [PIT Law arts. 11(1), 37]. A presumptive regime exists for those who cannot keep books (see 5.7); this example assumes the client keeps accounting records. Contributions are computed separately on a contribution base capped at the self-employed maximum (MKD 757,848/month).
- Annual PIT: 800,000 × 0.10 = **MKD 80,000.00**

Filing: annual accounts + tax balance by **15 March** of the following year; any balance of tax due within **15 days** after that deadline; monthly advance payments equal one-twelfth of the prior year's liability [PIT Law arts. 94(1), 97, 100(1)].

**Classification:** Annual PIT MKD 80,000 (excl. social contributions, computed separately).

### Example 6 -- Games-of-chance winnings (special 15% rate)

**Input line:**
`30/07/2025 ; HALKBANK ; LOTARIJA NA MK ; DOBIVKA IGRI NA SREKA ; +100,000.00 ; MKD`

**Reasoning:**
Gains from games of chance are taxed at the **special 15% rate**, not 10% [PIT Law art. 11(2)].
- PIT at 15%: 100,000 × 0.15 = **MKD 15,000.00**

**Classification:** PIT MKD 15,000 at the games-of-chance rate. Do NOT apply 10% and do NOT apply the salary exemption.

### Example 7 -- Salary above the contribution ceiling

**Input:** Gross monthly salary MKD 1,200,000 (above the employee ceiling base of MKD 1,010,464).

**Reasoning:**
Contributions are capped: they apply only on the ceiling base, not the full gross.
- Contributions: 1,010,464 × 28% = **MKD 282,929.92** (capped)
- After contributions: 1,200,000 − 282,929.92 = **MKD 917,070.08**
- Less tax reduction: 917,070.08 − 10,270 = **MKD 906,800.08** (PIT base)
- PIT at 10%: 906,800.08 × 0.10 = **MKD 90,680.01**
- Net pay: 917,070.08 − 90,680.01 = **MKD 826,390.07**

**Classification:** Contributions MKD 282,929.92 (capped at the ceiling); PIT MKD 90,680.01; net pay MKD 826,390.07. Note PIT itself is NOT capped — only the contribution base is.

### 5.1 The Flat 10% Rule

- **The Flat 10% Rule** — PIT is a flat 10% on virtually all income types — employment, self-employment/business, rental, capital (dividends/interest), taxable capital gains, royalties, agricultural sales, insurance, and other uncategorised income — for tax year 2025 [PIT Law art. 11(1)]. Two special rates override the flat rate: 15% on games-of-chance gains [art. 11(2)] and 70% on undeclared income [art. 78].  _(Law on Personal Income Tax (Official Gazette 241/2018 and amendments))_

### 5.2 Gross-to-Net Salary Computation

- **Order of operations for salary** — 1. Start from gross salary (бруто плата). 2. Deduct 28% social contributions (on gross between floor and ceiling). 3. Deduct the MKD 10,270 monthly tax reduction. 4. Apply 10% PIT to the remainder (the PIT base). 5. Net pay = gross − contributions − PIT. All payments (net wage, contributions, PIT) are remitted concurrently via a single encrypted payment order — the MPIN salary declaration [Eurofast].  _(Law on Mandatory Social Insurance Contributions; Eurofast Payroll Guide 2025)_

### 5.3 Social Contributions

- **Social Contributions rule** — Total mandatory contributions are 28% of gross salary (pension/disability 18.8%, health 7.5%, unemployment 1.2%, additional/disability 0.5%), all borne by the employee and withheld/remitted by the employer; there is no separate employer-side contribution [Contributions Law art. 25(1); Eurofast Tax Card 2025]. Contributions are levied on gross salary between a floor of MKD 31,577/month (50% of the average salary, art. 15(1)) and a ceiling of MKD 1,010,464/month (16 average salaries, art. 16(1)) for 2025 [amounts per Bloomberg Tax citing PRO]. For self-employed persons the maximum contribution base is MKD 757,848/month (12 average salaries, art. 16(3)). Contributions on employment income are fully deductible when computing the PIT base [Eurofast Tax Card 2025].  _(Law on Mandatory Social Insurance Contributions)_

### 5.4 The Tax Reduction (salary, wage compensation and pension)

- **Tax reduction rule** — The tax reduction (даночно намалување) is deducted from the PIT base on salary, wage compensation and pension only [PIT Law arts. 9, 10(1)]. The law set it at MKD 96,000 a year, indexed each year by 50% of the growth in the average gross salary; the Minister of Finance publishes the next year's amount by 31 December [art. 10(2)-(4)], and each monthly payroll uses one-twelfth of it [art. 17(2)]. The 2025 monthly amount is MKD 10,270 [Eurofast Tax Card 2025]. Do not apply it to service contracts, business income, rental, or other categories (see Conservative Defaults).  _(PIT Law arts. 10, 17; Eurofast Tax Card 2025)_

### 5.5 Income-Category Base Reductions

**5.5 Income-Category Base Reductions**  _(Law on Personal Income Tax)_

| Income category | Base | Source |
| --- | --- | --- |
| Sale of own agricultural products | Normative costs of 80% (base = 20% of gross) | PIT Law art. 44 |
| Copyright royalties | Normative costs of 50% (sculpture, tapestry, ceramics, stained glass), 40% (photography, painting, design and similar), 30% (scientific, professional and journalistic works, serious-music, ballet, opera and acting performances) or 20% (translations, lectures and other works); base = 50%-80% of gross | PIT Law art. 40 |
| Industrial-property rights | Normative costs of 10% (base = 90% of gross) | PIT Law art. 50 |
| Unfurnished property lease | 10% deduction from gross rent | PIT Law art. 53(1) |
| Furnished property lease | 15% deduction from gross rent | PIT Law art. 53(2) |

### 5.5 Income-Category Base Reductions

- **Mutual exclusivity note** — Apply 10% PIT to the reduced base. Do not stack the salary exemption on top of these — they are mutually exclusive categories.  _(Law on Personal Income Tax)_

### 5.6 Capital Gains

- **Capital Gains rule** — Taxable capital gains are taxed at 10% [PIT Law art. 11(1)]. Exempt: capital gains on securities and investment-fund shares held longer than two years [art. 12(1)(39-а)], and gains on securities and fund shares are taxable only for holdings acquired from 1 January 2023 [Official Gazette 274/2022 art. 21]. A home lived in for at least a year and sold more than three years after acquisition is exempt [art. 63]. Interest on term deposits is not taxed until EU accession [art. 116].  _(Law on Personal Income Tax)_

### 5.7 Self-Employed / Business Income

- **Self-Employed / Business Income rule** — Self-employed individuals who keep accounting records are taxed at 10% on net income from the tax balance. They file annual accounts and a tax balance by 15 March of the following year and pay any balance within 15 days after that deadline; monthly advance payments equal one-twelfth of the prior year's liability (January and February use the balance for the year before) [PIT Law arts. 94, 97, 100(1)]. A self-employed person who cannot keep books, or for whom bookkeeping would seriously hinder the activity, may ask the PRO each year (by the end of the preceding year) to tax a presumptive net income set by resolution; the regime is closed to trade, catering and commission activities (except green-market sellers), to anyone employing more than one person or with outside investors, and to those whose prior-year net income exceeded two annual average gross salaries [PIT Law art. 29].  _(Law on Personal Income Tax)_

### 5.8 Registration & VAT Interaction

**5.8 Registration & VAT Interaction**

| Trigger | Requirement | Source |
| --- | --- | --- |
| Income from selling own agricultural products > MKD 1,000,000 a year | Register an activity by 15 January of the following year | PIT Law art. 45 |
| Turnover > MKD 2,000,000 (prior year or expected) | VAT registration required | Company Formation Macedonia |
| VAT return (DDV-04) | File within 25 days after period end; pay within 30 days | Company Formation Macedonia |

### 5.8 Registration & VAT Interaction

- **VAT net income note** — For VAT-registered self-employed clients, report business income net of VAT (VAT collected is a liability, not income).

### 5.9 Filing & Deadlines

**5.9 Filing & Deadlines**

| Item | Detail | Source |
| --- | --- | --- |
| Annual draft return (pre-filled by PRO) | PRO delivers draft by 30 April; taxpayer confirms/corrects by 31 May; if no action, it is treated as confirmed; tax due by 30 June | PIT Law arts. 96, 100(2) |
| Self-employed annual accounts + tax balance | 15 March of the following year; balance due within 15 days after that deadline | PIT Law arts. 97, 100(1) |
| Self-assessed monthly PIT (rent, capital gains, foreign income, services to natural persons) | File by the 10th of the following month; pay by the 15th (payers who withhold pay at each payment) | PIT Law arts. 88(1), 92(1), 93(1) |
| MPIN salary declaration | Submitted concurrently with monthly net-salary payment | Eurofast Payroll Guide 2025 |
| Foreign salary or pension taxed abroad | Report by 31 March of the following year | PIT Law art. 88(2) |
| VAT return (DDV-04) | Within 25 days after period; VAT paid within 30 days | Company Formation Macedonia |

### 5.10 Assessments & Penalties

**5.10 Assessments & Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| PRO assessment after the return | A resolution is issued; the difference is payable within 15 days of delivery | PIT Law arts. 99, 100(3) |
| Fines | EUR 100-250 (in denars) for a sole trader or self-employed person who misses the calculation or tax balance deadline or fails to keep books for five years, plus a possible 3-30 day ban on the activity; EUR 50-250 for an individual who fails to file a calculation | PIT Law art. 107 |

### 6.1 Home Office / Mixed-Use Premises (self-employed)

- Calculate the proportion of the home used for business and apply it to utilities, rent, and internet.
- Must be a genuinely dedicated workspace.
- **Conservative default:** 0% deduction until the reviewer confirms the arrangement.
- **Flag for reviewer:** Confirm the floor-area basis and that the workspace is dedicated.

### 6.2 Motor Vehicle Business Use (self-employed)

- Only the business-use percentage of fuel, insurance, and maintenance is deductible; requires a mileage log.
- **Conservative default:** 0% business use until a mileage log is provided.

### 6.3 Phone / Internet Mixed Use

- Business-use portion only; client must give a reasonable estimate.
- **Conservative default:** 0% deduction until the business percentage is confirmed.

### 6.4 Income Categorisation (which rate / which reduction)

- Whether a receipt is salary, service-contract income, business income, rental, royalty, or "other" changes the rate base, whether the MKD 10,270 exemption applies, and whether contributions are due.
- **Flag for reviewer:** Confirm the legal category of each material receipt before applying a reduction or exemption.

### 6.5 Entertainment / Client Hospitality (self-employed)

- North Macedonia's specific deductibility limits for entertainment were not pinned to an authoritative figure **[RESEARCH GAP — reviewer to confirm]**.
- **Conservative default:** Treat as NOT deductible until the reviewer confirms the wholly-and-exclusively basis.

### 6.6 Contribution Base Floor/Ceiling Edge Cases

- For very low salaries (below the MKD 31,577 floor) contributions may be computed on the floor base rather than actual gross.
- **Conservative default:** Apply the floor base where gross < floor; flag for reviewer.

### 6.7 Allowance-Style Base Reductions

- Agricultural (80% normative costs, base 20%), copyright (20%-50%), industrial-property rights (base 90%) and lease (10%/15%) reductions depend on correct categorisation and documentation.
- **Flag for reviewer:** Confirm category and supporting evidence before applying a reduction.

## Section 7 -- Excel Working Paper Template

```
NORTH MACEDONIA PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Resident: Yes / No
Computation type: Salary (gross-to-net) / Service contract / Self-employed / Other

-------------------------------------------------------------
PART A -- MONTHLY SALARY (gross-to-net)
  A1. Gross salary (MKD)                          ___________
  A2. Contribution base (A1, capped 31,577..1,010,464) _______
  A3. Social contributions = A2 x 28%             ___________
        Pension/disability 18.8%   ____________
        Health 7.5%                ____________
        Unemployment 1.2%          ____________
        Additional/disability 0.5% ____________
  A4. Salary after contributions (A1 - A3)        ___________
  A5. Tax reduction (salary/pension)                ( 10,270  )
  A6. PIT base (A4 - A5)                           ___________
  A7. PIT = A6 x 10%                               ___________
  A8. NET PAY (A4 - A7)                            ___________

-------------------------------------------------------------
PART B -- SERVICE CONTRACT (договор на дело)
  B1. Gross fee (MKD)                              ___________
  B2. PIT = B1 x 10%   (NO contributions, NO exemption) ______
  B3. Net to individual (B1 - B2)                  ___________

-------------------------------------------------------------
PART C -- SELF-EMPLOYED (annual)
  C1. Net business income (tax balance)            ___________
  C2. Annual PIT = C1 x 10%                         ___________
  C3. Contributions (separate, base capped 757,848/mo) _______
  C4. Monthly advance = prior-year liability / 12  ___________

-------------------------------------------------------------
PART D -- OTHER CATEGORY INCOME (apply base reduction first)
  D1. Rental (less 10% unfurnished / 15% furnished) _________
  D2. Copyright (base = 50%-80% of gross, art. 40) / industrial property (base = 90%) ___
  D3. Agricultural (base = 20% of gross)           ___________
  D4. Games of chance (rate = 15%, not 10%)        ___________
  D5. PIT on D1-D3 = base x 10%; on D4 = base x 15% ________

REVIEWER FLAGS:
  [ ] Gross vs net of salary confirmed?
  [ ] Income category confirmed for each receipt?
  [ ] Tax reduction applied to salary or pension ONLY?
  [ ] Contributions capped at correct ceiling (employee vs self-employed)?
  [ ] Base reductions (agri/IP/lease) supported by evidence?
  [ ] Games-of-chance at 15% (not 10%)?
  [ ] VAT-registered? Income reported net of VAT?
  [ ] Service-contract income carries PIT only (no contributions)?
  [ ] RESEARCH GAP items reconfirmed against UJP?
```

## Section 8 -- Bank Statement Reading Guide

### Macedonian Bank Statement Formats

**Macedonian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| NLB Banka | PDF, CSV | Датум (Date), Опис (Description), Задолжување (Debit), Одобрување (Credit), Состојба (Balance) | Most common; description contains counterparty + reference |
| Komercijalna Banka | PDF, CSV | Date, Description, Amount, Balance | Counterparty in description field |
| Stopanska Banka | PDF | Датум, Опис, Износ | Shorter descriptions |
| Halkbank / ProCredit / Sparkasse | PDF, CSV | Date, Description, Amount, Balance | CSV export available |
| Revolut / Wise (MK resident) | CSV | Date, Counterparty, Amount, Currency, Reference | Multi-currency — use MKD-equivalent |

### Key Macedonian Banking & Tax Terms

**Key Macedonian Banking & Tax Terms**

| Term (Macedonian) | Transliteration | English | Classification Hint |
| --- | --- | --- | --- |
| Бруто плата | Bruto plata | Gross salary | Starting point for gross-to-net |
| Нето плата | Neto plata | Net salary | Amount that hits the account |
| Придонеси | Pridonesi | Contributions | The 28% social contributions |
| Данок на личен доход | Danok na licen dohod | Personal income tax | The PIT |
| Хонорар / Договор на дело | Honorar / Dogovor na delo | Fee / Service contract | PIT only, no contributions |
| Кирија / Закуп | Kirija / Zakup | Rent / Lease | Rental income (base reduction) |
| Камата | Kamata | Interest | Income from capital |
| Дивиденда | Dividenda | Dividend | Income from capital |
| Авторски права | Avtorski prava | Copyright royalties | Base = 50%-80% of gross by type of work |
| Игри на среќа | Igri na sreka | Games of chance | Special 15% rate |
| Провизија / Трошок | Provizija / Trošok | Fee / Charge | Bank charge (business cost) |
| Уплата / Исплата | Uplata / Isplata | Inbound / Outbound payment | Check direction for income/expense |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement or salary figure but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1) — including treating ambiguous receipts as "other income" at 10% with no exemption.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- NORTH MACEDONIA PERSONAL INCOME TAX
1. Is the salary figure GROSS (бруто) or NET (нето)?
2. Employment status: employee (MPIN salary), service contract (договор на дело), or self-employed with accounting records?
3. For each material receipt: which category — salary, service contract, business, rental, royalty, agricultural, capital, capital gain, or games of chance?
4. Are you VAT-registered (turnover > MKD 2,000,000)?
5. Self-employed: what is the net business income (tax balance) for the year, and what was the prior-year liability (for monthly advances)?
6. Home office / vehicle / phone: any business-use percentage you can document?
7. Did income from selling your own agricultural products exceed MKD 1,000,000 (registration trigger)?
8. Any income from abroad (foreign salary or pension taxed abroad is reportable by 31 March)?
9. Any games-of-chance winnings (taxed at 15%)?
```

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References**

| Topic | Reference | Source |
| --- | --- | --- |
| PIT rates & categories | Law on Personal Income Tax (Official Gazette 241/2018 as amended to 274/2022), arts. 3, 11, 12, 78 | Ministry of Finance unofficial consolidated text (finance.gov.mk, Laws and regulations, Taxes) |
| Social contributions | Law on Mandatory Social Insurance Contributions (Official Gazette 142/2008 as amended to 247/2018), arts. 15, 16, 18, 24, 25 | Public Revenue Office unofficial consolidated text |
| Income determination / base reductions | Law on Personal Income Tax, arts. 10, 29, 40, 44, 50, 53 | Ministry of Finance unofficial consolidated text |
| Filing & administration | Law on Personal Income Tax, arts. 80, 88, 92-100, 107 | Ministry of Finance unofficial consolidated text |
| VAT | Law on Value Added Tax | Company Formation Macedonia |
| Minimum wage | Labour Relations Law (Official Gazette 62/05 & amendments) | Pepeljugoski law office |
| Tax authority | Public Revenue Office (UJP / PRO), www.ujp.gov.mk | UJP |
| Policy | Ministry of Finance, finance.gov.mk | Ministry of Finance |

### Primary sources

- Law on Personal Income Tax (Закон за данокот на личен доход), Official Gazette 241/2018, 275/2019, 290/2020, 85/2021 and 274/2022, unofficial consolidated text (scanned PDF): https://portal.mdt.gov.mk/post-body-files/propisi-od-oblasta-na-danocite-taksite-i-drugite-javni-prixodi-file-Rpj2.pdf, listed on the Ministry of Finance's tax-laws page https://finance.gov.mk/mk-MK/zakoni-i-propisi/danoci
- Law on Mandatory Social Insurance Contributions (Закон за придонеси од задолжително социјално осигурување), Official Gazette 142/2008 as amended to 247/2018, the Public Revenue Office's unofficial consolidated text (the copy read is hosted by the Economic Chamber of North Macedonia because ujp.gov.mk returned HTTP 502 on 8 October 2026): https://mchamber.mk/Upload/Editor_Upload//%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%BF%D1%80%D0%B8%D0%B4%D0%BE%D0%BD%D0%B5%D1%81%D0%B8%20%D0%BE%D0%B4%20%D0%B7%D0%B0%D0%B4%D0%BE%D0%BB%D0%B6%D0%B8%D1%82%D0%B5%D0%BB%D0%BD%D0%BE%20%D1%81%D0%BE%D1%86%D0%B8%D1%98%D0%B0%D0%BB%D0%BD%D0%BE%20%20%D0%BE%D1%81%D0%B8%D0%B3%D1%83%D1%80%D1%83%D0%B2%D0%B0%D1%9A%D0%B5%20%D0%A3%D0%88%D0%9F.pdf
- Law on Tax Procedure (Закон за даночна постапка), Official Gazette 13/2006 as amended to 35/2018, Ministry of Finance unofficial consolidated text: https://portal.mdt.gov.mk/post-body-files/propisi-od-oblasta-na-danocite-taksite-i-drugite-javni-prixodi-file-HwLH.pdf

### Key 2025 Figures (with provenance)

**Key 2025 Figures (with provenance)**

| Figure | Value | Source |
| --- | --- | --- |
| Flat PIT rate | 10% | PIT Law art. 11(1) |
| Games-of-chance rate | 15% | PIT Law art. 11(2) |
| Undeclared-income rate | 70% | PIT Law art. 78 |
| Total social contributions | 28% (18.8 + 7.5 + 1.2 + 0.5) | Contributions Law art. 25(1) |
| National average gross salary | MKD 63,154/month | Bloomberg Tax citing PRO; Eurofast |
| Contribution floor | MKD 31,577/month | Bloomberg Tax citing PRO |
| Contribution ceiling (employees) | MKD 1,010,464/month | Bloomberg Tax citing PRO |
| Contribution ceiling (self-employed) | MKD 757,848/month | Bloomberg Tax citing PRO |
| Monthly tax reduction (salary and pension) | MKD 10,270/month | Eurofast Tax Card 2025 (PIT Law arts. 10, 17) |
| Minimum gross wage (Mar 2025) | MKD 36,037/month (net ≈ 24,379) | Pepeljugoski law office |
| Registration threshold (own agricultural products) | MKD 1,000,000 annual income | PIT Law art. 45 |
| VAT registration threshold | MKD 2,000,000 turnover | Company Formation Macedonia |

### Research Caveats

- The rates, multipliers, normative costs, deadlines and fines cite the two laws' unofficial consolidated texts (PIT Law to Official Gazette 274/2022, Contributions Law to 247/2018); amendments after those dates were not traced. The PRO's site (ujp.gov.mk) returned HTTP 502 on 8 October 2026, and the Ministry of Finance's PIT text is a scan read by OCR.
- The MKD 10,270 tax reduction, MKD 63,154 average salary and the MKD 31,577 / 1,010,464 / 757,848 amounts come from the Eurofast Tax Card 2025 and Bloomberg Tax (reporting the PRO's January 2025 clarification). The bases are the statutory multiples of that average (Contributions Law arts. 15-16). **Reconfirm the amounts against the Ministry of Finance's annual tax-reduction notice and the State Statistical Office release before publication.**
- The 0.5% component is the additional health contribution for injury at work and occupational disease (Contributions Law art. 25(1)(7)); Eurofast labels it "disability". Both agree on 0.5% and a 28% total.
- Minimum wage MKD 36,037 was effective from March 2025; a further revision took effect 1 March 2026 (out of scope for the 2025 skill).
- Overall research confidence: **medium**.

### Test Suite

**Test 1 -- Average-salary employee.**
Input: Gross MKD 63,154/month, employee.
Expected: Contributions = 17,683.12 (63,154 × 0.28); after-contributions 45,470.88; PIT base 35,200.88 (− 10,270); PIT 3,520.09; net pay 41,950.79.

**Test 2 -- Minimum-wage employee.**
Input: Gross MKD 36,037/month, employee.
Expected: Contributions = 10,090.36; after-contributions 25,946.64; PIT base 15,676.64; PIT 1,567.66; net pay 24,378.98 (≈ 24,379).

**Test 3 -- Higher-paid employee (below ceiling).**
Input: Gross MKD 120,000/month.
Expected: Contributions = 33,600.00; after-contributions 86,400.00; PIT base 76,130.00; PIT 7,613.00; net pay 78,787.00.

**Test 4 -- Salary above the contribution ceiling.**
Input: Gross MKD 1,200,000/month.
Expected: Contributions capped = 1,010,464 × 0.28 = 282,929.92; after-contributions 917,070.08; PIT base 906,800.08; PIT 90,680.01; net pay 826,390.07. (PIT is NOT capped; only the contribution base is.)

**Test 5 -- Service contract.**
Input: Service-contract fee MKD 45,000 from a legal entity.
Expected: PIT = 4,500 (10%); NO social contributions; NO MKD 10,270 exemption; net 40,500.

**Test 6 -- Self-employed annual.**
Input: Net business income MKD 800,000.
Expected: Annual PIT = 80,000 (10%); contributions computed separately on a base capped at MKD 757,848/month; advances = prior-year liability ÷ 12.

**Test 7 -- Games of chance (special rate).**
Input: Winnings MKD 100,000.
Expected: PIT = 15,000 (15%, not 10%); no exemption.

**Test 8 -- Wrong rate applied (negative test).**
Input: An agent computes games-of-chance winnings at 10%.
Expected: REJECT. Games of chance are 15% [PIT Law art. 11(2)]. Recompute at 15%.

**Test 9 -- Exemption misapplied (negative test).**
Input: An agent deducts the MKD 10,270 exemption from service-contract income.
Expected: REJECT. The tax reduction applies only to salary, wage compensation and pension; service-contract income gets neither contributions nor the reduction.

## PROHIBITIONS

- NEVER compute a salary net figure without confirming the input is GROSS, not net
- NEVER apply the MKD 10,270 tax reduction to anything other than salary, wage compensation or pension
- NEVER add a separate employer-side social contribution — North Macedonia has none; the full 28% is on the employee
- NEVER apply 10% to games-of-chance winnings — they are taxed at 15%
- NEVER self-classify undeclared income (70%) — escalate
- NEVER apply social contributions to service-contract (договор на дело) income — it is PIT-only
- NEVER cap the PIT itself at the contribution ceiling — only the contribution base is capped
- NEVER stack a category base reduction (agri/IP/lease) on top of the salary exemption — categories are mutually exclusive
- NEVER report VAT collected as income for VAT-registered self-employed clients
- NEVER present a figure marked [RESEARCH GAP] as confirmed — flag it for the reviewer
- NEVER present tax calculations as definitive — always label as estimated

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
