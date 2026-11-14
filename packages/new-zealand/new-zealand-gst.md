---
name: new-zealand-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a New Zealand GST return (GST101A form) for a self-employed individual or small business in New Zealand. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST101A", "create the return", "New Zealand GST", "NZ GST", or any request involving New Zealand GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill covers standard GST-registered persons under the invoice or payments basis. Financial services elections, GST groups, non-profit bodies, and complex change-of-use adjustments on high-value mixed-use assets are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any NZ GST work.
version: 2.1
jurisdiction: NZ
category: international
tax_year: 2026
last_updated: 2026-11-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand GST

## New Zealand GST Return Skill (GST101A) v2.1

## Section 1 — Quick reference

**Selected rules checked 13 November 2026.** The verified core below covers ordinary supplies by an established resident GST-registered small business, using its confirmed accounting basis and taxable period. It uses the GST101A layout currently published by Inland Revenue. The form is dated April 2023 and IR375 is dated March 2026. GST is a continuing tax; the frontmatter year records this source check, not an income-year rate change.

Confirm the actual supply, consideration, timing, supplier GST treatment, business use and supporting records before using a figure. A bank narration, supplier name or request for a return cannot establish these facts. Unresolved items stay in a separate reconciliation with their amount and missing evidence recorded. Do not deliver filing-ready figures until all material transactions and adjustments are reconciled. Never omit an unresolved transaction silently.  Do not label an incomplete reconciliation as a nil return. Legacy transaction suggestions and special-regime examples elsewhere in this guide do not establish eligibility and were not reverified by this update.

