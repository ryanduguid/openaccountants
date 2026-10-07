---
name: kosovo-income-tax
description: Use this skill whenever asked about Kosovo personal income tax for self-employed individuals and individuals. Trigger on phrases like "how much tax do I pay in Kosovo", "tatimi mbi te ardhurat personale", "ATK declaration", "TAK return", "annual personal income tax return", "PD form", "quarterly advance payment", "gross-income method", "real-income method", "self-employed tax Kosovo", "Trusti pension contribution", "wage withholding Kosovo", "EDI declaration", or any question about filing or computing personal income tax for a self-employed or employed individual in Kosovo. Also trigger when preparing or reviewing a Kosovo annual PD return, quarterly advance instalment, payroll withholding, computing deductible business expenses, or advising on the gross-income vs real-income method. This skill covers the graduated PIT rates (0%/8%/10%), the self-employed gross-income (3%/9%) and real-income (net profit at the graduated rates) methods, mandatory pension contributions (Trusti/KPST), payroll withholding, penalties, and interaction with VAT. ALWAYS read this skill before touching any Kosovo income tax work.
version: 0.2
jurisdiction: XK
tax_year: 2025
last_updated: 2026-10-08
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kosovo Personal Income Tax -- Self-Employed and Individuals

## Kosovo Personal Income Tax -- Self-Employed and Individuals Skill v0.2

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Kosovo (Republika e Kosoves / Republika Kosovo) |
| ISO code | XK (ISO 3166-1 user-assigned code; Kosovo lacks a universally assigned 2-letter code) [caveat: research] |
| Tax | Personal Income Tax (Tatimi mbi te Ardhurat Personale / TAP) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) [[Law No. 05/L-028](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) art. 2(1.27)] |
| Primary legislation | **Law No. 05/L-028 on Personal Income Tax** (Official Gazette, published 14 August 2015), as amended by Law No. 08/L-142 (Official Gazette 18/2024, published and in force 23 August 2024). The amending law's own record on the Official Gazette lists the five laws it amends, and 05/L-028 is the tax one — [gzk.rks-gov.net](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360). **Law No. 08/L-110, cited here previously, is the Law on the Kosovo Accreditation Agency and has nothing to do with tax** |
| Supporting legislation | [Law No. 06/L-105 on Corporate Income Tax](https://www.atk-ks.org/wp-content/uploads/2019/09/LAW_NO.06_L-105.pdf); [Law No. 04/L-101 on Pension Funds of Kosovo](https://www.atk-ks.org/wp-content/uploads/2017/07/Law-No.-04-L-101.pdf), as amended by Laws No. 04/L-115, 04/L-168 and 05/L-116; [Law No. 05/L-037 on VAT](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf); [Law No. 08/L-257 on the Administration of Tax Procedures](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) (adopted 14 December 2023; art. 122 repeals Law No. 03/L-222 and its amendments) |
| Tax authority | Tax Administration of Kosovo (Administrata Tatimore e Kosoves, ATK/TAK) -- atk-ks.org |
| Filing portal | ATK EDI e-filing portal (edideklarimi.atk-ks.org) |
| Pension administrator | Kosovo Pensions Savings Trust (Trusti / KPST, trusti.org), under the BQK/CBK framework |
| Annual filing deadline | 31 March of the year following the tax year (form PD) [Law No. 05/L-028 art. 48(1)] |
| Quarterly advance deadlines | 15 days after each calendar quarter ends: 15 April, 15 July, 15 October, 15 January [Law No. 05/L-028 art. 43(1)] |
| Validated by | Pending -- requires sign-off by a Kosovo-licensed tax adviser / accountant |
| Validation date | Pending |
| Skill version | 0.2 |

### Tax Rate Brackets -- Personal Income Tax (annual, 2025/2026)

**Tax Rate Brackets -- Personal Income Tax (annual, 2025/2026)**  _(Law No. 05/L-028 art. 6, as replaced by [Law No. 08/L-142 art. 5, quoted in TAK's notice of 27 August 2024](https://www.atk-ks.org/en/notice-to-taxpayers-personal-income-tax-rates-are-changed/): 0% to EUR 3,000; 8% of the excess to EUR 5,400; EUR 192 plus 10% of the excess above EUR 5,400)_

| Annual taxable income (EUR) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0.00 -- 3,000.00 | 0% | EUR 0.00 |
| 3,000.01 -- 5,400.00 | 8% | EUR 192.00 |
| 5,400.01 and above | 10% | -- |

Brackets are stated as **annual** amounts in the law. ATK applies them via monthly cumulative withholding for primary-employer wages. Rates in force from 23 August 2024 under Law No. 08/L-142, the day of its publication (TAK notice above); TAK's laws page (atk-ks.org/en/legislation/laws/, read 8 October 2026) lists no later personal income tax law, so the same rates apply for 2025 and 2026. They replaced the 0%/4%/8%/10% schedule of the original art. 6 (EUR 960 / 3,000 / 5,400).

**Arithmetic note (verified):** Tax at top of the 8% band = (5,400 - 3,000) x 8% = 2,400 x 8% = EUR 192.00. Above EUR 5,400, tax = EUR 192.00 + 10% x (income - 5,400.00).

**Kosovo has no standard deduction and no personal/family allowance -- the first EUR 3,000 (0% band) IS the only general relief.** Law No. 05/L-028 defines taxable income as gross income less the deductions it allows (art. 5); those deductions are business, rental and intangible-property expenses (arts. 15 to 30), and the law grants no personal or family allowance.

**Secondary-employer wages** are taxed at a **flat 10%** with no 0%/8% bands: the principal employer withholds at the art. 6 rates, and any other employer withholds 10% of the wages for each period (Law No. 05/L-028 art. 38(2) and (3)).

### Self-Employed Taxation Methods

**Self-Employed Taxation Methods**

| Method | Eligibility | Rate | Reference |
| --- | --- | --- | --- |
| Gross-income (turnover) method -- trade | Annual gross income up to EUR 50,000 (PIT Law 05/L-028; see the note below on the three thresholds) | 3% of gross receipts (trade, transport, agriculture and similar) | Law No. 05/L-028 art. 43(2.1.1) |
| Gross-income (turnover) method -- services | Annual gross income up to EUR 50,000 (PIT Law 05/L-028; see the note below on the three thresholds) | 9% of gross receipts (services, professional, vocational, entertainment and similar) | Law No. 05/L-028 art. 43(2.1.2) |
| Real-income method | Annual gross income over EUR 50,000 (mandatory), or elected voluntarily below the threshold | Net taxable profit (gross income less allowable expenses) taxed at the art. 6 graduated rates (0% / 8% / 10%), together with the taxpayer's other taxable income | Law No. 05/L-028 arts. 5, 6, 33(1) and (2) and 48(1) |
| Minimum quarterly payment (gross-income method) | Applies under the gross-income method | EUR 37.50 per quarter; no payment is due for a quarter with no income, but the quarterly declaration is still filed | Law No. 05/L-028 art. 43(2.1.1) to (2.1.3) |

Version 0.1 of this guide applied a flat 10% to real-income profit. Law No. 05/L-028 has no separate business rate: the annual declaration computes "the tax due pursuant to Article 6" on taxable income from all sources (art. 48(1)), so profit is taxed at the graduated rates and the effective rate stays below 10%.

> **Resolved.** Kosovo has three thresholds that are easy to run together, and they are three different numbers in three different laws:
>
> - **EUR 50,000** — the gross-income-method ceiling for an individual under the **Personal Income Tax** Law (05/L-028 arts. 33(1) and 43(2) and (3)). Above it, the real-income method at the progressive rates is mandatory for that period and at least three further periods. This is the one that governs this guide.
> - **EUR 30,000** — the flat gross-receipts threshold for small taxpayers under the **Corporate Income Tax** Law (06/L-105 arts. 35(1) and 38(2.1), dated 27 June 2019), which *reduced* it from EUR 50,000. The old corporate figure and the current personal one are both 50,000, which is how the two get conflated.
> - **EUR 30,000** — **VAT** registration (Law 05/L-037 art. 6(1)), unrelated to either.
>
> The earlier note here sent a reviewer to "the consolidated text of PIT Law No. 08/L-110" to settle it. That law is the Kosovo Accreditation Agency Act.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Residency status unknown | STOP -- do not compute without confirming Kosovo tax residency (worldwide vs Kosovo-source) |
| Self-employed activity ambiguous between trade (3%) and services (9%) | Apply 9% services rate (conservative) |
| Annual gross income exceeds EUR 50,000 | Real-income method (net profit at the graduated rates) -- mandatory above threshold (PIT Law 05/L-028 art. 33(1)) |
| Secondary employment | Withhold flat 10% (no 0%/8% bands) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| High wage (any amount) | Compute the 5% + 5% pension on the full gross wage: Law No. 04/L-101 art. 6.2 sets no ceiling (see 5.6) |
| Unknown VAT registration status | Assume not registered until turnover/registration confirmed |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) Kosovo tax residency, (b) employment vs self-employed status, and (c) for self-employed, the taxation method (gross-income 3%/9% or real-income at the graduated rates).

**Recommended** -- all sales invoices, purchase invoices/receipts, Trusti/KPST pension contribution records, prior-year PD return or ATK assessment, VAT registration status, payroll WM/WR records if an employer.

**Ideal** -- complete income and expenditure account, fixed-asset register, quarterly advance-payment confirmations (QS/QL), employment-income certificates, evidence of activity classification (trade vs services).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This Kosovo PIT computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation, that the correct taxation method (gross-income vs real-income) was applied, and that pension contributions reconcile to Trusti/KPST records."

### Refusal Catalogue

- **R-XK-1 -- Residency unknown** — Residents are taxed on worldwide income; non-residents only on Kosovo-source income. A natural person is resident with a principal residence in Kosovo or 183 days' presence in any twelve-month period. This skill cannot compute tax without confirming Kosovo tax residency. Please confirm before proceeding.  _(Law No. 05/L-028 arts. 2(1.18) and 4)_
- **R-XK-2 -- Companies / partnerships** — This skill covers individuals and self-employed sole proprietors only. Corporate income tax (Law No. 06/L-105), partnerships, and group structures file separately. Escalate to a Kosovo-licensed accountant.  _(Law No. 06/L-105)_
- **R-XK-3 -- Cross-border / treaty** — Non-resident and treaty-relief taxation, foreign tax credits, and permanent-establishment analysis are out of scope. Escalate to a Kosovo-licensed accountant.
- **R-XK-4 -- Capital gains / property disposals** — Capital gains and immovable-property disposal computations require specialised analysis. Escalate to a Kosovo-licensed accountant.
- **R-XK-5 -- Arrears / enforcement** — Client has outstanding tax arrears or is subject to ATK enforcement. Late-payment interest accrues monthly up to ten years (Law No. 08/L-257 art. 24) and understatement fines are 15% or 25% of the shortfall (art. 100). Do not advise. Escalate to a Kosovo-licensed accountant immediately.
- **R-XK-6 -- VAT return requested** — This skill covers personal income tax only. For Kosovo VAT (standard 18%, reduced 8%; registration above EUR 30,000 turnover), use a dedicated Kosovo VAT skill.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. Albanian terms are shown alongside English equivalents.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFER, DEPOZITE, PAGESE, PAYMENT RECEIVED | Business income (gross receipts) | If VAT-registered, extract net (excl. 18% VAT) |
| HONORAR, FATURA, FEES, CONSULTANCY, KESHILLIM | Business income | Professional/consultancy fees -- self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Platform payout -- match to invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Business income | Platform payout -- verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Business income | International platform payout |
| UPWORK, FIVERR, TOPTAL | Business income | Freelance platform -- net of platform commission |
| PAGA, RROGA, SALARY, EMPLOYER [name] | Employment income | Primary vs secondary employment matters for withholding |
| QIRA, RENT RECEIVED | Rental income | Taxed as rental income (see 5.7) |
| INTERES, INTEREST RECEIVED | Investment income | Interest on instruments issued or guaranteed by a Kosovo public authority is EXEMPT [Law No. 05/L-028 art. 8(1.9)] |
| DIVIDENDE, DIVIDEND | EXCLUDE | Dividends are EXEMPT from PIT (resident and non-resident) [Law No. 05/L-028 art. 8(1.26)] |
| KTHIM TATIMI, TAX REFUND, ATK REFUND | EXCLUDE | Tax refund from prior year |
| GRANT, SUBVENCION, GOVERNMENT GRANT | Check nature | Capital grants EXCLUDE; revenue grants = business income |

### 3.2 Expense Patterns (Debits) -- Fully Deductible (real-income method only)

Deductions apply **only under the real-income method**. Under the gross-income (3%/9%) method, tax is on gross receipts and **no expense deductions are taken**.

**3.2 Expense Patterns (Debits) -- Fully Deductible (real-income method only)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| QIRA ZYRE, OFFICE RENT, RENT [commercial address] | Office rent | Deductible | Dedicated business premises |
| SIGURIM PROFESIONAL, PROFESSIONAL INDEMNITY | Professional insurance | Deductible |  |
| KONTABILIST, ACCOUNTANT, AUDITOR, BOOKKEEP | Accountancy fees | Deductible |  |
| AVOKAT, LAWYER, LEGAL, NOTER | Legal fees | Deductible | Must be business-related |
| ZYRE, OFFICE SUPPLIES, STATIONERY | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, REKLAMA | Marketing/advertising | Deductible |  |
| TRAJNIM, TRAINING, COURSE, SEMINAR | Training | Deductible | Must relate to current business |
| TARIFE BANKE, BANK FEE, BANK CHARGE | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN | IT infrastructure | Deductible | Capitalise large items (see 3.7) |

### 3.3 Expense Patterns (Debits) -- SaaS and Software (real-income method)

**3.3 Expense Patterns (Debits) -- SaaS and Software (real-income method)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment, real-income method)

**3.4 Expense Patterns (Debits) -- Utilities (may need apportionment, real-income method)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| KEK, KESCO, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| UJESJELLES, WATER | Water | T2 if home office | Apportion for home use |
| IPKO, KUJTESA, VALA, TELEKOM, BROADBAND | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBILE, GSM | Phone | T2 | Business-use portion only |

### 3.5 Expense Patterns (Debits) -- Travel (real-income method)

**3.5 Expense Patterns (Debits) -- Travel (real-income method)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| WIZZ AIR, AIR PRISTINA, EASYJET, FLIGHT | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| TAXI, BOLT, UBER | Local transport | Deductible if business purpose |  |
| KARBURANT, FUEL, PETROL, NAFTE | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING, PARKIM | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORANT, RESTAURANT, DINNER, CLIENT MEAL, ARGETIM | Entertainment | NOT deductible | Treat as entertainment by default |
| PERSONAL, USHQIM, GROCERIES, SUPERMARKET, VIVA FRESH | Personal expenses | NOT deductible | Private living costs |
| GJOBE, FINE, PENALTY, MULTA | Fines/penalties | NOT deductible | Public policy |
| ATK PAYMENT, TATIM, INCOME TAX | Tax payments | NOT deductible | Income tax cannot reduce income |
| TERHEQJE, DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (real-income method, depreciate)

Depreciation under the real-income method follows corporate rules (Law No. 06/L-105). Specific category rates are **[RESEARCH GAP -- reviewer to confirm exact depreciation pool rates against the CIT Law and ATK guidance]**.

**3.7 Expense Patterns (Debits) -- Capital Items (real-income method, depreciate)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | Capitalise + depreciate | Rate per CIT Law [RESEARCH GAP] |
| PRINTER, SCANNER, COPIER | Office equipment | Capitalise + depreciate | Rate per CIT Law [RESEARCH GAP] |
| MOBILJE, FURNITURE, DESK, CHAIR | Furniture/fittings | Capitalise + depreciate | Rate per CIT Law [RESEARCH GAP] |
| VETURE, VEHICLE, CAR (business) | Motor vehicle | Capitalise + depreciate | Business % only |

### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER INTERN, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| KREDI, LOAN REPAYMENT, PRINCIPAL | EXCLUDE | Loan principal movement |
| TRUSTI, KPST, PENSION, CONTRIBUTION | Pension deduction | Mandatory 5% employee portion deductible for PIT (see 5.6) |
| TVSH, VAT PAYMENT | EXCLUDE | VAT liability payment, not expense |
| KESTI, ADVANCE PAYMENT, QS, QL | Advance tax paid | Credit against annual liability, not an expense |

### 3.9 Kosovo Banks -- Statement Format Reference

**3.9 Kosovo Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| ProCredit Bank | TRANSFER, PAGESE, TARIFA | PDF/CSV; description holds counterparty + reference |
| Raiffeisen Bank Kosovo | PAYMENT, TRANSFER, FEE | PDF/CSV; merchant in description |
| Banka Kombetare Tregtare (BKT) | TRANSFER, DEBIT DIRECT, TARIFE | PDF; Albanian-language descriptions common |
| TEB Bank | PAGESE, KARTE, TRANSFER | PDF/CSV |
| NLB Banka | TRANSFER, PAGESE, KOMISION | PDF; shorter descriptions |

## Section 4 -- Worked Examples

All amounts in EUR. Tax recomputed end-to-end.

### Example 1 -- Self-Employed, Real-Income Method, Net Profit Computation

**Inputs:** Resident sole proprietor, real-income method, no other income. Gross receipts EUR 60,000 (over the EUR 50,000 threshold, so real-income is mandatory). Allowable business expenses EUR 22,000. Mandatory self-employed pension contribution paid EUR 2,400 (EUR 600 a quarter).

**Reasoning:**
Net profit before pension = 60,000 - 22,000 = EUR 38,000. The mandatory contribution is 10% of that net amount, but not more than EUR 600 of obligatory contribution a quarter (Law No. 04/L-101 art. 6.12, as amended by [Law No. 04/L-168 art. 3](https://bqk-kos.org/wp-content/uploads/2024/11/Ligji-fondet-pensionale-te-Kosoves-anglisht.pdf)): 10% x 38,000 / 4 = EUR 950 a quarter, so the EUR 600 cap applies and EUR 2,400 a year is due. For the self-employed only the mandatory share is exempt from PIT ([TAK Public Explanatory Decision No. 01/2013](https://www.atk-ks.org/wp-content/uploads/2017/08/Vendim-Shpjegues-Publik-NR-01-2013Anglisht.pdf) art. 6). Taxable income = 38,000 - 2,400 = EUR 35,600, taxed at the art. 6 graduated rates (Law No. 05/L-028 arts. 5, 6 and 48(1)).

**Computation:** PIT = 0% on the first 3,000 + 8% x 2,400 (EUR 192.00) + 10% x (35,600 - 5,400) = 192.00 + 3,020.00 = **EUR 3,212.00**. Quarterly advances in the first real-income year are one quarter of the estimated liability (art. 43(2.2.1)).

> Where the individual also has wages, the annual declaration adds the wage income and the business profit and applies art. 6 once to the total, crediting the tax the employer withheld (arts. 47(1.1) and 48(1) and (4)).

### Example 2 -- Self-Employed, Gross-Income Method, Services (9%)

**Input line:**
`12/03/2025 ; PROCREDIT TRANSFER IN ; KLIENTI SH.P.K. ; PAGESE FATURA 2025-014 ; +4,500.00 ; EUR`

**Reasoning:**
Annual gross receipts EUR 41,000 (under EUR 50,000), services activity. Gross-income method at 9% applies to gross receipts; no expense deductions (Law No. 05/L-028 art. 43(2.1.2)). Quarterly tax is 9% of that quarter's gross receipts, subject to a minimum of EUR 37.50.

**Computation (annual):** PIT = 41,000 x 9% = **EUR 3,690.00**. Each quarter pays 9% of quarterly gross receipts (minimum EUR 37.50).

**Classification:** This single credit (EUR 4,500) is gross business income; quarter's tax on it = 4,500 x 9% = EUR 405.00 (> EUR 37.50 minimum, so EUR 405.00 applies).

### Example 3 -- Self-Employed, Gross-Income Method, Trade (3%)

**Reasoning:**
Resident sole proprietor, retail trade, annual gross receipts EUR 30,000 (under EUR 50,000). Trade activity uses the 3% gross-income rate (Law No. 05/L-028 art. 43(2.1.1)).

**Computation:** PIT = 30,000 x 3% = **EUR 900.00**. Compare quarterly: 900 / 4 = EUR 225.00 per quarter, each above the EUR 37.50 minimum.

### Example 4 -- Primary Employment Wage Withholding (graduated brackets)

**Input line:**
`31/01/2025 ; RAIFFEISEN ; EMPLOYER ABC SH.A. ; PAGA JANAR (NET) ; +1,140.00 ; EUR`

**Reasoning:**
Annual gross wage EUR 14,400 (EUR 1,200/month) from the primary employer. First the mandatory employee pension of 5% is withheld; it is not subject to PIT (Law No. 04/L-101 art. 37.2, as replaced by [Law No. 05/L-116 art. 10](https://bqk-kos.org/wp-content/uploads/2024/10/Ligji-05L116-per-ndryshimin-e-fondeve-pensionale.pdf)), and TAK computes the wage-tax base as gross salary less the employee's share (TAK Public Explanatory Decision No. 01/2013 art. 6). PIT is then computed on the graduated annual brackets.

**Computation (annual basis):**
- Gross wage: EUR 14,400.00
- Employee pension 5%: 14,400 x 5% = EUR 720.00 (deductible; no contribution ceiling applies)
- PIT base: 14,400 - 720 = EUR 13,680.00
- PIT: 0% on first 3,000 = EUR 0; 8% on 3,000.01-5,400 = EUR 192.00; 10% on (13,680 - 5,400) = 8,280 x 10% = EUR 828.00
- Total annual PIT = 192.00 + 828.00 = **EUR 1,020.00**
- Net annual = 14,400 - 720 - 1,020 = **EUR 12,660.00** (employer also remits its own 5% pension)

> The principal employer withholds monthly at the art. 6 rates, reducing each month's tentative tax by the amount withheld in the previous month of the year (Law No. 05/L-028 art. 38(2)); TAK's notice of 27 August 2024 gives the monthly bands as EUR 0 to 250 at 0%, 250.01 to 450 at 8% and above 450 at 10%. **[RESEARCH GAP -- reviewer to confirm]** how the EDI withholding form applies the art. 38(2) reduction when the wage changes during the year.

### Example 5 -- Secondary Employment (flat 10%)

**Input line:**
`28/02/2025 ; TEB BANK ; EMPLOYER XYZ ; PAGA DYTESORE SHKURT ; +500.00 ; EUR`

**Reasoning:**
Wage from a **secondary** employer. Graduated 0%/8% bands apply only to the primary employer; secondary-employer wages are withheld at a **flat 10%** (Law No. 05/L-028 art. 38(3)).

**Computation:** PIT withheld = 500 x 10% = **EUR 50.00** per the gross secondary wage for that period.

### Example 6 -- Mandatory Pension Contribution (Trusti/KPST)

**Input line:**
`15/02/2025 ; BKT ; TRUSTI KPST ; KONTRIBUT PENSIONAL JANAR ; -120.00 ; EUR`

**Reasoning:**
On a gross wage of EUR 1,200, total mandatory pension = 10% = EUR 120.00 (5% employee EUR 60.00 + 5% employer EUR 60.00) remitted to Trusti/KPST (Law No. 04/L-101 art. 6.2(a) and (b)). The employee 5% (EUR 60.00) reduces the employee's PIT base; the employer 5% is the employer's deductible expense (art. 37.1 and 37.2, as replaced by Law No. 05/L-116 art. 10).

**Classification:** Employee 5% (EUR 60.00) = PIT deduction; employer 5% (EUR 60.00) = employer cost, not a PIT deduction for the individual.

### Example 7 -- Dividend Received (Exempt)

**Input line:**
`20/04/2025 ; NLB BANKA ; KOMPANIA SH.P.K. ; DIVIDENDE 2024 ; +2,000.00 ; EUR`

**Reasoning:**
Dividends received by residents and non-residents are **exempt** from PIT (Law No. 05/L-028 art. 8(1.26)).

**Classification:** EXCLUDE. EUR 0 added to taxable income.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency and Scope

- **Residency and Scope** — Residents are taxed on worldwide income; non-residents only on Kosovo-source income. Confirm residency before any computation.  _([Law No. 05/L-028 on Personal Income Tax](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) arts. 2(1.18) and 4; amending Law No. 08/L-142 on [gzk.rks-gov.net](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360))_

### 5.2 Graduated PIT Rates (employment / general income)

**5.2 Graduated PIT Rates (employment / general income)**  _(Law No. 05/L-028 art. 6, as replaced by Law No. 08/L-142 art. 5)_

| Annual taxable income (EUR) | Rate |
| --- | --- |
| 0.00 -- 3,000.00 | 0% |
| 3,000.01 -- 5,400.00 | 8% |
| 5,400.01+ | 10% |

- **No standard deduction / allowance** — In force from 23 August 2024 (Law No. 08/L-142), unchanged for 2025/2026. No standard deduction; no personal/family allowance.  _(Law No. 08/L-142 art. 5; Law No. 05/L-028 art. 5)_

### 5.3 Self-Employed -- Gross-Income (Turnover) Method

- **Gross-income method trade rate** — 3% on gross receipts for trade, transport, agriculture and similar  _(Law No. 05/L-028 art. 43(2.1.1))_
- **Gross-income method services rate** — 9% on gross receipts for services, professional, vocational, entertainment and similar  _(Law No. 05/L-028 art. 43(2.1.2))_
- **Minimum quarterly payment and no deductions** — Minimum quarterly payment EUR 37.50; no expense deductions (tax is on gross receipts, reported on a cash basis). The method applies to annual gross income up to EUR 50,000 unless the taxpayer opts for full books by 1 March of the year; a new taxpayer's first quarterly statement records the option.  _(Law No. 05/L-028 arts. 32(2), 33(2) and (3.1) to (3.2) and 43(2.1))_

### 5.4 Self-Employed -- Real-Income Method

- **Real-income method** — For annual gross income over EUR 50,000 (mandatory), or elected below the threshold: net taxable profit on the accrual basis, after the expenses Law No. 05/L-028 allows (arts. 15 to 30), taxed at the art. 6 graduated rates with any other income. Once in the method, the taxpayer stays for at least three further tax periods.  _(Law No. 05/L-028 arts. 5, 6, 32(3), 33(1) to (4) and 48(1))_

### 5.5 Exempt Income

**5.5 Exempt Income**

| Item | Treatment | Reference |
| --- | --- | --- |
| Dividends (resident and non-resident recipients) | Exempt from PIT | Law No. 05/L-028 art. 8(1.26) |
| Interest on financial instruments issued or guaranteed by a Kosovo public authority | Exempt | Law No. 05/L-028 art. 8(1.9) |
| Pensions and social assistance paid by the Government of Kosovo | Exempt | Law No. 05/L-028 art. 8(1.13) |

### 5.6 Mandatory Pension Contributions

**5.6 Mandatory Pension Contributions**  _([Law No. 04/L-101 on Pension Funds](https://www.atk-ks.org/wp-content/uploads/2017/07/Law-No.-04-L-101.pdf) art. 6; [TAK Public Explanatory Decision No. 01/2013](https://www.atk-ks.org/wp-content/uploads/2017/08/Vendim-Shpjegues-Publik-NR-01-2013Anglisht.pdf) arts. 4 to 7)_

| Party | Rate | Base | Cap | Reference |
| --- | --- | --- | --- | --- |
| Employee | 5% of gross wage | Gross wage | None | Law No. 04/L-101 art. 6.2(b) |
| Employer | 5% of gross wage | Gross wage | None | Law No. 04/L-101 art. 6.2(a) |
| **Total mandatory** | **10%** | Gross wage | None | -- |

**Verification:** employee 5% + employer 5% = 10% total. Confirmed.

- Floor: where a full-time wage is below the minimum wage, the employer pays 5% of the minimum wage (art. 6.6; TAK Decision 01/2013 art. 7). No ceiling: art. 6.2 sets 5% of total wages without an upper limit, and Laws No. 04/L-168 and 05/L-116 did not add one (04/L-168 changes only art. 6.12 for the self-employed; 05/L-116 does not touch art. 6). Version 0.1 applied a EUR 24,000 annual cap that none of these texts contains.
- The employee's share, including voluntary contributions up to 15% of gross salary, is deductible from the employee's PIT base, and the employer's share up to 15% is the employer's expense (TAK Decision 01/2013 art. 6; Law No. 04/L-101 art. 37.1 and 37.2, as replaced by [Law No. 05/L-116 art. 10](https://bqk-kos.org/wp-content/uploads/2024/10/Ligji-05L116-per-ndryshimin-e-fondeve-pensionale.pdf)). Voluntary contributions may add up to 10% each, for a maximum of 15% each and 30% combined (art. 6.2(c); TAK Decision 01/2013 art. 5).
- Self-employed persons on the real-income method contribute at least 10% of net profit before the contribution, up to 30%, with the obligatory part capped at EUR 600 a quarter; those on the gross-income method contribute at least one third of the quarterly presumptive tax; every self-employed person pays at least 30% of the minimum wage a quarter. Only the mandatory share is exempt from PIT for the self-employed (Law No. 04/L-101 art. 6.12, as amended by Law No. 04/L-168 art. 3; TAK Decision 01/2013 arts. 4 and 6).
- Kosovo has **no separate general social-security or state health-insurance payroll tax** beyond the mandatory pension contribution **[RESEARCH GAP -- reviewer to confirm no health-insurance contribution introduced for 2026]**.

### 5.7 Rental Income

- **Rental income taxation** — An individual who rents out property without making renting their business may deduct 10% of rents received instead of keeping expense records, and pays quarterly 10% of the taxable rent (gross rent less that 10%), which is 9% of gross rent, less any tax a business tenant withheld. A business tenant withholds 9% of the gross rent and pays it over by the 15th of the following month. Renting carried on as a business is taxed as economic activity under the gross-income or real-income method.  _(Law No. 05/L-028 arts. 11(2), 27, 39(4) and 44)_
- Version 0.1 stated 10% of gross rent; art. 44(2) applies 10% to rent after the 10% deduction.

### 5.8 Charitable Donations

- **Charitable donations deduction** — Charitable donations/sponsorships are deductible up to 10% of taxable income (an additional 10% may be possible under other laws), for taxpayers keeping full books under art. 33(5) only, and only for gifts to registered NGOs or the public-interest bodies the article lists.  _(Law No. 05/L-028 art. 28(1), (2) and (5))_

### 5.9 Inheritances / Gifts; Wealth Tax

- **Inheritances/gifts and wealth tax** — An inheritance is exempt when the heir is the spouse, a biological or adopted child or a parent, or when its value is EUR 5,000 or less (art. 8(1.14)). Gifts between spouses, from parent to child and from child to parent are exempt whatever their value; any other gift a resident receives counts as other income "if the value of such gift amounts exceeds" EUR 5,000 in a tax period (art. 14(2) and (3)). The law does not limit the taxable amount to the excess over EUR 5,000. No net wealth tax is imposed by these laws.  _(Law No. 05/L-028 arts. 8(1.14) and 14)_

### 5.10 VAT Interaction

**5.10 VAT Interaction**

| Scenario | PIT Treatment |
| --- | --- |
| VAT collected on sales (registered, standard 18%) | NOT income -- exclude from business receipts |
| Input VAT recovered (registered) | NOT an expense -- exclude (real-income method) |
| Non-registered (below EUR 30,000 turnover) | VAT paid on purchases is part of the gross cost |

- **VAT rates and registration threshold** — VAT: standard rate 18%, reduced rate 8% for the goods and services listed in art. 26(2); registration is required once turnover exceeds EUR 30,000 in a calendar year, and a person not established in Kosovo registers from the start of its activity there.  _([Law No. 05/L-037 on VAT](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) arts. 6(1) and (5) and 26)_

### 5.11 Filing, Advance Payments, Deadlines

**5.11 Filing, Advance Payments, Deadlines**

| Item | Detail | Reference |
| --- | --- | --- |
| Annual return (form PD) | Due 31 March of the following year; calendar tax year. Not required where the only income is wages, gross-income-method business income, fully paid rent, interest, lottery winnings, intangible-property income or special-category income | Law No. 05/L-028 art. 48(1) and (2) |
| Quarterly advance (QS, gross-income 3%/9%) | Due 15 April, 15 July, 15 October, 15 January | Law No. 05/L-028 art. 43(1) and (2.1) |
| Quarterly advance (QL, real-income / business income over EUR 50,000 or full books elected) | One quarter of the estimated liability in the first year or after a loss year; afterwards at least one quarter of 110% of the prior-year liability, less tax withheld; same quarterly dates | Law No. 05/L-028 art. 43(2.2) and (7.4) |
| Employer payroll filing/remittance (WM/WR) | Within 15 days after the end of each month | Law No. 05/L-028 art. 38(5) |
| New-hire reporting | Notify TAK one day before the employee starts work; EUR 500 fine for each undeclared worker | [Law No. 08/L-257](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) arts. 43(5) and 102(3) |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (real-income method)

- Apportion rent and utilities by business-use proportion; dedicated workspace required.
- **Conservative default:** 0% until reviewer confirms arrangement.
- **Flag for reviewer:** floor-area basis and dedicated-use confirmation.

### 6.2 Motor Vehicle Business Use (real-income method)

- Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible; mileage log required.
- **Conservative default:** 0% business use until log provided.

### 6.3 Phone / Internet Mixed Use (real-income method)

- Business-use portion only; reasonable estimate required.
- **Conservative default:** 0% until business percentage confirmed.

### 6.4 Activity Classification (3% vs 9%)

- If activity sits between trade (3%) and services (9%), apply 9% by default.
- **Flag for reviewer:** confirm the predominant activity and applicable rate.

### 6.5 Method Election Near the Threshold

- Below EUR 50,000 gross, the taxpayer may elect the real-income method by statement to TAK by 1 March; above EUR 50,000 it is mandatory, and either way the taxpayer stays in it for at least three further periods (Law No. 05/L-028 arts. 33(1) to (4) and 43(3)).
- **Flag for reviewer:** confirm gross-income figure and any election filed with ATK.

### 6.6 Pension Minimum-Wage Floor

- No contribution ceiling applies (5.6). Use the minimum wage as the floor for a full-time employee paid less than it.
- **Flag for reviewer:** confirm the minimum wage in force for the month; the government decision on the 2026 rates was not read for this guide.

### 6.7 Capital Asset Depreciation

- Straight-line by asset, at 5% for buildings (category 1), 20% for vehicles, computers, office furniture and equipment (category 2) and 10% for plant, machinery and other tangible assets (category 3). An asset costing up to EUR 1,000 is expensed unless it forms part of a larger whole worth more than EUR 1,000. Land and works of art are not depreciated.  _(Law No. 05/L-028 arts. 2(1.2) and 20)_
- **Flag for reviewer:** treatment of gains and losses on disposal (art. 31) and of assets still in pre-2010 pools.

## Section 7 -- Excel Working Paper Template

```
KOSOVO PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident (worldwide) / Non-resident (Kosovo-source)
Status: Employed / Self-employed
If self-employed -- Method: Gross-income (3% / 9%) / Real-income (graduated rates)

A. BUSINESS INCOME
  A1. Gross receipts (net of VAT if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, Wise)     ___________
  A3. Other business income                        ___________
  A4. TOTAL gross receipts                         ___________

GROSS-INCOME METHOD (3% / 9%) -- skip Section B
  G1. Rate (3% trade / 9% services)                ___________
  G2. PIT = A4 x rate                              ___________
  G3. Quarterly = G2 / 4 (min EUR 37.50/qtr)       ___________

REAL-INCOME METHOD (graduated rates) -- complete Section B
B. ALLOWABLE DEDUCTIONS (real-income only)
  B1. Office rent                                  ___________
  B2. Professional insurance                       ___________
  B3. Accountancy / legal fees                     ___________
  B4. Office supplies                              ___________
  B5. Software subscriptions                       ___________
  B6. Marketing / advertising                      ___________
  B7. Bank / payment processing fees               ___________
  B8. Training                                     ___________
  B9. Travel                                       ___________
  B10. Telecoms (business %)                       ___________
  B11. Home office (business %)                    ___________
  B12. Vehicle (business %)                        ___________
  B13. Depreciation (5% / 20% / 10%, art. 20)     ___________
  B14. Charitable donations (max 10% of income)    ___________
  B15. Mandatory self-employed pension             ___________
  B16. TOTAL deductions                            ___________

C. NET TAXABLE PROFIT (A4 - B16)                   ___________
  C1. Add to D3 and apply the graduated rates once (art. 48(1))

EMPLOYMENT INCOME (graduated brackets)
D. WAGE COMPUTATION
  D1. Gross annual wage (primary employer)         ___________
  D2. Employee pension 5% (no ceiling)             ___________
  D3. PIT base = D1 - D2                           ___________
  D4. 0% on 0-3,000                                = 0.00
  D5. 8% on 3,000.01-5,400 (max EUR 192.00)        ___________
  D6. 10% on amount over 5,400                     ___________
  D7. PIT on primary wage = D5 + D6                ___________
  D8. Secondary wage x 10% (flat)                  ___________

E. ADVANCE PAYMENTS / CREDITS
  E1. Quarterly advances paid (QS / QL)            ___________
  E2. Wage tax already withheld                    ___________

F. ANNUAL RECONCILIATION (form PD)
  F1. Total PIT liability                          ___________
  F2. Less advances/withholding (E1 + E2)          ___________
  F3. Tax due / refund (F1 - F2)                   ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Method (gross-income vs real-income) confirmed?
  [ ] Activity classification (3% vs 9%) confirmed?
  [ ] Gross income vs EUR 50,000 threshold confirmed?
  [ ] Pension on full gross wage, minimum-wage floor applied?
  [ ] Employee pension deducted for PIT (voluntary share only up to 15% of gross)?
  [ ] Primary vs secondary employment split correct (flat 10% on secondary)?
  [ ] Dividends / govt-bond interest excluded (exempt)?
  [ ] VAT excluded from receipts/expenses if registered?
  [ ] All T2 items flagged?
```

## Section 8 -- Bank Statement Reading Guide

### Kosovo Bank Statement Formats

**Kosovo Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| ProCredit Bank | PDF, CSV | Date, Description, Debit, Credit, Balance | Description holds counterparty + reference |
| Raiffeisen Bank Kosovo | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant |
| BKT (Banka Kombetare Tregtare) | PDF | Date, Pershkrimi, Debi, Kredi | Albanian-language descriptions common |
| TEB Bank | PDF, CSV | Date, Description, Amount, Balance |  |
| NLB Banka | PDF | Date, Pershkrimi, Amount, Balance | Shorter descriptions |

### Key Albanian Banking / Tax Terms

**Key Albanian Banking / Tax Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFER / TRANSFERIM | Transfer | Check direction for income/expense |
| PAGESE | Payment | Expense or income depending on direction |
| PAGA / RROGA | Wage / salary | Employment income (primary vs secondary) |
| QIRA | Rent | Rental income or office-rent expense |
| FATURA | Invoice | Business income (incoming) |
| HONORAR | Fee / honorarium | Professional self-employment income |
| TARIFA / KOMISION | Fee / commission | Bank charge (deductible, real-income) |
| INTERES | Interest | Interest income (govt-bond interest exempt) |
| DIVIDENDE | Dividend | EXEMPT -- exclude |
| KONTRIBUT PENSIONAL / TRUSTI / KPST | Pension contribution | Mandatory 5% employee portion deductible |
| TVSH | VAT | Exclude from income tax |
| TATIM / ATK | Tax / tax authority | Tax payment -- not deductible |
| GJOBE | Fine | Not deductible |
| TERHEQJE | Withdrawal | Possible drawings -- ask |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- KOSOVO PERSONAL INCOME TAX
1. Are you a Kosovo tax resident (taxed on worldwide income)?
2. Are you employed, self-employed, or both?
3. If self-employed: what is your annual gross income? (Threshold EUR 50,000)
4. If self-employed: is your activity trade (3%) or services (9%)?
5. Have you elected the real-income method, or use the gross-income method?
6. Are you VAT-registered? (Threshold EUR 30,000 turnover)
7. If employed: is this your primary or a secondary employer?
8. Pension: how much was paid to Trusti/KPST during the year (employee portion)?
9. Quarterly advances paid (QS/QL) during the year?
10. Any exempt income (dividends, Kosovo govt-bond interest)?
11. Any capital assets purchased during the year (real-income method)?
12. Any rental income, and is it an economic activity?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference |
| --- | --- |
| PIT rates and rules | Law No. 05/L-028, as amended by Law No. 08/L-142 (in force 23 Aug 2024) — [gzk.rks-gov.net](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360) |
| Corporate / small-business gross-receipts rules | [Law No. 06/L-105](https://www.atk-ks.org/wp-content/uploads/2019/09/LAW_NO.06_L-105.pdf) arts. 35 and 38 |
| Pension contributions | [Law No. 04/L-101](https://www.atk-ks.org/wp-content/uploads/2017/07/Law-No.-04-L-101.pdf) arts. 6 and 37, as amended by [Law No. 04/L-168](https://bqk-kos.org/wp-content/uploads/2024/11/Ligji-fondet-pensionale-te-Kosoves-anglisht.pdf) and [Law No. 05/L-116](https://bqk-kos.org/wp-content/uploads/2024/10/Ligji-05L116-per-ndryshimin-e-fondeve-pensionale.pdf); [TAK Public Explanatory Decision No. 01/2013](https://www.atk-ks.org/wp-content/uploads/2017/08/Vendim-Shpjegues-Publik-NR-01-2013Anglisht.pdf) |
| VAT | [Law No. 05/L-037](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) arts. 6 and 26 |
| Penalties / procedure | [Law No. 08/L-257 on the Administration of Tax Procedures](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Filing portal | ATK EDI (edideklarimi.atk-ks.org) |

### Key Figures (with provenance)

**Key Figures (with provenance)**

| Figure | Value | Reference |
| --- | --- | --- |
| PIT 0% band | EUR 0 -- 3,000/yr | Law No. 05/L-028 art. 6, as replaced by Law No. 08/L-142 art. 5 |
| PIT 8% band | EUR 3,000.01 -- 5,400/yr | Same |
| PIT 10% band | EUR 5,400.01+/yr | Same |
| Tax at top of 8% band | EUR 192.00 | Computed: 2,400 x 8%; the same figure is written into art. 6(1.3) |
| Secondary-employer wage rate | Flat 10% | Law No. 05/L-028 art. 38(3) |
| Gross-income method ceiling | EUR 50,000/yr | Law No. 05/L-028 arts. 33(1) and 43(2.1) |
| Gross-income trade rate | 3% | Law No. 05/L-028 art. 43(2.1.1) |
| Gross-income services rate | 9% | Law No. 05/L-028 art. 43(2.1.2) |
| Gross-income minimum quarterly | EUR 37.50 | Law No. 05/L-028 art. 43(2.1.1) and (2.1.2) |
| Real-income method rate | Graduated art. 6 rates on net profit plus other income | Law No. 05/L-028 arts. 6 and 48(1) |
| Mandatory pension (employee + employer) | 5% + 5% = 10% | Law No. 04/L-101 art. 6.2 |
| Pension contribution ceiling | None | Law No. 04/L-101 art. 6.2 (unchanged by Laws No. 04/L-168 and 05/L-116) |
| Self-employed obligatory pension cap | EUR 600 a quarter | Law No. 04/L-101 art. 6.12, as amended by Law No. 04/L-168 art. 3 |
| Voluntary pension cap | Up to 15% each (30% combined incl. mandatory) | Law No. 04/L-101 art. 6.2(c); TAK Decision 01/2013 art. 5 |
| VAT standard / reduced rate | 18% / 8% | Law No. 05/L-037 art. 26 |
| VAT registration threshold | EUR 30,000 turnover/yr | Law No. 05/L-037 art. 6(1) |
| CIT / small-business turnover threshold | EUR 30,000/yr | Law No. 06/L-105 arts. 35(1) and 38(2.1) |
| Quarterly advance trigger (individual business, real-income) | over EUR 50,000/yr, or full books elected | Law No. 05/L-028 art. 43(2.2) |
| Quarterly advance instalment | 1/4 of 110% of prior-year liability (estimate in the first year or after a loss) | Law No. 05/L-028 art. 43(2.2) and (7.4) |
| Inheritance exemption (heir outside spouse, child, parent) | value up to EUR 5,000 | Law No. 05/L-028 art. 8(1.14) |
| Gift included in other income (other donors) | value over EUR 5,000 in a tax period | Law No. 05/L-028 art. 14(2) and (3) |
| Charitable donation deduction | up to 10% of taxable income | Law No. 05/L-028 art. 28(1) |
| Minimum wage (2025) | EUR 350/month gross (effective 1 Oct 2024) | Government Decision; Playroll |
| Minimum wage (from 1 Jan 2026) | EUR 425/month gross | Government Decision 10/273; Playroll |
| Minimum wage (from 1 Jul 2026) | EUR 500/month gross | Government Decision 10/273; Playroll |

### Penalties

**Penalties**

| Type | Amount | Reference |
| --- | --- | --- |
| Tax understatement / under-declaration | 15% of the shortfall where it is 10% or less of the correct tax; 25% where it is more | Law No. 08/L-257 art. 100(1) |
| Failure to file a declaration that results in a liability | EUR 50 per declaration for a business natural person; EUR 20 for a non-business natural person; EUR 150 for a legal entity | Law No. 08/L-257 art. 99 |
| Failure to withhold or pay over wage tax or pension contributions | 25% of the amount not paid over | Law No. 08/L-257 art. 103 |
| Late payment interest | Monthly, at a rate the Minister sets at least once a year above commercial bank lending rates; accrues for at most ten years from the due date | Law No. 08/L-257 art. 24 |
| Amendment window | An amended declaration may be filed within three years of the mandatory filing date | Law No. 08/L-257 art. 14(2) |
| Fine reductions | 75% off for voluntary disclosure before notice of an investigation; 50% off a fine paid within 15 days of notice (not for art. 103 fines) | Law No. 08/L-257 art. 110(1) and (7) |

### Forms

**Forms**

| Form | Purpose | Deadline |
| --- | --- | --- |
| PD -- Annual Personal Income Tax declaration | Annual reconciliation of personal income | 31 March of following year |
| QS -- Quarterly statement (gross-income 3%/9%) | Quarterly tax on gross receipts | 15 Apr, 15 Jul, 15 Oct, 15 Jan |
| QL -- Quarterly advance instalment (real-income) | Advance for individual business income over EUR 50,000 or full books elected | 15 Apr, 15 Jul, 15 Oct, 15 Jan |
| WM / WR -- Monthly wage withholding statements | Employer reports PIT + pension withheld | By the 15th of following month |
| Rental tax (non-business landlord) | 10% of rent after the 10% deduction, less tax withheld by a business tenant | Quarterly, 15 days after the quarter (Law No. 05/L-028 art. 44) |

> **[RESEARCH GAP -- reviewer to confirm]** Exact EDI form codes (especially the individual annual declaration code) were not pinned to an ATK source page in research; verify the precise form codes on the ATK portal. On 8 October 2026 atk-ks.org answered normally, and the figures in this guide were checked against the English law texts it publishes.

### Test Suite

Input: Resident sole proprietor, real-income method, no other income, gross receipts EUR 60,000, deductions EUR 22,000, mandatory pension EUR 2,400.
Expected: Profit before pension = EUR 38,000; taxable income = EUR 35,600. PIT = 192.00 + (30,200 x 10% = 3,020.00) = **EUR 3,212.00**.

Input: Self-employed services, annual gross receipts EUR 41,000 (under EUR 50,000).
Expected: PIT = 41,000 x 9% = **EUR 3,690.00**.

Input: Self-employed trade, annual gross receipts EUR 30,000.
Expected: PIT = 30,000 x 3% = **EUR 900.00**; quarterly = EUR 225.00 (above EUR 37.50 min).

Input: Primary-employer gross wage EUR 14,400/yr; employee pension 5%.
Expected: Pension = EUR 720.00; PIT base = EUR 13,680.00; PIT = 192.00 + (8,280 x 10% = 828.00) = **EUR 1,020.00**.

Input: Secondary-employer wage EUR 500.
Expected: PIT = 500 x 10% = **EUR 50.00**.

Input: Gross wage EUR 1,200/month.
Expected: Total pension = EUR 120.00 (employee EUR 60.00 + employer EUR 60.00); the employee EUR 60.00 reduces the employee's PIT base.

Input: Dividend received EUR 2,000.
Expected: EXCLUDE -- EUR 0 added to taxable income.

Input: Annual taxable income exactly EUR 5,400.
Expected: PIT = 0 + (2,400 x 8% = 192.00) = **EUR 192.00**.

## PROHIBITIONS

- NEVER compute Kosovo PIT without confirming tax residency
- NEVER apply expense deductions under the gross-income (3%/9%) method -- it taxes gross receipts
- NEVER apply the graduated 0%/8% bands to secondary-employer wages -- use flat 10%
- NEVER include exempt dividends or Kosovo government-bond interest in taxable income
- NEVER deduct an employee's pension contributions above 15% of gross salary, or a self-employed person's voluntary contributions, for PIT
- NEVER cap the 5% + 5% pension contribution at a wage ceiling -- the law sets none
- NEVER apply a flat 10% to real-income profit -- use the graduated art. 6 rates
- NEVER include VAT collected on sales in business receipts for VAT-registered taxpayers
- NEVER allow fines, penalties, drawings, or income tax itself as a deduction
- NEVER use current-year income for quarterly advances after the first real-income year (unless the prior year was a loss) -- use 1/4 of 110% of prior-year liability
- NEVER present tax calculations as definitive -- always label as estimated and flag every [RESEARCH GAP] for reviewer confirmation

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
