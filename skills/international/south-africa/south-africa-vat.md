---
name: south-africa-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a South Africa VAT return (VAT201), classify transactions for South African VAT purposes, or advise on VAT registration and filing in South Africa. Trigger on phrases like "South Africa VAT", "VAT201", "SARS VAT", "input tax South Africa", "output tax South Africa", "South African Revenue Service VAT", or any SA VAT request. ALWAYS read this skill before touching any South Africa VAT work.
version: 2.1
jurisdiction: ZA
tax_year: 2025
last_updated: 2026-09-29
reviewed_by: Werner Britz
review_status: current
depends_on:
  - vat-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# South Africa VAT

## South Africa VAT (VAT201) Skill v2.1

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Werner Britz** on 2026-06-12; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.

## Section 1 — Quick reference

**Section 1 — Quick reference**

| Field | Value |
| --- | --- |
| Country | South Africa (Republic of South Africa) |
| Tax | VAT (Value-Added Tax) |
| Currency | ZAR (South African Rand / R) |
| Tax year | Tax periods under s 27: Category A bimonthly (default); B monthly (>R30m); C six-monthly (farming <R1.5m); D annual (connected-party farming/rental); E annual (connected-party rental); F four-monthly (micro businesses on turnover tax). No quarterly category exists. |
| Standard rate | 15% |
| Zero rate | 0% (exports; basic foodstuffs (Schedule 2); international transport; certain farming inputs; petrol/diesel; illuminating paraffin; supply of enterprise as going concern (s 11(1)(e)); gold to SARB/bank) |
| Exempt | Financial services (narrow s 2 definition -- interest, exchange margins, life insurance, dealing in securities; fee-based services are STANDARD-RATED per s 2(1) proviso), residential rental, public road and rail transport (s 12(g)), educational services by recognised institutions, childcare, donated goods/services by associations not for gain. Short-term insurance is STANDARD-RATED, not exempt. |
| Registration threshold | ZAR 2,300,000 in any consecutive 12-month period (from 1 April 2026). Voluntary registration: ZAR 120,000. |
| Tax authority | SARS (South African Revenue Service) |
| Return form | VAT201 (eFiling) |
| Filing portal | SARS eFiling (https://www.sarsefiling.co.za) — the `efiling.sars.gov.za` form does not resolve |
| Filing frequencies | Category A bimonthly (default); Category B monthly (>R30m); Category C six-monthly (farming <R1.5m); Category D annual (connected-party farming/rental); Category E annual (connected-party rental); Category F four-monthly (micro businesses on turnover tax) |
| Filing deadline | Last business day of month following tax period (eFiling); 25th for paper (not recommended) |
| Tax invoice | Required for input tax: a full tax invoice above R5,000 (VAT inclusive, s 20(4)); an abridged invoice from R50 to R5,000 (s 20(5)); no invoice at R50 or less (s 20(6)) but keep the till slip. See Section 5.4 |
| VAT number | Format: 4xxxxxxxx (10 digits starting with 4) |
| Contributor | Open Accountants Community |
| Validated by | Werner Britz CA(SA), Spurwing CFO |
| Validation date | May 2026 |
| Skill version | 2.1 |

### Key VAT201 fields

**Key VAT201 fields**

| Field | Meaning |
| --- | --- |
| 1 | Standard-rated supplies (VAT-inclusive, excluding capital goods) |
| 1A | Standard-rated capital goods supplied (VAT-inclusive) |
| 2 | Zero-rated supplies (excluding exports) |
| 2A | Zero-rated exported goods |
| 3 | Exempt and non-supplies |
| 4 | Output VAT on Field 1 (Field 1 x 15/115) |
| 4A | Output VAT on Field 1A |
| 5 | Commercial accommodation supplied for 28+ days |
| 9 | Output VAT on commercial accommodation |
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

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 15% standard |
| Unknown counterparty country | Domestic South Africa |
| Unknown export qualification | 15% until export evidence confirmed |
| Unknown business-use % (vehicle, entertainment) | 0% input tax. Note: for motor cars as defined, input is FULLY BLOCKED under s 17(2)(c) regardless of business use percentage. |
| Unknown whether tax invoice compliant | No input tax |
| Unknown whether zero-rated or exempt | Treat as taxable 15% |
| Unknown B2B vs B2C for cross-border | 15% if consumed in South Africa |

### Red flag thresholds

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single transaction | ZAR 50,000 |
| HIGH tax delta on single default | ZAR 7,500 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | ZAR 30,000 |

### Required inputs

Minimum viable — bank statement for the tax period in CSV, PDF, or pasted text. VAT registration number (starting with 4).

Recommended — tax invoices for every input claim (a full tax invoice above ZAR 5,000, an abridged invoice from ZAR 50 to ZAR 5,000, a till slip at ZAR 50 or less), sales invoices for all output, and the prior period excess credit from the SARS statement of account (it is not a VAT201 field; Field 14 is input VAT on capital goods).

Ideal — complete creditors/debtors ledger, import VAT certificates (SAD500), asset register, prior VAT201 return.

Refusal if minimum missing — SOFT WARN. No bank statement = hard stop. "Input tax credits require a valid VAT tax invoice per Section 20 of the VAT Act. All credits are provisional pending invoice verification."

### Refusal catalogue

- **R-ZA-1 — Non-VAT-registered vendor** — "Only registered vendors can charge VAT and claim input tax. Confirm VAT registration before proceeding."  _(R-ZA-1)_
- **R-ZA-2 — Partial exemption / apportionment** — "If the vendor makes both taxable and exempt supplies, input tax must be apportioned under Section 17(1) of the VAT Act. The apportionment ratio changes annually — out of scope without full-year data. Escalate to a CA(SA)."  _(R-ZA-2, Section 17(1) VAT Act)_
- **R-ZA-3 — Change-in-use adjustments (Section 18)** — "South Africa has no capital goods scheme of the EU kind. Adjustments under s 18 apply when goods or services acquired for taxable use are applied for non-taxable use (s 18(1): output VAT on the lesser of cost and open market value), when previously non-claimed goods are brought into taxable use (s 18(4): input on the lesser of cost and open market value), and when the taxable-use proportion of a capital asset changes (s 18(2)). They require specialist computation. Out of scope."  _(R-ZA-3, VAT Act s 18)_
- **R-ZA-4 — Financial services (Section 2)** — "Financial services have complex VAT treatment. Banks, insurers, and financial institutions require specialist handling. Out of scope."  _(R-ZA-4, Section 2)_
- **R-ZA-5 — Property transactions** — "South Africa has no option to tax commercial property. A vendor's sale of commercial property is standard-rated by default; the going-concern zero-rating under s 11(1)(e) needs both parties to be vendors, a written agreement that the supply is of a going concern and the enterprise to be income-earning at transfer; and transfer duty applies instead of VAT where the seller is not a vendor. Highly fact-sensitive: escalate to a specialist."  _(R-ZA-5, VAT Act s 11(1)(e); Transfer Duty Act)_

### 3.1 South African banks — fees (standard-rated per s 2(1) proviso)

**South African banks — fees (standard-rated per s 2(1) proviso)**  _(s 2(1) proviso; s 12(a); s 2(1)(f))_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ABSA BANK, ABSA GROUP | Input 15% | Bank service fees are standard-rated per s 2(1) proviso; banks issue monthly VAT tax invoices. Interest remains exempt. |
| STANDARD BANK, STANBIC | Input 15% | Standard-rated per s 2(1) proviso |
| FIRSTRAND, FNB, FIRST NATIONAL BANK | Input 15% | Standard-rated per s 2(1) proviso |
| NEDBANK | Input 15% | Standard-rated per s 2(1) proviso |
| CAPITEC BANK | Input 15% | Standard-rated per s 2(1) proviso |
| INVESTEC | Input 15% | Standard-rated per s 2(1) proviso |
| AFRICAN BANK | Input 15% | Standard-rated per s 2(1) proviso |
| BANK CHARGES, SERVICE FEE | Input 15% | Standard-rated per s 2(1) proviso |
| INTEREST | EXCLUDE | Exempt under s 12(a) / s 2(1)(f) |

### 3.2 South African government and statutory (exclude)

**South African government and statutory (exclude)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SARS, SOUTH AFRICAN REVENUE SERVICE | EXCLUDE | Tax payment |
| UIF, UNEMPLOYMENT INSURANCE FUND | EXCLUDE | Statutory contribution |
| WORKMEN'S COMP, COIDA | EXCLUDE | Compensation fund |
| MUNICIPALITY, LOCAL AUTHORITY (rates) | EXCLUDE the rates; claim the rest | Property rates are outside VAT. The electricity, water and refuse charges on the same municipal bill are standard-rated and input is claimable, so split the bill by line |
| ROAD ACCIDENT FUND, RAF | EXCLUDE | Statutory levy |

### 3.3 South African utilities (taxable at 15%)

**South African utilities (taxable at 15%)**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| ESKOM | Input 15% | 15% | National electricity — taxable |
| CITY POWER (Johannesburg) | Input 15% | 15% | Municipal electricity — taxable |
| CAPE TOWN ELECTRICITY | Input 15% | 15% | Municipal electricity — taxable |
| RAND WATER, RAND WATER BOARD | Input 15% | 15% | Water — taxable |
| CITY OF CAPE TOWN WATER | Input 15% | 15% | Water — taxable |
| VODACOM | Input 15% | 15% | Mobile/internet — taxable |
| MTN SOUTH AFRICA | Input 15% | 15% | Mobile — taxable |
| CELL C | Input 15% | 15% | Mobile — taxable |
| TELKOM SA | Input 15% | 15% | Fixed-line/internet — taxable |
| RAIN NETWORK | Input 15% | 15% | Internet — taxable |
| AFRIHOST | Input 15% | 15% | Internet — taxable |

### 3.4 Transport and logistics

**Transport and logistics**  _(s 12(g))_

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| SOUTH AFRICAN AIRWAYS, SAA | Check route and split the ticket | 0%/15% | International 0% (s 11(2)(a)); domestic 15%, but not on every line of the e-ticket: the base fare, fuel surcharge, passenger service charge and insurance carry 15% and are claimable; the SACAA and ATNS charges and the Air Passenger Tax carry no VAT |
| FLYSAFAIR, LIFT, CEMAIR | Split the ticket | 15% on VATable components | Domestic airlines; the same component split as SAA applies, so "15% on the ticket total" over-claims |
| AIRLINK | Check route and split the ticket | 0%/15% | International 0%; domestic 15% on the VATable components only |
| UBER SOUTH AFRICA / BOLT SOUTH AFRICA | EXEMPT (s 12(g)) | — | Fare is exempt -- road transport of fare-paying passengers. No input VAT claimable on the fare. Only the booking fee (if separately shown on Uber tax invoice) may carry input VAT. |
| DHL SOUTH AFRICA | Input 15% | 15% | Courier — taxable |
| FEDEX SOUTH AFRICA | Input 15% | 15% | Courier — taxable |
| DAWN WING | Input 15% | 15% | Courier — taxable |
| THE COURIER GUY, TCG | Input 15% | 15% | Courier — taxable |
| ARAMEX SOUTH AFRICA | Input 15% | 15% | Courier — taxable |

### 3.5 Food and retail

**Food and retail**  _(s 17(2)(a))_

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| CHECKERS, SHOPRITE | Input 15%/0% | Mixed | Basic zero-rated food items; non-food 15%. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| PICK N PAY, PNP | Input 15%/0% | Mixed | Same — zero-rate basic foodstuffs. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| WOOLWORTHS FOOD | Input 15%/0% | Mixed | Food hall: basic items 0%; prepared/luxury food 15%. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| SPAR | Input 15%/0% | Mixed | Same. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| FOOD LOVERS MARKET | Input 15%/0% | Mixed | Same. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| CLICKS | Input 15% on office consumables; BLOCKED on entertainment items | 15% | Claimable for business use: cleaning supplies, toiletries for the office, stationery, first-aid supplies (required under the OHS Act), batteries and other consumables. Blocked under s 17(2)(a): food, beverages and snacks for staff or clients. Personal items: not business |
| DIS-CHEM | Input 15% | 15% | Prescription medicines are standard-rated at 15%; all pharmacy items 15% |
| MCDONALD'S SA, STEERS, NANDO'S | BLOCKED under s 17(2)(a) | 15% | BLOCKED under s 17(2)(a) for the buying business. Only the restaurant itself (being in the entertainment trade) can claim its own inputs. |

- **Zero-rated basic foodstuffs** — Brown bread, maize meal, mielie rice, dried mealies, dried beans, lentils, pilchards/sardines in tins, milk, eggs, fruits and vegetables, vegetable oil, edible legumes. These are zero-rated under Schedule 2 of the VAT Act.  _(Schedule 2 of the VAT Act)_

### 3.6 SaaS — international suppliers (reverse charge / imported services)

- **Imported services rule** — An imported service is a service supplied by a non-resident, or by a resident from outside South Africa, to a recipient who is a resident, for use otherwise than in making taxable supplies (VAT Act s 7(1)(c) read with s 14). A fully taxable vendor buying a service for its taxable supplies therefore has nothing to self-assess; a non-vendor or a partly exempt vendor declares the VAT on the portion of the service used otherwise than for taxable supplies (Form VAT215 for a non-vendor; Field 12 of the VAT201 for a vendor), and no input tax is deductible on that portion, so it is a cost; the portion used for taxable supplies is not an imported service at all. Most large foreign platforms are registered as foreign suppliers of electronic services and charge SA VAT on the invoice, in which case the invoice is an ordinary input: check the invoice before self-assessing.  _(VAT Act s 7(1)(c), s 14; Foreign Suppliers of Electronic Services Regulations (2014, expanded 2019))_

**SaaS — international suppliers**  _(VAT Act s 7(1)(c), s 14; Foreign Suppliers of Electronic Services Regulations)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE (Workspace, Ads, Cloud) | Standard input where the invoice shows SA VAT | Billed by Google SA or Google Ireland as a registered foreign electronic services supplier; where an invoice carries no SA VAT, apply the imported-services test above (nothing to declare for a fully taxable vendor) |
| MICROSOFT (365, Azure) | Standard input | Registered foreign electronic services supplier; bills SA VAT directly |
| META, FACEBOOK ADS | Standard input | Meta SA (Pty) Ltd or Meta Platforms Ireland bills SA VAT |
| ZOOM, SLACK | Standard input | Registered for SA VAT; bill SA VAT directly |
| NOTION, OPENAI, ANTHROPIC | Check the invoice | Some are SA VAT-registered (Notion, OpenAI); a supplier billing from a foreign entity without SA VAT (Anthropic API direct billing at the review date) is an imported service only to the extent the vendor uses it otherwise than for making taxable supplies: nothing to declare for a fully taxable vendor; a partly exempt vendor declares output VAT on the exempt-use portion in Field 12, with no input tax on it |
| AWS | Standard input | The AWS South Africa region bills SA VAT to SA-resident accounts |
| XERO (billed from NZ) | Standard input | Xero South Africa now bills SA customers with SA VAT |
| SAGE (billed from the UK) | Check the invoice | Sage South Africa bills SA VAT; a UK-billed invoice without SA VAT is an imported service only for the portion used otherwise than for taxable supplies (nothing to declare for a fully taxable vendor) |

### 3.7 Local SaaS and professional tools (15%)

**Local SaaS and professional tools (15%)**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| XERO (South Africa entity) | Input 15% | 15% | Accounting software |
| SAGE SOUTH AFRICA | Input 15% | 15% | Accounting/payroll |
| PASTEL, SAGE PASTEL | Input 15% | 15% | South African accounting |
| QUICKBOOKS SOUTH AFRICA | Input 15% | 15% | Accounting SaaS |

### 3.8 Payment processors (standard-rated per s 2(1) proviso)

**Payment processors (standard-rated per s 2(1) proviso)**  _(s 2(1) proviso)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PAYFAST (transaction fees) | Input 15% | Standard-rated -- fee-based payment processing is not a financial service per s 2(1) proviso |
| YOCO (transaction fees) | Input 15% | Standard-rated -- fee-based payment processing is not a financial service per s 2(1) proviso |
| PEACH PAYMENTS (fees) | Input 15% | Standard-rated -- fee-based payment processing is not a financial service per s 2(1) proviso |
| STRIPE (fees) | Input 15% | Standard-rated -- fee-based payment processing is not a financial service per s 2(1) proviso |

### 3.9 Internal transfers and exclusions

**Internal transfers and exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN ACCOUNT TRANSFER, INTER-ACCOUNT | EXCLUDE | Internal movement |
| LOAN, BOND REPAYMENT | EXCLUDE | Loan principal |
| SALARY, WAGES, PAYROLL | EXCLUDE | Outside VAT scope |
| DIVIDEND | EXCLUDE | Out of scope |
| MUNICIPAL RATES, PROPERTY RATES | EXCLUDE | Local government levy — not a supply |
| ATM, CASH WITHDRAWAL | Tier 2 — ask | Default exclude |

## Section 4 — Worked examples

Six classifications from a hypothetical Johannesburg-based IT consultant. Format: FNB (First National Bank) account statement.

### Example 1 — Domestic B2B revenue (15%)

**Input line:**
`15 Apr 2025  CREDIT  ABC TECHNOLOGY (PTY) LTD  INV-2025-041  R 115,000.00  R 500,000.00`

**Reasoning:**
Incoming R 115,000 (VAT-inclusive) from a SA company for IT consulting. Standard 15% VAT. Gross R 115,000 includes VAT. Net = R 100,000 (taxable supply) + R 15,000 output tax (R 115,000 × 15/115). A VAT-compliant tax invoice must be issued per Section 20 of the VAT Act. Report R 115,000 VAT-inclusive on VAT201 Field 1. Output VAT R 15,000 goes to Field 4.

**Classification:** Output tax 15% — R 15,000. Net supply: R 100,000. VAT-inclusive: R 115,000.

### Example 2 — Export service (zero-rated)

**Input line:**
`22 Apr 2025  CREDIT  ACME CORP USA  USD 5,000 (R 92,500)  R 592,500.00`

**Reasoning:**
USD receipt from a US company for IT consulting services exported from South Africa. Zero-rated under s 11(2)(l) of the VAT Act (Schedule 1 is not the zero-rating schedule; Schedule 2 lists zero-rated goods) provided the services are supplied to a non-resident who is not in South Africa when the services are rendered, and the services are not supplied directly in connection with land or movable property in South Africa. Evidence: contract showing the foreign client, its location abroad, payment in foreign currency. Report R 92,500 on Field 2 (zero-rated supplies other than exported goods). Output tax: R 0.

**Classification:** Zero-rated export — R 92,500. Output tax: R 0.

### Example 3 — Electricity (15%, input credit)

**Input line:**
`10 Apr 2025  DEBIT  ESKOM HOLDINGS SOC  April electricity  -R 11,500.00  R 388,500.00`

**Reasoning:**
Eskom electricity bill. Taxable at 15%. Gross R 11,500. Net = R 10,000 + R 1,500 input tax (R 11,500 × 15/115). Eskom issues VAT-compliant tax invoices — input credit of R 1,500 claimable. Report on Field 15 (input VAT on other goods/services).

**Classification:** Input tax 15% — R 1,500. Net expense: R 10,000.

### Example 4 — Zero-rated food (basic foodstuffs)

**Input line:**
`12 Apr 2025  DEBIT  PICK N PAY  Groceries (business kitchen)  -R 800.00  R 387,700.00`

**Reasoning:**
Grocery purchase. If itemised receipt shows basic foodstuffs only (brown bread, eggs, fresh vegetables, etc.) — zero-rated under Schedule 2 of the VAT Act. No input tax on zero-rated items (the input tax rate is 0%). If mixed grocery (some 15% non-food items), split the purchase. Without itemised receipt: conservative default is 15% on full amount.

**Classification:** Zero-rated (if basic foodstuffs only) — R 0 input tax. Conservative default: 15% on R 800 = R 104 input tax / (R 695.65 net + R 104 VAT = R 800 gross). Flag: obtain itemised receipt.

### Example 5 — Imported service — self-assess (Google Ads)

**Input line:**
`08 Apr 2025  DEBIT  GOOGLE IRELAND LIMITED  Google Ads April  -R 10,000.00  R 377,700.00`

**Reasoning:**
Google Ads billed from Ireland. Note: Google typically bills SA VAT directly now via its local entity; check the invoice. If billed by a non-resident entity without SA VAT, apply the imported-services test of s 7(1)(c) and s 14: the service is an imported service only to the extent it is used otherwise than for making taxable supplies. A fully taxable vendor buying the advertising for its taxable supplies has no imported service and declares nothing (the habit of declaring R 1,500 output in Field 12 and R 1,500 input in Field 15 for a net of zero reports a supply the Act does not deem to exist). A partly exempt vendor with, say, 40% exempt use declares output VAT of R 10,000 × 40% × 15% = R 600 in Field 12, with no input tax on it.

**Classification:** No SA VAT on the invoice: nothing to declare for a fully taxable vendor; a partly exempt vendor declares output VAT on the exempt-use share in Field 12 (R 600 at 40% exempt use), no input.

### Example 6 — Rent: commercial premises versus a dwelling

**Input line:**
`01 Apr 2025  DEBIT  CITY PROP MANAGEMENT  April office rent  -R 23,000.00  R 354,700.00`

**Reasoning:**
Monthly rent. South Africa has no "option to tax": a landlord of commercial premises charges VAT if the landlord is a registered vendor (compulsorily or voluntarily) and none if not, and the letting of a dwelling is exempt under s 12(c) whatever the landlord's status. If this is commercial office space and the landlord issues a tax invoice showing 15% VAT, input tax of R 3,000 is claimable (R 23,000 × 15/115). If the landlord is not registered (common for individual landlords below the threshold), no VAT was charged and there is nothing to claim. Default: ask whether the premises are commercial or residential and for the landlord's tax invoice.

**Classification:** Tier 2 — ask. Commercial premises with a tax invoice from a registered landlord: Input 15% — R 3,000. Unregistered landlord: no VAT charged, no input. Dwelling: EXEMPT — no input tax.

### 5.1 Standard rate 15%

- **Standard rate** — 15% (Default rate for all taxable supplies)  _(VAT Act No. 89 of 1991, Section 7(1)(a))_

### 5.2 Zero rate 0%

- **Zero rate 0% supplies** — Exports of goods and qualifying services; basic foodstuffs (Schedule 2); illuminating paraffin; petrol and diesel (specific provisions); certain agricultural inputs; supply of enterprise as going concern (s 11(1)(e)); gold to SARB/bank. Evidence required for export zero-rating. Prescription medicines are STANDARD-RATED at 15%.  _(VAT Act Section 11; Schedule 2)_

### 5.3 Exempt supplies

- **Exempt supplies** — Financial services in the narrow s 2 sense (interest, currency exchange margins, life insurance, dealing in securities; fee-based services are standard-rated under the proviso to s 2(1)); the letting of a dwelling (s 12(c)); public road and rail transport of fare-paying passengers (s 12(g)); educational services by recognised institutions; childcare; donated goods sold by associations not for gain. No output tax charged; no input tax claimable on the related costs.  _(VAT Act Section 12; s 2(1))_

### 5.4 Tax invoice requirements (Section 20)

- **Supplies R50 or less** — NO invoice required (till slip sufficient)  _(Section 20)_
- **Supplies R50 to R5,000** — ABRIDGED tax invoice (omits recipient details)  _(Section 20)_
- **Supplies above R5,000** — FULL tax invoice required with supplier name/address/VAT number, invoice number, date, buyer name/address/VAT number (if VAT-registered), description, net amount, VAT rate, VAT amount, total  _(Section 20)_
- **Tax invoice issuance timeframe** — Must be issued within 21 days.  _(Section 20)_

### 5.5 Imported services

- **Imported services treatment** — An imported service is one supplied by a person not resident or carrying on business in South Africa, or by a resident from outside South Africa, to a South African-resident recipient, used otherwise than for making taxable supplies. A non-vendor declares and pays the VAT on Form VAT215. A partly exempt vendor declares output VAT in Field 12 on the portion used otherwise than for taxable supplies, and no input tax is deductible on that portion, so it is a cost; the portion used for taxable supplies is not an imported service. A fully taxable vendor using the service for its taxable supplies has no imported service to declare; a service partly for private use is declared on the private portion only.  _(VAT Act s 7(1)(c), s 14; SARS Form VAT215)_

### 5.6 Anti-avoidance — entertainment

- **Entertainment input tax block** — Input tax on entertainment, accommodation, and food/beverages is BLOCKED under Section 17(2)(a) UNLESS the vendor is in the business of providing entertainment (hotels, restaurants, conference venues). "Entertainment" includes meals, beverages, social functions, prizes, hampers, recreation and corporate gifts. Other exceptions: subsistence for an employee away from the usual place of work for at least a night; an employee canteen that charges at least cost; bona fide promotional gifts within the BGR conditions; meals supplied by long-distance road transport operators to their personnel.  _(Section 17(2)(a); BGR 16; SARS IN 70)_

### 5.7 Motor vehicles

- **Motor vehicle input tax block** — Input tax on the supply (purchase, lease or rental) of a "motor car" is BLOCKED under Section 17(2)(c) regardless of the business-use percentage, even at 100% business use. "Motor car" is defined in s 1 and is wider than "passenger vehicle" in ordinary speech: it includes station wagons, SUVs, double-cab bakkies and minibuses of up to 16 seats; the test is objective, on the vehicle's construction (passenger area versus loading area, per IN 82), not on how it is used. A single-cab bakkie, a panel van or a truck is not a motor car, and input on it is claimable for business use. Running costs (fuel, repairs, insurance) are claimable even on a blocked motor car. Exceptions: a vendor that continuously supplies motor cars in the ordinary course of its enterprise (dealers, rental companies), and a motor car acquired as a demonstration model or a prize.  _(Section 1, Section 17(2)(c); SARS IN 82; RTCC v CSARS, Tax Court VAT 1345 (2016))_

### 5.8 Filing deadlines

**Filing deadlines**

| Category | Period | Due date |
| --- | --- | --- |
| Category B (>R30m) | Monthly | Last business day of following month |
| Category A (default) | Bimonthly | Last business day of following month |
| Category C (farming <R1.5m) | Six-monthly | Last business day of following month |
| Category D (connected-party farming/rental) | Annual | Last business day of following month |
| Category E (connected-party rental) | Annual | Last business day of following month |
| Category F (micro business turnover tax) | Four-monthly | Last business day of following month |

### 5.9 Penalties

**Penalties**

| Offence | Penalty |
| --- | --- |
| Late payment | Percentage-based penalty of 10% of the tax paid late (VAT Act s 39; TAA s 213) |
| Late return, tax paid on time | No percentage penalty. SARS states that it does not currently impose the fixed-amount administrative non-compliance penalty (TAA ss 210 and 211, a monthly scale by taxable income from R250 to R16,000) for a late VAT return, although the Act allows it; a return filed late with its tax paid late attracts the 10% penalty and interest on the tax |
| Interest | 10.25% a year from 2 March 2026 on late or underpaid VAT, compounding monthly (TAA s 187); SARS sets the rate by reference to the repo rate, so read the current SARS interest rate table |
| Understatement | 10%–200% of the shortfall depending on behaviour (TAA ss 222 to 224) |
| Fraud | Criminal prosecution |

### 6.1 Entertainment — is vendor in the hospitality trade?

**What it shows:** Restaurant, entertainment, or accommodation expense.
**What's missing:** Whether the vendor's primary business is hospitality/entertainment (unblocks the input).
**Conservative default:** BLOCKED — no input tax.
**Question to ask:** "Is this entertainment expense directly related to the provision of entertainment to customers (e.g., you are a restaurant, hotel, or conference venue)? If not, does one of the other exceptions apply: employee subsistence away from the usual place of work, an employee canteen that charges at least cost, or a bona fide promotional gift within the BGR conditions? Otherwise the input tax is blocked."

### 6.2 Motor vehicle — is it a "motor car" as defined?

**What it shows:** Vehicle purchase, lease, rental, or maintenance.
**What's missing:** Whether the vehicle is a "motor car" as defined in s 1: an objective test on the vehicle's construction (passenger area versus loading area, per IN 82), not on its use. Sedans, hatchbacks, SUVs, station wagons, double-cab bakkies and minibuses up to 16 seats are motor cars; single-cab bakkies, panel vans and trucks are not.
**Conservative default:** BLOCKED — no input tax on the supply (purchase, lease or rental) of a motor car, whatever the business-use percentage.
**Question to ask:** "What type of vehicle is it (sedan, SUV, single-cab bakkie, double-cab bakkie, panel van, truck)? If a motor car as defined: input on the purchase, lease or rental is blocked under s 17(2)(c); its running costs (fuel, repairs, insurance) are claimable for business use. If a single-cab bakkie, van or truck used for the business: input is claimable for business use."

### 6.3 Rent — commercial premises from a registered landlord, or a dwelling?

**What it shows:** Monthly rent payment.
**What's missing:** Whether the premises are commercial (standard-rated where the landlord is a registered vendor) or a dwelling (exempt under s 12(c) whatever the landlord's status), and whether the landlord has issued a tax invoice showing 15% VAT. South Africa has no "option to tax".
**Conservative default:** No input tax until a tax invoice is confirmed.
**Question to ask:** "Are the premises commercial or residential? Does your landlord issue a tax invoice for the rent showing their VAT number and 15% VAT? If the landlord is not registered, no VAT was charged and no input credit is available."

