---
name: sa-zakat
description: "Use this skill whenever asked about Saudi Arabian Zakat — the religious-origin wealth levy administered by ZATCA (Zakat, Tax and Customs Authority) on Saudi/GCC-owned business activity in the Kingdom of Saudi Arabia. Trigger on phrases like \"Saudi Zakat\", \"ZATCA Zakat\", \"Zakatable base Saudi\", \"2.5% Zakat KSA\", \"Implementing Regulations Zakat\", \"Saudi GCC zakat\", \"mixed entity Saudi\", \"Zakat return KSA\", \"Saudi Hijri filing\", \"Zakat working capital base\", \"Zakat net adjusted profit\", \"mixed ownership Saudi Zakat CIT split\", or \"ZATCA 120 days return\". Covers the 2.5% Hijri rate (2.5777% for a 365-day year), Zakatable persons (Saudi/GCC nationals and Saudi/GCC-owned share of capital), the Zakat base of additions less deductions with minimum and maximum limits under the Implementing Regulation issued by Ministerial Resolution 1007 of 19/8/1445H, mixed-entity Saudi/GCC vs foreign proportional split (Zakat on Saudi/GCC share; CIT 20% on foreign share — see sa-corporate-tax), passive entities, financing/banking sector specials, accounting-basis adjustments, and ZATCA portal annual filing within 120 days of fiscal year-end. Out of scope: pure CIT on 100%-foreign-owned entities (see sa-corporate-tax), Withholding Tax (see sa-wht), VAT (see saudi-arabia-vat), e-invoicing (see saudi-einvoice), Excise Tax, Real Estate Transaction Tax (RETT), Customs, oil and hydrocarbon sector special regimes, natural gas investment tax, Saudi Aramco special rate, and individual personal Zakat on non-commercial wealth (mosque/charitable Zakat al-mal outside ZATCA scope). ALWAYS read this skill before touching any Saudi Zakat work."
jurisdiction: SA
category: international
tax_year: 2025
last_updated: 2026-10-31
reviewed_by: Mehran Habib
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SA Zakat

## Saudi Arabia — Zakat — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill is for informational purposes only and does not constitute tax, legal, religious, or financial advice. All outputs must be reviewed and signed off by a Saudi-licensed Zakat advisor (SOCPA member or ZATCA-approved consultant) before filing or acting upon. Zakat carries both a fiscal and a religious dimension; this skill addresses only the fiscal compliance administered by ZATCA.

