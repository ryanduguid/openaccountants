---
name: au-capital-gains
description: "Use this skill for any Australian capital gains tax question, for any entity type. Trigger on: \"CGT Australia\", \"capital gains Australia\", \"sell shares Australia\", \"50% CGT discount\", \"cost base Australia\", \"capital loss\", \"carry forward capital losses\", \"small business CGT concessions\", \"SBCGT\", \"active asset test\", \"15-year exemption\", \"retirement exemption CGT\", \"CGT rollover\", \"CGT event A1\", \"main residence exemption\", \"Australian CGT\", \"sell my Australian company\", \"dispose of property Australia\", \"CGT indexation from 2027\". Covers the calculation workflow from CGT event and cost base through losses, discounts and concessions, entity and residency differences, and the enacted 1 July 2027 changes. Routes to au-small-business-cgt, au-nonresident-cgt, au-rental-property and au-crypto-tax for their specialist rules."
version: 1.10
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 core computations; historical periods and enacted 2027-28 changes require their own operative sources and conditions"
last_updated: 2026-11-02
review_status: pending_review
depends_on:
  - workflow-base
  - au-individual-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Capital Gains Tax v1.10

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### Australia Capital Gains Tax v1.10

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.
>
> **Enacted change from 1 July 2027.** The 50% CGT discount for individuals, trusts and
> partnerships is replaced by cost base indexation with a 30% minimum tax rate on capital gains.
> Eligible assets may be deemed sold just before, and reacquired on, 1 July 2027. Deferred gains,
> new dwellings, affordable housing and foreign or temporary residence have separate conditions.
> Do not assume every asset receives a market-value reset or retains a 50% discount. Residential rental losses are
> quarantined from 2027-28 unless the property was acquired before 7:30 pm on 12 May 2026 or is a
> new residential dwelling. Both measures are law. See Section 9 before advising on any disposal
> planned for 2027-28 or later.
> [ATO, Reforming negative gearing and capital gains tax](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax)

This guide prepares CGT working papers for a qualified Australian reviewer. It covers event identification, ordinary disposal calculations, loss allocation and eligibility for discounts or concessions. It does not calculate final income tax, determine disputed ownership or valuations, approve an election or lodge a return. Use the specialist guides for property, foreign residence, crypto, small business concessions and trust distributions. Load `workflow-base` and `au-individual-return` for engagement workflow and return assembly.

**Period and source condition.** The 6 computational cases below use 2026-27 facts. Current compilation 268 of the ITAA 1997 was checked on 2 November 2026 for the named provisions in Sources. An editing date does not establish every rule's currency. Verify the requested period's law, application provisions, amendments and return instructions before an engagement computation. Section 9 records conditional future rules and unresolved points; it does not authorise an automated 2027-28 position.

## Ask the client first

- What entity and beneficial owner holds each asset, and in what proportions? Establish capital, trading-stock or other revenue treatment before calculating CGT.
- What acquisition, contract and disposal dates, previous-owner periods, rollover choices and receipt records apply? Identify the event rather than assuming every receipt is A1.
- What proceeds, AUD conversion evidence, first-element amount, incidental costs, ownership costs, improvements, capital works and recoupments support each parcel?
- What is the full tax-residency history, including foreign or temporary residence after 8 May 2012? For a dwelling, obtain main-residence and income-use dates and any required valuation.
- What current-year losses and unused prior-year losses exist, separated by origin year, collectable status, entity and restrictions? Obtain prior returns and evidence of use, ownership or business continuity and bankruptcy where relevant.
- Which exemptions, Division 152 conditions, retirement facts, lifetime-limit usage, replacement assets and written elections are supported? Confirm withholding certificates, requested income year and any 1 July 2027 transition facts.
- Which source conditions, legal classifications or facts remain unresolved? Confirm the inferred profile under the workflow base before engagement calculations.

## The method, step by step

### AU Capital Gains

### Section 1 - Quick Reference

**Quick reference table**

| Field | Value | Primary source |
| --- | --- | --- |
| Country | Australia | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) |
| Income year covered | 2026-27 (1 July 2026 to 30 June 2027) | 2026-27 computation scope; verify requested period |
| CGT rate | No separate rate. The net capital gain is included in assessable income and taxed at the entity's rate | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) s 102-5 |
| Incremental top-rate illustration | 23.5% only if the whole taxable half is in the 45% bracket, the ordinary 2% Medicare levy applies and no other tax interaction changes the result; calculate actual tax separately | [Resident rates](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents); `au-medicare-levy.md` |
| 50% general discount | Eligible individuals and trusts, at least 12 months under s 115-25, for events before 1 July 2027; residence and event exclusions apply | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) ss 115-25, 115-100 |
| Complying superannuation fund discount | Exactly one-third (33 1/3%) | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) s 115-100(b) |
| Companies | Ordinary companies have no general discount; a life insurance company can have a discount gain on a complying superannuation asset under s 115-10(d) | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) s 115-10 |
| Annual tax-free amount | None. Australia has no annual CGT exemption | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) s 102-5 |
| Personal use gain exemption | First-element cost $10,000 or less; personal use losses are disregarded regardless of cost; collectables are separate | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) ss 118-10(3), 108-20 |
| Collectable exemption | First-element cost $500 or less; test interests and sets separately | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) ss 118-10(1)-(2), 108-15 |
| CGT small business gateways | Aggregated turnover below $2 million for the CGT small business entity gateway, or maximum net asset value not exceeding $6 million; other statutory pathways and conditions can apply | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) ss 152-10, 152-15 |
| Active asset test period | At least half the test period if owned 15 years or less; at least 7.5 years if owned more than 15 years | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) s 152-35 |
| 15-year exemption | 15 years of continuous ownership plus the relevant basic and significant-individual conditions; age 55 or over and connection with retirement, or permanent incapacity | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) ss 152-105, 152-110 |
| Retirement exemption | $500,000 lifetime limit per individual; required super contribution where under 55, subject to entity-specific timing and choice rules | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) ss 152-305, 152-315, 152-325 |
| Foreign-resident main-residence life-events test | Continuous foreign residence of 6 years or less plus a qualifying event; not a time-only exemption | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) s 118-110 |
| Foreign resident capital gains withholding | 15% for Australian real-property contracts from 1 January 2025, no value threshold; certificate, variation and other conditions in Section 8 | [ATO, withholding](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding) |
| Foreign-resident regime from 1 October 2026 | Principal asset test includes the preceding 365 days; specified $50 million or more not-TAP declarations require at least 28 days notice; eligible renewable-energy discount is 50% before 1 July 2040 | [Act No. 86 of 2026, Schedules 2-3](https://www.legislation.gov.au/C2026A00086/asmade/text); Section 8 |
| Active asset reduction | 50% of the remaining eligible gain after losses and general discount; taxpayer can choose not to apply it | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) ss 152-205, 152-220 |
| Affordable housing discount | Additional discount up to 10 percentage points, giving up to 60% for a qualifying resident individual; all use-period and provider conditions apply | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) s 115-125; Section 6 |
| Main residence land area | At most 2 hectares including land under the dwelling; adjacent land must satisfy the private-use and other conditions | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) s 118-120; Section 3 |
| Non-widely-held entity screen | Fewer than 300 members triggers the specific share or trust-interest discount tests, not automatic denial in every case | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) ss 115-45, 115-50; Section 6 |
| Primary legislation | ITAA 1997 Parts 3-1 and 3-3 | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/latest/text) |
| Tax authority | Australian Taxation Office | [ATO, calculating CGT](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt) |
| Where reported | Capital gains item in the return, with a CGT schedule where required | [ATO, how to calculate CGT](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/how-to-calculate-your-cgt) |
| Reviewed by | Pending. Australian CPA or CA review required | Workflow control; professional review not obtained |

