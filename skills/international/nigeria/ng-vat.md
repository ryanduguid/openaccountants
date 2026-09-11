---
name: ng-vat
description: "Nigerian VAT working papers for periods from 1 January 2026 under the Nigeria Tax Act and Nigeria Tax Administration Act 2025. Covers the 7.5% standard rate, zero-rated and exempt supplies, small-business eligibility, professional-services exclusion, input credits, non-resident supplies, VAT withholding and separate remittance deadlines. Use for Nigeria VAT calculations, NRS returns, imported services, input VAT, supplier classification or monthly reconciliations. Includes invoice checks, worked examples and statutory penalty references. The generated fact block is retained as a historical record and contains superseded statements; use the operative sections below. Pending professional review."
jurisdiction: NG
tax_year: 2026
version: 2.1
last_updated: 2026-09-11
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nigeria VAT from 1 January 2026

> Pending professional review. The generated fact block below is an unchanged
> historical record, not the operative 2026 instructions. Its thresholds,
> zero-rate/exemption classifications, payment deadline, input-credit description
> and refund timing include incorrect or superseded statements. Use the sections
> after the block. Correct the underlying `skill_facts` before regenerating it;
> the historical review does not sign off these amendments.

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Omolola Fasasi** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### ng-vat

- **Standard VAT rate** — 7.5%  _(Finance Act 2019, effective 1 February 2020)_
- **Pre-2020 (superseded) VAT rate — no longer applicable** — 5%  _(Finance Act 2020)_
- **Zero rate — exports and specified supplies** — 0%  _(Finance Act 2021)_
- **Reverse-charge rate on imported services** — 7.5%  _(Section 10 VATA / NTA 2025)_
- **Compulsory VAT registration threshold (annual turnover)** — NGN 25,000,000  _(Finance Act 2019, effective 2020)_
- **Compulsory VAT registration threshold (annual turnover)** — NGN 100m  _(Nigeria Tax Act (NTA) 2025)_
- **Below-threshold exemption from VAT registration and filing** — Annual turnover ≤ NGN 25,000,000  _(Finance Act 2019, effective 2020)_
- **VAT return form** — VAT Form 002
- **Filing frequency** — Monthly (including nil returns)
- **VAT return filing and payment deadline** — 21st of the following month
- **TIN digit length** — 10 digits
- **Current unified statute** — Nigeria Tax Act (NTA) 2025, effective 1 January 2026  _(Nigeria Tax Act (NTA) 2025)_
- **Current unified statute** — Nigeria Tax Act (NTA) 2025, effective 1 January 2026  _(Nigeria Tax Act (NTA) 2025)_
- **VAT Form 002 Line 2 — Output VAT formula** — OUTPUT VAT =TOTAL(TAXABLE SALES * TAX RATE)
- **VAT Form 002 Line 6 — Net VAT payable formula** — NET VAT PAYABLE = TOTAL OUTPUT TAX -TOTAL INPUT TAX
- **Foreign currency invoice conversion rate** — CBN official rate on date of supply
- **HIGH single transaction** — NGN 10,000,000
- **Input VAT credit — unknown business-use portion (mixed personal/business)** — you can only claim input VAT credit for the business-use portion of mixed expense
- **Input VAT credit — supplier not displaying VRN on invoice** — No input credit (input claim not supported)
- **Zero-rate: exports of goods (documentation requirement — form)** — Form NXP, shipping documents and foreign exchange evidence required
- **Zero-rate: exported services — legislative basis** — Section 10A VATA; FIRS Information Circular 2021/02  _(Nigeria Tax Act (NTA) 2025)_
- **Zero-rate: humanitarian donor organisations — effective legislation** — All NGOs are expected to register for tax purposes, obtain tax identification number and file annual company income tax (CIT) with the nigerian revenue service (NRS)  _(Nigeria Tax Act (NTA) 2025)_
- **Reverse-charge: foreign digital services (B2B) — default classification** — 7.5% reverse-charge — buyer self-assesses under Section 10  _(Nigeria Tax Act (NTA) 2025)_
- **Reverse-charge: treatment for fully taxable business (net VAT effect)** — 0.075  _(Nigeria Tax Act (NTA) 2025)_
- **NRS cash refund processing time (in practice)** — 30 TO 90 DAYS  _(Nigeria Tax Act (NTA) 2025)_
- **VAT return excess input credit — treatment when refund not claimed** — Excess is automatically treated as an accumulated credit  _(Nigeria Tax Act (NTA) 2025)_
- **Processed/packaged food VAT treatment** — 7.5% (standard-rated)  _(Nigeria Tax Act (NTA) 2025)_
- **Stationery VAT treatment** — 7.5% (standard-rated)  _(Nigeria Tax Act (NTA) 2025)_
- **Commercial freight VAT treatment** — 7.5% (standard-rated)  _(Nigeria Tax Act (NTA) 2025)_
- **Pharmaceutical products — exemption condition** — Tax exempt  _(Nigeria Tax Act (NTA) 2025)_
- **Filing portal** — taxpayer self service (NSS) portal  _(Nigeria Tax Act (NTA) 2025)_
- **e-Invoice system** — Operated by the Nigeria Revenue Service (NRS)  _(Nigeria Tax Act (NTA) 2025)_