### 6.4 Zero-rated basic food vs. standard-rated food

**What it shows:** Supermarket purchase.
**What's missing:** Itemised receipt showing which items are basic (zero-rated) vs. standard (15%).
**Conservative default:** 15% on full amount.
**Question to ask:** "Do you have an itemised till slip? Items like brown bread, eggs, fresh vegetables, milk are zero-rated; packaged snacks, prepared food, non-food items are 15%."

### 6.5 Imported services — partial exemption interaction

**What it shows:** Payment for foreign digital services.
**What's missing:** Whether the vendor has any exempt income that blocks full input tax recovery on imported services.
**Conservative default:** Where every supply the vendor makes is standard-rated or zero-rated, nothing to declare. Where any exempt income exists, declare output VAT in Field 12 on the exempt-use share of the foreign service, claim no input on it, and flag the apportionment for the reviewer.
**Question to ask:** "Does the business have any exempt income (residential rent, financial services)? If yes, the imported services input tax recovery may be limited."

### 6.6 Motor vehicle — is it a "motor car" as defined?

- **Motor car definition and blocked input** — Input tax on the supply of a "motor car" is BLOCKED under s 17(2)(c). "Motor car" definition includes sedans, SUVs, double-cab bakkies, minibuses up to 16 seats. Objective test per IN 82 (passenger area vs loading area). Single-cab bakkies are NOT motor cars. Running costs (fuel, repairs, insurance) ARE claimable even on blocked motor cars. Exception: vendor who continuously supplies motor cars in ordinary course (dealers, rental companies).  _(s 17(2)(c); IN 82)_

