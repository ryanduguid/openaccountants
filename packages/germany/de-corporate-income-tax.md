---
name: de-corporate-income-tax
description: >
  Germany corporate income tax reference for an ordinary resident GmbH or UG in
  assessment year 2026. Covers Körperschaftsteuer, solidarity surcharge and
  Gewerbesteuer: enacted rate steps to 2032, the multiplier floor, participation
  exemption, non-deductible items, interest barrier, loss limits, prepayments,
  filing dates, penalties and a fictional computation. Trigger on GmbH or UG
  corporate tax, KSt, GewSt, Hebesatz, Verlustvortrag or Zinsschranke. Refuses
  groups, Organschaft, financial sector, non-residents, liquidation and Pillar
  Two scope. This source-cited draft awaits local professional review and is not
  filing readiness.
jurisdiction: DE
category: international
tax_year: 2026
tax_year_notes: "Assessment year (VZ) and collection period (EZ) 2026; later rate steps recorded as enacted. Statute captures retrieved 30 and 31 October 2026."
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

# Germany Corporate Income Tax: Ordinary Resident GmbH and UG, VZ 2026

Load this on top of `corporate-income-tax-workflow-base`. Its runbook, 26-field intake, output specification and 18 self-checks apply; this file fills its section 9 slots. A slot marked HOLD was not established from the sources read for this draft, and no figure may be supplied for it from memory.

## Scope and refusals

**In scope:** a GmbH or UG with management or seat in Germany (KStG s 1), taxable on worldwide income, carrying on no regulated financial or insurance business, standing alone, solvent, with one municipality of establishment.

**Refuse and escalate, without computing:**

| Trigger | Reason |
|---|---|
| Bank, insurer, pension fund, asset manager, fund, REIT | R-CIT-1, R-CIT-2; KStG s 8b(7) and (8) sector rules |
| Organschaft or profit-transfer agreement, or any group calculation (KStG s 14) | Income is attributed to the parent; group rules are not covered |
| Liquidation or insolvency | R-CIT-10 |
| Non-resident company, German branch or permanent establishment of one | Limited liability and treaty allocation are not covered |
| Disputed or dual residence, hybrid arrangement | R-CIT-9, R-CIT-12 |
| Revenue at or above the MinStG s 1 threshold (EUR 750m in 2 of the previous 4 years) | Pillar Two |
| Establishments in more than one municipality | Apportionment (Zerlegung) was not read |
| Reorganisation, or a share transfer over 50% with a claim to keep losses | R-CIT-8; KStG ss 8c, 8d need reviewer judgement |
| Pure property company seeking the extended reduction (GewStG s 9 no 1 sentence 2) | Conditions need reviewer judgement |
| Audit or a deficiency notice | R-CIT-6 |

## [REGIME IDENTIFICATION]

- **Jurisdiction:** DE.
- **Statutes:** Körperschaftsteuergesetz (KStG); Solidaritätszuschlaggesetz (SolZG); Gewerbesteuergesetz (GewStG); Einkommensteuergesetz (EStG), incorporated by KStG s 8(1); Abgabenordnung (AO).
- **Authority:** the Finanzamt assesses corporate income tax and the trade tax base amount. The municipality sets the multiplier (GewStG s 16). Portal: ELSTER.
- **Forms:** KSt 1 and GewSt 1 A through ELSTER. HOLD: the capture lists form years only to 2025, so confirm the VZ 2026 form set when it is provided.
- **Period:** tax is annual (KStG s 7). A year-end other than 31 December falls in the VZ in which it ends (KStG s 7(4)); a change of year-end to a non-calendar date needs Finanzamt consent.

**Filing dates for VZ 2026, calendar-year company:**

| Case | Statutory date | Date for VZ 2026 | Source |
|---|---|---|---|
| Self-prepared | 7 months after the period | 31 July 2027 is a Saturday, so Monday 2 August 2027 | AO ss 149(2), 108(3) |
| Prepared by an authorised adviser | Last day of February of the second following year | 29 February 2028 | AO s 149(3) |
| Early call by the Finanzamt, on an adviser-prepared return | 4 months after notice, and never shorter than the 7-month period | As notified, not before the self-prepared date | AO s 149(4) |

The extended dates in EGAO art 97 s 36(3) stop at period 2024. No extension for VZ 2026 was found in that unit.

**Payment:**

