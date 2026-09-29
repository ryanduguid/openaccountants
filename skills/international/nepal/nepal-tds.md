---
name: nepal-tds
version: 1.1
description: ALWAYS read this skill before touching any Nepal TDS / withholding tax work. Use whenever asked to compute or deduct Nepal withholding tax (TDS) on rent, interest, dividends, service/contract payments, or payments to non-residents under the Income Tax Act 2058. Trigger on phrases like "Nepal TDS", "Nepal withholding", "TDS rates Nepal", "Section 88 Nepal", "rent TDS Nepal 10%", "dividend TDS Nepal 5%", "interest TDS Nepal 6%", "contract TDS Nepal 1.5%", or "FY 2082/83 TDS". Out of scope — personal income tax computation (separate skill), corporate tax (separate skill), payroll/SSF salary TDS (use the payroll skill), and VAT.
jurisdiction: NP
category: international
tax_year: 2025
last_updated: 2026-09-29
reviewed_by: Ashish Bista
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nepal Tds

## Nepal — TDS / Withholding Tax — Skill v1.1
> **Produced by OpenAccountants (openaccountants.com).** **Accountant-reviewed (`tier: 1`).** Ashish Bista reviewed the rates and thresholds in this guide against the cited authorities on 2026-06-06; the reviewed figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29), and the sign-off is recorded in the frontmatter (`reviewed_by`, `review_status: current`) and on the roster in `PARTNERS.md`. Coverage: FY 2082/83. Until 2026-09-29 this banner still read "Research-grade (tier 2)", the draft label the guide carried before that review. **Source provenance of the draft:** figures derive from Nepali professional-firm publications (PKF T.R. Upadhya, Union Nepal) reflecting the Income Tax Act 2058 §87–§88 and Finance Act 2082, not re-anchored to primary IRD pages; the review excluded items flagged for further clarification. Confirm any figure outside the reviewed figures against the statute before reliance. Not tax advice.

## Section 1 — Quick reference (rates, FY 2082/83 — "no change" from FY 2024-25)

**Payment type / Rate / Notes**

| Payment type | Rate | Notes |
| --- | --- | --- |
| **Rent** (paid by a resident person) | **10%** |  |
| **Dividend** (paid by resident company / partnership) | **5%** | Same to resident AND non-resident |
| **Interest** (Nepal source, from resident banks / FIs / cooperatives / debenture issuers / listed companies) | **6%** to a natural person (not in business); **15%** to entities |  |
| **Contract / agreement payment to a non-resident** | **5%** | Income Tax Act 2058 s.89; not where the payment is a s.88 service, royalty or technical fee, which takes 15% (§3.6) |
| **Contract payments exceeding NPR 50,000** | **1.5%** | Income Tax Act 2058 s.89; resident contract/supply payments that are not a s.88 service fee (§3.5) |
| **Freight and transportation services** | **1.5%** if the payee is VAT-registered; **2.5%** if not | Income Tax Act 2058 s.88 |
| **Service and consultancy fees** (resident payee) | **1.5%** if the payee is VAT-registered; **15%** if not | Income Tax Act 2058 s.88 |
| **Service, royalty or technical fees to a non-resident** | **15%** | Income Tax Act 2058 s.88; a lower rate only under an applicable DTAA |
| **Windfall gains** (prizes, lotteries) | **25%**, final withholding | Income Tax Act 2058 s.88 |

**Field / Value**

| Field | Value |
| --- | --- |
| Country / authority | Nepal — Inland Revenue Department (IRD), ird.gov.np |
| Statute | Income Tax Act 2058 (2002) §87–§88, as amended by Finance Act 2082 |
| Income year | Shrawan 1 – Ashad end (BS); FY 2082/83 |
| Validated by | Pending — Nepali CA / registered tax practitioner |
| Skill version | 1.1 |

> **Refuted / do NOT use:** a flat 15% Section 88 TDS on interest/rent/service, and a 10% dividend TDS — both appear in some secondary commentary but were adversarially refuted; the effective FY 2082/83 rates above govern.

### Conservative defaults

**Ambiguity / Default**

| Ambiguity | Default |
| --- | --- |
| Recipient natural person vs entity (interest) | Treat as entity (15%) and flag |
| Resident vs non-resident recipient | Flag; a non-resident's service, royalty or technical fees take 15% (s.88) unless a DTAA rate is documented |
| Contract payment near NPR 50,000 threshold | Apply 1.5% if it exceeds 50,000 |
| Payment under a contract that is also a service fee | Withhold under s.88 (§3.5 / §3.6), not at the s.89 contract rate, and flag |

## Section 2 — Refusal catalogue

- **R-NP-TDS-1 — Salary TDS** — Employment withholding sequences with SSF — use `nepal-payroll`.
- **R-NP-TDS-2 — Treaty relief on non-resident payments** — The domestic rate on a non-resident's service, royalty or technical fees is 15% (s.88, §3.6); a lower treaty rate needs the DTAA article and the payee's residence certificate, and the rest of the non-resident Section 88 schedule was NOT established — VERIFY; escalate.
- **R-NP-TDS-3 — Full Section 88 schedule** — Many payment categories exist beyond those listed; this skill covers the common ones. Confirm the full §88 table for FY 2082/83.

