---
name: pl-corporate-income-tax
description: >
  Poland corporate income tax reference for an ordinary resident sp. z o.o. or
  S.A. in tax year 2026. Covers CIT rates of 19% and 9%, income sources,
  non-deductible items, debt financing limit, losses, reliefs, monthly and
  quarterly advances, CIT-8 dates, JPK_CIT, penalties and a fictional computation.
  Trigger on Polish CIT, CIT-8, sp. z o.o. tax, zaliczki or minimum tax. Refuses
  tax groups, financial sector, Estonian CIT computation, minimum tax computation,
  non-residents and Pillar Two scope. This source-cited draft awaits local
  professional review and is not filing readiness.
jurisdiction: PL
category: international
tax_year: 2026
tax_year_notes: "Calendar tax year 2026. Consolidated text Dz.U. 2026 poz. 554, status 18 March 2026, read with later amenders to 31 October 2026."
tier: 2
last_updated: 2026-11-03
version: 0.3
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Poland Corporate Income Tax: Ordinary Resident Sp. z o.o. and S.A., 2026

Load this on top of `corporate-income-tax-workflow-base`. Its runbook, 26-field intake, output specification and 18 self-checks apply; this file fills its section 9 slots. A slot marked HOLD was not established from the sources read for this draft, and no figure may be supplied for it from memory.

Article references are to the CIT Act of 15 February 1992 (Dz.U. 2026 poz. 554) unless stated. Later amenders were checked: poz. 779, 846, 912, 1123, 1287 and 1371 change no rate or base rule for an ordinary 2026 company. Poz. 331 (28 March 2026) concerns banks; only its art 12 was sighted.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This is a template migration of retained research, not a new law-reading exercise or whole-guide current-law verification. The dated events below identify historical source checks with their actual retained extents. Acquisition times, legal cutoffs and this migration date are not reading dates. Every retained table row is explicitly unverified in this migration; the source index does not independently qualify every statement on that row. Resolve all applicable holds before using a figure.

## Scope

Ordinary resident standalone companies, calendar tax year 2026, within the exclusions retained in the boundary table. Load the stated workflow bases before computing. The historical source and delivery limits remain binding.

### [CROSS-REFERENCES]

| Topic | Position | Source or qualification |
|---|---| --- |
| Withholding tax | Outbound dividends 19% (art 22(1)); interest, royalties and listed services 20% (art 21(1)). Pay and refund above PLN 2m for related payments under art 21(1)(1) and 22(1), on the excess (art 26(2e)). Surcharges on ordinary companies: none in art 19. Treaty relief: escalate | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Pillar Two | Above; refused | unverified: retained statement; scoped source checks below do not qualify this whole row |
| DAC6 | Above | unverified: retained statement; scoped source checks below do not qualify this whole row |
| IP box, R&D | Credits slot | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Free zone | HOLD | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Transfer pricing | Transfer pricing workflow base | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Deferred tax | Reviewer sets the provision | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Payroll, VAT, formation, annual accounts | Separate guides | unverified: retained statement; scoped source checks below do not qualify this whole row |

## Ask the client first

- Entity, residence, reporting period, ordinary-regime eligibility and each boundary trigger.
- Current-year revenue and prior-year VAT-inclusive sales, separately evidenced EUR conversions and startup/restructuring history.
- Ledger, income-source allocation, permanent/temporary differences, debt costs and connected transactions.
- Loss vintage, same-source amount, prior use and chosen statutory option; separately supported relief eligibility.
- Advances, actual payment records, return obligations and proposed filing date.
- Group/foreign interests, audit/accounts status and any unresolved legal or procedural hold.

## The method, step by step

Confirm scope and inputs; identify the regime; reconcile each income source from the ledger; apply supported adjustments, losses and reliefs in their required order; compute liability and reconcile advances; complete all boundary, filing and review holds. Do not turn the hypothetical examples into eligibility decisions.