## Scope and sources

Use this guide for periods from 1 January 2026. Earlier periods require the law
then in force. The operative sources are the [Nigeria Tax Act 2025 (NTA)](https://nass.gov.ng/documents/download/11249),
especially sections 144–157 and 185–188, and the [Nigeria Tax Administration Act
2025 (NTAA)](https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf), especially section 22,
the small-business definition and the penalty provisions. The second link's
filename says Tax Act, but the document is the Administration Act.

This guide supports transaction classification and draft working papers. Confirm
the taxpayer's facts and applicable Nigeria Revenue Service (NRS) notices before
filing. Petroleum operations, free zones, restructurings and disputed refunds need
separate review. Income tax, withholding income tax and state consumption taxes
are separate taxes.

## Registration and filing status

Determine status before calculating VAT. Under NTAA section 22(4), the monthly
return obligation does not apply to a small business. Its definition requires
both annual gross turnover of **NGN 100,000,000 or less** and total fixed assets
of **NGN 250,000,000 or less**. A business providing professional services is
excluded from that definition, even below both amounts.

For the turnover test, section 22(7) excludes capital-asset supplies and supplies
made solely on selling all or part of the business or permanently ceasing trade.
A small business may opt out of the exemption from registration, charging VAT
and filing by written notice under section 22(5). On ceasing to qualify, it must
begin monthly returns under section 22(6). Check the separate petroleum-operations
exception in section 22(9). Do not substitute the NTA definition of a small
company, which serves a different tax.

Obtain the income period, activity, turnover calculation, fixed-asset total,
Tax ID, registration status and any opt-out notice. Missing turnover or asset
evidence leaves exemption eligibility unresolved. The former NGN 25 million
threshold does not establish a 2026 exemption.

## Classifying supplies

The standard rate is **7.5%** under NTA section 147. Establish that a supply is
within Nigeria under section 145, then check the specific exemption or zero-rate
provision. Use the supply description and supporting documents. A supplier name
or bank narration alone cannot establish tax treatment.

| Supply | Treatment from 1 January 2026 | Source and qualification |
| --- | --- | --- |
| Ordinary taxable consultancy, software or other services | 7.5% | Sections 144–147, subject to a specific relief |
| Basic food items | 0% | Section 186(a); use the definition in section 188. Processing or packaging alone does not establish standard rating |
| Medical and pharmaceutical products, including medicinal herbal products | 0% | Section 186(b) |
| Educational books and materials | 0% | Section 186(c) |
| Fertilisers | 0% | Section 186(d) |
| Locally produced agricultural chemicals, veterinary medicine and animal feeds | 0% | Section 186(e) |
| Medical services; tuition for nursery, primary, secondary or tertiary education | 0% | Section 186(j)–(k) |
| Exported non-oil goods, services and incorporeal property | 0% | Section 186(l)–(n); verify the statutory export definition and evidence of the foreign supply |
| Land or buildings, including an interest in them | Exempt | Section 185(1)(l); this includes commercial property. Separately supplied services need their own classification |
| Money, securities and interest in money | Exempt | Section 185(1)(m); this does not exempt every fee charged by a bank |
| Baby products; locally manufactured sanitary products | Exempt | Section 185(1)(d)–(e), subject to the exact product wording |
| Shared road passenger transport | Exempt | Section 185(1)(g); verify that the service meets the definition |
| Agricultural equipment | Exempt | Section 185(1)(h) |
| Qualifying diplomatic supplies | Exempt | Section 185(1)(j), subject to the diplomatic and non-commercial conditions |
| Qualifying donor-funded humanitarian goods | Exempt, with payment then refund | Section 185(1)(c) expressly requires VAT first to be paid and the donor to request a refund |

This table is not the complete statutory list. Check the remaining items in
sections 185–186, the definitions in section 188 and any applicable gazetted
order. Section 185(2) also addresses supplies in the Eleventh Schedule on which
VAT is not to be collected pending the specified ministerial order.

Zero-rated supplies are taxable supplies at 0%. Input tax attributable to them
can qualify for deduction. Exempt supplies do not support that deduction.

## Invoices, time and value

Use NTA section 146 to determine the tax point, including the first relevant
invoice, receipt, delivery or payment event and the specific rules for the type
of supply. Do not equate the bank posting date with the tax point without checking.

For a standard-rated amount explicitly exclusive of VAT:

```text
VAT = exclusive value × 7.5%
Invoice total = exclusive value + VAT
```

For a price explicitly inclusive of VAT:

```text
VAT = inclusive price × 7.5 / 107.5
Exclusive value = inclusive price / 1.075
```

Do not back-solve an invoice whose VAT basis is unknown. Apply section 148 for
valuation and non-cash consideration. Record the source and date of any foreign
currency conversion accepted for the transaction; do not invent an exchange rate.

Check the tax invoice against section 152, including the supplier's Tax ID,
sequential invoice number, supplier name, address and business registration number, date of supply,
purchaser name, gross
transaction amount and VAT amount and rate. Retain the invoice and evidence of
supply, business use and payment. Reconcile invoices to the sales and purchase
ledgers before comparing them with the bank statement.

## Non-resident suppliers and VAT withheld

Under NTA section 150, a non-resident making taxable supplies to Nigeria must
register and include VAT on its invoice. The Nigerian recipient generally
withholds and remits that VAT. Where NRS has appointed a supplier or intermediary
to collect VAT, check the section 150(3)–(4) rules before withholding again; the
recipient must account where the appointed collector fails to collect.

Section 154 also covers government and other appointed withholding persons, and
self-accounting where NRS directs a taxable recipient of a supply without VAT
to account for it. Record the legal basis for the recipient's obligation.

VAT withheld or self-accounted for under section 154 is remitted by the **14th
of the following month**, or another date prescribed by NRS, under subsection
(4). Keep this remittance separate from the ordinary monthly net-VAT calculation.
An eligible input credit does not cancel the duty to remit tax withheld.

Example: a taxable foreign service has an invoice value explicitly exclusive of
VAT of NGN 11,200,000. VAT is NGN 840,000. If the Nigerian customer must withhold
and remit it, show NGN 840,000 in that remittance schedule. Assess any input
deduction separately under section 155. Do not describe the transaction as having
zero cash VAT merely because an equal input deduction may be available.

For a domestic invoice subject to VAT withholding, reconcile the gross supply,
VAT, amount withheld, remittance evidence and cash received. Income-tax withholding
does not reduce the taxable value of the supply or replace VAT withholding.

## Input deductions and monthly computation

Under NTA section 155(4), a registered person may deduct input VAT on goods,
services and fixed assets to the extent used, consumed or supplied in making
taxable supplies. Attribute costs directly where possible and apportion mixed
taxable and non-taxable use on a supported basis. Private and exempt use does
not qualify.

The claim must be within five years after the end of the period in which the
input tax was incurred. Section 155(5) limits this deduction to supplies made
from the Act's commencement. Do not retrospectively claim pre-2026 service or
capital input VAT under the expanded 2026 rule.

```text
Output VAT = total VAT on standard-rated supplies and relevant adjustments
Eligible input VAT = supported VAT attributable to taxable supplies
Current-period net VAT = output VAT − eligible input VAT
```

Reconcile opening credits, prior remittances and adjustments separately to avoid
double counting. Under section 155, excess input tax is a credit against later
periods; a refund requires a request and supporting documents. Do not promise a
processing time or record an unapproved refund as cash received.

Example: a registered business has NGN 8,000,000 standard-rated sales exclusive
of VAT, NGN 2,000,000 zero-rated sales and NGN 1,000,000 exempt sales. Output VAT
is NGN 600,000. Supported input VAT of NGN 225,000 directly attributable to
taxable sales gives current-period net VAT of NGN 375,000. An additional
NGN 30,000 directly attributable to exempt sales is not deductible. Any VAT the
business withheld from suppliers still appears in its separate remittance schedule.

## Filing, penalties and records

NTAA section 22 generally requires a monthly return by the **21st of the following
month**, including a month with no economic activity. Apply the small-business
and other statutory exceptions before requiring a nil return. NTA section 155
requires ordinary net VAT payment on or before that return date. Check section
22(10) for real-time returns under the electronic fiscal system and verify the
applicable NRS implementation notice.

NTA section 157 and NTAA section 23 govern fiscalisation. Confirm the taxpayer's
assigned system, scope and commencement notice with NRS. This guide does not
establish a rollout deadline, API specification or current portal address.

Use the provision for the actual default:

| Default | Statutory amount | Source |
| --- | --- | --- |
| Failure to register when required | NGN 50,000 for the first month and NGN 25,000 for each subsequent month | NTAA section 100 |
| Failure to file a required return | NGN 100,000 for the first month and NGN 50,000 for each subsequent month | NTAA section 101 |
| Failure to deduct or collect tax when required | 40% of the amount not deducted, as stated in the provision | NTAA section 105 |

For failure to remit tax deducted or collected, apply NTAA section 107, including
its timing, 10% per annum penalty and interest at the prevailing CBN monetary
policy rate. Assess general late-payment provisions separately where applicable.
Do not substitute a penalty's trigger date for the section 154(4) remittance date.
Use the actual period of default and confirm any NRS relief before quantifying it.

Keep the return, invoice schedules, credit calculations, withholding evidence,
receipts and supporting records for the statutory retention period under NTAA
section 31, including the minimum of six years after the relevant year of assessment,
and any continuing audit or dispute needs.

## Working paper and final checks

Record the following in the draft return package:

1. Period, Tax ID, business activity, registration and small-business assessment.
2. Sales split into standard-rated, zero-rated, exempt and outside-scope amounts,
   with a section reference for each relief.
3. Tax points, exclusive values, output VAT and invoice adjustments.
4. Input VAT by taxable, exempt and private use; eligibility, apportionment and
   claim-period evidence; opening credits and refunds requested separately.
5. Supplier VAT withheld or self-accounted for, remittance deadlines and receipts.
6. Ledger and bank reconciliation, unexplained differences and missing documents.
7. Ordinary return and payment deadlines, any separate remittance deadline,
   required nil returns and applicable NRS notices.

Leave unresolved classifications and missing evidence visible. Have an ICAN/ANAN
accountant or CITN-registered tax practitioner review the draft before filing.

## Disclaimer

This guide provides general reference and calculation support. It does not
constitute tax, legal or financial advice. A qualified Nigerian professional
must review the taxpayer's facts, applicable law and final return before filing
or acting on the calculations.

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
