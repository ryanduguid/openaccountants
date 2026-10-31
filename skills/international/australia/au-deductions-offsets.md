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
version: 0.4
jurisdiction: AU
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
depends_on:
  - au-individual-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Deductions, Offsets and Concessions v0.4

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## What this file is

**Obligation category:** Income tax
**Functional role:** Router and decision framework for everything that reduces Australian tax
**Status:** Source-cited draft, pending accountant review

Australia has no single "reliefs and allowances" concept. Four mechanisms sit behind that idea and
they behave differently, so getting the mechanism right matters more than finding the item.

## Section 1 - The vocabulary map

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
refundable, so the excess is paid out. Franking credits attached to franked dividends and the private health insurance
rebate are refundable. Check this before telling a taxpayer an offset is worth anything to them.
[ATO, About tax offsets](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets)

## Section 2 - Scope statement

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

## Section 3 - The order of operations

- **Order of operations** — Apply the statutory offset priorities, including the rules for any unused amount. 1. Work out assessable income, including net capital gains. 2. Subtract allowable deductions to get taxable income. 3. Apply the rates for the income year to taxable income, giving basic income tax liability. 4. Calculate the Medicare levy and any Medicare levy surcharge separately. 5. Apply offsets to basic income tax liability in the order in section 63-10. For each unused amount, follow its statutory treatment: application to another liability, transfer, carry-forward, refund or loss. See Section 8.2 for the Medicare levy exceptions. 6. Add the remaining income tax and levy liabilities, then subtract any refundable excess offsets. 7. Subtract amounts already paid: PAYG withholding and PAYG instalments.  _([ITAA 1997 (Cth) s 63-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10))_
- **Tax losses** — A tax loss arises where deductions exceed assessable income. A loss is carried forward, not converted to a refund, and its use is restricted for individuals by the non-commercial loss rules and for companies by the continuity of ownership and business continuity tests.

## Section 4 - Deductions: the decision steps

- **Deductions decision steps overview** — Identify the provision that allows the deduction before applying these steps. Steps 1 and 2 test general deductions under section 8-1. A specific deduction, such as a qualifying gift under Division 30, follows its own eligibility rules; failure of the section 8-1 test does not decide that claim. For specific deductions, apply steps 3 to 6 using the relevant provision's limits, apportionment, timing and evidence requirements.  _([ITAA 1997 (Cth) s 8-5](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-5))_

### Step 1 - Is there a nexus with assessable income?

- **Nexus test** — A loss or outgoing is deductible to the extent it is incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business for that purpose.  _([ITAA 1997 s 8-1](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-1))_
- **ATO three conditions for employees** — The ATO states the test for an employee as three conditions: the taxpayer spent the money and was not reimbursed, the expense directly relates to earning income, and there is a record to prove it. An employer instruction to buy something does not by itself make it deductible.  _([ATO, Claiming deductions](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/claiming-deductions))_

### Step 2 - Is it private, domestic or capital in nature?

- **Private, domestic or capital exclusion** — Section 8-1 denies a deduction to the extent the outgoing is private or domestic, or capital or of a capital nature. Ordinary travel between home and work and daily lunches are private. If section 8-1 excludes capital expenditure, check whether it qualifies under another regime: Division 40 decline in value, Division 43 capital works, the CGT cost base, or a specific write-off provision such as section 40-880 for certain business-related capital expenditure.

### Step 3 - Does a specific provision deny or limit it?

- **Specific denial or limit provisions** — Deductibility can be denied even where the nexus exists. Examples include entertainment expenses, penalties and fines, holding costs for vacant land held by most non-business taxpayers, and general interest charge and shortfall interest charge incurred on or after 1 July 2025. Check the specific provision before allowing an unusual item.

### Step 4 - Apportion

- **Apportionment** — Where an expense serves both an income-producing and a private purpose, only the income-producing share is deductible. The apportionment method must be reasonable and documented. A percentage guessed at year end is not a method.

### Step 5 - Is it incurred in this income year?

- **Timing / incurred** — "Incurred" is not the same as "paid". Prepayment rules can spread a deduction over the period the benefit covers, with a 12 month exception available to individuals for non-business expenditure and to small business entities. For a specific deduction, use its own timing rule. For example, a qualifying gift of money under Division 30 is generally deducted in the income year the gift is made.

### Step 6 - Is there evidence?

- **Evidence** — See Section 6. Substantiation is a condition of the deduction, not an audit formality.

## Section 5 - The standard deduction for work-related expenses, from 2026-27

Section 25-130 of the ITAA 1997, inserted by Schedule 4 to the Treasury Laws Amendment (Tax
Reform No. 1) Act 2026, applies to assessments for 2026-27 and later years. It does not apply to
the 2025-26 return.

