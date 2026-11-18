---
name: au-fbt
description: >
  Use this skill whenever asked about Australian Fringe Benefits Tax -- identifying fringe benefits in a general ledger, car fringe benefits (statutory formula or operating cost), the electric vehicle exemption, meal entertainment, minor benefits, expense payments and the otherwise-deductible rule, LAFHA, loan benefits, the taxable value of car parking, loan, debt waiver, property, residual, housing, LAFHA and board benefits, employee contributions, reportable fringe benefits amounts (RFBA), FBT gross-up and return preparation. Trigger on phrases like "FBT", "fringe benefits tax", "car fringe benefit", "novated lease FBT", "EV FBT exemption", "entertainment FBT", "minor benefit", "50/50 method", "LAFHA", "living away from home", "gross-up", "Type 1 Type 2", "RFBA", "reportable fringe benefits", or when sweeping a GL for FBT exposure. The FBT year runs 1 April to 31 March. ALWAYS read this skill before touching any FBT work.
version: 1.7
jurisdiction: AU
tax_year: 2026
tax_year_notes: "FBT year ending 31 March 2027 (1 April 2026 - 31 March 2027)"
last_updated: 2026-11-18
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Fringe Benefits Tax (FBT) -- Employer Skill v1.7

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

> Use this skill whenever asked about Australian Fringe Benefits Tax -- identifying fringe benefits in a general ledger, car fringe benefits (statutory formula or operating cost), the electric vehicle exemption, meal entertainment, minor benefits, expense payments and the otherwise-deductible rule, LAFHA, loan benefits, the taxable value of car parking, loan, debt waiver, property, residual, housing, LAFHA and board benefits, employee contributions, reportable fringe benefits amounts (RFBA), FBT gross-up and return preparation. Trigger on phrases like "FBT", "fringe benefits tax", "car fringe benefit", "novated lease FBT", "EV FBT exemption", "entertainment FBT", "minor benefit", "50/50 method", "LAFHA", "living away from home", "gross-up", "Type 1 Type 2", "RFBA", "reportable fringe benefits", or when sweeping a GL for FBT exposure. The FBT year runs 1 April to 31 March. ALWAYS read this skill before touching any FBT work.

## Ask the client first

### Section 2 -- Required inputs and refusal catalogue

#### Required inputs

**Minimum viable** -- entity type and FBT registration status, GL for the FBT year (1 April - 31 March), motor vehicle list with cost/dates/users, entertainment account detail, any salary packaging arrangements.

**Recommended** -- logbooks and odometer records, employee contribution records, declarations (or alternative records under the 1 April 2024 measures), prior year FBT return and workpapers, lease agreements for novated/associate leases.

**Ideal** -- per-employee benefit register, car parking fee evidence, valuer's reports and 12-week registers, LAFH declarations and expense evidence, loan agreements with rates and daily balances, housing leases with prior-year statutory annual values.

#### Refusal catalogue

**R-AU-FBT-1 -- NFP capping and rebates.** *Trigger:* employer is a PBI, health promotion charity, public/not-for-profit hospital, or rebatable employer. *Message:* "Salary packaging caps ($30,000/$17,000 grossed-up; $15,900/$9,010 in benefit value), meal entertainment card arrangements and the FBT rebate are specialist territory. Out of scope -- escalate."

**R-AU-FBT-2 -- Employee share schemes.** *Trigger:* benefit involves shares/options. *Message:* "ESS interests are generally excluded from FBT and taxed under ESS rules. Out of scope."

**R-AU-FBT-3 -- Car parking valuation judgements.** *Trigger:* a car parking value under Rule 13 rests on a fee that may not be representative (s 39AB) or may not be at arm's length or may have been set to cut FBT (s 39E(2)); on a market value without an arm's length valuer's report received before the declaration date (s 39D(3)); on employee or space counts that may not be representative (s 39FB(6)); or on a register that may not be representative or whose benefit count may have risen more than 10% (ss 39GE(2), 39GF(3)). *Message:* "These conditions turn on valuation judgement. Compute only from evidenced fees, reports, counts and registers; escalate the judgement."

**R-AU-FBT-4 -- Airline transport, remote area housing.** *Trigger:* these benefit categories appear. *Message:* "Specialised valuation rules. Out of scope -- escalate."

