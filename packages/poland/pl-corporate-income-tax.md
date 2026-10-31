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
last_updated: 2026-10-31
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - corporate-income-tax-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Poland Corporate Income Tax: Ordinary Resident Sp. z o.o. and S.A., 2026

Load this on top of `corporate-income-tax-workflow-base`. Its runbook, 26-field intake, output specification and 18 self-checks apply; this file fills its section 9 slots. A slot marked HOLD was not established from the sources read for this draft, and no figure may be supplied for it from memory.

Article references are to the CIT Act of 15 February 1992 (Dz.U. 2026 poz. 554) unless stated. Later amenders were checked: poz. 779, 846, 912, 1123, 1287 and 1371 change no rate or base rule for an ordinary 2026 company. Poz. 331 (28 March 2026) concerns banks; only its art 12 was sighted.

## Scope and refusals

**In scope:** a solvent sp. z o.o. or S.A. with seat or management in Poland (art 3(1)), with a calendar tax year, standing alone, and taxed under the ordinary regime.

**Refuse and escalate, without computing:**

| Trigger | Reason |
|---|---|
| Bank, credit union, insurer, fund, other financial firm | R-CIT-1, R-CIT-2; art 19(1)(3) to (5) sector rates and art 38ab |
| Tax capital group (art 1a) | Group rules are not covered |
| Estonian CIT election | Eligibility and rates below; computation refused |
| Minimum tax triggered (art 24ca) | Test below; computation refused |
| Holding company relief (arts 24m to 24o) | Conditions need reviewer judgement |
| Family foundation funding | Scope choice; not covered |
| Liquid fuel producer or licensed importer | Windfall tax Act, Dz.U. 2026 poz. 1287, which adds art 38zb |
| Non-resident company or Polish branch | Not covered |
| Liquidation or insolvency | R-CIT-10 |
| Disputed or dual residence, hybrid arrangement | R-CIT-9, R-CIT-12 |
| Revenue at or above EUR 750m in 2 of the previous 4 years (Dz.U. 2024 poz. 1685) | Pillar Two |
| Merger, or a takeover followed by a change of activity or 25% new owners, with a claim to keep losses (art 7(3)(4), 7(3)(7)) | R-CIT-8 |
| Audit or a deficiency notice | R-CIT-6 |

## [REGIME IDENTIFICATION]

- **Jurisdiction:** PL.
- **Statutes:** CIT Act; Ordynacja podatkowa (OP, Dz.U. 2026 poz. 622); Kodeks karny skarbowy (KKS, Dz.U. 2025 poz. 633).
- **Authority:** the tax office (urząd skarbowy), through electronic filing. Portal name: HOLD.
- **Form:** CIT-8, named on the official portal. The Act says 'established form' (art 27(1)).

**Dates for tax year 2026:**

| Item | Rule | Date | Source |
|---|---|---|---|
| Return and balance | End of month 3 of the following year, electronically | 31 March 2027 | Art 27(1), (1c) |
| Monthly advance | By the 20th, for the previous month | See below | Art 25(1a) |
| Quarterly advance (small and first-year taxpayers) | By the 20th after the quarter | 20 April, 20 July, 20 October 2026; 20 January 2027 | Art 25(1b), (1c) |
| Tax books (JPK_CIT) where required | End of month 7 after the year end | 31 July 2027 is a Saturday, so 2 August 2027 if OP art 12 §5 applies | Art 9(1c), poz. 779; inference on the shift |

- **Monthly dates, shifted for weekends under OP art 12 §5:** 20 February, 20 March, 20 April, 20 May, 22 June, 20 July, 20 August, 21 September, 20 October, 20 November and 21 December 2026, and 20 January 2027. The statutory holiday list was not read, so only weekends are accounted for.
- **Quarterly exclusion:** a first-year company formed by transformation, merger or split, by transforming a partnership without legal personality, or by individuals contributing a business or assets above EUR 10,000 cannot use quarterly advances (art 25(1d), 16k(11)).
- **Final advance:** none is due if the return is filed and the tax paid before its date (art 25(1a), (1c)).
- **Weekend rule:** OP art 12 §5 was reworded from 1 October 2026 (poz. 846 arts 1(1), 35). A reviewer confirms that shifts after that date still reach payments.
- **Simplified advances:** for 2026, 1/12 of the tax on the return filed in 2025; if it showed no tax, the return filed in 2024 (art 25(6)). If neither showed tax, the simplified form is not available. A reference return covering a year that is not 12 months is apportioned monthly under art 25(6a): reviewer. Art 25(7) onward was not read.
- **JPK_CIT start (Dz.U. 2021 poz. 2105 art 66(2), as amended by Dz.U. 2023 poz. 1059 art 13):** years after 31 December 2024 for tax groups and revenue above EUR 50m; after 2025 for JPK VAT filers; after 2026 for others. A search of later amendments found no change to that article; the search is not a full read.

