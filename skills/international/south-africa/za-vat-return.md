---
name: za-vat-return
description: Use this skill whenever asked about South African VAT returns for self-employed individuals or small businesses. Trigger on phrases like "South Africa VAT", "VAT201", "SARS VAT", "15% VAT", "eFiling VAT", "zero-rated SA", "VAT vendor", or any question about VAT filing, computation, or registration for vendors in South Africa. Covers the 15% standard rate, zero-rated and exempt supplies, R2.3M registration threshold, VAT201 return, and bimonthly filing via SARS eFiling. ALWAYS read this skill before touching any South African VAT work.
version: 2.1
jurisdiction: ZA
tax_year: 2026
last_updated: 2026-09-29
reviewed_by: Werner Britz
review_status: current
depends_on:
  - vat-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ZA VAT Return

## South Africa VAT Return (VAT201) -- Self-Employed Skill v2.1

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Werner Britz** on 2026-06-12; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | South Africa |
| Tax | Value-Added Tax (VAT) at 15% |
| Currency | ZAR only |
| Primary legislation | Value-Added Tax Act 89 of 1991 (VAT Act) |
| Supporting legislation | Tax Administration Act 28 of 2011 (TAA); SARS interpretation notes |
| Tax authority | South African Revenue Service (SARS) |
| Filing portal | SARS eFiling (www.sarsefiling.co.za) — `efiling.sars.gov.za` does not resolve |
| Default filing frequency | Bimonthly (Category A) |
| Filing deadline | Last business day of month following period end (eFiling) |
| Contributor | Open Accountants Community |
| Validated by | Werner Britz CA(SA), Spurwing CFO |
| Validation date | May 2026 |
| Skill version | 2.1 |

### Rate Table

**Rate Table**

| Rate | Application |
| --- | --- |
| 15% | Standard rate (effective 1 April 2018) |
| 0% | Exports of goods (s 11(1)(a), with the Export Regulation documents), services to a non-resident outside SA (s 11(2)(l)), basic foodstuffs (Schedule 2), petrol/diesel (s 11(1)(h)), international transport, agricultural inputs, going concern (s 11(1)(e)), gold to SARB/bank, illuminating paraffin |
| Exempt | Financial services in the narrow s 2 sense (interest, exchange margins, life insurance, dealing in securities; fee-based services are STANDARD-RATED under the proviso to s 2(1)), residential rental (s 12(c)), public road and rail transport of fare-paying passengers (s 12(g)), educational services by recognised institutions, childcare, donated goods sold by associations not for gain |

### Tax Fraction

- **Tax fraction** — For VAT-inclusive amounts at 15%: 15/115.

### Key Thresholds

**Key Thresholds table**

| Item | Amount (ZAR) |
| --- | --- |
| Compulsory registration | R2,300,000 taxable supplies in any 12-month period (from 1 April 2026) |
| Voluntary registration | R120,000 taxable supplies in any 12-month period (from 1 April 2026) |
| Payments basis eligibility | R2,500,000 threshold applies to natural persons only. Full s 15(2) list includes public authorities, water boards, municipal entities, municipalities, associations not for gain, foreign suppliers of electronic services, SABC Ltd, and natural persons under R2,500,000 |
| Full tax invoice threshold | Supplies above R5,000 (VAT inclusive): full tax invoice under s 20(4) |
| Abridged tax invoice | Supplies of more than R50 up to R5,000: abridged invoice acceptable (s 20(5)) |
| No invoice required | Supplies of R50 or less (s 20(6)); a till slip or sales docket is still needed to support the input claim |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Registration status unknown | STOP -- do not compute |
| Accounting basis unknown | Invoice basis (default) |
| Supply classification unknown | Standard-rated at 15% |
| Private use proportion unknown | 0% recovery |
| Second-hand goods claim | Not claimable until documentation confirmed |

### Required Inputs

**Minimum viable:** Bank statement for the VAT period in CSV, PDF, or pasted text, plus confirmation of VAT registration status and vendor number.

**Recommended:** Sales invoices, purchase invoices with VAT shown, prior period VAT201.

**Ideal:** Complete invoice register, filing category confirmation, prior year VAT reconciliation.