### 6.7 Fringe benefits — output VAT on employee benefits (s 18(3))

- **Deemed supplies to employees** — A VAT-registered employer who grants a Seventh Schedule fringe benefit makes a deemed taxable supply under s 18(3) and pays output VAT on the cash equivalent in the tax period in which the benefit accrues (s 9(7), s 10(13)). Common items: the right of use of a company car (3.5% of the determined value a month, 3.25% where a maintenance plan applies), free or cheap services, and assets given below market value, where the underlying supply would be taxable. Excluded by the proviso to s 18(3): a benefit that is an exempt supply (a low-interest loan is an exempt financial service under s 12(a); residential accommodation is exempt under s 12(c)), a zero-rated supply, or a benefit on which the employer's input tax was denied under s 17(2) (entertainment, a blocked motor car). No output VAT arises on those. **Question to ask:** "Do you employ staff and grant any of these benefits?"  _(VAT Act s 18(3), s 9(7), s 10(13); Income Tax Act Seventh Schedule)_

### 6.8 Change-in-use adjustments (s 18)

- **Adjustments** — s 18(1): goods or services acquired for taxable use and later applied for non-taxable use trigger output VAT on the lesser of cost and open market value. s 18(4): goods on which no input was claimed and later brought into taxable use allow an input on the lesser of cost and open market value. s 18(2): a change in the taxable-use proportion of a capital asset above the threshold triggers an annual adjustment. Report in Field 10/11 (output) or Field 16 (input). **Question to ask:** "Has any business asset been taken into private or exempt use, or any private asset brought into the business?"  _(VAT Act s 18)_