## [RATES]

| Rate | Rule | Source |
|---|---|---|
| 19% | Standard | Art 19(1)(1) |
| 9% | On income other than capital gains, if revenue in the year is at most the PLN equivalent of EUR 2m, at the NBP rate on the first business day of the year, rounded to PLN 1,000, and pro-rated by full months for a year that is not 12 months (where no full calendar month is covered, 30 days counts as a month; the order of pro-rating and rounding goes to the reviewer), **and** the company is a small taxpayer: prior-year sales revenue including VAT at most EUR 2m, at the NBP rate on the first business day of October of that prior year. The small taxpayer test does not apply in the first year of activity, subject to art 19(1a) and (1c) | Art 19(1)(2)(a), (b), (1d), (1e), 4a(10), from 1 January 2026 |

- **Exclusions from 9%:** tax groups and family foundations (art 19(1b)). For the start year and the next: companies formed by transformation, merger or split, except a company transformed into another company; formed by transforming a sole trader or a partnership without legal personality; or formed with, or within the formation year and the next receiving as capital, a previously run business, an organised part or its assets above EUR 10,000; or formed with in-kind assets from liquidated companies in which the contributor held shares (art 19(1a)). Cash contributions are not listed. For the year of the event and the next: a company that split, or that contributed such a business or assets above EUR 10,000, or such liquidation assets, to another entity (art 19(1c)). A reviewer tests these. Whether capital revenue counts towards EUR 2m is not settled by the text: if it changes the result, hold the rate.
- **Advances:** computed at 19% by default; start-ups and small taxpayers may use 9% until revenue passes the limit (art 25(1f), (1g)).
- **Income sources:** capital gains and other income are taxed separately, and a loss in one cannot reduce the other (art 7(1), (3)(2a), 7b(1)). Capital gains stay at 19%.
- **Minimum tax (art 24ca):** a test for each company. It is 10% of a special base where the non-capital source shows a loss or a margin of at most 2%, after the art 24ca(2) adjustments, which leave out items including fixed asset depreciation and lease fees. Exclusions in art 24ca(14) include small taxpayers, start-up plus 2 years, a 30% revenue fall, owners who are only individuals and hold no over-5% shares and similar interests, a 2% margin in one of the previous 3 years, and insolvency. The list is longer. If triggered, refuse.
- **Estonian CIT (arts 28j, 28k, 28o):** tax on distribution at 10% for small or start-up taxpayers, otherwise 20%. Eligibility: under 50% passive revenue, 3 non-owner staff for at least 300 days or the art 28j(1)(3)(b) alternative, individual owners, no shareholdings, no IFRS, notice by the end of the first month, and no art 28k exclusion. If elected, refuse.
- **Reduced rates by activity:** IP Box 5% (art 24d): reviewer.
- **Branch profits tax:** out of scope.

## [ADJUSTMENTS]

Income is revenue less deductible costs for each source (art 7). A cost is deductible if incurred to earn revenue or to preserve or secure its source, unless listed in art 16(1) (art 15(1)).

**Main non-deductible items in art 16(1). This list is not exhaustive:**

| Point | Item |
|---|---|
| 1 | Capital expenditure on land and fixed assets; the undepreciated cost is deductible on a sale for consideration |
| 14 | Gifts |
| 15, 15b | Income tax; top-up taxes |
| 18 | Fines and penalties, and interest on them |
| 21 | Late-payment interest on budget amounts |
| 22 | Contractual penalties and damages for defects or delay |
| 26, 26a, 27 | Reserves and write-downs |
| 28 | Entertainment |
| 46 | Deductible VAT |
| 66 | Unlawful acts |

**Cars (art 16(1)(4), (49), (49a), (51)):** depreciation limit PLN 225,000 for electric and hydrogen cars; PLN 150,000 under 50 g/km; PLN 100,000 at or above 50 g/km. Lease and rental fees are limited in the same proportion that the limit bears to the car's value (point 49a). Insurance limit PLN 150,000 of value, also proportional (point 49). Mixed use: 25% not deductible. HOLD on the transitional rule for older leases.

**Exempt income and dividends:**