### Refusal Catalogue

- **R-ZA-1 -- Below threshold** — If taxable supplies have not exceeded R2,300,000 in any 12-month period (from 1 April 2026) and client is not voluntarily registered, no VAT obligations. Stop.
- **R-ZA-2: Cross-border services** — Complex cross-border service transactions and customs VAT require specialist review. Escalate.
- **R-ZA-3 -- VAT grouping** — South Africa has no VAT group registration of the UK kind. The nearest equivalents, separate registration of a vendor's branches under s 50 and a single registration for a foreign group's branches under s 23(2A), are outside this skill's scope. Escalate.  _(VAT Act s 50, s 23(2A))_
- **R-ZA-4: Large complex transactions** — Transactions involving property, construction, or financial instruments require specialist review. Escalate.

### 3.1 Income Patterns (Credits)

**Income Patterns table**

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| EFT FROM [client] / EFT CREDIT | Taxable supply | Output VAT at 15% | Standard electronic transfer |
| INSTANT MONEY / CASH DEPOSIT | Taxable supply | Revenue | Cash receipt |
| PAYFAST PAYOUT / PAYFAST SETTLEMENT | Taxable supply | Revenue | PayFast payment gateway |
| YOCO SETTLEMENT / YOCO PAYOUT | Taxable supply | Revenue | Yoco card machine settlement |
| SNAPSCAN PAYOUT | Taxable supply | Revenue | SnapScan mobile payment |
| ZAPPER SETTLEMENT | Taxable supply | Revenue | Zapper payment |
| CAPITEC / FNB / ABSA / NEDBANK / STD BANK CREDIT | Potential taxable supply | Classify by the character of the receipt | A bank credit is not a VAT classifier: the same credit can be a taxable sale (output VAT), rent of a dwelling (exempt), a loan drawdown or a capital injection (outside VAT). Trace it to the invoice or agreement |
| SWIFT / FOREIGN CURRENCY CREDIT | Zero-rated export | Output VAT 0% | Goods exported under s 11(1)(a) with the Export Regulation (GN R316) documents; services supplied to a non-resident who is outside SA when the services are rendered under s 11(2)(l). Report in Field 2A (goods) or Field 2 (services) |
| INSURANCE PAYOUT / CLAIM SETTLEMENT | Deemed taxable supply | Output VAT under s 8(8) | Where the insured asset or expense was used for taxable supplies; a common reviewer trap |
| INTEREST / INT EARNED | Exempt | NOT taxable | Bank interest -- financial service (s 12(a) read with s 2(1)(f)) |
| SARS REFUND | EXCLUDE | Not income | Tax refund |
| LOAN DRAWDOWN | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