### 6.9 Bad debts and bad debts recovered (s 22)

- **Bad debt relief** — A vendor on the invoice basis deducts 15/115 of a bad debt written off where the original supply was taxable, the output VAT was accounted for, the debt is more than 12 months past due (or has been proved irrecoverable) and it has been written off in the books; report in Field 17. If the debt is later recovered, output VAT on the recovered amount is accounted for again (s 22(2)). A vendor on the payments basis never accounted for the output, so gets no relief. **Question to ask:** "Which debts written off were invoiced with VAT more than 12 months ago?"  _(VAT Act s 22(1), s 22(2))_

## Section 7 — Excel working paper template

```
SOUTH AFRICA VAT201 WORKING PAPER
Tax Period: ____________  VAT Registration No.: ____________

A. OUTPUT TAX
  A1. Standard-rated supplies, VAT-inclusive, excl. capital goods -> Field 1   ___________
  A2. Standard-rated capital goods supplied, VAT-inclusive -> Field 1A         ___________
  A3. Output tax: A1 x 15/115 -> Field 4; A2 x 15/115 -> Field 4A             ___________
  A4. Zero-rated supplies -> Field 2 (services, other) / Field 2A (exported goods) ___________
  A5. Exempt supplies -> Field 3                                                ___________
  A6. Commercial accommodation over 28 days -> Fields 5 to 9                    ___________
  A7. Change-in-use and second-hand goods exported -> Field 10 / Field 11       ___________
  A8. Other output adjustments and imported services -> Field 12                ___________
  A9. Total output tax (4 + 4A + 9 + 11 + 12) -> Field 13                       ___________

B. INPUT TAX
  B1. Input tax on capital goods -> Field 14 (imported: Field 14A, SAD500)      ___________
  B2. Input tax on other goods and services -> Field 15 (imported: Field 15A)   ___________
  B3. Imported services input (to the extent of taxable use) -> Field 15        ___________
  B4. Change-in-use input adjustment -> Field 16                                ___________
  B5. Bad debts (s 22) -> Field 17; other input adjustments -> Field 18         ___________
  B6. Blocked input (entertainment, motor cars): excluded, no field             ___________
  B7. Total input tax (14 + 14A + 15 + 15A + 16 + 17 + 18) -> Field 19         ___________

C. NET VAT
  C1. Net VAT payable / (refundable): Field 13 - Field 19 -> Field 20           ___________
  C2. Prior period credit (per the SARS statement of account)                   ___________
  C3. Net payable / (refund) after the credit                                   ___________

REVIEWER FLAGS:
  [ ] Tax invoices (Section 20) confirmed for all input claims?
  [ ] Entertainment and motor car inputs correctly blocked?
  [ ] Export evidence held for zero-rated supplies?
  [ ] Imported services: invoice checked for SA VAT; self-assessed only where none?
  [ ] Basic foodstuffs correctly zero-rated?
  [ ] Rent — commercial premises and landlord tax invoice confirmed?
  [ ] Fringe benefits (s 18(3)), change-in-use (s 18) and bad debts (s 22) considered?
```

