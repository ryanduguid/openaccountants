---
name: mauritius-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Mauritius VAT return. Standard rate 15%. Tourist refund scheme. Freeport treatment. GBL interactions. ALWAYS read before handling Mauritius VAT work.
version: 2.1
jurisdiction: MU
category: international
tax_year: 2025
last_updated: 2026-10-04
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mauritius VAT

## Mauritius VAT Return Skill v2.1

## Section 1 -- Quick reference

**Quick reference**  _(VAT Act 1998 (Act No. 2 of 1998))_

| Field | Value |
| --- | --- |
| Country | Mauritius |
| Standard rate | 15% |
| Zero rate | 0% (exports, basic foodstuffs, domestic electricity first 75 kWh, freeport supplies) |
| Filing portal | https://www.mra.mu |
| Authority | Mauritius Revenue Authority (MRA) |
| Currency | MUR |
| Filing frequency | Quarterly (standard); Monthly (large taxpayers) |
| Deadline | Last day of month following quarter (quarterly); 20th (monthly) |
| Registration | MUR 6,000,000 annual turnover |
| Tourist refund | MUR 2,300 minimum per invoice |
| Primary legislation | VAT Act 1998 (Act No. 2 of 1998) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

## Section 2 -- Required inputs and refusal catalogue

- **Minimum viable input** — Minimum viable -- bank statement. Acceptable from MCB (Mauritius Commercial Bank), SBM (State Bank of Mauritius), Absa Mauritius, AfrAsia Bank, Bank One, or any Mauritian bank.
- **R-MU-1 -- GBL company** — Trigger: Global Business Licence. Message: "GBL companies have specific VAT treatment. Escalate."

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MCB, MAURITIUS COMMERCIAL BANK | EXCLUDE | Exempt financial |
| SBM, STATE BANK OF MAURITIUS | EXCLUDE | Same |
| ABSA MU, AFRASIA | EXCLUDE | Same |
| BANK ONE | EXCLUDE | Same |
| MRA, MAURITIUS REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT |  |
| NPF, NSF, CSG | EXCLUDE | Social contributions |
| CEB | Domestic 15% | Electricity |
| CWA | Domestic 15% | Water |
| MAURITIUS TELECOM, EMTEL, MTML | Domestic 15% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 15% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Standard sale

MUR 1,000,000 net. Output VAT = MUR 150,000 (15%).

### Example 2 -- Tourist refund

Tourist purchases goods MUR 5,000. Issues Tax-Free Shopping receipt. Tourist claims refund at airport.

## Section 5 -- Classification rules

- **Classification of supplies** — 15% standard. 0% exports, basic foodstuffs (rice, flour, bread, cooking gas), domestic electricity (first 75 kWh), freeport supplies. Exempt: financial, medical, education, residential rental, public transport, postal, residential property sales (subsequent).  _(Value Added Tax Act 1998 (MRA consolidation to May 2026), ss 10 and 11, Fourth Schedule (rate), Fifth Schedule (zero-rated supplies) and First Schedule (exempt supplies) — https://www.mra.mu/download/VATAct.pdf)_
- **Tourist refund** — minimum MUR 2,300 per invoice. Claimed at airport. MUR

## Section 6 -- VAT return form

- **VAT return form boxes** — Output: Boxes 1-7 (standard, zero-rated, exempt, total, output VAT, adjustments, total output). Input: Boxes 8-14 (local purchases, imports, input local, input imports, capital goods, adjustments, net input). Net: Boxes 15-17 (net, credit b/f, net payable).

## Section 7 -- Reverse charge

- **Reverse charge** — Services received from abroad from a supplier who does not belong in Mauritius and is not VAT registered: the registered recipient accounts for output VAT at 15% as if it had made the supply and may claim the same amount as input tax under s 21, so the net effect is nil for a fully taxable business (s 14)  _(Value Added Tax Act 1998 (MRA consolidation to May 2026), s 14 — https://www.mra.mu/download/VATAct.pdf)_

## Section 8 -- Deductibility and blocked input

- **Blocked input and partial exemption** — Blocked (s 21(2)): motor cars and other vehicles for not more than 9 persons including the driver, motorcycles and mopeds for own use, with their parts, parking, maintenance and fuel; accommodation, catering, receptions and entertainment. Mixed use (s 21(3)): input tax on goods or services used for both taxable and exempt supplies is allowed in the proportion of taxable supplies to total turnover, and the Director-General may approve an alternative basis where that is not fair and reasonable  _(Value Added Tax Act 1998 (MRA consolidation to May 2026), s 21(2) and (3) — https://www.mra.mu/download/VATAct.pdf)_

## Section 9 -- Filing, deadlines, and penalties

- **Filing, deadlines, and penalties** — Monthly taxable periods where annual taxable turnover exceeds Rs 10 million, otherwise quarterly. Return and payment within 20 days after the end of the taxable period, or within one month where both are made electronically; May and November returns fall two working days before the end of June and December. Late filing: Rs 2,000 per month or part, capped at Rs 20,000 (Rs 5,000 for a small enterprise). Late payment: 10% penalty (2% for a small enterprise) plus interest at 1% per month or part  _(Value Added Tax Act 1998 (MRA consolidation to May 2026), s 2 (taxable period), Second Schedule (Rs 10 million), ss 22, 26, 27 and 27A — https://www.mra.mu/download/VATAct.pdf ; Value Added Tax Regulations 1998 (MRA consolidation), reg 3 — https://www.mra.mu/download/VATReg.pdf)_

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge 15%. Net zero.
**EC2 -- IT export.** Zero-rated. Input recoverable.
**EC3 -- Motor vehicle blocked.**
**EC4 -- Freeport supply.** Zero-rated with certificate. Verify.
**EC5 -- GBL company.** Escalate.
**EC6 -- Basic foodstuffs.** Rice/flour zero-rated.
**EC7 -- Bad debt.** 6+ months, written off.
**EC8 -- Residential first sale.** Standard-rated by developer. Subsequent exempt.

**Test 1** -- MUR 1M sale. Output 150K.
**Test 2** -- MUR 500K purchase + 75K VAT. Recoverable.
**Test 3** -- UK consulting MUR 2M. Output 300K, input 300K.
**Test 4** -- Textiles export MUR 10M. Zero-rated.
**Test 5** -- Entertainment. Blocked.
**Test 6** -- Bank interest MUR 50M. Exempt. Input not recoverable.

Out of scope: CIT 15%, PAYE progressive, NPF/NSF, CSG 3%+1.5%/3%.

### Prohibitions

- NEVER confuse tourist refund with standard refund
- NEVER allow recovery on blocked categories
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
