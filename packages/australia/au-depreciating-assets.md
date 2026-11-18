---
name: au-depreciating-assets
description: >
  Use this skill to prepare or review the income tax treatment when an Australian
  business or individual stops holding or using a depreciating asset in 2026-27 or an
  earlier open year: the Division 40 balancing adjustment, its reduction for private
  use, cars under the car limit and switched car expense methods, CGT event K7,
  trade-ins with GST on both sides and the replacement's cost, section 40-880
  business capital costs, and hire purchase notional interest under Division 240.
  Trigger on "balancing adjustment", "sold a business asset", "trade-in",
  "car limit", "black hole expenditure", "40-880" or "hire purchase interest".
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27 (law and car limits read 18 November 2026; car limits from 2020-21 kept for cars first used in those years)"
tier: 2
last_updated: 2026-11-18
version: 0.1
review_status: pending_review
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - workflow-base
---

# Australian Depreciating Assets: Balancing Adjustments, Trade-ins, Business Capital Costs and Hire Purchase v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide builds the workpaper for what happens at the end of a depreciating asset's life under the Income Tax Assessment Act 1997 (ITAA 1997): whether a balancing adjustment event has occurred, the termination value, the amount assessable or deductible, its reduction for use other than a taxable purpose, the car rules, CGT event K7, and the trade-in of an old asset for a replacement. It also covers 2 regimes that sit beside Division 40: business capital costs deducted under section 40-880, and the notional sale and loan that Division 240 makes of a hire purchase agreement. It loads on top of `workflow-base`, whose reviewer brief, intake and self-check rules apply. The law is as read on 18 November 2026.

It covers individuals, partnerships, companies and trusts that hold a depreciating asset whose decline in value they work out under Subdivision 40-B, for balancing adjustment events up to 30 June 2027. It does not cover:

- Working out each year's decline in value (effective life, prime cost and diminishing value, the instant asset write-off, low-value and small business pools) and the s 40-291A fixed 50% reduction for work assets: `au-deductions-offsets`. This guide takes each year's decline and deduction as inputs.
- The GST credit on buying a car, its car limit cap and the BAS labels for vehicle purchases: `australia-gst`.
- The CGT discount and other CGT treatment of a K7 gain or loss, including the changes from 1 July 2027: `au-capital-gains`.
- Second-hand depreciating assets in residential rental properties (s 40-27): `au-rental-property`.
- Car expense methods and log books: `au-sole-trader-schedule` and `au-deductions-offsets`.
- Roll-over relief under s 40-340: `au-restructure-rollovers`. Research and development assets: `au-rd-incentive`. Primary production assets: `au-primary-production`.
- Assets in a low-value pool, a software development pool, a project pool or a small business pool, split or merged assets (s 40-290(3)), leisure facilities and boats, mining rights and information, assets on which temporary full expensing was claimed, and assets acquired before 1 July 2001: refer (R-AU-DEP-5).

**The reviewer is the customer of this output.** The output is a workpaper and a reviewer brief, not a lodged return.

## Quick reference

| Question | Rule | Source |
|---|---|---|
| Has an event occurred? | Stopping holding the asset, stopping use with no expected use again, deciding never to use it, or a change in a partnership's holding | ITAA 1997 s 40-295 |
| What was received? | The termination value: the table in s 40-300(2) where an item applies, otherwise what s 40-305 treats as received; less GST on a taxable supply, plus a decreasing adjustment | ss 40-300, 40-305, 27-95 |
| What is assessable or deductible? | Termination value less adjustable value just before the event: assessable if positive, deductible if negative, in the event's income year | s 40-285 |
| Private use? | Reduce the amount by sum of reductions / total decline | s 40-290(2) |
| A car above the car limit? | Termination value x (car limit for the year first used + second element) / total cost ignoring the limit | s 40-325 |
| A car claimed by both car expense methods? | s 40-370 steps: the reduced amount x days the decline was deducted / days held | s 40-370 |
| Only cents per kilometre? | Nothing assessable or deductible | s 40-370(1) Note 2 |
| A capital gain or loss? | CGT event K7: (termination value less cost) x sum of reductions / total decline, disregarded for a car or motor cycle | ss 104-235, 104-240, 118-5 |
| A trade-in? | Old asset: the allowance is the liability terminated, less its GST, plus any decreasing adjustment. New asset: the whole price less its input tax credit, a car then capped at the car limit | ss 40-305, 40-185, 27-80, 27-95, 40-230; GST Act s 132-5 |
| A business capital cost no other provision takes? | One fifth a year for 5 years from the year incurred, to the extent of taxable purpose; some start-up costs at once | s 40-880 |
| A hire purchase agreement? | The hirer is treated as buying the goods with a loan; it deducts notional interest, never the instalments | Division 240 |

## Ask the client first

Collect these before any figure is worked. Missing items become Needs Input, not assumptions.

1. **The event**: what happened to the asset and when (sale, trade-in, loss, destruction, compulsory acquisition, gift, scrapping, stopping use), the contract, invoice or insurance settlement, and whether the other party is an associate or the disposal was private or domestic.
2. **The asset record**: cost broken into first and second elements, the input tax credits claimed on each, the start time, the method and effective life used, and for each income year from the start time to the event's year, the decline in value, the deduction allowable under s 40-25 and the deduction actually claimed.
3. **Use evidence**: the taxable-use percentage for each year and its evidence. For a car, the car expense method chosen in each year (log book or cents per kilometre), the days held in each year, and whether the car's cost was reduced to the car limit.
4. **GST facts**: GST registration, whether the disposal is a taxable supply, the full and the claimed input tax credit on acquisition and any later adjustments, and for a replacement asset its price, luxury car tax and creditable purpose.
5. **For section 40-880 items**: what each amount was paid for, when it was incurred, which business it relates to (current, former, proposed, or a wind-up), the taxable-purpose extent of that business, the entity's small business status for the year, and why no other provision takes the amount.
6. **For hire purchase**: the agreement, the stated cost or value of the goods, deposits and trade-ins credited at the start, the instalment schedule and any balloon or residual, whether the parties dealt at arm's length, and whether the hirer is likely to acquire the goods.

## The method, step by step

### Step 1: Confirm the event and the termination value