| Tax | Prepayment dates in 2026 | Amount |
|---|---|---|
| KSt and SolZ | 10 March, 10 June, 10 September, 10 December (EStG s 37; SolZG s 3(1) no 2; KStG s 31) | As fixed by the Finanzamt |
| GewSt | Statutory dates 15 February, 15 May, 15 August, 15 November (GewStG s 19) | One quarter of the last assessment, as adjusted; rounded down to a full euro and fixed only if at least 50 euro (s 19(5)). 15 February, 15 August and 15 November 2026 fall on a weekend: HOLD on whether payment moves, as AO s 108(3) speaks of a period |

## [RATES]

**KSt (KStG s 23(1), as amended by BGBl. 2025 I Nr. 161 Art 2):**

| VZ | Rate |
|---|---|
| 2026, 2027 | 15% |
| 2028 | 14% |
| 2029 | 13% |
| 2030 | 12% |
| 2031 | 11% |
| 2032 onward | 10% |

- **Small company or reduced rate:** none in s 23(1). The GmbH or UG pays the same rate at every profit level.
- **Rounding:** each KSt amount in the assessment is rounded to full euro in the taxpayer's favour (KStG s 31(1) sentence 2); capital gains tax credits are rounded up to full euro (EStG s 36(3)).
- **Solidarity surcharge:** 5.5% of assessed KSt, with fractions of a cent dropped (SolZG ss 3(1) no 1, 4). The exemption threshold in s 3(3) applies only to income tax payers. Derived rate: 15.825% for VZ 2026.
- **Trade tax:** trade income, rounded down to 100 euro, times 3.5% (GewStG s 11(1), (2)), times the municipal multiplier. A corporation has no allowance.
- **Multiplier:** take it from the municipality's current statute and never assume one. The floor is 200% for EZ 2026 and 280% from EZ 2027 (GewStG s 16(4) sentence 2, s 36(5b); BGBl. 2026 I Nr. 197 Art 8). Section 36(5b) cites 'Artikel 7' whilst the change sits in Art 8; the first-application year is clear, but a reviewer should note the citation.
- **Combined nominal rate, VZ 2026:** 15.825% + (3.5% x multiplier). At the 200% floor that is 22.825%; at a fictional 400% it is 29.825%.
- **Reduced rates by activity:** HOLD. No IP box or zone rate appears in s 23(1); no wider statement is made.
- **Branch profits tax:** out of scope (non-residents refused).

## [ADJUSTMENTS]

Start from the tax profit under the EStG (KStG s 8(1)); all income of a GmbH or UG is trade income (KStG s 8(2); GewStG s 2(2)).

**Not deductible for KSt and, through the profit base, for GewSt:**

- Hidden distributions; hidden contributions do not increase income (KStG s 8(3)).
- KSt, SolZ and other income taxes and their ancillary amounts; criminal fines; half of supervisory board pay; costs of purposes set by the articles (KStG s 10).
- Trade tax and its ancillary amounts (EStG s 4(5b)).
- Gifts to a non-employee, in full, where the year's total to that recipient exceeds EUR 50; 30% of business meals, with the required records; fines and related costs (EStG s 4(5) nos 1, 2, 8).
- Also in EStG s 4(5): guest facilities, hunting and yachts, unreasonable lifestyle costs, interest on evaded tax, illegal benefits and s 162(4) AO surcharges (nos 3, 4, 7, 8a, 10, 12). The rest of s 4(5) and any non-deduction outside these units: HOLD. This list is not exhaustive.

**Donations:** up to 20% of income or 4 per mille of turnover plus wages (KStG s 9(1) no 2). For GewSt they are added back (s 8 no 9), then reduced within the matching limit (s 9 no 5).

**Exempt income:**

- Dividends are exempt only so far as they did not reduce the payer's income (KStG s 8b(1) sentence 2). Share gains are exempt, unless earlier tax-effective write-downs have not been reversed, or tax-effective s 6b or similar deductions were taken (s 8b(2) sentences 4 and 5). 5% is deemed non-deductible (s 8b(3), (5)).
- Dividends are taxable if the direct holding was under 10% at the start of the calendar year; acquiring at least 10% during the year is treated as made at its start. Those taxable dividends carry no 5% adjustment (s 8b(4) sentences 1, 6, 7). Share gains have no such test.
- Reductions in profit connected with shares, including share losses, are not deductible at any holding (s 8b(3) sentence 3). Reductions on loans or security from a shareholder holding over 25%, or a related person, are also caught, unless the arm's length test in sentence 7 is met (s 8b(3) sentences 4 to 7).