**Expense Patterns table**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT / COMMERCIAL LEASE | Rent | Input VAT claimable only where the landlord is VAT-registered and issues a tax invoice | Many individual landlords are below the threshold and charge no VAT, in which case there is no input to claim. Residential rent is exempt whatever the landlord's status (s 12(c)) |
| ESKOM / CITY POWER / CITY OF CAPE TOWN | Utilities | Input VAT claimable | Electricity, water and refuse charges on a municipal bill are standard-rated; the property rates on the same bill are not a supply and carry no VAT: split the bill |
| TELKOM / VODACOM / MTN / CELL C / RAIN | Communications | Business portion claimable | Mixed use: apportion |
| ENGEN / SHELL / CALTEX / SASOL | Fuel | ZERO-RATED (s 11(1)(h)) -- no VAT on fuel | Lubricants, car-wash, shop purchases at fuel stations are 15% |
| TAKEALOT / MAKRO / GAME | Office supplies | Input VAT claimable | Business purchases |
| GOOGLE ADS / META / LINKEDIN | Advertising | Input VAT claimable where the invoice carries SA VAT | Google, Meta and LinkedIn bill through a South African entity or as registered foreign electronic services suppliers, so the invoice normally shows 15% VAT and is a standard input. Where the invoice comes from a foreign entity without SA VAT, it is an imported service under s 7(1)(c) and s 14 only to the extent the vendor uses it otherwise than for making taxable supplies: a fully taxable vendor declares nothing; a partly exempt vendor declares output VAT on the exempt-use portion in Field 12, with no input tax on that portion |
| SANTAM / HOLLARD / OUTSURANCE / DISCOVERY INSURE (premiums) | Insurance | Input VAT claimable | Short-term premiums (asset, business interruption, public liability, fleet) are standard-rated and the insurer issues a tax invoice; a claim payout is a deemed supply with output VAT under s 8(8). Life and income-protection premiums are exempt financial services with no input |
| UBER SA / BOLT SA / TAXI | Travel | EXEMPT (s 12(g)) -- fare is exempt; no input VAT claimable | Only the small booking fee (if separately shown) may carry input VAT |
| SARS INCOME TAX / SARS PAYE | EXCLUDE | Tax payment | Not deductible |
| SARS VAT PAYMENT | EXCLUDE | VAT payment | Not input tax |
| BANK CHARGES / FNB FEE / ABSA FEE | Input 15% | Input VAT claimable | Fee-based services are standard-rated per s 2(1) proviso; banks issue monthly VAT tax invoices |
| MOTOR CAR PURCHASE / LEASE / RENTAL (AVIS, EUROPCAR, HERTZ, BIDVEST) | BLOCKED | Input tax blocked under s 17(2)(c) | "Motor car" includes sedans, SUVs, double-cab bakkies, minibuses. Running costs (fuel, repairs) ARE claimable |
| CLIENT LUNCHES / ENTERTAINMENT / CORPORATE GIFTS | BLOCKED | Input tax blocked under s 17(2)(a) | Unless vendor is in the business of providing entertainment |
| CHECKERS / SHOPRITE / PICK N PAY / WOOLWORTHS / SPAR | Office supplies | Input VAT claimable if for resale | For office consumption (tea, coffee, staff fridge), input tax is BLOCKED under s 17(2)(a) entertainment block regardless of whether items are zero-rated or standard-rated. Only claimable where items are for resale |
| OWN TRANSFER / PERSONAL | EXCLUDE | Drawings | Not business |

### 3.3 Zero-Rated Supply Indicators

**Zero-Rated Supply Indicators table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EXPORT / INTERNATIONAL SHIPMENT | Zero-rated output | Goods exported from SA |
| BROWN BREAD / MAIZE MEAL / RICE / EGGS / MILK | Zero-rated | Basic foodstuffs |
| FUEL LEVY / PETROL / DIESEL | Zero-rated | Fuel levy applies instead |

### 3.4 Transport Patterns

**Transport Patterns table**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| FLYSAFAIR / LIFT / CEMAIR | Domestic flights | Input VAT claimable | Domestic air travel is standard-rated at 15% |
| SA AIRLINK | Domestic flights | Input VAT claimable | Standard-rated |
| UBER SA / BOLT SA / TAXI | Local transport | EXEMPT (s 12(g)) | Fare is exempt; no input VAT. Only the booking fee (if separately shown) may carry input VAT |
| GREYHOUND / INTERCAPE | Long-distance bus | EXEMPT (s 12(g)) | Public road transport of fare-paying passengers |

### 3.5 Payment Processor Fees

**Payment Processor Fees table**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| PAYFAST FEE / PAYFAST CHARGE | Payment processing | Input 15% | Standard-rated -- fee-based processing is not a financial service per s 2(1) proviso |
| YOCO FEE / YOCO CHARGE | Payment processing | Input 15% | Standard-rated -- fee-based processing is not a financial service per s 2(1) proviso |
| PEACH PAYMENTS FEE | Payment processing | Input 15% | Standard-rated -- fee-based processing is not a financial service per s 2(1) proviso |

### Example 1 -- Standard Bimonthly Return

**Input:** Standard-rated supplies R500,000 (VAT-exclusive, from the sales invoices). Purchases R200,000 (VAT-exclusive, all standard-rated, valid tax invoices held).

**Reasoning:**
Output VAT: R500,000 x 15% = R75,000. Input VAT: R200,000 x 15% = R30,000. VAT payable: R75,000 - R30,000 = R45,000. VAT-inclusive supply total: R575,000 (Field 1); output VAT R75,000 (Field 4). VAT-inclusive purchase total: R230,000; input VAT R30,000 (Field 15).