- A balancing adjustment event occurs when the holder stops holding the asset, stops using it (or having it installed ready for use) and expects never to use it again, or has not used it and decides never to use it ([ITAA 1997 s 40-295(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-295)). A change in the holding of a partnership asset is also one (s 40-295(2)). Splitting or merging an asset is not (s 40-295(3)).
- The termination value is worked out at the time of the event: the amount in the table in s 40-300(2) where an item applies (the last applicable item if several do), otherwise the amount s 40-305 treats as received ([s 40-300(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-300)). The common table items are market value when the asset is no longer used but still held (items 1 and 2), market value where a party did not deal at arm's length and the value would otherwise be lower (item 6), market value for a private or domestic arrangement such as a gift (item 7), and the insurance or other amount for loss or destruction (item 8).
- Otherwise the termination value is what s 40-305(1) treats as received: the greater of (a) the amounts deducted or deductible because of the event and (b) the sum of the applicable table items, such as an amount received (item 1), the amount of a liability terminated (item 2) and the market value of a non-cash benefit received (item 4) ([s 40-305(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-305)). Apportion a sale price that covers other property on market values ([ATO, Guide to depreciating assets 2026](https://www.ato.gov.au/law/view/document?docid=SAV/DEPRECIATING/00001), 'Selling a depreciating asset with other property').
- GST: reduce the termination value by the GST payable where the event is a taxable supply, and increase it by a decreasing adjustment (or decrease it by an increasing adjustment) relating to that supply in the event's income year ([s 27-95(1), (3), (4)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/27-95)). The GST reduction does not apply where Division 40 substitutes market value (s 27-95(2)). An adjustment in a later income year is assessable or deductible then, not added to the termination value (s 27-95(5), (6)).

### Step 2: Rebuild the adjustable value year by year

- The adjustable value just before the event is cost less the decline in value since the start time; in a later year it is the opening adjustable value plus any second element for that year, less that year's decline up to the event ([s 40-85(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-85)). The decline for the event's year runs only to the event.
- Build one row for each income year from the start time to the event's year, with that year's decline in value and the deduction allowable under s 40-25. A year with no decline still gets a row with 0. Both totals in s 40-290(2) are sums over every year held, so a schedule that skips a year, or stops before the event's year, cannot give them: return Needs Input (R-AU-DEP-1).
- A year's deduction is its decline in value less the part attributable to use other than a taxable purpose ([s 40-25(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-25)), so it cannot exceed the decline; a row that shows more is a data error. The s 40-290 reduction counts the deduction allowable, not the amount claimed: where a year's claim differs from what s 40-25 allowed, return Needs Input (R-AU-DEP-1).
- A later GST credit or adjustment can change the cost or an opening adjustable value after the start year ([s 27-80(3A)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/27-80), [s 27-90](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/27-90)), and a Division 129 change in creditable purpose gives its own adjustments. Where the asset had one, refer (R-AU-DEP-1).

### Step 3: Work out the balancing adjustment amount

- If the termination value is more than the adjustable value just before the event, the difference is assessable; if less, it is deductible; either way for the income year in which the event occurred ([s 40-285(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-285)). The adjustable value is then nil (s 40-285(3)).
- A car whose expenses were claimed by different car expense methods is worked under s 40-370 instead (s 40-285 Notes; Step 5).

### Step 4: Reduce for use other than a taxable purpose

- Where the deductions for the asset were reduced under s 40-25 for use other than a taxable purpose (private use, for example), reduce the balancing adjustment amount by: sum of reductions / total decline x balancing adjustment amount ([s 40-290(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-290)). The sum of reductions is each year's decline less each year's allowable deduction; the total decline is the decline since the holder started to hold the asset (s 40-290(2); it also counts a roll-over transferor's and a deceased individual's years where those apply).
- Work the fraction from the year-by-year rows of Step 2. Do not substitute the event year's business-use percentage when use varied between years.
- An asset used wholly for a non-taxable purpose has its balancing adjustment amount reduced to nil; the difference between termination value and cost is then the K7 capital gain or loss ([ATO, Guide to depreciating assets 2026](https://www.ato.gov.au/law/view/document?docid=SAV/DEPRECIATING/00001), 'Depreciating asset you use for a non-taxable purpose').
- An asset used to produce assessable labour income, where the taxpayer claimed the s 25-130 standard deduction in a year overlapping its effective life, may take a fixed 50% reduction instead ([s 40-291A](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-291A)). That choice is held in `au-deductions-offsets`. Where it is made, the K7 sum of reductions is the amount of that reduction ([s 104-240(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-240)).

### Step 5: Apply the car rules

1. **Car limit at acquisition.** The first element of cost of a car designed mainly for carrying passengers, after s 40-225 and the GST reduction, is reduced to the car limit for the financial year in which the holder started to hold it ([s 40-230(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-230)). The limit does not apply to a car fitted out to carry people with disabilities in wheelchairs for profit, or one over the limit only because of disability modifications (s 40-230(2)). A 'car' here carries a load of less than one tonne and fewer than 9 passengers ([ATO, Assets and exclusions, Car limit](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/assets-and-exclusions)).
2. **Car limit at the event.** For a car whose cost s 40-230 reduced, multiply the termination value by (car limit for the financial year in which the car was first used + amounts in the second element of its cost) / total cost of the car ignoring the car limit, after the GST reduction ([s 40-325](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-325)). The car's cost in the workpaper must then equal the car limit plus the second element. If it does not, or if the car was first used in a later financial year than the one it was first held in (so the 2 limits can differ), or the car is held jointly (s 40-230(4)), refer (R-AU-DEP-2).
3. **Car limits by financial year.** Read the year first held (s 40-230) and the year first used (s 40-325):

| Financial year | Car limit | Source |
|---|---|---|
| 2026-27 | $69,883 | [ATO, Car thresholds from 1 July, QC107449, published 9 June 2026](https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/car-thresholds-from-1-july) |
| 2025-26 | $69,674 | [ATO, Assets and exclusions, Table 2, QC64425, updated 27 May 2026](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/assets-and-exclusions); Guide to depreciating assets 2026 |
| 2024-25 | $69,674 | ATO, Assets and exclusions, Table 2 |
| 2023-24 | $68,108 | Same table |
| 2022-23 | $64,741 | Same table |
| 2021-22 | $60,733 | Same table |
| 2020-21 | $59,136 | Same table |

4. **Switched car expense methods.** Where a balancing adjustment event occurs for a car, a decline in value has been or can be deducted for an income year, and the cents per kilometre method was chosen for one or more other years, work the amount under s 40-370 instead of s 40-285 ([s 40-370(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-370)). The ATO's public ruling [TD 2006/49](https://www.ato.gov.au/law/view/document?docid=TXD/TD200649/NAT/ATO/00001) applies both the 20% assumption at step 2 and the days at steps 3 and 4 to the same cents per kilometre year (paras 10, 19 and 20; its example predates 2015-16, when 2 other methods also counted):
   1. Termination value less adjustable value just before the event. For the cents per kilometre years, the adjustable value assumes a decline worked on the same basis as the other years (s 40-370(3)).
   2. Reduce it by the s 40-290(2) formula. For each cents per kilometre year, treat taxable use as 20%, so 80% of that year's notional decline is a reduction (s 40-370(4)).
   3. Multiply by the total days for which the holder deducted the car's decline in value. A cents per kilometre year adds no days, and neither does a log book year whose deduction was nil, because no decline was deducted for it. A year whose decline could have been deducted but was not claimed is not settled by this wording, as s 40-370(1)(b) speaks of 'deducted or can deduct' and step 3 only of 'deducted': refer it (R-AU-DEP-5).
   4. Divide by the total days the car was held.
   5. A positive result is assessable; a negative one is deductible.
5. **One method throughout.** Log book only: use s 40-285 with the s 40-290 reduction (s 40-370(1) Note 1). Cents per kilometre only: nothing is assessable or deductible (s 40-370(1) Note 2; Guide to depreciating assets 2026, 'Balancing adjustment rules for cars').
6. **Before 2015-16.** Section 40-370 names only the cents per kilometre and log book methods. A car held in a year when the one-third of actual expenses or 12% of original value method was chosen is outside this guide (R-AU-DEP-5).

### Step 6: Work out CGT event K7

- CGT event K7 happens when a balancing adjustment event occurs for a depreciating asset that was at some time used, or installed ready for use, for a purpose other than a taxable purpose ([s 104-235(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-235)). It is not disregarded by the general rule for depreciating assets ([s 118-24(2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-24)).
- Capital gain = (termination value - cost) x sum of reductions / total decline, where termination value exceeds cost; capital loss = (cost - termination value) x the same fraction, where cost exceeds termination value ([s 104-240(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-240); formula read from the [Federal Register, compilation 268, volume 3](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html)). Cost base and capital proceeds play no part (s 104-240(1) Note 2).
- Disregard the gain or loss for a car, motor cycle or similar vehicle ([s 118-5](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-5)), a pre-CGT asset, and an asset for which a Division 328 deduction is available for the event's year (s 104-235(4)). An asset in a low-value pool uses s 104-245 (s 104-235(3); R-AU-DEP-5).
- Pass the gain or loss to `au-capital-gains`, which applies any discount, loss and the changes from 1 July 2027.

### Step 7: Trade-ins and replacement assets

**The old asset.**

- A trade-in terminates the holder's liability to pay part of the replacement's price, so the allowance is the amount taken to be received ([s 40-305(1) item 2](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-305)).
- For a GST-registered holder, trading in an asset used solely or partly in the business is a taxable sale: report it at G1 and its GST at 1A, and give the dealer a tax invoice if asked ([ATO, Disposing of a motor vehicle](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/motor-vehicle-and-transport/gst-and-motor-vehicles/disposing-of-a-motor-vehicle)). The GST is 1/11 of the GST-inclusive allowance (ATO, GST and the disposal of capital assets: Ian's $22,000 sale includes $2,000 GST).
- Where the old asset's input tax credit was reduced for private use, the sale gives a decreasing adjustment of 1/11 x price x (1 - adjusted input tax credit / full input tax credit), capped at the full credit less the adjusted credit ([GST Act s 132-5(2), (3)](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/132-5); [ATO, GST and the disposal of capital assets](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/business-asset-transactions/gst-and-the-disposal-of-capital-assets)). An asset bought without GST has a nil full credit, so the cap gives a nil adjustment.
- Termination value = allowance - GST on the trade-in + decreasing adjustment (s 27-95(1), (3)). Then work Steps 2 to 6 as for a sale.

**The replacement.**

- Its first element of cost is the whole price: the liability to pay it is incurred, whatever part the trade-in settles ([s 40-185(1) item 2](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-185)). Reduce it by the input tax credit to which the holder is entitled, whether or not it has been claimed yet ([s 27-80(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/27-80)). Luxury car tax is part of the price, and no credit is claimed for it ([ATO, Purchasing a motor vehicle](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/motor-vehicle-and-transport/gst-and-motor-vehicles/purchasing-a-motor-vehicle)).
- For a car above the car limit, the credit is capped at 1/11 of the limit for the year first used and reduced for part creditable use ([GST Act s 69-10](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/69-10)); take that figure from `australia-gst`. Then reduce the cost to the car limit for the year first held (Step 5). Record the cost ignoring the limit: s 40-325 needs it when the replacement is sold.

**Trade-ins this guide does not work.**

- Not at arm's length. If a dealer cuts the replacement's price in return for a trade-in below market value, the old asset's termination value becomes its market value (s 40-300(2) item 6), s 27-95(1) does not apply to it (s 27-95(2)), and a car's first element of cost increases by the discount portion where s 40-225 applies (Guide to depreciating assets 2026, Kristine example), as does that car's termination value when it is later disposed of ([s 40-320](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-320)). Refer (R-AU-DEP-3).
- Involuntary disposal. Where the old asset was lost, destroyed or compulsorily acquired, the holder may choose to exclude some or all of an assessable balancing adjustment amount and reduce the replacement's cost by it instead. The replacement must be acquired from one year before the event to one year after the end of the event's income year, and be used wholly for a taxable purpose at the end of the year acquired ([s 40-365](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-365)). The choice is the taxpayer's: quantify both treatments and refer (R-AU-DEP-4).

### Step 8: Section 40-880 business capital costs

- **Last resort.** Section 40-880 deducts business-related capital expenditure only where no other provision allows, denies or takes it into account ([TR 2011/6 para 10](https://www.ato.gov.au/law/view/document?docid=TXR/TR20116/NAT/ATO/00001)). Settle capital or revenue first: a revenue outlay goes to s 8-1, not here.
- **What qualifies.** Capital expenditure in relation to the holder's business, a business that used to be carried on, a business proposed to be carried on, or the liquidation, deregistration or wind-up of a company, partnership or trust that carried on a business and of which the holder was a member, partner or beneficiary ([s 40-880(2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-880)).
- **Extent.** Only to the extent the business is, was or is proposed to be carried on for a taxable purpose (s 40-880(3)). For another entity's former or proposed business, the expenditure must also be in connection with the holder's deriving assessable income from that business (s 40-880(4)). Taxable purpose is tested when the expenditure is incurred; for a former business, over a period that reasonably reflects it (TR 2011/6 paras 157 and 160).
- **Exclusions.** Nothing is deductible to the extent the expenditure forms part of the cost of a depreciating asset (Division 40 takes it), is deductible elsewhere, forms part of the cost of land, relates to a lease or other legal or equitable right, is taken into account in a profit or loss, could be taken into account in a capital gain or loss (the CGT provisions take it), is made non-deductible by another provision, is private or domestic, or relates to exempt or non-assessable non-exempt income (s 40-880(5)(a) to (j)). Expenditure preserving goodwill through a right valued solely for its effect on goodwill escapes (5)(d) and (f) (s 40-880(6)). A proposed business must be likely to start within a reasonable time (s 40-880(7)). Amounts excluded by a market value substitution rule, returns of non-assessable amounts and returns on or of equity or debt interests are excluded (s 40-880(8), (9)).
- **Timing.** Deduct in equal proportions over 5 income years starting in the year incurred (s 40-880(2)), one fifth a year, not apportioned for part of the first year, and never more than one fifth in a year (TR 2011/6 paras 10, 319 and 320). Eligibility is fixed once, when the expenditure is incurred (TR 2011/6 para 10).
- **Start-up costs at once.** For a proposed business, advice or services about its proposed structure or operation, and fees, taxes or charges paid to an Australian government agency for establishing it or its structure, are deductible in full in the year incurred by a small business entity, an entity covered by s 40-880(2B), or an entity that carries on no business that year and is not connected with, or an affiliate of, an entity carrying on a business that is neither a small business entity nor covered by s 40-880(2B) (s 40-880(2A)). Subsection (2B) covers an entity that would be a small business entity if Subdivision 328-C's $10 million were $50 million (s 40-880(2B)). The ATO's examples are advice on a business structure, setting up legal arrangements or systems, viability advice and due diligence, a business plan, and the fee for creating a company; asset costs are not included ([ATO, Deductions for depreciating assets and capital expenses, updated 28 August 2026](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-depreciating-assets-and-capital-expenses)).
- **Period covered.** The amendments that added s 40-880(2B) apply to expenditure incurred on or after 1 July 2020 ([Treasury Laws Amendment (A Tax Plan for the COVID-19 Economic Recovery) Act 2020 (No. 92, 2020) Sch 3 item 40(7)](https://www.legislation.gov.au/C2020A00092/asmade/text)). Expenditure incurred before then is outside this guide (R-AU-DEP-6).
- **Other limits.** Division 35 (non-commercial losses) and Division 85 (personal services income) can defer or deny the deduction (TR 2011/6 para 11): route those tests to `au-deductions-offsets` and `au-psi`.

### Step 9: Hire purchase under Division 240

- A hire purchase agreement for any goods is treated as a notional sale and a notional loan ([s 240-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-10)). The financier is the notional seller and the hirer the notional buyer ([s 240-17](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-17)), who is taken to have acquired the goods at the start of the agreement ([s 240-20](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-20)).
- The cost of the goods to the hirer is the cost or value stated in the agreement where the parties dealt at arm's length, otherwise the arm's length price; the notional loan principal is that amount less anything paid or credited at or before the start, such as a deposit or trade-in ([s 240-25(3), (5)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-25)). The payments repay the principal and pay the interest (s 240-25(6)).
- The hirer holds the goods for Division 40, and claims their decline in value, where it is reasonably likely to acquire them. If it does not acquire them, it is treated as selling them back at market value and works out a balancing adjustment ([ATO, Guide to depreciating assets 2026](https://www.ato.gov.au/law/view/document?docid=SAV/DEPRECIATING/00001), 'Depreciating assets subject to hire purchase agreements').
- The hirer cannot deduct the instalments ([s 240-55](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-55)). It deducts the notional interest for the payment periods, and parts of periods, in the income year, to the extent it could have deducted the payments if none of them were capital ([s 240-50](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-50)). Private use therefore reduces the interest deduction.
- Notional interest for each payment period is the outstanding notional loan principal (principal plus earlier interest, less payments made or due) times the implicit interest rate found from the payments and any termination amounts ([s 240-60(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-60)). The interest of a period that spans 30 June is related to each income year 'in accordance with generally accepted accounting principles' (s 240-60(2)); the Act names no method, so show that period's interest and its days on each side and leave the split to the reviewer.
- The financier includes the notional interest in its assessable income ([s 240-35](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-35)). The notional loan is a limited recourse debt; if it ends unpaid, excess capital allowances can become assessable (Guide to depreciating assets 2026, 'Limited recourse debt arrangements'): refer (R-AU-DEP-7).

### Conservative defaults

| Ambiguity | Default |
|---|---|
| A year's decline or deduction missing from the asset record | Needs Input for the whole adjustment; never estimate the s 40-290 fraction from one year's percentage (R-AU-DEP-1) |
| Taxable-use evidence missing for a year | Take the deduction claimed as the allowable one and flag the year for the reviewer |
| Car expense method for a year unknown | Needs Input: the method decides between s 40-285 and s 40-370 |
| Whether the car's cost was reduced to the car limit unknown | Compare the first element of cost with the limit for the year first held; if above, apply s 40-325 and flag |
| Disposal to an associate, or allowance well below the dealer's valuation | Treat as not at arm's length until shown otherwise (R-AU-DEP-3) |
| A s 40-880 item that might belong to an asset's cost or a CGT asset's cost base | Treat it as excluded by s 40-880(5)(a) or (f) until the reviewer decides |
| A hire purchase period spanning 30 June | Show it apart with its days on each side; claim no part of it in the earlier year until the reviewer decides the split |

## Worked cases

All facts are hypothetical unless a case names its ATO source. Amounts are worked to the cent and shown rounded half up.

### Case A: computer used 60% for business (ATO's Andrew example)

Andrew bought a computer for $1,000, used it 60% for a taxable purpose, and sold it for $600 when its total decline in value was $300. He deducted 60% of each year's decline, so his deductions were reduced by $120 in total ([Guide to depreciating assets 2026](https://www.ato.gov.au/law/view/document?docid=SAV/DEPRECIATING/00001), 'Example: depreciating asset used partly for a taxable purpose'). The ATO's answer: a $60 deduction and a $160 capital loss.

```oa-check
name: AU depreciating asset with 60% taxable use, balancing adjustment and K7 capital loss
tolerance: 0.000001
inputs:
  cost: 1000
  termination_value: 600
  total_decline: 300
  sum_of_reductions: 120
steps:
  - adjustable_value: cost - total_decline
  - balancing_adjustment_amount: abs(termination_value - adjustable_value)
  - reduction_for_private_use: balancing_adjustment_amount * sum_of_reductions / total_decline
  - deductible_amount: balancing_adjustment_amount - reduction_for_private_use
  - k7_capital_loss: (cost - termination_value) * sum_of_reductions / total_decline
expected:
  adjustable_value: 700
  balancing_adjustment_amount: 100
  reduction_for_private_use: 40
  deductible_amount: 60
  k7_capital_loss: 160
```

### Case B: a car on the log book method (ATO's Louise example)

Louise bought a car on 1 July 2024, used the log book method at 40% business use in 2024-25 and 2025-26, and sold it for $24,500 on 30 June 2026 when its adjustable value was $18,200 (Guide to depreciating assets 2026, 'Example: using the logbook method'). The ATO gives $2,520 assessable. The cost of $30,000 and the split of the $11,800 decline between the 2 years are added here to show the s 40-290 fraction; any split at 40% gives the same answer. The K7 gain or loss on a car is disregarded (s 118-5).

```oa-check
name: AU 2025-26 log book car sold, balancing adjustment reduced for private use
tolerance: 0.000001
inputs:
  cost: 30000
  termination_value: 24500
  decline_2024_25: 7500
  decline_2025_26: 4300
  business_use_percent: 40
steps:
  - total_decline: decline_2024_25 + decline_2025_26
  - adjustable_value: cost - total_decline
  - sum_of_reductions: total_decline - pct(total_decline, business_use_percent)
  - balancing_adjustment_amount: termination_value - adjustable_value
  - assessable_amount: balancing_adjustment_amount - balancing_adjustment_amount * sum_of_reductions / total_decline
expected:
  adjustable_value: 18200
  sum_of_reductions: 7080
  balancing_adjustment_amount: 6300
  assessable_amount: 2520
```

### Case C: a car claimed under both car expense methods (s 40-370)

A $30,000 car was bought on 1 July 2024. In 2024-25 the owner used the cents per kilometre method; the notional decline for that year, worked on the same basis as later years, was $7,500 (s 40-370(3)). In 2025-26 the owner used the log book method at 60%: decline $5,625, deduction $3,375. The car was sold for $18,000 after 200 days of 2026-27, a log book year at 60% with a $2,000 decline and a $1,200 deduction. It was held for 365 + 365 + 200 = 930 days; a decline was deducted for 365 + 200 = 565 of them.

```oa-check
name: AU 2026-27 car sold after switching from cents per kilometre to log book, s 40-370
tolerance: 0.000001
inputs:
  cost: 30000
  termination_value: 18000
  notional_decline_cents_year: 7500
  decline_2025_26: 5625
  deduction_2025_26: 3375
  decline_2026_27: 2000
  deduction_2026_27: 1200
  days_held: 930
  days_decline_deducted: 565
steps:
  - total_decline: notional_decline_cents_year + decline_2025_26 + decline_2026_27
  - adjustable_value: cost - total_decline
  - step_1: termination_value - adjustable_value
  - sum_of_reductions: notional_decline_cents_year * 0.8 + (decline_2025_26 - deduction_2025_26) + (decline_2026_27 - deduction_2026_27)
  - step_2: step_1 - step_1 * sum_of_reductions / total_decline
  - assessable_amount: round(step_2 * days_decline_deducted / days_held, 2)
expected:
  adjustable_value: 14875
  step_1: 3125
  sum_of_reductions: 9050
  assessable_amount: 762.55
```

If the 2026-27 log book deduction had been nil (the car was used only privately in those 200 days), that year still counts in the total decline and the sum of reductions, but adds no days at step 3, because no decline was deducted for it.

```oa-check
name: AU 2026-27 s 40-370 car whose last log book year had a nil deduction
tolerance: 0.000001
inputs:
  cost: 30000
  termination_value: 18000
  notional_decline_cents_year: 7500
  decline_2025_26: 5625
  deduction_2025_26: 3375
  decline_2026_27: 2000
  deduction_2026_27: 0
  days_held: 930
  days_decline_deducted: 365
steps:
  - total_decline: notional_decline_cents_year + decline_2025_26 + decline_2026_27
  - step_1: termination_value - (cost - total_decline)
  - sum_of_reductions: notional_decline_cents_year * 0.8 + (decline_2025_26 - deduction_2025_26) + (decline_2026_27 - deduction_2026_27)
  - step_2: step_1 - step_1 * sum_of_reductions / total_decline
  - assessable_amount: round(step_2 * days_decline_deducted / days_held, 2)
expected:
  sum_of_reductions: 10250
  assessable_amount: 395.31
```

### Case D: a car above the car limit (s 40-325)

A business bought a car first held and first used in 2025-26. Its cost after the GST reduction, ignoring the car limit, was $80,000, with no second element; s 40-230 reduced the cost to the 2025-26 limit of $69,674. It was used wholly for business, declined $10,000 and was then sold for $50,000 after GST. Without s 40-325 the deduction would be $9,674; scaling the termination value raises it.

```oa-check
name: AU 2025-26 car limit car sold, termination value scaled under s 40-325
tolerance: 0.000001
inputs:
  car_limit_year_first_used: 69674
  second_element: 0
  cost_ignoring_car_limit: 80000
  decline: 10000
  sale_price_after_gst: 50000
steps:
  - cost: car_limit_year_first_used + second_element
  - adjustable_value: cost - decline
  - termination_value: sale_price_after_gst * (car_limit_year_first_used + second_element) / cost_ignoring_car_limit
  - deductible_amount: adjustable_value - termination_value
  - deductible_without_s_40_325: adjustable_value - sale_price_after_gst
expected:
  cost: 69674
  adjustable_value: 59674
  termination_value: 43546.25
  deductible_amount: 16127.75
  deductible_without_s_40_325: 9674
```

### Case E: trading in a part-private vehicle (ATO's Ian example)

Ian, a GST-registered plumber, bought a car for $44,000 including $4,000 GST, used it 80% in his business and claimed a $3,200 credit. In the ATO's example he sells it for $22,000 including GST, a taxable sale, with a $400 decreasing adjustment ([ATO, GST and the disposal of capital assets](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/business-asset-transactions/gst-and-the-disposal-of-capital-assets)). Added here: he trades it in for a $22,000 allowance instead, which is also a taxable sale; he held the car for one full income year on the log book method, with a decline of $10,200 and a deduction of $8,160, and the trade-in happens at the end of that year. The car's capital gain or loss is disregarded (s 118-5).

```oa-check
name: AU trade-in of an 80% business car, GST on the sale and the balancing adjustment
tolerance: 0.000001
inputs:
  price_incl_gst: 44000
  full_input_tax_credit: 4000
  adjusted_input_tax_credit: 3200
  trade_in_allowance: 22000
  decline: 10200
  deduction: 8160
steps:
  - cost: price_incl_gst - adjusted_input_tax_credit
  - trade_in_gst: trade_in_allowance / 11
  - decreasing_adjustment: min(trade_in_gst * (1 - adjusted_input_tax_credit / full_input_tax_credit), full_input_tax_credit - adjusted_input_tax_credit)
  - termination_value: trade_in_allowance - trade_in_gst + decreasing_adjustment
  - adjustable_value: cost - decline
  - balancing_adjustment_amount: adjustable_value - termination_value
  - reduction_for_private_use: balancing_adjustment_amount * (decline - deduction) / decline
  - deductible_amount: balancing_adjustment_amount - reduction_for_private_use
expected:
  cost: 40800
  trade_in_gst: 2000
  decreasing_adjustment: 400
  termination_value: 20400
  adjustable_value: 30600
  balancing_adjustment_amount: 10200
  deductible_amount: 8160
```

### Case F: the replacement car's cost (ATO's Darren example)

Darren buys a new car on 12 July 2026 for $91,242.80, including $8,075.91 GST and $2,407.80 luxury car tax, and plans to use it 50% in his business. The ATO caps the credit at 1/11 of the 2026-27 car limit, $6,353, and gives $3,176.50 at 50% use ([ATO, Purchasing a motor vehicle](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/motor-vehicle-and-transport/gst-and-motor-vehicles/purchasing-a-motor-vehicle)). For income tax, the cost is the price less that credit (s 27-80), reduced to the $69,883 car limit (s 40-230); keep the cost ignoring the limit for s 40-325.

```oa-check
name: AU 2026-27 replacement car cost after the capped credit and the car limit
tolerance: 0.000001
inputs:
  price: 91242.80
  luxury_car_tax: 2407.80
  car_limit_2026_27: 69883
  creditable_purpose_percent: 50
steps:
  - full_input_tax_credit: min((price - luxury_car_tax) / 11, car_limit_2026_27 / 11)
  - input_tax_credit: pct(full_input_tax_credit, creditable_purpose_percent)
  - cost_ignoring_car_limit: price - input_tax_credit
  - cost: min(cost_ignoring_car_limit, car_limit_2026_27)
expected:
  full_input_tax_credit: 6353
  input_tax_credit: 3176.50
  cost_ignoring_car_limit: 88066.30
  cost: 69883
```

### Case G: a section 40-880 cost in a business with 20% non-assessable income

A company carries on a business that earns 20% non-assessable non-exempt income, as in TR 2011/6 Example 16, so the business is carried on 80% for a taxable purpose. On 1 September 2026 it incurs $10,000 of capital expenditure to raise equity for the business, which no other provision takes. It deducts 80% of it over 5 years from 2026-27, a full fifth in the first year despite starting part way through (TR 2011/6 paras 319 to 321).

```oa-check
name: AU 2026-27 s 40-880 cost at 80% taxable purpose over 5 years
tolerance: 0.000001
inputs:
  expenditure: 10000
  taxable_purpose_percent: 80
  years: 5
steps:
  - deductible_total: pct(expenditure, taxable_purpose_percent)
  - deduction_each_year: deductible_total / years
  - deduction_2026_27: deduction_each_year
  - remaining_after_2026_27: deductible_total - deduction_2026_27
expected:
  deductible_total: 8000
  deduction_each_year: 1600
  deduction_2026_27: 1600
  remaining_after_2026_27: 6400
```

### Case H: hire purchase interest by income year

A business enters an arm's length hire purchase agreement on 1 March 2027 for a machine stated at $26,000, ignoring GST, and pays a $2,000 deposit, so the notional loan principal is $24,000 (s 240-25(3)). Twelve monthly instalments in arrears each repay $2,000 of principal plus 1% of the balance outstanding at the start of the month; at 1% a month the balance after the last instalment is nil, so 1% is the implicit rate (s 240-60(1)). The machine is used 75% for business. Each instalment period is a calendar month, so none spans 30 June: March to June 2027 fall in 2026-27 and July 2027 to February 2028 in 2027-28. The hirer deducts the business share of the notional interest, not the instalments (ss 240-50, 240-55).

```oa-check
name: AU hire purchase notional interest split by income year and reduced for private use
tolerance: 0.000001
inputs:
  stated_cost: 26000
  deposit: 2000
  monthly_rate_percent: 1
  principal_each_month: 2000
  business_use_percent: 75
steps:
  - notional_loan_principal: stated_cost - deposit
  - interest_2026_27: pct(24000 + 22000 + 20000 + 18000, monthly_rate_percent)
  - interest_2027_28: pct(16000 + 14000 + 12000 + 10000 + 8000 + 6000 + 4000 + 2000, monthly_rate_percent)
  - total_instalments: notional_loan_principal + interest_2026_27 + interest_2027_28
  - balance_after_12_months: notional_loan_principal - 12 * principal_each_month
  - deduction_2026_27: pct(interest_2026_27, business_use_percent)
  - deduction_2027_28: pct(interest_2027_28, business_use_percent)
expected:
  notional_loan_principal: 24000
  interest_2026_27: 840
  interest_2027_28: 720
  total_instalments: 25560
  balance_after_12_months: 0
  deduction_2026_27: 630
  deduction_2027_28: 540
```

### Further positions

- **Case I: a gift to a family member.** A sole trader gives a 70% business laptop to her son. The termination value is its market value just before she stopped holding it (s 40-300(2) item 7), not nil. Work Steps 2 to 6 on that value; the K7 amount arises for the 30% private share.
- **Case J: an asset destroyed in a fire.** The termination value is the insurance payout (s 40-300(2) item 8). If the payout exceeds the adjustable value and a replacement is bought within the s 40-365(3) window and used wholly for business, the taxpayer may choose to reduce the replacement's cost instead of returning the assessable amount. Show both and refer (R-AU-DEP-4).
- **Case K: start-up advice.** An individual who carries on no business, and is not connected with or an affiliate of any entity that carries on a business, pays an accountant $1,500 in 2026-27 for advice on the structure of a business she proposes to start within months. It is deductible in full in 2026-27 (s 40-880(2A)(a), (b)(i), (c)). The same amount paid by a company that carries on a business and is not a small business entity or covered by s 40-880(2B) is deducted over 5 years.
- **Case L: a hirer who hands the goods back.** A hirer returns the goods at the end of the agreement without buying them. It is treated as selling them back to the financier at market value, and works out a balancing adjustment on that termination value (Guide to depreciating assets 2026).
- **Case M: a car first held in June and first used in July.** A car bought on 25 June 2026 and first driven on 2 July 2026 had its cost reduced to the 2025-26 limit ($69,674, s 40-230), but s 40-325 uses the 2026-27 limit ($69,883). The cost no longer equals the limit used at the event plus the second element. Refer (R-AU-DEP-2).

## Common errors

- Using the event year's business-use percentage for the whole balancing adjustment instead of the year-by-year sum of reductions and total decline (s 40-290(2)).
- Leaving a nil-decline year, or the event's part year, out of the schedule.
- Applying s 40-285 alone to a car that was on cents per kilometre for some years and log book for others, or counting days of a nil-deduction log book year at s 40-370 step 3.
- Working out a balancing adjustment for a car claimed only on cents per kilometre.
- Forgetting s 40-325 when a car's cost was capped, which understates a deduction or overstates an assessable amount.
- Taking the trade-in allowance as the termination value without removing its GST, or forgetting the decreasing adjustment for a part-private asset.
- Recording the replacement's cost as the cash paid after the trade-in instead of the whole price, or leaving the input tax credit in it.
- Reporting a K7 capital gain or loss on a car or motor cycle.
- Deducting hire purchase instalments, or deducting the full notional interest on a part-private asset.
- Claiming a s 40-880 deduction for a cost that belongs to a depreciating asset or a CGT asset's cost base, or apportioning the first fifth for part of a year.

## When to refuse or refer

Stop the affected calculation where a fact, source condition or scope requirement in this guide is unresolved, and return Needs Input or refer it for qualified review.

**Topical refusals**

- **R-AU-DEP-1, incomplete asset history.** *Trigger:* the decline and allowable deduction are not known for every income year from the start time to the event's year, a year's claim differs from its allowable deduction, a later GST credit or adjustment changed the cost or an opening adjustable value, or the declines total nil (the s 40-290(2) and s 104-240 fraction is then undefined) or more than cost. *Message:* "The balancing adjustment cannot be reduced for private use without every year's decline in value and deduction, including a year with nil decline and the part year to the event. Provide the full schedule and resubmit."
- **R-AU-DEP-2, car limit facts inconsistent.** *Trigger:* a car's cost was reduced by s 40-230 but does not equal the car limit plus its second element, the car was first used in a later financial year than the one it was first held in, or it is held jointly (s 40-230(4)). *Message:* "The car limit used for the cost and the one s 40-325 uses at the event differ or cannot be confirmed from the records. The reviewer must settle the car's cost and its s 40-325 fraction before the balancing adjustment is worked."
- **R-AU-DEP-3, market value substitution.** *Trigger:* a disposal or trade-in not at arm's length, to an associate, or under a private or domestic arrangement, or a dealer discount linked to an undervalued trade-in. *Message:* "Market value replaces the agreed amount (s 40-300(2) items 6 and 7), the GST reduction of s 27-95(1) may not apply, and a car's cost can increase under s 40-225, with its later termination value increased under s 40-320. The workpaper records the facts and a market value estimate; the reviewer decides the values."
- **R-AU-DEP-4, involuntary disposal choice.** *Trigger:* the asset was lost, destroyed or compulsorily acquired and a replacement is bought or planned. *Message:* "Section 40-365 lets the taxpayer exclude some or all of the assessable amount and reduce the replacement's cost instead, if its timing and use conditions are met. The workpaper shows both treatments; the choice is the taxpayer's, made with the reviewer."
- **R-AU-DEP-5, assets this guide does not work.** *Trigger:* a pooled asset, split or merged asset, leisure facility or boat, mining right or information, R&D asset, primary production asset, temporary full expensing asset, roll-over relief, an asset acquired before 1 July 2001, a car held in a year under the one-third of actual expenses or 12% of original value method, or a car worked under s 40-370 with a year whose decline could have been deducted but was not claimed. *Message:* "This asset's balancing adjustment follows rules this guide does not carry. Route it to the guide or practitioner named in Scope."
- **R-AU-DEP-6, section 40-880 outside the guide's period or rules.** *Trigger:* expenditure incurred before 1 July 2020, a dispute whether an outlay is capital or revenue, or a question whether another provision takes the expenditure. *Message:* "Section 40-880 is a provision of last resort and this guide carries its form from 1 July 2020. The reviewer must decide the character of the outlay and the provisions ahead of s 40-880 before any deduction is claimed."
- **R-AU-DEP-7, hire purchase edge cases.** *Trigger:* a payment period spanning 30 June, doubt whether the hirer is likely to acquire the goods, an agreement that ends unpaid, or parties not at arm's length. *Message:* "Division 240 relates a part period by generally accepted accounting principles, the hirer's holding depends on its likely acquisition, and an unpaid notional loan can trigger the limited recourse debt rules. The workpaper shows the facts and figures; the reviewer decides."
- **R-AU-DEP-8, unpublished car limit.** *Trigger:* a car first held or first used in 2027-28 or later. *Message:* "The car limit for that financial year was not published on the ATO pages read for this guide. Read it from the ATO page then current, record the source and date, and resubmit."

**Reviewer attention thresholds (guide policy, not law)**

- Any balancing adjustment or K7 amount above $10,000.
- Any asset whose taxable use changed by more than 20 percentage points between years.
- Any trade-in allowance that differs from the dealer's or an independent valuation by more than 10%.
- Any s 40-880 item above $20,000, and any start-up deduction claimed in full.
- Any hire purchase agreement with a balloon or residual above 30% of the stated cost.

**Prohibitions**

- Never state a car limit, input tax credit cap or rate from memory; read it from the source for the financial year.
- Never estimate a missing year's decline or deduction.
- Never deduct hire purchase instalments, or a s 40-880 fifth before the year it falls in.
- Never make the s 40-365 choice, decide a market value or lodge on the taxpayer's behalf.

## Completion checklist

- [ ] The balancing adjustment event and its date are evidenced, and the termination value traces to the contract, settlement or market value evidence, net of GST and with any decreasing adjustment.
- [ ] The asset schedule has one row for every income year from the start time to the event's year; total decline equals cost less adjustable value.
- [ ] No year's deduction exceeds its decline; each year's allowable deduction ties to the deduction claimed in the return, or the difference is referred.
- [ ] Each car shows its method for every year, the days held and the days a decline was deducted, and whether s 40-230 and s 40-325 applied with the limits used.
- [ ] K7 is worked only where use was not wholly taxable, and disregarded for cars and motor cycles; the gain or loss is passed to `au-capital-gains`.
- [ ] Each trade-in shows the GST on the old asset, the decreasing adjustment, the replacement's whole price, its credit and its cost before and after the car limit.
- [ ] Each s 40-880 item names the business, the paragraph of s 40-880(2), the taxable-purpose extent, the exclusions considered and the year of each fifth.
- [ ] Each hire purchase agreement shows the notional loan principal, the implicit rate, the interest by income year with any spanning period set apart, and the deductible share.
- [ ] Reviewer brief additions: each conservative default triggered, each refusal raised, and each figure's source and read date.

## Sources

| Source | URL | Read on |
|---|---|---|
| ITAA 1997 ss 27-80, 27-90, 27-95, 40-25, 40-85, 40-185, 40-225, 40-230, 40-285, 40-290, 40-291A, 40-295, 40-300, 40-305, 40-320, 40-325, 40-365, 40-370, 40-880 (ATO legal database, CCH consolidation) | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-285 (and the matching docid for each section) | 2026-11-18 |
| ITAA 1997 ss 104-235, 104-240, 118-5, 118-24 (ATO legal database) | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-240 (and the matching docid for each section) | 2026-11-18 |
| ITAA 1997 compilation 268 (1 October 2026), volume 3: text alternative of the s 104-240 formula | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2026-11-18 |
| ITAA 1997 ss 240-10, 240-17, 240-20, 240-25, 240-35, 240-50, 240-55, 240-60 (ATO legal database) | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/240-60 (and the matching docid for each section) | 2026-11-18 |
| GST Act ss 69-10 and 132-5 (ATO legal database) | https://www.ato.gov.au/law/view/document?docid=PAC/19990055/132-5 | 2026-11-18 |
| Treasury Laws Amendment (A Tax Plan for the COVID-19 Economic Recovery) Act 2020 (No. 92, 2020), as made, Sch 3 item 40(7) | https://www.legislation.gov.au/C2020A00092/asmade/text | 2026-11-18 |
| TD 2006/49, paras 1, 9, 10 and 18 to 20: s 40-370 method statement | https://www.ato.gov.au/law/view/document?docid=TXD/TD200649/NAT/ATO/00001 | 2026-11-18 |
| TR 2011/6, paras 10, 11, 157, 160, 163 and 164 (Example 16), 319 to 321 (Example 41) | https://www.ato.gov.au/law/view/document?docid=TXR/TR20116/NAT/ATO/00001 | 2026-11-18 |
| ATO, Guide to depreciating assets 2026: balancing adjustments, non-taxable use, cars, car acquired at a discount, involuntary disposal, hire purchase, limited recourse debt | https://www.ato.gov.au/law/view/document?docid=SAV/DEPRECIATING/00001 | 2026-11-18 |
| ATO, Assets and exclusions (QC64425, updated 27 May 2026): car limit, Table 2 | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/assets-and-exclusions | 2026-11-18 |
| ATO, Car thresholds from 1 July (QC107449, published 9 June 2026) | https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/car-thresholds-from-1-july | 2026-11-18 |
| ATO, Purchasing a motor vehicle (updated 3 June 2026): Darren example | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/motor-vehicle-and-transport/gst-and-motor-vehicles/purchasing-a-motor-vehicle | 2026-11-18 |
| ATO, Disposing of a motor vehicle (updated 29 May 2024): trade-ins | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/motor-vehicle-and-transport/gst-and-motor-vehicles/disposing-of-a-motor-vehicle | 2026-11-18 |
| ATO, GST and the disposal of capital assets (updated 24 May 2017): decreasing adjustment, Ian example | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/business-asset-transactions/gst-and-the-disposal-of-capital-assets | 2026-11-18 |
| ATO, Deductions for depreciating assets and capital expenses (updated 28 August 2026): business-related and start-up costs | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-depreciating-assets-and-capital-expenses | 2026-11-18 |

Named but not read for this guide: ITAA 1997 s 104-245 (pooled assets), Subdivision 328-C, Divisions 35, 85 and 243, s 40-340 and GSTR 2004/8. Read each before relying on a position that turns on it.

Method adapted by its author from the `balancing-adjustment`, `trade-in`, `business-capital-expenditure` and `hire-purchase-schedule` worksheets in ryanduguid/australian-accounting (commits 18f14a01, 01f25920, fb9c46e1 and 46ef08a9).

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