### Common South African bank statement formats

**Common South African bank statement formats**

| Bank | Key columns | Date format | Amount |
| --- | --- | --- | --- |
| FNB | Date, Description, Debit, Credit, Balance | DD Mon YYYY | ZAR with 2 decimals |
| Standard Bank | Date, Narrative, Debit, Credit, Balance | DD MMM YYYY | ZAR |
| ABSA | Date, Description, Amount, Balance | DD/MM/YYYY | ZAR |
| Nedbank | Date, Details, Debit, Credit, Balance | DD/MM/YYYY | ZAR |
| Capitec | Date, Description, Debit, Credit, Balance | YYYY-MM-DD | ZAR |

### Key South African banking terms

**Key South African banking terms**

| Term | Meaning | Classification hint |
| --- | --- | --- |
| CREDIT | Incoming funds | Potential revenue |
| DEBIT | Outgoing payment | Potential expense |
| ATM WITHDRAWAL | Cash withdrawal | Tier 2 — ask |
| BANK CHARGES | Bank fee | Standard-rated (s 2(1) proviso) — claim input VAT |
| INTEREST EARNED | Interest received | Exempt |
| BALANCE | Running balance | Ignore |
| SALARY / WAGES | Payroll | Out of VAT scope |
| EFT / EFT DEBIT | Electronic fund transfer | Check direction |

