---
name: australia-bookkeeping
description: Use this skill whenever asked about Australian bookkeeping for sole traders, partnerships, or small companies. Trigger on phrases like "chart of accounts", "BAS", "GST codes", "bookkeeping", "profit and loss", "balance sheet", "AASB", "simplified disclosures", "Tier 2", "bank reconciliation", "expense categories", "revenue recognition", "depreciation", "instant asset write-off", "small business pool", "ABN", "ATO reporting", "activity statement", "accrual basis", "cash basis", "general ledger", or any question about day-to-day transaction recording, financial statement preparation, or account coding for an Australian business.
version: 1.1
jurisdiction: AU
tax_year: 2025
last_updated: 2026-09-14
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD ($) only |
| Financial year | 1 July – 30 June (standard); substituted accounting period available for companies |
| Accounting standards | AASB Tier 1 or Tier 2 according to public accountability and regulator requirements; special-purpose reporting only where permitted (Section 9) |
| Governing body | Australian Accounting Standards Board (AASB) |
| Tax authority | Australian Taxation Office (ATO) |
| Key legislation | Corporations Act 2001 (financial reporting Ch.2M); Income Tax Assessment Act 1936/1997; A New Tax System (GST) Act 1999 |
| GST registration threshold | $75,000 turnover ($150,000 for non-profits) |
| Small business entity threshold | Aggregated turnover < $10 million |
| BAS lodgement | Quarterly (most small businesses) or monthly ($20m+ turnover) |

## Section 2 -- Standard Chart of Accounts

Australian software (Xero, MYOB, QuickBooks) typically uses 3–4 digit codes. The structure below follows common Australian practice.

### Assets (1000–1999)

**Assets (1000–1999)**

| Code | Account | Type |
| --- | --- | --- |
| 1000 | Cash on Hand / Petty Cash | Current asset |
| 1010 | Business Bank Account | Current asset |
| 1020 | Savings Account | Current asset |
| 1030 | Term Deposits (< 12 months) | Current asset |
| 1050 | Undeposited Funds | Current asset |
| 1100 | Accounts Receivable (Trade Debtors) | Current asset |
| 1110 | Other Debtors | Current asset |
| 1120 | Prepayments | Current asset |
| 1150 | GST Receivable (Input Tax Credits) | Current asset |
| 1200 | Inventory / Stock on Hand | Current asset |
| 1300 | Land | Non-current asset |
| 1310 | Buildings | Non-current asset |
| 1311 | Accumulated Depreciation — Buildings | Contra asset |
| 1320 | Plant and Equipment | Non-current asset |
| 1321 | Accumulated Depreciation — Plant & Equipment | Contra asset |
| 1330 | Motor Vehicles | Non-current asset |
| 1331 | Accumulated Depreciation — Motor Vehicles | Contra asset |
| 1340 | Office Equipment | Non-current asset |
| 1341 | Accumulated Depreciation — Office Equipment | Contra asset |
| 1350 | Computer Equipment | Non-current asset |
| 1351 | Accumulated Depreciation — Computer Equipment | Contra asset |
| 1360 | Furniture and Fittings | Non-current asset |
| 1361 | Accumulated Depreciation — Furniture & Fittings | Contra asset |
| 1400 | Small Business Pool | Non-current asset |

### Liabilities (2000–2999)

**Liabilities (2000–2999)**

| Code | Account | Type |
| --- | --- | --- |
| 2000 | Accounts Payable (Trade Creditors) | Current liability |
| 2010 | Other Creditors | Current liability |
| 2020 | Accrued Expenses | Current liability |
| 2050 | GST Payable (Collected) | Current liability |
| 2060 | GST Clearing / Control | Current liability |
| 2100 | PAYG Withholding Payable | Current liability |
| 2110 | Superannuation Payable | Current liability |
| 2120 | Provision for Annual Leave | Current liability |
| 2130 | Provision for Long Service Leave | Split current and non-current under AASB 1060 paragraphs 40 and 41 |
| 2140 | Provision for Income Tax | Current liability |
| 2200 | Credit Card | Current liability |
| 2300 | Short-Term Loan (< 12 months) | Current liability |
| 2400 | Long-Term Loan (> 12 months) | Non-current liability |
| 2410 | Hire Purchase Liability | Non-current liability |
| 2500 | Director's Loan Account | Non-current liability |

