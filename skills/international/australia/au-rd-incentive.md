---
name: au-rd-incentive
description: >
  Use this skill for 2026-27 whenever asked about the Australian R&D Tax Incentive (R&DTI) -- the Division 355 tax offset for eligible research and development, who can claim (eligible corporate R&D entities and qualifying trustee/foreign-company cases), the refundable offset for companies under $20m aggregated turnover, the non-refundable offset with intensity tiers for larger companies, core vs supporting R&D activities, excluded activities, registration with AusIndustry/DISR within 10 months of year end, the $20,000 expenditure threshold, the $150 million cap, feedstock and clawback adjustments, aggregated turnover grouping, and record-keeping. Trigger on phrases like "R&D tax incentive", "R&DTI", "R&D offset", "research and development tax", "43.5% offset", "refundable R&D", "Division 355", "AusIndustry registration", "core R&D activities", "feedstock adjustment", or "R&D intensity". ALWAYS read this skill before touching any R&D tax offset work.
version: 1.7
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-04
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia R&D Tax Incentive Skill v1.7

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

> **Law-change context.** The R&DTI was reformed for income years starting on or after 1 July 2021 (Treasury Laws Amendment (A Tax Plan for the COVID-19 Economic Recovery) Act 2020): the old flat 43.5% refundable and 38.5% non-refundable rates were replaced with company-tax-rate-plus-premium rates and a two-tier R&D intensity test; the expenditure cap rose from $100m to $150m; a uniform clawback rule and Part IVA were extended to the offset. From income years starting on or after 1 July 2025, R&D activities relating to gambling, gambling services or gambling-like practices are ineligible unless conducted solely to generate new knowledge about minimising harm from them, and activities relating to tobacco, a tobacco product or accessory, a vaping good, tobacco extract, goods made using tobacco or its extract, or goods containing nicotine for human use (other than food whose only nicotine is naturally occurring) are ineligible unless conducted solely to generate new knowledge about the therapeutic use of therapeutic goods to minimise harm from those things or about ceasing the ingestion or transfer of nicotine ([Treasury Laws Amendment (Delivering an Efficient and Trusted Tax System) Act 2026, Sch 4](https://www.legislation.gov.au/C2026A00058/asmade/text), assent 30 June 2026); an earlier DISR finding for such a year does not bind the Commissioner to the extent it would treat an excluded activity as R&D. The statutory four-year amendment period applies to R&D claims. **Announced, not law:** the 2026-27 Budget (12 May 2026) proposes, from 1 July 2028, removing supporting R&D activities, raising the core offset rate by 4.5 percentage points, lowering the intensity premium threshold from 2% to 1.5%, limiting the refundable offset to a company's first 10 years, raising the minimum spend from $20,000 to $50,000, the refundable turnover threshold from $20m to $50m and the expenditure cap from $150m to $200m ([ATO, Better targeting the R&DTI](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/tax-reform-better-targeting-the-research-and-development-tax-incentive), read 4 November 2026; the announcement expressly says it is not yet law). Never apply these to a claim or plan around them as if enacted. Verify all rates before relying.

> **AUDIT FLASH POINT** Registration does not establish that activities or expenditure are eligible. The ATO and DISR may review both after registration. Classifying core R&D turns on scientific uncertainty and the knowledge threshold; this guide refers that technical judgement to a competent professional. The offset is claimed with the ATO after DISR registration. The ATO must publish limited expenditure data 2 years after the relevant financial year, with no opt-out. See [TA 2017/3](https://www.ato.gov.au/law/view/document?DocID=TPA/TA20173/NAT/ATO/00001) and [R&D transparency](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-transparency-reports).

This is a 2026-27 computation and preparation guide using the law read on 4 November 2026. Example 5 preserves the ATO's historical 2021-22 example. The form map under Filing and payment is expressly for Company tax return 2026, not authority for a 2026-27 return. Tier 2 does not establish taxpayer-specific eligibility or professional sign-off.

## Ask the client first

1. What are the income period, incorporation and tax residence, consolidated/MEC or R&D partnership status, and any treaty permanent establishment?
2. Which activities and activity years are registered with DISR, what are their IISA numbers and findings, and where and for whose benefit were the activities conducted?
3. What are worldwide aggregated turnover, connected/affiliate relationships and intra-group dealings, and the company tax rate supported by the company tax workpaper?
4. Did one or more exempt entities control the claimant at any time in the year under the modified 50% test in Rule 5? Provide ownership and control changes, not only year-end balances.
5. What are the eligible notional deductions, statutory total expenses, tax reconciliation, associate amounts/payments, prior deductions or offsets, and the asset deduction/pooling history?
6. What project records and apportionment evidence support the claim, and are there funding guarantees, grants, feedstock sales/own use, asset balancing events or other offsets/debts affecting the result?

### Section 9 -- Onboarding fallback

If the client provides only financial statements:

1. Sweep the GL per Section 3 for R&D-coded accounts, project codes and payroll allocations.
2. Confirm the entity is a corporation and request the DISR registration (IISA) number for the relevant income year.
3. Request timesheets, project plans and the apportionment methodology -- do not accept bare account balances.
4. Compute aggregated turnover across connected/affiliated entities before selecting an offset rate.
5. **Flag:** "Figures prepared from financial statements only. DISR registration number, contemporaneous project documentation, timesheets, apportionment methodology and group turnover not sighted. Activity eligibility is a technical judgement requiring review. No position should be taken until a qualified R&D tax adviser confirms."

## The method, step by step

### Section 1 -- Quick reference [ATO rates](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/rates-of-r-d-tax-incentive-offset)

**Read this whole section before computing or classifying anything.**

**Quick reference**

| Field | Value and conditions | Income period | Official source |
| --- | --- | --- | --- |
| Country | Australia | 2026-27 | [ATO eligibility](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/eligibility-for-the-r-d-tax-incentive) |
| Primary legislation | ITAA 1997 Division 355; Industry Research and Development Act 1986 | Current law read 4 November 2026 | [ATO statutory text, s 355-100](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100); [DISR registration](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/apply-for-the-randd-tax-incentive) |
| Administrators | ATO: offset/expenditure; AusIndustry/DISR on behalf of IISA: registration, activity eligibility and findings | 2026-27 | [ATO claim steps](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset) |
| Income year | 1 July 2026 to 30 June 2027 for a standard balancer; verify substituted accounting periods | 2026-27 | [ATO annual registration and claim steps](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset) |
| What it is | A tax offset claimed in the company tax return; no grant application or independent funding entitlement | 2026-27 | [ATO claim steps](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset) |
| Eligible entity | Australian-incorporated or Australian-resident foreign body corporate; qualifying treaty-resident foreign corporation to the extent of its Australian permanent-establishment business. Apply Rule 2's separate activity tests | 2026-27 | [s 355-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-35); [s 355-210](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-210) |
| Not eligible | Individuals, ordinary trusts, partnerships in their own right, corporate limited partnerships and exempt entities. Public trading trust corporate trustees and eligible corporate R&D partners have specific rules | 2026-27 | [s 355-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-35); [ATO entity guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/eligibility-for-the-r-d-tax-incentive) |
| Refundable offset | Aggregated turnover below $20m and no exempt control under Rule 5 at any time in the year: company tax rate plus 18.5 percentage points, up to the cap. At an established 25% rate this is 43.5% | 2026-27 | [s 355-100(1), (3)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) |
| Non-refundable offset | Turnover at least $20m or exempt control: company tax rate plus 8.5 points on deductions up to 2% of s 355-115 total expenses, plus 16.5 points on deductions above that band, up to the cap | 2026-27 | [s 355-100(1A)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100); [total expenses](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-115) |
| Expenditure cap | $150m of notional deductions receives the applicable premium calculation; excess receives only the company tax rate. Applies to either offset type | 2026-27 | [s 355-100(3)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) |
| Minimum spend | At least $20,000 total notional deductions. Below it, only qualifying non-associate RSP expenditure and monetary CRC contributions qualify; Rule 8 | 2026-27 | [s 355-100(2)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) |
| Registration deadline | Normally 10 months after the activity income year ends; register before claiming. Rule 7 covers extensions and earlier-year associate costs | Each activity year | [DISR application](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/apply-for-the-randd-tax-incentive); [extensions](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/request-an-extension-or-variation) |
| Amendment window | Generally 4 years; earlier-year and DISR finding/review exceptions, distinct objection rules and nil-assessment limits apply in Rule 12 | R&D claims | [ATO amendments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/correcting-mistakes-and-disputing-decisions) |
| Contributor | Open Accountants | This version | Repository history |
| Validated by | Pending; Tier 2 | This version | No professional approval claimed |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether an activity is core R&D | Do NOT self-classify. This is a technical/engineering judgement about scientific uncertainty -- escalate (R-AU-RD-1) |
| Unknown registration status | Assume NOT registered; confirm the DISR registration (IISA) number and that it matches the income year before computing any offset |
| Unknown aggregated turnover | Compute the group figure (entity + connected + affiliated, net of intra-group dealings) before choosing refundable vs non-refundable; do not guess |
| Software development claimed | Check internal-administration purpose for the claimant, connected entities and either direction of affiliate relationship; refer activity classification |
| Business-as-usual / routine activity claimed | Treat as ineligible ordinary business activity until shown to involve scientific uncertainty and the scientific method (TA 2017/3) |
| Feedstock output sold or used | Screen the actual s 355-445 supply/own-use trigger and attributable expenditure; quantify only when the conditions are met. Further transformation for supply and earlier adjustments need review |
| Overseas R&D activity | Hold the claim until registered activities and the required overseas finding in force are verified, including the statutory link, location and expenditure conditions; domestic foreign-beneficiary routes in Rule 2 are different |
| Expenditure incurred to an associate | Notionally deductible only when paid; check the ordinary-deduction choice for unpaid amounts in Rule 10 |

### Section 2 -- What it is and who can claim [ATO offsets](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/refundable-and-non-refundable-offsets)

The R&DTI is a tax offset through the company tax return. It is not a grant: there is no competitive funding round or payment independent of the tax system. For an eligible refundable entity, an excess offset can be refunded after the tax-offset priority and tax-debt rules. A non-refundable offset reduces tax; an unused amount can only be carried forward where the carry-forward rules are met. It is not refunded.

Eligible R&D expenditure generally replaces another deduction for the same amount. Unpaid associate expenditure has the specific otherwise-available ordinary-deduction or later R&D choice in Rule 10. Never deduct it twice or claim another offset for the same expenditure.

Aggregated turnover and the modified exempt-control test choose the offset type. Rule 5 supplies the rate calculation and cap. Refundable offsets are applied after other offsets except franking deficit tax offsets; non-refundable R&D offsets precede those refundable and franking deficit tax offsets but follow other offsets. Credits can be applied against tax debts and refunds can be retained for verification. Do not promise a cash payment from the offset calculation alone.

For refunded R&D offsets, the ordinary refund franking debit is effectively deferred. Later income-tax or PAYG payments do not create franking credits until those deferred debits have been recovered. This is not an additional refund or a waiver of all franking rules. See [ATO refund and franking guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/refundable-and-non-refundable-offsets).

### Section 3 -- GL sweep library

R&DTI work starts with the general ledger and the project/time records, not the offset claim the client hopes to make.

**GL sweep library**

| GL pattern | Likely issue | Action |
| --- | --- | --- |
| R&D expense / "R&D project" cost centres | Candidate notional deduction | Map each account to a registered DISR activity; confirm it is core or supporting, not BAU |
| Project codes / job codes linked to a DISR registration number | Expenditure linked to registered activities | Trace to the registration (IISA number) for the correct income year; confirm the statutory or approved extended deadline was met |
| Payroll allocations / timesheet-coded wages to R&D projects | Salary notional deduction | Substantiate time via timesheets/job cards; apportion between R&D and non-R&D on a reasonable, documented basis |
| Contractor / RSP invoices for R&D | External R&D expenditure | Ordinary contractors need not be RSPs. Below $20,000 total deductions, only the qualifying non-associate RSP field-of-registration or monetary CRC exception applies; verify it, not merely the invoice label |
| Depreciation on assets used in R&D | Tangible asset cost is excluded from the expenditure route | Test held/use, registration, modified Division 40 and previous simplified-depreciation/pooling conditions before claiming eligible decline; separate non-R&D use |
| Government grant income (recoupment) for R&D | At-risk and recoupment tests | Apply the at-risk test at incurrence first. For offsets actually obtained, screen the government recoupment trigger, CRC exclusion, repayments and project cap in Rule 11; assess grant income separately |
| "R&D" account holding rent, marketing, admin overhead | Ineligible / apportionment risk | Remove general operations and marketing; apply a reasonable, documented apportionment methodology only where there is a direct link |
| Software development capitalised/expensed | Internal-administration exclusion risk | Check dominant purpose and both directions of affiliate relationship as well as connected entities; capitalisation does not settle activity eligibility or intangible tax treatment |
| Intercompany charges to associates for R&D | Payment, beneficiary, prior deduction/offset and mark-up risks | Verify actual or constructive payment, no disqualifying earlier claim for that amount, market-value ceiling and group mark-up reduction; apply Rule 10 and TA 2023/4 |
| Materials/feedstock consumed in trials | Feedstock adjustment on sale/own use of output | Track feedstock inputs and outputs; quantify the adjustment in the trigger year |

### Section 5 -- Rules checked against the law

#### Rule 1 -- It is an offset, not a grant [ATO claim steps](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset)

The R&DTI is claimed as a tax offset in the company return after activity registration with DISR. It is not a government grant or a competitive funding application. A refundable excess may be paid after the offset-ordering, debt and verification rules in Section 2. A non-refundable excess is subject to carry-forward rules. Registration and expenditure eligibility remain separate tests.

#### Rule 2 -- Entity, location and beneficiary tests [ss 355-35 and 355-210](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-35)

An R&D entity is a body corporate incorporated under Australian law, or incorporated under foreign law and Australian tax resident. A foreign-incorporated treaty resident carrying on business through an Australian treaty-defined permanent establishment qualifies only to the extent it carries on business through that establishment. An exempt entity cannot qualify. Individuals, ordinary trusts, partnerships in their own right and corporate limited partnerships have no direct claim; a corporate trustee of a public trading trust is specifically covered, and eligible corporate R&D partners have special rules. A consolidated or MEC group is treated as a single entity for these activities: only its head company should register and claim. Refer those structures before computing. See [ATO entities](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/eligibility-for-the-r-d-tax-incentive).

Entity status alone is insufficient. For registered activities, [s 355-210](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-210) separately covers own-benefit work solely in Australia, the permanent-establishment exception, qualifying Australian work for foreign corporations, and own-benefit work wholly or partly outside Australia covered by a required finding in force. An activity conducted to a significant extent for another entity outside those permitted routes fails subsection (2).

The [s 355-215 permanent-establishment route](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-215) requires activity solely in Australia and, if it is supporting R&D, each corresponding core activity conducted or to be conducted solely in Australia with the specified registration or registrability. It also requires written evidence that the activity is for the body corporate but not for the purposes of the permanent establishment.

The [s 355-220 foreign-beneficiary route](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-220) is also Australian work, not permission for overseas work. Each foreign beneficiary must be incorporated abroad and resident under the qualifying treaty. Activity must be solely in Australia. If it is supporting R&D, each corresponding core activity must be conducted or to be conducted solely in Australia and meet the specified registration or registrability condition. Each foreign beneficiary must be connected or affiliated in either direction whilst the activity is conducted. A written agreement must bind only the claimant and those foreign corporations, with direct performance by the claimant or indirect performance under an agreement binding it. The related R&D-entity subcontract arrangements excluded by subsection (2) must not apply. Refer the full agreements and benefit/IP evidence under R-AU-RD-1 and R-AU-RD-5.

Physical overseas work remains R-AU-RD-4. Verify the finding, significant scientific link to Australian core activities, statutory reason it cannot be conducted in Australia/external territories, and the overseas-versus-related-Australian expenditure condition. Do not infer entitlement from registration, a foreign invoice or a domestic foreign-beneficiary agreement. See [ATO overseas conditions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/amounts-you-can-claim/expenditure-you-can-claim).

#### Rule 3 -- Core R&D activities [s 355-25](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-25)

Core R&D activities are experimental activities whose outcome cannot be known or determined in advance from current knowledge, information or experience, but can only be determined through a systematic progression of work based on established science, proceeding from hypothesis to experiment, observation and evaluation and logical conclusions. They must be conducted for the purpose of generating new knowledge, including new or improved materials, products, devices, processes or services. Preserve all limbs and apply the exclusions in Rule 6. Commercial risk or difficulty is not itself scientific uncertainty. The competent-professional technical judgement belongs with the relevant scientist/engineer and R&D adviser; this guide does not classify a client's activities (R-AU-RD-1).

#### Rule 4 -- Supporting R&D activities [s 355-30](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-30)

Ordinary supporting activities are directly related to core R&D activities. Under subsection (2), an activity referred to in s 355-25(2), producing goods/services or directly related to producing them must also be undertaken for the dominant purpose of supporting core R&D. Ordinary supporting activities need the corresponding eligible core activity; a broad link to a commercial project is insufficient.

Apply the special gambling and tobacco/vaping/nicotine subsections (3) and (4) separately. They disapply subsection (2) for the specified activities and allow supporting status only if the corresponding harm-minimisation purpose condition in s 355-25(3) or (4) is met. A generic dominant-purpose argument cannot bypass those conditions. Refer classification under R-AU-RD-1.

#### Rule 5 -- Offset rates, exempt control and intensity [s 355-100](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100)

For 2026-27, aggregated turnover below $20m gives the refundable company-tax-rate-plus-18.5-point offset only if item 2 does not apply. At any time during the income year, test whether an exempt entity or combination of exempt entities would control the R&D entity under s 328-125 with 50% substituted for 40% and subsection 328-125(6) ignored. This is distinct from ordinary turnover grouping and is not a year-end-only ownership check.

Otherwise the offset is non-refundable: the company tax rate applies to eligible deductions, increased by 8.5 percentage points on deductions up to 2% of statutory total expenses and by 16.5 points above that band. For either offset type, apply the premium calculation only up to $150m of notional deductions; excess gets the bare company rate. The historical $100m cap applied to income years commencing from 1 July 2014 and before 1 July 2021, not all pre-2021 years. See [ATO rates and historical cap](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/refundable-and-non-refundable-offsets).

At an independently established 25% company rate the refundable rate is 43.5%; at 30% it is 48.5%. Company tax-rate eligibility is a separate question: use [au-company-tax](au-company-tax.md), including its base-rate passive-income and turnover tests, rather than infer 25% from R&D turnover alone.

R&D intensity uses notional deductions divided by [s 355-115 total expenses](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-115). Start with expenses under applicable accounting principles, or commercially accepted accounting principles if none apply. Add eligible s 355-100(1) deductions not already included. Prevent counting an amount twice, including where accounting expense and notional deduction arise in different years. A tax-return expenses total or cash expenditure alone is not automatically the denominator. Keep the reconciliation.

#### Rule 6 -- Excluded core activities [s 355-25(2)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-25)

The following cannot be core activities: market research/testing/development or sales promotion, including consumer surveys; prospecting, exploring or drilling for minerals or petroleum to discover, locate or determine the size or quality of deposits; management studies or efficiency surveys; research in social sciences, arts or humanities; commercial, legal or administrative aspects of patenting, licensing or other IP activities; statutory-requirement/standards compliance including routine testing and analysis; reproduction of a commercial product or process from physical examination, plans, blueprints, detailed specifications or public information; and software developed, modified or customised for the dominant purpose of internal administration of the claimant, connected entities, its affiliates or entities of which it is an affiliate. Some excluded-core activities can meet the ordinary supporting tests, subject to Rule 4's special regimes.

For income years starting on or after 1 July 2025, gambling, gambling services and gambling-like activities fail unless conducted solely to generate new knowledge about minimising harm from them. Tobacco, tobacco products/accessories, vaping goods, tobacco extract, goods made using tobacco/extract and nicotine goods for human use, except food whose only nicotine is naturally occurring, fail unless conducted solely to generate new knowledge about therapeutic use of therapeutic goods to minimise harm from those things or about ceasing nicotine ingestion/transfer. General harm-minimisation research is not enough for this tobacco limb. These tests also govern the specified supporting activities under s 355-30(3)-(4).

[Act No. 58 of 2026, s 2 and Schedule 4](https://www.legislation.gov.au/C2026A00058/asmade/text) commenced this amendment on 1 July 2026 but applies it to income years starting on or after 1 July 2025. Its application provision also displaces an earlier DISR finding to the extent it would require treating an excluded activity as eligible. Do not confuse assent, commencement and the earlier application date.

#### Rule 7 -- Registration and the 10-month deadline [DISR](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/apply-for-the-randd-tax-incentive)

Register activities with DISR for each income year before claiming the offset. The normal deadline is 10 months after year end, for example 30 April 2027 for a 30 June 2026 year end. Use the correct IISA registration number for the activities and income year. For an earlier-year associate amount claimed on payment, preserve its original activity-year registration and verify the schedule's payment-year requirements. Registration does not certify activity eligibility.

If the deadline cannot be met or has passed, refer the entity to DISR or its R&D adviser to request an extension through the R&DTI customer portal, with reasons and supporting evidence.

DISR states that a request for 14 days or less made before the statutory deadline will be approved; the application must explain why extra time is needed and why that period is sufficient. Longer requests, or requests made after the deadline, are considered case by case with supporting reasons and evidence. An application remains required.

Extensions generally cannot exceed 92 days after the statutory deadline; a related pending decision is the exception. Confirm valid registration within the statutory or approved extended period before claiming. A late application alone does not establish entitlement.

DISR cannot extend the application deadline for an advance or overseas finding or accept those applications late. See [DISR: request an extension or variation](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/request-an-extension-or-variation) and Part 3 of the Industry Research and Development Decision-making Principles 2022.

#### Rule 8 -- The minimum spend and RSP/CRC exceptions [s 355-100(2)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100)

Normally total eligible notional deductions must be at least $20,000. Below that amount, calculate the offset only on eligible expenditure incurred to a non-associate RSP for services within a research field for which it is registered, and eligible monetary CRC contributions. The RSP must not be an associate of the claimant or relevant R&D partnership. Registration of one provider does not make other expenditure eligible. Check field and period, activity eligibility and all other conditions.

Thus $18,000 paid to an associated RSP gives no $7,830 offset at an assumed 43.5% if no other exception applies. Ordinary non-RSP contractors can qualify when the normal threshold is met. See [ATO eligibility](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/eligibility-for-the-r-d-tax-incentive).

#### Rule 9 -- Aggregated turnover grouping [ATO grouping](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/grouping-for-aggregated-turnover-purposes)

Include the claimant's annual turnover plus connected and affiliated entities' annual turnover for the relevant periods of connection/affiliation, including Australian and foreign entities, excluding dealings between them. Annual turnover is worldwide ordinary business income excluding GST; part-year businesses need the reasonable full-year estimate described in the ATO guidance. Ordinary connection/control rules use their own thresholds, discretion and indirect-control exceptions; the modified exempt-control test in Rule 5 is different. Substituted periods, discretionary trusts, foreign structures and grouping/Part IVA questions require R-AU-RD-5 review. Compute the group before selecting refundability.

#### Rule 10 -- The notional deduction base [ATO expenditure](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/amounts-you-can-claim/expenditure-you-can-claim)

Under [s 355-205](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-205), claim eligible expenditure incurred on registered activities meeting s 355-210, subject to exclusions and integrity rules. Registration may be confirmed later but must relate to the activities/year concerned; do not move the expenditure year simply because registration is later. Services provided over a period require the prepayment rules before selecting the deductible year. Direct linkage and reasonable documented apportionment are required for overheads; tax-return and registration-preparation fees are not R&D activity expenditure merely because they relate to a claim.

[Section 355-225](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-225) excludes interest and expenditure included in a tangible depreciating asset's cost, with a potential separate decline-in-value route. It also excludes building/part/extension/alteration/improvement expenditure and the specified acquisition or right-to-use core technology expenditure. Do not infer every intangible or other capital work has the same treatment. Rule 13 supplies asset controls. Non-arm's-length or associate expenditure also has a market-value ceiling; an invoice is not conclusive.

For associates, confirm actual or constructive payment, including application or dealing on the associate's behalf or as directed. Amounts incurred and paid in the same year can qualify under s 355-205. Under [s 355-480](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-480), an otherwise eligible earlier-year amount can qualify when paid only to the extent the earlier ordinary-deduction or other tax-offset entitlement exists and neither was taken by lodgement of the return for the most recent year before payment. That earlier entitlement then ceases for the remaining amount. Apply this amount by amount: a prior partial deduction prevents R&D treatment for that portion, not automatically for the whole invoice. The ordinary deduction choice cannot be reversed by amendment to obtain a later R&D benefit. Never claim both. Preserve earlier activity-year registration and confirm the payment-year schedule identifiers; payment is not a new activity.

Apply [s 355-405](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-405) at each incurrence point. Where the claimant or an associate has received or could reasonably expect consideration as a direct or indirect result of that expenditure, regardless of R&D results, deny the expenditure if that consideration equals or exceeds it; otherwise reduce it by that consideration. Consider relevant earlier facts and likely later events. Monetary and non-monetary benefits can count; funding alone does not establish the two tests. The section excepts expenditure on the s 355-210(1)(b)/(c) routes. See [TR 2021/5, paragraphs 4-43](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20215/NAT/ATO/00001); passing this integrity rule does not establish other eligibility.

[Section 355-415](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-415) reduces expenditure deductions for relevant group mark-ups: examine connected entities and either affiliate direction at the statutory times, amounts derived for goods/services less corresponding actual costs, previous reductions and the order of reduction against current then earlier-year associate deductions. Do not claim an internal profit margin as R&D expenditure without applying this rule. [TA 2023/4](https://www.ato.gov.au/law/view/document?DocID=TPA/TA20234/NAT/ATO/00001) also flags actual incurrence/payment, beneficiary/IP, market value, mark-ups, at-risk and Part IVA risks in associate service arrangements.

#### Rule 11 -- Clawback and catch-up adjustments [ATO guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/clawback-of-r-d-tax-incentive-offset-and-catch-up-deductions)

A qualifying clawback adds assessable income to recover the incentive premium; it does not directly reduce the offset or simply net the grant off. Apply the at-risk and expenditure tests first. Under [s 355-440](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-440), an Australian government agency or state/territory body recoupment received or entitled to by the claimant, a connected entity or an affiliate in either direction can trigger an adjustment for R&D deductions/asset decline used for offsets. CRC-program recoupments are excluded from this trigger. Account for repayments and, for project funding, the cap based on net recoupment multiplied by R&D expenditure divided by project expenditure. Grant assessability is a separate question.

Under [s 355-445](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-445), eligible feedstock input/energy/related asset-decline expenditure used in a claimed offset can trigger an adjustment when the claimant or relevant related entity supplies output or applies it to own use, except own use for further transformation/processing for supply. The clawback amount is the lesser of attributable eligible amounts and statutory feedstock revenue. Subsection (2) does not apply if the output becomes, or is transformed into, a feedstock input, or if it already applied to that output at an earlier time in the present year or an earlier year. Market value, cost apportionment and related supplies can matter. Track the actual output and year; do not substitute all sale proceeds or all project expenditure automatically.

For each offset year, [s 355-450](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-450) includes (starting offset minus adjusted offset minus deduction amount) divided by the present-year company tax rate. Adjusted offset is recomputed with the attributable clawback removed; deduction amount uses that clawback multiplied by the offset-year company tax rate. Prior clawback and catch-up amounts adjust the starting base under subsection (2). Example 5 uses equal rates in both years; do not generalise that shortcut to a rate change or an intensity/cap crossing.

An assessable R&D-asset balancing adjustment can also trigger clawback; a deductible event may instead give an additional catch-up deduction. Mixed use, previous offsets and modified Division 40 require separate calculation, not another R&D offset for the catch-up amount. From 1 July 2021 Part IVA also extends to R&D offset schemes, including obtaining refundability instead of a non-refundable benefit; refer structuring.

#### Rule 12 -- Amendments, objections and findings [ATO instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/correcting-mistakes-and-disputing-decisions)

R&D amendments generally have a 4-year period; a 2-year period may apply to 2021-22 and earlier assessments. Special rules give effect to timely DISR findings on registration, overseas activities/core technology and internal-review, ART or court decisions outside ordinary windows. Check the actual assessment, notice, year and statutory route rather than use one universal date.

To amend, complete the amended year-specific R&D schedule and send a letter specifying company-return labels and changes to the ATO address in the current instructions. For an original assessment the ATO gives a 4-year objection period from notice, with specified earlier-year small/medium-business exceptions. For an amended assessment the limit is the later of 60 days from the amended notice and the applicable period from the original notice. Nil-assessment objections are restricted; refund amounts can have their own objection route, and a carried-forward non-refundable R&D offset generally waits until first applied. Obtain advice for a disputed deadline or review.

A finding removing entitlement should prompt self-amendment. The ATO says it will not commence an audit for 28 days to allow that request; this is a grace period, not a promise of an audit exactly on day 28 or an extension of every statutory deadline. Findings take immediate effect despite a review/ART/court challenge. Qualify the usual binding-finding rule for the [2026 Schedule 4 exclusion override](https://www.legislation.gov.au/C2026A00058/asmade/text) described in Rule 6.

#### Rule 13 -- Assets and small business concessions [ss 355-305 and 355-310](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-305)

An R&D entity may separately qualify for small business concessions, with their own eligibility and asset rules. Do not treat an instant asset write-off as a notional R&D deduction. Tangible asset cost is excluded from the expenditure route; eligible decline in value may qualify where the entity holds and uses the asset for registered qualifying activities and meets modified Division 40.

[Section 355-310](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-310) substitutes qualifying R&D use for taxable purpose, disregards simplified depreciation and low-value pooling for the notional calculation and separately excludes specified building works. Other capital works may qualify; this tangible-asset route does not decide intangible treatment. Use the same depreciation method where the statute requires consistency, and document R&D/non-R&D use.

Check prior years first: s 355-305 prevents this route where an amount for the asset is deductible for an earlier year under Subdivision 328-D or the specified low-value-pool route. Under [s 355-715](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-715), do not also claim the R&D-attributable decline under another deduction or offset, subject to its balancing exceptions. Assess any ordinary non-R&D portion separately. Refer mixed-use assets, prior immediate deductions and existing pools.

Use [au-company-tax](au-company-tax.md) for small business depreciation eligibility and the current write-off amount; the R&DTI's $20m/refundability test is distinct. [Tax Reform No. 2 Act 2026, s 2 and Schedule 2](https://www.legislation.gov.au/C2026A00071/asmade/text) enacted the $20,000 threshold amendment with 1 October 2026 commencement and distinct application dates: first taxable-purpose use/installation and relevant second-element costs from 1 July 2026, and the pool-balance amendment for income years ending on or after that date. Schedule 1 concerns loss carry-back. None of these amendments displaces the R&D restrictions above; do not infer an unrestricted same-year mixed-use claim or describe a no-sunset substitution as an unconditional permanent entitlement.

### Section 6 -- Tier 2 catalogue

#### T2-1 -- Core vs ordinary business activity

- **Core vs ordinary business activity**: **Trigger:** claim includes routine, business-as-usual, or commercial-risk activities. **Issue:** TA 2017/3 targets claims for ordinary business activities dressed as R&D (no scientific uncertainty, no hypothesis-driven experiment, no new knowledge). **Action:** refuse classification (R-AU-RD-1); document; escalate.  _(TA 2017/3)_

#### T2-2 -- Software development claims

- **Software development claims**: **Trigger:** software development claimed as core R&D. **Issue:** internal-administration software for the entity, connected entities or affiliates in either direction is excluded from core; even non-internal-admin software must still clear the knowledge threshold (outcome not knowable in advance). Much routine development fails. **Action:** test dominant purpose and the knowledge threshold; escalate (R-AU-RD-1).

#### T2-3 -- R&D delivered by associates / overseas related entities

**Trigger:** associate-delivered R&D, related funding, set-offs, share issues or physical overseas work. **Issue:** [TA 2023/4](https://www.ato.gov.au/law/view/document?DocID=TPA/TA20234/NAT/ATO/00001) identifies possible failures of actual incurrence/payment, claimant benefit/IP, market value, group mark-ups, at-risk and Part IVA conditions. A journal entry or circular funds do not establish payment. Physical overseas work needs the relevant finding and own-benefit conditions; Australian work for qualifying foreign beneficiaries has the separate Rule 2 routes. **Action:** trace real obligations, funds, agreements, prior claims and findings, document each statutory test and refer R-AU-RD-4/R-AU-RD-5.

#### T2-4 -- Overhead apportionment

- **Overhead apportionment**: **Trigger:** rent, utilities, admin overheads apportioned to R&D. **Issue:** apportionment must reflect the actual extent of R&D use on a reasonable, documented basis; salary-based ratios are appropriate for personnel but not necessarily for utilities. **Action:** sight the documented methodology; flag unreasonable apportionment.

#### T2-5 -- Group aggregation and Part IVA

- **Group aggregation and Part IVA**: **Trigger:** aggregated turnover near the $20m threshold, or group structures that appear to engineer a refundable rather than non-refundable outcome. **Issue:** connected/affiliate turnover must be aggregated; from 1 July 2021 Part IVA can cancel an offset (including a refundability benefit) where the dominant purpose was to obtain it. **Action:** compute group turnover properly; escalate structuring (R-AU-RD-5).

#### T2-6 -- At-risk expenditure

**Trigger:** guaranteed returns, indemnities, subsidies or commercial contracts. **Issue:** [TR 2021/5 paragraphs 4-43](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20215/NAT/ATO/00001) applies the nexus-to-expenditure and regardless-of-results tests at each incurrence, including qualifying parts of monetary/non-monetary consideration. Funding alone does not prove those tests. Rule 10 retains the statutory foreign-route exceptions. **Action:** examine actual and likely arrangements and timing, quantify any denied portion and refer.

### Section 8 -- Reading guide [ATO steps](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset)

1. Registration first: confirm valid DISR registration for the income year within the statutory or approved extended period (Rule 7) before claiming.
2. Entity test second: confirm the eligible body corporate and capacity. Sole traders and ordinary trusts do not qualify; public trading trust corporate trustees and eligible corporate partners have the specific routes in Rule 2.
3. Activity test third: core activities must clear all three limbs (unknowable outcome, systematic progression, new knowledge) -- and that is a technical judgement this skill refuses to make.
4. Rate test fourth: aggregated turnover and the separate at-any-time modified exempt-control test choose refundability; statutory total expenses set the intensity bands.
5. Expenditure test fifth: apply registration, beneficiary, at-risk, market-value and group mark-up controls. Associate amounts require payment and prior-claim checks; eligible tangible asset decline has its separate conditions.
6. Clawback always: screen grants, feedstock outputs and asset events against their conditions, offset years and prior adjustments; calculate assessable income or catch-up deductions separately.


#### Key figures

**Key figures**

| Item | Amount and conditions | Income period | Official source |
| --- | --- | --- | --- |
| Refundable offset | Below $20m and no modified exempt control at any time: company rate plus 18.5 points; at an established 25% rate, 43.5% | 2026-27 | [Official text](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) |
| Non-refundable offset | At least $20m or exempt controlled: company rate plus 8.5 points up to 2% of statutory total expenses, plus 16.5 points above, subject to cap | 2026-27 | [Official text](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) |
| R&D intensity | Notional deductions divided by s 355-115 total expenses, with accounting/notional and cross-year duplication removed | 2026-27 | [Official text](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-115) |
| Expenditure cap | $150m premium base; company rate alone on excess, either offset type | 2026-27 | [Official text](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) |
| Minimum deduction | $20,000 normally; below it only the qualifying RSP/monetary CRC amounts in Rule 8 | 2026-27 | [Official text](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) |
| Registration deadline | Normally 10 months after activity year end; approved extensions as Rule 7, registration before claim | Each activity year | [Official text](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/request-an-extension-or-variation) |
| Amendment period | Generally 4 years, earlier-year/special finding/review exceptions and distinct objection limits in Rule 12 | R&D claims | [Official text](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/correcting-mistakes-and-disputing-decisions) |
| Tobacco/gambling | Special exclusions and sole-purpose exceptions in Rule 6, including supporting activities | Years starting on/after 1 July 2025 | [Official text](https://www.legislation.gov.au/C2026A00058/asmade/text) |
| Announced reform | Not law: all 7 proposals in Scope, including 4.5 points/1.5%, first 10 years, $50m turnover, $50,000 minimum and $200m cap | Proposed 1 July 2028 | [Official text](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/tax-reform-better-targeting-the-research-and-development-tax-incentive) |

## Worked cases

All 2026-27 synthetic cases stipulate eligible R&D entities, substantively eligible activities, valid relevant DISR registration and all expenditure/place/beneficiary tests. Company rates, exempt control, total expenses and tax positions are supplied facts. Offsets replace the related ordinary deduction. Arithmetic cannot establish those facts. Sources: [s 355-100](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100), [s 355-115](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-115) and [ATO calculation steps](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset).

### Section 4 -- Worked examples

#### Example 1 -- Small company refundable offset

Innovate Pty Ltd (2026-27) has aggregated turnover $4.2m, no exempt control at any time, an established 25% company rate and $300,000 eligible notional deductions. Taxable income is $150,000 after adding back R&D expenses and all other tax adjustments. There are no other offsets, PAYG/withholding credits, tax debts, refund retention or clawback. The refundable rate is 25% + 18.5% = 43.5%, giving $130,500 offset. Basic tax is $37,500; tax payable becomes zero and the refundable excess is $93,000. The subtraction balance is minus $93,000, not a negative assessed tax liability. Cash equals that excess only under the stated assumptions; apply Section 2's refund/franking rules to an actual claim.

```oa-check
name: Innovate refundable excess, 2026-27
inputs:
  notional_deductions: 300000
  taxable_income: 150000
  company_rate: 0.25
  premium: 0.185
steps:
  - offset_rate: company_rate + premium
  - rd_offset: notional_deductions * offset_rate
  - basic_tax: taxable_income * company_rate
  - offset_used: min(basic_tax, rd_offset)
  - tax_payable: max(0, basic_tax - rd_offset)
  - refundable_excess: max(0, rd_offset - basic_tax)
expected:
  offset_rate: 0.435
  rd_offset: 130500
  basic_tax: 37500
  offset_used: 37500
  tax_payable: 0
  refundable_excess: 93000
```

#### Example 2 -- Loss-making small company

StartUp Co (2026-27) has $1.8m aggregated turnover, no exempt control at any time, an established 25% rate and $250,000 eligible notional deductions. It remains in a tax loss after adding back the R&D amounts and completing the tax reconciliation. With no other offsets, credits, debts or retention, basic tax is zero and all $108,750 of its 43.5% offset is refundable. A book loss before addbacks would not establish this result. The notional deduction is not also deducted ordinarily. See [ATO refundable offsets](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/refundable-and-non-refundable-offsets).

```oa-check
name: StartUp refundable offset after tax-loss reconciliation, 2026-27
inputs:
  notional_deductions: 250000
  company_rate: 0.25
  premium: 0.185
  basic_tax: 0
steps:
  - rd_offset: notional_deductions * (company_rate + premium)
  - tax_payable: max(0, basic_tax - rd_offset)
  - refundable_excess: max(0, rd_offset - basic_tax)
expected:
  rd_offset: 108750
  tax_payable: 0
  refundable_excess: 108750
```

#### Example 3 -- Non-refundable intensity tiers

BigCo Ltd (2026-27) has $80m aggregated turnover, a 30% rate, no exempt control and $8m eligible notional deductions. Its reconciled s 355-115 total expenses are $200m, including the deductions once. Intensity is 4%. The first $4m, being 2% of total expenses, receives 38.5%; the remaining $4m receives 46.5%. The offset is $1,540,000 + $1,860,000 = $3,400,000, non-refundable. This is an offset calculation; the actual amount used and any carry-forward need the company's tax position and carry-forward tests.

```oa-check
name: BigCo statutory expense intensity, 2026-27
inputs:
  notional_deductions: 8000000
  total_expenses: 200000000
  company_rate: 0.30
  lower_premium: 0.085
  upper_premium: 0.165
  intensity_boundary: 0.02
steps:
  - intensity: notional_deductions / total_expenses
  - lower_deductions: min(notional_deductions, total_expenses * intensity_boundary)
  - upper_deductions: notional_deductions - lower_deductions
  - lower_offset: lower_deductions * (company_rate + lower_premium)
  - upper_offset: upper_deductions * (company_rate + upper_premium)
  - rd_offset: lower_offset + upper_offset
expected:
  intensity: 0.04
  lower_deductions: 4000000
  upper_deductions: 4000000
  lower_offset: 1540000
  upper_offset: 1860000
  rd_offset: 3400000
```

#### Example 4 -- Expenditure cap

Company XYZ (2026-27) has $600m aggregated turnover, a 30% rate, $250m of reconciled s 355-115 total expenses and $170m eligible notional deductions. The lower band is $5m; the higher band below the cap is $145m; the $20m above the cap receives only 30%. The non-refundable offset is $1,925,000 + $67,425,000 + $6,000,000 = $75,350,000. No premium is given on the excess. Use/carry-forward remains conditional, as in Example 3.

```oa-check
name: XYZ capped non-refundable offset, 2026-27
inputs:
  notional_deductions: 170000000
  total_expenses: 250000000
  company_rate: 0.30
  premium_cap: 150000000
  intensity_boundary: 0.02
  lower_premium: 0.085
  upper_premium: 0.165
steps:
  - premium_deductions: min(notional_deductions, premium_cap)
  - lower_deductions: min(premium_deductions, total_expenses * intensity_boundary)
  - upper_deductions: premium_deductions - lower_deductions
  - excess_deductions: max(0, notional_deductions - premium_cap)
  - lower_offset: lower_deductions * (company_rate + lower_premium)
  - upper_offset: upper_deductions * (company_rate + upper_premium)
  - excess_offset: excess_deductions * company_rate
  - rd_offset: lower_offset + upper_offset + excess_offset
expected:
  premium_deductions: 150000000
  lower_deductions: 5000000
  upper_deductions: 145000000
  excess_deductions: 20000000
  lower_offset: 1925000
  upper_offset: 67425000
  excess_offset: 6000000
  rd_offset: 75350000
```

#### Example 5 -- Historical ATO feedstock clawback

This retains the ATO's Landscape Supplies Pty Ltd example for 2021-22. Aggregated turnover is $15m, the company tax rate 25% and refundable rate 43.5%. There are $22,000 notional deductions including $10,000 feedstock expenditure, all output is sold for $9,000 in that year and there are no other clawback amounts. The lesser amount is $9,000. Starting offset $9,570 minus adjusted offset $5,655 minus deduction equivalent $2,250 gives $1,665 premium, grossed up at 25% to $6,660 assessable income. The adjusted calculation is the statutory clawback counterfactual, not a new independent $13,000 claim to reject under the minimum-spend test. Sources: [s 355-450](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-450) and [ATO's complete Landscape Supplies example](https://www.ato.gov.au/api/public/content/0-814e20bf-be69-4e69-b755-b50eef6101a6).

```oa-check
name: Landscape Supplies published feedstock example, 2021-22
inputs:
  original_deductions: 22000
  feedstock_expenditure: 10000
  feedstock_revenue: 9000
  offset_rate: 0.435
  offset_year_company_rate: 0.25
  present_year_company_rate: 0.25
steps:
  - clawback_amount: min(feedstock_expenditure, feedstock_revenue)
  - starting_offset: original_deductions * offset_rate
  - adjusted_offset: (original_deductions - clawback_amount) * offset_rate
  - deduction_amount: clawback_amount * offset_year_company_rate
  - premium_recovered: starting_offset - adjusted_offset - deduction_amount
  - assessable_income: premium_recovered / present_year_company_rate
expected:
  clawback_amount: 9000
  starting_offset: 9570
  adjusted_offset: 5655
  deduction_amount: 2250
  premium_recovered: 1665
  assessable_income: 6660
```

#### Example 6 -- Decision: ordinary deduction now or R&D offset on later payment

Synthetic comparison under [s 355-480](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-480), made before lodging the 2025-26 return and before payment in 2026-27. A company has incurred $100,000 eligible associate expenditure in 2025-26 but has not paid it. An ordinary deduction is otherwise available in 2025-26 and would reduce taxable income taxed at 25%. All relevant registration and activity conditions are established, including the ongoing activity years; payment in 2026-27 and the 43.5% refundable-rate conditions are stipulated for the deferred route. No prior deduction or other offset has been taken, no clawback arises and there are no other credits/debts or refund retention. The example does not resolve a case where only earlier-year registration exists; confirm that schedule mapping with the adviser.

Route A takes the otherwise-available ordinary deduction: tax falls $25,000 now and no later R&D claim is available for that amount. Route B takes neither the earlier deduction nor another offset by the statutory cut-off: no tax saving now, then a $43,500 R&D offset on eligible payment in 2026-27. The nominal additional benefit is $18,500 one year later. With a purely illustrative 10% one-year discount assumption, Route B's present value is $39,545.45, exceeding Route A by $14,545.45. Under these facts and this discount assumption Route B has the larger present value. Route A delivers the earlier tax saving, whilst Route B depends on future payment/eligibility and funding. Do not treat a future offset as current cash or claim both. The ordinary-deduction choice cannot later be reversed to obtain R&D treatment. Partial earlier claims require amount-by-amount separation.

```oa-check
name: Associate ordinary-versus-deferred choice, 2025-26 to 2026-27
inputs:
  associate_amount: 100000
  current_company_rate: 0.25
  payment_year_company_rate: 0.25
  rd_premium: 0.185
  one_year_discount: 0.10
steps:
  - route_a_current_tax_saving: associate_amount * current_company_rate
  - route_a_later_rd_offset: 0
  - route_b_current_tax_saving: 0
  - route_b_later_rd_offset: associate_amount * (payment_year_company_rate + rd_premium)
  - nominal_later_advantage: route_b_later_rd_offset - route_a_current_tax_saving
  - route_b_present_value: route_b_later_rd_offset / (1 + one_year_discount)
  - present_value_advantage: route_b_present_value - route_a_current_tax_saving
expected:
  route_a_current_tax_saving: 25000
  route_a_later_rd_offset: 0
  route_b_current_tax_saving: 0
  route_b_later_rd_offset: 43500
  nominal_later_advantage: 18500
  route_b_present_value: 39545.45
  present_value_advantage: 14545.45
```

#### Example 7 -- Partial at-risk reduction

A synthetic domestic own-benefit 2026-27 case follows [TR 2021/5 paragraphs 58-63](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20215/NAT/ATO/00001) and [s 355-405](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-405). At incurrence of $100,000, the entity reasonably expects $30,000 under a government scheme solely because it incurs qualifying research expenditure, regardless of research results. Both tests are stipulated and neither foreign-route exception applies. Deny $30,000, leaving $70,000 potential notional deductions. Only after all other eligibility tests, a stipulated 25% company rate and refundable conditions give $30,450 offset. Apply this incurrence-time test before considering clawback. Grant assessability and any separately qualifying recoupment remain separate questions; no full net-tax/refund result is shown.

```oa-check
name: Partial at-risk exclusion before offset, 2026-27
inputs:
  incurred_expenditure: 100000
  relevant_consideration: 30000
  company_rate: 0.25
  refundable_premium: 0.185
steps:
  - denied_expenditure: min(incurred_expenditure, relevant_consideration)
  - remaining_notional_deductions: max(0, incurred_expenditure - relevant_consideration)
  - rd_offset: remaining_notional_deductions * (company_rate + refundable_premium)
expected:
  denied_expenditure: 30000
  remaining_notional_deductions: 70000
  rd_offset: 30450
```

#### Example 8 -- Below and at the minimum-spend boundary

For 2026-27, a synthetic eligible refundable claimant at an established 43.5% rate has $18,000 total deductions: $10,000 otherwise-eligible non-associate RSP expenditure within its registered research field and $8,000 internal expenditure. Below $20,000, only the $10,000 qualifies, so the offset is $4,350. If that provider is an associate and no CRC exception applies, the below-threshold offset is zero. In the separately stipulated at-threshold scenario, eligible deductions total exactly $20,000 and all qualify, giving $8,700. Sources: [s 355-100(2)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) and Rule 8. There is no cash/refund conclusion without the tax reconciliation.

```oa-check
name: Expenditure-specific RSP exception and exact threshold, 2026-27
inputs:
  low_total: 18000
  qualifying_non_associate_rsp: 10000
  low_total_if_associate_eligible: 0
  exact_threshold_total: 20000
  offset_rate: 0.435
steps:
  - excluded_internal_amount: low_total - qualifying_non_associate_rsp
  - low_total_offset: qualifying_non_associate_rsp * offset_rate
  - associated_provider_offset: low_total_if_associate_eligible * offset_rate
  - exact_threshold_offset: exact_threshold_total * offset_rate
expected:
  excluded_internal_amount: 8000
  low_total_offset: 4350
  associated_provider_offset: 0
  exact_threshold_offset: 8700
```

## When to refuse or refer

### Section 7 -- Refusal catalogue

These are deliberate refusal-and-escalate zones. Do NOT answer them from this skill.

- **R-AU-RD-1**: Whether a specific activity qualifies as a core or supporting R&D activity  ("Whether an activity is R&D is a technical/engineering judgement about scientific uncertainty and the knowledge threshold under s 355-25, not an accounting judgement. This needs a competent professional in the field and, for certainty, an AusIndustry/DISR advance finding. I can help organise the project documentation but cannot classify the activity.")  _(s 355-25)_
- **R-AU-RD-2**: Preparing or lodging the DISR registration application  ("Registration is a self-assessed application to AusIndustry/DISR describing the activities against the legislative criteria. I can't draft or lodge it. Refer to AusIndustry (13 28 46) or a registered R&D tax adviser. The normal deadline is 10 months after year end; assess the Rule 7 extension route if late.")
- **R-AU-RD-3**: Advance findings, overseas findings, or binding certainty on eligibility  ("Only DISR can make an advance finding (activity eligibility) or an overseas finding (s 28D IR&D Act). These are binding decisions for your specific facts. Refer to AusIndustry; I can help assemble the supporting records.")  _(s 28D IR&D Act)_
- **R-AU-RD-4**: Overseas R&D activities  ("Activities conducted overseas are claimable only with a positive DISR overseas finding, and only where conducted for the claimant (not a foreign related entity). This needs the finding in place before claiming. Refer to AusIndustry.")
- **R-AU-RD-5**: Aggregated expenditure/turnover across connected or affiliated groups  ("Aggregated turnover across connected and affiliated entities (including foreign ones) determines refundable vs non-refundable, and group structuring can attract Part IVA. Compute the group position with the client's adviser; I can prepare the underlying turnover figures per entity.")


#### Prohibitions

- NEVER treat the R&DTI as a grant -- it is a tax offset claimed in the company return
- NEVER classify an activity as core/supporting R&D -- that is a technical/engineering judgement (R-AU-RD-1); escalate
- NEVER prepare or lodge the DISR registration application -- refer to AusIndustry (R-AU-RD-2)
- NEVER advise on advance or overseas findings -- DISR only (R-AU-RD-3, R-AU-RD-4)
- NEVER compute an actual claim without valid DISR registration within the statutory or approved extended period for the relevant activity year, including earlier-year associate conditions and schedule verification
- NEVER choose refundable vs non-refundable without computing aggregated turnover across connected/affiliated entities (R-AU-RD-5)
- NEVER claim an associate amount before payment or for a portion already deducted or given another tax offset; apply the latest-prepayment-return cut-off and irreversible-choice rule
- NEVER claim tangible depreciating asset cost under the R&D expenditure route; test eligible decline in value, prior deductions/pools and other capital/intangible treatment under Rule 13
- NEVER ignore a feedstock, recoupment or balancing-adjustment clawback
- NEVER present figures as definitive


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

For the platform version, visit [openaccountants.com](https://www.openaccountants.com). Log in to check available updates or request a professional review from a licensed accountant. Check the sources and applicable year before relying on any version.

> Contributed by Ryan Duguid.



## Filing and payment

### Preparation and claim workflow [ATO steps](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset)

1. Establish the entity/capacity, period and Rule 2 activity route, then obtain the final registration and any required findings. The authorised applicant/adviser uses the [DISR R&DTI customer portal](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/apply-for-the-randd-tax-incentive), with role-based authorisation, activity records and the applicable 10-month/approved-extension timetable. This guide does not prepare or lodge that application (R-AU-RD-2), classify activities or obtain findings.
2. Prepare an activity-to-ledger schedule: eligible wages/contracts/overheads, associate payment/prior-claim roll-forward, asset decline and excluded amounts. Reconcile book R&D expense back into taxable income where required; a notional deduction is not a second ordinary deduction. Keep funding, beneficiary, market-value, group mark-up and at-risk evidence.
3. Compute group turnover, modified exempt control, the independently established company rate and s 355-115 expenses. Apply the R&D schedule to eligible amounts, threshold, intensity and cap. Compute feedstock, recoupment, balancing/catch-up amounts separately and reconcile them into the return.
4. Use the [ATO R&D calculator and company-return workflow](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset) with the correct income-year form and DISR number. The completed schedule goes with the company return through the taxpayer's authorised lodgement channel or registered tax agent's software. Do not send a standalone registration form to the ATO as the offset claim.
5. Verify every transfer against the actual year/software instructions and applicable return/payment due date. The 2026 map below is evidence for Company tax return 2026 only. Stop at Needs Input for a 2026-27 return until its current form and software mapping, taxpayer-specific due date and any special earlier-year associate identifiers are confirmed. Do not infer boxes from the latest visible PDF or treat the DISR registration deadline as the company-return due date.
6. After authorised lodgement, retain the receipt, final schedule, registration/findings, calculation and tax reconciliation. Reconcile the assessment, offset use/carry-forward, tax-debt allocation and actual refund. Respond to verification requests; do not recognise an expected offset as an unconditional cash receipt. If an error or adverse finding is discovered, use Rule 12's amended schedule/letter or appropriate objection route and preserve its deadline evidence.

### Dated form map: Company tax return 2026

The official [Research and development tax incentive schedule 2026, NAT 73794-06.2026](https://iorder.com.au/publication/Download.aspx?ProdID=73794-6.2026) was read as native text and visually checked on all 4 pages on 4 November 2026. It instructs attachment to Company tax return 2026. This map does not establish the 2026-27 form or software fields. No live portal submission or software export was tested.

| Schedule area | Fields and transfer shown on the 2026 form | Use |
| --- | --- | --- |
| Header | Original/amended choice, company name, TFN, AusIndustry-IISA number and ABN | Correct entity, period and claim type; use identifiers only in the authorised tax workflow |
| Preliminary calculation | R&D accounting-expenditure addback D transfers to company-return item 7D | Reconcile book expenses before taxable income |
| Part A | Australian-owned/foreign-owned columns; RSP 1A/B, contracts 2C/D, salaries 3E/F, other 4G/H, feedstock 5I/J, paid associates 6K/L, asset decline 7M/N, CRC 9Q/R; totals 10X/Y and 11Z | Classify only after activity-route review; Z = X + Y |
| Part B | Feedstock adjustment B, recoupment M, assessable balancing O, total clawback P and catch-up Q | P transfers to company-return 21W; Q transfers to 21X. Use the statutory calculations, not raw grants/proceeds |
| Part C | E1 prior unpaid/unclaimed, E2 current incurred, E3 otherwise claimed, E4 paid; E = E1 + E2 - E3 - E4 | E4 is included in Part A item 6; preserve amount-by-amount histories |
| Part D | Exempt-control question, turnover threshold, reporting/connected/affiliate entity figures and exclusions; AT = a + b + c + d + e - f | Apply statute, including timing and modified control; the form's short question is not the whole legal test |
| Part E | Company rate R; refundable Z1 from Part A Z and offset U; non-refundable total expenses V, deductions Z2, intensity W, band/excess deductions A1/B1/C1 and offsets A2/B2/C2, total A | Refundable U transfers to company-return 21U; non-refundable A to 21A |
| Declaration | Required particulars and declaration; separate signature/date where not lodged with company return | Only the authorised taxpayer/agent signs or submits |

A Part B clawback amount goes into additional assessable income; it is distinct from the R&D tax offset. [ATO transparency reporting](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-transparency-reports) uses Part A Z less Part B feedstock B for the published expenditure data. The tax offset or entire grant is not that figure.

## Completion checklist



Before release, reconcile the source ledger, activity registration, group/control workpapers, expense and tax reconciliation, associate history, asset history and each clawback year. Check form-year transfers, taxpayer due dates, assessment/carry-forward/refund movements and review sign-off. Mark unmet items Needs Input and refer; passing the arithmetic cases does not clear those holds.

#### Test suite

**Test 1:** Eligible 25% entity, turnover $4m, no modified exempt control at any time, notional deductions $300,000. -> Offset $130,500 refundable, with cash subject to the tax/credit/debt rules.

**Test 2:** Sole trader spends $80,000 on genuine R&D. -> No R&DTI claim: not an R&D entity.

**Test 3:** Eligible 30% non-refundable entity, statutory s 355-115 total expenses $200m, notional deductions $8m. -> Intensity 4%; offset ($4m x 38.5%) + ($4m x 46.5%) = $3,400,000.

**Test 4:** Notional deductions $170m, statutory total expenses $250m, eligible 30% entity. -> Offset $75,350,000; the $20m above the $150m cap earns only the bare 30%.

**Test 5:** Notional deductions $18,000, no RSP/CRC. -> Below the $20,000 threshold; no claim.

**Test 6:** Software built to run the claimant's own payroll. -> Internal-administration software; excluded from core R&D activities.

**Test 7:** Registration lodged 11 months after year end without an approved extension. -> Late under the normal deadline. Refer for an extension request with reasons and evidence; keep the claim pending until valid registration is confirmed. Approval is not automatic. Apply the 92-day limit and related-pending-decision exception in Rule 7. A late advance or overseas finding application has no extension route.

**Test 8:** Feedstock revenue $9,000, feedstock expenditure $10,000, 43.5% offset, 25% CTR. -> $6,660 added to assessable income (Example 5).

**Test 9:** $100,000 incurred to an associate for R&D, unpaid at year end. No notional R&D deduction until payment. If an ordinary deduction is otherwise available and chosen now, sufficient taxable income at 25% gives a $25,000 current tax reduction. That choice prevents a later R&D claim for the same amount and cannot be reversed to obtain the incentive.

**Test 10:** A $50,000 government grant may trigger recoupment clawback only after the statutory conditions, repayments and project cap are checked. -> Calculate the premium attributable to qualifying offset-year amounts and gross it up at the present-year company rate to assessable income; the premium itself is not the assessable-income amount. The grant is not simply netted off.

## Sources

The dates below describe the stated passages, not full Acts, rulings or a taxpayer-specific legal review. Current statute and current operative guidance govern the calculation. In particular, TR 2013/3 discusses an older feedstock regime and cannot supply the present uniform-clawback formula. The 2026 form map is dated evidence; the 2026-27 form/software mapping remains a hold.

| Source | URL | Read on |
| --- | --- | --- |
| Entitlement, exempt control, premiums and cap | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-100) | 2026-11-04; operative ss 355-100(1)-(3), including both tables and expenditure-specific exceptions |
| Statutory total expenses | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-115) | 2026-11-04; operative accounting/notional expense reconciliation and cross-year no-double-count provisions |
| Core activity and exclusions | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-25) | 2026-11-04; operative core test, exclusions and tobacco/gambling purpose exceptions |
| Supporting activities | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-30) | 2026-11-04; operative ordinary dominant-purpose and special tobacco/gambling subsections |
| Eligible bodies corporate | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-35) | 2026-11-04; operative Australian/foreign residence, permanent-establishment extent and exempt exclusion |
| Current expenditure | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-205) | 2026-11-04; operative incurrence, registration, payment and exception provisions |
| Place and beneficiary | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-210) | 2026-11-04; all operative routes and significant-other-beneficiary exclusion |
| Permanent-establishment exception | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-215) | 2026-11-04; complete operative Australian-location, core/supporting and written-evidence conditions |
| Australian work for foreign corporations | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-220) | 2026-11-04; complete operative relationship, agreement, location and subcontract restrictions |
| Excluded expenditure | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-225) | 2026-11-04; operative tangible asset, building, interest and core-technology restrictions |
| Tangible asset decline | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-305) | 2026-11-04; operative held/use, registration and earlier simplified-depreciation/pooling conditions |
| Modified Division 40 | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-310) | 2026-11-04; operative R&D use, building, pooling and method rules |
| Earlier associate expenditure | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-480) | 2026-11-04; complete operative payment, prior deduction/offset, partial choice and cessation rules |
| No double deduction | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-715) | 2026-11-04; operative exclusion and balancing-exception provisions |
| At-risk integrity rule | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-405) | 2026-11-04; complete operative full/partial reduction, timing and foreign-route exceptions |
| Group mark-ups | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-415) | 2026-11-04; complete operative group timing, cost/margin method, order and earlier-reduction rules |
| Recoupments | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-440) | 2026-11-04; complete operative government/CRC boundary, repayments, project cap and related entities |
| Feedstock trigger and amount | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-445) | 2026-11-04; complete operative supply/own use, further transformation, lesser amount, revenue/apportionment and earlier-trigger provisions |
| Clawback assessable income | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-450) | 2026-11-04; complete operative offset-year/present-year formula and prior-adjustment rules |
| Sole-R&D asset catch-up condition | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-465) | 2026-11-04; complete operative held asset, balancing event, registration and deduction conditions |
| Catch-up deduction | [Official source](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/355-475) | 2026-11-04; complete operative counterfactual offset formula, prior adjustments and non-notional character |
| ATO rates | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/rates-of-r-d-tax-incentive-offset) | 2026-11-04; substantive rate page, premiums, intensity and excess deductions |
| ATO refunds and grouping | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/refundable-and-non-refundable-offsets) | 2026-11-04; full substantive page: aggregation, annual turnover, offset ordering, retention, debt allocation, franking and carry-forward qualifications |
| ATO ordinary grouping | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/grouping-for-aggregated-turnover-purposes) | 2026-11-04; substantive connected/affiliate and exempt-control sections; linked determinations not fully read |
| ATO eligibility | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/eligibility-for-the-r-d-tax-incentive) | 2026-11-04; substantive entity, activity, minimum-spend, expenditure and overseas sections |
| ATO expenditure | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/amounts-you-can-claim/expenditure-you-can-claim) | 2026-11-04; selected direct-linkage, market-value, overhead, overseas, associate payment and asset sections; prepayment rule identified, not a complete prepayment-law review |
| ATO calculation and lodgement | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/steps-for-claiming-r-d-tax-offset) | 2026-11-04; registration, calculation, statutory total-expense adjustment, schedule, DISR number and records passages |
| DISR registration application | [Official source](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/apply-for-the-randd-tax-incentive) | 2026-11-04; public portal authorisation, checklist, guidance and application process; no logged-in submission |
| DISR extensions and variations | [Official source](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/request-an-extension-or-variation) | 2026-11-04; substantive 14-day, 92-day, pending-decision and finding/variation limits; no whole-instrument review |
| ATO clawback overview | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/clawback-of-r-d-tax-incentive-offset-and-catch-up-deductions) | 2026-11-04; substantive recoupment, feedstock, balancing/catch-up and gross-up steps |
| ATO amendments and objections | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/correcting-mistakes-and-disputing-decisions) | 2026-11-04; substantive amended-schedule/letter route, ordinary/special periods, nil assessments and findings/audit grace |
| ATO transparency | [Official source](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-transparency-reports) | 2026-11-04; publication timing, limited fields, amendment treatment, no opt-out and schedule-label definitions |
| Tobacco/gambling amendment | [Official source](https://www.legislation.gov.au/C2026A00058/asmade/text) | 2026-11-04; s 2 commencement and complete Schedule 4/application/finding override; not whole Act |
| Small business depreciation amendment | [Official source](https://www.legislation.gov.au/C2026A00071/asmade/text) | 2026-11-04; independent reader checked s 2 and complete Schedule 2/application/transitions; not whole Act or full Division 328 |
| Announced 2028 reform | [Official source](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/tax-reform-better-targeting-the-research-and-development-tax-incentive) | 2026-11-04; complete announcement, all 7 proposals and explicit not-yet-law qualification |
| TR 2021/5 | [Official source](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20215/NAT/ATO/00001) | 2026-11-04; paragraphs 1-43 and subsidy example paragraphs 58-63; remaining examples not a complete fresh ruling review |
| TA 2017/3 | [Official source](https://www.ato.gov.au/law/view/document?DocID=TPA/TA20173/NAT/ATO/00001) | 2026-11-04; description/background/concerns on ordinary activities, eligibility, expenditure and governance |
| TA 2023/4 | [Official source](https://www.ato.gov.au/law/view/document?DocID=TPA/TA20234/NAT/ATO/00001) | 2026-11-04; overview, arrangement description and concerns through paragraph 11; no universal finding against associate arrangements |
| TR 2013/3, historical context | [Official source](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20133/NAT/ATO/00001) | 2026-11-04; paragraphs 1-9 identify the historical feedstock regime and old rates/one-third formula; those figures are not the current calculation |
| Published Landscape Supplies example | [Official source](https://www.ato.gov.au/api/public/content/0-814e20bf-be69-4e69-b755-b50eef6101a6) | 2026-11-04; selected complete 2021-22 example and offset-order/franking passages from native PDF text; no whole-PDF or visual review |
| Published 2026 schedule | [Official source](https://iorder.com.au/publication/Download.aspx?ProdID=73794-6.2026) | 2026-11-04; native text and visual label/column review of all 4 blank pages; Company tax return 2026 only |

### Retained historical provenance

The original guide recorded a 20 August 2026 primary-source pass, a 31 October 2026 tobacco/gambling Act read, an 11 October 2026 announced-reform check and an 11 September 2026 extension check. These inherited dates keep their original scope; they are not new complete page-read receipts. Its source catalogue and QC references are retained below, subject to the current passage-level table and outstanding items.

| Topic | Source |
| --- | --- |
| Statute | ITAA 1997 Division 355 (ss 355-1 to 355-750); s 355-25 (core activities/exclusions); s 355-35 (R&D entity); Industry Research and Development Act 1986, s 28D (overseas findings) |
| Rates/entitlements | ato.gov.au -- R&D tax incentive rates and entitlements (QC 107282, 70869, 70890, updated 13 May 2026) |
| Eligibility | ato.gov.au -- Eligibility for the R&D tax incentive (QC 70871, updated 13 May 2026) |
| Steps/registration/records | ato.gov.au -- Steps for claiming R&D tax offset (QC 70872); Keeping records and calculating notional deductions (QC 71853) |
| Excluded activities | business.gov.au -- Excluded R&D activities under the R&DTI (s 355-25(2) ITAA 1997) |
| Clawback/feedstock | ato.gov.au -- Clawback of R&D tax incentive offset (QC 70876, 70889); TR 2013/3 (feedstock); TR 2021/5 (at-risk rule) |
| Compliance | ato.gov.au -- Helping you get R&D claims right (QC 70873); TA 2017/3 (ordinary business activities); TA 2023/4 (associates) |
| Amendments | ato.gov.au -- Correcting mistakes and disputing decisions (QC 70877) |
| Registration extensions (checked 11 September 2026) | [DISR: request an extension or variation](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/request-an-extension-or-variation); Industry Research and Development Decision-making Principles 2022, Part 3 |

Not yet confirmed: taxpayer-specific activity classification, entity/group/exempt control, place/beneficiary and findings; full IR&D Act and Decision-making Principles 2022 Part 3 review, including disputed or exceptional applications; 2026-27 return/schedule/software labels, taxpayer lodgement/payment dates and earlier-only registration identifiers for payment-year associate claims; detailed prepayment provisions, full asset/capital-works/intangible classification and same-year simplified-depreciation/mixed-use interactions; the original $20,000 instant write-off claim for 2025-26 was not established by the 2026 amendment alone; full historical TR 2013/3/pre-2021 claims, remaining ruling examples and linked determinations; taxpayer-specific losses, carry-forward, franking, grant assessability and penalty/interest consequences; the original comparative claim that this is one of the most actively audited concession areas has no comparative evidence here; independent whole-guide and professional reliance sign-off.

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