## Section 9 — Onboarding fallback

```
SOUTH AFRICA VAT ONBOARDING — MINIMUM QUESTIONS
1. VAT registration number (10 digits starting with 4)?
2. Tax period covered by this bank statement?
3. Filing frequency: Category A bimonthly, B monthly, C six-monthly, D/E annual, F four-monthly?
4. Do you have any exports (zero-rated)? Evidence held?
5. Do you have exempt income (financial services, residential rent)?
6. Does the business provide entertainment as its primary service?
   (Determines whether entertainment input tax is blocked)
7. Do you own, lease or rent any motor vehicles? What type (sedan, SUV, single-cab bakkie,
   double-cab bakkie, panel van, truck)? The "motor car" block turns on construction, not use.
8. Imported services (Google, Microsoft, etc.) — which suppliers bill SA VAT and which do not?
   Only the latter trigger self-assessment.
9. Prior period credit/refund amount to carry forward?
10. Do you employ staff and grant any Seventh Schedule fringe benefits (company car,
    low-interest loan, cheap or free services, accommodation)? Triggers s 18(3) output VAT.
11. Do all your supplier tax invoices meet the s 20 requirements (full above R5,000,
    abridged R50 to R5,000)? Has SARS queried any?
```

### Key legislation

**Key legislation**