## Section 3 — Tier 1 rules

- **Tier 1 rules intro** — 

### 3.1 Rent — 10%

- **Rent** — TDS of 10% on rent paid by a resident person.

### 3.2 Dividend — 5%

- **Dividend** — TDS of 5% on dividends paid by a resident company/partnership — to both resident and non-resident recipients.

### 3.3 Interest — 6% / 15%

- **Interest** — On Nepal-source interest paid by resident banks, financial institutions, cooperatives, debenture issuers, or listed companies: 6% to a natural person who is not deriving the interest in the course of business; 15% to entities.

### 3.4 Contracts

- **Contracts** — Payment under a contract/agreement to a non-resident: 5%. Resident contract/supply payments exceeding NPR 50,000: 1.5%. **Source:** PKF Trunco "Tax Rates 2082-83" §7.1 (each marked "No change"); Union Nepal TDS guide.  _(PKF Trunco "Tax Rates 2082-83" §7.1; Union Nepal TDS guide)_
- **Precedence of s.88 over s.89** — Section 89 does not apply to a payment that is liable to withholding under s.87, s.88 or s.88Ka (s.89(4)(kha)): a service, royalty or technical fee paid under a contract or agreement is withheld at the s.88 rate (§3.5 for a resident payee, §3.6 for a non-resident), and the s.89 contract rates (1.5% resident, 5% non-resident) apply to a deed or contract for the supply of goods or labour, or for construction, installation or the establishment of tangible property, that is not a s.88 fee.  _(Income Tax Act 2058 s.89(4))_

### 3.5 Service fees — 1.5% / 15%

- **Service and consultancy fees (resident payee)** — 1.5% where the payee is VAT-registered, 15% where it is not; freight and transportation services likewise 1.5% (VAT-registered) or 2.5% (not).  _(Income Tax Act 2058 s.88)_

### 3.6 Non-resident service, royalty and technical fees — 15%

- **Non-resident service, royalty and technical fees** — 15% on payments to a non-resident for services, royalties or technical fees, reduced only where a double-taxation agreement applies (R-NP-TDS-2); a contract payment to a non-resident that is not such a fee (a supply, works or installation contract) takes the 5% rate of s.89 (§3.4).  _(Income Tax Act 2058 s.88)_

### 3.7 Windfall gains — 25%

- **Windfall gains** — 25% on prizes, lottery winnings and other windfall gains, as a final withholding.  _(Income Tax Act 2058 s.88)_

## Section 4 — Worked examples

- Rent NPR 200,000 to a resident landlord → TDS = 10% × 200,000 = **NPR 20,000**.
- Bank interest NPR 100,000 to an individual (not in business) → TDS = 6% × 100,000 = **NPR 6,000**.
- Dividend NPR 500,000 → TDS = 5% × 500,000 = **NPR 25,000**.
- Resident supply contract NPR 300,000 → TDS = 1.5% × 300,000 = **NPR 4,500**.
- Consultancy fee NPR 100,000 to a resident firm that is not VAT-registered → TDS = 15% × 100,000 = **NPR 15,000** (1.5% × 100,000 = NPR 1,500 if it is VAT-registered).
- Technical fee NPR 1,000,000 to a non-resident under a service contract, no treaty claim → s.88 governs (s.89(4)(kha)), so TDS = 15% × 1,000,000 = **NPR 150,000**, not 5% under s.89.

## Section 5 — Filing

TDS is deducted at payment and deposited to the IRD with a credit certificate to the payee. The tax withheld in a month is deposited, and the withholding return filed, by the 25th of the following Nepali month (Income Tax Act 2058 s.90).

## Section 6 — Sources

Research-grade, FY 2082/83. **Secondary firm publications — re-anchor to primary IRD/statute (§87–§88):**
1. PKF T.R. Upadhya & Co. "Tax Rates 2082-83" §7.1 — https://pkf.trunco.com.np/files/publications/1748841198_Tax%20Rates%202082-83_Final_250601_213028.pdf
2. Union Nepal — TDS in Nepal — https://unionnepal.com/tds-in-nepal
3. Income Tax Act 2058 (2002) §88 (rates) and §90 (deposit and return by the 25th of the following month) — confirm at https://ird.gov.np

**Known gaps / VERIFY:** the §88 schedule beyond the categories in §1 and §3; treaty rates on non-resident payments.

## Prohibitions

- NEVER use the refuted flat 15% (interest/rent/service) or 10% dividend rates — use the rates in §1.
- NEVER apply the 6% interest rate to an entity recipient — entities are 15%.
- NEVER apply a rate below 15% to a non-resident's service, royalty or technical fees without the DTAA article and the payee's residence certificate.
- NEVER present these as primary-IRD-confirmed — flag for verifier re-anchoring.
- NEVER file or instruct filing — working paper for practitioner review only.

## Disclaimer

For informational and computational purposes only; not tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Nepali professional (CA / registered tax practitioner) before filing or acting upon. Latest verified version at [openaccountants.com](https://openaccountants.com).

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