### [RATES]

| Rate | Rule | Source | Source or qualification |
|---|---|---| --- |
| 19% | Standard | Art 19(1)(1) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 9% | On income other than capital gains, if revenue in the year is at most the PLN equivalent of EUR 2m, at the NBP rate on the first business day of the year, rounded to PLN 1,000, and pro-rated by full months for a year that is not 12 months (where no full calendar month is covered, 30 days counts as a month; the order of pro-rating and rounding goes to the reviewer), **and** the company is a small taxpayer: prior-year sales revenue including VAT at most EUR 2m, at the NBP rate on the first business day of October of that prior year, rounded to PLN 1,000. The small taxpayer test does not apply in the first year of activity, subject to art 19(1a) and (1c) | Art 19(1)(2)(a), (b), (1d), (1e), 4a(10), from 1 January 2026 | unverified: retained statement; scoped source checks below do not qualify this whole row |

- **Exclusions from 9%:** tax groups and family foundations (art 19(1b)). For the start year and the next: companies formed by transformation, merger or split, except a company transformed into another company; formed by transforming a sole trader or a partnership without legal personality; or formed with, or within the formation year and the next receiving as capital, a previously run business, an organised part or its assets above EUR 10,000; or formed with in-kind assets from liquidated companies in which the contributor held shares (art 19(1a)). Cash contributions are not listed. For the year of the event and the next: a company that split, or that contributed such a business or assets above EUR 10,000, or such liquidation assets, to another entity (art 19(1c)). A reviewer tests these. Whether capital revenue counts towards EUR 2m is not settled by the text: if it changes the result, hold the rate.
- **Advances:** computed at 19% by default; start-ups and small taxpayers may use 9% until revenue passes the limit (art 25(1f), (1g)).
- **Income sources:** capital gains and other income are taxed separately, and a loss in one cannot reduce the other (art 7(1), (3)(2a), 7b(1)). Capital gains stay at 19%.
- **Minimum tax (art 24ca):** a test for each company. It is 10% of a special base where the non-capital source shows a loss or a margin of at most 2%, after the art 24ca(2) adjustments, which leave out items including fixed asset depreciation and lease fees. Exclusions in art 24ca(14) include small taxpayers, start-up plus 2 years, a 30% revenue fall, owners who are only individuals and hold no over-5% shares and similar interests, a 2% margin in one of the previous 3 years, and insolvency. The list is longer. If triggered, refuse.
- **Estonian CIT (arts 28j, 28k, 28o):** tax on distribution at 10% for small or start-up taxpayers, otherwise 20%. Eligibility: under 50% passive revenue, 3 non-owner staff for at least 300 days or the art 28j(1)(3)(b) alternative, individual owners, no shareholdings, no IFRS, notice by the end of the first month, and no art 28k exclusion. If elected, refuse.
- **Reduced rates by activity:** IP Box 5% (art 24d): reviewer.
- **Branch profits tax:** out of scope.

### [ADJUSTMENTS]

Income is revenue less deductible costs for each source (art 7). A cost is deductible if incurred to earn revenue or to preserve or secure its source, unless listed in art 16(1) (art 15(1)).

**Main non-deductible items in art 16(1). This list is not exhaustive:**

| Point | Item | Source or qualification |
|---|---| --- |
| 1 | Capital expenditure on land and fixed assets; the undepreciated cost is deductible on a sale for consideration | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 14 | Gifts | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 15, 15b | Income tax; top-up taxes | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 18 | Fines and penalties, and interest on them | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 21 | Late-payment interest on budget amounts | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 22 | Contractual penalties and damages for defects or delay | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 26, 26a, 27 | Reserves and write-downs | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 28 | Entertainment | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 46 | Deductible VAT | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 66 | Unlawful acts | unverified: retained statement; scoped source checks below do not qualify this whole row |