| Topic | Reference |
| --- | --- |
| VAT Act | Value-Added Tax Act No. 89 of 1991 |
| Standard rate | Section 7(1)(a) |
| Zero rate | Section 11; Schedule 2 |
| Exemptions | Section 12 |
| Input tax | Section 16 |
| Blocked input — entertainment | Section 17(2)(a) |
| Blocked input — motor cars | Section 17(2)(c) |
| Tax invoice | Section 20 |
| Imported services | Section 7(1)(c); Section 14 |
| Definitions ("motor car", "entertainment", "tax fraction") | Section 1 |
| Deemed supplies (insurance payouts; fringe benefits) | Section 8(8); Section 18(3) |
| Time and value of supply | Sections 9 and 10 |
| Accounting basis | Section 15 |
| Change-in-use adjustments | Section 18 |
| Bad debts | Section 22 |
| Registration | Section 23 |
| Tax periods and returns | Sections 27 and 28 |
| Agents and principals | Section 54 |
| Interest, penalties, understatement | Tax Administration Act No. 28 of 2011, s 187, s 210, s 213, ss 222 to 224 |

### Known gaps

- Partial exemption (Section 17(1)) apportionment beyond the BGR 16 standard turnover method — escalate
- Property going-concern zero-rating (no "option to tax" exists in South Africa) — escalate
- Financial services VAT — escalate
- Change-in-use adjustments (Section 18) — escalate
- Gold and valuable metals, foreign electronic services supply, mining, long-term insurance, share blocks, instalment credit agreements, connected-person supplies — out of scope

