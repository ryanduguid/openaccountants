---
name: nd-corporate-tax
description: North Dakota Corporate Income Tax
jurisdiction: US-ND
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ND Corporate Tax

## North Dakota Corporate Income Tax

North Dakota imposes a graduated corporate income tax under N.D.C.C. Chapter 57-38 (the Income Tax Act of 1981) at three statutory brackets: **1.41% on the first $25,000**, **3.55% on the next $25,000 (to $50,000)**, and **4.31% on income above $50,000** (N.D.C.C. § 57-38-30, confirmed against the current Century Code text; the section imposes exactly these three brackets and has not been amended since the 2015 session). ND does **not** impose a separate corporate franchise tax (contrast NC, TX, DE) and does **not** currently offer a pass-through entity tax (PTET) election — leaving ND S-corp and partnership owners without a federal SALT-cap workaround. The corporation return is **Form 40**, due the 15th day of the 4th month after year-end. ND apportions corporate income using an **equally weighted three-factor formula** — (property + payroll + sales) / 3 — as the statutory default under N.D.C.C. § 57-38.1-09(1), with an elective **100% weighted sales factor** (single sales factor) under § 57-38.1-09(4) for taxpayers that are not passthrough entities. ND is **not** a double-weighted-sales state: the (P + PR + 2S)/4 formula in § 57-38.1-09(2) was available only for the first two tax years beginning after 31 Dec 2015, and the (P + PR + 6S)/8 formula in § 57-38.1-09(3) only for the first tax year beginning after 31 Dec 2017. Both have lapsed. The Oil Extraction Tax (NDCC § 57-51.1) and Oil & Gas Gross Production Tax (NDCC § 57-51) are **severance taxes computed at the well** and are **not** part of the entity-level CIT — they are mentioned here only because new ND practitioners frequently confuse them with corporate income tax. Tax year 2025.

## 1. Scope

This skill covers North Dakota state-level entity-level income tax:

- **Corporate income tax** (N.D.C.C. Chapter 57-38, Income Tax Act of 1981) — imposed on C-corporations doing business in or deriving income from ND sources, including LLCs that have elected federal C-corp treatment under Form 8832 or Form 2553-then-revoked.
- **Apportionment, sourcing, NOL, and estimated-payment rules** as they apply to ND corporate income tax.
- **S-corporation pass-through treatment** (informational only — Form 60 is the ND S-corp return).
- **Partnership / LLC pass-through treatment** (informational only — Form 58 is the ND partnership return).
- **Cross-link only:** Oil Extraction Tax (NDCC § 57-51.1) and Oil & Gas Gross Production Tax (NDCC § 57-51), and Bank of North Dakota's unique exemption (NDCC § 6-09). These are surfaced as **audit flash points** because new ND practitioners confuse them with corporate income tax; the operative computation belongs in dedicated severance / banking skills not yet authored.

**In scope:** Form 40 (Corporation Income Tax Return), Form 40-ES (corporate estimated tax voucher), Form 40-EXT (extension), Form 40-UT (underpayment of estimated tax), Schedule SA (apportionment), Form 60 (S-corp informational), Form 58 (partnership informational), Schedule K-1 (Form 58/60).

**Out of scope (refer elsewhere):**

- ND personal income tax (PIT) — covered by `nd-income-tax.md`. The 2025 PIT is a near-flat structure with a 0% / 1.95% / 2.50% schedule following the rate reductions enacted by HB 1158 (68th Legislative Assembly, 2023).
- ND sales and use tax — covered by `nd-sales-tax.md`.
- Federal corporate income tax (Form 1120) — covered by federal skills.
- **Oil Extraction Tax (5% of gross value at the well, NDCC § 57-51.1)** — severance tax on oil producers, computed at the well on producer's net interest. **NOT** a corporate income tax. Mentioned here only as a refusal / disambiguation.
- **Oil and Gas Gross Production Tax (NDCC § 57-51)** — separate 5% production tax on oil and gas. Also severance, not income tax.
- **Coal Conversion Tax (NDCC § 57-60)**, cigarette/tobacco tax, liquor tax — out of scope.
- **Bank of North Dakota** — the only state-owned bank in the United States, organized under NDCC Chapter 6-09. The bank itself is a state instrumentality and **pays no corporate income tax**. Private banks doing business in ND are subject to the **financial institution privilege tax** under NDCC Chapter 57-35.3, **not** the standard corporate income tax — refusal item, see § 13.
- **Insurance companies** — subject to the gross premiums tax under NDCC § 26.1-03-17, not corporate income tax.
- **Cities and counties** — ND has no local corporate income tax.

