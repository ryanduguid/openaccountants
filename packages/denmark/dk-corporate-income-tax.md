---
name: dk-corporate-income-tax
description: >
  Denmark corporate income tax source reference for ordinary resident ApS and
  A/S companies for income year 2026. Covers the 22% rate, accounting-to-tax
  reconciliation, indexed loss restriction, advance assessments and payment
  reconciliation, DIAS return preparation and specialist scope screens.
  Trigger on Danish company tax, selskabsskat, acontoskat, DIAS or Danish
  corporate losses. Includes fictional computations and explicit source holds.
  This Tier 2 draft awaits complete applicable-source qualification and
  professional review. It does not establish filing readiness.
jurisdiction: DK
category: international
tax_year: 2026
tax_year_notes: "Selected source reading on 2 November 2026. Ordinary registered resident ApS/A/S and calendar income year assumed for examples. Alternate income years, amended procedural interest, sectoral regimes and applicable specialist branches require separate qualification."
tier: 2
last_updated: 2026-11-02
version: 0.4
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark Corporate Income Tax Reference: Ordinary Resident ApS and A/S, 2026 v0.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This draft helps a Danish professional reviewer assess selected corporate tax sources and fictional computations for an ordinary registered resident anpartsselskab (ApS) or aktieselskab (A/S). Load both declared bases before actual work. Their intake, refusal messages, source gates, computation sequence, outputs and checks apply in full.

**General source reference, not an engagement calculation.** Complete applicable-source qualification, integration checks and professional review remain required. A populated country section identifies both supported rules and unresolved branches. It does not establish comprehensive Danish coverage. No actual classification, calculation or output preparation may use an unresolved applicable rule.