### Self-check

- [ ] All tax invoices Section 20 compliant (full above R5,000; abridged R50 to R5,000; till slip at R50 or less)
- [ ] Entertainment and motor car inputs blocked (the motor car block applies whatever the business-use percentage)
- [ ] Export zero-rating supported by evidence
- [ ] Imported services: invoices checked for SA VAT; self-assessed only where none
- [ ] Basic foodstuffs correctly split from 15% items
- [ ] Output VAT on fringe benefits (s 18(3)) and change-in-use adjustments (s 18) included
- [ ] Bad debt relief (s 22) claimed only on the invoice basis after 12 months
- [ ] Prior period credit carried forward

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2024 | Initial |
| 2.0 | April 2026 | v2.0 rewrite: pattern library, worked examples, no inline tier tags |
| 2.1 | May 2026 | Validated by Werner Britz CA(SA); corrected registration threshold to R2.3m; corrected bank fees and payment processors to standard-rated; corrected VAT201 field structure; corrected Uber/Bolt to exempt; added motor car and entertainment blocks; fixed tax invoice thresholds; removed prescription medicines from zero-rated; fixed filing categories |

## Prohibitions

- NEVER allow input tax on entertainment expenses unless vendor's primary business is hospitality
- NEVER allow input tax on the supply of a motor car as defined, whatever the business-use percentage: even 100% business use is blocked unless a s 17(2)(c) exception applies
- NEVER zero-rate exports without evidence (customs documents, foreign payment records)
- NEVER allow input tax from a non-VAT-registered supplier
- NEVER self-assess imported services without recording both output and input in the same period
- NEVER present calculations as definitive — direct to a CA(SA) or registered tax practitioner
- NEVER claim input on the supply of a motor car as defined, unless within s 17(2)(c) exception
- NEVER claim input on entertainment unless vendor is in the entertainment trade or supply is employee subsistence
- NEVER exclude bank service fees as exempt -- they are standard-rated (s 2(1) proviso)
- NEVER omit output VAT on Seventh Schedule fringe benefits under s 18(3)

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