> ⚠️ **Authority confirmation rule.** Before relying on a rate, threshold, or form line in production, confirm against the current ND Office of State Tax Commissioner publications (Form 40 Corporate Income Tax Booklet, Schedule SA instructions, and any Commissioner's guidelines). The 1.41% / 3.55% / 4.31% bracket schedule has been stable since 2015 but the Legislative Assembly meets biennially and could amend rates in any odd-year session. Statutes change.

## 2. Metadata and Sources

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | US-ND (North Dakota) |
| Tier | 2 (content) |
| Skill name | `nd-corporate-tax` |
| Version | 0.1 |
| Last updated | 2026-05-28 |
| Verified by | pending |
| Companion skills | `us-tax-workflow-base`, `us-federal-return-assembly`, `nd-income-tax`, `nd-sales-tax` |
| Primary statute | N.D.C.C. Chapter 57-38 (Income Tax Act of 1981) |
| Apportionment statute | N.D.C.C. Chapter 57-38.1 (Uniform Division of Income for Tax Purposes Act / UDITPA) |
| Primary form | Form 40 (Corporation Income Tax Return) |
| Filing agency | North Dakota Office of State Tax Commissioner |
| Tax year covered | 2025 (calendar) |

### Primary sources

1. **N.D.C.C. § 57-38-30** — Corporate income tax rate brackets. Confirmed: § 57-38-30 is the operative rate section and states the three brackets as 1.41% on the first $25,000, 3.55% over $25,000 up to $50,000, and 4.31% over $50,000. § 57-38-30.3 is a different provision and is not the corporate rate section.
2. **N.D.C.C. § 57-38-01.4** — NOL rules; ND adopts federal § 172 by reference subject to ND modifications.
3. **N.D.C.C. Chapter 57-38.1** — Apportionment (UDITPA-derived; property + payroll + sales).
4. **N.D.C.C. § 57-38-08** — Sourcing rules and what constitutes ND-source income.
5. **N.D.C.C. § 57-38-62** — Estimated tax for corporations.
6. **Form 40 Corporation Income Tax Booklet (2025)** — ND Office of State Tax Commissioner.
7. **Form 40 Vendor Version (2025)** — referenced for line-level detail.

## 3. Quick Reference (TY 2025)

**Quick Reference table**  _(NDCC § 57-38-30 / Form 40 instructions)_

| Item | Value | Authority |
| --- | --- | --- |
| Corporate income tax — Bracket 1 | **1.41%** on first $25,000 of ND taxable income | NDCC § 57-38-30 — confirmed |
| Corporate income tax — Bracket 2 | **3.55%** on next $25,000 (to $50,000) | NDCC § 57-38-30 — confirmed |
| Corporate income tax — Bracket 3 | **4.31%** on income above $50,000 | NDCC § 57-38-30 — confirmed |
| Water's edge surtax | Additional **3.5%** of ND taxable income for water's-edge electors; election binds five consecutive tax years | NDCC § 57-38.4-02(3) (confirmed) / Form 40 instructions |
| Apportionment formula | **Equally weighted** three-factor: (property + payroll + sales) / 3. A **100% weighted sales factor election** is available to non-passthrough taxpayers. Not a double-weighted-sales state | NDCC § 57-38.1-09(1) and (4); Form 40 instructions, "Apportionment factor in general" |
| Sourcing | Cost-of-performance for sales other than tangible personal property; ND has **not** adopted market-based sourcing | NDCC § 57-38.1-17 (confirmed against the current chapter text) |
| NOL carryforward | **Follows the federal carryforward period for a loss of like character** (N.D. Admin. Code 81-03-05.1-07(2)): losses arising in tax years before 2018 carry forward 20 years; losses arising in tax years after 2017 carry forward **indefinitely**, matching federal. No carryback for ND loss years beginning after 31 Dec 2002. Do not apply a flat 20-year life to a current-year loss | NDCC § 57-38-01.3(3) (**not** § 57-38-01.4, which is the subchapter S recognition section); N.D. Admin. Code 81-03-05.1-07 |
| NOL 80% taxable-income limitation | **No.** ND does not apply the federal § 172(a)(2)(B) 80% limit. § 57-38-01.3(1)(g) adds back the whole federal NOL deduction and § 57-38-01.3(3) then allows the ND-source NOL with no percentage cap. Neither the statute, N.D. Admin. Code 81-03-05.1-07, nor the Form 40 instructions impose one | NDCC § 57-38-01.3(1)(g), (3) |
| Filing form | Form 40 (Corporation Income Tax Return) | ND Tax Commissioner |
| Due date (calendar-year filer) | **April 15** (15th day of 4th month after year-end) | NDCC § 57-38-34 |
| Extension | Automatic 7-month extension if federal extension filed; Form 40-EXT for ND-only extension | Form 40 instructions |
| Estimated-tax threshold | Required if **both** the current year's estimated liability is expected to exceed $5,000 **and** the prior year's ND net tax liability exceeded $5,000 | NDCC § 57-38-62(2) (confirmed); Form 40 instructions, "Estimated Tax Payments" |
| Estimated-tax form | Form 40-ES | ND Tax Commissioner |
| Underpayment form | Form 40-UT | ND Tax Commissioner |
| PTE election | **None — ND has NOT enacted a PTET.** Chapter 57-38 contains no entity-level election, and the Tax Commissioner's own legislative history for the 2025 (69th) session records only the new employer child care contribution credit (S.B. 2282) | NDCC Ch. 57-38; ND Tax Commissioner, *Corporate Income Tax History* |
| Separate franchise tax? | **No.** ND has no general corporate franchise tax. | n/a |
| Minimum tax? | **None.** No statutory minimum CIT (unlike NC's $200 franchise floor). | n/a |
| S-corp at entity level? | No CIT; files Form 60. **Exception:** an S corporation that was subject to the pre-2013 financial institution tax and elected under N.D.C.C. § 57-38-01.35 to be taxed as a C corporation files Form 40, on paper | NDCC §§ 57-38-01.4, 57-38-01.35 |
| Partnership / LLC default at entity level? | No CIT; files informational Form 58 | NDCC Chapter 57-38 |

## 4. Who's Subject

**Who's Subject table**

| Entity Type | Subject to ND CIT? | Form |
| --- | --- | --- |
| C-corporation (ND-domiciled or foreign doing business in ND) | YES — Form 40 | Form 40 |
| LLC electing C-corp treatment (federal Form 8832) | YES — Form 40 | Form 40 |
| LLC electing S-corp treatment (federal Form 2553) | NO at entity level; informational only | Form 60 |
| S-corporation (federal § 1362 election in effect) | NO at entity level; informational only | Form 60 |
| Multi-member LLC, default partnership | NO at entity level; informational only | Form 58 |
| Single-member LLC, disregarded | NO at entity level; owner reports on Form ND-1 or Form 40 if owner is a corp | none (flows to owner) |
| Limited partnership (LP) | NO at entity level; informational only | Form 58 |
| Nonprofit § 501(c)(3) corporation | NO if exempt under federal § 501; UBI subject to CIT | Form 40 if UBTI |
| Insurance company | NO (gross premiums tax instead) | NDCC § 26.1-03-17 |
| Bank of North Dakota | NO (state instrumentality) | NDCC Chapter 6-09 |
| Private bank / financial institution | NO standard CIT — subject to **financial institution privilege tax** | NDCC Chapter 57-35.3 |

### 4.1 Federal S-election automatically applies in ND

- **Federal S-election carries automatically to ND** — ND mirrors federal Subchapter S treatment under NDCC § 57-38-01.4. A federal S-corp election under IRC § 1362 automatically carries to North Dakota; there is no separate ND S-election and no separate S-revocation form. Shareholders of ND S-corps pay ND personal income tax on their pro-rata share of ND-source income at the standard PIT rates (covered in `nd-income-tax.md`).  _(NDCC § 57-38-01.4)_

### 4.2 LLCs electing C-corp — the same trap as elsewhere

- **LLC C-corp election binding for ND** — An LLC that affirmatively elects C-corp treatment by filing federal Form 8832 (or Form 2553 then revoked) becomes a Form 40 filer for ND purposes. The election is binding for ND. Practitioners should verify the federal election before assuming a multi-member LLC is on Form 58.  _(Form 40)_

### 4.3 Nexus

- **ND nexus criteria** — The tax is imposed "with respect to its North Dakota income ... received by every corporation **doing business in this state**" (N.D.C.C. § 57-38-11), and reaches "only that portion of a corporation's taxable income which is derived from or attributable to sources within this state" (Form 40 instructions, *Method of Corporation Taxation*). ND has **not** codified a bright-line factor-presence dollar threshold for corporate income tax — do not quote MTC factor-presence numbers as ND law. P.L. 86-272 immunity is recognised and worked through the apportionment rules (N.D. Admin. Code 81-03-09-26 et seq., which include immune-state sales in the denominator). Note that §§ 57-38-12 and 57-38-13, the old corporate allocation sections, were **repealed in 2003**; allocation and apportionment now run entirely through Ch. 57-38.1 by way of § 57-38-01.3(1)(e). N.D.C.C. § 57-38-08 is *Partnerships not subject to tax* and is not a corporate nexus provision.  _(N.D.C.C. § 57-38-11; Form 40 instructions)_

### 5.1 Graduated brackets — TY 2025

**Graduated brackets table**  _(N.D.C.C. § 57-38-30)_

| ND Taxable Income | Marginal Rate | Cumulative Tax at Top of Bracket |
| --- | --- | --- |
| $0 – $25,000 | **1.41%** | $352.50 |
| $25,001 – $50,000 | **3.55%** | $352.50 + 3.55% × (income − $25,000); $1,240 at $50,000 |
| Above $50,000 | **4.31%** | $1,240 + 4.31% × (income − $50,000) |

**Effective-rate examples table**  _(N.D.C.C. § 57-38-30)_

| ND Taxable Income | ND CIT | Effective Rate |
| --- | --- | --- |
| $10,000 | $141 | 1.41% |
| $25,000 | $352.50 | 1.41% |
| $50,000 | $1,240 | 2.48% |
| $100,000 | $3,395 | 3.40% |
| $500,000 | $20,635 | 4.13% |
| $1,000,000 | $42,185 | 4.22% |
| $5,000,000 | $214,685 | 4.29% |

The brackets are **not** indexed for inflation. The $25,000 and $50,000 thresholds and the 1.41% / 3.55% / 4.31% rates have been unchanged since the 2015 legislative session, when rates were cut by roughly 5% to the current range — confirmed against the ND Tax Commissioner's own *Corporate Income Tax History*, whose most recent entry (2025 session) records a new employer child care contribution credit and no rate or bracket change.

### 5.2 Water's-edge surtax (NDCC § 57-38.1-15)

- **Water's-edge surtax** — A corporation otherwise required to file a worldwide unitary combined report may elect the water's edge method instead, on the return as **originally filed**, binding for **five consecutive tax years**. Every corporation covered by the election is then subject to an additional **3.5% surtax** on its ND taxable income (N.D.C.C. § 57-38.4-02(3)). The election trades broader inclusion of foreign affiliates for a flat 3.5% surcharge, so it only pays where the excluded foreign income exceeds the surtax on what remains. Electors must still include foreign dividends and 80/20-corporation income in the water's-edge group — for tax years beginning after 31 Dec 1994 every elector may use the **30%** inclusion for both (§ 57-38.4-02(2)(c)). A taxpayer and its affiliates are **presumed** unitary and their income presumed apportionable, and the taxpayer carries the burden of proof on membership of the water's-edge group (§ 57-38.4-04). Most US-only ND filers do not need to think about this; it matters only for groups with foreign affiliates. The surtax has no connection to the sales factor weighting election.  _(N.D.C.C. §§ 57-38.4-02, 57-38.4-04; Form 40 instructions, "Water's Edge Election")_

### 5.3 No minimum tax

- **No minimum tax** — Unlike NC ($200 franchise tax floor), CA ($800 LLC tax / franchise tax), or TX ($0 below the no-tax-due threshold), ND imposes no minimum corporate income tax. A C-corp with zero ND taxable income (e.g., a loss year or an entity with zero ND apportionment) owes $0 in ND CIT. The corporation must still file Form 40 to report the zero, but it owes nothing.  _(n/a)_

### 5.4 No separate franchise tax

- **No separate franchise tax** — ND has no general corporate franchise tax. The only entity-level taxes that apply to a typical ND C-corp are: 1. Corporate income tax under NDCC § 57-38-30 (this skill). 2. Sales/use tax on its purchases and (if a seller) on its sales (`nd-sales-tax.md`). 3. Payroll taxes on its employees (federal + ND state unemployment). 4. Real and personal property tax at the county/city level (not in scope). 5. Any industry-specific tax (e.g., oil extraction tax for producers). The absence of a franchise tax means an ND C-corp at the $0 income / loss-year extreme owes nothing at the entity level — a notable contrast with NC, TX, DE, and CA, where a loss-year C-corp still owes a franchise / privilege tax minimum.  _(n/a)_

### 6.1 Three-factor formula — default

- **Three-factor apportionment formula** — Apportionment = (Property Factor + Payroll Factor + Sales Factor) / 3. The three factors are **equally weighted**; ND is not a double-weighted-sales state. The Form 40 instructions state it directly: "In general, the apportionment factor is a product of a formula consisting of an equally weighted three-factor (property, payroll, and sales) apportionment." Where a factor's denominator is zero, that factor is excluded from the calculation, and a corporation holding an interest in a passthrough entity includes its proportionate share of that entity's factors. Ratios are carried to six decimal places.  _(N.D.C.C. § 57-38.1-09(1); N.D. Admin. Code 81-03-09-14; Form 40 instructions)_
- **Factor definitions** — The sales factor is double-weighted by default — i.e., the denominator is 4 (one each for property, payroll, and two for sales). This is the standard UDITPA "modified" formula widely adopted by states that have not moved to single sales factor. Each factor is: - Property factor = ND tangible property (owned at original cost + rented × 8) ÷ everywhere tangible property. - Payroll factor = ND wages and salaries ÷ everywhere wages and salaries. - Sales factor = ND-sourced sales (gross receipts) ÷ everywhere sales.  _(N.D.C.C. § 57-38.1-09)_

### 6.2 Single-sales-factor election (optional)

- **Sales factor weighting election (100% weighted sales factor)** — ND calls this the *sales factor weighting election*, not a "single sales factor election", and it lives at **N.D.C.C. § 57-38.1-09(4)** (tax years beginning after 31 Dec 2018), implemented by **N.D. Admin. Code Ch. 81-03-09.2**. Mechanics, all confirmed against the rule and the Form 40 instructions: - Available to a taxpayer that is **not a passthrough entity**; a passthrough entity may not make the election itself, though a corporate partner's election covers its share of the passthrough's factors. A sole proprietor apportioning under N.D.C.C. § 57-38-04(5) may elect by attaching a statement to the individual return. - Made by marking the box on **Schedule FACT, line 15a** (or Schedule CR, Part II, line 15a for a consolidated or combined filing) on an **original, timely filed** return, including extensions. - Applies to **every** company in the unitary group and to all companies on a consolidated ND return; an affiliate joining the group afterwards is treated as having consented. - **Binding for five consecutive tax years** starting with the election year. An election made on the sixth-year return is a fresh five-year election (years six through ten). If no new election is made for year six, the equally weighted three-factor formula must be used for **at least three tax years** before another election can be made. - **Rescinded automatically** — no Commissioner consent is involved — where more than 50% of the taxpayer's voting stock is acquired by a nonaffiliated entity, where a reorganisation or spinoff leaves it outside the unitary group, or on complete liquidation. A taxpayer whose election is rescinded may make a new election in the first tax year following the rescission. - The election is **unrelated to** the water's-edge election; making one says nothing about the other. - Generally beneficial for ND-headquartered manufacturers and oil/gas producers with substantial ND payroll and property but sales delivered nationally.  _(N.D.C.C. § 57-38.1-09(4); N.D. Admin. Code 81-03-09.2-02 to 81-03-09.2-04; Form 40 instructions, "Sales Factor Weighting Election")_

### 6.3 Special industries

**Special industries apportionment table**  _(N.D. Admin. Code Ch. 81-03-09, adopted under N.D.C.C. § 57-38.1-18)_

ND's special-industry rules are the MTC-model ones and sit in the **administrative code**, not in Chapter 57-38.1 — that chapter is plain UDITPA and ends at § 57-38.1-21. Each rule **modifies the property, payroll and sales factors** within the standard three-factor formula; none of them replaces the formula with a bespoke single-factor method. Making a sales factor weighting election is not precluded by being in one of these industries.

| Industry | Apportionment Method | Citation |
| --- | --- | --- |
| Railroads | Standard three factors with modified definitions (rented property at 8× net annual rent; car-day and track-mile style modifications) | N.D. Admin. Code 81-03-09-35 |
| Trucking companies (motor common, contract and express carriers) | Standard three factors with mileage-based modifications to the property, payroll and sales factors | N.D. Admin. Code 81-03-09-37 |
| Airlines | Standard three factors with modifications keyed to cost of aircraft by type, departures and revenue tons | N.D. Admin. Code 81-03-09-36 |
| Television and radio broadcasting | Standard three factors with audience/subscriber-based sales-factor modification | N.D. Admin. Code 81-03-09-38 |
| Publishing | Standard three factors with circulation-based sales-factor modification | N.D. Admin. Code 81-03-09-39 |
| Financial institutions | **File Form 40 and pay CIT.** Special property and sales factor provisions apply, identical to those that applied under the repealed financial institution tax (Form 35, tax years before 2013). Loans and receivables go on the "Other assets" line of the property factor with a supporting schedule | N.D. Admin. Code Ch. 81-03-09.1 |

> The separate financial institution privilege tax under N.D.C.C. Ch. 57-35.3 applied only to tax years **before 2013**. Do not tell a bank or credit union client that it is outside the corporate income tax on that basis.

### 6.4 NOL interaction with apportionment

- **NOL post-apportionment tracking** — Apportionment is applied after ND modifications to federal taxable income but before the ND NOL deduction. The ND NOL operates on a post-apportionment basis; it is tracked in ND-apportioned dollars, not pre-apportionment federal dollars.

### 6.5 Alternative apportionment

- **Alternative apportionment petition** — A taxpayer (or the Commissioner) may petition for an alternative apportionment method under NDCC § 57-38.1-18 if the statutory formula does not "fairly represent" the corporation's ND activity. As elsewhere, taxpayer-initiated alternative apportionment is rarely granted; the Commissioner more often imposes combined / unitary computation against an aggressive separate-entity filer.  _(NDCC § 57-38.1-18)_

### 7.1 Sales of tangible personal property — destination

- **Destination sourcing rule** — Sales of tangible personal property are sourced to ND if the property is delivered or shipped to a purchaser within ND, regardless of FOB terms (NDCC § 57-38.1-16). This is the standard UDITPA destination rule.  _(NDCC § 57-38.1-16)_

### 7.2 Sales of services — cost of performance (with caveats)

- **Cost-of-performance sourcing for services** — Confirmed against the current text of N.D.C.C. § 57-38.1-17: sales other than sales of tangible personal property are in ND if "the income-producing activity is performed in this state" or is performed both in and outside ND "and a greater proportion of the income-producing activity is performed in this state than in any other state, **based on costs of performance**." This is unmodified UDITPA § 17; ND has not adopted market-based sourcing. This is a meaningful divergence from NC, CA, MA, IL, and 30+ other states that have moved to market-based sourcing. ND-headquartered service providers selling nationally are **disadvantaged**, not helped, by cost-of-performance: ND payroll and overhead generate ND-sourced receipts even where the customer is out of state, which pushes the sales-factor numerator up. The planning point runs the other way — an out-of-state service provider selling *into* ND generally sources those receipts away from ND.

  > ⚠️ **Audit flash point.** Re-read § 57-38.1-17 each filing season. Several Plains-region states (Iowa, Missouri) have moved to market sourcing, and a shift here would reverse the direction of the planning above.  _(N.D.C.C. § 57-38.1-17; UDITPA § 17)_

### 7.3 Oil and gas — extraction at the well, not income tax

- **Oil and gas severance tax disambiguation** — This is the single most important sourcing disambiguation for new ND practitioners. The Oil Extraction Tax (NDCC Ch. 57-51.1) and the Oil & Gas Gross Production Tax (NDCC Ch. 57-51) are severance taxes imposed on the value of oil and gas at the wellhead. They are paid by the producer (or first purchaser) based on the volume × price × statutory rate (typically 5% each, so combined ~10% on oil and ~5% on gas at the well). The taxes are administered by the ND Tax Commissioner's Oil and Gas Tax Section. These taxes are not ND corporate income tax. They are NOT: - Computed on ND apportioned taxable income. - Reduced by ND NOL carryforwards. - Filed on Form 40. - Within the scope of this skill. For a C-corp producer doing business in ND, the oil extraction and gross production taxes are paid separately (different forms, different schedules) and are deductible in computing federal taxable income (and thus ND taxable income, as ND starts from federal taxable income). The producer also files Form 40 reporting ND apportioned income from its production activity (after deducting the severance taxes federally). A common practitioner error is to attempt to claim ND CIT credits for oil extraction tax paid, or to net the extraction tax against CIT liability. There is no such credit. They are separate tax regimes.  _(NDCC Ch. 57-51.1 / NDCC Ch. 57-51)_

### 7.4 Sourcing for SaaS and intangibles

- **SaaS and intangibles sourcing** — ND has **no** statute or rule that speaks to SaaS by name. § 57-38.1-16 governs *local tangible personal property sales* and does not reach it; the operative provision is the residual rule in **§ 57-38.1-17**, so SaaS and licence receipts fall to be sourced by cost of performance like any other non-TPP sale, with § 57-38.1-18 (and N.D. Admin. Code 81-03-09-32 to 81-03-09-34) available to either party if that does not fairly represent ND activity. Non-business income from intangibles is *allocated* to the commercial domicile under §§ 57-38.1-07 and 57-38.1-08, which is a different question from apportioning business receipts and should not be conflated with it. This remains an under-developed area in ND guidance and is a frequent grey zone in practice.  _(N.D.C.C. §§ 57-38.1-07, 57-38.1-08, 57-38.1-17, 57-38.1-18)_

### 8.1 Regime

- **NOL regime parameters** — The ND corporate NOL is a **state-law creature**, not federal § 172 adopted by reference. § 57-38-01.3(1)(g) **adds back in full** the federal NOL deduction taken in arriving at federal taxable income (Schedule SA, line 1), and § 57-38-01.3(3) then allows a deduction for the ND-source NOL (Form 40, page 1, line 12). Confirmed parameters: - **Carryforward period:** the same period a federal loss of like character may be carried forward — 20 years for losses arising in tax years beginning before 2018, **indefinite** for losses arising after 2017. Do not apply a flat 20-year life to a current-year loss. - **Carryback:** not permitted for ND loss years beginning after **31 Dec 2002** — this predates TCJA by fifteen years and is not federal conformity. Capital losses must still be carried back and then forward. - **No 80% of taxable income limitation.** Neither § 57-38-01.3(3), nor N.D. Admin. Code 81-03-05.1-07, nor the Form 40 instructions imposes a percentage cap, and the federal § 172(a)(2)(B) limit does not travel to a deduction ND grants itself. The practical ceiling is simply ND income after exemptions on line 11. - **Computed after allocation and apportionment** — the ND NOL is a post-apportionment ND figure, not the pre-apportionment federal NOL. - **Belongs to the FEIN that incurred it.** An ND NOL may only be used by the corporation that incurred it, whatever its later ND activity or filing method. The ND NOL of the non-surviving corporation in a merger, liquidation or dissolution is **forfeited**, and a corporation that has elected to become a disregarded entity cannot transfer its NOL. - **No dedicated ND NOL schedule.** Attach a worksheet showing the accumulated ND loss by year less any previously deducted loss. Combined-report filers enter the carryforward for all corporations listed on Schedule CR.  _(N.D.C.C. §§ 57-38-01.3(1)(g), 57-38-01.3(3), 57-38-40(3); N.D. Admin. Code 81-03-05.1-07; Form 40 instructions, lines 11-12 and Schedule SA line 1)_

### 8.2 Ownership-change limitations (§ 382)

- **Ownership-change limitations — ND departs from the federal pattern** — Do not carry a federal § 382 analysis straight into ND. **N.D. Admin. Code 81-03-05.1-07(3)** provides that where a corporation does **not** file an ND consolidated return, its ND NOL "may be carried forward even if ... the ownership of the corporation in the loss year is not the same as the ownership in each of the years to which the loss is carried, e.g., the corporation is acquired by another corporation" — and even if the filing method changed (separate-entity in the loss year, combined in the carry year, or the reverse). An ND-only acquired corporation can therefore keep the full ND carryforward in circumstances where its federal NOL is § 382-limited. Two limits remain: for a corporation filing an **ND consolidated return**, subsection (4) requires the NOL to be computed corporation-by-corporation and used only against that corporation's own ND taxable income; and under subsection (6) and the Form 40 instructions, a corporation dissolved as a separate corporate entity loses the carryforward outright.

  > ⚠️ **AUDIT FLASH POINT** — this cuts both ways. A practitioner who applies a federal § 382 limitation to the ND return overstates ND tax; one who assumes ND freely follows the loss into a consolidated group understates it.  _(N.D. Admin. Code 81-03-05.1-07(3), (4), (6))_

### 8.3 Interaction with rate stability

- **NOL value stability** — Unlike NC (whose CIT rate is phasing to 0% by 2030, eroding NOL value), ND CIT rates have been stable since 2015. An ND NOL carryforward holds its value across years — there is no rate-arbitrage planning lever analogous to the NC scenario. The only NOL planning is the standard "use it before it expires" check and the § 382 limitation if ownership changes.

## 9. PTE Election — **Absent in North Dakota**

### 9.1 Current status (TY 2025)

- **No PTET enacted** — North Dakota has NOT enacted a Pass-Through Entity Tax (PTET) election as of the 2025 tax year. Chapter 57-38 contains no entity-level election for S corporations or partnerships, and the ND Tax Commissioner's own *Corporate Income Tax History* records no such measure. ND remains in the small group of broad-based income tax states without a PTET workaround for the federal SALT cap; practitioner surveys generally list Delaware and Pennsylvania alongside it, though those peer lists move year to year and should not be quoted to a client as fixed.

### 9.2 Legislative history

- The 67th Legislative Assembly (2021) did not enact a PTET despite the federal SALT-cap workaround trend.
- The 68th Legislative Assembly (2023) considered tax reform broadly but did not enact a PTET.
- The 69th Legislative Assembly (2025) adjourned sine die without enacting a PTET. The only corporate income tax measure the Tax Commissioner records for that session is **S.B. 2282**, creating an employer child care contribution income tax credit — 50% of the first $1,000 of child care contributions per employee, effective for tax years beginning in 2025 (N.D.C.C. § 57-38-01.42). Rates and brackets were untouched.

### 9.3 Practical consequences for ND pass-through owners

- **SALT cap exposure for ND pass-through owners** — ND S-corp shareholders and ND partnership/LLC members cannot elect entity-level taxation to escape the federal $10,000 SALT cap on their personal Schedule A. Their ND personal income tax remains a personal itemized deduction subject to the cap. For a high-income ND S-corp owner this is a meaningful federal tax disadvantage relative to peers in NC, CA, NY, MN, or any of the ~37 states that have enacted PTETs. A 2025 owner with $1,000,000 of ND S-corp income paying ~$25,000 of ND personal income tax has no SALT-cap workaround — the $25,000 is capped at $10,000 on Schedule A, costing roughly $5,550 in federal tax at the 37% marginal bracket compared with a PTET-eligible state.

### 9.4 OBBBA (2025) interaction

- **OBBBA SALT cap interaction** — The federal SALT cap was modified by the One Big Beautiful Bill Act (P.L. 119-21, July 4 2025) — relevant for years 2025 and onward. OBBBA § 70120 raised the cap from $10,000 to **$40,000** for 2025 ($20,000 MFS), indexed by 1% a year through 2029 (**$40,400** for 2026), phasing down by 30% of MAGI above $500,000 ($505,000 for 2026) but never below $10,000, and reverting to $10,000 for tax years beginning after 2029. Even with that relief, the absence of a ND PTET means ND owners cannot capture entity-level federal-deductible state-tax payments in the way that PTET-state owners can. This continues to be a competitive disadvantage for the ND professional-services and small-corporation sector.  _(P.L. 119-21)_

### 9.5 Planning workaround alternative

- **C-corp conversion workaround** — The principal practitioner workaround in a non-PTET state like ND is: - C-corp conversion analysis. For owners who can tolerate two layers of tax, converting an S-corp to a C-corp captures the corporate ND CIT (top bracket 4.31%) as a federal Form 1120 deductible item (no SALT cap applies to corporate state-tax deductions). The 21% federal corporate rate + 4.31% ND blended into an effective ~25% on the corp side may be worse or better than pass-through depending on owner's federal bracket and dividend distribution policy. The C-corp election is rarely beneficial purely for SALT-cap reasons — but in ND it is the only entity-level workaround. Practitioners should consult `us-s-corp-election-decision.md` and run the C-corp vs. S-corp model annually for high-income ND owners.

### 10.1 Forms

**Forms table**

| Form | Used By | Purpose |
| --- | --- | --- |
| Form 40 | C-corps and LLCs taxed as C-corps | ND Corporation Income Tax Return |
| Form 40-ES | All Form 40 filers above threshold | Quarterly estimated payment voucher |
| Form 40-EXT | All Form 40 filers needing extension | Application for extension (if not relying on federal extension) |
| Form 40-UT | All Form 40 filers underpaying | Underpayment of Estimated Income Tax |
| Schedule SA | All Form 40 filers | **Statutory adjustments** — additions to and subtractions from federal taxable income (line 1 adds back the federal NOL deduction) |
| Schedule FACT | Form 40 filers apportioning income | **Apportionment factor** schedule (property, payroll, sales). The 100% weighted sales factor election is made by marking line 15a |
| Schedule CR | Members of a unitary group filing a combined report | Combined report — Part II carries the group apportionment factor (election box at Part II, line 15a) |
| Schedule TC | Filers claiming credits | Tax credits |
| Schedule WE / WW | Water's-edge and worldwide filers | Water's-edge group and worldwide group income |
| Form 40-QR | Corporations overpaying estimates by more than $500 | Quick refund of overpaid estimated tax (filed after year-end and before the 15th day of the 4th month) |
| Form 40X | Any Form 40 filer amending | Amended Corporation Income Tax Return |
| There is **no** ND schedule dedicated to NOL tracking | Form 40 filers with an NOL | Attach a worksheet showing the accumulated ND loss by year less any previously deducted loss; the deduction is taken on Form 40, page 1, line 12 |
| Form 60 | S-corps (informational) | ND S-Corporation Income Tax Return |
| Schedule K-1 (Form 60) | S-corps | Shareholder's share of ND income |
| Form 58 | Partnerships and multi-member LLCs (informational) | ND Partnership Return |
| Schedule K-1 (Form 58) | Partnerships | Partner's share of ND income |

### 10.2 Due dates

- **Due dates and extension rules** — - Calendar-year filers: April 15 of the year following the tax year (15th day of the 4th month after year-end). - Fiscal-year filers: 15th day of the 4th month after the close of the fiscal year. - Extension: If a federal extension (Form 7004) is filed, ND automatically grants the same extension — no separate ND extension is required. If no federal extension is filed, a corporation may request a 7-month ND-only extension on Form 40-EXT. Extension extends time to file, not time to pay; interest and underpayment penalty run from the original due date.  _(NDCC § 57-38-34)_

### 10.3 Estimated payments — Form 40-ES

- **Estimated payment requirement** — Under N.D.C.C. § 57-38-62(2) a corporation must make quarterly estimated payments if **both** of the following hold: - its estimated tax for the current year can reasonably be expected to exceed **$5,000**, **and** - its ND net tax liability for the immediately preceding year exceeded **$5,000**.

  Fail either limb and no estimates are required — Form 40-UT says so twice on its face ("If $5,000 or less, do not complete form" against both the current-year and prior-year lines).

  **Instalment due dates — the fourth one is not in the tax year.** Instalments are due on the 15th day of the **4th, 6th and 9th months of the taxable year, and the 15th day of the first month of the following taxable year** (N.D.C.C. § 57-38-63; Form 40-UT column headings). For a calendar-year filer that is **15 April, 15 June, 15 September and 15 January**. It is *not* the federal 4/6/9/12 corporate pattern, and treating the fourth instalment as due in December will not produce a wrong payment but will misstate the interest run for anyone reconstructing a late year.

  **Safe harbour.** Each instalment is 25% of the *lesser* of 90% of the current year's net tax liability or 100% of the prior year's net tax liability (§ 57-38-62(2)(a)-(b); Form 40-UT line 4). No interest is due if the corporation instead uses the annualised income or adjusted seasonal instalment method under IRC § 6655(e), computed as for federal Form 2220, which must be attached (§ 57-38-62(3); Form 40-UT line 10).

  **Overpayments** may be applied to the following year's estimates and, absent an election to a specific instalment, are applied to the first (§ 57-38-62(6)). A **quick refund** of overpaid estimates is available on **Form 40-QR** where the expected overpayment exceeds **$500**, filed after year-end and before the 15th day of the 4th month (§ 57-38-64).  _(N.D.C.C. §§ 57-38-62 to 57-38-64; Form 40 and Form 40-UT instructions)_

**Quarterly installment schedule table**

| Installment | Due Date | Cumulative % |
| --- | --- | --- |
| 1st | April 15 | 25% |
| 2nd | June 15 | 50% |
| 3rd | September 15 | 75% |
| 4th | December 15 | 100% |

### 10.4 Safe harbor

- **Underpayment safe harbor** — The underpayment penalty (Form 40-UT) is avoided if the corporation has paid at least the lesser of: 1. 100% of the prior year's tax liability, OR 2. 90% of the current year's tax liability. The prior-year safe harbor is not available if the corporation had no liability or did not file a return in the prior year, or if the prior tax year was a short period.

### 10.5 Penalties and interest

- **Penalties and interest schedule** — All of the following are confirmed against the current text of N.D.C.C. § 57-38-45 and the 2025 Form 40 instructions. **ND does not have federal-style accuracy penalties — there is no 20%/25% negligence penalty and no 75% civil fraud penalty in Chapter 57-38.** Do not quote IRC §§ 6662/6663 figures at an ND assessment.

  - **Late filing:** 5% of the net tax liability or $5, whichever is greater, for the month the return is due, plus a further 5% for each additional month or fraction, capped at **25%** (§ 57-38-45(2)(b)).
  - **Late payment:** 5% of the unpaid tax or $5, whichever is greater (§ 57-38-45(2)(a)), plus interest.
  - **Interest on late tax:** 1% per month or fraction, excluding the month the tax became due (§ 57-38-45(1)(b)). Where an **extension** was obtained, interest runs at **12% per annum** through the later of the extended due date or the date paid, and at 1% per month thereafter (§ 57-38-45(1)(a)).
  - **Underpayment of estimated tax:** interest only — the penalty provisions of § 57-38-45 are expressly **disapplied** to estimated tax by § 57-38-62(3). It is computed on **Form 40-UT** at a fixed statutory **12% per annum** from each instalment due date to the earlier of payment or the unextended due date of the return (Form 40-UT, line 8), and carried to Form 40, line 24b. The rate is fixed in the form and statute; it is **not** reset semi-annually by the Commissioner.
  - **Intent to evade:** a civil penalty of not more than **$1,000**, recovered by the attorney general, plus a class A misdemeanour (§ 57-38-45(3)).
  - **Refusal to file after notice:** the Commissioner may determine income from the best information available and assess tax at **not more than double** that amount, plus the usual interest and penalty (§ 57-38-45(6)).
  - **Corporate failure to file after 30 days' notice:** up to **$500** per failure (§ 57-38-45(7)).
  - The Commissioner **may waive** all or part of any civil penalty or interest for good cause (§ 57-38-45(5)).

  Interest also runs **in the taxpayer's favour** at 1% per month on an overpayment, beginning 45 days after the later of the unextended due date or the date the return is filed and deemed complete.  _(N.D.C.C. §§ 57-38-45, 57-38-62(3); 2025 Form 40 and Form 40-UT instructions)_

### 10.6 Combined and unitary reporting

- **Combined and unitary reporting requirement** — ND's default is **worldwide** unitary combined reporting. The Form 40 instructions put it flatly: "A corporation engaged in a unitary business with one or more corporations (**irrespective of the country or countries in which the corporations conduct business**) must file using the combined report method." N.D.C.C. § 57-38.4-02 then frames the water's-edge election as the alternative — "a corporation required to file a worldwide unitary combined report must do so unless it elects to apportion its income using the water's edge method."

  **A unitary business** is a group of corporations transferring value among themselves through unities of ownership, operation and use. *Unity of ownership* means common control by a single corporation that is itself a group member, owning directly or indirectly **more than 50%** of the voting stock. Where unity of ownership exists, unity of operation and use are **presumed** if the activities are in the same general line of business, constitute different steps in a vertically structured enterprise, or the group is characterised by centralised management. The group files a combined report on **Schedule CR**, with each factor's denominator carrying the everywhere amounts for all corporations in the report, intercompany transactions and allocable-income amounts excluded.

  Practitioners migrating from separate-return states (NC's default is separate-entity) must affirmatively analyse unitary status for any multistate ND filer — and, for any group with foreign affiliates, must reach the water's-edge question at § 5.2 rather than assuming a US-only group.

  Note the citation: **§ 57-38.1-19 is not a combined-reporting provision** — it is the UDITPA construction clause ("This chapter must be so construed as to effectuate its general purpose to make uniform the law of those states which enact it"). The authorities are Ch. 57-38.4, N.D. Admin. Code 81-03-09-08, and the Form 40 instructions.  _(N.D.C.C. Ch. 57-38.4; N.D. Admin. Code 81-03-09-08; Form 40 instructions, "Method of Corporation Taxation")_

### 11.1 Example A — Small all-ND C-corp at the lowest bracket

**Facts.** Prairie Print Shop, Inc. is a Bismarck-domiciled C-corp providing commercial printing. Calendar-year filer. For 2025:

- Federal taxable income (Form 1120, line 30): $20,000
- ND additions: $0
- ND subtractions: $0
- 100% of activity (property, payroll, sales) in ND. Apportionment factor: 1.0000.
- No NOL carryforward.

**Step 1 — ND taxable income (2025):**

```
Federal taxable income            20,000
+ ND additions                         0
- ND subtractions                      0
= Pre-apportionment income        20,000
× ND apportionment factor         1.0000
= ND apportioned income           20,000
- NOL deduction                        0
= ND taxable income               20,000
```

**Step 2 — ND corporate income tax (bracket 1 only):**

```
$20,000 × 1.41% = $282.00
```

**Step 3 — Estimated-tax obligation:**

```
$282 prior-year < $5,000 threshold → no estimated payments required for 2026.
```

**Step 4 — Total 2025 ND tax:**

```
ND CIT       $282.00
(No franchise tax in ND)
Total        $282.00
```

**Takeaway.** A small ND C-corp at the lowest bracket owes a few hundred dollars. There is no minimum tax, no franchise tax, and no required estimated payments below the $5,000 threshold. This is dramatically simpler than NC, CA, TX, or DE, where even a tiny C-corp owes hundreds in franchise / minimum tax annually.

### 11.2 Example B — Mid-size C-corp with multistate apportionment (ND + MN + MT)

**Facts.** Red River Equipment, Inc. is a Fargo-domiciled C-corp selling agricultural equipment across the Plains. Calendar 2025:

- Federal taxable income: $2,000,000
- ND additions: $50,000 (state taxes deducted federally)
- ND subtractions: $10,000 (federal bonus depreciation timing)
- No NOL carryforward.

**Step 1 — Three-factor formula (sales double-weighted):**

```
Apportionment = (0.5000 + 0.6000 + 2 × 0.4000) / 4
              = (0.5000 + 0.6000 + 0.8000) / 4
              = 1.9000 / 4
              = 0.4750
```

**Step 2 — ND taxable income:**

```
Federal taxable income          2,000,000
+ ND additions                     50,000
- ND subtractions                 (10,000)
= Pre-apportionment income      2,040,000
× ND apportionment factor          0.4750
= ND apportioned income           969,000
- NOL deduction                         0
= ND taxable income               969,000
```

**Step 3 — ND CIT (graduated brackets):**

```
Bracket 1: $25,000  × 1.41% = $   352.50
Bracket 2: $25,000  × 3.55% = $   887.50
Bracket 3: $919,000 × 4.31% = $39,608.90
                              ----------
Total ND CIT                  $40,848.90
```

**Step 4 — Counterfactual: single-sales-factor election**

If Red River had previously elected single-sales-factor apportionment:

```
Apportionment = 0.4000 (sales only)
ND apportioned income = 2,040,000 × 0.4000 = 816,000
ND CIT:
  Bracket 1 / 2:                     $1,240.00
  Bracket 3: 766,000 × 4.31% =     $33,014.60
  Total                            $34,254.60

Saving from single-sales-factor:    $6,594.30
```

The single-sales election saves ~$6,600 annually because Red River has heavy ND payroll and property relative to ND sales — the classic ND-headquartered exporter profile. Over the 5-year minimum election period, that's ~$33,000 in cumulative ND tax savings, before factoring in growth.

**Step 5 — Estimated-tax obligation for 2026:**

```
$40,849 > $5,000 → quarterly Form 40-ES required.
Safe harbor: pay 100% of 2025 liability ($40,849) split into 4 installments
  of $10,212.25, due April / June / September / December 15, 2026.
```

**Takeaway.** A multistate ND C-corp needs to think carefully about whether to make the single-sales-factor election. The break-even is roughly where the ND sales factor is materially lower than the average of the property and payroll factors — typical of ND-headquartered producers selling nationally. The election is binding for 5 years, so model carefully.

**Apportionment factor inputs (Schedule SA)**

| Factor | ND | Everywhere | Factor Ratio |
| --- | --- | --- | --- |
| Property | $5,000,000 | $10,000,000 | 0.5000 |
| Payroll | $3,000,000 | $5,000,000 | 0.6000 |
| Sales | $8,000,000 | $20,000,000 | 0.4000 |

### 11.3 Example C — ND S-corp with zero entity-level CIT but pass-through

**Facts.** Bakken Software Solutions, Inc. is an ND S-corp (federal § 1362 election in effect) providing software consulting to oil & gas producers. Single shareholder, ND resident. Calendar 2025:

- Federal Form 1120-S ordinary business income: $400,000 (passes through to shareholder)
- 100% of activity in ND.
- No PTE election available (ND has none — see § 9).

**Step 1 — Entity-level ND CIT (Form 40):**

```
$0 — S-corps are exempt from ND corporate income tax. File Form 60 (informational).
```

**Step 2 — Shareholder-level ND PIT (Form ND-1, separate return):**

The $400,000 of S-corp income flows through to the shareholder's federal Schedule K-1 and onto ND Form ND-1. The shareholder pays ND personal income tax at the 2025 rates (top bracket **2.50%**, confirmed against N.D.C.C. § 57-38-30.3, which sets a 0.00% / 1.95% / 2.50% schedule for every filing status; see `nd-income-tax.md` for the indexed thresholds):

```
Approx. ND PIT (top bracket 2.50% on amount above ND PIT threshold):
  400,000 × 2.50% ≈ $10,000 (simplified — actual ND-1 computation differs)
```

**Step 3 — Federal SALT-cap exposure (no PTET workaround):**

The shareholder pays approximately $10,000 of ND PIT plus state and local taxes (property tax on home, etc.). Total SALT likely well over $10,000. The federal Schedule A SALT deduction is capped at $10,000 (or as modified by OBBBA — verify).

Because ND has no PTET, the entity cannot pay the shareholder's ND PIT at the entity level and deduct it on Form 1120-S. The shareholder is fully exposed to the SALT cap.

**Comparison vs. a hypothetical PTET election:**

If ND had a PTET at a 2.50% rate, the entity would pay $10,000 of PTET, deduct it on Form 1120-S (reducing pass-through income to $390,000), and the shareholder would claim a refundable credit on Form ND-1. Federal tax saving at the 37% marginal bracket: $10,000 × 37% ≈ $3,700. This saving is unavailable in ND.

**Step 4 — Total ND tax burden:**

```
Entity-level (Form 60)         $0.00
Shareholder ND PIT (Form ND-1) ~$10,000.00
Federal SALT relief (lost)     ~($3,700) opportunity cost
Total ND tax                   ~$10,000
```

**Takeaway.** ND S-corp owners pay only personal income tax — there is no entity-level CIT. But because ND has no PTET, high-income S-corp owners lose ~$3,700 per $400,000 of pass-through income in federal tax compared with peers in PTET states. This is the principal competitive disadvantage of the ND tax code for the small-corporation owner segment.

### 11.4 Example D — Oil & gas C-corp: extraction tax vs. income tax (disambiguation)

**Facts.** Bakken Crude Operators, Inc. is an ND C-corp operating oil wells in McKenzie County. Calendar 2025:

- Federal taxable income: $5,000,000 (after deducting all severance taxes paid)
- 100% of activity in ND. Apportionment 1.0000.
- ND additions / subtractions: net $0.

**Question that confuses new practitioners:** "We paid $3,000,000 in ND oil extraction tax in 2025. Do we get a credit against our ND CIT?"

**Answer: No.** The oil extraction tax (NDCC Ch. 57-51.1) is a severance tax computed at the wellhead on the producer's net interest, at a base rate of approximately 5% of gross value (with various rate triggers tied to oil price). The oil and gas gross production tax (NDCC Ch. 57-51) is a separate 5% severance tax. These taxes are:

- Paid separately to the Oil and Gas Tax Section of the ND Tax Commissioner.
- Deductible in computing federal taxable income under § 164 (state taxes paid in carrying on a trade or business).
- Not credited against ND CIT.
- Not computed on Form 40.

**Step 1 — ND CIT computation on Form 40:**

```
Federal taxable income            5,000,000
  (already reduced by the $3M of severance tax deducted federally)
+ ND additions                            0
- ND subtractions                         0
= Pre-apportionment income        5,000,000
× ND apportionment                   1.0000
= ND taxable income               5,000,000
```

**Step 2 — ND CIT:**

```
Bracket 1: $25,000   × 1.41% = $    352.50
Bracket 2: $25,000   × 3.55% = $    887.50
Bracket 3: $4,950,000 × 4.31% = $213,345.00
                                 ----------
Total ND CIT                    $214,585.00
```

**Step 3 — Total ND tax burden (entity-level only):**

```
ND CIT (Form 40)                        $214,585
ND Oil Extraction Tax (paid separately)  $3,000,000
ND Oil & Gas Gross Production Tax        (varies — typically a similar magnitude)
                                        ----------
Total entity-level ND tax              ~$5M+
```

**Takeaway — audit flash point.** The severance taxes are vastly larger than the CIT for an ND oil producer and are governed by entirely separate statutes and forms. A new ND practitioner who attempts to net severance tax against CIT, or to claim a CIT credit, will produce a materially wrong return. The two regimes are independent. The only interaction is that the severance taxes are federally deductible (reducing federal taxable income, which is the starting point for ND CIT). For the actual severance computation, refer to a dedicated `nd-oil-extraction-tax` skill (not yet authored as of v0.1).

## 12. Quick Reference Summary Table

**Quick Reference Summary Table**

| Item | 2024 | 2025 | 2026 (planning) |
| --- | --- | --- | --- |
| ND CIT bracket 1 (up to $25,000) | 1.41% | 1.41% | 1.41% (confirmed, NDCC § 57-38-30) |
| ND CIT bracket 2 ($25K–$50K) | 3.55% | 3.55% | 3.55% (confirmed, NDCC § 57-38-30) |
| ND CIT bracket 3 (above $50K) | 4.31% | 4.31% | 4.31% (confirmed, NDCC § 57-38-30) |
| Water's-edge surtax | 3.5% | 3.5% | 3.5% (confirmed, **NDCC § 57-38.4-02(3)** — not § 57-38.1-15, which is the sales factor; the election binds for five consecutive tax years) |
| Minimum tax | $0 | $0 | $0 |
| Franchise tax | none | none | none |
| Apportionment (default) | 3-factor, **equally weighted** | 3-factor, **equally weighted** | 3-factor, **equally weighted** — (P+PR+S)/3 in all three years. ND is not a double-weighted-sales state: (P+PR+2S)/4 under NDCC § 57-38.1-09(2) was available only for tax years 2016-2017, and (P+PR+6S)/8 under § 57-38.1-09(3) only for 2018 |
| Sales factor weighting (100% sales) election available? | Yes | Yes | Yes — NDCC § 57-38.1-09(4), N.D. Admin. Code Ch. 81-03-09.2, for tax years beginning after 31 Dec 2018; not available to passthrough entities; binds five consecutive tax years |
| Sourcing (services) | Cost-of-performance | Cost-of-performance | Cost-of-performance — confirmed, NDCC § 57-38.1-17 |
| NOL carryforward period | 20 yrs (pre-2018 losses) / indefinite (post-2017) | same | same — ND follows the federal period for a loss of like character (N.D. Admin. Code 81-03-05.1-07(2)). No ND carryback for loss years beginning after 31 Dec 2002 |
| NOL 80% TI limit (post-2017) | **No** | **No** | **No** in every year — the ND NOL is granted by NDCC § 57-38-01.3(3) with no percentage cap, after the federal NOL deduction is added back in full under § 57-38-01.3(1)(g). The federal § 172(a)(2)(B) limit does not travel to it |
| PTE election | NONE | NONE | NONE — confirmed through the 69th (2025) Assembly, which adjourned sine die without enacting one |
| Filing form (C-corp) | Form 40 | Form 40 | Form 40 |
| Filing form (S-corp) | Form 60 | Form 60 | Form 60 |
| Filing form (partnership) | Form 58 | Form 58 | Form 58 |
| Est. tax threshold | $5,000 | $5,000 | $5,000 — confirmed, and it is a TWO-part test: estimates are required only where the current year's estimated tax is expected to exceed $5,000 AND the prior year's ND net tax liability also exceeded $5,000 (N.D.C.C. § 57-38-62(2); Form 40-UT, lines 1 and 3) |
| Due date (calendar) | Apr 15 | Apr 15 | Apr 15 |
| ND PIT rate (top, for context) | ~2.50% | ~2.50% | ~2.50% |

## 13. Refusal Catalogue

- **Insurance companies** — Subject to the gross premiums tax under NDCC § 26.1-03-17, not Form 40 CIT. Refuse the engagement; refer to insurance-tax specialist.  _(NDCC § 26.1-03-17)_
- **Bank of North Dakota** — State-owned instrumentality under NDCC Ch. 6-09. Pays no corporate income tax. Has no Form 40 filing obligation. Audit flash point: practitioners encountering BND in apportionment denominators or intercompany analyses should refer to ND Treasury / specialized counsel.  _(NDCC Ch. 6-09)_
- **Private banks and financial institutions** — Subject to the financial institution privilege tax under NDCC Ch. 57-35.3, computed on net worth (not income). Form 35 series, not Form 40. Refuse standard CIT engagement; refer to financial-institution tax specialist.  _(NDCC Ch. 57-35.3)_
- **Oil and gas severance taxes** — NDCC Ch. 57-51 (gross production) and NDCC Ch. 57-51.1 (extraction). Computed at the wellhead on producer's net interest. NOT a CIT computation; NOT reduced by NOL; NOT credited against CIT. Refer to dedicated severance skill (not yet authored) or to a ND oil & gas tax specialist. Surface as audit flash point — see § 11.4.  _(NDCC Ch. 57-51 / NDCC Ch. 57-51.1)_
- **Coal Conversion Tax** — Coal Conversion Tax (NDCC Ch. 57-60). Separate severance regime on coal mined in ND. Out of scope.  _(NDCC Ch. 57-60)_
- **Cigarette / tobacco / liquor excise taxes** — Out of scope.
- **Multistate combined / unitary reporting beyond standard** — Complex Joyce / Finnigan questions, intercompany transfer pricing audits, and §482-style adjustments require a multistate tax specialist. Refer.
- **Transfer pricing and § 482 adjustments** — Refuse; refer to multistate / international tax specialist.
- **Captive REITs, captive RICs, and REIT subsidiary structures** — Special add-back rules; refer.
- **Federal tax controversy / IRS examination support** — Refer to tax controversy specialist.
- **Real and personal property tax assessments** — Real and personal property tax assessments (county/city level). Refer to local-tax specialist.
- **ND Indian Country tax issues** — ND Indian Country tax issues (tribal sovereignty, tax-immunity questions on reservation activity for the Three Affiliated Tribes / Standing Rock / Spirit Lake / Turtle Mountain / Trenton Indian Service Area). Highly fact-specific; refer to tribal-law specialist.
- **Renaissance Zone / Opportunity Zone tax credits** — Renaissance Zone / Opportunity Zone tax credits under NDCC Ch. 40-63 — not addressed in this v0.1; refer to a dedicated ND credits skill.  _(NDCC Ch. 40-63)_

## 14. Provenance and Authority

### 14.1 Primary statutory authority

- **N.D.C.C. Chapter 57-38** — Income Tax Act of 1981 (corporate provisions).  _(N.D.C.C. Chapter 57-38)_
- **N.D.C.C. § 57-38-30** — Corporate income tax rate brackets. Section number confirmed against the current Century Code: § 57-38-30 imposes the three corporate brackets; **§ 57-38-30.3 is the individual, estate and trust rate section** and is not an alternative cite for corporate rates. (§ 57-38-30.1, the corporate new-industry credit, was repealed in 2017, and § 57-38-30.2, the surtax on income, in 1975.)  _(N.D.C.C. § 57-38-30)_
- **N.D.C.C. § 57-38-01.4** — NOL conformity with federal § 172.  _(N.D.C.C. § 57-38-01.4)_
- **N.D.C.C. § 57-38-08** — Sourcing rules and ND-source income.  _(N.D.C.C. § 57-38-08)_
- **N.D.C.C. § 57-38-34** — Due dates for corporate returns.  _(N.D.C.C. § 57-38-34)_
- **N.D.C.C. § 57-38-45** — Penalties.  _(N.D.C.C. § 57-38-45)_
- **N.D.C.C. § 57-38-62** — Estimated-tax requirements for corporations.  _(N.D.C.C. § 57-38-62)_
- **N.D.C.C. Chapter 57-38.1** — Apportionment (UDITPA-derived).  _(N.D.C.C. Chapter 57-38.1)_
- **N.D.C.C. § 57-38.1-09** — Apportionment of business income. Subsection (1) is the equally weighted three-factor default; (2) the lapsed 2016-2017 double-weighted-sales election; (3) the lapsed 2018-only (P+PR+6S)/8 election; **(4) the current 100% weighted sales factor election** for tax years beginning after 31 Dec 2018.  _(N.D.C.C. § 57-38.1-09)_
- **N.D.C.C. § 57-38.1-15** — Water's-edge surtax.  _(N.D.C.C. § 57-38.1-15)_
- **N.D.C.C. § 57-38.1-16** — Sales-factor sourcing.  _(N.D.C.C. § 57-38.1-16)_
- **N.D.C.C. § 57-38.1-18** — Alternative apportionment.  _(N.D.C.C. § 57-38.1-18)_
- **N.D.C.C. § 57-38.1-19** — Combined / unitary reporting.  _(N.D.C.C. § 57-38.1-19)_

### 14.2 Cross-referenced (out-of-scope) statutes

- **N.D.C.C. Chapter 6-09** — Bank of North Dakota organization and tax status.  _(N.D.C.C. Chapter 6-09)_
- **N.D.C.C. Chapter 57-35.3** — Financial institution privilege tax (private banks).  _(N.D.C.C. Chapter 57-35.3)_
- **N.D.C.C. § 26.1-03-17** — Insurance gross premiums tax.  _(N.D.C.C. § 26.1-03-17)_
- **N.D.C.C. Chapter 57-51** — Oil and Gas Gross Production Tax.  _(N.D.C.C. Chapter 57-51)_
- **N.D.C.C. Chapter 57-51.1** — Oil Extraction Tax.  _(N.D.C.C. Chapter 57-51.1)_
- **N.D.C.C. Chapter 57-60** — Coal Conversion Tax.  _(N.D.C.C. Chapter 57-60)_

### 14.3 Session laws (key reforms)

- **2015 — Rate bracket stabilization** — The 2015 session cut corporate rates by roughly 5%, producing the current 1.41% / 3.55% / 4.31% range, which has not changed since. Confirmed against the ND Office of State Tax Commissioner's *Corporate Income Tax History*, which records rate cuts in the 2011 (1.68%-5.15%) and 2013 (1.48%-4.53%) sessions and no rate change in any session after 2015.  _(ND Office of State Tax Commissioner, Corporate Income Tax History)_
- **2023 — 68th Legislative Assembly** — Considered tax reform; did not enact PTET.  _(68th Legislative Assembly)_
- **2025 — 69th Legislative Assembly** — Adjourned sine die with no change to corporate rates or brackets and no PTET. Its one corporate income tax measure was **S.B. 2282**, the employer child care contribution income tax credit (N.D.C.C. § 57-38-01.42): 50% of the first $1,000 of child care contributions per employee, effective for tax years beginning in 2025.  _(69th Legislative Assembly, S.B. 2282; ND Tax Commissioner, Corporate Income Tax History)_

### 14.4 Administrative guidance

- **Form 40 Corporation Income Tax Booklet (2025)** — ND Office of State Tax Commissioner. Source of bracket confirmation, due-date confirmation, water's-edge surtax mechanics, and Schedule SA apportionment instructions.  _(Form 40 Corporation Income Tax Booklet (2025))_
- **Form 40-ES instructions** — estimated-tax mechanics and the $5,000 threshold, confirmed as a two-part test (current-year expectation AND prior-year liability both above $5,000).  _(Form 40-ES instructions)_
- **Form 40-UT instructions** — underpayment penalty computation.  _(Form 40-UT instructions)_
- **Form 60 instructions** — ND S-corporation filing.  _(Form 60 instructions)_
- **Form 58 instructions** — ND partnership filing.  _(Form 58 instructions)_
- **ND Office of State Tax Commissioner Corporate Income Tax web page** — current rates, forms, and Commissioner directives.  _([tax.nd.gov/business/corporate-income-tax](https://tax.nd.gov/business/corporate-income-tax))_

### 14.5 Cross-references in this skill bundle

ND personal income tax (Form ND-1), relevant for S-corp shareholders, LLC members, and the SALT-cap discussion (since no PTET workaround exists).

ND sales and use tax (separate regime).

Federal corporate return assembly (Form 1120) feeding ND starting taxable income.

Federal/state S-corp election framework — particularly relevant in ND given the absence of PTET makes the C-corp vs. S-corp analysis non-trivial.

federal SALT-cap parameters and OBBBA conformity.

### 14.6 Verification status

pending (skill is in draft; awaiting credentialed ND CPA/EA review per the verification model — lead + contributors per country).

entire skill (rate brackets, apportionment weighting, sourcing rules, NOL parameters, estimated-tax threshold, PTET absence confirmation through 69th Legislative Assembly).

1. Confirm 2025 bracket thresholds ($25,000 / $50,000) and rates (1.41% / 3.55% / 4.31%) in current NDCC § 57-38-30.
2. Confirm three-factor formula weighting (sales 2×) and that single-sales-factor election is still available under § 57-38.1-09.
3. Confirm ND has not adopted broad market-based sourcing as of TY 2025.
4. NOL carryforward period confirmed: federal period for a loss of like character — 20 years for pre-2018 losses, indefinite for post-2017. Still confirm conformity with the federal 80% taxable-income limit.
5. Confirm $5,000 estimated-tax threshold under § 57-38-62.
6. Confirm absence of PTET through the 69th Legislative Assembly (2025).
7. Confirm water's-edge surtax remains at 3.5%.
8. Confirm sections of Form 40 booklet that reference current Schedule SA mechanics and any 2025 form-line renumbering.

### 14.7 Citation discipline

- **Re-verification requirement** — All statutory rate, threshold, and apportionment claims must be re-verified against the cited statute on each filing-season run.
- **Form line renumbering** — ND form line numbers may change year-to-year; cross-tie to the current-year Form 40 booklet before relying on line-level guidance in production.

Worked examples are illustrative; precise mechanics on the actual Form 40 / Schedule SA may differ in line ordering and rounding conventions.

This skill is **not** a substitute for credentialed reviewer signoff under the OpenAccountants verification model.

### 14.8 Audit flash points (re-summary)

For the reviewer's quick scan:

- **Bank of North Dakota** — state instrumentality, pays no CIT. Do not confuse with private banks (which pay the privilege tax under NDCC Ch. 57-35.3). See § 13 #2 and #3.  _(NDCC Ch. 57-35.3)_
- **Oil Extraction Tax** — severance, NOT income tax. Computed at well, not on Form 40. No CIT credit. See § 11.4 and § 13 #4.
- **No PTET in ND** — high-income S-corp owners cannot escape federal SALT cap via entity-level election. Materially different from NC, CA, NY, MN. See § 9.
- **Three-factor (not single-sales) by default** — practitioners migrating from single-sales states must use the modified UDITPA formula unless the taxpayer has elected single-sales. See § 6.
- **Cost-of-performance sourcing for services** — ND has not adopted market-based sourcing. See § 7.2.
- **Combined / unitary reporting required** — ND is not a separate-return state. See § 10.6.
- **No minimum tax, no franchise tax** — a zero-income ND C-corp owes $0 entity-level tax (still must file). See § 5.3 and § 5.4.

## End of nd-corporate-tax.md

*End of nd-corporate-tax.md (v0.1, 2026-05-28).*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