**Cars (art 16(1)(4), (49), (49a), (51)):** depreciation limit PLN 225,000 for electric and hydrogen cars; PLN 150,000 under 50 g/km; PLN 100,000 at or above 50 g/km. Lease and rental fees are limited in the same proportion that the limit bears to the car's value (point 49a). Insurance limit PLN 150,000 of value, also proportional (point 49). Mixed use: 25% not deductible. HOLD on the transitional rule for older leases.

**Exempt income and dividends:**

- Domestic dividends are 19% but exempt with a 10% holding kept for 2 years and the recipient conditions in art 22(4) (art 22(1), (4), (4a)).
- Foreign dividends: exempt from an EU or EEA payer on a 10% direct holding for 2 years, 25% for Switzerland, where the payer could not deduct them and on the other conditions (art 20(3), (9), (11), (12), (16)).

**Depreciation:** low-value assets up to PLN 10,000 (art 16d(1)); rates by the Schedule (art 16i(1)); one-off up to EUR 50,000 for small or start-up taxpayers, on groups 3 to 8 except cars (art 16k(7)); PLN 100,000 on brand-new assets in groups 3 to 6 and 8, on the art 16k(15) conditions (art 16k(14)). A reviewer applies the Schedule.

**Debt financing limit (art 15c):** excess debt financing costs are not deductible above the higher of PLN 3m or 30% of tax EBITDA, as the art 15c(1) formula defines it. The PLN 3m is pro-rated at PLN 250,000 a month only for a tax year that is not 12 months (art 15c(1a)), and is unavailable for financing from a family foundation (art 15c(1b)). Carryforward 5 years (art 15c(18)). Excess at or above that limit goes to the reviewer. Art 15e is repealed.

### [LOSSES]

| Point | Rule | Art | Source or qualification |
|---|---|---| --- |
| Period | 5 following years, by source | 7(5) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Annual use | At most 50% of the loss each year, or a one-off deduction up to PLN 5m with the rest over the remaining years at 50% | 7(5)(1), (2) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Across sources | Barred | 7(3)(2a) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Virtual currency disposal losses | Outside these rules: hold | 7(6) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Carryback | Only the COVID-19 rule in art 38f was located, so none in general for 2026 (inference) | 38f | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Mergers and acquisitions | Merged-entity losses barred; acquirer's losses barred on an activity change or 25% new owners | 7(3)(4), (7) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Group relief | Refused | 1a | unverified: retained statement; scoped source checks below do not qualify this whole row |

### [CREDITS]

- **Foreign tax:** proportional credit (art 20(1)). HOLD any computation.
- **Withholding on interest received and other credits:** HOLD.
- **Donations:** deduction from income for public-benefit bodies, with a combined cap of 10% of income, and exclusions (art 18(1)(1), (1a)). HOLD on its order against losses.
- **R&D relief:** 200% of staff costs, for the share of working time spent on R&D, and 100% of other listed costs, with higher limits for art 18d(3a) research centres (art 18d(2), (7)). The deduction cannot exceed non-capital income for the year (art 18d(1)); the rest carries forward 6 tax years (art 18d(8)).
- **Other reliefs (reviewer):** IP Box 5% (art 24d); robotisation 50% (art 38eb); prototype 30% (art 18ea); sales growth to PLN 1m (art 18eb); CSR 50% (art 18ee); venture capital PLN 250,000 (art 18ec).

## Boundary and exception table

### Scope and refusals

**In scope:** a solvent sp. z o.o. or S.A. with seat or management in Poland (art 3(1)), with a calendar tax year, standing alone, and taxed under the ordinary regime.

**Refuse and escalate, without computing:**

