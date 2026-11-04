---
name: au-payroll-tax
description: >
  Use this skill for any Australian state or territory payroll tax question in
  New South Wales, Victoria, Queensland, Western Australia, South Australia,
  Tasmania, the ACT or the Northern Territory: registration thresholds, rates,
  deductions and phase-outs, grouping, contractor and employment agency
  provisions, nexus rules for interstate and overseas workers, taxable wages,
  exempt allowances, surcharges and levies, and monthly and annual return due
  dates. Trigger on "payroll tax", "payroll tax threshold", "payroll tax rate",
  "designated group employer", "relevant contract", "payroll tax grouping",
  "mental health levy", "payroll tax nexus", "annual reconciliation". Covers the
  2026-27 financial year for employers, payroll staff and advisers.
version: 1.3
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-04
depends_on:
  - australia-payroll
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Payroll Tax v1.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Apply the payroll tax rules for the 2026-27 financial year, 1 July 2026 to 30 June 2027, to employers with wages connected to any Australian state or territory. This guide covers remuneration classification, monthly nexus, grouping, contractor and agency rules, deductions, rates, regional concessions, levies and lodgement/payment controls. Federal PAYG withholding and superannuation are separate obligations; use the linked Australian payroll and termination-payment guides for their own figures.

**Built from the law, Tier 2.** This is a source-cited working paper awaiting qualified Australian review. The examples use synthetic facts. A local exemption, group exclusion or regional status must be established before its arithmetic is used.

## Ask the client first

1. Which legal employer/ABN, return period and states or territories are involved, and when did Australian employment begin, cease or change?
2. What are each employer's monthly and annual Australian/local wage components, fringe benefits, super, termination payments, contractors and agency arrangements?
3. Which related entities, common employees, ownership/control interests or existing grouping/exclusion decisions affect the group and its DGE or single lodger?
4. Where did each worker perform services each month, reside, receive wages and work overseas, including assignment dates and breaks?
5. What records establish an exemption, relevant-contract exclusion or regional concession, including the applicable wage proportions and geography?
6. Which registrations, return cycles, prior returns/payments, portal access and outstanding notices exist, and which facts or source conditions need review before submission?

## The method, step by step

### Section 1 - Quick Reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia, all 8 states and territories |
| Financial year covered | 2026-27 (1 July 2026 to 30 June 2027) |
| What is taxed | Taxable wages paid by an employer or group above the jurisdiction's threshold, self-assessed |
| Who administers it | Each state and territory revenue office; the ATO has no role |
| Harmonised areas | Many wage, allowance, FBT, nexus and grouping provisions are harmonised; local Acts, exemptions, registration triggers, rates and filing procedures still control |
| Registration trigger | Test local wages plus Australian/group wages and the local registration rule; Queensland also uses a $25,000 weekly trigger. See Filing and payment |
| Monthly return | Usually the 7th, subject to local business-day/December rules; NT usually 21 days. June treatment and WA reconciliation differ: see Filing and payment |
| Annual return | Usually 21 July; ACT, NSW and SA 28 July. WA June/EOYL information is due 21 July, with later assessed reconciliation adjustments |
| Annual thresholds 2026-27 | $1.0m in VIC and WA, $1.2m NSW, $1.25m TAS, $1.3m QLD, $1.5m SA, $1.75m ACT, $2.5m NT |
| Records | Retain supporting records for at least 5 years; NSW permits English or a form easily translated into English. Check any longer local/notice requirement |
| Reviewed by | Pending. Australian CPA or CA review required |

### Section 2 - The calculation workflow

**Step 1. Identify taxable wages.**
Wages is defined broadly: salary, allowances, bonuses, commissions, director's fees,
superannuation contributions, the grossed-up value of fringe benefits, employment termination
payments, shares and options, payments to contractors under relevant contracts and payments by
employment agents to on-hired workers. See Section 4.

**Step 2. Assign each employee's wages to a jurisdiction.**
Apply the nexus rules month by month. See Section 6.

**Step 3. Test grouping.**
Related corporations, common control, shared employees and traced interests form a group that
shares one threshold and is jointly and severally liable. See Section 7.

**Step 4. Work out the threshold or deduction.**
Use the jurisdiction's formula and the correct Australian employment period and interstate share. SA's deduction base is $600,000, distinct from its $1.5m zero-rate threshold. NT, QLD, VIC and WA taper rules cannot be replaced by a simple local-wages threshold.

**Step 5. Apply the rate and each levy or surcharge separately.**
Determine the relevant employer/group wage base and period. ACT tiers, NT's relevant-period $100m test, QLD rates/levy and Victorian surcharges have different conditions. QLD's regional-discount cap concerns the employer's Queensland taxable wages under s 10A, despite the authority page's conflicting Australian-wage label.

**Step 6. Register, lodge and pay.**
Use each applicable registration trigger and approved return cycle. Reconcile component wages, group/interstate amounts and paid tax before lodgement. Obtain lodgement confirmation, separately authorise payment and retain its reference and settlement evidence. A saved draft or payment reference alone does not prove lodgement or payment.

### Section 3 - Rates and thresholds for 2026-27

**Rates and thresholds by jurisdiction, 2026-27**

The annual amounts below assume a full year and a threshold-claiming employer unless stated. Monthly thresholds, part-year adjustments and group allocations require the local calculation.