Bank statements show VAT-inclusive amounts, so state which basis the figures are on. Had R500,000 and R200,000 been the VAT-inclusive bank totals: output VAT R500,000 x 15/115 = R65,217.39; input VAT R200,000 x 15/115 = R26,086.96; VAT payable R39,130.43.

**Classification:** VAT payable R45,000 (Field 20) on the VAT-exclusive facts.

### Example 2 -- Exporter in Refund Position

**Input:** Zero-rated exports R800,000. Purchases R300,000 (standard-rated).

**Reasoning:**
Output VAT: R0. Input VAT: R300,000 x 15% = R45,000. Refund: R45,000. A refund position almost always triggers a SARS verification or audit: the vendor must hold the prescribed export documents under the Export Regulation (GN R316) for every zero-rated export, and SARS withholds the refund under TAA s 190 until the verification is complete.

**Classification:** VAT refund R45,000; flag the export documents for the reviewer.

### Example 3 -- Second-Hand Goods Purchase

**Input:** Vendor buys used equipment from non-vendor for R50,000 (no VAT charged).

**Reasoning:**
Notional input tax: R50,000 x 15/115 = R6,521.74, claimable in the period in which the goods are both acquired and paid for, capped at the tax fraction of the lesser of the consideration paid and the open market value, and only with the VAT264 declaration (modernised 2023), proof of the seller's identity and proof of payment. Reported in Field 15 (input VAT on other goods/services).

**Classification:** Input tax R6,521.74 (Field 15). Flag for reviewer on documentation.

### Example 4 -- Bad Debt Relief

**Input:** Invoice for R23,000 (incl. VAT) written off after 14 months.

**Reasoning:**
Bad debt relief under s 22(1): debt outstanding over 12 months and written off. Relief: R23,000 x 15/115 = R3,000.

**Classification:** Input tax deduction R3,000.

### Example 5 -- Google Ads (Imported Services)

**Input:** Google Ads spend R50,000 for the period. Google now bills via SA-registered entity with SA VAT number and issues VAT tax invoices.

**Reasoning:**
Where Google bills via a South African entity registered for VAT and issues a valid tax invoice showing 15% VAT, the vendor claims input tax directly. VAT amount: R50,000 x 15/115 = R6,521.74. Reported in Field 15 (input VAT on other goods/services). If billed by a non-resident entity without SA VAT, the imported-services test of s 7(1)(c) and s 14 applies: a fully taxable vendor using the advertising for its taxable supplies has nothing to declare; a partly exempt vendor declares output VAT in Field 12 on the exempt-use share (at 40% exempt use, R50,000 x 40% x 15% = R3,000), with no input tax on it.

**Classification:** Input tax R6,521.74 (Field 15) where billed by SA entity. Foreign-billed without SA VAT: nothing for a fully taxable vendor; output VAT on the exempt-use share in Field 12 for a partly exempt vendor, no input.

### 5.1 VAT201 Return Fields

**VAT201 Return Fields table**

| Field | Description |
| --- | --- |
| 1 | Standard-rated supplies (VAT-inclusive, excluding capital goods) |
| 1A | Standard-rated capital goods supplied (VAT-inclusive) |
| 2 | Zero-rated supplies (excluding exports) |
| 2A | Zero-rated exported goods |
| 3 | Exempt and non-supplies |
| 4 | Output VAT on Field 1 (Field 1 x 15/115) |
| 4A | Output VAT on Field 1A (Field 1A x 15/115) |
| 5 | Commercial accommodation supplied for 28+ days (value) |
| 6 | Field 5 x 60% (deemed taxable portion) |
| 7 | Field 6 x 15/115 (VAT on deemed portion) |
| 8 | Sum of Fields 6 and 7 |
| 9 | Output VAT on commercial accommodation (Field 8 x 15%) |
| 10 | Change-in-use / second-hand goods exported (consideration) |
| 11 | Field 10 x 15/115 |
| 12 | Other output adjustments and imported services |
| 13 | Total output tax (4 + 4A + 9 + 11 + 12) |
| 14 | Input VAT on capital goods |
| 14A | Input VAT on imported capital goods |
| 15 | Input VAT on other goods/services |
| 15A | Input VAT on imported other goods/services |
| 16 | Change-in-use input adjustment |
| 17 | Bad debts (s 22 relief) |
| 18 | Other input adjustments |
| 19 | Total input tax (14 + 14A + 15 + 15A + 16 + 17 + 18) |
| 20 | Net VAT payable / refundable (13 - 19) |