| Trigger | Reason | Source or qualification |
|---|---| --- |
| Bank, credit union, insurer, fund, other financial firm | R-CIT-1, R-CIT-2; art 19(1)(3) to (5) sector rates and art 38ab | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Tax capital group (art 1a) | Group rules are not covered | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Estonian CIT election | Eligibility and rates below; computation refused | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Minimum tax triggered (art 24ca) | Test below; computation refused | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Holding company relief (arts 24m to 24o) | Conditions need reviewer judgement | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Family foundation funding | Scope choice; not covered | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Liquid fuel producer or licensed importer | Windfall tax Act, Dz.U. 2026 poz. 1287, which adds art 38zb | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Non-resident company or Polish branch | Not covered | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Liquidation or insolvency | R-CIT-10 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Disputed or dual residence, hybrid arrangement | R-CIT-9, R-CIT-12 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Revenue at or above EUR 750m in 2 of the previous 4 years (Dz.U. 2024 poz. 1685) | Pillar Two | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Merger, or a takeover followed by a change of activity or 25% new owners, with a claim to keep losses (art 7(3)(4), 7(3)(7)) | R-CIT-8 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Audit or a deficiency notice | R-CIT-6 | unverified: retained statement; scoped source checks below do not qualify this whole row |

### [ANTI-AVOIDANCE]

- **GAAR:** OP art 119a. A benefit contrary to the purpose of the law, where that benefit is the main or one of the main aims and the arrangement is artificial. Any such position goes to R-CIT-7.
- **CFC:** art 24a, 19%. Tests include a listed state, a state without an information exchange basis, or over 50% control (including de facto control) with 33% passive income and tax at least 25% lower. Art 24a(3)(4) and the substance exit were not read. Any foreign subsidiary goes to the reviewer, without applying the tests here.
- **Hybrids:** arts 16n to 16u, located only. Escalate under R-CIT-12.
- **DAC6:** OP art 86a from 1 October 2026 covers cross-border arrangements (poz. 846). Reviewer.
- **BEAT or GILTI equivalent:** HOLD.

### [PILLAR TWO OVERLAY]

Dz.U. 2024 poz. 1685: EUR 750m in 2 of 4 years; 15%; income inclusion, national top-up and undertaxed profits rules, from 1 January 2025. HOLD on UTPR commencement and domestic top-up details. An in-scope company is refused here.

## Worked cases

### Worked example (fictional)

Scofield Inżynieria sp. z o.o.; calendar 2026; revenue PLN 20,000,000, above the 9% limit; all income from the non-capital source; no capital gains; debt financing costs PLN 100,000, below the PLN 3m limit.

Accounting profit before CIT is PLN 2,000,000, after these items: fine imposed in administrative proceedings PLN 10,000; late-payment interest on tax PLN 5,000; hospitality for clients PLN 20,000; accounting reserve not listed in the Act as a cost PLN 30,000. Loss from the same source in 2024: PLN 400,000, none used yet, with the 50% option chosen. Advances paid: PLN 300,000.

| Step | PLN | Source or qualification |
|---|---| --- |
| Accounting profit before CIT | 2,000,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Fine (art 16(1)(18)) | +10,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Late-payment interest (art 16(1)(21)) | +5,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Entertainment (art 16(1)(28)) | +20,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Reserve (art 16(1)(27)) | +30,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Income | 2,065,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Loss, 50% of 400,000 (art 7(5)(1)) | -200,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Tax base | 1,865,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| CIT at 19% | 354,350 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Balance after PLN 300,000 advances | 54,350 | unverified: retained statement; scoped source checks below do not qualify this whole row |

Minimum tax test: 2,065,000 / 20,000,000 = 10.325%, above 2%, so it is not triggered. The example makes no art 24ca(2) adjustment; a reviewer checks that.

The 9% rate fails at the current-year revenue test, so small taxpayer status is not reached.

**One-off alternative:** deducting the whole PLN 400,000 under art 7(5)(2) gives a base of PLN 1,665,000 and CIT of PLN 316,350.

### Executable comparison and assumptions

