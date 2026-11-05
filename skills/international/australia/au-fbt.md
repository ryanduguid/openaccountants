---
name: au-fbt
description: >
  Use this skill whenever asked about Australian Fringe Benefits Tax -- identifying fringe benefits in a general ledger, car fringe benefits (statutory formula or operating cost), the electric vehicle exemption, meal entertainment, minor benefits, expense payments and the otherwise-deductible rule, LAFHA, loan benefits, employee contributions, reportable fringe benefits amounts (RFBA), FBT gross-up and return preparation. Trigger on phrases like "FBT", "fringe benefits tax", "car fringe benefit", "novated lease FBT", "EV FBT exemption", "entertainment FBT", "minor benefit", "50/50 method", "LAFHA", "living away from home", "gross-up", "Type 1 Type 2", "RFBA", "reportable fringe benefits", or when sweeping a GL for FBT exposure. The FBT year runs 1 April to 31 March. ALWAYS read this skill before touching any FBT work.
version: 1.6
jurisdiction: AU
tax_year: 2026
tax_year_notes: "FBT year ending 31 March 2027 (1 April 2026 - 31 March 2027)"
last_updated: 2026-11-05
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Fringe Benefits Tax (FBT) -- Employer Skill v1.6

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

> Use this skill whenever asked about Australian Fringe Benefits Tax -- identifying fringe benefits in a general ledger, car fringe benefits (statutory formula or operating cost), the electric vehicle exemption, meal entertainment, minor benefits, expense payments and the otherwise-deductible rule, LAFHA, loan benefits, employee contributions, reportable fringe benefits amounts (RFBA), FBT gross-up and return preparation. Trigger on phrases like "FBT", "fringe benefits tax", "car fringe benefit", "novated lease FBT", "EV FBT exemption", "entertainment FBT", "minor benefit", "50/50 method", "LAFHA", "living away from home", "gross-up", "Type 1 Type 2", "RFBA", "reportable fringe benefits", or when sweeping a GL for FBT exposure. The FBT year runs 1 April to 31 March. ALWAYS read this skill before touching any FBT work.

## Ask the client first

### Section 2 -- Required inputs and refusal catalogue

#### Required inputs

**Minimum viable** -- entity type and FBT registration status, GL for the FBT year (1 April - 31 March), motor vehicle list with cost/dates/users, entertainment account detail, any salary packaging arrangements.

**Recommended** -- logbooks and odometer records, employee contribution records, declarations (or alternative records under the 1 April 2024 measures), prior year FBT return and workpapers, lease agreements for novated/associate leases.

**Ideal** -- per-employee benefit register, car parking market surveys, LAFH declarations and expense evidence, loan agreements with rates and balances.

#### Refusal catalogue

**R-AU-FBT-1 -- NFP capping and rebates.** *Trigger:* employer is a PBI, health promotion charity, public/not-for-profit hospital, or rebatable employer. *Message:* "Salary packaging caps ($30,000/$17,000 grossed-up; $15,900/$9,010 in benefit value), meal entertainment card arrangements and the FBT rebate are specialist territory. Out of scope -- escalate."

**R-AU-FBT-2 -- Employee share schemes.** *Trigger:* benefit involves shares/options. *Message:* "ESS interests are generally excluded from FBT and taxed under ESS rules. Out of scope."

**R-AU-FBT-3 -- Car parking commercial valuation.** *Trigger:* car parking benefits arise and a taxable value beyond the threshold test is needed. *Message:* "Commercial parking station rate selection, market valuation, and the statutory spaces method involve valuation judgment. Compute exposure flag only; escalate valuation."

**R-AU-FBT-4 -- Airline transport, board, remote area housing.** *Trigger:* these benefit categories appear. *Message:* "Specialised valuation rules. Out of scope -- escalate."

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