- Domestic dividends are 19% but exempt with a 10% holding kept for 2 years and the recipient conditions in art 22(4) (art 22(1), (4), (4a)).
- Foreign dividends: exempt from an EU or EEA payer on a 10% direct holding for 2 years, 25% for Switzerland, where the payer could not deduct them and on the other conditions (art 20(3), (9), (11), (12), (16)).

**Depreciation:** low-value assets up to PLN 10,000 (art 16d(1)); rates by the Schedule (art 16i(1)); one-off up to EUR 50,000 for small or start-up taxpayers, on groups 3 to 8 except cars (art 16k(7)); PLN 100,000 on brand-new assets in groups 3 to 6 and 8, on the art 16k(15) conditions (art 16k(14)). A reviewer applies the Schedule.

**Debt financing limit (art 15c):** excess debt financing costs are not deductible above the higher of PLN 3m or 30% of tax EBITDA, as the art 15c(1) formula defines it. The PLN 3m is pro-rated at PLN 250,000 a month only for a tax year that is not 12 months (art 15c(1a)), and is unavailable for financing from a family foundation (art 15c(1b)). Carryforward 5 years (art 15c(18)). Excess at or above that limit goes to the reviewer. Art 15e is repealed.

## [LOSSES]

| Point | Rule | Art |
|---|---|---|
| Period | 5 following years, by source | 7(5) |
| Annual use | At most 50% of the loss each year, or a one-off deduction up to PLN 5m with the rest over the remaining years at 50% | 7(5)(1), (2) |
| Across sources | Barred | 7(3)(2a) |
| Virtual currency disposal losses | Outside these rules: hold | 7(6) |
| Carryback | Only the COVID-19 rule in art 38f was located, so none in general for 2026 (inference) | 38f |
| Mergers and acquisitions | Merged-entity losses barred; acquirer's losses barred on an activity change or 25% new owners | 7(3)(4), (7) |
| Group relief | Refused | 1a |

## [CREDITS]

- **Foreign tax:** proportional credit (art 20(1)). HOLD any computation.
- **Withholding on interest received and other credits:** HOLD.
- **Donations:** deduction from income for public-benefit bodies, with a combined cap of 10% of income, and exclusions (art 18(1)(1), (1a)). HOLD on its order against losses.
- **R&D relief:** 200% of staff costs, for the share of working time spent on R&D, and 100% of other listed costs, with higher limits for art 18d(3a) research centres (art 18d(2), (7)). The deduction cannot exceed non-capital income for the year (art 18d(1)); the rest carries forward 6 tax years (art 18d(8)).
- **Other reliefs (reviewer):** IP Box 5% (art 24d); robotisation 50% (art 38eb); prototype 30% (art 18ea); sales growth to PLN 1m (art 18eb); CSR 50% (art 18ee); venture capital PLN 250,000 (art 18ec).

## [FILING MECHANICS]

- CIT-8 electronically, with payment (art 27(1), (1c)).
- Tax books per art 9, as amended by poz. 779, from 1 July 2026.
- Transfer pricing local file: PLN 10m for goods and financial transactions, PLN 2m for services and other; tax-haven PLN 2.5m and PLN 0.5m; information by the end of month 11 (arts 11k, 11t). Poz. 1371 changes TP information for years starting after 31 December 2025: reviewer.
- **Audit and accounts (Accounting Act, Dz.U. 2026 poz. 522):** all S.A. are audited, except those in organisation at the balance date. Others are audited if they met 2 of 50 full-time staff, EUR 3.125m assets and EUR 6.25m revenue in the preceding financial year (art 64(1)). Approval within 6 months (art 53(1)); court register filing under art 69(1). Poz. 640 and 644 were not read.

**Consequences:**

| Item | Rule | Source |
|---|---|---|
| Late-payment interest | 200% of the NBP lombard rate plus 2%, minimum 8%; take the current rate from NBP. Also on advances, on the part above the tax due. Halved on correction within 6 months and payment within 7 days, with exclusions | OP arts 53, 56, 56a |
| Not filing to evade tax | Fiscal offence: up to 720 daily rates, or prison, or both; fine only at small value; petty offence below the threshold | KKS arts 54, 23, 53 |
| Late return where the taxable matter was disclosed | Petty offence | KKS art 56(4) |
| Persistent non-payment | Petty offence | KKS art 57, 48 |
| Voluntary disclosure | Notify and pay in full; ineffective after documented knowledge or action | KKS art 16 |

