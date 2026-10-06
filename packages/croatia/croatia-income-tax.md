---
name: croatia-income-tax
description: Use this skill whenever asked about Croatia (Hrvatska) personal income tax (porez na dohodak) for self-employed individuals and employees. Trigger on phrases like "how much tax do I pay in Croatia", "porez na dohodak", "godišnja porezna prijava", "osobni odbitak", "personal allowance Croatia", "obrt tax", "paušalni obrt", "JOPPD", "DOH form", "PO-SD", "doprinosi", "mirovinsko", "net salary Croatia", "neto plaća", "self-employed Croatia", "sole trader Croatia", "prirez", or any question about computing or filing personal income tax for an individual or sole trader (obrtnik) in Croatia. Also trigger when preparing or reviewing a payroll net-pay computation, an annual income tax return, or advising on the lump-sum (paušalni) regime. This skill covers progressive PIT rates (default 20%/30% with local-unit ranges), final/flat income taxes (12%/24%/36%), the personal allowance and dependant coefficients, employee and self-employed contributions (pension 20% + health 16.5%), the JOPPD/DOH/PO-SD forms, and penalties. ALWAYS read this skill before touching any Croatian income tax work.
version: 0.2
jurisdiction: HR
tax_year: 2025
last_updated: 2026-10-06
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Croatia Personal Income Tax -- Individuals & Self-Employed

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Croatia (Republika Hrvatska) |
| Tax | Personal Income Tax (porez na dohodak) |
| Currency | EUR only (Croatia adopted the euro on 1 January 2023) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Zakon o porezu na dohodak (Personal Income Tax Act) |
| Supporting legislation | Zakon o doprinosima (Contributions Act); Naredba o iznosima osnovica za obračun doprinosa za 2025. godinu (NN 137/2024); Zakon o minimalnoj plaći (Minimum Wage Act) |
| Tax authority | Ministarstvo financija -- Porezna uprava (Croatian Tax Administration), https://porezna-uprava.gov.hr |
| Pension administration | Hrvatski zavod za mirovinsko osiguranje (HZMO) |
| Health administration | Hrvatski zavod za zdravstveno osiguranje (HZZO) |
| Filing portal | ePorezna (Porezna uprava e-services) |
| Annual return deadline | End of February of the following year (self-employed; most employees auto-assessed) |
| Validated by | Pending -- requires sign-off by a Croatian tax adviser (porezni savjetnik) / ovlašteni računovođa |
| Validation date | Pending |
| Skill version | 0.2 |

### Tax Rate Brackets (2025)

- **Annual vs final income split** — Croatia splits income into annual income (employment, self-employment, other) taxed progressively and reconciled annually, and final income (capital, property, certain other) taxed at flat rates and not aggregated.  _(PwC, Income determination)_
- **Local surtax abolished** — Local surtax (prirez) was abolished from 1 January 2024 and folded into the income-tax rate ranges.  _([ZPD amendment NN 114/2023, in force 1 January 2024: surtax references deleted, art. 19.a added](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1609.html))_

**Default progressive rates (annual income)**  _(porezna-uprava.gov.hr/en/income-tax/7363; [ZPD arts. 19 and 19.a, as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html): EUR 60,000.00 a year, EUR 5,000.00 a month under art. 24(3), and 20% / 30% where the local unit adopts no decision)_

| Annual taxable income (EUR) | Monthly equivalent (EUR) | Default rate | Cumulative tax at top |
| --- | --- | --- | --- |
| 0 -- 60,000.00 | 0 -- 5,000.00 | 20% | EUR 12,000.00 |
| 60,000.01+ | 5,000.01+ | 30% | -- |

**Local-unit statutory rate ranges**  _([ZPD arts. 19 and 19.a, as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html), art. 19.a(2))_

| Unit type | Lower rate range | Higher rate range |
| --- | --- | --- |
| Municipality (općina) | 15% -- 20% | 25% -- 30% |
| Town (grad) | 15% -- 21% | 25% -- 31% |
| Large city (veliki grad) or county seat | 15% -- 22% | 25% -- 32% |
| City of Zagreb | 15% -- 23% | 25% -- 33% |

**Final / flat income (not aggregated into the annual assessment)**  _(ZPD arts. 57(1), 62 and 70 ([consolidated text, NN 115/16 to 152/24](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak)) for the 12%, 24% and 36% rates and the 30% rental expense allowance; PwC, Income determination for the seasonal-work and undeclared-assets rows)_

| Category | Rate | Notes |
| --- | --- | --- |
| Capital income -- interest, dividends, capital gains | 12% | Final tax |
| Rental / lease of immovable & movable property | 12% | After a 30% lump-sum expense deduction |
| Grant of own shares / stock options (capital) | 24% |  |
| Property rights; disposal of property and rights | 24% |  |
| Withdrawal of assets / use of services (hidden distributions) | 36% |  |
| Seasonal agricultural work (other income) | 10% |  |
| Undeclared assets difference | 36% | Plus 100% penalty surcharge |

Note (2026): The 2026 contribution base caps have been increased (see Section 5.4). The EUR 60,000 threshold and the EUR 600 monthly allowance are unchanged for 2026: the consolidated Income Tax Act on zakon.hr, read on 6 October 2026 with the database current to NN 104/2026, lists NN 152/2024 (in force 1 January 2025) as its last amendment (https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak). Use 2025 figures for a 2025 computation.

### Personal Allowance and Dependant Coefficients (2025)

- **Basic monthly personal allowance** — EUR 600.00/month = EUR 7,200.00/year, coefficient 1.0, raised from EUR 560 in 2024  _([ZPD art. 14(1) and (3), as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html))_

**Dependant coefficients**  _([ZPD art. 14(1) and (3), as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html))_

