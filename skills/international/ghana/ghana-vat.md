---
name: ghana-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Ghana VAT return. VAT 15% + NHIL 2.5% + GETFund 2.5% = 20% effective. Act 1151 effective 1 Jan 2026 recouples levies. Flat rate scheme abolished. Withholding VAT at 7%. ALWAYS read before handling Ghana VAT work.
version: 2.2
jurisdiction: GH
category: international
tax_year: 2026
last_updated: 2026-10-06
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana VAT

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Ghana |
| VAT | 15% |
| NHIL | 2.5% |
| GETFund | 2.5% |
| Effective total | 20% |
| COVID-19 HRL | ABOLISHED |
| Flat Rate Scheme | ABOLISHED (Act 1151) |
| Zero rate | 0% (exports, Free Zones supplies) |
| Filing portal | https://taxpayersportal.ghana.gov.gh |
| Authority | Ghana Revenue Authority (GRA) |
| Currency | GHS (Ghana Cedi) |
| Filing frequency | Monthly |
| Deadline | Last working day of following month |
| Registration | Goods: taxable supplies above GHS 750,000 in 12 months (or GHS 187,500 in 3 months with the 12-month total expected above GHS 750,000); services: within 30 days of starting, whatever the turnover (Act 1151, s 6) |
| Withholding VAT | 7% of the taxable value of standard-rated supplies (Act 1151, s 56) |
| Primary legislation | VAT Act 2025 (Act 1151) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | October 2026 |

**Key change under Act 1151:** NHIL and GETFund recoupled -- now recoverable as input. COVID HRL abolished. Flat rate abolished.

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from GCB (Ghana Commercial Bank), Ecobank Ghana, Stanbic GH, Standard Chartered GH, Fidelity Bank GH, or any Ghanaian bank.

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GCB, GHANA COMMERCIAL BANK | EXCLUDE | Exempt financial |
| ECOBANK GH, ECOBANK GHANA | EXCLUDE | Same |
| STANBIC GH, STANDARD CHARTERED GH | EXCLUDE | Same |
| FIDELITY BANK GH | EXCLUDE | Same |
| GRA, GHANA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT |  |
| SSNIT | EXCLUDE | Social security |
| ECG, VRA | Domestic 20% | Electricity |
| GHANA WATER | Domestic 20% | Water |
| MTN GH, VODAFONE GH, AIRTEL-TIGO | Domestic 20% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 20% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Standard sale with levies

GHS 10,000 net. VAT GHS 1,500 + NHIL GHS 250 + GETFund GHS 250 = total GHS 2,000 (20%).

### Example 2 -- Withholding VAT

Government ministry pays supplier. Invoice GHS 20K + VAT 3K + NHIL 500 + GETFund 500 = GHS 24K. Withholding = 7% of the GHS 20K taxable value = GHS 1,400. Supplier receives GHS 22,600 and a Withholding VAT Credit Certificate, and claims the GHS 1,400 credit (Box 20).

## Section 5 -- Classification rules

- **Levy stacking on same base** — 15% VAT + 2.5% NHIL + 2.5% GETFund on same base. Under Act 1151, all three recoverable as input.  _(Act 1151)_
- **Zero rate categories** — 0% (exports, Free Zones)  _(Act 1151)_
- **Exempt categories** — Exempt: financial (margin-based), residential rental, medical, education, unprocessed foodstuffs, agricultural inputs, petroleum (separate levies).  _(Act 1151)_

## Section 6 -- VAT return form

**VAT return form boxes**

| Section | Boxes | Description |
| --- | --- | --- |
| Output | 1-8 | standard, zero-rated, exempt, total, output VAT, NHIL, GETFund, total output |
| Input | 10-15 | local purchases, imports, total input VAT 15%, capital goods, overheads, resale |
| Net | 16-21 | net VAT, net NHIL, net GETFund, credit b/f, withholding credits, net payable |

## Section 7 -- Reverse charge and withholding VAT