Registered A/S and ApS fall within Selskabsskatteloven (SEL) § 1(1), no. 1. Do not apply § 1(6), which addresses other enumerated entities, as the governing residence test for item 1. A foreign entity, branch, residence conflict or treaty claim requires its own classification and sources. SEL § 8 excludes foreign permanent-establishment and foreign immovable-property income and related expenses subject to its exceptions, including §§ 31 A and 31 E. Do not describe all foreign income as automatically included or excluded. [S1, §§ 1 and 8](https://www.retsinformation.dk/eli/lta/2025/279)

The examples assume 1 January to 31 December 2026 and DKK. Establish the actual registered income year under SEL § 10. A changed, short, long or substitute-calendar income year requires its own commencement, assessment and deadline analysis. Incorporation in Denmark alone does not clear every residence or treaty issue. [S1, § 10](https://www.retsinformation.dk/eli/lta/2025/279)

### Source currency and limits

S1 is LBK nr 279 af 13/03/2025, not a complete stand-alone statement of law on 2 November 2026. Its official page lists later amendments S2 to S6. Their selected corporate provisions and commencement sections were read. This establishes the selected amendment chain, not a whole-tax-system review or the completeness of every linked instrument.

| Later Act | Selected corporate unit and commencement | Effect relevant to this reference |
| --- | --- | --- |
| [S2, LOV nr 562 of 27 May 2025](https://www.retsinformation.dk/eli/lta/2025/562) | § 11 and § 17 | Changes entry-to-tax asset bases and forestry valuation. General commencement 1 July 2025; the specified forestry amendment applies to income years starting 1 January 2026. Asset-entry and forestry calculations remain outside the qualified method. |
| [S3, LOV nr 750 of 20 June 2025](https://www.retsinformation.dk/eli/lta/2025/750) | § 2 and § 7 | Changes selected nonresident, reverse-hybrid, related-party and international joint-tax rules. General commencement 1 July 2025, with distinct application dates for specified items, including 1 January 2025 and 1 July 2025. Applicable special branches require the full conditions. |
| [S4, LOV nr 1755 of 29 December 2025](https://www.retsinformation.dk/eli/lta/2025/1755) | § 5 and actual commencement § 8 | Commences 1 January 2026. Adds or changes specified employee-ownership and energy/co-operative treatments and scope lists. Its § 5, no. 7 changes the § 17 entity cross-reference without changing the ordinary 22% rate. § 9 is territorial, not the commencement provision. |
| [S5, LOV nr 1783 of 29 December 2025](https://www.retsinformation.dk/eli/lta/2025/1783) | §§ 2–3, 5–6 | The SEL § 30 changes apply from 1 January 2026. BEK 1793/2025 commences the selected OPKL interest-base changes on that date. Actual balance, calendar-year rate, payment and procedural qualification remain required. |
| [S6, LOV nr 763 of 8 September 2026](https://www.retsinformation.dk/eli/lta/2026/763) | §§ 1, 4 and 8 | Applies from 14 September 2026. Repeals a sentence of SEL § 24, changes the § 30(3) cross-reference to SEL § 29 B(4) and raises the OPKL reminder fee from DKK 65 to DKK 160. Do not use the unamended procedural text. |

All monetary thresholds must be tied to their stated income year. The ministry's rates page dated 1 September 2026 has separate 2026 and 2027 columns. The loss threshold below uses 2026. The page leaves 2026 advance-tax supplements, refund compensation and residual-tax percentage to later determination. [S7](https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven)

## Ask the client first

Infer facts from the evidence, then confirm the profile under the universal workflow. Complete all 26 fields of the corporate base; these additions do not replace them. Keep tax identifiers, credentials and private personal identifiers outside agent inputs. The reviewer retains the legal identity and portal access.

| Danish addition | Evidence needed and consequence if absent |
| --- | --- |
| Registered entity, tax status and income year | Redacted registration and DIAS basic information; identify A/S or ApS, actual period and any change. Residence conflict or dual residence fires the applicable base refusal. |
| Accounts, transaction population, losses and tax schedules | Signed or final accounts, framework, trial balance, detailed ledger and prior-year reconciliation. Record every item once, including excluded items and reasons. Obtain assessed loss vintage/category balances and utilisation; asset tax bases, disposals and depreciation; interest and related financing; dividends, capital gains, R&D and other credit claims. Missing applicable law is a source hold, not a zero. |
| Domestic and foreign activity | Revenue and expense locations, foreign property and establishments, shipping/aviation, special-sector activities and related entities. Resolve § 8 and all applicable exceptions before computation. |
| Group and ownership history | Direct and indirect shares and votes, changes since each loss year, group entry/exit dates, administration company, international joint-tax elections and restructuring/debt arrangements. A statement that the company is small does not resolve these tests. |
| Assessment, cash, filing and review | Ordinary and voluntary advance assessments, their dates, adjustments, actual payments and allocation evidence, withheld dividend tax, tax-account postings and prior balances. Retain both assessments and payment history. Obtain the actual DIAS return deadline, extensions or notices, required schedules, reviewer authority, filed-return history and acknowledgement. A draft in the portal is not a filed return. |
| Pillar Two | Ultimate-parent consolidated revenue in each of the preceding 4 financial years, group structure, reporting entity, scope changes and domestic/foreign notification plans. |

Missing documents or facts yield **Needs Input**. Missing operative authority yields the applicable source refusal below. An answer or professional signature cannot substitute for missing law.

## The method, step by step

### [REGIME IDENTIFICATION] [Official source](https://www.retsinformation.dk/eli/lta/2025/279)

Confirm ordinary resident A/S or ApS, no fired refusal, period and accounting framework. Read the operative SEL provisions and applicable amendments for each position. Ordinary corporate income tax and preliminary/advance tax are separate stages of the same annual liability, not separate deductions from taxable profit. [S1, §§ 1, 8, 10, 17 and 29 A–29 B](https://www.retsinformation.dk/eli/lta/2025/279)

The ordinary return is the company oplysningsskema through TastSelv Erhverv's Selskabsskat/DIAS service. The authority describes the ordinary deadline as 6 months after the accounting year end; confirm the actual registered deadline and any special timing in DIAS. SKL §§ 12–14 and 73, with their listed later amendments, supply the selected filing and late-filing rules below; actual DIAS registration, extensions and case facts still require confirmation. [S9](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/oplysningsskemaet-for-selskaber-og-fonde)

Advance-tax latest ordinary payment dates are 20 March and 20 November of the income year, with voluntary additional payment possible by 1 February of the following year. Calendar-year mapping differs for a shifted income year. Apply the actual decision, valid changes and the official next-weekday rule where a date is a weekend or holiday. The ordinary assessment, voluntary declarations and tax account must agree. [S1, § 29 A](https://www.retsinformation.dk/eli/lta/2025/279) [S8](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/betal-acontoskat-og-selskabsskat)

### [RATES] [Official source](https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven)

| Item | Rate, amount or treatment | Boundary | Tax year | Official URL |
| --- | --- | --- | --- | --- |
| Ordinary corporate income tax | 22% of taxable income under SEL § 17(1) | Determine taxable income first. No assumed small-company band or additional local surcharge is added. This is the ordinary selected rate, not a finding that no other levy exists. | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven |
| Brought-forward loss capacity | DKK 21,830,700 plus 60% of positive income above that amount | Apply only to losses established as available and eligible. The DKK 15.9 million statutory figure is the 2010 base, not the 2026 indexed threshold. | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven |
| Ordinary advance assessment | Total ordinary advance tax is 50% of the prior 3-income-year average tax, payable in 2 equal instalments | Each instalment is half of that total, not 50% of the average. Statutory amount multiples, minimum and initial-year provisions also apply. Use the actual assessment. | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven |
| 2026 voluntary adjustments, residual-tax supplement and refund compensation | Not yet fixed in the ministry's 2026 table read on 2 November 2026 | Do not substitute zero, a 2025 percentage or the 2027 column. Recheck the official publication before the affected calculation. | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven |
| Ordinary tax-account collection interest | 0.95% per month, converted to a daily rate | Calendar year 2026 only: published 0.1% base plus enacted 0.85 percentage points. Not the annual residual-tax supplement or the rate for a 2027 payment period. Qualify the eligible daily balance and exceptions. | 2026 | https://info.skat.dk/data.aspx?oid=2459995 |
| Special sectors, funds, branches and other regimes | No operational rate qualified here | The ministry lists special treatments. Sector classification requires its own provisions and refusal screen. | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven |
| GloBE | Separate conditional 15% minimum-tax system | The ordinary 22% rate does not establish the GloBE effective tax rate or remove reporting obligations. | 2026 | https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/global-minimumsskat-for-store-koncerner-globe |

Sources: [S1, §§ 12, 17 and 29 A–29 B](https://www.retsinformation.dk/eli/lta/2025/279), [S7, 2026 column](https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven) and [S13](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/global-minimumsskat-for-store-koncerner-globe).

### [ADJUSTMENTS] [Official source](https://info.skat.dk/data.aspx?oid=2049133)

1. Reconcile profit before tax to the accounts and full transaction population. Preserve the book amount, classification, tax adjustment, source, period, evidence and reviewer decision for each line.
2. Separate taxable receipts, exempt receipts and receipts governed by other tax Acts. SEL § 8 uses general income rules with exceptions; accounting recognition alone establishes neither taxability nor exemption. The authority's C.D.2.4.1 identifies separate capital-gains Acts and related-party adjustments. [S1, § 8](https://www.retsinformation.dk/eli/lta/2025/279) [S11](https://info.skat.dk/data.aspx?oid=2049133)
3. Test operating deductions against the connection to acquiring, securing and maintaining taxable income. Costs must be incurred and connected to the business. Private expenditure, asset acquisition, establishment costs and hypothetical expenditure cannot be treated as ordinary operating costs merely because they appear in the ledger. Specific exceptions require their own authority. [S12, C.C.2.2.1.2, main principles](https://info.skat.dk/data.aspx?oid=2083469)
4. Build separate book/tax schedules for depreciation, provisions, leases, asset disposals, capital gains, finance and participation income. Add back book depreciation before deducting the established tax allowance. The selected ordinary asset rules below do not qualify all building, intangible, investment or participation-income positions.
5. Apply the interest screens below in statutory order, establish related-party conditions and any group-level allocation, then determine the supported finance adjustment. Missing applicable definitions, arm’s-length evidence or specialist rules stop the affected computation.
6. Reconcile each permanent difference and timing difference, then establish income before loss relief. Do not apply loss relief or tax credits twice. After loss utilisation, round the taxable amount down to a multiple of DKK 100 before calculating tax under SEL § 22. Keep unrounded reconciliation and loss movements distinct from that final tax-base rounding. [S1, § 22](https://www.retsinformation.dk/eli/lta/2025/279)

**Source holds:** an actual capital allowance, interest restriction, exemption, special cost or asset-disposal position needs its complete applicable statutory rule, amendments, election conditions and records before calculation. Refusing an unsupported claim does not authorise an unsupported alternative taxable treatment.


#### Ordinary equipment, immediate expensing and investment window

Afskrivningsloven (AL), LBK 1222 of 13 October 2025, was read with its listed amendments: LOV 749 of 20 June 2025 § 2 takes effect on 1 January 2026 for the stated agreements and repeals AL § 40(7); LOV 615 of 30 June 2026 § 3 changes specified property terminology with effect from 1 January 2027 under § 16(5). These changes do not replace the selected ordinary equipment rules for calendar income year 2026. They do not establish the treatment of all other assets. [S15](https://www.retsinformation.dk/eli/lta/2025/1222) [S16](https://www.retsinformation.dk/eli/lta/2025/749) [S17](https://www.retsinformation.dk/eli/lta/2026/615)

| Position | Rule and conditions | Tax year | Official URL |
| --- | --- | --- | --- |
| Ordinary wholly business equipment | A separate business pool: opening written-down balance + qualified acquisitions/improvements − delivered disposals. The annual allowance is at most 25% of the closing balance before allowance; check §§ 5 B–5 E and other exceptions first. | 2026 | https://www.retsinformation.dk/eli/lta/2025/1222 |
| Small pool and small asset | DKK 36,000 indexed threshold for §§ 5 and 6. Under § 5(3), a qualifying pool at or below that threshold before the year’s allowance may be deducted in full instead of applying the 25% limit. For § 6, assets forming a set or intended to function together are one asset; additions to an existing set cannot be separated to evade the threshold. | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/afskrivningsloven |
| Short physical life | AL § 6 allows an election to expense qualifying equipment with an expected physical life no more than 3 years. Rental-company timing exceptions still apply. | 2026 | https://www.retsinformation.dk/eli/lta/2025/1222 |
| New eligible equipment, AL § 5 E | Elect a separate 108% basis for factory-new equipment acquired from 1 January 2025 through 31 December 2026 and used wholly for business. Excludes passenger cars, ships, software and equipment powered or capable of being powered by fossil fuel through its own energy supply. No § 6 immediate expensing of the same cost. Maximum 25% annual pool allowance, 108% disposal proceeds and applicable rental/individual-loss rules. Merge with the ordinary pool at the end of 2030 for § 5 treatment from 2031. | 2026 | https://www.retsinformation.dk/eli/lta/2025/1222 |
| Older 116% pool, AL § 5 D | Applies to its separate 23 November 2020–31 December 2022 acquisition window and exclusions. Merge its balance with the ordinary pool at the end of 2026 for treatment from 2027. A 2026 acquisition does not enter that old window. | 2026 | https://www.retsinformation.dk/eli/lta/2025/1222 |

Establish acquisition by delivery to an operating business, intended business use and sufficient completion under AL § 3. Exclude non-depreciating assets under § 2(3). Changes of use are deemed disposals/acquisitions at market value under § 4. Establish cash-value bases and the written allocation among transferred assets under § 45; the authority may review the allocation and a changed seller value affects the buyer's basis correspondingly. Do not substitute accounting cost without testing the tax basis. [S15, §§ 2–4 and 45](https://www.retsinformation.dk/eli/lta/2025/1222)

For corporate rental assets, § 5(4) ordinarily defers the first allowance: no ordinary-pool inclusion in the acquisition year or the next year, a separate allowance up to 50% in the next year, then the remaining balance joins the pool in the second following year. Disposals and an actual § 5(6) permission change the treatment. § 6(3) similarly defers specified immediate deductions to the following year unless permission applies. Do not apply the own-use method automatically to rental equipment.

A negative pool is not a negative depreciation deduction: AL § 8 governs inclusion or offset by acquisitions in the following year and conditional extensions. The § 5 A individual asset loss election reduces the pool by the unrelieved asset amount, disallows depreciation on that asset in the sale year and cannot produce a negative pool. Trading assets fall under § 50. These paths need their complete facts and election analysis.

Special ships/infrastructure under §§ 5 B–5 C, mixed use, business cessation, buildings, leasehold improvements, goodwill/intangibles and R&D tangible-asset deductions need their own complete applicable units and companions. The selected LL § 8 B enhancement and § 8 X cash-credit principles are below. The source table lists which units were actually read. A ministry table alone cannot establish asset eligibility.

#### Interest restrictions and order

The complete selected SEL §§ 11, 11 B and 11 C were read. Apply § 11 first, then § 11 B and finally § 11 C; do not compare 3 unrelated ceilings and choose one. [S1](https://www.retsinformation.dk/eli/lta/2025/279)

| Screen | Selected rule and conditions | Tax year | Official URL |
| --- | --- | --- | --- |
| Thin capitalisation, § 11 | Controlled debt above DKK 10 million and year-end debt/equity above 4:1 can disallow interest and exchange losses on the specified excess controlled debt. Third-party debt with related guarantees can count. Arm’s-length funding evidence, statutory definitions, equity retention, aggregation and ordering exceptions apply. | 2026 | https://www.retsinformation.dk/eli/lta/2025/279 |
| Asset-based limit, § 11 B | Defined net financing expenses are limited by defined tax asset value × 4.2% standard rate, with a DKK 21.3 million deduction floor, exceptions for specified exchange losses and special group/short-period rules. The floor and standard rate are not a universal safe harbour for every finance charge. | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven |
| Earnings-based limit, § 11 C | Defined exceeding borrowing costs after §§ 11 and 11 B face the 30% tax-earnings-before-interest-and-depreciation limit, with a DKK 22,313,400 deduction floor, proportional short/long-period adjustment and group conditions. Disallowed costs and unused capacity have different carryforward treatment. | 2026 | https://www.retsinformation.dk/eli/lta/2025/279 |

For § 11 B, retain the statutory reconciliation of financing income/expenses and excluded trade items, hedges, swaps and CFC amounts; tax asset value excludes or adjusts specified financial assets, related holdings, working capital, leased assets and other items. Group aggregation, the allocation of restrictions and special exchange-loss carryforwards must be traced. The old 20% foreign-share inclusion in § 11 B(6) is reduced by § 11 B(12) to zero for 2017 and later; never apply the isolated 20% sentence to 2026.

Under § 11 C, restricted costs carry forward; unused interest capacity carries for 5 subsequent income years with oldest capacity first. Group computation, a qualifying audited group-ratio election and financial-sector exclusions have separate conditions. A small finance balance may clear a threshold only after its proper statutory definition and aggregation are established. The linked Ligningsloven, Kursgevinstloven, tax-asset and group definitions remain required where applicable.


#### Participation income and share classification

Classify each holding before excluding any dividend, gain or loss. Under ABL § 4 A, subsidiary shares start with at least 10% of capital but must also meet the entity, tax, information-exchange and other conditions; intermediary-holding rules can change the attributed owner. ABL § 4 B uses qualifying joint-tax/group relationships, with its own intermediary and excluded-instrument rules. ABL § 4 C covers qualifying unlisted holdings below 10%, subject to entity, composition, look-through and excluded-instrument conditions. Its listed-share composition test is no more than 85% of the portfolio company’s equity under the prescribed averaging method. A percentage holding alone does not settle exemption. [S31, §§ 4 A–4 C](https://www.retsinformation.dk/eli/lta/2026/849)

For the classes covered by ABL § 8, both gains and losses on disposal are excluded from taxable income. Taxable portfolio holdings under § 9 have different gain and loss treatment, including the applicable timing method and restricted-loss baskets. Do not deduct an exempt-holding loss or freely offset every realisation loss against operating profit. Complete §§ 10, 17, 19 and 23 and other special-class or timing provisions where relevant; those units are not qualified here. [S31, §§ 8–9](https://www.retsinformation.dk/eli/lta/2026/849)

Dividends have a separate SEL § 13 analysis. Qualifying subsidiary/group or tax-free portfolio dividends can be exempt under their specific conditions; deductible distributions, hybrid mismatches, beneficial ownership, intermediary holdings and LL § 3 can prevent a claimed benefit. Do not carry the disposal classification across to dividend, withholding or treaty treatment without checking each applicable rule. Record the ownership chain, tax residence/status, instrument, listing, costs, distribution terms, entitlement and supporting evidence. Actual cross-border or special-class positions remain held until all applicable authority is complete. [S1, § 13](https://www.retsinformation.dk/eli/lta/2025/279) [S30, § 3](https://www.retsinformation.dk/eli/lta/2025/1500)

### [LOSSES] [Official source](https://www.retsinformation.dk/eli/lta/2025/279)

SEL § 12 permits carryforward and requires available losses to be used at the earliest permitted opportunity. The official guidance describes carryforward without a fixed time limit. The indexed 2026 full-relief threshold is DKK 21,830,700; above it, brought-forward losses can reduce only 60% of the excess income. The remaining taxable fraction is not a new tax rate. Current-year group losses and brought-forward losses must be distinguished. [S1, § 12](https://www.retsinformation.dk/eli/lta/2025/279) [S7](https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven) [S10](https://info.skat.dk/data.aspx?oid=2049731)

For the fictional standalone positive-income cases only, let P be established income before brought-forward losses, L be eligible available brought-forward losses and T = DKK 21,830,700:

- Capacity = min(P, T) + 60% × max(P − T, 0).
- Used = min(L, capacity).
- Taxable income = P − used.
- Closing eligible losses = L − used.

This arithmetic is conditional on P being positive and all eligibility gates being cleared. It does not qualify group allocation, debt relief, ownership changes, elections or ring-fenced capital losses. SEL § 12's special election interaction also requires checking.

A greater-than-50% capital or voting change can restrict loss utilisation under SEL § 12 D, with different restrictions for specified capital income and companies essentially without business economic risk, and detailed exceptions/look-through conditions. SEL § 12 A reduces losses in specified reconstruction/debt-relief arrangements, with adjustments and related-claim rules. Do not convert these into an automatic cancellation whenever an owner changes or debt is reduced. §§ 12 B–12 C, applicable elections, full group rules and loss-registration procedures remain unqualified. Any such fact pattern stops the ordinary loss method. [S1, §§ 12 A and 12 D](https://www.retsinformation.dk/eli/lta/2025/279)

#### Domestic joint taxation and loss order

Qualifying domestic group members must enter national joint taxation under SEL § 31. Establish the actual group and periods under § 31 C, including contractual control, currently exercisable rights and entry/exit events; a capital-percentage shortcut is insufficient. The control definitions in § 31 C, LL § 2 and SEL § 32(6) serve different rules. The selected ordinary provisions are read with S4’s entity cross-reference amendment effective from 1 January 2026. [S1, §§ 31 and 31 C](https://www.retsinformation.dk/eli/lta/2025/279) [S4, §§ 5 and 8](https://www.retsinformation.dk/eli/lta/2025/1755)

Prepare entity-by-entity and period-by-period taxable income, then follow § 31(2)–(3):

1. Use a profitable company’s eligible own pre-joining losses against its own income only.
2. Next use its own eligible carried losses from the joint-tax period.
3. Allocate usable current-year group losses proportionately amongst the remaining profitable companies.
4. Then offset eligible remaining carried losses from other group members proportionately, respecting common membership and uninterrupted continuity. Allocate the usable amount across eligible loss balances proportionately. Within each company, use its oldest eligible losses first; do not exhaust one company’s losses simply because its oldest vintage is earlier than another company’s.
5. Apply § 12(2)’s brought-forward-loss limit only if the sum of the jointly taxed companies’ current-year incomes is positive. For a positive sum, apply the limit once across the group and allocate the restriction proportionately across the otherwise usable carried-loss amounts as § 31(3) prescribes. For a zero or negative sum, § 31(3) does not apply that restriction. Do not grant the full threshold separately to each member. Current-year loss sharing and the carried-loss limit are different stages.
6. Preserve unutilised loss ownership, origin, vintage, restrictions and closing balances. Part-year membership, restructuring and interrupted joint taxation require their complete special analysis.

Identify the administration company and common tax period. Under § 31(8), establish the tax-value compensation for used domestic group losses and the corresponding obligations through the administration company, subject to the statutory alternative payment route. Record income-tax, advance-tax and liability allocations separately. Do not assume accounting consolidation settles tax grouping, that every group transfer is deductible or that every member has identical payment liability. Full § 31 D grant conditions, international joint taxation, recapture, final foreign losses and actual group filing/payment procedures remain required where applicable. [S1, §§ 31, 31 C and 31 D](https://www.retsinformation.dk/eli/lta/2025/279)

Maintain loss vintage, origin, assessed amount, adjustments, ownership/group restrictions, utilisation and closing balance. Loss entitlement and deferred-tax-asset recognition are separate questions. Apply the established accounting framework's recoverability rule; this guide supplies no assumed recognition percentage.

### [CREDITS] [Official source](https://www.retsinformation.dk/eli/lta/2025/279)

SEL § 17(2)–(4) includes conditional foreign-dividend underlying-tax relief, not a general credit for every foreign payment. Its gross-up, ownership, limit and underlying-tax conditions must be qualified before a claim. [S1, § 17](https://www.retsinformation.dk/eli/lta/2025/279)

#### Foreign-tax credit and net-income limit

For a supported ordinary LL § 33 claim, establish the foreign source, income included in Danish taxable income, foreign tax actually paid and legal entitlement under any applicable treaty. The relief cannot exceed the Danish tax attributable to that foreign income; where a treaty applies, it also cannot exceed the foreign state’s unconditional treaty entitlement. Withholding above that entitlement does not become a Danish credit merely because it was paid. [S30, § 33](https://www.retsinformation.dk/eli/lta/2025/1500)

Calculate the Danish attributable-tax limit using the established foreign net income and total Danish-taxed income, with the applicable tax calculation and source/period allocation. LL § 33 F requires directly related expenses to reduce the foreign-income base and allocates non-attributable common expenses by the Danish/foreign gross-income ratio, subject to its specific exception. Keep an expense-allocation schedule. Do not use gross receipts as net foreign income, divide by a non-positive denominator or assume that a loss-period cap equals the ordinary positive-income ratio. [S30, §§ 33 and 33 F](https://www.retsinformation.dk/eli/lta/2025/1500)

LL § 33 H permits a separate election to disregard specified losses in order to preserve double-tax relief, with group and proportional-allocation conditions; disregarded losses move to later years under SEL § 12. It is not an automatic increase in a credit. Establish the election and every applicable country/source, treaty, group, dividend, CFC or special-tax rule before an actual claim. No general excess-credit carryforward is established here; § 33(9)’s specific shipping-tax rule cannot be generalised. [S30, §§ 33, 33 F and 33 H](https://www.retsinformation.dk/eli/lta/2025/1500)

#### R&D deduction and cash credit

LL § 8 B eligibility requires qualifying research or development linked to the taxpayer’s business. The authority’s selected guidance examines novelty relative to the industry, creativity and uncertainty, commercial connection and exploitation of the results. Routine software work, marketing, production start-up and other listed costs do not qualify merely because they are called R&D. Tangible assets use the applicable AL provisions. Preserve project evidence, cost allocation, commencement, ownership/use and the chosen immediate or 5-year deduction method. Basic research and pre-business expenditure have separate conditions. [S30, § 8 B](https://www.retsinformation.dk/eli/lta/2025/1500) [S34, selected eligibility and timing sections](https://info.skat.dk/data.aspx?oid=2083520)

| Position | Selected rule and conditions | Tax year | Official URL |
| --- | --- | --- | --- |
| Eligible enhanced R&D deduction | 114% within the combined expenditure ceiling; LL § 8 B and AL § 6(1), no. 3 have their own eligibility and elections. This is separate from AL § 5 E’s 108% equipment option. | 2026 | https://www.retsinformation.dk/eli/lta/2024/1472 |
| Combined expenditure ceiling | DKK 1,088.8 million, shared across the relevant joint-tax group and allocated proportionately under the statute. This is the eligible expenditure ceiling, not a cash-credit amount. | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/ligningsloven |
| Eligible expenditure above that ceiling | 110% from 2026 under the enacted rule. The ministry table’s dash in its 2026 above-ceiling cell is not substituted for this statutory rule. | 2026 | https://www.retsinformation.dk/eli/lta/2024/1472 |
| R&D cash-credit base | At most DKK 25 million for a full 12-month income year, with short-year reduction, joint-tax and common-controller aggregation. The printed DKK 35 million wording starts in 2027. | 2026 | https://www.retsinformation.dk/eli/lta/2024/1691 |
| Gross cash-credit value | 22% of the qualifying current-year loss base; no credit for the enhancement component or more than the actual qualifying costs. The full-year DKK 25 million cap implies at most DKK 5.5 million before other limits and offsets. | 2026 | https://www.retsinformation.dk/eli/lta/2025/1500 |

Read LL § 8 X with its official notes 4–6 and LOV 1691/2024 § 9(6): the consolidated text includes future wording for the 2027 cap and payment cross-reference. The inspected 2026 cap is DKK 25 million, also confirmed by S35’s year columns. LOV 1472/2024 §§ 1–2 and 4 qualify the enhancement chain and its commencement. [S30](https://www.retsinformation.dk/eli/lta/2025/1500) [S32](https://www.retsinformation.dk/eli/lta/2024/1472) [S33](https://www.retsinformation.dk/eli/lta/2024/1691) [S35](https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/ligningsloven)

A cash-credit request accompanies the annual SKL § 2 return and reduces the current loss by the loss base requested. It does not both pay cash and leave that same loss available to carry forward. Joint-tax groups use the administration company and the statutory group calculation/allocation; commonly controlled businesses have an additional shared cap. Tax arrears can offset the payment, and overpaid credit can be reclaimed with the corresponding loss restoration. Actual request fields, payment timing, collection law and eligibility decisions remain held until their applicable sources and facts are complete. A gross illustrative credit is not a verified bank receipt or an ordinary foreign-tax credit. [S30, § 8 X](https://www.retsinformation.dk/eli/lta/2025/1500) [S34, selected claim, loss-adjustment and offset sections](https://info.skat.dk/data.aspx?oid=2083520)

No complete actual IP, investment-incentive, specialist withholding or cross-border credit package has been qualified here. An asserted benefit remains held until its operative authority, eligibility, ordering, facts and procedure are established. A blank claim field is not evidence of no claim.


### [FILING MECHANICS] [Official source](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/oplysningsskemaet-for-selskaber-og-fonde)

Verify basic registrations first, including group status, income year and return deadline. The authority warns that incorrect basic information can produce the wrong fields or calculation. Follow TastSelv Erhverv → Skat for selskaber m.fl. → Selskabsskat → Selskabsskat → Oplysningsskema → income year → Begynd indberetning. Retain the relevant return-field/manual version for the actual period; the linked PDF manuals were discovered but not read. [S9](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/oplysningsskemaet-for-selskaber-og-fonde)

Assemble all required specifications and attachments, examine the consequence summary and obtain reviewer acceptance before submission. The reviewer submits personally. Save the acknowledgement and final submitted copy. Drafts are not visible to the authority as filed returns. The authority says that changing a draft or basic information before the deadline may require resetting and resubmitting; after the deadline, the reopening process applies. Do not treat a saved draft, reset or amendment request as accepted filing. [S9](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/oplysningsskemaet-for-selskaber-og-fonde)

SKL § 2 requires annual reporting of positive or negative income, with its exceptions; § 5 addresses the designated digital channels and does not excuse a missing return form. For ordinary legal persons, § 12 sets 6 months after the income year, except an income year ending during March has 1 September of that year. Under § 13, if the deadline is the day before or on a Saturday, Sunday or public holiday, filing by 9 am on the first following weekday is timely. § 14 permits a taxpayer-specific extension for special circumstances and specified group extensions; obtain the actual decision. For the stipulated calendar year ending 31 December 2026, the ordinary § 12 date is **30 June 2027**, subject to the actual registered period, § 13 and any valid extension. [S19, §§ 2, 5 and 12–14](https://www.retsinformation.dk/eli/lta/2024/12)

The 2024 consolidation's § 73 printed DKK 200/day and a DKK 5,000 cap. LOV 16 of 14 January 2025 § 2 replaces these with **DKK 400/day**, capped at **DKK 10,000**, and commences on 15 January 2025 under § 4. That is the ordinary selected § 73(1) late-information charge, not an understatement penalty or collection interest. Other subsections cover different persons or special declarations; § 73(4) permits full/partial relief on application in special circumstances. Do not infer relief, the number of late days or a final assessment without the actual facts and decision. The later-amendment review below identifies no change to the selected ordinary deadline or corporate § 73(1) figures. [S19, § 73](https://www.retsinformation.dk/eli/lta/2024/12) [S20](https://www.retsinformation.dk/eli/lta/2025/16)

The authority says inactive and newly formed companies still submit returns. Audit requirements and annual-report filing need their own current sources; a tax return is not the annual report. [S9](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/oplysningsskemaet-for-selskaber-og-fonde)

**Selected tax-account and collection rules.** OPKL LBK 1040/2024 must be read with its later amendments. The selected OPKL targets in all 10 listed later Acts and their commencement provisions were read: LOV 620/2024 § 18 and § 17; 683/2024 § 5 and § 9; 1473/2024 § 5 and § 19; 1694/2024 § 1 and § 18; 16/2025 § 1 and § 4; 749/2025 § 3 and § 5; 1642/2025 § 4 and § 10; 1648/2025 § 22 and § 25; 1783/2025 §§ 2, 5 and 6; 763/2026 §§ 1 and 8. This establishes the selected chain below, not every collection, refund, remission, appeal or enforcement procedure. [S44](https://www.retsinformation.dk/eli/lta/2024/1040) [S47](https://www.retsinformation.dk/eli/lta/2024/620) [S48](https://www.retsinformation.dk/eli/lta/2024/683) [S23](https://www.retsinformation.dk/eli/lta/2024/1473) [S46](https://www.retsinformation.dk/eli/lta/2024/1694) [S20](https://www.retsinformation.dk/eli/lta/2025/16) [S16](https://www.retsinformation.dk/eli/lta/2025/749) [S38](https://www.retsinformation.dk/eli/lta/2025/1642) [S49](https://www.retsinformation.dk/eli/lta/2025/1648) [S5](https://www.retsinformation.dk/eli/lta/2025/1783) [S6](https://www.retsinformation.dk/eli/lta/2026/763)

OPKL § 16 includes corporate-tax payments. From 1 January 2026, LOV 1783/2025 § 2, no. 4 also includes SKL § 73 charges imposed on legal persons. Keep that late-information charge separate from a fine and from collection interest. Under § 16 A, payments and credits offset automatically on the tax account; claims affect the balance from their last timely payment day and cash payments from the payment day. Where a payment covers a debit balance of several claims, the oldest-due claim is covered first. Debts transferred for collection follow the separate enforcement legislation. [S44, §§ 16–16 A](https://www.retsinformation.dk/eli/lta/2024/1040) [S5, § 2 and § 6](https://www.retsinformation.dk/eli/lta/2025/1783)

Ordinary payments are unallocated under § 16 B(1), with the specific voluntary corporate advance-payment designation requirement in § 16 B(2). LOV 1642/2025 § 4 removes that subsection’s pension-advance wording and repeals subsection 3 from 1 January 2026. Designating a voluntary corporate advance does not itself establish that funds were available, credited to it or given priority over older debts. Reconcile the declaration, actual account balance, posting and S8 payment instructions before claiming a credit. [S44, § 16 B](https://www.retsinformation.dk/eli/lta/2024/1040) [S38, § 4 and § 10](https://www.retsinformation.dk/eli/lta/2025/1642) [S8](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/betal-acontoskat-og-selskabsskat)

BEK 1793/2025 §§ 1–3 starts LOV 1694/2024 § 1, nos 6 and 17 and LOV 1783/2025 § 2, nos 5–6 on **1 January 2026**. LOV 1783 § 5 repeals LOV 1694 § 1, nos 15 and 18 before they take effect and revises its deferred-commencement list. Use the operative LOV 1783 amendments, not those repealed items, for the principal-and-fees base and cessation test. Its § 6(7) interim interest rule must be read with that now-established commencement date. [S45](https://www.retsinformation.dk/eli/lta/2025/1793) [S46](https://www.retsinformation.dk/eli/lta/2024/1694) [S5](https://www.retsinformation.dk/eli/lta/2025/1783)

For the selected ordinary 2026 tax-account regime, amended § 16 C charges interest on the debit balance attributable to **principal claims and fees**. Already accrued interest does not enter that interest base. Interest accrues daily and is posted monthly, is not deductible and does not apply to fines under the statutory exception. Customs debt uses its separate EU rule; a credit balance earns no interest. The DKK 200 cessation test concerns the principal-and-fees part of a debit balance after registered cessation, not a general exemption for small balances. Determine the actual debt type and applicable exception first. [S44, § 16 C](https://www.retsinformation.dk/eli/lta/2024/1040) [S46, § 1](https://www.retsinformation.dk/eli/lta/2024/1694) [S5, § 2](https://www.retsinformation.dk/eli/lta/2025/1783) [S45](https://www.retsinformation.dk/eli/lta/2025/1793)

SKM2025.720.SKTST sets the OPKL § 7(2) base at **0.1% from 1 January 2026**. The enacted 0.85 percentage-point supplement gives **0.95% per month** for the selected ordinary calendar-year 2026 interest. The authority’s daily method converts using 365/12 days per average month for 2026; interest runs after the last timely payment day through the payment day inclusive. Use each eligible daily balance and the rate for that calendar year. The 2026 collection rate does **not** establish a rate for a residual balance for income year 2026 that falls due in 2027. The 2027 collection rate, annual 2026 settlement percentages, actual dates, daily changes, posting precision, relief and final payable amount remain held. Case 13 is a limited constant-balance illustration. [S51](https://info.skat.dk/data.aspx?oid=2459995) [S46, § 1](https://www.retsinformation.dk/eli/lta/2024/1694) [S45](https://www.retsinformation.dk/eli/lta/2025/1793) [S50, interest calculation](https://info.skat.dk/data.aspx?oid=2290071) [S52, tax-account interest](https://info.skat.dk/data.aspx?oid=2168702)

LOV 763/2026 §§ 1 and 8 raises the OPKL § 6 reminder fee from DKK 65 to **DKK 160 from 14 September 2026** and changes the § 16 C reminder rules. Establish the actual notice, date, debt composition and procedure before charging a fee or calculating an enforcement deadline. The inspected A.D.8.1 still prints DKK 65 and attributes removal of compound interest to LOV 1694 § 1, no. 15. Those passages are stale against LOV 763 and LOV 1783’s repeal/substitution. Apply the enacted chain above. The historical back-charging discussion in A.B.4.5.3 does not establish the current method; its underlying historical decisions were not independently qualified here. [S6](https://www.retsinformation.dk/eli/lta/2026/763) [S5](https://www.retsinformation.dk/eli/lta/2025/1783) [S50](https://info.skat.dk/data.aspx?oid=2290071) [S52](https://info.skat.dk/data.aspx?oid=2168702)

### [ANTI-AVOIDANCE] [Official source](https://www.retsinformation.dk/eli/lta/2025/750)

Screen related-party dealings, transfer pricing, CFC, reverse hybrids and other hybrid mismatches, withholding, treaty benefits, beneficial ownership, restructurings, debt relief and general anti-abuse. Do not treat Denmark as having a US-style BEAT/GILTI charge by analogy. No equivalence or absence finding has been established.

LL § 2 requires arm’s-length prices and terms for the specified controlled dealings. Its control and aggregation rules, corresponding adjustments and secondary-adjustment conditions require their own evidence. The selected SKL reporting/documentation amendments do not qualify the complete transfer-pricing workflow. LL § 3 addresses non-genuine arrangements seeking a tax advantage contrary to the law’s purpose, with its commercial-reality, treaty-purpose and procedural conditions. Do not treat a legal form, accountant approval or a nominal business explanation as automatic clearance. [S30, §§ 2–3](https://www.retsinformation.dk/eli/lta/2025/1500)

SEL § 32’s CFC entry conditions include CFC income exceeding one-third of the subsidiary’s defined total taxable income, its specific control test and other conditions. The control test includes more than 50% voting, capital or profit entitlement with statutory aggregation and associated-person rules. The statute is not a generic low-tax or foreign-only test. The financial-entity, territorial, intellectual-property, attribution, loss, relief and transitional rules must be applied together. Its official transitional note can change the relevant intangible-asset basis. [S1, § 32 and official note 3](https://www.retsinformation.dk/eli/lta/2025/279)

Under § 32(15)–(16), CFC-income-only attribution is an election with a 5-income-year binding period and its own loss consequences. An omitted or late election can result in attribution of the subsidiary’s total income under the statutory method. Do not default to CFC-income-only or calculate actual CFC liability from the entry ratio alone. Complete applicable supporting law, elections, records, disclosure and credit interactions remain required; actual CFC outputs remain held. [S1, § 32](https://www.retsinformation.dk/eli/lta/2025/279)

S3 changes specified hybrid and international joint-tax provisions, including effective-date distinctions. The complete applicable hybrid and specialist reporting workflows remain unqualified. Preserve every fired base refusal and source hold. A reviewer flag cannot clear a fired refusal or establish missing law. [S3](https://www.retsinformation.dk/eli/lta/2025/750)

### [PILLAR TWO OVERLAY] [Official source](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/global-minimumsskat-for-store-koncerner-globe)

The authority describes Danish global minimum tax as enacted in December 2023, with a 15% minimum and a scope threshold of at least EUR 750 million consolidated revenue in at least 2 of the preceding 4 financial years. Its guidance includes covered domestic entities and reporting/notification requirements, with first reporting generally 18 months and subsequent reporting 15 months after the relevant financial year. The threshold is a scope screen, not a tax computation. [S13](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/global-minimumsskat-for-store-koncerner-globe)

Capture all 4 years, the group and entity scope and any transparent-entity or stateless issue. If potentially covered, load the global Pillar Two companion and qualify Minimumsbeskatningsloven, amendments, IIR/QDMTT/UTPR effective provisions, elections, safe harbours, reporting and actual deadlines before computing or preparing outputs. Those statutory units are not qualified here. Do not set top-up tax to zero because the ordinary rate is 22%, infer non-enactment from a missing source or fire R-CIT-11 merely because this draft lacks the law.

### [CROSS-REFERENCES]

Load the applicable companion content and its current country sources for corporate workflow, transfer pricing, permanent-establishment risk, outbound withholding, foreign tax credits, Pillar Two, DAC6/MDR, CbCR, R&D and IP incentives, special zones and relevant bookkeeping/financial reporting. A generic matrix is a screening aid unless its Danish row and applicable authority have been verified. The existing Danish personal income-tax guide excludes companies and cannot fill this corporate-law gap.

The ordinary corporation method does not settle VAT, payroll, social contributions, company formation, annual reporting or owner taxation. Identify those related obligations and route them to supported companions. Never drop a transaction because its branch requires another skill.

### Defaults, materiality and outputs

No missing-fact default is authorised in this draft. Keep an unresolved value as **Needs Input** and stop the affected calculation; do not assume zero, no foreign activity, no group, no credits, no tax adjustment or no Pillar Two exposure. The hypothetical cases below stipulate their facts and are not defaults.

The reviewer sets and documents cash/materiality thresholds for enquiries and presentation under the applicable engagement and accounting framework. Such thresholds cannot waive legal eligibility, statutory filing, refusal checks, source evidence or rounding requirements. No Danish statutory materiality threshold is asserted here.

After all source and fact holds clear, preserve all 4 universal deliverables: recalculated working-paper workbook, reviewer brief, action list and review checklist. Also preserve every corporate-base output: return and schedules, current/deferred tax provision, DTA recoverability, credit and loss schedules, tax payment schedule, cross-border/GloBE analysis where applicable and supporting-document index. Record a positively established non-applicability with reasons. Do not deliver a package with an unresolved applicable branch.

The workbook additionally separates ordinary advances assessed, voluntary amounts declared, cash paid, credited amounts, unpaid assessed advances, principal residual tax, statutory supplements/compensation, collection interest and tax-account allocations. Record each credit and payment exactly once.

## Boundary and exception table

| Trigger | Consequence |
| --- | --- |
| Registered ordinary standalone A/S or ApS, supported facts and complete applicable sources | The selected ordinary rules may support preparation only after all base gates and professional review requirements are satisfied. This draft alone does not clear them. |
| Foreign residence, branch, PE or property, treaty issue | Resolve classification and § 8 exceptions with complete sources; apply the base residence/dual-residence refusal where triggered. |
| Group, ownership change, debt relief or restructuring | Qualify group aggregation, loss restrictions and timing. No standalone loss allocation or assumed restoration of losses. |
| Assets, depreciation, interest limitation, dividend/capital gain or incentive | Stop the affected position until the complete applicable sources and records are loaded. |
| Financial, extractive, fund, tonnage, nonprofit or insolvency regime | Apply the corporate base's named refusal and load the required specialist content. |
| Potential GloBE threshold or coverage | Obtain the applicable Danish law and global companion; complete scope/reporting and calculation before ordinary-tax delivery. |
| Unknown 2026 supplement, refund or voluntary-adjustment percentage | Stop final settlement; monitor the authority's publication. Do not recycle 2025 figures. |
| Actual filing, penalty or collection-interest case | Apply the qualified ordinary filing/charge rules, establish any special procedure and obtain the actual notice. The selected 2026 collection chain does not establish actual dates, allocation, 2027 rates, relief or a complete procedure. No portal acceptance is inferred. |

## Worked cases

All cases are fictional arithmetic in DKK. Cases 1–12 concern calendar income year 2026; Case 13 concerns interest days wholly within calendar year 2026. Cases 1–7 concern a standalone ordinary resident company with no group, ownership or debt-relief restriction, credits, foreign activity or adjustments beyond those expressly stated. Case 8 stipulates a foreign-credit position, Case 9 a domestic group and Case 10 an eligible R&D deduction and cash-credit request. Cases 11–12 test domestic group-loss conditions, allocation and vintages. Case 13 stipulates an already-established ordinary tax-account balance and 20 interest days. Every case assumes complete positive evidence of its stated facts. These assumptions do not clear real-source or engagement holds. Taxable amounts are rounded under SEL § 22 where shown. Remaining settlement adjustments and actual taxpayer acceptance stay held.

### Case 1: ordinary liability and held settlement

Established income before loss relief is 1,000,000; eligible losses are zero. Taxable income is 1,000,000 and ordinary tax is 1,000,000 × 22% = **220,000**. Ordinary advance tax assessed and paid is 100,000; there is no voluntary advance or withholding credit. Residual-tax principal under the stipulated facts is 220,000 − 100,000 = **120,000**. The 2026 residual-tax supplement remains unqualified/not fixed in the selected table; **120,000 is not the final payable balance**. Keep final settlement held. Sources: S1 §§ 17 and 29 B, S7.



```oa-check
name: Case 1; ordinary liability and principal, final settlement held
inputs:
  income: 1000000
  assessed_advances: 100000
steps:
  - tax: income * 0.22
  - residual_principal: tax - assessed_advances
expected:
  tax: 220000
  residual_principal: 120000
```

### Case 2: losses below the indexed threshold

Established income before losses is 1,000,000 and eligible brought-forward losses are 2,000,000. Capacity = 1,000,000 + 60% × 0 = **1,000,000**. Used = min(2,000,000, 1,000,000) = **1,000,000**. Taxable income = **zero**; ordinary current tax = **zero**. Closing eligible losses = 2,000,000 − 1,000,000 = **1,000,000**. No cash refund or DTA follows merely from that closing loss. Sources: S1 § 12, S7, S10.



```oa-check
name: Case 2; eligible loss below 2026 threshold
inputs:
  income: 1000000
  eligible_losses: 2000000
  threshold: 21830700
steps:
  - capacity: min(income, threshold) + 0.60 * max(income - threshold, 0)
  - used: min(eligible_losses, capacity)
  - taxable: income - used
  - closing_losses: eligible_losses - used
  - tax: taxable * 0.22
expected:
  capacity: 1000000
  used: 1000000
  taxable: 0
  closing_losses: 1000000
  tax: 0
```

### Case 3: losses above the indexed threshold

Established income before losses is 30,000,000 and eligible losses are 30,000,000. Excess over T = 30,000,000 − 21,830,700 = **8,169,300**. Restricted excess relief = 8,169,300 × 60% = **4,901,580**. Total capacity = 21,830,700 + 4,901,580 = **26,732,280**. Use **26,732,280**, leaving taxable income **3,267,720** and closing eligible losses **3,267,720**. SEL § 22 rounds the taxable amount down to **3,267,700** before tax. Ordinary tax = 3,267,700 × 22% = **718,894**. The exact loss movement and closing loss above remain **3,267,720**; tax-base rounding does not create another DKK 20 of available losses. Sources: S1 §§ 12, 17 and 22, S7.



```oa-check
name: Case 3; 2026 indexed loss restriction and tax-base rounding
inputs:
  income: 30000000
  eligible_losses: 30000000
  threshold: 21830700
steps:
  - excess: max(income - threshold, 0)
  - excess_relief: excess * 0.60
  - capacity: min(income, threshold) + excess_relief
  - used: min(eligible_losses, capacity)
  - taxable: income - used
  - closing_losses: eligible_losses - used
  - rounded_taxable: floor(taxable / 100) * 100
  - tax: rounded_taxable * 0.22
expected:
  excess: 8169300
  excess_relief: 4901580
  capacity: 26732280
  used: 26732280
  taxable: 3267720
  closing_losses: 3267720
  rounded_taxable: 3267700
  tax: 718894
```

### Case 4: ordinary advance assessment is split once

For a mature company with no group or initial-year exception, the prior 3 income-year taxes are 200,000, 240,000 and 280,000. Average = (200,000 + 240,000 + 280,000) ÷ 3 = **240,000**. Total ordinary advance assessment = 240,000 × 50% = **120,000**, split into **60,000** and **60,000**. These amounts satisfy the stated statutory minimum and divisibility conditions. Taking 120,000 in each instalment would double the selected statutory total. Reconcile to the actual notice and any lawful changes; this is not a payment instruction. Source: S1 § 29 A(2).



```oa-check
name: Case 4; total ordinary advance split once
inputs:
  year1: 200000
  year2: 240000
  year3: 280000
steps:
  - average: (year1 + year2 + year3) / 3
  - ordinary_total: average * 0.50
  - instalment: ordinary_total / 2
expected:
  average: 240000
  ordinary_total: 120000
  instalment: 60000
```

### Case 5: assessed advances differ from cash paid

Ordinary tax liability is **220,000**. Ordinary advances assessed are **120,000**, but cash paid against them is only **100,000**; no voluntary advance, credits or allocation differences exist. SEL § 29 B(4) includes assessed advances in the residual-tax computation whether paid or not. Residual-tax principal = 220,000 − 120,000 = **100,000**. The unpaid advance is separately **20,000**. Together those principal balances are **120,000**, but calling all 120,000 residual tax would misclassify the assessment. Interest, supplements and allocation still require separate qualified treatment. Sources: S1 § 29 B(4), S5–S6 for affected procedure, S8.



```oa-check
name: Case 5; assessed advances and unpaid cash balance
inputs:
  tax: 220000
  assessed: 120000
  cash_paid: 100000
steps:
  - residual_principal: tax - assessed
  - unpaid_advance: assessed - cash_paid
  - total_principal: residual_principal + unpaid_advance
expected:
  residual_principal: 100000
  unpaid_advance: 20000
  total_principal: 120000
```

### Case 6: reduce an instalment by a delta

The actual ordinary instalment shown is 60,000. The reviewer has independently established a lawful revised amount of 40,000 and authority to change it. The change field requires a delta: 40,000 − 60,000 = **−20,000**. Entering positive 40,000 as the delta would instead produce 100,000. This illustrates the authority's field semantics only; the reviewer checks the live sign convention, eligibility, confirmation and resulting amount before any action. No login or portal test was performed. Source: S8.



```oa-check
name: Case 6; change field needs delta
inputs:
  current: 60000
  desired: 40000
steps:
  - delta: desired - current
  - wrong_input_total: current + desired
expected:
  delta: -20000
  wrong_input_total: 100000
```

### Case 7: ordinary pool or eligible 108% investment election

Assume a factory-new, wholly business, own-use machine with a verified cash-value tax basis of **100,000**, delivered ready for an operating business in 2026. It is not a car, ship, software, fossil-powered asset, special § 5 C asset or rental asset; no immediate-expensing claim is made. The relevant opening pools and disposal proceeds are zero. The accounts' profit before tax is **1,000,000**, including **10,000** of book depreciation on this machine; all other book/tax items match.

Under the ordinary § 5 pool at the elected maximum 25%, tax depreciation = 100,000 × 25% = **25,000**. Closing pool = **75,000**. Taxable amount = 1,000,000 + 10,000 − 25,000 = **985,000**, already a multiple of DKK 100. Tax = 985,000 × 22% = **216,700**.

Under an eligible § 5 E election, separate tax basis = 100,000 × 108% = **108,000**. Maximum annual depreciation = 108,000 × 25% = **27,000**; closing enhanced pool = **81,000**. Taxable amount = 1,000,000 + 10,000 − 27,000 = **983,000**. Tax = **216,260**. The fictional current-year tax reduction is **440**. This compares 2 lawful stated alternatives under stipulated eligibility; it does not establish that an actual asset qualifies or that maximum depreciation is always the best choice. Record the chosen election and carry the correct separate pool into future years. Sources: S1 §§ 17 and 22; S15 §§ 3, 5 and 5 E; S18.

```oa-check
name: Case 7; ordinary versus eligible enhanced equipment basis
inputs:
  accounting_profit: 1000000
  book_depreciation: 10000
  basis: 100000
steps:
  - ordinary_depreciation: basis * 0.25
  - ordinary_closing_pool: basis - ordinary_depreciation
  - ordinary_taxable: floor((accounting_profit + book_depreciation - ordinary_depreciation) / 100) * 100
  - ordinary_tax: ordinary_taxable * 0.22
  - enhanced_basis: basis * 1.08
  - enhanced_depreciation: enhanced_basis * 0.25
  - enhanced_closing_pool: enhanced_basis - enhanced_depreciation
  - enhanced_taxable: floor((accounting_profit + book_depreciation - enhanced_depreciation) / 100) * 100
  - enhanced_tax: enhanced_taxable * 0.22
  - current_year_tax_difference: ordinary_tax - enhanced_tax
expected:
  ordinary_depreciation: 25000
  ordinary_closing_pool: 75000
  ordinary_taxable: 985000
  ordinary_tax: 216700
  enhanced_basis: 108000
  enhanced_depreciation: 27000
  enhanced_closing_pool: 81000
  enhanced_taxable: 983000
  enhanced_tax: 216260
  current_year_tax_difference: 440
```

### Case 8: foreign credit uses net income and both limits

A supported ordinary LL § 33 claim has foreign gross income 100,000 and properly allocated § 33 F expenses 30,000. Total Danish-taxed income is 1,000,000 after those expenses, with no losses or other relief. Foreign tax paid is 20,000. For this fictional case only, a separately established treaty entitlement limits the creditable foreign tax to 18,000; this is an assumed input, not a rate attributed to any treaty. Danish tax before credit is 220,000. Foreign net income is 70,000, so the attributable Danish tax is 220,000 × 70,000 / 1,000,000 = **15,400**. The credit is min(20,000, 18,000, 15,400) = **15,400**, leaving **204,600** Danish tax before advances and settlement adjustments. Do not credit the excess foreign withholding or infer an excess-credit carryforward. Actual treaty, income-source, expense, paid-tax and filing evidence remain required. Sources: S30 §§ 33 and 33 F, S1 §§ 17 and 22.

```oa-check
name: Case 8; net foreign-income cap and stipulated treaty limit
inputs:
  foreign_gross: 100000
  foreign_expenses: 30000
  total_taxable: 1000000
  foreign_tax_paid: 20000
  treaty_entitlement: 18000
steps:
  - foreign_net: foreign_gross - foreign_expenses
  - tax_before_credit: total_taxable * 0.22
  - danish_foreign_cap: tax_before_credit * foreign_net / total_taxable
  - allowed_credit: min(foreign_tax_paid, treaty_entitlement, danish_foreign_cap)
  - tax_after_credit: tax_before_credit - allowed_credit
expected:
  foreign_net: 70000
  tax_before_credit: 220000
  danish_foreign_cap: 15400
  allowed_credit: 15400
  tax_after_credit: 204600
```

### Case 9: current group loss and protected pre-joining loss

A, B and C are qualifying ordinary Danish group companies in uninterrupted national joint taxation for all of 2026, with A as administration company and no applicable restructuring, CFC, foreign, financing or other special adjustment. Established current income before loss relief is A +1,500,000, B −500,000 and C zero. C alone has an eligible pre-joining loss of 200,000 and no own profit against which to use it. There are no other carried losses. B’s current loss offsets 500,000 of A’s income, giving group income **1,000,000** and ordinary group tax **220,000**. C’s **200,000** pre-joining loss remains unused; it cannot reduce A’s profit. The brought-forward-loss cap has no deduction to restrict in this stipulated case. The § 31(8) compensation value for B’s utilised loss is 500,000 × 22% = **110,000**, subject to the statutory obligations and payment route. This is not a final tax-account, liability-allocation or bank-payment reconciliation. Sources: S1 §§ 12, 17, 22, 31 and 31 C, read with S4.

```oa-check
name: Case 9; current group loss does not release pre-joining losses
inputs:
  a_income: 1500000
  b_income: -500000
  c_income: 0
  c_prejoin_loss: 200000
steps:
  - c_own_loss_used: min(c_prejoin_loss, max(c_income, 0))
  - group_income: a_income + b_income + c_income - c_own_loss_used
  - group_tax: group_income * 0.22
  - c_closing_prejoin_loss: c_prejoin_loss - c_own_loss_used
  - b_loss_compensation: 500000 * 0.22
expected:
  c_own_loss_used: 0
  group_income: 1000000
  group_tax: 220000
  c_closing_prejoin_loss: 200000
  b_loss_compensation: 110000
```

### Case 10: R&D enhancement is excluded from the cash-credit base

A standalone ordinary company has no income before eligible immediately expensed LL § 8 B R&D costs of 1,000,000. Its 12-month year is 2026; there are no other adjustments, prior losses, joint-tax members or commonly controlled applicants sharing the cash-credit cap. Eligibility and timing are expressly stipulated, not inferred from the cost label. All expenditure is within the relevant enhancement ceiling. The enhanced deduction is 1,000,000 × 114% = **1,140,000**, producing a current tax loss of **1,140,000**. The **140,000** enhancement does not qualify for cash credit. The supported base is the actual-cost loss of **1,000,000**, giving gross credit **220,000** at 22%, below the full-year cap. Requesting that credit reduces the loss by 1,000,000, leaving **140,000** to carry, subject to the ordinary loss rules. No cash credit and carryforward are claimed for the same 1,000,000. The gross credit is not a verified payout; actual claim, offsets and payment remain held. Sources: S30 §§ 8 B and 8 X with official notes 4–6, S32 §§ 1–2 and 4, S33 §§ 5 and 9, S34 and S35.

```oa-check
name: Case 10; R&D enhancement, cash-credit base and remaining loss
inputs:
  eligible_cost: 1000000
  income_before_rd: 0
  full_year_credit_cap: 25000000
steps:
  - enhanced_deduction: eligible_cost * 1.14
  - enhancement: enhanced_deduction - eligible_cost
  - current_loss: max(enhanced_deduction - income_before_rd, 0)
  - cash_credit_base: min(eligible_cost, current_loss, full_year_credit_cap)
  - gross_cash_credit: cash_credit_base * 0.22
  - closing_loss: current_loss - cash_credit_base
expected:
  enhanced_deduction: 1140000
  enhancement: 140000
  current_loss: 1140000
  cash_credit_base: 1000000
  gross_cash_credit: 220000
  closing_loss: 140000
```

### Case 11: positive, zero and negative aggregate group income

A and B are qualifying companies in uninterrupted domestic joint taxation for all of 2026. Their current-year incomes before using brought-forward losses are stipulated below. A has eligible own brought-forward losses of 30,000,000; all other restrictions are absent. Establish the aggregate current-year sign before applying the § 31(3) condition. A’s positive income alone does not trigger a group restriction. [S1, § 31(2)–(3)](https://www.retsinformation.dk/eli/lta/2025/279)

| Profile | A current income | B current income | Aggregate current income | Apply the § 12(2) group restriction? |
| --- | --- | --- | --- | --- |
| Positive | 30,000,000 | 0 | 30,000,000 | Yes, once for the group, with the statutory proportional allocation. |
| Zero | 30,000,000 | −30,000,000 | 0 | No. Preserve the § 31(2) loss order and each loss owner’s closing balances. |
| Negative | 30,000,000 | −31,000,000 | −1,000,000 | No. Preserve the § 31(2) loss order and each loss owner’s closing balances. |

This is an applicability screen, not a final group tax or settlement calculation. The executable block checks the 3 aggregate amounts; the yes/no rule is the express condition in § 31(3).

```oa-check
name: Case 11; current-year aggregate sign before group loss restriction
inputs:
  a_income: 30000000
  b_positive: 0
  b_zero: -30000000
  b_negative: -31000000
steps:
  - aggregate_positive: a_income + b_positive
  - aggregate_zero: a_income + b_zero
  - aggregate_negative: a_income + b_negative
expected:
  aggregate_positive: 30000000
  aggregate_zero: 0
  aggregate_negative: -1000000
```

### Case 12: proportional carried-loss allocation and company vintages

A, B and C have qualifying uninterrupted national joint taxation throughout all relevant loss years and 2026. In 2026 A has positive income of 300,000 and B and C each have zero current income. A has no own losses. B has eligible joint-tax carried losses of 50,000 from 2024 and 150,000 from 2025; C has 300,000 from 2024 and 100,000 from 2025. There are no current-year group losses, pre-joining losses or other restrictions. The aggregate income is positive but below the 2026 threshold, so the § 12(2) ceiling adds no restriction.

Eligible other-member carried losses total 600,000. Allocate A’s 300,000 capacity proportionately: B uses **100,000** and C uses **200,000**. Within B, use all 50,000 from 2024 and 50,000 from 2025; B carries 100,000 from 2025. Within C, use 200,000 from 2024; C carries 100,000 from 2024 and 100,000 from 2025. Closing carried losses total **300,000**, equal to 600,000 opening less 300,000 used. A’s remaining taxable income is zero. Do not use B’s full 200,000 or exhaust every 2024 loss across the group before respecting the proportional allocation. Tax-value compensation and actual payment/filing remain separate. [S1, § 31(2)–(3)](https://www.retsinformation.dk/eli/lta/2025/279)

```oa-check
name: Case 12; proportional group carried losses and oldest first within each company
inputs:
  a_income: 300000
  b_2024: 50000
  b_2025: 150000
  c_2024: 300000
  c_2025: 100000
steps:
  - b_open: b_2024 + b_2025
  - c_open: c_2024 + c_2025
  - total_open: b_open + c_open
  - b_used: a_income * b_open / total_open
  - c_used: a_income * c_open / total_open
  - b_old_used: min(b_2024, b_used)
  - b_new_used: b_used - b_old_used
  - c_old_used: min(c_2024, c_used)
  - c_new_used: c_used - c_old_used
  - b_2024_closing: b_2024 - b_old_used
  - b_2025_closing: b_2025 - b_new_used
  - c_2024_closing: c_2024 - c_old_used
  - c_2025_closing: c_2025 - c_new_used
  - total_closing: b_2024_closing + b_2025_closing + c_2024_closing + c_2025_closing
  - group_taxable: a_income - b_used - c_used
expected:
  total_open: 600000
  b_used: 100000
  c_used: 200000
  b_2024_closing: 0
  b_2025_closing: 100000
  c_2024_closing: 100000
  c_2025_closing: 100000
  total_closing: 300000
  group_taxable: 0
```

### Case 13: calendar-year collection interest excludes accrued interest

Stipulate 20 interest days wholly within calendar year 2026, an established constant ordinary principal of DKK 10,000 and already-due eligible fees of DKK 160. Already accrued interest of DKK 200 is also outstanding. There are no fines, customs claims, other balances, payments, credits, relief, cessation or balance changes. The actual due date, fee assessment and interest-day count have already been established for this fictional case; no real deadline or taxpayer position is inferred.

The outstanding balance before new interest is DKK 10,360, but the interest base is **DKK 10,160**, excluding the DKK 200 accrued interest. At 0.95% per month, the unrounded mathematical amount for 20 days is 10,160 × 0.0095 × 12/365 × 20 = **DKK 63.465205479…**, or **DKK 63.47** using illustrative aggregate rounding to 2 decimals. As a method cross-check, the authority’s principal-only DKK 10,000 / 20-day example gives DKK 62.47. These illustrative results do not establish actual daily or monthly posting precision, the amount posted to a real account or a 2027 rate. Monthly posting may require a separate rounding reconciliation. SEL § 22 taxable-income rounding does not govern this interest illustration. [S44, § 16 C](https://www.retsinformation.dk/eli/lta/2024/1040) [S5, § 2](https://www.retsinformation.dk/eli/lta/2025/1783) [S45](https://www.retsinformation.dk/eli/lta/2025/1793) [S51](https://info.skat.dk/data.aspx?oid=2459995) [S50](https://info.skat.dk/data.aspx?oid=2290071)

```oa-check
name: Case 13; ordinary 2026 collection interest without interest on interest
inputs:
  principal: 10000
  eligible_fees: 160
  old_interest: 200
  base_monthly_rate: 0.001
  supplement: 0.0085
  days: 20
  year_days: 365
steps:
  - balance_before: principal + eligible_fees + old_interest
  - eligible_base: balance_before - old_interest
  - monthly_rate: base_monthly_rate + supplement
  - raw_interest: eligible_base * monthly_rate * 12 / year_days * days
  - illustrative_interest: round(raw_interest, 2)
  - principal_only_cross_check: round(principal * monthly_rate * 12 / year_days * days, 2)
expected:
  balance_before: 10360
  eligible_base: 10160
  monthly_rate: 0.0095
  illustrative_interest: 63.47
  principal_only_cross_check: 62.47
```

## When to refuse or refer

Apply every universal and corporate-base refusal, with its loaded trigger and verbatim message. Retain a trace for all loaded codes. A source missing from this draft is not evidence that Danish law is absent.

The following additional country catalogue is defined here; use the message exactly:

| Code | Trigger | Verbatim message |
| --- | --- | --- |
| R-DK-CIT-SOURCE | An applicable operative statute, amendment, commencement, order, election condition, method or mandatory companion remains unresolved before actual classification, computation or output preparation | The applicable Danish corporate tax rule or required companion has not been established. Stop the affected work and obtain the complete operative authority before preparing a tax position or output. Refer the matter to a qualified Danish professional. |
| R-DK-CIT-SETTLEMENT | Actual settlement needs an unpublished or unqualified percentage, interest basis, tax-account allocation or actual assessment detail | The Danish corporate tax settlement cannot be established from the verified sources and records. Do not issue a final payable or refundable amount. Obtain the missing rate, rule, assessment or allocation evidence and refer the settlement to a qualified Danish professional. |

Missing user-answerable facts require Needs Input under the bases. A fired refusal is not cured by a disclaimer, numerical conservatism, materiality threshold or professional signature alone.

## Filing and payment

The reviewer controls access, submission, authorisation and payment. Never request or process credentials, tax identifiers, bank details or client personal identifiers.

1. Confirm the actual registered income year, deadline, group status and required return version in DIAS. Apply the statutory filing and tax-base rounding rules and resolve applicable source holds first.
2. Reconcile return fields and schedules to the recalculated working paper, including income, losses, credits and assessed advances. Obtain reviewer decisions on every unresolved fact before final outputs.
3. Follow the authority's submission sequence and retain the acknowledgement and submitted copy. A stored draft is not a receipt. No live return was tested in this research.
4. Reconcile ordinary advances to their assessment. For voluntary increases, the authority requires declaration before payment and warns of refunds if the declaration is missing. Changes use a delta; do not enter the intended new total into the change field. Special restrictions apply after reducing an ordinary instalment. [S8](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/betal-acontoskat-og-selskabsskat)
5. Keep assessed amounts, payments, statutory credits and tax-account postings separate. SEL § 29 B includes assessed advances in residual/excess tax whether or not paid. Any unpaid advance remains a separate balance; subtracting cash paid alone cannot reproduce that statutory computation. [S1, § 29 B(4)–(5)](https://www.retsinformation.dk/eli/lta/2025/279)
6. Recheck the official 2026 percentages when published. SEL § 29 B(12) calls for publication by 15 December of the income year. The ministry's table read on 2 November still left them to later determination. A 2025 worked example on the practical guidance is not a 2026 percentage.
7. The authority describes the ordinary assessment in October of the following year and ordinary residual payment by 20 November, adjusted to the next weekday where required. Reconcile the actual notice and qualified § 30 chain before an engagement deadline or interest calculation. Use S5–S6 with the qualified S45 commencement order and selected OPKL chain above. Establish the rate for the actual payment calendar year, including 2027 where applicable. Do not use the unamended S1 § 30 as current procedure.
8. Preserve the tax account, acknowledgement, assessment, payment allocation and later amendments in the reviewer-held evidence index. No actual filing or payment is authorised by this reference.

## Completion checklist

- Confirm all 26 base intake fields and Danish additions; keep identifiers outside agent inputs.
- Verify entity, residence, period and all applicable source/commencement chains.
- Run all loaded refusal catalogues and include every code in the trace.
- Clear source holds before actual classification, computation and output preparation.
- Reconcile accounts, every source row and each adjustment once.
- Confirm 22% applies to the established ordinary entity and period.
- Use the 2026 indexed loss threshold, establish eligible losses and check restrictions/group rules.
- Apply credits at their lawful stage once; reconcile assessed advances and cash separately.
- Keep unknown percentages, interest and allocation unresolved rather than zero.
- Complete the GloBE and cross-border screens with current country sources.
- Recalculate every workbook formula, compare totals across all deliverables and run every universal/domain self-check.
- Preserve all universal and domain outputs, or record the refusal before preparing them.
- Obtain the Danish professional's recorded sign-off after evidence gaps are resolved; the examples and future project checks cannot supply professional acceptance.
- Complete canonical-template, project/example and generated-artifact checks before any integration.

### Version and currency

Version 0.4, 2 November 2026: adds the selected operative 2026 tax-account interest, allocation and commencement chain, source-currency conflicts and a constant-balance illustration. Actual allocation, posting precision, complete procedures, 2027 rates and settlement remain held. Version 0.3, 2 November 2026: repairs the positive aggregate-income condition and proportional carried-loss allocation, with sign and company-vintage examples. Version 0.2, 2 November 2026: adds selected domestic group/loss, participation, foreign-credit, transfer-pricing, CFC and R&D principles, operative-date qualifications and fictional examples. It retains all applicable-source, specialist, procedure, settlement, portal, filing and professional holds. Complete workflows beyond the selected rules remain required; this reference does not establish comprehensive Danish coverage. Version 0.1 supplied the ordinary equipment, finance, filing, late-information charge and SEL § 22 foundation. No predecessor Danish corporate guide was changed.

## Sources

Read on 2 November 2026 unless otherwise stated. The source reading is limited to the identified units or sections. Retaining a complete page does not mean every part was read.

| ID | Primary source | Reading extent and limitation | Read on |
| --- | --- | --- | --- |
| S1 | [Selskabsskatteloven, LBK nr 279 af 13/03/2025](https://www.retsinformation.dk/eli/lta/2025/279) | Page metadata and later-amendment list; complete § 1 introduction/item 1 and § 1(6), §§ 8, 10, 11, 11 B, 11 C, 12, 12 A, 12 D, 13, 17, 22, 29 A, 29 B, 30, 31, 31 C, 31 D and 32, including official transitional note 3. Section 30 requires S5–S6 and related procedural reconstruction before use. Other retained units are unqualified. | 2026-11-02 |
| S2 | [LOV nr 562 af 27/05/2025](https://www.retsinformation.dk/eli/lta/2025/562) | Complete § 11 and commencement § 17. | 2026-11-02 |
| S3 | [LOV nr 750 af 20/06/2025](https://www.retsinformation.dk/eli/lta/2025/750) | Complete § 2 and commencement § 7. | 2026-11-02 |
| S4 | [LOV nr 1755 af 29/12/2025](https://www.retsinformation.dk/eli/lta/2025/1755) | Complete SEL amendment § 5, actual commencement § 8 and territorial § 9; LL amendment § 4 also read. | 2026-11-02 |
| S5 | [LOV nr 1783 af 29/12/2025](https://www.retsinformation.dk/eli/lta/2025/1783) | Complete §§ 2, 3, 5 and 6, including repeal of the old OPKL amendments and the order-linked transition. Read with S45; actual procedures remain held. | 2026-11-02 |
| S6 | [LOV nr 763 af 08/09/2026](https://www.retsinformation.dk/eli/lta/2026/763) | Complete OPKL amendment § 1, LL amendment § 2, SEL amendment § 4 and commencement § 8. | 2026-11-02 |
| S7 | [Ministry, Selskabsskatteloven rates and thresholds](https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven) | Main table dated 1 September 2026, separate 2026/2027 columns. Uses the 2026 loss threshold. Relevant 2026 supplement/compensation percentages still to be determined. | 2026-11-02 |
| S8 | [Skattestyrelsen, Betal acontoskat og selskabsskat](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/betal-acontoskat-og-selskabsskat) | Main practical guidance and payment/change instructions; examples explicitly for 2025 are not adopted for 2026. No live portal test. | 2026-11-02 |
| S9 | [Skattestyrelsen, Oplysningsskemaet for selskaber og fonde](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/oplysningsskemaet-for-selskaber-og-fonde) | Main filing, basic-registration, draft/submission, correction and inactive-company instructions. Linked PDF manuals not read; governing selected statutory filing/charge units are qualified separately in S19–S29. | 2026-11-02 |
| S10 | [Den juridiske vejledning 2026-2, C.D.2.4.5.3](https://info.skat.dk/data.aspx?oid=2049731) | General loss-carryforward and selected group/order discussion. Historical 2025 and older examples not used as 2026 thresholds or rates. Full case-law table not reviewed. | 2026-11-02 |
| S11 | [Den juridiske vejledning 2026-2, C.D.2.4.1](https://info.skat.dk/data.aspx?oid=2049133) | Main taxable-income principles, separate gain Acts, related-party treatment and separate company entities. | 2026-11-02 |
| S12 | [Den juridiske vejledning 2026-2, C.C.2.2.1.2](https://info.skat.dk/data.aspx?oid=2083469) | Main operating-expense principles selected, including business connection, incurred costs and private/capital/establishment boundaries. Full case-law table not read. | 2026-11-02 |
| S13 | [Skattestyrelsen, Global minimumsskat for store koncerner](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/global-minimumsskat-for-store-koncerner-globe) | Opening scope and reporting introduction. Underlying Minimumsbeskatningsloven and complete IIR/QDMTT/UTPR commencement rules not qualified. | 2026-11-02 |
| S14 | [Skattestyrelsen, Indberet selskabsskat](https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/indberet-selskabsskat) | Opening and selected registration/year-change instructions only. Historical FAQ dates do not establish a 2026 deadline. | 2026-11-02 |
| S15 | [Afskrivningsloven, LBK 1222 of 13 October 2025](https://www.retsinformation.dk/eli/lta/2025/1222) | Metadata; complete §§ 1–6, including §§ 5 A–5 E, and §§ 8, 45, 47 and 50. Other asset units remain unqualified. | 2026-11-02 |
| S16 | [LOV 749 of 20 June 2025](https://www.retsinformation.dk/eli/lta/2025/749) | Complete LL amendment § 1, AL amendment § 2, OPKL amendment § 3 and commencement § 5. Other amended-law provisions are unqualified. | 2026-11-02 |
| S17 | [LOV 615 of 30 June 2026](https://www.retsinformation.dk/eli/lta/2026/615) | Complete AL amendment § 3 and commencement/application § 16; LL amendment § 10 also read. One initial loading-shell result was replaced by a successful rendering retry. | 2026-11-02 |
| S18 | [Ministry, Afskrivningsloven rates](https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/afskrivningsloven) | Main 2026/2027 table dated 26 August 2026; 2026 column used. A rate table does not establish asset eligibility. | 2026-11-02 |
| S19 | [Skattekontrolloven, LBK 12 of 8 January 2024](https://www.retsinformation.dk/eli/lta/2024/12) | Metadata and complete §§ 2, 5, 12–14 and 73; later-amendment corporate units in S20–S29 checked. The unamended § 73 figures are superseded. | 2026-11-02 |
| S20 | [LOV 16 of 14 January 2025](https://www.retsinformation.dk/eli/lta/2025/16) | Complete OPKL amendment § 1, SKL amendment § 2 and commencement § 4; raises ordinary late-information charge to DKK 400/day, cap DKK 10,000. | 2026-11-02 |
| S21 | [LOV 482 of 22 May 2024](https://www.retsinformation.dk/eli/lta/2024/482) | Complete SKL § 9 and commencement § 10; changes § 73(2) terminology, not ordinary corporate § 73(1). | 2026-11-02 |
| S22 | [LOV 1214 of 26 November 2024](https://www.retsinformation.dk/eli/lta/2024/1214) | Complete SKL § 3 and commencement § 5; changes § 8 property terminology. | 2026-11-02 |
| S23 | [LOV 1473 of 10 December 2024](https://www.retsinformation.dk/eli/lta/2024/1473) | Complete SKL amendment § 3, OPKL amendment § 5 and commencement § 19; changes control provisions and repeals SKL §§ 75–81. | 2026-11-02 |
| S24 | [LOV 1454 of 10 December 2024](https://www.retsinformation.dk/eli/lta/2024/1454) | Complete SKL amendment § 11 and commencement § 9; repeals § 88(2). Its headings include text on the same line; bare-section extraction initially missed it and was corrected. | 2026-11-02 |
| S25 | [LOV 96 of 4 February 2025](https://www.retsinformation.dk/eli/lta/2025/96) | Complete SKL § 5 and commencement § 7; changes § 73(2) personal-tax terminology. | 2026-11-02 |
| S26 | [LOV 409 of 29 April 2025](https://www.retsinformation.dk/eli/lta/2025/409) | Complete SKL § 2 and commencement § 5, read subject to S28 repeal of specified amendments before their effect. | 2026-11-02 |
| S27 | [LOV 750 of 20 June 2025](https://www.retsinformation.dk/eli/lta/2025/750) | Complete SKL § 3 and commencement § 7. Changes selected reporting and transfer-pricing documentation provisions; those specialist workflows are not fully qualified. | 2026-11-02 |
| S28 | [LOV 1643 of 16 December 2025](https://www.retsinformation.dk/eli/lta/2025/1643) | Complete SKL § 2, amendment to LOV 409 in § 4 and commencement § 5. Other GloBE amendments are not qualified by this selected reading. | 2026-11-02 |
| S29 | [LOV 1784 of 29 December 2025](https://www.retsinformation.dk/eli/lta/2025/1784) | Complete SKL § 4 and commencement § 5; specified lender reporting changes apply from 1 July 2026. | 2026-11-02 |

| S30 | [Ligningsloven, LBK 1500 of 24 November 2025](https://www.retsinformation.dk/eli/lta/2025/1500) | Metadata; complete §§ 2, 3, 8 B, 8 X, 33, 33 F and 33 H, plus official notes 4–6. Printed future § 8 X wording is read with S33. Listed later LL amending units in S4, S6, S16–S17 and S36–S43 do not directly edit these selected sections; linked secondary and specialist rules still require qualification. | 2026-11-02 |
| S31 | [Aktieavancebeskatningsloven, LBK 849 of 21 September 2026](https://www.retsinformation.dk/eli/lta/2026/849) | Metadata; complete §§ 4 A, 4 B, 4 C, 8 and 9 and official notes. The future-text note concerns § 34 from 2027. Other special-class and timing units remain unqualified. | 2026-11-02 |
| S32 | [LOV 1472 of 10 December 2024](https://www.retsinformation.dk/eli/lta/2024/1472) | Complete §§ 1, 2 and 4: AL and LL R&D enhancement amendments, commencement and specified asset transitional provisions. | 2026-11-02 |
| S33 | [LOV 1691 of 30 December 2024](https://www.retsinformation.dk/eli/lta/2024/1691) | Complete §§ 5 and 9, including § 9(6), which defers the § 8 X cap and payment cross-reference changes to income year 2027. Other amended-law units are not qualified. | 2026-11-02 |
| S34 | [Den juridiske vejledning 2026-2, C.C.2.2.2.20](https://info.skat.dk/data.aspx?oid=2083520) | Selected eligibility, costs and deduction-method sections; 2026 enhancement, cash-credit cap, claim, loss adjustment and offset sections. Full group-allocation discussion, case-law table, underlying cases and separate collection law not read. | 2026-11-02 |
| S35 | [Ministry, Ligningsloven rates and thresholds](https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/ligningsloven) | Table dated 1 September 2026, year header and relevant R&D ceiling, credit-cap and percentage rows. The 2026 above-ceiling cell is a dash; S32 and S34 supply the explicit enacted 110% rule. | 2026-11-02 |
| S36 | [LOV 2025/198 selected LL amendment](https://www.retsinformation.dk/eli/lta/2025/198) | Complete selected LL amending § 3 read. It does not directly amend the selected S30 sections; its other provisions, commencement and linked regimes are not fully qualified by this limited reading. | 2026-11-02 |
| S37 | [LOV 2025/1630 selected LL amendment](https://www.retsinformation.dk/eli/lta/2025/1630) | Complete selected LL amending § 2 read. It does not directly amend the selected S30 sections; its other provisions, commencement and linked regimes are not fully qualified by this limited reading. | 2026-11-02 |
| S38 | [LOV 2025/1642 selected LL and OPKL amendments](https://www.retsinformation.dk/eli/lta/2025/1642) | Complete selected LL amending § 2, OPKL amending § 4 and commencement § 10 read. The LL target does not directly amend the selected S30 sections. Other provisions and linked regimes remain unqualified. | 2026-11-02 |
| S39 | [LOV 2025/1775 selected LL amendment](https://www.retsinformation.dk/eli/lta/2025/1775) | Complete selected LL amending § 2 read. It does not directly amend the selected S30 sections; its other provisions, commencement and linked regimes are not fully qualified by this limited reading. | 2026-11-02 |
| S40 | [LOV 2025/1781 selected LL amendment](https://www.retsinformation.dk/eli/lta/2025/1781) | Complete selected LL amending § 1 read. It does not directly amend the selected S30 sections; its other provisions, commencement and linked regimes are not fully qualified by this limited reading. | 2026-11-02 |
| S41 | [LOV 2026/616 selected LL amendment](https://www.retsinformation.dk/eli/lta/2026/616) | Complete selected LL amending § 1 read. It does not directly amend the selected S30 sections; its other provisions, commencement and linked regimes are not fully qualified by this limited reading. | 2026-11-02 |
| S42 | [LOV 2026/722 selected LL amendment](https://www.retsinformation.dk/eli/lta/2026/722) | Complete selected LL amending § 18 read. It does not directly amend the selected S30 sections; its other provisions, commencement and linked regimes are not fully qualified by this limited reading. | 2026-11-02 |
| S43 | [LOV 2026/729 selected LL amendment](https://www.retsinformation.dk/eli/lta/2026/729) | Complete selected LL amending § 11 read. It does not directly amend the selected S30 sections; its other provisions, commencement and linked regimes are not fully qualified by this limited reading. | 2026-11-02 |
| S44 | [Opkrævningsloven, LBK 1040 of 13 September 2024](https://www.retsinformation.dk/eli/lta/2024/1040) | Metadata, later-amendment list and complete §§ 1, 7 and 16–16 C read. Apply the selected later-amendment chain, not the consolidation alone. Full collection, refund, remission and enforcement workflows remain unqualified. | 2026-11-02 |
| S45 | [BEK 1793 of 29 December 2025](https://www.retsinformation.dk/eli/lta/2025/1793) | Complete identity and §§ 1–3; starts the identified OPKL rate, base and fines-exception amendments on 1 January 2026. | 2026-11-02 |
| S46 | [LOV 1694 of 30 December 2024](https://www.retsinformation.dk/eli/lta/2024/1694) | Complete outer OPKL amending § 1, nos 1–21 and commencement § 18. Read with S5 § 5, which repeals nos 15/18 before effect and changes the deferred list. Other amended laws remain unqualified. | 2026-11-02 |
| S47 | [LOV 620 of 11 June 2024](https://www.retsinformation.dk/eli/lta/2024/620) | Complete OPKL amending § 18 and commencement § 17; passenger-levy annex change. Other laws remain unqualified. | 2026-11-02 |
| S48 | [LOV 683 of 11 June 2024](https://www.retsinformation.dk/eli/lta/2024/683) | Complete OPKL amending § 5 and commencement § 9; emissions-levy annex change. Other laws remain unqualified. | 2026-11-02 |
| S49 | [LOV 1648 of 16 December 2025](https://www.retsinformation.dk/eli/lta/2025/1648) | Complete OPKL amending § 22 and commencement § 25; registration-related § 16 G. Other laws and that separate procedure remain unqualified. | 2026-11-02 |
| S50 | [Den juridiske vejledning 2026-2, A.D.8.1](https://info.skat.dk/data.aspx?oid=2290071) | Selected applicability, fee, interest, daily-conversion and exception sections, including the DKK 10,000 / 20-day example. The DKK 65 fee and LOV 1694 no. 15 cross-reference are stale against S6/S5; use the operative law. | 2026-11-02 |
| S51 | [SKM2025.720.SKTST, 2026 OPKL base rate](https://info.skat.dk/data.aspx?oid=2459995) | Complete notice, published 12 December 2025: 0.1% from 1 January 2026. Does not establish 2027 rates or annual corporate settlement percentages. | 2026-11-02 |
| S52 | [Den juridiske vejledning 2026-2, A.B.4.5.3](https://info.skat.dk/data.aspx?oid=2168702) | Selected current tax-account interest and historical back-charging discussion. Underlying historical decisions were not independently read or adopted. | 2026-11-02 |

Not yet confirmed: complete applicable special depreciation, interest definitions, share-class/timing and withholding interactions, full credit/group/anti-abuse and Pillar Two workflows; annual reporting/audit requirements; complete collection/refund/remission/enforcement procedures, actual daily balance and posting precision, 2027 collection rate; actual DIAS operation, assessment/allocation, R&D cash-credit procedures and professional acceptance. The selected participation, group, CFC, foreign-credit and R&D provisions above have been read; their unqualified dependencies and actual-use gates remain.

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