| Dependant | Coefficient | Monthly allowance (EUR) | Annual allowance (EUR) |
| --- | --- | --- | --- |
| Basic (taxpayer) | 1.0 | 600.00 | 7,200.00 |
| 1st child | 0.5 | 300.00 | 3,600.00 |
| 2nd child | 0.7 | 420.00 | 5,040.00 |
| 3rd child | 1.0 | 600.00 | 7,200.00 |
| 4th child | 1.4 | 840.00 | 10,080.00 |
| 5th child | 1.9 | 1,140.00 | 13,680.00 |
| 6th child | 2.5 | 1,500.00 | 18,000.00 |
| 7th child | 3.2 | 1,920.00 | 23,040.00 |
| 8th child | 4.0 | 2,400.00 | 28,800.00 |
| 9th child | 4.9 | 2,940.00 | 35,280.00 |
| Dependent immediate family member | 0.5 | 300.00 | 3,600.00 |
| Disability (taxpayer, each dependant or child) | 0.3 | 180.00 | 2,160.00 |
| 100% disability, or care allowance / personal disability allowance / inclusion allowance (replaces the 0.3 row) | 1.0 | 600.00 | 7,200.00 |

For the 10th and each further child, art. 14(3) row 11 says the coefficient rises progressively by 1.1 and more over the previous child's, with the sequence elided in the published text. [RESEARCH GAP -- reviewer to confirm] the coefficient for a 10th or later child with Porezna uprava before using it.

- **Dependant income cap** — A person qualifies as a dependant only if their own annual income does not exceed EUR 3,600.00. Receipts that are not taxed or not treated as income count towards the limit too, except social assistance, child benefit, the minimum maternity and parental payment and newborn grants (art. 17(2)). The earlier EUR 3,360.00 was six times the 2024 allowance of EUR 560  _(ZPD art. 17(1): six times the art. 14(1) basic allowance a year ([consolidated text](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak); allowance set by [NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html)))_

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown local self-government unit (municipality) | Use default rates 20% / 30% -- do NOT guess a local rate |
| Unknown whether income is "annual" or "final" | Treat as annual (progressive) -- never silently apply a flat rate |
| Contribution base caps | Use 2025 figures: monthly EUR 10,788.00, annual first-pillar EUR 129,456.00 (NOT the 2026 EUR 11,958 figure) |
| Unknown dependants | Apply only the basic EUR 600/month allowance |
| Unknown salary-relief band | Compute the low-salary pension relief explicitly from the gross figure |
| Health contribution | Always an employer on-cost (16.5%), never deducted from employee net |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown sole-trader regime | Determining-income obrt (full books), NOT paušalni |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable -- for an employee: gross monthly salary (bruto plaća), number/type of dependants, and the local self-government unit (municipality) OR explicit instruction to use default rates. For a sole trader: bank statement for the full tax year (CSV, PDF, or pasted text), the obrt regime (determining-income vs paušalni), and dependant details.

Recommended -- prior-year annual return or assessment, all sales invoices, purchase invoices/receipts, JOPPD records, confirmation of pension pillar membership (most under-40s are in both pillar I + II), VAT registration status (relevant at the EUR 60,000 turnover threshold).

Ideal -- complete income & expenditure ledger (knjiga primitaka i izdataka), asset register, contribution-payment confirmations, confirmation of local-unit rate decision, age (for any youth PIT relief).

Refusal if minimum is missing -- SOFT WARN. For a sole trader, no bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from a bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that contributions, allowances, and the correct local-unit rate have been applied."

### Refusal Catalogue

- **R-HR-1** — Croatian PIT rates vary by municipality within statutory ranges (15-23% / 25-33%). Where the exact local rate materially changes the answer and the municipality is unknown, this skill defaults to 20% / 30% and flags the assumption. Confirm the taxpayer's jedinica lokalne samouprave for a precise figure.  _(R-HR-1)_
- **R-HR-2** — This skill covers individuals and sole traders (obrt) only. d.o.o. / j.d.o.o. companies pay corporate profit tax (porez na dobit) and file separate returns. Escalate to a Croatian tax adviser.  _(R-HR-2)_
- **R-HR-3** — Non-resident and dual-resident taxation and treaty relief have different rules. Out of scope. Escalate to a Croatian tax adviser.  _(R-HR-3)_
- **R-HR-4** — Capital gains, dividend, and property-disposal computations are final-taxed at flat rates (12% / 24% / 36%) and are not aggregated. Confirm the precise category before applying a rate; complex disposals should be escalated.  _(R-HR-4)_
- **R-HR-5** — Undeclared-asset differences are taxed at 36% with a 100% penalty surcharge, plus default interest. Do not advise. Escalate to a Croatian tax adviser immediately.  _(R-HR-5)_
- **R-HR-6** — This skill covers personal income tax only. For Croatian VAT (PDV), use the croatia-vat-return skill. For detailed payroll mechanics, see croatia-payroll; for contributions, croatia-social-contributions.  _(R-HR-6)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier for a sole trader's (obrt) bank statement. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the statement. Croatian descriptions are common; English equivalents are given. If multiple patterns match, use the most specific. If none match, fall through to Tier 1.

### 3.1 Income Patterns (Credits / Uplate)

**Income Patterns table**

| Pattern | Ledger line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + UPLATA, DOZNAKA, PLAĆANJE, TRANSFER | Business receipt (primitak) | Business income | If VAT-registered, extract net (excl. 25% PDV) |
| HONORAR, NAKNADA, USLUGA, RAČUN [number] | Business receipt | Business income | Professional fee -- typical for obrt |
| STRIPE PAYOUT, STRIPE TRANSFER | Business receipt | Business income | Platform payout -- match to invoices |
| PAYPAL, WISE, REVOLUT PAYOUT | Business receipt | Business income | Verify business vs personal account |
| UPWORK, FIVERR, TOPTAL | Business receipt | Business income | Freelance platform -- net of commission |
| PLAĆA, NETO PLAĆA, POSLODAVAC [name] | Other income (employment) | Employment income | NOT obrt income -- separate annual-income source |
| NAJAMNINA, ZAKUPNINA, RENT RECEIVED | Final income (rental) | Rental -- 12% after 30% deduction | Final-taxed; not aggregated |
| KAMATE, INTEREST | Final income (capital) | Interest -- 12% final |  |
| DIVIDENDA, DIVIDEND | Final income (capital) | Dividend -- 12% final |  |
| POVRAT POREZA, TAX REFUND | EXCLUDE | Not income | Prior-year refund |
| POTPORA, GRANT, HZZ POTPORA | Check nature | Capital grant EXCLUDE; revenue grant = receipt | Verify grant type |