**R-AU-FBT-5 -- Notional and market values.** *Trigger:* a property, residual or housing value needs a notional value or market value (an arm's length price) that no document establishes: no provider's price to the public, no arm's length cost price or expenditure, no valuer's report and no comparable rents; or the documented price or rent comes from a sale or letting outside the ordinary course of business or whose terms, circumstances or arm's length basis are not comparable. *Message:* "An arm's length value without a market comparison is a valuation judgement. Escalate."

### Section 9 -- Onboarding fallback

If the client provides only a GL and payroll data:

1. Run the Section 3 sweep and build a candidate benefit list by employee
2. Compute car benefits on statutory formula (no logbook assumed)
3. Apply minor benefit screens to gifts/events with per-head < $300
4. Produce a draft liability with every assumption listed
5. **Flag:** "Draft computed from ledger patterns only. Declarations, logbooks, employee contributions, lease documents and salary packaging arrangements not sighted. Reviewer must confirm before lodgment."

## The method, step by step

### Section 1 -- Quick reference

**Read this whole section before computing or classifying anything. The FBT year is 1 April - 31 March, NOT the income year.**

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Australia |
| Primary Legislation | Fringe Benefits Tax Assessment Act 1986 (FBTAA) |
| Tax Authority | Australian Taxation Office (ATO) |
| FBT Year | Ending 31 March 2027 (1 April 2026 -- 31 March 2027) |
| Currency | AUD only |
| FBT rate | 47% |
| Type 1 gross-up (provider or GST group member entitled to the relevant GST credit) | 2.0802 |
| Type 2 gross-up (no GST credit entitlement) | 1.8868 |
| Return due -- self-preparer, or tax agent lodging on paper | 21 May 2027 (lodge and pay) |
| Return due -- tax agent lodging electronically | 25 June 2027 (client must be on the agent's FBT list by 21 May 2027) |
| Quarterly instalments | Required in the next year if prior-year FBT liability was $3,000 or more (via activity statements) |
| Record-keeping exemption (base-year aggregate) | $10,962 (year ending 31 March 2027; 20% growth condition -- Rule 12) |
| Car statutory formula rate | 20% flat (post-10 May 2011 commitments) |
| Operating cost deemed depreciation / deemed interest | 25% diminishing value / 8.27% |
| Car parking daily fee threshold | $11.48 |
| Minor benefits exemption | Notional taxable value < $300 AND infrequent/irregular (s 58P) |
| RFBA trigger | Individual fringe benefits amount > $2,000 -> report x 1.8868 via STP (exclusions apply -- Rule 9) |
| EV exemption | Battery electric / hydrogen cars still exempt (conditions apply); **PHEVs NOT exempt from 1 April 2025** except grandfathered binding commitments; announced wind-back from 1 April 2027, not yet law -- Rule 5 |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown GST creditability of a benefit | Ask -- decides Type 1 vs Type 2 gross-up; never assume Type 1 |
| Unknown car method election | Compute both statutory formula and operating cost where a logbook exists; use statutory if no logbook |
| Unknown logbook or odometer records | Assume NO valid logbook/odometer set (statutory formula applies); flag |
| PHEV in the fleet | Assume NOT exempt (post-1 April 2025) unless a pre-1-April-2025 binding commitment is evidenced |
| Unknown employee contribution | Assume nil; ask |
| Entertainment attendee split unknown | Flag -- actual method needs the employee/non-employee split |
| Not-for-profit employer | STOP -- capping/rebate rules out of scope (R-AU-FBT-1) |

### Section 3 -- GL sweep library

FBT work starts with a ledger sweep, not a form. These are the account patterns that hide benefits.

#### 3.1 High-yield accounts

**High-yield accounts**

| GL account pattern | Likely benefit | Action |
| --- | --- | --- |
| Motor vehicle -- fuel, rego, insurance, repairs, lease | Car fringe benefit | Build the car register (Section 5, Rules 3-4) |
| Entertainment, staff amenities, sundry expenses | Meal entertainment / minor benefits | Split sustenance vs entertainment; attendee analysis |
| Staff gifts, staff welfare | Property/minor benefits | $300 minor test per gift (s 58P) |
| Travel -- accommodation and meals | Travelling vs LAFH boundary | Apply PCG 2021/3 safe harbour (T2-4) |
| Employee reimbursements | Expense payment benefits | Otherwise-deductible check + declaration |
| Loans to employees / directors' loan accounts (debit) | Loan benefit | Compare rate charged to 8.27% benchmark (also check Div 7A for shareholders -- separate regime) |
| Gym/health/wellness, club memberships | Expense payment / residual | Rarely exempt; work-related-item test fails for these |
| Phone/laptop purchases for staff | Possibly exempt s 58X | Portable device, primarily work use; one-per-year rule unless small business (Rule 10 -- NOTE rules change 1 April 2027) |

#### 3.2 Sustenance vs entertainment (the perennial misclassification)

**Sustenance vs entertainment**

| Fact pattern | Treatment |
| --- | --- |
| Morning tea, biscuits, sandwiches consumed on premises during work | Sustenance -- NOT entertainment, no FBT, deductible |
| Meal with alcohol, restaurant, off-site | Entertainment -- FBT analysis required |
| Coffee with a client (light, on business) | Likely sustenance/marginal -- flag, err to entertainment if elaborate |
| Christmas party, staff drinks: taxable employer, no Division 9A election, food and drink provided to and consumed by current employees on a working day on business premises | Exempt property benefit even if entertainment, unless salary packaged ([s 41 FBTAA](https://www.ato.gov.au/law/view/document?docid=PAC/19860039/41); [TR 97/17 para 44](https://www.ato.gov.au/law/view/document?docid=TXR/TR9717/NAT/ATO/00001); [FBT guide ch 14](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00015)). No minor benefit test needed for those items |
| Same on-premises function: associates of employees | Not exempt under s 41. Apportion per head ([FBT guide ch 14](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00015); TR 97/17 para 45), then apply the minor benefit test to the associates' share |
| Taxable employer, no Division 9A election: function off the premises | Entertainment -- minor benefit test per head if < $300 and infrequent |
| Employer elected the 50/50 or 12-week register method (Rule 8) | Section 41 does not apply to meal entertainment: include all of it, on-premises functions and non-employees too, in total meal entertainment ([TR 97/17 paras 31-32, 44](https://www.ato.gov.au/law/view/document?docid=TXR/TR9717/NAT/ATO/00001)). No minor benefit exclusion |
| Income-tax-exempt employer | A Christmas party is tax-exempt body entertainment, on or off the premises ([s 38 FBTAA](https://www.ato.gov.au/law/view/document?docid=PAC/19860039/38); [FBT guide ch 15](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00016)). Section 41 does not apply to it (TR 97/17 para 34), and the minor benefit exemption is limited. Flag for reviewer; these employers may also elect Division 9A |
| Meal while travelling overnight for work | Not entertainment for the traveller -- travel expense |

### Section 5 -- Tier 1 rules

#### Rule 1 -- FBT liability formula

For an ordinary taxable employer, add the taxable values by GST-creditability class, gross up each class and add the results. Type 1 uses **2.0802** where the benefit provider or a member of its GST group is or was entitled to the relevant GST credit under FBTAA s 149A. Actual claiming is not the test. Type 2 uses **1.8868** where there is no such entitlement. Confirm the facts; unknown entitlement means **Needs Input**.

Include taxable benefits excluded from employee RFBA reporting in the appropriate employer aggregate. An RFBA exclusion is not an FBT exemption. Apply the current ATO employer guide's nearest-whole-dollar rounding to each grossed-up aggregate, add those amounts and multiply by **47%**, keeping cents in the tax. Do not round each benefit separately or apply the rate to the unrounded aggregates. For return preparation, use the approved form/software for the relevant year; the 2026 form specifies whole-dollar fields at items 14 and 15. NFP caps/rebates and the record-keeping exemption's earlier-year calculation require separate assessment.

Sources: [FBTAA ss 5B, 5C](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1), [s 149A](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/2), [FBT Tax Act s 6](https://www.legislation.gov.au/C2004A03281/2018-06-19/text) and [ATO employer guide, chapter 2](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00003).

#### Rule 2 -- Return and payment dates (2027 FBT year)

- **Return and payment dates** — Self-preparers and paper-lodging agents: lodge and pay by 21 May 2027. Agents lodging electronically: 25 June 2027, client must be on the agent's FBT client list by 21 May 2027 -- a client added after 21 May reverts to the 21 May due date (already late if unlodged). Prior-year liability >= $3,000 -> quarterly instalments next year via activity statements.

#### Rule 3 -- Car statutory formula

- **Car statutory formula** — ``` Taxable value = 20% x base value x (days available for private use / days in FBT year) - employee contributions ``` Base value = GST-inclusive cost including luxury car tax and non-business accessories fitted at acquisition (less registration/stamp duty), reduced by one-third from the first FBT year commencing after the fourth anniversary of the date the car was first held by the employer or an associate (once only; holding need not be continuous; the reduction never applies to non-business accessories added after acquisition). 20% applies to all post-10-May-2011 commitments. A car garaged at or near the employee's home is taken to be available for private use.

#### Rule 4 -- Car operating cost method

- **Car operating cost method** — ``` Taxable value = total operating costs x private-use percentage - employee contributions ``` Operating costs include actual running costs PLUS deemed depreciation (25% diminishing value on the depreciated value, cars held from 10 May 2006) and deemed interest (8.27% for the year ending 31 March 2027) for owned cars. Business percentage requires a valid logbook: continuous 12-week representative period, valid 5 years, plus full-year odometer records. No valid logbook -> statutory formula. Employer may choose per car, per year, whichever gives the lower value.

#### Rule 5 -- Electric vehicle exemption (and its edges)

- **Electric vehicle exemption** — Exempt if ALL: battery electric or hydrogen fuel cell car (PHEVs excluded from 1 April 2025 -- see below); designed to carry < 1 tonne and < 9 passengers (motorcycles/scooters never qualify); first held AND used on or after 1 July 2022; used by a current employee or their associates; luxury car tax has NEVER been payable on any supply or importation -- check whether LCT was actually payable from the sale documents (the car's LCT value against the fuel-efficient threshold for the financial year of the relevant sale; $91,661 for 2026-27 sales), never by raw price comparison. Associated car expenses (registration, insurance, repairs or maintenance, fuel including electricity) are also exempt, but a home charging station is not an associated car expense and may be a property or expense payment fringe benefit ([ATO, Electric cars exemption](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/types-of-fringe-benefits/fbt-on-cars-other-vehicles-parking-and-tolls/electric-cars-exemption)). **The exempt car benefit still generates an RFBA** via notional taxable value (Rule 9); the value of associated car expense benefits is left out of that amount ([ATO, Electric vehicles and FBT fact sheet](https://www.ato.gov.au/law/view/document?DocID=AFS%2FEV-FBT%2F00001&PiT=99991231235958)). PHEV grandfathering: exempt use before 1 April 2025 plus a financially binding commitment continuing on and after that date; optional extensions are not binding. **Transition warning -- ANNOUNCED, NOT YET LAW:** the Government announced on 5 May 2026, as part of the 2026-27 Budget (delivered 12 May 2026), a wind-back of the exemption from 1 April 2027: full exemption retained only for electric cars costing $75,000 or less (0% statutory formula rate); cars above $75,000 but below the LCT threshold get a 25% discount on FBT payable (15% statutory formula rate); from 1 April 2029 all eligible electric cars drop to the 25% discount. Existing leases are grandfathered. The current exemption runs unchanged to 31 March 2027. Flag any new EV novated lease commencing on or after 1 April 2027 and verify enactment status (ato.gov.au new legislation QC 107286) before advising -- this is an announcement only, not enacted law.  _(ato.gov.au new legislation QC 107286; LCT thresholds 2026-27 ($91,661 for 2026-27 sales))_

#### Rule 6 -- Car parking

- **Car parking** — A car parking benefit needs, on the same day: parking > 4 hours between 7am-7pm on employer premises at/near the primary place of employment; the employee's car parked and commuting use; AND at least one commercial parking station within 1 km that charged a lowest representative fee for all-day parking above $11.48 on the first business day of the FBT year (1 April 2026 for the 2027 year -- no on-the-day fee test exists). Small business exemption: parking is not at a commercial car park AND (gross total income < $10m OR aggregated turnover < $50m) AND not a government body or listed company. Value the benefits under Rule 13.

#### Rule 7 -- Minor benefits (s 58P)

- **Minor benefits** — Notional taxable value < $300 (not indexed; per benefit, per occasion) AND unreasonable to treat as a fringe benefit having regard to infrequency/irregularity and the other s 58P(1)(f) criteria (TR 2007/12: no fixed number of occasions). Assess all s 58P factors for the actual benefits and associated benefits. Frequency is a screening input, not a quarterly safe harbour; document the conclusion under TR 2007/12. Exempt entertainment gets no deduction and no GST credit.  _(s 58P FBTAA; TR 2007/12)_

#### Rule 8 -- Meal entertainment methods

- **Meal entertainment methods** — 1. **Actual** (default; MANDATORY for salary-packaged meal entertainment): taxable value = amounts for employees/associates; client share not subject to FBT (and not deductible). 2. **50/50 split** (Division 9A election): 50% of ALL meal entertainment is the taxable value, regardless of attendees; only 50% deductible/GST-creditable (s 51AEA). 3. **12-week register**: register percentage applied to the year's spend. The minor benefits exemption is NOT available for meal entertainment once a 50/50 or register election is made -- it applies only under the actual method. Entertainment is income-tax deductible and GST-creditable ONLY to the extent it is a fringe benefit subject to FBT.  _(Division 9A FBTAA; s 51AEA)_

#### Rule 9 -- Employee contributions and RFBA

- **Employee contributions and RFBA** — Contributions: after-tax only, reduce the taxable value of THAT benefit only (no cross-application; not for tax-exempt body entertainment), are assessable income to the employer, and carry GST consequences. RFBA: computed on the employee's INDIVIDUAL fringe benefits amount, which EXCLUDES car parking benefits, meal entertainment not provided under a salary packaging arrangement (50/50 and register amounts are never allocable to employees), pooled/shared cars, and remote-area concessions -- and INCLUDES the notional value of exempt electric car benefits (the exception running the other way). Where that amount exceeds $2,000 for the FBT year, report it x 1.8868 (always the Type 2 factor, in whole dollars) through STP finalisation. RFBA affects the employee's income tests, not their taxable income.

#### Rule 10 -- Otherwise-deductible rule and declarations

- **Otherwise-deductible rule and declarations** — Expense payment/property/residual/loan benefits: taxable value reduced by what the employee could have claimed as a once-only deduction. Requires a declaration in the approved form before the declaration date -- or, from 1 April 2024, adequate alternative records per the Commissioner's legislative instruments (available for 11 record types; logbooks and odometer records still need the approved form). Portable electronic devices (s 58X): exempt if primarily for work; one substantially-identical item per year unless a replacement, or the employer's aggregated turnover is under $50 million. **Transition warning:** from 1 April 2027, Act No 49 of 2026 (Sch 4 Pt 2) removes the one-per-year limit and the turnover carve-out, denies s 58X entirely for items provided under a salary packaging arrangement, and (new s 24(1A)) blocks the otherwise-deductible rule for salary-packaged expense payments of standard-deduction work expenses -- flag any packaging arrangement extending past 31 March 2027.  _(s 58X FBTAA; Act No 49 of 2026 (Sch 4 Pt 2); new s 24(1A))_

#### Rule 11 -- LAFHA (standard cases only)

Concessional LAFHA treatment: employee maintains an Australian home they're living away from, first 12 months at a location (FIFO/DIDO excepted from both), declaration held. Without substantiation, food spending is accepted only up to the reasonable amounts in TD 2026/2 (year ending 31 March 2027: $353/week one adult within Australia; $530 two adults; statutory food amount $42/week adult, $21/week child under 12 deducted first). Within reasonable amounts -> no substantiation of food; above -> full substantiation.

Taxable value. Where s 31 (Australian home, first 12 months, declaration) or s 31A (fly-in fly-out or drive-in drive-out, declaration) applies, the taxable value is the allowance less the exempt accommodation component and the exempt food component; otherwise it is the whole allowance (s 31B). Work it per period:

1. Accommodation component and food component: the parts of the allowance the payment terms show to be for accommodation and for food or drink. If the terms do not identify them, escalate.
2. Exempt accommodation component = the lesser of the accommodation component and the accommodation expenses the employee incurred and substantiated (s 31G; s 136(1) 'exempt accommodation component'). Unspent accommodation allowance stays taxable.
3. Applicable statutory food total = $42 a week for each eligible family member aged 12 or more before the FBT year began and $21 a week for each younger one (s 136(1) 'statutory food amount'), reduced, never below nil, by any normal home food cost the employer already took out of the food component (s 31H(2)).
4. Exempt food component = the lesser of (food component - applicable statutory food total) and the food expenses incurred, never below nil (s 31H). The test is what the employee spent, not the allowance: food spending at or below the reasonable amount needs no substantiation; above it, every food expense must be substantiated, not just the excess (s 31G(1)(b); employer guide 11.6). Where spending is at or below the reasonable amount and unsubstantiated, the ATO accepts that the employee spent the lesser of the food component and the reasonable amount, on the footing that before paying the food component the employer could conclude the employee would spend on food or drink; if the evidence does not support that conclusion, escalate. That is ATO administrative practice (employer guide 11.6, 'Expenditure equal to or less than the Commissioner's reasonable food amount'), not the Act, which counts only expenses incurred (s 31H(1)); record that the workpaper relies on it. No exempt food component for days the employee resumes living at home (s 31(3)), and neither reduction while the 12-month period is paused (s 31(4)).
5. Taxable value = allowance - exempt accommodation component - exempt food component.

Sources: [FBTAA ss 30 to 31H](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1) and [s 136(1)](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/2) (compilation 97, read 18 November 2026); [ATO employer guide chapter 11](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00012) (read 18 November 2026). Example 13.

Travelling-vs-LAFH boundary: MT 2030's 21-day rule is WITHDRAWN; TR 2021/4 governs. The PCG 2021/3 compliance approach permits no more than 21 continuous calendar days per stay and no more than 90 calendar days in total at the same work location in the FBT year. Count departure days as directed in paragraph 13. The employee must be away from their normal residence for work, outside FIFO/DIDO arrangements, and return when practicable. Paragraph 12 also requires the employer's qualifying allowance or expense payment, no salary packaging or additional-remuneration option, appropriate reporting and withholding, and substantiating records. Six qualifying 15-day stays meet the numerical limits. Failing the guideline alone does not establish LAFHA treatment; apply TR 2021/4 to the facts.

#### Rule 12 -- Record-keeping exemption and loan benchmark

- **Record-keeping exemption and loan benchmark** — Record-keeping exemption (Pt XIA): an employer with a base year (return lodged, full records kept) whose aggregate fringe benefits amount was <= $10,962 may stop keeping records and pay FBT on the base-year amount -- unless the current year's aggregate exceeds the base-year amount by more than 20%, in which case current-year liability applies and records are needed. In-house benefits (s 62): aggregate taxable value reduced by $1,000 per employee per year; not available for salary-packaged benefits. Loan benefits: notional interest at the benchmark rate (8.27%) on the daily balances, less interest accrued (Rule 14). The benchmark and car-parking figures now publish ONLY on the ATO rates page -- TDs are issued only for cents-per-km and LAFHA food amounts.  _(Pt XIA FBTAA; s 62 FBTAA)_

#### Rule 13 -- Car parking taxable value (Division 10A)

Value car parking only after Rule 6 finds a benefit, which needs a commercial parking station within 1 km whose lowest representative all-day fee on the first business day of the FBT year exceeded the car parking threshold: $11.48 for the year ending 31 March 2027 and $11.03 for the year ending 31 March 2026 (ATO rates page, Table 9; s 39A(1)(a)(iii)). Count benefits per car per day: a space gives one benefit for each car parked in it for more than 4 hours that day (employer guide 16.2). The commercial parking station method applies unless the employer elects another; elections can cover some benefits or employees only, and cannot be changed after the return is lodged (employer guide 16.2.2).

| Method | Taxable value | Inputs the employer must evidence |
| --- | --- | --- |
| Commercial parking station (s 39C), the default | For each benefit, the lowest fee any commercial parking station within 1 km charged the public for all-day parking that day, less the recipient's contribution | Benefits by day; fee evidence for each day |
| Market value (s 39D), elected | For each benefit, the arm's length amount in the valuer's report, less the recipient's contribution | A report in the approved form from a suitably qualified valuer at arm's length, received before the declaration date, on which the return is based (s 39D(3)); benefit count |
| Average cost (s 39DA), elected | For each benefit, (A + B) / 2, less the recipient's contribution; A and B are the lowest fees within 1 km on the first and last days of the FBT year on which a benefit is provided | The 2 days' fee evidence; benefit count |
| Spaces (ss 39FA to 39FE), elected | For each space with a benefit in the year, daily rate amount x days in its availability period / 366 x 228; add the spaces (total statutory benefit); where the average number of employees covered is below the average number of eligible spaces, multiply by average employees / average eligible spaces (s 39FB); then subtract every relevant recipient's contribution | Each space's daily rate amount (by one of the first 3 methods, before contributions, s 39FC); its first and last benefit days in the year; employee and space numbers at the start and end of the parking period |
| 12-week register (ss 39G to 39GH), elected | Total value of benefits in the register x 52 / 12 x days in the car parking availability period / 366 (s 39GB). The register total is the taxable value of the 12 weeks' benefits by one of the first 3 methods, so already net of the recipients' contributions (s 39GC) | A register kept for 12 continuous weeks of benefits, representative of the first year's usage, with the s 39GG details entered as soon as practicable; valid for the FBT year its 12 weeks end in and the 4 after it (s 39GF(1), (2)) |

Fees: a fee charged weekly, monthly or for another period counts as the total fee / business days in the period (s 39E(1)); an early bird fee counts where a reasonable number of spaces are set aside for it; a nil fee, a long-term storage fee or a fee not available on the day does not count (employer guide 16.2.4). The availability periods run from the first to the last day in the FBT year with a benefit (ss 39FD, 39GD), and both formulas divide by 366 whether or not the year has 366 days. The ATO's register example (employer guide 16.2.7.5, Example 17): $2,500 x 52 / 12 x 183 / 366 = $5,416.67. Choose the method giving the lowest value only among methods whose conditions hold. An average cost or spaces election is ineffective if its fees are not representative (ss 39DA(4), 39FA(5)), and a register that is not representative or omits the s 39GG details is not valid (ss 39GE, 39GG). Unrepresentative employee or space counts stop the s 39FB reduction (s 39FB(6)); employer guide 16.2.8.2 goes further and says they bar the spaces method. Those judgements go to R-AU-FBT-3, as does a register whose benefit count may have risen more than 10% on any day of the year (s 39GF(3)). Car parking benefits are excluded from the employee's RFBA (Rule 9); gross up by the GST class (Rule 1).

Sources: [FBTAA Division 10A](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1) (compilation 97, read 18 November 2026); [ATO FBT rates and thresholds, Table 9](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds) (last updated 20 May 2026, read 18 November 2026); [ATO employer guide chapter 16](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00017) (read 18 November 2026). Examples 8 and 9.

#### Rule 14 -- Loan and debt waiver benefits (Divisions 3 and 4)

Loan. A loan gives a benefit for each FBT year in which any of it is owed (s 16(1)). An amount left unpaid after its due date is a loan from the day after, at the interest rate (if any) accruing on it (s 16(2)); unpaid interest on a deferred interest loan (interest neither due within 6 months nor payable by instalments at most 6 months apart, the first within 6 months) becomes a separate nil-interest loan at the end of each 6 months (s 16(3), (4)).

1. Notional interest = the sum of the loan's daily balances in the FBT year x the statutory interest rate / days in the FBT year. The statutory interest rate is the benchmark rate: 8.27% for the year ending 31 March 2027 and 8.62% for the year ending 31 March 2026 (ATO rates page, Table 10; s 136(1) 'notional amount of interest', 'statutory interest rate', 'benchmark interest rate'). Loans made before 1 July 1986 or housing loans made before 3 April 1986 may take a lower rate: escalate. The Act sets the rate on daily balances but no day count and no rounding (s 136(1) 'notional amount of interest'). For a 365-day FBT year, such as the year ending 31 March 2027, dividing by 365 and by the days in the year agree, and a balance owed all year gives balance x rate, as in the ATO's examples (employer guide 8.5, 8.8). For a 366-day FBT year (the year ending 31 March 2028) the 2 divisors differ: send the day count to the reviewer. Rounding to the cent is this guide's convention, not the Act's. Flag a loan agreement that accrues interest on another basis.
2. Taxable value = notional interest - interest accrued on the loan for the year, never below nil (s 18).
3. Otherwise deductible rule (s 19), only where the recipient is the employee and the employee gives a declaration in the approved form before the declaration date (not needed for an employee credit loan or employee share loan, s 19(1)(c); Rule 10 covers alternative records): GD = the once-only deduction the employee would have had for interest equal to the notional interest; RD = the deduction for the interest that accrued (nil if none); ND = GD - RD; taxable value = step 2 - ND, never below nil. Where the employer set the rate having regard to the employee's intended use of the loan, the employee's deduction for the accrued interest is limited and RD changes (employer guide 8.8, second example): escalate. A car loan, including the part of a loan used to buy a car or pay a car expense (s 19(1)(ca), (d), (2)), or a loan deemed provided to the employee alone under s 138(3) (s 19(1)(i), (5)) has its own ND: escalate.

Exempt loans (s 17), for a lender whose business includes lending to the public: a fixed rate, specified in a document when the loan was made and not variable, no lower than its rate for a similar arm's length loan made at or about that time to a member of the public in the ordinary course of its business (s 17(1)); or, year by year, a rate that throughout the FBT year was no lower than the rate applying at that time to a similar arm's length loan the lender made at or about the time it made this loan to a member of the public in the ordinary course of its business (s 17(2)), so a variable-rate loan needs its rate history against the lender's public rates for each year claimed, and any period below them leaves that year's benefit taxable. Also exempt: an advance used only for employment expenses incurred and accounted for within 6 months; an advance for a rental bond or utility deposit repaid within 12 months where the accommodation benefit is exempt or relocation-reduced. A loan that Division 7A of the ITAA 1936 treats as a dividend, or that complies with it under s 109N, is not a fringe benefit (s 136(1) 'fringe benefit' paragraphs (r) and (s)): route shareholder loans through T2-6 first.

Debt waiver. Waiving an employee's obligation to pay or repay an amount is a debt waiver benefit (s 14). Taxable value = the whole amount waived, principal and interest (s 15; employer guide 8.2). No contribution or otherwise deductible reduction applies. A genuine bad debt written off for reasons unrelated to employment is not a benefit (employer guide 8.1); that judgement goes to the reviewer. A waiver that Division 7A treats as a dividend is not a fringe benefit (paragraph (r)).

Loan and debt waiver benefits are always Type 2 (employer guide 8.2, 8.5). Both count towards the employee's individual fringe benefits amount for RFBA (Rule 9): s 5E(3) does not exclude them, nor do the exclusions prescribed under s 5E(3)(i) (FBTA Regulations 2018 ss 6 to 11), and the examples to s 135P(1) are debt waivers.

Sources: [FBTAA Divisions 3 and 4](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1) and [s 136(1)](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/2) (compilation 97, read 18 November 2026); [ATO FBT rates and thresholds, Table 10](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds) (read 18 November 2026); [ATO employer guide chapter 8](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00009) (read 18 November 2026); [FBTA Regulations 2018 Part 2](https://www.ato.gov.au/law/view/fulldocument?filename=REG20181284) (read 18 November 2026). Examples 6 and 10.

#### Rule 15 -- Property and residual benefits (Divisions 11 and 12)

Classify first. A property benefit is in-house where the property is tangible and the provider (the employer or an associate, or a third party that bought it from them, where both carried on such a business) carried on a business providing identical or similar property principally to outsiders at or about the time; a residual benefit (any benefit no other Division covers, s 45) is in-house on the same test for identical or similar benefits (s 136(1)). Everything else is external. Use GST-inclusive values (employer guide 17.3, 18.3).

| Benefit | Value before the recipient's contribution | FBTAA |
| --- | --- | --- |
| In-house, provided under a salary packaging arrangement | Notional value at the provision or comparison time | ss 42(1)(aa), 48(aa), 49(aa) |
| In-house property the provider made, identical goods sold in the ordinary course of business to manufacturers, wholesalers or retailers | The lowest arm's length price for the identical goods at or about the time, early-payment discount included | s 42(1)(a)(i) |
| In-house property the provider made, identical goods sold in the ordinary course of business to the public at arm's length but not to manufacturers, wholesalers or retailers | 75% of the lowest price to the public at or about the time, on identical terms other than price | s 42(1)(a)(ii) |
| In-house property the provider bought for resale | The lesser of its arm's length cost price and its notional value | s 42(1)(b), (2) |
| Other in-house property | 75% of the notional value | s 42(1)(a)(iii), (c) |
| In-house residual, identical benefits (for a period benefit, identical overall benefits) provided to the public in the ordinary course of business at arm's length at or about the time, in similar circumstances and on identical terms other than price | 75% of the lowest price to the public; for a period benefit, the lowest amount for the current year's part | ss 48(a), 49(a) |
| In-house residual, no identical public benefit | 75% of the notional value | ss 48(b), 49(b) |
| External, the employer or an associate bought it at arm's length (property: at or about the provision time) | The amount it paid; a period residual benefit takes the amount for the current year | ss 43(a), 50(a), 51(a) |
| External, a third party provided it and the employer or an associate paid them at arm's length | That expenditure | ss 43(b), 50(b), 51(b) |
| External, otherwise | The notional value | ss 43(c), 50(c), 51(c) |

Airline transport benefits (ss 42(1)(ab), 48(ab), 49(ab)) go to R-AU-FBT-4. Notional value is what the recipient could reasonably be expected to pay the provider at arm's length (s 136(1)): take it from the provider's own price to the public at the time, or escalate under R-AU-FBT-5. A public price sets a value only for a sale in the ordinary course of business, at arm's length, at or about the time, in similar circumstances and on identical terms other than price, and for a period residual benefit only for identical overall benefits (ss 42(1)(a)(ii), 48(a), 49(a)); where any of these differs or is unclear, escalate under R-AU-FBT-5. Then:

1. Subtract the recipient's contribution (consideration the recipient or employee paid for it, less any reimbursement of it, s 136(1)), never below nil.
2. Otherwise deductible rule (ss 44, 52), only where the recipient is the employee and a declaration in the approved form is held before the declaration date (none is needed for an exclusive employee property or residual benefit or one covered by a recurring fringe benefit declaration, ss 44(1)(c), 52(1)(c); Rule 10 covers alternative records): GD = the once-only deduction the employee would have had for spending the value before contribution; RD = the deduction for the contribution (nil if none); reduce the value by GD - RD, never below nil. Car property or car residual benefits and extended travel benefits need car substantiation or a travel diary: escalate.
3. In-house reduction (s 62): reduce the sum of the employee's in-house expense payment, property and residual taxable values for the FBT year by $1,000, or by the sum where it is less. It does not apply to in-house benefits provided under a salary packaging arrangement (s 62(2)).

A period residual benefit spanning 2 FBT years is apportioned between them (employer guide 18.4, 18.5). Gross up by the GST class (Rule 1).

Sources: [FBTAA Divisions 11 and 12, s 62](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1) and [s 136(1)](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/2) (compilation 97, read 18 November 2026); [ATO employer guide chapters 17](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00018) and [18](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00019) (read 18 November 2026). Example 11.

#### Rule 16 -- Housing benefits (Division 6)

A lease or licence to occupy a unit of accommodation as the employee's usual place of residence gives a housing benefit for each FBT year in which it subsists (s 25). Remote area housing goes to R-AU-FBT-4; accommodation while living away from home or travelling for work is not a housing benefit (employer guide 10.6).

Accommodation in a State or internal Territory, other than a caravan, mobile home, hotel, motel, hostel or guesthouse whose provider lets similar units to outsiders (s 26(1)(c)):

1. Statutory annual value (s 26(2)). In a base year: the market value of the housing right for the tenancy period x days in the FBT year / whole days in the tenancy period. In any other year: the previous FBT year's statutory annual value (an occupancy-weighted average where that year was a base year with several benefits for the same or an equivalent right) x the current year's indexation factor for the State or Territory. A base year is a year the employer elects by written notice lodged by the declaration date, a year after one with no housing benefit for the same or an equivalent right, or a year after 9 consecutive years of such benefits none of which was a base year (s 26(3), (7)). A material alteration changing the market value by 10% or more makes a new unit, so a new base year (s 26(5)).
2. Taxable value = statutory annual value x whole days in the tenancy period / days in the FBT year - the recipient's rent (rent or other consideration the recipient or employee paid for the right in the year, less any reimbursement, s 136(1)), never below nil.

Indexation factors (s 28; ATO rates page, Table 11):

| FBT year ending | NSW | VIC | QLD | SA | WA | TAS | NT | ACT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 31 March 2027 | 1.040 | 1.044 | 1.051 | 1.051 | 1.073 | 0.999 | 1.029 | 1.007 |
| 31 March 2026 | 1.076 | 1.066 | 1.076 | 1.060 | 1.100 | 0.988 | 1.031 | 1.010 |

The market value is a market rent for the property as it stands, ignoring any right to have expenses paid and any onerous employment conditions (s 27; employer guide 10.2): take it from a valuer or comparable rents, or escalate under R-AU-FBT-5. The ATO's annualising example for 121 days at $5,200 (employer guide 10.5) prints $15,687.70, which rounds the daily rate to $42.98 before multiplying by 365; the s 26(2)(a) formula, A x B / C, gives $5,200 x 365 / 121 = $15,685.95. Use the formula's figure. The Act sets no rounding; carrying the statutory annual value to the cent, as it becomes next year's base, is this guide's convention and matches the employer guide's other examples. Accommodation outside a State or internal Territory is valued at market value less the recipient's rent (s 26(1)(a)); a caravan or mobile home, or a unit in a hotel, motel, hostel or guesthouse, whose provider lets similar units to outsiders, at market value (75% of it where it would otherwise be an in-house residual benefit) less the recipient's rent (s 26(1)(b)). Escalate either under R-AU-FBT-5 unless a market rent is documented. Gross up by the GST class (Rule 1).

Sources: [FBTAA Division 6](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1) and [s 136(1)](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/2) (compilation 97, read 18 November 2026); [ATO FBT rates and thresholds, Table 11](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds) (read 18 November 2026); [ATO employer guide chapter 10](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00011) (read 18 November 2026). Example 12.

#### Rule 17 -- Board benefits (Division 9)

A board meal needs every one of these, each shown by the employment terms, the arrangement or the premises (s 35; s 136(1) 'board meal', 'meal entitlement day'):

- **Meal entitlement day.** On that day the recipient (the employee or an associate) was entitled, in respect of the employee's employment, to residential accommodation, and was entitled to at least 2 meals either under an industrial instrument in respect of that employment or under an arrangement in respect of that employment that also entitled them to at least 2 meals on each working day of the arrangement period and under which they were ordinarily given at least 2 meals on those days. Accommodation or meals the recipient is entitled to for another reason do not count.
- **In respect of employment.** The meal itself is provided in respect of the employee's employment.
- **Provider.** The employer, or for a company employer a related company.
- **Where it is made and served.** Either cooked or prepared on the employer's eligible premises and provided there, not in a dining facility that is at any time open to the public; or, for an employee whose duties are principally performed in or in connection with the employer's eligible dining facility (or the accommodation, recreation or travel facility it is part of), cooked in that facility's kitchen and provided in it.
- **Not a private kitchen.** The facility where it is prepared is not used wholly or principally to prepare meals solely for the employee or the employee's associates.
- **Not a function.** It is not provided at a party, reception or other social function.

Where any condition is unclear on the evidence, escalate; a meal that fails one may be a property or tax-exempt body entertainment benefit instead (employer guide 13.4).

1. Taxable value of each meal = $2.00 for a recipient who turned 12 before the FBT year began, otherwise $1.00 (s 36), less the recipient's contribution for that meal, never below nil.
2. Otherwise deductible rule (s 37), employee recipients only: reduce by GD - RD, where GD is the s 8-1 ITAA 1997 deduction for spending the value before contribution and RD the deduction for the contribution.

Incidental refreshments supplied with board are exempt, and board benefits are always Type 2 (employer guide 13.2). A combined contribution for board and accommodation may be apportioned on any reasonable basis (employer guide 13.2); an apportionment the agreement does not state goes to the reviewer. Meals on working days to employees of a primary production business at a location not in or adjacent to an eligible urban area are exempt (s 58ZD): send the location question to the reviewer.

Sources: [FBTAA Division 9](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1) and [s 136(1)](https://www.legislation.gov.au/C2004A03280/2026-07-01/text/2) (compilation 97, read 18 November 2026); [ATO employer guide chapter 13](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00014) (read 18 November 2026). Example 14.

### Section 6 -- Tier 2 catalogue

#### T2-1 -- Not-for-profit capping regimes

**Trigger:** rebatable employer / PBI / hospital. **Action:** Refuse per R-AU-FBT-1; specialist review.

#### T2-2 -- Grandfathered PHEV commitments

**Trigger:** PHEV claimed exempt in 2026-27. **Issue:** needs pre-1-April-2025 exempt use AND a binding commitment; refinancing or optional extensions break it. **Action:** obtain the lease/commitment documents; flag for reviewer.

**Note -- announced, not yet law:** the EV exemption itself narrows for arrangements from 1 April 2027 (Rule 5 transition warning); existing leases are grandfathered under the announcement. For any new EV novated lease commencing on or after 1 April 2027, flag commencement timing and verify enactment status before advising.

#### T2-3 -- Car parking valuation

**Trigger:** a Rule 13 value rests on a fee, valuer's report, space or employee count, or register whose representativeness, arm's length basis or validity is in doubt. **Issue:** these conditions decide whether a method, election or reduction has effect (ss 39AB, 39D(3), 39DA(4), 39E(2), 39FA(5), 39FB(6), 39GE, 39GF(3)). **Action:** compute what the evidence supports; flag the doubtful condition and escalate it (R-AU-FBT-3).

#### T2-4 -- Travelling vs living away from home

**Trigger:** extended work travel with allowances. **Issue:** outside the PCG 2021/3 safe harbour (21/90 days) the boundary needs TR 2021/4 analysis; consequences differ sharply (deductible travel allowance vs LAFHA FBT). **Action:** map the pattern of stays; flag for reviewer.

#### T2-5 -- Logbook adequacy

**Trigger:** logbook older than 5 years, non-representative period, missing full-year odometer records, or business % looks aggressive vs role. **Action:** flag; default to statutory formula until resolved.

#### T2-6 -- Directors' debit loans

**Trigger:** loan benefit computed for a shareholder-employee. **Issue:** Division 7A and FBT interact -- a Div 7A complying loan is generally not a fringe benefit; misclassification double-counts. **Action:** route shareholder loans through the Div 7A analysis first; flag for reviewer.

### Section 7 -- Excel working paper template

```
AUSTRALIA FBT -- WORKING PAPER
Employer: [name]
FBT year: 1 April 2026 - 31 March 2027
Prepared: [date]

CAR REGISTER (PER CAR)
  Make/model/rego:                [____]
  Base value (incl GST, less rego/stamp duty): AUD [____]
  Fourth anniversary of first holding before FBT year start (1/3 reduction): [YES/NO]
  Days available for private use: [____]/365
  Method (statutory / operating cost): [____]
  Logbook valid (date started, <5 yrs): [____]  Business %: [____]
  Deemed depreciation (25% DV):   AUD [____]
  Deemed interest (8.27%):        AUD [____]
  Employee contribution:          AUD [____]
  Taxable value:                  AUD [____]
  EV exempt? (BEV/H2, conditions Rule 5): [YES/NO]  Notional TV for RFBA: AUD [____]

ENTERTAINMENT
  Method (actual / 50-50 / register): [____]
  Total meal entertainment:       AUD [____]
  Employee/associate share (actual): AUD [____]
  Minor benefit exclusions (<$300, infrequent -- actual method only): AUD [____]
  Taxable value:                  AUD [____]
  Deduction/GST mirror check (only to extent FBT'd): [____]

OTHER BENEFITS (PER TYPE)
  Expense payments (net of otherwise-deductible + declarations): AUD [____]
  Car parking (method: [____]; benefits [____]):  AUD [____]
  Loans (notional interest at 8.27% on daily balances - interest accrued - ND): AUD [____]
  Debt waivers (amount waived):   AUD [____]
  Property/residual (after s 62 in-house $1,000): AUD [____]
  Housing (statutory annual value x days / days in year - rent): AUD [____]
  LAFHA (allowance - exempt accommodation - exempt food): AUD [____]
  Board ($2 / $1 per meal - contributions): AUD [____]

GROSS-UP AND LIABILITY
  Type 1 taxable values:          AUD [____] x 2.0802 -> nearest dollar [____]
  Type 2 taxable values:          AUD [____] x 1.8868 -> nearest dollar [____]
  Fringe benefits taxable amount: AUD [____] (sum the rounded aggregates)
  FBT @ 47%:                      AUD [____] (retain cents)
  Instalment credit:              AUD [____] (reported/payable, net of variation credits)
  Cash paid / unpaid instalments: AUD [____] / [____] (reconcile separately)

RFBA (PER EMPLOYEE, individual fringe benefits amount > $2,000 -- excl car parking,
non-salary-packaged meal entertainment, pooled cars; INCL exempt EV notional)
  Employee: [____]  TV: AUD [____]  RFBA (x 1.8868): AUD [____]

REVIEWER FLAGS
  [List any Tier 2 flags]
```

### Section 8 -- GL reading guide

1. Sweep the accounts in Section 3.1 for the FULL FBT year (1 Apr - 31 Mar) -- not the income year; a July-June income-year export misses Q1 of the FBT year (April-June 2026, the prior income year's final quarter). Export 1 April to 31 March exactly.
2. Entertainment split first: sustenance out, client share identified, per-head amounts for the minor benefit test.
3. Motor vehicles: match every vehicle carrying costs in the GL to the car register; a car with running costs but no register entry is the classic missed benefit.
4. Separate actual-expense reimbursements from ordinary fixed cash allowances. Reimbursements may be expense payment benefits with supported otherwise-deductible reductions; ordinary allowances are employee assessable income requiring payroll treatment. Classify LAFHA and kilometre-based car reimbursements separately before applying FBT rules.
5. Directors' debit loans: route via Div 7A first (T2-6).


#### Key figures (FBT year ending 31 March 2027)

**Key figures**

| Item | Value |
| --- | --- |
| FBT rate | 47% |
| Type 1 / Type 2 gross-up | 2.0802 / 1.8868 |
| Car statutory rate | 20% |
| Deemed depreciation / deemed interest | 25% DV / 8.27% |
| Car parking threshold | $11.48/day |
| Minor benefit | < $300 + infrequent |
| Record-keeping exemption | $10,962 |
| In-house benefit reduction | $1,000/employee (not salary-packaged) |
| RFBA trigger / factor | > $2,000 taxable value / 1.8868 |
| LAFHA reasonable food (1 adult, Australia) | $353/week (TD 2026/2); statutory food amount $42 adult / $21 child |
| EV home charging shortcut | 5.47 c/km (PCG 2024/2) |
| LCT fuel-efficient threshold (2026-27 sale year) | $91,661 |
| Instalment trigger | Prior-year FBT >= $3,000 |

## Worked cases

### Section 4 -- Worked examples

#### Example 1 -- Car fringe benefit, statutory formula

An ordinary taxable employer first acquires the car on 1 April 2026. Verified statutory-formula inputs are a $40,000 GST-inclusive base value, all 365 days available for private use and a $1,000 after-tax contribution paid directly to the employer for that car. No base-value reduction, exemption, otherwise-deductible reduction or operating-cost election applies. The employer has an established GST credit entitlement on acquisition. This is its only taxable benefit for the year ending 31 March 2027; NFP concessions and the record-keeping exemption do not apply.

```
Taxable value = 20% x $40,000 x (365/365) - $1,000 = $7,000
GST credit entitlement established above -> Type 1 (established, never assumed)
Grossed-up calculation = $7,000 x 2.0802 = $14,561.40
Nearest-dollar Type 1 aggregate = $14,561; Type 2 = $0
Fringe benefits taxable amount = $14,561
FBT = 47% x $14,561 = $6,843.67
```

Employee contribution is assessable income to the employer and has GST consequences. The calculation uses current ATO aggregate rounding; verify the approved 2027 form/software before filing.

```oa-check
name: Car-only employer rounds the aggregate before tax
inputs:
  base_value: 40000
  statutory_percent: 20
  available_days: 365
  year_days: 365
  contribution: 1000
  type1_factor: 2.0802
  fbt_percent: 47
steps:
  taxable_value: max(0, pct(base_value, statutory_percent) * available_days / year_days - contribution)
  unrounded_aggregate: taxable_value * type1_factor
  taxable_amount: round(unrounded_aggregate, 0)
  tax_payable: pct(taxable_amount, fbt_percent)
expected:
  taxable_value: 7000
  unrounded_aggregate: 14561.40
  taxable_amount: 14561
  tax_payable: 6843.67
tolerance: 0
```

#### Example 2 -- Exempt EV that still creates RFBA

Battery electric car, first held and used March 2024, LCT value at first retail sale below the fuel-efficient LCT threshold for that year so LCT was never payable (verified from the sale documents, not a raw price comparison), provided to a current employee through 2026-27.

Car benefit and associated expenses (rego, insurance, servicing, charging): **exempt** -- no FBT. A home charging station is not an associated car expense: providing or reimbursing one may be a property or expense payment fringe benefit. The **notional** taxable value of the car benefit must still be computed, leaving out associated car expense benefits such as rego: if it exceeds $2,000 for the employee, an RFBA is reported through STP (notional TV x 1.8868). Home charging may use the PCG 2024/2 shortcut: 5.47 c/km for the FBT year starting 1 April 2026.

#### Example 3 -- The PHEV trap

Plug-in hybrid delivered under a novated lease commencing 1 June 2025. NOT exempt -- PHEVs ceased qualifying 1 April 2025, and the lease began after that date, so no grandfathering. Full car fringe benefit applies. (Grandfathering needs BOTH pre-1-April-2025 exempt use AND a binding commitment spanning the date; optional lease extensions break it.)

#### Example 4 -- Christmas party under the minor benefits exemption

Off-site Christmas party, $180 per head including partners, once a year. Per-attendee notional taxable value < $300 and the event is infrequent -> minor benefit, exempt (s 58P). Consequence of exemption: the cost is NOT income tax deductible and no GST credits (entertainment is only deductible/creditable to the extent FBT applies).

#### Example 5 -- Meal entertainment, 50/50 election

Total meal entertainment for the year $28,000 across staff and clients, no register kept, employer elects 50/50.

```
Taxable value = 50% x $28,000 = $14,000 (attendee split irrelevant under 50/50)
Only 50% of the spend is income tax deductible (s 51AEA); GST credits follow the same 50%
```

Compare before electing: actual method may beat 50/50 when client (non-employee) share is high; the register method needs a 12-week register. Salary-packaged meal entertainment MUST use the actual method.

#### Example 6 -- Loan benefit

$50,000 interest-free loan to an employee outstanding all year.

```
Notional interest = $50,000 x 8.27% (benchmark, year ending 31 Mar 2027) = $4,135
Interest charged = $0 -> taxable value = $4,135 (Type 2 -> x 1.8868)
```

If the employee would have deducted the interest (e.g. loan used for their income-producing investment), the otherwise-deductible rule can reduce the taxable value -- declaration required.

#### Example 7 -- RFBA exclusions remain in employer aggregates

For an ordinary taxable employer in the year ended 31 March 2026, assume the benefit valuations and GST entitlements have been verified: $7,700 car benefits and $1,100 non-salary-packaged meal entertainment are Type 1; $6,000 school-fee reimbursements and $3,000 remote-area rent reimbursements are Type 2. The meal entertainment and remote-area rent are excluded from employee RFBA reporting, but remain taxable in the employer aggregates. No NFP concession, exemption or earlier-year record-keeping method applies.

This reproduces the [ATO employer guide chapter 2 illustration](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00003): Type 1 $8,800 x 2.0802 = $18,305.76, rounded to $18,306; Type 2 $9,000 x 1.8868 = $16,981.20, rounded to $16,981. The taxable amount is $35,287 and FBT is $16,584.89. Round after aggregation within each class.

```oa-check
name: Taxable RFBA-excluded benefits and nearest-dollar gross-up
inputs:
  car: 7700
  meal_entertainment: 1100
  school_fees: 6000
  remote_rent: 3000
  type1_factor: 2.0802
  type2_factor: 1.8868
  fbt_percent: 47
steps:
  type1_values: car + meal_entertainment
  type2_values: school_fees + remote_rent
  type1_aggregate: round(type1_values * type1_factor, 0)
  type2_aggregate: round(type2_values * type2_factor, 0)
  taxable_amount: type1_aggregate + type2_aggregate
  tax_payable: pct(taxable_amount, fbt_percent)
expected:
  type1_values: 8800
  type2_values: 9000
  type1_aggregate: 18306
  type2_aggregate: 16981
  taxable_amount: 35287
  tax_payable: 16584.89
tolerance: 0
```

#### Example 8 -- Car parking: commercial parking station against average cost

Year ending 31 March 2027. On 1 April 2026, the first business day, the lowest representative all-day fee at the only commercial parking station within 1 km of the employer's car park is $14.00, above the $11.48 threshold, and the other Rule 6 conditions hold for one employee on 230 days. The station charges $14.00 on the first 120 of those days and $15.50 on the last 110. The employee pays $460 for parking in the year. The fee evidence is held for every day and is representative.

```
Commercial parking station method = 120 x $14.00 + 110 x $15.50 - $460 = $2,925.00
Average cost = ($14.00 + $15.50) / 2 = $14.75 a benefit
Average cost method = 230 x $14.75 - $460 = $2,932.50
```

Without an election the default method's $2,925.00 applies; electing average cost would raise the value. Car parking is excluded from the employee's RFBA.

```oa-check
name: Car parking default method against average cost
inputs:
  low_days: 120
  low_fee: 14.00
  high_days: 110
  high_fee: 15.50
  contribution: 460
steps:
  station_method: max(0, low_days * low_fee + high_days * high_fee - contribution)
  average_cost: (low_fee + high_fee) / 2
  average_cost_method: max(0, (low_days + high_days) * average_cost - contribution)
expected:
  station_method: 2925.00
  average_cost: 14.75
  average_cost_method: 2932.50
tolerance: 0
```

#### Example 9 -- Car parking: spaces method

This reproduces the [ATO employer guide's Example 18](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00017) for the year ended 31 March 2023, the inputs being the ATO's. The employer elects the spaces method for all employees. Its 4 spaces each give benefits from 1 October 2022 to 31 March 2023 (182 days); the daily rate amount of each space by the average cost method is $10; the 3 employees each pay $30 a week for 26 weeks; the employee and space numbers are representative.

```
Each space = $10 x 182 / 366 x 228 = $1,133.77
Total statutory benefit = 4 x $1,133.77 = $4,535.08
3 employees for 4 spaces = $4,535.08 x 3 / 4 = $3,401.31
Taxable value = $3,401.31 - $2,340.00 = $1,061.31
```

```oa-check
name: Spaces method with fewer employees than spaces
inputs:
  daily_rate: 10
  availability_days: 182
  statutory_days: 228
  spaces: 4
  average_employees: 3
  average_spaces: 4
  weekly_contribution: 30
  weeks: 26
steps:
  each_space: daily_rate * availability_days / 366 * statutory_days
  total_statutory_benefit: each_space * spaces
  reduced_benefit: total_statutory_benefit * average_employees / average_spaces
  contributions: weekly_contribution * weeks * average_employees
  taxable_value: round(max(0, reduced_benefit - contributions), 2)
expected:
  each_space: 1133.77
  total_statutory_benefit: 4535.08
  reduced_benefit: 3401.31
  contributions: 2340
  taxable_value: 1061.31
```

#### Example 10 -- Loan under the otherwise deductible rule, and a debt waiver

Year ending 31 March 2027. An employee owes $50,000 all year on a loan at 4%, so $2,000 of interest accrues. The employee used 60% of the loan to buy income-producing shares and 40% privately, and gives the approved declaration before the declaration date. The rate was not set by reference to that use. Separately, the employer waives $1,200 the employee owed for a staff purchase and $30 of interest charged on it. This follows the six steps in [employer guide 8.8](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00009) with the 2027 benchmark rate.

```
Notional interest = $50,000 x 8.27% = $4,135.00 (365 daily balances of $50,000 / 365)
Before the rule = $4,135.00 - $2,000.00 = $2,135.00
GD = $4,135.00 x 60% = $2,481.00; RD = $2,000.00 x 60% = $1,200.00; ND = $1,281.00
Loan taxable value = $2,135.00 - $1,281.00 = $854.00 (Type 2)
Debt waiver taxable value = $1,200 + $30 = $1,230 (Type 2)
```

```oa-check
name: Loan otherwise deductible rule and debt waiver
inputs:
  balance: 50000
  days: 365
  benchmark_percent: 8.27
  interest_accrued: 2000
  income_use_percent: 60
  principal_waived: 1200
  interest_waived: 30
steps:
  notional_interest: round(pct(balance * days, benchmark_percent) / days, 2)
  before_rule: max(0, notional_interest - interest_accrued)
  gross_deduction: pct(notional_interest, income_use_percent)
  accrued_deduction: pct(interest_accrued, income_use_percent)
  notional_deduction: gross_deduction - accrued_deduction
  loan_taxable_value: max(0, before_rule - notional_deduction)
  debt_waiver_taxable_value: principal_waived + interest_waived
expected:
  notional_interest: 4135.00
  before_rule: 2135.00
  gross_deduction: 2481.00
  accrued_deduction: 1200.00
  notional_deduction: 1281.00
  loan_taxable_value: 854.00
  debt_waiver_taxable_value: 1230
tolerance: 0
```

#### Example 11 -- In-house property and residual benefits with the $1,000 reduction

Year ending 31 March 2027, no salary packaging. An electronics retailer sells an employee a laptop for private use for $400. It bought the laptop at arm's length for $1,800 and was selling it to the public at the time for $2,400, so the notional value exceeds the cost price. It also gives the employee, free, a one-off home set-up and data transfer service it sells to the public for $300 on the same terms. Separately, under its own contract with a gym, it pays the gym $960 at arm's length for the employee's membership from 1 April 2026 to 31 March 2027. No otherwise deductible reduction applies.

```
Laptop (s 42(1)(b)) = lesser of $1,800 and $2,400, less $400 = $1,400
Set-up service (s 48(a), non-period) = 75% x $300 = $225
In-house total = $1,400 + $225 = $1,625; s 62 reduction $1,000 -> $625
Gym membership (s 51(b), external period benefit within the year, no s 62 reduction) = $960
Taxable value = $625 + $960 = $1,585
```

```oa-check
name: In-house reduction applies only to in-house benefits
inputs:
  laptop_cost: 1800
  laptop_public_price: 2400
  laptop_contribution: 400
  plan_public_price: 300
  in_house_percent: 75
  in_house_cap: 1000
  gym_expenditure: 960
steps:
  laptop_value: max(0, min(laptop_cost, laptop_public_price) - laptop_contribution)
  plan_value: pct(plan_public_price, in_house_percent)
  in_house_total: laptop_value + plan_value
  in_house_reduction: min(in_house_total, in_house_cap)
  in_house_taxable: in_house_total - in_house_reduction
  taxable_value: in_house_taxable + gym_expenditure
expected:
  laptop_value: 1400
  plan_value: 225
  in_house_total: 1625
  in_house_reduction: 1000
  in_house_taxable: 625
  taxable_value: 1585
tolerance: 0
```

#### Example 12 -- Housing benefit indexed from the prior year

Year ending 31 March 2027. The employer leases a house in Victoria that is the employee's usual residence for the whole year. The year ended 31 March 2026 gave the right a statutory annual value of $26,000.00. The year ending 31 March 2027 is not a base year: the employer makes no base-year election, the right gave housing benefits in 2026, the 9-year rule does not apply and there was no material alteration. The employee pays the employer $7,800 rent in the year.

```
Statutory annual value = $26,000.00 x 1.044 (VIC, year ending 31 March 2027) = $27,144.00
Taxable value = $27,144.00 x 365 / 365 - $7,800.00 = $19,344.00
```

```oa-check
name: Housing statutory annual value indexed and rent deducted
inputs:
  prior_statutory_annual_value: 26000.00
  vic_factor_2027: 1.044
  tenancy_days: 365
  year_days: 365
  rent: 7800
steps:
  statutory_annual_value: round(prior_statutory_annual_value * vic_factor_2027, 2)
  taxable_value: max(0, statutory_annual_value * tenancy_days / year_days - rent)
expected:
  statutory_annual_value: 27144.00
  taxable_value: 19344.00
tolerance: 0
```

#### Example 13 -- LAFHA with substantiated food above the reasonable amount

Year ending 31 March 2027. An employee who owns a home in Australia that stays available to them is in the first 12 months at a new location and has given the s 31F declaration. Living alone there, they receive a weekly allowance of $1,100: $600 for accommodation, $400 for total food costs (no normal home food cost deducted) and $100 for the disadvantage of living away. Rent is $560 a week, substantiated. The employee spends $380 a week on food; as that spending exceeds the $353 reasonable amount for one adult (TD 2026/2), all of it must be substantiated, and it is. The allowance is paid for 20 weeks.

```
Exempt accommodation component = lesser of $600 and $560 = $560
Exempt food component = lesser of ($400 - $42) and $380 = $358
Weekly taxable value = $1,100 - $560 - $358 = $182
Taxable value = $182 x 20 = $3,640
```

```oa-check
name: LAFHA exempt components cap at spending and the statutory food amount
inputs:
  allowance: 1100
  accommodation_component: 600
  accommodation_spent: 560
  food_component: 400
  statutory_food: 42
  food_spent: 380
  weeks: 20
steps:
  exempt_accommodation: min(accommodation_component, accommodation_spent)
  exempt_food: max(0, min(food_component - statutory_food, food_spent))
  weekly_taxable: allowance - exempt_accommodation - exempt_food
  taxable_value: weekly_taxable * weeks
expected:
  exempt_accommodation: 560
  exempt_food: 358
  weekly_taxable: 182
  taxable_value: 3640
tolerance: 0
```

#### Example 14 -- Board meals

Year ending 31 March 2027. On 200 meal entitlement days the employer provides board meals, 2 a day, to an employee, the employee's spouse (both adults) and their 8-year-old child. The employee pays $0.50 a meal for each person. No meal is otherwise deductible.

```
Adult meals = 2 x 2 x 200 = 800; each $2.00 - $0.50 = $1.50; 800 x $1.50 = $1,200.00
Child meals = 2 x 200 = 400; each $1.00 - $0.50 = $0.50; 400 x $0.50 = $200.00
Taxable value = $1,200.00 + $200.00 = $1,400.00 (Type 2)
```

```oa-check
name: Board meals at the statutory amounts less contributions
inputs:
  adult_meals: 800
  child_meals: 400
  adult_value: 2.00
  child_value: 1.00
  contribution_per_meal: 0.50
steps:
  adult_taxable: adult_meals * max(0, adult_value - contribution_per_meal)
  child_taxable: child_meals * max(0, child_value - contribution_per_meal)
  taxable_value: adult_taxable + child_taxable
expected:
  adult_taxable: 1200
  child_taxable: 200
  taxable_value: 1400
tolerance: 0
```

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


#### Prohibitions

- NEVER use the Type 1 gross-up without confirmed GST creditability
- NEVER treat a PHEV as exempt for 2026-27 without evidence of a pre-1-April-2025 binding commitment
- NEVER skip RFBA computation for exempt electric cars
- NEVER claim income tax deductions or GST credits on entertainment beyond the extent FBT applies (50% cap under a 50/50 election)
- NEVER accept a logbook older than 5 years or a non-12-week period
- NEVER net an employee contribution against a different benefit
- NEVER compute NFP capping or ESS -- escalate
- NEVER value car parking from an unrepresentative or non-arm's-length fee, a market value without an arm's length valuer's report, or an invalid register -- escalate (R-AU-FBT-3)
- NEVER estimate a notional value or market rent without a documented market comparison -- escalate (R-AU-FBT-5)
- NEVER use the income year (July-June) for FBT -- the FBT year ends 31 March
- NEVER present figures as definitive


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

This guide is maintained in the [ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants). Check its quality tier, recorded review status and cited primary sources for the requested period. The upstream website does not publish or verify this fork's changes.

> Contributed by Ryan Duguid.



## Completion checklist



#### Test suite

**Test 1:** Type 1 aggregate $10,000, Type 2 aggregate $5,000. -> ($10,000 x 2.0802) + ($5,000 x 1.8868) = $30,236.00; FBT = 47% x $30,236.00 = $14,210.92.

**Test 2:** Under all Example 1 assumptions, the only benefit is the car: verified $40,000 base, 365/365 availability and $1,000 contribution. -> TV $7,000, Type 1 nearest-dollar aggregate $14,561 and FBT $6,843.67.

**Test 3:** Same car, fourth anniversary of first holding fell before the start of the FBT year. -> Base value $26,666.67 (one-third reduction); TV = 20% x $26,666.67 - $1,000 = $4,333.33.

**Test 4:** BEV first held 2024, LCT never payable, notional TV $6,500. -> FBT nil; RFBA = $6,500 x 1.8868 = $12,264.20, reported as $12,264 (whole dollars, rounded down); affects income tests only.

**Test 5:** PHEV novated lease started June 2025, claimed exempt. -> NOT exempt (post-1-April-2025 commencement). Full car benefit.

**Test 6:** Staff gift $250 voucher, twice a year. -> Minor benefit candidates: < $300 each and infrequent -> exempt; not deductible if entertainment-type, deductible if property (non-entertainment gift vouchers generally deductible).

**Test 7:** Meal entertainment $28,000, 50/50 elected. -> TV $14,000; deduction and GST credits limited to 50%.

**Test 8:** Interest-free loan $50,000 all year. -> TV = $50,000 x 8.27% = $4,135.

**Test 9:** Employee individual fringe benefits amount exactly $2,000. -> NO RFBA (must exceed $2,000). At $3,000 -> 3,000 x 1.8868 = $5,660.40, reported as $5,660 (whole dollars, rounded down).

**Test 10:** LAFHA one adult, food component $353/week, declaration held, month 8 of 12. -> Food exempt up to $353 less statutory $42; no substantiation needed at or below reasonable amount.

**Test 11:** Lowest all-day fee within 1 km on 1 April 2026 is $11.48 exactly. -> No car parking benefit for the year ending 31 March 2027 (the fee must exceed the threshold).

**Test 12:** Market value method elected, valuer's report received after the declaration date. -> Election of no effect (s 39D(3)); value by the commercial parking station method unless another election holds.

**Test 13:** Example 10's loan without the employee's declaration. -> No otherwise deductible reduction; taxable value $2,135.00.

**Test 14:** Employee's only in-house benefit has a taxable value of $640, not salary packaged. -> s 62 reduces it to nil; salary packaged, it stays $640.

**Test 15:** Housing right in its first year, market rent $5,200 for a 121-day tenancy in the year ending 31 March 2027. -> Statutory annual value $15,685.95; taxable value $5,200.00 before rent ($15,685.95 x 121 / 365).

**Test 16:** Board meal to a child who turned 12 on 15 April 2026. -> $1.00 for the year ending 31 March 2027 (12 not reached before 1 April 2026).

**Test 17:** Meal served to a live-in office employee, whose duties are not performed in or in connection with a dining facility, in the employer's staff canteen, which is also open to the public. -> Not a board meal (s 136(1) 'board meal' (c)(i)); do not use $2 or $1; escalate.

**Test 18:** In-house residual benefit valued from a public price list whose public sales carry a different term (for example a 24-month contract against the employee's month-to-month use). -> No s 48(a) or 49(a) value from that price; escalate (R-AU-FBT-5).

**Test 19:** LAFHA food component paid with no basis for concluding the employee would spend on food, and no food receipts. -> The ATO's deemed-spending practice does not apply; escalate.

**Test 20:** Staff loan from a bank employer at a variable rate that sat below the bank's public rate for 2 months of the FBT year. -> Not exempt under s 17(2) for that year; value under Rule 14.

**Test 21:** Loan balance owed throughout the FBT year ending 31 March 2028 (366 days). -> Day count not settled by the Act; send to the reviewer (Rule 14).

**Test 22:** Spaces election with daily rate amounts by the average cost method, where the lowest fee on the first benefit day was a one-day promotion well below the 4-week average. -> Fee not representative, election of no effect (ss 39AB, 39FA(5)); escalate (R-AU-FBT-3).

## Sources

| Source | URL | Read on |
|---|---|---|
| Current FBT rate, FBT Tax Act s 6 | <https://www.legislation.gov.au/C2004A03281/2018-06-19/text> | 2 November 2026; compilation 9 current metadata and s 6 |
| Employer aggregation, FBTAA ss 5B, 5C and RFBA exclusions in s 5E | <https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1> | 2 November 2026; compilation 97, selected provisions |
| GST-creditable benefits s 149A and instalment credit s 105 | <https://www.legislation.gov.au/C2004A03280/2026-07-01/text/2> | 2 November 2026; compilation 97, selected provisions |
| Employer guide chapter 2, aggregation and nearest-dollar illustration | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00003> | 2 November 2026; selected sections 2.3 to 2.12, current document 22 November 2024 |
| 2026 return instructions, ordinary taxable employers items 14 to 22 | <https://www.ato.gov.au/forms-and-instructions/fringe-benefits-tax-return-2026-instructions/fbt-return-2026-calculation-details-for-taxable-employers> | 2 November 2026; annual assembly and credit sections |
| ATO rates covering years ending 31 March 2026 and 2027 | <https://www.ato.gov.au/forms-and-instructions/fringe-benefits-tax-return-2026-instructions/fbt-rates-and-thresholds-for-2026> | 2 November 2026; Table 1 |
| Approved 2026 FBT return NAT 1067-01.2026 | <https://iorder.com.au/publication/Download.aspx?ProdID=1067-01.2026> | 2 November 2026; page 3 field precision |
| Benefit valuations, FBTAA Divisions 3, 4, 6, 7, 9, 10A, 11 and 12 and s 62 | <https://www.legislation.gov.au/C2004A03280/2026-07-01/text/1> | 18 November 2026; compilation 97, in force from 1 July 2026; the ss 39DA, 39E, 39FA, 39FB and 39GB formulas checked in the compilation's [Volume 1 PDF](https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/pdf/1), pages 103 to 109 |
| Excluded fringe benefits prescribed under FBTAA s 5E(3)(i), FBTA Regulations 2018 ss 6 to 11 | <https://www.ato.gov.au/law/view/fulldocument?filename=REG20181284> | 18 November 2026 |
| Definitions, FBTAA s 136(1) | <https://www.legislation.gov.au/C2004A03280/2026-07-01/text/2> | 18 November 2026; compilation 97 |
| ATO rates: car parking threshold (Table 9), statutory interest rate (Table 10), housing indexation (Table 11), LAFHA food amounts (Table 12) | <https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds> | 18 November 2026; page last updated 20 May 2026 |
| Employer guide chapter 8, loans and debt waivers | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00009> | 18 November 2026 |
| Employer guide chapter 10, housing | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00011> | 18 November 2026 |
| Employer guide chapter 11, LAFHA | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00012> | 18 November 2026 |
| Employer guide chapter 13, board | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00014> | 18 November 2026 |
| Employer guide chapter 16, car parking | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00017> | 18 November 2026 |
| Employer guide chapter 17, property | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00018> | 18 November 2026 |
| Employer guide chapter 18, residual | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00019> | 18 November 2026 |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19860039/41> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=TXR/TR9717/NAT/ATO/00001> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00015> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=PAC/19860039/38> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00016> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/types-of-fringe-benefits/fbt-on-cars-other-vehicles-parking-and-tolls/electric-cars-exemption> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/law/view/document?DocID=AFS%2FEV-FBT%2F00001&PiT=99991231235958> | Not re-read for this format update; see retained provenance |

### Section 10 -- Reference material

#### Primary sources (verified 1 August 2026)

**Primary sources**

| Topic | Source |
| --- | --- |
| Rate, gross-ups, thresholds tables | ato.gov.au -- FBT rates and thresholds (updated 20 May 2026) |
| Lodgment/payment dates | ato.gov.au -- Lodging your FBT return and paying; agent lodgment program May/June 2027 |
| Cars: statutory, operating cost, logbooks | FBT guide for employers Ch 7; ato.gov.au rates page (deemed interest 8.27%) |
| EV exemption, PHEV end, home charging | ato.gov.au -- Electric cars exemption; Electric vehicles and FBT fact sheet (AFS/EV-FBT/00001); PCG 2024/2; LCT thresholds 2026-27 |
| Announced EV wind-back (not yet law) | ato.gov.au new legislation QC 107286 -- Electric car discount (announced 5 May 2026 as part of the 2026-27 Budget; Budget delivered 12 May 2026, budget.gov.au); exposure draft legislation released September 2026, consultation closed 28 September 2026: full exemption to 31 March 2027, then from 1 April 2027 a $75,000 price cap with a 25% concession above it, and a flat 25% concession from 1 April 2029 |
| Car parking | ato.gov.au -- Car parking fringe benefits (threshold $11.48; small business exemption) |
| Minor benefits | s 58P FBTAA; TR 2007/12 |
| Meal entertainment | Division 9A FBTAA; s 51AEA ITAA36; s 41 FBTAA (exempt property benefits on business premises); s 38 FBTAA; TR 97/17; FBT guide for employers chs 14 and 15 |
| Alternative records (from 1 Apr 2024) | ato.gov.au QC 101342 + Commissioner's legislative instruments |
| LAFHA | TD 2026/2 (25 March 2026); TR 2021/4; PCG 2021/3 |
| Record-keeping exemption | ato.gov.au rates page Table 6 |

The 18 November 2026 source check covers the benefit valuations in Rules 11 and 13 to 17, read in FBTAA compilation 97, the ATO rates page and the employer guide chapters listed in Sources. Examples 8 to 14 recompute stated inputs; they do not establish eligibility, elections, representativeness or market values from client evidence.

Not yet confirmed: The 2 November 2026 source check covers ordinary-employer annual aggregation, GST-creditability classification, rounding and instalment credit only. The 2 oa-check cases of Examples 1 and 7 recompute the stated numeric inputs; they do not establish benefit valuations, GST entitlements or legal eligibility from client evidence. A complete page-level source/read-date audit, the approved 2027 form/software and independent qualified legal review remain outstanding. Other retained dates, source claims and qualifications keep their original scope. If taxable values or contributions contain cents, confirm the approved return/software input precision and reconcile the workpaper before filling whole-dollar fields. These cases use whole-dollar inputs and do not settle that policy; return **Needs Input** if it is unconfirmed.

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
