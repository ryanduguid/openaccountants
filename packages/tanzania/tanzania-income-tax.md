---
name: tanzania-income-tax
description: Use this skill whenever asked about Tanzania (Mainland) personal income tax, PAYE, or self-employed/sole-trader tax. Trigger on phrases like "how much PAYE do I pay", "Tanzania income tax", "TRA return", "ITX 201", "presumptive tax", "turnover tax Tanzania", "NSSF deduction", "SDL", "Skills Development Levy", "PSSSF", "WCF", "chargeable income TZS", "provisional tax Tanzania", "Return of Income individual", or any question about computing or filing personal income tax for an employee or self-employed individual in Tanzania. Also trigger when preparing or reviewing an ITX 201.01.E return, computing PAYE on a salary, applying the presumptive (turnover-based) regime, or advising on statutory contributions (NSSF/PSSSF/SDL/WCF). This skill covers the resident PAYE bands, non-resident flat rate, presumptive tax, social-security and statutory contributions, filing forms and deadlines, registration thresholds, and penalties. ALWAYS read this skill before touching any Tanzania income tax work.
jurisdiction: TZ
category: international
version: 0.2
tax_year: 2025
last_updated: 2026-10-11
reviewed_by: Baraka Cassian
review_status: pending_review
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tanzanian Income Tax -- Personal / Self-Employed

## Scope note

Tanzania **does** levy a personal income tax administered by the **Tanzania Revenue Authority (TRA)**. This skill covers **Tanzania Mainland**. The TRA also administers Zanzibar PAYE on the same income bands, but Zanzibar runs its own VAT/levy regime — treat Zanzibar-specific indirect taxes as out of scope and escalate. All figures are TZS (Tanzanian Shilling). Tax year = calendar year (1 January – 31 December).

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Baraka Cassian** on 2026-06-12; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.
>
> **Edited since review (2026-10-11).** Citations now point to the statutes and TRA's own publications instead of a secondary tax summary: the Income Tax Act, Cap 332 (the Revised Edition 2023 published by TRA, "ITA" below, with the Finance Act 2026 amendments), the Tax Administration Act, Cap 438 ("TAA"), the National Social Security Fund Act, Cap 50, the Public Service Social Security Fund Act 2018, the Vocational Education and Training Act, Cap 82, the Workers Compensation Act, Cap 263, and TRA's "Income Tax for Individuals", "Pay As You Earn", SDL, VAT and penalties pages and its "Taxes and Duties at a Glance 2025/2026" booklet (July 2025). The sources changed four statements: PAYE is computed on pay after the employee's contribution to an approved retirement fund (ITA s.61; TRA PAYE page), so Examples 1 and 2 and the tests are recomputed; the Finance Act 2026 raised the presumptive turnover ceiling to TZS 200,000,000 and the top band to 4% from 1 July 2026, with a twelve-month relief for new traders; late-payment interest is the Bank of Tanzania discount rate compounded monthly, not that rate plus five points (TAA ss.3 and 76); and the WCF tariff is 0.5% for public as well as private employers (WCF). Section numbers of the ITA follow the Revised Edition 2023 (the former s.90 is now s.115, s.91 is s.117, ss.88-89 are ss.113-114); the reviewer's citations that still carry the 2019 numbers are marked. These edits are not covered by the 2026-06-12 sign-off.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Republic of Tanzania (Mainland) |
| Tax | Personal Income Tax / PAYE |
| Currency | TZS (Tanzanian Shilling) only |
| Tax year | Calendar year (1 January – 31 December) |
| Primary legislation | Income Tax Act, Cap. 332; Tax Administration Act, Cap. 438 |
| Tax authority | Tanzania Revenue Authority (TRA) |
| Filing portal | TRA online services (PAYE/SDL/WHT monthly); IDRAS for SDL |
| PAYE deadline | 7th day of the month following the payroll month (TRA) |
| Annual individual return | Form ITX 201.01.E — due within 6 months of year-end (by 30 June) (ITA s.117; TRA, "Income Tax for Individuals") |
| Tax-free threshold | First TZS 270,000/month (TZS 3,240,000/year) (ITA First Schedule para 1(1), as substituted by Finance Act 2021 s.25; TRA) |
| Top marginal rate | 30% (ITA First Schedule para 1(1); TRA) |
| Validated by | Pending — requires sign-off by a Tanzanian tax practitioner |
| Validation date | Verified by Baraka Cassian (ACPA 3158) on 2026-06-12 |
| Skill version | 0.2 |

### Resident PAYE Bands — Monthly (TRA)