### 3.2 Expense Patterns (Debits / Isplate) -- Fully Deductible

**Expense Patterns Fully Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| NAJAMNINA UREDA, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| OSIGURANJE (poslovno), PROFESSIONAL INDEMNITY | Business insurance | Deductible | Business cover only |
| KNJIGOVODSTVO, RAČUNOVODSTVO, ACCOUNTANT | Accountancy fees | Deductible |  |
| ODVJETNIK, LAWYER, JAVNI BILJEŽNIK (business) | Legal/notary fees | Deductible | Must be business-related |
| UREDSKI MATERIJAL, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, OGLAŠAVANJE | Marketing/advertising | Deductible |  |
| EDUKACIJA, TEČAJ, SEMINAR, CPD | Training | Deductible | Must relate to current business |
| ČLANARINA, KOMORA (HOK, HGK) | Professional subscriptions | Deductible | Chamber membership |
| NAKNADA BANCI, BANK FEE, TROŠAK VOĐENJA | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, NAKNADA | Payment processing fees | Deductible |  |
| DOMENA, HOSTING, AWS, CLOUDFLARE | IT infrastructure | Deductible | Recurring = expense |

### 3.3 Expense Patterns -- SaaS and Software

**SaaS and Software table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| PERPETUAL LICENCE (high value) | Capital item | Depreciate | Flag for reviewer -- capitalisation threshold |

### 3.4 Expense Patterns -- Utilities (may need apportionment)

**Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| HEP, ELEKTRA, STRUJA | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| VODOOPSKRBA, VODA | Water | T2 if home office | Apportion if home |
| HRVATSKI TELEKOM, A1, TELEMACH, OPTIMA | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| MOBILNI, MOBILE | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns -- Travel

**Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| CROATIA AIRLINES, RYANAIR, WIZZ AIR, EASYJET | Flights | Deductible if business travel | Must be wholly business |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| BOLT, UBER, TAKSI, TAXI | Local transport | Deductible if business purpose |  |
| GORIVO, INA, PETROL, BENZIN | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING, PARKIRANJE, ZSC | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns -- NOT Deductible / Restricted

**Not Deductible / Restricted table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORAN, RUČAK, VEČERA, REPREZENTACIJA | Entertainment/representation | Restricted -- partly blocked | Reprezentacija is partly non-deductible -- flag for reviewer (see 6.4) |
| OSOBNO, NAMIRNICE, KONZUM, LIDL, PLODINE | Personal/groceries | NOT deductible | Private living costs |
| KAZNA, GLOBA, PENAL | Fines/penalties | NOT deductible | Public policy |
| PLAĆANJE POREZA, INCOME TAX | Tax payments | NOT deductible | Income tax cannot reduce income |
| PODIZANJE, ATM (personal), PRIVATNO | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns -- Capital Items (Long-Term Assets)

**Capital Items table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, RAČUNALO, MACBOOK, DESKTOP | Computer hardware | Capitalise & depreciate | Long-term asset register |
| PISAČ, PRINTER, SKENER | Office equipment | Capitalise & depreciate |  |
| NAMJEŠTAJ, STOL, STOLICA | Furniture/fittings | Capitalise & depreciate |  |
| VOZILO, AUTOMOBIL (business) | Motor vehicle | Capitalise, business % only |  |

[RESEARCH GAP -- reviewer to confirm] the exact statutory depreciation rates for sole traders under the Croatian PIT Act (the stopa amortizacije schedule) and any low-value immediate-write-off threshold. Apply reviewer-confirmed rates before finalising.

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNI PRIJENOS, VLASTITI RAČUN, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| OTPLATA KREDITA, LOAN REPAYMENT (principal) | EXCLUDE | Loan principal movement |
| DOPRINOSI, MIROVINSKO, ZDRAVSTVENO | Contributions | Statutory contribution payment -- track separately |
| PDV, VAT PAYMENT, POREZNA UPRAVA PDV | EXCLUDE | VAT liability payment, not expense |
| PREDUJAM POREZA, PT INSTALMENT | Advance/prepaid tax | Credit against liability -- not an expense |

### 3.9 Croatian Banks -- Statement Format Reference

**Croatian Banks Statement Format Reference table**

| Bank | Common patterns | Notes |
| --- | --- | --- |
| Zagrebačka banka (Zaba) | UPLATA, ISPLATA, NAKNADA, TRAJNI NALOG | PDF/CSV; date DD.MM.YYYY |
| Privredna banka Zagreb (PBZ) | DOZNAKA, PLAĆANJE, TROŠAK | PDF/CSV |
| Erste banka | UPLATA, KARTIČNO PLAĆANJE, NAKNADA | PDF/CSV |
| OTP banka | TRANSFER, DIREKTNO TEREĆENJE | PDF |
| Revolut Business | PAYMENT, TRANSFER, CARD PAYMENT | CSV; clean counterparty names |
| Wise Business | TRANSFER, CONVERSION, FEE | CSV; multi-currency -- use EUR amounts |

## Section 4 -- Worked Examples

All examples use 2025 figures and the default 20% / 30% progressive rates (no local-unit decision known). Contributions use 2025 caps (NN 137/2024). Currency is EUR.

### Example 1 -- Standard employee net pay (gross > EUR 1,300)

Input line:
`31/01/2025 ; ZABA UPLATA ; POSLODAVAC d.o.o. ; PLAĆA SIJEČANJ ; +1,400.00 ; EUR`

Scenario: Employee, gross monthly salary EUR 2,000.00, single, no dependants.