| Jurisdiction | Annual threshold/base | Rate and conditions | Deduction/levy conditions | Official source, read 4 November 2026 |
| --- | --- | --- | --- | --- |
| ACT | $1,750,000; published monthly $145,833.33 | Australian/group wages: 6.75% up to $20m; 6.85% over $20m to $50m; 7.35% over $50m to $100m; 7.85% over $100m to $150m; 8.75% over $150m | Days and ACT/Australian share reduce threshold; non-DGE gets none. Eligible university cap requires separately confirmed eligibility | [ACT Revenue, rate bands](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/about-payroll-tax), [calculation](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/calculating-payroll-tax) |
| NSW | $1,200,000 | 5.45% | Australian employment days and NSW/Australian wage share reduce threshold; one group threshold | [Payroll Tax Act 2007, Sch 1 cl 1 R(g), TA(f)](https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021#sch.1), [Revenue NSW thresholds](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/thresholds-and-rates) |
| NT | $2,500,000; published monthly $208,333 | 5.5%; 6.5% if relevant employer/group Australian wages are $100m or more from 1 July 2026 | Deduction loses $1 per $2 above adjusted threshold, floored at zero; full-year exhaustion $7.5m. Relevant s 84 periods are separate and $100m is not prorated | [Payroll Tax Act 2009, s 7A, Sch 1 cls 1, 3-5, 7-9](https://legislation.nt.gov.au/api/sitecore/Act/PDF?id=12078), [current changes](https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-changes-from-1-july-2026) |
| QLD | $1,300,000; published monthly $108,333 | 4.75% at Australian/group wages up to $6.5m; 4.95% above. Qualifying regional employer discount is 1 percentage point through 30 June 2030 | Deduction loses $1 per $7 above $1.3m, nil at $10.4m, with period/interstate/group adjustments. Levy is 0.25% above adjusted $10m plus 0.5% above adjusted $100m, not on all local wages | [Payroll Tax Act 1971 ss 10, 10A, 29, 33, 43C-43J](https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1971-037), [QRO rates](https://qro.qld.gov.au/payroll-tax/calculate/rates-thresholds/), [levy](https://qro.qld.gov.au/payroll-tax/mental-health-levy/calculating/) |
| SA | $1,500,000 zero-rate/registration threshold; maximum deduction base $600,000 | Variable 0% to 4.95% where annual Australian/group wages exceed $1.5m but not $1.7m; 4.95% above $1.7m | Select rate before deduction; annualise part-year Australian wages for rate, then adjust $600,000 deduction for days/local share/group allocation | [RevenueSA rates](https://www.revenuesa.sa.gov.au/payrolltax/rates-and-thresholds), [calculation](https://www.revenuesa.sa.gov.au/payrolltax/how-is-payroll-tax-calculated) |
| TAS | $1,250,000 lower and $2,000,000 upper threshold | 4% on the adjusted middle band; 6.1% above adjusted upper threshold | Adjust both thresholds for period/interstate wages; round monthly thresholds to nearest whole dollar. Non-threshold-claiming group members pay 6.1% on all taxable TAS wages | [SRO Tasmania rates and calculation panels](https://www.sro.tas.gov.au/payroll-tax/rates-thresholds) |
| VIC | $1,000,000; published monthly $83,333 | 4.85%; 1.2125% only for qualifying regional employer | Threshold tapers at 50 cents per dollar above adjusted $3m, nil at $5m full-year Australian wages; period/interstate share applies. Combined surcharges are 1% above adjusted $10m plus a further 1% above adjusted $100m. Only COVID component expires 30 June 2033 | [SRO rates](https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/payroll-tax-current-rates), [phase-out](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/threshold-and-phase-out-rate), [surcharges](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/payroll-tax-surcharges) |
| WA | $1,000,000; published monthly $83,333 | 5.5% | Deduction loses $2 per $13 above $1m Australian/group wages, nil at $7.5m; period/interstate/group adjustments apply | [RevenueWA calculation guide](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide) |

- **Source hierarchy.** The local Act and current revenue-office page control. The Payroll Tax Australia rates page is a jurisdiction-link index, not a substitute for reading the current linked rates, conditions and calculation. Its original claimed update date is not a new read receipt.
- **ACT tiers from 1 July 2026.** Use the group Australian-wage tier and the applicable ACT threshold apportionment. The published university maximum of 6.85% is retained as an unresolved eligibility item in Sources; do not apply it merely because an employer calls itself a university. [ACT calculation](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/calculating-payroll-tax).
- **Northern Territory**; The threshold rose to $2.5m from 1 July 2025, and from 1 July 2026 a 6.5% rate applies to employers and group members with Australia-wide wages of $100m or more.  _(Territory Revenue Office, Payroll tax rates and thresholds; https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-tax-rates-and-thresholds)_
- **Northern Territory deduction.** For an ungrouped employer, ETA = $2,500,000 × Australian employment days / financial-year days; A = NT taxable wages plus interstate wages. If A does not exceed ETA, no tax is payable. Otherwise AD = max(0, ETA − (A − ETA) / 2), and local deduction = AD × NT wages / A. Tax is max(0, NT wages − local deduction) × the applicable rate. The zero floor prevents negative deductions above $7.5m full-year wages. At $4m of full-year NT-only wages, deduction is $1.75m and tax is $123,750. Groups use GTA/group wages under Sch 1 cls 7-9, with the DGE rules, not a separate threshold for every member. Read the relevant-period rules when joining/leaving a group or ceasing Australian employment; $100m for the higher rate is not prorated. [NT Act s 7A, s 84, Sch 1](https://legislation.nt.gov.au/api/sitecore/Act/PDF?id=12078), [unchanged deduction/current changes](https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-changes-from-1-july-2026).
- **Queensland deduction and levy.** A full-year deduction starts at $1.3m, loses $1 for every $7 of Australian wages above it and reaches zero at $10.4m; apportion for period and Queensland share. Only the DGE claims the group deduction, with excess allocated to members where applicable. Separately compute the levy on Queensland wages above each adjusted threshold. For a full-year ungrouped employer, those thresholds are $10m and $100m multiplied by Queensland/Australian taxable wages. QRO Online applies combined period/group/interstate adjustments. QLD-only $11m produces $2,500 primary levy, not $27,500. [Deductions, including Act ss 17, 23, 29, 33, 37, 41](https://qro.qld.gov.au/payroll-tax/calculate/deductions/), [levy calculation](https://qro.qld.gov.au/payroll-tax/mental-health-levy/calculating/).
- **Victorian phase-out**; An employer with Australian wages between $3m and $5m loses 50 cents of threshold for every dollar of wages above $3m (after apportionment), so a metropolitan employer paying $4.2m only in Victoria for a full year gets $400,000. Above $5m there is no threshold.  _(SRO Victoria, Threshold and phase-out rate; https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/threshold-and-phase-out-rate)_
- **Victorian surcharges.** Each surcharge has a primary 0.5% above the adjusted $10m threshold and an additional 0.5% above adjusted $100m. Together this is 1% of excess over adjusted $10m plus 1% of excess over adjusted $100m; the total marginal surcharge above $100m is 2%. Adjust for relevant days, interstate share and grouping. The mental health surcharge is ongoing; only COVID debt surcharge ends 30 June 2033. Exempt wages remain exempt from surcharges. [SRO surcharge conditions](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/payroll-tax-surcharges).
- **Western Australia.** For a full-year WA-only ungrouped employer above $1m, deduction = max(0, $1m − (Australian wages − $1m) × 2 / 13). At $1.2m, the exact deduction is $969,230.7692…, displayed as $969,231. At $7.5m or more there is no deduction. Use the local/group/interstate/part-year calculation for other facts. [RevenueWA calculation](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide).
- **South Australia.** Determine the rate using Australian/group wages before subtracting the deduction; annualise those wages for a part-year employer. The deductible base is $600,000, reduced for employment days and SA/Australian share, and allocated under group rules. RevenueSA Online reconciles estimated rates and deductions against actual annual facts. The published 2026-27 allowance caps are 88c per qualifying business kilometre and $328.85 per qualifying night; apply the allowance conditions below. [Rates](https://www.revenuesa.sa.gov.au/payrolltax/rates-and-thresholds), [calculation](https://www.revenuesa.sa.gov.au/payrolltax/how-is-payroll-tax-calculated).
- **Tasmania and NSW.** Tasmania adjusts both marginal thresholds and rounds monthly thresholds to whole dollars; its currently linked annual guideline is for 2025-26 and is used only for structural mechanics. NSW publishes 2026-27 monthly thresholds of $92,055, $98,630 and $101,918 for 28-, 30- and 31-day months. [TAS current rates](https://www.sro.tas.gov.au/payroll-tax/rates-thresholds), [NSW current rates](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/thresholds-and-rates).



**Regional eligibility is a classification decision.** QLD requires the employer's principal place of employment in regional Queensland and at least 85% of its Queensland taxable wages paid to employees whose principal residence is in the defined regional areas. Temporary accommodation alone is not a principal residence. Under Act s 10A(4)-(5), the discount is unavailable when that employer's Queensland taxable wages exceed $350m for an annual period or $29,166,666 for a monthly period. The QRO page describes this cap as Australian wages; follow the Act and resolve any portal discrepancy before lodging. The discount reduces 4.75% to 3.75% or 4.95% to 3.95%, and does not remove the levy. [Act s 10A](https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1971-037#sec.10A), [QRO regional criteria](https://qro.qld.gov.au/payroll-tax/calculate/regional-discount/).

VIC requires at least 85% of Victorian taxable wages to regional employees: each does more than half their Victorian work in regional Victoria. Test monthly for monthly returns and across the full year for annual reconciliation; businesses in a group are individually assessed. A qualifying group member does not make every other member regional. [Regional criteria and defined councils](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/industries-and-locations/regional-employers).

**SA variable annual rate.** For annualised Australian relevant wages TARW above $1.5m and up to $1.7m, R = ((TARW − $1.5m) / $200,000) × 4.95%. Above $1.7m use 4.95%; up to $1.5m the rate is nil. TARW = (local + interstate relevant wages) × financial-year days / relevant Australian employment days, substituting group totals where required. Subtract the separate adjusted $600,000 deduction when computing the taxable base, not when selecting R. [Payroll Tax Act 2009 (SA), Sch 1 cl 1, cl 5(2)-(3), cl 9(4)-(5), compilation 31 March 2026](https://www.legislation.sa.gov.au/_legislation-documents/lz/c/a/payroll-tax-act-2009/current/2009.22.auth.pdf). Monthly estimates are reconciled by RevenueSA Online; do not transplant the annual formula without the period rules.

### Section 4 - Taxable wages, exemptions and allowances

- **Definition of wages**; The harmonised definition is not limited to salary. It covers remuneration, allowances, bonuses, commissions, director's fees, superannuation contributions, fringe benefits, shares and options, employment termination payments and deemed wages under the contractor and employment agency provisions.  _(Payroll Tax Australia, Definitions: wages; https://www.payrolltax.gov.au/definitions-acronyms-list/w)_
- **Termination payments**; An employment termination payment within s 82-130 ITAA 1997 that would be included in the employee's assessable income is wages, as is a payment that would be an ETP but for being made more than 12 months after termination. The tax-free ETP component and tax-free genuine redundancy/early-retirement amount are not liable under the confirmed NSW treatment; unused annual/long-service leave and taxable termination components remain liable. A federal ETP exclusion does not itself establish payroll-tax exemption. See `au-employment-termination-payments.md`. [NSW Act ss 27-28](https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021#sec.27), [NSW termination classifications](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/termination-payments).  _(Payroll Tax Australia, Definitions: employment termination payment; https://www.payrolltax.gov.au/employment-termination-payment)_
- **Exempt allowances.** The verified 2026-27 NSW/QLD/SA caps are 88c per substantiated business kilometre and $328.85 per qualifying overnight absence. A cap does not exempt a fixed allowance without the required records or qualifying travel. NSW accommodation must be temporary; absences over 21 days require the maintained domestic-dwelling condition, and sleepover allowances remain taxable. Meals/incidentals-only and truck-driver amounts have separate rules; QLD publishes $170.85 for meals/incidentals-only. The motor-vehicle basis uses the preceding income-year ATO rate, accommodation the relevant current-year amount. Do not substitute the current income-tax car rate. Deduct only the qualifying exempt component and include excess in wages. Check other jurisdictions' local rulings before claiming. [NSW motor vehicle](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/allowances/motor-vehicle), [NSW accommodation](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/allowances/accommodation), [QRO allowance conditions](https://qro.qld.gov.au/payroll-tax/exemptions/allowances/), [SA rates](https://www.revenuesa.sa.gov.au/payrolltax/rates-and-thresholds).
- **Fringe benefits.** NSW includes taxable FBT values, excludes FBT-exempt/nil values and uses (Type 1 aggregate + Type 2 aggregate) × Type 2 gross-up, 1.8868 through 30 June 2027. Tax-exempt bodies exclude their entertainment fringe benefits from that calculation. The prior-FBT-year alternative method requires benefits paid for at least 15 months before the financial year starts; otherwise use actual monthly values. Under the alternative method monthly July-May uses the preceding FBT return divided by 12 and annual reconciliation uses the return immediately preceding year-end. In NSW declare the local amount in 'Fringe benefits' and other-jurisdiction amounts in 'Gross interstate wages'. Other offices' methods and elections must be checked locally. [NSW FBT calculation and methods](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/fringe-benefits).
- **Common exemptions**; Each Act exempts particular wages, for example wages paid during maternity, paternity or adoption leave, workers compensation payments, and wages paid by certain charities for exempt work; some jurisdictions also exempt apprentices and trainees. The lists differ, so confirm each exemption on the relevant office's site before claiming it.  _(Payroll Tax Australia, Revenue rulings table; https://www.payrolltax.gov.au/revenue-rulings-table)_
- **Audit findings**; The revenue offices report the same errors year after year: omitted director's fees, super and fringe benefits; undeclared employee share scheme benefits; wrongly claimed exemptions; wages declared in the wrong jurisdiction; employees classified as contractors; and wrong grouping status.  _(Payroll Tax Australia, Lodging; https://www.payrolltax.gov.au/lodging)_

### Section 5 - Thresholds, deductions and apportionment

- **Part-year employment.** Use the local statutory employment-day definition and days in that financial year; do not simply count days paying local wages whilst Australian employment continues interstate. Revenue NSW’s historical 2025-26 illustration for 184 days gives $1.2m × 184/365 = $604,931.51. SA separately annualises wages for the rate and adjusts the $600,000 deduction. [NSW thresholds](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/thresholds-and-rates), [SA calculation](https://www.revenuesa.sa.gov.au/payrolltax/how-is-payroll-tax-calculated).
- **Interstate wages**; Multiply the threshold by the jurisdiction's wages divided by total Australian wages. NSW wages of $900,000 out of $3,000,000 Australian wages give a NSW threshold of $360,000. Interstate wages must be declared in every return even where they fall below the other jurisdiction's threshold.  _(Revenue NSW, Interstate wages; https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages)_
- **Both adjustments.** Victoria's source example for 335/365 days and $1.5m Victorian/$3.5m Australian wages uses historical 2024-25 settings: $900,000 threshold and 45% phase-out, giving its published $210,030 after rounded intermediate amounts. At current $1m and 50%, exact intermediates are $393,346.3796… and $1,180,039.1389…; exact deduction is $233,365.9491…, displayed $233,366. The former shorthand $393,346 − (($1,500,000 − $1,180,039) × 50%) rounds intermediate figures and should not be mistaken for exact arithmetic. Apply the office/return rounding rules when lodging. [SRO phase-out steps and historical examples](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/threshold-and-phase-out-rate).
- **Groups**; One threshold per group, claimed by the designated group employer. Other members pay the flat rate on all their wages. In some jurisdictions an unused deduction can be allocated to another member at the annual return.  _(Payroll Tax Australia, Lodging; https://www.payrolltax.gov.au/lodging)_
- **Registration in several jurisdictions**; Liability is tested on Australia-wide wages, so an employer whose total wages exceed a state's threshold must register there even if the wages paid in that state alone are below it.  _(Payroll Tax Australia, Registration; https://www.payrolltax.gov.au/registration)_

### Section 6 - Nexus: which jurisdiction taxes the wages

- **Services wholly in one jurisdiction**; Where an employee's services in a calendar month are performed wholly in one state or territory, the wages for that month are taxable there, even if the employee normally works elsewhere.  _(Revenue NSW, Nexus provisions; https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions)_
- **Services in more than one place.** For services in multiple jurisdictions and/or partly overseas in a month, use the ordered test: (1) employee's Australian principal place of residence (last-day residence if more than one); (2) only if no Australian residence, employer's Australian ABN address or principal place of business if no single ABN address; (3) only if neither applies, Australian payment location, aggregating split Australian payments in the jurisdiction with the largest portion; (4) only if there is no Australian payment location, where more than half the actual services were performed. A deemed corporate employee uses ABN address/PPB and last-day fallback. Do not skip an earlier satisfied tier. [NSW Act ss 11-11C and nexus guide](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions).
- **Working overseas.** For services wholly overseas up to 6 continuous months, NSW taxes wages paid/payable there; if payments are split with overseas, declare the NSW part, and if paid in multiple Australian jurisdictions aggregate the Australian wages where the largest portion is paid. Once wholly overseas service exceeds 6 continuous months, the NSW-paid wages are exempt including the first 6 months, even across financial years. A holiday or return for less than one month exclusively for that assignment does not break continuity; other returns do. Services offshore outside any state/territory but not overseas do not receive that 6-month exemption: NSW-paid wages remain taxable regardless of duration, with the largest-Australian-payment rule for split payments. Verify another state's local implementation before allocating its wages. [NSW nexus situations 3 and offshore](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions).
- **Harmonised ruling**; Revenue Ruling PTA 039 sets out the nexus rules and their deeming provisions, and each office publishes its own copy.  _(Payroll Tax Australia, Revenue rulings table; https://www.payrolltax.gov.au/revenue-rulings-table)_

### Section 7 - Grouping

- **How a group forms.** NSW Part 5 gateways include related corporations under Corporations Act s 50, common employees, common control, tracing of interests, subsuming smaller groups and the illegal-phoenix provisions. A common director or shareholder alone is not an automatic conclusion: test actual control/influence and the statutory interest threshold, whilst also testing every other gateway. Grouping can cross states and industries. [NSW grouping](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping), [CPN 009 control tests](https://www.revenue.nsw.gov.au/help-centre/resources-library/cpn/cpn009), [Act Part 5](https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021).
- **Consequences**; The gross wages of every member are added together, a single threshold applies to the group, the threshold is apportioned by the group's share of wages in the jurisdiction, and every member is liable for any unpaid payroll tax of any other member. Group Australia-wide wages also set the rate tier and levy position in the ACT, NT, QLD and VIC.  _(Revenue NSW, What is payroll tax grouping; https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping)_
- **Claiming the threshold**; In NSW the group claims through a designated group employer (which must itself exceed the monthly threshold) or a group single lodger (mandatory where no member exceeds it on its own). Lodging one way or the other does not change the group's total liability. The DGE does not need to be the same entity in every jurisdiction.  _(Revenue NSW, What is payroll tax grouping; https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping)_
- **Exclusion.** NSW requires a written Chief Commissioner determination under s 79; the applicant must establish that its business is independent of and not connected with every other group member, considering ownership/control, business nature and other relevant matters. Related corporations cannot be excluded and s 79(8) also excludes groups subject to the illegal-phoenix s 74A. Smaller-group cases have their own analysis. An application or private opinion does not itself remove grouping. [Act s 79](https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021#sec.79), [PTA 031v2](https://www.revenue.nsw.gov.au/about/legislation-and-rulings/revenue-rulings/rulings/payroll/commissioners-discretion-to-exclude-from-a-group).
- **Registration failures.** Reconcile every related entity and all potential gateways against the registrations; common shareholders/directors are enquiry indicators, not a substitute for the actual grouping test. Non-lodging NSW group members still register when they employ in NSW; the GSL includes their wages. [NSW grouping and registration](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping).

### Section 8 - Contractors and employment agents

- **Employee first.** Test the legal rights and obligations in the contractual relationship; an ABN, company or contractor label does not settle classification. Employee wages remain subject to ordinary wage/employer exemptions and threshold rules. Contractor exclusions do not apply to common law employee wages. [NSW Act ss 7, 10 and contractor guidance](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors).
- **Relevant contracts**; A relevant contract is one under which a person in the course of business supplies or receives services for the performance of work, or gives out goods for work to be done on them and re-supplied. The contractor is deemed the employee and the payer the employer, and the labour component of the payments is wages unless an exemption applies. Western Australia has no relevant contract provisions and relies on the employee tests.  _(Payroll Tax Australia, relevant contract; https://www.payrolltax.gov.au/relevant-contract)_
- **The 7 NSW relevant-contract exclusions.** Test the qualifying contract in the relevant financial year, not permanent contractor status: (1) services ancillary to goods; (2) services not ordinarily required by the business **and** ordinarily supplied by that contractor to the public generally; (3) services of that kind ordinarily required for **less than 180 days** in the year across employees/contractors, counting partial days once; (4) services by that person for **90 days or less**, aggregated across relevant contracts/arrangements; (5) services ordinarily supplied to the public generally in that year, to the Commissioner's satisfaction; (6) significant directly related work by the requisite 2 people, including an individual contractor plus one engaged worker, a partner plus one engaged worker or 2 workers engaged by a company; (7) services solely for or ancillary to conveying goods in the conveying person's vehicle, not installation/repair as the main purpose. All are subject to s 32(2A). Section 32(2B) also prevents the s 32(2)(a)-(d) exclusions where the contract supplies additional services/work of a kind outside the relevant paragraph. Test the whole contract and mixed services, not an isolated exempt component. Keep contract/year-specific proof. [Act s 32](https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021#sec.32), [CPN 007](https://www.revenue.nsw.gov.au/help-centre/resources-library/cpn/cpn007), [PTA 020](https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta020), [PTA 006](https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta006).

  **Conflicting summaries.** The overview says '180 days or less'; the Act and PTA 020 require **less than 180**. For public services, current PTA 021v2 supersedes CPN 007's older monthly shorthand: its accepted method uses an **average of 10 days or less per month**, excluding months with no service to that principal, plus same-kind services to an unrelated other principal. Failing that method does not automatically fail the statutory exclusion; seek determination. Merely advertising or having another customer does not establish it. [PTA 021v2](https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta021v2).
- **Non-labour deductions.** Exclude the GST component under the applicable rule, but do not automatically deduct every amount labelled materials, tools, vehicle or expenses. Substantiate non-labour components attributable to the contract and apply s 35(2), approved trade deductions in PTA 018 and the determination requirements in PTA 019. A separately issued invoice does not override an approved deduction; higher/unlisted deductions require approval/determination. General office, accounting and insurance expenses do not become deductible merely because incurred. The overview's owner-driver fuel exception depends on an instrument whose continued force is not confirmed here. [PTA 018](https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta018), [PTA 019](https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta019), [Act s 35](https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021#sec.35).
- **Employment agents.** Agency rules can deem payments wages where the agent procures workers for a client; contractor exclusions are unavailable. The specific s 40(2) exempt-client declaration route remains, subject to its exclusions: test whether the payment would be exempt if the client employed the worker, obtain the required declaration per contract at commencement and retain it for 5 years. Exempt client status alone does not exempt every activity. Distinguish actual employees under s 66B/Sch 2 cl 13B. [Act ss 36A-40, 66B and Sch 2](https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021), [agency guidance](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/employment-agencies), [declarations](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/exemptions/employment-agency-contracts).
- **Principal contractor recovery.** NSW can recover a subcontractor's unpaid tax on relevant employees' work under the principal's business contract when unpaid 60 days after financial-year end. An approved subcontractor statement protects its covered period unless the principal had reason to believe it false. It does not remove the principal's separate payroll-tax liability on its own payments to the subcontractor. [Act Sch 2 cls 17-18](https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021#sch.2).
- **Medical and allied health practices**; Practices that engage practitioners under service agreements have been an audit focus, and several offices publish rulings and concessions on when the relevant contract provisions apply. Check the ruling in the relevant jurisdiction before assuming the practitioners fall outside the provisions.  _(ACT Revenue Office, Designated medical practices with general practitioners; https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/designated-medical-practices-with-general-practitioners)_

## Boundary and exception table

### Section 11 - Common errors

- Claiming the full threshold whilst paying interstate wages, or not updating the interstate figure after another office's audit.
- Leaving out director's fees, superannuation contributions, grossed-up fringe benefits and employee share scheme benefits.
- Declaring wages in the wrong jurisdiction when services were performed wholly in one state for the month.
- Treating a worker with an ABN or a company as outside the contractor provisions without testing the exemptions.
- Missing the employment agency provisions, which switch off the contractor exemptions.
- Lodging as non-grouped without testing control, shared employees and every grouping gateway; a common director/shareholder is not automatically sufficient.
- Applying the Victorian phase-out or the Queensland or NT deduction taper to the jurisdiction's wages rather than Australian wages.
- Missing the relevant group/period wage base for ACT/NT rates, QLD levy and VIC surcharges, or confusing the QLD regional cap with those tests.
- Missing the monthly due date (generally the 7th; Section 9), or the 21 July and 28 July annual due dates.
- Applying one rule to WA and ACT portable long service leave/redundancy payments. WA taxes employer fund contributions; ACT PTA034 gives different treatment for the covered construction-industry funds, subject to the qualification below.



| Boundary or exception | Decision and evidence required |
| --- | --- |
| Australian wages below local headline threshold | Check group wages, period and local registration trigger before returning nil; QLD's weekly registration rule is separate |
| DGE/GSL or regional classification | Obtain group nomination/status and actual regional wage/work records; do not choose the lower result by assumption |
| Exactly 180 service-kind days in NSW | The less-than-180 exclusion fails; test another supported exclusion or include the relevant wages |
| NSW grouping exclusion or agency declaration | Obtain the written determination or valid contract-specific declaration; an application/client label is insufficient |
| WA versus ACT portable funds | WA employer contributions to portable LSL and redundancy funds are taxable when paid/payable; direct LSL wages are exempt to the extent recoverable from the fund. For the construction-industry schemes covered by ACT PTA034, the statutory portable-scheme levy is not liable; covered LSL/approved redundancy contributions are not liable unless a taxable fringe benefit, and benefits from those covered funds are not wages |
| Mixed interstate/overseas work | Apply monthly nexus in order; do not apportion by workdays without first testing wholly-local/PPR/payment rules |
| Missing allowance travel/km proof | Do not apply the cap automatically; obtain substantiation or treat/refer the unsupported exemption |
| Filing/payment unresolved | Hold submission, preserve the due date and obtain authorised source/fact clarification; a saved draft is not a lodged return |

Portable-fund sources: [RevenueWA other taxable wages](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/wages-payroll-tax-employer-guide/taxable-wages-payroll-tax-employer-guide/other-taxable-wages-payroll-tax-employer-guide), [ACT PTA034 paragraphs 4-5, Payroll Tax Act 2011 s 14](https://www.revenue.act.gov.au/__data/assets/pdf_file/0004/2944597/PTA034.pdf).

## Worked cases

### Section 10 - Worked example

**Worked example facts**

| Item | Detail |
| --- | --- |
| Employer | Harbour Fitouts Pty Ltd, not a member of a group, metropolitan, employing for all of 2026-27 |
| NSW taxable wages | $1,500,000 |
| Victorian taxable wages | $1,000,000 |
| Australian taxable wages | $2,500,000 |
| Contractors and fringe benefits | None |

**Facts.** All figures are synthetic.

**Step 1, registration.** Monthly Australian wages of about $208,333 exceed the NSW and Victorian
monthly thresholds, so the company is registered in both and lodges monthly returns by the 7th (NSW December return: 14 January; no separate June return in either).

**Step 2, NSW.**

```
NSW threshold 1,200,000 x (1,500,000 / 2,500,000)        720,000
NSW taxable wages                                       1,500,000
Wages above the threshold                                 780,000
Payroll tax at 5.45%                                       42,510
```

**Step 3, Victoria.** Australian wages are below $3m, so the phase-out does not apply and the
deduction is simply apportioned. Australian wages are below $10m, so neither surcharge applies.

```
Victorian deduction 1,000,000 x (1,000,000 / 2,500,000)  400,000
Victorian taxable wages                                 1,000,000
Wages above the deduction                                 600,000
Payroll tax at 4.85%                                       29,100
```

**Step 4, total.** $71,610 for the year, reconciled in the NSW annual return by 28 July 2027 and
the Victorian annual reconciliation by 21 July 2027.

**The same $2,500,000 payroll paid in one jurisdiction only**

| Jurisdiction | Threshold or deduction | Taxable amount | Payroll tax |
| --- | --- | --- | --- |
| NSW | $1,200,000 | $1,300,000 | $70,850 |
| VIC, metropolitan | $1,000,000 | $1,500,000 | $72,750 |
| QLD, non-regional | Exact $1,128,571.4286…; displayed $1,128,571 | Exact $1,371,428.5714… | $65,142.86; nearest dollar $65,143 |
| WA | Exact $769,230.7692…; displayed $769,231 | Exact $1,730,769.2308… | $95,192.31; nearest dollar $95,192 |
| SA | $600,000 | $1,900,000 at 4.95% | $94,050 |
| TAS | $1,250,000 | $750,000 at 4% plus $500,000 at 6.1% | $60,500 |
| ACT | $1,750,000 | $750,000 at 6.75% | $50,625 |
| NT | $2,500,000 | Nil | Nil |

**Comparison scope.** The same payroll costs nothing in the NT and $95,192 in WA. The NT nil result holds only up to $2.5m of Australia-wide wages: at $4,000,000 of NT-only wages the deduction tapers to $1,750,000 and tax is $123,750 (Section 3). Interstate
employers should model the group's Australian wages in each jurisdiction before assuming a single
national rate.

### Recomputing controls for the retained examples

Use exact amounts through each calculation below, then round the displayed tax to cents with half-up rounding. The original comparison's nearest-dollar amounts remain identified as display figures. These conventions test the illustration; the actual return's published field/rounding rules control lodgement.

**Case 1: Harbour Fitouts, interstate wages.** The facts and 4-step walk-through above are retained. Full-year NSW/VIC shares reduce their deductions to $720,000 and $400,000. The NSW tax is $42,510 and Victorian tax $29,100, total $71,610. Neither Victorian surcharge applies.

```oa-check
name: Harbour Fitouts interstate payroll 2026-27
inputs:
  nsw_wages: 1500000
  vic_wages: 1000000
steps:
  australian_wages: nsw_wages + vic_wages
  nsw_deduction: 1200000 * nsw_wages / australian_wages
  vic_deduction: 1000000 * vic_wages / australian_wages
  nsw_tax: (nsw_wages - nsw_deduction) * 0.0545
  vic_tax: (vic_wages - vic_deduction) * 0.0485
  total: nsw_tax + vic_tax
expected:
  nsw_deduction: 720000
  vic_deduction: 400000
  nsw_tax: 42510
  vic_tax: 29100
  total: 71610
```

**Case 2: the same $2.5m paid wholly in one jurisdiction.** This recomputes every row of the retained comparison. Each alternative is a separate full-year, ungrouped, ordinary-rate employer; no regional eligibility, exemption, levy or special university status is assumed. TAS is marginal-band tax; SA deducts $600,000. The comparison illustrates the rates, without deciding where a real business should operate.

```oa-check
name: Eight jurisdictions full-year 2.5m comparison 2026-27
inputs:
  wages: 2500000
steps:
  nsw: (wages - 1200000) * 0.0545
  vic: (wages - 1000000) * 0.0485
  qld_deduction: 1300000 - (wages - 1300000) / 7
  qld: round((wages - qld_deduction) * 0.0475, 2)
  qld_display: round(qld)
  wa_deduction: 1000000 - (wages - 1000000) * 2 / 13
  wa: round((wages - wa_deduction) * 0.055, 2)
  wa_display: round(wa)
  sa: (wages - 600000) * 0.0495
  tas: (2000000 - 1250000) * 0.04 + (wages - 2000000) * 0.061
  act: (wages - 1750000) * 0.0675
  nt: max(0, wages - 2500000) * 0.055
expected:
  nsw: 70850
  vic: 72750
  qld: 65142.86
  qld_display: 65143
  wa: 95192.31
  wa_display: 95192
  sa: 94050
  tas: 60500
  act: 50625
  nt: 0
```

**Case 3: may the employer claim the regional rate?** Compare both outcomes before deciding. A full-year QLD-only employer with $2.5m wages has ordinary tax $65,142.86 or regional tax $51,428.57. It may use the regional result only if its principal place of employment, 85% wage/residence test and cap all qualify. Otherwise the ordinary result applies; absence of proof is not a choice to save $13,714.29.

Separately, a full-year VIC-only employer with $1.1m wages pays $4,850 at the ordinary rate or $1,212.50 if its regional work/wage tests are met, a $3,637.50 difference. Regional businesses in a group are tested individually. Neither example reaches levy/surcharge thresholds.

```oa-check
name: Regional eligibility decision both outcomes 2026-27
inputs:
  qld_wages: 2500000
  vic_wages: 1100000
steps:
  qld_deduction: 1300000 - (qld_wages - 1300000) / 7
  qld_base: qld_wages - qld_deduction
  qld_ordinary: round(qld_base * 0.0475, 2)
  qld_eligible: round(qld_base * 0.0375, 2)
  qld_difference: qld_ordinary - qld_eligible
  vic_base: vic_wages - 1000000
  vic_ordinary: vic_base * 0.0485
  vic_eligible: vic_base * 0.012125
  vic_difference: vic_ordinary - vic_eligible
expected:
  qld_ordinary: 65142.86
  qld_eligible: 51428.57
  qld_difference: 13714.29
  vic_ordinary: 4850
  vic_eligible: 1212.50
  vic_difference: 3637.50
```

**Case 4: QLD levy taxes excess wages.** These are levy amounts only; ordinary payroll tax is additional. For full-year ungrouped QLD-only employers, $10m gives nil levy, $11m gives $2,500, $100m gives $225,000 and $110m gives $300,000. For a separate full-year employer with $4m QLD/$16m Australian wages, the primary threshold is $2.5m and levy $3,750; its adjusted additional threshold is $25m, so no additional levy.

```oa-check
name: Queensland levy excess and interstate bases 2026-27
inputs:
  low: 10000000
  middle: 11000000
  boundary: 100000000
  high: 110000000
  local: 4000000
  australian: 16000000
steps:
  low_levy: max(0, low - 10000000) * 0.0025
  middle_levy: max(0, middle - 10000000) * 0.0025
  boundary_levy: max(0, boundary - 10000000) * 0.0025 + max(0, boundary - 100000000) * 0.005
  high_levy: max(0, high - 10000000) * 0.0025 + max(0, high - 100000000) * 0.005
  local_primary_threshold: 10000000 * local / australian
  local_additional_threshold: 100000000 * local / australian
  local_levy: max(0, local - local_primary_threshold) * 0.0025 + max(0, local - local_additional_threshold) * 0.005
expected:
  low_levy: 0
  middle_levy: 2500
  boundary_levy: 225000
  high_levy: 300000
  local_primary_threshold: 2500000
  local_additional_threshold: 25000000
  local_levy: 3750
```

**Case 5: NT deduction floor and higher-rate boundary.** For full-year ungrouped NT-only employers, the retained $4m illustration gives deduction $1.75m and tax $123,750. At $7.5m deduction is nil and tax $412,500; at $8m the deduction remains nil, rather than becoming negative, and tax is $440,000. A separate employer with $100m in the relevant period uses 6.5%, giving $6.5m. The case stipulates full-year relevant periods; it does not prorate the statutory $100m test.

```oa-check
name: Northern Territory taper zero floor and rate boundary 2026-27
inputs:
  four: 4000000
  exhaustion: 7500000
  above: 8000000
  higher: 100000000
steps:
  four_deduction: max(0, 2500000 - (four - 2500000) / 2)
  four_tax: (four - four_deduction) * 0.055
  exhaustion_deduction: max(0, 2500000 - (exhaustion - 2500000) / 2)
  exhaustion_tax: (exhaustion - exhaustion_deduction) * 0.055
  above_deduction: max(0, 2500000 - (above - 2500000) / 2)
  above_tax: (above - above_deduction) * 0.055
  higher_tax: higher * 0.065
expected:
  four_deduction: 1750000
  four_tax: 123750
  exhaustion_deduction: 0
  exhaustion_tax: 412500
  above_deduction: 0
  above_tax: 440000
  higher_tax: 6500000
```

**Case 6: Victorian full-year phase-out.** For separate VIC-only ungrouped metropolitan employers, the deduction is $1m at $3m wages, $400,000 at $4.2m and nil at $5m or above. The retained current $4.2m illustration gives tax $184,300.

```oa-check
name: Victoria current full-year phase-out boundaries 2026-27
inputs:
  start: 3000000
  example: 4200000
  end: 5000000
  above: 5100000
steps:
  start_deduction: max(0, 1000000 - max(0, start - 3000000) * 0.5)
  example_deduction: max(0, 1000000 - max(0, example - 3000000) * 0.5)
  end_deduction: max(0, 1000000 - max(0, end - 3000000) * 0.5)
  above_deduction: max(0, 1000000 - max(0, above - 3000000) * 0.5)
  example_tax: (example - example_deduction) * 0.0485
expected:
  start_deduction: 1000000
  example_deduction: 400000
  end_deduction: 0
  above_deduction: 0
  example_tax: 184300
```

**Case 7: retained small illustrations and historical rounding.** NSW's 184/365 historical-days example gives $604,931.51; its $900,000/$3m interstate share gives $360,000. WA's $1.2m full-year example gives exact deduction $969,230.7692…, displayed $969,231.

For the Victorian 335-day/$1.5m-local/$3.5m-Australian example, the source's 2024-25 result $210,030 uses rounded intermediate amounts: $354,012 minus $143,982. Unrounded 2024-25 arithmetic gives $210,029.35, so these are distinct rounding presentations. Current 2026-27 settings give exact $233,365.9491…, displayed $233,366. The source's historical worked example is not a current rate or a direction to round every return step.

```oa-check
name: Retained apportionment illustrations and historical rounding
inputs:
  nsw_days: 184
  vic_days: 335
  year_days: 365
  vic_local: 1500000
  vic_australian: 3500000
steps:
  nsw_days_threshold: round(1200000 * nsw_days / year_days, 2)
  nsw_interstate_threshold: 1200000 * 900000 / 3000000
  wa_deduction: 1000000 - (1200000 - 1000000) * 2 / 13
  wa_display: round(wa_deduction)
  vic_share: vic_days / year_days * vic_local / vic_australian
  vic_old_base: round(900000 * vic_share)
  vic_phase_base: round(3000000 * vic_share)
  vic_old_reduction: round((vic_local - vic_phase_base) * 0.45)
  vic_old_published: vic_old_base - vic_old_reduction
  vic_old_exact_cents: round(900000 * vic_share - (vic_local - 3000000 * vic_share) * 0.45, 2)
  vic_current_exact: 1000000 * vic_share - (vic_local - 3000000 * vic_share) * 0.5
  vic_current_cents: round(vic_current_exact, 2)
  vic_current_display: round(vic_current_exact)
expected:
  nsw_days_threshold: 604931.51
  nsw_interstate_threshold: 360000
  wa_display: 969231
  vic_old_published: 210030
  vic_old_exact_cents: 210029.35
  vic_current_cents: 233365.95
  vic_current_display: 233366
```

The source URLs for these illustrations are on the corresponding rates/conditions rows and apportionment paragraphs above. All eligibility, full-year and grouping assumptions must be rechecked for a real employer.


## When to refuse or refer

Return **Needs Input** for missing wage components, Australian/group totals, employment dates, nexus, contractor records, regional eligibility or payment history. Give the exact missing item and the affected period/calculation; do not fill it with an assumed exemption or nil amount.

Refer disputed grouping/control, worker classification, agency chains, medical-practice concessions, overseas/offshore nexus, retrospective amendments, penalty remission and conflicting portal/law treatment to a qualified Australian adviser. Preserve lodgement/payment deadlines and identify any extension request separately. This working paper does not authorise submission or payment for a client.

## Filing and payment

### Section 9 - Registration, lodgement and compliance

**Registration and return cycle.** Test each jurisdiction in which taxable wages arise against Australian/group wages and its local trigger. NSW and WA registration is ordinarily required within 7 days after the relevant month, ACT within 7 days and NT within 21 days; QLD also requires registration when Australian wages exceed $25,000 in a week even if the expected annual total is below $1.3m. Confirm the exact local trigger and commencement period from the registration notice. An approved quarterly/annual cycle is not an automatic election.

| Jurisdiction | Ordinary monthly and June treatment | Annual/adjustment deadline and payment distinction | Source |
| --- | --- | --- | --- |
| NSW | 7th/next business day; December 2026 due 14 January 2027; June included in annual return | 28 July 2027, lodge and pay separately | [Published 2026-27 calendar](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/key-dates) |
| VIC | 7th/next business day; June in annual e-AR | 21 July/next business day, lodge and pay | [Monthly](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/lodge-your-monthly-return), [annual](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/lodge-your-annual-reconciliation) |
| QLD | 7th/next business day; December 2026 due 14 January 2027; no June periodic return | 21 July 2027, lodge and pay | [Due dates](https://qro.qld.gov.au/payroll-tax/returns/due-dates/) |
| WA | Usually 7th; June return/payment and year-end ATW/ETW information by 21 July | RevenueWA later performs reconciliation; pay any later assessed adjustment by its Assessment Advice date. Current FAQ describes ordinary October settlement, not a guaranteed 2027 timetable | [Returns](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/returns-payroll-tax-employer-guide), [annual FAQ](https://www.wa.gov.au/government/multi-step-guides/revenue-online-frequently-asked-questions/revenue-online-faqs-payroll-tax/payroll-tax-faqs-annual-reconciliation) |
| SA | 7th/next business day; no June monthly return. Christmas/New Year extensions may be published; no fixed December 2026 extension is confirmed here | 28 July/next business day annual reconciliation/payment | [Monthly](https://www.revenuesa.sa.gov.au/payrolltax/returns-and-annual-reconciliation/monthly-returns), [annual](https://www.revenuesa.sa.gov.au/payrolltax/returns-and-annual-reconciliation) |
| TAS | 7th/next business day; June included in annual adjustment | 21 July, lodge and pay, subject to published calendar | [Lodgement](https://www.sro.tas.gov.au/payroll-tax/lodge-your-return) |
| ACT | 7th/next business day; December due 14 January; all outstanding monthly/nil returns precede June annual | 28 July, lodge and pay | [ACT about payroll tax](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/about-payroll-tax), [lodging returns](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/lodging-returns) |
| NT | Within 21 days after month-end; annual June adjustment replaces separate June monthly return | 21 July/next NT business day; earlier cessation rules may apply | [Act ss 86-87](https://legislation.nt.gov.au/api/sitecore/Act/PDF?id=12078), [current changes](https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-changes-from-1-july-2026) |

These are standing rules and the expressly dated calendars identified above. Public tutorials may still show 2025-26 annual forms. Verify the selected return's financial year, current form fields and issued due/payment dates before lodging for 2026-27.

### Public portal workflow by jurisdiction

**NSW, Payroll Tax Online.** Register through the [online registration instructions/form](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/registration/register-for-payroll-tax), preparing ABN/entity/contact/group details and current/preceding wage records; the registration form cannot save unfinished work. Retain its acknowledgement/reference and issued Client ID. Access Payroll Tax Online with Client ID and the latest Correspondence ID.

For a monthly actual return, select **Calculate a monthly return → Actual**, enter NSW wage components, liable interstate wages and required group wages, then **Calculate and save**. The alternative Estimate method has eligibility conditions; do not assume it is available. Annual preparation uses **Lodge your annual return**, NSW/June components, employment dates, interstate wages and DGE/group identifiers. Review and select **Lodge**, then retain the green confirmation/lodgement reference. **Pay Online** requires payment authorisation; **Other Payment Options** only supplies EFT/BPAY details. Verify **Return History Summary**, the separate payment confirmation and bank settlement. [Monthly method](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/monthly-return), [annual fields/lodgement](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/annual-return), [payment references](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/payment-options).

**VIC, PTX Express.** Follow [registration](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/register-payroll-tax), retain written registration confirmation and use **Create Login**. Monthly: **Lodge Monthly Return → month → taxable wages → lodge**; retain the supplied payment reference. Annual: **Annual Reconciliation → correct year → Begin**, update details, enter Victorian components/interstate amounts/employment periods, tax paid and relevant group/regional splits. Review the balance, choose **Lodge** on the **Lodgement** page and retain the lodgement number/**View PDF Summary**. Pay using **Pay Online** or the supplied EFT/BPAY/card details and retain the payment receipt. [Monthly](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/lodge-your-monthly-return), [annual e-AR instructions](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/lodge-your-annual-reconciliation).

**QLD, QRO Online.** Register an individual user, then **Registration → Payroll tax registration form**; supply employer/ABN/status, dates, group/DGE identifiers and actual/estimated local/interstate wages. **Save → Review → resolve errors → Submit** gives a submission popup, not approval. Await the registration notice and activation/linking instructions. For returns: **View accounts → client → Returns → period → Lodge returns**. Enter Queensland wage components, apprentice/trainee amounts, applicable fixed deduction and required levy/group estimates. **Save as draft** can issue a transaction/payment number but does not lodge. Review, complete the authorised declaration and **Submit**; verify the confirmation and **Year to date/Lodgement history → View form**. Before the annual return, lodge all required periodic returns and any outstanding final return for a relevant status change. Annual own interstate wages and DGE group wages are distinct inputs; include the DGE's own amounts in group wage totals. For the DGE levy reconciliation, include its own wages in the group levy-period totals, but exclude its own periodic levy from **Less total periodic levy amounts for your group members**: the system credits its own amount separately in **Less periodic levy amounts**. Pay via **Payments → Pay → Make payment**, retain the receipt and verify cleared funds. [Registration](https://qro.qld.gov.au/payroll-tax/register/), [periodic tutorial](https://qro.qld.gov.au/payroll-tax/returns/periodic-tutorials/), [annual tutorial](https://qro.qld.gov.au/payroll-tax/returns/annual-tutorials/). The current annual tutorial illustrates 2025-26 and 2026-27 estimates; it does not prove final July 2027 fields.

**WA, Revenue Online through RevenueWAConnect.** Check registration type and return frequency in **Client Profile**. Use **Lodge Return/Lodge Return and Pay** for the period and complete through the confirmation screen. At year end reconcile wages and supply actual **Australian Taxable Wages (ATW)** and next-year **Estimated Taxable Wages (ETW)** by 21 July. **End of Year Lodgment (EOYL)** applies to interstate non-group employers and relevant DGEs; a DGE must wait for members' outstanding returns. Ordinary group members, local non-group employers and annual-frequency local DGEs use **Lodge Return/Modify Return** for June; eligible EOYL users can include June through **Taxable Wages - Wage Adjustment**. Use the actual registration type's instructions. Missing ATW/ETW can remove the relevant deduction. Pay June separately by its due date, then check the later reconciliation Assessment Advice and its payment date. CIPA payments require employer initiation; EFT references are transaction-specific. [Registration](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/registration-payroll-tax-employer-guide), [annual guide](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/annual-reconciliation-payroll-tax-employer-guide), [annual FAQ](https://www.wa.gov.au/government/multi-step-guides/revenue-online-frequently-asked-questions/revenue-online-faqs-payroll-tax/payroll-tax-faqs-annual-reconciliation), [payments](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/payments-payroll-tax-employer-guide).

**SA, RevenueSA Online.** Register from the briefcase icon's **New Payroll Tax Registration**, with entity, employment dates, grouping and SA/interstate wage data. Monthly: **Payroll Tax → Monthly Returns → month**, enter whole-dollar wage components as instructed and review the system's rate/deduction. EFT/BPAY: **Generate Payment Advice**, download the **Payroll Tax Return Declaration** and use that return's exact unique reference. Direct debit requires its own authorisation/**Submit** and payment summary. Nil liability requires **Lodge Nil Return** and confirmation. Annual: **Payroll Tax → Annual Returns**, prepare status periods, SA/interstate/group wages and estimates, with DGE first where grouped. Review **Reconciliation Calculation/Deduction Allocation/Declaration** and retain the **Payroll Tax Annual Reconciliation Report** and payment evidence. The detailed public annual page currently describes 2025-26, so confirm current-year fields. [Registration](https://www.revenuesa.sa.gov.au/payrolltax/register-for-payroll-tax), [monthly transcript](https://www.revenuesa.sa.gov.au/payrolltax/returns-and-annual-reconciliation/monthly-returns), [annual help](https://www.revenuesa.sa.gov.au/payrolltax/returns-and-annual-reconciliation/prtar).

**TAS, Tasmanian Revenue Online (TRO).** Create the user and register the entity. Periodic: account → **Returns → Manage Returns → Create** beside period → enter details → **Submit → acknowledgement → Submit (pay outside Portal)**. Annual: confirm registration details, then **Returns → Manage Returns → Submit** beside the annual return to open it. Enter the details → **Submit** → tick the acknowledgement checkbox → **Submit (pay outside Portal)**. Retain the acknowledgement, return to the account and verify the submitted date. Payment is separate: assessment/invoice in **Summary/Financial summary → Pay → Pay Now → Submit**, with the EPA agreement/bank setup if applicable. **Payment Scheduled** establishes scheduling, not settled payment; amounts remain italic until processed. The public return pages do not enumerate every wage field: inspect the selected year rather than invent labels. [Register](https://www.sro.tas.gov.au/payroll-tax/Registration), [periodic help](https://www.sro.tas.gov.au/resources/tasmanian-revenue-online/payroll-tax-and-insurance-duty/manage-returns/submit-a-periodic-return), [annual help](https://www.sro.tas.gov.au/resources/tasmanian-revenue-online/payroll-tax-and-insurance-duty/manage-returns/submit-an-annual-return), [payment help](https://www.sro.tas.gov.au/resources/tasmanian-revenue-online/payroll-tax-and-insurance-duty/payments-accounts/make-a-payment).

**ACT, Self Service Portal (SSP).** Register using the [registration/notification form](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/registration); obtain authorised Digital ID/myID/RAM access for SSP. Select **Return Lodgements → Payroll Tax** or the outstanding **Lodge Return**, select period, then **Save and Next → Wages/Reconciliation**. Mandatory wage fields require at least zero. Enter own ACT wages, or consolidated wages only if approved jointly, and required threshold/group Australian/ACT wage amounts. Review **Lodgement Summary**, declaration and **Submit**. Retain the submitted PDF in **Activity History** and use its payment details; BPAY references differ by month/lodgement. Lodge all required monthly/nil returns before the June annual; approved annual lodgers do not need monthly returns. [SSP instructions](https://www.revenue.act.gov.au/business-taxes-and-levies/self-service-portal), [public return guide, November 2024](https://www.revenue.act.gov.au/__data/assets/pdf_file/0008/2952395/Lodge-a-Payroll-Tax-Return.pdf), [payment/lodging](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/lodging-returns).

**NT, INTRA.** Register through [INTRA](https://intra.nt.gov.au/) and retain the registration response. Supply NT wage components and separate exemptions, expected Australian/group annual wages for the rate test, and annual actual NT/Australian/group wages plus commencement/cessation dates. INTRA calculates liability; lodge the **Annual Adjustment Return (AAR)** for the correct year. Public sources reviewed do not establish every live menu label, confirmation or payment-reference field: obtain them from the issued return/payment advice before completing the action. The official guide lists direct credit/EFT/BPAY. An annual cycle is subject to the Commissioner's treatment/approval; the guide records a $20,000 estimated annual tax threshold from 1 September 2026. [Public INTRA guidance](https://treasury.nt.gov.au/dtf/territory-revenue-office/intra), [NT employer guide, updated 1 September 2026, pp 47-49, 53-55](https://treasury.nt.gov.au/pms/tro/information/payroll-tax-guide-for-nt-employers-and-businesses.pdf).

### Cessation, amendments, penalties and records

**Final returns and cancellation.** A new ABN, cessation, grouping change or insolvency appointment may require a local final return/registration change. Do not cancel merely because one period is nil. In SA, cancellation is available on cessation or when the employer's Australian wages, or the group's Australian wages if grouped, fall below the threshold. An annual cycle may be requested instead where liability is expected to recur. A 30 June cancellation is completed through annual reconciliation; for a midyear request, wait for RevenueSA to open the current-year reconciliation, then lodge the final return. RevenueSA publishes a **14-day payment requirement** for this route, but its paragraph does not clearly identify the starting event: confirm the actual due date from the issued notice and pay accordingly. In TAS, settle outstanding returns/liabilities and use **Update/Cancel Registration → Request Cancellation**, with last wage date/reason, then check request details. ACT publishes **Service Requests → Tax Registration Cancellation**, but this guide does not confirm a separate cessation deadline. [SA cancellation](https://www.revenuesa.sa.gov.au/payrolltax/cancel-registration), [TAS cancellation](https://www.sro.tas.gov.au/resources/tasmanian-revenue-online/payroll-tax-and-insurance-duty/manage-your-registration/cancel-your-registration), [ACT SSP](https://www.revenue.act.gov.au/business-taxes-and-levies/self-service-portal).

For QLD, ordinary final returns and payment are due within 21 days of a change of status. Mental health levy final returns and payment have a separate deadline: within 21 days after the end of the DGE's periodic return period containing the change. Identify the affected status period and levy return separately. [QRO final-return due dates](https://qro.qld.gov.au/payroll-tax/returns/due-dates/).

For NT, cancellation may be requested on cessation or when wages fall below the threshold, subject to the Australian/group wage test; one nil local period does not establish eligibility. Ceasing **all Australian wages** requires **F-PRT-002** and an AAR within 21 days after the cessation month ends, with any tax due paid by the 21st of the month following the final wage month. Ceasing NT wages whilst interstate employment continues requires cancellation plus nil monthly returns through May or approved annual treatment, then final AAR by 21 July; an immediate AAR may be possible if no annual deduction is claimed. Do not substitute the all-Australia rule for the interstate-continuing case. [NT guide pp 54-55](https://treasury.nt.gov.au/pms/tro/information/payroll-tax-guide-for-nt-employers-and-businesses.pdf).

**Penalties and disclosure.** Underpaid tax can attract interest and penalty tax. Revenue NSW states voluntary disclosure reduces penalty treatment compared with detected noncompliance, whilst interest remains. Obtain the jurisdiction's current schedule/notice before quantifying a penalty or claiming remission; no blanket national rate is asserted. [NSW interstate compliance and disclosure](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages).

**Records.** Retain source payroll, group/nexus/contract/exemption evidence, deductions, return versions, lodgement confirmations, payment references and settlement evidence for at least 5 years and any longer applicable requirement. NSW requires English or an easily translated form available for audit. Reconcile earlier amendments and other-state audits back to every affected local/interstate return. [NSW records/interstate reconciliation](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages).


## Completion checklist

### Section 12 - Self-checks

- [ ] Every component of remuneration, including super, fringe benefits and ETPs, is in the wages figure.
- [ ] Each employee's wages are assigned month by month under the nexus rules.
- [ ] Grouping has been tested for related corporations, common control, shared employees and traced interests.
- [ ] The threshold is apportioned for part-year employment and for the jurisdiction's share of Australian wages.
- [ ] The jurisdiction's phase-out or diminishing formula is applied to Australian wages.
- [ ] Each rate, levy, surcharge and regional cap uses its own verified employer/group/local wage base and relevant period.
- [ ] Every contractor exemption claimed has evidence on file.
- [ ] Exempt allowance rates match the current year's published figures.
- [ ] Monthly and annual returns are lodged in every registered jurisdiction, including nil returns.
- [ ] Records supporting each jurisdiction's wages are kept for 5 years.
- [ ] The correct current form/year, group status and return period were checked before submission.
- [ ] Lodgement confirmation, separate payment authorisation/reference and cleared funds are evidenced.
- [ ] June, later WA assessments and any cessation return have their own checked due dates.
- [ ] Every unresolved source/client condition is recorded for review rather than filled with an assumption.

## Sources

| Source | URL | Read on and scope |
| --- | --- | --- |
| Payroll Tax Australia index | <https://www.payrolltax.gov.au/harmonisation/payroll-tax-rates-and-thresholds> | 4 November 2026; Jurisdiction links only; original claimed update date not reverified |
| ACT calculation | <https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/calculating-payroll-tax> | 4 November 2026; Threshold/day/interstate apportionment and current rate context |
| NT rates | <https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-tax-rates-and-thresholds> | 4 November 2026; 2026-27 threshold and rate bands |
| NT Act, current 1 July 2026 | <https://legislation.nt.gov.au/api/sitecore/Act/PDF?id=12078> | 4 November 2026; s 7A, ss 84, 86-87 and Sch 1 cls 1, 3-5, 7-9; formula images visually read at printed pp 67, 69; not whole Act |
| NT current changes | <https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-changes-from-1-july-2026> | 4 November 2026; Expanded 2026 higher-rate, relevant-period and June-adjustment conditions |
| QLD deductions | <https://qro.qld.gov.au/payroll-tax/calculate/deductions/> | 4 November 2026; Actual/fixed/annual deduction, group excess and cited statutory provisions |
| VIC threshold and phase-out | <https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/threshold-and-phase-out-rate> | 4 November 2026; Current threshold/50% rule and historical 2024-25 examples; rounded source intermediates distinguished |
| VIC rates | <https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/payroll-tax-current-rates> | 4 November 2026; Current ordinary/regional rates and surcharge context |
| WA calculation | <https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide> | 4 November 2026; Expanded ordinary rate, diminishing threshold and local/group/interstate routes |
| SA rates | <https://www.revenuesa.sa.gov.au/payrolltax/rates-and-thresholds> | 4 November 2026; Current rate/threshold/deduction and 2026-27 allowance table |
| TAS rates | <https://www.sro.tas.gov.au/payroll-tax/rates-thresholds> | 4 November 2026; Expanded 2026-27 marginal rates, monthly rounding and group/interstate calculation |
| Payroll Tax Australia wages | <https://www.payrolltax.gov.au/definitions-acronyms-list/w> | 4 November 2026; Wage components/definition only |
| Payroll Tax Australia ETP | <https://www.payrolltax.gov.au/employment-termination-payment> | 4 November 2026; Assessable ETP and late-payment definition only; read with NSW ss 27-28 |
| NSW FBT | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/fringe-benefits> | 4 November 2026; Type2 valuation, exempt benefits, 15-month alternative eligibility and annual/monthly fields |
| Payroll Tax Australia rulings index | <https://www.payrolltax.gov.au/revenue-rulings-table> | 4 November 2026; Ruling descriptions and jurisdiction differences only; index updated 2023, not proof of each current ruling |
| Payroll Tax Australia lodging | <https://www.payrolltax.gov.au/lodging> | 4 November 2026; Portal/index overview only; local operational pages below control |
| NSW thresholds | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/thresholds-and-rates> | 4 November 2026; 2026-27 rates/monthly thresholds and historical 184-day illustration |
| NSW interstate wages | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages> | 4 November 2026; Local/Australian share, reporting, audit/disclosure and records |
| Payroll Tax Australia registration | <https://www.payrolltax.gov.au/registration> | 4 November 2026; Local-trigger differences/adjustment and cancellation overview |
| NSW nexus | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions> | 4 November 2026; Whole-local, ordered tiers, corporate PPR, pure overseas/split payments and offshore distinction |
| NSW grouping | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping> | 4 November 2026; Gateways, DGE/GSL/NL, threshold sharing and exclusion overview |
| NSW contractors | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors> | 4 November 2026; Overview and identified conflicts; detailed Act/rulings below control |
| Payroll Tax Australia relevant contract | <https://www.payrolltax.gov.au/relevant-contract> | 4 November 2026; Definition and WA non-application only |
| ACT designated GP practices | <https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/designated-medical-practices-with-general-practitioners> | 4 November 2026; Relevant-contract warning and designated-GP exemption context; no client eligibility certified |
| NSW key dates | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/key-dates> | 4 November 2026; Published 2026-27 monthly/annual calendar |
| ACT about payroll tax | <https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/about-payroll-tax> | 4 November 2026; Current rate bands, ordinary deadlines and registration context |
| TAS lodge return | <https://www.sro.tas.gov.au/payroll-tax/lodge-your-return> | 4 November 2026; Ordinary monthly, June and annual deadlines |
| VIC annual reconciliation | <https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/lodge-your-annual-reconciliation> | 4 November 2026; Current public e-AR inputs, sequence, confirmation and payment |
| SA returns/reconciliation | <https://www.revenuesa.sa.gov.au/payrolltax/returns-and-annual-reconciliation> | 4 November 2026; Ordinary annual deadline and next-business-day rule |
| QLD rates | <https://qro.qld.gov.au/payroll-tax/calculate/rates-thresholds/> | 4 November 2026; Ordinary rate tiers/current thresholds |
| QLD mental health levy | <https://qro.qld.gov.au/payroll-tax/mental-health-levy/> | 4 November 2026; Overview, read with detailed excess/adjustment calculation |
| WA returns | <https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/returns-payroll-tax-employer-guide> | 4 November 2026; Return cycle, June deadline and amendments |
| QLD regional discount | <https://qro.qld.gov.au/payroll-tax/calculate/regional-discount/> | 4 November 2026; 85%, residence/geography and authority cap wording; conflict with Act recorded |
| QLD Act | <https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1971-037> | 4 November 2026; ss 9-10A, annual-deduction and levy provisions; selected text only, not all formulas/Act |
| QLD levy calculation | <https://qro.qld.gov.au/payroll-tax/mental-health-levy/calculating/> | 4 November 2026; Excess bases, zero floors and interstate/period/group adjustment |
| QLD due dates | <https://qro.qld.gov.au/payroll-tax/returns/due-dates/> | 4 November 2026; Dated December 2026/annual 2027 calendar |
| QLD registration | <https://qro.qld.gov.au/payroll-tax/register/> | 4 November 2026; Weekly trigger, registration fields, submit/activate sequence |
| VIC regional criteria | <https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/industries-and-locations/regional-employers> | 4 November 2026; Monthly/annual 85%, regional work and separate group-member qualification |
| VIC surcharge conditions | <https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/payroll-tax-surcharges> | 4 November 2026; Separate/combined rates, period/share adjustments and COVID-only expiry |
| SA monthly returns | <https://www.revenuesa.sa.gov.au/payrolltax/returns-and-annual-reconciliation/monthly-returns> | 4 November 2026; Expanded workflow, unique payment references, nil and June treatment |
| SA calculation | <https://www.revenuesa.sa.gov.au/payrolltax/how-is-payroll-tax-calculated> | 4 November 2026; Annualised rate selection, $600,000 deduction, days/interstate and group allocation |
| NT payroll main | <https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax> | 4 November 2026; Ordinary annual/payment overview only |
| NSW registration | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/registration/register-for-payroll-tax> | 4 November 2026; Trigger/timing, historical wage/group inputs and acknowledgement |
| WA registration | <https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/registration-payroll-tax-employer-guide> | 4 November 2026; Local trigger/type and RevenueWAConnect/ROL route |
| NSW motor vehicle allowance | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/allowances/motor-vehicle> | 4 November 2026; Business-km records and 2026-27 cap |
| NSW accommodation | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/allowances/accommodation> | 4 November 2026; Temporary travel, 21-day/domestic dwelling, sleepover and component limits |
| QLD allowances | <https://qro.qld.gov.au/payroll-tax/exemptions/allowances/> | 4 November 2026; Previous-year vehicle rate, overnight and meals-only distinctions |
| VIC exempt wages | <https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/exempt-wages-and-organisations/wages-exempt-payroll-tax> | 4 November 2026; Examples/local exemptions only; not all client eligibility |
| SA annual detail | <https://www.revenuesa.sa.gov.au/payrolltax/returns-and-annual-reconciliation/prtar> | 4 November 2026; Workflow/help sections; page describes 2025-26, not released 2027 form |
| SA registration | <https://www.revenuesa.sa.gov.au/payrolltax/register-for-payroll-tax> | 4 November 2026; Registration and current public field sequence |
| TAS registration | <https://www.sro.tas.gov.au/payroll-tax/Registration> | 4 November 2026; Entity/TRO registration steps |
| NSW PTA031v2 | <https://www.revenue.nsw.gov.au/about/legislation-and-rulings/revenue-rulings/rulings/payroll/commissioners-discretion-to-exclude-from-a-group> | 4 November 2026; Exclusion test, applicant burden and smaller-group rule; Act s 79(8) adds phoenix bar |
| NSW CPN009 | <https://www.revenue.nsw.gov.au/help-centre/resources-library/cpn/cpn009> | 4 November 2026; Corporate common control and exclusion/connection discussion only |
| WA other taxable wages | <https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/wages-payroll-tax-employer-guide/taxable-wages-payroll-tax-employer-guide/other-taxable-wages-payroll-tax-employer-guide> | 4 November 2026; Specified benefits, redundancy/portable LSL contributions and recoverable direct leave wages |
| NSW termination payments | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/termination-payments> | 4 November 2026; Taxable/assessable leave and termination components; exempt redundancy/early retirement |
| NSW CPN007 | <https://www.revenue.nsw.gov.au/help-centre/resources-library/cpn/cpn007> | 4 November 2026; Contract exclusions/deductions; current Act/PTA021v2 control conflicting shorthand |
| NSW PTA020 | <https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta020> | 4 November 2026; Strict less-than-180 service-kind days and counting conditions |
| NSW PTA021v2 | <https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta021v2> | 4 November 2026; Current public-services exclusion and average 10 days/month accepted method |
| NSW PTA006 | <https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta006> | 4 November 2026; Conveyance/vehicle exclusion, main-purpose and contribution limits |
| NSW PTA018 | <https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta018> | 4 November 2026; Approved trade deductions and higher-deduction approval |
| NSW PTA019 | <https://www.revenue.nsw.gov.au/help-centre/resources-library/rulings/payroll/pta019> | 4 November 2026; Labour/non-labour deduction and separate-invoice limitations |
| NSW agencies | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/employment-agencies> | 4 November 2026; Agency wage treatment and actual-employee distinctions |
| NSW agency declarations | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/exemptions/employment-agency-contracts> | 4 November 2026; Contract-specific exempt-client declaration and retention |
| NSW Act | <https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-2007-021> | 4 November 2026; ss 7, 10-11C, 27-28, 32, 35-40, 66B, 72, 79, Sch 1 cl 1 and Sch 2 cls 13B, 17-18; targeted independent reads, not whole Act |
| ACT PTA034 | <https://www.revenue.act.gov.au/__data/assets/pdf_file/0004/2944597/PTA034.pdf> | 4 November 2026; Full 2-page current construction-industry circular, especially paragraphs 4-5; not every fund |
| SA Act | <https://www.legislation.sa.gov.au/_legislation-documents/lz/c/a/payroll-tax-act-2009/current/2009.22.auth.pdf> | 4 November 2026; Compilation 31 March 2026; independent selected Sch 1 cls 1, 5, 9 rate/annualisation reads. Selected statutory provisions only; formula extraction checked against the group provision |
| NSW monthly workflow | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/monthly-return> | 4 November 2026; Actual/Estimate, wage fields, save and payment sequence |
| NSW annual workflow | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/annual-return> | 4 November 2026; Annual inputs, Lodge and green confirmation |
| NSW payment options | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/payment-options> | 4 November 2026; Direct debit versus manual references and history |
| VIC registration | <https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/register-payroll-tax> | 4 November 2026; Registration confirmation/Create Login |
| VIC monthly workflow | <https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/lodge-your-monthly-return> | 4 November 2026; Period/menu, lodgement and payment reference |
| QLD periodic workflow | <https://qro.qld.gov.au/payroll-tax/returns/periodic-tutorials/> | 4 November 2026; Draft versus submit, levy inputs, transaction number and payments |
| QLD annual workflow | <https://qro.qld.gov.au/payroll-tax/returns/annual-tutorials/> | 4 November 2026; Own/group wage fields and submission; still 2025-26 example/2026-27 estimates |
| WA annual guide | <https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/annual-reconciliation-payroll-tax-employer-guide> | 4 November 2026; EOYL eligibility and ATW/ETW fields/deadline |
| WA annual FAQ | <https://www.wa.gov.au/government/multi-step-guides/revenue-online-frequently-asked-questions/revenue-online-faqs-payroll-tax/payroll-tax-faqs-annual-reconciliation> | 4 November 2026; June/EOYL distinctions, later assessment and issued payment date; not dated 2027 schedule |
| WA payments | <https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/payments-payroll-tax-employer-guide> | 4 November 2026; CIPA initiation, references and June payment |
| SA cancellation | <https://www.revenuesa.sa.gov.au/payrolltax/cancel-registration> | 4 November 2026; 30 June annual route versus midyear request/final return |
| TAS periodic help | <https://www.sro.tas.gov.au/resources/tasmanian-revenue-online/payroll-tax-and-insurance-duty/manage-returns/submit-a-periodic-return> | 4 November 2026; Period/create/acknowledgement/submitted date; public text omits detailed fields |
| TAS annual help | <https://www.sro.tas.gov.au/resources/tasmanian-revenue-online/payroll-tax-and-insurance-duty/manage-returns/submit-an-annual-return> | 4 November 2026; Annual confirmation/submit/acknowledgement |
| TAS payments | <https://www.sro.tas.gov.au/resources/tasmanian-revenue-online/payroll-tax-and-insurance-duty/payments-accounts/make-a-payment> | 4 November 2026; EPA/Pay Now/Payment Scheduled versus processed |
| TAS cancellation | <https://www.sro.tas.gov.au/resources/tasmanian-revenue-online/payroll-tax-and-insurance-duty/manage-your-registration/cancel-your-registration> | 4 November 2026; Cancellation request/date/reason/confirmation |
| ACT registration | <https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/registration> | 4 November 2026; Published registration/notification route |
| ACT SSP | <https://www.revenue.act.gov.au/business-taxes-and-levies/self-service-portal> | 4 November 2026; Access, return lodgement, Activity History and cancellation menus |
| ACT lodging/payment | <https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/lodging-returns> | 4 November 2026; Monthly/nil before annual, channels and per-lodgement BPAY references |
| ACT return guide | <https://www.revenue.act.gov.au/__data/assets/pdf_file/0008/2952395/Lodge-a-Payroll-Tax-Return.pdf> | 4 November 2026; November 2024 public guide; independent wage/group/threshold/submit steps, not 2027 form availability |
| NT INTRA | <https://treasury.nt.gov.au/dtf/territory-revenue-office/intra> | 4 November 2026; Public register/returns/history overview; exact live reference fields not established |
| NT employer guide | <https://treasury.nt.gov.au/pms/tro/information/payroll-tax-guide-for-nt-employers-and-businesses.pdf> | 4 November 2026; Updated 1 September 2026; independent printed pp 47-49, 53-55: inputs, annual cycle, cessation, payment; not all 86 pages |
| TAS annual guideline | <https://www.sro.tas.gov.au/Documents/Annual-Adjustment-Return-Guideline.pdf> | 4 November 2026; Cover 2025-26; both thresholds/day/interstate structural mechanics only, not current 2027 form |

### Section 13 - Sources

- Payroll Tax Act 2007 (NSW), Payroll Tax Act 2007 (Vic), Payroll Tax Act 1971 (Qld), Pay-roll Tax Assessment Act 2002 (WA), Payroll Tax Act 2009 (SA), Payroll Tax Act 2008 (Tas), Payroll Tax Act 2011 (ACT) and Payroll Tax Act 2009 (NT); links on the Payroll Tax Australia legislation table.
- Payroll Tax Australia, Rates and thresholds, https://www.payrolltax.gov.au/harmonisation/payroll-tax-rates-and-thresholds
- Payroll Tax Australia, Registration, https://www.payrolltax.gov.au/registration
- Payroll Tax Australia, Lodging, https://www.payrolltax.gov.au/lodging
- Payroll Tax Australia, Revenue rulings table, https://www.payrolltax.gov.au/revenue-rulings-table
- Payroll Tax Australia, definitions of wages, relevant contract and employment termination payment, https://www.payrolltax.gov.au/definitions-acronyms-list/w
- Revenue NSW, Payroll tax thresholds and rates, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/thresholds-and-rates
- Revenue NSW, Payroll tax and interstate wages, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages
- Revenue NSW, Nexus provisions for payroll tax, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions
- Revenue NSW, Contractors and payroll tax, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors
- Revenue NSW, What is payroll tax grouping, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping
- SRO Victoria, Payroll tax current rates, https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/payroll-tax-current-rates
- SRO Victoria, Threshold and phase-out rate, https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/threshold-and-phase-out-rate
- Queensland Revenue Office, Payroll tax rates and thresholds, https://qro.qld.gov.au/payroll-tax/calculate/rates-thresholds/
- Queensland Revenue Office, Payroll tax deductions, https://qro.qld.gov.au/payroll-tax/calculate/deductions/
- Queensland Revenue Office, Mental health levy, https://qro.qld.gov.au/payroll-tax/mental-health-levy/
- WA Department of Treasury and Finance, Calculation: Payroll Tax Employer Guide, https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide
- RevenueSA, Rates and thresholds, https://www.revenuesa.sa.gov.au/payrolltax/rates-and-thresholds
- RevenueSA, Returns and Annual Reconciliation, https://www.revenuesa.sa.gov.au/payrolltax/returns-and-annual-reconciliation
- SRO Tasmania, Rates and thresholds, https://www.sro.tas.gov.au/payroll-tax/rates-thresholds
- ACT Revenue Office, Calculating payroll tax, https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/calculating-payroll-tax
- Territory Revenue Office, Payroll tax rates and thresholds, https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-tax-rates-and-thresholds
- Territory Revenue Office, Payroll changes from 1 July 2026, https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-changes-from-1-july-2026
- Payroll Tax Act 2009 (NT), as in force at 1 July 2026, https://legislation.nt.gov.au/api/sitecore/Act/PDF?id=12078
- Revenue NSW, Key dates for payroll tax, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/key-dates
- ACT Revenue Office, About payroll tax, https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/about-payroll-tax
- SRO Tasmania, Lodge your return, https://www.sro.tas.gov.au/payroll-tax/lodge-your-return
- SRO Victoria, Lodge your annual reconciliation, https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/managing-your-payroll-tax/lodge-your-annual-reconciliation

The previous guide recorded checks on 27 September and 31 October 2026, with v1.2 dated 2 November 2026. Those are inherited provenance, not new verification. The Sources table records the 4 November 2026 targeted reads and their scope.

> **Working paper only, not a lodged return.** Have a qualified Australian CPA or CA review this before registering, lodging or amending a payroll tax return. Thresholds, deduction formulas and levies change with each state budget, and grouping and contractor positions turn on the facts.
>
> Contributed by Ryan Duguid.

Not yet confirmed: Final accountant approval has not been obtained. Current-year 2027 annual form availability/final live fields; ACT university-cap eligibility (published maximum 6.85%); WA-specific allowance conditions; the continued force of the NSW owner-driver fuel exception instrument; the original WA harmonisation date of 1 July 2012 and claimed Payroll Tax Australia index update of 2 September 2026; full penalty/interest/remission schedules; and client-specific grouping, regional, contract, travel and overseas facts. A saved source body is not a full-document legal review. Exact NT live confirmation/payment-reference fields and all ACT cessation deadlines remain unresolved. The SA midyear 14-day payment starting event requires confirmation from the issued notice. Below-threshold cancellation is supported for SA and NT as described above; eligibility in other jurisdictions requires local confirmation. One nil period does not establish entitlement to cancel.

**Fork provenance.** This guide is maintained in the ryanduguid/openaccountants fork. The inherited referral block below describes upstream services; those services do not publish or verify this fork's changes.

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