### Equity (3000–3999)

**Equity (3000–3999)**

| Code | Account | Type |
| --- | --- | --- |
| 3000 | Share Capital / Owner's Equity | Equity |
| 3010 | Owner's Drawings | Equity |
| 3020 | Owner's Contributions | Equity |
| 3100 | Retained Earnings | Equity |
| 3200 | Current Year Profit/Loss | Equity |
| 3300 | Reserves | Equity |

### Revenue (4000–4999)

**Revenue (4000–4999)**

| Code | Account | Type |
| --- | --- | --- |
| 4000 | Sales Revenue — Taxable (GST 10%) | Revenue |
| 4010 | Sales Revenue — GST-Free | Revenue |
| 4020 | Sales Revenue — Input Taxed | Revenue |
| 4030 | Sales Revenue — Export (GST-Free) | Revenue |
| 4100 | Service Revenue | Revenue |
| 4200 | Interest Income | Revenue |
| 4300 | Rental Income | Revenue |
| 4400 | Government Grants / Subsidies | Revenue |
| 4500 | Other Income | Revenue |
| 4900 | Discount Allowed | Contra revenue |

### Cost of Goods Sold (5000–5999)

**Cost of Goods Sold (5000–5999)**

| Code | Account | Type |
| --- | --- | --- |
| 5000 | Purchases — Trading Stock | COGS |
| 5010 | Purchases — Materials / Components | COGS |
| 5020 | Freight Inward | COGS |
| 5030 | Direct Labour | COGS |
| 5040 | Subcontractor Costs | COGS |
| 5100 | Opening Stock Adjustment | COGS |
| 5110 | Closing Stock Adjustment | COGS |
| 5200 | Import Duty and Customs | COGS |

### Operating Expenses (6000–6999)

**Operating Expenses (6000–6999)**

| Code | Account | Type |
| --- | --- | --- |
| 6000 | Rent — Business Premises | Expense |
| 6010 | Rates and Body Corporate | Expense |
| 6020 | Electricity and Gas | Expense |
| 6030 | Water | Expense |
| 6040 | Insurance — Business | Expense |
| 6050 | Repairs and Maintenance | Expense |
| 6100 | Wages and Salaries | Expense |
| 6110 | Superannuation Guarantee (12% from Jul 2025) | Expense |
| 6120 | Workers' Compensation Insurance | Expense |
| 6130 | Payroll Tax (state-based) | Expense |
| 6140 | Staff Training | Expense |
| 6200 | Advertising and Marketing | Expense |
| 6210 | Website and Hosting | Expense |
| 6220 | Printing and Stationery | Expense |
| 6230 | Postage and Delivery | Expense |
| 6300 | Motor Vehicle — Fuel | Expense |
| 6310 | Motor Vehicle — Registration and Insurance | Expense |
| 6320 | Motor Vehicle — Repairs | Expense |
| 6330 | Travel — Domestic | Expense |
| 6340 | Travel — International | Expense |
| 6350 | Meals and Entertainment (50% deductible FBT) | Expense |
| 6400 | Accounting and Tax Agent Fees | Expense |
| 6410 | Legal Fees | Expense |
| 6420 | Bank Charges | Expense |
| 6430 | Merchant / Payment Processing Fees | Expense |
| 6440 | Interest Expense | Expense |
| 6500 | Telephone and Internet | Expense |
| 6510 | Software Subscriptions (SaaS) | Expense |
| 6520 | Professional Subscriptions and Memberships | Expense |
| 6600 | Depreciation — Buildings | Expense |
| 6610 | Depreciation — Plant and Equipment | Expense |
| 6620 | Depreciation — Motor Vehicles | Expense |
| 6630 | Depreciation — Office/Computer Equipment | Expense |
| 6700 | Bad Debts Written Off | Expense |
| 6800 | General and Sundry Expenses | Expense |

### Other Income / Expenses (7000–7999)

**Other Income / Expenses (7000–7999)**

| Code | Account | Type |
| --- | --- | --- |
| 7000 | Gain on Sale of Assets | Other income |
| 7010 | Loss on Sale of Assets | Other expense |
| 7020 | Foreign Exchange Gain/Loss | Other income/expense |
| 7100 | Other Material Expenses | Classify by nature or function; describe the item in the statements or notes |

