---
name: it-corporate-income-tax
description: >
  Italy corporate income tax reference for an ordinary resident SRL or SPA with
  a calendar 2026 tax period. Covers IRES and IRAP: rates, the expired premium
  rate, participation exemption, dividends, interest limit, losses, advances,
  return dates, penalties and a fictional computation, with the new consolidated
  text from 2027 flagged. Trigger on SRL or SPA corporate tax, IRES, IRAP,
  Redditi SC, ROL or perdite fiscali. Refuses groups, consolidation, financial
  sector, non-residents, liquidation and Pillar Two scope. This source-cited
  draft awaits local professional review and is not filing readiness.
jurisdiction: IT
category: international
tax_year: 2026
tax_year_notes: "Calendar 2026 tax period, returned in 2027. Statute captures retrieved 31 October 2026."
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

# Italy Corporate Income Tax: Ordinary Resident SRL and SPA, 2026 Period

Load this on top of `corporate-income-tax-workflow-base`. Its runbook, 26-field intake, output specification and 18 self-checks apply; this file fills its section 9 slots. A slot marked HOLD was not established from the sources read for this draft, and no figure may be supplied for it from memory.

**Version warning.** D.Lgs. 117/2026 applies its new income tax consolidated text from 1 January 2027 and repeals TUIR arts 1 to 191 from then (annex arts 377, 376(1)(e)). This guide applies the TUIR to income of a period closing on 31 December 2026. That is an inference: no express saving rule was found, and annex arts 365 to 374 were not read. A reviewer confirms it before any filing. Do not use these article numbers for 2027 periods.

## Scope and refusals

**In scope:** a solvent SRL or SPA resident in Italy (TUIR art 73), with a calendar tax period, standing alone, in no regulated financial sector.

**Refuse and escalate, without computing:**

| Trigger | Reason |
|---|---|
| Bank, insurer, financial intermediary, holding of them, fund, REIT | R-CIT-1, R-CIT-2; IRES surcharge of 3.5 points (TUIR art 77 note) and IRAP art 16(1-bis)(b), (c) |
| Concession company other than motorway and tunnel construction and management | IRAP art 16(1-bis)(a) prints 3.80%; the rate restored by its note was not read |
| Dividend from a foreign payer, or IFRS reporter with shares held for trading | TUIR art 89(2-bis), (3); the art 44(2)(a) condition was not read |
| Gain on shares in a holding company | TUIR art 87(5) look-through |
| Gain on shares in a foreign company | Art 47-bis was not read |
| Company with production in more than one region | IRAP art 4(2) allocation was not read |
| Tax consolidation or transparency (TUIR art 117 onward) | Group rules are not covered |
| Liquidation or insolvency | R-CIT-10 |
| Non-resident company or Italian branch | Not covered |
| Disputed or dual residence, hybrid arrangement | R-CIT-9, R-CIT-12 |
| Revenue at or above EUR 750m in 2 of the previous 4 years (D.Lgs. 209/2023) | Pillar Two |
| Reorganisation, or a majority share transfer with a claim to keep losses | R-CIT-8; TUIR art 84(3) to (3-quater) need reviewer judgement |
| Non-operating or loss-making shell company tests | Not read |
| Listed energy sector ATECO codes | IRAP +2 points for 2026 and 2027 (D.L. 21/2026 art 3); confirm the list, then escalate |
| Audit or a deficiency notice | R-CIT-6 |

## [REGIME IDENTIFICATION]

- **Jurisdiction:** IT.
- **Statutes:** TUIR (DPR 917/1986) to 31 December 2026; D.Lgs. 446/1997 (IRAP); DPR 322/1998 (returns); DPR 435/2001 (payment); D.Lgs. 241/1997 (F24); D.Lgs. 471/1997 and 472/1997 (penalties).
- **Authority:** Agenzia delle Entrate. Format: electronic filing. Portal name: HOLD.
- **Forms:** Redditi SC and IRAP. The 2027 form names are an inference from the naming pattern: HOLD until the 2027 models are issued.

**Dates for a calendar-2026 period:**