### 5.2 Filing Categories

**Filing Categories table**

| Category | Frequency | Who |
| --- | --- | --- |
| A | Bimonthly | Default for most vendors |
| B | Monthly | Taxable supplies > R30M/year |
| C | Six-monthly | Farming enterprises (by approval) |
| D | Annual | Enterprises supplying only connected persons: farming or rental (by approval, s 27(4A)) |
| E | Annual | Connected-party rental enterprises (by approval) |
| F | Four-monthly | Micro businesses registered for turnover tax |

There is no quarterly category.

### 5.3 Filing Deadlines

**Filing Deadlines table**

| Method | Deadline |
| --- | --- |
| eFiling | Last business day of month following period end |
| Manual (branch) | 25th of month following period end |

### 5.4 Payments Basis (s 15)

- **Payments basis (s 15)** — R2,500,000 threshold applies to natural persons only. Full s 15(2) list includes public authorities, water boards, municipal entities, municipalities, associations not for gain, foreign suppliers of electronic services, SABC Ltd, and natural persons under R2,500,000. Account for VAT when payment is made or received. Must apply to SARS.  _(VAT Act s 15)_

### 5.5 Penalties (TAA Chapter 15)

**Penalties table**

| Offence | Penalty |
| --- | --- |
| Late payment | Percentage-based penalty of 10% of the tax paid late (VAT Act s 39; TAA s 213) |
| Late return, tax paid on time | No percentage penalty. SARS states that it does not currently impose the fixed-amount administrative non-compliance penalty (TAA ss 210 and 211, a monthly scale set by taxable income) for a late VAT return, although the Act allows it; a return filed late with its tax paid late attracts the 10% penalty and interest on the tax |
| Interest | 10.25% a year from 2 March 2026 on late or underpaid VAT, compounding monthly (TAA s 187). SARS sets the rate by reference to the repo rate, so read the current SARS interest rate table rather than relying on this figure |
| Understatement | 10% to 200% of the shortfall depending on behaviour (TAA ss 222 to 224) |

### 6.1 Mixed Supplies Apportionment

- **Mixed Supplies Apportionment** — Input tax must be apportioned when making both taxable and exempt supplies. Directly attributable input follows its supply. Residual input is apportioned by the standard turnover-based method of BGR 16 (taxable supplies as a fraction of total supplies, recomputed each year); another method (transaction count, headcount, floor area) needs a ruling under s 41B. De minimis: where taxable supplies are at least 95% of total supplies, the full input is claimed. Flag for reviewer.  _(VAT Act s 17(1), s 41B; BGR 16; CSARS v African Bank Ltd [2025] ZASCA 101)_

### 6.2 Imported Services (Reverse Charge, s 7(1)(c))

- **Imported Services** — An imported service is a service supplied by a non-resident, or by a resident from outside South Africa, to a resident recipient for use otherwise than in making taxable supplies. A fully taxable vendor who buys a service for its taxable supplies has no imported service to declare; a non-vendor or a partly exempt vendor declares the VAT on the portion used otherwise than for taxable supplies, on Form VAT215 (a non-vendor) or in Field 12 of the VAT201 (a vendor), and no input tax is deductible on that portion; the portion used for taxable supplies is not an imported service. Where the foreign supplier is a registered foreign electronic services supplier and charges SA VAT, the invoice is an ordinary input.  _(VAT Act s 7(1)(c), s 14; Foreign Suppliers of Electronic Services Regulations)_

### 6.3 Second-Hand Goods Input Tax (s 16(3)(a)(ii))

- **Second-Hand Goods Input Tax** — Notional input tax: tax fraction (15/115) of consideration paid. Requires declaration from seller and proof of payment. Cannot exceed lesser of consideration paid or open market value. Flag for reviewer.