Both blocks use the fictional ledger above. Eligibility for the ordinary 19% regime, every adjustment, the same-source loss, its 5-year window and availability of both loss options are stipulated, with no prior use and sufficient income. The one-off option is compared only after those conditions are established; it does not promise a lifetime tax saving. All other items, credits and payments are unchanged. The inherited revenue-rate conclusion needs its applicable EUR/PLN conversion verified; no exchange rate is inferred from the PLN revenue. The inherited minimum-tax ratio assumes no Article 24ca(2) adjustment and does not replace the complete trigger/exclusion review; any unresolved trigger remains a refusal.

```oa-check
name: PL CIT same-source 50-percent loss option, hypothetical 2026
inputs:
  profit: 2000000
  fine: 10000
  tax_interest: 5000
  entertainment: 20000
  reserve: 30000
  loss: 400000
  rate: 0.19
  advances: 300000
steps:
  - income: profit + fine + tax_interest + entertainment + reserve
  - loss_used: loss * 0.5
  - base: income - loss_used
  - cit: base * rate
  - balance: cit - advances
expected:
  income: 2065000
  loss_used: 200000
  base: 1865000
  cit: 354350
  balance: 54350
```

```oa-check
name: PL CIT decision: same-source one-off option versus 50 percent
inputs:
  income: 2065000
  loss: 400000
  one_off_cap: 5000000
  rate: 0.19
  advances: 300000
steps:
  - half_base: income - loss * 0.5
  - one_off_used: min(loss, one_off_cap)
  - one_off_base: income - one_off_used
  - half_cit: half_base * rate
  - one_off_cit: one_off_base * rate
  - difference: half_cit - one_off_cit
  - balance: one_off_cit - advances
expected:
  one_off_used: 400000
  one_off_base: 1665000
  half_cit: 354350
  one_off_cit: 316350
  difference: 38000
  balance: 16350
```

## When to refuse or refer

Apply every boundary refusal above. Do not fill a HOLD from memory or describe this draft as a filing-ready computation.

### Delivery holds

This reference is a Tier 2 draft pending review by a Polish tax adviser. It establishes no filing, form version or administrative practice. Tax authority interpretations and case law were not read and can narrow or extend the statute. Output is a working paper under the base's section 10.

## Filing and payment

### [REGIME IDENTIFICATION]

- **Jurisdiction:** PL.
- **Statutes:** CIT Act; Ordynacja podatkowa (OP, Dz.U. 2026 poz. 622); Kodeks karny skarbowy (KKS, Dz.U. 2025 poz. 633).
- **Authority:** the tax office (urząd skarbowy), through electronic filing. Portal name: HOLD.
- **Form:** CIT-8, named on the official portal. The Act says 'established form' (art 27(1)).

**Dates for tax year 2026:**

| Item | Rule | Date | Source | Source or qualification |
|---|---|---|---| --- |
| Return and balance | End of month 3 of the following year, electronically | 31 March 2027 | Art 27(1), (1c) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Monthly advance | By the 20th, for the previous month | See below | Art 25(1a) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Quarterly advance (small and first-year taxpayers) | By the 20th after the quarter | 20 April, 20 July, 20 October 2026; 20 January 2027 | Art 25(1b), (1c) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Tax books (JPK_CIT) where required | End of month 7 after the year end | 31 July 2027 is a Saturday, so 2 August 2027 if OP art 12 §5 applies | Art 9(1c), poz. 779; inference on the shift | unverified: retained statement; scoped source checks below do not qualify this whole row |