### Section 2 - The calculation workflow

Use this sequence for 2026-27. A disregarded gain or loss leaves the calculation at the exemption step. From 2027-28, verify Section 9 and the application provisions first; do not reuse the loss-allocation choice without the enacted gain-category ordering.

**Step 1. Identify the CGT event and its date.**
A CGT event, not a payment, triggers CGT. For a disposal under a contract, the event happens at
the contract date, not settlement. This determines the income year, the 12-month holding test and
the residency position.

**Step 2. Check whether the asset or the gain is exempt.**
Test the actual exemption conditions for each event. A main residence can be partly taxable, and foreign residence can deny its exemption. A car or motorcycle is generally outside CGT. A personal use asset's gain is disregarded when its first-element cost is $10,000 or less; its loss is disregarded regardless of cost. Collectables have a separate $500 first-element threshold, with special rules for interests and sets. Pre-CGT acquisition does not exempt every later event. Apply the specific compensation, gambling or depreciating-asset rule rather than treating a category label as proof.

**Test the small business 15-year exemption here, before allocating capital losses or discounting.** A gain qualifying under Subdivision 152-B is disregarded entirely; it does not use losses or enter the net-capital-gain calculation. Verify all basic, ownership, significant-individual and retirement or incapacity conditions with `au-small-business-cgt.md`. [ITAA 1997 ss 118-5, 118-10, 108-15, 108-20 and Subdivision 152-B](https://www.legislation.gov.au/C2004A05138/latest/text).

**Step 3. Work out the cost base or reduced cost base.**
Use the cost base for a gain and the reduced cost base for a loss. See Section 4.

**Step 4. Calculate the gross gain or loss per asset.**
For an ordinary A1 disposal, a gain is the excess of capital proceeds over cost base; a loss is the excess of reduced cost base over proceeds. Proceeds between the two produce neither. Do not report a negative cost-base calculation as a capital loss. Other events have their own formulas: for example, D1 compares proceeds with incidental costs. [ITAA 1997 ss 104-10, 104-35](https://www.legislation.gov.au/C2004A05138/latest/text).

**Step 5. Apply capital losses.**
Exclude disregarded amounts and ring-fence collectable losses. Apply available current-year losses first, then eligible unused net capital losses from earlier years, oldest year first, before discounting. For 2026-27 you can choose which eligible gains to reduce; test non-discount gains first. Do not discount a gain before using an available loss. Check entity and bankruptcy restrictions. [ITAA 1997 ss 102-5, 102-15, 108-10](https://www.legislation.gov.au/C2004A05138/latest/text).

**Step 6. Apply the discount, if available.**
See Section 6 for the entity and residency tests.

**Step 7. Apply concessions.**
Apply the remaining eligible Division 152 concessions: active asset reduction, unless validly chosen out, then retirement exemption and/or small business rollover. The 15-year exemption was tested at Step 2. Other rollovers and event-specific relief have their own conditions and timing; do not postpone every rollover decision until here. See `au-small-business-cgt.md`.

**Step 8. Report the net capital gain.**
Include the net capital gain in assessable income. A net capital loss cannot reduce salary or other ordinary income. Carry forward eligible unused losses by origin year and restriction; there is no ordinary expiry period, but entity continuity, bankruptcy and other restrictions can prevent use. Verify the requested year's return item, CGT schedule requirements and reporting precision. This guide does not calculate final tax or approve lodgment.

### Section 3 - What triggers CGT

**Common CGT events**

| Event | What it is |
| --- | --- |
| A1 | Disposal of a CGT asset by sale, gift or transfer |
| B1 | Use and enjoyment before title passes |
| C1 | Loss or destruction of an asset |
| C2 | Cancellation, surrender or expiry of a right or option |
| D1 | Creation of a contractual or other right |
| E4 | Capital payment from a trust exceeding the cost base of the interest |
| G1 | Return of capital on shares exceeding the cost base |
| I1 and I2 | Ceasing to be an Australian resident |
| K6 | Pre-CGT shares or trust interests where post-CGT property dominates |

- **Multiple events** — More than one event can apply to the same transaction. Where that happens, the most specific event generally prevails.
- **CGT assets** — CGT assets include land and buildings, shares and units, goodwill, contractual rights, options, crypto assets, foreign currency and leases.
- **A gift is a disposal** — A gift is a disposal. Where parties are not dealing at arm's length, or where no consideration passes, the market value substitution rule replaces the actual proceeds with market value.
- **Capital versus revenue** — Establish whether the profit is on capital or revenue account before applying CGT. A trading business or an isolated profit-making transaction produces ordinary income, and section 118-20 reduces a capital gain to the extent the amount is otherwise assessable, so the same profit is not taxed twice. Holding an asset for more than a year does not by itself make it a capital investment.  _(ITAA 1997 (Cth) s 118-20, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-20)_
- **Main residence conditions** — The main residence exemption depends on the dwelling being the taxpayer's home, land of two hectares or less, the extent of any income-producing use, the absence rule and residency at the CGT event. A property bought as an investment is not exempt because the owner later moves in: the exemption is apportioned to the days it was the main residence. Check occupation, absences and use before applying it.  _(ITAA 1997 (Cth) s 118-110, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-110; s 118-185, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-185)_

### Section 4 - Cost base and reduced cost base

**The five elements of the cost base**

| Element | Content |
| --- | --- |
| 1 | Money paid, or the market value of property given, to acquire the asset |
| 2 | Incidental costs of acquisition and disposal, such as stamp duty, legal fees, agent commission, valuation and brokerage |
| 3 | Non-capital costs of ownership, such as rates, land tax, insurance and interest, only for assets acquired after 20 August 1991 and only to the extent not deductible |
| 4 | Capital expenditure to increase or preserve the asset's value, or to install or move it |
| 5 | Capital expenditure to establish, preserve or defend title to the asset |

- **The reduced cost base** — The reduced cost base is used to work out a capital loss and has five elements. Elements 1, 2, 4 and 5 match the cost base. Its third element replaces ownership costs with the assessable balancing-adjustment amounts specified in section 110-55(3), including its statutory relief cases. Apply the section's exclusions separately: subsection (4) excludes deductible amounts, including deductible balancing adjustments, and subsection (6) excludes recouped expenditure unless the recoupment is assessable. Do not subtract an assessable balancing adjustment merely because a deductible balancing adjustment is excluded.  _(ITAA 1997 (Cth) s 110-55, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-55)_
- **Deductions reduce the cost base** — Amounts you have deducted or can deduct under Division 43 reduce the cost base of an asset acquired after 7:30 pm on 13 May 1997, and of older land or a building for fourth element expenditure incurred after 30 June 1999, and element 3 excludes anything that was deductible. The reduced cost base is separate: s 110-55(4) excludes an amount you have deducted or can deduct, with no such acquisition date limit. Under TD 2005/47 you can deduct an amount at a particular time if the deduction provision's terms are satisfied and the s 170 ITAA 1936 amendment periods have not expired for that deduction. There is no fixed time for the test, so an unclaimed amount still counts while it can be deducted by amendment, but not once it is out of time, provided you are within the amendment period for the CGT event. PS LA 2006/1 (GA) separately relieves you where you lack sufficient information to determine the construction expenditure and have not sought any deduction for it. This is the most common cost base error on a rental property disposal. See `au-rental-property.md`.  _(ITAA 1997 (Cth) s 110-45, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-45; s 110-55, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-55; [TD 2005/47](https://www.ato.gov.au/law/view/document?docid=TXD/TD200547/NAT/ATO/00001); [PS LA 2006/1 (GA)](https://www.ato.gov.au/law/view/document?docid=PSR/GA20061/NAT/ATO/00001))_
- **Selling costs belong in the cost base, not the proceeds** — Capital proceeds are the money and the market value of property received for the event. Agent commission, legal fees and other disposal costs are second-element cost base amounts. Reconcile proceeds to the contract before adding selling costs to the cost base, otherwise they are counted twice.  _(ITAA 1997 (Cth) s 116-20, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/116-20; s 110-25, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-25)_

### Section 5 - Capital losses

- **Capital loss applied only against capital gains** — A capital loss can be applied only against capital gains, never against ordinary income.
- **Order of losses** — Current year capital losses are applied before prior year losses.
- **Losses before discount** — Losses are applied before any CGT discount. Applying the discount first overstates the benefit of the loss.
- **Choice of which gains to offset** — Where there is a choice, apply losses first against gains that do not qualify for the discount, because a discounted gain loses only half its value to a loss offset.
- **Carry forward of net capital losses** — Net capital losses carry forward indefinitely for individuals. Company and trust loss use is restricted by the continuity of ownership, business continuity and trust loss rules.
- **Personal use asset losses** — Disregard losses on personal use assets. They cannot offset capital gains or carry forward.  _(ITAA 1997 (Cth) s 108-20(1), https://www.ato.gov.au/law/view/document?docid=PAC/19970038/108-20)_
- **Collectable losses** — A collectable loss can offset only collectable gains. Carry any unused amount forward for future collectable gains, subject to the collectable exemption rules.  _(ITAA 1997 (Cth) s 108-10, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/108-10)_
- **Wash sales** — Wash sale arrangements, where an asset is sold and substantially repurchased to crystallise a loss, attract Part IVA attention.

### Section 6 - The discount, and who gets it

**Entity treatment for assets held more than 12 months**

| Entity | Discount | Note |
| --- | --- | --- |
| Australian resident individual | 50% | Applies until 30 June 2027. See Section 9 |
| Australian trust | 50% | The discount flows through to beneficiaries, who must be able to use it in their own right |
| Complying superannuation fund | One-third (33 1/3%) | Use the exact statutory fraction, not a rounded 33.33% input |
| Ordinary company | None | Excludes a life insurance company's complying-superannuation-asset gain, which can receive the statutory one-third discount |
| Foreign or temporary resident | Apportioned | No discount for the part of the gain accruing after 8 May 2012 while a foreign or temporary resident. A period of Australian residency during ownership can support an apportioned discount. For events from 1 July 2027 see the mixed residency row in Section 9 |

- **The 12-month test** — The asset must be owned for at least 12 months before the CGT event, excluding the day of acquisition and the day of the event. Previous ownership can count where the asset was acquired through a deceased estate, through a relationship breakdown rollover, or as a replacement asset under a rollover for a lost, destroyed or compulsorily acquired asset.
- **Exclusions from the discount** — - A home first used for rental or business less than 12 months before disposal. - Where the indexation method is chosen for an asset acquired before 21 September 1999. - A CGT event that creates a new asset, such as granting a lease or a restrictive covenant, because the asset was not held for 12 months. - Certain disposals of interests in companies and trusts with fewer than 300 members. - An income asset converted into a capital asset to access the discount, under Part IVA.
- **Additional affordable housing discount** — An additional discount of up to 10% can apply to individuals who provide eligible affordable rental housing.  _(ATO, CGT discount, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount)_
- **Trust capital gains in a beneficiary's hands** — A beneficiary specifically entitled to a trust capital gain grosses up any discounted or reduced amount under Subdivision 115-C, then applies their own capital losses, discount percentage and concessions. The trust's discount does not settle the beneficiary's net capital gain. See `au-trust-distributions.md`.  _(ITAA 1997 (Cth) s 115-215, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-215)_

### Section 7 - Small business CGT concessions

- **Overview and basic conditions** - Test the 15-year exemption before losses; the other concessions operate on a remaining gain and can reduce it to nil. Full rules are in `au-small-business-cgt.md`. In outline: a CGT event happens to an asset that would otherwise produce a gain, the taxpayer meets a permitted basic-condition gateway and the asset satisfies the active asset test. Additional conditions apply to shares and trust interests.

**The four concessions**

| Concession | Effect | Core condition |
| --- | --- | --- |
| 15-year exemption | The whole qualifying gain is disregarded before losses | Subdivision 152-A basic conditions, 15 years of continuous ownership and the applicable significant-individual and retirement/incapacity tests under ss 152-105 or 152-110 |
| 50% active asset reduction | Halves the remaining gain | Basic conditions only |
| Retirement exemption | Exempts up to a $500,000 lifetime limit per individual | An amount must be paid into superannuation if the individual is under 55 |
| Rollover | Defers the gain | A replacement asset must be acquired, or capital improvement incurred, within the replacement asset period |

- **Order of application** - First disregard a gain covered by the 15-year exemption. For other eligible gains, apply capital losses, then the general discount, then the 50% active asset reduction unless validly chosen out, then the retirement exemption and/or rollover. If both of the last 2 apply, the taxpayer can choose their order. [ITAA 1997 ss 152-1, 152-205 to 152-220](https://www.legislation.gov.au/C2004A05138/latest/text).
- **Gateways and the active asset test period** — The basic conditions are met through a CGT small business entity with aggregated turnover below $2 million, the $6 million maximum net asset value test, or the partnership and passively held asset pathways, counting connected entities and affiliates. The asset must be active for at least half the test period, or 7.5 years where it was owned for more than 15 years. Shares and trust interests carry additional conditions.  _(ITAA 1997 (Cth) s 152-10, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/152-10; s 152-35, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/152-35)_

### Section 8 - Residency, foreign assets and withholding

- **Australian residents** — Australian residents are taxed on worldwide capital gains. A foreign income tax offset may be available for foreign tax paid on the same gain, limited to the Australian tax on that income. See `au-foreign-income.md`.
- **Foreign residents** — Foreign residents are taxed only on taxable Australian property, principally Australian real property, an indirect interest in Australian real property, and assets used in an Australian permanent establishment. See `au-nonresident-cgt.md`.
- **Ceasing residency** — CGT event I1 generally brings unrealised gains and losses to account at market value when an individual or company ceases Australian residency. Section 104-160(3) excludes taxable Australian real property, Australian permanent-establishment assets, and options or rights over those latter two categories (section 855-15 items 1 and 3). Section 104-160(5) separately disregards gains and losses on assets acquired before 20 September 1985. The event does not exclude all taxable Australian property: indirect Australian real-property interests can remain within I1. An individual may choose under section 104-165 to disregard all I1 gains and losses, with affected assets remaining in the Australian CGT net. Event I2 concerns a trust ceasing to be a resident trust. See ITAA 1997 sections 104-160 to 104-175 and `leaving-australia-tax-residency-cgt.md`.  _(ITAA 1997 sections 104-160 to 104-175, https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-160)_
- **Main residence exemption for foreign residents** — A foreign resident at the time of disposal cannot claim the main residence exemption for property sold after 30 June 2020 unless the life events test is satisfied. There is no partial or apportioned exemption in that case, and the home first used to produce income rule is also unavailable. The life events test requires a continuous period of foreign residency of six years or less, plus a terminal medical condition of the taxpayer, spouse or child under 18, the death of a spouse or child under 18, or a CGT event arising from a formal relationship breakdown agreement.  _(ATO, Main residence exemption for foreign residents, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents)_
- **Foreign resident capital gains withholding** — For contracts signed from 1 January 2025, the purchaser must withhold 15% of the market value (normally the sale price; see `au-nonresident-cgt.md` for non-arm's length sales) for all Australian real property, with no value threshold. An Australian resident vendor avoids withholding by giving the purchaser a clearance certificate before settlement. A foreign resident can apply for a variation. The withheld amount is credited against the vendor's assessment.  _(ATO, Foreign resident capital gains withholding, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding)_
- **Foreign resident CGT regime changes from 1 October 2026** — Schedule 2 to the Treasury Laws Amendment (Strengthening Accountability for Tax Adviser Misconduct and Other Measures) Act 2026 (No. 86, assent 15 September 2026) applies to CGT events from 1 October 2026. It broadens taxable Australian real property to include interests in or rights over land, licences, and things fixed or installed on land; applies the principal asset test at the CGT event or at any time in the preceding 365 days; and requires a vendor declaring an interest is not an indirect Australian real property interest to notify the Commissioner at least 28 days before ownership passes where the transaction is $50 million or more. Schedule 3 gives eligible foreign resident companies and trusts a 50% discount on Australian renewable energy assets for events before 1 July 2040. See `au-nonresident-cgt.md`.  _([Act No. 86 of 2026](https://www.legislation.gov.au/C2026A00086/asmade/text); [ATO, Strengthening the foreign resident CGT regime](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime))_

### Section 9 - The changes taking effect on 1 July 2027

- **Changes taking effect on 1 July 2027** — **AUDIT FLASH POINT.** Advice on a disposal straddling 1 July 2027, and on timing a disposal to sit either side of that date, will be examined closely. Part IVA applies to arrangements entered into for the dominant purpose of obtaining a tax benefit. The Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (assent 26 June 2026) and the Income Tax Rates Amendment (Tax Reform No. 1) Act 2026 enact the reforms announced in the 12 May 2026 Budget. Until 30 June 2027 the 50% discount continues on the current tests. **Do not apply the new mechanism to a 2026-27 disposal.**

**How the enacted rules work (Schedule 1 of the Tax Reform No. 1 Act).**

| Element | Rule | Provision |
| --- | --- | --- |
| Deemed sale and reacquisition | An individual for whom s 115-105 would not apply to a discount capital gain from the realisation event, which excludes anyone who was a foreign or temporary resident at any time in the ownership period after 8 May 2012, even if resident again by the event; or a trust with at least one beneficiary who would make a discount capital gain to which s 115-110 or s 115-120 does not apply, unless s 115-102 or s 115-125 applies to all the capital gains attributed to its beneficiaries; holding a post-CGT asset from before 1 July 2027 until a later realisation event is taken to sell it just before 1 July 2027 and reacquire it on 1 July 2027 for its market value, or for an amount worked out under an apportioning method the Minister determines (the choice is made when the return for the realisation year is lodged). | ss 112-155, 112-165, 112-185 |
| Deferred pre-July 2027 gain | The gain or loss on the deemed sale is disregarded until the asset is actually realised, then brought in as a deferred gain or loss. A deferred gain keeps the 50% discount if it would have been a discount capital gain, with the 12-month test applied at the realisation date. | ss 112-160, 112-170, 115-100(aa), (ab) |
| Indexation of the post-July 2027 gain | For CGT events from 1 July 2027, the cost base of an individual's or trust's asset includes indexation of each element except the third, from 1 July 2027 (or later expenditure). An individual must not be a foreign or temporary resident at any time from the later of 1 July 2027 and acquisition until the event. | ss 110-36(1A), 114-25, 960-275(1B) |
| Discount for later gains | 0% for an individual's or trust's gain from an event after 30 June 2027, except new residential dwellings (50%) and qualifying affordable housing (50% plus the extra up to 10%), where indexation can be chosen instead, and subject to the mixed residency row below. Complying super funds keep one-third. | ss 115-100, 115-102, 115-125 |
| Mixed residency after 1 July 2027 | **Unresolved: no ATO guidance found at 31 October 2026. Do not apply a discount outcome without specialist review; escalate.** Individuals: if s 115-105 would apply to a discount capital gain from the realisation event, s 112-155 does not apply, so there is no deemed sale. Trustees: s 112-165 has its own test. Paragraph (d) is met if at least one beneficiary would make a discount capital gain to which s 115-110 or s 115-120 does not apply, even if another beneficiary has mixed residency, but the deemed sale also needs the other s 112-165(1) conditions, and paragraph (e) prevents it where s 115-102 or s 115-125 applies to all the capital gains attributed to the beneficiaries. The text: s 115-100(c) and (d) lack the 1 July 2027 limit in paragraphs (aa) and (ab), Act No. 49 of 2026 does not amend s 115-115, and paragraph (f) gives 0% only if no earlier paragraph applies. That raises, but does not settle, whether a resident-days discount reaches the whole gain. Open points: how a mixed resident beneficiary is treated where the trust has a deemed sale; s 114-25(2), which denies indexation for foreign or temporary residence in its testing period; for someone abroad only before 1 July 2027, s 960-275(1B), which reaches only expenditure incurred on or after 1 July 2027, with the s 115-20(1)(a) unindexed cost base condition and the s 115-20(2) recalculation; and how Division 119 applies. Schedule 4 of the Tax Reform No. 3 Bill would change this outcome (note below). | ss 112-155(1)(d), 112-165(1)(d), 114-25, 115-20, 115-100(c), (d), (f), 115-105, 115-110, 115-115, 115-120, 960-275(1B), Div 119 |
| 30% minimum tax | A resident individual pays extra tax so that the remaining residential and non-residential capital gains, after losses, discounts and small business concessions and reduced by gift deductions, bear at least 30% before offsets. It does not apply in a year the individual receives listed payments such as the age pension, JobSeeker, parenting payment, youth allowance, family tax benefit or parental leave pay. Gains covered by the new-dwelling or affordable-housing discount are excluded. | Div 119 (ss 119-5 to 119-15) |
| Pre-CGT assets | A pre-CGT asset held on 30 June 2027 is deemed sold and reacquired at market value on 1 July 2027, so only the later gain is taxed and the asset stops being pre-CGT. | s 112-175 |
| Loss ordering | Capital losses reduce deferred non-residential gains first, then deferred residential, then non-residential, then residential gains; quarantined negative-gearing amounts reduce residential gains (see `au-rental-property.md`). | s 102-5(1) |
| Small business concessions | Still apply after indexation; the 50% active asset reduction can reduce an indexed gain, and for it the $2 million CGT small business entity limit is disregarded, so a small business entity with aggregated turnover under $10 million qualifies. | ss 152-10(1AA) note 2, 152-205(2) |
| Trusts | Beneficiaries apply their own indexation, discount and minimum-tax position to attributed gains, and trustees must give beneficiaries a statement (with an administrative penalty for failure). | Subdiv 115-C, s 115-235 |

**Bill, not law: Schedule 4 (noted 31 October 2026; selected provisions of the Bill and Explanatory Memorandum read).** For assessments for the income year that includes 1 July 2027 and later income years, Schedule 4 to the Tax Reform No. 3 Bill would:

- extend the deemed sale to any individual who is an Australian resident (not a temporary resident) at any time in the ownership period (replacement s 112-155(1)(d)); set the s 115-115 percentage at 0% for events from 1 July 2027 other than new dwellings and affordable housing (s 115-115(1A)); repeal s 114-25; and pro-rate indexation by resident days (s 960-275(1D), (1E)). The Explanatory Memorandum says a person who stops being resident before 1 July 2027 gets a pro-rated discount on the deferred gain, and one who stops only after that date keeps the full 50% on it. It leaves mixed residents with gains through trusts, and other aspects for foreign, mixed and temporary residents, to later consideration or a further tranche;
- recognise a deferred gain or loss only on a deferral realisation event, which excludes listed CGT events (s 112-152(1)), and apply listed exemptions, including the s 152-105 and s 152-110 15-year exemption, to the deferred gain (s 112-152(2));
- remove the apportioning method for assets with CGT event E4, E10 or G1 cost base adjustments, and for managed investment trusts and attribution managed investment trusts (AMITs) with routine valuation and unit pricing obligations;
- except gains from genuine testamentary trusts and deceased estates, special disability trusts and certain minors' income from the 30% minimum tax, with integrity rules for the first 2; and
- bring AMITs into the regime, let a trustee choose not to index where no beneficiary could benefit (s 110-36A), and let trusts apply the new dwelling and affordable housing discounts (ss 115-103, 115-126).

Schedule 5 would define new residential dwelling in the Act, which also sets the discount at s 115-102 (see `au-rental-property.md`). Status: Treasury Laws Amendment (Tax Reform No. 3) Bill 2026 and Income Tax Rates Amendment (Minimum Tax on Discretionary Trusts) Bill 2026: introduced 14 October 2026, passed the House 29 October 2026, referred to the Senate Economics Legislation Committee (report due 13 November 2026); not law at 31 October 2026. [APH, Bill r7554](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554); [Bill, first reading](https://parlinfo.aph.gov.au/parlInfo/download/legislation/bills/r7554_first-reps/toc_pdf/26132b01.pdf;fileType=application%2Fpdf); [Explanatory Memorandum, ch 4](https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf).

**Before a 2027-28 computation.** Establish whether the asset and taxpayer meet the deemed-sale rules before obtaining or applying a transition valuation. Test deferred-gain discount eligibility, new-dwelling and affordable-housing exceptions, residency and the minimum-tax exclusions separately. Do not assume a 50% discount on every pre-transition gain, no discount on every later gain or a 30% charge on every gain. The mixed-residency issue above remains held for specialist review. _([Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/asmade/text); [Income Tax Rates Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00050/latest))_

## Boundary and exception table

### Section 11 - Common errors

- Using the settlement date instead of the contract date for a property or share disposal.
- Applying the discount before capital losses.
- Offsetting a capital loss against salary or business income.
- Including element 3 ownership costs in the reduced cost base, or including costs that were deductible.
- Failing to reduce the cost base by capital works deductions deducted or deductible on a rental property.
- Claiming the 50% discount for a company, or the full 50% for a complying super fund.
- Claiming the main residence exemption for a foreign resident vendor without testing the life events test.
- Assuming an Australian resident vendor is outside foreign resident capital gains withholding without obtaining a clearance certificate before settlement.
- Treating the 15-year exemption as available on age alone, without the 15 years of continuous ownership and the retirement or incapacity condition.
- Applying the 2027-28 rules to a 2026-27 disposal, or the reverse.

## Worked cases

### Section 10 - Worked example

**Worked example facts**

| Item | Detail |
| --- | --- |
| Asset | Listed shares in one company |
| Acquired | 2 September 2022, for $28,000 plus $95 brokerage |
| Sold | Contract dated 14 March 2027, proceeds $46,000, brokerage on sale $110 |
| Other current year disposal | A second parcel sold at a capital loss of $1,500 |
| Carried forward | Net capital loss of $3,200 from 2024-25 |

**Facts.** Priya holds both parcels on capital account and is an Australian resident individual throughout ownership. No exemption, rollover, other cost-base adjustment or small business concession applies. Her prior loss is supported and unused, and no loss restriction applies. All cases in this section use hypothetical data.

**Step 1, CGT event and date.** CGT event A1 happens at the contract date, 14 March 2027, so the gain falls in the 2026-27 income year.

**Step 2, exemptions.** None apply. Shares are not personal use assets.

**Step 3, cost base.**

```
Element 1  purchase price                        28,000
Element 2  brokerage on acquisition                  95
Element 2  brokerage on disposal                    110
Cost base                                        28,205
```

**Step 4, gross gain.**

```
Capital proceeds                                 46,000
Less cost base                                   28,205
Gross capital gain                               17,795
```

**Step 5, apply losses, current year first.**

```
Gross capital gain                               17,795
Less current year capital loss                    1,500
                                                 16,295
Less prior year net capital loss                  3,200
Gain remaining after losses                      13,095
```

**Step 6, discount.** Priya held the shares from 2 September 2022 to 14 March 2027, which is more than 12 months, and she is an Australian resident. The disposal is before 1 July 2027, so the 50% discount applies.

```
Gain after losses                                13,095
CGT discount at 50%                               6,547.50
Net capital gain included in assessable income    6,547.50
```

**Step 7, report.** The workpaper net capital gain is $6,547.50. Transfer it using the applicable return instructions and precision. Final tax depends on Priya's other income, rates, offsets and Medicare position; no final tax is calculated here.

**Why the order matters.** Applying the 50% discount before the losses would give ($17,795 x 50%) less $4,700, or $4,197.50, understating the net capital gain by $2,350. The losses must come first.

Sources for Case 1: [ITAA 1997 ss 104-10, 110-25, 110-35, 102-5 and 115-100](https://www.legislation.gov.au/C2004A05138/latest/text). Decimal workpaper values below do not prescribe whole-dollar return reporting.

```oa-check
name: AU CGT 2026-27 - Priya losses before discount
inputs:
  purchase: 28000
  buy_brokerage: 95
  sale_brokerage: 110
  proceeds: 46000
  current_loss: 1500
  prior_loss: 3200
steps:
  - cost_base: purchase + buy_brokerage + sale_brokerage
  - gross_gain: proceeds - cost_base
  - after_current: gross_gain - current_loss
  - after_prior: after_current - prior_loss
  - net_gain: after_prior / 2
  - wrong_discount_first: gross_gain / 2 - current_loss - prior_loss
  - understatement: net_gain - wrong_discount_first
expected:
  cost_base: 28205
  gross_gain: 17795
  after_current: 16295
  after_prior: 13095
  net_gain: 6547.50
  wrong_discount_first: 4197.50
  understatement: 2350
```

### Case 2 - Allocate losses to a non-discount gain first

An individual who is an Australian resident throughout ownership holds investments on capital account. In 2026-27, one parcel held for 6 months produces a $6,000 gain and another held for 3 years produces a $20,000 gain. Both gains are supported after all costs. No exemption, other concession or restriction applies. There is a $4,000 current-year capital loss and an eligible unused $3,000 prior-year net capital loss. Apply $4,000 then $2,000 to the non-discount gain, leaving $1,000 prior loss for the discount gain. The net capital gain is $9,500. Allocating all $7,000 losses to the discount gain instead produces $12,500, a $3,000 increase in assessable gain, not a calculated tax difference. [ITAA 1997 s 102-5](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/102-5); [ATO, using capital losses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/using-capital-losses-to-reduce-capital-gains).

```oa-check
name: AU CGT 2026-27 - choose loss allocation before discount
inputs:
  non_discount_gain: 6000
  discount_gain: 20000
  current_loss: 4000
  prior_loss: 3000
steps:
  - after_current_non_discount: non_discount_gain - current_loss
  - prior_used_non_discount: min(prior_loss, after_current_non_discount)
  - prior_left: prior_loss - prior_used_non_discount
  - discount_gain_after_losses: discount_gain - prior_left
  - net_gain: discount_gain_after_losses / 2
  - alternative_net_gain: non_discount_gain + (discount_gain - current_loss - prior_loss) / 2
  - extra_assessable_gain: alternative_net_gain - net_gain
expected:
  after_current_non_discount: 2000
  prior_used_non_discount: 2000
  prior_left: 1000
  discount_gain_after_losses: 19000
  net_gain: 9500
  alternative_net_gain: 12500
  extra_assessable_gain: 3000
```

### Case 3 - The 15-year exemption preserves losses

A resident individual, aged 60, disposes of an active business asset on 1 February 2027 after 16 continuous years of ownership. The documented event is connected with retirement, all Subdivision 152-A conditions are met and the reviewer has confirmed section 152-105 applies. Its $300,000 gain is fully disregarded before losses. A separate non-exempt investment disposal produces a $2,000 gain. The individual's $5,000 current-year capital loss absorbs that gain, leaving a $3,000 current-year net capital loss. The supported, unused $7,000 prior-year net capital loss is untouched. No loss restriction or other gain applies. Carry forward $10,000, retaining the 2 origin years. Age or a label of 'business asset' alone would not establish the exemption. [ITAA 1997 ss 102-5, 102-10, 152-1 and 152-105](https://www.legislation.gov.au/C2004A05138/latest/text).

```oa-check
name: AU CGT 2026-27 - 15-year exemption before losses
inputs:
  qualifying_gain: 300000
  other_gain: 2000
  current_loss: 5000
  prior_loss: 7000
steps:
  - disregarded_gain: qualifying_gain
  - gain_entering_loss_calculation: qualifying_gain - disregarded_gain + other_gain
  - current_loss_used: min(current_loss, gain_entering_loss_calculation)
  - net_gain: gain_entering_loss_calculation - current_loss_used
  - current_net_loss: current_loss - current_loss_used
  - prior_loss_used: min(prior_loss, net_gain)
  - prior_carried: prior_loss - prior_loss_used
  - total_carried: current_net_loss + prior_carried
expected:
  disregarded_gain: 300000
  gain_entering_loss_calculation: 2000
  current_loss_used: 2000
  net_gain: 0
  current_net_loss: 3000
  prior_loss_used: 0
  prior_carried: 7000
  total_carried: 10000
```

### Case 4 - Proceeds between cost base and reduced cost base

An ordinary A1 disposal in 2026-27 has $10,500 proceeds. Supported acquisition and incidental costs total $10,000. A further $1,500 consists solely of eligible, non-deductible third-element ownership costs on an investment acquired after 20 August 1991. No balancing adjustment, recoupment, deduction, exemption or other adjustment applies. Cost base is $11,500, reduced cost base is $10,000. There is neither gain nor loss. Treating proceeds less cost base as a $1,000 capital loss is wrong. [ITAA 1997 ss 104-10, 110-25(4) and 110-55](https://www.legislation.gov.au/C2004A05138/latest/text).

```oa-check
name: AU CGT 2026-27 - distinct gain and loss cost bases
inputs:
  common_elements: 10000
  ownership_costs: 1500
  proceeds: 10500
steps:
  - cost_base: common_elements + ownership_costs
  - reduced_cost_base: common_elements
  - capital_gain: max(0, proceeds - cost_base)
  - capital_loss: max(0, reduced_cost_base - proceeds)
  - wrong_loss: max(0, cost_base - proceeds)
expected:
  cost_base: 11500
  reduced_cost_base: 10000
  capital_gain: 0
  capital_loss: 0
  wrong_loss: 1000
```

### Case 5 - Collectable and personal use losses stay separate

An individual who is an Australian resident throughout ownership sells an investment share parcel held for 3 years for $20,000 with a $10,000 cost base in 2026-27. A collectable artwork bought for $8,000 is sold for $5,000; there are no incidental costs or adjustments. Its $3,000 loss cannot reduce the share gain. A separate personal use asset bought for $12,000 is sold for $10,000: that $2,000 loss is disregarded. There are no other gains, losses, exemptions or concessions. Discount the $10,000 share gain to $5,000 and carry the $3,000 collectable loss forward only against collectable gains. [ITAA 1997 ss 108-10, 108-20, 118-10 and 115-100](https://www.legislation.gov.au/C2004A05138/latest/text).

```oa-check
name: AU CGT 2026-27 - ring-fenced and disregarded losses
inputs:
  share_proceeds: 20000
  share_cost_base: 10000
  artwork_reduced_cost_base: 8000
  artwork_proceeds: 5000
  private_reduced_cost_base: 12000
  private_proceeds: 10000
steps:
  - share_gain: share_proceeds - share_cost_base
  - collectable_loss: artwork_reduced_cost_base - artwork_proceeds
  - disregarded_private_loss: private_reduced_cost_base - private_proceeds
  - collectable_used_against_shares: 0
  - net_gain: (share_gain - collectable_used_against_shares) / 2
  - collectable_carried: collectable_loss - collectable_used_against_shares
expected:
  share_gain: 10000
  collectable_loss: 3000
  disregarded_private_loss: 2000
  collectable_used_against_shares: 0
  net_gain: 5000
  collectable_carried: 3000
```

### Case 6 - Exact fund discount and no company discount

Compare 2 separate taxpayers, a complying superannuation fund and an ordinary company outside the life-insurance complying-superannuation-asset exception, each disposing of an investment held for 3 years in 2026-27. Each has a supported $30,000 gain after costs and a $6,000 current-year allowable capital loss. No exemption, retirement-phase exempt income, other concession or loss restriction applies. Each has $24,000 after losses. The fund's exact one-third discount removes $8,000, leaving $16,000. This ordinary company has no Division 115 discount and includes $24,000. These are net capital gains, not income-tax liabilities. [ITAA 1997 ss 115-10 and 115-100(b)](https://www.legislation.gov.au/C2004A05138/latest/text).

```oa-check
name: AU CGT 2026-27 - exact one-third fund discount
inputs:
  gross_gain: 30000
  current_loss: 6000
steps:
  - after_losses: gross_gain - current_loss
  - fund_discount: after_losses / 3
  - fund_net_gain: after_losses - fund_discount
  - company_net_gain: after_losses
expected:
  after_losses: 24000
  fund_discount: 8000
  fund_net_gain: 16000
  company_net_gain: 24000
```

**Missing-record position.** An exchange export proves a crypto disposal but omits the acquired parcel's date and cost. Reconstruct exchange, wallet and bank records. Return Needs Input for the affected gain and any aggregate depending on it. Do not enter a zero cost base, infer a holding period or silently omit the disposal. A zero cost base established by a specific rule is a different fact pattern. [ATO, keeping crypto records](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records).

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.

| Code | Trigger | Verbatim output |
| --- | --- | --- |
| R-AU-CGT-SOURCE | Asked to apply a treatment without operative primary authority, including treating the Tax Reform No. 3 Bill as law | 'I cannot apply this CGT treatment without verified authority for the requested period. The affected position is held for a qualified Australian reviewer.' |
| R-AU-CGT-RECORDS | Asked to finalise a gain, loss or exemption using an invented date, cost, valuation or eligibility fact | 'I cannot finalise this CGT position from unsupported facts. Provide the identified evidence or refer the position to a qualified Australian reviewer.' |
| R-AU-CGT-REFORM | A proposed 2027-28 calculation depends on unresolved mixed-residency, transition or other Section 9 conditions | 'I cannot automate this unresolved CGT reform position. A qualified Australian reviewer must establish its operative treatment first.' |
| R-AU-CGT-REVIEW | Asked to lodge, act on or present a filing-ready result without professional review | 'These are working papers for a qualified Australian reviewer. I cannot remove that review or present them as an approved tax position.' |

Ordinary missing evidence remains Needs Input until supplied. Fire the applicable refusal when its trigger is met and record the exact message. Apply the workflow base's excessive-ambiguity refusal above 10 grouped factual questions. Continue independent supported work, but hold any aggregate affected by unresolved gains, losses or eligibility.

### Permitted defaults and reviewer attention

| Missing or disputed fact | Treatment |
| --- | --- |
| Acquisition date, parcel identity, proceeds, cost base or AUD valuation | No numerical default. Reconstruct records or return Needs Input; do not replace missing cost with zero |
| Capital versus revenue, beneficial ownership or residency history | No classification default. Hold the affected calculation for evidence and review |
| Exemption, discount, concession or election eligibility | No presumed entitlement or presumed failure for a final result. Hold eligibility; a clearly labelled sensitivity is not an approved position |
| Loss origin, prior use, collectable class or entity restrictions | No assumed loss availability. Reconcile the loss register before netting |
| 2027-28 source condition or requested historical-period law | No factual default can establish law. Apply the source or reform refusal where triggered |

These are workflow controls, not statutory money thresholds: there is no cash floor for unresolved evidence and no permitted factual default in this guide. Flag every source conflict, valuation, residency, capital/revenue judgment, election and concession claim for the reviewer regardless of amount. Review every final net gain and carried loss. Group questions under the workflow base's limit; an unknown impact cannot be filtered out as immaterial.

### Reviewer delivery and revision

Produce all 4 workflow-base outputs: recalculated Excel working paper, reviewer brief, action list and review checklist. Add an event register showing stable asset/parcel ID, owner, dates, event, source records, AUD proceeds, each cost-base and reduced-cost-base element, disregarded amounts, gross gain/loss, loss allocation, discount and concession sequence, final position and citation. Maintain a loss register by origin year, class, brought forward, used, restriction and carried forward. Reconcile both registers to source totals and the return assembly; transfer no T3 aggregate as a completed amount.

The brief records the requested period, source/read scopes, unresolved dependencies, alternative impacts where established, withholding reconciliation, reviewer decisions and required elections or valuations. The action list identifies who supplies each missing item and its verified deadline. The checklist records each refusal as cleared or fired, every flag and the final transfer precision. The reviewer confirms current return fields and CGT schedule requirements before lodgment.

**Revision 1.10, 2 November 2026:** corrected the 15-year exemption's priority, distinguished gain and loss cost bases, clarified loss allocation and exact fund discount, added 6 executable cases and completed topical intake, refusal, default, reviewer and output controls. Tier 2 and pending professional review remain applicable.

## Completion checklist

### Section 12 - Self-checks

- [ ] The CGT event and its date are identified, and the correct income year follows from them.
- [ ] Residency at the time of the CGT event is established, not assumed.
- [ ] Each element of the cost base is supported by a document.
- [ ] Capital works and capital allowance amounts deducted or deductible have been removed from the cost base (subject to the acquisition date limit) and the reduced cost base (s 110-55(4)), applying TD 2005/47 and PS LA 2006/1 (GA).
- [ ] Disregarded amounts, including any qualifying 15-year-exemption gain, are excluded before loss allocation.
- [ ] Current-year losses are applied before eligible prior-year losses, oldest year first, and before discount; collectable losses remain separate.
- [ ] No negative cost-base result has been treated as a loss without checking reduced cost base and the event's formula.
- [ ] The discount percentage matches the entity type.
- [ ] The 12-month test excludes the acquisition day and the event day.
- [ ] Small business concession conditions have been tested individually, not assumed as a set.
- [ ] Withholding and clearance certificate obligations are addressed before settlement.
- [ ] For a disposal in 2027-28 or later, Section 9 has been applied and the Acts have been read.
- [ ] The workpapers hold the event date, proceeds, each cost base element, the loss and discount calculations, valuations, and any concession choice or rollover election.

## Sources

**Read scope, 2 November 2026.** The entries below record the provisions or page sections checked for this revision. Other retained citations keep their earlier provenance. Capturing a volume or opening a landing page does not establish that every provision was reviewed.

| Source | URL | Read on |
|---|---|---|
| ITAA 1997, compilation 268, volume 3 | [Official text](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) | 2 November 2026: selected ss 102-5, 102-10, 102-15, 104-10, 110-25, 110-35, 110-55, 112-155, 115-100 and 118-10; not the whole volume |
| ITAA 1997, compilation 268, volume 4 | [Official text](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html) | 2 November 2026: ss 152-1, 152-105, 152-110 and 152-205 to 152-220 |
| Tax Reform No. 1 Act 2026 | [As made](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html) | 2 November 2026: Schedule 1 item 82 applies the Division 102 amendments to the income year including 1 July 2027 and later years; do not apply that future gain-category order to 2026-27 |
| ATO, using capital losses | [Dedicated losses page](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/using-capital-losses-to-reduce-capital-gains) | 2 November 2026: current losses, prior losses oldest first, collectables and entity restrictions |
| ATO, cost base of assets | [Cost-base page](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cost-base-of-asset) | 2 November 2026: 5 elements, reduced cost base and events that do not use cost base |
| ATO, CGT discount | [Discount page](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount) | 2 November 2026: holding period, exclusions, residency and entity sections; statutory fund percentage is exactly one-third |
| ATO, keeping crypto records | [Records page](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records) | 2 November 2026: parcel records and reconstruction using exchange records or blockchain explorers |
| Parliament, Tax Reform No. 3 Bill | [Bill r7554](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554) | 2 November 2026: page records third reading agreed to on 29 October and committee report due 13 November; status header still says Before Reps. No assent shown; do not treat proposals as law |

**Source discrepancy.** At this read, Step 5 of the ATO's [how-to page](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/how-to-calculate-your-cgt) says to subtract prior-year losses first. That conflicts with s 102-5 and the dedicated losses page. Use current-year losses before eligible prior-year losses, with prior losses oldest first. For 2027-28, also apply the enacted category ordering and any intervening amendments. The discrepancy does not authorise changing the statutory method.

### Retained source provenance

| Source | URL | Read on |
|---|---|---|
| Retained citation | <https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-20> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-110> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-185> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-55> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-45> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=TXD/TD200547/NAT/ATO/00001> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PSR/GA20061/NAT/ATO/00001> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/116-20> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-25> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/108-20> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/108-10> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-215> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/152-10> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/152-35> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-160> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C2026A00086/asmade/text> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://parlinfo.aph.gov.au/parlInfo/download/legislation/bills/r7554_first-reps/toc_pdf/26132b01.pdf;fileType=application%2Fpdf> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C2026A00049/asmade/text> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C2026A00050/latest> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C2026A00049/latest> | Not re-read for this format update; see retained provenance |

### Section 13 - Sources

- Income Tax Assessment Act 1997, Part 3-1 (CGT events, cost base, exemptions), Part 3-3 (CGT concessions), Division 115 (discount capital gains), Division 152 (small business concessions), Subdivision 118-B (main residence).
- Treasury Laws Amendment (Tax Reform No. 1) Act 2026, https://www.legislation.gov.au/C2026A00049/latest
- Income Tax Rates Amendment (Tax Reform No. 1) Act 2026, https://www.legislation.gov.au/C2026A00050/latest
- ATO, CGT discount, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount
- ATO, Main residence exemption for foreign residents, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents
- ATO, Foreign resident capital gains withholding, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding
- ATO, Reforming negative gearing and capital gains tax, https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax
- ATO, Strengthening the foreign resident CGT regime, https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime
- Treasury Laws Amendment (Strengthening Accountability for Tax Adviser Misconduct and Other Measures) Act 2026, https://www.legislation.gov.au/C2026A00086/asmade/text

Sources were checked on 16 September 2026. The Tax Reform No. 1 Act and Act No. 86 of 2026 were read on the Federal Register of Legislation on 11 October 2026. The Division 43 cost base and reduced cost base rules, the mixed residency row and the Tax Reform No. 3 Bill note were checked on 31 October 2026.

> **Working paper only, not a lodged return.** Have a qualified Australian CPA or CA review this before lodging. Small business CGT eligibility requires detailed analysis of the active asset test, the aggregation rules and the maximum net asset value test.
>
> Contributed by Ryan Duguid.

Not yet confirmed: the 6 executable cases check their stated arithmetic and conditions, not the entire guide's legal accuracy. A complete page-level source audit, requested-year form/software validation and qualified Australian professional sign-off remain outstanding. Historical periods and unresolved Section 9 transition or mixed-residency positions require their own verified authority before use.

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