### 6.4 Change from Payments to Invoice Basis

- **Change from Payments to Invoice Basis** — When turnover exceeds R2,500,000. Transitional adjustments required. Flag for tax practitioner.

### 6.5 Motor vehicle -- is it a "motor car" as defined?

- **Motor vehicle test** — What it shows: Vehicle purchase, lease, rental, or maintenance payment. What's missing: Whether the vehicle is a "motor car" as defined in s 1 (objective test per IN 82 -- passenger area vs loading area). Conservative default: BLOCKED -- no input tax on supply of motor car. Question: "Is this a passenger vehicle (sedan, SUV, hatchback, double-cab bakkie, minibus)? If yes: input on purchase/lease/rental is blocked under s 17(2)(c). Running costs (fuel, repairs, insurance) are claimable for business use." Exception: vendor who continuously supplies motor cars in ordinary course (dealers, rental companies).

### 6.6 Entertainment -- which exception applies?

- **Entertainment sub-cases** — Input tax on entertainment (meals, beverages, accommodation, social functions, prizes, hampers, corporate gifts, golf days, year-end functions) is blocked under s 17(2)(a). Default: blocked. Exceptions to test: the vendor is in the business of supplying entertainment (restaurants, hotels, venues); subsistence for an employee away from the usual place of work for at least one night; an employee canteen that charges at least cost; bona fide promotional gifts within the BGR conditions; and long-distance road transport operators' meals for their personnel. Question: "Is the vendor in the entertainment trade, or does one of the listed exceptions apply?"  _(VAT Act s 17(2)(a); BGR 16; SARS IN 70)_

### 6.7 Fringe benefits -- output VAT on employee benefits (s 18(3))

- **Deemed supplies to employees** — A VAT-registered employer who grants a Seventh Schedule fringe benefit makes a deemed taxable supply under s 18(3) and pays output VAT on the cash equivalent in the tax period in which the benefit accrues (s 9(7), s 10(13)). Common items: the right of use of a company car (3.5% of the determined value a month, 3.25% where a maintenance plan applies, on which the VAT is computed by the tax fraction), free or cheap services, and assets given below market value, where the underlying supply would be taxable. Excluded by the proviso to s 18(3): a benefit that is an exempt supply (a low-interest loan is an exempt financial service under s 12(a); residential accommodation is exempt under s 12(c)), a zero-rated supply, or a benefit on which the employer's input tax was denied under s 17(2) (entertainment, a blocked motor car). No output VAT arises on those. Question: "Do you employ staff and grant any of these benefits?"  _(VAT Act s 18(3), s 9(7), s 10(13); Income Tax Act Seventh Schedule)_

### 6.8 Tax invoice compliance (s 20)

- **Full tax invoice contents** — The single most common reason SARS disallows input. For a supply above R5,000 (VAT inclusive) the invoice must carry: the words "Tax Invoice", "VAT Invoice" or "Invoice"; the supplier's name, address and VAT registration number; the recipient's name, address and VAT number; a serial number and the date; a description of the goods or services and their quantity or volume; and either the consideration and the VAT, or the consideration with a statement that it includes VAT at 15%. Between R50 and R5,000 an abridged invoice omits the recipient's details and the quantity; at R50 or less no invoice is required but a till slip is kept. Question: "Do all supplier tax invoices meet these requirements? Has SARS queried any?"  _(VAT Act s 20(4), (5) and (6); SARS Tax Invoices page)_

### 6.9 Diesel refund

- **Out of scope** — Vendors in mining, farming, electricity generation, rail, foreign-going ships and offshore operations complete the diesel refund schedule (Fields 21 to 38) on the VAT201. Refer to a specialist.  _(Customs and Excise Act Schedule 6 Part 3; VAT Act s 75)_

## Section 7 -- Working Paper Template

