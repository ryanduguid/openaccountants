---
name: bahamas-vat
description: Use this skill to prepare, review or classify transactions for a Bahamas VAT return. Trigger on "Bahamas VAT", "DIR Bahamas" or "Department of Inland Revenue Bahamas". Load alongside vat-workflow-base v0.1 or later.
version: 2.2
jurisdiction: BS
category: international
tax_year: 2026
tax_year_notes: "VAT return deadlines, selected food supply rules, imported and exported services and withholding checked through 28 November 2026."
last_updated: 2026-11-28
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahamas VAT

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | The Bahamas (Commonwealth of The Bahamas) |
| Standard rate | 10% |
| Reduced rate | 5% on qualifying supplies and imports under the current Fourth Schedule |
| Zero rate | 0% on qualifying exports and international transport |
| Exempt | Qualifying financial services, residential rent, education, medical care, public transport and specified food supplies |
| Return form | VAT return in the prescribed form |
| Filing portal | [DIR VAT portal](https://vat.revenue.gov.bs), listed in the [DIR VAT FAQ](https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/) |
| Authority | Department of Inland Revenue (DIR) |
| Currency | BSD (Bahamian Dollar, pegged 1:1 to USD) |
| Tax period | Calendar month or a different period set by the Comptroller |
| Return and payment | Within 21 days after the period ends. Large taxpayer registrants have 14 days. |
| Registration threshold | BSD 100,000 for ordinary cases. Check the applicable test, special cases and the Comptroller's conditions for voluntary registration. |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

From 1 July 2023, a registrant classified as a large taxpayer files and pays within 14 days after each tax period. The definition includes turnover of BSD 5 million or more and any other applicable classification. File a return even when no VAT is payable for the period. Confirm the assigned tax period and any special rule. Check the separate requirement to file invoice and adjustment details electronically when annual turnover from taxable activity exceeds BSD 5 million. [VAT Act, ss 2, 19–21 and 47](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf), [Act 20 of 2023, ss 1–2 and 11](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2023/2023-0020A/2023-0020A.pdf)

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Confirm the applicable rate or exemption before classifying |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Confirm the supplier, recipient and service location before applying VAT |
| Unknown food classification | Confirm the tariff item, preparation, seller or importer status and transaction date |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | BSD 10,000 |
| HIGH tax-delta on a single default | BSD 500 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable input** — bank statement for the period. Acceptable from: CIBC FirstCaribbean, RBC Bahamas (Royal Bank), Scotiabank Bahamas, Commonwealth Bank, Fidelity Bank, or any other.  _(Section 2 — Required inputs and refusal catalogue)_

### Bahamas-specific refusal catalogue

- **R-BS-1 — Grand Bahama Freeport** — Trigger: client operates within Grand Bahama Port Authority area. Message: "Freeport operations under the Hawksbill Creek Agreement have special VAT provisions requiring specialist analysis. Please escalate."  _(R-BS-1)_
- **R-BS-2 — Investment fund structures** — Trigger: client is an investment fund. Message: "Investment fund VAT treatment requires specialist analysis. Please escalate."  _(R-BS-2)_

## Section 3 — Supplier pattern library

### 3.1 Bahamian banks (fees exempt — exclude)

**Bahamian banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CIBC FIRSTCARIBBEAN, CIBC FC | EXCLUDE for bank charges | Financial service, exempt |
| RBC BAHAMAS, ROYAL BANK | EXCLUDE for bank charges | Same |
| SCOTIABANK BS, COMMONWEALTH BANK | EXCLUDE for bank charges | Same |
| FIDELITY BANK | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Taxes and statutory charges

**Government pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DIR, DEPT INLAND REVENUE | EXCLUDE | Tax payment |
| CUSTOMS, BAHAMAS CUSTOMS | EXCLUDE | Duty (import VAT separate) |
| BUSINESS LICENCE, BL FEE | EXCLUDE | Government fee |
| NIB, NATIONAL INSURANCE | EXCLUDE | National insurance |

Classify a Government supply payment using its contract, invoice and VAT withholding evidence under Section 3.8. Use the customs declaration to identify import VAT separately from customs duties.

### 3.3 Utilities

**Utilities pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BPL, BAHAMAS POWER AND LIGHT | Domestic 10% | Electricity |
| WSC, WATER AND SEWERAGE | Domestic 10% | Water |
| BTC, BAHAMAS TELECOMMUNICATIONS | Domestic 10% | Telecoms |
| ALIV | Domestic 10% | Mobile |

### 3.4 Insurance (exempt — exclude)

**Insurance pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BAHAMAS FIRST, COLINA, J.S. JOHNSON | EXCLUDE | Exempt |
| SUMMIT INSURANCE | EXCLUDE | Same |

### 3.5 Imported and exported services

Record the contracting supplier, invoice entity, recipient, service, place of performance and use, VAT registration and dates of the invoice, payment and work. For an overseas service, check the place-of-supply rules and whether VAT is due on a taxable importation. Where the importer and recipient are different, they are jointly and severally liable for the tax. A local branch or affiliate is a separate person from its nonresident branch or home office for these rules. [VAT Act, ss 2, 33–34, 39 and 45](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf)

Section 45(2) calls for a return on completion of the service or entry of the people contracted to perform it. The payment period depends on the recipient. For a recipient outside the definition of a taxable person, payment is due within 7 calendar days of import. For an unregistered taxable person, use the date in the assessment notice. For a registrant, payment is due within 21 calendar days after the tax period in which the services were imported. Confirm any deferment and the applicable filing form. [VAT Act, ss 39 and 45](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf)

When evaluating an input deduction, check use in a taxable activity, the approved import evidence, payment of the VAT and relevant restrictions. For mixed-use, exempt or specified property work, review attribution and the relevant restrictions separately. [VAT Act, ss 48–50](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf), [Act 45 of 2025, s 12](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0045A/2025-0045A.pdf)

**Exported services**

Check the First Schedule category and its conditions. For the professional services in Part II item 9, verify the listed service and supplier qualifications and that the recipient uses the service or obtains its benefit or advantage outside The Bahamas under the place-of-supply rules. Keep evidence of the contract, recipient, service and use or benefit. [VAT Act, ss 33–34 and First Schedule Part II](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf), [Act 45 of 2025, s 20](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0045A/2025-0045A.pdf)

For an audit supplied from The Bahamas to a Bahamian international business company, record where and why the company uses the audit. The Comptroller's ruling treats an audit for a Bahamian regulator as standard-rated and an audit for a foreign regulator as zero-rated in the stated circumstances. Keep records from the recipient supporting foreign use and confirm the ruling applies to the facts. The ruling applies from 3 March 2023 until withdrawn. [DIR ruling VAT 2023-01, paras 1–4 and 8–9](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2023/12/VAT-Ruling-Zero-Rating-of-Professional-Services.pdf)

### 3.6 Tourism

**Tourism pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HOTEL, RESORT, ATLANTIS | Domestic 10% (output) | Tourism supply |
| Online booking platform | Verify the contracting entity, service and place of supply | See Section 3.5 for imported services |

### 3.7 Payroll and exclusions

**Payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES | EXCLUDE | Employee services to an employer under employment. [Value Added Tax Act, s 3(6), 1 July 2024 reprint](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf) |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| DIVIDEND | REVIEW | Verify the underlying payment and its VAT treatment before classifying |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

### 3.8 VAT withholding

Identify the applicable withholding authority for the payment. The 2022 rules for appointed agents commenced on 1 August 2022. They define prescribed payments for specified supplies to Ministries and Departments, including construction, certain materials or equipment, certain maintenance and commercial leases. The prescribed payment threshold is BSD 10,000. Rules 6–7 prescribe withholding of 40% of the VAT due irrespective of the supplier's registration status, subject to the payment hold in rule 7(2). If a prescribed payment reaches or exceeds the section 21(a) threshold of BSD 100,000, the agent must wait until the supplier is a VAT registrant and deduct 40% of the VAT due at payment. Confirm the current appointment and the practical interaction with the 2026 Government rule. [VAT Act, ss 21(a) and 23A](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf), [S.I. 74 of 2022, rr 1–2 and 6–7 and Schedule Part I](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2022/08/Extraordinary-Gazette-29th-July-2022.pdf)

For deductions under rule 6, rule 14 requires remittance within 12 calendar days after the end of the month of deduction. An agent withholding under section 23A(3) must give the supplier a certificate at payment. A supplier with a duty to account for VAT retains that duty under section 23A(5). Under rule 8, an unregistered supplier who is outside the definition of a taxable person and had VAT withheld may apply in writing to the Comptroller for a refund within 3 years of the agent's remittance. The claim is subject to assessment and any statutory offset. [VAT Act, ss 23A and 56](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf), [S.I. 74 of 2022, rr 8 and 14–15](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2022/08/Extraordinary-Gazette-29th-July-2022.pdf)

From 1 July 2026 a Government entity making a supply contract payment is a deemed withholding agent under section 23A(11)–(12) and withholds the full VAT payable for that contract. Apply that rate to payments covered by those subsections, which state no minimum payment amount. Confirm the administrative treatment where the 2022 rules also apply. Match the contract, invoice and withholding evidence. DIR publishes V26 versions of Form 73, the withholding certificate, and Form 74, the return. Confirm the current version and filing instructions for the agent and payment. [Act 19 of 2026, ss 1–2](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0019A/2026-0019A.pdf), [DIR VAT forms](https://inlandrevenue.finance.gov.bs/value-added-tax/forms/)

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 10%

**Input line:** `05.04.2026 ; NASSAU TRADING CO ; CREDIT ; Invoice BS-041 ; BSD 1,100`

**Reasoning:** Domestic. 10%. Net = BSD 1,000, VAT = BSD 100.

**Example 1 result table**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | NASSAU TRADING CO | +1,100 | +1,000 | 100 | 10% | Output | N | — |

### Example 2 — Exempt food purchase in April 2026

**Input line:** `10.04.2026 ; QUALIFYING FOOD STORE ; DEBIT ; Unprepared fresh beef ; BSD -100`

**Reasoning:** The food store imported fresh beef classified under Second Schedule Part III heading 02.01 and sold it unprepared. The purchase has no VAT charge or input VAT claim. [Act 4 of 2026, ss 1 and 3](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf)

**Example 2 result table**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | QUALIFYING FOOD STORE | -100 | -100 | 0 | Exempt | No input VAT | N | — |

### Example 3 — Export, zero-rated

**Input line:** `15.04.2026 ; US BUYER INC ; CREDIT ; Exported conch ; BSD 5,000`

**Example 3 result table**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | US BUYER INC | +5,000 | +5,000 | 0 | 0% | Zero-rated | N | — |

### Example 4 — Imported advisory service

A Bahamian individual outside the definition of a taxable person imports a standard-rated advisory service for personal use. The import and completion occur on the same date. The invoice value is BSD 1,000 before VAT. The tax is BSD 100 at the 10% standard rate, payable within 7 calendar days of the import. Check the prescribed return and retain the invoice and payment evidence. The individual has no input deduction for the private use. [VAT Act, ss 39, 42, 45 and 50](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf), [Act 3 of 2025, s 3](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0003A/2025-0003A.pdf), [Act 4 of 2026, s 2](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf)

### Example 5 — Bank charges, excluded

**Input line:** `30.04.2026 ; CIBC FIRSTCARIBBEAN ; DEBIT ; Monthly fee ; BSD -25`

**Example 5 result table**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30.04.2026 | CIBC FIRSTCARIBBEAN | -25 | — | — | — | — | N | "Exempt" |

### Example 6 — Government supply contract VAT withholding

A Government entity pays under a standard-rated supply contract after 1 July 2026. On a BSD 10,000 invoice before VAT, the VAT is BSD 1,000 at 10%. The entity withholds BSD 1,000 of the BSD 11,000 invoice total, paying the supplier BSD 10,000. Reconcile the BSD 1,000 withholding to the applicable remittance evidence. [Act 19 of 2026, s 2](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0019A/2026-0019A.pdf), [Act 3 of 2025, s 3](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0003A/2025-0003A.pdf), [Act 4 of 2026, s 2](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf)

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 10% — Default for most taxable supplies.

- **Standard rate** — 10%  _(5.1 Standard rate 10% — Default for most taxable supplies.)_

### 5.2 Reduced rate and exempt food

From 1 April 2026, the Second Schedule exempts the wholesale or retail supply of listed items sold unprepared by a qualifying food store and specified imports by a qualifying food store. Check the Second Schedule Part III tariff item, food-store definition and relevant conditions for the transaction. For transactions outside those provisions, select any applicable exemption or the rate under section 6, including the 5% rate for qualifying Fourth Schedule supplies and imports. Apply the law for the transaction date. [Act 3 of 2025, ss 1 and 3](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0003A/2025-0003A.pdf), [Act 45 of 2025, ss 1–2](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0045A/2025-0045A.pdf), [Act 4 of 2026, ss 1–4](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf)

### 5.3 Zero rate — Exports, international transport.

- **Zero rate** — 0% for exports, international transport.  _(5.3 Zero rate — Exports, international transport.)_

### 5.4 Exempt — Financial services, residential rent, education, medical, public transport.

- **Exempt categories** — Financial services, residential rent, education, medical, public transport.  _(5.4 Exempt)_

### 5.5 Input tax credit — Available on purchases for taxable supplies. Apportionment if mixed.

- **Input tax credit** — Available on purchases for taxable supplies. Apportionment if mixed.  _(5.5 Input tax credit)_

### 5.6 Blocked input — Entertainment, personal vehicles, personal consumption.

- **Blocked input** — Entertainment, personal vehicles, personal consumption.  _(5.6 Blocked input)_

### 5.7 Imported goods

Check the exemption and rate for the declared goods and import date under Section 5.2. For a taxable import, use the statutory import value, including relevant duties, levies and taxes other than VAT. File the customs declaration and pay any VAT due on entry under section 44. Retain the declaration and payment evidence. [VAT Act, ss 41–42 and 44](https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf)

### 5.8 Imported services

- **Imported services** — Verify the service, place of supply, recipient and VAT registration. Apply the import VAT payment window under Section 3.5. Check input VAT deductibility separately.

### 5.9 Income tax scope

Through 10 November 2026, Bahamian domestic personal income tax is inapplicable. The separate Domestic Minimum Top-Up Tax applies to Bahamian constituent entities of in-scope multinational groups. Determine VAT treatment under the VAT rules. [Bahamas–Japan MAP guidance, ‘Scope of the MAP “Limitations”’](https://cdn.bahamas.gov.bs/tenant/tenantministryoffinance/documents/All%20Documents/BAHAMAS-JAPANMAPGUIDANCEDOCUMENT-20240718120503.pdf) · [Domestic Minimum Top-Up Tax Act, 2024, ss 1 and 5](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/2024/2024-0058/2024-0058_1.pdf)

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Food classification

- **Food classification** — Ask for the tariff item, preparation, transaction date and qualifying food-store status. Apply the exemption or rate under Section 5.2.

### 6.2 Freeport operations — Default: refuse (R-BS-1).

- **Freeport operations default** — Default: refuse (R-BS-1).  _(6.2 Freeport operations)_

### 6.3 Tourism sector — Default: 10%. Question: "Hotel occupancy tax separate from VAT?"

- **Tourism sector default** — Default: 10%. Question: "Hotel occupancy tax separate from VAT?"  _(6.3 Tourism sector)_

### 6.4 Software subscriptions

- **Software subscriptions** — Use the contract and invoice to identify the supply and supplier and determine the applicable VAT treatment under Section 3.5.

### 6.5 Cash withdrawals — Default: exclude.

- **Cash withdrawals default** — Default: exclude.  _(6.5 Cash withdrawals)_

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Bahamas fields: Output 10%, Output 5%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT.

## Section 8 — Bank statement reading guide

CIBC FirstCaribbean and RBC exports CSV/PDF. BSD primary (= USD). Internal transfers: exclude. No foreign currency conversion needed for USD (BSD pegged 1:1).

## Section 9 — Onboarding fallback

### 9.1 TIN — "What is your DIR TIN?"

- **TIN question** — "What is your DIR TIN?"  _(9.1 TIN)_

### 9.2 Filing frequency and due date

- **Filing frequency and due date** — Ask for the assigned tax period, turnover and large-taxpayer classification. Apply the statutory deadline in Section 1.

### 9.3 Industry — "What does the business do?"

- **Industry question** — "What does the business do?"  _(9.3 Industry)_

### 9.4 Exports — "Do you export?"

- **Exports question** — "Do you export?"  _(9.4 Exports)_

### 9.5 Freeport — "Are you in Grand Bahama Freeport?" (If yes, R-BS-1 fires.)

- **Freeport question** — "Are you in Grand Bahama Freeport?" (If yes, R-BS-1 fires.)  _(9.5 Freeport)_

### 9.6 Credit brought forward — Always ask.

- **Credit brought forward** — Always ask.  _(9.6 Credit brought forward)_

## Section 10 — Reference material

### Sources

1. Value Added Tax Act 2014 (as amended). 2. DIR guidelines. 3. Rate history: 7.5% (2015), 12% (2018), 10% (2022), 5% reduced (2025).

### Known gaps

Confirm the actual tax period, any applicable special registration or reporting procedure and the precise tariff treatment of mixed or prepared food items. Freeport requires specialist review. For imported services and VAT withholding, confirm digital-service registration, the current agent directions, the interaction of the 2022 and 2026 rules and the live return and payment channels. Nonresident income tax and royalty obligations, treaties and group arrangements require separate evidence.

### Change log

- v2.2 (November 2026): Update imported and exported services, VAT withholding, return deadlines and the April 2026 food rules.
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