| Item | Rule | Date | Source |
|---|---|---|---|
| First advance | 40% of the advance due, by the balance date in the period; one payment in November if the first instalment would not exceed EUR 103 | 30 June 2026 | DPR 435/2001 art 17(3) |
| Second advance | The rest, by end of month 11 | 30 November 2026 | Same |
| Balance | End of month 6 after the period | 30 June 2027 | Art 17(1) |
| Deferred balance | 30 days later, adding 0.40% | 30 July 2027 | Art 17(2) |
| Return | Electronic, from 15 April to the last day of month 10 | 31 October 2027 is a Sunday | DPR 322/1998 art 2(2) |

- **Weekend shift:** D.L. 70/2011 art 7(2)(l) moves a Saturday or holiday date to the next working day, but the captured version ends on 31 December 2026. HOLD on the exact 2027 return date until the replacement text is read. If the same rule continues and 1 November is a holiday, the date is 2 November 2027.
- **Later accounts approval:** a company that by law approves accounts after the 4-month term pays by the last day of the month after approval, or, if not approved within the statutory term, by the last day of the month after that term (art 17(1)). The first advance moves with it (art 17(3)).
- **Companies under synthetic reliability indexes (ISA):** two equal advances, if revenue does not exceed the limit set for the index (D.L. 124/2019 art 58(1), in a version ending 31 December 2026; D.L. 34/2019 art 12-quinquies(3), (4)).
- **Advance level:** 100% for IRES, none at or below EUR 20.66. These rest on Agenzia instructions for Redditi 2026, not on law read here. HOLD on the IRAP advance percentage.
- **Late return:** valid if filed within 90 days of the due date; later it counts as not filed (DPR 322/1998 art 2(7)).

## [RATES]

- **IRES:** 24% (TUIR art 77(1)).
- **Premium rate (IRES premiale):** 20%, for one period only, which is 2025 for a calendar company (L. 207/2024 art 1(436)). It does not apply to 2026. The 2026 advance is computed as if it had not applied (art 1(443)). A company that claimed it in 2025 checks the recapture rule in art 1(438), which reaches a distribution of the set-aside profit by the second following year; escalate any recapture.
- **Other 2026 reduced rate:** none found. L. 199/2025 was read or text-searched across all 10 partitions of art 1, with no IRES rate change. A broader search of later law was not done.
- **IRAP:** 3.90% standard, by derivation: D.Lgs. 446/1997 art 16(1) still prints 3.50%, whilst L. 190/2014 art 1(22) repealed the cuts. A reviewer confirms this against the IRAP 2027 instructions, and any IRAP figure stays provisional until then. Regions may vary it by up to 0.92 points (art 16(3)), so take the regional rate from the region's law and never assume one.
- **Small company rate, IP box, zones:** HOLD.
- **Branch profits tax:** out of scope.

## [ADJUSTMENTS]

Start from the accounting result, with the variations in the TUIR (art 83). Income and costs follow accrual, and must be certain and determinable (art 109(1)). Costs must be charged to profit and loss, except costs deferred under earlier rules and costs deductible by law (art 109(4)(a), (b)) and relate to activities or assets yielding income that is taxable or excluded. Costs shared with exempt income are deductible in proportion, leaving art 87 gains out of the ratio. This link test does not apply to interest or to fiscal, contribution and social-utility charges (art 109(5)).

**Limits read. This list is not exhaustive; there is no single statutory list (inference):**

| Item | Rule | TUIR |
|---|---|---|
| Income taxes | Not deductible; other taxes deductible when paid | 99(1) |
| IRAP | Not deductible in principle (D.Lgs. 446/1997 art 1(2)). Labour-share deduction under D.L. 201/2011 art 2(1). A 10% deduction rests on Agenzia instructions citing D.L. 185/2008 art 6, not read | 99 |
| Entertainment | 1.5% of revenue to EUR 10m, 0.6% to EUR 50m and 0.4% above; gifts up to EUR 50 in full; traceable payment | 108(2) |
| Hotel and meal costs | 75%, other than art 95(3) travel, before the entertainment limit where both apply: reviewer settles the interaction. Food, lodging and non-scheduled public transport costs in Italy, and itemised reimbursements of them, are deductible only if paid by bank or post or another art 23 D.Lgs. 241/1997 system | 109(5), (5-bis); 95(3-bis) |
| Social costs and donations | 5 per mille of staff cost; 2% of business income for listed donations | 100(1), (2)(a) |
| Directors' pay | Deductible in the period paid | 95(5) |
| Vehicles | 20% in general, ignoring car purchase cost above lire 35m, the matching share of lease fees and rental cost above lire 7m (the caps print in lire: reviewer converts them); 70% for vehicles given to employees in mixed use for most of the period; 100% if exclusively instrumental; fuel only if paid by electronic card | 164(1)(a), (b), (b-bis), (1-bis) |
| Bad debt provision | 0.5% a year, to 5% of receivables | 106(1) |
| Employee severance (TFR) | Accrued amounts | 105(1) |

