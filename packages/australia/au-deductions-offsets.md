---
name: au-deductions-offsets
description: >
  Use this skill to work out what an Australian taxpayer can claim: deductions, tax offsets,
  rebates, credits, capital allowances and small business concessions, and how they interact. It
  maps the general "credits, reliefs, deductions and allowances" category onto Australian
  concepts, which behave differently from each other. Trigger on phrases like "what can I claim",
  "tax deductions Australia", "work-related expenses", "$1,000 standard deduction", "instant tax
  deduction", "tax offset", "rebate", "low income tax offset", "LITO", "refundable offset",
  "franking credits refund", "substantiation", "do I need a receipt", "capital or revenue",
  "apportion private use", "small business concessions". It routes to the specialist guides
  rather than restating their rules.
version: 0.9
jurisdiction: AU
tax_year: 2026
tax_year_notes: "Primarily 2026-27; prepayment cases follow deductions into 2027-28 and 2028-29"
last_updated: 2026-11-02
review_status: pending_review
depends_on:
  - au-individual-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Deductions, Offsets and Concessions v0.9

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

### What this file is

**Obligation category:** Income tax
**Functional role:** Router and decision framework for everything that reduces Australian tax
**Status:** Source-cited draft, pending accountant review

Australia has no single "reliefs and allowances" concept. Four mechanisms sit behind that idea and
they behave differently, so getting the mechanism right matters more than finding the item.

### Section 2 - Scope statement

This skill covers:

- The order in which deductions, offsets and concessions are applied.
- The general deduction test, apportionment, the capital and revenue boundary, and the specific
  denial provisions.
- The standard deduction for work-related expenses that applies from the 2026-27 income year.
- Substantiation requirements and record retention.
- The main tax offsets and how refundability changes their value.
- Where each specialist rule set lives.

This skill does NOT cover:

- The detailed computation of any single item. Each has its own guide.
- GST credits. Those are not income tax deductions. See `australia-gst.md`.
- Fringe benefits tax. See `au-fbt-year.md`.
- State and territory concessions, including duty concessions and land tax exemptions. See
  `au-stamp-duty.md` and `au-land-tax.md`.

**Where the specialist rules live**

**Where the specialist rules live**

| Topic | Guide |
| --- | --- |
| Individual return items and work-related expense patterns | `au-individual-return.md` |
| Rental property income and expenses | `au-rental-property.md` |
| Small business CGT concessions | `au-small-business-cgt.md` |
| CGT discount, losses and cost base | `au-capital-gains.md` |
| Research and development tax incentive | `au-rd-incentive.md` |
| Personal services income restrictions | `au-psi.md` |
| Medicare levy and the surcharge | `au-medicare-levy.md` |
| Superannuation contribution deductions and caps | `au-super-guarantee.md` |
| Company losses, franking and Division 7A | `au-company-tax.md`, `au-div7a.md` |
| Foreign income tax offset | `au-foreign-income.md` |

## Ask the client first

- Which income year applies? The standard deduction begins with 2026-27 assessments, not the 2025-26 return.
- Is the taxpayer an individual, and were they an Australian resident at any time in that year? Confirm dates and unresolved residency facts.
- Which amounts fall within the listed assessable labour income categories, and what is their total? Distinguish wages from business income, attributed PSI and investment income; actual withholding alone does not decide this.
- Which covered actual deductions will be claimed, after confirming eligibility, timing, apportionment and substantiation for the whole claimed amount? Choosing not to claim covered expenses is different from guessing their amounts.
- Which separately allowable deductions fall outside the standard-deduction reduction, and what provision and records support each?
- Are there reimbursements, salary packaging or GST credits affecting a claim?
- Which facts or source conditions remain unresolved? Hold the affected calculation and return Needs Input.

## The method, step by step

### Section 1 - The vocabulary map

**The vocabulary map**

| Mechanism | What it reduces | Typical value of $1 | Australian examples |
| --- | --- | --- | --- |
| **Deduction** | Assessable income, producing taxable income | The taxpayer's marginal rate, so worth more to higher earners | Work-related expenses, rental expenses, business expenses, personal super contributions, donations to deductible gift recipients |
| **Capital allowance** | Assessable income, spread over time or immediately | Marginal rate, but timing changes the value | Decline in value under Division 40, capital works under Division 43, instant asset write-off |
| **Tax offset (also called a rebate)** | Tax payable, after tax is calculated | $1 of tax, regardless of marginal rate | Low income tax offset, seniors and pensioners tax offset, foreign income tax offset, private health insurance rebate |
| **Concession or exemption** | The base itself, or the rules that apply to it | Varies | Small business CGT concessions, the 50% CGT discount, main residence exemption, small business entity concessions |

**Why the distinction matters.** A deduction of $1,000 saves $320 for someone on a 30% marginal
rate plus the 2% Medicare levy, and $470 for someone on the top rate. An offset of $1,000 saves
$1,000 for both, but only if there is $1,000 of tax to reduce.

**Refundable and non-refundable offsets.** Most offsets are non-refundable: they can reduce tax
payable to zero but do not pay out an unused offset. The treatment of any unused amount depends
on the offset: some can transfer, carry forward or reduce other liabilities. Some offsets are
refundable, subject to their eligibility and refundability rules. Franking offsets are generally refundable for eligible resident individuals and complying super funds, but section 67-25 excludes specified recipients, including most corporate tax entities. Section 67-23 makes private health insurance offsets refundable except for the trustee offsets under section 61-205(2). Establish the recipient and the applicable exclusions before promising an offset refund.
[ATO, About tax offsets](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets)

### Section 3 - The order of operations

- **Order of operations** — Apply the statutory offset priorities, including the rules for any unused amount. 1. Work out assessable income, including net capital gains. 2. Subtract allowable deductions to get taxable income. 3. Apply the rates for the income year to taxable income, giving basic income tax liability. 4. Calculate the Medicare levy and any Medicare levy surcharge separately. 5. Apply offsets to basic income tax liability in the order in section 63-10. For each unused amount, follow its statutory treatment: application to another liability, transfer, carry-forward, refund or loss. See Section 8.2 for the Medicare levy exceptions. 6. Add the remaining income tax and levy liabilities, then subtract any refundable excess offsets. 7. Subtract amounts already paid: PAYG withholding and PAYG instalments.  _([ITAA 1997 (Cth) s 63-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10))_
- **Tax losses** — A tax loss arises where deductions exceed assessable income. A loss is carried forward, not converted to a refund, and its use is restricted for individuals by the non-commercial loss rules and for companies by the continuity of ownership and business continuity tests.

### Section 4 - Deductions: the decision steps

- **Deductions decision steps overview** — Identify the provision that allows the deduction before applying these steps. Steps 1 and 2 test general deductions under section 8-1. A specific deduction, such as a qualifying gift under Division 30, follows its own eligibility rules; failure of the section 8-1 test does not decide that claim. For specific deductions, apply steps 3 to 6 using the relevant provision's limits, apportionment, timing and evidence requirements.  _([ITAA 1997 (Cth) s 8-5](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-5))_

#### Step 1 - Is there a nexus with assessable income?