Stop this ordinary workflow for GST groups, non-resident registration, land or business transfers, marketplaces, imported goods or services, associated persons, secondhand goods credits, hire purchase, progressive/periodic or other special time-of-supply arrangements, cancellation, basis changes and special adjustments unless their separate current treatment has been established. A payments-basis supply over $225,000 also requires separate section 19D analysis; payments basis alone does not justify cash treatment. Mixed/private/exempt use requires an established credit allocation before any Box 11 amount is used. [GSTA ss 9, 19D, 20](https://www.legislation.govt.nz/act/public/1985/141/en/latest/); [IR375, pp 7 and 11–13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

**Quick reference table**  _(https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst)_

| Field | Value |
| --- | --- |
| Country | New Zealand |
| Standard rate | 15% (single rate -- no reduced rates) |
| Zero rate | 0% (exports, going concerns, certain land transactions, financial services election, international transport) |
| Exempt | Financial services, residential rental, donated goods by nonprofits |
| Return form | GST101A (GST Return) |
| Filing portal | myIR (myir.ird.govt.nz) |
| Authority | Inland Revenue Department (IRD / Te Tari Taake) |
| Currency | NZD only |
| Filing frequencies | Confirm monthly/2-monthly/6-monthly registration; see the statutory thresholds and boundary qualifications in Section 5 |
| Deadline | 28th of the month after the taxable period ends, except periods ending 31 March are due 7 May and periods ending 30 November are due 15 January; if the date falls on a weekend or public holiday, use the next working day |
| Registration threshold | Confirm registration/effective date and section 51 tests; exactly $60,000 and GST charged while unregistered require separate resolution |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later -- MUST be loaded** |
| Contributor | Open Accounting Skills Community |
| Validation date | Selected core checked 13 November 2026; tier 2/pending review |

**Key GST101A fields**

| Box | GST101A entry for the verified ordinary slice |
| --- | --- |
| 5 | GST-inclusive taxable sales, including established zero-rated sales; exclude exempt and non-supply receipts |
| 6 | The established zero-rated part already included in Box 5 |
| 7 | Box 5 minus Box 6, before applying the tax fraction |
| 8 | Box 7 × 3/23 |
| 9 | Separately established debit adjustments from the calculation sheet |
| 10 | Box 8 + Box 9 |
| 11 | Eligible GST-inclusive purchases for this period; exclude imported goods, exempt/zero-rated purchases and any unclaimable portion |
| 12 | Box 11 × 3/23 |
| 13 | Separately established credit adjustments from the calculation sheet |
| 14 | Box 12 + Box 13 |
| 15 | Difference between Boxes 10 and 14; record the amount and payment/refund indicator |

Use GST-inclusive amounts on **both** the invoice and payments bases. The basis changes recognition timing. It does not change the GST101A tax fraction. Convert a wholly standard-rated GST-exclusive amount to its inclusive amount by multiplying by 1.15 before entering Box 5 or 11. Keep the exclusive value and GST separately in the reconciliation. Exempt receipts are excluded from Box 5; zero-rated taxable receipts are included in both Boxes 5 and 6. Never extract 3/23 from zero-rated, exempt or unsubstantiated purchases. [GST101A, p 1](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/gst100---gst199/gst101a/gst101a-2023.pdf?modified=20230330222032); [IR375, pp 7 and 12–13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

For the working paper define a signed balance as Box 10 − Box 14: positive is payable, negative is a refund and zero means no balance. The paper form requires the absolute amount in Box 15 and the appropriate indicator. No balance does not remove the filing obligation. A GST103-series combined return has additional provisional-tax fields; use its actual issued form and the separate provisional-tax guide rather than treating GST101A as the complete filing. [IR375, pp 11–17 and 19](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).


**Conservative defaults**  _(NZ-specific values for the universal categories in vat-workflow-base Section 2)_

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | STOP classification; obtain actual supply evidence |
| Unknown GST status of a purchase | Not claimable (no input tax) |
| Unknown counterparty country | Unresolved; do not assume domestic |
| Unknown business-use proportion (vehicle, phone, home office) | 0% input tax |
| Unknown whether personal or business expense | Personal (no input tax) |
| Unknown non-resident supplier GST status | Assume not registered (no input tax claim) |
| Unknown whether transaction is in scope | Unresolved; obtain evidence |

**Red flag thresholds**  _(country slot values for the reviewer brief in vat-workflow-base Section 3)_

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | NZD 5,000 |
| HIGH tax-delta on a single conservative default | NZD 400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net GST position | NZD 10,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before calculation obtain the registration record and effective date, confirmed basis, balance date, exact return period and due date, complete sales and purchase records, taxable supply information, all relevant bank/cash/processor activity and reconciled prior-period allocations. Confirm any zero rating, exempt activity, private use and adjustments separately. A bank statement alone is a transaction-gathering input; it is not sufficient authority to populate the return. Missing status, basis or material supply evidence means stop the calculation and list what is missing. Do not request credentials or submit the return on the user's behalf.

For supplies from 1 April 2023 the general evidence requirement is **taxable supply information**, which can be held across invoices, contracts, accounting records and other documents. A document may still be called a tax invoice. The old universal '$50 tax invoice' rule must not be used. Confirm the current information requirements for the value and type of supply and keep the evidence before claiming. This update does not verify the full value-band table or every special credit. [IRD taxable supply information](https://www.ird.govt.nz/gst/tax-invoices-for-gst); [IR375, pp 2 and 8–10](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

### NZ-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation.

- **R-NZ-1 — Financial services election (s.20F)** — Trigger: client has elected to zero-rate financial services or asks about s.20F. Message: "The election to zero-rate financial services under s.20F of the GST Act requires complex calculations and specific conditions. This skill covers standard taxable and zero-rated supplies only. Please use a chartered accountant familiar with financial services GST."  _(s.20F)_
- **R-NZ-2 — GST groups** — Trigger: client is part of a GST group registration. Message: "GST group registrations require consolidated reporting and intra-group supply rules. Out of scope."
- **R-NZ-3 — Non-profit bodies with donated goods** — Trigger: client is a non-profit using the donated goods exemption. Message: "Non-profit bodies have special GST rules for donated goods and services. Out of scope."
- **R-NZ-4 — Complex change-of-use adjustments on high-value assets** — Trigger: client has a high-value mixed-use asset (e.g., holiday home used partly for Airbnb) requiring annual change-of-use adjustments under s.21–21H. Message: "Change-of-use adjustments for mixed-use assets with a value exceeding $5,000 require annual recalculation of the taxable-use proportion. This is too fact-sensitive for this skill. Please use a chartered accountant."  _(s.21–21H)_
- **R-NZ-5 — Compulsory zero-rating of land** — Trigger: client is selling or buying land between GST-registered persons. Message: "Land transactions between registered persons are subject to compulsory zero-rating under s.11(1)(mb). This requires specific contractual wording and a vendor/purchaser notification process. Please use a property lawyer and chartered accountant."  _(s.11(1)(mb))_
- **R-NZ-6 — Secondhand goods input tax credit (s.24)** — Trigger: client regularly buys secondhand goods from unregistered persons and claims input tax under s.24. Message: "The secondhand goods input tax credit under s.24 has specific documentation requirements and valuation rules. If this is a significant part of the business, please use a chartered accountant to confirm eligibility and amounts."  _(s.24)_
- **R-NZ-7 — GST on imported services (s.8(4B))** — Trigger: client is a non-profit or makes significant exempt supplies and receives services from non-residents. Message: "The reverse charge on imported services under s.8(4B) applies when the recipient cannot claim a full input tax credit. For fully taxable businesses, there is no reverse charge obligation (the input tax offsets the output tax). If your business makes exempt supplies, please use a chartered accountant."  _(s.8(4B))_
- **R-NZ-8 — Payments basis with large accruals** — Trigger: client uses payments basis but has significant unpaid invoices at period end that may distort the return. Message: "Under the payments basis, GST is accounted for when payment is made or received, not when invoiced. If you have large outstanding invoices at period end, ensure only paid amounts are included. If you are unsure, confirm your accounting basis with your accountant."

## Section 3 — Supplier pattern library (the lookup table)

Use these legacy patterns only to locate records and frame questions. A treatment in a table is conditional on current supporting evidence for the actual supply. Do not assign a GST rate, exemption or credit from a name or narration. Unverified items remain unclassified and must not enter return totals.

### 3.1 New Zealand banks (fees exempt — exclude)

**NZ banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ANZ, ANZ NEW ZEALAND, ANZ NZ | EXCLUDE for bank charges/fees | Financial service, exempt (s.14(a), s.3) |
| WESTPAC, WESTPAC NZ | EXCLUDE for bank charges/fees | Same |
| ASB, ASB BANK | EXCLUDE for bank charges/fees | Same |
| BNZ, BANK OF NEW ZEALAND | EXCLUDE for bank charges/fees | Same |
| KIWIBANK | EXCLUDE for bank charges/fees | Same |
| TSB BANK, HEARTLAND BANK, CO-OPERATIVE BANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, INT | EXCLUDE | Interest income/expense, exempt |
| MORTGAGE, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Government, ACC and local-authority payments

A public body or levy narration does not establish GST treatment. Identify the actual payment, date, supply and GST record. Do not exclude all government charges, ACC invoices or rates, and do not assume all consent fees are standard-rated. Inland Revenue's [special-supplies guidance](https://www.ird.govt.nz/gst/charging-gst/special-supplies) describes date-dependent legislative charges and separate rates rules. Full classifications and exceptions remain for verification.

| Pattern | Required check before any return allocation |
| --- | --- |
| IRD, INLAND REVENUE, TE TARI TAAKE | Confirm whether this is a tax remittance, refund, correction or another transaction; an actual tax remittance is not a purchase credit |
| ACC, ACCIDENT COMPENSATION | Obtain the actual invoice, GST component, credit eligibility and period; do not infer zero GST from the levy name |
| NZTA, WAKA KOTAHI, MINISTRY OF, DEPARTMENT OF | Identify the charge and applicable rules at its date; retain the GST evidence |
| COMPANIES OFFICE, NZBN | Obtain the fee record and GST treatment; do not decide from the registry name |
| COUNCIL, CITY COUNCIL, DISTRICT COUNCIL | Obtain the rates/consent/service invoice, taxable-use allocation and applicable special timing; do not apply a blanket rates exclusion |

Unresolved payments remain in the reconciliation with no computed credit until the evidence is established.


### 3.3 New Zealand utilities

**Utilities table**

| Pattern | Treatment | Field | Notes |
| --- | --- | --- | --- |
| MERCURY ENERGY, GENESIS ENERGY, CONTACT ENERGY | Domestic 15% | 11/12 | Electricity — overhead |
| MERIDIAN ENERGY, TRUSTPOWER, FLICK ELECTRIC | Domestic 15% | 11/12 | Electricity — overhead |
| NOVA ENERGY, ELECTRIC KIWI, POWERSHOP | Domestic 15% | 11/12 | Electricity — overhead |
| SPARK, SPARK NZ | Domestic 15% | 11/12 | Telecoms — overhead |
| VODAFONE NZ, VODAFONE NEW ZEALAND | Domestic 15% | 11/12 | Telecoms — overhead |
| 2DEGREES, TWO DEGREES | Domestic 15% | 11/12 | Telecoms — overhead |
| SKINNY MOBILE | Domestic 15% | 11/12 | Telecoms — overhead |
| CHORUS, ENABLE, ULTRAFAST FIBRE | Domestic 15% | 11/12 | Fibre broadband — overhead |
| WATERCARE, WELLINGTON WATER | Domestic 15% | 11/12 | Water — overhead |

### 3.4 Insurance

An insurer's name does not establish an exemption. General/fire insurance and life insurance do not have the same GST treatment. Obtain the policy type, premium/GST record, business use and any special receipt or adjustment rules before allocating a return amount. See [IR375, p 41](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047) and [IRD special supplies](https://www.ird.govt.nz/gst/charging-gst/special-supplies).

| Pattern | Required check |
| --- | --- |
| IAG, STATE INSURANCE, AMI, NZI, AA INSURANCE, TOWER | Establish the actual cover and GST treatment; no blanket exclusion |
| SOUTHERN CROSS, PARTNERS LIFE, AIA NZ | Identify the actual health/life/other policy rather than treating all products alike |
| INSURANCE, INS PREMIUM | Obtain the policy and GST evidence before classification |


### 3.5 Post and logistics

**Post and logistics table**

| Pattern | Treatment | Field | Notes |
| --- | --- | --- | --- |
| NZ POST, NEW ZEALAND POST | Domestic 15% | 11/12 | NZ Post is taxable (unlike some EU postal services) |
| COURIER POST, PACE | Domestic 15% | 11/12 | NZ Post courier service |
| FASTWAY, ARAMEX NZ, TOLL, MAINFREIGHT | Domestic 15% | 11/12 | Courier/freight services |
| DHL NZ, FEDEX NZ, UPS NZ | Domestic 15% | 11/12 | Express courier |

### 3.6 Transport

**Transport table**

| Pattern | Treatment | Field | Notes |
| --- | --- | --- | --- |
| AIR NEW ZEALAND, AIR NZ (domestic) | Domestic 15% | 11/12 | Domestic flights taxable |
| AIR NEW ZEALAND (international) | Zero-rated | 6 | International transport — s.11A(1)(a) |
| JETSTAR NZ (domestic) | Domestic 15% | 11/12 | Domestic flights taxable |
| AT HOP, METLINK, METRO CANTERBURY | Domestic 15% | 11/12 | Public transport — taxable in NZ (not exempt like some countries) |
| UBER NZ | Domestic 15% | 11/12 | Ride-sharing — GST registered |
| OLA NZ | Domestic 15% | 11/12 | Ride-sharing |
| INTERISLANDER, BLUEBRIDGE | Domestic 15% (inter-island) | 11/12 | Cook Strait ferry — domestic |
| RENTAL CAR, BUDGET NZ, HERTZ NZ, AVIS NZ | Domestic 15% | 11/12 | Car rental |

### 3.7 Food retail (blocked unless hospitality business)

**Food retail table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| COUNTDOWN, WOOLWORTHS NZ | Default BLOCK input tax | Personal provisioning. Zero-rated basic food + 15% non-food mix. Only deductible if hospitality business. |
| PAK'N SAVE, PAK N SAVE, PAKNSAVE | Default BLOCK | Same |
| NEW WORLD | Default BLOCK | Same |
| FOUR SQUARE | Default BLOCK | Same |
| FARRO, MOORE WILSONS | Default BLOCK | Same (though Moore Wilsons is popular with hospitality) |
| RESTAURANTS, CAFES, BARS (any named) | Default BLOCK | Entertainment — see Section 5.11 |

### 3.8 SaaS — non-resident suppliers (reverse charge or GST-registered)

- **Reverse charge explanation** — In New Zealand, a reverse charge on imported services applies only when the recipient cannot claim a full input tax credit (s.8(4B)). For fully taxable businesses, there is NO reverse charge obligation — the supplier either charges NZ GST (if registered under the non-resident rules) or does not, and the recipient cannot claim input tax on a supply where no GST was charged. Many large non-resident digital suppliers are now GST-registered in NZ.  _(s.8(4B))_

**SaaS non-resident table**

| Pattern | GST status | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | GST-registered in NZ | If NZ GST on invoice: domestic 15%, Boxes 11/12 | Check invoice — Google NZ entity charges GST |
| MICROSOFT (365, Azure) | GST-registered in NZ | If NZ GST on invoice: domestic 15%, Boxes 11/12 | Same |
| ADOBE | GST-registered in NZ | If NZ GST on invoice: domestic 15%, Boxes 11/12 | Same |
| META, FACEBOOK ADS | GST-registered in NZ | If NZ GST on invoice: domestic 15%, Boxes 11/12 | Same |
| SPOTIFY | GST-registered in NZ | If NZ GST on invoice: domestic 15%, Boxes 11/12 | Same |
| NOTION | Not NZ-registered (US) | No GST charged, no input tax claim | Cost is a non-deductible GST expense |
| ANTHROPIC, CLAUDE | Not NZ-registered (US) | No GST charged, no input tax claim | Same |
| OPENAI, CHATGPT | Not NZ-registered (US) | No GST charged, no input tax claim | Same |
| GITHUB | Check invoice | If NZ GST charged: domestic 15%; if not: no claim |  |
| FIGMA | Not NZ-registered (US) | No GST charged, no input tax claim |  |
| CANVA | GST-registered in NZ (AU entity) | If NZ GST on invoice: domestic 15%, Boxes 11/12 | Canva AU registered for NZ GST |
| SLACK, ATLASSIAN, ZOOM, DROPBOX | Check invoice | If NZ GST charged: 15%; if not: no claim | Some have registered, some not |

### 3.9 New Zealand SaaS / domestic suppliers

**NZ SaaS table**

| Pattern | Treatment | Field | Notes |
| --- | --- | --- | --- |
| XERO | Domestic 15% | 11/12 | NZ-headquartered accounting software |
| STRIPE NZ, STRIPE PAYMENTS NZ | Check invoice |  | Transaction fees may be exempt; subscription taxable |
| VEND (LIGHTSPEED) | Domestic 15% | 11/12 | POS software |
| TIMELY, UNLEASHED | Domestic 15% | 11/12 | NZ SaaS |
| PUSHPAY | Domestic 15% | 11/12 | NZ SaaS |
| TRADEME, TRADE ME | Domestic 15% | 11/12 | NZ marketplace fees |

### 3.10 Payment processors

**Payment processors table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| WINDCAVE, PAYMARK, DPS | EXCLUDE for transaction fees | Payment gateway — exempt financial service |
| EFTPOS NZ | EXCLUDE | Card processing fees — exempt |
| AFTERPAY, LAYBUY | Check invoice | Merchant fees may be exempt (financial service) |

### 3.11 Professional services (NZ)

**Professional services table**

| Pattern | Treatment | Field | Notes |
| --- | --- | --- | --- |
| CHARTERED ACCOUNTANT, CA, CPA | Candidate standard-rated purchase | 11/12 only if eligible | Confirm actual service, GST, taxable use and period |
| LAWYER, SOLICITOR, BARRISTER | Domestic 15% | 11/12 | Claimable if business purpose |
| SURVEYOR, VALUER, ENGINEER | Domestic 15% | 11/12 | Claimable if business purpose |
| COMPANIES OFFICE | Unresolved pending fee record |  | Establish actual GST, eligibility and timing |

### 3.12 Payroll and statutory (exclude entirely)

**Payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, PAY | EXCLUDE | Wages — outside GST scope |
| PAYE, IRD PAYE | EXCLUDE | PAYE tax remittance |
| KIWISAVER | EXCLUDE | Superannuation contribution |
| ACC LEVY | Unresolved pending invoice | Establish actual GST, eligibility and timing; no blanket exclusion |
| STUDENT LOAN | EXCLUDE | Loan repayment |

### 3.13 Property and rent

**Property and rent table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RENT (commercial) | Domestic 15% | Commercial lease — GST on rent, input tax claimable |
| RENT (residential) | EXCLUDE | Residential rental exempt (s.14(c)) |
| BODY CORPORATE | EXCLUDE if residential | Residential body corporate exempt |
| RATES, COUNCIL RATES | Unresolved pending rates record | Establish taxable use, GST and special timing; no blanket exclusion |

### 3.14 Internal transfers and exclusions

**Internal transfers table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER, TFR, OWN ACCOUNT | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Dividend, out of scope |
| LOAN REPAYMENT | EXCLUDE | Principal, out of scope |
| ATM, CASH WITHDRAWAL | TIER 2 — ask | Default exclude; ask what cash was for |
| DRAWINGS, OWNER DRAW | EXCLUDE | Owner withdrawal |

### 3.15 Specific NZ patterns

**Specific NZ patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BUNNINGS NZ | Domestic 15% | Hardware/tools — claimable if business purpose |
| THE WAREHOUSE | Default BLOCK | Likely personal — mixed retail |
| MITRE 10 | Domestic 15% if trade purchase | Hardware — claimable if business tools/materials |
| NOEL LEEMING, PB TECH, MIGHTY APE | Domestic 15% if business | Electronics — claimable if business asset |
| Z ENERGY, BP NZ, MOBIL NZ, CALTEX | Domestic 15% | Fuel — claimable to extent of business use |
| AA NZ (membership) | Domestic 15% | Automobile Association — claimable if business |

## Section 4 — Worked examples

### Verified core worked checks

These are synthetic, conditional examples for the selected core. They check arithmetic and box placement after classification, eligibility, timing and records have been established. They do not test a live return or grant filing authority.

#### Core case 1: Ordinary payments-basis return

Confirmed ordinary standard-rated customer receipts are $23,000 and eligible supplier payments are $8,050, both GST-inclusive. There are no zero-rated supplies or adjustments. The result is $1,950 payable.

```oa-check
name: nz-gst-core-payments-standard
tolerance: 0
inputs:
  sales: 23000
  eligible_purchases: 8050
  debit_adjustments: 0
  credit_adjustments: 0
  zero_sales: 0
steps:
  box5: sales
  box6: zero_sales
  box7: box5 - box6
  box8: box7 * 3 / 23
  box9: debit_adjustments
  box10: box8 + box9
  box11: eligible_purchases
  box12: box11 * 3 / 23
  box13: credit_adjustments
  box14: box12 + box13
  signed_balance: box10 - box14
  box15: abs(signed_balance)
expected:
  box5: 23000
  box6: 0
  box7: 23000
  box8: 3000
  box9: 0
  box10: 3000
  box11: 8050
  box12: 1050
  box13: 0
  box14: 1050
  signed_balance: 1950
  box15: 1950
```

#### Core case 2: Invoice basis still uses inclusive GST101A amounts

The ordinary invoice-basis sales register has $20,000 exclusive standard-rated sales plus $5,000 separately established zero-rated supplies. Eligible purchases are $7,000 exclusive, all standard-rated. Convert the standard-rated values to inclusive amounts before using the form. Box 5 is $28,000, Box 11 is $8,050 and GST payable is $1,950.

```oa-check
name: nz-gst-core-invoice-exclusive-conversion
tolerance: 0
inputs:
  sales_exclusive: 20000
  zero_sales: 5000
  purchases_exclusive: 7000
steps:
  box5: sales_exclusive * 1.15 + zero_sales
  box6: zero_sales
  box7: box5 - box6
  box8: box7 * 3 / 23
  box10: box8
  box11: purchases_exclusive * 1.15
  box12: box11 * 3 / 23
  box14: box12
  signed_balance: box10 - box14
expected:
  box5: 28000
  box6: 5000
  box7: 23000
  box8: 3000
  box10: 3000
  box11: 8050
  box12: 1050
  box14: 1050
  signed_balance: 1950
```

#### Core case 3: Debit and credit adjustments use separate boxes

Ordinary inclusive sales are $23,000 and eligible purchases $8,050. A separately verified adjustment schedule supplies a $150 debit and a $60 credit for this period. This example checks their placement and arithmetic only; it does not establish entitlement to either adjustment. Box 9 is $150, Box 13 is $60 and the balance is $2,040 payable.

```oa-check
name: nz-gst-core-supplied-adjustments
tolerance: 0
inputs:
  sales: 23000
  purchases: 8050
  debit: 150
  credit: 60
steps:
  box8: sales * 3 / 23
  box9: debit
  box10: box8 + box9
  box12: purchases * 3 / 23
  box13: credit
  box14: box12 + box13
  signed_balance: box10 - box14
expected:
  box8: 3000
  box9: 150
  box10: 3150
  box12: 1050
  box13: 60
  box14: 1110
  signed_balance: 2040
```

#### Core case 4: Established zero-rated supplies and a refund

The business has $50,000 of supplies whose zero-rating conditions have already been independently established and $17,250 of eligible inclusive purchases. The sales appear in Boxes 5 and 6; ordinary output tax is zero. The working-paper balance is −$2,250. Box 15 shows $2,250 with the refund indicator.

```oa-check
name: nz-gst-core-zero-rated-refund
tolerance: 0
inputs:
  zero_sales: 50000
  purchases: 17250
steps:
  box5: zero_sales
  box6: zero_sales
  box7: box5 - box6
  box8: box7 * 3 / 23
  box10: box8
  box12: purchases * 3 / 23
  box14: box12
  signed_balance: box10 - box14
  box15: abs(signed_balance)
expected:
  box5: 50000
  box6: 50000
  box7: 0
  box8: 0
  box10: 0
  box12: 2250
  box14: 2250
  signed_balance: -2250
  box15: 2250
```

#### Core case 5: Ordinary part payment before an invoice

For a fixed-price ordinary sale of $1,150 inclusive, $115 is received before any invoice and before period end. The balance is received later. There is no refundable deposit or special timing rule. Invoice basis recognises the full $1,150 and $150 GST at the earlier payment; payments basis recognises $115 and $15 GST in this period. Keep the later allocations so the sale is not counted twice.

```oa-check
name: nz-gst-core-payment-before-invoice
tolerance: 0
inputs:
  full_price: 1150
  part_payment: 115
steps:
  invoice_box5: full_price
  invoice_box8: invoice_box5 * 3 / 23
  payments_box5: part_payment
  payments_box8: payments_box5 * 3 / 23
  later_payments_receipt: full_price - part_payment
expected:
  invoice_box5: 1150
  invoice_box8: 150
  payments_box5: 115
  payments_box8: 15
  later_payments_receipt: 1035
```

#### Core case 6: Hybrid uses invoice sales and paid purchases

An ordinary $2,300 inclusive sale is invoiced and unpaid. An eligible $1,150 inclusive purchase is invoiced, with only $230 paid in the period. The confirmed hybrid basis recognises all $2,300 of sales but only $230 of purchases: output tax $300, input tax $30 and $270 payable.

```oa-check
name: nz-gst-core-hybrid-direction
tolerance: 0
inputs:
  invoiced_sales: 2300
  purchase_invoice: 1150
  purchase_payment: 230
steps:
  box5: invoiced_sales
  box8: box5 * 3 / 23
  box11: purchase_payment
  box12: box11 * 3 / 23
  signed_balance: box8 - box12
  unpaid_purchase: purchase_invoice - purchase_payment
expected:
  box5: 2300
  box8: 300
  box11: 230
  box12: 30
  signed_balance: 270
  unpaid_purchase: 920
```

#### Core case 7: Exempt and non-supply receipts stay out of Box 5

Confirmed ordinary inclusive taxable receipts are $11,500, established zero-rated sales $2,000, exempt receipts $500 and a non-supply loan receipt $1,000. Reconcile all $15,000 of receipts, but Box 5 is $13,500 and Box 6 $2,000. Output tax is $1,500. Classification is an input to this example, not a conclusion from a bank narration.

```oa-check
name: nz-gst-core-exclude-exempt-nonsupply
tolerance: 0
inputs:
  standard: 11500
  zero: 2000
  exempt: 500
  loan: 1000
steps:
  reconciled_receipts: standard + zero + exempt + loan
  box5: standard + zero
  box6: zero
  box7: box5 - box6
  box8: box7 * 3 / 23
  excluded_receipts: exempt + loan
expected:
  reconciled_receipts: 15000
  box5: 13500
  box6: 2000
  box7: 11500
  box8: 1500
  excluded_receipts: 1500
```

#### Core case 8: Invoice timing avoids counting a settled invoice twice

A $1,150 inclusive sale was invoiced and returned in the previous invoice-basis period, then paid in this period. A new $2,300 inclusive ordinary sale is invoiced in this period and remains unpaid. With no special rule or adjustment, this period has Box 5 of $2,300 and output tax $300. The old invoice receipt clears the debtor and is not another sale. In a counterfactual comparison where payments basis had applied from the outset, the established $1,150 current receipt would instead give $150 output tax; the unpaid new sale is deferred. This is not a change-of-basis calculation.

```oa-check
name: nz-gst-core-invoice-prior-period-receipt
tolerance: 0
inputs:
  old_invoice_receipt: 1150
  new_unpaid_invoice: 2300
steps:
  invoice_box5: new_unpaid_invoice
  invoice_box8: invoice_box5 * 3 / 23
  payments_box5: old_invoice_receipt
  payments_box8: payments_box5 * 3 / 23
expected:
  invoice_box5: 2300
  invoice_box8: 300
  payments_box5: 1150
  payments_box8: 150
```

#### Core case 9: A zero balance still requires filing

Eligible ordinary inclusive sales and purchases are each $2,300, with no adjustments. Output and input tax are each $300, giving a zero balance. The activity and return still need to be reported. An actual no-activity return also needs filing; unresolved records must never be substituted with zeros.

```oa-check
name: nz-gst-core-zero-balance-activity
tolerance: 0
inputs:
  sales: 2300
  purchases: 2300
steps:
  box8: sales * 3 / 23
  box12: purchases * 3 / 23
  signed_balance: box8 - box12
  gross_activity: sales + purchases
expected:
  box8: 300
  box12: 300
  signed_balance: 0
  gross_activity: 4600
```


These are six fully worked classifications drawn from a hypothetical bank statement of an Auckland-based self-employed software consultant.

### Example 1 — Non-resident SaaS, no NZ GST (Notion)

**Input line:**
`2026-04-03 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; NZD 26.18`

**Reasoning:**
Notion Labs Inc is a US entity not registered for NZ GST (Section 3.8). No GST on the invoice. In NZ, there is no reverse charge obligation for fully taxable businesses (s.8(4B) only applies to recipients who cannot claim full input tax). The NZD 26.18 is a business expense for income tax purposes but generates no GST input tax claim. Exclude this no-GST purchase from the ordinary Box 11 tax-fraction base; record the expense separately. Its income-tax treatment and any imported-service rule require their own analysis.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-03 | NOTION LABS INC | -26.18 | -26.18 | 0 | — | No ordinary return box | N | — | — |

### Example 2 — Non-resident SaaS, NZ GST charged (Google Ads)

**Input line:**
`2026-04-10 ; GOOGLE NEW ZEALAND LTD ; DEBIT ; Google Ads April 2026 ; -920.00 ; NZD`

**Reasoning:**
Google is GST-registered in NZ and charges 15% GST. The NZD 920.00 is GST-inclusive. GST = 920 * 3/23 = 120.00. Net = 800.00. Full input tax claim in Box 12.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-10 | GOOGLE NZ | -920.00 | -800.00 | -120.00 | 15% | 11/12 | N | — | — |

### Example 3 — Entertainment, 50% deduction

**Input line:**
`2026-04-15 ; THE GROVE RESTAURANT AUCKLAND ; DEBIT ; Client dinner ; -350.00 ; NZD`

**Reasoning:**
Restaurant transaction. In NZ, entertainment expenses are subject to the 50% deduction limitation under the Income Tax Act 2007, s.DD 1. For GST purposes, the input tax claim follows the entertainment limitation — only 50% of the GST is claimable (s.21(1) read with ITA s.DD 1). GST on full amount = 350 * 3/23 = 45.65. Claimable input tax = 22.83 (50%). Conservative default: block entirely as likely personal. If confirmed as business, 50% is claimable.

**Output table**  _("Entertainment: blocked (conservative). If business, 50% claimable.")_

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-15 | THE GROVE RESTAURANT | -350.00 | -350.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked (conservative). If business, 50% claimable." |

### Example 4 — Capital asset (business equipment)

**Input line:**
`2026-04-18 ; PB TECH AUCKLAND ; DEBIT ; MacBook Pro 16 ; -4,599.00 ; NZD`

**Reasoning:**
NZD 4,599 GST-inclusive. GST = 4,599 * 3/23 = 599.87. Net = 3,999.13. This is a business asset. In NZ there is no separate capital goods line on the GST101A — ordinary purchase tax is calculated in Box 12. However, assets over $5,000 (GST-exclusive) are subject to change-of-use adjustment rules (s.21–21H). At $3,999.13 net, this is below the $5,000 threshold. Full input tax claim.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-18 | PB TECH | -4,599.00 | -3,999.13 | -599.87 | 15% | 11/12 | N | — | — |

### Example 5 — Export sale (zero-rated)

**Input line:**
`2026-04-22 ; ACME PTY LTD SYDNEY ; CREDIT ; Invoice NZ-2026-018 IT consulting March ; +8,500.00 ; NZD`

**Reasoning:**
Incoming NZD 8,500 from an Australian company. Client provides IT consulting services to a non-resident outside NZ. Under s.11A(1)(k), services supplied to a non-resident who is outside NZ at the time of supply are zero-rated (subject to conditions — the service must not be performed for a person in NZ or relate to NZ land/goods). Include in field 5 (total sales) and field 6 (zero-rated). No output tax in Box 8.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-22 | ACME PTY LTD | +8,500.00 | +8,500.00 | 0 | 0% | 5 + 6 | Y | Q2 (HIGH) | "Verify non-resident and outside-NZ conditions for zero-rating" |

### Example 6 — Vehicle costs, no logbook

**Input line:**
`2026-04-28 ; Z ENERGY PARNELL ; DEBIT ; Fuel ; -102.00 ; NZD`

**Reasoning:**
Fuel purchase. In NZ, motor vehicle expenses are claimable to the extent of business use. IRD accepts a logbook kept for 3 consecutive months as evidence of the business-use percentage, which then applies for 3 years. Without a logbook, the conservative default is 0% input tax claim. If a logbook exists showing, say, 70% business use, then 70% of the GST is claimable.

**Output table**  _("Vehicle fuel: 0% (no logbook). Provide 3-month logbook for partial claim.")_

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-28 | Z ENERGY | -102.00 | -102.00 | 0 | — | — | Y | Q3 | "Vehicle fuel: 0% (no logbook). Provide 3-month logbook for partial claim." |

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 15% (GST Act s.8(1))

- **Standard rate** — 15% percent (The only positive GST rate in New Zealand. Standard-rated taxable supplies are taxed at 15%; separately established zero-rated supplies have a 0% rate. There are no reduced rates. Sales → field 5 (total), output tax → Box 8. Eligible purchases → Box 11, ordinary input tax → Box 12.)  _(GST Act s.8(1))_

### 5.2 Zero-rated supplies (GST Act s.11, s.11A, s.11AB)

- **Zero-rated supplies** — Exports of goods (s.11(1)(a)): requires Customs export entry. Services to non-residents (s.11A(1)(k)): conditions — recipient must be non-resident, outside NZ at time of supply, service must not relate to NZ land or be performed for a person in NZ. Going concerns (s.11(1)(mb)): supply of a business as a going concern to a registered person. Land between registered persons (s.11(1)(mb)): compulsory zero-rating — R-NZ-5 fires. International transport (s.11A(1)(a)–(c)). Report in field 5 (total) and field 6 (zero-rated).  _(GST Act s.11, s.11A, s.11AB)_

### 5.3 Exempt supplies (GST Act s.14)

- **Exempt supplies** — Financial services (s.14(a), s.3): lending, currency exchange, life insurance, equity securities — exempt. Residential rental (s.14(c)): rental of a dwelling — exempt. Donated goods/services by nonprofits (s.14(ca)). Penalties, fines, and default interest (s.14). Exempt supplies do NOT go on the return. No output tax, no input tax on related costs.  _(GST Act s.14)_

### 5.4 Purchase evidence and credits

For supplies from 1 April 2023 the general evidence requirement is **taxable supply information**, which can be held across invoices, contracts, accounting records and other documents. A document may still be called a tax invoice. The old universal '$50 tax invoice' rule must not be used. Confirm the current information requirements for the value and type of supply and keep the evidence before claiming. This update does not verify the full value-band table or every special credit. [IRD taxable supply information](https://www.ird.govt.nz/gst/tax-invoices-for-gst); [IR375, pp 2 and 8–10](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

Use only the separately established credit for taxable business use. Exclude private, exempt and no-GST expenditure from the ordinary Box 11 base; special credits, imported supplies and mixed-use adjustments need separate current evidence.

### 5.5 No reverse charge for fully taxable businesses

- **No reverse charge for fully taxable businesses** — Unlike the EU, NZ does not require a fully taxable business to self-assess GST on imported services. The reverse charge under s.8(4B) only applies when the recipient makes exempt supplies and therefore cannot claim full input tax. For a typical self-employed consultant making only taxable supplies, no reverse charge applies — either the non-resident supplier charges NZ GST (if registered) or no NZ GST applies and there is no input tax claim.  _(s.8(4B))_

### 5.6 Non-resident supplier registration

- **Non-resident supplier registration** — Since October 2016, non-resident suppliers of remote services (digital services, streaming, SaaS) to NZ consumers must register for NZ GST if their supplies exceed $60,000. Many large suppliers (Google, Microsoft, Adobe, Meta, Spotify, Netflix, Canva) are now registered and charge NZ GST. Check the invoice: if NZ GST is on the invoice, treat as a domestic supply with input tax. If no NZ GST, no input tax claim.

### 5.7 Registration, accounting basis and filing

### Registration check

Confirm the registration record and effective date. An unregistered business may already be required to register. Inland Revenue's public registration page says taxable turnover of at least $60,000 in the past or expected next 12 months, or adding GST to prices, requires registration. Section 51(1) uses a month-end past-12-month test that **exceeds** $60,000 and a month-start reasonable expectation that the next 12 months **will exceed** $60,000, with statutory exceptions. Values are GST-exclusive under section 51(6). At exactly $60,000, or where an exception or charging GST without registration is involved, obtain Inland Revenue's registration determination rather than deciding from this guide. A person liable under section 51(1) must apply within 21 days under section 51(2). Voluntary registration under section 51(3) is a separate application for a taxable activity or intended taxable activity. Do not infer registration or an automatic right to cease filing from turnover. [Registering for GST](https://www.ird.govt.nz/registering-for-gst); [GSTA s 51](https://www.legislation.govt.nz/act/public/1985/141/en/latest/).

### Confirmed accounting basis and timing

| Basis | Ordinary treatment after all scope and record checks |
| --- | --- |
| Payments | Recognise customer receipts and supplier payments in the period paid. Section 19A permits an application where either the past-12-month taxable-supply value or the relevant expected value is no more than $2 million; special approvals and directions also exist. Confirm the registered basis and eligibility, including at exactly $2 million. |
| Invoice | Apply the ordinary section 9(1) time of supply: the earlier invoice or any payment. A partial pre-invoice payment for an ordinary fixed-price sale brings in the full sale price. Include qualifying supplier invoices or earlier payments with the required records, even if not fully paid. |
| Hybrid | Invoice treatment for sales and payments treatment for purchases. The reverse combination is not the hybrid method. |

Unknown basis means stop and obtain the registration record. A bank statement alone cannot establish an invoice-basis return; obtain the sales/purchase registers, opening and closing unpaid invoices, earlier receipts/payments and prior-period allocations to prevent duplication. Even on payments basis, reconcile all relevant accounts, cash and payment processors to gross sales and costs; a net settlement is not the sale price. The special rules excluded above can override ordinary timing. [GSTA ss 9, 19, 19A, 19D and 20](https://www.legislation.govt.nz/act/public/1985/141/en/latest/); [IRD accounting basis](https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use); [IR375, pp 6–7](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

### Taxable periods, filing and payment

Confirm the actual period and due date shown in myIR. Ordinary monthly filing is available by choice and required if the past or expected 12-month supply value exceeds $24 million under section 15. Two-monthly is the ordinary default. Section 15 allows an application for 6-monthly periods where the applicable 12-month taxable-supply value is no more than $500,000 and is not likely to be more than $500,000. Inland Revenue's summary uses 'under $500,000'; at exactly $500,000 confirm eligibility and approval with Inland Revenue. Do not change periods or basis before the change is confirmed.

For a 31 March balance date, the ordinary aligned 2-monthly periods end in May, July, September, November, January and March; 6-monthly periods end in September and March. Use the registered dates, not the span of the supplied bank statement. Alternative end dates, transitions and other balance dates require their actual approved periods. [GSTA ss 15–15ED](https://www.legislation.govt.nz/act/public/1985/141/en/latest/); [IRD accounting basis and filing frequency](https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use); [IR375, p 6](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

File for every taxable period, including a genuine nil return. Filing and payment are ordinarily due on the 28th of the following month, except a 31 March period ends with a 7 May due date and a 30 November period with a 15 January due date in the next year. If that date is a weekend or public holiday use the next working day. Confirm the applicable holiday calendar and myIR date. Ordinary GST filing has no extension simply because an income-tax agent extension exists. Special statutory variations remain outside this ordinary slice. [GSTA ss 16 and 23](https://www.legislation.govt.nz/act/public/1985/141/en/latest/); [Filing GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst); [IR375, pp 6 and 19](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).


### 5.8 Change-of-use adjustments (s.21–21H)

- **Change-of-use adjustments** — When an asset or expense changes its proportion of taxable use, an adjustment may be required. For assets under $5,000 (GST-exclusive), no adjustment is needed. For assets $5,000–$10,000, a one-off adjustment at first non-taxable use. For assets over $10,000, annual adjustments for up to 10 years (land: 10 years; other: useful life or 5 years). Report adjustments in Box 9 (debit) or Box 13 (credit). If complex → R-NZ-4 fires.  _(s.21–21H)_

### 5.9 Secondhand goods (s.24(5))

- **Secondhand goods** — A registered person who purchases goods from an unregistered seller can claim input tax based on the purchase price (not exceeding the open market value). Must maintain records: name/address of seller, date, description, and price. No tax invoice required from seller (since they are not registered). The separately established credit belongs in Box 13, not the ordinary purchase tax-fraction base.  _(s.24(5))_

### 5.10 Motor vehicles

- **Motor vehicles** — No blanket block on motor vehicles in NZ (unlike Malta). ITCs are claimable to the extent of business use. IRD expects a logbook: keep for a 3-month representative period, then apply the resulting percentage for 3 years. FBT (fringe benefit tax) applies if a company provides a vehicle to an employee for private use — but FBT is outside GST scope.

### 5.11 Entertainment — 50% limitation

- **Entertainment 50% limitation** — GST Act s.21(1) read with Income Tax Act 2007 subpart DD. Entertainment expenses (meals, functions, corporate hospitality) are subject to a 50% limitation. The GST input tax claim is limited to 50% of the GST component. This applies to: meals and drinks, corporate boxes, holiday accommodation for employees, entertainment allowances. Does NOT apply to: light refreshments at business meetings, meals while traveling on business overnight, conferences/seminars with incidental catering.  _(GST Act s.21(1); Income Tax Act 2007 subpart DD)_

### 5.12 Goods and services purchased from non-residents

- **Goods and services purchased from non-residents** — If the non-resident supplier is GST-registered in NZ and charges GST: treat as domestic purchase, claim input tax. If not registered and no GST charged: no input tax claim (for fully taxable businesses). The cost is still deductible for income tax. If the recipient makes exempt supplies: reverse charge under s.8(4B) may apply — R-NZ-7 fires.  _(s.8(4B))_

### 5.13 Bad debts (s.26)

- **Bad debts** — If a registrant has accounted for GST on a sale (invoice basis) and the debt becomes bad, an adjustment is made in Box 13 (credit adjustment for tax previously returned). The adjustment is 3/23 of the bad debt written off. If the debt is later recovered, a reverse adjustment is required.  _(s.26)_

## Section 6 — Unresolved transactions and special treatments

These patterns generate questions only. Keep their amounts in the unresolved reconciliation and stop a filing-ready result until every material item has a supported classification, period and credit allocation.

| Pattern | Evidence still needed |
| --- | --- |
| Vehicle costs | Actual supply/GST record, taxable use and applicable vehicle/adjustment rules |
| Entertainment | Business/private purpose, actual GST and the applicable restriction, timing and adjustment rules; a restaurant name does not prove a percentage |
| Non-resident SaaS | Supplier treatment, actual NZ GST and applicable imported-service rules |
| Round-number transfers or owner/private names | Whether this is a sale, loan, capital contribution, drawing, wages or another movement |
| Overseas receipts | Actual supply, parties, place/timing and every zero-rating condition; an overseas bank is not proof |
| Large purchases | Actual GST, credit eligibility, capital/mixed-use facts and adjustment requirements |
| Phone, internet and home office | Taxable/private/exempt allocation with its evidence |
| Payments to individuals | Actual goods/services, employment/contractor/private character and GST evidence |
| Cash withdrawals | Cash-use records and any separately evidenced supplies; reconcile movements without inventing purchases |
| Rent | Commercial/residential/other nature, supplier GST, taxable use and timing |
| Trade Me or other marketplace | Gross underlying sales, fees, parties and actual marketplace rules; do not classify the net payout automatically |
| Airbnb | Marketplace/accommodation rules, actual supply chain, taxable use and adjustments; separate analysis is required |
| Secondhand goods | Actual seller, acquisition, use, statutory credit conditions, records and valuation; separate analysis is required |
| Foreign currency | Applicable NZD conversion method/date/rate and any special supply or financial-service rule |


## Section 7 -- GST101A working paper

Record registration, effective date, basis, period, due date, preparer and source references before figures. Use the Box 5–15 mapping in Section 1/5; do not renumber fields for a spreadsheet.

1. Reconcile all receipts to taxable, zero-rated, exempt, non-supply and unresolved items, using the confirmed timing basis. Box 5 includes only taxable receipts/sales recognised in this period, with GST included; Box 6 is its zero-rated subset.
2. Reconcile all costs to eligible standard-rated purchases, separately established adjustments and excluded/unresolved amounts. Box 11 is the ordinary GST-inclusive credit base after the established eligibility allocation. Keep imported goods and other special credits out of this base.
3. Compute Boxes 7, 8, 10, 12 and 14 from the published form equations. Boxes 9 and 13 require a separate adjustment schedule with legal basis, evidence, period and amount. An example using supplied adjustment amounts verifies only the field mapping.
4. Retain signed balance = Box 10 − Box 14 in the working paper. Enter its absolute value and payment/refund indicator in Box 15. A zero balance still requires filing; a net zero from offsetting activity does not mean no transactions.
5. Reconcile invoice and payments allocations to prior returns. Review exceptions, duplicate payments, outstanding invoices and all unresolved amounts before calling the return complete. Use software calculations and cross-check totals against the form; do not copy a formula that changes 3/23 to 15% merely because the basis is invoice.

This is a working-paper specification. No spreadsheet file or live myIR filing was created or tested by this update.


## Section 8 — New Zealand bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these NZ-specific patterns.

**ANZ NZ export format.** CSV download from ANZ Internet Banking. Columns: Date (DD/MM/YYYY), Transaction Details, Amount, Balance. The Amount column uses negative for debits. Transaction Details combines type and payee (e.g., "Visa Purchase - PB Tech Auckland", "Direct Debit - Spark NZ").

**Westpac NZ export format.** CSV from Westpac One. Columns: Date, Amount, Other Party, Description, Reference, Particulars, Analysis Code. The "Other Party" field contains the counterparty name. "Particulars", "Reference", and "Description" are the three freeform fields from NZ bank payment references.

**ASB export format.** CSV from ASB FastNet Classic. Columns: Date, Unique Id, Tran Type, Cheque Number, Payee, Memo, Amount. Date format: YYYY-MM-DD.

**BNZ export format.** CSV from BNZ Online. Columns: Date, Amount, Payee, Particulars, Code, Reference, Tran Type, This Party Account. Date format: DD/MM/YYYY.

**Kiwibank export format.** CSV from Kiwibank Internet Banking. Columns: Date, Description, Amount, Balance. Simple format.

**Common NZ bank statement patterns**

| Term | Meaning |
| --- | --- |
| Visa Purchase, EFTPOS | Card purchase (debit) |
| Direct Debit, D/D | Pre-authorized direct debit |
| Automatic Payment, A/P | Scheduled automatic payment |
| Direct Credit, D/C | Incoming direct credit |
| Transfer, TFR | Internal transfer |
| ATM W/D | Cash withdrawal |
| BNPL | Buy now pay later (Afterpay, Laybuy) |
| Particulars / Code / Reference | NZ-specific 3-field payment reference system |

**NZ payment reference system.** New Zealand bank payments have three freeform reference fields: Particulars (12 chars), Code (12 chars), Reference (12 chars). These often contain invoice numbers, account references, or payment descriptions. Always read all three fields when identifying a transaction.

**Internal transfers.** Own-account transfers between the client's ANZ, ASB, Westpac accounts. Labelled "transfer", "TFR", or matching account numbers. Always exclude.

**Sole trader draws.** A self-employed sole trader cannot pay themselves wages. Transfers to personal accounts are drawings. Exclude.

**ACC invoices.** A direct debit labelled ACC does not establish the invoice GST or credit. Obtain the actual invoice and establish the GST amount, eligibility and period before any claim. Do not apply a blanket exclusion.

**IRD payments.** GST payments, provisional tax, PAYE appear as "IRD" or "INLAND REVENUE". Always exclude — these are tax payments, not supplies.

**Refunds and reversals.** Identify by "refund", "reversal", "credit adj". Book as a negative in the same field as the original.

**Foreign currency.** Convert to NZD at the RBNZ (Reserve Bank of New Zealand) mid-rate on the transaction date. Note the rate in column L.

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type

- **Entity type** — Inference rule: personal name = sole trader; "Ltd", "Limited" = company; "LP" = limited partnership. Fallback: "Are you a sole trader, partnership, company, or look-through company?"

### 9.2 GST registration

Obtain the registration record and effective date; do not infer registration from a request for GST101A. Resolve any possible registration liability before treating an unregistered business as having no GST obligations.

### 9.3 Accounting basis

Obtain the registered invoice, payments or hybrid basis. Business size, bank-only data and an accrual export do not prove the registered basis. Stop until it is confirmed.

### 9.4 Filing period

Obtain the registered period and due date from myIR or the issued return. Do not infer them from a statement date range. Confirm balance-date alignment and any approved change.

### 9.5 Industry

- **Industry** — Inference rule: counterparty mix. Fallback: "In one sentence, what does the business do?"

### 9.6 Employees

- **Employees** — Inference rule: PAYE/KiwiSaver/wages outgoing. Fallback: "Do you have employees?"

### 9.7 Exempt supplies

- **Exempt supplies** — Inference rule: financial services, residential rental income patterns. Fallback: "Do you make any GST-exempt supplies (financial services, residential rental)?"

### 9.8 Zero-rated supplies

- **Zero-rated supplies** — Inference rule: foreign currency incoming, Australian/overseas counterparties. Fallback: "Do you export goods or provide services to customers outside NZ?"

### 9.9 Prior period balance

- **Prior period balance** — Not inferable. Always ask. "Do you have any GST owing or refund due from the previous period?"

### 9.10 Vehicle use

- **Vehicle use** — Inference rule: fuel purchases, vehicle-related charges. Fallback: "Do you use a vehicle for business? Do you have a logbook?"

## Section 10 — Reference material

### Validation status

Version 2.1 checks only the selected core described in Section 1. Other classification suggestions and special regimes retain their stated gaps and require current evidence. This update does not constitute whole-guide or practitioner verification.

### Sources

**Primary legislation:**
1. Goods and Services Tax Act 1985 (NZ) — s.3 (definitions), s.8 (imposition), s.8(4B) (reverse charge), s.11/11A (zero-rating), s.14 (exempt), s.20 (calculation of tax), s.21–21H (change of use), s.24 (tax invoices and secondhand goods), s.26 (bad debts), s.51 (registration)
2. Tax Administration Act 1994 — filing and payment obligations
3. Income Tax Act 2007, subpart DD — entertainment limitation

**IRD guidance:**
4. GST101A form and guide — ird.govt.nz
5. IR375 GST guide — comprehensive GST guidance
6. IR546 Keeping records — record-keeping requirements
7. IS 24/07 (or current version) — non-resident digital services GST registration

**Other:**
8. RBNZ exchange rates — rbnz.govt.nz
9. Companies Office — companiesoffice.govt.nz (entity verification)
10. myIR — myir.ird.govt.nz (filing portal)

### Known gaps

1. Financial services election (s.20F) is refused — specialized skill needed.
2. Compulsory zero-rating of land is refused — requires property lawyer involvement.
3. Complex change-of-use adjustments on high-value mixed-use assets are refused — too fact-sensitive.
4. GST group registrations are refused.
5. The non-resident supplier GST registration landscape is evolving — always check the invoice for NZ GST before assuming no input tax claim.
6. Special timing, record-value bands, registration exceptions and actual-period allocations require their own evidence. The ordinary GST101A uses inclusive values and 3/23 on both bases.
7. The secondhand goods credit (s.24) has been subject to legislative tightening — verify current requirements.
8. Crypto/digital asset transactions have no specific GST guidance as of April 2026 — flag for reviewer.

### Change log

- **v2.1 (13 November 2026):** Correct GST101A boxes and inclusive values on all bases; confirm registration, timing, filing periods and records before calculation; add conditional arithmetic cases.

- **v2.0 (April 2026):** Full rewrite to align with three-tier OpenAccountants architecture. 10-section Malta v2.0 structure adopted. Supplier pattern library added (Section 3). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template added (Section 7). Bank statement guide with ANZ/Westpac/ASB/BNZ formats added (Section 8). Onboarding moved to fallback (Section 9).
- **v1.1 (April 2026):** Previous version with inline tier tags. Superseded.

### Self-check (v2.1)

1. Quick reference at top with single-rate table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples (hypothetical Auckland IT consultant): yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 13 rules).
5. Tier 2 catalogue compressed: yes (Section 6, 15 items).
6. GST101A working-paper reconciliation: Section 7; no spreadsheet artifact tested.
7. Registration, basis and period must be confirmed before calculation (Sections 2 and 9).
8. All 8 NZ-specific refusals present: yes (Section 2, R-NZ-1 through R-NZ-8).
9. Reference material at bottom: yes (Section 10).
10. No reverse charge for fully taxable businesses explicit: yes (Section 5.5 + Example 1).
11. Non-resident GST registration landscape documented: yes (Section 5.6 + Section 3.8).
12. Entertainment 50% limitation explicit: yes (Section 5.11 + Example 3).
13. Vehicle logbook requirement explicit: yes (Section 5.10 + Example 6).
14. 3/23 formula explained: yes (Section 1 + Section 7).
15. Payments vs invoice basis distinction explicit: yes (Section 5.7 + Section 7).

## End of New Zealand GST Return Skill v2.1

This skill is incomplete without the companion workflow file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a GST101A without it loaded.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
