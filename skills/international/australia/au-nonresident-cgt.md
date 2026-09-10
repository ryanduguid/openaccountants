---
name: au-nonresident-cgt
description: "Use this skill for any non-resident selling Australian assets. Trigger on: \"non-resident CGT Australia\", \"TAP test Australia\", \"taxable Australian property\", \"FRCGW\", \"foreign resident capital gains withholding\", \"15% withholding Australia\", \"12.5% withholding Australia\", \"clearance certificate ATO\", \"sell Australian shares non-resident\", \"sell Australian property non-resident\", \"Australian CGT non-resident seller\", \"no CGT discount non-resident Australia\". Covers the TAP test, individual marginal rates, FRCGW withholding (15%, no threshold, from 1 January 2025), clearance certificates. For Australian residents see au-capital-gains."
version: 1.2
jurisdiction: AU
tax_year: 2025
last_updated: 2026-09-10
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Nonresident Cgt

## Section 1 — Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Applies to | Non-residents of Australia disposing of Australian assets |
| CGT rate (non-resident individual) | Net capital gain enters taxable income; apply graduated non-resident individual rates |
| Key test | Taxable Australian Property (TAP) test |
| Withholding | 15% of gross proceeds on all TAP transactions, no minimum value (contracts entered into on or after 1 January 2025). Contracts before that date: 12.5% on property valued at AUD $750,000 or more |
| Primary legislation | ITAA 1997 Div 855; TAA 1953 Sch 1 Subdiv 14-D |
| Tax authority | ATO (ato.gov.au) |
| Verified by | Pending — Australian CPA/CA sign-off required |

## Section 2 — The Core Rule

Non-residents are only subject to Australian CGT on **Taxable Australian Property (TAP)**. Non-TAP assets sold by non-residents: **no Australian CGT**.

## Section 3 — The TAP Test: What Qualifies as TAP

**TAP test asset types table**

| Asset type | TAP? |
| --- | --- |
| Australian real property (land, buildings) | **Always TAP** |
| Mining, quarrying, prospecting rights in Australia | **Always TAP** |
| Shares in a company | Indirect real property interest only if both the principal asset test and non-portfolio interest test pass |
| Units in a trust | Indirect real property interest only if both the principal asset test and non-portfolio interest test pass |
| Options/rights to acquire any of the above | TAP |
| Assets used in Australian permanent establishment of a non-resident | TAP |
| Shares in an Australian company where assets are predominantly operating business, IP, goodwill, cash | **NOT TAP** |
| Portfolio interests (listed or unlisted) | Generally not indirect real property interests if the non-portfolio test fails; check associates, holding history and other TAP categories |

- **Indirect Australian real property interests:** Both tests must pass. The principal asset test compares Australian real property assets with other assets by market value. The non-portfolio test requires at least 10% direct interests including associates, at the event or throughout a 12-month period in the preceding 24 months. Check both tests for company shares and trust interests, listed or unlisted. A 5% unlisted holding with no associate interests, no qualifying earlier holding and no other TAP basis fails this route. (ITAA 1997 ss 855-25, 855-30; Library, Tax/Capital Gains Tax (CGT).)

## Section 4 — CGT Rate for Non-Residents

**CGT rate for non-residents table**

| Item | Non-resident treatment |
| --- | --- |
| CGT rate | For a full-year prescribed non-resident individual from 1 July 2024: 30% on income to $135,000; 37% on the next $55,000; 45% above $190,000. Companies use their applicable company rate |
| General discount | Preserve qualifying resident-period entitlement and apply the separate pre-8 May 2012 rules; obtain the full acquisition and residency history |
| SBCGT concessions | Available if all basic conditions met (including active asset test) |
| Main residence exemption | Generally not available to non-residents (unless Australian citizen/PR in specific circumstances) |
| Cost base calculation | Same as residents |

