---
name: bm-corporate-income-tax
description: "Source-cited draft: corporate income tax for Bermuda (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BM
category: international
tax_year: 2025
last_updated: 2026-11-14
version: 1.4
review_status: pending_review
tier: 2
depends_on:
  - corporate-income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bermuda Corporate Income Tax

## Corporate income tax (Pillar Two CIT)

Apply the [current system screening](bm-tax-overview.md#corporate-income-tax-screening) before a corporate-tax conclusion. It covers group consolidation, the 2-of-4-year revenue lookback, entity exclusions/elections, limited international footprint, fiscal periods and tax assurances. The charging provisions apply from 1 January 2025; the current captured consolidated Act includes listed amendments through 2026:25 (operative 29 July 2026). No company is exempt solely because it is incorporated in Bermuda or holds an assurance certificate.

**Detailed calculation boundary.** This update reconciles headline scope and the charge. The retained loss, economic-transition adjustment, other tax-credit and filing/payment details below have not been fully reconciled against the current amendment and administrative chain. Mark any computation or filing decision using those details **Needs Input** until its topic-specific review is complete.

- **Corporate income tax charge:** 15% of the Bermuda Constituent Entity Group’s net taxable income, less applicable foreign tax credits under Part 4. Section 4(3) imposes joint and several liability across Bermuda constituent entities of the same in-scope MNE Group. This is not a tax on gross revenue. [Consolidated CIT Act, s 4](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)
- **CIT effective date** — Fiscal years beginning on or after 1 January 2025  _(Corporate Income Tax Act 2023 (https://www.gov.bm/CIT))_
- **Group revenue threshold:** generally at least EUR 750 million in the UPE’s consolidated financial statements in at least 2 of the 4 immediately preceding fiscal years, subject to s 11 special rules, s 13 and relevant elections. Threshold satisfaction alone does not settle liability. [CIT Act, ss 2 and 8–15A](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) · [Full screening](bm-tax-overview.md#corporate-income-tax-screening)
- **Outside the charge:** determine in-scope group and Bermuda constituent-entity/group status before concluding that s 4 does not charge CIT. This is not proof of the absence of every other tax or foreign-country liability. [CIT Act, ss 4 and 8–15A](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)
- **CIT tax base:** ss 5–6 and 20–46 govern the detailed income, loss and adjustment computation. The retained summary of an 80% loss limitation is not an unconditional rule: current s 6(8) contains a separate shock-loss mechanism. The detailed computation and its evidence remain **Needs Input**; do not apply 15% directly to book income. [CIT Act](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)
- **Shared workflow boundary:** the corporate workflow base supplies controls, not Bermuda law. The EUR 750 million threshold does not itself authorise a Bermuda GloBE top-up calculation: General Guidance v2 states that GloBE rules are not incorporated by reference unless expressly stated. Establish each applicable domestic or foreign Pillar Two rule separately. The base’s sector refusals still apply; screening a non-corporate entity under the Act does not permit its computation through a corporation-only workflow. Detailed computation remains **Needs Input** under the boundary above. [General Guidance v2, p 5](https://www.cita.bm/assets/documents/2026-11-13-13-18-25-CIT%20Guidance%20Notes%20(General)%20V2.pdf)
- **Economic Transition Adjustment (ETA)** — A Bermuda Constituent Entity included in a group in its first fiscal year beginning on or after 1 January 2025 adjusts taxable income for the fair value of its assets and liabilities (excluding goodwill) at 30 September 2023, with the adjustments capped at 80% of the relevant amount and intangibles amortised over the first ten fiscal years  _(Corporate Income Tax Act 2023 (2023:35), Bermuda Laws Online, s 33 — https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Corporate%20Income%20Tax%20Act%202023)_
- **Entity exclusions and elections:** apply s 10’s defined excluded-entity categories and subsidiary ownership/activity conditions; investment funds and real-estate vehicles are not all automatically excluded. Section 9(2)(b)’s under-80%-by-value exclusion is subject to election. Sections 9(4) and 10(4) identify five-year elections; current ss 49(6) and 49A contain revocation provisions. Check the facts and election history. [CIT Act, ss 2, 9–10, 49 and 49A](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)
- **Dividend withholding:** the prior 0%/none claim remains a current primary-evidence gap. Do not use it as a verified rate. [Evidence boundary](bm-tax-overview.md#claims-still-requiring-evidence)
- **Interest and royalty withholding:** each prior 0%/none claim remains a current primary-evidence gap. Keep the categories separate and do not output zero. [Evidence boundary](bm-tax-overview.md#claims-still-requiring-evidence)
- **CIT filing & payment** — Each Bermuda Constituent Entity Group files a CIT return for every fiscal year beginning on or after 1 January 2025 through CITA Online (Form 100 with the standard S-101 or simplified S-102 schedules); the Agency collects instalments during the fiscal year and charges interest on late instalments  _(Corporate Income Tax Agency, Corporate Income Tax Return — https://www.cita.bm/corporate-income-tax-return1 ; Corporate Income Tax Agency, home page (instalment deadlines) — https://www.cita.bm/ ; EY tax alert — https://www.ey.com/en_gl/technical/tax-alerts/bermuda-releases-final-cit-administrative-regulations)_

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
