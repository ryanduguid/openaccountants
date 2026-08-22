---
name: australia-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for an Australian GST return (Business Activity Statement / BAS) for any client. Trigger on phrases like "prepare BAS", "do the GST", "fill in BAS", "create the return", "GST return", "Activity Statement", or any request involving Australian GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill covers Australia only and covers both Simpler BAS and full BAS reporting. GST groups, margin scheme, partial exemption complex, and going concern are all in the refusal catalogue. ALWAYS read this skill before touching any GST-related work.
version: 2.1
jurisdiction: AU
tax_year: 2025
last_updated: 2026-08-20
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia GST

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Standard rate | 10% (single rate -- no reduced rates) |
| GST-free (zero rate equivalent) | 0% -- input tax credits retained (Division 38) |
| Input taxed (exempt equivalent) | No GST -- no input tax credits (Division 40) |
| Return form | BAS (Business Activity Statement) -- Simpler BAS or Full BAS |
| Filing portal | ATO Business Portal (https://bp.ato.gov.au) / myGov (https://my.gov.au) |
| Authority | Australian Taxation Office (ATO) |
| Currency | AUD only |
| Filing frequencies | Monthly (turnover > $20M); Quarterly (standard); Annual (voluntary, turnover < $75K) |
| Deadline | Monthly: 21st of following month; Quarterly: 28th of month after quarter; Annual: 28 February |
| Registration threshold | AUD $75,000 (general); AUD $150,000 (non-profit); $1 (taxi/rideshare) |
| Primary legislation | A New Tax System (Goods and Services Tax) Act 1999 (GST Act) |
| Supporting legislation | Taxation Administration Act 1953 (Schedule 1); GST Regulations 2019; LCT Act 1999; WET Act 1999 |
| Contributor | Open Accounting Skills Registry |
| Validation date | April 2026 |
| Skill version | 2.0 |

**Read this whole section before classifying anything.**

**Key BAS labels table**

| Label | Meaning |
| --- | --- |
| G1 | Total sales (GST-exclusive for taxable sales; include GST-free and input taxed) |
| G2 | Export sales (GST-free, Division 38-E) |
| G3 | Other GST-free sales (food, health, education -- Division 38-A to 38-D, 38-F+) |
| G4 | Input taxed sales (financial supplies, residential rent -- Division 40) |
| G5 | G2 + G3 + G4 (derived) |
| G6 | G1 minus G5 (derived -- total taxable sales, the base for output GST) |
| G7 | Adjustments on sales (bad debts, price changes -- Division 19) |
| G10 | Capital purchases (plant, equipment, vehicles -- GST-inclusive) |
| G11 | Non-capital purchases (operational expenses, stock -- GST-inclusive) |
| G12 | G10 + G11 (derived) |
| G13 | Purchases for making input taxed sales (no credit) |
| G14 | Purchases with no GST in the price (from unregistered, GST-free, wages) |
| G15 | Estimated purchases for private use (no credit) |
| G16 | G13 + G14 + G15 (derived) |
| G17 | G12 minus G16 (derived -- total creditable purchases) |
| G18 | Adjustments on purchases (Division 19, Division 129) |
| 1A | GST on sales (output GST) |
| 1B | GST on purchases (input tax credits) |

- **Simpler BAS reporting scope** — Simpler BAS (turnover < $10M, default since 1 July 2017): Report only G1, 1A, 1B. No need for G2-G18.
- **Full BAS reporting scope** — Full BAS: Report all G labels plus 1A, 1B, and PAYG/FBT labels as applicable.
- **GST calculation formulas** — GST = GST-inclusive price x 1/11 GST = GST-exclusive price x 10% GST-inclusive = GST-exclusive x 1.1 GST-exclusive = GST-inclusive / 1.1

**Conservative defaults -- Australian-specific**

| Ambiguity | Default |
| --- | --- |
| Unknown GST status of a sale | Taxable at 10% |
| Unknown GST status of a purchase | No input tax credit claimed |
| Unknown business-use proportion (vehicle, phone, home office) | 0% credit |
| Unknown whether food is basic or prepared | Taxable at 10% (prepared food) |
| Unknown counterparty registration status | Unregistered (no GST in price, G14) |
| Unknown SaaS billing entity location | Non-resident, reverse charge applies |
| Unknown insurance type (general vs life) | Input taxed (no credit) |
| Unknown property type (commercial vs residential) | Residential (input taxed, no credit) |
| Unknown whether transaction is in scope | In scope |
| Cash withdrawal purpose | Owner drawing, exclude |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | AUD $5,000 |
| HIGH tax-delta on a single conservative default | AUD $500 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net GST position | AUD $10,000 |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable, recommended, ideal inputs** — Minimum viable -- bank statement for the period in CSV, PDF, or pasted text. Must cover the full BAS period. Acceptable from any Australian business bank: CBA, Westpac, ANZ, NAB, Macquarie, Bendigo, Suncorp, Bank of Queensland, Up Bank, ING, Revolut AU, Wise, or any other. Recommended -- sales invoices for the period (especially for exports and GST-free supplies), purchase invoices for any input tax credit claim above AUD $500, the client's ABN in writing (11 digits), prior period BAS. Ideal -- complete accounting software export (Xero, MYOB, QuickBooks), tax invoice register, prior period BAS with any credit carried forward.
- **Refusal policy if minimum is missing** — SOFT WARN. If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This BAS was produced from bank statement alone. The reviewer must verify, before lodging, that input tax credit claims above AUD $500 are supported by valid tax invoices and that all GST-free and reverse-charge classifications match the supplier's invoice."

### Australia-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation. Refusal is a safety mechanism.

- **R-AU-1 -- Partial exemption complex** — Trigger: client makes both taxable/GST-free supplies AND input taxed supplies, and the input taxed proportion is not de minimis (financial acquisitions threshold exceeded). Message: "You make both taxable and input taxed supplies. Your input tax credits must be apportioned under Division 11 (s 11-30), which requires determining the extent of creditable purpose for each acquisition. This cannot be completed without a documented apportionment methodology confirmed by a registered tax agent. Please escalate."  _(Division 11, s 11-30)_
- **R-AU-2 -- GST groups** — Trigger: client is part of a GST group under Division 48 or asks about group registration. Message: "GST groups under Division 48 require consolidation across the group with a representative member lodging a single BAS. Intra-group supplies are disregarded. This is out of scope for this skill. Please use a registered tax agent."  _(Division 48)_
- **R-AU-3 -- Margin scheme** — Trigger: client sells property using the margin scheme under Division 75. Message: "Margin scheme transactions under Division 75 require computing GST on the margin (sale price minus acquisition cost) and confirming eligibility based on the original acquisition. This is too fact-sensitive for this skill. Please use a registered tax agent."  _(Division 75)_
- **R-AU-4 -- Going concern** — Trigger: client sells or buys a business as a going concern under s 38-325. Message: "Going concern supplies under s 38-325 require verification that all three conditions are met (going concern, both parties registered, written agreement). Incorrect classification results in either 10% GST on the full sale price or a missed GST-free entitlement. Please use a registered tax agent to confirm eligibility before proceeding."  _(s 38-325)_
- **R-AU-5 -- Financial supply complex (financial institution)** — Trigger: client is a financial institution (bank, insurer, super fund) whose primary supplies are input taxed financial supplies, or client asks about Reduced Input Tax Credits (RITC). Message: "Financial institutions making predominantly input taxed supplies require specialist apportionment, RITC calculations (75%/55%), and the financial acquisitions threshold test. This is out of scope. Please use a registered tax agent specialising in financial services GST."  _(RITC 75%/55%)_

## Section 3 -- Supplier pattern library (Australian vendors)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules -- the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Australian banks (fees input taxed -- exclude)

**Australian banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CBA, COMMONWEALTH BANK, COMMBANK, NETBANK | EXCLUDE for bank fees/charges | Financial supply, input taxed. No GST on bank fees. |
| WESTPAC, ST GEORGE, BANK OF MELBOURNE, BANKSA | EXCLUDE for bank fees/charges | Same -- all Westpac group |
| ANZ, ANZ BANK | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| NAB, NATIONAL AUSTRALIA BANK | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| MACQUARIE, MACQUARIE BANK | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| BENDIGO BANK, ADELAIDE BANK | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| SUNCORP BANK, BOQ, BANK OF QUEENSLAND | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| UP BANK, ING DIRECT, ING AUSTRALIA | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| REVOLUT, WISE (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, INT PAID, INT RECEIVED | EXCLUDE | Interest income/expense, input taxed or out of scope |
| LOAN, HOME LOAN, PERSONAL LOAN, MORTGAGE | EXCLUDE | Loan principal movement, out of scope |

### 3.2 ATO and government (exclude entirely)

**ATO and government table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO, AUSTRALIAN TAXATION OFFICE | EXCLUDE | Tax payment (GST, PAYG, income tax), not a supply |
| ATO BAS, BAS PAYMENT | EXCLUDE | GST remittance |
| ASIC, AUSTRALIAN SECURITIES | EXCLUDE | Regulatory fee -- note: ASIC annual review fee has no GST |
| COUNCIL RATES, CITY OF, SHIRE OF | EXCLUDE | Local government rates, not a supply |
| STATE REVENUE, OSR, REVENUE NSW, SRO VIC | EXCLUDE | State tax (payroll tax, stamp duty, land tax) |
| CENTRELINK, SERVICES AUSTRALIA | EXCLUDE | Government benefit, not a supply |
| DEPARTMENT OF, DEPT OF | EXCLUDE | Government fee, sovereign act |
| WORKCOVER, WORKSAFE, ICARE | Domestic 10% | Workers compensation premium -- taxable supply, GST claimable |

### 3.3 Australian utilities (taxable 10%)

**Australian utilities table**

| Pattern | Treatment | BAS Label | Notes |
| --- | --- | --- | --- |
| ORIGIN ENERGY, ORIGIN | Domestic 10% | G11 | Electricity, gas -- overhead |
| AGL, AGL ENERGY | Domestic 10% | G11 | Electricity, gas -- overhead |
| ENERGY AUSTRALIA, ENERGYAUST | Domestic 10% | G11 | Electricity, gas -- overhead |
| TELSTRA, TELSTRA CORP | Domestic 10% | G11 | Telecommunications -- overhead |
| OPTUS, SINGTEL OPTUS | Domestic 10% | G11 | Telecommunications -- overhead |
| TPG, TPG TELECOM, VODAFONE AU, IINET | Domestic 10% | G11 | Telecommunications/broadband -- overhead |
| NBN CO, NBN | Domestic 10% | G11 | National Broadband Network -- overhead |
| ALINTA ENERGY, RED ENERGY, SIMPLY ENERGY | Domestic 10% | G11 | Electricity, gas -- overhead |
| SYDNEY WATER, MELBOURNE WATER, SA WATER | Domestic 10% | G11 | Water/sewerage -- overhead (some water supply is GST-free but metered charges are taxable) |

### 3.4 Australian insurance (mixed treatment)

**Australian insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| QBE, QBE INSURANCE | Domestic 10% | General insurance -- taxable, GST claimable |
| SUNCORP INSURANCE, GIO, AAMI | Domestic 10% | General insurance -- taxable |
| NRMA INSURANCE, NRMA | Domestic 10% | General insurance -- taxable |
| ALLIANZ AUSTRALIA | Domestic 10% | General insurance -- taxable |
| CGU, ZURICH AUSTRALIA | Domestic 10% | General insurance -- taxable |
| AMP LIFE, MLC LIFE, TAL LIFE | EXCLUDE | Life insurance -- input taxed, Division 40 |
| HEALTH INSURANCE, MEDIBANK, BUPA, HCF, NIB | EXCLUDE | Private health insurance -- input taxed financial supply |
| WORKCOVER, WORKSAFE, ICARE | Domestic 10% | Workers comp premium is taxable at 10% |

### 3.5 Australian transport (taxable 10%)

**Australian transport table**

| Pattern | Treatment | BAS Label | Notes |
| --- | --- | --- | --- |
| UBER AU, UBER AUSTRALIA, UBER *AU | Domestic 10% | G11 | Rideshare -- taxable. Driver must be GST-registered regardless of turnover. |
| DIDI, DIDI AU | Domestic 10% | G11 | Rideshare -- taxable |
| 13CABS, SILVER TOP, TAXI | Domestic 10% | G11 | Taxi -- taxable (mandatory GST registration) |
| SYDNEY TRAINS, TRANSPORT NSW, OPAL | Domestic 10% | G11 | Public transport -- taxable at 10% (Australia does not zero-rate public transport) |
| METRO CARDS MELBOURNE, MYKI, PTV | Domestic 10% | G11 | Public transport -- taxable at 10% |
| TRANSLINK, GO CARD | Domestic 10% | G11 | QLD public transport -- taxable |
| QANTAS, QANTAS AIRWAYS (domestic) | Domestic 10% | G11 | Domestic flights -- taxable at 10% |
| VIRGIN AUSTRALIA (domestic) | Domestic 10% | G11 | Domestic flights -- taxable |
| JETSTAR (domestic) | Domestic 10% | G11 | Domestic flights -- taxable |
| QANTAS (international), VIRGIN (international) | GST-free | G14 | International flights -- GST-free export (Division 38-E). Check ticket destination. |
| TOLL, LINKT, TRANSURBAN, CITYLINK, EASTLINK | Domestic 10% | G11 | Toll road charges -- taxable |
