---
name: nz-gst-return
description: Use this skill whenever asked about New Zealand GST returns for self-employed individuals. Trigger on phrases like "GST return", "GST101A", "GST rate NZ", "input tax", "output tax", "zero-rated", "GST registration", "taxable supply", "IRD GST", "myIR GST", or any question about GST filing for sole traders in New Zealand. Covers the 15% standard rate, zero-rated and exempt supplies, $60K registration threshold, invoice and payments basis, and GST101A return preparation. ALWAYS read this skill before touching any NZ GST work.
version: 2.1
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-11-13
review_status: pending_review
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NZ GST Return

## Section 1 -- Quick Reference

**Selected rules checked 13 November 2026.** The verified core below covers ordinary supplies by an established resident GST-registered small business, using its confirmed accounting basis and taxable period. It uses the GST101A layout currently published by Inland Revenue. The form is dated April 2023 and IR375 is dated March 2026. GST is a continuing tax; the frontmatter year records this source check, not an income-year rate change.

Confirm the actual supply, consideration, timing, supplier GST treatment, business use and supporting records before using a figure. A bank narration, supplier name or request for a return cannot establish these facts. Unresolved items stay in a separate reconciliation with their amount and missing evidence recorded. Do not deliver filing-ready figures until all material transactions and adjustments are reconciled. Never omit an unresolved transaction silently.  Do not label an incomplete reconciliation as a nil return. Legacy transaction suggestions and special-regime examples elsewhere in this guide do not establish eligibility and were not reverified by this update.

