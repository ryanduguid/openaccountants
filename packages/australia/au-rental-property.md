---
name: au-rental-property
description: Use this skill whenever asked about Australian rental property income and deductions. Trigger on phrases like "rental income Australia", "negative gearing", "rental deductions", "investment property tax", "Division 40", "Division 43", "capital works deduction", "depreciation schedule", "rental property CGT", "rental withholding", "body corporate fees", "strata levy deduction", "repairs vs improvements", "TR 97/23", "GST on property", "land tax on an investment property", "stamp duty on a rental", or any question about completing the rental property schedule in an Australian individual tax return. This skill covers rental income reporting, deductible expenses, depreciation (Div 40 plant and Div 43 building), negative gearing including the enacted 1 July 2027 limit, CGT on disposal, foreign resident withholding, the GST decision path, the state and territory taxes that attach to property, and common transaction classifications. ALWAYS read this skill before touching any Australian rental property work.
version: 1.9
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27; myTax 2026 instructions cover 2025-26; enacted 2027-28 provisions separately labelled"
last_updated: 2026-11-04
review_status: pending_review
category: international
tier: 2
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Rental Property v1.9

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare Australian rental income, expense, capital-allowance and disposal working papers for a qualified reviewer. The principal period is **2026-27**, 1 July 2026 to 30 June 2027. The ATO's Rental properties guide 2026 and myTax 2026 instructions instead concern **2025-26**. Later return fields must be checked when published. This is a Tier 2 source-cited draft, not approval for a taxpayer's return.

Use this guide with `workflow-base` and the relevant individual, company, trust or SMSF guide. Its ordinary rental examples concern individuals who are not carrying on a rental business. Commercial property, GST, state taxes, foreign residence, estates and development require the linked specialist guides and their own evidence. Do not apply an individual's rental schedule or rate table to another entity.

## Ask the client first

- Who owns each legal interest, in what proportions, through which entity and with what tax residence history? Is this an investment or a rental business?
- Which income year is being prepared? Obtain acquisition, contract, settlement, construction, first-use and disposal dates, including the history needed for the 2017 and 2027 changes.
- For each part of the property, when was it rented, genuinely available, occupied privately or offered to relatives? Obtain floor areas, rent terms, advertising and booking evidence; identify holiday or leisure use.
- What do the agent statements, bank records and itemised invoices show? Trace every borrowing, redraw, repayment and offset balance to its actual use, separately from the property's security.
- Which assets were new or previously used, when were they acquired and first used, and what construction cost, effective life, method, pool and previous deductions are evidenced?
- Is there a sale, development, main-residence claim, estate or relationship transfer, GST issue or state-tax exposure? Which elections, certificates, exceptions, source conditions and deadlines remain unresolved?

## The method, step by step

### Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax | Income Tax -- Rental Property Schedule |
| Currency | AUD only |
| Tax year | 2026-27 (1 July 2026 to 30 June 2027); 2025-26 filing instructions are separately labelled |
| Primary legislation | Income Tax Assessment Act 1997 (ITAA 1997) |
| Supporting legislation | ITAA 1936; TR 97/23 (repairs vs improvements); TR 2026/1 (rental income and deductions for individuals not in business); PCG 2026/2 (apportionment); PCG 2026/3 (holiday homes and section 26-50); [ATO, Rental properties guide 2026](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026) |
| Tax authority | Australian Taxation Office (ATO) |
| Filing portal | myTax / tax agent lodgement (Online Services for Agents) |
| Filing deadline | 31 October (self-lodgement); agent-managed deadlines vary |
| Skill version | 1.9 |

#### Select the income year before calculating

Ask which income year is being prepared before calculating anything. For resident bands and the tax-free threshold, use the period owner [Australian rates 2026-27](au-rates-2026-27.md), with its official sources and prior-year boundaries. Use [Medicare levy and surcharge](au-medicare-levy.md) for that year's amounts, tier tests and family adjustments. A rental result alone is not a complete personal tax calculation.

Check the law and the asset's history for the requested period. An editing date does not establish the operative law. The 2017 asset/travel restrictions, construction dates, transitional rules, residence history and enacted 2027-28 changes can alter the result.

#### Key Thresholds (2026-27)

**Key Thresholds (2026-27)**

| Item | Amount and conditions | Official source |
| --- | --- | --- |
| Resident individual rates and tax-free threshold | Use [Australian rates 2026-27](au-rates-2026-27.md) for a full-year resident entitled to the full threshold; use the residence-specific guide otherwise | https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents |
| Medicare levy | Use [Medicare levy and surcharge](au-medicare-levy.md), including reductions and exemptions. A rental result alone does not determine the levy | https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents |
| Medicare levy surcharge | Use [Medicare levy and surcharge](au-medicare-levy.md) for amounts, tiers and dependent-child adjustments. Test appropriate hospital cover, MLS income and family conditions. Net investment losses are added back in MLS income: a rental loss does not automatically remove MLS | https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates |
| Individual/trust CGT discount | Use [Capital gains](au-capital-gains.md) and [Non-resident CGT](au-nonresident-cgt.md) for the rate and holding-period tests. Foreign residence and the enacted dwelling rules can restrict entitlement; companies do not receive the individual/trust discount | https://www.legislation.gov.au/C2004A05138/latest/text , Division 115 |
| Ordinary post-15 September 1987 residential capital works | Generally 2.5% of eligible construction expenditure, after completion, for qualifying use and within remaining expenditure | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-25 |
| Capital works used in the 4% manner | 4% only where the construction period and Table 43-145 conditions qualify; not every short-stay property | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-145 |
| Low-cost / low-value pooling | Cost or opening adjustable value must be **less than $1,000**, with the relevant method, election and exclusions. This is not an automatic immediate write-off. The $300 rule and denied second-hand purposes cannot be bypassed through pooling | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-425 ; https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-435 |
| Immediate decline-in-value deduction | Cost **$300 or less**, predominantly for non-business assessable income, with the set and identical/substantially identical asset conditions; first test s 40-27 | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-80 |

#### Individual Marginal Tax Rates (2026-27)

**Individual Marginal Tax Rates (2026-27)**

[Australian rates 2026-27](au-rates-2026-27.md) owns the full-year-resident bands, marginal rates and cumulative calculations. Apply that guide, including Medicare, offsets and residence adjustments, to the complete personal return. Do not calculate a person's final tax by treating rental profit as a separate tax base.

#### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown apportionment (private vs rental) | Needs Input; do not book an unsupported deduction or infer a zero legal entitlement |
| Unknown whether repair or improvement | Needs Input; obtain the itemised scope, asset entirety and acquisition condition before selecting a tax treatment |
| Unknown construction cost for Div 43 | Do not claim -- obtain quantity surveyor report. An unclaimed deduction can still reduce the cost base while it remains deductible by amendment (Section 2.8) |
| Unknown contract date for CGT | Do not compute -- obtain contract |
| Unknown cost base | Do not compute CGT -- escalate |

### Section 2 -- Classification Rules

#### 2.1 Rental Income

**Rental Income Types**

| Income Type | Treatment |
| --- | --- |
| Rent received from tenant | For an ordinary individual investor, report gross rent in the year the tenant pays you or your agent; do not add unpaid receivables automatically |
| Bond forfeited (retained for damage) | Assessable in year retained |
| Insurance payout (loss of rent) | Assessable |
| Reimbursement from tenant (excess utilities) | Assessable |
| Key money / lease premium | Refer for classification under the lease, ordinary-income and CGT rules; the label alone does not establish ordinary rental income |

- Report assessable receipts gross, including agent fees withheld, retained bonds, lost-rent insurance and tenant reimbursements where applicable. A refundable bond held in trust is not income merely because received. Allocate legal co-ownership shares before assembling the return. [ATO, Rental income you must declare](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-income-you-must-declare). Item 21 and myTax 2026 Rent are 2025-26 instructions; later-year fields require verification.

#### 2.2 Negative Gearing