- **Car parking** — A car parking benefit needs, on the same day: parking > 4 hours between 7am-7pm on employer premises at/near the primary place of employment; the employee's car parked and commuting use; AND at least one commercial parking station within 1 km that charged a lowest representative fee for all-day parking above $11.48 on the first business day of the FBT year (1 April 2026 for the 2027 year -- no on-the-day fee test exists). Small business exemption: parking is not at a commercial car park AND (gross total income < $10m OR aggregated turnover < $50m) AND not a government body or listed company. Valuation beyond the threshold check: escalate (R-AU-FBT-3).

#### Rule 7 -- Minor benefits (s 58P)

- **Minor benefits** — Notional taxable value < $300 (not indexed; per benefit, per occasion) AND unreasonable to treat as a fringe benefit having regard to infrequency/irregularity and the other s 58P(1)(f) criteria (TR 2007/12: no fixed number of occasions). Assess all s 58P factors for the actual benefits and associated benefits. Frequency is a screening input, not a quarterly safe harbour; document the conclusion under TR 2007/12. Exempt entertainment gets no deduction and no GST credit.  _(s 58P FBTAA; TR 2007/12)_

#### Rule 8 -- Meal entertainment methods

- **Meal entertainment methods** — 1. **Actual** (default; MANDATORY for salary-packaged meal entertainment): taxable value = amounts for employees/associates; client share not subject to FBT (and not deductible). 2. **50/50 split** (Division 9A election): 50% of ALL meal entertainment is the taxable value, regardless of attendees; only 50% deductible/GST-creditable (s 51AEA). 3. **12-week register**: register percentage applied to the year's spend. The minor benefits exemption is NOT available for meal entertainment once a 50/50 or register election is made -- it applies only under the actual method. Entertainment is income-tax deductible and GST-creditable ONLY to the extent it is a fringe benefit subject to FBT.  _(Division 9A FBTAA; s 51AEA)_

#### Rule 9 -- Employee contributions and RFBA

- **Employee contributions and RFBA** — Contributions: after-tax only, reduce the taxable value of THAT benefit only (no cross-application; not for tax-exempt body entertainment), are assessable income to the employer, and carry GST consequences. RFBA: computed on the employee's INDIVIDUAL fringe benefits amount, which EXCLUDES car parking benefits, meal entertainment not provided under a salary packaging arrangement (50/50 and register amounts are never allocable to employees), pooled/shared cars, and remote-area concessions -- and INCLUDES the notional value of exempt electric car benefits (the exception running the other way). Where that amount exceeds $2,000 for the FBT year, report it x 1.8868 (always the Type 2 factor, in whole dollars) through STP finalisation. RFBA affects the employee's income tests, not their taxable income.

#### Rule 10 -- Otherwise-deductible rule and declarations

- **Otherwise-deductible rule and declarations** — Expense payment/property/residual/loan benefits: taxable value reduced by what the employee could have claimed as a once-only deduction. Requires a declaration in the approved form before the declaration date -- or, from 1 April 2024, adequate alternative records per the Commissioner's legislative instruments (available for 11 record types; logbooks and odometer records still need the approved form). Portable electronic devices (s 58X): exempt if primarily for work; one substantially-identical item per year unless a replacement, or the employer's aggregated turnover is under $50 million. **Transition warning:** from 1 April 2027, Act No 49 of 2026 (Sch 4 Pt 2) removes the one-per-year limit and the turnover carve-out, denies s 58X entirely for items provided under a salary packaging arrangement, and (new s 24(1A)) blocks the otherwise-deductible rule for salary-packaged expense payments of standard-deduction work expenses -- flag any packaging arrangement extending past 31 March 2027.  _(s 58X FBTAA; Act No 49 of 2026 (Sch 4 Pt 2); new s 24(1A))_

#### Rule 11 -- LAFHA (standard cases only)

Concessional LAFHA treatment: employee maintains an Australian home they're living away from, first 12 months at a location (FIFO/DIDO excepted from both), declaration held. Exempt food component limited to the reasonable amounts in TD 2026/2 (year ending 31 March 2027: $353/week one adult within Australia; $530 two adults; statutory food amount $42/week adult, $21/week child under 12 deducted first). Within reasonable amounts -> no substantiation of food; above -> full substantiation.