- **Monthly dates, shifted for weekends under OP art 12 §5:** 20 February, 20 March, 20 April, 20 May, 22 June, 20 July, 20 August, 21 September, 20 October, 20 November and 21 December 2026, and 20 January 2027. The statutory holiday list was not read, so only weekends are accounted for.
- **Quarterly exclusion:** a first-year company formed by transformation, merger or split, by transforming a partnership without legal personality, or by individuals contributing a business or assets above EUR 10,000 cannot use quarterly advances (art 25(1d), 16k(11)).
- **Final advance:** none is due if the return is filed and the tax paid before its date (art 25(1a), (1c)).
- **Weekend rule:** OP art 12 §5 was reworded from 1 October 2026 (poz. 846 arts 1(1), 35). A reviewer confirms that shifts after that date still reach payments.
- **Simplified advances:** for 2026, 1/12 of the tax on the return filed in 2025; if it showed no tax, the return filed in 2024 (art 25(6)). If neither showed tax, the simplified form is not available. A reference return covering a year that is not 12 months is apportioned monthly under art 25(6a): reviewer. Art 25(7) onward was not read.
- **JPK_CIT start (Dz.U. 2021 poz. 2105 art 66(2), as amended by Dz.U. 2023 poz. 1059 art 13):** years after 31 December 2024 for tax groups and revenue above EUR 50m; after 2025 for JPK VAT filers; after 2026 for others. A search of later amendments found no change to that article; the search is not a full read.

### [FILING MECHANICS]

- CIT-8 electronically, with payment (art 27(1), (1c)).
- Tax books per art 9, as amended by poz. 779, from 1 July 2026.
- Transfer pricing local file: PLN 10m for goods and financial transactions, PLN 2m for services and other; tax-haven PLN 2.5m and PLN 0.5m; information by the end of month 11 (arts 11k, 11t). Poz. 1371 changes TP information for years starting after 31 December 2025: reviewer.
- **Audit and accounts:** screen all Accounting Act art 64 categories and special routes before concluding whether an audit is required. Annual accounts of continuing S.A. are audited except those in organisation at the balance date. For the remaining-entity route, at least 2 of the preceding year's measures must reach 50 average full-time equivalent staff, EUR 3.125m assets or EUR 6.25m net sales of goods and products, converted under art 3(2). Audit status and small-company presentation are separate. Ordinary approval is within 6 months, with a required audit before approval (art 53(1), (1a)); KRS filing is within 15 days of approval, with separate unapproved/repeated filing under art 69(2). Selected changes in poz. 640, 644 and future poz. 1206 were checked on 1 November 2026; their different commencement and excluded branch/group routes do not create a 60-day ordinary filing period. See `pl-small-company-financial-statements` for the scoped ordinary small-but-not-micro sp. z o.o. Annex 5 workflow, its elections, periods and holds. This paragraph is not a requalification of the rest of this tax guide.

**Consequences:**

| Item | Rule | Source | Source or qualification |
|---|---|---| --- |
| Late-payment interest | 200% of the NBP lombard rate plus 2%, minimum 8%; take the current rate from NBP. Also on advances, on the part above the tax due. Halved on correction within 6 months and payment within 7 days, with exclusions | OP arts 53, 56, 56a | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Not filing to evade tax | Fiscal offence: up to 720 daily rates, or prison, or both; fine only at small value; petty offence below the threshold | KKS arts 54, 23, 53 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Late return where the taxable matter was disclosed | Petty offence | KKS art 56(4) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Persistent non-payment | Petty offence | KKS art 57, 48 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Voluntary disclosure | Notify and pay in full; ineffective after documented knowledge or action | KKS art 16 | unverified: retained statement; scoped source checks below do not qualify this whole row |

KKS was read in Dz.U. 2025 poz. 633; amenders poz. 347, 421, 846 and 901 did not touch the cited articles in the parts read (poz. 846 art 8 points 5 and 6 were not seen). Any fiscal offence exposure goes to the reviewer. Amounts round to full zloty, with under 50 groszy dropped (OP art 63 §1).

## Completion checklist

- Confirm ordinary-regime scope and clear every boundary trigger or refer.
- Reconcile both income sources, adjustments, loss history, reliefs, liability and advances to evidence.
- Check the actual return version, instructions, calendar, extensions and payment reference; unresolved operational slots remain held.
- Keep accounting approval, audit, filing, CIT return/payment and JPK duties separate.
- Deliver the base workflow outputs and a reviewer brief listing every unresolved source, fact and procedural item.
- Obtain qualified Polish professional review before filing, paying or acting.