**Trade tax additions and reductions:**

| Item | Rule |
|---|---|
| Financing add-back (s 8 no 1) | Sum of all interest, annuities and silent partner shares, plus one fifth of rents for movable fixed assets owned by another (one half of that fraction for certain electric vehicles and bikes under contracts made after 31 December 2019, to EZ 2030; s 36(4)), plus half of rents for immovable fixed assets owned by another, plus a quarter of time-limited rights (not licences that only permit sublicensing). Only rents that meet the fixed-asset test count; a reviewer tests this. One quarter of the sum above EUR 200,000 is added |
| Dividends (s 8 no 5; s 9 nos 2a, 7) | The dividend stays out only if the holding was at least 15% at the start of the EZ. Below 15%, the s 8b(1) exempt dividend is added back net of directly connected expenses, so the deemed 5% is not counted twice |
| Land tax (s 9 no 1) | Reduction for land tax expensed in the EZ on land in business assets, in the version applying from EZ 2025 (s 36(4b)) |
| Foreign permanent establishment (s 9 no 3) | That share of trade income is removed; the KSt position is a treaty question, so escalate |

**Depreciation:**

- Low-value movable assets up to EUR 800 net of input VAT may be expensed (EStG s 6(2)). A pooled alternative exists (s 6(2a)).
- Declining balance is available for movable assets acquired after 30 June 2025 and before 1 January 2028, at up to 3 times the straight-line rate and no more than 30% (EStG s 7(2)).
- HOLD: asset lives under official tables, and the electric vehicle rule in s 7(2a), were not worked through.

**Interest barrier (EStG s 4h; KStG s 8a):**

- Interest expense is deductible up to interest income and, above that, up to 30% of tax EBITDA (s 4h(1)). Excess interest carries forward; unused EBITDA carries forward 5 years, but no EBITDA carryforward arises in a year where s 4h(2) excludes the barrier.
- The barrier does not apply if: (a) net interest is under EUR 3m; (b) the company is related to no person under AStG s 1(2) and has no permanent establishment outside its state of seat or management; or (c) it belongs to a group and passes the equity comparison.
- KStG s 8a(3) narrows exception (c) by a 10% shareholder debt test; KStG s 8a(2) is repealed. The s 4h(2) exceptions do not apply so far as interest expense is increased by an interest carryforward (s 4h(1) sentence 7). A company at or above EUR 3m net interest, or with an interest carryforward, goes to the reviewer.

## [LOSSES]

| Point | KSt | GewSt |
|---|---|---|
| Carryforward period | No limit stated | No limit stated |
| Annual use | EUR 1m in full, then 70% of the excess for VZ 2026 (EStG s 10d(2)) | EUR 1m in full, then 60% of the excess (GewStG s 10a) |
| Carryback | EUR 1m to the 2 preceding years, unless waived on application (EStG s 10d(1)) | None in s 10a |
| Ownership change | Over 50% within 5 years forfeits losses, subject to the hidden reserves and group exceptions (KStG s 8c) and the application in s 8d | KStG s 8c applies (GewStG s 10a) |
| Group relief | Refused (Organschaft) | Refused |

- Keep the 2 loss balances apart; they differ because the bases differ.
- HOLD: this guide found a 60% KSt rate for use from VZ 2028 only in a prior capture of BGBl. 2024 I Nr. 108, not in the current text. It does not affect VZ 2026; re-read before any 2028 use.

## [CREDITS]

- **Withholding tax:** capital gains tax of 25% on dividends (EStG s 43a) and the surcharge on it (SolZG s 3(1) no 5) are credited, if the s 45a certificate is held (EStG s 36(2)). Check that the credit is not also the subject of a refund.
- **Foreign tax:** credit through KStG s 26 and EStG s 34c, with the per-country limit in EStDV s 68a not read. HOLD any computation.
- **R&D allowance, investment deduction, reinvestment relief:** HOLD. The Forschungszulagengesetz and EStG ss 6b, 7g were not read.
- **Trade tax credit against KSt:** HOLD on any credit; trade tax is not deductible (EStG s 4(5b)).

## [FILING MECHANICS]

