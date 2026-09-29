---
name: tanzania-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Tanzania VAT return. Standard rate 18% (16% reduced for non-VAT-registered B2C electronic payments from Sep 2025). EAC customs union but no common VAT. Withholding VAT 3% goods / 6% services from July 2025. ALWAYS read before handling Tanzania VAT work.
version: 2.0
jurisdiction: TZ
tax_year: 2025
last_updated: 2026-09-29
reviewed_by: Baraka Cassian
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tanzania VAT

## Tanzania VAT Return Skill v2.0

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Baraka Cassian** on 2026-06-12; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Tanzania |
| Standard rate | 18% (16% reduced for B2C electronic payments to unregistered persons, from Sep 2025) |
| Zero rate | 0% (exports, agricultural inputs, diplomatic, SEZ) |
| Filing portal | https://ots.tra.go.tz |
| Authority | Tanzania Revenue Authority (TRA) |
| Currency | TZS |
| Filing frequency | Monthly |
| Deadline | 20th of the following month, even when the 20th falls on a weekend or public holiday (s.66, as amended by Finance Act 2025) |
| Registration | TZS 200,000,000 annual taxable turnover (Mainland; VAT Act, Cap 148, s.28). Professional service providers (lawyers, accountants and the like) and government entities carrying on economic activities register whatever their turnover (s.28). A non-resident supplying electronic services to Mainland consumers registers under the simplified regime, with no threshold, and charges 18% on B2C supplies (VAT (Registration of Non-Resident Electronic Service Suppliers) Regulations) |
| Zanzibar (separate regime) | Zanzibar VAT Act, administered by the ZRA: 15% standard rate (18% for banking, postal, telecommunication, insurance and digital services); registration threshold TZS 100,000,000. This guide covers Mainland Tanzania |
| Withholding VAT | 3% goods / 6% services (from July 2025) |
| Primary legislation | VAT Act 2014 (Act No. 5) |
| EAC members | Kenya, Uganda, Rwanda, Burundi, South Sudan, DRC |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from CRDB, NMB (National Microfinance Bank), Stanbic TZ, Standard Chartered TZ, NBC, or any Tanzanian bank.

- **R-TZ-1 -- Mining** — Mining has specific provisions under Mining Act 2010. Escalate.  _(Mining Act 2010)_

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CRDB | EXCLUDE | Exempt financial |
| NMB, NATIONAL MICROFINANCE | EXCLUDE | Same |
| STANBIC TZ, NBC | EXCLUDE | Same |
| TRA, TANZANIA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT |  |
| NSSF, PPF | EXCLUDE | Social security |
| TANESCO | Domestic 18% | Electricity |
| DAWASA | Domestic 18% | Water |
| VODACOM TZ, AIRTEL TZ, TIGO, HALOTEL | Domestic 18% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 18% only where the buyer's exempt supplies are 10% or more of its total supplies | Non-resident; see Section 7 |

## Section 4 -- Worked examples

### Example 1 -- Standard sale

TZS 10M net. Output VAT = TZS 1.8M (18%).

### Example 2 -- EAC import

Goods from Kenya TZS 20M. VAT 18% at customs = TZS 3.6M. Recoverable. No intra-community mechanism.

## Section 5 -- Classification rules

- **Classification rules** — 18% standard (16% for B2C electronic payments to unregistered, from Sep 2025). 0% exports, agricultural inputs, diplomatic, SEZ. Exempt: unprocessed foodstuffs, financial, medical, education, residential rental, life insurance, public transport, agricultural equipment, water (public utilities), petroleum (fuel levy). Natural gas supplied for conversion to CNG for motor vehicles is exempt from 1 July 2025 to 30 June 2028 (Finance Act 2025).

## Section 6 -- VAT return form (ITX222.01.E)

Output: A1-A7 (18% sales, zero-rated, exempt, total, output VAT, adjustments, total output).

Input: B1-B7 (local purchases, imports, input local, input imports, total input, adjustments, net input).

Net: C1-C3 (net, credit b/f, net payable).

## Section 7 -- Reverse charge, withholding VAT, and imports