Reasoning:
1. Gross > EUR 1,300 → no low-salary relief; pension base = full gross EUR 2,000.00.
2. Pension contribution 20% (15% pillar I + 5% pillar II) = EUR 2,000.00 × 20% = EUR 400.00 (withheld). (Zakon o doprinosima arts. 13(1) and 14(1) ([consolidated text](https://www.zakon.hr/z/365/Zakon-o-doprinosima)).)
3. Income after pension = EUR 2,000.00 - EUR 400.00 = EUR 1,600.00.
4. Personal allowance = EUR 600.00 (osobni odbitak). PIT base = EUR 1,600.00 - EUR 600.00 = EUR 1,000.00.
5. PIT base EUR 1,000.00 < EUR 5,000.00 monthly threshold → 20%. PIT = EUR 1,000.00 × 20% = EUR 200.00.
6. Net pay = EUR 1,600.00 - EUR 200.00 = EUR 1,400.00.
7. Employer health contribution = EUR 2,000.00 × 16.5% = EUR 330.00 (on top of gross, not from net). Total employer cost = EUR 2,330.00.

Classification: Net EUR 1,400.00; employee pension EUR 400.00; PIT EUR 200.00; employer health EUR 330.00.

### Example 2 -- Low-salary relief band (EUR 700.01 -- EUR 1,300.00)

Scenario: Employee, gross monthly salary EUR 1,000.00, single, no dependants.

Reasoning:
1. Gross EUR 1,000.00 is in the EUR 700.01--1,300.00 band → relief base = gross - 0.5 × (1,300.00 - gross) = 1,000.00 - 0.5 × 300.00 = EUR 850.00. ([Zakon o doprinosima art. 21.a, added by NN 114/2023](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html).)
2. Pension 20% × EUR 850.00 = EUR 170.00 (withheld).
3. Income after pension = EUR 1,000.00 - EUR 170.00 = EUR 830.00.
4. PIT base = EUR 830.00 - EUR 600.00 allowance = EUR 230.00.
5. PIT = EUR 230.00 × 20% = EUR 46.00.
6. Net pay = EUR 830.00 - EUR 46.00 = EUR 784.00.
7. Employer health = EUR 1,000.00 × 16.5% = EUR 165.00.

Classification: Net EUR 784.00; pension EUR 170.00 (on reduced base EUR 850.00); PIT EUR 46.00; employer health EUR 165.00.

### Example 3 -- Final income: dividend (not aggregated)

Input line:
`15/05/2025 ; PBZ DOZNAKA ; XYZ d.o.o. ; DIVIDENDA 2024 ; +5,000.00 ; EUR`

Reasoning: Dividend is capital income, taxed as final income at 12% and NOT aggregated into the annual progressive assessment (ZPD arts. 57(1), 62 and 70 ([consolidated text, NN 115/16 to 152/24](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak))). PIT = EUR 5,000.00 × 12% = EUR 600.00 (typically withheld at source by the payer).

Classification: Final income; tax EUR 600.00; do NOT add to annual progressive base.

### Example 4 -- Final income: residential rental

Input line:
`05/03/2025 ; ERSTE UPLATA ; TENANT NAME ; NAJAMNINA OŽUJAK ; +800.00 ; EUR`

Reasoning: Rental of immovable property is final income at 12% after a 30% lump-sum expense deduction (ZPD arts. 57(1), 62 and 70 ([consolidated text, NN 115/16 to 152/24](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak))). Taxable base = EUR 800.00 × (1 - 0.30) = EUR 560.00. PIT = EUR 560.00 × 12% = EUR 67.20 per month.

Classification: Final income; monthly tax EUR 67.20; not aggregated.

### Example 5 -- Sole trader (obrt, determining income) annual PIT

Scenario: Determining-income sole trader, net business income after deductible contributions = EUR 40,000.00, one child (1st child coefficient 0.5).

Reasoning:
1. Annual personal allowance = basic EUR 7,200.00 + 1st child EUR 3,600.00 = EUR 10,800.00.
2. Taxable income = EUR 40,000.00 - EUR 10,800.00 = EUR 29,200.00.
3. EUR 29,200.00 < EUR 60,000.00 threshold → 20%. PIT = EUR 29,200.00 × 20% = EUR 5,840.00. (porezna-uprava.gov.hr/en/income-tax/7363.)

Classification: Annual progressive income; PIT EUR 5,840.00. File the annual return by end of February of the following year.

### Example 6 -- High earner crossing the EUR 60,000 threshold

Scenario: Determining-income sole trader, taxable income (after allowance) = EUR 80,000.00, default rates.

Reasoning:
1. First EUR 60,000.00 × 20% = EUR 12,000.00.
2. Excess EUR 20,000.00 × 30% = EUR 6,000.00.
3. Total PIT = EUR 12,000.00 + EUR 6,000.00 = EUR 18,000.00. (porezna-uprava.gov.hr/en/income-tax/7363.)

Classification: Annual progressive income; PIT EUR 18,000.00.

### Example 7 -- Internal transfer (exclude)

Input line:
`20/04/2025 ; ZABA INTERNI PRIJENOS ; VLASTITI RAČUN ŠTEDNJA ; ; -3,000.00 ; EUR`

Reasoning: Transfer between own accounts. Neither income nor expense. Exclude entirely.

Classification: EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residence and Scope

- **Residence and scope** — Tax year is the calendar year. Residents are taxed on worldwide income; non-residents on Croatian-source income. Income splits into annual income (employment, self-employment, other) taxed progressively and reconciled annually, and final income (capital, property, certain other) taxed at flat rates and not aggregated.  _(Zakon o porezu na dohodak; PwC, Tax administration)_

### 5.2 Progressive Rates and Local Units

- **Progressive rates and local units** — Default rates for 2025 are 20% on annual income up to EUR 60,000.00 (EUR 5,000.00/month) and 30% on the excess. Local self-government units may set the lower rate within 15%--23% and the higher rate within 25%--33% (max ranges: City of Zagreb); the default applies where no decision is made by the end of November. Local surtax (prirez) was abolished from 1 January 2024 and absorbed into the wider PIT rate ranges.  _([ZPD arts. 19 and 19.a, as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html), art. 19.a(3) and (5); [ZPD amendment NN 114/2023, in force 1 January 2024: surtax references deleted, art. 19.a added](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1609.html); porezna-uprava.gov.hr/en/income-tax/7363)_

### 5.3 Personal Allowance and Dependants

- **Personal allowance and dependants** — The basic monthly personal allowance is EUR 600.00 (EUR 7,200.00/year), coefficient 1.0. Dependant coefficients are additive: 1st child 0.5 (EUR 300/month), 2nd child 0.7 (EUR 420), 3rd child 1.0 (EUR 600), 4th 1.4, 5th 1.9, 6th 2.5, 7th 3.2, 8th 4.0, 9th 4.9, and a dependent immediate family member 0.5 (EUR 300); disability adds 0.3, or 1.0 for 100% disability or a care, personal disability or inclusion allowance. A person qualifies as a dependant only if own annual income does not exceed EUR 3,600.00.  _([ZPD art. 14(1) and (3), as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html); ZPD art. 17(1): six times the art. 14(1) basic allowance a year ([consolidated text](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak); allowance set by [NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html)))_

### 5.4 Employee Contributions (Pension)

- **Employee pension contributions** — Employee pension contributions total 20% of gross salary: 15% first pillar (mirovinsko I. stup) + 5% second pillar (mirovinsko II. stup). 2025 base caps: highest monthly base EUR 10,788.00; highest annual first-pillar base EUR 129,456.00 (average gross salary EUR 1,798.00 × coefficient 6.00; NN 137/2024).  _(Zakon o doprinosima arts. 13(1) and 14(1) ([consolidated text](https://www.zakon.hr/z/365/Zakon-o-doprinosima)); [Naredba for 2025, NN 137/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_11_137_2266.html))_

**Employee Contributions (Pension) table**  _([Naredba for 2025, NN 137/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_11_137_2266.html); Zakon o doprinosima arts. 13(1) and 14(1) ([consolidated text](https://www.zakon.hr/z/365/Zakon-o-doprinosima)))_

| Contribution | Who pays | Rate | 2025 base cap |
| --- | --- | --- | --- |
| Pension pillar I | Employee (withheld) | 15% | Monthly EUR 10,788.00 / annual EUR 129,456.00 |
| Pension pillar II | Employee (withheld) | 5% | Monthly EUR 10,788.00 |
| **Pension total (employee)** | **Employee** | **20%** | **Monthly EUR 10,788.00** |
| Health (zdravstveno) | **Employer** (on top) | 16.5% | Uncapped |

- **Component check** — Component check: pillar I 15% + pillar II 5% = 20% total employee pension; this is the only employee statutory deduction. Employer pays health 16.5% separately, so the employer column total on-cost is 16.5%.  _(Zakon o doprinosima arts. 13(1) and 14(1) ([consolidated text](https://www.zakon.hr/z/365/Zakon-o-doprinosima)))_

2026 update: NN 150/2025 raises the 2026 monthly base cap to EUR 11,958.00 and the annual cap to EUR 143,496.00 (average gross salary EUR 1,993.00 × 6.00), and the lowest monthly base to EUR 757.34 ([Naredba for 2026, NN 150/2025, arts. 3-5](https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html)). Use 2025 figures for a 2025 computation.

### 5.5 Low-Salary Pension Relief (2025)

**Low-Salary Pension Relief table**  _([Zakon o doprinosima art. 21.a, added by NN 114/2023](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html))_

| Monthly gross | Pension base |
| --- | --- |
| Up to EUR 700.00 | gross - EUR 300.00 |
| EUR 700.01 -- 1,300.00 | gross - 0.5 × (1,300.00 - gross) |
| Above EUR 1,300.00 | full gross |

- **Maximum effective reduction** — Maximum effective reduction is EUR 300/month for the lowest earners. The relief applies whatever the days insured or hours worked in the month, is split pro rata across several employers, and does not reduce the base used for pension rights.  _([Zakon o doprinosima art. 21.a, added by NN 114/2023](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html), paras. 1 to 5 and 7)_

### 5.6 Employer Health Contribution

- **Employer health contribution** — Employer pays a health insurance contribution (zdravstveno osiguranje) of 16.5% of gross salary, uncapped. This is an employer on-cost; it is never deducted from the employee's net pay.  _(Zakon o doprinosima arts. 13(1) and 14(1) ([consolidated text](https://www.zakon.hr/z/365/Zakon-o-doprinosima)))_

### 5.7 Self-Employed (Obrt) Contributions

- **Self-employed obrt contributions** — For a determining-income sole trader (craft), pension 20% + health 16.5% apply on the contribution base. The 2025 minimum monthly contribution base for craft activity is EUR 1,168.70 (NN 137/2024, code 0101) = EUR 14,024.40/year. Contributions paid are deductible in computing business income.  _(NN 137/2024, code 0101)_

[RESEARCH GAP -- reviewer to confirm] the exact base determination (percentage of income vs minimum base) and any maximum base for self-employed.

### 5.8 Final / Flat Income

**Final / Flat Income table**  _(ZPD arts. 57(1), 62 and 70 ([consolidated text, NN 115/16 to 152/24](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak)); the seasonal-work row: PwC, Income determination)_

| Category | Rate | Base |
| --- | --- | --- |
| Interest, dividends, capital gains | 12% | Gross (final) |
| Rental of immovable/movable property | 12% | After 30% lump-sum deduction |
| Own shares / stock options | 24% |  |
| Property rights; disposal of property/rights | 24% |  |
| Withdrawal of assets / hidden distributions | 36% |  |
| Seasonal agricultural work | 10% |  |

- **Not aggregated** — Final income is NOT aggregated into the annual progressive assessment.  _(ZPD arts. 57(1), 62 and 70 ([consolidated text, NN 115/16 to 152/24](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak)))_

### 5.9 Lump-Sum (Paušalni Obrt) Regime

- **Lump-sum paušalni obrt regime** — Available to sole traders with annual receipts up to EUR 60,000 who are not VAT-registered. Lump-sum income is determined across statutory receipt brackets and taxed at 12%, paid quarterly. The PO-SD annual report is filed by 15 January.  _(Zakon o porezu na dohodak; Porezna uprava (obrtnici-paušalisti); PwC)_

**Paušalni annual lump-sum income by receipt band (2025)**  _([NN 25/2025, art. 1 (new art. 14 of the 2025 Naredba)](https://narodne-novine.nn.hr/clanci/sluzbeni/2025_02_25_231.html), which restates the lump-sum income set by the paušal ordinance)_

| Annual receipts (EUR) | Annual lump-sum income (EUR) |
| --- | --- |
| up to 11,300.00 | 1,695.00 |
| 11,300.01 -- 15,300.00 | 2,295.00 |
| 15,300.01 -- 19,900.00 | 2,985.00 |
| 19,900.01 -- 30,600.00 | 4,590.00 |
| 30,600.01 -- 40,000.00 | 6,000.00 |
| 40,000.01 -- 50,000.00 | 7,500.00 |
| 50,000.01 -- 60,000.00 | 9,000.00 |

[RESEARCH GAP -- reviewer to confirm] the tax rate applied to the lump-sum income and the quarterly instalments, which are in the paušal ordinance (Pravilnik o paušalnom oporezivanju samostalnih djelatnosti) and were not read in this pass.

### 5.10 Youth PIT Relief

- **Youth PIT relief** — The annual income tax is reduced by 100% for a person up to 25 years of age and by 50% for a person aged 26 to 30, in each case only on the proportional part of the tax charged at the lower rate on salary (employment income under art. 21(1)1). It is given in the annual assessment, before the 50% reduction for pensioners and residents of assisted areas, and it does not reduce contributions.  _(ZPD art. 46(2) ([consolidated text](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak)) and (7))_

### 5.11 Non-Deductible Expenses (Self-Employed)

**Non-Deductible Expenses table**

| Expense | Reason |
| --- | --- |
| Personal living expenses | Not business-related |
| Fines and penalties (kazne) | Public policy |
| Income tax itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |
| VAT paid (if registered & recoverable) | Recovered via VAT system, not a cost |

### 5.12 Filing Deadlines

**Filing Deadlines table**  _(porezna-uprava.gov.hr/en/income-tax/7363)_

| Item | Detail |
| --- | --- |
| Annual income tax return (self-employed; DOH) | End of February of the following year |
| Auto-assessment for most employees | No filing required (poseban postupak) |
| JOPPD (monthly withholding & contributions) | By the day of salary payment |
| PO-SD (paušalni annual report) | By 15 January (within 15 days of year-end) |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Apportionment

- **Home office apportionment** — Calculate the proportion of the home used for business (dedicated room / floor area). Apply that percentage to rent, electricity (HEP), water, internet. Dual-use space generally does not qualify. Conservative default: 0% deduction until the reviewer confirms the arrangement.

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel (INA), insurance, maintenance, and depreciation is deductible. Requires a mileage log. Conservative default: 0% business use until a log is provided.

### 6.3 Phone / Internet Mixed Use

- **Phone / internet mixed use** — Business-use portion only (Hrvatski Telekom, A1, Telemach). Conservative default: 0% until the business percentage is confirmed.

### 6.4 Representation (Reprezentacija)

- **Representation (reprezentacija)** — Entertainment / client hospitality (reprezentacija) is partly non-deductible under Croatian rules. Conservative default: treat as non-deductible until the reviewer confirms the apportionment.

[RESEARCH GAP -- reviewer to confirm] the exact deductible percentage (commonly cited as 50% disallowed) for sole-trader PIT purposes.

### 6.5 Local-Unit Rate Selection

- **Local-unit rate selection** — If the taxpayer's municipality has set rates other than the default 20%/30%, the reviewer must substitute the local rates (within the statutory bands) before finalising. Conservative default: 20% / 30% with an explicit flag.

### 6.6 Asset Depreciation

- **Asset depreciation** — Long-term assets are capitalised and depreciated, not expensed in full.

[RESEARCH GAP -- reviewer to confirm] the applicable stopa amortizacije rates and any low-value immediate-write-off threshold.

### 6.7 Pillar Membership

- **Pillar membership** — Pillar II (5%) applies to insured persons enrolled in the mandatory second pillar (generally those who entered the labour market from 2002 / were under 40 in 2002). Older workers may be pillar-I-only (15%). Flag for reviewer: confirm pillar membership before splitting 15% / 5%.

## Section 7 -- Excel Working Paper Template

```
CROATIA PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Type: Employee / Sole trader (obrt) / Paušalni
Marital/dependants: ____ children, ____ other dependants
Local unit (municipality): ____________  [default 20%/30% if unknown]

A. GROSS / BUSINESS INCOME (annual income)
  A1. Gross salary or business receipts (net of VAT)  ___________
  A2. Other annual income                              ___________
  A3. TOTAL annual income                              ___________

B. DEDUCTIBLE BUSINESS EXPENSES (sole trader only)
  B1. Office rent                                      ___________
  B2. Professional / accountancy / legal fees          ___________
  B3. Office supplies                                  ___________
  B4. Software subscriptions                           ___________
  B5. Marketing / advertising                          ___________
  B6. Bank / payment processing fees                   ___________
  B7. Training / chamber subscriptions                 ___________
  B8. Travel (business)                                ___________
  B9. Telecoms (business %)                            ___________
  B10. Home office (business %)                         ___________
  B11. Vehicle (business %)                             ___________
  B12. Depreciation (per confirmed rates)              ___________
  B13. TOTAL expenses                                  ___________

C. CONTRIBUTIONS
  C1. Pension 20% (employee) / self-employed base      ___________
  C2. (Employer health 16.5% -- on-cost, memo only)    ___________

D. INCOME AFTER CONTRIBUTIONS (A3 - B13 - C1)          ___________

E. PERSONAL ALLOWANCE (osobni odbitak)
  E1. Basic (EUR 7,200 / yr or EUR 600 / mo)           ___________
  E2. Dependant coefficients (children + family)       ___________
  E3. TOTAL allowance                                  ___________

F. PIT BASE (D - E3)                                   ___________

G. TAX COMPUTATION (pass to deterministic engine)
  G1. 20% on base up to EUR 60,000                     ___________
  G2. 30% on excess over EUR 60,000                    ___________
  G3. TOTAL PIT (G1 + G2)                              ___________
  G4. Less: advance tax / withholding paid             ___________
  G5. Tax due / refund                                 ___________

H. FINAL INCOME (separate, NOT aggregated)
  H1. Capital income 12%                               ___________
  H2. Rental 12% (after 30% deduction)                 ___________
  H3. Other final income (24% / 36% / 10%)             ___________

REVIEWER FLAGS:
  [ ] Local-unit rate confirmed (or default 20%/30% accepted)?
  [ ] Dependant coefficients confirmed (income <= EUR 3,600 each)?
  [ ] Pension pillar split (15%/5%) confirmed?
  [ ] Low-salary relief applied where gross <= EUR 1,300?
  [ ] Contribution base caps (2025) applied?
  [ ] Final income kept separate from progressive base?
  [ ] Home/vehicle/phone business % documented?
  [ ] Representation (reprezentacija) apportionment confirmed?
  [ ] Depreciation rates confirmed?
  [ ] Youth PIT relief checked (age < 30)?
```

## Section 8 -- Bank Statement Reading Guide

### Croatian Bank Statement Formats

**Croatian Bank Statement Formats table**

| Bank | Format | Key fields | Notes |
| --- | --- | --- | --- |
| Zagrebačka banka (Zaba) | PDF, CSV | Datum, Opis, Duguje, Potražuje, Stanje | Most common; description holds counterparty + reference |
| Privredna banka Zagreb (PBZ) | PDF, CSV | Datum valute, Opis, Iznos, Stanje |  |
| Erste banka | PDF, CSV | Datum, Opis transakcije, Iznos | Card transactions show merchant |
| OTP banka | PDF | Datum, Opis, Isplate, Uplate | Shorter descriptions |
| Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency |
| Wise Business | CSV | Date, Description, Amount, Currency, Running Balance | Multi-currency; conversion fees separate line |

### Key Croatian Banking / Tax Terms

**Key Croatian Banking / Tax Terms table**

| Term | English | Classification hint |
| --- | --- | --- |
| UPLATA | Credit / payment in | Potential income |
| ISPLATA | Debit / payment out | Expense -- check counterparty |
| DOZNAKA | Transfer / remittance | Check direction |
| TRAJNI NALOG | Standing order | Regular expense (rent, loan) |
| IZRAVNO TEREĆENJE | Direct debit | Regular expense (utility, subscription) |
| NAKNADA | Fee / charge | Bank charge (deductible) or platform fee |
| KAMATE | Interest | Final income (12%) or bank charge |
| PLAĆA / NETO PLAĆA | Salary / net salary | Employment income (annual income) |
| NAJAMNINA / ZAKUPNINA | Rent | Final income (rental, 12%) |
| DOPRINOSI | Contributions | Pension/health -- track separately |
| PDV | VAT | VAT liability -- exclude |
| POVRAT POREZA | Tax refund | Exclude |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1), including default 20%/30% rates.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- CROATIA INCOME TAX
1. Are you an employee, a sole trader (obrt), or paušalni? If obrt, do you keep full books or use the lump-sum regime?
2. What is your local self-government unit (municipality / grad)?
3. How many dependants (children + others)? Do any have annual income above EUR 3,600?
4. Gross monthly salary or annual business receipts?
5. Are you in the second pension pillar (pillar II 5%), or pillar I only?
6. Are you VAT-registered (turnover above EUR 60,000)?
7. Home office: dedicated room or shared space? If dedicated, what % of floor area?
8. Vehicle: business use %? Do you keep a mileage log?
9. Phone / internet: business use %?
10. Any final income (interest, dividends, rent, capital gains)?
11. Your age (for any youth PIT relief)?
12. Any capital assets purchased during the year?
```

### Key Legislation and Authority References

**Key Legislation and Authority References**  _(Zakon o porezu na dohodak; porezna-uprava.gov.hr/en/income-tax/7363)_

| Topic | Reference |
| --- | --- |
| Income tax rates & general rules | Zakon o porezu na dohodak; porezna-uprava.gov.hr/en/income-tax/7363 |
| Personal allowance | porezna-uprava.gov.hr/en/personal-allowance/7358 |
| Contributions & 2025 base caps | Zakon o doprinosima; NN 137/2024 (narodne-novine.nn.hr/clanci/sluzbeni/2024_11_137_2266.html) |
| Final / flat income | ZPD arts. 57(1), 62 and 70 ([consolidated text, NN 115/16 to 152/24](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak)) |
| Tax administration & residence | PwC, Croatia -- Tax administration |
| Deductions / dependants | [ZPD art. 14(1) and (3), as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html); ZPD art. 17(1): six times the art. 14(1) basic allowance a year ([consolidated text](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak); allowance set by [NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html)) |
| Minimum wage 2025 / 2026 | [Uredba, NN 124/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_10_124_2072.html); [Uredba, NN 132/2025](https://narodne-novine.nn.hr/clanci/sluzbeni/2025_10_132_1931.html) |

### Key 2025 Figures (with provenance)

**Key 2025 Figures (with provenance)**  _(porezna-uprava.gov.hr/en/income-tax/7363)_

| Figure | 2025 value | Source |
| --- | --- | --- |
| Progressive lower rate (default) | 20% | porezna-uprava.gov.hr/en/income-tax/7363 |
| Progressive higher rate (default) | 30% | porezna-uprava.gov.hr/en/income-tax/7363 |
| Bracket threshold | EUR 60,000.00/yr (EUR 5,000.00/mo) | porezna-uprava.gov.hr/en/income-tax/7363 |
| Local lower-rate range | 15% -- 23% | [ZPD arts. 19 and 19.a, as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html) |
| Local higher-rate range | 25% -- 33% | [ZPD arts. 19 and 19.a, as amended by NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html) |
| Basic personal allowance | EUR 600.00/mo (EUR 7,200.00/yr) | porezna-uprava.gov.hr/en/personal-allowance/7358 |
| Dependant income ceiling | EUR 3,600.00/yr | ZPD art. 17(1): six times the art. 14(1) basic allowance a year ([consolidated text](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak); allowance set by [NN 152/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html)) |
| Employee pension total | 20% (15% + 5%) | Zakon o doprinosima arts. 13(1) and 14(1) ([consolidated text](https://www.zakon.hr/z/365/Zakon-o-doprinosima)) |
| Employer health | 16.5% (uncapped) | Zakon o doprinosima arts. 13(1) and 14(1) ([consolidated text](https://www.zakon.hr/z/365/Zakon-o-doprinosima)) |
| Monthly contribution base cap | EUR 10,788.00 | NN 137/2024 |
| Annual first-pillar base cap | EUR 129,456.00 | NN 137/2024 |
| Self-employed min. monthly base (craft) | EUR 1,168.70 | NN 137/2024 (code 0101) |
| Capital income / rental flat rate | 12% | ZPD arts. 57(1), 62 and 70 ([consolidated text, NN 115/16 to 152/24](https://www.zakon.hr/z/85/Zakon-o-porezu-na-dohodak)) |
| VAT registration / paušalni ceiling | EUR 60,000 turnover/yr | PwC, Income determination |
| Minimum wage 2025 | EUR 970.00 gross/mo | [Uredba, NN 124/2024](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_10_124_2072.html) |
| Minimum wage 2026 | EUR 1,050.00 gross/mo | [Uredba, NN 132/2025](https://narodne-novine.nn.hr/clanci/sluzbeni/2025_10_132_1931.html) |
| 2026 monthly base cap | EUR 11,958.00 | NN 150/2025 |
| 2026 annual first-pillar cap | EUR 143,496.00 | NN 150/2025 |

### Test Suite

**Test 1 -- Standard employee net pay (gross > EUR 1,300).**
Input: Single, gross EUR 2,000.00/month, no dependants, default rates.
Expected: Pension 20% = EUR 400.00; income after pension EUR 1,600.00; PIT base EUR 1,600.00 - EUR 600.00 = EUR 1,000.00; PIT EUR 200.00; net EUR 1,400.00; employer health EUR 330.00.

**Test 2 -- Low-salary relief band.**
Input: Single, gross EUR 1,000.00/month, no dependants.
Expected: Pension base = 1,000 - 0.5×(1,300-1,000) = EUR 850.00; pension EUR 170.00; income after pension EUR 830.00; PIT base EUR 230.00; PIT EUR 46.00; net EUR 784.00; employer health EUR 165.00.

**Test 3 -- Low-salary relief at EUR 700 boundary.**
Input: Single, gross EUR 700.00/month, no dependants.
Expected: Pension base = 700 - 300 = EUR 400.00; pension EUR 80.00; income after pension EUR 620.00; PIT base EUR 20.00; PIT EUR 4.00; net EUR 616.00.

**Test 4 -- Sole trader annual PIT with one child.**
Input: Determining-income obrt, income after deductible contributions EUR 40,000.00, one child (coeff 0.5).
Expected: Allowance EUR 7,200 + EUR 3,600 = EUR 10,800.00; taxable EUR 29,200.00; PIT 20% = EUR 5,840.00.

**Test 5 -- High earner crossing EUR 60,000.**
Input: Taxable income (after allowance) EUR 80,000.00, default rates.
Expected: 60,000 × 20% = EUR 12,000.00; 20,000 × 30% = EUR 6,000.00; total PIT EUR 18,000.00.

**Test 6 -- Dividend as final income.**
Input: Dividend EUR 5,000.00.
Expected: 12% final = EUR 600.00; NOT added to progressive base.

**Test 7 -- Residential rental as final income.**
Input: Monthly rent EUR 800.00.
Expected: Base after 30% deduction = EUR 560.00; PIT 12% = EUR 67.20/month; not aggregated.

**Test 8 -- Contribution base cap applied.**
Input: Gross monthly salary EUR 12,000.00 (above the cap).
Expected: Pension base capped at EUR 10,788.00; pension 20% = EUR 2,157.60 (NOT 20% of EUR 12,000). Employer health 16.5% on full uncapped gross EUR 12,000.00 = EUR 1,980.00.

## PROHIBITIONS

- **Local-unit rate confirmation** — NEVER apply a local-unit rate without confirming the municipality -- default to 20%/30% with an explicit flag  _(PROHIBITIONS)_
- **No aggregation of final income** — NEVER aggregate final income (capital, dividends, rent) into the annual progressive base  _(PROHIBITIONS)_
- **PIT estimate labeling** — NEVER compute the final PIT figure as definitive -- always label it estimated and pass the base to the deterministic engine  _(PROHIBITIONS)_
- **Employer health not deducted from net pay** — NEVER deduct the employer health contribution (16.5%) from the employee's net pay -- it is an employer on-cost  _(PROHIBITIONS)_
- **Low-salary relief formula requirement** — NEVER use the full gross as the pension base when gross <= EUR 1,300 -- apply the low-salary relief formula  _(PROHIBITIONS)_
- **No 2026 caps for 2025 computation** — NEVER use 2026 contribution caps for a 2025 computation (use EUR 10,788/month, EUR 129,456/year per NN 137/2024)  _(NN 137/2024)_
- **Dependant income ceiling qualification** — NEVER treat a dependant as qualifying if their own annual income exceeds EUR 3,600.00  _(PROHIBITIONS)_
- **No fines/penalties/income tax as deduction** — NEVER allow fines, penalties, or income tax itself as a deduction  _(PROHIBITIONS)_
- **Research gaps disclaimer** — NEVER invent the paušalni tax rate and quarterly instalments or depreciation rates -- these are RESEARCH GAPS for the reviewer  _(PROHIBITIONS)_
- **Pillar II confirmation required** — NEVER apply pillar II (5%) without confirming second-pillar membership  _(PROHIBITIONS)_

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