- **Reverse charge on non-resident services** — Reverse charge: non-resident services. Self-assess VAT 15% + NHIL 2.5% + GETFund 2.5%. Under Act 1151, all recoverable. Net zero.  _(Act 1151)_
- **Withholding VAT rate** — 7% of the taxable output value of standard-rated supplies, withheld by an appointed VAT withholding agent at the time of payment, with a Withholding VAT Credit Certificate issued to the supplier; the agent files and pays by the 15th of the following month, and a failure to withhold and remit costs the tax plus a 30% penalty. GRA's VAT Withholding page, written before the 2026 reform, describes the base as the taxable value inclusive of NHIL and GETFund; confirm the base for 2026 supplies with GRA  _(Value Added Tax Act, 2025 (Act 1151), ss 55 to 57 — https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf ; GRA, VAT Withholding — https://gra.gov.gh/domestic-tax/tax-types/vat-withholding/)_

## Section 8 -- Deductibility and blocked input

- **Blocked input items** — No input tax on motor vehicles or vehicle spare parts unless the business deals in or hires motor vehicles or sells spare parts; on entertainment, including restaurant, meals and hotel expenses, unless the business provides entertainment; or on club, association or society subscriptions of a sporting, social or recreational nature. Mixed business and private use is restricted to the business part  _(Value Added Tax Act, 2025 (Act 1151), s 50 — https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf)_
- **NHIL/GETFund recoverability under Act 1151** — Under Act 1151: NHIL and GETFund on inputs ARE recoverable.  _(Act 1151)_
- **Partial exemption** — Input tax directly attributable to taxable supplies is deductible; unattributable input tax is apportioned by the ratio of taxable to total supplies under the Fifth Schedule formula. Below 5% taxable supplies no input tax is deductible for the period; above 95% all of it is  _(Value Added Tax Act, 2025 (Act 1151), s 52 — https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf)_

## Section 9 -- Filing, deadlines, and penalties

- **Filing frequency and deadline** — Monthly. Return due by the last working day of the following month, whether or not tax is payable; withholding VAT remittance by the 15th of the following month  _(Value Added Tax Act, 2025 (Act 1151), ss 57(2) and 59(5) — https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf)_
- **Late filing penalty** — GHS 500 plus GHS 10 for each day the failure continues  _(GRA, VAT Withholding — https://gra.gov.gh/domestic-tax/tax-types/vat-withholding/)_
- **Late payment penalty** — Interest at 125% of the Bank of Ghana monetary policy rate, compounded monthly, on the amount outstanding  _(GRA, VAT Withholding — https://gra.gov.gh/domestic-tax/tax-types/vat-withholding/)_

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge all three components. Net zero under Act 1151.
**EC2 -- Former flat rate business.** Now standard 15% + levies.
**EC3 -- Withholding VAT.** 7% of the taxable value of the supply (s 56), not 7% of the VAT.
**EC4 -- Cocoa export.** Zero-rated. All input recoverable. Excess credit from exports is refundable where exports exceed 25% of total supplies for the period and the export proceeds have been repatriated (s 53(1)(b)); otherwise it is carried as a credit.
**EC5 -- Free Zone supply.** Zero-rated with valid permit.
**EC6 -- Bad debt.** Deduction due when the debt is written off in the accounts and recovery action has proved futile (s 47); the Act sets no fixed waiting period.
**EC7 -- Motor vehicle.** Blocked unless the business deals in or hires motor vehicles (s 50(1)).

**Test 1** -- GHS 10K sale. VAT 1.5K, NHIL 250, GETFund 250. Total 2K.
**Test 2** -- Local purchase GHS 2K + VAT 300 + NHIL 50 + GETFund 50. All recoverable under Act 1151.
**Test 3** -- UK services GHS 5K. Self-assess 750+125+125. Claim all. Net zero.
**Test 4** -- Export GHS 50K. Zero-rated.
**Test 5** -- Flat rate transition. Now standard regime.
**Test 6** -- Govt pays GHS 20K + VAT 3K. Withholding 7% of 20K = 1,400.
**Test 7** -- Entertainment. All blocked.

Out of scope: CIT 25%, PAYE progressive, SSNIT 13% employer + 5.5% employee, CST 9%.

### Prohibitions

- NEVER apply flat rate scheme -- abolished under Act 1151
- NEVER ignore withholding VAT credits
- NEVER compute withholding VAT as 7% of the VAT amount -- it is 7% of the taxable value (s 56)
- NEVER compute numbers -- engine handles arithmetic

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
