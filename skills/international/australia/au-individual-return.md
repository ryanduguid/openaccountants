---
name: au-individual-return
description: Use this skill whenever asked about Australian individual income tax for sole traders. Trigger on phrases like "how much tax do I pay in Australia", "Australian tax return", "sole trader tax", "ABN tax", "Medicare levy", "LITO", "PAYG", "tax brackets Australia", "BAS", "instant asset write-off", "home office deduction", "HELP repayment", "HECS debt", "small business income tax offset", "motor vehicle deduction", or any question about filing or computing income tax for an Australian sole trader. Covers 2025-26 resident tax rates, Medicare levy and surcharge, LITO, business income computation, allowable deductions, depreciation, instant asset write-off, small business income tax offset, HELP/HECS repayments, and final tax computation. ALWAYS read this skill before Australian individual income tax work on a 2025-26 return. For 2026-27 work, read its year coverage section first, then use au-rates-2026-27 and au-deductions-offsets.
version: 2.4
jurisdiction: AU
tax_year: 2025
tax_year_notes: "2025-26"
last_updated: 2026-10-31
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Individual Return

## Year coverage

The figures in this guide are for 2025-26 returns. The current income year is 2026-27 (1 July 2026 to 30 June 2027). For 2026-27 work, do not use the 2025-26 rows below: take figures from `au-rates-2026-27` and the standard deduction from `au-deductions-offsets`. The main differences are:

| Item | 2025-26 (this guide) | 2026-27 | Source |
| --- | --- | --- | --- |
| Resident rate, $18,201 to $45,000 | 16% (maximum $4,288) | 15% (maximum $4,020), so the 16% table overstates 2026-27 tax by $268 at taxable income of $45,000 or more | [ATO, Tax rates: Australian residents](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents) |
| Cents per km | 88c | 91c, same 5,000 km cap | [LI 2026/19, s 6](https://www.ato.gov.au/law/view/view.htm?docid=OPS%2FLI202619%2F00001) |
| Standard deduction for work-related expenses | None | Up to $1,000 for eligible taxpayers with assessable labour income; the $300 and $150 substantiation exceptions end | [ATO, Standard deduction](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/standard-deduction-for-work-related-expenses) |
| MLS base tier | $101,000 single, $202,000 family | $105,000 single, $210,000 family | [ATO, MLS thresholds](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates) |
| HELP bands | Section 5.5 table | Section 5.5, 2026-27 bullet | [ATO, Repayment thresholds](https://www.ato.gov.au/tax-rates-and-codes/study-and-training-support-loans-rates-and-repayment-thresholds) |

## Asset-threshold currency

- **Asset-threshold currency** — For 2025–26, eligible small business entities using simplified depreciation can deduct assets costing less than $20,000 when first used or installed ready for taxable use. The permanent threshold was enacted on 26 August 2026; Schedule 2 commenced on 1 October 2026 and applies to assets first used or installed ready for use from 1 July 2026. The acquisition date alone does not establish the first-use year or a second deduction. Check prior claims and business use.  _([Tax Reform No. 2 Act 2026, schedules 1–2](https://www.legislation.gov.au/C2026A00071/asmade/text))_

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia |
| Tax | Income tax + Medicare levy + HELP repayments (if applicable) |
| Currency | AUD only |
| Tax year | 1 July 2025 -- 30 June 2026 (for 2026-27, see Year coverage) |
| Primary legislation | Income Tax Assessment Act 1997 (ITAA 1997); Income Tax Assessment Act 1936 (ITAA 1936) |
| Supporting legislation | Taxation Administration Act 1953; Medicare Levy Act 1986; Higher Education Support Act 2003 |
| Tax authority | Australian Taxation Office (ATO) |
| Filing portal | myTax (via myGov) or registered tax agent |
| Filing deadline | Self-lodged: 31 October following the 30 June year-end. Tax-agent dates depend on the client: 15 May is the general date for eligible clients not required earlier, and engagement before 31 October does not guarantee it. For 2025-26, self-lodgment is due Monday 2 November 2026 because 31 October 2026 falls on a Saturday; confirm agent dates in the ATO lodgment program |
| Contributor | Open Accountants Community |
| Validated by | Pending -- Australian CPA/CA sign-off required |
| Skill version | 2.4 |

### Tax Rates -- Resident Individual (2025-26) [T1]

**Tax Rates -- Resident Individual (2025-26) [T1]**  _([ATO, Tax rates: Australian residents](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents))_

| Taxable Income (AUD) | Rate | Tax on This Band |
| --- | --- | --- |
| 0 -- 18,200 | 0% | Tax-free threshold |
| 18,201 -- 45,000 | 16% | Max $4,288 |
| 45,001 -- 135,000 | 30% | Max $27,000 |
| 135,001 -- 190,000 | 37% | Max $20,350 |
| 190,001+ | 45% |  |

### Medicare Levy [T1]

**Medicare Levy [T1]**

| Item | Value |
| --- | --- |
| Rate | 2% of taxable income |
| Low-income threshold (single) | $28,011 (no levy below; shade-in $28,012-$35,013) |
| Low-income threshold (family) | $47,238 + $4,338 per dependent child |
| Surcharge (no private hospital cover) | Additional 1%-1.5% if income for MLS purposes exceeds $101,000 (single) or $202,000 (family) in 2025-26 |

### Low Income Tax Offset (LITO) [T1]

**Low Income Tax Offset (LITO) [T1]**

| Taxable Income (AUD) | LITO |
| --- | --- |
| Up to $37,500 | $700 |
| $37,501 -- $45,000 | $700 less 5c per $1 over $37,500 |
| $45,001 -- $66,667 | $325 less 1.5c per $1 over $45,000, minimum $0 |
| $66,668+ | $0 |

### Small Business Income Tax Offset (SBITO) [T1]

**Small Business Income Tax Offset (SBITO) [T1]**

| Item | Value |
| --- | --- |
| Rate | 16% x (total net small business income / taxable income) x basic income tax liability. Total net small business income is limited to taxable income ([ITAA 1997 s 328-360](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/328-360)) |
| Cap | $1,000 |
| Eligibility | Eligible individual with net small business income from their sole-trader business or a qualifying partnership/trust share; business aggregated turnover under $5 million. A trustee is not an additional eligible claimant |
| Net small business income | Assessable income from carrying on the business less deductions attributable to it. Excludes net capital gains, personal services income unless from a personal services business, and salary and wages. Not reduced by tax-related expenses, gifts or personal super contributions. This matters for mixed wage and business income below the cap ([ATO, SBITO](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/concessions-offsets-and-rebates/small-business-income-tax-offset)) |


### Key Deduction Rate Lookups

**Key Deduction Rate Lookups**

| Item | Rate/threshold | Claim handling |
| --- | --- | --- |
| Home office -- fixed rate method | 70 cents per work hour for 2025-26. [PCG 2023/1 para 26A](https://www.ato.gov.au/law/view/document?docid=COG/PCG20231/NAT/ATO/00001) reads 70c from 1 July 2024 with no end date; the [ATO page](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method), updated 8 June 2026, names years only to 2025-26. Confirm for 2026-27, when a claim also reduces any standard deduction | T2 -- method choice, hours, and records/substantiation required |
| Motor vehicle -- cents per km method | 88 cents per km for 2025-26; 91 cents for 2026-27 (max 5,000 km) | T2 -- method choice and business-km support required |
| Instant asset write-off (small business) | $20,000 threshold (assets under $20,000 immediately deductible) | T1 if small-business eligibility and asset cost are clear; otherwise escalate |
| Superannuation (deductible personal contribution) | Up to concessional cap ($30,000 in 2025-26; $32,500 in 2026-27) | T1 rate-cap lookup; notice of intent must be lodged before claiming |

### Conservative Defaults [T1]

**Conservative Defaults [T1]**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | Australian resident (but STOP if genuinely unclear) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown depreciation effective life | Use ATO's Table of Depreciation |
| Unknown private health insurance status | No cover (Medicare levy surcharge may apply) |
| Unknown aggregated turnover | Over $10 million (no small business concessions) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full financial year (1 July to 30 June), confirmation of ABN/TFN, and whether the taxpayer is an Australian resident.

**Recommended** -- all tax invoices issued, purchase receipts, PAYG payment summaries or income statements (via myGov), prior year tax return, BAS lodgments.

**Receipts and substantiation (critical)** -- for deduction claims, keep written evidence (receipt or tax invoice) showing supplier name, cost, date, and nature of expense, plus records of business-use apportionment. A bank or credit-card statement alone is generally not sufficient evidence. Keep most business records for 5 years, generally from when the record was prepared or obtained or the transaction was completed, whichever is later; some records have a different start or a longer period ([ATO, Record-keeping for business](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/record-keeping-for-business/overview-of-record-keeping-rules-for-business)).

**Ideal** -- complete bookkeeping records, depreciation schedule, motor vehicle logbook, home office hours log, private health insurance statement, HELP debt balance.

### Refusal Catalogue

- **R-AU-1 -- Companies and trusts** — Companies lodge company tax returns and trusts lodge trust returns. This skill covers individuals only; use `au-company-tax` or `au-trust-distributions`.
- **R-AU-2 -- Non-residents** — Non-resident tax rates and rules differ significantly. Out of scope; see `au-tax-residency` and `au-nonresident-cgt`.
- **R-AU-3 -- Capital gains tax events** — CGT events require specialised computation (cost base, discounts, exemptions). Out of scope here; use `au-capital-gains`.
- **R-AU-4 -- Complex depreciation (effective life disputes)** — Where the ATO effective life is contested or the asset has no published rate, escalate.
- **R-AU-5 -- Partnership or PSI (Personal Services Income)** — PSI rules and partnership allocations require separate analysis. Use `au-psi` or `au-partnerships` and escalate unresolved facts.

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Tax Label | Treatment | Notes |
| --- | --- | --- | --- |
| ABN INCOME, CLIENT PAYMENT, [client name] | Business income (Item P8) | Gross business income | Core sole trader income |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Revenue | Match to underlying invoices |
| PAYPAL TRANSFER | Business income | Revenue | Report gross before fees |
| DIRECT CREDIT [client name] | Business income | Revenue | Bank transfer from client |
| INTEREST, SAVINGS INTEREST | Interest income (Item 10) | NOT business income | Report separately as interest |
| DIVIDEND, DISTRIBUTION | Dividend income (Item 11) | NOT business income | Report separately. Include franking credits. |
| FRANKING CREDIT | Gross-up dividend | Add to assessable income | Franking credit is both income and tax offset |
| ATO REFUND, TAX REFUND | EXCLUDE | Not income | Prior year tax refund |
| JOBSEEKER, YOUTH ALLOWANCE, AUSTUDY | Australian Government allowances and payments (Item 5) | May be taxable | [ATO, Question 5, 2026](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/income-questions-1-12-individual-tax-return-2026/5-australian-government-allowances-and-payments-2026) names these payments |
| CENTRELINK (other or unnamed payment) | Item 5 (allowances and payments) or Item 6 (pensions and allowances) | May be taxable | Check specific payment type against both questions |
| SUPERANNUATION (lump sum or pension) | Item 7 or 8 | Check | Depends on age and components |
| OWN TRANSFER, SAVINGS | EXCLUDE | Internal | Between own accounts |
| RENTAL INCOME | Rental income (Item 21) | NOT business income | Separate rental schedule |

### 3.2 Expense Patterns (Debits on Bank Statement)

**3.2 Expense Patterns (Debits on Bank Statement)**

A sole trader's business costs go at the P8 expense labels on the business and professional items schedule and flow to net business income (see `au-sole-trader-schedule`; [ATO, Expenses P8](https://www.ato.gov.au/forms-and-instructions/business-and-professional-items-schedule-2026-instructions/instructions-to-complete-the-bpi-schedule-2026/business-income-and-expenses-p8/expenses-p8)). D labels are for employment and other non-business deductions. Putting business costs at D labels overstates net small business income, so it can overstate SBITO and distort the Division 35 and PSI working.

| Pattern | Deduction Category | Tier | Treatment |
| --- | --- | --- | --- |
| RENT, OFFICE RENT, SERVICED OFFICE | Business expense -- occupancy | T1 | Fully deductible if dedicated business premises |
| HOME OFFICE, WORK FROM HOME | Business: P8 P, all other expenses. Employee: D5 | T2 | Fixed rate for the verified return year (70c/hr for 2025-26) OR actual cost method. See Tier 2. |
| PETROL, FUEL, CALTEX, BP, SHELL, AMPOL | Business: P8 N, motor vehicle. Employee: D1 | T2 | Cents/km (88c for 2025-26, max 5,000 km) OR logbook method |
| CAR INSURANCE, REGO, SERVICE | Business: P8 N. Employee: D1 | T2 | Only under logbook method (not cents/km) |
| TOLL, CITYLINK, LINKT | Business: P8 N or P8 P. Employee: D1 or D2 | T1 | Business travel tolls: deductible under either method |
| FLIGHT, QANTAS, VIRGIN, JETSTAR | Business: P8 P. Employee: D2 | T1 | Fully deductible if business travel |
| ACCOMMODATION, HOTEL | Business: P8 P. Employee: D2 | T1 | Deductible if business travel with overnight stay |
| MEALS (business travel, overnight) | Travel | T1 | Reasonable amount while travelling overnight |
| MEALS (client entertainment) | NOT deductible | T1 | Entertainment: NOT deductible for sole traders |
| INSURANCE, PROFESSIONAL INDEMNITY | Business expense -- insurance | T1 | Fully deductible |
| INCOME PROTECTION INSURANCE | Deduction (D15) | T1 | Fully deductible (personal deduction, not business) |
| ACCOUNTING, TAX AGENT, BAS AGENT | Cost of managing tax affairs (D10) | T1 | Fully deductible |
| OFFICE SUPPLIES, OFFICEWORKS | Business expense | T1 | Fully deductible |
| SOFTWARE, SUBSCRIPTION, XERO, MYOB | Business expense -- IT | T1 | Fully deductible |
| GOOGLE ADS, META ADS, FACEBOOK ADS | Business expense -- advertising | T1 | Fully deductible |
| PHONE, TELSTRA, OPTUS, VODAFONE | Business expense -- telecom | T2 | Business portion only |
| INTERNET, NBN | Business expense -- telecom | T2 | Business portion only (or included in home office fixed-rate method) |
| TRAINING, COURSE, SELF-EDUCATION | Business: P8 P. Employee: D4 | T1 | Deductible if directly related to current income-producing activity. NOT deductible if for new career. |
| COMPUTER, LAPTOP, EQUIPMENT (under $20,000) | Instant asset write-off (P8 M and P10) | T1 | Immediately deductible if small business entity and cost < $20,000 |
| COMPUTER, LAPTOP, EQUIPMENT ($20,000 or more), simplified depreciation user | Small business pool (P8 M and P10) | T1 | 15% in the first year, then 30% ([ATO, Simpler depreciation](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business)) |
| COMPUTER, LAPTOP, EQUIPMENT, not using simplified depreciation | Decline in value (P8 M) | T1 | Depreciate over effective life per ATO table |
| SUPER CONTRIBUTION, SUNSUPER, AUSTRALIAN SUPER | Deduction (Item D12) | T1 | Personal deductible super contribution up to the concessional cap ($30,000 in 2025-26; $32,500 in 2026-27). Must lodge notice of intent. |
| ATO TAX, INCOME TAX, PAYG INSTALMENT | EXCLUDE | Not deductible | Tax payments are not deductions |
| GST PAYMENT, BAS PAYMENT | EXCLUDE from income tax | T1 | GST is separate. Report net of GST if registered. |
| PRIVATE HEALTH, MEDIBANK, BUPA, NIB, HCF | NOT a deduction (but affects MLS) | T1 | Private health insurance is NOT tax deductible. But having it avoids Medicare Levy Surcharge. PHI rebate claimed separately. |
| PERSONAL, GROCERY, ENTERTAINMENT | EXCLUDE | Not deductible | Personal expenses |
| DONATION, CHARITY, DGR | Deduction (Item D9) | T1 | Deductible if to a deductible gift recipient (DGR) and genuinely a gift. The $2 minimum no longer applies to gifts made from 1 July 2024 (Treasury Laws Amendment (Delivering an Efficient and Trusted Tax System) Act 2026, Sch 1). |

### 3.3 SaaS Subscriptions

**3.3 SaaS Subscriptions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE | Fully deductible business expense | Operating expense |
| SLACK, ZOOM, NOTION, FIGMA, GITHUB | Fully deductible | Same |
| AWS, HEROKU, DIGITAL OCEAN | Fully deductible | Hosting costs |
| CANVA (AU entity) | Fully deductible | Australian company |
| XERO, MYOB | Fully deductible (cost of managing tax affairs or business expense) | Accounting software |
| SPOTIFY, NETFLIX | NOT deductible | Personal entertainment |

### 3.4 Internal Transfers and Exclusions

**3.4 Internal Transfers and Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER, SAVINGS, TERM DEPOSIT | EXCLUDE | Internal movement |
| MORTGAGE, HOME LOAN | EXCLUDE (or home office %) | Personal. Home office actual costs method only. |
| ATM, CASH | T2 -- ask | Default exclude |
| HECS REPAYMENT, HELP | NOT a deduction | Compulsory repayment is not a tax deduction |

## Section 4 -- Worked Examples

### Example 1 -- Standard Sole Trader (Graphic Designer, 2025-26 rate illustration)

**Input:** ABN income AUD 92,000. Business expenses: software AUD 3,600, advertising AUD 1,200, accounting AUD 1,100, office supplies AUD 800. Home office 1,200 hours at 70c/hr. Car 4,000 business km at 88c/km. No other income. No HELP debt. Has PHI.

**Computation:**
- Business income: AUD 92,000
- Expenses: 3,600 + 1,200 + 1,100 + 800 = AUD 6,700
- Home office: 1,200 x 0.70 = AUD 840
- Motor vehicle: 4,000 x 0.88 = AUD 3,520
- Total deductions: 6,700 + 840 + 3,520 = AUD 11,060
- Taxable income: 92,000 - 11,060 = AUD 80,940
- Tax: 0 + 4,288 + (80,940 - 45,000) x 30% = 4,288 + 10,782 = AUD 15,070
- Medicare: 80,940 x 2% = AUD 1,619
- LITO: $0 (income > $66,667)
- SBITO: 16% x (tax attributable to business income) -- business is 100% of income, so 16% x 15,070 = 2,411, capped at AUD 1,000
- Final tax: 15,070 + 1,619 - 1,000 = AUD 15,689

### Example 2 -- Instant Asset Write-Off

**Input:** Eligible small business entity using simplified depreciation (turnover < $10M). Laptop cost AUD 2,800 and monitor cost AUD 950, both under $20,000 on the applicable cost basis. Both are first used or installed ready for taxable use in 2025-26 and used wholly for the business.

**Classification:** Total immediate deduction: AUD 3,750 in 2025-26, the first-use or ready-for-use year, subject to the remaining write-off conditions. Retain asset and first-use records. If instead purchased on 28 June 2026 but first usable on 2 July 2026, purchase alone gives no 2025-26 write-off; the asset falls into 2026-27, where the $20,000 threshold is permanent.

### Example 3 -- Motor Vehicle (Logbook vs Cents/Km)

**Input:** Total km: 20,000. Business km: 12,000 (60%). Car costs: fuel AUD 4,800, insurance AUD 1,600, rego AUD 800, service AUD 1,200, depreciation AUD 4,000. Total AUD 12,400.

**Computation:**
- Cents/km: min(12,000, 5,000) x $0.88 = AUD 4,400 (capped at 5,000 km)
- Logbook: 12,400 x 60% = AUD 7,440
- Logbook method is significantly more beneficial. But requires a valid logbook kept for a continuous 12-week period.
- [T2] Flag: confirm logbook exists and is valid.

### Example 4 -- Home Office (Fixed Rate vs Actual, 2025-26)

**Input:** Works from home 1,600 hours/year. Dedicated office in 3-bedroom house (1/4 area). Electricity AUD 2,400, internet AUD 1,200, phone AUD 960 (80% business), depreciation on furniture AUD 400.

**Computation:**
- Fixed rate: 1,600 x $0.70 = AUD 1,120 for the covered running costs, plus eligible furniture depreciation of AUD 400. Total = AUD 1,520.
- Actual cost: electricity 1/4 x AUD 2,400 = AUD 600. Internet 80% x AUD 1,200 = AUD 960. Phone 80% x AUD 960 = AUD 768. Depreciation AUD 400. Total = AUD 2,728.
- On these assumptions, the actual-cost deduction of AUD 2,728 exceeds the fixed-rate total of AUD 1,520 by AUD 1,208.
- The fixed rate covers energy, phone, internet, stationery and computer consumables. Eligible furniture and equipment depreciation, repairs to those assets and home-office cleaning can be claimed separately. Occupancy costs require the separate place-of-business conditions. Under actual costs, assess and apportion each expense.
- [T2] Flag: confirm method choice and occupancy costs if actual.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Business Income [T1]

- **Business income treatment** — All amounts derived from carrying on a business. If GST-registered, report net of GST. If not registered, report gross.  _(ITAA 1997 Div 6)_

### 5.2 General Deduction [T1]

- **General deduction** — A deduction for any loss or outgoing to the extent it is incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business. Must not be private, domestic, or capital in nature.  _(ITAA 1997 s8-1)_

### 5.3 Depreciation [T1]

- **Diminishing value** — Base value x (days held / 365) x (200% / effective life)  _(ITAA 1997 Div 40)_
- **Prime cost (straight line)** — Cost x (days held / 365) x (100% / effective life)  _(ITAA 1997 Div 40)_
- **Small business entity simplified depreciation** — Small business entity (turnover < $10M): can use simplified depreciation -- pool assets costing $20,000 or more at 15% in the first year and 30% thereafter.  _(ITAA 1997 Div 40)_
- **Instant asset write-off** - Eligible small business entities using simplified depreciation can deduct assets costing less than $20,000 that are first used or installed ready for taxable use in 2025-26, the year covered here (Treasury Laws Amendment (Strengthening Financial Systems and Other Measures) Act 2025). For assets first used or installed ready for use from 1 July 2026, Schedule 2 of the Treasury Laws Amendment (Tax Reform No. 2) Act 2026 makes the $20,000 threshold permanent; the Act received assent on 26 August 2026 and Schedule 2 commenced on 1 October 2026. _([Act, section 2 and Schedule 2 item 15](https://www.legislation.gov.au/C2026A00071/asmade/text); [ATO, $20,000 instant asset write-off](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/20000-dollars-instant-asset-write-off))_

### 5.4 Superannuation [T1]

- **Personal deductible super contributions** — Personal deductible contributions up to the concessional cap (combined with employer contributions if also employed): $30,000 in 2025-26, **$32,500 in 2026-27**. Must lodge a valid "Notice of intent to claim" with the super fund AND receive acknowledgment BEFORE lodging the tax return or rolling over.  _(ATO contributions caps QC 18123; au-rates-2026-27)_

### 5.5 HELP/HECS Repayment [T1]

Use the 2025–26 thresholds below for this return workflow. Use the separately labelled 2026–27 bands only for that requested year. Both years are marginal: nil at or below the minimum threshold; 15c then 17c on the excess; the top band is 10% of **total** repayment income. Do not use the old 1%--10% of whole-of-income rates.

**5.5 HELP/HECS Repayment [T1]**  _(ATO QC 16176)_

| Repayment income (2025-26) | Compulsory repayment |
| --- | --- |
| $0 -- $67,000 | Nil |
| $67,001 -- $125,000 | 15c for each $1 over $67,000 |
| $125,001 -- $179,285 | $8,700 + 17c for each $1 over $125,000 |
| $179,286+ | 10% of total repayment income |

- **2026-27 HELP repayment bands** — 2026-27: nil to $69,528; 15c over $69,528 to $129,717; $9,028 + 17c over $129,717 to $186,050; 10% of total repayment income from $186,051.  _([ATO, Study and training loan repayment thresholds and rates](https://www.ato.gov.au/tax-rates-and-codes/study-and-training-support-loans-rates-and-repayment-thresholds))_
- **Marginal basis (from 2025-26)** — From 2025-26 compulsory repayments are calculated on a marginal basis (only the income above the minimum repayment threshold), substituted by the Universities Accord (Cutting Student Debt by 20 Per Cent) Act 2025.  _(Universities Accord (Cutting Student Debt by 20 Per Cent) Act 2025)_
- **Repayment income** — Repayment income = taxable income (excluding assessable First Home Super Saver released amounts) + reportable fringe benefits + net investment losses + reportable super contributions + exempt foreign employment income. HELP repayments are NOT deductible.  _(Higher Education Support Act 2003; [ATO, Repayment thresholds](https://www.ato.gov.au/tax-rates-and-codes/study-and-training-support-loans-rates-and-repayment-thresholds))_

### 5.6 Filing and Penalties [T1]

**5.6 Filing and Penalties [T1]**

| Item | Value |
| --- | --- |
| Self-lodge deadline | 31 October following the year-end, or the next business day -- Monday 2 November 2026 for the 2025-26 year this guide covers, because 31 October 2026 is a Saturday |
| Tax agent deadline | Varies (typically March-May 2027) |
| Failure to lodge on time | For the 2025-26 return (due 2 November 2026): $364 per 28 days or part, up to five units ($1,820 base maximum). The unit was $313 from 1 July 2023 to 6 November 2024, $330 from 7 November 2024 to 30 June 2026, and is $364 from 1 July 2026 ([ATO, Penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units)). Determine the applicable date; statutory adjustments and remission can apply. |
| Shortfall penalty (reasonable care not taken) | 25% of shortfall |
| Shortfall penalty (recklessness) | 50% of shortfall |
| General Interest Charge (GIC) | Set quarterly, calculated daily and compounded. 2025-26 annual rates: 10.78% (July to September 2025), 10.61% (October to December 2025), 10.65% (January to March 2026), 10.96% (April to June 2026); 2026-27: 11.43% (July to September 2026), 11.51% (October to December 2026). GIC incurred from 1 July 2025 is not deductible ([ATO, GIC rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates)) |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office [T2]

**6.1 Home Office [T2] methods table**

| Method | What It Covers | Additional Claims |
| --- | --- | --- |
| Fixed rate (verify the return year; 70c/hr for 2025-26) | Electricity, gas, phone, internet, stationery, computer consumables | Eligible furniture and equipment depreciation, repairs to those assets and cleaning; occupancy costs only if the separate place-of-business conditions are met |
| Actual cost | Each expense claimed individually at actual business % | No fixed rate component |

- **Home office record keeping and occupancy expenses** — Under either method: must have records of hours worked from home. Fixed rate, 2023-24 and later: keep a record of the actual hours worked from home for the entire income year, such as a timesheet, roster or diary kept at the time, plus at least one record for each running expense the rate covers. An estimate is not accepted, whether for the whole year or from a sample period, and estimated hours cannot be included in the claim ([ATO, Fixed rate method](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/working-from-home-expenses/fixed-rate-method); [PCG 2023/1](https://www.ato.gov.au/law/view/document?docid=COG/PCG20231/NAT/ATO/00001), para 58). Actual: need receipts and usage records. Occupancy expenses (rent, mortgage interest, rates, home insurance, land tax) are ONLY deductible if you have a dedicated area set aside exclusively as a place of business. These are separate from running expenses. Confirm method, hours, and whether occupancy expenses apply.

### 6.2 Motor Vehicle [T2]

**6.2 Motor Vehicle [T2] methods table**

| Method | How It Works | Records |
| --- | --- | --- |
| Cents per km (88c for 2025-26; 91c for 2026-27) | Max 5,000 business km. No receipts needed. | Reasonable estimate of business km |
| Logbook | Business % of actual costs including depreciation | 12-week continuous logbook, valid for 5 years |

- **Cannot claim both methods** — Cannot claim both. Eligible business parking and tolls can be separate deductions. Roadside assistance is a car operating expense covered by the cents-per-kilometre rate; do not claim it again under that method. Confirm method and km/logbook records.

### 6.3 Private Health Insurance (Medicare Levy Surcharge) [T2]

- **MLS applicability** — If income for MLS purposes exceeds $101,000 (single) or $202,000 (family) for 2025-26 and no appropriate private hospital cover is held, Medicare levy surcharge applies ([ATO, MLS income thresholds and rates](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates)):

**MLS Rate table**

| Income | MLS Rate |
| --- | --- |
| $101,001 -- $118,000 (family $202,001 -- $236,000) | 1% |
| $118,001 -- $158,000 (family $236,001 -- $316,000) | 1.25% |
| $158,001+ (family $316,001+) | 1.5% |

- **PHI rebate** — PHI rebate: income-tested offset that reduces PHI premiums. Claimed via reduced premiums or tax offset. Confirm PHI status and income level.

### 6.4 Personal Services Income (PSI) [T2]

- **PSI rules** — If income is mainly a reward for personal efforts/skills and not from conducting a personal services business, PSI rules limit deductions. Cannot claim rent, mortgage interest, certain home office costs against PSI. Confirm whether PSI rules apply (results test, unrelated clients test, employment test, business premises test).

## Section 7 -- Excel Working Paper Template

```
AUSTRALIAN INDIVIDUAL TAX RETURN -- Working Paper
Tax Year: 2025-26 (for 2026-27, use au-rates-2026-27 figures)

A. INCOME
  A1. Business income (ABN income)                 ___________
  A2. Employment income (per income statement)     ___________
  A3. Interest income                              ___________
  A4. Dividend income (grossed up with franking)   ___________
  A5. Rental income (net)                          ___________
  A6. Other income                                 ___________
  A7. TOTAL ASSESSABLE INCOME                      ___________

B. DEDUCTIONS
  B1. Business expenses (direct)                   ___________
  B2. Home office (verified rate or actual)               ___________
  B3. Motor vehicle (rate for year or logbook)      ___________
  B4. Travel (flights, accommodation)              ___________
  B5. Self-education                               ___________
  B6. Depreciation / instant asset write-off       ___________
  B7. Personal super contributions                 ___________
  B8. Income protection insurance                  ___________
  B9. Cost of managing tax affairs                 ___________
  B10. Donations (DGR)                             ___________
  B11. Other deductions                            ___________
  B12. TOTAL DEDUCTIONS                            ___________

C. TAXABLE INCOME (A7 - B12)                       ___________

D. TAX COMPUTATION
  D1. Tax on taxable income (2025-26 rates)        ___________
  D2. Less: LITO (reduces income tax only)         ___________
  D3. Less: SBITO (16%, max $1,000; income tax only) _________
  D4. Income tax after D2 and D3 (not below nil)   ___________
  D5. Medicare levy (2%)                           ___________
  D6. Medicare levy surcharge (if applicable)      ___________
  D7. HELP/HECS repayment (if applicable)          ___________
  D8. Less: Franking credits offset                ___________
  D9. Less: PHI rebate offset                      ___________
  D10. Less: PAYG instalments paid                 ___________
  D11. Less: PAYG withholding (employment)         ___________
  D12. TAX DUE / (REFUND)                          ___________

REVIEWER FLAGS:
  [ ] Residency status confirmed?
  [ ] Home office method and hours verified?
  [ ] Motor vehicle method confirmed?
  [ ] Instant asset write-off eligibility (SBE < $10M)?
  [ ] Super contribution notice of intent lodged?
  [ ] PHI status confirmed (MLS)?
  [ ] HELP debt status confirmed?
  [ ] All T2 items flagged?
```

## Section 8 -- Bank Statement Reading Guide

### Australian Bank Statement Formats

**Australian Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| CBA, ANZ, Westpac, NAB | CSV, PDF | Date, Description, Debit, Credit, Balance |
| Macquarie, Suncorp, Bendigo | CSV | Date, Narrative, Amount |
| Up, ING, Ubank | CSV | Date, Description, Amount |
| Wise, Revolut | CSV | Date, Description, Amount, Currency |

### Key Australian Banking Terms

**Key Australian Banking Terms**

| Term | Classification Hint |
| --- | --- |
| Direct Credit | Incoming payment -- could be income |
| Direct Debit | Regular outgoing -- likely expense |
| EFTPOS | Point-of-sale purchase |
| BPAY | Bill payment |
| Osko / PayID | Fast payment -- check direction |
| ATM | Cash withdrawal -- ask purpose |
| Interest Paid | Income -- report separately |
| Dividend | Income -- check franking |

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- AUSTRALIA INDIVIDUAL RETURN
1. Are you an Australian resident for tax purposes?
2. Do you have an active ABN and TFN?
3. Are you registered for GST?
4. What is your aggregated turnover? (for small business concessions)
5. Do you work from home? How many hours per year? Method preference (verified fixed rate or actual)?
6. Do you use a vehicle for business? Method preference (cents/km or logbook)?
7. Any assets purchased this year? Cost?
8. Do you have private health insurance? Full year?
9. Do you have a HELP/HECS debt?
10. Are you also employed (PAYG income)?
11. Any personal super contributions made?
12. Prior year tax return / depreciation schedule available?
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**  _(ITAA 1997; Medicare Levy Act 1986; Higher Education Support Act 2003)_

| Topic | Reference |
| --- | --- |
| Assessable income | ITAA 1997 s6-1, s6-5 |
| General deduction | ITAA 1997 s8-1 |
| Capital vs revenue | ITAA 1997 s8-1(2)(a) |
| Depreciation | ITAA 1997 Div 40 |
| Small business entity | ITAA 1997 Div 328 |
| Instant asset write-off | ITAA 1997 s328-180 |
| Home office | ATO Practical Compliance Guideline PCG 2023/1 |
| Motor vehicle | ITAA 1997 s28-13, s28-15; cents-per-km rate set by Income Tax Assessment (Cents per Kilometre Deduction Rate for Car Expenses) Determination 2024 (F2024L00697): 88c for 2024-25 and 2025-26 |
| Superannuation deduction | ITAA 1997 Div 290 |
| Medicare levy | Medicare Levy Act 1986 |
| HELP repayments | Higher Education Support Act 2003 |
| LITO | ITAA 1997 Subdiv 61-D, s 61-110 |
| SBITO | ITAA 1997 Subdiv 328-F, ss 328-355 to 328-375 |

### Interaction with GST [T1]

**Interaction with GST [T1]**

| Scenario | Income Tax Treatment |
| --- | --- |
| GST collected on sales (registered) | NOT income. Report net of GST. |
| GST credits (ITC) recovered | NOT an expense. Report net of GST. |
| Not registered for GST | GST paid on purchases IS part of the cost. Report gross. |
| Must the business register? | Yes at GST turnover of $75,000 or more, current or projected, and for taxi, limousine or ride-sourcing travel regardless of turnover. Check this before treating the business as outside GST ([ATO, Registering for GST](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst)). |
| GST on private portion | Non-claimable GST is part of cost. |

## PROHIBITIONS

- NEVER allow private or domestic expenses as business deductions
- NEVER allow entertainment expenses for sole traders (not deductible)
- NEVER claim more than 5,000 km under the cents-per-km method
- NEVER claim occupancy expenses (rent, mortgage interest) for home office unless dedicated area exclusively for business
- NEVER forget to lodge notice of intent for personal super contributions
- NEVER claim HELP repayments as a deduction
- NEVER claim private health insurance premiums as a deduction
- NEVER apply the instant asset write-off without confirming small business entity status
- NEVER include income tax or GST payments as business deductions
- NEVER report GST-inclusive amounts if GST-registered
- NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or registered tax agent in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