## Sources

This is a template migration of retained research, not a new law-reading exercise or whole-guide current-law verification. The dated events below identify historical source checks with their actual retained extents. Acquisition times, legal cutoffs and this migration date are not reading dates. Every retained table row is explicitly unverified in this migration; the source index does not independently qualify every statement on that row. Resolve all applicable holds before using a figure.

| Official source | Exact URL | Recorded date and event | Reading extent and limits |
|---|---|---|---|
| CIT consolidation metadata | https://api.sejm.gov.pl/eli/acts/DU/2026/554 | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Metadata link, not a whole-law text reading. |
| Dz.U. 2026 poz. 554 | https://api.sejm.gov.pl/eli/acts/DU/2026/554/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected CIT clauses for rates, base, losses, reliefs and dates; legal cutoff 18 March 2026; not whole Act. |
| Dz.U. 2026 poz. 779 | https://api.sejm.gov.pl/eli/acts/DU/2026/779/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected CIT article including Article 9(1c), not whole Act. |
| Dz.U. 2026 poz. 846 | https://api.sejm.gov.pl/eli/acts/DU/2026/846/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected CIT references and amendment Article 35 / OP Article 86a scope; KKS Article 8 points 5/6 not seen; not whole 29-page Act. |
| Dz.U. 2026 poz. 912 | https://api.sejm.gov.pl/eli/acts/DU/2026/912/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected Article 17(1)(4g) effect only. |
| Dz.U. 2026 poz. 1123 | https://api.sejm.gov.pl/eli/acts/DU/2026/1123/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected Articles 6/15(1za); commencement exception list clipped, Article 6 commencement unconfirmed. |
| Dz.U. 2026 poz. 1287 | https://api.sejm.gov.pl/eli/acts/DU/2026/1287/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected fuel-only effect, not whole Act. |
| Dz.U. 2026 poz. 1371 | https://api.sejm.gov.pl/eli/acts/DU/2026/1371/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected Article 2 points 3/4 and transfer-pricing effect only. |
| Dz.U. 2026 poz. 622 | https://api.sejm.gov.pl/eli/acts/DU/2026/622/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected OP clauses including 119a section 1, 56 section 1, 63 section 1 and 86a scope; holiday list unread; no full current penalty calculation. |
| Dz.U. 2025 poz. 633 | https://api.sejm.gov.pl/eli/acts/DU/2025/633/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected KKS Articles 16 sections 1/2/5, 23 section 1, 48 section 1, 53 sections 3/6, 54 sections 1-3 and 57 section 1, not whole Code. |
| Dz.U. 2026 poz. 347 | https://api.sejm.gov.pl/eli/acts/DU/2026/347/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected KKS-amender checks only, not whole Act. |
| Dz.U. 2026 poz. 421 | https://api.sejm.gov.pl/eli/acts/DU/2026/421/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected KKS-amender checks only, not whole Act. |
| Dz.U. 2026 poz. 901 | https://api.sejm.gov.pl/eli/acts/DU/2026/901/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected KKS-amender checks only, not whole Act. |
| Dz.U. 2024 poz. 1685 | https://api.sejm.gov.pl/eli/acts/DU/2024/1685/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected EUR 750m/2-of-4-years/15%/commencement only; UTPR HOLD. |
| Dz.U. 2023 poz. 1059 | https://api.sejm.gov.pl/eli/acts/DU/2023/1059/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Selected Article 13/JPK start chain; later amendment search is not full reading. |
| Dz.U. 2026 poz. 331 | https://api.sejm.gov.pl/eli/acts/DU/2026/331/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Article 12 sighted only; banks out of scope. |
| Dz.U. 2026 poz. 522 | https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Original selected Articles 53(1), 64(1)(4) and 69(1); expanded 1 November accounts check separately recorded below. |
| 2021 poz. 2105 start-chain metadata | https://api.sejm.gov.pl/eli/acts/DU/2021/2105 | 2026-10-31: original guide records source check; separate per-URL reading day not independently recorded | Article 66(2) read/search statement retained; inspected evidence does not bind an exact text URL, so none is invented. |
| Inherited form-name lead | https://www.podatki.gov.pl | Reading date not established | Generic homepage, not an identified form/instruction page. Do not substitute capture timestamps for reading. |
| Dz.U. 2026 poz. 522 | https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf | 2026-11-01: historical independent source check | Selected complete articles/clauses and complete Annex 5 only; 89-unit retained map. Legal cutoff 26 March 2026, not a whole-Act reading. |
| Dz.U. 2026 poz. 640 | https://api.sejm.gov.pl/eli/acts/DU/2026/640/text.pdf | 2026-11-01: historical independent source check | Complete 1-page Act, all 4 articles and metadata; audit changes and transition. |
| Dz.U. 2026 poz. 644 | https://api.sejm.gov.pl/eli/acts/DU/2026/644/text.pdf | 2026-11-01: historical independent source check | Complete selected Articles 1, 2, 6, 18 and 19 and relevant footnotes; not the whole 35-page Act. Later ESAP/KSH dates are not 2026 duties. |
| Dz.U. 2026 poz. 1206 | https://api.sejm.gov.pl/eli/acts/DU/2026/1206/text.pdf | 2026-11-01: historical independent source check | Complete Articles 2 and 57 only, not the whole 51-page Act; 11 January 2027 commencement qualified. |
| Dz.U. 2024 poz. 18 | https://api.sejm.gov.pl/eli/acts/DU/2024/18/text.pdf | 2026-11-01: historical independent source check | Complete KSH Articles 4, 151, 156, 191-197, 227, 228 and 231; legal cutoff 5 December 2023; later full amendment chain not established. |
| Dz.U. 2024 poz. 96 | https://api.sejm.gov.pl/eli/acts/DU/2024/96/text.pdf | 2026-11-01: historical independent source check | Complete constitutional judgment only; broadcasting subject excluded. |
| Dz.U. 2026 poz. 176 | https://api.sejm.gov.pl/eli/acts/DU/2026/176/text.pdf | 2026-11-01: historical independent source check | Complete selected Article 1 and Articles 28-35 only; not whole Act. |
| Dz.U. 2026 poz. 187 | https://api.sejm.gov.pl/eli/acts/DU/2026/187/text.pdf | 2026-11-01: historical independent source check | Complete selected Article 138 and Articles 147-161 only; not whole Act. |

### Sources

Sources were checked on 31 October 2026. Official text through the [Sejm ELI API](https://api.sejm.gov.pl/eli/acts/DU/2026/554): CIT Act, Dz.U. 2026 poz. 554, with Dz.U. 2026 poz. 779, 846, 912, 1123, 1287, 1371; Ordynacja podatkowa, Dz.U. 2026 poz. 622; KKS, Dz.U. 2025 poz. 633; Dz.U. 2024 poz. 1685; Dz.U. 2023 poz. 1059; Accounting Act, Dz.U. 2026 poz. 522. Form name: [podatki.gov.pl](https://www.podatki.gov.pl).

Not yet confirmed: every retained HOLD; full later-law and commencement chain; current forms, field mapping, portal, payment-reference and submission workflow; statutory holidays and live dates; unqualified source rows; current-law accuracy of inherited claims and suitability for an actual engagement. The 1 November accounts checks do not requalify the 31 October CIT source set.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The upstream project is maintained at [openaccountants.com](https://www.openaccountants.com). This fork's migrated version and recorded review status are maintained in [ryanduguid/openaccountants](https://github.com/ryanduguid/openaccountants); upstream services do not publish or verify this fork's changes.

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
