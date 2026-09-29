---
name: cyprus-tax-optimization
description: Use this skill whenever asked about reducing tax in Cyprus, tax planning, or legal strategies to minimise tax for an individual, freelancer, or company in Cyprus. Trigger on phrases like "reduce tax Cyprus", "Cyprus non-dom", "non-domiciled", "0% dividend tax", "SDC exemption", "Cyprus IP box", "3% tax IP", "Cyprus company dividends", "60-day rule", "save tax Cyprus", "tax planning Cyprus". This skill covers the non-dom regime (17 years 0% SDC on dividends/interest/rents), the company-plus-dividend extraction structure, the IP Box (~3% on qualifying IP), self-employment vs company, the personal-income reliefs, and the substance/anti-avoidance red lines. ALWAYS read this skill before advising on any Cyprus tax optimisation.
version: 0.2
jurisdiction: CY
tax_year: 2025
last_updated: 2026-09-29
reviewed_by: Christos Thoma
review_status: current
depends_on: []
category: tax-optimization
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus Tax Optimization

## Cyprus Tax Optimization Skill v0.2
> **Accountant-reviewed (`tier: 1`).** Christos Thoma reviewed the rates and thresholds in this guide against the cited authorities on 2026-06-12; the reviewed figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29), and the sign-off is recorded in the frontmatter (`reviewed_by`, `review_status: current`) and on the roster in `PARTNERS.md`. Until 2026-09-29 this banner still read "Tier 2, research-verified, not yet signed off by a Cyprus tax adviser", the draft label the guide carried before that review. **Provenance of the draft:** Cyprus Tax Department, PwC/KPMG/Deloitte Cyprus and 2026 tax-reform commentary; figures must agree with `cyprus-income-tax.md` / `cyprus-social-contributions.md`. **Not covered by the review:** items flagged for further clarification were excluded, so any item below still marked `[RESEARCH GAP — reviewer to confirm]` remains unconfirmed. Aggressive positions are never advised; every suggestion must be reviewed against the client's facts.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Cyprus |
| Currency | EUR |
| Headline levers | Non-dom (0% SDC on dividends/interest/rents); company + dividend extraction; IP Box (~3% on qualifying IP) |
| Personal income tax | 0% up to €19,500 (2025); 20/25/30/35% bands above. **2026 reform raises the 0% band to €22,000** — confirm against `cyprus-income-tax.md`. |
| Corporate tax | **15%** from 1 January 2026 under the Cyprus tax reform (12.5% up to 31 December 2025); 15% is also the OECD Pillar Two minimum |
| SDC (Special Defence Contribution) | Applies to dividends/interest/rents of Cyprus-DOMICILED residents; **non-doms are exempt** |
| Self-employed social insurance | ~16.6% of deemed income |
| Anti-avoidance | Substance / place-of-effective-management; ATAD GAAR |

> **The Cyprus headline is the NON-DOM + COMPANY combo:** run profits through a Cyprus company (15% CIT from 1 January 2026; 12.5% up to 31 December 2025), then extract as dividends which — for a non-dom — bear **0% SDC and 0% PIT**. Total effective tax ≈ the corporate rate only.

## Section 2 -- Non-Dom Regime (the headline)

- **Non-dom 0% SDC on worldwide dividends, interest and rental income** — A Cyprus tax resident who is non-domiciled pays 0% SDC on worldwide dividends, interest and rental income for 17 years of residency (extendable by two further 5-year blocks via a €250,000 lump-sum fee each → up to 27 years).  _(Savva; KPMG)_
- **Becoming resident — routes** — 183-day rule, or 60-day rule: ≥60 days in Cyprus, no >183 days in any single country, plus a Cyprus tie (business/employment/directorship) and a residence (owned or rented). From 1 January 2026, the condition of not being tax-resident elsewhere is removed; other conditions must still be met.

**AUDIT FLASH POINT** — the 60-day route and non-dom status require genuine residency and ties; sham residency is challengeable. Confirm the client actually meets the day-count and tie tests.