**Exempt income:**

- **Dividends:** 95% excluded in the period received, from a resident company within art 73(1)(a) to (c) (art 89(2)). The exceptions in the refusal table are not computed.
- **Share gains:** 95% exempt on 4 tests (art 87(1)(a) to (d)): held without a break from the first day of the 12th month before sale, treating the latest acquired shares as sold first; classified as a financial fixed asset in the first balance sheet of the holding period; not from a privileged tax regime, or proof under art 47-bis; and a commercial business. Shares in a company whose assets are mainly real estate fail the last test, with no contrary proof allowed, unless the real estate is what it produces or trades or is used directly in its business, which includes property let on finance lease and land it farms. The privileged regime test must hold from the first period of holding, or for the 5 periods before sale if held for more than 5 periods and sold outside the group. The commercial business test must hold from the start of the third period before sale (art 87(2)), and does not apply to listed shares or to gains through public offers of sale (art 87(4)).
- **Sequence for 2026:** L. 199/2025 art 1(51) to (55) added conditions. D.L. 38/2026 art 11(4), (5) repealed them from 1 January 2026. Apply the text without them, and confirm the version on the date of filing.

**Depreciation:** ministerial coefficients, halved in the first period; assets up to EUR 516.46 may be written off; maintenance up to 5%, with the excess deductible equally over the next 5 periods (art 102(2), (5), (6)). HOLD on the coefficient table (DM 31 December 1988, not read).

**Interest limit (TUIR art 96):** interest expense is deductible up to taxable interest income and then 30% of ROL. ROL is value less costs of production, excluding items 10(a) and 10(b) and finance lease fees on instrumental assets, at the amounts that result under the business income rules (art 96(3), (4)). Excess interest carries forward; excess ROL carries forward 5 periods. Any carryforward goes to the reviewer.

**IRAP base (D.Lgs. 446/1997 art 5):**

- Value of production less costs of production (Civil Code art 2425 A less B), excluding items 9, 10(c), 10(d), 12 and 13 and extraordinary business-transfer items (art 5(1)).
- Also not deductible: staff and assimilated pay booked outside item 9, the amounts in art 11(1)(b) nos 2 to 5, the interest part of finance leases, bad debt losses and municipal property tax (art 5(3)). Treating directors' pay as within these is an inference from art 5(3) and art 11(1)(b)(4).
- Permanent staff cost is deductible (art 11(4-octies)), and 70% for seasonal workers on its conditions.
- Small company deductions, applied or sent to the reviewer: EUR 8,000 if the base does not exceed EUR 180,759.91, with bands to EUR 180,999.91 (art 11(4-bis)); EUR 1,850 for each employee not on a permanent contract, up to 5, if positive components do not exceed EUR 400,000 (art 11(4-bis.1)).
- Other art 11(1)(a) items: reviewer.

## [LOSSES]

| Point | Rule | TUIR |
|---|---|---|
| Carryforward period | No expiry stated | 84(1) |
| Annual cap | 80% of income | 84(1) |
| Loss amount | Reduced by exempt income other than art 87 gains: reviewer | 84(1) |
| First 3 periods | 100%, only for a new productive activity | 84(2) |
| Carryback | None in art 84 (inference) | 84(1) |
| Ownership change | Majority transfer plus change of main activity blocks use; 40% vitality test; net equity cap; extends to excess interest and ACE; indirect transfers read in (D.Lgs. 148/2026 art 7(1), by note 250) | 84(3) to (3-quater) |
| Group relief | Refused | 117 onward |
| IRAP | No loss carryforward was read: HOLD | |