**Who can claim.** An individual who is an Australian resident at any time in the year and derives
assessable labour income. Assessable labour income means amounts subject to PAYG withholding as
salary or wages, director's fees, office holder or religious practitioner payments, return to work
payments, termination and retirement payments, and parental leave pay (s 25-130(4)). Business
income, personal services income and investment income are not assessable labour income, so a
taxpayer with only those cannot claim it.

**How the amount is worked out (s 25-130(2)).**

```
standard deduction = max(0, min($1,000, assessable labour income) - actual work deductions)
```

Actual work deductions are the taxpayer's deductions, to the extent they relate to gaining or
producing assessable labour income, under section 8-1, Division 28 (car expenses), section 25-100
(travel between workplaces), section 25-10 (repairs to work assets), Subdivisions 40-B and 40-D
(decline in value and balancing adjustments of work assets) and section 25-125 (COVID-19 tests).
A taxpayer can claim those deductions, and the standard deduction then tops the total up to $1,000.
Alternatively, the taxpayer can leave out covered expenses and take the standard deduction, and then
needs no records for them. A claimed covered expense must be substantiated under the ordinary rules
for the whole amount claimed, not just the part above the standard deduction. If a claimed expense
is later disallowed, the ATO may increase the standard deduction ([LCR 2026/D5](https://www.ato.gov.au/law/view/view.htm?docid=%22COD%2FLCR2026D5%2FNAT%2FATO%2F00001%22), draft,
paras 28 to 33; [ATO, Standard deduction](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses), Example 2).
Work-related deductions of $780 therefore give a $220 standard deduction and $1,000 in total, and
deductions of $1,000 or more give a standard deduction of nil.

**Outside the calculation.** Income protection, personal sickness and accident insurance premiums,
and trade, business or professional association fees, do not reduce the standard deduction
(s 25-130(3)) and remain deductible in addition. So do deductions that are not work-related, such
as investment expenses, gifts to deductible gift recipients and the cost of managing tax affairs.

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

**Practical effect.** A work-only taxpayer with substantiated work-related expenses under $1,000
ends up with $1,000 of work deductions in total, and any items claimed still have to meet the
ordinary rules. Above $1,000 nothing changes. The standard deduction is reported in the
2026-27 return; check the 2027 return instructions for the label when the ATO publishes them.

### 5.1 Working Australians tax offset, from 2027-28

Schedule 3 to the same Act inserts Subdivision 61-E, applying to assessments for 2027-28 and later
years. A resident individual whose net labour income exceeds the tax-free threshold receives a
non-refundable offset equal to the lesser of $250 and the basic income tax liability that would
apply if taxable income were only that net labour income. Net labour income is labour amounts
(assessable labour income, sole trader business income, personal services income, ESS discounts and
labour hire payments) less the related labour deductions, including the standard deduction. The
offset cannot be refunded, transferred or carried forward (s 63-10 table item 3).

## Section 6 - Substantiation

Substantiation is a statutory condition. Division 900 of the ITAA 1997 sets the written evidence
rules for work expenses, car expenses, travel expenses and business travel expenses.

**Substantiation requirements**  _([ATO, Fixed rate method](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method); [ATO, Cents per kilometre method](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/deductions/deductions-for-motor-vehicle-expenses/cents-per-kilometre-method))_

| Requirement | Rule |
| --- | --- |
| General work expense evidence | Written evidence is required. The document must show the supplier, the amount, the nature of the goods or services, the date of the expense and the date of the document |
| The $300 total work expense rule, 2025-26 and earlier only | Where total work expense claims for the year are $300 or less, the written evidence rule is relaxed, but the expense must still have been incurred and the claim must still be reasonable. This is not a free $300. The exception does not apply from 2026-27 ([ATO, Standard deduction](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses)). Work expenses claimed from then need written evidence. A person who is not a resident at any time in the year, such as a foreign resident working holiday maker, cannot get the standard deduction and has no replacement (inferred from s 25-130(1)(b)) |
| Laundry, from 2026-27 | The $150 exception ends. Under the compliance approach in [draft LCR 2026/D5](https://www.ato.gov.au/law/view/view.htm?docid=%22COD%2FLCR2026D5%2FNAT%2FATO%2F00001%22), Appendix 2, the ATO accepts $1 per load of work clothes only and 50c per load if other clothes are mixed in, for washing, drying or ironing but not dry cleaning. Keep records showing the calculation. A claimed amount reduces the standard deduction |
| Car expenses, cents per kilometre method | Up to 5,000 business kilometres per car per year. No written evidence of the kilometres is required, but the basis of the estimate must be able to be shown, for example diary records |
| Car expenses, logbook method | A logbook covering a continuous period of at least 12 weeks, valid for five years, plus odometer readings and expense records |
| Working from home, fixed rate method | A record of the actual hours worked from home for the entire income year, kept as the hours are worked (an estimate is not accepted), plus at least one record for each running expense the rate covers. The rate is 70 cents per work hour: [PCG 2023/1 para 26A](https://www.ato.gov.au/law/view/document?docid=COG/PCG20231/NAT/ATO/00001) reads 70c from 1 July 2024 with no end date, whilst the ATO page, updated 8 June 2026, names years only to 2025-26, so confirm the rate for 2026-27. In 2026-27 a claimed amount also reduces the standard deduction |
| Travel with an allowance | Reasonable amounts determined annually by the Commissioner can remove the need to keep receipts, but not the requirement to have incurred the expense |
| Record retention | Generally five years from the date the return is lodged, and longer where a CGT asset or a carried-forward loss depends on the record |

The cents per kilometre rate and the working from home fixed rate can change between income years.
Look up the rate for the year being prepared rather than carrying last year's forward.

## Section 7 - Capital allowances and write-offs

**Capital allowances and write-offs**  _([ATO, Instant asset write-off](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off))_

| Mechanism | What it applies to | Key point |
| --- | --- | --- |
| Division 40 decline in value | Depreciating assets | Prime cost or diminishing value, over the asset's effective life. The Commissioner's effective life determination is a safe starting point |
| Immediate deduction for low cost items | Items costing $300 or less used mainly to produce non-business income | Does not apply to a set, or to substantially identical items, that together cost more than $300 |
| Instant asset write-off | Small business entities using the simplified depreciation rules | $20,000 per asset for businesses with aggregated turnover under $10 million. For 2025-26 the threshold was a temporary increase; Schedule 2 to the Treasury Laws Amendment (Tax Reform No. 2) Act 2026 makes it permanent for assets first used or installed ready for use from 1 July 2026 |
| Small business general pool | Assets costing at or above the instant asset write-off limit | 15% in the first year, 30% each year after |
| Division 43 capital works | Buildings and structural improvements | A fixed annual rate over a fixed period, claimed separately from Division 40 |
| Division 40-880 | Certain business-related capital expenditure not deductible elsewhere | Spread over five years |
| Car limit | Cars used for a business or income-producing purpose | Caps both the depreciation base and the GST credit. Look up the limit for the income year |

**The 2026-27 limit is settled.** The Treasury Laws Amendment (Tax Reform No. 2) Act 2026 received
assent on 26 August 2026, and its Schedule 2, which commenced on 1 October 2026, sets the
threshold at $20,000 for assets first used or installed ready for use from 1 July 2026, without an
end date. The acquisition date alone does not decide the year: test first use or installation.
[Tax Reform No. 2 Act 2026, Schedule 2](https://www.legislation.gov.au/C2026A00071/asmade/text);
[ATO, Instant asset write-off](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off)

## Section 8 - Tax offsets

### 8.1 The offsets most often in play

**The offsets most often in play**  _([ATO, Low income tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset); [ATO, Seniors and pensioners tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset))_

| Offset | Refundable | Summary |
| --- | --- | --- |
| Low income tax offset (LITO) | No | Up to $700 where taxable income is $37,500 or less. Between $37,501 and $45,000 the offset is $700 less 5 cents per dollar above $37,500. Between $45,001 and $66,667 it is $325 less 1.5 cents per dollar above $45,000. Nil above $66,667. Applied automatically |
| Seniors and pensioners tax offset (SAPTO) | No | Requires eligibility for a listed Australian Government pension or allowance, and income tests for the taxpayer and spouse. Unused amounts may be transferable between eligible spouses. Entitlement to at least $1 also raises the Medicare levy low income threshold |
| Private health insurance rebate | Yes | Income tested, and can be taken as a premium reduction or as an offset in the return |
| Franking credits on franked dividends | Yes | Included in assessable income first, then offset against tax, with the excess refundable to most resident individuals and complying super funds |
| Foreign income tax offset | No | Limited to the Australian tax on the doubly taxed income. See `au-foreign-income.md` |
| Small business income tax offset | No | For an individual with net small business income from a sole trader business or a share from a small business partnership or trust. Confirm the rate and cap for the income year |
| Zone and overseas forces offsets | No | Narrow eligibility rules |
| Beneficiary tax offset | No | For recipients of certain Commonwealth benefits and allowances |
| Working Australians tax offset | No | Up to $250 from 2027-28 for residents with net labour income above the tax-free threshold. See Section 5.1 |

### 8.2 Unused offsets and other liabilities

- **Unused offsets and other liabilities** — - An unused non-refundable offset is not paid out as an offset refund. Reducing income tax can still create or increase a refund of PAYG withholding or instalments already paid. - Most offsets do not reduce Medicare levy. However, section 63-10 table items 21 and 22 apply remaining veterans' superannuation (invalidity pension) tax offset and foreign income tax offset to Medicare levy, then Medicare levy (fringe benefits) surcharge. The remaining excess cannot be refunded, transferred or carried forward. See `au-foreign-income.md` for FITO limits. - SAPTO affects the Medicare levy indirectly through the low income threshold; it does not reduce the levy directly. - An offset does not reduce a HELP or other study and training support loan repayment, which is calculated on repayment income, not on tax payable.  _([ITAA 1997 (Cth) s 63-10(1), table items 21 and 22](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10); [ATO, About tax offsets](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/about-tax-offsets))_

## Section 9 - Concessions

Concessions change the base or the rules rather than reducing tax directly.

**Concessions**

| Concession | Test | Guide |
| --- | --- | --- |
| Small business entity concessions | Aggregated turnover thresholds, which differ by concession | `australia-bookkeeping.md`, `au-individual-return.md` |
| Small business CGT concessions | $6 million maximum net asset value test or CGT small business entity status (aggregated turnover under $2 million, ITAA 1997 s 152-10(1AA)), plus the active asset test | `au-small-business-cgt.md` |
| CGT discount | 12 months of ownership, and entity and residency tests | `au-capital-gains.md` |
| Main residence exemption | Dwelling used as the main residence, with partial and absence rules | `au-capital-gains.md`, `au-rental-property.md` |
| Research and development tax incentive | Registered eligible R&D activities | `au-rd-incentive.md` |
| Not-for-profit and DGR concessions | Endorsement and purpose tests | `au-not-for-profit.md` |

Do not treat a concession as available because the taxpayer is small. Each has its own test, and
the aggregated turnover threshold is not the same for every concession.

## Section 10 - Interactions and traps

- **Reimbursement removes the deduction.** An expense the employer pays or reimburses is not
  deductible to the employee. It may instead be a fringe benefit to the employer.
- **Salary packaging removes it too.** An expense met from pre-tax salary cannot also be deducted.
  The standard deduction measure includes a specific rule preventing that double benefit.
- **A GST credit is not a deduction.** Where a GST credit is claimable, the deductible amount is
  the GST-exclusive cost. Where it is not claimable, for example on an input taxed acquisition or
  by an unregistered taxpayer, the GST-inclusive amount is the cost.
- **Non-commercial losses.** An individual's loss from a business activity may be quarantined
  unless one of the statutory tests is met or the Commissioner exercises the discretion.
- **Personal services income.** PSI rules can deny deductions that would otherwise be available,
  particularly for rent, home office occupancy costs and payments to associates. See `au-psi.md`.
- **Capital allowance and CGT overlap.** Amounts deducted under Division 40 or Division 43 reduce
  the cost base of the underlying asset, so a deduction now can increase a capital gain later.
- **Deduction timing versus payment.** Superannuation contributions are deductible in the year the
  fund receives them, not the year they are journalised.

## Section 11 - Worked example

**Facts.** Nadia is an Australian tax resident for the whole of the 2026-27 income year. She is an
employee with salary of $92,000 and $19,000 of PAYG withheld. She has no spouse, no private health
insurance obligations in issue, and no HELP debt. All figures are synthetic.

Her substantiated amounts for the year:

**Nadia's substantiated amounts**

| Item | Amount | Treatment |
| --- | --- | --- |
| Tools, work-related journal, work-related phone use | $780 total | Work-related expenses |
| Union fees | $620 | Claimable in addition to the standard deduction |
| Income protection insurance premiums | $540 | Claimable in addition to the standard deduction |
| Donation to a deductible gift recipient | $200 | Not work-related, claimable in addition |
| Interest on a margin loan on income-producing shares | $1,300 | Investment expense, claimable in addition |

**Step 1, work out the standard deduction.** Her salary is assessable labour income, and her
work-related deductions under section 8-1 total $780. The standard deduction is $1,000 less $780,
or $220, so her work-related deductions total $1,000. Union fees and income protection premiums do
not reduce the standard deduction (s 25-130(3)).

**Step 2, total deductions.**

```
Work-related expenses (s 8-1)                       780
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
of them reduces the standard deduction, so each still reduces tax in full.

## Section 12 - Common errors

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

## Section 13 - Self-checks

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

## Section 14 - Sources

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

## Section 15 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions or outcomes arising from the use of this skill. All outputs
must be reviewed and signed off by a qualified professional in the relevant jurisdiction before
lodging or acting upon them.

The most up-to-date version of this skill is maintained at
[openaccountants.com](https://www.openaccountants.com).

> Contributed by Ryan Duguid.

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