- **Nexus test** — A loss or outgoing is deductible to the extent it is incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business for that purpose.  _([ITAA 1997 s 8-1](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-1))_
- **ATO three conditions for employees** — The ATO states the test for an employee as three conditions: the taxpayer spent the money and was not reimbursed, the expense directly relates to earning income, and there is a record to prove it. An employer instruction to buy something does not by itself make it deductible.  _([ATO, Claiming deductions](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/claiming-deductions))_

#### Step 2 - Is it private, domestic or capital in nature?

- **General-deduction exclusions.** Section 8-1 denies a deduction to the extent the outgoing is private or domestic, capital or of a capital nature, or incurred in gaining exempt or non-assessable non-exempt income. Another provision can also prevent the deduction. Ordinary travel between home and work and daily lunches are private. If section 8-1 excludes capital expenditure, check whether it qualifies under another regime: Division 40 decline in value, Division 43 capital works, the CGT cost base or a specific write-off provision such as section 40-880 for certain business-related capital expenditure.

#### Step 3 - Does a specific provision deny or limit it?

- **Specific denials and exceptions.** A qualifying nexus does not override a specific denial. Check section 26-5 for penalties, fines and the denial for general interest charge and shortfall interest charge incurred on or after 1 July 2025. Entertainment under section 32-5 has exceptions in Subdivision 32-B. For vacant-land holding costs, apply section 26-102: test the structure, land use, taxpayer type and exceptions before denying a claim. Qualifying business use by another entity can matter; personal ownership or an empty building alone does not settle the result. Check the specific provision and its exceptions before allowing or denying an unusual item.

#### Step 4 - Apportion

- **Apportionment** — Where an expense serves both an income-producing and a private purpose, only the income-producing share is deductible. The apportionment method must be reasonable and documented. A percentage guessed at year end is not a method.

#### Step 5 - Is it incurred in this income year?

- **Timing and prepayments.** ‘Incurred’ is not the same as ‘paid’. Under section 82KZM of the ITAA 1936, the 12-month rule requires an eligible service period of no more than 12 calendar months that ends no later than the last day of the income year after the expenditure was incurred. It applies to qualifying non-business expenditure of individuals and eligible small or medium business entities, including entities covered by the substituted $50 million turnover test in subsection (1A), where the relevant choice and other conditions are met. A 12-month service period ending later does not qualify for immediate deduction under this rule. Spread the otherwise allowable deduction over the eligible service period as required.

Check the eligible-service-period definition and excluded expenditure in section 82KZL, and any applicable tax-shelter prepayment rules. An exclusion from spreading, such as expenditure below $1,000, does not itself make the expense deductible. For a specific deduction, use its own timing rule. For example, a qualifying gift of money under Division 30 is generally deducted in the income year the gift is made.

#### Step 6 - Is there evidence?

- **Evidence** — See Section 6. Substantiation is a condition of the deduction, not an audit formality.

### Section 5 - The standard deduction for work-related expenses, from 2026-27

Section 25-130 of the ITAA 1997, inserted by Schedule 4 to the Treasury Laws Amendment (Tax
Reform No. 1) Act 2026, applies to assessments for 2026-27 and later years. It does not apply to
the 2025-26 return.

**Who can claim.** An individual who is an Australian resident at any time in the year and derives
assessable labour income. Assessable labour income means amounts subject to PAYG withholding as
salary or wages, director's fees, office holder or religious practitioner payments, return to work
payments, termination and retirement payments, and parental leave pay (s 25-130(4)). An amount in a listed category can count even if no amount was actually withheld; actual PAYG withholding is not an extra eligibility condition. Income outside the listed withholding categories, such as sole trader business income, attributed PSI and investment income, is not assessable labour income. Salary or wages actually paid by a personal services entity can qualify under the employee category. Assess the payment rather than treating every PSI-related amount as excluded.

**How the amount is worked out (s 25-130(2)).**

```
standard deduction = max(0, min($1,000, assessable labour income) - actual work deductions)
```