```
SOUTH AFRICA VAT WORKING PAPER (VAT201)
Vendor: _______________  VAT Number: ___________
Period: ___________  Category: A / B / C / D / E / F
Basis: Invoice / Payments

A. OUTPUT (SALES)
  A1. Standard-rated supplies, VAT-inclusive, excl. capital goods -> Field 1   ___________
  A2. Standard-rated capital goods supplied, VAT-inclusive -> Field 1A         ___________
  A3. Output VAT: A1 x 15/115 -> Field 4; A2 x 15/115 -> Field 4A             ___________
  A4. Zero-rated supplies -> Field 2 (excl. exports) / Field 2A (exported goods) ___________
  A5. Exempt supplies -> Field 3                                                ___________
  A6. Commercial accommodation over 28 days -> Fields 5 to 9                    ___________
  A7. Change-in-use and second-hand goods exported -> Field 10 / Field 11       ___________
  A8. Other output adjustments and imported services -> Field 12                ___________
  A9. Total output tax (4 + 4A + 9 + 11 + 12) -> Field 13                       ___________

B. INPUT (PURCHASES)
  B1. Input VAT on capital goods -> Field 14 (imported: Field 14A)              ___________
  B2. Input VAT on other goods and services -> Field 15 (imported: Field 15A)   ___________
  B3. Change-in-use input adjustment -> Field 16                                ___________
  B4. Bad debts (s 22) -> Field 17                                              ___________
  B5. Other input adjustments -> Field 18                                       ___________
  B6. Blocked input (entertainment, motor cars): excluded, no field             ___________
  B7. Total input tax (14 + 14A + 15 + 15A + 16 + 17 + 18) -> Field 19         ___________

C. NET VAT
  C1. Net VAT payable / (refundable): Field 13 - Field 19 -> Field 20           ___________
  C2. Prior period credit carried forward (per the SARS statement of account)   ___________

REVIEWER FLAGS:
  [ ] Registration and vendor number confirmed?
  [ ] Filing category confirmed?
  [ ] Accounting basis confirmed?
  [ ] Tax invoices held for all input claims (full, abridged or till slip by value band)?
  [ ] Second-hand goods documentation complete (VAT264, identity, proof of payment)?
  [ ] Zero-rated vs exempt correctly distinguished; export documents held?
  [ ] Motor car and entertainment inputs blocked?
  [ ] Output VAT on fringe benefits (s 18(3)) and change-in-use adjustments (s 18) included?
```

### South African Bank Statement Formats

**Bank Statement Formats table**

| Bank | Format | Key Fields |
| --- | --- | --- |
| FNB | CSV / PDF | Date, Description, Amount, Balance |
| ABSA | CSV | Date, Description, Debit, Credit, Balance |
| Standard Bank | CSV | Date, Description, Debit, Credit, Balance |
| Nedbank | CSV | Date, Description, Debit, Credit, Balance |
| Capitec | CSV | Date, Description, Debit, Credit, Balance |
| Investec | CSV | Date, Description, Debit, Credit, Balance |

### Key SA Banking Narrations

**Key SA Banking Narrations table**

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| EFT CREDIT / INWARD PAYMENT | Bank transfer in | Potential income |
| DEBIT ORDER / DEBI CHECK | Direct debit | Regular expense |
| POS / CARD PURCHASE | Point of sale | Expense |
| CASH DEPOSIT | Cash received | Income |
| SARS / RECEIVER OF REVENUE | Tax payment or refund | Exclude |
| BANK CHARGES / SERVICE FEE | Bank fee | Standard-rated 15% -- input claimable (s 2(1) proviso) |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all EFT credits from business sources as potential taxable supplies
2. Apply conservative defaults: invoice basis, standard-rated, 0% private recovery
3. Only claim input VAT where VAT is clearly evident
4. Flag all large purchases for capital goods review

Present these questions:

```
ONBOARDING QUESTIONS -- SOUTH AFRICA VAT
1. Are you registered as a VAT vendor? What is your VAT number?
2. What filing category are you (A bimonthly, B monthly, C six-monthly, D or E annual, F four-monthly)?
3. Are you on invoice basis or payments basis?
4. What types of goods or services do you sell?
5. Do you make any zero-rated supplies (exports, basic foodstuffs)?
6. Do you make any exempt supplies (financial, residential rent, education)? Do you buy anything used for both taxable and exempt supplies (mixed-use input)?
7. Do you purchase second-hand goods from non-vendors?
8. Do you import services from non-resident suppliers, and do their invoices show SA VAT?
9. Do you have any motor cars (including double cabs, station wagons, SUVs, minibuses) in the business? Have you claimed input tax on the purchase, lease or rental of any vehicle?
10. Do you employ staff and grant any fringe benefits (company car, low-interest loan, assets below market value, free or cheap services, accommodation)?
11. Do you incur entertainment, meals, accommodation or social functions for clients or staff?
12. Do all your supplier tax invoices meet the s 20 requirements? Has SARS queried any?
```