- **Reverse charge on imported services** — A registered person accounts for output VAT on services imported from a non-resident only where its exempt supplies are 10% or more of its total supplies; a fully taxable business does not self-assess. Where it applies, the self-assessed 18% is creditable only to the extent the partial-exemption rule in Section 8 allows, so the net cost is the share attributable to exempt supplies.  _(Value Added Tax Act, Cap 148, imported-services provisions and s.70)_
- **Withholding VAT (from July 2025)** — Designated agents (the Ministry of Finance, government institutions retaining own-source revenue and VAT-registered persons the Commissioner General appoints) withhold 3 percentage points of the 18% on goods (the supplier receives 15%) and 6 points on services (the supplier receives 12%); the agent remits by the 20th of the following month and issues a VAT Withholding Certificate, which the supplier needs to claim the withheld amount as a credit in its return.  _(Value Added Tax Act, Cap 148, as amended by Finance Act 2025)_
- **EAC imports** — VAT at border, no intra-community mechanism. Deferment of VAT on imported capital goods ceases from 30 June 2026 (Finance Act 2025 sunset).

## Section 8 -- Deductibility and blocked input

- **Blocked input tax** — No credit for entertainment, membership of sporting, social or recreational clubs, or spare parts and repair or maintenance of passenger vehicles; passenger vehicles of fewer than 13 seats other than taxis, hire cars and driving-instruction vehicles, private use and purchases for non-taxable supplies are likewise outside the credit.  _(Value Added Tax Act, Cap 148, s.68)_
- **Partial exemption** — Taxable supplies above 90% of total supplies: full input credit; below 10%: no credit; between 10% and 90%: apportion by the average method or direct attribution.  _(Value Added Tax Act, Cap 148, s.70)_
- **Time limits on input claims** — An input tax claim must be made within 6 months of the date of the fiscal receipt; VAT incurred in the 6 months before registration is claimable no later than the third VAT return after registration.  _(Value Added Tax Act, Cap 148, s.69 and the pre-registration provisions)_
- **Fiscal receipts** — A fiscal receipt is mandatory for every domestic supply, from an EFD/EFDMS, the Government e-Payment Gateway (GePG) or another system the Commissioner General approves, and an input claim on a domestic purchase without a valid fiscal receipt is not deductible. Input tax on imported goods is supported by the customs entry and the receipt for the VAT paid at the border, and self-assessed VAT on imported services by the return in which it was accounted for: both are input tax under the Act's definition and the fiscal-receipt rule does not reach them.  _(Value Added Tax Act, Cap 148, definition of input tax; Tax Administration (Electronic Fiscal Devices) Regulations)_
- **Deemed supplies** — Non-business use, gifts > TZS 100,000, cessation with stock.

## Section 9 -- Filing, deadlines, and penalties

- **Filing and penalties** — Monthly, 20th. Late filing: 1%/month (max 100%), min TZS 150K. Late payment: BoT rate + 5%, daily.
- **Refunds** — A remaining credit is claimable 6 months after the refund first became due, with every intervening return filed and an auditor's certificate of genuineness; a business in a consistent refund position (an exporter) may apply to lodge monthly.  _(Value Added Tax Act, Cap 148, ss.80–83)_

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge only if the buyer's exempt supplies are 10% or more of its total supplies; a fully taxable buyer accounts for nothing. Where it applies: output 18%, input credit per the Section 8 apportionment.
**EC2 -- Export to Kenya.** Zero-rated. Input recoverable.
**EC3 -- EAC import (Uganda).** VAT at customs. Recoverable.
**EC4 -- Mining.** Escalate.
**EC5 -- Deemed supply cessation.** 18% on market value.
**EC6 -- Tourism hotel.** May qualify for zero-rating if foreign currency. Reviewer flag.
**EC7 -- Credit note.** Adjust in A6.
**EC8 -- Bad debt.** 12 months + write-off.

**Test 1** -- TZS 10M sale. Output 1.8M.
**Test 2** -- TZS 5M furniture + 900K VAT. Recoverable.
**Test 3** -- Indian IT TZS 5M, fully taxable buyer. No reverse charge. (Buyer with exempt supplies at 10% or more of total: output 900K, input credit apportioned under s.70.)
**Test 4** -- Coffee export TZS 100M. Zero-rated.
**Test 5** -- Entertainment. Blocked.
**Test 6** -- Exempt financial TZS 50M. No output. Input not recoverable.
**Test 7** -- Kenya import TZS 20M. Customs VAT 3.6M. Recoverable.
**Test 8** -- Gift TZS 500K. Deemed supply. Output 90K.

Out of scope: CIT 30%, PAYE 0%-30%, SDL 3.5%, NSSF 10%+10%.

### Prohibitions

- NEVER treat EAC as intra-community
- NEVER ignore deemed supply rules
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
