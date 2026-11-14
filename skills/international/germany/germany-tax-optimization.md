---
name: germany-tax-optimization
description: Use this skill whenever asked about reducing tax in Germany, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals in Germany. Trigger on phrases like "reduce tax", "tax planning", "save tax", "optimize", "allowances", "deductions I'm missing", "Steuern sparen", "Steueroptimierung", "Steuerlast senken". ALWAYS read this skill before advising on any German tax optimization strategy.
version: 1.2
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-06
review_status: pending_review
depends_on: []
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Tax Optimization

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

This tax-planning reference produces a comparison working paper and professional brief for the stated self-employed cases in VZ 2026. Its empty depends_on list is retained; load the applicable computation workflow and qualified companion before producing an actual result. It does not establish an implementation recommendation.

Retained material marked unverified is for professional source review and must not be used to compute an actual liability, recommend an arrangement, register, file or pay. Structural conformance and hypothetical arithmetic do not establish legal currency or professional approval.

### Germany Tax Optimization -- Self-Employed Skill v1.2



### Section 1 -- Quick Reference

**Quick Reference**

| Field | Value | Source or qualification |
| --- | --- | --- |
| Country | Germany (Bundesrepublik Deutschland) | Retained context; see scope and source limits |
| Key optimization legislation | Einkommensteuergesetz (EStG, https://www.gesetze-im-internet.de/estg/) -- particularly §4 (Betriebsausgaben), §7g (Investitionsabzugsbetrag), §6 Abs. 2/2a (GWG), §9 (Werbungskosten), §10 (Sonderausgaben), §10a (Riester), §10d (Verlustvortrag/-rücktrag), §35a (haushaltsnahe Dienstleistungen) | unverified: inherited figure or assumption; professional/source qualification required |
| Statutory anti-abuse rule | Germany has a statutory general anti-abuse rule in [AO § 42](https://www.gesetze-im-internet.de/ao_1977/__42.html). Specific statutory anti-avoidance provisions take priority when their conditions are met. Apply the statutory test and qualification in Section 10. | unverified: inherited figure or assumption; professional/source qualification required |
| Currency | EUR | unverified: inherited figure or assumption; professional/source qualification required |
| Tax year | Calendar year (1 Jan -- 31 Dec) | unverified: inherited figure or assumption; professional/source qualification required |
| Filing deadline | For the relevant calendar-year return, normally 7 months after year-end. An eligible return prepared by an engaged authorised adviser normally runs to the last day of February in the second following calendar year, subject to an early call. Check the period, notice, statutory exceptions and weekend/public-holiday rules (AO §§ 149(2)-(4), 108(3)) | unverified: inherited figure or assumption; professional/source qualification required |

#### Income Tax Rates 2026

**Income Tax Rates 2026**

| Taxable income (EUR) | Marginal rate | Source or qualification |
| --- | --- | --- |
| 0 -- 12,348 | 0% (Grundfreibetrag) | unverified: inherited figure or assumption; professional/source qualification required |
| 12,349 -- 17,799 | 14% -- 24% (linear progression) | unverified: inherited figure or assumption; professional/source qualification required |
| 17,800 -- 69,878 | 24% -- 42% (linear progression) | unverified: inherited figure or assumption; professional/source qualification required |
| 69,879 -- 277,825 | 42% (Spitzensteuersatz) | unverified: inherited figure or assumption; professional/source qualification required |
| 277,826+ | 45% (Reichensteuersatz) | unverified: inherited figure or assumption; professional/source qualification required |

Source: § 32a Abs. 1 EStG (the 2026 tariff)  -  https://www.gesetze-im-internet.de/estg/__32a.html.

- **Solidaritätszuschlag and Kirchensteuer**  -  Plus Solidaritätszuschlag (5.5% of income tax, only for higher incomes above threshold) and Kirchensteuer (8-9% of income tax, if applicable).

## Scope statement

Confirm taxpayer and assessment year; income categories and taxable bases for each affected year; separate income-tax and trade-tax loss determinations; carryback waiver instructions and actual prior-year capacities; eligibility for each proposed allowance; and actual notices, adviser status and implementation constraints.

## Filing requirements

### Section 11 -- Annual Tax Planning Calendar

**Annual Tax Planning Calendar table**

| Month | Action | Source or qualification |
| --- | --- | --- |
| January | Review prior year's income and plan current year. Decide on IAB claims. File prior year's VAT annual return (if applicable). | Retained context; see scope and source limits |
| February | Gather Belege (receipts) and bank statements. Begin EÜR preparation. | Retained context; see scope and source limits |
| March | **10 March** -- quarterly Voranmeldung for January (if monthly). Vorauszahlung Q1 due 10 March. | unverified: inherited figure or assumption; professional/source qualification required |
| April | Review Ehegattensplitting benefit with spouse. | Retained context; see scope and source limits |
| May | Mid-year profit estimate. Consider Rürup contribution. | Retained context; see scope and source limits |
| June | **10 June** -- Voranmeldung Q1 (if quarterly) + Vorauszahlung Q2. | unverified: inherited figure or assumption; professional/source qualification required |
| July | Check the ordinary 7-month filing period for the prior calendar year, including applicable exceptions, extensions and AO § 108(3) weekend/public-holiday treatment. A universal 31 July date is insufficient. Apply for Herabsetzung if income is dropping. | unverified: inherited figure or assumption; professional/source qualification required |
| August | Review GWG purchases and capital equipment needs for H2. | unverified: inherited figure or assumption; professional/source qualification required |
| September | **10 September** -- Vorauszahlung Q3. | unverified: inherited figure or assumption; professional/source qualification required |
| October | Plan year-end purchases: GWG under EUR 800 for immediate deduction. | unverified: inherited figure or assumption; professional/source qualification required |
| November | Maximize Rürup contributions before December. Consider Sonderausgaben planning (donations, Vorsorgeaufwendungen). | Retained context; see scope and source limits |
| December | **10 December** -- Vorauszahlung Q4. Buy GWG assets. Prepay deductible expenses. Marry before 31 December for full-year Splitting. Claim IAB for planned investments. Maximize Rürup/pension contributions. | unverified: inherited figure or assumption; professional/source qualification required |

## Rates and thresholds

### Section 3 -- Deductions Most People Miss

**Deductions Most People Miss table**

| Deduction | Legislation | Notes | Source or qualification |
| --- | --- | --- | --- |
| Home office (Homeoffice-Pauschale) | EStG §4 Abs. 5 Nr. 6c | EUR 6/day, max 210 days = EUR 1,260/year. No documentation of actual costs needed. Alternatively, full costs if dedicated room is Mittelpunkt (center) of professional activity. | unverified: inherited figure or assumption; professional/source qualification required |
| Dedicated home office (häusliches Arbeitszimmer) | EStG §4 Abs. 5 Nr. 6b | If the room is the center of all professional activity, actual costs (proportional rent, utilities, insurance) are fully deductible, or the Jahrespauschale of EUR 1,260. From 2026: stricter documentation required (BFH ruling). | unverified: inherited figure or assumption; professional/source qualification required |
| Commuting allowance (Entfernungspauschale) | EStG §9 Abs. 1 Nr. 4 | EUR 0.30/km for first 20 km, EUR 0.38/km from 21st km, one way, per working day. | unverified: inherited figure or assumption; professional/source qualification required |
| Professional development | EStG §4 Abs. 4, §9 | Courses, seminars, conferences, books, trade journals -- fully deductible if related to current profession. | unverified: inherited figure or assumption; professional/source qualification required |
| Professional association dues | EStG §9 Abs. 1 Nr. 3 | Berufsverband, Kammer, Gewerkschaft -- fully deductible. | unverified: inherited figure or assumption; professional/source qualification required |
| Work equipment (Arbeitsmittel) | EStG §9 Abs. 1 Nr. 6 | Laptop, monitor, desk, chair, phone -- fully deductible if exclusively/predominantly for business. Mixed-use items at business-use %. | unverified: inherited figure or assumption; professional/source qualification required |
| Telephone & internet | EStG §4 Abs. 4 | Business-use proportion. Simplified: 20% of costs, max EUR 20/month without documentation. | unverified: inherited figure or assumption; professional/source qualification required |
| Travel expenses (Reisekosten) | EStG §4 Abs. 5, §9 Abs. 1 Nr. 5a | Actual costs or Pauschale: EUR 28/day (full day away), EUR 14/day (>8 hours). Overnight: actual costs. | unverified: inherited figure or assumption; professional/source qualification required |
| Insurance premiums (business) | EStG §4 Abs. 4 | Professional liability, legal expenses insurance (business), business interruption. | unverified: inherited figure or assumption; professional/source qualification required |
| Contributions to professional chambers | EStG §4 Abs. 4 | IHK, Handwerkskammer, Steuerberaterkammer, etc. | unverified: inherited figure or assumption; professional/source qualification required |
| Double household (doppelte Haushaltsführung) | EStG §9 Abs. 1 Nr. 5 | If maintaining a second household for work: rent up to EUR 1,000/month + travel costs. | unverified: inherited figure or assumption; professional/source qualification required |
| Relocation costs (Umzugskosten) | EStG §9 Abs. 1 | If job-related relocation: actual costs or Umzugskostenpauschale. | unverified: inherited figure or assumption; professional/source qualification required |

### Section 4 -- Capital Allowances Optimization

#### Investitionsabzugsbetrag (IAB) -- §7g EStG

**IAB table**

| Feature | Detail | Source or qualification |
| --- | --- | --- |
| What | Deduct up to 50% of the anticipated acquisition cost of a future asset BEFORE purchasing it | unverified: inherited figure or assumption; professional/source qualification required |
| Limit | EUR 200,000 total across all active IABs (rolling 4-year window) | unverified: inherited figure or assumption; professional/source qualification required |
| Timeline | Investment must occur within 3 years | unverified: inherited figure or assumption; professional/source qualification required |
| Business use requirement | ≥ 90% business use in year of acquisition and the following year | unverified: inherited figure or assumption; professional/source qualification required |
| Strategy | Claim IAB to reduce current-year profit, then purchase the asset within 3 years. Effectively shifts the deduction earlier. | unverified: inherited figure or assumption; professional/source qualification required |

#### Geringwertige Wirtschaftsgüter (GWG) -- §6 Abs. 2 EStG

**GWG table**

| Method | Threshold | Detail | Source or qualification |
| --- | --- | --- | --- |
| Sofortabschreibung (immediate write-off) | Up to EUR 800 (net) | Full deduction in year of purchase. No depreciation schedule. | unverified: inherited figure or assumption; professional/source qualification required |
| Sammelposten (pool depreciation) | EUR 250 -- EUR 1,000 (net) | Pool all items, depreciate over 5 years straight-line. Alternative to individual depreciation. | unverified: inherited figure or assumption; professional/source qualification required |
| Standard AfA | Over EUR 800/1,000 | Depreciate over useful life per AfA-Tabelle. | unverified: inherited figure or assumption; professional/source qualification required |

- **GWG strategy**  -  For items under EUR 800 net, always use Sofortabschreibung. For items EUR 800-1,000, compare Sammelposten (5 years) vs individual AfA -- choose whichever gives faster write-off.

#### Sonderabschreibung (Special Depreciation) -- §7g Abs. 5 EStG

- **Sonderabschreibung rule**  -  Up to 40% additional depreciation (for assets acquired after 31 December 2023; 20% before) in the year of acquisition and the following 4 years (on top of normal AfA; § 7g Abs. 5 EStG  -  https://www.gesetze-im-internet.de/estg/__7g.html). Combined with IAB, this allows extremely front-loaded deductions. Requirements: Business assets ≤ EUR 200,000 at end of prior year (or profits ≤ EUR 200,000 for Freiberufler).  _(§7g Abs. 5 EStG)_

### Section 9 -- Investment & Retirement

#### Basisrente (Rürup-Rente) -- §10 Abs. 1 Nr. 2 EStG

**Basisrente table**

| Feature | Detail | Source or qualification |
| --- | --- | --- |
| Deduction limit | 100% of contributions deductible (since 2023). Max EUR 30,826 (single) / EUR 61,652 (joint) for 2026: the maximum knappschaftliche pension contribution, 24.7% × EUR 124,800, rounded up (EUR 29,344 / EUR 58,688 in 2025). | § 10 Abs. 3 EStG (https://www.gesetze-im-internet.de/estg/__10.html); RV-Beitragssatz 2026 (https://www.gesetze-im-internet.de/rvbeitrsbek_2026/----.html); BBG 2026 (https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2025/sozialversicherungsrechengroessen-2026.html) |
| Tax treatment in retirement | Taxed as income, but typically at lower marginal rate. | Retained context; see scope and source limits |
| Strategy | The primary pension vehicle for Freiberufler and Gewerbetreibende. Contributions reduce taxable income EUR-for-EUR up to the limit. At 42% marginal rate, EUR 30,826 contribution = EUR 12,947 tax saving. | Derived from the deduction-limit ceiling: EUR 30,826 × 42% = EUR 12,946.92, shown as EUR 12,947. Ceiling sources are in the row above. |

#### Riester-Rente -- §10a EStG

**Riester-Rente table**

| Feature | Detail | Source or qualification |
| --- | --- | --- |
| Eligibility | Employees with mandatory GRV contributions (not most self-employed unless voluntarily contributing). | Retained context; see scope and source limits |
| Maximum deduction | EUR 2,100/year as Sonderausgaben | unverified: inherited figure or assumption; professional/source qualification required |
| Zulagen (allowances) | EUR 175 base + EUR 185-300/child | unverified: inherited figure or assumption; professional/source qualification required |
| Strategy | Only relevant for self-employed who voluntarily contribute to GRV. Compare Zulage benefit vs Sonderausgabenabzug. | Retained context; see scope and source limits |

#### Vermögenswirksame Leistungen (VWL) and Other

**VWL and Other table**

| Vehicle | Tax benefit | Legislation | Source or qualification |
| --- | --- | --- | --- |
| Sparer-Pauschbetrag | EUR 1,000 (single) / EUR 2,000 (joint) tax-free investment income | EStG §20 Abs. 9 | unverified: inherited figure or assumption; professional/source qualification required |
| Abgeltungsteuer | 25% flat tax on capital gains and investment income (+ Soli + KiSt) | EStG §32d | unverified: inherited figure or assumption; professional/source qualification required |
| Günstigerprüfung | If marginal rate < 25%, apply for taxation at marginal rate instead of Abgeltungsteuer | EStG §32d Abs. 6 | unverified: inherited figure or assumption; professional/source qualification required |

## Computation rules

### Section 2 -- Income Splitting & Structuring

#### Ehegattensplitting (Spousal Income Splitting)

**Ehegattensplitting table**

| Strategy | Detail | Legislation | Source or qualification |
| --- | --- | --- | --- |
| Joint assessment (Zusammenveranlagung) | Married couples/civil partners can combine income, halve it, apply the rate table, then double the resulting tax. Massive benefit when incomes are unequal. | EStG §26, §26b, §32a Abs. 5 | unverified: inherited figure or assumption; professional/source qualification required |
| Optimal Steuerklasse | Choose Steuerklasse III/V or IV/IV depending on income split. III/V benefits the higher earner's cash flow. | EStG §38b | unverified: inherited figure or assumption; professional/source qualification required |

#### Sole Proprietorship vs GmbH

**Sole Proprietorship vs GmbH table**

| Factor | Einzelunternehmen (sole trader) | GmbH | Source or qualification |
| --- | --- | --- | --- |
| Top marginal rate | 45% + Soli + KiSt | 15% KSt + 5.5% Soli on the KSt (0.825 points) + ~14% GewSt = ~30% in VZ 2026; KSt steps down from 14% in 2028 to 10% from 2032 (KStG s 23(1)) | unverified: inherited figure or assumption; professional/source qualification required |
| When to incorporate | When profits consistently exceed ~EUR 60,000 and can be retained. Extraction via salary (deductible) or dividends (25% Abgeltungsteuer + Soli). | EStG §20 Abs. 1 Nr. 1; KStG §1 | unverified: inherited figure or assumption; professional/source qualification required |

#### Employing Family Members (Ehegatten-Arbeitsverhältnis)

- **Family employment deductibility**  -  Salary to a spouse is deductible as Betriebsausgabe if the employment relationship is genuine, at arm's length, and actually performed. The BFH requires: written contract, regular payment to own bank account, and duties commensurate with salary.  _(EStG §4 Abs. 4; BFH case law)_

### Section 5 -- Loss Utilization

**Loss Utilization table**  _(EStG §10d)_

| Relief | Detail | Limit | Source or qualification |
| --- | --- | --- | --- |
| Verlustrücktrag (carry-back) | Eligible unoffset negative income goes first to the immediately preceding assessment period, then, insofar as offset is unavailable, to the second preceding period | Standard EStG § 10d(1) limit: EUR 1,000,000; EUR 2,000,000 for spouses jointly assessed under §§ 26/26b. The joint-spouse limit is not a company limit. A taxpayer may apply to waive carryback for both years together | https://www.gesetze-im-internet.de/estg/__10d.html (separate GewStG rule and all taxpayer restrictions remain held) |
| Verlustvortrag (carry-forward) | Eligible losses not deducted through carryback remain available under EStG § 10d(2) | For VZ 2026, full offset up to EUR 1,000,000 (EUR 2,000,000 for the specified jointly assessed spouses), then 70% of the excess. Keep the separate trade-tax balance and its EUR 1,000,000/60% rule apart (GewStG § 10a) | https://www.gesetze-im-internet.de/estg/__10d.html (separate GewStG rule and all taxpayer restrictions remain held) |
| Intra-year offset (Verlustausgleich) | Losses from one income category offset gains in other categories within the same year | No limit for horizontal offset; vertical offset generally unrestricted | Retained context; see scope and source limits |
| IAB as virtual loss | IAB under §7g reduces profit and can create or increase a loss that triggers carry-back/forward | Subject to IAB limits | unverified: inherited figure or assumption; professional/source qualification required |

#### Strategy

- **Loss utilisation conditions:** EStG § 10d(1) gives carryback priority before personal deductions and requires the specified § 34a(3) adjustment to the income of each carryback year. Hold a result if those facts or the applicable loss restrictions are unresolved. Establish any IAB deduction separately; § 10d does not itself establish eligibility under § 7g. Apply the 2 carryback years in sequence before carryforward unless the taxpayer requests the complete carryback waiver. Sources: [EStG § 10d](https://www.gesetze-im-internet.de/estg/__10d.html) and the selected application references in [§ 52(18b)](https://www.gesetze-im-internet.de/estg/__52.html). Historical higher-limit legislation and its applicable periods require separate verification.

### Section 6 -- Timing Strategies

**Timing Strategies table**

| Strategy | Detail | Source or qualification |
| --- | --- | --- |
| Defer invoicing | For Einnahme-Überschuss-Rechnung (EÜR/cash basis) taxpayers, defer invoicing to January to shift income to the next year. | Retained context; see scope and source limits |
| Accelerate expenses | Prepay insurance, subscriptions, training before 31 December. Under §11 EStG (Zufluss-/Abflussprinzip), expenses are deductible when paid for EÜR taxpayers. | unverified: inherited figure or assumption; professional/source qualification required |
| IAB timing | Claim IAB in a high-profit year to reduce current income by up to EUR 200,000. Purchase the asset within 3 years. | unverified: inherited figure or assumption; professional/source qualification required |
| GWG year-end purchases | Buy business equipment under EUR 800 (net) in December for immediate full deduction. | unverified: inherited figure or assumption; professional/source qualification required |
| Vorauszahlungen (advance tax payments) | If income drops, apply to the Finanzamt to reduce quarterly advance payments (Herabsetzungsantrag). Avoid tying up cash unnecessarily. | Retained context; see scope and source limits |
| Steuerberater filing extension | Using a tax advisor extends the filing deadline to end of February of the second following year -- gives more time for planning and documentation. | Retained context; see scope and source limits |
| Ehegattensplitting timing | If marrying in December, Zusammenveranlagung applies for the entire year. Marrying on 31 December gives full-year splitting benefit. | unverified: inherited figure or assumption; professional/source qualification required |

### Section 12 -- Cash Impact Examples

#### Example 1 -- Ehegattensplitting (Spouse with EUR 0 Income, Sole Trader EUR 80,000)

**Example 1 table**

| Scenario | Tax (excl. Soli/KiSt) | Source or qualification |
| --- | --- | --- |
| Single assessment | ~EUR 21,787 | unverified: inherited figure or assumption; professional/source qualification required |
| Zusammenveranlagung | ~EUR 14,996 | unverified: inherited figure or assumption; professional/source qualification required |
| **Annual saving** | **~EUR 6,791** | unverified: inherited figure or assumption; professional/source qualification required |

#### Example 2 -- Rürup-Rente Contribution (Single, Profit EUR 70,000)

**Example 2 table**

| Contribution | EUR 15,000 | Source or qualification |
| --- | --- | --- |
| Taxable income after deduction | EUR 55,000 | unverified: inherited figure or assumption; professional/source qualification required |
| Tax saving (at ~42% marginal rate) | **~EUR 6,300** | unverified: inherited figure or assumption; professional/source qualification required |

#### Example 3 -- IAB + Sonderabschreibung (Planned EUR 40,000 Vehicle Purchase)

**Example 3 table**

| Year | Deduction | Mechanism | Source or qualification |
| --- | --- | --- | --- |
| Year 0 (before purchase) | EUR 20,000 | IAB (50% of EUR 40,000) | unverified: inherited figure or assumption; professional/source qualification required |
| Year 1 (purchase year) | EUR 8,000 + EUR 3,200 | Sonderabschreibung (40% of the EUR 20,000 base left after the IAB) + regular AfA (16%/6yr on that base) | unverified: inherited figure or assumption; professional/source qualification required |
| **Total Year 0+1 deduction** | **EUR 31,200** | 78% of cost deducted within ~2 years | unverified: inherited figure or assumption; professional/source qualification required |
| Tax saving at 42% marginal rate | **~EUR 13,104** |  | unverified: inherited figure or assumption; professional/source qualification required |

#### Example 4 -- GWG Immediate Write-Off (EUR 799 Laptop)

**Example 4 table**

| Deduction | EUR 799 in year of purchase | Source or qualification |
| --- | --- | --- |
| Tax saving at 42% | **EUR 336** | unverified: inherited figure or assumption; professional/source qualification required |
| vs. 3-year AfA: Year 1 saving | EUR 112 (EUR 266 × 42%) | unverified: inherited figure or assumption; professional/source qualification required |

#### Example 5 -- Homeoffice-Pauschale (210 Days)

**Example 5 table**

| Deduction | 210 × EUR 6 = EUR 1,260 | Source or qualification |
| --- | --- | --- |
| Tax saving at 42% | **EUR 529** | unverified: inherited figure or assumption; professional/source qualification required |
| Tax saving at 24% | **EUR 302** | unverified: inherited figure or assumption; professional/source qualification required |

### Recomputing hypothetical components

These cases test arithmetic and the stated decision boundary only. All facts and unverified parameters are explicit assumptions. They do not establish entitlement or an actual tax, legal, investment or entity-choice recommendation.

#### Case 1

Assume the stated ordinary individual VZ 2026 regime, valid loss determination of EUR 2,000,000 and eligible positive income of EUR 2,500,000, with all other restrictions and adjustments already resolved. The EUR 1,000,000 full band plus 70% of EUR 1,500,000 permits EUR 2,050,000, capped by the EUR 2,000,000 loss. EUR 500,000 income remains. No trade-tax balance, spouse uplift or current tax amount is implied.

```oa-check
name: DE VZ2026 hypothetical ordinary individual loss carryforward
inputs:
  positive_income: 2500000
  available_loss: 2000000
  full_band: 1000000
  excess_fraction: 0.7
steps:
  - limit: min(positive_income, full_band) + max(0, positive_income - full_band) * excess_fraction
  - offset: min(available_loss, limit)
  - remaining_income: positive_income - offset
  - remaining_loss: available_loss - offset
expected:
  limit: 2050000
  offset: 2000000
  remaining_income: 500000
  remaining_loss: 0
```

#### Case 2

For a fictional EUR 1,400,000 loss with first/second prior-year eligible capacities of EUR 900,000 and EUR 500,000 and a EUR 1,000,000 total carryback cap, the sequence uses EUR 900,000 then EUR 100,000, leaving EUR 400,000. A complete waiver leaves EUR 1,400,000. On assumed later VZ 2026 positive income of EUR 2,000,000, the EUR 1,700,000 carryforward limit permits either balance: future bases are EUR 1,600,000 and EUR 600,000. The counterfactual compares allocation of the same loss between years; no rate, refund, time value or preferable election is established. Resolve section 34a adjustments, all loss restrictions and taxpayer instructions first.

```oa-check
name: DE hypothetical accept or waive complete carryback
inputs:
  current_loss: 1400000
  first_prior_capacity: 900000
  second_prior_capacity: 500000
  carryback_cap: 1000000
  future_positive_income: 2000000
steps:
  - first_offset: min(current_loss, first_prior_capacity, carryback_cap)
  - second_offset: min(current_loss - first_offset, second_prior_capacity, carryback_cap - first_offset)
  - remaining_after_carryback: current_loss - first_offset - second_offset
  - remaining_with_waiver: current_loss
  - future_limit: 1000000 + max(0, future_positive_income - 1000000) * 0.70
  - future_offset_accept: min(remaining_after_carryback, future_limit)
  - future_offset_waive: min(remaining_with_waiver, future_limit)
  - future_base_accept: future_positive_income - future_offset_accept
  - future_base_waive: future_positive_income - future_offset_waive
expected:
  first_offset: 900000
  second_offset: 100000
  remaining_after_carryback: 400000
  remaining_with_waiver: 1400000
  future_limit: 1700000
  future_offset_accept: 400000
  future_offset_waive: 1400000
  future_base_accept: 1600000
  future_base_waive: 600000
```

## Edge cases and special rules

### Section 7 -- VAT Optimization (Umsatzsteuer)

**VAT Optimization table**  _(Umsatzsteuergesetz (UStG))_

| Strategy | Detail | Legislation | Source or qualification |
| --- | --- | --- | --- |
| Kleinunternehmerregelung | If prior-year turnover ≤ EUR 25,000 and current-year estimated ≤ EUR 100,000, no VAT charged. No input VAT recovery. | UStG §19 | unverified: inherited figure or assumption; professional/source qualification required |
| Opt for Regelbesteuerung | Even below threshold, opt to charge VAT if input VAT is significant (e.g., startup with heavy investment). Lock-in: 5 calendar years. | UStG §19 Abs. 2 | unverified: inherited figure or assumption; professional/source qualification required |
| Ist-Versteuerung (cash basis VAT) | Pay output VAT only when payment is received, not when invoiced. Available if prior-year turnover ≤ EUR 800,000. | UStG §20 | unverified: inherited figure or assumption; professional/source qualification required |
| Vorsteuerabzug timing | Claim input VAT in the period the invoice is received and paid (for EÜR). Time large purchases accordingly. | UStG §15 | unverified: inherited figure or assumption; professional/source qualification required |
| Reverse charge for EU services | B2B services to/from other EU states: reverse charge applies. No German VAT on outgoing invoices to EU businesses. | UStG §13b | unverified: inherited figure or assumption; professional/source qualification required |

### Section 8 -- Social Security Optimization

Legislation: Sozialgesetzbuch (SGB)

#### Self-Employed Social Security

**Self-Employed Social Security table**

| Category | Detail | Source or qualification |
| --- | --- | --- |
| Freiberufler (liberal professions) | Generally exempt from mandatory pension insurance. Can opt for Versorgungswerk (professional pension fund) or private pension. | Retained context; see scope and source limits |
| Gewerbetreibende (traders) | Generally exempt from mandatory pension insurance (unless in specific trades like craft masters). | Retained context; see scope and source limits |
| Mandatory cases | Self-employed teachers, nurses, midwives, and those with only one client (scheinselbständig) -- mandatory pension contributions. | Retained context; see scope and source limits |

#### Optimization Strategies

**Optimization Strategies table**

| Strategy | Detail | Source or qualification |
| --- | --- | --- |
| Voluntary pension contributions | Voluntary contributions to gesetzliche Rentenversicherung (GRV) are fully deductible as Sonderausgaben under §10 Abs. 1 Nr. 2 EStG. | unverified: inherited figure or assumption; professional/source qualification required |
| Opt for Versorgungswerk | Contributions to berufsständische Versorgungswerke are treated the same as GRV contributions for tax purposes. | Retained context; see scope and source limits |
| Krankenversicherung optimization | Self-employed can choose private (PKV) or voluntary statutory (GKV). Compare costs: PKV may be cheaper when young/healthy; GKV may be better with family (free family coverage). Basis contributions are fully deductible (§10 Abs. 1 Nr. 3 EStG). | unverified: inherited figure or assumption; professional/source qualification required |
| Beitragsbemessungsgrenze | Social security contributions are capped at the Beitragsbemessungsgrenze. Income above the ceiling incurs no additional social security cost. | Retained context; see scope and source limits |

### Section 10 -- Red Lines

**Red Lines table**

| Risk | Detail | Source or qualification |
| --- | --- | --- |
| §42 AO (Gestaltungsmissbrauch) | An inappropriate legal arrangement is abusive if, compared with an appropriate arrangement, it produces a tax advantage not provided for by law for the taxpayer or a third party. This does not apply if the taxpayer proves non-tax reasons significant in the overall circumstances. Apply AO § 42(1)’s priority and tax-consequence rules below. | https://www.gesetze-im-internet.de/ao_1977/__42.html |
| Scheinselbständigkeit | If effectively an employee of one client, reclassification triggers full social security contributions and back-payments. | Retained context; see scope and source limits |
| IAB without investment intent | If the investment is not made within 3 years, the IAB is reversed with interest (§§ 233a and 238 Abs. 1a AO: 0.15% a month, 1.8% a year, from 15 months after the tax year). | unverified: inherited figure or assumption; professional/source qualification required |
| Fictitious family employment | Spouse/family employment must be genuine: written contract, actual work, arm's-length salary, regular payment. BFH scrutinizes closely. | Retained context; see scope and source limits |
| Private expenses as business | The Finanzamt will disallow expenses that are not exclusively or predominantly business-related. Mixed-use items require documented apportionment. | Retained context; see scope and source limits |
| Liebhaberei (hobby) | If a business consistently makes losses with no realistic profit expectation, the Finanzamt may reclassify it as Liebhaberei and disallow all losses. | Retained context; see scope and source limits |
| Excessive Homeoffice claims | From 2026, the BFH requires comprehensive documentation: room sketches, usage logs, actual cost receipts. | unverified: inherited figure or assumption; professional/source qualification required |

Under [AO § 42(1)](https://www.gesetze-im-internet.de/ao_1977/__42.html), a specific statutory anti-avoidance provision determines the consequences when its conditions are met. Otherwise, where subsection (2)’s abuse test is met, the tax claim arises as it would under a legal arrangement appropriate to the economic transactions. [EGAO article 97 § 7](https://www.gesetze-im-internet.de/aoeg_1977/art_97__7.html) applies the 2007 version from 1 January 2008 for calendar years beginning after 31 December 2007; earlier years retain the applicable earlier text. Assess any actual arrangement against its facts and all applicable specific rules before recommending or implementing it.

## Self-checks

Confirm the workflow base and output specification; retain all original refusal codes; trace each material input to evidence; establish the period and each source condition; recompute components; separate assumptions, unresolved items and nominal ceilings from actual entitlements; obtain professional review and all required filing/registration confirmations before acting.

## Sources

The table distinguishes previously evidenced complete or selected readings from inherited citations whose reading date is not established. No new source reading is claimed. A recorded reading does not establish every historical application, amendment, incorporated rule or actual-case condition.

| Source | URL | Read on |
| --- | --- | --- |
| Inherited legislation citation; period and extent unqualified | https://www.gesetze-im-internet.de/estg/ | Reading date not established in retained evidence; unverified |
| AO42: Complete selected unit with printed footnotes; retained text including printed footnotes read in the prior qualification | https://www.gesetze-im-internet.de/ao_1977/__42.html | 2026-11-01 |
| Inherited legislation citation; period and extent unqualified | https://www.gesetze-im-internet.de/estg/__32a.html | Reading date not established in retained evidence; unverified |
| Inherited legislation citation; period and extent unqualified | https://www.gesetze-im-internet.de/estg/__7g.html | Reading date not established in retained evidence; unverified |
| estg __10d.html: Complete unit with printed footnotes; retained text including printed footnotes read in the prior qualification | https://www.gesetze-im-internet.de/estg/__10d.html | 2026-11-01 |
| estg __52.html: Only complete paragraph (18b), not the full section; retained text including printed footnotes read in the prior qualification | https://www.gesetze-im-internet.de/estg/__52.html | 2026-11-01 |
| EGAO Art97 §7: Complete selected unit with printed footnotes; retained text including printed footnotes read in the prior qualification | https://www.gesetze-im-internet.de/aoeg_1977/art_97__7.html | 2026-11-01 |

Not yet confirmed: complete VZ 2026 source/amendment chain; inherited marginal-rate shortcuts and approximate savings; commuting, home-office/BFH, IAB/Sonderabschreibung, GWG, pension and social-security claims; universal incorporation advice; VAT eligibility/input-tax/timing and planning-calendar rows; full section 52 and historical loss limits; actual taxpayer restrictions, notices, fields, acknowledgments and implementation/filing readiness.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The upstream project is maintained at [openaccountants.com](https://www.openaccountants.com). This fork's migrated version and recorded review status are maintained in [ryanduguid/openaccountants](https://github.com/ryanduguid/openaccountants); upstream services do not publish or verify this fork's changes.

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