Stop this ordinary workflow for GST groups, non-resident registration, land or business transfers, marketplaces, imported goods or services, associated persons, secondhand goods credits, hire purchase, progressive/periodic or other special time-of-supply arrangements, cancellation, basis changes and special adjustments unless their separate current treatment has been established. A payments-basis supply over $225,000 also requires separate section 19D analysis; payments basis alone does not justify cash treatment. Mixed/private/exempt use requires an established credit allocation before any Box 11 amount is used. [GSTA ss 9, 19D, 20](https://www.legislation.govt.nz/act/public/1985/141/en/latest/); [IR375, pp 7 and 11–13](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | New Zealand |
| Tax | Goods and Services Tax (GST) at 15% |
| Currency | NZD only |
| Taxable periods | Confirm registered dates and balance-date alignment; GST is not an annual income-tax return |
| Primary legislation | Goods and Services Tax Act 1985 (GSTA 1985) |
| Tax authority | Inland Revenue (IR / Te Tari Taake) |
| Filing portal | myIR (myir.ird.govt.nz) |
| Filing deadline | 28th of following month; 31 March → 7 May and 30 November → 15 January; next working day if needed |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a New Zealand chartered accountant (CA) |
| Skill version | 2.1 |

### Rate Table

**Rate Table**

| Rate | Application |
| --- | --- |
| 15% | Standard-rated taxable supplies |
| 0% | Supplies whose statutory zero-rating conditions have been established; do not infer zero rating from a product or narration |
| Exempt | Financial services, residential rent, donated goods (certain conditions) |

### Tax Fraction

- **Tax fraction for GST-inclusive amounts at 15%** — 3/23 (i.e. 15/115 = 3/23)

### Key Thresholds

**Key Thresholds**

| Item | Amount (NZD) |
| --- | --- |
| Registration | Confirm registration/effective date and section 51 tests; exactly $60,000 and GST charged while unregistered require separate resolution |
| Voluntary registration | Any person making taxable supplies |
| Payments basis eligibility | Ordinary statutory limit includes $2,000,000; confirm approved basis and section 19A tests |
| Six-monthly filing eligibility | Statutory tests include $500,000; confirm approval and the wording difference in Section 5.3 |
| Monthly filing required | Taxable supplies > $24,000,000 |
| Purchase evidence | Current taxable supply information; no universal $50 invoice rule |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| GST registration status unknown | STOP -- do not compute |
| Accounting basis unknown | STOP; obtain registered basis |
| Supply classification unknown | STOP classification; obtain evidence |
| Private use proportion unknown | 0% GST recovery |
| Going concern status unknown | STOP; establish the transfer treatment separately |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Before calculation obtain the registration record and effective date, confirmed basis, balance date, exact return period and due date, complete sales and purchase records, taxable supply information, all relevant bank/cash/processor activity and reconciled prior-period allocations. Confirm any zero rating, exempt activity, private use and adjustments separately. A bank statement alone is a transaction-gathering input; it is not sufficient authority to populate the return. Missing status, basis or material supply evidence means stop the calculation and list what is missing. Do not request credentials or submit the return on the user's behalf.

For supplies from 1 April 2023 the general evidence requirement is **taxable supply information**, which can be held across invoices, contracts, accounting records and other documents. A document may still be called a tax invoice. The old universal '$50 tax invoice' rule must not be used. Confirm the current information requirements for the value and type of supply and keep the evidence before claiming. This update does not verify the full value-band table or every special credit. [IRD taxable supply information](https://www.ird.govt.nz/gst/tax-invoices-for-gst); [IR375, pp 2 and 8–10](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

### Refusal Catalogue

- **R-NZ-1 -- Registration unresolved**: stop calculation if registration or its effective date is unknown. If unregistered, check liability under section 51 and any GST charged before concluding no filing is due.
- **R-NZ-2 -- Companies and partnerships** — This skill covers individual self-employed persons only. Company and partnership GST returns may have additional requirements.
- **R-NZ-3 -- Financial services (complex)** — Complex financial services GST treatment requires specialist review. Escalate.
- **R-NZ-4 -- Cross-border digital services (complex)** — Non-resident digital services GST has specific registration and collection rules. Escalate if amounts are material.

## Section 3 -- Transaction Pattern Library

Names and narrations only help locate evidence. These legacy suggestions do not establish a supply, tax rate, exemption or credit. Confirm current treatment from the actual documents before including any amount in the return; leave unresolved items unclassified.

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| DIRECT CREDIT [client] / DC [client] | Taxable supply | GST-inclusive revenue | Standard client payment |
| EFTPOS SETTLEMENT / EFTPOS CREDIT | Taxable supply | Revenue | Card terminal settlement |
| INTERNET BANKING CREDIT [client] | Taxable supply | Revenue | Online bank transfer |
| STRIPE NZ / STRIPE PAYOUT | Taxable supply | Revenue (net of fees) | Stripe payout -- gross up for fees |
| SHOPIFY PAYOUT / SHOPIFY SETTLEMENT | Taxable supply | Revenue | E-commerce platform settlement |
| XERO INVOICE PAYMENT | Taxable supply | Revenue | Xero-linked payment |
| INTEREST / INT EARNED [bank] | Exempt | NOT taxable supply | Bank interest -- exempt financial service |
| DIVIDEND [company] | Exempt | NOT taxable supply | Dividend |
| IRD REFUND / TAX REFUND | EXCLUDE | Not income | Tax refund |
| LOAN DRAWDOWN | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

**Expense Patterns (Debits)**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| SPARK / VODAFONE / 2DEGREES | Communications | Business portion deductible | Mixed use: apportion |
| VECTOR / MERCURY / GENESIS / CONTACT ENERGY | Utilities | Business portion deductible | Home office: apportion |
| COUNTDOWN / PAK'N SAVE / NEW WORLD | NOT business | Private | Unless entertainment or business meeting |
| BUNNINGS / MITRE 10 | Office supplies | Deductible if business | Keep receipts |
| GOOGLE ADS / META / LINKEDIN | Advertising | Fully deductible |  |
| ADOBE / MICROSOFT / XERO / SLACK | Software | Fully deductible | Business subscription |
| AIR NEW ZEALAND / JETSTAR | Travel | Deductible if business | Keep itinerary |
| UBER NZ / TAXI | Travel | Deductible if business | Not commuting |
| ACC LEVY | Unresolved pending invoice | Check actual GST, eligibility and timing | No blanket exclusion |
| IRD INCOME TAX / IRD PAYE | EXCLUDE | Tax payment | Not deductible |
| BANK FEE / ANZ FEE / ASB FEE / BNZ FEE / WESTPAC FEE | Exempt | No GST on bank fees | Financial service exempt |
| PERSONAL TRANSFER / OWN ACCOUNT | EXCLUDE | Drawings | Not business |

### 3.3 Zero-Rated Supply Indicators

**Zero-Rated Supply Indicators**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EXPORT / INTERNATIONAL FREIGHT | Zero-rated output | Goods exported from NZ |
| GOING CONCERN SALE | Zero-rated output | Both parties must be GST-registered |
| FINE METALS / GOLD BULLION | Zero-rated | Gold, silver, platinum of certain fineness |

## Section 4 -- Worked Examples

### Verified core worked checks

These are synthetic, conditional examples for the selected core. They check arithmetic and box placement after classification, eligibility, timing and records have been established. They do not test a live return or grant filing authority.

#### Core case 1: Ordinary payments-basis return

Confirmed ordinary standard-rated customer receipts are $23,000 and eligible supplier payments are $8,050, both GST-inclusive. There are no zero-rated supplies or adjustments. The result is $1,950 payable.

```oa-check
name: nz-gst-return-core-payments-standard
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
name: nz-gst-return-core-invoice-exclusive-conversion
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
name: nz-gst-return-core-supplied-adjustments
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
name: nz-gst-return-core-zero-rated-refund
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
name: nz-gst-return-core-payment-before-invoice
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
name: nz-gst-return-core-hybrid-direction
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
name: nz-gst-return-core-exclude-exempt-nonsupply
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
name: nz-gst-return-core-invoice-prior-period-receipt
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
name: nz-gst-return-core-zero-balance-activity
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


### Example 1 -- Standard Two-Monthly Return

**Input:** Period Jan-Feb. Total sales (incl. GST) $23,000. Total purchases (incl. GST) $8,050. All standard-rated. No adjustments.

**Reasoning:**
Output tax: $23,000 x 3/23 = $3,000. Input tax: $8,050 x 3/23 = $1,050. Net GST payable: $3,000 - $1,050 = $1,950.

**Classification:** GST payable $1,950.

### Example 2 -- Exporter in Refund Position

**Input:** Total sales $50,000 (all zero-rated exports). Total purchases (incl. GST) $17,250.

**Reasoning:**
Output tax: $0 (zero-rated). Input tax: $17,250 x 3/23 = $2,250. GST refund: $2,250.

**Classification:** GST refund $2,250.

### Example 3 -- Entertainment Expense

**Input:** Business dinner $460 (incl. GST).

**Reasoning:**
GST content: $460 x 3/23 = $60. Entertainment 50% restriction applies. Claimable: 50% x $60 = $30. Non-claimable: $30.

**Classification:** Input tax claimable $30 only.

### Example 4 -- Private Use Apportionment

**Input:** Laptop purchased for $2,300 (incl. GST), used 70% business, 30% private.

**Reasoning:**
GST content: $2,300 x 3/23 = $300. Claim 70%: $300 x 70% = $210.

**Classification:** Input tax $210. Flag for reviewer on apportionment basis.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 GST101A return entries

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


### 5.2 Registration and accounting basis

### Registration check

Confirm the registration record and effective date. An unregistered business may already be required to register. Inland Revenue's public registration page says taxable turnover of at least $60,000 in the past or expected next 12 months, or adding GST to prices, requires registration. Section 51(1) uses a month-end past-12-month test that **exceeds** $60,000 and a month-start reasonable expectation that the next 12 months **will exceed** $60,000, with statutory exceptions. Values are GST-exclusive under section 51(6). At exactly $60,000, or where an exception or charging GST without registration is involved, obtain Inland Revenue's registration determination rather than deciding from this guide. A person liable under section 51(1) must apply within 21 days under section 51(2). Voluntary registration under section 51(3) is a separate application for a taxable activity or intended taxable activity. Do not infer registration or an automatic right to cease filing from turnover. [Registering for GST](https://www.ird.govt.nz/registering-for-gst); [GSTA s 51](https://www.legislation.govt.nz/act/public/1985/141/en/latest/).

### Confirmed accounting basis and timing

| Basis | Ordinary treatment after all scope and record checks |
| --- | --- |
| Payments | Recognise customer receipts and supplier payments in the period paid. Section 19A permits an application where either the past-12-month taxable-supply value or the relevant expected value is no more than $2 million; special approvals and directions also exist. Confirm the registered basis and eligibility, including at exactly $2 million. |
| Invoice | Apply the ordinary section 9(1) time of supply: the earlier invoice or any payment. A partial pre-invoice payment for an ordinary fixed-price sale brings in the full sale price. Include qualifying supplier invoices or earlier payments with the required records, even if not fully paid. |
| Hybrid | Invoice treatment for sales and payments treatment for purchases. The reverse combination is not the hybrid method. |

Unknown basis means stop and obtain the registration record. A bank statement alone cannot establish an invoice-basis return; obtain the sales/purchase registers, opening and closing unpaid invoices, earlier receipts/payments and prior-period allocations to prevent duplication. Even on payments basis, reconcile all relevant accounts, cash and payment processors to gross sales and costs; a net settlement is not the sale price. The special rules excluded above can override ordinary timing. [GSTA ss 9, 19, 19A, 19D and 20](https://www.legislation.govt.nz/act/public/1985/141/en/latest/); [IRD accounting basis](https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use); [IR375, pp 6–7](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

### 5.3 Filing periods and due dates

### Taxable periods, filing and payment

Confirm the actual period and due date shown in myIR. Ordinary monthly filing is available by choice and required if the past or expected 12-month supply value exceeds $24 million under section 15. Two-monthly is the ordinary default. Section 15 allows an application for 6-monthly periods where the applicable 12-month taxable-supply value is no more than $500,000 and is not likely to be more than $500,000. Inland Revenue's summary uses 'under $500,000'; at exactly $500,000 confirm eligibility and approval with Inland Revenue. Do not change periods or basis before the change is confirmed.

For a 31 March balance date, the ordinary aligned 2-monthly periods end in May, July, September, November, January and March; 6-monthly periods end in September and March. Use the registered dates, not the span of the supplied bank statement. Alternative end dates, transitions and other balance dates require their actual approved periods. [GSTA ss 15–15ED](https://www.legislation.govt.nz/act/public/1985/141/en/latest/); [IRD accounting basis and filing frequency](https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use); [IR375, p 6](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

File for every taxable period, including a genuine nil return. Filing and payment are ordinarily due on the 28th of the following month, except a 31 March period ends with a 7 May due date and a 30 November period with a 15 January due date in the next year. If that date is a weekend or public holiday use the next working day. Confirm the applicable holiday calendar and myIR date. Ordinary GST filing has no extension simply because an income-tax agent extension exists. Special statutory variations remain outside this ordinary slice. [GSTA ss 16 and 23](https://www.legislation.govt.nz/act/public/1985/141/en/latest/); [Filing GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst); [IR375, pp 6 and 19](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).


### 5.4 Purchase evidence and credits

For supplies from 1 April 2023 the general evidence requirement is **taxable supply information**, which can be held across invoices, contracts, accounting records and other documents. A document may still be called a tax invoice. The old universal '$50 tax invoice' rule must not be used. Confirm the current information requirements for the value and type of supply and keep the evidence before claiming. This update does not verify the full value-band table or every special credit. [IRD taxable supply information](https://www.ird.govt.nz/gst/tax-invoices-for-gst); [IR375, pp 2 and 8–10](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

For this ordinary slice, use only a separately confirmed eligible credit for taxable business use. Do not extract GST from exempt, zero-rated, private or no-GST expenditure. Mixed use, entertainment, imports and special credits need their own allocation and timing evidence.

### 5.5 Late filing and payment

Do not apply a universal $250 late-filing penalty. Inland Revenue distinguishes payments-basis returns from invoice/hybrid returns. Notices, statutory exceptions, payment penalties and interest require separate verification before an amount is calculated. See [IR375, p 19](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf?modified=20260331214047).

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Mixed-Use Assets

- **Mixed-use assets adjustment flag** — If the proportion of taxable use changes, adjustments may be required. Flag for reviewer if mixed-use assets exceed $5,000.

### 6.2 Bad Debts (s 26)

- **Bad debt adjustment** — On invoice basis, if a debt is written off and the statutory conditions are established, consider a credit adjustment in Box 13 for the GST component.  _(GSTA 1985, s 26)_

### 6.3 Second-Hand Goods Input Tax

- **Second-hand goods input tax claim** — A registered person can claim input tax on second-hand goods purchased from a non-registered person, subject to conditions.

### 6.4 Change of Use Adjustments

- **Change of use adjustment** — When the business/private use proportion of an asset changes, adjustments may be required in the GST return.

## Section 7 -- GST101A working paper

Record registration, effective date, basis, period, due date, preparer and source references before figures. Use the Box 5–15 mapping in Section 1/5; do not renumber fields for a spreadsheet.

1. Reconcile all receipts to taxable, zero-rated, exempt, non-supply and unresolved items, using the confirmed timing basis. Box 5 includes only taxable receipts/sales recognised in this period, with GST included; Box 6 is its zero-rated subset.
2. Reconcile all costs to eligible standard-rated purchases, separately established adjustments and excluded/unresolved amounts. Box 11 is the ordinary GST-inclusive credit base after the established eligibility allocation. Keep imported goods and other special credits out of this base.
3. Compute Boxes 7, 8, 10, 12 and 14 from the published form equations. Boxes 9 and 13 require a separate adjustment schedule with legal basis, evidence, period and amount. An example using supplied adjustment amounts verifies only the field mapping.
4. Retain signed balance = Box 10 − Box 14 in the working paper. Enter its absolute value and payment/refund indicator in Box 15. A zero balance still requires filing; a net zero from offsetting activity does not mean no transactions.
5. Reconcile invoice and payments allocations to prior returns. Review exceptions, duplicate payments, outstanding invoices and all unresolved amounts before calling the return complete. Use software calculations and cross-check totals against the form; do not copy a formula that changes 3/23 to 15% merely because the basis is invoice.

This is a working-paper specification. No spreadsheet file or live myIR filing was created or tested by this update.


## Section 8 -- Bank Statement Reading Guide

### NZ Bank Statement Formats

**NZ Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| ANZ NZ | CSV / PDF | Date, Description, Amount, Balance |
| ASB | CSV | Date, Unique Id, Tran Type, Cheque Number, Payee, Memo, Amount |
| BNZ | CSV | Date, Description, Debit, Credit, Balance |
| Westpac NZ | CSV | Date, Description, Debit, Credit, Balance |
| Kiwibank | CSV | Date, Description, Amount, Balance |
| TSB | CSV | Date, Details, Debit, Credit, Balance |

### Key NZ Banking Narrations

**Key NZ Banking Narrations**

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| D/C or DIRECT CREDIT | Bank transfer in | Potential income |
| AP or AUTOPAY | Automatic payment out | Regular expense |
| EFTPOS | Card terminal payment | Expense or income |
| TFR / TRANSFER | Internal transfer | Investigate -- may be drawings |
| DD / DIRECT DEBIT | Direct debit | Regular expense |
| IRD / INLAND REVENUE | Tax payment or refund | Exclude |
| ACC | Possible levy payment | Obtain invoice/GST and eligibility; no blanket exclusion |

## Section 9 -- Missing onboarding information

Stop return calculation if registration, effective date, basis, period or material supply evidence is missing. Prepare a list of unresolved amounts and questions only. Obtain the registered invoice/payments/hybrid basis and taxable period, balance date, current purchase records and evidence for zero rating, exempt activity, private use or special supplies. Bank narrations and business size do not answer these questions. Resume only when the required facts and reconciliation are established.

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Section |
| --- | --- |
| Imposition of GST | GSTA 1985, s 8 |
| Zero-rated supplies | GSTA 1985, s 11 |
| Exempt supplies | GSTA 1985, s 14 |
| Registration | GSTA 1985, s 51 |
| Accounting basis | GSTA 1985, s 19, 19A |
| Input tax | GSTA 1985, s 20, 21 |
| Filing periods | GSTA 1985, s 15, 16 |
| Bad debts | GSTA 1985, s 26 |

### Known Gaps / Out of Scope

- Company and partnership GST returns
- Complex financial services
- Cross-border digital services (non-resident supplier rules)
- Associated persons transactions
- GST grouping

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 2.1 | 13 November 2026 | Correct GST101A boxes, inclusive values, registration/basis/period checks and conditional examples |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; NZ bank formats; local platform patterns; worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Registration confirmed and GST number recorded?
- [ ] Accounting basis confirmed (invoice vs payments)?
- [ ] Tax fraction 3/23 used consistently?
- [ ] Entertainment 50% restriction applied?
- [ ] Exempt receipts excluded from Box 5 and zero-rated sales included in Boxes 5 and 6?
- [ ] Zero-rated supplies correctly reported in Box 6?

## PROHIBITIONS

- NEVER charge GST if the person is not GST-registered
- NEVER claim input tax on private expenditure
- NEVER claim full input tax on entertainment -- the 50% restriction applies
- NEVER use a tax fraction other than 3/23 for the 15% rate
- NEVER allow a going concern zero-rating unless both parties are registered
- NEVER ignore the accounting basis -- invoice vs payments basis changes when GST is accounted for
- Exclude exempt receipts from Box 5; do not deduct them a second time in Box 8.
- NEVER present calculations as definitive -- always label as estimated and direct client to IR or a qualified NZ chartered accountant

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

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
