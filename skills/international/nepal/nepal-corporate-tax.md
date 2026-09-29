---
name: nepal-corporate-tax
version: 1.1
description: "ALWAYS read this skill before touching any Nepal corporate income tax work. Use whenever asked about Nepal company tax for a resident entity. Trigger on phrases like \"Nepal corporate tax\", \"Nepal CIT\", \"company tax Nepal\", \"25% corporate Nepal\", \"30% bank tax Nepal\", \"special industry rebate Nepal\", \"Section 11 Nepal\", \"Income Tax Act 2058 company\", or \"FY 2082/83 company\". Covers the Income Tax Act 2058 (2002) as amended by the Finance Act 2082: the 25% normal rate, the 30% sector rate (banks/insurance/telecom/liquor-tobacco/etc.), and the effective 20% for special industries. Out of scope — personal income tax (separate skill), TDS (separate skill), payroll/SSF, VAT, and sector special computational regimes."
jurisdiction: NP
category: international
tax_year: 2025
last_updated: 2026-09-29
reviewed_by: Ashish Bista
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nepal Corporate Tax

## Nepal — Corporate Income Tax — Skill v1.1
> **Produced by OpenAccountants (openaccountants.com).** **Accountant-reviewed (`tier: 1`).** Ashish Bista reviewed the rates and thresholds in this guide against the cited authorities on 2026-06-06; the reviewed figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29), and the sign-off is recorded in the frontmatter (`reviewed_by`, `review_status: current`) and on the roster in `PARTNERS.md`. Coverage: FY 2082/83. Until 2026-09-29 this banner still read "Research-grade (tier 2)", the draft label the guide carried before that review. **Source provenance of the draft:** figures derive from Nepali professional-firm tax-fact publications (PKF T.R. Upadhya, Baker Tilly Nepal) reflecting the Income Tax Act 2058 and Finance Act 2082, not re-anchored to primary IRD pages; the review excluded items flagged for further clarification. Confirm any figure outside the reviewed figures against the statute before reliance. Not tax advice.

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country / authority | Nepal — Inland Revenue Department (IRD), ird.gov.np |
| Currency | NPR |
| Income year | Shrawan 1 – Ashad end (BS); FY 2082/83 ≈ mid-July 2025 – mid-July 2026 |
| Primary legislation | Income Tax Act 2058 (2002), as amended by Finance Act 2082 |
| **Normal rate** | **25%** of taxable income (general companies, firms, industries) |
| **Sector rate** | **30%** — see §3.2 |
| **Special industries (Sec 11)** | Effective **20%** (25% normal less a 20% rebate) |
| Validated by | Pending — Nepali CA / registered tax practitioner |
| Skill version | 1.1 |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Sector unclear | Apply 25% normal |
| Whether 30% sector rate applies | Apply 30% if the entity is in any §3.2 sector; flag |
| Special-industry (Sec 11) rebate claimed | Apply 25% until eligibility confirmed; flag |

## Section 2 — Refusal catalogue

- **R-NP-CT-1** — Sector special computational regimes (banking provisioning, insurance, petroleum) — out of scope; escalate.  _(Section 2 — Refusal catalogue)_
- **R-NP-CT-2** — Special-industry / export / SEZ concessions beyond the headline Section 11 rebate and the Finance Act 2083 concessions stated in §3.4 (startups, IT service exports, SEZ rent, IT bonus shares, the dispute-settlement window) — VERIFY against the Act; escalate. The §3.4 concessions themselves are applied only once eligibility is confirmed.  _(Section 2 — Refusal catalogue)_
- **R-NP-CT-3** — Cross-skill. Personal → `nepal-income-tax`; TDS → `nepal-tds`; payroll/SSF → `nepal-payroll`; VAT → `nepal-vat`.  _(Section 2 — Refusal catalogue)_

## Section 3 — Tier 1 rates

### 3.1 Normal rate — 25%

- **Normal rate** — 25% (general companies, firms, industries)  _(Income Tax Act 2058 Sch.1 (PKF/Baker Tilly))_

### 3.2 Sector rate — 30%