AASB 1060 paragraph 57 prohibits presenting income or expenses as extraordinary items in financial statements or notes. An unusual transaction still needs a description of its nature.

### Tax (8000–8999)

**Tax (8000–8999)**

| Code | Account | Type |
| --- | --- | --- |
| 8000 | Income Tax Expense | Tax |
| 8010 | Deferred Tax Liability | Tax |
| 8020 | Deferred Tax Asset | Tax |

## Section 3 -- Revenue Recognition

### Cash vs Accrual Rules

**Cash vs Accrual Rules**

Determine income-tax derivation, GST attribution and financial reporting separately. Turnover below $10 million does not itself permit the receipts method for income tax.

| Purpose | Rule |
| --- | --- |
| Ordinary income for income tax | Use the method giving a substantially correct reflection of income under TR 98/1. The receipts method can suit a sole professional's personal skill; an earnings method may be needed where staff or equipment produce income. Assess the business circumstances. |
| Statutory income and deductions | Apply the specific tax rules, including when a deductible liability is incurred, capital exclusions and prepayment spreading. A cash receipt basis does not make every cash payment deductible. |
| GST | Test eligibility for cash attribution separately under GST Act s 29-40, including the small-business concession. Cash GST attribution can coexist with accrual financial accounts. |
| AASB financial reporting | Apply the relevant recognition and measurement standards, including AASB 15 below; a GST election does not change them. |
| Trading stock | An eligible business may choose simplified treatment if the reasonably estimated stock-value change is $5,000 or less; otherwise apply the opening/closing stock rules. |
| Prepaid expenses | Test deductibility first. For eligible small or medium businesses, the s 82KZM rule allows a service period of 12 months or less ending by the end of the following income year. Separately, otherwise deductible expenditure below $1,000 is excluded from spreading under s 82KZL, after allowing for input tax credit entitlement. Otherwise apply the relevant spreading rules. |

### AASB 15 Revenue from Contracts with Customers

Applies to reporting entities using Tier 1/Tier 2. Five-step model:
1. Identify contract
2. Identify performance obligations
3. Determine transaction price
4. Allocate price to obligations
5. Recognise when obligation satisfied

Small businesses using simplified reporting typically recognise on delivery/completion.

## Section 4 -- Expense Classification

### ATO Individual Tax Return Categories (Sole Trader — Business Schedule)

**ATO Individual Tax Return Categories (Sole Trader — Business Schedule)**

| 2025 BPI label | Category | Nominal Codes |
| --- | --- | --- |
| P8 I / J (income section) | Other business income, primary / non-primary production | 4000–4500 |
| P8 Cost of sales | Cost of sales | 5000–5200 |
| P8 F | Contractors and commission | 5040 |
| P8 G | Superannuation | 6110 |
| P8 I (expenses section) | Bad debts | 6700 |
| P8 J (expenses section) | Lease expense (plant/equipment) | 6000 |
| P8 Q | Interest expense within Australia | 6440 |
| P8 M | Depreciation; complete simplified-depreciation details and reconciliation where required | 6600–6630 |
| P8 N | Motor vehicle expenses | 6300–6320 |
| P8 O | Repairs and maintenance | 6050 |
| P8 P | All other expenses | 6000–6800 (remainder) |