## [CREDITS]

- **Advances and withholdings:** offset against IRES (TUIR art 79(1)).
- **Foreign tax:** credit limited by country, with the excess rule (TUIR art 165(1), (3), (6)). HOLD any computation.
- **ACE:** repealed after the period in progress at 31 December 2023; existing surplus runs off (D.Lgs. 216/2023 art 5(1)).
- **R&D credit (L. 160/2019) and investment incentives:** HOLD; no 2026 statement read.

## [FILING MECHANICS]

- Redditi SC and IRAP returns are electronic, and IRAP-only filers use the same window (DPR 322/1998 art 2(2), (3)). IRAP procedure follows the income tax rules (D.Lgs. 446/1997 arts 25, 30).
- Payment through F24, with set-off (D.Lgs. 241/1997 art 17(1), in a version ending 31 December 2026: a reviewer confirms it for 2027 payments).
- Supporting schedules and audit thresholds: HOLD.

**Penalties:**

| Item | Rule | Source |
|---|---|---|
| No return | 120%, minimum EUR 250; EUR 250 to EUR 1,000 if no tax is due | D.Lgs. 471/1997 art 1(1) |
| Filed over 90 days late, within the art 43 assessment limit and before formal knowledge of an audit | Art 13(1) penalty tripled on the tax due | Art 1(1-bis) |
| Inaccurate return | 70%, minimum EUR 150 | Art 1(2) |
| Late payment | 25%; half within 90 days; 1/15 a day within 15 days | Art 13(1) |
| Voluntary correction | 1/10 to 1/4 of the minimum by timing, with legal interest; 1/10 for a return filed within 90 days | D.Lgs. 472/1997 art 13(1), (2) |

These rules apply to violations from 1 September 2024 (D.Lgs. 87/2024 art 5(1)). The D.Lgs. 173/2024 annex replaces the penalty text from 1 January 2027 (annex art 102). HOLD on which text governs a violation occurring in 2027: a reviewer checks the annex.

## [ANTI-AVOIDANCE]

- **GAAR:** L. 212/2000 art 10-bis. Abuse means transactions without economic substance that essentially yield undue tax advantages; valid non-tax reasons take a transaction outside it (art 10-bis(1), (3)). Any such position goes to R-CIT-7.
- **CFC:** TUIR art 167. Control or over 50% of profits; effective tax under 15%; over a third passive income; substance exit (art 167(2), (4), (5)). Any foreign subsidiary goes to the reviewer.
- **Hybrids:** D.Lgs. 142/2018 (located, art 6 definitions only). Escalate under R-CIT-12.
- **Transfer pricing:** arm's length (TUIR art 110(7)). Load the transfer pricing workflow base.
- **BEAT or GILTI equivalent:** HOLD.

## [PILLAR TWO OVERLAY]

D.Lgs. 209/2023: EUR 750m in 2 of the previous 4 years (art 10(1)). Income inclusion rule for a parent (art 13), undertaxed profits rule (art 19). Domestic top-up (art 18, not read): HOLD. Commencement dates of each rule: HOLD. An in-scope company is refused here. Being below the threshold is the only conclusion this file supports.

## [CROSS-REFERENCES]

| Topic | Position |
|---|---|
| Withholding tax | Outbound dividends 1.20% to companies subject to corporate income tax in a listed EU or EEA state, on holdings not tied to an Italian permanent establishment (DPR 600/1973 art 27(3-ter)). The non-resident rate prints as 27% in art 27(3), with a note to D.L. 66/2014, not read: HOLD and escalate |
| Pillar Two | Above; refused |
| DAC6 | HOLD |
| IP box, R&D credit, free zone | HOLD |
| Transfer pricing | Transfer pricing workflow base |
| Deferred tax | Reviewer sets the provision |
| Payroll, VAT, formation, annual accounts | Separate guides; `it-irap` covers IRAP for other taxpayers |

## Worked example (fictional)

Largo Forniture S.r.l.; calendar 2026; one region, assumed at 3.90%; all staff on permanent contracts; no change of ownership.