**Resident PAYE Bands — Monthly**  _(ITA First Schedule para 1(1), the annual scale substituted by Finance Act 2021 s.25 (NIL to TZS 3,240,000; 8% to 6,240,000; 240,000 plus 20% to 9,120,000; 816,000 plus 25% to 12,000,000; 1,536,000 plus 30% above), in force from 1 July 2021 and divided by twelve for monthly withholding; TRA, "Income Tax for Individuals" (https://www.tra.go.tz/page/income-tax-for-individuals) and "Taxes and Duties at a Glance 2025/2026", section 4.0)_

| Monthly taxable income (TZS) | Rate | Tax on band | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 – 270,000 | 0% (NIL) | 0 | 0 |
| 270,001 – 520,000 | 8% of excess over 270,000 | 20,000 | 20,000 |
| 520,001 – 760,000 | 20,000 + 20% of excess over 520,000 | 48,000 | 68,000 |
| 760,001 – 1,000,000 | 68,000 + 25% of excess over 760,000 | 60,000 | 128,000 |
| Above 1,000,000 | 128,000 + 30% of excess over 1,000,000 | — | — |

**Arithmetic check (do not alter without re-deriving):** band 2 cap 250,000 × 8% = 20,000; band 3 cap 240,000 × 20% = 48,000 → 68,000 cumulative; band 4 cap 240,000 × 25% = 60,000 → 128,000 cumulative. Tax-free first TZS 270,000/month = TZS 3,240,000/year, stated explicitly by TRA.

**The bands apply to pay after the employee's retirement contribution.** An individual reduces total income by the retirement contributions made to an approved retirement fund (NSSF, PSSSF or another approved fund) by the individual, or by the employer where the contribution is included in the individual's employment income, up to the statutory contribution (ITA s.61). TRA applies the same reduction in monthly withholding: the contributions to approved retirement funds "are reduced from the gross pay when calculating the PAYE", the reduction being the lower of the contributions and the statutory amount (TRA, "Pay As You Earn"). The monthly PAYE base is therefore gross pay less the employee's NSSF or PSSSF share. TRA publishes the same monthly scale for Mainland and Zanzibar (its booklet heads the table "Tanzania Mainland and Zanzibar"); First Schedule para 1(7) lets the Minister set a different Zanzibar rate in consultation with Zanzibar's finance minister, so check TRA's Zanzibar table for the year.

### Other Income-Tax Rates on Individuals

**Other Income-Tax Rates on Individuals**

| Item | Rate | Source |
| --- | --- | --- |
| Non-resident employment income | 15% of gross employment income, withheld by the employer and effectively FINAL; a non-resident whose income consists only of such employment need not file a return | ITA First Schedule para 4(a)(ii); TRA, "Pay As You Earn" ("Specific rates applicable to certain categories of employees"); TRA booklet 2025/2026 section 4.0 |
| Total income of a non-resident individual (other income) | 30% flat | ITA First Schedule para 1(4) |
| Secondary employment (second employer) | Withheld at the highest individual rate (30%) on the whole payment; the employee nominates the primary employment and tells the other employers; a secondary employer may be allowed a lower rate by the Commissioner where the top rate causes hardship | TRA, "Pay As You Earn" ("Secondary employment") |
| Directors' fees (non-full-time directors) | 15%, not final | ITA s.7(2)(h) and First Schedule para 4(a)(iii); TRA PAYE page |
| Capital gains — resident, Tanzanian shares, securities, land or buildings | 10% of the gain, paid as a single instalment within 30 days of realisation and before title transfers (3% of the incomings or approved value where a resident has no cost records for land or buildings); the gain is then taxed at 10% in the annual computation while the rest of total income uses the normal scale | ITA s.115(1)(a)-(b), (3)-(4) (s.90 in R.E. 2019); First Schedule para 1(2)-(3) |
| Capital gains — non-resident, Tanzanian-source investment | 20% single instalment at realisation, credited against the 30% rate on the non-resident's total income | ITA s.115(1)(d); First Schedule para 1(4) |
| Capital gains — resident, overseas-source investment | Not within the para 1(2) gains, so included in total income at the progressive scale (top rate 30%) | ITA First Schedule para 1(1)-(2); Second Schedule exemptions in Section 5.5 |

### Presumptive (Turnover-Based) Tax — Individual Traders (TRA)

**Presumptive (Turnover-Based) Tax — Individual Traders, year of income 2025**  _(ITA First Schedule para 2, in the Revised Edition 2023 wording that applied until 30 June 2026; TRA, "Taxes and Duties at a Glance 2025/2026", section 6.0)_

| Annual turnover (TZS) | Tax — incomplete records (TAA s.43 not complied with) | Tax — complete records (TAA s.43 complied with) |
| --- | --- | --- |
| 0 – 4,000,000 | NIL | NIL |
| 4,000,001 – 7,000,000 | 100,000 | 3% of excess over 4,000,000 |
| 7,000,001 – 11,000,000 | 250,000 | 90,000 + 3% of excess over 7,000,000 |
| 11,000,001 – 100,000,000 | 3.5% of turnover | 3.5% of turnover |

Applies to **resident individuals** whose income consists only of business income with a source in Tanzania, whose turnover **does not exceed TZS 100,000,000** and who do not elect out of the regime (ITA First Schedule para 2(1)-(2)); a VAT-registered trader keeps full accounts and is outside it in practice. "Complete records" means the records required by TAA s.43. **Arithmetic check:** complete-records band 2 at TZS 7,000,000 = 3% × 3,000,000 = 90,000, which is the base of band 3 — consistent. Turnover **above TZS 100,000,000**: taxed on net profit under the standard regime with audited accounts, NOT presumptive (TRA booklet, section 7.0 note).

**From 1 July 2026 (Finance Act 2026 s.27).** The ceiling is TZS 200,000,000 and the table is: NIL to 4,000,000; NIL for the first twelve months after obtaining a TIN to start a business, for turnover between 4,000,000 and 200,000,000, on application to the Commissioner; 100,000 or 3% of the excess over 4,000,000 for 4,000,001 – 7,000,000; 250,000 or 90,000 + 3% of the excess over 7,000,000 for 7,000,001 – 11,000,000; and **4.0% of turnover** for 11,000,001 – 200,000,000 whether or not records are complete. The new-trader relief needs a statutory declaration, a business description and a projected turnover, is decided within seven working days, cannot be transferred and is refused or revoked for a "chaining arrangement" (a business registered under the spouse, dependant, child or nominee of someone who already had the relief, or the same trade at the same location within 180 days of the previous business ceasing) (Income Tax (Presumptive Tax Relief for New Traders) Regulations 2026, GN 158B, regs 2, 5, 6 and 8). TRA's individuals page already shows the new table. A rate change that takes effect part way through a year of income is applied by apportioning the year by days (ITA First Schedule para 5(3)); confirm with TRA how the 2026 calendar year is split before quoting a 2026 figure.

**Presumptive tax — transport operators (selected annual amounts per vehicle)**  _(ITA First Schedule para 2(5), amounts per TRA's "Taxes and Duties at a Glance 2025/2026", section 7.0)_

| Vehicle | Annual tax (TZS) |
| --- | --- |
| Passenger vehicles, up to 5 seats | 120,000 |
| Passenger vehicles, over 65 seats | 2,200,000 (seat bands in between carry intermediate amounts) |
| Taxis | 180,000 |
| Ride-hailing vehicles | 350,000 |
| Ride-sharing vehicles | 450,000 |
| Special hire | 750,000 |
| Goods vehicles | 120,000 to 2,200,000 by tonnage |

Transport operators pay these vehicle-based amounts instead of the turnover bands above; confirm the seat and tonnage band of the vehicle against the current First Schedule before quoting a figure.

### Statutory Contributions (Quick View)

**Statutory Contributions (Quick View)**

| Contribution | Total | Employee | Employer | Source |
| --- | --- | --- | --- | --- |
| NSSF (private sector) | 20% of wages | up to 10% | balance (min 10%) | National Social Security Fund Act, Cap 50, ss.12-13 and First Schedule; NSSF, "Rate of Contributions" |
| PSSSF (public sector) | 20% of monthly salary | 5% | 15% | Public Service Social Security Fund Act 2018, s.18(1)-(2) |
| SDL (Skills Development Levy) | 3.5% of gross emoluments | 0% | 3.5% (employer-only, 10 or more employees) | Vocational Education and Training Act, Cap 82, s.14 (headcount from Finance Act 2021 s.81); TRA, "Skills Development Levy" |
| WCF (Workers' Compensation Fund) | 0.5% of employee earnings | 0% | 0.5% (employer-only, private and public employers) | Workers Compensation Act, Cap 263, ss.74-75; WCF, "Michango" |

**Arithmetic check:** NSSF employee (10%) + employer (10%) = 20% total. PSSSF employee (5%) + employer (15%) = 20% total. SDL and WCF are employer-only — employee column is 0.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP — do not apply a rate table without residency |
| Unknown whether second employer exists | Treat as primary employment (progressive bands), flag for reviewer |
| Unknown record quality (presumptive) | Use **incomplete-records** column (higher) |
| Unknown VAT-registration status of trader | Assume VAT-registered → presumptive NOT available; flag |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown sector (public vs private) | Assume private sector (NSSF, not PSSSF) |
| Number of employees unknown (SDL) | Flag — SDL applies only at 10+ employees |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — payroll details (gross monthly salary) for an employee, OR a bank statement for the full tax year plus confirmation of business turnover for a self-employed trader; plus confirmation of **residency** (resident / non-resident) and **employment status** (single employer / second employer / self-employed).
- **Recommended** — all sales invoices/receipts, purchase invoices, NSSF/PSSSF contribution records, SDL/WCF records (if employer), prior-year ITX 201 or assessment, VAT-registration confirmation, statement of whether business records are "complete" or "incomplete".
- **Ideal** — complete income and expenditure account, asset register, provisional-tax (statement of estimated tax) payment confirmations, all employer P9/PAYE schedules, sector confirmation (public/private).
- **Refusal if minimum is missing** — SOFT WARN. No payroll or bank data at all = hard stop. Data without supporting invoices = proceed with reviewer warning: "This computation was produced from bank/payroll data alone. The reviewer must verify that every deduction is supported and that turnover/record-completeness drives the correct presumptive column."

### Refusal Catalogue

- **R-TZ-1** — Residency unknown. "Residency determines whether progressive resident bands or the 15% non-resident flat (final) rate applies. This skill cannot compute tax without confirming residency. Please confirm before proceeding."
- **R-TZ-2** — Companies, partnerships, group structures. "This skill covers resident individuals (employees and sole traders) only. Companies, partnerships, and groups file separately. Escalate to a Tanzanian tax practitioner."
- **R-TZ-3** — Zanzibar indirect taxes. "Zanzibar runs its own VAT/levy regime. PAYE bands are shared, but Zanzibar VAT and levies are out of scope. Escalate."
- **R-TZ-4** — Capital gains / property disposals. "Capital gains on investments and property require specialised analysis (resident 10% on Tanzanian shares, securities, land and buildings; non-resident 20% instalment and 30% on total income; a resident's overseas-source gains at the progressive scale). Out of scope for routine computation. Escalate."
- **R-TZ-5** — Arrears / enforcement. "Client has outstanding tax arrears or is subject to TRA enforcement. Statutory interest (the prevailing Bank of Tanzania discount rate, compounded monthly) and penalties are severe. Do not advise — escalate to a Tanzanian tax practitioner immediately."
- **R-TZ-6** — VAT return requested. "This skill covers income tax/PAYE and presumptive tax only. Tanzania VAT (standard rate 18%, registration threshold TZS 200,000,000 in twelve months or TZS 100,000,000 in six months on the Mainland) is a separate workflow."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5. Match by case-insensitive substring on the counterparty/description. Most specific match wins. Swahili terms are included because Tanzanian statements frequently mix English and Swahili.

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + MALIPO, PAYMENT, DEPOSIT, AMANA | Business income | Sole-trader turnover / revenue | If VAT-registered (Art.), extract net (excl. 18% VAT) |
| ADA, FEES, USHAURI, CONSULTANCY, PROFESSIONAL FEES | Business income | Professional fees | Typical self-employed income |
| MSHAHARA, SALARY, MISHAHARA, EMPLOYER [name] | Employment income | PAYE income | Goes to employment computation, not turnover |
| STRIPE PAYOUT, PAYPAL, WISE, FLUTTERWAVE, DPO | Business income | Platform payout | Match to underlying invoices |
| M-PESA, TIGO PESA, AIRTEL MONEY, HALOPESA (received) | Business income (if trade) | Mobile-money receipt | Verify business vs personal; mobile money is ubiquitous |
| KODI / RENT RECEIVED | Other income | Rental income | Not trading turnover |
| RIBA, INTEREST RECEIVED | Other income | Investment income |  |
| GAWIO, DIVIDEND | Other income | Investment income |  |
| TRA REFUND, MAREJESHO YA KODI | EXCLUDE | Tax refund | Prior-year refund, not income |
| RUZUKU, GOVERNMENT GRANT | Check nature | Capital grant EXCLUDE; revenue grant = income | Flag for reviewer |

### 3.2 Expense Patterns (Debits) — Fully Deductible (Self-Employed)

**Expense Patterns (Debits) — Fully Deductible (Self-Employed)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| KODI YA OFISI, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| BIMA, INSURANCE (business), PROFESSIONAL INDEMNITY | Business insurance | Deductible |  |
| MHASIBU, ACCOUNTANT, AUDIT, BOOKKEEP | Accountancy fees | Deductible |  |
| WAKILI, LAWYER, LEGAL (business) | Legal fees | Deductible | Must be business-related |
| VIFAA VYA OFISI, STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MATANGAZO, MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| MAFUNZO, TRAINING, SEMINAR, WARSHA | Training | Deductible | Must relate to current business |
| ADA YA BENKI, BANK CHARGE, CRDB CHARGE, NMB FEE | Bank charges | Deductible | Business account only |
| STRIPE FEE, M-PESA FEE, MAKATO | Transaction/processing fees | Deductible |  |

### 3.3 Expense Patterns (Debits) — Software / SaaS

**Expense Patterns (Debits) — Software / SaaS**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, ZOOM, ADOBE | Software subscription | Deductible | Recurring = operating expense |
| ANTHROPIC, OPENAI, GITHUB, CANVA, NOTION | Software subscription | Deductible |  |
| PERPETUAL SOFTWARE LICENCE (high value) | Capital item | Capitalise — capital allowances | Intangible assets are written off straight-line over their useful life (Class 7, Section 6.7); flag the useful life for the reviewer |

### 3.4 Expense Patterns (Debits) — Utilities (apportion)

**Expense Patterns (Debits) — Utilities (apportion)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| LUKU, TANESCO, UMEME, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated premises; apportion if home |
| MAJI, DAWASA, WATER | Water | T2 if home office | Apportion if home |
| VODACOM, AIRTEL, TIGO, HALOTEL, TTCL, INTERNET | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) — Travel

**Expense Patterns (Debits) — Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| PRECISION AIR, AIR TANZANIA, FLIGHT, NDEGE | Flights | Deductible if business travel | Must be wholly business |
| HOTEL, BOOKING.COM, GUEST HOUSE, NYUMBA YA WAGENI | Accommodation | Deductible if business travel |  |
| BOLT, UBER, TAXI, BAJAJI, DALADALA | Local transport | Deductible if business purpose |  |
| MAFUTA, PETROL, FUEL, ORYX, PUMA, TOTAL | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARKING, MAEGESHO | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) — NOT Deductible

**Expense Patterns (Debits) — NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| MGAHAWA, RESTAURANT, CHAKULA, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private/entertainment — flag, no partial deduction by default |
| BINAFSI, PERSONAL, GROCERIES, DUKA, SUPERMARKET | Personal expenses | NOT deductible | Private living costs |
| FAINI, FINE, PENALTY, ADHABU | Fines/penalties | NOT deductible | Public policy |
| TRA PAYMENT, INCOME TAX, KODI YA MAPATO | Tax payments | NOT deductible | Income tax cannot reduce income |
| MATUMIZI BINAFSI, DRAWINGS, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Statutory / Exclusion Patterns

**Statutory / Exclusion Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NSSF, MFUKO WA HIFADHI | Social-security contribution | Employee NSSF (10%) is deducted from gross pay before PAYE is computed (ITA s.61; TRA PAYE page) |
| PSSSF | Social-security contribution (public) | Public-sector only |
| SDL, SKILLS DEVELOPMENT LEVY | Employer levy | Employer-only (3.5%); not an employee deduction |
| WCF, WORKERS COMPENSATION | Employer levy | Employer-only (0.5%) |
| VAT PAYMENT, TRA VAT, KODI YA ONGEZEKO | EXCLUDE | VAT liability, not expense |
| PROVISIONAL TAX, STATEMENT OF ESTIMATED TAX | Credit against liability | Not an expense |
| TRANSFER KWENDA ACCOUNT YANGU, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| LOAN, MKOPO (principal) | EXCLUDE | Loan principal movement |

### 3.8 Tanzanian Banks / Payment Rails — Statement Format Reference

**Tanzanian Banks / Payment Rails — Statement Format Reference**

| Provider | Common Patterns | Notes |
| --- | --- | --- |
| CRDB Bank | TRANSFER, MALIPO, CHARGE, FT | PDF/CSV; description holds counterparty + reference |
| NMB Bank | PAYMENT, DEPOSIT, WITHDRAWAL, FEE | PDF; common nationwide |
| NBC (National Bank of Commerce) | TRF, DD, CHARGES | PDF |
| M-Pesa / Tigo Pesa / Airtel Money | C2B, B2C, PAYBILL, LIPA, MAKATO | Mobile-money statements; very common for SMEs |
| Equity / Stanbic / Absa | PAYMENT, TRANSFER, CARD | PDF/CSV |

## Section 4 -- Worked Examples

### Example 1 — Employee PAYE, gross TZS 1,500,000/month (resident)

**Input line:**
`28/03/2025 ; CRDB ; MSHAHARA MACHI 2025 ; EMPLOYER ACME LTD ; +1,500,000 ; TZS`

**Reasoning:**
Resident employee, single employer. Employee NSSF = 10% × 1,500,000 = **150,000**, deducted before PAYE (ITA s.61).
PAYE base = 1,500,000 − 150,000 = 1,350,000, in the top band (above 1,000,000).
PAYE = 128,000 + 30% × (1,350,000 − 1,000,000) = 128,000 + 30% × 350,000 = 128,000 + 105,000 = **233,000**.
Net pay = 1,500,000 − 150,000 − 233,000 = **1,117,000**.

**Classification:** PAYE = TZS 233,000; employee NSSF = TZS 150,000; net = TZS 1,117,000. (Computed on gross, as this guide did before 2026-10-11, PAYE would be 278,000; that overstates the tax by 30% of the NSSF deduction.)

### Example 2 — Employee PAYE, gross TZS 600,000/month (resident)

**Input line:**
`28/04/2025 ; NMB ; MSHAHARA ; EMPLOYER BLUE LTD ; +600,000 ; TZS`

**Reasoning:**
Employee NSSF = 10% × 600,000 = **60,000**. PAYE base = 600,000 − 60,000 = 540,000, in band 520,001–760,000.
PAYE = 20,000 + 20% × (540,000 − 520,000) = 20,000 + 20% × 20,000 = 20,000 + 4,000 = **24,000**.
Net pay = 600,000 − 60,000 − 24,000 = **516,000**.

**Classification:** PAYE = TZS 24,000; employee NSSF = TZS 60,000; net = TZS 516,000.

### Example 3 — Self-employed presumptive, turnover TZS 9,000,000, complete records

**Input:**
Resident trader, not VAT-registered, annual turnover TZS 9,000,000, maintains complete records.

**Reasoning:**
Turnover in band 7,000,001–11,000,000 (complete records).
Tax = 90,000 + 3% × (9,000,000 − 7,000,000) = 90,000 + 3% × 2,000,000 = 90,000 + 60,000 = **150,000**.

**Classification:** Presumptive tax = TZS 150,000.

### Example 4 — Self-employed presumptive, turnover TZS 9,000,000, incomplete records

**Input:**
Same trader, but records are incomplete.

**Reasoning:**
Turnover in band 7,000,001–11,000,000 (incomplete records) → flat **250,000**.

**Classification:** Presumptive tax = TZS 250,000. (Note the penalty for poor records: TZS 100,000 higher than the complete-records case in Example 3.)

### Example 5 — Self-employed presumptive, turnover TZS 50,000,000

**Input:**
Resident trader, not VAT-registered, turnover TZS 50,000,000 (records complete or incomplete — same column above 11m).

**Reasoning:**
Year of income 2025: band 11,000,001–100,000,000 → 3.5% of turnover regardless of records.
Tax = 3.5% × 50,000,000 = **1,750,000**.

**Classification:** Presumptive tax = TZS 1,750,000. From 1 July 2026 the band is 11,000,001–200,000,000 at 4.0% (Finance Act 2026 s.27): on a full year at the new rate the same turnover bears 4% × 50,000,000 = 2,000,000, and a trader with turnover of TZS 120,000,000, who was outside the regime in 2025, pays 4% × 120,000,000 = 4,800,000 instead of filing audited accounts.

### Example 6 — Non-resident employee, gross TZS 4,000,000/month

**Input line:**
`28/05/2025 ; STANBIC ; SALARY ; EMPLOYER GLOBAL LTD ; +4,000,000 ; TZS`

**Reasoning:**
Non-resident employment income → the employer withholds a flat **15%** of the gross employment income (ITA First Schedule para 4(a)(ii)); TRA treats it as final and does not require a return from a non-resident whose income is only such employment (TRA PAYE page; TRA booklet 2025/2026 section 4.0). Progressive bands do NOT apply.
Tax = 15% × 4,000,000 = **600,000**. This is final — no annual reconciliation on this employment income.

**Classification:** PAYE (final) = TZS 600,000.

### Example 7 — Mobile-money receipt (M-Pesa) for a trader

**Input line:**
`12/06/2025 ; M-PESA ; LIPA NA M-PESA / TILL ; CUSTOMER SALE ; +85,000 ; TZS`

**Reasoning:**
Till receipt = trading turnover. Include in annual turnover for presumptive/standard determination. If VAT-registered, extract net of 18% VAT.

**Classification:** Business income (turnover).

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency Drives Everything

- **Residency determines rate regime** — **Resident individual:** progressive monthly PAYE bands (Section 1). **Non-resident individual:** 15% withheld from gross employment income, treated as final (ITA First Schedule para 4(a)(ii); TRA PAYE page); other income of a non-resident individual is taxed at 30% (para 1(4)). Confirm residency before any computation.

### 5.2 PAYE Computation (Resident)

- **PAYE computation** — Deduct the employee's contribution to an approved retirement fund (NSSF or PSSSF) from gross pay, then apply the monthly bands to the remainder (ITA s.61; TRA PAYE page). Tax-free threshold = first TZS 270,000/month of that base. Top marginal rate 30% above TZS 1,000,000/month. PAYE is withheld by the employer and paid to TRA within seven days after the end of the month (ITA s.109(1); TRA).

### 5.3 Secondary Employment

- **Secondary employment withholding** — An employee with more than one employment nominates one as primary and tells the other employers; each secondary employer withholds at the **highest individual rate (30%)** on the whole payment, unless the Commissioner allows a lower rate on the employee's application for hardship (TRA, "Pay As You Earn"). Do not run the progressive bands on second-employer income; the annual return reconciles the total.

### 5.4 Presumptive vs Standard (Self-Employed)

**Presumptive vs Standard (Self-Employed)**

| Condition | Regime |
| --- | --- |
| Resident individual with only Tanzanian business income, turnover ≤ TZS 100,000,000 (year of income 2025) or ≤ TZS 200,000,000 (from 1 July 2026), not electing out | Presumptive (Section 1 turnover tables) |
| Turnover above the ceiling, income from other sources, or an election out (a VAT-registered trader keeps full accounts) | Standard net-profit regime; full accounts required, audited above TZS 100,000,000 |

Records "complete" (TAA s.43 complied with) → use the lower complete-records column; "incomplete" → higher fixed amounts (ITA First Schedule para 2(3); TRA). Above TZS 11,000,000 turnover both columns are identical: 3.5% of turnover for 2025, 4.0% from 1 July 2026.

### 5.5 Capital Gains

**Capital Gains**

| Disposer / source | Rate |
| --- | --- |
| Resident — Tanzanian shares, securities, land or buildings | 10% (ITA s.115(1)(a) single instalment; First Schedule para 1(3)(b)) |
| Non-resident — Tanzanian-source investment | 20% single instalment (s.115(1)(d)); 30% on total income (First Schedule para 1(4)) |
| Resident — overseas-source investment | Progressive scale with other income, top rate 30% (First Schedule para 1(1)) |

Out of scope for routine PAYE/turnover work — flag for specialist. The rules the review verified, for when a client does realise an investment (section numbers as cited by the reviewer, from the Revised Edition 2019; s.90 is s.115 in the 2023 edition):

- **Realisation of land or buildings — payment and notice** — The tax is a single instalment payable within 30 days of the realisation, and the Commissioner must be notified within 14 days.  _(Income Tax Act, Cap 332, s.90; Tax Administration Act, Cap 438)_
- **Resident individual without cost records** — For land or buildings, 3% of the greater of the incomings and the approved value of the asset, in place of 10% of the gain.  _(Income Tax Act, Cap 332, s.90 as amended)_
- **Exemptions (selected)** — A private residence where the gain is TZS 15,000,000 or less; agricultural land with a market value of TZS 10,000,000 or less; DSE-listed shares held by a resident, and DSE-listed shares of a non-resident holding under 25%.  _(Income Tax Act, Cap 332, s.9 and Second Schedule)_
- **Corporations** — Gains on the realisation of investments are included in income and taxed at 30%.  _(Income Tax Act, Cap 332)_

### 5.6 The Wholly-and-Exclusively Principle (Standard Regime)

- **Wholly-and-exclusively principle** — Under the standard net-profit regime, an expense is deductible only if incurred wholly and exclusively in the production of income (Income Tax Act, Cap. 332). Mixed-use expenses must be apportioned on a reasonable, documented basis. Entertainment, private living costs, fines/penalties, income tax itself, and drawings are not deductible.  _(Income Tax Act, Cap. 332)_

### 5.6.1 Losses, Donations and Administration (Standard Regime)

The remaining rules the review verified for a self-employed person under the standard regime, and the entity-level rules a sole trader meets when the business incorporates:

- **Loss carryforward** — Indefinite, but brought-forward losses shelter at most 60% of a year's taxable profit (the excess carries forward); the 60% cap does not apply to agriculture, health and education businesses.  _(Income Tax Act, Cap 332, s.19 as amended)_
- **Loss ring-fencing** — Agricultural, mining-licence-area, petroleum-licence-area, foreign-source, investment and speculative losses are offset only against income of the same category or area.  _(Income Tax Act, Cap 332, s.19)_
- **Charitable contributions** — Approved charitable or social-development contributions are deductible up to 2% of taxable income before the deduction; Education Fund, LGA statutory community obligations and AIDS Trust Fund contributions are also deductible.  _(Income Tax Act, Cap 332, s.16)_
- **Alternative minimum tax (entities)** — 1% of turnover for an entity with unrelieved tax losses in the current and the two preceding years of income; it does not apply to an individual.  _(Income Tax Act, Cap 332, AMT provisions as amended by Finance Act 2025, in force 1 July 2025)_
- **Extractive-sector service fees** — 10% final withholding on technical and management services a resident provides to mining, oil and gas entities (5% before Finance Act 2025).  _(Income Tax Act, Cap 332, as amended by Finance Act 2025)_
- **Digital services and assets** — A non-resident provider of electronic services pays a digital service tax of 2% of turnover excluding VAT, with a monthly return and payment by the 20th of the following month; payments to residents for the exchange or transfer of digital assets bear 3% withholding, deducted by the platform owner or facilitator (a non-resident platform registers under the simplified regime).  _(Income Tax Act, Cap 332; Income Tax (Registration of Non-Resident Electronic Service Suppliers) Regulations 2022; Finance Act 2024)_
- **Forest produce** — 2% of the gross payment is remitted as a single instalment before timber, logs, mirunda or poles are transported; the base is the greatest of the farm-gate price, the purchase price and the value the Tanzania Forest Services determines.  _(Income Tax Act, Cap 332, as amended by Finance Act 2025)_
- **Corporate rates (context)** — 30% standard for resident corporations and PEs; 25% for three consecutive years from a DSE listing with at least 25% of the shares issued to the public; 10% for the first five years for new assemblers of vehicles, tractors and fishing boats; 20% for the first five years for new manufacturers of pharmaceuticals or leather products under a performance agreement with the Government. Where profits are not distributed within 12 months of year-end, the Commissioner General may treat 30% of the after-tax profit as distributed, with 10% dividend withholding on the deemed distribution.  _(Income Tax Act, Cap 332, First Schedule; Finance Act 2025)_
- **Entity filing** — Statement of estimated tax within 3 months of the start of the accounting period, instalments by the end of months 3, 6, 9 and 12; final return within 6 months of the period end (9 months for public-sector entities).  _(Income Tax Act, Cap 332, ss.88–89 and s.91; Tax Administration Act, Cap 438)_
- **Certification and audit** — The return of a corporation with gross income above TZS 100,000,000, or of an individual with turnover above TZS 500,000,000, must be prepared or certified by a CPA in public practice; a sole trader with turnover of TZS 100,000,000 or more needs audited financial statements.  _(Tax Administration Act, Cap 438, as amended by Finance Act 2025)_
- **Assessments, objections and appeals** — TRA may adjust a return within 5 years of the final-return due date, with no limit for fraud, wilful neglect or serious omission (s.48). An objection needs a deposit of the higher of the tax not in dispute and one-third of the assessed tax, and Finance Act 2025 lets the Commissioner General demand 100% where the objector is a flight risk (s.51); an objection not determined within 6 months of admission is treated as confirmed and may be appealed (s.52). The route is TRA objection, then the Tax Revenue Appeals Board, the Tax Revenue Appeals Tribunal and the Court of Appeal.  _(Tax Administration Act, Cap 438, ss.48, 51 and 52; Tax Revenue Appeals Act, Cap 408)_
- **Currency and year** — Accounts are kept in TZS unless the Commissioner permits a convertible foreign currency on written application; the year of income is the calendar year, and an entity may apply to use its own accounting period.  _(Income Tax Act, Cap 332, ss.20–21; Tax Administration Act, Cap 438)_

### 5.7 Statutory Contributions

**Statutory Contributions**

| Contribution | Rate | Who pays | Source |
| --- | --- | --- | --- |
| NSSF (private) | 20% of wages | Employer and employee shares at the First Schedule percentages: the share deductible from wages is at most 10%, so the employer bears at least 10% (10/10 is the norm; the employer may bear more, up to all 20%) | NSSF Act, Cap 50, ss.12-13 and First Schedule; NSSF, "Rate of Contributions" |
| PSSSF (public) | 20% of monthly salary | 5% deducted from the member's salary, 15% contributed by the employer, unless the Minister varies the amounts by order after an actuarial valuation | PSSSF Act 2018, s.18(1)-(2) |
| SDL | 3.5% of gross monthly emoluments | Employer-only; applies to employers with **10 or more employees**; monthly return through IDRAS and payment on form ITX 300.01.E by the 7th of the following month; a half-year certificate reconciles the monthly returns | VETA Act, Cap 82, s.14 (Finance Act 2021 s.81 for the headcount); TRA, "Skills Development Levy" |
| WCF | 0.5% of employee earnings (basic salary plus fixed allowances) | Employer-only, private and public employers alike; paid through the WCF portal within the month or the following month | Workers Compensation Act, Cap 263, ss.74-75; WCF, "Michango" |

**NSSF basis:** the Act applies the percentages to every complete shilling of wages and sets **no ceiling or floor** on the contributory wage (NSSF Act First Schedule). SDL exemptions (TRA SDL page; VETA Act s.19): Government departments and institutions wholly financed by the Government, diplomatic missions, the UN and its organisations, foreign aid and technical-assistance institutions, religious institutions whose employees only administer places of worship, give religious instruction or provide public health, charitable organisations with a TAA s.11 ruling, registered educational institutions from nursery schools to universities, local government authorities, TAESA-programme interns and farm employers whose employees are directly and solely engaged in farming. WCF: 0.5% applies to both sectors; a WCF statement showing a different amount is arrears, an assessment or interest.

### 5.8 Filing Forms and Deadlines (ITA / TRA)

**Filing Forms and Deadlines**  _(ITA ss.109, 113, 114, 117 and 118 (Revised Edition 2023); TRA, "Income Tax for Individuals"; TRA booklet 2025/2026 section 9.0)_

| Item | Detail |
| --- | --- |
| PAYE monthly remittance + return | Tax withheld in a month is paid within seven days after the end of the month, with the monthly withholding statement (ITA s.109(1)-(2), as amended by Finance Act 2021 s.24); TRA's calendar states the 7th of the following month |
| SDL / WHT monthly returns | Same 7th-day deadline (TRA SDL and withholding pages) |
| Individual annual return | Form **ITX 201.01.E** ("Return of Income — Individual"); due within 6 months after the end of the year of income (ITA s.117) → file between 1 January and **30 June** (TRA) |
| Who must file the annual return | Everyone except a resident individual with no tax payable or whose income is only employment income withheld under s.104 from one employer (or final withholding payments), and a non-resident with no tax payable beyond such withholding (ITA s.118). Business, self-employed, multiple-employer and investment income therefore require a return. |
| Statement of estimated tax (provisional) | Form ITX 200.01.E, due by the first instalment date, within 3 months of the start of the year of income (by **31 March**); the estimated tax is paid in instalments on or before 31 March, 30 June, 30 September and 31 December (ITA ss.113-114; TRA). An instalment is nil when the estimated tax for the year is TZS 50,000 or less or the instalment is TZS 12,500 or less (s.113(4)). |

### 5.9 Registration Thresholds

**Registration Thresholds**

| Item | Threshold | Source |
| --- | --- | --- |
| TIN | Required for all taxpayers / anyone in business (obtain before trading) | TAA s.22; TRA |
| Presumptive eligibility | Turnover ≤ TZS 100,000,000 for the year of income 2025; ≤ TZS 200,000,000 from 1 July 2026 | ITA First Schedule para 2(2); Finance Act 2026 s.27 |
| VAT registration (Mainland) | TZS 200,000,000 of taxable turnover in twelve months, or TZS 100,000,000 in six months; apply within 30 days of becoming liable | VAT Act, Cap 148, s.28 (threshold set by regulations); TRA, "Value Added Tax (VAT)" |
| VAT registration (Zanzibar) | TZS 100,000,000, with VAT at 15% | TRA booklet 2025/2026 sections 10.5-10.6 |
| VAT — professional service providers (accountants, lawyers, engineers) | Must register regardless of turnover | VAT Act s.29(1); TRA VAT page |
| VAT standard rate | 18% | TRA VAT page |

### 5.10 Penalties and Interest (TRA)

**Penalties and Interest**  _(TAA ss.3, 4, 76, 77, 78 and 79; TRA, https://www.tra.go.tz/page/interest-penalties-offences)_

| Default | Charge |
| --- | --- |
| Late filing or late payment (per month / part-month) | HIGHER of 2.5% of (tax assessed − tax paid), OR 5 currency points (TZS 100,000) for an individual / 15 currency points (TZS 300,000) for a body corporate; the estimate and the final return are penalised separately (TAA s.78) |
| Underestimation / late payment | Interest at the statutory rate, compounded monthly (TAA s.76); the statutory rate is the prevailing discount rate determined by the Bank of Tanzania (TAA s.3; ITA s.3), so read it off the Bank of Tanzania for the period rather than quoting a fixed figure |
| Failure to maintain documents | 1 currency point (TZS 20,000) individual / 10 currency points (TZS 200,000) corporate (TAA s.77) |
| False or misleading statement | 50% of the tax shortfall without reasonable excuse; 100% of the shortfall (or 30% of the adjusted loss) when made knowingly or recklessly; plus 10% on a repeat, less 10% on voluntary disclosure (TAA s.79 as amended; TRA) |

- **Currency point** — TZS 20,000, the value the Minister has set by order under TAA s.4(4) (the Act's Second Schedule started at TZS 15,000)  _(TRA, https://www.tra.go.tz/page/interest-penalties-offences)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction (Standard Regime)

- **Home office deduction** — Apportion rent, electricity (LUKU/TANESCO), water, internet by the proportion of the dwelling genuinely used for business. Dual-use space does not qualify. **Conservative default:** 0% until reviewer confirms a dedicated workspace and basis.

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible; requires a mileage log. **Conservative default:** 0% business use until log provided.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use** — Business-use portion only; reasonable documented estimate required. **Conservative default:** 0% until business percentage confirmed.

### 6.4 Records Completeness (Presumptive)

- **Records completeness** — Whether a trader's records are "complete" determines the column used (Examples 3 vs 4 — a TZS 100,000 swing on TZS 9,000,000 turnover). Reviewer must judge whether records genuinely support the complete-records column.

### 6.5 Employee NSSF Treatment in PAYE Base

- **Employee NSSF treatment** — Settled: the employee's contribution to an approved retirement fund reduces the PAYE base (ITA s.61; TRA PAYE page). The reviewer's call is whether a fund is "approved" and whether the contribution exceeds the statutory amount (only the statutory amount is deductible); a voluntary top-up above the statutory 10% does not reduce PAYE.

### 6.6 SDL Headcount Threshold

- **SDL headcount threshold** — SDL applies only to employers with **10 or more** employees. Reviewer must confirm headcount before applying or omitting the 3.5% levy. Confirm exemption status (schools/universities/religious-run health).

### 6.7 Capital Allowances / Depreciation (Standard Regime)

**Depreciation classes and rates**  _(Income Tax Act, Cap 332, Third Schedule)_

| Class | Rate and method | Assets |
| --- | --- | --- |
| 1 | 37.5% reducing balance | Computers and data-handling equipment; automobiles, buses and minibuses of fewer than 30 passengers; goods vehicles under 7 tonnes; construction and earth-moving equipment |
| 2 | 25% reducing balance | Buses of 30 passengers or more; heavy and specialised trucks and trailers; rail, vessels and aircraft; plant and machinery used in agriculture or manufacturing; public utility plant |
| 3 | 12.5% reducing balance | Office furniture, fixtures and equipment; any asset not in another class |
| 5 | 20% straight line | Buildings, dams and fences used in agriculture, livestock or fish farming |
| 6 | 5% straight line | Other buildings and structures |
| 7 | Straight line over useful life | Intangible assets |
| 8 | 100% | Plant and machinery used in agriculture; electronic fiscal devices bought by non-VAT-registered traders |

- **Enhanced allowance** — Manufacturing, fish farming and tourist hotels: a 50% allowance on qualifying plant and machinery, taken equally in the first and second years, with the normal class rate on the remaining balance thereafter.  _(Income Tax Act, Cap 332, Third Schedule)_
- **Mineral and petroleum operations** — Expenditure is written off at 20% a year, straight line.  _(Income Tax Act, Cap 332, Third Schedule)_
- **Reviewer judgement** — Which class an asset falls in (a pickup under 7 tonnes is Class 1, a specialised truck Class 2) and whether plant is "used in" agriculture or manufacturing are reviewer calls; the rates are not.

## Section 7 -- Excel Working Paper Template

```
TANZANIA INCOME TAX -- WORKING PAPER
Tax Year: 2025 (calendar)
Client: ___________________________
Residency: Resident / Non-resident
Type: Employee / Self-employed (presumptive) / Self-employed (standard)
Sector (if employee): Private (NSSF) / Public (PSSSF)

=== A. EMPLOYEE PAYE (monthly) ===
  A1. Gross monthly emoluments                 ___________
  A2. Employee NSSF / PSSSF (10% / 5% of A1)   ___________
  A3. PAYE base (A1 - A2)                      ___________
  A4. Band applied (per Section 1)             ___________
  A5. PAYE (resident bands on A3, OR 15% of A1 non-res) ___________
  A6. Net pay (A1 - A2 - A5)                   ___________

=== B. EMPLOYER LEVIES (employer-only) ===
  B1. Employer NSSF (10% of gross)             ___________
  B2. SDL (3.5% of gross; 10+ employees)       ___________
  B3. WCF (0.5% of cash sums, private)         ___________

=== C. SELF-EMPLOYED PRESUMPTIVE ===
  C1. Annual turnover                          ___________
  C2. VAT-registered? (Y → not presumptive)    ___________
  C3. Records complete? (Y/N)                  ___________
  C4. Presumptive tax (per turnover table)     ___________

=== D. SELF-EMPLOYED STANDARD (turnover > 100m or VAT-reg) ===
  D1. Turnover (net of VAT if registered)      ___________
  D2. Allowable expenses (wholly & exclusively)___________
  D3. Capital allowances [class/rate – review] ___________
  D4. Net profit (D1 - D2 - D3)                ___________
  D5. Tax (pass to deterministic engine)       ___________

=== E. FILING ===
  E1. Annual return ITX 201.01.E required?     ___________
  E2. Provisional tax (statement of est. tax)  ___________
  E3. Deadline annual return: 30 June          ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Second employer? (withheld at the top rate at source)
  [ ] Sector confirmed (NSSF vs PSSSF)?
  [ ] Retirement contribution deducted before PAYE, at no more than the statutory amount?
  [ ] SDL headcount (10+) confirmed?
  [ ] Records completeness confirmed (presumptive)?
  [ ] Presumptive ceiling for the period (100m to 30 June 2026; 200m after) confirmed?
  [ ] VAT-registration status confirmed?
  [ ] Capital allowance class confirmed for each asset?
  [ ] Entertainment / personal / fines excluded?
```

## Section 8 -- Bank Statement Reading Guide

### Tanzanian Statement Formats

**Tanzanian Statement Formats**

| Provider | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| CRDB Bank | PDF, CSV | Date, Description, Debit, Credit, Balance | Description holds counterparty + reference |
| NMB Bank | PDF | Date, Particulars, Withdrawal, Deposit, Balance | Nationwide; shorter descriptions |
| NBC | PDF | Date, Narrative, Debit, Credit |  |
| M-Pesa / Tigo Pesa / Airtel Money | PDF, CSV | Date, Details, Paid In, Withdrawn, Balance | Mobile-money — critical for SMEs; includes MAKATO (fees) |
| Stanbic / Absa / Equity | PDF, CSV | Date, Description, Amount, Balance | Card transactions show merchant |

### Key Swahili / Local Banking Terms

**Key Swahili / Local Banking Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| MSHAHARA | Salary | Employment income (PAYE) |
| MALIPO | Payment | Check direction (income / expense) |
| AMANA / HLAS | Deposit | Potential income |
| MAKATO | Charges / deduction | Bank/transaction fee (deductible if business) |
| KODI | Tax OR rent | Disambiguate: "kodi ya mapato" = income tax; "kodi ya nyumba" = rent |
| RIBA | Interest | Interest income / charge |
| GAWIO | Dividend | Investment income |
| MKOPO | Loan | Exclude principal |
| FAINI / ADHABU | Fine / penalty | NOT deductible |
| LUKU | Prepaid electricity token | Utility (apportion) |
| LIPA NA M-PESA / TILL | Merchant till receipt | Trading turnover |
| MAREJESHO | Refund | Check nature (tax refund = exclude) |

## Section 9 -- Onboarding Fallback

If the client provides data but cannot answer all onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present these questions:

```
ONBOARDING QUESTIONS -- TANZANIA INCOME TAX
1. Are you resident or non-resident in Tanzania for tax?
2. Are you an employee, self-employed, or both?
3. (Employee) Do you have a second employer? (second job = 30% flat at source)
4. (Employee) Private or public sector? (NSSF vs PSSSF)
5. (Self-employed) What is your annual turnover?
6. (Self-employed) Are you VAT-registered? Are your records complete?
7. (Employer) Do you have 10 or more employees? (SDL applies at 10+)
8. Did you pay any provisional tax (statement of estimated tax)?
9. Any other income (rental, interest, dividends, second employment)?
10. Any capital assets purchased during the year?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference |
| --- | --- |
| Income Tax Act, Cap 332, Revised Edition 2023 (TRA copy): s.7 employment income, s.27 and Fifth Schedule benefits, s.61 retirement contributions, s.104 withholding by employers, s.109 payment of tax withheld, s.113-114 instalments and estimate, s.115 single instalment on realisation, s.117-118 returns, First Schedule rates, Third Schedule depreciation | TRA — https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf (Revised Edition 2019 text with the 2019 numbering on TanzLII: https://tanzlii.org/akn/tz/act/2004/11) |
| Finance Act 2021 (s.25: current PAYE scale; s.81: SDL headcount of 10) | TanzLII — https://media.tanzlii.org/media/legislation/47415/source_file/40650f45f1377e7d/tz-act-2021-3-publication-document.pdf |
| Finance Act 2026 (s.27: presumptive ceiling TZS 200,000,000 and 4% band, new-trader relief) and Income Tax (Presumptive Tax Relief for New Traders) Regulations 2026, GN 158B | TRA — https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf ; https://www.tra.go.tz/images/uploads/acts/GN158B-THE_INCOME_TAX_%28PRESUMPTIVE_TAX_RELIEF_FOR_NEW_TRADERS%29_REGULATIONS%2C_2026_%281%29-TGPA.pdf |
| PAYE bands, presumptive tax, filing calendar | TRA, "Income Tax for Individuals" — https://www.tra.go.tz/page/income-tax-for-individuals |
| PAYE base (retirement contributions), secondary employment, non-resident and directors' rates | TRA, "Pay As You Earn" — https://tra.go.tz/page/pay-as-you-earn |
| Rates booklet (PAYE, benefits in kind, SDL, presumptive and transport amounts, filing, depreciation, VAT thresholds) | TRA, "Taxes and Duties at a Glance 2025/2026" (July 2025) — https://www.tra.go.tz/images/uploads/pages/TAXES_AND_DUTIES_AT_A_GLANCE_2025_2026.pdf |
| NSSF contributions (20%, employee share at most 10%, payment within one month, 5% monthly penalty) | National Social Security Fund Act, Cap 50, ss.12-14 and First Schedule — https://media.tanzlii.org/media/legislation/316707/source_file/2147b8a1005295b8/1997-28.pdf ; NSSF — https://www.nssf.go.tz/pages/rate-of-contributions |
| PSSSF contributions (20%: 5% employee, 15% employer) | Public Service Social Security Fund Act 2018, s.18 — https://tanzlii.org/akn/tz/act/2018/2 |
| SDL (3.5%, 10 or more employees, exemptions) | VETA Act, Cap 82, ss.14 and 19; TRA — https://www.tra.go.tz/page/skills-development-levy-sdl |
| WCF (0.5%, both sectors, deadline, 2% interest) | Workers Compensation Act, Cap 263, ss.74-75 — https://tanzlii.org/akn/tz/act/2008/20 ; WCF — https://www.wcf.go.tz/pages/contribution |
| Minimum wage order (sectoral rates from 1 January 2026) | Labour Institutions (Minimum Wage for Private Sector) Order, 2025, GN 605A/2025 — https://tanzlii.org/akn/tz/act/gn/2025/605a |
| VAT (registration thresholds, professionals, 18%) | VAT Act, Cap 148, ss.28-29 — https://tanzlii.org/akn/tz/act/2014/5 ; TRA — https://www.tra.go.tz/page/value-added-tax-vat |
| Penalties / interest (TAA ss.3, 4, 76-79; currency point) | Tax Administration Act, Cap 438 — https://tanzlii.org/akn/tz/act/2015/10 ; TRA — https://www.tra.go.tz/page/interest-penalties-offences |

### Minimum Wage (Employment-Law Context — NOT a Tax Figure)

Source: Labour Institutions (Minimum Wage for Private Sector) Order, 2025 — https://tanzlii.org/en/akn/tz/act/gn/2025/605a/eng@2025-10-13.

- New private-sector wage order in force from **1 January 2026** (replaces the 2022 order); average increase ~33.4%.
- Lowest sectoral minimum: **TZS 175,000/month** (e.g. agriculture). Sector rates range up to ~TZS 644,000 (telecoms) and higher (~765,900 for international mining/energy).
- Prior 2022 benchmark (through end of 2025): ~TZS 275,060/month.
- Public-sector minimum wage raised to TZS 500,000/month in 2025 (reported by TanzaniaInvest; the private-sector order GN 605A/2025 does not cover public servants) [RESEARCH GAP — reviewer to confirm against the public-service circular].

### Test Suite

Input: resident employee, gross TZS 1,500,000/month, NSSF 10%.
Expected: employee NSSF = 150,000; PAYE base = 1,350,000; PAYE = 128,000 + 30%×(1,350,000−1,000,000) = **233,000**; net = **1,117,000**.

Input: resident employee, gross TZS 600,000/month, NSSF 10%.
Expected: employee NSSF = 60,000; PAYE base = 540,000; PAYE = 20,000 + 20%×(540,000−520,000) = **24,000**; net = **516,000**.

Input: resident employee, gross TZS 300,000/month, NSSF 10%.
Expected: employee NSSF = 30,000; PAYE base = 270,000; PAYE = **0** (top of the NIL band); on gross, without the deduction, it would have been 2,400.

Input: resident employee, gross TZS 270,000/month, NSSF 10%.
Expected: PAYE base = 243,000; PAYE = **0** (NIL band).

Input: trader, turnover TZS 9,000,000, complete records, not VAT-registered.
Expected: 90,000 + 3%×(9,000,000−7,000,000) = **150,000**.

Input: same trader, incomplete records.
Expected: flat **250,000**.

Input: trader, turnover TZS 50,000,000, year of income 2025.
Expected: 3.5%×50,000,000 = **1,750,000**. On a full year at the Finance Act 2026 rate: 4%×50,000,000 = **2,000,000**.

Input: non-resident, gross TZS 4,000,000/month.
Expected: 15%×4,000,000 = **600,000** (withheld under ITA First Schedule para 4(a)(ii); final per TRA).

Expected: NSSF employee 10% + employer 10% = **20%**; PSSSF employee 5% + employer 15% = **20%**.

Input: trader, turnover TZS 120,000,000, year of income 2025.
Expected: presumptive NOT available (ceiling 100,000,000); standard net-profit regime, audited accounts required. From 1 July 2026 the ceiling is 200,000,000 and the same turnover bears 4%×120,000,000 = **4,800,000** under the presumptive regime.

## PROHIBITIONS

- NEVER apply a rate table without confirming residency.
- NEVER compute PAYE on gross pay -- deduct the employee's statutory NSSF or PSSSF contribution first (ITA s.61).
- NEVER run progressive bands on non-resident employment income (15% flat, final) or on second-employer income (withheld at the top rate at source).
- NEVER use the complete-records presumptive column without confirming records are genuinely complete — default to the higher incomplete-records column.
- NEVER treat a VAT-registered trader, or turnover above the ceiling for the period (TZS 100,000,000 to 30 June 2026; TZS 200,000,000 from 1 July 2026), as eligible for presumptive tax.
- NEVER deduct an employee's PAYE, fines/penalties, entertainment, private living costs, or drawings as a business expense.
- NEVER treat SDL or WCF as an employee deduction — they are employer-only levies.
- NEVER apply SDL without confirming the employer has 10 or more employees.
- NEVER state the statutory interest rate as a fixed number — it is the prevailing Bank of Tanzania discount rate, compounded monthly (TAA ss.3 and 76).
- NEVER include VAT collected on sales in turnover/income for a VAT-registered trader.
- NEVER present tax calculations as definitive — always label as estimated and flag all [RESEARCH GAP] items for the reviewer.

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