KKS was read in Dz.U. 2025 poz. 633; amenders poz. 347, 421, 846 and 901 did not touch the cited articles in the parts read (poz. 846 art 8 points 5 and 6 were not seen). Any fiscal offence exposure goes to the reviewer. Amounts round to full zloty, with under 50 groszy dropped (OP art 63 §1).

## [ANTI-AVOIDANCE]

- **GAAR:** OP art 119a. A benefit contrary to the purpose of the law, where that benefit is the main or one of the main aims and the arrangement is artificial. Any such position goes to R-CIT-7.
- **CFC:** art 24a, 19%. Tests include a listed state, a state without an information exchange basis, or over 50% control (including de facto control) with 33% passive income and tax at least 25% lower. Art 24a(3)(4) and the substance exit were not read. Any foreign subsidiary goes to the reviewer, without applying the tests here.
- **Hybrids:** arts 16n to 16u, located only. Escalate under R-CIT-12.
- **DAC6:** OP art 86a from 1 October 2026 covers cross-border arrangements (poz. 846). Reviewer.
- **BEAT or GILTI equivalent:** HOLD.

## [PILLAR TWO OVERLAY]

Dz.U. 2024 poz. 1685: EUR 750m in 2 of 4 years; 15%; income inclusion, national top-up and undertaxed profits rules, from 1 January 2025. HOLD on UTPR commencement and domestic top-up details. An in-scope company is refused here.

## [CROSS-REFERENCES]

| Topic | Position |
|---|---|
| Withholding tax | Outbound dividends 19% (art 22(1)); interest, royalties and listed services 20% (art 21(1)). Pay and refund above PLN 2m for related payments under art 21(1)(1) and 22(1), on the excess (art 26(2e)). Surcharges on ordinary companies: none in art 19. Treaty relief: escalate |
| Pillar Two | Above; refused |
| DAC6 | Above |
| IP box, R&D | Credits slot |
| Free zone | HOLD |
| Transfer pricing | Transfer pricing workflow base |
| Deferred tax | Reviewer sets the provision |
| Payroll, VAT, formation, annual accounts | Separate guides |

## Worked example (fictional)

Scofield Inżynieria sp. z o.o.; calendar 2026; revenue PLN 20,000,000, above the 9% limit; all income from the non-capital source; no capital gains; debt financing costs PLN 100,000, below the PLN 3m limit.

Accounting profit before CIT is PLN 2,000,000, after these items: fine imposed in administrative proceedings PLN 10,000; late-payment interest on tax PLN 5,000; hospitality for clients PLN 20,000; accounting reserve not listed in the Act as a cost PLN 30,000. Loss from the same source in 2024: PLN 400,000, none used yet, with the 50% option chosen. Advances paid: PLN 300,000.

| Step | PLN |
|---|---|
| Accounting profit before CIT | 2,000,000 |
| Fine (art 16(1)(18)) | +10,000 |
| Late-payment interest (art 16(1)(21)) | +5,000 |
| Entertainment (art 16(1)(28)) | +20,000 |
| Reserve (art 16(1)(27)) | +30,000 |
| Income | 2,065,000 |
| Loss, 50% of 400,000 (art 7(5)(1)) | -200,000 |
| Tax base | 1,865,000 |
| CIT at 19% | 354,350 |
| Balance after PLN 300,000 advances | 54,350 |

Minimum tax test: 2,065,000 / 20,000,000 = 10.325%, above 2%, so it is not triggered. The example makes no art 24ca(2) adjustment; a reviewer checks that.

The 9% rate fails at the current-year revenue test, so small taxpayer status is not reached.

**One-off alternative:** deducting the whole PLN 400,000 under art 7(5)(2) gives a base of PLN 1,665,000 and CIT of PLN 316,350.

## Delivery holds

This reference is a Tier 2 draft pending review by a Polish tax adviser. It establishes no filing, form version or administrative practice. Tax authority interpretations and case law were not read and can narrow or extend the statute. Output is a working paper under the base's section 10.

## Sources

Sources were checked on 31 October 2026. Official text through the [Sejm ELI API](https://api.sejm.gov.pl/eli/acts/DU/2026/554): CIT Act, Dz.U. 2026 poz. 554, with Dz.U. 2026 poz. 779, 846, 912, 1123, 1287, 1371; Ordynacja podatkowa, Dz.U. 2026 poz. 622; KKS, Dz.U. 2025 poz. 633; Dz.U. 2024 poz. 1685; Dz.U. 2023 poz. 1059; Accounting Act, Dz.U. 2026 poz. 522. Form name: [podatki.gov.pl](https://www.podatki.gov.pl).

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