These labels follow the [ATO 2025 BPI expenses instructions](https://www.ato.gov.au/forms-and-instructions/business-and-professional-items-schedule-2025-instructions/instructions-to-complete-the-bpi-schedule-2025/business-income-and-expenses-p8/expenses-p8). Keep the income and expenses sections separate where letters repeat, and check the applicable form for another year.

### Non-Deductible Expenses (ATO)

- Entertainment (not subject to FBT election) — non-deductible portion
- Capital expenditure — must be depreciated or written off via SB pool
- Private portion of mixed expenses — must be apportioned
- Fines and penalties — not deductible
- Clothing (non-compulsory, non-protective) — not deductible
- Traffic infringements — not deductible

### GST Classification for BAS

**GST Classification for BAS**

| GST Code | Description | BAS Label |
| --- | --- | --- |
| GST (10%) | Standard taxable supply | G1, 1A |
| GST-Free | Food (basic), medical, education, exports | G1 (no 1A) |
| Input Taxed | Financial supplies, residential rent | G1 (no credit) |
| BAS Excluded | Wages, drawings, loan principal, private | Not reported |
| No ABN Withholding | Payments to suppliers without ABN (47% w/h, subject to exceptions) | Separate |

## Section 5 -- Asset vs Expense Thresholds

### Instant Asset Write-Off (IAWO)

**Instant Asset Write-Off (IAWO)**

| Period | Threshold | Eligibility |
| --- | --- | --- |
| 1 Jul 2023 – 30 Jun 2026 | < $20,000 per asset | Aggregated turnover < $10m, using simplified depreciation |
| From 1 Jul 2026 | < $20,000 per asset under enacted amendments | Eligible small business entities using simplified depreciation. Treasury Laws Amendment (Tax Reform No. 2) Act 2026 received assent on 26 August 2026. Schedule 2 commences on 1 October 2026, with application to assets first used or installed ready for taxable use from 1 July 2026. As at 10 September the amendment has not commenced. [Act, section 2 and Schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text) |

### Small Business Pool (Simplified Depreciation)

**Small Business Pool (Simplified Depreciation)**

| Pool | Rate | Notes |
| --- | --- | --- |
| Year 1 (first use) | 15% | On cost (or adjustable value if added later) |
| Subsequent years | 30% | On opening pool balance |
| Pool balance < IAWO threshold | Write off entire pool | End-of-year check |

### General (Non-SB) Depreciation

**General (Non-SB) Depreciation**

| Method | Application |
| --- | --- |
| Diminishing value | rate = days held ÷ 365 × (200% ÷ effective life) |
| Prime cost (straight-line) | rate = days held ÷ 365 × (100% ÷ effective life) |

### Common Effective Lives

Use the Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025 for Commissioner-determined Div 40 lives, or a supportable self-assessed life. Div 43 uses its own construction-date, use and rate rules; 4% applies only to an eligible category.

**Common Effective Lives**

| Asset | Effective Life | DV Rate | PC Rate |
| --- | --- | --- | --- |
| Desktop computers | 4 years | 50% | 25% |
| Laptops | 2 years | 100% | 50% |
| Printers/Scanners | 5 years | 40% | 20% |
| Freestanding office chairs and general tables | 10 years | 20% | 10% |
| Freestanding office desks and workstations | 20 years | 10% | 5% |
| Motor vehicles | 8 years | 25% | 12.5% |
| Air-conditioning room units and mini split systems up to 20 kW | 10 years | 20% | 10% |
| Packaged air-conditioning units | 15 years | 13.33% (rounded) | 6.67% (rounded) |
| Eligible capital works (Div 43, 2.5% category) | 40 years | Not applicable | 2.5% of eligible construction expenditure; separate from Div 40 |

These are selected Table B asset classes in the 2025 determination. Match the actual asset and applicable industry entry before using a Commissioner-determined life; other furniture and air-conditioning components have different lives. Calculate rates from the life without rounding intermediate deductions. A $10,000 freestanding office desk has a $500 prime-cost deduction for a full year of qualifying business use at 20 years, assuming no immediate-write-off concession.

### Car Limit

- **Car cost limit for depreciation (2025–26)** — $69,674 AUD (Only the business-use portion of this amount can be depreciated)

## Section 6 -- P&L Format

### Income Statement (AASB Simplified / Tier 2)

```
STATEMENT OF PROFIT OR LOSS
For the year ended 30 June 20XX
                                            $           $
Revenue                                               xxx
Cost of sales                                        (xxx)
                                                     ────
Gross profit                                          xxx

Other income                                          xxx

Expenses:
  Employee benefits expense               (xxx)
  Depreciation and amortisation           (xxx)
  Finance costs                           (xxx)
  Other expenses                          (xxx)
                                                     (xxx)
                                                     ────
Profit before income tax                              xxx
Income tax expense                                   (xxx)
                                                     ────
Profit for the year                                   xxx
                                                     ════
```

### Sole Trader — ATO Business Schedule Format

```
BUSINESS INCOME
  Gross payments subject to withholding       xxx
  All other business income                   xxx
  TOTAL BUSINESS INCOME                       xxx

BUSINESS EXPENSES
  Cost of sales                              (xxx)
  Contractor/subcontractor/commission        (xxx)
  Superannuation expenses                    (xxx)
  Bad debts                                  (xxx)
  Lease expenses within Australia            (xxx)
  Interest expenses within Australia         (xxx)
  Depreciation expenses                      (xxx)
  Motor vehicle expenses                     (xxx)
  Repairs and maintenance                    (xxx)
  All other expenses                         (xxx)
  TOTAL BUSINESS EXPENSES                    (xxx)

NET INCOME OR LOSS FROM BUSINESS              xxx
```

## Section 7 -- Balance Sheet Format

Long service leave is current if settlement is expected in the normal operating cycle, it is held for trading, it is due within 12 months, or the entity lacks a right at the reporting date to defer settlement for at least 12 months. Classify other portions as non-current. A vested entitlement can be current even if payment is expected later. Apply AASB 1060 paragraphs 40 and 41 consistently to account 2130 and the statement.

### Statement of Financial Position (Vertical — AASB Tier 2)

```
STATEMENT OF FINANCIAL POSITION
As at 30 June 20XX
                                            $           $
CURRENT ASSETS
  Cash and cash equivalents                           xxx
  Trade and other receivables                         xxx
  Inventories                                         xxx
  Other current assets                                xxx
                                                     ────
Total current assets                                  xxx

NON-CURRENT ASSETS
  Property, plant and equipment                       xxx
  Intangible assets                                   xxx
  Other non-current assets                            xxx
                                                     ────
Total non-current assets                              xxx
                                                     ────
TOTAL ASSETS                                          xxx
                                                     ════

CURRENT LIABILITIES
  Trade and other payables                            xxx
  Current tax liabilities                             xxx
  Provisions (including current leave obligations)    xxx
  Short-term borrowings                               xxx
                                                     ────
Total current liabilities                             xxx

NON-CURRENT LIABILITIES
  Long-term borrowings                                xxx
  Provisions meeting non-current criteria             xxx
                                                     ────
Total non-current liabilities                         xxx
                                                     ────
TOTAL LIABILITIES                                     xxx
                                                     ════

NET ASSETS                                            xxx
                                                     ════

EQUITY
  Issued capital                                      xxx
  Retained earnings                                   xxx
  Reserves                                            xxx
                                                     ────
TOTAL EQUITY                                          xxx
                                                     ════
```

## Section 8 -- Bank Reconciliation Patterns

### Common Australian Bank Formats

**Common Australian Bank Formats**

| Bank | Export Format | Key Fields |
| --- | --- | --- |
| Commonwealth Bank (CBA) | CSV, OFX, QIF | Date, Amount, Description, Balance |
| ANZ | CSV, OFX | Date, Description, Amount, Type |
| Westpac | CSV, OFX, QIF | Date, Narration, Debit, Credit, Balance |
| NAB | CSV, OFX | Date, Narration, Amount, Type, Balance |
| Macquarie | CSV | Date, Description, Amount, Balance |
| Bendigo Bank | CSV, OFX | Date, Description, Debit, Credit, Balance |
| Up Bank / Neobanks | CSV | Date, Description, Amount, Category |

### Common Transaction Descriptions

**Common Transaction Descriptions**

| Pattern | Likely Classification |
| --- | --- |
| DIRECT CREDIT, BPAY CREDIT | Income — customer payment |
| EFTPOS, VISA PURCHASE, DEBIT CARD | Expense — check merchant |
| DIRECT DEBIT, D/D | Regular expense (insurance, subscription, utility) |
| BPAY | Expense — bill payment (utilities, ATO, rates) |
| TRANSFER, INT TFR | Internal transfer or payment — check counterparty |
| ATM WITHDRAWAL | Drawings (sole trader) or petty cash replenishment |
| INTEREST CHARGED | Interest expense (6440) |
| INTEREST PAID | Interest income (4200) |
| ATO PAYMENT, ATO IAS, ATO BAS | Tax payment — not a P&L expense |
| PAYROLL, WAGES | Staff costs (6100) |
| SUPER STREAM, SUPER CLEARING | Superannuation (6110) |
| XERO, STRIPE, SQUARE PAYOUT | Platform payout — match to invoices |

## Section 9 -- Micro-Entity / Small Business Simplifications

### Small Business Entity Concessions (turnover < $10m)

**Small Business Entity Concessions (turnover < $10m)**

| Concession | Detail |
| --- | --- |
| Simplified depreciation | Instant write-off < $20,000; pool balance at 15%/30% |
| Simplified trading stock | Eligible business may choose no stocktake if the reasonably estimated change is $5,000 or less |
| Prepaid expenses | Otherwise deductible expenditure: service period of 12 months or less, ending by the end of the following income year (ITAA 1936 s 82KZM). The separate under-$1,000 exclusion also applies; see Section 3. |
| Simpler BAS | Report only G1, 1A, 1B (no G2, G3, G10, G11) |
| Amendment period | Usually 2 years from notice of assessment for eligible taxpayers with simple affairs; 4-year cases, unlimited fraud/evasion amendments and other s 170 exceptions apply. An amended particular can have a refreshed period under s 170(3); unrelated particulars do not automatically reopen. |
| Cash accounting for GST | Report GST when paid/received, not invoiced |
| PAYG instalments | Option to pay quarterly amount the ATO calculates |

### Reporting Tiers

**Reporting Tiers**

| Tier | Who | Standards | Required Statements |
| --- | --- | --- | --- |
| Tier 1 (Full AASB / IFRS) | For-profit private entities with public accountability and a legislative standards obligation; also where a regulator requires Tier 1 | Full recognition + full disclosure | Applicable complete statement set + notes |
| Tier 2 (AASB 1060 Simplified) | Eligible entities without public accountability, including large proprietary companies, subject to regulator requirements; may elect Tier 1 | Full recognition, reduced disclosure | Applicable complete statement set + reduced notes |
| Special Purpose | Entities permitted to use this basis after checking legislation, constituting documents and other reporting obligations | Applicable requirements for that entity | Scope depends on the reporting obligation |
| No statutory reporting | Sole traders, small partnerships (non-company) | None mandated | Prepare for ATO/tax purposes only |

AASB 1053 paragraphs 11, 13 and 15 govern the tiers above. For periods beginning on or after 1 July 2021, the special-purpose change covered specified for-profit private entities (AASB 1057 paragraph 5):

- those required by legislation to comply with Australian Accounting Standards or accounting standards
- those required only by a constituting or other document to comply with Australian Accounting Standards, where the document was created or amended on or after 1 July 2021.

Check the reporting obligation and the compilation applicable to the period; size alone does not establish eligibility for special-purpose reporting.

### Large proprietary thresholds (reporting obligation, not tier selection)

- **Large Proprietary Thresholds** — Meet 2 of 3: Revenue ≥ $50m, assets ≥ $25m, employees ≥ 100.

## Section 10 -- Interaction with Tax Skills

### Income Tax Return

- Sole traders: business schedule in individual return (myTax or tax agent)
- Companies: Company Tax Return (form with labels mapped to financial statements)
- Tax rate: individuals at marginal rates; companies at 25% (base rate entity, turnover < $50m) or 30%
- Franking: company tax paid generates franking credits for shareholder dividends
- Losses: carried forward indefinitely, subject to continuity of ownership test (companies) or non-commercial loss rules (individuals)

### BAS / GST Return

**BAS / GST Return**

| BAS Label | Description | CoA Mapping |
| --- | --- | --- |
| G1 | Total sales (incl. GST-free and input taxed) | 4000–4500 |
| 1A | GST on sales | 2050 |
| 1B | GST on purchases (Input Tax Credits) | 1150 |
| W1 | Total salary/wages and other payments | 6100 |
| W2 | Amounts withheld from payments (PAYG-W) | 2100 |
| T1 | PAYG instalment income | 4000–4500 |
| T2 | PAYG instalment rate | Percentage; no nominal account |
| 5A | PAYG instalment payable (from T7, varied T9 or rate-method T11) | 2140 |

### Superannuation Guarantee

- Rate: 11.5% of ordinary time earnings for 2024-25; 12% from 1 Jul 2025
- Due: 28 days after end of quarter
- Nominal: 6110 (expense) / 2110 (payable)
- SG Charge: if late, lose deduction and pay additional penalties

### Fringe Benefits Tax (FBT)

- FBT year: 1 April – 31 March
- Rate: 47% (top marginal + Medicare levy)
- Common items: car fringe benefit, entertainment, loan fringe benefit
- Meals/entertainment: 50/50 method available — 50% deductible for income tax, 50% subject to FBT

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