- **Negative gearing**. Where total deductions exceed gross rental income, the net rental loss reduces other assessable income (salary, business income). This remains the position for income years up to and including 2026-27.
- **Enacted limit from 2027-28 (ITAA 1997 s 26-155)**. From the 2027-28 income year, where deductions for using or holding residential dwellings as residential accommodation exceed the assessable income from them, the excess is not deductible that year. It becomes a quarantined amount that first reduces residential capital gains in the net capital gain calculation (s 102-5, steps 3 and 4) and is otherwise carried forward to the next year as a residential dwelling expense. Disregard income and deductions for a dwelling interest last acquired before 7:30 pm (ACT time) on 12 May 2026, counting from the contract date (s 26-155(3)); a dwelling that is a new residential dwelling for the taxpayer under the Minister's determination; and dwellings used for an activity the Minister has determined. A net gain from those excepted dwellings, and gains on residential dwellings held as revenue assets, reduce the excess (s 26-155(6)). The rule does not apply to widely held unit trusts or complying superannuation entities, a beneficiary's share of trust net income referable to residential dwellings counts as residential income (s 26-155(7)), and expenditure denied by the section does not enter the cost base (s 110-38(8A)). Hotels, motels, boarding houses, student accommodation, caravans and boats are not residential dwellings (s 26-160(1)).  _([Treasury Laws Amendment (Tax Reform No. 1) Act 2026, Sch 2](https://www.legislation.gov.au/C2026A00049/asmade/text); [ATO, Reforming negative gearing and capital gains tax](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax))_
- **Extensions for death and relationship breakdown, 2027-28 onwards.** A surviving spouse's qualifying joint-tenancy or estate-beneficiary acquisition can preserve the deceased spouse's pre-Budget and new-dwelling status under s 26-156. For a non-spouse co-owner under s 26-157, **both** the survivor's existing interest and the deceased's interest must meet the relevant pre-Budget test; both must have the required new-dwelling status for that extension. Section 26-158 requires an order, agreement or award of a kind in s 126-5(1)(a)-(f) involving the taxpayer and spouse/former spouse; the transferor may be the spouse/former spouse, a company or a trustee. Extended new-dwelling status also applies for s 115-102(2) through s 26-159. Apply the death-timing and s 118-192 disregards in the enacted provisions, rather than treating every inherited or family transfer alike. [Tax Reform No. 2 Act 2026, Schedule 4](https://www.legislation.gov.au/C2026A00071/asmade/text).
- **Example (2028-29)**. An established dwelling acquired in July 2028 earns $50,000 rent and has $65,000 of deductions. $50,000 is deductible and $15,000 is carried forward; in a later year with net rental income, the carried-forward amount is deducted against it (the statutory example in s 26-155(1)).
- **Further enacted conditions.** Disregard fringe-benefit amounts under s 26-155(5). Specified bankruptcy/debt-release events extinguish unapplied quarantined amounts under subsections (8)-(9). Denied expenditure is excluded from **both** cost base and reduced cost base, ss 110-38(8A) and 110-55(9JA). Section 26-160 includes occupant-available adjacent land and associated structures; exclusions include mobile tiny/other mobile homes, caravans, boats, hotels, motels, inns, hostels, boarding houses and student accommodation connected with a school or other educational institution. The student exclusion is not every student tenancy. Ministerial determinations under ss 26-155(2)(c) and 26-160(4) remain unverified here: do not assume an exception. [Tax Reform No. 1 Act 2026, Schedule 2](https://www.legislation.gov.au/C2026A00049/asmade/text).

- **Capital-gain ordering.** Apply capital losses first, then use quarantined amounts against deferred residential capital gains at step 3 of s 102-5 and other residential capital gains at step 4, before CGT discounts. Carry only the unapplied eligible balance forward, subject to the extinguishment rules. [Tax Reform No. 1 Act 2026, Schedule 1 and Schedule 2](https://www.legislation.gov.au/C2026A00049/asmade/text).

- **Bill, not enacted law verified: introduced Schedule 5, checked 4 November 2026.** The introduced Tax Reform No. 3 Bill would apply from 2027-28 and move the dwelling definition to s 960-580, including the 'other similar dwelling' exclusion. Its proposed s 960-590 has 4 Australian new-dwelling routes: building on land acquired without a dwelling, adding a dwelling with a net increase in dwelling numbers, converting a non-residential building and acquiring within 24 months of the first occupancy certificate from an entity for which the dwelling was new. For the ordinary routes, the first occupancy certificate must be issued at or after **7:30 pm ACT time on 12 May 2026**, subject to the unsold-stock transition, and the dwelling's legal interest must be separately transferable. Apply each route's acquisition and certificate dates; the added/conversion routes require the certificate at or after the **later** of Budget time and acquisition. Multiple-dwelling interests must be independently acquirable. The unsold-stock transition substitutes pre-Budget certification and first-entity ownership, with continuous holding for sale after Budget time, whilst retaining the 24-month limit. Proposed subsection (5) concerns a principal purpose, or one principal purpose, of obtaining a tax benefit through treating the dwelling as new, rather than any tax-benefit purpose.

  Proposed exceptions include NDIS-enrolled specialist disability accommodation, affordable housing, public housing made available to the specified government body solely for that use and active build to rent developments; residential care/retirement-village operating businesses have their own conditions. The first-reading text's commencement is the first 1 January, 1 April, 1 July or 1 October after assent, with 2027-28 application. The [Parliament page](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554) labels the bill 'Before Reps', records introduction on 14 October and House third reading on 29 October 2026, and shows no Senate passage or assent; the committee report is due 13 November. Both listed House detail amendment divisions were negatived. This does not establish a complete amendment history. Use the verified [introduced Schedule 5 HTML](https://parlinfo.aph.gov.au/parlInfo/search/display/display.w3p;db=LEGISLATION;id=legislation%2Fbills%2Fr7554_first-reps%2F0005;query=Id%3A%22legislation%2Fbills%2Fr7554_first-reps%2F0000%22;rec=0) only as a proposal, not as a current exception or a forecast taxpayer entitlement.

#### 2.3 Deductible Expenses (Immediate)

**Deductible Expenses (Immediate)**

| Expense | Treatment | Notes |
| --- | --- | --- |
| Interest on investment loan | Deductible | Must trace loan purpose to rental property |
| Council rates | Deductible | Apportioned if part-private |
| Water rates / charges | Deductible |  |
| Body corporate / strata fees | Ordinary administration and general maintenance contributions may be deductible | Special levies funding a particular capital improvement are not immediately deductible. Check capital-works eligibility and timing after work is completed and charged to the fund. [ATO common property expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/common-property-expenses) |
| Land tax | Deductible |  |
| Property management fees | Deductible | Agent commissions, letting fees |
| Insurance (landlord, building, contents) | Deductible |  |
| Advertising for tenants | Deductible |  |
| Pest control | Deductible |  |
| Gardening / lawn mowing (if provided to tenant) | Deductible |  |
| Tax agent fee | Test s 25-5 separately | Tax-affairs expenditure belongs in the appropriate return deduction, with its own private/capital conditions. Do not automatically apply the property's day fraction or deduct it twice. https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-5 |
| Travel to residential rental property | Generally denied for individuals not in business from 1 July 2017 | Section 26-31 also excepts the listed entities, including corporate tax entities, non-SMSF superannuation plans, public unit trusts, managed investment trusts and qualifying all-member partnerships/unit trusts. Check the exact taxpayer rather than stating a universal ban. https://www.ato.gov.au/law/view/document?docid=PAC/19970038/26-31 |

- First establish deductibility and apportion each expense for income-producing use; an expense label is not proof of a full deduction. Private ownership costs, capital work and periods failing the holiday/leisure test need separate treatment. Ordinary strata administration/maintenance contributions and a special capital levy are different. [ATO, Common property expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/common-property-expenses).

- **Borrowing expenses.** Loan establishment fees, lenders mortgage insurance, qualifying valuation fees and duty on the mortgage concern borrowing, rather than interest or transfer duty on the property. Under [s 25-25](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-25), use the shortest of the original contract period, actual borrowing-to-repayment period and **5 years**. For each year, divide remaining expenditure by days in the remaining loan period and multiply by that period's days in the year, then apply the income-producing proportion. A first part year is not automatically one fifth. Subsection (6)'s **$100 or less** immediate rule tests the aggregate qualifying expenditure, including the appropriate income-use proportion of mixed-purpose borrowing costs. Early repayment can change the remaining period. Keep the calculation and refinancing evidence.

#### 2.4 Repairs vs Improvements (TR 97/23)

**Repairs vs Improvements (TR 97/23)**  _([TR 97/23](https://www.ato.gov.au/law/view/document?docid=TXR/TR9723/NAT/ATO/00001))_

| Characteristic | Repair (immediate deduction) | Improvement (capitalise) |
| --- | --- | --- |
| Restores to original condition | Yes | No |
| Replaces with substantially same materials | Can support repair classification | Different materials alone do not establish an improvement; test function, character, extent and incidental modernisation |
| Initial repair on acquisition | Not an immediate s 25-10 deduction | Capital; test Div 40, Div 43 or eligible CGT cost base separately rather than adding it automatically |
| Replaces a roof | Can be a repair where it restores part of the building without an improvement; the roof is not automatically the relevant entirety | Initial repairs, improvements and replacement of the relevant entirety are capital; apply [TR 97/23](https://www.ato.gov.au/law/view/document?docid=TXR/TR9723/NAT/ATO/00001) to the facts |
| Example: patching cracked tiles | Repair | -- |
| Example: replacing all tiles with stone | -- | Improvement |
| Example: replacing broken tap with same model | Repair | -- |
| Example: full kitchen renovation | -- | Improvement |

- **Identify the entirety and the cause**. For each repair, identify the asset or entirety repaired, its condition when acquired, the cause of the deterioration and what the work changed. Modern materials can restore an asset without making every job an improvement, and an itemised invoice that separates repair from capital work supports the split.  _([ATO, Repair and maintenance expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/repair-and-maintenance-expenses))_

#### 2.5 Division 40 -- Plant & Equipment Depreciation

**Division 40 Effective Lives**  _(Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025, Table A, Residential property operators (67110). [2025 determination, Schedule 2 Table A](https://www.legislation.gov.au/F2025L01097/asmade))_

These are Commissioner-determined lives in the 2025 Effective Life Determination's residential property operators table. Confirm the determination applicable when the asset starts use; a supportable self-assessed life is a separate choice.

| Asset | Effective Life (ATO) | Decline Method |
| --- | --- | --- |
| Hot water system (gas or electric) | 12 years | Diminishing value or prime cost |
| Hot water system (solar) | 15 years | Either |
| Carpet | 8 years | Either |
| Internal window blinds | 10 years | Either |
| Window curtains | 6 years | Either |
| Oven / cooktop | 12 years | Either |
| Air conditioning (mini-split, up to 20 kW, in the specified table class) | 10 years | Either; do not apply this life to every split system |
| Dishwasher | 8 years | Either |
| Smoke alarm | 6 years | Either |
| Ceiling fan | 5 years | Either |

The table follows Table A, Residential property operators (67110), in the *Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025*. Choose the applicable determination under section 40-95, including its contract-date and start-time rules, or a valid self-assessed life; do not automatically reset an existing asset register. See [2025 determination, Schedule 2 Table A](https://www.legislation.gov.au/F2025L01097/asmade).

Every effective life above comes from the specified Table A asset class, not the property's purchase price. [Section 40-95](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-95) generally selects the Commissioner's life in force at contract/acquisition/construction time if start time is within **5 years**, otherwise at start time, with the older plant and associate/rollover exceptions. Make the permitted choice for the start-time year; do not replace a continuing register merely because a newer determination exists.

- **Diminishing value.** For assets first held on or after **10 May 2006**, decline is base value × days held / 365 × 200% / effective life, capped at base value. The first-year base is cost; later base is opening adjustable value plus relevant second-element costs. Older s 40-70 assets generally use 150%, not 200%. Apply taxable-use and other statutory reductions after working out decline. [Sections 40-70](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-70) and [40-72](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-72).
- **Prime cost.** The ordinary formula is cost × days held / 365 × 100% / effective life, not written-down value × the rate. Adjust the formula for the changes specified in s 40-75(2), including certain later costs and effective-life recalculation. The days exclude periods before start time and when no longer held. [Section 40-75](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-75).
- **Second-hand restriction.** [Section 40-27](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-27) reduces the deduction for specified previously used or private-use assets used to provide residential accommodation. It does **not** set the asset's tax cost to zero. Preserve cost, decline and termination-value records for a possible K7 event. Refurbishing a property is not a general exception, and an owner can also bring previously privately used assets within the restriction.
- **Exceptions and transition.** Test the business boundary in s 40-27(2) and the specified-entity and all-member exceptions in subsection (3), not only the identity of the first owner. Corporate tax entities, non-SMSF superannuation plans, public unit trusts and managed investment trusts are listed, with qualifying all-member partnerships/unit trusts. The new-premises exception in subsections (4)-(5) has precise supplier, occupancy and **6-month** conditions; substantial renovation alone does not establish it. The 2017 transition generally protects assets acquired, or contracted for, before **7:30 pm AEST on 9 May 2017**, and installed before **1 July 2017**; check the complete history and other transition conditions, including the statutory application rule in item 13 of Schedule 2 to Act No. 126 of 2017. A genuinely new appliance can qualify in an old building, subject to taxable use and the other rules. [ATO, Second-hand depreciating assets](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/depreciating-assets-in-rental-properties/second-hand-depreciating-assets).
- **Pooling.** A valid low-cost choice carries commitment rules; a low-value asset has its own diminishing-value history requirement. Sections [40-425](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-425), [40-430](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-430), [40-435](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-435) and [40-440](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-440) govern the choice, taxable-use percentage, exclusions and calculation. Section 40-435(2) excludes a purpose denied under s 40-27; pooling does not restore that deduction.

#### 2.6 Division 43 -- Capital Works Deduction

**Division 43 Capital Works Deduction Rates**

| Construction Date | Rate and conditions | Official source |
| --- | --- | --- |
| Ordinary residential works begun before 18 July 1985 | Outside the ordinary residential commencement category; test any other qualifying category rather than assuming all older works qualify | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-140 |
| Ordinary residential works begun 18 July 1985 to 15 September 1987 | 4%, subject to qualifying use and remaining expenditure | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-25 ; https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-140 |
| Ordinary residential works begun after 15 September 1987 | Generally 2.5%, subject to the applicable construction category, qualifying use and remaining expenditure | same |
| Qualifying traveller-accommodation works begun before 27 February 1992 | 4% if begun after 21 August 1984 and before 16 September 1987; otherwise 2.5%. A 1990 start does not receive 4% merely for traveller use | same |
| Qualifying works begun after 26 February 1992 | Basic 2.5%; 4% only for parts used as Table 43-145 specifies. Traveller accommodation must satisfy that table | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-25 ; https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-145 |
| Eligible new build to rent developments begun after 7:30 pm on 9 May 2023 | 4% over 25 years rather than 40, subject to the active-development, ownership and approved-choice conditions. From 1 January 2025 the owner can choose the incentive on the approved form; not an automatic individual-landlord rate | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-145 ; https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/whats-new-in-the-rental-properties-guide |

- **Base and timing.** Establish eligible construction expenditure, the expenditure area/pool, construction start and completion, qualifying current use and undeducted expenditure. Construction begins with the first construction-phase step, such as foundations; no deduction is available before completion. Land, plant, landscaping and other excluded costs are not automatically construction expenditure, and purchase price is not the deduction base. Obtain builder records or a supportable estimate from an appropriately qualified person. [Sections 43-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-10), [43-20](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-20), [43-30](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-30), [43-70](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-70) and [43-80](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-80). Apply the correct rate/use-day calculation and remaining-expenditure cap, not a blanket 2.5% to every property.
- **Undeducted construction cost:** A new owner continues the annual deduction using the original eligible construction expenditure and remaining deduction period, subject to qualifying use and the remaining expenditure cap. Each deduction is the original expenditure x 2.5% x qualifying days in the income year / 365, so $400,000 of eligible 2.5% construction gives $10,000 for a 365-day year and $10,027.40 for a 366-day year until the undeducted expenditure runs out. (ITAA 1997 Div 43, ss 43-15, 43-70 and 43-210 Step 3.)

#### 2.7 Interest Deductibility

- **Nexus requirement**. The loan must have a clear nexus to producing rental income. Key rules follow in the table.
- **Mixed-purpose loans and redraws.** A private redraw creates a private borrowing. Ordinary principal repayments to one mixed account reduce its income and private components proportionately; they cannot simply be allocated to the private component. TR 2000/2 paragraphs 17-18 provide exceptions for traced recouped funds repaid to the account and refinancing the separate income/private debt portions. Paragraphs 19-20 accept a monthly average opening/closing-principal approach for the specified daily-interest facilities. Trace changes and choose a fair, supportable method; do not apply a fixed annual percentage after the facts change. [ATO interest expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/interest-expenses); [TR 2000/2 paragraphs 12-25](https://www.ato.gov.au/law/view/document?docid=TXR/TR20002/NAT/ATO/00001).

**Interest Deductibility Scenarios**

| Scenario | Deductible? |
| --- | --- |
| Loan to purchase rental property | To the extent the money is used for the assessable-income purpose and no denial applies |
| Loan to renovate rental property | Trace use and timing; capital character of the works does not itself determine interest deductibility |
| Refinanced loan (same purpose, same or lower amount) | May retain the traced income-purpose nexus; mixed/private portions remain separate |
| Loan redrawn for personal use | No -- apportioned |
| Line of credit (mixed purpose) | Must trace each drawdown |
| Interest on loan while property vacant (available for rent) | May qualify where the continuing income nexus, genuine availability and other conditions hold; vacancy does not cure private borrowings or s 26-50 denial |
| Interest directly attributable to constructing an intended rental property | May be currently deductible under s 8-1 before rental availability where the income-producing intention and other deduction conditions are met |
| Interest on land acquisition during construction | Check s 26-102 vacant-land restrictions and exclusions separately. Trace and apportion combined loans. Consider cost base only for amounts denied a deduction and otherwise eligible |

#### 2.8 CGT on Disposal

**CGT on Disposal Elements**

| Element | Treatment |
| --- | --- |
| Cost base | Purchase price + stamp duty + legal fees on purchase and sale + agent commission on sale + capital improvements - Div 43 amounts the owner has deducted or can deduct, for property acquired after 7:30 pm on 13 May 1997, and for fourth element expenditure incurred after 30 June 1999 on older property ([s 110-45(1A), (2), (4)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-45)). The reduced cost base is separate: [s 110-55(4)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-55) excludes an amount deducted or deductible, with no such acquisition date limit. Under [TD 2005/47](https://www.ato.gov.au/law/view/document?docid=TXD/TD200547/NAT/ATO/00001) an amount can be deducted at a particular time if the deduction provision's terms are satisfied and the s 170 ITAA 1936 amendment periods have not expired for that deduction. So an unclaimed amount still counts while it can be deducted by amendment, but not once it is out of time, provided the owner is within the amendment period for the CGT event. [PS LA 2006/1 (GA)](https://www.ato.gov.au/law/view/document?docid=PSR/GA20061/NAT/ATO/00001) separately relieves an owner who lacks sufficient information to determine the construction expenditure and has not sought any deduction for it |
| Capital proceeds | Sale price under the contract; selling costs belong in the cost base, not here |
| Capital gain | Capital proceeds - cost base; capital losses and the discount then apply to reach the net capital gain (see `au-capital-gains.md`) |
| CGT discount | Apply Division 115's eligible taxpayer, holding-period, residence and transaction-year tests; [Capital gains](au-capital-gains.md) owns the discount rate and dwelling changes. Do not promise a discount for every long holding |
| Main residence exemption (partial) | Test actual main-residence history, income use, entity and foreign-resident restrictions. Part-period residence can give a partial exemption under s 118-185. Where s 118-192 applies, first income use after 7:30 pm ACT time on 20 August 1996 and full exemption immediately before that use can require a market-value reset; obtain valuation evidence. https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-185 ; https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-192 |
| 6-year absence choice | The dwelling must first have been the main residence. Income-producing use has a maximum 6-year period, renewed when it again becomes and ceases to be the main residence; non-income-producing absence can be indefinite. Generally no other main residence can be chosen for the same time, subject to the changing-homes exception. This does not override foreign-resident exclusions. https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-145 ; https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-110 |
| Non-residents | Work out preserved discount entitlement for qualifying resident periods and any pre-8 May 2012 rules; see au-nonresident-cgt |
| Second-hand depreciating assets denied under s 40-27 | A balancing adjustment event, including on sale of the property, generally triggers CGT event K7 ([s 104-235(1)(b)(ii)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-235)). It usually gives a capital loss, because cost normally exceeds termination value, scaled by the share of decline in value denied. Allocate purchase and sale prices between these assets and the property so the loss is not missed |

#### 2.9 Foreign Resident Landlords and Vendors

**Foreign Resident Landlords and Vendors**  _([ATO, FRCGW overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview); [ATO, FRCGW](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding))_

| Rule | Detail |
| --- | --- |
| Rental income | No general withholding applies to rent paid to a foreign resident landlord. The landlord lodges an Australian return and pays tax at foreign resident rates, with no tax-free threshold; the ATO can direct a tenant or agent to pay amounts to it under a garnishee notice |
| FRCGW (foreign resident CGT withholding) | [Non-resident CGT](au-nonresident-cgt.md) owns the rates, thresholds and contract-date periods. Establish market value, normally the arm's-length sale price, and the clearance-certificate, variation and excluded-transaction rules. Use contract date rather than settlement date. [ATO, FRCGW](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding) |
| Clearance certificate | An Australian resident vendor obtains one and gives it to the purchaser before settlement to avoid FRCGW. Apply for it early; processing is not immediate |
| Variation | A foreign resident vendor can apply for a variation where withholding exceeds the expected Australian tax on the sale; use [Non-resident CGT](au-nonresident-cgt.md) for the conditions |

### Section 3 -- Transaction Pattern Library

#### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| REAL ESTATE AGENT [name], RENT COLLECTION | Assessable rental income | Net of agent commission (report gross; deduct commission separately) |
| TENANT [name], RENT PAYMENT, BOND TRANSFER | Assessable rental income | Bond held in trust is NOT income until forfeited |
| [INSURER] CLAIM PAYOUT, LOSS OF RENT | Assessable | Insurance for lost rent |
| AIRBNB PAYOUT, STAYZ PAYOUT | Assessable | Short-term rental income |

#### 3.2 Expense Patterns (Debits) -- Immediate Deductions

**Expense Patterns (Debits) -- Immediate Deductions**

| Pattern | Category | Treatment |
| --- | --- | --- |
| [COUNCIL NAME] RATES, COUNCIL RATES | Council rates | Deductible only to the established income-use extent, subject to timing and statutory denials |
| WATER CORP, SA WATER, SYDNEY WATER | Water rates | Deductible only to the established income-use extent, subject to timing and statutory denials |
| BODY CORPORATE, STRATA LEVY, OWNERS CORP | Body corporate fees | Separate regular administration/maintenance fees from special capital levies. No immediate deduction for a capital levy; check capital works after completion and charging |
| [STATE] LAND TAX, REVENUE NSW, SRO VIC | Land tax | Deductible only to the established income-use extent, subject to timing and statutory denials |
| [AGENT NAME] MANAGEMENT FEE, LETTING FEE | Property management | Deductible only to the established income-use extent, subject to timing and statutory denials |
| [INSURER] LANDLORD INSURANCE, BUILDING INS | Insurance | Deductible only to the established income-use extent, subject to timing and statutory denials |
| PLUMBER, ELECTRICIAN, [TRADESPERSON] REPAIR | Repair (if restoring) | Deductible if repair per TR 97/23 |
| BUNNINGS, HARDWARE (minor repair materials) | Repair materials | Deductible if repair nature |
| PEST CONTROL, TERMITE INSPECTION | Pest control | Deductible only to the established income-use extent, subject to timing and statutory denials |

#### 3.3 Expense Patterns (Debits) -- Capital (Depreciate)

**Expense Patterns (Debits) -- Capital (Depreciate)**

| Pattern | Category | Treatment |
| --- | --- | --- |
| KITCHEN RENOVATION, BATHROOM RENO | Capital improvement | Test eligible cost base and Div 43 separately; neither is established by the label alone |
| NEW HOT WATER SYSTEM (replacement-upgrade) | Potential Div 40 asset | Identify gas/electric versus solar and the applicable effective-life class; new does not remove private-use or other conditions |
| NEW AIR CONDITIONER (split system install) | Potential Div 40 asset | Identify the exact capacity and table class before using the effective-life table |
| NEW CARPET (full replacement, better quality) | Potential Div 40 asset | Apply the effective-life table and s 40-27, including transition/entity exceptions; previously used carpet does not automatically have zero tax cost |

#### 3.4 Loan / Interest Patterns

**Loan / Interest Patterns**

| Pattern | Category | Treatment |
| --- | --- | --- |
| [BANK] HOME LOAN INTEREST, INVESTMENT LOAN INT | Interest expense | Deductible (if loan traces to rental property) |
| [BANK] LOAN REPAYMENT, PRINCIPAL + INTEREST | Mixed | Only interest portion deductible -- NOT principal |
| [BANK] OFFSET ACCOUNT INTEREST | Interest saving | Reduces deductible interest (net interest method) |
| [BANK] LINE OF CREDIT DRAWDOWN | Capital movement | NOT income; trace use of funds |

#### 3.5 Exclusions

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BOND LODGEMENT, RTA BOND, RTBA | EXCLUDE | Bond held in trust -- not income |
| MORTGAGE PRINCIPAL REPAYMENT | EXCLUDE | Capital repayment -- not deductible |
| PERSONAL USE period expenses | APPORTION | Deduct only rental-use portion |

### Section 4 -- Computation Method

#### Step 1: Gross Rental Income

- **Gross Rental Income**. Sum all assessable rental receipts for the financial year.

#### Step 2: Immediate Deductions

- **Immediate Deductions**. Sum all allowable expenses (interest, rates, insurance, management fees, repairs, body corporate, etc.).

#### Step 3: Depreciation (Div 40 + Div 43)

- Calculate allowed Div 40 decline using the chosen method, asset-specific life, days, taxable use and restrictions. Calculate Div 43 separately from eligible construction expenditure, qualifying use, the correct rate and remaining expenditure. Do not deduct an asset cost twice or add an undeductible private-use amount to the rental total.

#### Step 4: Net Rental Income / Loss

- **Net Rental Income / Loss**. Gross income − deductions − depreciation = net rental income (or loss if negative gearing).

#### Step 5: Report on Tax Return

- **Reporting outcome**. Positive: included in assessable income and taxed at marginal rates. Negative: offsets other assessable income (salary, business) dollar-for-dollar up to and including 2026-27; from 2027-28 apply the s 26-155 quarantining test in Section 2.2 first.

### Section 8 -- Which tax applies, and where its rules live

A property transaction can touch four separate regimes at once. Work out which apply before
calculating anything, because the answer to one changes the inputs to another.

#### 8.1 Decision table by event

**Decision table by event**

| Event | Income tax | GST | CGT | State or territory |
| --- | --- | --- | --- | --- |
| Buying a residential investment property | Borrowing costs, and holding costs once available for rent | Generally input taxed on an existing residential premises, so no credit on the purchase. New residential premises may be taxable and may trigger GST at settlement | Establishes the cost base | Transfer duty, and possibly foreign purchaser surcharge duty |
| Holding and renting it out | Rental income assessable, deductions under Section 2, Div 40 and Div 43 | Residential rent is input taxed, so no GST on rent and no credits on expenses | Div 43 amounts deducted or deductible generally reduce the cost base (Section 2.8) | Land tax, and possibly a foreign owner or vacancy surcharge |
| Renovating | Repair deductible, improvement capital | Credits depend on whether the premises remain input taxed | Capital work enters the cost base or Div 43 | Nil, unless it changes the land tax position |
| Short-stay or holiday letting | Apportionment for private use and periods not genuinely available | Commercial residential premises can be taxable rather than input taxed. Test this, do not assume | Main residence exemption can be lost or reduced | Some jurisdictions apply short-stay levies |
| Buying or holding a commercial property | Rent assessable, deductions available | Generally taxable, so GST on rent and credits on expenses, subject to registration. A going concern or margin scheme may apply on sale | Cost base as normal | Transfer duty and land tax |
| Selling | Balancing adjustments on Div 40 assets | See `au-gst-property.md`. GST at settlement can require the purchaser to withhold | The CGT calculation. See `au-capital-gains.md` | Duty is payable by the purchaser, not the vendor |
| Selling as a foreign resident | Rental income to the date of sale | As above | No automatic CGT discount, and the main residence exemption is generally unavailable | As above |

#### 8.2 The GST decision path

1. **Is the supply residential premises?** Existing residential premises are input taxed: no GST
   on the sale or the rent, and no credits on related acquisitions.
2. **Are they new residential premises, and what supply is made?** A sale or long-term lease can fall outside the input-taxed residential rules; it is taxable only if s 9-5 and the other applicable conditions are met. An ordinary residential lease can remain input taxed even when the dwelling is new. Do not treat new-property rent as taxable merely because a sale would be taxable. GST withholding has separate exceptions, including for certain substantially renovated premises. [GST Act ss 40-35](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/40-35), [40-65](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/40-65), [40-70](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/40-70) and [9-5](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/9-5).
3. **Are they commercial residential premises?** Hotels, motels and similar are generally taxable if s 9-5 applies. Long-term commercial accommodation can have Division 87 treatment, including input taxation following a supplier choice under s 87-25; check the GST guide and the actual supply before classifying it. Short-stay accommodation also needs the actual facts. [Section 40-35(1)(b)](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/40-35).
4. **Is it commercial property?** Generally taxable, subject to registration and turnover.
5. **Does an entity-level test change the answer?** Establish consideration, enterprise, Australian connection and registration/required registration under s 9-5. The ordinary registration threshold is a separate turnover test, not a rule that turns input-taxed rent into a taxable supply; [Australia GST](australia-gst.md) owns its amount, scope and calculation.
6. **Does a special rule apply on sale?** The margin scheme, the going concern exemption and GST
   at settlement each have their own conditions. A GST-free going concern requires consideration, the recipient's registration/required registration, written agreement, all things necessary for the enterprise and its continuation until supply. The margin scheme requires an eligible acquisition history and agreement within its statutory timing. [Sections 38-325](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/38-325) and [75-5](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/75-5).

The full rules are in `au-gst-property.md` and `australia-gst.md`. Do not decide a property GST
question from this file alone.

#### 8.3 State and territory taxes are not federal, and are not uniform

Land tax, transfer duty, foreign purchaser and foreign owner surcharges, and vacancy or short-stay
levies are imposed by each state and territory under its own Act. Thresholds, rates, exemptions,
aggregation rules, trust surcharges and the definition of a principal place of residence all
differ. A rule from one jurisdiction must never be applied to another.

Establish the jurisdiction first, then read that jurisdiction's own guidance:

**Jurisdiction revenue authorities**

| Jurisdiction | Revenue authority |
| --- | --- |
| New South Wales | Revenue NSW, https://www.revenue.nsw.gov.au/ |
| Victoria | State Revenue Office Victoria, https://www.sro.vic.gov.au/ |
| Queensland | Queensland Revenue Office, https://qro.qld.gov.au/ |
| Western Australia | RevenueWA (Department of Treasury and Finance), https://www.wa.gov.au/organisation/department-of-treasury-and-finance |
| South Australia | RevenueSA, https://www.revenuesa.sa.gov.au/ |
| Tasmania | State Revenue Office Tasmania, https://www.sro.tas.gov.au/ |
| Australian Capital Territory | ACT Revenue Office, https://www.revenue.act.gov.au/ |
| Northern Territory | Territory Revenue Office, https://treasury.nt.gov.au/dtf/territory-revenue-office |

Land tax paid on an income-producing property is generally deductible in the year it is incurred.
Transfer duty on the purchase is not deductible; it is a cost base element. See `au-land-tax.md`
and `au-stamp-duty.md` for the jurisdiction-specific detail.

#### 8.4 Related guides

**Related guides**

| Question | Guide |
| --- | --- |
| GST on a property sale, margin scheme, GST at settlement | `au-gst-property.md` |
| CGT calculation, losses, discount, the 1 July 2027 changes | `au-capital-gains.md` |
| Land tax by jurisdiction | `au-land-tax.md` |
| Transfer duty by jurisdiction | `au-stamp-duty.md` |
| Reporting the rental schedule in the return | `au-individual-return.md` |
| Deductions and offsets generally | `au-deductions-offsets.md` |
| Foreign resident disposals | `au-nonresident-cgt.md` |
| Property held in a trust or SMSF | `au-trust-distributions.md`, `au-smsf.md` |

## Boundary and exception table

### Section 6 -- Edge Cases

#### 6.1 Property Vacant

- **Vacancy and continuing income purpose.** For ordinary holding costs during vacancy, establish genuine availability on commercial terms and exclude private/holiday periods, subject to section 26-50 and each expense's rules. Do not make advertising an absolute condition for every deduction: interest may remain deductible whilst damage repairs make the rental uninhabitable. Pre-commencement or construction interest requires the separate nexus and vacant-land analysis above. [ATO, interest expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/interest-expenses).

#### 6.2 Part-Year Rental / Part-Private Use

- **Apportionment.** First separate costs attributable solely to letting from shared ownership/use costs and costs attributable solely to private use. Depending on the facts, shared costs need both a reasonable area allocation and eligible days divided by actual days in the income year. Under PCG 2026/2, a room in the owner's home has **zero** eligible unoccupied days held for income production under that approach. Another property may have eligible genuinely available days, subject to its use and s 26-50. Do not apply one fraction indiscriminately to every expense, tax-agent fee or asset, and do not assume full interest deduction merely because the property was advertised. [PCG 2026/2](https://www.ato.gov.au/law/view/document?docid=COG/PCG20262/NAT/ATO/00001).
- **Co-owners and domestic arrangements.** Ordinarily allocate rental income and shared expenses by legal interests; one owner paying the shared bills does not change the split. Very limited, sufficiently evidenced equitable-interest cases need separate analysis. Interest on money borrowed solely by one co-owner and used exclusively to acquire that person's interest need not be divided between the co-owners. [TR 2026/1 paragraphs 72-75](https://www.ato.gov.au/law/view/document?docid=TXR/TR20261/NAT/ATO/00001). A partnership carrying on a rental business needs separate analysis, and sharing household costs with a family member is not automatically a commercial rental arrangement.  _([ATO, Rental income you must declare](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-income-you-must-declare))_

#### 6.3 Holiday Homes

- **Holiday home deduction limitation**. Deductions follow genuine availability for rent. Periods of private use, or of advertising on terms that make letting unlikely, are not deductible, and where the property is let to a relative or friend at below-market rent the ATO limits deductions to the rent received. Apportion under PCG 2026/2 and test section 26-50 below. The ATO scrutinises holiday letting closely.
- **Section 26-50 leisure facilities.** Test the statutory denial and exceptions **before** apportioning otherwise deductible expenses. 'Mainly' requires an objective qualitative and quantitative assessment of use/holding purpose, rather than a simple majority-of-days formula. A definite, sustained part-year change can engage subsection (4). Keep advertisements, agency agreements, bookings, private-use and market-rent evidence. A short letting period alone does not establish the income-purpose exception. [Section 26-50](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/26-50); [TR 2026/1 paragraphs 30-48](https://www.ato.gov.au/law/view/document?docid=TXR/TR20261/NAT/ATO/00001).
- **Earlier expenses and compliance approach.** TR 2026/1 Appendix 2 paragraphs 137-140 says the Commissioner will not devote compliance resources to s 26-50 expenses incurred before **1 July 2026**, excluding avoidance, fraud, evasion or inappropriate advantage. Requested assessments, amendments and rulings still follow the ruling's view. This administrative approach is not a statutory exemption or a new commencement date for s 26-50. PCG 2026/3 separately describes compliance risk. [TR 2026/1](https://www.ato.gov.au/law/view/document?docid=TXR/TR20261/NAT/ATO/00001); [PCG 2026/3](https://www.ato.gov.au/law/view/document?docid=COG/PCG20263/NAT/ATO/00001).
- **TR 2026/1 and the 2026 compliance guidelines**. TR 2026/1 sets out when rental receipts are assessable, when outgoings are deductible and how to apportion mixed use for individuals not in business. PCG 2026/2 gives the apportionment methods the ATO accepts, and PCG 2026/3 its compliance approach to section 26-50 for holiday homes that are also let. Read them before claiming a loss on a property with any private use.  _([ATO, What's new in the rental properties guide 2026](https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/whats-new-in-the-rental-properties-guide); [ITAA 1997 (Cth) s 26-50](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/26-50); [ATO, How to claim rental expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/how-to-claim-rental-expenses))_

#### 6.4 Subdivision and Development

- **Subdivision profit treatment**. If a rental property is subdivided, the profit on sale of subdivided lots may be ordinary income (not CGT) if the taxpayer has a profit-making intention. Escalate to specialist.

#### 6.5 Deceased Estates

- **Deceased estate.** Separate pre-death and estate income. Who is assessed on estate rental income depends on administration, present entitlement, actual distributions, disability and residence; legal transfer date alone is insufficient. An LPR's sale can trigger CGT before any transfer to a beneficiary. Section 128-15(3) disregards the relevant gain/loss on an asset **passing** from the LPR to a beneficiary; it is not a blanket exemption for all estate disposals. Use `au-deceased-estates.md` and obtain the will, administration and distribution evidence. [IT 2622](https://www.ato.gov.au/law/view/document?docid=ITR/IT2622/NAT/ATO/00001); [s 128-15](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/128-15).

## Worked cases

All amounts below are hypothetical AUD. Each case stipulates the legal classifications and evidence described; the executable blocks check arithmetic, not eligibility, a taxpayer's documents or the current law. A case does not authorise filing or an election.

### 1. Full-year individual rental, 2026-27

A sole owner has no private use, no mixed borrowings and a genuine income-producing property throughout the 365-day year. Gross rent is $26,000; interest $10,000, rates $2,000, insurance $1,000, repairs $500 and management $1,300 are all independently established as deductible. Eligible new carpet costs $8,000, has an 8-year effective life and uses prime cost for the full year. Completed eligible construction expenditure is $400,000 at 2.5%, with sufficient undeducted expenditure. Immediate expenses are $14,800, Div 40 $1,000 and Div 43 $10,000, leaving **$200 net rental income**. Personal income tax, Medicare, other income and tax-agent fees are separate.

```oa-check
name: Full-year rental income and separate capital allowances, 2026-27
inputs:
  rent: 26000
  interest: 10000
  rates: 2000
  insurance: 1000
  repairs: 500
  management: 1300
  carpet_cost: 8000
  effective_life: 8
  construction_expenditure: 400000
  capital_works_rate: 0.025
steps:
  immediate: interest + rates + insurance + repairs + management
  div40: carpet_cost / effective_life
  div43: construction_expenditure * capital_works_rate
  net_rental: rent - immediate - div40 - div43
expected:
  immediate: 14800
  div40: 1000
  div43: 10000
  net_rental: 200
```

### 2. Decision: prime cost or diminishing value for a new asset

Before making the permitted method choice, compare both methods for new $8,000 carpet first held and first used on 1 July 2025, an 8-year life, 100% taxable use and 365 days in each of 2025-26 and 2026-27. There are no later costs, pooling, immediate-write-off or s 40-27 restrictions. Prime cost gives **$1,000 each year**, $2,000 over 2 years and $6,000 adjustable value. Diminishing value gives **$2,000 then $1,500**, $3,500 over 2 years and $4,500 adjustable value. DV accelerates $1,500 of deductions over these 2 years; that is not a permanent $1,500 tax saving. The taxpayer's tax rates, future use/disposal and lawful choice restrictions determine the decision. Do not switch methods each year to select the larger result. [Sections 40-72](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-72) and [40-75](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-75).

```oa-check
name: Prime cost versus diminishing value, two full years
inputs:
  cost: 8000
  life: 8
steps:
  pc_year1: cost / life
  pc_year2: cost / life
  pc_total: pc_year1 + pc_year2
  pc_adjustable: cost - pc_total
  dv_year1: cost * 2 / life
  dv_year2: (cost - dv_year1) * 2 / life
  dv_total: dv_year1 + dv_year2
  dv_adjustable: cost - dv_total
  accelerated_deduction: dv_total - pc_total
expected:
  pc_year1: 1000
  pc_year2: 1000
  pc_total: 2000
  pc_adjustable: 6000
  dv_year1: 2000
  dv_year2: 1500
  dv_total: 3500
  dv_adjustable: 4500
  accelerated_deduction: 1500
```

### 3. A room in the owner's home, 2026-27

Eligible shared ownership expenses are $3,650. A reasonable documented area share, including the appropriate common-area allocation, is 30%, and the room is actually let for 200 days. Under the selected PCG 2026/2 approach, its 100 advertised but unoccupied days count as **zero** held-for-income days because it is part of the owner's home. Shared deductible expenses are **$600**. Advertising costing $200 relates solely to the actual letting and independently qualifies, giving **$800 total deductions**. There is no s 26-50 denial on these stipulated facts. This case does not apply the same fraction to every asset or expense. [PCG 2026/2](https://www.ato.gov.au/law/view/document?docid=COG/PCG20262/NAT/ATO/00001).

```oa-check
name: Room at home, area and actual letting days
inputs:
  shared_expenses: 3650
  area_fraction: 0.30
  let_days: 200
  eligible_unoccupied_days: 0
  year_days: 365
  letting_only_advertising: 200
steps:
  shared_deduction: shared_expenses * area_fraction * (let_days + eligible_unoccupied_days) / year_days
  total_deduction: shared_deduction + letting_only_advertising
expected:
  shared_deduction: 600
  total_deduction: 800
```

### 4. Ordinary repayment to one mixed-purpose loan

A mixed account begins the month with $300,000 traced to qualifying rental use and $100,000 to private use. A $40,000 principal repayment is not recouped sale proceeds, a refinancing or another exception. It leaves **$270,000 rental debt and $90,000 private debt**. With no other drawdowns or purpose changes, the accepted opening/closing monthly proportion is 75%. Of $2,000 interest, **$1,500** is deductible, subject to the continuing income nexus. A repayment is not itself a rental expense. [TR 2000/2 paragraphs 16-25](https://www.ato.gov.au/law/view/document?docid=TXR/TR20002/NAT/ATO/00001).

```oa-check
name: Mixed loan ordinary repayment and monthly interest
inputs:
  rental_open: 300000
  private_open: 100000
  principal_repaid: 40000
  monthly_interest: 2000
steps:
  total_open: rental_open + private_open
  rental_close: rental_open - principal_repaid * rental_open / total_open
  private_close: private_open - principal_repaid * private_open / total_open
  total_close: rental_close + private_close
  income_fraction: (rental_open + rental_close) / (total_open + total_close)
  deductible_interest: monthly_interest * income_fraction
expected:
  rental_close: 270000
  private_close: 90000
  income_fraction: 0.75
  deductible_interest: 1500
```

### 5. Successor's capital works deduction

Retain the construction example: $400,000 eligible expenditure, completed and qualifying throughout, at 2.5%. The deduction is expenditure x 2.5% x qualifying days / 365, with 365 as the divisor even in a leap year. Deductions for the 3,652 days from 1 July 2016 to 30 June 2026 total **$100,054.79**, leaving undeducted expenditure of **$299,945.21**. A successor with uninterrupted qualifying use continues on the original $400,000 base: **$10,000** for a 365-day year and **$10,027.40** for a 366-day year, capped by the undeducted expenditure. Applying 2.5% to the undeducted amount would wrongly give $7,498.63. Actual acquisitions, use days, destruction and prior deductions require the statutory calculation. [Division 43](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-15); [section 43-210](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-210).

```oa-check
name: Capital works successor retains original expenditure base
inputs:
  original_expenditure: 400000
  annual_rate: 0.025
  divisor_days: 365
  standard_year_days: 365
  leap_year_days: 366
  elapsed_qualifying_days: 3652
steps:
  standard_year_deduction: original_expenditure * annual_rate * standard_year_days / divisor_days
  leap_year_deduction: original_expenditure * annual_rate * leap_year_days / divisor_days
  prior_deductions: original_expenditure * annual_rate * elapsed_qualifying_days / divisor_days
  remaining_expenditure: original_expenditure - prior_deductions
  wrong_rate_on_remaining: remaining_expenditure * annual_rate
expected:
  standard_year_deduction: 10000
  leap_year_deduction: 10027.40
  prior_deductions: 100054.79
  remaining_expenditure: 299945.21
  wrong_rate_on_remaining: 7498.63
```

### 6. Borrowing expenditure in a part year, 2026-27

Qualifying borrowing expenditure is $1,500. Borrowing begins on 1 January 2027, the original contract exceeds 5 years, there is no early repayment and all money is used for the income purpose. The selected 5-year loan period has 1,826 days, of which 181 fall in 2026-27. The first deduction is **$148.69**, not $300. Keep full precision until the return's rounding step and reassess the remaining period each year. [Section 25-25](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-25).

```oa-check
name: Borrowing expenditure uses loan-period days
inputs:
  remaining_expenditure: 1500
  remaining_loan_days: 1826
  loan_days_this_year: 181
steps:
  maximum_deduction: remaining_expenditure / remaining_loan_days * loan_days_this_year
expected:
  maximum_deduction: 148.69
```

### 7. Enacted future quarantining example, 2028-29 to 2030-31

An established dwelling acquired in July 2028 has no established exception. Assume the enacted rule applies unchanged, all listed expenses otherwise qualify, there are no residential capital gains to absorb amounts and no extinguishment event. In 2028-29, $50,000 rent and $65,000 expenses leave **$15,000 quarantined**, not an offset against salary. In 2029-30, $52,000 rent, $70,000 new expenses and the carried amount produce **$33,000 carried forward**. In 2030-31, $72,000 rent less $20,000 new expenses and $33,000 carried expenses leaves **$19,000 net income**. Recheck future law and exceptions before actual use. [Tax Reform No. 1 Act 2026, Schedule 2 statutory example](https://www.legislation.gov.au/C2026A00049/asmade/text).

```oa-check
name: Enacted future residential loss carry-forward, three years
inputs:
  rent1: 50000
  expenses1: 65000
  rent2: 52000
  expenses2: 70000
  rent3: 72000
  expenses3: 20000
steps:
  carry1: max(expenses1 - rent1, 0)
  carry2: max(carry1 + expenses2 - rent2, 0)
  net3: max(rent3 - expenses3 - carry2, 0)
  carry3: max(carry2 + expenses3 - rent3, 0)
expected:
  carry1: 15000
  carry2: 33000
  net3: 19000
  carry3: 0
```

### 8. A co-owner's acquisition borrowing and shared borrowing

Compare 2 stipulated full-year, wholly income-producing borrowings for a property owned equally by 2 individuals. There is no private use, business, equitable-interest exception or other deduction denial. In the first alternative, only A borrows, exclusively to acquire A's own interest, and A incurs $5,000 interest. A's interest deduction is **$5,000**, without another ownership-share reduction. In the second alternative, A and B jointly borrow to acquire the whole property and incur $5,000 shared interest; A's ordinary equal share is **$2,500**. Do not claim both alternatives for the same loan. [TR 2026/1 paragraphs 72-75](https://www.ato.gov.au/law/view/document?docid=TXR/TR20261/NAT/ATO/00001).

```oa-check
name: Co-owner acquisition interest versus jointly incurred interest
inputs:
  interest_incurred: 5000
  ownership_fraction: 0.5
steps:
  sole_acquisition_claim: interest_incurred
  shared_interest_claim: interest_incurred * ownership_fraction
expected:
  sole_acquisition_claim: 5000
  shared_interest_claim: 2500
```

## When to refuse or refer

### Section 7 -- Prohibitions

Use these topical refusal codes in the working paper; they are workflow controls, not statutory classifications. There is no monetary safe harbour: every rental result requires qualified review, with these issues flagged regardless of amount.

| Code | Trigger | Required output |
| --- | --- | --- |
| R-AU-RP-1 | Year, entity, residence, legal shares or operative law unresolved | Needs Input: establish the taxpayer, period and legal ownership before computing the rental result. |
| R-AU-RP-2 | Private use, holiday purpose, genuine availability, area or rent terms unsupported | Needs Input: establish deductible use and the section 26-50 position before apportioning expenses. |
| R-AU-RP-3 | Borrowing/redraw/repayment purpose cannot be traced | Needs Input: obtain the loan-use reconciliation; do not deduct principal or assume all interest is rental interest. |
| R-AU-RP-4 | Repair/capital, asset history, life, method or construction base unsupported | Needs Input: obtain the asset and work evidence before selecting the deduction or cost-base treatment. |
| R-AU-RP-5 | Main residence, foreign residence, estate, development, GST, future exception or state-law question unresolved | Refer: obtain the applicable specialist analysis and evidence before taking the tax position. |
| R-AU-RP-6 | Filing fields, certificate, payment reference, deadline or assessment cannot be verified | Needs Input: verify the relevant year's official instructions and notice before lodging or paying. |

Do not claim travel or second-hand decline where the statutory denial applies; apply the exceptions rather than a universal prohibition. Do not deduct private costs, principal, unsupported construction amounts or the same expense twice. Apply the Div 43 cost-base adjustments with their date and amendment-period conditions. Calculate any preserved foreign-resident CGT discount from the full history. Label all tax calculations as estimates pending qualified review. Mark unresolved inputs and treatments as Needs Input; do not present them as definitive tax results.


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

This version is maintained in the [ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants). The upstream website does not publish or verify this fork's changes. Check the version, Tier 2 status, sources and unresolved items for the requested period.

> Contributed by Ryan Duguid.



## Filing and payment

### Section 5 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Form | Individual Tax Return (ITR) -- Rental Property Schedule (Item 21) |
| Reporting | Per-property basis (complete separate schedule for each property) |
| Joint ownership | Each co-owner reports their share (typically 50/50 for joint tenants) |
| Records retention | Keep the rental records for the required 5-year period, with the relevant start date and any longer asset, loss, amendment or dispute period. The 2025-26 myTax Rent instructions specify 5 years from 31 October 2026, or later lodgment, rather than reducing the period by lodging early. Keep depreciating-asset records for 5 years from the date of your last claim for the decline in value of the asset. CGT records continue until 5 years after it becomes certain no relevant further CGT event can happen under s 121-25. Keep loss records until the period of review for the year fully using the loss ends, and dispute records for **5 years after the dispute is resolved**. [ATO rental records](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/records-for-rental-properties-and-holiday-homes); [s 121-25](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/121-25) |
| Quantity surveyor report | Recommended for all post-1985 properties to substantiate Div 43 and Div 40 claims |

### Individual filing sequence and year boundary

1. Reconcile each property's gross income, legal ownership share, expense categories and separate Div 40/43 schedules. Retain the evidence, loan reconciliation and review decisions. The ordinary self-lodgment date is **31 October**; a registered agent's actual lodgment programme or a granted deferral can differ. Verify that year's due date rather than carrying it forward. [ATO, myTax access and lodging](https://www.ato.gov.au/individuals-and-families/your-tax-return/how-to-lodge-your-tax-return/lodge-your-tax-return-online-with-mytax).
2. For an authorised individual filing, sign in to **myGov**, select the linked **ATO** service and **Manage tax returns**, then select the correct year. A tax agent uses their authorised agent/software route. This guide's field sequence below is verified for **myTax 2026, 2025-26 only**; 2026-27 forms and software labels are not verified.
3. In Personalise, select the Australian investment/property income option and **Rent (Australian properties)**. In Prepare, use the Rent section's **Add/Edit** and add each property, its address, first available date, rented weeks and ownership share. Enter the property's gross receipts and expense categories in the specified total/share fields; check the resulting share calculations. Do not enter a net agent deposit as gross rent or add another co-owner's share to your own. [ATO, myTax 2026 Rent](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/australian-income-or-losses-from-investments-or-property/rent).
4. Reconcile the capital-allowance/depreciation entries and capital works separately. The low-value-pool deduction is reported in its separate deduction section; foreign property uses the foreign-income section. Record tax-affairs fees in their proper category. Save each property, then **Save and continue**. Paper Item 21 is the 2025-26 Rent item; verify any required rental schedule and its current labels for the actual lodgment method.
5. Have the qualified reviewer check the complete return, not only the rental schedule. Review the estimate, declarations and evidence; an estimate is not the final assessment. After authorised lodgment, save the lodged return, receipt and reference. The ATO's myTax page states a lodgment receipt is emailed. Check processing rather than submitting a duplicate return.
6. Review the **notice of assessment (NOA)** in the myGov Inbox and reconcile any statement of account. The NOA or statement gives the amount due, payment advice and due date. For BPAY, use ATO biller code **75556**, the payment reference number (PRN) for the correct tax account and the amount and due date on the actual advice. Allow up to **4 business days** for receipt and processing. ATO online services also provide official payment options; do not substitute a tax file number, another account's reference or the lodgment receipt. [ATO, NOA](https://www.ato.gov.au/individuals-and-families/your-tax-return/your-notice-of-assessment); [ATO, How to pay](https://www.ato.gov.au/individuals-and-families/paying-the-ato/how-to-pay); [ATO, Pay with BPAY](https://www.ato.gov.au/individuals-and-families/paying-the-ato/how-to-pay/pay-with-bpay). This guide does not execute a lodgment or payment.
7. If a figure is wrong, use the amendment route within the applicable period or obtain objection advice. The ATO describes a general **2-year** individual period beginning the day after the NOA is sent, with exceptions; it separately states **4 years** for sole traders from 2024-25. Do not assume all landlords have the same period or reproduce the general webpage's date example without checking the applicable law. See `au-amending-individual-income-tax-return-period.md` and [ATO amendment limits](https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments).
8. A tax bill or rental investment income can also affect PAYG instalments. Follow the current notice and `au-payg-instalments.md`; a rental loss does not automatically cancel instalments. If a deadline is missed or payment cannot be made, contact the ATO/agent promptly and verify any deferral, payment arrangement, penalty or interest decision. [ATO, If you don't lodge](https://www.ato.gov.au/individuals-and-families/financial-difficulties-and-disasters/if-you-don-t-lodge). Current penalty-unit amounts, GIC rates and taxpayer-specific remission outcomes are not confirmed in this guide.

## Completion checklist

- [ ] Identify the taxpayer, year, legal shares, residence and genuine use; resolve all refusal triggers.
- [ ] Reconcile gross rent to owner/agent receipts and refundable/retained bonds; document each co-owner's share.
- [ ] Separate immediate expenses, borrowing expenses, asset decline and capital works; trace loan use and reject duplicate/private costs.
- [ ] Apply holiday/leisure, repair, second-hand asset, construction-date and remaining-expenditure conditions.
- [ ] Screen estate, development, GST, state tax, main residence, foreign residence, FRCGW and enacted future-law issues.
- [ ] Recompute the calculations and check the relevant year's official fields, assessment and payment deadline/reference.
- [ ] Produce the workflow base's working papers, reviewer brief, action list and review checklist. Extend the property register with ownership/use dates, loan movements, asset/Div 43 history, cost-base adjustments, evidence and unresolved items. No taxpayer-specific filing, payment or election is authorised by this guide.
- [ ] Record reviewer decisions and retain supporting records for the applicable period. Version 1.9 corrects conditional rules and adds executable cases; Tier 2 does not certify a person's return.

## Sources

Read dates below concern the stated passages, including separately identified independent reading. A successful capture is not a complete page, Act, ruling, PDF or taxpayer review. The period of a form is stated explicitly.

| Source | URL | Read on and scope |
| --- | --- | --- |
| Rental properties guide 2026  /  Australian Taxation Office | <https://www.ato.gov.au/forms-and-instructions/rental-properties-2026> | 2026-11-04; selected passages only: Landing substantive text |
| Tax rates – Australian resident  /  Australian Taxation Office | <https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents> | 2026-11-04; 2026-27 bands and comparison with 2025-26, not a complete personal tax calculation |
| Tax Reform No. 1 Act 2026 | <https://www.legislation.gov.au/C2026A00049/asmade/text> | 2026-11-04; independent reader: commencement, Schedule 2 and selected Schedule 1 Division 102 amendments, not the whole Act |
| Tax reform – Boosting home ownership – Reforming negative gearing and capital gains tax  /  Australian Taxation Office | <https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax> | 2026-11-04; selected passages only: Whole short substantive reformnotice |
| Tax Reform No. 2 Act 2026 | <https://www.legislation.gov.au/C2026A00071/asmade/text> | 2026-11-04; independent reader: commencement and complete Schedule 4, not the whole Act |
| Tax Reform No. 3 Bill status | <https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554> | 2026-11-04; status, progress, text/amendment links and committee note; full amendment history unresolved |
| Retained original citation | <https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf> | Not read in this correction; retained provenance only |
| Common property expenses  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/common-property-expenses> | 2026-11-04; selected deduction, strata, land-tax and borrowing passages |
| Legal database - View: Principal legislation: SECTION 25-25 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-25> | 2026-11-04; operative subsections (1)-(6), including day method and eligible $100 aggregate |
| TR 97/23  /  Legal database | <https://www.ato.gov.au/law/view/document?docid=TXR/TR9723/NAT/ATO/00001> | 2026-11-04; selected paragraphs 1-10 and 12-58; not the whole ruling |
| Repair and maintenance expenses  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/repair-and-maintenance-expenses> | 2026-11-04; repair introduction, initial-repair and entirety examples |
| Retained original citation | <https://www.legislation.gov.au/F2025L01097/asmade> | Not read in this correction; retained provenance only |
| Second-hand depreciating assets  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/depreciating-assets-in-rental-properties/second-hand-depreciating-assets> | 2026-11-04; selected transition and exception passages; section 40-27 read separately |
| What's new in the rental properties guide?  /  Australian Taxation Office | <https://www.ato.gov.au/forms-and-instructions/rental-properties-2026/whats-new-in-the-rental-properties-guide> | 2026-11-04; substantive reform, effective-life, FRCGW and TR/PCG notices |
| Interest expenses  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/interest-expenses> | 2026-11-04; selected nexus, private-borrowing, proportionate-repayment and ownership examples |
| TR 2000/2  /  Legal database | <https://www.ato.gov.au/law/view/document?docid=TXR/TR20002/NAT/ATO/00001> | 2026-11-04; paragraphs 12-25, including repayment/recoupment/refinancing and monthly-average conditions |
| Legal database - View: Principal legislation: SECTION 110-45 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-45> | 2026-11-04; selected passages only: 110-45relevantDiv43cost-baseprovisions |
| Legal database - View: Principal legislation: SECTION 110-55 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-55> | Captured; substantive read scope not established here, retained provenance only |
| TD 2005/47  /  Legal database | <https://www.ato.gov.au/law/view/document?docid=TXD/TD200547/NAT/ATO/00001> | 2026-11-04; selected passages only: TD2005/47operative1-5andselectedexamples |
| PS LA 2006/1 (GA)  /  Legal database | <https://www.ato.gov.au/law/view/document?docid=PSR/GA20061/NAT/ATO/00001> | 2026-11-04; selected passages only: PSLA2006/1GAoperative1-3andselectedexample |
| Legal database - View: Principal legislation: SECTION 104-235 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-235> | 2026-11-04; selected passages only: 104-235K7trigger,timing,104-240/245crossreferences;notamountformulafullreview |
| Foreign resident capital gains withholding  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding> | 2026-11-04; selected passages only: Landingonly;historic/currentoperativeFRCGWfullbodyfurtherneeded |
| Legal database - View: Principal legislation: SECTION 121-25 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/121-25> | 2026-11-04; selected passages only: 121-25completeoperativeprovisions |
| Records for rental properties and holiday homes  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/records-for-rental-properties-and-holiday-homes> | 2026-11-04; record requirements, start dates and loss/amendment/dispute conditions |
| Rental income you must declare  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-income-you-must-declare> | 2026-11-04; selected domestic arrangements, gross receipts, agent-receipt year and ownership passages |
| Legal database - View: Principal legislation: SECTION 26-50 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/26-50> | 2026-11-04; selected passages only: 26-50completeoperativeconditions |
| How to claim rental expenses  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/how-to-claim-rental-expenses> | Captured; substantive read scope not established here, retained provenance only |
| Revenue NSW  /  Revenue NSW | <https://www.revenue.nsw.gov.au/> | 2026-11-04; selected passages only: Landing identity and selected introduction only; no state rates checked |
| Home  /  State Revenue Office | <https://www.sro.vic.gov.au/> | 2026-11-04; selected passages only: Landing identity and selected introduction only; no state rates checked |
| State taxes, grants and royalty - Queensland Revenue Office | <https://qro.qld.gov.au/> | 2026-11-04; selected passages only: Landing identity and selected introduction only; no state rates checked |
| Department of Treasury and Finance | <https://www.wa.gov.au/organisation/department-of-treasury-and-finance> | 2026-11-04; selected passages only: Landing identity and selected introduction only; no state rates checked |
| RevenueSA  /  RevenueSA | <https://www.revenuesa.sa.gov.au/> | 2026-11-04; selected passages only: Landing identity and selected introduction only; no state rates checked |
| State Revenue Office  /  State Revenue Office Tasmania | <https://www.sro.tas.gov.au/> | 2026-11-04; selected passages only: Landing identity and selected introduction only; no state rates checked |
| Home - ACT Revenue Office | <https://www.revenue.act.gov.au/> | 2026-11-04; selected passages only: Landing identity and selected introduction only; no state rates checked |
| Territory Revenue Office (TRO)  /  Department of Treasury and Finance | <https://treasury.nt.gov.au/dtf/territory-revenue-office> | 2026-11-04; selected passages only: Landing identity and selected introduction only; no state rates checked |
| Medicare levy surcharge income, thresholds and rates  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates> | 2026-11-04; 2026-27 full threshold tiers and family additions, with selected 2025-26 comparison |
| Linked primary context | <https://www.legislation.gov.au/C2004A05138/latest/text> | Not read in this correction; linked context only, not a verified complete source |
| Legal database - View: Principal legislation: SECTION 43-25 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-25> | 2026-11-04; operative rate categories |
| Legal database - View: Principal legislation: SECTION 43-145 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-145> | 2026-11-04; use table and selected build-to-rent conditions |
| Legal database - View: Principal legislation: SECTION 40-425 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-425> | 2026-11-04; selected low-cost, low-value and $300 exclusions |
| Legal database - View: Principal legislation: SECTION 40-435 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-435> | 2026-11-04; operative pool taxable-use percentage and excluded-purpose rules |
| Legal database - View: Principal legislation: SECTION 40-80 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-80> | 2026-11-04; subsection (2), all 4 immediate-deduction conditions |
| Tax Reform No. 3 Bill, introduced Schedule 5 | <https://parlinfo.aph.gov.au/parlInfo/search/display/display.w3p;db=LEGISLATION;id=legislation%2Fbills%2Fr7554_first-reps%2F0005;query=Id%3A%22legislation%2Fbills%2Fr7554_first-reps%2F0000%22;rec=0> | 2026-11-04; independent reader: introduced Schedule 5, proposed definitions and exceptions; amendment completeness unresolved |
| Legal database - View: Principal legislation: SECTION 25-5 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/25-5> | 2026-11-04; subsections (1)-(2), selected tax-affairs conditions |
| Legal database - View: Principal legislation: SECTION 26-31 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/26-31> | 2026-11-04; operative business, entity and member exceptions |
| Legal database - View: Principal legislation: SECTION 40-95 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-95> | 2026-11-04; effective-life choice, start time, 5-year and older-plant conditions; not every associate/rollover provision |
| Legal database - View: Principal legislation: SECTION 40-70 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-70> | 2026-11-04; 150% diminishing-value formula, base, days and cap |
| Legal database - View: Principal legislation: SECTION 40-72 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-72> | 2026-11-04; post-9 May 2006 200% diminishing-value formula and cap |
| Legal database - View: Principal legislation: SECTION 40-75 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-75> | 2026-11-04; ordinary prime-cost formula and adjustment introduction |
| Legal database - View: Principal legislation: SECTION 40-27 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-27> | 2026-11-04; operative subsections (1)-(6), including member, 6-month new-premises and pool conditions |
| Legal database - View: Principal legislation: SECTION 40-430 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-430> | 2026-11-04; operative pool commitment rules |
| Legal database - View: Principal legislation: SECTION 40-440 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-440> | 2026-11-04; operative pool formula and balance |
| Legal database - View: Principal legislation: SECTION 43-140 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-140> | 2026-11-04; complete use table and notes |
| Legal database - View: Principal legislation: SECTION 43-10 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-10> | 2026-11-04; deduction prerequisites |
| Legal database - View: Principal legislation: SECTION 43-20 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-20> | 2026-11-04; operative works and structural-improvement date categories |
| Legal database - View: Principal legislation: SECTION 43-30 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-30> | 2026-11-04; completion requirement |
| Legal database - View: Principal legislation: SECTION 43-70 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-70> | 2026-11-04; construction-expenditure exclusions |
| Legal database - View: Principal legislation: SECTION 43-80 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-80> | 2026-11-04; construction-expenditure area conditions |
| Legal database - View: Principal legislation: SECTION 118-185 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-185> | 2026-11-04; operative partial main-residence formula and foreign-resident conditions |
| Legal database - View: Principal legislation: SECTION 118-192 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-192> | 2026-11-04; first-income-use market-value reset conditions |
| Legal database - View: Principal legislation: SECTION 118-145 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-145> | 2026-11-04; operative absence conditions |
| Legal database - View: Principal legislation: SECTION 118-110 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-110> | 2026-11-04; main-residence conditions and foreign-resident life events |
| Legal database - View: Principal legislation: 40-35 | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/40-35> | 2026-11-04; ordinary residential rent, including new residential premises |
| Legal database - View: Principal legislation: 40-65 | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/40-65> | 2026-11-04; residential sales and new/commercial residential exceptions |
| Legal database - View: Principal legislation: 40-70 | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/40-70> | 2026-11-04; residential long-term leases |
| Legal database - View: Principal legislation: 9-5 | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/9-5> | 2026-11-04; taxable-supply prerequisites |
| Legal database - View: Principal legislation: 38-325 | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/38-325> | 2026-11-04; going-concern conditions |
| Legal database - View: Principal legislation: 75-5 | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/75-5> | 2026-11-04; subsections (1)-(2), including written agreement; full ineligible-acquisition list not read |
| PCG 2026/2  /  Legal database | <https://www.ato.gov.au/law/view/document?docid=COG/PCG20262/NAT/ATO/00001> | 2026-11-04; paragraphs 1-17 and 21-43, with selected paragraph 44; image formulas not fully extracted |
| TR 2026/1  /  Legal database | <https://www.ato.gov.au/law/view/document?docid=TXR/TR20261/NAT/ATO/00001> | 2026-11-04; selected operative paragraphs 20-48 and 72-75, and Appendix 2 paragraphs 137-140; not the whole ruling |
| PCG 2026/3  /  Legal database | <https://www.ato.gov.au/law/view/document?docid=COG/PCG20263/NAT/ATO/00001> | 2026-11-04; selected risk-zone passages and paragraphs 7-18; not a complete example review |
| IT 2622  /  Legal database | <https://www.ato.gov.au/law/view/document?docid=ITR/IT2622/NAT/ATO/00001> | 2026-11-04; selected paragraphs 1-18, including interim distributions and present entitlement; not the whole ruling |
| Legal database - View: Principal legislation: SECTION 128-15 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/128-15> | 2026-11-04; subsections (1)-(5), death transfer, acquisition and cost-base conditions; not the whole estate regime |
| Legal database - View: Principal legislation: SECTION 43-15 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/43-15> | 2026-11-04; deduction caps and 25/40-year limits |
| Lodge your tax return online with myTax  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/your-tax-return/how-to-lodge-your-tax-return/lodge-your-tax-return-online-with-mytax> | 2026-11-04; myGov/ATO access sequence, deadline and emailed receipt |
| Linked primary context | <https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/australian-income-or-losses-from-investments-or-property/rent> | 2026-11-04; myTax 2026, 2025-26 period, property, ownership, receipt, expense, saving and record instructions; no live filing |
| Your notice of assessment  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/your-tax-return/your-notice-of-assessment> | 2026-11-04; assessment, payment advice and statement-of-account fields |
| How to pay  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/paying-the-ato/how-to-pay> | Captured payment landing only; specific BPAY instructions read separately |
| Pay with BPAY  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/paying-the-ato/how-to-pay/pay-with-bpay> | 2026-11-04; independent reader: biller code, PRN reference field and up to 4 business days to reach the ATO account; replaces the former how-to-pay/bpay URL, which returned 404 |
| Time limits on tax return amendments  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments> | 2026-11-04; general individual and sole-trader periods; webpage date example not adopted |
| If you don't lodge  /  Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/financial-difficulties-and-disasters/if-you-don-t-lodge> | 2026-11-04; contact, lodgment and penalty warning; no taxpayer-specific remission outcome |
| Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025, Table A | <https://www.legislation.gov.au/F2025L01097/asmade/2025-09-15/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-04; selected Table A class 67110 effective-life rows and instrument metadata; not the whole determination |
| Foreign resident capital gains withholding overview | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview> | 2026-11-04; historic/current rates, contract dates, valuation and excluded transactions |

Not yet confirmed: The full law/amendment and Ministerial-determination history; complete House amendment history for Bill r7554 (only the introduced Schedule 5 and listed rejected divisions are verified); 2026-27 return/schedule/software labels and live portal behaviour; all state rates, surcharge/vacancy/short-stay regimes; case-specific key money/lease-premium treatment; taxpayer-specific business, repair, use, asset and construction classifications; all non-resident rent collection/garnishee exceptions; full K7 formula and foreign-discount histories; current penalty units, GIC, remission, objections and all filing/payment exceptions; complete source-page/PDF review and independent professional approval for a taxpayer. The retained explanatory-memorandum PDF was not opened in this correction. Captured but unread source passages are not certified.

The standard closing below links to the upstream service. It does not identify a professional reviewer for this fork or establish that the fork's content is current.

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