## Section 3 -- Company + Dividend Extraction

**Section 3 -- Company + Dividend Extraction**

| Step | Treatment |
| --- | --- |
| Trade through a Cyprus company | 12.5–15% CIT on profits |
| Pay a modest director salary | Deductible; subject to PIT + social insurance; covers cover/pension |
| Distribute the rest as dividends | Non-dom shareholder: **0% SDC + 0% PIT** on dividends (GHS at 2.65% may apply, subject to the EUR 180,000 annual GHS cap) |

Net effect for a non-dom owner-manager: roughly the **corporate rate only** on extracted profit. Compare with operating as a **self-employed individual**, taxed on the progressive scale up to 35% — usually worse at higher incomes. **[RESEARCH GAP — model the salary/dividend split and confirm the GHS (health) contribution treatment on dividends.]**

## Section 4 -- IP Box (~3% on qualifying IP)

- **IP Box mechanics** — Qualifying IP income (patents, copyrighted software, etc.) gets an 80% deemed deduction, so only 20% is taxed at the corporate rate → ≈3% effective. Benefit is proportional to the R&D you actually incur (OECD modified nexus). Ideal for SaaS/tech/IP founders.  _(Mondaq; LCK)_

**AUDIT FLASH POINT** — the nexus rule ties the benefit to genuine R&D substance in Cyprus; acquired IP with no local development does not qualify. **[RESEARCH GAP — reviewer to confirm qualifying-asset definitions and the nexus fraction.]**

## Section 5 -- Personal Reliefs & Exemptions

**Section 5 -- Personal Reliefs & Exemptions**

| Relief | Detail |
| --- | --- |
| 0% band | Income up to €19,500 (2025) / €22,000 (2026 reform) is tax-free. |
| Expat / first-employment relief | 50% exemption (Art. 8(23A)) for new residents with remuneration above EUR 55,000, for up to 17 years; the older 20% relief (Art. 8(21A): lower of 20% or EUR 8,550 a year, 7 years) is closed to new entrants from 2026; from tax year 2026 the Art. 8(21B) "Minds in Cyprus" relief (Law 17(I)/2026) exempts 25% of employment income or business profits, capped at EUR 25,000 a year, for 7 years, for individuals who commence work in Cyprus between 2025 and 2030 after 7 years of non-residence. The three cannot be combined; see `cyprus-income-tax` §5.7 |
| Foreign pension | Taxed at a flat 5% above EUR 5,000 from 1 January 2026 (taxpayer may elect annually to be taxed under normal PIT rates instead). |
| Life insurance / provident / social insurance | Deductible up to a capped percentage of income. |

## Section 6 -- Red Lines (do not cross)

- **Substance & management** — A Cyprus company must be genuinely managed and controlled in Cyprus (board, decisions, substance) to be Cyprus-resident and to benefit. Letterbox companies are challengeable.
- **Non-dom residency must be real** — Meet the day-count and tie tests; don't fabricate residency.
- **IP Box needs real R&D** — Nexus approach; no benefit for parked, acquired IP.
- **ATAD GAAR / anti-abuse** — ATAD GAAR / anti-abuse applies to arrangements whose main purpose is a tax advantage without substance.

## PROHIBITIONS

- **Non-dom 0% SDC without residency confirmation** — NEVER present non-dom 0% SDC without confirming genuine Cyprus tax residency (60-day or 183-day test).
- **IP Box 3% without nexus condition** — NEVER present the IP Box 3% without the R&D-nexus / substance condition.
- **Substance-free company as tax shell** — NEVER advise a substance-free Cyprus company as a tax shell.
- **Contradicting other skills' rates** — NEVER contradict the rates/bands in `cyprus-income-tax.md` / `cyprus-social-contributions.md`.
- **Research gap figures presented as confirmed** — NEVER present any [RESEARCH GAP] figure as confirmed, nor present optimisation as definitive advice — route to a licensed Cyprus tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Cyprus) before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