- KSt return electronically (KStG s 31(1a)); trade tax return electronically (GewStG s 14a).
- E-Bilanz: balance sheet and profit and loss, with the account-level detail, are filed electronically (EStG s 5b; KStG s 31).
- Tax contribution account (steuerliches Einlagekonto) determined each year (KStG s 27).
- UG only: a quarter of annual surplus, net of any prior-year loss, goes to a statutory reserve (GmbHG s 5a(3)); the rule ends through the capital increase in s 5a(5). This is company law, not a tax adjustment.
- Audit thresholds: HOLD. The audit selection rules and HGB size classes were not read.

**Consequences:**

| Item | Rule | Source |
|---|---|---|
| Late filing | Discretionary from the missed date (s 152(1)). Mandatory after 14 months, including for an adviser-prepared return, or after a date set under s 149(4) (s 152(2)), unless the deadline was extended under s 109, the tax is nil or negative, or the tax does not exceed prepayments and withholding credits (s 152(3)). 0.25% per started month of tax net of prepayments and credits, minimum EUR 25 per month, rounded down, maximum EUR 25,000 | AO ss 109, 152(1), (2), (3), (5), (10) |
| Late filing, GewSt base return | EUR 25 per started month | AO s 152(6) |
| Late payment | 1% per started month, on the amount rounded down to 50 euro, with 3 days' grace, except payment under s 224(2) no 1 | AO s 240 |
| Interest on balances | 0.15% per full month from month 15 after the period, so from 1 April 2028 for VZ 2026; part months are ignored and the balance is rounded down to 50 euro | AO ss 233a, 238(1), (1a), (2) |

## [ANTI-AVOIDANCE]

- **GAAR:** AO s 42. Abuse is an inappropriate legal arrangement giving a tax advantage the law does not provide, compared with an appropriate one, unless the taxpayer proves non-tax reasons that are significant overall (s 42(2)). A specific anti-avoidance rule takes precedence where its conditions are met (s 42(1)). Any such position goes to R-CIT-7.
- **Hidden distributions:** KStG s 8(3).
- **CFC:** AStG ss 7 and 8; low tax means under 15% (s 8(5)). Any foreign subsidiary with passive income goes to the reviewer.
- **Transfer pricing records:** transaction matrix, facts and arm's length support (AO s 90(3)). Load the transfer pricing workflow base; AStG s 1 was not read.
- **Hybrids and royalty barrier:** HOLD. EStG ss 4k and 4j were not read; escalate under R-CIT-12.
- **BEAT or GILTI equivalent:** HOLD.

## [PILLAR TWO OVERLAY]

The Mindeststeuergesetz applies from the EUR 750m threshold in s 1. An in-scope company is refused here. HOLD on the detail of the income inclusion, undertaxed profit and domestic top-up rules, which were not read. Being below the threshold is the only conclusion this file supports.

## [CROSS-REFERENCES]

| Topic | Position |
|---|---|
| Withholding tax | Outbound dividends: 25% plus surcharge (EStG s 43a; SolZG). Treaty and directive relief: HOLD, escalate |
| Pillar Two | Above; refused |
| DAC6 | HOLD; AO s 138d was not read |
| IP box, R&D credit, free zone | HOLD as above |
| Transfer pricing | Transfer pricing workflow base |
| Deferred tax | The s 23(1) steps change the rate on temporary differences by year of reversal; HGB treatment was not read, so a reviewer sets the provision |
| Real estate transfer tax | BGBl. 2026 I Nr. 197 Art 9 amends share-deal rules; out of scope, and flag any share transfer in a land-holding company |
| Payroll, VAT, formation, annual accounts | Separate guides |

## Worked example (fictional)

Madrigal Elektromotoren GmbH, a fictional company; calendar year; VZ and EZ 2026; one municipality with a fictional 400% multiplier; rents all premises; no change of ownership; revenue far below the Pillar Two threshold.

Accounting profit before KSt, SolZ and GewSt is EUR 480,000, after these items: dividend received EUR 40,000 from a 20% holding in a German GmbH held throughout, which did not reduce the payer's income (EUR 10,000 capital gains tax and EUR 550 surcharge withheld, certificates held); fine EUR 3,000; business meals EUR 10,000, properly recorded; supervisory board pay EUR 8,000; eligible donation EUR 5,000; interest EUR 120,000 (all net expense); rents for movable fixed assets EUR 50,000 (no electric vehicle relief); rents for immovable fixed assets EUR 200,000; time-limited licences EUR 40,000, none only for sublicensing. Losses brought forward: KSt EUR 300,000; GewSt EUR 250,000. Prepaid: KSt EUR 8,000, SolZ EUR 440, GewSt EUR 20,000.