Value of production (A) is EUR 3,000,000 and costs of production (B) EUR 2,710,000. Below B there are only a dividend of EUR 50,000, received in 2026 from an Italian company with no withholding, and net interest expense of EUR 40,000. Accounting profit before IRES and IRAP is therefore EUR 300,000.

B includes staff EUR 900,000 (B9); depreciation EUR 110,000 at tax rates (B10(a), (b)); a bad debt provision EUR 20,000 within the art 106 limit (B10(d)); vehicle costs EUR 10,000, within the art 164 caps with fuel paid by card; and directors' pay EUR 12,000, accrued in 2026, unpaid at year end and booked in B7, treated as pay assimilated to employment (a professional services contract goes to the reviewer). Every other cost is fully deductible, and there are no leases.

IRES loss brought forward EUR 100,000, not from the first 3 periods. Advances paid: IRES EUR 30,000; IRAP EUR 10,000. The IRAP deductions from IRES are left out as a simplification, and a reviewer adds them.

| IRES step | EUR |
|---|---|
| Accounting profit before income taxes | 300,000 |
| Dividend, 95% excluded (art 89(2)) | -47,500 |
| Vehicle costs, 80% not deductible (art 164(1)) | +8,000 |
| Directors' pay, unpaid (art 95(5)) | +12,000 |
| Income before losses | 272,500 |
| Loss deducted (cap 80% x 272,500 = 218,000, not reached) | -100,000 |
| Taxable income | 172,500 |
| IRES at 24% | 41,400 |
| Balance after EUR 30,000 advances | 11,400 |

Interest needs no adjustment. ROL is 290,000 + 110,000 + tax add-backs 20,000 = EUR 420,000 (art 96(4)), and EUR 40,000 is below 30% x 420,000 = EUR 126,000.

| IRAP step | EUR |
|---|---|
| Value of production (A) | 3,000,000 |
| Costs of production (B) | 2,710,000 |
| Less excluded: item B9 staff | 900,000 |
| Less excluded: item B10(d) | 20,000 |
| Less not deductible: directors' pay in B7 (art 5(3)) | 12,000 |
| Deductible costs | 1,778,000 |
| Net value of production | 1,222,000 |
| Permanent staff deduction (art 11(4-octies)) | -900,000 |
| IRAP base | 322,000 |
| IRAP at 3.90% | 12,558 |
| Balance after EUR 10,000 advances | 2,558 |

The art 11(4-bis) deduction is not reached at this base. Preliminary total before the IRAP deductions from IRES: 41,400 + 12,558 = EUR 53,958. This is not a final liability. No rounding rule was read for this example; its figures fall on whole euro.

## Delivery holds

This reference is a Tier 2 draft pending review by an Italian tax adviser. It establishes no filing, form version, regional rate or administrative practice. Agenzia circulars and case law were not read and can narrow or extend the statute. Output is a working paper under the base's section 10.

## Sources

Sources were checked on 31 October 2026. Official text at [Normattiva](https://www.normattiva.it): TUIR arts 73, 77, 79, 83, 84, 87, 89, 95, 96, 99, 100, 102, 105, 106, 108, 109, 110, 164, 165, 167; D.Lgs. 446/1997 arts 1, 5, 11, 16, 25, 30; DPR 322/1998 art 2; DPR 435/2001 art 17; D.Lgs. 241/1997 art 17; D.Lgs. 471/1997 arts 1, 13; D.Lgs. 472/1997 art 13; D.Lgs. 87/2024 art 5; L. 207/2024 art 1; L. 199/2025 art 1; D.L. 38/2026 art 11; D.L. 21/2026 art 3; D.L. 124/2019 art 58; D.L. 70/2011 art 7; D.L. 201/2011 art 2; L. 190/2014 art 1; D.Lgs. 216/2023 art 5; L. 212/2000 art 10-bis; D.Lgs. 142/2018 art 6; D.Lgs. 148/2026 art 7; D.Lgs. 209/2023 arts 10, 13, 19; DPR 600/1973 art 27; D.Lgs. 117/2026 annex arts 376, 377; D.Lgs. 173/2024 annex art 102. Instructions: [Agenzia delle Entrate](https://www.agenziaentrate.gov.it), Redditi SC 2026.

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