Actual work deductions are the taxpayer's deductions, to the extent they relate to gaining or
producing assessable labour income, under section 8-1, Division 28 (car expenses), section 25-100
(travel between workplaces), section 25-10 (repairs to work assets), Subdivisions 40-B and 40-D
(decline in value and balancing adjustments of work assets) and section 25-125 (COVID-19 tests).
A taxpayer can claim those deductions. Where their total is below the lesser of $1,000 and assessable labour income, the standard deduction tops the covered total up to that lower ceiling. It does not cap otherwise allowable actual deductions.
Alternatively, the taxpayer can leave out covered expenses and take the standard deduction, and then
needs no records for them. A claimed covered expense must be substantiated under the ordinary rules
for the whole amount claimed, not just the part above the standard deduction. If a claimed expense
is later disallowed, the ATO may increase the standard deduction ([LCR 2026/D5](https://www.ato.gov.au/law/view/view.htm?docid=%22COD%2FLCR2026D5%2FNAT%2FATO%2F00001%22), draft,
paras 28 to 33; [ATO, Standard deduction](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses), Example 2).
With at least $1,000 of assessable labour income, covered actual deductions of $780 give a $220 standard deduction and $1,000 in total. With only $600 of assessable labour income, covered actual deductions of $250 give a $350 standard deduction and $600 in total, even if the taxpayer has substantial investment income. If covered actual deductions equal or exceed the applicable ceiling, the standard deduction is nil; the ceiling does not restrict an independently allowable actual claim.

**Outside the calculation.** Income protection, personal sickness and accident insurance premiums,
and trade, business or professional association fees, do not reduce the standard deduction
(s 25-130(3)) and remain deductible in addition. So do deductions that are not work-related, such
as investment expenses, qualifying gifts to deductible gift recipients and eligible costs of managing tax affairs.

Being outside the standard-deduction calculation does not establish deductibility. For income protection, claim only the personally paid premium component that protects assessable income. Exclude capital cover, such as life, trauma or critical-care cover, and premiums deducted through super. A payment replacing salary can be income even when paid as a lump sum; classify the benefit rather than the payment frequency. [ATO, Income protection insurance](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/investments-insurance-and-super/income-protection-insurance), updated 8 June 2026.

For tax-affairs costs, section 25-5 allows only expenditure within its specified purposes and limits. It excludes tax payments, specified withholding amounts and borrowing costs to pay them, offence-related matters, advice fees without a recognised tax adviser and capital expenditure. A tax-affairs fee is not capital merely because it concerns a capital matter. A computer bought for tax work follows capital-allowance rules rather than an immediate s 25-5 deduction. Classify and apportion the service or asset before claiming; an accounting or software supplier name does not establish the treatment.

**Related changes in the same Schedule.**

- A depreciating asset expected to be used mainly to produce assessable labour income cannot be
  allocated to a low-value pool when first used from 2026-27 (s 40-425(9)); assets pooled for
  2025-26 or earlier are unaffected.
- On a balancing adjustment event for a work asset, a taxpayer who has claimed the standard
  deduction in a year overlapping the asset's effective life may choose a fixed 50% reduction of
  the balancing adjustment amount instead of apportioning (s 40-291A).
- The $300 work expense and $150 laundry exceptions in ss 900-35 to 900-45, and the award transport
  payment exception in Subdivision 900-I, are repealed for assessments for 2026-27 and later years
  (Sch 4 items 11, 12 and 17). This applies to all taxpayers, whether or not they are eligible for
  the standard deduction. See Section 6.
- From FBT years starting on or after 1 April 2027, the otherwise deductible rule does not reduce a
  salary packaged expense payment benefit of a kind the standard deduction covers, and the work
  related item exemption (portable electronic devices, software, protective clothing, briefcases,
  tools of trade) no longer applies to items provided under salary packaging (FBTAA ss 24(1A) and
  58X(2)).

[Treasury Laws Amendment (Tax Reform No. 1) Act 2026, Sch 4](https://www.legislation.gov.au/C2026A00049/asmade/text);
[ATO, New legislation: individuals](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals)

**Practical effect.** For an eligible taxpayer, covered actual deductions plus the standard deduction reach the greater of the covered actual deductions and the lesser of $1,000 and assessable labour income. Confirm eligibility and allowable actual amounts before using that arithmetic; additional deductions outside the calculation remain separate. A zero standard deduction does not remove the accompanying substantiation or asset-rule changes above. The standard deduction is reported in the
2026-27 return; check the 2027 return instructions for the label when the ATO publishes them.

#### 5.1 Working Australians tax offset, from 2027-28

Schedule 3 to the same Act inserts Subdivision 61-E, applying to assessments for 2027-28 and later
years. A resident individual whose net labour income exceeds the tax-free threshold receives a
non-refundable offset equal to the lesser of $250 and the basic income tax liability that would
apply if taxable income were only that net labour income. Net labour income is labour amounts
(assessable labour income, sole trader business income, personal services income, ESS discounts and
labour hire payments) less the related labour deductions, including the standard deduction. The
offset cannot be refunded, transferred or carried forward (s 63-10 table item 3). Include an amount only once if more than one labour-income or labour-deduction category covers it (s 61-155(3)).

### Section 6 - Substantiation

Substantiation is a statutory condition. Division 900 of the ITAA 1997 sets the written evidence
rules for work expenses, car expenses, travel expenses and business travel expenses.

**Substantiation requirements**  _([ATO, Fixed rate method](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method); [ATO, Cents per kilometre method](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-motor-vehicle-expenses/cents-per-kilometre-method))_

| Requirement | Rule |
| --- | --- |
| General work expense evidence | Obtain the applicable written evidence. For supplier documents under s 900-115, record the supplier, amount, nature, expense date and document date. If the expense date is missing, a bank statement or other reasonable independent evidence can establish when it was paid. Missing goods or services details may be written in before lodgement. Decline-in-value evidence follows separate rules |
| The $300 total work expense rule, 2025-26 and earlier only | Where total work expense claims for the year are $300 or less, the written evidence rule is relaxed, but the expense must still have been incurred and the claim must still be reasonable. This is not a free $300. The exception does not apply from 2026-27 ([ATO, Standard deduction](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses)). Work expenses claimed from then need written evidence unless another substantiation rule applies, such as the cents per kilometre method below. A person who is not a resident at any time in the year, such as a foreign resident working holiday maker, cannot get the standard deduction and has no replacement (inferred from s 25-130(1)(b)) |
| Laundry, from 2026-27 | The $150 exception ends. The [ATO standard deduction page](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses) accepts $1 per work-clothes-only load and 50c per mixed load. [Draft LCR 2026/D5](https://www.ato.gov.au/law/view/view.htm?docid=%22COD%2FLCR2026D5%2FNAT%2FATO%2F00001%22), Appendix 2 paragraphs 131-146, describes a proposed compliance approach when claiming all work-related expenses: washing, drying or ironing, not dry cleaning. The detailed ruling is still draft. Confirm deductibility and keep records of the expense and load calculation. A claimed covered amount reduces the standard deduction |
| Car expenses, cents per kilometre method | Up to 5,000 business kilometres per car per year. No written evidence of the kilometres is required, but the basis of the estimate must be able to be shown, for example diary records |
| Car expenses, logbook method | Keep a logbook for at least 12 continuous weeks, or the whole holding period if shorter. A new logbook is normally required after 4 intervening income years, and earlier where s 28-115 requires, including an ATO direction or additional cars. Keep annual odometer records, the business-kilometre estimate, business-use percentage and expense evidence |
| Working from home, fixed rate method | A record of the actual hours worked from home for the entire income year, kept as the hours are worked (an estimate is not accepted), plus at least one record for each running expense the rate covers that the taxpayer incurred. The rate is 70 cents per work hour: [PCG 2023/1 para 26A](https://www.ato.gov.au/law/view/document?docid=COG/PCG20231/NAT/ATO/00001) reads 70c from 1 July 2024 with no end date, whilst the ATO page, updated 8 June 2026, names years only to 2025-26, so confirm the rate for 2026-27. In 2026-27 a claimed amount also reduces the standard deduction |
| Travel with an allowance | Reasonable amounts determined annually by the Commissioner can remove the need to keep receipts, but not the requirement to have incurred the expense |
| Record retention | For Division 900 work-expense records, retain for 5 years from the return due date, or actual lodgement if later (s 900-25). A related tax dispute can extend the period. Check the separate retention rules for depreciating assets, logbooks, CGT assets and carried-forward losses before discarding records |

The cents per kilometre rate and the working from home fixed rate can change between income years.
Look up the rate for the year being prepared rather than carrying last year's forward.

### Section 7 - Capital allowances and write-offs

**Capital allowances and write-offs**  _([ATO, Instant asset write-off](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off))_

| Mechanism | What it applies to | Key point |
| --- | --- | --- |
| Division 40 decline in value | Depreciating assets | Prime cost or diminishing value, over the asset's effective life. The Commissioner's effective life determination is a safe starting point |
| Immediate deduction for low cost items | Depreciating assets costing $300 or less, used predominantly to produce non-business assessable income | Under s 40-80(2), test sets and identical or substantially identical assets started to be held in the same income year. The combined relevant cost must not exceed $300 |
| Instant asset write-off | Small business entities using the simplified depreciation rules | Less than $20,000 per eligible asset for businesses with aggregated turnover under $10 million. Test the asset cost before applying its business-use proportion. For 2025-26 the threshold was a temporary increase; Schedule 2 to the Treasury Laws Amendment (Tax Reform No. 2) Act 2026 makes it permanent for assets first used or installed ready for use from 1 July 2026 |
| Small business general pool | Eligible assets allocated under Subdivision 328-D | Test s 328-210 before annual depreciation: opening pool plus taxable-purpose additions and cost additions, less taxable-purpose termination values. If the amount is above zero but below $20,000, deduct it and close the pool at zero. Otherwise apply 30% to the opening pool and 15% to relevant current-year additions, subject to the disposal and adjustment rules |
| Division 43 capital works | Buildings and structural improvements | A fixed annual rate over a fixed period, claimed separately from Division 40 |
| Division 40-880 | Certain business-related capital expenditure not deductible elsewhere | Spread over five years |
| Car limit | Cars used for a business or income-producing purpose | Caps both the depreciation base and the GST credit. Look up the limit for the income year |

**The 2026-27 limit is settled.** The Treasury Laws Amendment (Tax Reform No. 2) Act 2026 received
assent on 26 August 2026, and its Schedule 2, which commenced on 1 October 2026, sets the
threshold at $20,000 for assets first used or installed ready for use from 1 July 2026, without an
end date. The acquisition date alone does not decide the year: test first use or installation.
[Tax Reform No. 2 Act 2026, Schedule 2](https://www.legislation.gov.au/C2026A00071/asmade/text);
[ATO, Instant asset write-off](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off)

### Section 8 - Tax offsets

#### 8.1 The offsets most often in play

**The offsets most often in play**  _([ATO, Low income tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset); [ATO, Seniors and pensioners tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset))_

| Offset | Refundable | Summary |
| --- | --- | --- |
| Low income tax offset (LITO) | No | Up to $700 where taxable income is $37,500 or less. Between $37,501 and $45,000 the offset is $700 less 5 cents per dollar above $37,500. Above $45,000 it is max(0, $325 less 1.5 cents per dollar above $45,000). The zero floor applies at the upper boundary, including $66,667. Applied automatically |
| Seniors and pensioners tax offset (SAPTO) | No | Requires eligibility for a listed Australian Government pension or allowance, and income tests for the taxpayer and spouse. Unused amounts may be transferable between eligible spouses. Entitlement to at least $1 also raises the Medicare levy low income threshold |
| Private health insurance rebate | Generally, for eligible individuals | Income tested, and can be taken as a premium reduction or an offset. Section 67-23 excludes the trustee offsets under s 61-205(2) from refundable treatment |
| Franking credits on franked dividends | Depends on the recipient | Eligible recipients include the grossed-up dividend in assessable income, then claim the offset. Excess can be refundable for eligible resident individuals and complying super funds; apply the qualification rules and s 67-25 exclusions |
| Foreign income tax offset | No | Limited to eligible foreign tax and the statutory offset limit. The ordinary limit under s 770-75 is the greater of $1,000 and the statutory Australian-tax difference; s 770-80 can increase it for specified amounts. An intended claim no greater than $1,000 does not require the full limit calculation. Apply non-refundable offset ordering separately. See `au-foreign-income.md` |
| Small business income tax offset | No | For an individual with net small business income from a sole trader business or a share from a small business partnership or trust. Confirm the rate and cap for the income year |
| Zone and overseas forces offsets | No | Narrow eligibility rules |
| Beneficiary tax offset | No | For recipients of certain Commonwealth benefits and allowances |
| Working Australians tax offset | No | Up to $250 from 2027-28 for residents with net labour income above the tax-free threshold. See Section 5.1 |
| Research and development tax offset | Depends on the statutory category | Eligible R&D entities and activities under Division 355; see `au-rd-incentive.md` for eligibility, calculation and refundability |

#### 8.2 Unused offsets and other liabilities

- **Unused offsets and other liabilities** — - An unused non-refundable offset is not paid out as an offset refund. Reducing income tax can still create or increase a refund of PAYG withholding or instalments already paid. - Most offsets do not reduce Medicare levy. However, section 63-10 table items 21 and 22 apply remaining veterans' superannuation (invalidity pension) tax offset and foreign income tax offset to Medicare levy, then Medicare levy (fringe benefits) surcharge. The remaining excess cannot be refunded, transferred or carried forward. See `au-foreign-income.md` for FITO limits. - SAPTO affects the Medicare levy indirectly through the low income threshold; it does not reduce the levy directly. - An offset does not reduce a HELP or other study and training support loan repayment, which is calculated on repayment income, not on tax payable.  _([ITAA 1997 (Cth) s 63-10(1), table items 21 and 22](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10); [ATO, About tax offsets](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets))_

### Section 9 - Concessions

Concessions can change the tax base or the rules that apply to it. Keep the mechanism clear: the research and development incentive is a tax offset under section 355-100, rather than a deduction or exemption. Its eligibility and refundability require separate checks in `au-rd-incentive.md`.

**Concessions**

| Concession | Test | Guide |
| --- | --- | --- |
| Small business entity concessions | Aggregated turnover thresholds, which differ by concession | `australia-bookkeeping.md`, `au-individual-return.md` |
| Small business CGT concessions | $6 million maximum net asset value test or CGT small business entity status (aggregated turnover under $2 million, ITAA 1997 s 152-10(1AA)), plus the active asset test | `au-small-business-cgt.md` |
| CGT discount | 12 months of ownership, and entity and residency tests | `au-capital-gains.md` |
| Main residence exemption | Dwelling used as the main residence, with partial and absence rules | `au-capital-gains.md`, `au-rental-property.md` |
| Not-for-profit and DGR concessions | Endorsement and purpose tests | `au-not-for-profit.md` |

Do not treat a concession as available because the taxpayer is small. Each has its own test, and
the aggregated turnover threshold is not the same for every concession.

### Section 10 - Interactions and traps

- **Employer-paid or reimbursed amounts.** An employee cannot also deduct the portion an employer pays or reimburses under the ordinary work-expense rules. Check any remaining personally borne portion against the deduction conditions. Distinguish allowances and taxable recoupments from an ordinary reimbursement; section 51AH of the ITAA 1936 has its own conditions and exclusions. Employer FBT treatment is a separate question.
- **Salary packaging removes it too.** An expense met from pre-tax salary cannot also be deducted.
  The standard deduction measure includes a specific rule preventing that double benefit.
- **GST credits reduce the otherwise allowable cost only to their extent.** Under section 27-5, exclude the amount relating to the input tax credit entitlement and any applicable decreasing adjustment. A partial credit does not require removing all GST. With no credit entitlement, the cost can include GST, but the underlying expense must still qualify for a deduction. Check creditable purpose and any private-use apportionment separately.
- **Non-commercial losses.** Under Division 35, passing one of the 4 activity tests is not enough by itself: the individual must also satisfy the income requirement in section 35-10(2E), which is strictly below $250,000 after its specified adjustments and before deducting the affected business losses. Alternatively, the primary-production or professional-arts exception can apply where unrelated assessable income, excluding any net capital gain, is strictly below $40,000, or the Commissioner may exercise the section 35-55 discretion. Otherwise defer the excess business deductions under section 35-10(2), subject to its modifications. Do not equate business turnover or ordinary taxable income with the statutory income requirement.
- **Personal services income.** PSI rules can deny deductions that would otherwise be available,
  particularly for rent, home office occupancy costs and payments to associates. See `au-psi.md`.
- **Capital allowance and CGT overlap.** Apply the Division 40 balancing-adjustment rules to depreciating assets. Section 118-24 generally disregards a CGT event that is also a balancing adjustment event; its exceptions, including CGT event K7 for non-taxable use, require separate consideration. Division 43 capital works can instead affect the CGT cost base through amounts deducted or deductible under the applicable acquisition and expenditure date rules. Check those rules and exceptions rather than treating both regimes alike. See `au-capital-gains.md`.
- **Personal super contribution timing and entitlement.** A journal entry is not a contribution. Section 290-150 permits a personal contribution deduction only for the year the contribution is made, subject to all applicable Division 290 conditions. Timing alone does not establish entitlement: give a valid notice of intent within the section 290-170 deadline and obtain the fund’s acknowledgement before claiming. The deadline is the earlier of the return-lodgement day and the end of the following income year. Check notice validity before rollovers, withdrawals or starting an income stream, and use `au-super-guarantee.md` for the remaining eligibility and contribution rules.

## Boundary and exception table

### Section 12 - Common errors

- Treating an offset as a deduction, or the reverse, and overstating the benefit by a factor of
  three or more.
- Assuming a non-refundable offset produces a refund where there is no tax to reduce.
- Applying the 2025-26 rules to a 2026-27 return, or the reverse, now that the standard deduction
  and the 15% second bracket apply from 1 July 2026.
- Claiming $300 of work expenses with no expense actually incurred. For 2025-26 and earlier the
  relaxation is of the written evidence rule, not of the requirement to have spent the money, and
  from 2026-27 it does not apply.
- Carrying forward last year's cents per kilometre rate or working from home rate.
- Claiming a deduction for an expense the employer reimbursed, or that was salary packaged.
- Claiming the GST-inclusive cost where a GST credit was also claimed.
- Claiming a capital item as an immediate deduction because it is small, without checking the
  instant asset write-off limit and eligibility for the year.
- Ignoring the non-commercial loss rules for an individual's side business.
- Claiming both Division 40 and Division 43 on the same expenditure.

## Worked cases

### Standard-deduction cases (1 to 4)

Cases 1 to 4 isolate deductions and taxable income for 2026-27. All facts are synthetic. Each taxpayer is an individual Australian resident, and every actual expense shown is independently confirmed deductible for that year after apportionment, GST treatment and evidence checks, with no reimbursement or salary packaging. The salary amounts fall within section 25-130(4), including where no PAYG amount was actually withheld. These are stipulated eligibility facts, not conclusions established by the arithmetic checker. The cases exclude income-tax rates, offsets, Medicare, HELP, payment credits and assessment rounding; they do not calculate a refund or final liability. Use [section 25-130](https://www.legislation.gov.au/C2026C00471/latest/text) and the [ATO standard deduction guidance](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses) for the ceiling and reductions.

### Case 1: separate deductions do not use up the standard deduction

Nadia's $92,000 salary supports a $1,000 ceiling. Her $780 of covered actual deductions leaves a $220 standard deduction. The union fees, eligible income protection premiums, DGR gift and investment interest remain separate deductions. Total deductions are $3,660 and taxable income is $88,340. The retained illustration below continues beyond this deduction-only case; its levy and refund assumptions are outside this new check.

```oa-check
name: AU 2026-27 standard deduction with separate eligible deductions
inputs:
  assessable_labour_income: 92000
  other_assessable_income: 0
  covered_actual_deductions: 780
  union_fees: 620
  eligible_income_protection: 540
  eligible_dgr_gift: 200
  investment_interest: 1300
steps:
  - ceiling: min(1000, assessable_labour_income)
  - standard_deduction: max(0, ceiling - covered_actual_deductions)
  - covered_total: covered_actual_deductions + standard_deduction
  - additional_deductions: union_fees + eligible_income_protection + eligible_dgr_gift + investment_interest
  - total_deductions: covered_total + additional_deductions
  - taxable_income: assessable_labour_income + other_assessable_income - total_deductions
expected:
  ceiling: 1000
  standard_deduction: 220
  covered_total: 1000
  additional_deductions: 2660
  total_deductions: 3660
  taxable_income: 88340
```

### Case 2: investment income does not raise the labour-income ceiling

A resident has $600 of qualifying salary, $20,000 of investment income and $250 of covered actual deductions. The employer withheld no PAYG amount, but the salary still falls within the statutory withholding category. The ceiling is $600, leaving a $350 standard deduction. Independently eligible association fees of $80, income protection premiums of $40 and a DGR gift of $100 do not reduce it. Total deductions are $820 and taxable income is $19,780. A $1,000 ceiling would incorrectly overstate this taxpayer's standard deduction by $400.

```oa-check
name: AU 2026-27 low labour income with investment income
inputs:
  assessable_labour_income: 600
  other_assessable_income: 20000
  covered_actual_deductions: 250
  eligible_association_fees: 80
  eligible_income_protection: 40
  eligible_dgr_gift: 100
steps:
  - ceiling: min(1000, assessable_labour_income)
  - standard_deduction: max(0, ceiling - covered_actual_deductions)
  - covered_total: covered_actual_deductions + standard_deduction
  - additional_deductions: eligible_association_fees + eligible_income_protection + eligible_dgr_gift
  - total_deductions: covered_total + additional_deductions
  - taxable_income: assessable_labour_income + other_assessable_income - total_deductions
expected:
  ceiling: 600
  standard_deduction: 350
  covered_total: 600
  additional_deductions: 220
  total_deductions: 820
  taxable_income: 19780
```

### Case 3: the ceiling does not cap an otherwise allowable actual claim

With $600 of qualifying salary, $20,000 of investment income and $800 of otherwise allowable covered actual deductions, the standard deduction is zero. The $800 actual claim remains deductible on the stipulated facts. Total deductions are $800 and taxable income is $19,800. The floor at zero prevents a negative standard deduction; it does not reduce the actual claim to $600.

```oa-check
name: AU 2026-27 covered actual claim exceeds standard deduction ceiling
inputs:
  assessable_labour_income: 600
  other_assessable_income: 20000
  covered_actual_deductions: 800
steps:
  - ceiling: min(1000, assessable_labour_income)
  - standard_deduction: max(0, ceiling - covered_actual_deductions)
  - total_deductions: covered_actual_deductions + standard_deduction
  - taxable_income: assessable_labour_income + other_assessable_income - total_deductions
expected:
  ceiling: 600
  standard_deduction: 0
  total_deductions: 800
  taxable_income: 19800
```

### Case 4: investment income alone gives no standard deduction

A resident with only $20,000 of investment income has no assessable labour income and does not satisfy section 25-130(1)(c). There is no standard deduction. Independently eligible investment interest of $500 remains deductible, giving taxable income of $19,500. The zero amount below records that prior eligibility decision; the checker cannot decide whether income belongs to a statutory category.

```oa-check
name: AU 2026-27 investment income without qualifying labour income
inputs:
  other_assessable_income: 20000
  eligible_investment_interest: 500
steps:
  - standard_deduction: 0
  - total_deductions: eligible_investment_interest + standard_deduction
  - taxable_income: other_assessable_income - total_deductions
expected:
  standard_deduction: 0
  total_deductions: 500
  taxable_income: 19500
```

Recompute these cases with `python3 scripts/check-examples.py --require skills/international/australia/au-deductions-offsets.md`. It checks arithmetic and assertions, not eligibility, source accuracy or the rest of this guide.

### Further cases: GST entitlement, prepayment timing and Division 35

Cases 5 to 9 use synthetic facts for the rules stated below. They apply the legislation in force on 2 November 2026, assuming it remains applicable to the stated periods. Each underlying expense is independently confirmed otherwise deductible, correctly apportioned and supported by records. The statutory classifications and eligibility decisions described in the prose are established before running the arithmetic checker. These cases exclude final income-tax liability, offsets, Medicare, HELP, payment credits and refunds.

### Case 5: a partial GST credit leaves part of the GST in deductible cost

For 2026-27, a wholly income-producing business expense costs $110 including $10 GST. Mixed taxable and input-taxed activities give a $5 input tax credit entitlement; there is no private use, reimbursement or decreasing adjustment. The otherwise deductible cost is $105 under section 27-5. The comparison results below are separate alternatives: full $10 entitlement gives $100, and no entitlement gives $110. They are not 3 deductions for the same acquisition.

```oa-check
name: AU 2026-27 deductible cost follows actual GST credit entitlement
inputs:
  otherwise_deductible_gross_cost: 110
  partial_credit_entitlement: 5
  full_credit_entitlement: 10
  no_credit_entitlement: 0
steps:
  - cost_with_partial_credit: otherwise_deductible_gross_cost - partial_credit_entitlement
  - cost_with_full_credit: otherwise_deductible_gross_cost - full_credit_entitlement
  - cost_with_no_credit: otherwise_deductible_gross_cost - no_credit_entitlement
expected:
  cost_with_partial_credit: 105
  cost_with_full_credit: 100
  cost_with_no_credit: 110
```

### Case 6: a 12-month prepayment can still fail the end-date condition

An eligible individual incurs and pays $3,660 in June 2027 for otherwise deductible non-business services from 1 January to 31 December 2028. The agreement permits no earlier service. The eligible service period is 12 calendar months, but ends after 30 June 2028, the end of the following income year. Section 82KZM therefore spreads this deduction. No excluded expenditure, tax-shelter rule or other timing provision displaces that treatment. The leap year has 366 service days: zero in 2026-27, 182 in 2027-28 and 184 in 2028-29. Deductions are $0, $1,820 and $1,840. Paying before 30 June does not make $3,660 immediately deductible.

```oa-check
name: AU prepayment ending after the following income year is spread
inputs:
  otherwise_allowable_deduction: 3660
  eligible_service_days: 366
  days_in_2026_27: 0
  days_in_2027_28: 182
  days_in_2028_29: 184
steps:
  - deduction_2026_27: otherwise_allowable_deduction * days_in_2026_27 / eligible_service_days
  - deduction_2027_28: otherwise_allowable_deduction * days_in_2027_28 / eligible_service_days
  - deduction_2028_29: otherwise_allowable_deduction * days_in_2028_29 / eligible_service_days
  - total_deductions: deduction_2026_27 + deduction_2027_28 + deduction_2028_29
expected:
  deduction_2026_27: 0
  deduction_2027_28: 1820
  deduction_2028_29: 1840
  total_deductions: 3660
```

### Case 7: a qualifying 12-calendar-month period can contain 366 days

An eligible individual incurs and pays an otherwise deductible $3,660 non-business prepayment in June 2027 for services from 1 July 2027 to 30 June 2028. The eligible service period is 12 calendar months and ends on the last day of the following income year. No excluded expenditure, tax-shelter rule or other provision changes the result. On those established conditions, the 12-month rule permits the full $3,660 deduction in 2026-27. Do not substitute a 365-day ceiling for the statutory calendar-month test or claim the amount again in 2027-28.

```oa-check
name: AU qualifying leap-year prepayment is deducted once in the incurred year
inputs:
  otherwise_allowable_deduction: 3660
steps:
  - deduction_2026_27: otherwise_allowable_deduction
  - deduction_2027_28: otherwise_allowable_deduction - deduction_2026_27
  - total_deductions: deduction_2026_27 + deduction_2027_28
expected:
  deduction_2026_27: 3660
  deduction_2027_28: 0
  total_deductions: 3660
```

### Case 8: exactly $250,000 fails the Division 35 income requirement

A resident individual has $250,000 of independently classified non-labour assessable bank interest and a genuine sole-trader activity with $25,000 assessable income and $35,000 otherwise allowable deductions for 2026-27. The activity satisfies the $20,000 assessable-income test, but the section 35-10(2E) income total is exactly $250,000 after the required adjustments and before its loss. There is no qualifying labour income, standard deduction or other deduction outside this activity. There are no reportable fringe benefits, reportable super contributions, net investment losses, FHSS amount, exempt income or earlier deferred losses. Neither the primary-production/professional-arts exception nor a Commissioner discretion applies. The $10,000 excess is deferred: passing the activity test does not bypass the income requirement. Taxable income for this limited case is $250,000.

```oa-check
name: AU 2026-27 non-commercial loss at the income requirement boundary
inputs:
  assessable_bank_interest: 250000
  activity_assessable_income: 25000
  otherwise_allowable_activity_deductions: 35000
  other_income_requirement_adjustments: 0
steps:
  - activity_excess: otherwise_allowable_activity_deductions - activity_assessable_income
  - income_requirement_total: assessable_bank_interest + other_income_requirement_adjustments
  - current_activity_deductions: min(otherwise_allowable_activity_deductions, activity_assessable_income)
  - deferred_activity_loss: otherwise_allowable_activity_deductions - current_activity_deductions
  - taxable_income: assessable_bank_interest + activity_assessable_income - current_activity_deductions
expected:
  activity_excess: 10000
  income_requirement_total: 250000
  current_activity_deductions: 25000
  deferred_activity_loss: 10000
  taxable_income: 250000
```

### Case 9: below $250,000, the activity test can permit the loss

Use the same independently confirmed facts as Case 8, except assessable bank interest and the section 35-10(2E) total are $249,999. Both the income requirement and the activity's assessable-income test are satisfied. The $35,000 activity deductions can therefore be used in this year, with no $10,000 deferral under Division 35. Taxable income is $239,999. The checker recomputes this result; it does not decide whether an activity is a business or establish the statutory income classifications.

```oa-check
name: AU 2026-27 non-commercial loss below the income requirement boundary
inputs:
  assessable_bank_interest: 249999
  activity_assessable_income: 25000
  otherwise_allowable_activity_deductions: 35000
  other_income_requirement_adjustments: 0
steps:
  - activity_excess: otherwise_allowable_activity_deductions - activity_assessable_income
  - income_requirement_total: assessable_bank_interest + other_income_requirement_adjustments
  - current_activity_deductions: otherwise_allowable_activity_deductions
  - deferred_activity_loss: otherwise_allowable_activity_deductions - current_activity_deductions
  - taxable_income: assessable_bank_interest + activity_assessable_income - current_activity_deductions
expected:
  activity_excess: 10000
  income_requirement_total: 249999
  current_activity_deductions: 35000
  deferred_activity_loss: 0
  taxable_income: 239999
```

### Case 10: the FITO limit has a $1,000 floor

An otherwise eligible resident individual has $900 of foreign income tax that counts towards the offset. Independently established section 770-75 inputs are $2,000 of Australian tax before offsets and $1,400 under the statutory counterfactual. No section 770-80 increase, other offset, levy or special modification applies. The ordinary limit is the greater of $1,000 and the $600 difference, so the offset is $900. An intended claim no greater than $1,000 does not require the full limit calculation; the optional working here shows why capping it at $600 is wrong. This is an offset-limit illustration, not a final assessment.

```oa-check
name: AU ordinary FITO floor for eligible foreign tax below 1000
inputs:
  foreign_tax_that_counts: 900
  statutory_australian_tax: 2000
  counterfactual_australian_tax: 1400
steps:
  - tax_difference: statutory_australian_tax - counterfactual_australian_tax
  - ordinary_offset_limit: max(1000, tax_difference)
  - foreign_income_tax_offset: min(foreign_tax_that_counts, ordinary_offset_limit)
  - remaining_stated_tax: statutory_australian_tax - foreign_income_tax_offset
expected:
  tax_difference: 600
  ordinary_offset_limit: 1000
  foreign_income_tax_offset: 900
  remaining_stated_tax: 1100
```

### Case 11: the floor can also matter when eligible foreign tax exceeds $1,000

Use Case 10's independently established conditions and tax inputs, but eligible foreign tax is $1,500. The ordinary limit is still $1,000, so the offset is $1,000 and $500 lies above that limit. Do not replace the statutory floor with the $600 Australian-tax difference merely because eligible foreign tax exceeds $1,000. Neither the amount above the limit nor the offset itself is an automatic cash refund.

```oa-check
name: AU ordinary FITO floor for eligible foreign tax above 1000
inputs:
  foreign_tax_that_counts: 1500
  statutory_australian_tax: 2000
  counterfactual_australian_tax: 1400
steps:
  - tax_difference: statutory_australian_tax - counterfactual_australian_tax
  - ordinary_offset_limit: max(1000, tax_difference)
  - foreign_income_tax_offset: min(foreign_tax_that_counts, ordinary_offset_limit)
  - foreign_tax_above_limit: foreign_tax_that_counts - foreign_income_tax_offset
  - remaining_stated_tax: statutory_australian_tax - foreign_income_tax_offset
expected:
  tax_difference: 600
  ordinary_offset_limit: 1000
  foreign_income_tax_offset: 1000
  foreign_tax_above_limit: 500
  remaining_stated_tax: 1000
```

Recompute all 11 cases with `python3 scripts/check-examples.py --require skills/international/australia/au-deductions-offsets.md`. The statutory decisions, eligibility and all excluded assessment components still require separate verification.

### Section 11 - Worked example

**Facts.** Nadia is an Australian tax resident for the whole of the 2026-27 income year. She is an
employee with salary of $92,000 and $19,000 of PAYG withheld. She has no spouse, no private health
insurance obligations in issue, and no HELP debt. All figures are synthetic.

Her substantiated amounts for the year:

**Nadia's substantiated amounts**

| Item | Amount | Treatment |
| --- | --- | --- |
| One qualifying $200 work tool, plus work-related journal and phone use of $580 | $780 total | $200 under s 40-80(2); $580 under s 8-1 |
| Union fees | $620 | Claimable in addition to the standard deduction |
| Income protection insurance premiums | $540 | Claimable in addition to the standard deduction |
| Donation to a deductible gift recipient | $200 | Not work-related, claimable in addition |
| Interest on a margin loan on income-producing shares | $1,300 | Investment expense, claimable in addition |

The tool is first used wholly for her employment in 2026-27, costs no more than $300 and is not part of a set or a group of identical or substantially identical assets exceeding the statutory limit. The journal and phone amount is the independently allowable work-related portion. These are synthetic eligibility assumptions, not conclusions drawn from merchant names.

**Step 1, work out the standard deduction.** Her salary is assessable labour income, and her
covered actual deductions under section 8-1 and Subdivision 40-B total $780. The standard deduction is $1,000 less $780,
or $220, so her work-related deductions total $1,000. Union fees and income protection premiums do
not reduce the standard deduction (s 25-130(3)).

**Step 2, total deductions.**

```
Covered work deductions (ss 8-1 and 40-80(2))        780
Standard deduction for work-related expenses        220
Union fees                                          620
Income protection premiums                          540
DGR donation                                        200
Margin loan interest                              1,300
Total deductions                                  3,660
```

**Step 3, taxable income.**

```
Salary                                           92,000
Less deductions                                   3,660
Taxable income                                   88,340
```

**Step 4, tax at 2026-27 resident rates.**

```
0 to 18,200                                         nil
18,201 to 45,000 at 15c      26,800 x 0.15      = 4,020
45,001 to 88,340 at 30c      43,340 x 0.30      = 13,002
Gross tax                                       = 17,022
```

**Step 5, offsets.** Taxable income of $88,340 exceeds $66,667, so LITO is nil.

**Step 6, Medicare levy and the result.**

```
Medicare levy   88,340 x 2%                     =  1,766.80
Total tax and levy                              = 18,788.80
Less PAYG withheld                              = 19,000.00
Refund                                          =    211.20
```

**Step 7, compare without the standard deduction.** At the same 2026-27 rates, her deductions would
be $3,440, giving taxable income of $88,560, tax of $17,088, a Medicare levy of $1,771.20 and a
refund of $140.80. The $220 standard deduction is worth $70.40, being $220 at her 30% marginal
rate plus the 2% Medicare levy. This is not a 2025-26 result: that year's 16% rate on the same
$88,560 gives tax of $17,356 and $127.20 payable.

**What the example shows.** The value of a deduction is the deduction multiplied by the marginal
rate and the levy, not the deduction itself. It also shows why the four extra items matter: none
of them reduces the standard deduction. Each remains a separate deduction from income, subject to its own eligibility rules; its tax saving depends on the taxpayer's rates and circumstances.

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


### Section 15 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions or outcomes arising from the use of this skill. All outputs
must be reviewed and signed off by a qualified professional in the relevant jurisdiction before
lodging or acting upon them.

The most up-to-date version of this skill is maintained at
[openaccountants.com](https://www.openaccountants.com).

> Contributed by Ryan Duguid.



## Completion checklist

### Section 13 - Self-checks

- [ ] The income year is identified, and the rules used are those for that year.
- [ ] Each item is classified as a deduction, capital allowance, offset or concession.
- [ ] Each offset is identified as refundable or non-refundable.
- [ ] Every deduction meets its governing provision's eligibility rules, limits and apportionment requirements; section 8-1 claims pass the nexus test.
- [ ] Each claim meets its applicable evidence requirements, and any apportionment method is documented.
- [ ] Capital items use the correct regime, including the eligibility rules for any immediate write-off.
- [ ] Amounts reimbursed or salary packaged are excluded.
- [ ] The offsets are applied to tax payable, not to taxable income.
- [ ] Offsets follow section 63-10 priorities, including any application to Medicare levy or surcharge and the treatment of unused amounts.
- [ ] Refunds of excess PAYG payments are distinguished from refunds of unused offsets.
- [ ] Rates, thresholds and limits are confirmed against the ATO page for the income year.

## Sources

| Source | URL | Read on |
|---|---|---|
| ITAA 1936, compilation 193 (C2026C00454): s 51AH; s 82KZL eligible-service-period and excluded-expenditure definitions; s 82KZM | <https://www.legislation.gov.au/C2026C00454/latest/text> | 2026-11-02; compilation in force 1 October 2026; selected provisions and spreading formula only |
| ATO vacant-land guidance: selected overview and excluded entity types | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/land-vacant-land-and-subdividing/deductions-for-vacant-land> | 2026-11-02; page updated 22 June 2026; not a complete page or land-eligibility audit |
| ATO non-commercial losses index: links to loss, income-test and discretion guidance | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/losses/non-commercial-losses> | 2026-11-02; routing page only, not evidence of detailed thresholds |
| ATO: Income protection insurance | <https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/investments-insurance-and-super/income-protection-insurance> | 2026-11-02; updated 8 June 2026; premium/benefit classification and super exclusion only |
| ATO: Gifts and donations | <https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/gifts-and-donations> | 2026-11-02; updated 6 July 2026; gift conditions, DGR status and money-gift overview only |
| ITAA 1997, compilation 268 (C2026C00471): selected ss 8-1, 8-5, 25-5, 25-130, 26-5, 26-102, 27-5, 28-100, 28-115, 28-120, 30-15(1)-(2) and item 1 (money gifts only), 32-5, 32-20, 35-10, 35-30, 35-55, 40-80(2), 40-291A, 40-425, 61-155, 61-160, 61-205, 63-10, 67-23, 67-25, 110-45(1)-(4), 118-24, 290-150, 290-170, 328-180, 328-185, 328-190, 328-200, 328-210, 328-215, 355-100 (offset classification), 770-75, 770-80, 900-15, 900-25, 900-115 and 900-165 | <https://www.legislation.gov.au/C2026C00471/latest/text> | 2026-11-02; compilation in force 1 October 2026; selected provisions, not the whole Act |
| ATO about tax offsets: general non-refundable and refundable distinction | <https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets> | 2026-11-02; page updated 8 June 2026 |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-5> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-1> | Not re-read for this format update; see retained provenance |
| ATO claiming deductions: employee nexus, private/capital exclusions, apportionment, reimbursement and evidence | <https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/claiming-deductions> | 2026-11-02; page updated 13 July 2026; selected general and work-expense guidance |
| Draft LCR 2026/D5: draft status, paragraphs 15-33 on labour income, reductions, exclusions and records, and Appendix 2 paragraphs 131-146 on proposed laundry compliance | <https://www.ato.gov.au/law/view/view.htm?docid=%22COD%2FLCR2026D5%2FNAT%2FATO%2F00001%22> | 2026-11-02; preliminary ATO view, not a final ruling |
| ATO standard deduction: start year, eligibility, labour-income ceiling, exclusions, substantiation, low-value pooling, balancing adjustments and laundry | <https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses> | 2026-11-02; page updated 14 September 2026 |
| Tax Reform No. 1 Act 2026: commencement, selected Schedule 4 standard-deduction, asset, substantiation and FBT amendments and item 17 application; selected Schedule 3 offset provisions and application | <https://www.legislation.gov.au/C2026A00049/asmade/text> | 2026-11-02; standard deduction applies to 2026-27 and later assessments |
| Retained citation | <https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals> | Not re-read for this format update; see retained provenance |
| ATO fixed rate method: covered expenses, actual-hour records and expense evidence | <https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method> | 2026-11-02; page updated 8 June 2026; the page expressly names rates only through 2025-26 |
| ATO cents per kilometre method: eligible taxpayers, car limit and records of the calculation basis | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-motor-vehicle-expenses/cents-per-kilometre-method> | 2026-11-02; page updated 27 May 2026; capture does not establish a numeric 2026-27 rate |
| PCG 2023/1: paragraph 26A rate table and selected paragraphs 27-28 and 58-63 on covered costs and records | <https://www.ato.gov.au/law/view/document?docid=COG/PCG20231/NAT/ATO/00001> | 2026-11-02; 70c from 1 July 2024 without a stated end date; confirm 2026-27 applicability as explained above |
| ATO instant asset write-off: eligibility, timing and cost before business-use apportionment | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off> | 2026-11-02; page updated 28 August 2026; selected guidance |
| Tax Reform No. 2 Act 2026: commencement and Schedule 2 items 1-22, including application | <https://www.legislation.gov.au/C2026A00071/asmade/text> | 2026-11-02; Schedule 2 commenced 1 October 2026 |
| ATO LITO: eligibility, taper and non-refundable limit | <https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset> | 2026-11-02; page updated 8 June 2026; unchanged captured evidence reused from the rates-card check |
| ATO SAPTO: selected pension/allowance and income-test eligibility, transfer and Medicare-threshold guidance | <https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset> | 2026-11-02; page updated 2 October 2026; full pension and income-threshold rules not re-audited |
| Retained citation | <https://www.legislation.gov.au/C2026A00049/latest> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C2026A00050/latest> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents> | Not re-read for this format update; see retained provenance |

### Section 14 - Sources

- Income Tax Assessment Act 1997, s 8-1 (general deductions), s 8-5 (specific deductions),
  Division 25 (specific deductions), Division 26 (denials), Division 40 (capital allowances),
  Division 43 (capital works), Division 900 (substantiation).
- Treasury Laws Amendment (Tax Reform No. 1) Act 2026,
  https://www.legislation.gov.au/C2026A00049/latest
- Income Tax Rates Amendment (Tax Reform No. 1) Act 2026,
  https://www.legislation.gov.au/C2026A00050/latest
- ATO, New legislation: individuals,
  https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals
- ATO, Standard deduction for work-related expenses (updated 14 September 2026),
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses
- Draft Law Companion Ruling LCR 2026/D5, The standard deduction for work-related expenses (draft),
  https://www.ato.gov.au/law/view/view.htm?docid=%22COD%2FLCR2026D5%2FNAT%2FATO%2F00001%22
- PCG 2023/1, working from home fixed rate, para 26A and para 58,
  https://www.ato.gov.au/law/view/document?docid=COG/PCG20231/NAT/ATO/00001
- ATO, Claiming deductions,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/claiming-deductions
- ATO, About tax offsets,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets
- ATO, Low income tax offset,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset
- ATO, Seniors and pensioners tax offset,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset
- ATO, Fixed rate method for working from home,
  https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method
- ATO, Instant asset write-off,
  https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off
- ATO, Tax rates: Australian resident,
  https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents

Sources were checked on 16 September 2026. On 11 October 2026 Schedules 3 and 4 of the Tax Reform
No. 1 Act and Schedule 2 of the Tax Reform No. 2 Act were read on the Federal Register of
Legislation, and the ATO working from home page (updated 8 June 2026) still listed 70 cents only
for 2024-25 and 2025-26. On 31 October 2026 the same page was still updated 8 June 2026, and PCG
2023/1 para 26A read 70c from 1 July 2024 with no end date.

Not yet confirmed: A complete page-level source/read-date audit and independent legal review of the whole guide have not been performed. The 2 November 2026 checks cover only the stated read scopes in the 18 named source rows above and arithmetic in the 11 executable cases. The newer general-deduction, denial, GST, prepayment, Division 35, personal-super notice and R&D classification checks do not establish taxpayer eligibility. Detailed gift eligibility, detailed PSI and concession gateways, other offset eligibility, contribution methods and caps, the retained full-return illustration and levy/refund claims still require reconciliation and qualified review. Other dates and qualifications retain their original scope, including statutory application dates not re-audited here. This remains a tier 2 draft pending qualified review.

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