| KSt step | EUR |
|---|---|
| Accounting profit before income taxes | 480,000 |
| Exempt dividend (KStG s 8b(1)) | -40,000 |
| 5% deemed non-deductible (s 8b(5)) | +2,000 |
| Fine | +3,000 |
| 30% of meals | +3,000 |
| Half of supervisory board pay | +4,000 |
| Income after donation (limit 20% x 457,000 = 91,400, not reached) | 452,000 |
| Loss deducted (under EUR 1m, so in full) | -300,000 |
| Taxable income | 152,000 |
| KSt at 15% | 22,800.00 |
| SolZ at 5.5% | 1,254.00 |
| KSt due after EUR 10,000 credit and EUR 8,000 prepaid | 4,800.00 |
| SolZ due after EUR 550 credit and EUR 440 prepaid | 264.00 |

| GewSt step | EUR |
|---|---|
| Profit base (as KSt, before loss) | 452,000 |
| Donation added back (s 8 no 9) | +5,000 |
| Financing add-back (below) | +10,000 |
| Donation reduction (s 9 no 5, within limit) | -5,000 |
| Trade income before loss | 462,000 |
| Loss (under EUR 1m, so in full) | -250,000 |
| Trade income, rounded down to 100 | 212,000 |
| Base amount at 3.5% | 7,420.00 |
| GewSt at 400% | 29,680.00 |
| Due after EUR 20,000 prepaid | 9,680.00 |

Financing add-back: 120,000 + (50,000 / 5) + (200,000 / 2) + (40,000 / 4) = 240,000; less 200,000 = 40,000; one quarter = 10,000. The dividend needs no s 8 no 5 add-back because the holding is at least 15%, and no s 9 no 2a reduction because the exempt part is already out of the profit base; the 5% stays in (s 9 no 2a sentence 4).

Total VZ 2026 charge: 22,800 + 1,254 + 29,680 = EUR 53,734.

**Loss limit illustration (separate fictional company):** income before losses EUR 3,000,000, with large losses available for both taxes. KSt use is 1,000,000 + 70% x 2,000,000 = EUR 2,400,000. GewSt use is 1,000,000 + 60% x 2,000,000 = EUR 2,200,000.

## Delivery holds

This reference is a Tier 2 draft pending review by a German tax adviser. It establishes no filing, form version, municipal multiplier or administrative practice. BMF circulars and case law were not read and can narrow or extend the statute. Output is a working paper under the base's section 10.

## Sources

Sources were checked on 30 and 31 October 2026. Official text at [gesetze-im-internet.de](https://www.gesetze-im-internet.de), unless noted: [KStG](https://www.gesetze-im-internet.de/kstg_1977/) ss 1, 7, 8, 8a, 8b, 8c, 8d, 9, 10, 14, 23, 26, 27, 31, 34; [SolZG](https://www.gesetze-im-internet.de/solzg_1995/) ss 3, 4; [GewStG](https://www.gesetze-im-internet.de/gewstg/) ss 2, 5, 7, 8, 9, 10a, 11, 14, 14a, 16, 19, 36; [EStG](https://www.gesetze-im-internet.de/estg/) ss 4, 4h, 5b, 6, 7, 10d, 36, 37, 43a, 52; [AO](https://www.gesetze-im-internet.de/ao_1977/) ss 42, 90, 108, 109, 149, 152, 233a, 238, 240; [EGAO art 97 s 36](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html); [AStG](https://www.gesetze-im-internet.de/astg/) ss 7, 8; [MinStG](https://www.gesetze-im-internet.de/minstg/) s 1; [GmbHG](https://www.gesetze-im-internet.de/gmbhg/) s 5a. Bundesgesetzblatt originals: [BGBl. 2025 I Nr. 161](https://www.recht.bund.de/bgbl/1/2025/161/) and [BGBl. 2026 I Nr. 197](https://www.recht.bund.de/bgbl/1/2026/197/). Form list: [ELSTER](https://www.elster.de/eportal/formulare-leistungen/alleformulare/gewst).

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