- **Sector rate applicability** — A 30% rate applies to entities in these sectors: Banks and financial institutions (commercial/development banks, finance companies); General (non-life) insurance; Financial-transaction (money-transaction) entities; Petroleum; Cigarettes, tobacco, cigars, pan masala, alcohol, beer; Telecommunications and internet service providers; Money transfer; Capital market / securities / merchant banking / brokerage businesses  _(Income Tax Act 2058 (as amended by Finance Act 2082))_

### 3.3 Special industries — effective 20% (Section 11)

- **Special industries rebate mechanism** — "Special industries" under Section 11 receive a 20% rebate on the normal rate, yielding an effective 20% (25% × 80%). Confirm eligibility under Section 11.  _(Income Tax Act 2058 s.11)_

Rates are **unchanged from FY 2024-25**. **Source:** PKF Trunco; Baker Tilly; actNepal (Section 11 mechanism).

### 3.4 Concessions of Finance Act 2083 (FY 2083/84)

- **Startups** — Exempt from income tax for 5 years where annual turnover does not exceed NPR 100 million.  _(Finance Act 2083)_
- **IT service exports** — 75% exemption on income from the export of IT services.  _(Finance Act 2083)_
- **Special Economic Zone rent** — 100% exemption from SEZ rent for the first 3 years for a new industry established in a Special Economic Zone.  _(Finance Act 2083)_
- **IT industry bonus shares** — 0% dividend tax on the capitalisation of profits (bonus shares) issued by an IT industry.  _(Finance Act 2083)_
- **Tax dispute settlement window** — One-time settlement of a pending dispute by paying the principal tax plus a 1% fee, with penalties and interest waived.  _(Finance Act 2083)_

The eligibility conditions and the commencement of each concession are not stated here: confirm them against the Act and the IRD's notice before applying one (R-NP-CT-2). Reviewed by Ashish Bista on 2026-06-06.

## Section 4 — Tier 2 (capital gains for entities)

- **Listed shares disposed by a resident entity** — 10%
- **Land/building owned by a non-individual (entity)** — 1.5%

(Individual rates are in `nepal-income-tax` / a CGT context.)

## Section 5 — Worked examples

- General company, taxable income NPR 20,000,000 → CIT = 25% × 20,000,000 = **NPR 5,000,000**.
- Commercial bank, taxable income NPR 20,000,000 → CIT = 30% × 20,000,000 = **NPR 6,000,000**.
- Qualifying special industry, taxable income NPR 20,000,000 → CIT = 20% × 20,000,000 = **NPR 4,000,000**.

## Section 6 — Filing

- Income year Shrawan 1 – Ashad end; file via IRD with PAN.
- Advance tax instalments: 40% of the estimated annual liability by Poush end (mid-January), 70% cumulative by Chaitra end (mid-April) and 100% by Ashad end (mid-July); the annual return is due by Ashwin end (mid-October) — Income Tax Act 2058 ss. 94 and 96.

## Section 7 — Sources

Research-grade, FY 2082/83. **Secondary firm publications — re-anchor to primary IRD/statute:**
1. PKF T.R. Upadhya & Co. "Tax Rates 2082-83" — https://pkf.trunco.com.np/files/publications/1748841198_Tax%20Rates%202082-83_Final_250601_213028.pdf
2. Baker Tilly Nepal "Tax Fact 2025-2026" — https://bakertilly.com.np/storage/download/1750310698_Tax_Fact_2025-2026.pdf
3. Income Tax Act 2058 (2002), Section 11 + Schedule 1 — confirm at https://ird.gov.np
4. Finance Act 2082.
5. Finance Act 2083 (the §3.4 concessions).

**Known gaps / VERIFY:** primary citations; the full special-industry / export / SEZ concession schedule beyond the Finance Act 2083 concessions in §3.4, and the eligibility conditions and commencement of those.

## Prohibitions

- **Prohibitions** — - NEVER apply 25% to a §3.2 sector entity — those are 30%. - NEVER apply the Section 11 effective-20% without confirming special-industry eligibility. - NEVER present these as primary-IRD-confirmed — flag for verifier re-anchoring. - NEVER file or instruct filing — working paper for practitioner review only.

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