Travelling-vs-LAFH boundary: MT 2030's 21-day rule is WITHDRAWN; TR 2021/4 governs. The PCG 2021/3 compliance approach permits no more than 21 continuous calendar days per stay and no more than 90 calendar days in total at the same work location in the FBT year. Count departure days as directed in paragraph 13. The employee must be away from their normal residence for work, outside FIFO/DIDO arrangements, and return when practicable. Paragraph 12 also requires the employer's qualifying allowance or expense payment, no salary packaging or additional-remuneration option, appropriate reporting and withholding, and substantiating records. Six qualifying 15-day stays meet the numerical limits. Failing the guideline alone does not establish LAFHA treatment; apply TR 2021/4 to the facts.

#### Rule 12 -- Record-keeping exemption and loan benchmark

- **Record-keeping exemption and loan benchmark** — Record-keeping exemption (Pt XIA): an employer with a base year (return lodged, full records kept) whose aggregate fringe benefits amount was <= $10,962 may stop keeping records and pay FBT on the base-year amount -- unless the current year's aggregate exceeds the base-year amount by more than 20%, in which case current-year liability applies and records are needed. In-house benefits (s 62): aggregate taxable value reduced by $1,000 per employee per year; not available for salary-packaged benefits. Loan benefits: taxable value = benchmark rate (8.27%) minus rate actually charged, on the outstanding balance. The benchmark and car-parking figures now publish ONLY on the ATO rates page -- TDs are issued only for cents-per-km and LAFHA food amounts.  _(Pt XIA FBTAA; s 62 FBTAA)_

### Section 6 -- Tier 2 catalogue

#### T2-1 -- Not-for-profit capping regimes

**Trigger:** rebatable employer / PBI / hospital. **Action:** Refuse per R-AU-FBT-1; specialist review.

#### T2-2 -- Grandfathered PHEV commitments

**Trigger:** PHEV claimed exempt in 2026-27. **Issue:** needs pre-1-April-2025 exempt use AND a binding commitment; refinancing or optional extensions break it. **Action:** obtain the lease/commitment documents; flag for reviewer.

**Note -- announced, not yet law:** the EV exemption itself narrows for arrangements from 1 April 2027 (Rule 5 transition warning); existing leases are grandfathered under the announcement. For any new EV novated lease commencing on or after 1 April 2027, flag commencement timing and verify enactment status before advising.

#### T2-3 -- Car parking valuation

**Trigger:** threshold conditions met. **Issue:** lowest-fee selection, market valuation, statutory spaces vs actual usage methods. **Action:** flag exposure; escalate valuation choice.

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
  Loans (benchmark 8.27% - rate charged):  AUD [____]
  Property/residual:              AUD [____]
  LAFHA (excess over TD 2026/2 reasonable + statutory food): AUD [____]

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

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


#### Prohibitions

- NEVER use the Type 1 gross-up without confirmed GST creditability
- NEVER treat a PHEV as exempt for 2026-27 without evidence of a pre-1-April-2025 binding commitment
- NEVER skip RFBA computation for exempt electric cars
- NEVER claim income tax deductions or GST credits on entertainment beyond the extent FBT applies (50% cap under a 50/50 election)
- NEVER accept a logbook older than 5 years or a non-12-week period
- NEVER net an employee contribution against a different benefit
- NEVER compute NFP capping, ESS, or car parking valuations -- escalate
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

Not yet confirmed: This source check covers ordinary-employer annual aggregation, GST-creditability classification, rounding and instalment credit only. The 2 oa-check cases recompute the stated numeric inputs; they do not establish benefit valuations, GST entitlements or legal eligibility from client evidence. A complete page-level source/read-date audit, the approved 2027 form/software and independent qualified legal review remain outstanding. Other retained dates, source claims and qualifications keep their original scope. If taxable values or contributions contain cents, confirm the approved return/software input precision and reconcile the workpaper before filling whole-dollar fields. These cases use whole-dollar inputs and do not settle that policy; return **Needs Input** if it is unconfirmed.

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