> **Source-cited draft (tier 2), not accountant-reviewed.** On 2026-06-06 Mehran Habib checked the rates, thresholds and deadlines listed for this guide against the cited authorities; the corrections of that fact check are in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). It was a check of listed facts, not a sign-off on the guide: no reviewer sign-off is recorded in the frontmatter, the guide is not on the roster in `PARTNERS.md`, and `review_status` is `pending_review`. Items the check flagged for clarification remain marked in the text.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Kingdom of Saudi Arabia (KSA) |
| Tax | Zakat — religious wealth levy administered as a fiscal charge |
| Currency | SAR (Saudi Riyal) |
| Tax authority | **ZATCA** — Zakat, Tax and Customs Authority (merged from GAZT + Saudi Customs, 2021) |
| Primary legislation | Royal Decree No. 17/2/28/8634 of 1370H (1950G) establishing the Zakat charge |
| Implementing Regulation | Ministerial Resolution No. 1007 of 19/8/1445H, for Zakat years starting on or after 1 January 2024. It replaced Resolution No. 2216 of 7/7/1440H (from 1 January 2019), which followed Resolution No. 2082 of 1438H. [ZATCA Zakat General Guideline 1445AH](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Zakat-General-Guideline-Zakat-Collection-1445AH.pdf), s 3.1 |
| Standard rate | **2.5%** of the Zakatable base (Hijri lunar year) |
| Rate for other years | **2.5% ÷ days in the Hijri year × actual days in the Zakat year**: **2.5777%** for a 365-day year on ZATCA's 354-day Hijri year (Regulation Art. 15; [ZATCA Zakat General Guideline 1445AH](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Zakat-General-Guideline-Zakat-Collection-1445AH.pdf), s 3.4.8 and examples 19 and 20) |
| Zakat base | Additions (equity and equivalents; liabilities within the limits of deducted assets; the difference between adjusted and net book profit) less deductions, then the maximum and minimum limits (see §3.4) |
| Zakatable persons | (a) Saudi & GCC natural persons engaged in commercial activity; (b) companies wholly owned by Saudi/GCC nationals; (c) Saudi/GCC-owned share of capital in mixed-ownership companies |
| Mixed entity | Saudi/GCC share → Zakat 2.5%; foreign share → CIT 20% (see sa-corporate-tax). Same accounting profit; apportioning the base is not worked in the guideline read (see §4.1) |
| Annual return | Zakat Declaration via ZATCA portal |
| Filing deadline | Within **120 days** of fiscal year-end |
| Payment deadline | Same — within 120 days of FYE |
| Advance instalments | Quarterly advance Zakat may apply for larger taxpayers (threshold per ZATCA notice) |
| Late-payment penalty | Not confirmed. [ZATCA's Zakat General Guideline 1445AH](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Zakat-General-Guideline-Zakat-Collection-1445AH.pdf) states no late-payment rate; the 5% per month figure formerly here matched no source read. Check the Implementing Regulation before quoting a rate |
| Failure-to-file penalty | Per ZATCA penalty schedule (variable; verify current circular) |
| Calendar election | Taxpayer may elect Hijri or Gregorian fiscal year; most large taxpayers elect Gregorian (rate adjusted) |
| Validated by | Pending — sign-off by SOCPA-licensed Zakat advisor |
| Skill version | 1.0 |

### 1.1 Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Ownership mix unclear | Treat as mixed entity — apply Saudi/GCC vs foreign split |
| GCC national status of shareholder unclear | Treat as non-GCC foreign (CIT 20% applies to that share) |
| Hijri vs Gregorian year unclear | Assume Gregorian (use 2.5777% for 365 days — most common large-taxpayer filing) |
| Adjustment item categorisation unclear | Treat as **add-back to base** (conservative — increases Zakatable base) |
| Liability classification unclear | Follow the Regulation's rules for added liabilities (Art 29); flag for advisor |
| Asset deduction conditions unclear | Do not deduct until the conditions are shown, and correct added liabilities accordingly (see §3.4); flag for advisor |
| Provision deductibility for Zakat purposes unclear | Add to base (conservative) |
| Financing arrangement Sharia-compliance unclear | Apply standard adjustment rules; flag for advisor |
| Advance Zakat instalment obligation unknown | Assume required — verify with ZATCA notice |
| Recent regulation amendment status | Flag "verify latest ZATCA circular (2024-2025 amendments to Implementing Regulations re: financing arrangements and intangibles)" |

## Section 2 — Required Inputs and Refusal Catalogue

### 2.1 Required Inputs

- **Minimum viable** — Full-year financial statements (income statement, balance sheet) prepared under SOCPA-endorsed IFRS, a complete shareholder register identifying Saudi/GCC vs foreign ownership percentages at the FYE (and ideally throughout the year), prior-year Zakat return, and confirmation of (i) fiscal calendar election (Hijri vs Gregorian), (ii) advance instalment status, (iii) any sector-specific designation.
- **Recommended** — General ledger, fixed-asset register (with classification of long-term vs short-term), full schedule of provisions and reserves, related-party transaction schedule, financing arrangement schedule (Sharia-compliant and conventional), commercial registration (CR) and ZATCA Zakat registration certificate.
- **Ideal** — SOCPA-audited financial statements, full reconciliation from accounting profit to Zakatable net adjusted profit, Zakat base worksheet with every line item supported, ownership percentage attestation, ZATCA prior-year assessment notice.
- **HARD STOP if minimum is missing** — Without financial statements and an ownership breakdown, no Zakat computation may be produced. Ownership identification is the gating fact — it determines Zakat-vs-CIT routing.

### 2.2 Refusal Catalogue

- **R-SA-Z-1** — 100%-foreign-owned entity. No Zakat applies; route entirely to sa-corporate-tax (CIT 20%). Out of scope here.
- **R-SA-Z-2** — Oil and hydrocarbon sector. Saudi Aramco and upstream oil/gas concessionaires are subject to special tax regimes (rates up to 85% historically; Aramco at 20%/50%/85% tiered post-IPO restructuring). Out of scope. Escalate to a Saudi tax specialist.
- **R-SA-Z-3** — Natural gas investment tax. Separate regime — out of scope.
- **R-SA-Z-4** — Banking and insurance sector specials. Certain Zakat base adjustments specific to financial institutions (statutory deposits with SAMA, regulatory capital treatment, technical reserves for insurers) are outside the general Implementing Regulations framework and require specialist sign-off. Skill produces a preliminary computation only; final return MUST be reviewed by a financial-services Zakat specialist.
- **R-SA-Z-5** — Real Estate Transaction Tax (RETT) interactions. RETT is a separate 5% transactional charge — out of scope.
- **R-SA-Z-6** — Personal Zakat al-mal on non-commercial wealth. Religious obligation outside ZATCA fiscal scope (personal savings, gold, agricultural Zakat, livestock Zakat). Refer the taxpayer to a religious scholar; not a ZATCA filing.
- **R-SA-Z-7** — Group / consolidated Zakat. Saudi tax group regime (introduced under amended regulations) and consolidated returns for related Zakat payers are out of scope of v1.0.
- **R-SA-Z-8** — Permanent establishments / treaty positions. PE attribution under tax treaty rules is out of scope (and largely a CIT question, not Zakat).
- **R-SA-Z-9** — Disputed assessments / objections. ZATCA appeals before the Tax Violations and Disputes Resolution Committee require licensed representation. Out of scope.
- **R-SA-Z-10** — Stale regulation reliance. The Implementing Regulations have been amended several times since 2017G, including in 2024-2025G affecting financing arrangements and intangibles. The skill MUST flag "verify latest ZATCA circular" in every output and refuse to finalise without confirmation that the cited regulation version is current.

## Section 3 — Tier 1: The Zakat Charge

### 3.1 Nature of the Charge

- **Nature of the charge** — Zakat in Saudi Arabia is a hybrid religious-fiscal levy. Its origin is the third Pillar of Islam (obligation to purify wealth by paying 2.5% of qualifying assets held for a lunar year, hawl). The Kingdom has since 1370H (1950G) codified the collection of Zakat from commercial enterprises owned by Saudi nationals as a fiscal charge administered by the state. Since 2021G this is administered by ZATCA (Zakat, Tax and Customs Authority), formed by the merger of the former General Authority of Zakat and Tax (GAZT) and Saudi Customs. The legal basis is Royal Decree No. 17/2/28/8634 of 1370H, with detailed computation rules in the Implementing Regulation for Zakat Collection issued by Ministerial Resolution No. 1007 of 19/8/1445H, for Zakat years starting on or after 1 January 2024.  _(Royal Decree No. 17/2/28/8634 of 1370H; Ministerial Resolution No. 1007 of 19/8/1445H)_

### 3.2 The Rate

- **Hijri rate** — 2.5% under the Hijri lunar calendar (one hawl = one lunar year ≈ 354.36 days).
- **Rate for a Gregorian year** — 2.5777% for a 365-day year: 2.5% ÷ 354 × 365. Other lengths use actual days; ZATCA's example for a 426-day first year gives 3.0085%.  _(Regulation Art. 15; ZATCA Zakat General Guideline 1445AH, s 3.4.8)_

### 3.3 Persons Subject to Zakat

**Persons Subject to Zakat**

| Person | Treatment |
| --- | --- |
| Saudi natural person — commercial activity | Subject to Zakat on Zakatable base of the business |
| GCC national (Bahrain, Kuwait, Oman, Qatar, UAE) natural person — commercial activity in KSA | Subject to Zakat (treated as Saudi for Zakat purposes) |
| Company wholly owned by Saudi/GCC nationals | Subject to Zakat on entire Zakatable base |
| Company wholly owned by non-GCC foreign persons | **NOT** Zakat — subject to CIT 20% (see sa-corporate-tax) |
| Mixed-ownership company | **Split**: Saudi/GCC share % → Zakat 2.5%; foreign share % → CIT 20%. Same accounting profit, proportional split with separately computed adjustments |
| Listed company shares — Saudi/GCC shareholders | Saudi/GCC-owned proportion of the listed company subject to Zakat |
| Listed company shares — non-GCC foreign shareholders | Foreign-owned proportion subject to CIT 20% |
| Government-owned entities | Generally exempt; specific treatment per ZATCA notice |
| Charitable / non-profit organisations | Generally outside scope; verify registration |

- **GCC** — GCC = Gulf Cooperation Council: Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, United Arab Emirates. GCC nationals are treated as Saudi nationals for Zakat purposes under reciprocal arrangements.

### 3.4 Zakat Base: Additions, Deductions and Limits

For Zakat years starting on or after 1 January 2024, a Zakat payer holding statutory accounts computes the base by the indirect method (Art 21). Zakat payers assessed on an arbitrary basis follow Arts 82 to 91, which this guide does not compute. _([ZATCA Zakat General Guideline 1445AH](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Zakat-General-Guideline-Zakat-Collection-1445AH.pdf))_

**Zakat base = addition items − deduction items, then test against the limits.**

- **Additions (Art 23)**: (1) Equity and its equivalents, without limit. Most provisions count as equity (Art 24). (2) Liabilities under Art 29, within the limits of the deducted assets: non-current debts, provisions that are a stable debt to non-owners such as end-of-service benefits and leave, deferred tax liability, contract obligations, lease liabilities and negative derivatives. A current liability is added if a current asset is deducted, if current liabilities exceed current assets (the excess), or if it is shown to be equivalent to a non-current liability. (3) The difference between adjusted net profit or loss and net book profit or loss, after Zakat and tax.
- **Deductions (Arts 26, 31 and 32), where their conditions are met**: Investments in establishments in and outside the Kingdom (Arts 43 and 44); investments in funds in the Kingdom (Art 45); net fixed assets and equivalents (Arts 49 and 51); intangible assets (Art 50); materials not for sale and raw materials (Art 52); investments in registered financing funds; bonds and instruments the issuer treats as capital (Art 55); statutory deposits (Art 56); deferred tax asset; and partners' debit loans (Art 31).
- **Correcting added liabilities**: If a non-current asset is not deducted, exclude (asset not deducted ÷ total non-current assets) × non-current liabilities, up to the value of that asset. If a current asset is deducted, add (asset deducted ÷ total current assets) × current liabilities.
- **Maximum limit (Art 28)**: The base can never exceed equity and its equivalents at the end of the Zakat year, plus the difference between adjusted net profit or loss and net book profit or loss.
- **Minimum limit (Art 27)**: Considered only if the base is below adjusted net profit. The base then becomes the lower of (a) undeducted assets plus that difference and (b) adjusted net profit.
- **Loss cases**: A negative base with no adjusted net profit gives no Zakat. A positive base with an adjusted net loss is Zakatable, subject to the maximum limit.

_([ZATCA Zakat General Guideline 1445AH](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Zakat-General-Guideline-Zakat-Collection-1445AH.pdf), sections on forming the base and limits, examples 6, 15, 16, 17 and 18)_

**Years starting before 1 January 2024** follow the earlier regulations, subject to the Resolution's own election rules; this guide does not compute them.


### 3.5 Filing & Payment in Brief

- **Annual Zakat Declaration** — Annual Zakat Declaration via ZATCA portal.
- **Filing due date** — Within 120 days of fiscal year-end (≈ 4 months). For a Gregorian calendar-year taxpayer with FYE 31 December, the deadline is 30 April of the following year.
- **Payment same window** — Payment same window.
- **Advance Zakat instalments** — Advance Zakat instalments (quarterly) may apply for larger taxpayers per ZATCA notice — verify thresholds.
- **Late-payment penalty** — Not confirmed. [ZATCA's Zakat General Guideline 1445AH](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Zakat-General-Guideline-Zakat-Collection-1445AH.pdf) states no late-payment rate; the 5% per month figure formerly here matched no source read. Check the Implementing Regulation before quoting a rate.

## Section 4 — Tier 2: Computation Details

### 4.1 Mixed Entities — Saudi/GCC vs Foreign Split

- **The mechanics** — 1. Compute the entity's Zakat base under §3.4, including the limits. 2. Identify the ownership percentages at FYE (and ideally weighted across the year if changes occurred — verify ZATCA position). 3. Apply the Saudi/GCC share to the base and apply the Zakat rate. 4. Compute the foreign adjusted base and apply 20% CIT (cross-reference sa-corporate-tax). The guideline establishes that the Saudi partner's share is subject to Zakat and the other partner's is not, but the sections read give no worked apportionment, so step 3 is this guide's working method and needs advisor confirmation.
- **Where ownership changes mid-year** — The conservative default is time-apportionment of the base, but ZATCA practice on this point has evolved — verify current circular.
- **Listed companies** — Saudi/GCC-owned float subject to Zakat; foreign-owned float subject to CIT. Practical apportionment usually based on year-end Tadawul shareholder registry, with weighted-average if material movement.

### 4.2 Passive Entities

- **Holding companies — general** — Holding companies whose income is predominantly dividends/interest from subsidiaries face specific Zakat treatment.
- **Investments in establishments in the Kingdom**: A deduction from the Zakat base where the conditions in Art 43 are met.
- **Investments in establishments outside the Kingdom**: A deduction from the Zakat base where the conditions in Art 44 are met. Otherwise not deducted, and added liabilities are corrected (§3.4).
- **Dividend income** — Net adjusted profit adjustments depend on the nature of the source.

The skill flags any holding/passive structure as requiring specialist sign-off (R-SA-Z-4 adjacent).

### 4.3 Financing and Banking Sector Specials

- **Banks** — Statutory deposits with SAMA (Saudi Central Bank), regulatory capital, and specific provisioning rules (ECL / IFRS 9 provisions) interact non-trivially with the Zakat base. Recent ZATCA guidance (post-2020) on financing arrangements affects how Murabaha, Ijarah, and Sukuk are treated in the long-term liability and long-term asset categorisation.
- **Insurers** — Technical reserves, unearned premium reserves, and Takaful pool treatment differ from conventional accounting reserve treatment under the Implementing Regulations.
- **Both sectors** — Out of scope for autonomous computation by this skill — preliminary indicative only; require specialist sign-off (R-SA-Z-4).

### 4.4 Accounting Basis Adjustments

- **Accounting basis** — Saudi entities prepare statements under SOCPA-endorsed IFRS (mandatory for listed companies and large entities; IFRS-SME for smaller). The Zakat computation starts from these statements and applies fiscal adjustments.

**Typical Zakat treatment of items**

| Item | Typical Zakat treatment |
| --- | --- |
| Provisions | Treated as equity and added to the base without limit, also counting in the maximum limit, except a stable debt to non-owners such as end-of-service benefits and leave, which is a liability within the limits of deducted assets (Art 24) |
| Depreciation | Accounting depreciation generally accepted; specific limits per regulations on certain asset classes |
| Partners' debit loans | Deducted only under the criteria in Art 31 |
| Partners' credit loans | Treated by entity type under Art 30 |
| Intangibles (goodwill, brands, software) | A deduction item under Art 50, where its conditions are met |
| Sharia-compliant financing (Murabaha, Ijarah, Sukuk) | Re-characterised per ZATCA guidance; substance-over-form approach |
| Foreign-currency translation differences | Per Implementing Regulations; generally follow accounting treatment |
| Deferred tax assets/liabilities | Deferred tax liability is an added liability; deferred tax asset is a deduction item (Art 29 and the deduction list in §3.4) |

- **Critical flag — 2024-2025 amendments** — Recent amendments to the Implementing Regulations have clarified treatment of certain financing arrangements and intangibles. Every output of this skill MUST include the line: "Treatment of [financing arrangement / intangible item] requires verification against the latest ZATCA circular (2024-2025 amendments to Implementing Regulations)."

## Section 5 — Worked Examples

All 3 examples are illustrative, for the Zakat year ended 31 December 2025G (365 days, rate 2.5777%). They assume every deduction meets its conditions and that current assets exceed current liabilities. The filing deadline is 30 April 2026G.

### 5.1 Example A — 100% Saudi-Owned LLC (Simple Trading Company)

**Example A facts and figures**

| Item | SAR |
| --- | --- |
| Paid-up capital | 5,000,000 |
| Retained earnings (opening) | 3,200,000 |
| Statutory reserve | 500,000 |
| General provisions (no movement in the year) | 200,000 |
| Net book profit after Zakat | 1,600,000 |
| Purchases with no supporting documents, disallowed | 200,000 |
| Adjusted net profit | 1,800,000 |
| Long-term bank loan (Sharia-compliant Murabaha) | 4,000,000 |
| Net book value of fixed assets | 6,500,000 |

- **Equity and its equivalents**: 5,000,000 + 3,200,000 + 500,000 + 200,000 + 1,600,000 = 10,500,000
- **Additions**: 10,500,000 + 4,000,000 + 200,000 = 14,700,000. The loan is below the deducted assets, so all of it is added.
- **Base before limits**: 14,700,000 − 6,500,000 = 8,200,000
- **Maximum limit**: 10,500,000 + 200,000 = 10,700,000, not reached.
- **Minimum limit**: Not considered: the base is above adjusted net profit of 1,800,000.

**Zakat at 2.5777%**: 8,200,000 × 2.5777% = **SAR 211,371.40**

Pay via ZATCA portal. The late-payment rate is unconfirmed (see Section 1).

### 5.2 Example B — 60/40 Saudi/Foreign Mixed Entity

**Facts**: KSA LLC, 60% Saudi national / 40% Cayman-resident shareholder. Same facts as Example A.

**Step 1: Entity base**: as Example A, 8,200,000.

**Step 2 — Saudi/GCC share (60%)** (PROVISIONAL: this guide's working assumption, not a confirmed ZATCA method; see §4.1):
- Provisional Saudi-share base = 8,200,000 × 60% = 4,920,000. ZATCA's Zakat General Guideline 1445AH subjects only the Saudi share to Zakat, but neither it nor ZATCA's 2023 FAQ guideline sets out or works this multiplication of a whole-entity, limit-tested base; the FAQ's one mixed-company answer covers the financing-activity rules only.
- Provisional Zakat at 2.5777% = **SAR 126,822.84**. Do not file on this figure until ZATCA or a Saudi Zakat adviser confirms the apportionment.

**Step 3 — Foreign share (40%) — CIT (see sa-corporate-tax)**:
- Foreign-share taxable profit = 1,800,000 × 40% = 720,000 (with foreign-specific CIT adjustments: *not* the Zakat base method)
- CIT at 20% = **SAR 144,000** (illustrative — see sa-corporate-tax for full adjustments)

**Step 4 — Combined liability (provisional, because Step 2 is)**: Zakat 126,822.84 + CIT 144,000 = **SAR 270,822.84 total**.

Both filed via ZATCA portal within 120 days of FYE. Zakat declaration and CIT declaration are typically filed together as a unified Mixed Entity Declaration.

### 5.3 Example C — Individual Saudi National Sole Trader (Minimum Limit Applies)

**Facts**: Saudi individual operating a sole-trader trading business under a Commercial Registration and holding statutory accounts. Equity at year end SAR 500,000, including net book profit of SAR 430,000. Disallowed expenses SAR 20,000, so adjusted net profit is SAR 450,000. Deductible fixed assets SAR 140,000. Undeducted assets SAR 400,000.

- Base before limits: 500,000 + 20,000 − 140,000 = 380,000, below adjusted net profit, so the minimum limit is considered.
- Minimum limit: the lower of 400,000 + 20,000 = 420,000 and 450,000 = 420,000.
- Maximum limit: 500,000 + 20,000 = 520,000, not reached.
- Zakat at 2.5777%: 420,000 × 2.5777% = **SAR 10,826.34**.
- Personal non-commercial Zakat al-mal on the individual's personal savings/gold/etc. is **outside ZATCA scope** (R-SA-Z-6) — refer to a religious scholar.

## Section 6 — Filing and Payment

### 6.1 Process

- **Filing process steps** — 1. **Register / verify Zakat Number** — taxpayers should be registered with ZATCA at incorporation (Commercial Registration triggers ZATCA registration). 2. **Prepare financial statements** under SOCPA-endorsed IFRS. 3. **Compute Zakat base**: additions less deductions, then the limits in §3.4. 4. **Mixed entities** — also compute CIT for foreign share (cross-reference sa-corporate-tax). 5. **File Zakat Declaration** on the ZATCA portal (https://zatca.gov.sa) — login via taxpayer credentials or licensed representative. 6. **Upload supporting documents** — financial statements, ownership schedule, base computation worksheet. 7. **Pay** via SADAD (Saudi national payments system) or other ZATCA-approved channel within 120 days of FYE. 8. **Obtain Zakat Certificate** (شهادة الزكاة) — required to renew Commercial Registration, bid for government contracts, and clear customs.

### 6.2 Advance Instalments

- **Advance instalments detail** — Larger taxpayers (threshold per ZATCA notice — verify current) may be required to pay quarterly advance Zakat instalments based on prior-year liability, with reconciliation in the annual return. Penalties for missed instalments apply per ZATCA penalty schedule.

### 6.3 Penalties

- **Late payment** — Not confirmed. [ZATCA's Zakat General Guideline 1445AH](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Zakat-General-Guideline-Zakat-Collection-1445AH.pdf) states no late-payment rate; the 5% per month figure formerly here matched no source read. Check the Implementing Regulation before quoting a rate.
- **Failure to file** — variable penalty per ZATCA schedule.
- **Inaccurate return / under-declaration** — ZATCA assessment with penalty (verify current circular).
- **Failure to register** — separate penalty.

### 6.4 Zakat Certificate

- **Uses of Zakat Certificate** — A current-year Zakat Certificate from ZATCA is required to: - Renew the Commercial Registration (annually). - Bid for or be paid on government contracts. - Clear goods through customs (linked to ZATCA's unified ID). - Transfer real estate (interaction with RETT). The certificate is issued upon successful filing and payment.

## Section 7 — Conservative Defaults (Reprise)

When in doubt:

1. **Treat as mixed entity** with foreign-share default — produces both a Zakat number and a CIT number; reviewer can collapse to pure Zakat if pure Saudi ownership is later confirmed.
2. **Use the 365-day rate of 2.5777%** as the default — the most common large-taxpayer filing basis.
3. **For each adjustment**, ask: "Does this increase or decrease the Zakatable base?" Default to the direction that **increases the base** unless a clear regulation or ruling supports the reduction.
4. **Always flag**: "Treatment of [item] requires verification against the latest ZATCA circular (2024-2025 amendments)."
5. **Refuse to finalise** banking/insurance computations — preliminary only; route to a financial-services Zakat specialist.
6. **Refuse to finalise** any return without sign-off by a SOCPA-licensed Zakat advisor.

## Section 8 — Sources

### 8.1 Primary Legislation

- **Primary legislation list** — - Royal Decree No. 17/2/28/8634 of 1370H (1950G) — establishment of the Zakat charge on commercial activity in the Kingdom. - Ministerial Resolution No. 1007 of 19/8/1445H: Implementing Regulation for Zakat Collection, Zakat years starting on or after 1 January 2024. - [ZATCA Zakat General Guideline 1445AH](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Zakat-General-Guideline-Zakat-Collection-1445AH.pdf): ZATCA's guideline on that regulation; the regulation's own text was not separately opened for this guide. - Earlier regulations: Resolution No. 2216 of 7/7/1440H and Resolution No. 2082 of 1438H.

### 8.2 Administering Body

- **ZATCA** — ZATCA — Zakat, Tax and Customs Authority (Hay'at al-Zakat wa al-Dareeba wa al-Jamarik). Formed 2021G from merger of GAZT and Saudi Customs. Portal: https://zatca.gov.sa.

### 8.3 Related Skills

- **Related skills list** — - sa-corporate-tax — CIT 20% on foreign-owned share of mixed entities and on 100%-foreign-owned entities. - sa-wht — Withholding Tax on payments to non-residents. - saudi-arabia-vat — VAT 15% (since July 2020). - saudi-einvoice — FATOORAH e-invoicing. - foundation — OpenAccountants foundation skill.

### 8.4 Verification Discipline

Every output of this skill MUST end with:

> "This Zakat computation is preliminary. The Zakat base is provisional pending verification against the latest ZATCA circular (most recently amended 1446H/2024-2025G affecting financing arrangements and intangibles). The final return MUST be reviewed and signed off by a SOCPA-licensed Zakat advisor or ZATCA-approved consultant before submission to the ZATCA portal."

## End of sa-zakat skill v1.0.

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