The Library's Michael example states a 42.67% discount alongside 50% x 884/1,036 qualifying days. Its stated percentage gives a $106,675 discount and $143,325 net gain on $250,000. The displayed fraction does not round to 42.67%, so confirm the day-count calculation before applying it to a return. Preserve the qualifying resident-period entitlement. (Library, Tax/Capital Gains Tax (CGT), discount apportionment.)

## Section 5 — Foreign Resident Capital Gains Withholding (FRCGW)

- **FRCGW obligation** — When a non-resident sells TAP, the buyer is required to withhold and remit to the ATO. For contracts entered into on or after 1 January 2025 the rate is 15% of gross proceeds and the AUD $750,000 threshold is removed, so it applies to every disposal regardless of value. For contracts entered into between 1 July 2017 and 31 December 2024, the rate is 12.5% and applies only where the property is valued at AUD $750,000 or more.
- **FRCGW nature** — This is a payment on account (not a final tax). Actual tax liability is computed in the non-resident's Australian tax return.

**FRCGW threshold table**

| FRCGW threshold | None for contracts from 1 January 2025 (was AUD $750,000 for contracts to 31 December 2024) |
| --- | --- |
| Withholding rate | 15% of gross proceeds from 1 January 2025 (12.5% for contracts to 31 December 2024) |
| Who withholds | The buyer (purchaser) |
| Remittance deadline | Day of settlement |

**Example:** A full-year prescribed non-resident individual sells a TAP interest for AUD $10 million after 1 January 2025. Assume the transaction attracts 15% withholding, the final net capital gain after losses and any available discount is $8 million, there is no other taxable income, and no offsets apply. Tax = $135,000 x 30% + $55,000 x 37% + $7,810,000 x 45% = $3,575,350. After the $1.5 million withholding credit, the balance is $2,075,350. At $200,000 taxable income, the same rate table gives $65,350.

## Section 6 — Clearance Certificate

- **Clearance certificate for resident sellers** — If the seller is an Australian resident (not a foreign resident), the seller can apply for a clearance certificate from the ATO to confirm residency, relieving the buyer of the withholding obligation. Because the $750,000 threshold was removed from 1 January 2025, an Australian resident vendor now needs a clearance certificate for every property contract, whatever the price.
- **Variation for non-resident sellers** — If the seller IS a non-resident but believes no tax is payable (e.g. asset is not TAP, or gain is nil due to losses), the seller can apply for a variation to reduce the withholding amount.

Applications: via ATO online portal (myGov / Tax Agent portal). Processing time: 14-28 days typically.

## Section 7 — Filing Obligations for Non-Residents

- **Filing requirement** — A non-resident who sells TAP must lodge an Australian non-resident individual tax return for the year of disposal (even if no tax is payable after losses/concessions). Due date: 31 October following the end of the financial year (or later with a tax agent).
- **TFN requirement** — Australian Tax File Number (TFN) is required. Non-residents can apply via ATO.

## Section 8 — Interaction with Tax Treaties

- **DTA coverage and Article 13** — Australia has double tax agreements (DTAs) with 45+ countries. Article 13 of most DTAs follows the OECD Model — gains on shares may be taxed by the country of residence of the seller UNLESS the shares derive principally from Australian real property (aligns with the TAP domestic test).
- **Treaty outcome mirrors domestic TAP rules** — Under most treaties, the outcome mirrors the domestic TAP rules: if TAP → Australia taxes; if not TAP → Australia does not tax (residence country taxes).

Always check the saving clause and specific treaty wording.

## Section 9 — Sources

- ITAA 1997 Division 855 (non-resident CGT)
- Tax Administration Act 1953, Schedule 1, Subdivision 14-D (FRCGW)
- ATO: ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax
- ATO: Foreign resident capital gains withholding (ato.gov.au/FRCGW)

> **Working paper only.** The TAP classification requires analysis of the company's asset composition by market value — not book value. Engage a qualified Australian tax adviser for transaction-specific advice.

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