### Key Legislation

**Key Legislation table**

| Topic | Section |
| --- | --- |
| Definitions ("motor car", "entertainment", "tax fraction") | VAT Act s 1 |
| Financial services and the fee-based proviso | VAT Act s 2 |
| Imposition of VAT; imported services | VAT Act s 7, s 14 |
| Deemed supplies (insurance payouts, fringe benefits) | VAT Act s 8(8), s 18(3) |
| Time and value of supply | VAT Act s 9, s 10 |
| Zero-rated supplies | VAT Act s 11 |
| Exempt supplies | VAT Act s 12 |
| Accounting basis | VAT Act s 15 |
| Input tax; blocked input; apportionment | VAT Act s 16, s 17 |
| Change-in-use adjustments | VAT Act s 18 |
| Tax invoices | VAT Act s 20 |
| Bad debts | VAT Act s 22 |
| Registration | VAT Act s 23 |
| Filing | VAT Act s 27, 28 |
| Agents and principals | VAT Act s 54 |
| Interest, penalties, understatement | TAA s 187, s 210, s 213, ss 222 to 224 |

### Known Gaps / Out of Scope

- Cross-border services (complex)
- Customs VAT on imports
- VAT grouping
- Large-value property transactions

### Changelog

**Changelog table**

| Version | Date | Change |
| --- | --- | --- |
| 2.1 | May 2026 | Validated by Werner Britz CA(SA); corrected R2.3m registration threshold; corrected bank charges and payment processor fees to standard-rated; corrected VAT201 field structure; added motor car block; corrected Uber/Bolt to exempt; corrected fuel to zero-rated; added entertainment block; removed Kulula (ceased 2022) |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; SA bank formats; local payment patterns (PayFast, Yoco, SnapScan); worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Registration and vendor number confirmed?
- [ ] Filing category and accounting basis confirmed?
- [ ] Tax fraction 15/115 used consistently?
- [ ] Zero-rated vs exempt correctly distinguished?
- [ ] Second-hand goods claims properly documented?
- [ ] Bad debt relief only after 12 months?
- [ ] Motor car inputs blocked (s 17(2)(c)) and entertainment inputs blocked (s 17(2)(a))?
- [ ] Output VAT on fringe benefits (s 18(3)) and change-in-use adjustments (s 18) included?

## PROHIBITIONS

- **NEVER claim input tax on exempt supplies** — only taxable (including zero-rated) supplies qualify
- **NEVER charge VAT if not registered as a vendor** — 
- **NEVER use a rate other than 15% for standard-rated supplies** — 
- **NEVER confuse zero-rated (input tax claimable) with exempt (input tax NOT claimable)** — 
- **NEVER claim input tax without a valid tax invoice (for supplies over R50)** — 
- **NEVER ignore the bimonthly filing deadline -- penalties apply from the first day late** — 
- **NEVER apply payments basis without SARS approval** — 
- **NEVER claim notional input on second-hand goods without proper documentation and declarations** — 
- **NEVER claim input on the supply (purchase, lease, rental) of a motor car as defined, unless within an exception under s 17(2)(c)** — 
- **NEVER claim input on entertainment, accommodation, or food and beverages unless the vendor is in the business of providing entertainment or the supply is to an employee away from usual place of work** — 
- **NEVER exclude bank service fees as exempt -- they are standard-rated and input claimable (s 2(1) proviso)** — 
- **NEVER omit output VAT on Seventh Schedule fringe benefits granted to employees under s 18(3)** — 
- **NEVER present calculations as definitive -- always label as estimated and direct client to a SARS-registered tax practitioner** — 

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, chartered accountant (CA(SA)), or equivalent licensed practitioner in South Africa) before filing or acting upon.

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
