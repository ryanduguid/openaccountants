---
name: uganda-vat
description: "Uganda VAT guide for the 2025 baseline, with changes to the registration threshold and withholding from 1 July 2026. Standard rate 18%. Pending local-accountant review."
version: 2.2
jurisdiction: UG
category: international
tax_year: 2025
last_updated: 2026-11-28
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uganda VAT

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Uganda |
| Standard rate | 18% |
| Zero rate | 0% (exports, drugs/medicines, educational materials, agricultural inputs) |
| Filing portal | https://efiling.ura.go.ug |
| Authority | Uganda Revenue Authority (URA) |
| Currency | UGX |
| Filing frequency | Monthly |
| Deadline | 15th of following month |
| Registration | In 2025-26, UGX 150 million annual threshold and UGX 37.5 million for the ordinary 3-calendar-month tests. From 1 July 2026, UGX 300 million and UGX 75 million respectively. See registration rules below. |
| Withholding VAT | Generally 6% of taxable value where withholding applies. From 1 July 2026, check the e-invoice or e-receipt exception. |
| Primary legislation | VAT Act, Cap. 344, as amended |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | Registration and withholding transition checked in November 2026. Other classifications remain pending review. |

For an unregistered person under the ordinary 3-calendar-month tests, apply within 20 days after a period in which VAT-exclusive taxable supplies exceeded the applicable amount, or at the start of a period if there are reasonable grounds to expect to exceed it. Check the separate s 7 provisions for other cases. URA says businesses below the updated threshold can apply to deregister, or remain voluntarily registered and meet their VAT obligations. [VAT Act, s 7](https://ulii.org/en/akn/ug/act/statute/1996/8/eng%402024-12-23#part_III__sec_7) · [VAT (Amendment) Act 2026, ss 1 and 3](https://ulii.org/en/akn/ug/act/2026/14/eng@2026-06-05) · [URA threshold notice](https://ura.go.ug/en/revised-value-added-tax-registration-threshold/)

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Stanbic Uganda, dfcu Bank, Standard Chartered UG, Centenary Bank, Bank of Baroda UG, or any Ugandan bank.

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STANBIC UG, STANBIC UGANDA | EXCLUDE | Exempt financial |
| DFCU, DFCU BANK | EXCLUDE | Same |
| STANDARD CHARTERED UG | EXCLUDE | Same |
| CENTENARY BANK | EXCLUDE | Same |
| URA, UGANDA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT |  |
| NSSF UGANDA | EXCLUDE | Social security |
| UMEME | Domestic 18% | Electricity |
| NWSC | Domestic 18% | Water |
| MTN UG, AIRTEL UG | Domestic 18% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 18% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Withholding VAT

A designated person pays a supplier on a transaction subject to withholding. Invoice UGX 50 million plus UGX 9 million VAT totals UGX 59 million. The designated person withholds UGX 3 million, or 6% of the taxable value, and pays UGX 56 million to the supplier. The supplier accounts for UGX 3 million as a payment in the subsequent VAT return. For payments from 1 July 2026, check the electronic document exception below.

### Example 2 -- Agricultural inputs zero-rated

Farm purchases fertilizer. Supplier charges 0%. Zero-rated supply.

## Section 5 -- Classification rules

18% standard. 0% exports, drugs/medicines, educational materials, agricultural inputs (seeds/fertilizers/pesticides/hoes), aircraft for international transport, diplomatic. Exempt: unprocessed foodstuffs, financial (interest/forex/life insurance), medical/dental, education, residential rental (unfurnished), social welfare, burial, postal, water (domestic public).

## Section 6 -- VAT return form

Output: 1a-1d, 2-4 (standard, zero-rated, exempt, total, output VAT, adjustments, total output).

Input: 5a-5c, 6-11 (local purchases, imports, imported services, input local, input imports, input imported services, total input, adjustments, allowable input).

Net: 12-15 (net, credit b/f, withholding VAT credits, net payable).

## Section 7 -- Withholding VAT and reverse charge

- **Designated withholding agents.** Where required, the designated person withholds 6% of the taxable value. The supplier accounts for that amount as a payment in the subsequent VAT return. From 1 July 2026, s 5(3) does not apply when a designated person paying for taxable supplies receives an e-invoice or e-receipt under s 92 of the Tax Procedures Code Act. Confirm designation, registration status and other s 5 exceptions. [VAT Act, s 5](https://ulii.org/en/akn/ug/act/statute/1996/8/eng%402024-12-23) · [VAT (Amendment) Act 2026, ss 1–2](https://ulii.org/en/akn/ug/act/2026/14/eng@2026-06-05)
- **Reverse charge for non-resident services** — Non-resident services. Self-assess 18%. Net zero.  _(VAT Act s.14)_
- **EAC intra-community mechanism** — EAC: no intra-community mechanism.

## Section 8 -- Deductibility and blocked input

- **Blocked input** — Blocked (s.21): entertainment, vehicles < 10 seats (unless taxi/hire/driving instruction), clubs, personal use, non-taxable supply purchases.  _(s.21)_
- **Deemed supplies** — Deemed supplies: non-business use, gifts > UGX 100,000, cessation with stock.
- **Bad debt relief period** — Bad debt: 3 years (long period).

## Section 9 -- Filing, deadlines, and penalties

- **Filing frequency and deadline** — Monthly; the return is filed and the VAT paid within 15 days after the end of the month, with EFRIS pre-filled returns.  _(Uganda Revenue Authority, Value Added Tax (VAT) page — https://ura.go.ug/en/value-added-tax-vat/ ; Uganda Revenue Authority, Returns page (filing deadlines) — https://ura.go.ug/en/domestic-taxes/returns/)_
- **Late filing penalty** — Late filing: UGX 200K/month or 2%/month, whichever greater.
- **Late payment penalty** — Late payment: 2%/month compounding.

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge 18%. Net zero.
**EC2. Withholding VAT.** Apply 6% of the taxable value when withholding is required. For payments from 1 July 2026, check whether a qualifying e-invoice or e-receipt removes the requirement.
**EC3 -- Coffee export.** Zero-rated. Input recoverable.
**EC4 -- Furnished rental.** May be 18%. Reviewer flag.
**EC5 -- EAC import (Kenya).** VAT at customs. Recoverable.
**EC6 -- Motor vehicle blocked.**
**EC7 -- Agricultural inputs.** Zero-rated.
**EC8 -- Bad debt.** 3-year period.

**Test 1** -- UGX 20M sale. Output 3.6M.
**Test 2** -- UGX 5M equipment + 900K VAT. Recoverable.
**Test 3** -- SA services UGX 10M. Output 1.8M, input 1.8M.
**Test 4** -- Fish export UGX 100M. Zero-rated.
**Test 5.** A designated person pays UGX 30 million plus UGX 5.4 million VAT on a supply subject to withholding. Withholding is UGX 1.8 million. For the same payment from 1 July 2026 with a qualifying e-invoice or e-receipt, expected withholding under s 5(3) is zero.
**Test 6** -- Entertainment. Blocked.
**Test 7** -- Exempt financial UGX 500M. No output. Input not recoverable.
**Test 8** -- Gift UGX 500K. Deemed supply. Output 90K.

Out of scope: CIT 30%, PAYE 0%-40%, NSSF 5%+5%, LST.

### Prohibitions

- NEVER confuse withholding VAT (6% of taxable value) with withholding income tax
- NEVER treat EAC as intra-community
- NEVER ignore withholding VAT credits
- NEVER compute numbers -- engine handles arithmetic

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
