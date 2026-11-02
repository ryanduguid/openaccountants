---
name: au-small-business-cgt
description: >
  Use this skill for Australian small business CGT working papers for individuals, companies, trusts and partners in 2026-27. It covers Division 152 eligibility, aggregated turnover, maximum net asset value, active assets, shares and trust interests, the 15-year exemption, active asset reduction, retirement exemption and replacement asset rollover. It distinguishes concession choices, stakeholder payments and super CGT cap elections, with dated source conditions and hypothetical calculations. Trigger on 'small business CGT', 'SBCGT', 'Division 152', 'active asset', 'significant individual', 'retirement exemption', 'replacement asset period' and 'CGT cap election'. Read before preparing these positions; unresolved facts, period law and filing procedures require review.
version: 1.3
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 framework; verify operative law for each event, choice, payment and contribution date"
last_updated: 2026-11-02
review_status: pending_review
depends_on:
  - workflow-base
  - au-capital-gains
  - au-individual-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Small Business CGT Concessions v1.3

> **General reference only.** Prepare a working paper for a qualified Australian reviewer. This source-cited draft does not establish a taxpayer's eligibility, an approved return field or final tax liability. Obtain professional review before filing, paying, making an election or taking a position.

## Scope

Prepare an Australian Division 152 eligibility register, concession comparison and payment/election timetable for 2026-27. Cover a capital gain on a business asset, goodwill, qualifying share or trust interest, including an asset held outside the entity using it. Separate the asset owner, business user, concession claimant, CGT concession stakeholder and super contributor. These roles can belong to different people or entities. Use AUD and supported market values. [ITAA 1997 Div 152](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

Load [workflow-base](../../foundation/workflow-base.md), [au-capital-gains](au-capital-gains.md) and the relevant return guide. Route company tax and extraction to [au-company-tax](au-company-tax.md), trust assessment and distributions to [au-trust-distributions](au-trust-distributions.md), partnerships to [au-partnerships](au-partnerships.md), residence to [au-tax-residency](au-tax-residency.md), foreign-resident CGT to [au-nonresident-cgt](au-nonresident-cgt.md) and SMSF acceptance/administration to [au-smsf](au-smsf.md). A deduction, trading-stock profit or Division 40 balancing adjustment is not automatically a Division 152 capital gain. CGT event K7 is excluded by s 152-10(1)(a).

The current compilation read here applies from 1 October 2026 to 1 December 2026. It contains amendments whose assessment application starts later. Verify amendments and applicable compilations for the actual event, choice, payment and contribution dates, including earlier historical events. For assessments in the income year including 1 July 2027 and later years, the Tax Reform No. 1 Act changes the active asset reduction gateway by disregarding the specific $2 million restriction for that reduction. The general small business entity requirements still apply. It does not extend that change to the other 3 concessions. Establish the actual reform application, residence, asset and transition conditions with [au-capital-gains](au-capital-gains.md); do not assume a universal cost-base reset or minimum tax on every disposal. No timing recommendation or final 2027-28 liability is supplied here. [Tax Reform No. 1 Act, Sch 1 items 77A-82](https://www.legislation.gov.au/C2026A00071/latest/text).

## Ask the client first

1. Who legally and beneficially owns each asset, who uses it, which entity claims the concession and what residence history applies?
2. What are the acquisition, contract/event, cessation, proceeds, choice, stakeholder payment and proposed super contribution dates? Which requested periods are supported by operative sources?
3. What control rights, affiliates, trust distributions, connected entities and partnership interests exist, including changes during the relevant income years?
4. What supports every turnover route, market value, related debt/provision and asset-use period, including residential income use, rent and the share/trust look-through tests?
5. What capital losses, previous retirement exemption choices, previous CGT cap contributions, stakeholder ages, retirement/incapacity evidence and proposed replacement expenditure apply?
6. What records, written choices, fund acceptance evidence, election receipts, approved forms/software and professional decisions remain missing?

## The method, step by step


### Figures and timing register

This is the consolidated register for the checked 2026-27 framework. Conditions, exceptions and the relevant person/date are explained in the numbered steps. A figure does not establish eligibility or operative law for an unverified date.

| Measure | Amount, boundary or period | Official source |
|---|---|---|
| CGT small business turnover / MNAV | Aggregated turnover less than $2 million under the applicable route / net asset value no more than $6 million just before the event | [ss 152-10/15, 328-110](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Turnover estimate exception | Both previous 2 business years at least $2 million prevents that estimate route; actual-year route remains separate | same |
| General control / modified object-entity control | At least 40% / substitute 20%; possible general control determination only at least 40% but below 50% | [ss 328-125, 152-10(2)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Discretionary trust control distribution history | Previous 4 income years; statutory 40% distribution test, separate from directions/wishes | [s 328-125(3)-(6)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Special child affiliate rule | Child under 18, subject to the specific passive-asset conditions | [s 152-47](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Active periods | Owned no more than 15 years: at least half the test period; owned more than 15 years: at least 7.5 active years | [s 152-35](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Cessation modification | Normally business ceased within 12 months before event; longer period only if allowed | same |
| Share/trust asset ratio / significant individual / alternative stakeholder ownership | At least 80% / at least 20% / at least 90%, each subject to its own statutory conditions | [ss 152-40, 152-55, 152-10(2)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| 15-year exemption | At least 15 years continuous ownership; age 55 or older with retirement connection, or permanent incapacity; additional significant-individual history where required | [ss 152-105/110/115](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| General individual discount / active asset reduction | Each 50% where separately eligible; companies have no general discount; J-event restrictions apply | [ss 115-100, 152-205](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Retirement exemption | $500,000 lifetime per individual, reduced by earlier choices; age under 55 at individual choice or stakeholder payment triggers the relevant mandatory super rule | [ss 152-305/320/325](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Entity retirement payments / individual mandatory contribution | Normally later of 7 days after choice and 7 days after proceeds / at the later of choice and receipt; special J-event and instalment rules apply | [ss 152-305/325](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Stakeholder exemption and allocation measures | For s 152-125, relevant stakeholder percentage multiplied by exempt amount; discretionary category percentage is 100 divided by stakeholder count. Retirement allocations in writing total 100%, and may include zero | [ss 152-125(2), 152-315(5)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| General CGT choice deadline | By the day the relevant return is actually lodged, or further time actually allowed; written retirement-choice requirements remain separate | [ss 103-25, 152-315](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Entity 15-year payment window | Before later of 2 years after event and relevant 6-month earnout period, subject to an allowed s 152-125 extension | [s 152-125](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Individual CGT cap contribution category / qualifying entity payment contribution | Normally by later of required return-lodgement day and 30 days after proceeds / within 30 days after qualifying payment; amount and category conditions apply | [s 292-100](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| CGT cap published index amounts | 2026-27 $1,935,000; 2025-26 $1,865,000 as historical comparison. Reconcile individual prior usage and annual increases in the contribution year | [ATO Table 6](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps?anchor=CGTcapamount); [s 292-105](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| CGT cap election | At or before contribution; late election invalid for this exclusion | [s 292-100(9)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Replacement asset period | One year before last qualifying rollover event in income year to later of 2 years after that event and relevant 6-month earnout period; specific modifications/extensions apply | [s 104-190](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Estate event window | Normally within 2 years of death; longer period requires actual Commissioner extension | [s 152-80](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |

### 1. Establish the asset, source period and evidence states

Build a dated register of each separately acquired asset or interest. Establish the CGT event and its timing, proceeds, GST adjustments, cost base, reduced cost base, market-value substitutions and any earnout before applying concessions. A sale contract usually determines A1 timing; settlement and super contribution can fall in different income years. Defer to the actual event rules in [au-capital-gains](au-capital-gains.md). Separate pre-CGT assets, depreciating assets, revenue transactions and foreign/temporary-resident restrictions.

For each fact, record source document, date, classification and reviewer flag. The permitted factual default is to leave an unsupported amount or condition as Needs Input. Do not invent a connected entity, age, retirement intention, rent classification, zero trust participation, $2 million eligibility, extension or election. Reconstruct missing records from available legal documents, accounts, valuations and transaction records. Withhold the affected concession, dependent net capital gain and final tax until resolved; disclose any independently calculable gross amount as provisional. No monetary threshold permits guessing these conditions.


| Unresolved fact | Permitted default | Effect |
|---|---|---|
| Turnover, control map or market value | No invented amount or connected/affiliate status | Needs Input for affected gateway and dependent totals. |
| Rental/main use, active period or intangible classification | No assumed activity or automatic rejection | Obtain rights and use history before deciding. |
| Trust distributions or stakeholder rights | No assumed zero percentage or nomination | Obtain relevant-year and prior-year documents. |
| Age, retirement, incapacity or prior lifetime usage | No presumed age or remaining limit | Hold affected exemption and required-payment conclusion. |
| Contribution year, fund acceptance or timely election | No assumed acceptance or CGT cap exclusion | Hold cap treatment; identify the actual evidence gap. |
| Extension, determination or period law | No assumed discretion or legal authority | Refer the condition and withhold affected results. |

### 2. Prove a basic eligibility gateway

A gain generally needs a CGT event other than K7, an otherwise resulting capital gain, a gateway in s 152-10(1)(c) and the active asset test. Check the modified D1 conditions for a created right, the additional share/trust conditions and the special partnership membership-interest requirement. Do not use the ordinary disposal shortcut for every event. [ITAA 1997 ss 152-10/12](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

| Gateway or condition | Amount and timing | Official source |
|---|---|---|
| CGT small business entity | Carries on business; apply the less-than-$2 million aggregated-turnover substitution for 2026-27 | [ss 152-10(1AA), 328-110](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Maximum net asset value (MNAV) | No more than $6 million just before the relevant event; exactly $6 million passes this gateway | [ss 152-15/20](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Passively held asset | Claimant carries on no business other than in partnership; qualifying affiliate/connected business user is a CGT small business entity; satisfy all asset and use conditions | [s 152-10(1A)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Partnership asset interest | Claimant is a partner in a partnership that is a CGT small business entity; gain concerns their interest in a partnership asset | [s 152-10(1)(c)(iii)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Partner's separately owned asset | Partnership is a CGT small business entity; claimant is a partner, carries on no business other than in partnership and satisfies the non-partnership-interest and business-use conditions | [s 152-10(1B)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |

For the turnover route, distinguish the previous year's actual aggregated turnover, a permitted current-year estimate made at the start of the year or business, and actual aggregated turnover established at year end. The estimate route is unavailable where business was carried on in both previous years and each year's aggregated turnover was at least $2 million. Failure of that estimate does not establish that the year-end actual route fails. Exactly $2 million fails a less-than test. Record the route and evidence for every relevant year. Winding-up rules can preserve business status in specified circumstances. [ss 328-110, 152-49](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO CGT small business entity eligibility](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/cgt-small-business-entity-eligibility).

Annual turnover is ordinary income in the ordinary course of business, excluding GST and retail fuel sales under the specific rules. Exclude capital asset proceeds and borrowings; assess the actual receipt's character. Apply reasonable full-year estimation for a part-year business and arm's-length amounts for associate dealings. Aggregate the relevant annual turnovers of affiliates and connected entities, excluding specified dealings within the group and periods outside the connection. Do not substitute accounting sales or profit for the statutory calculation. [ss 328-115/120](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

Map direct, common and indirect control under s 328-125. The usual control threshold is at least 40% of relevant income/capital rights or company voting power, including relevant affiliate rights. A discretionary trust also has the directions/wishes test and the distribution test over the previous 4 income years. A Commissioner determination for a control percentage of at least 40% but less than 50% is conditional, never automatic. An affiliate can be an individual or company acting according to directions/wishes or in concert in its business affairs. Trusts, partnerships and super funds cannot themselves be affiliates. Relationship, directorship, trusteeship or partnership alone is insufficient. Consider the special spouse/child-under-18 rule for passively held assets, its 2-stage application and the related aggregation rules. [ss 328-125/130, 152-47/48/78](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO affiliates](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/small-business-affiliates).

For MNAV, total supported market values of the statutory asset group less related liabilities and the specified provisions for annual leave, long service leave, unearned income and tax liabilities. Net value can be negative, zero or positive. Include non-business CGT assets unless a specific exclusion applies. Do not deduct every accounting provision. Do not double-count excluded connected-entity equity interests and underlying net assets; the equity exclusion does not exclude debt interests and specifically preserves related liabilities. Affiliate-only asset inclusion and the exception for an entity connected only through an affiliate require the actual business-use facts. [ss 152-15/20](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

For an individual, test the specific exclusions for assets used solely for personal use, qualifying residence value, super rights and life insurance. An interest-earning personal bank account is not solely personal-use property. Residential income use depends on the hypothetical interest-deductibility test, floor area and length of income use over ownership, not just the percentage used on sale day. Apportion the related residence liability consistently. A high MNAV result rules out this gateway; it does not rule out an independently proved turnover, passive-asset or partnership gateway. [s 152-20(2)-(4)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO MNAV](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/maximum-net-asset-value-test).

### 3. Establish active use and additional ownership tests

| Test | Requirement | Official source |
|---|---|---|
| Owned for 15 years or less | Active for at least half the statutory test period | [s 152-35](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Owned for more than 15 years | Active for at least 7.5 years during that test period | same |
| End of test period | Earlier of event or business cessation where cessation is within the preceding 12 months, or a longer period allowed by the Commissioner | same |
| Resident company/trust share or interest | Apply the 80% asset test, inherent-business cash/financial instruments, continuity and temporary-failure rules, then the modified conditions where required | [ss 152-40(3)-(4), 152-10(2)-(2B)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Significant individual | Small business participation percentage at least 20%, direct plus indirect | [ss 152-55/65/70/75](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| CGT concession stakeholder | Significant individual, or that person's spouse with a participation percentage above zero | [s 152-60](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Alternative ownership condition | Relevant stakeholders in the object company/trust together have at least 90% participation in the claimant just before the event | [s 152-10(2)(d)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |

Measure active periods, which need not be continuous. An asset, tangible or intangible, can qualify through actual use or functional readiness in the relevant business. An intangible can alternatively qualify through inherent connection with that business; it need satisfy only one of those routes. Assess the whole asset's main use in the relevant periods. Financial instruments and assets mainly used to derive rent, interest, annuities, royalties or foreign exchange gains are generally excluded, subject to the statutory exceptions, including temporary rental use and qualifying improved intangibles. For rent, inspect the actual occupation rights, services and use. Business status alone does not defeat the rent exclusion. [s 152-40](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO active asset test](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/active-asset-test).

Under s 152-40(4A), disregard specified personal use and treat use by an affiliate or connected entity as the owner's use. That is not a universal rental exemption: a connected user's subletting to an unrelated tenant can retain a rent character. Nor does a later unrelated lease automatically erase earlier qualifying active periods. Where relevant, verify the statutory continuation choices for relationship breakdown or involuntary disposals rather than replacing the actual ownership history. [ss 152-40(4A), 152-45/115](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

For company participation, use the smallest applicable voting, dividend and capital rights, considering all relevant classes, redeemable-share exclusions and the jointly held voting rule. Fixed-trust rights and discretionary-trust distributions have different tests. Under s 152-70, where only one distribution measure applies, use that measure; do not invent a zero capital percentage when no capital distribution occurred. A no-distribution year can use a qualifying prior distribution year where the tax-loss/no-net-income conditions hold. No distribution history, or undistributed net income without a tax loss, can instead produce zero. Separate this from the signed controller nomination under s 152-78, which is not an automatic significant-individual election. Multiply indirect percentages through each intermediate entity and add separate direct/indirect paths. [ss 152-65/70/75/78](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

Widely held company shares and specified listed/widely held trust interests are excluded from active-asset status unless the holder is a CGT concession stakeholder in the relevant entity under s 152-40(4)(b)/(c). The 80% ratio or alternative 90% ownership route does not remove that holder restriction; a company/trust cannot itself be an individual stakeholder. Refer or hold such a position unless the actual statutory exception is established.

For shares or trust interests subject to s 152-10(2), also prove the claimant's business status just before the event unless the claimant meets MNAV. Apply the object entity's modified CGT small business/MNAV tests: the controlled-entity threshold is 20%, with the specified Commissioner determination disregarded and the statutory affiliate/controlled group included. Apply the modified active-asset look-through, weighting later-entity assets by participation, excluding the replaced equity interests and limiting qualifying later-entity assets by that entity's modified gateway and the claimant's participation/stakeholder conditions. Exclude cash or instruments injected with a purpose of passing the test. A current 80% ratio alone does not prove the required active period. [ss 152-10(2)-(2B)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO additional conditions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/additional-conditions-if-the-cgt-asset-is-a-share-or-trust-interest).

### 4. Compare concessions in the correct order

First test the 15-year exemption. For a qualifying individual, continuous ownership for at least 15 years and the age-55/retirement connection or permanent-incapacity condition are required. If the asset is a share/trust interest, the object entity must also have had a significant individual for at least 15 years in total during ownership. For a company/trust claimant, test its continuous ownership, at least 15 years in total with a significant individual and a significant individual just before the event meeting the age/retirement or incapacity condition. The significant individual need not be the same person for all 15 years. Test each separately acquired interest. Retirement is a factual connection, not an assumption from age or the concession's name. [ss 152-105/110/115](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

If the 15-year exemption applies, disregard that gain before using capital losses; preserve losses for other eligible gains or future years. Otherwise apply current-year capital losses, available prior-year capital losses in the required order, any eligible Division 115 discount and then the 50% active asset reduction. Companies do not receive the general discount. The active asset reduction applies where its conditions hold unless the claimant chooses out; it is distinct from the general discount. After that, choose a supported retirement exemption, rollover or their order for any remaining gain. Compare only legally available choices and disclose lifetime-limit, payment and extraction effects. Do not equate the resulting net capital gain with tax payable. [ss 102-5, 152-205/210/215/220](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO active asset reduction](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-50-percent-active-asset-reduction).

A qualifying 15-year company/trust payment has its own stakeholder, time and amount limits under s 152-125, normally before the later of 2 years after the event and 6 months after the latest possible look-through earnout benefit, subject to an allowed extension. The exemption limit for each stakeholder is its statutory participation percentage multiplied by the exempt amount. For a company or the fixed-entitlement trust category, use the relevant small business participation percentage just before the event; for the discretionary-trust category, use 100 divided by the number of CGT concession stakeholders just before the event, expressed as a percentage. Other company/trust cash distributions do not become tax free merely because the entity reduced or rolled over a gain. Trust beneficiary gross-up/assessment and company distributions require their separate rules. Do not assign a flat 47% personal or 25% company tax saving without establishing the actual incremental assessment. [s 152-125](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO 15-year exemption](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-15-year-exemption).

### 5. Make retirement choices and payments separately from a super cap election

The retirement exemption has a $500,000 lifetime limit per individual, reduced by previous choices made by or for that individual, including applicable old-law amounts. Actual retirement is not required. Specify the CGT exempt amount in writing. A company/trust in a public-entity category listed in s 328-125(8) cannot make the retirement choice. For an eligible non-public company/trust, prove a significant individual and all s 152-325 conditions; allocate the exempt amount in writing amongst its stakeholders, with percentages totalling 100%. A percentage may be zero and need not match equity ownership. Track each person's remaining lifetime limit. [ss 152-305/315/320/325](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

| Situation | Required payment/contribution and timing | Official source |
|---|---|---|
| Individual under 55 just before choosing retirement exemption | Contribute the exempt amount to a complying super fund/RSA at the later of the choice and proceeds receipt; apply the instalment rules | [s 152-305(1)-(1B)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Individual J2/J5/J6 retirement choice | Required under-55 contribution when the choice is made | same |
| Individual 55 or older just before choice | No compulsory Division 152 super contribution; a voluntary CGT cap contribution still has its own conditions | same |
| Company/trust ordinary retirement payment | Pay the statutory amount by the later of 7 days after choice and 7 days after proceeds receipt; apply instalments successively up to the exempt amount | [s 152-325(1)-(6)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| Company/trust J2/J5/J6 retirement choice | Make the required payment within 7 days after the choice | same |
| Stakeholder under 55 just before payment | Entity must contribute the required payment to the stakeholder's complying fund/RSA and notify the fund at that time under s 152-325(7) | [s 152-325(7)-(8)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |

A gift or deemed market-value gain can qualify without actual cash proceeds, but the payment/contribution conditions still require evidence and funding. Entity payments use the statutory lesser-of limit and stakeholder allocations, not a free distribution of all proceeds. Qualifying payments have the specific non-assessable/non-exempt, non-deductible and company dividend/Division 7A treatment in ss 152-310/325. Do not extend that treatment to an unrelated payment. [ATO retirement exemption](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-retirement-exemption).

A mandatory contribution under Division 152 is not automatically a contribution under the super CGT cap. Section 292-100 requires an eligible personal contribution satisfying the relevant 15-year or retirement category, its amount and time conditions, and an approved election made at or before contribution. Give the signed and dated NAT 71161 to the receiving fund at or before the contribution, not to the ATO. Retain delivery/acceptance evidence. A missing or late election cannot be treated as valid. The separate entity notice under s 152-325(7) does not replace this election. [s 292-100(1), (9)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO CGT cap election](https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-cap-election).

For an individual's qualifying 15-year contribution, the category concerns eligible capital proceeds; for an individual's retirement contribution, it concerns the disregarded gain. The s 292-100(2)/(7) outer deadline is the later of the day the relevant income tax return is required to be lodged and 30 days after receipt of the capital proceeds. That outer cap-category deadline does not extend a stricter required retirement contribution at choice/receipt. For qualifying entity payments, separately check s 292-100(4)/(8), including the payment's amount/time conditions and the individual's contribution within 30 days of payment where applicable. A direct required entity contribution must still meet its earlier s 152-325 deadline. A payment extension under s 152-125 does not itself extend the separate s 292-100(4) contribution-category conditions. The ATO 15-year page uses the day of actual lodgement in its contribution summary; the statutory required-lodgement date controls. Do not conflate either with the general CGT choice deadline in s 103-25, which refers to the day the return is lodged, or assume an extension. [ss 103-25, 292-100](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

| Super CGT cap measure | Amount/condition | Official source |
|---|---|---|
| Published index amount for 2026-27 | $1,935,000 | [ATO contributions caps, CGT cap amount](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps?anchor=CGTcapamount) |
| Published index amount for 2025-26 | $1,865,000; historical comparison only, not proof of the law for another transaction | same |
| Individual's available CGT cap | Reconcile previous qualifying contributions and annual index increases; use the contribution financial year, not automatically the sale year | [s 292-105](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |

Fund acceptance, personal-contribution character, age restrictions and any non-concessional or bring-forward capacity require their own current evidence. The CGT cap is separate from the $500,000 retirement exemption lifetime limit. A failure of the CGT cap exclusion does not itself calculate excess-contributions tax or establish fund acceptance. Do not direct a taxpayer to contribute a residual amount without those checks.

### 6. Record a rollover and monitor its conditions

A claimant satisfying the applicable basic conditions can choose rollover for all or part of a gain before acquiring a replacement asset or incurring qualifying fourth-element improvement expenditure. The same claimant must acquire/incur it. Record the disregarded amount, relevant events, replacement asset period, expenditure and active/stakeholder conditions; do not report permanent exemption. [ss 152-410/415](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

The replacement asset period starts one year before the last CGT event in the income year for which rollover is obtained. It ends at the later of 2 years after that last event and, where relevant, 6 months after the latest possible look-through earnout benefit. Apply the specific s 104-190 modifications for recovered/misappropriated proceeds or an actual Commissioner extension. Several events in a year can change the period; do not calculate a separate assumed 2-year deadline from each sale. [s 104-190](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

| Event | Consequence under the checked provisions | Official source |
|---|---|---|
| J5 | At period end, no qualifying replacement/expenditure or failed required conditions can bring back the full deferred gain | [s 104-197](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| J6 | Qualifying assets/expenditure exist but qualifying first-element cost, incidental costs and fourth-element expenditure total less than the deferred gain; gain is the shortfall at period end | [s 104-198](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |
| J2 | After period end a relevant change in replacement-asset use/status can bring back the deferred amount, adjusted for qualifying remaining assets and prior J2/J6 recaptures | [s 104-185](https://www.legislation.gov.au/C2004A05138/2026-10-01/text) |

J2/J5/J6 gains cannot receive the 15-year exemption or active asset reduction; they do not receive the ordinary general discount. J5/J6 cannot receive a further small business rollover. A retirement exemption may remain available, with the basic-condition waiver for J5/J6 but all relevant retirement requirements still needed. J2 can potentially qualify for further rollover or retirement relief where the applicable conditions hold. A disposal of the replacement asset can also produce a separate A1 gain. Apply the law for the later event year and do not double-count earlier recaptures. [ss 152-10(4), 152-305(4), 115-25/40](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [ATO rollover](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-roll-over).

## Boundary and exception table

| Situation | Required treatment |
|---|---|
| Unknown turnover or group map | Leave eligibility unresolved, reconstruct records and test alternate gateways only with evidence. |
| MNAV above $6 million | This gateway fails. Independently test the other statutory gateways and all additional conditions. |
| Mixed rent/business use or connected user's sublease | Establish main use during each relevant period; a family or company relationship alone does not establish activity. |
| No discretionary trust distribution | Check tax loss/net income and the last actual distribution year; do not assume either zero participation or a valid controller nomination. |
| Earnout, non-arm's-length dealing or no cash proceeds | Establish event/proceeds/substitution rules, relevant payment funding and extended statutory periods. Obtain specialist review for unresolved rights or valuation. |
| Foreign/temporary residence, pre-CGT interest or 2027 reform boundary | Route to the relevant CGT/residence guide; hold affected calculations until operative sources and application are established. |
| Death or permanent incapacity | Check s 152-80/152-420 and the actual qualifying facts. The estate rule can modify retirement/age/super conditions, normally within 2 years of death, with any longer period requiring an actual extension. |
| Relationship breakdown or compulsory acquisition | Verify the particular rollover and continuity choice under ss 152-45/115. A transfer does not automatically supply 15 years' ownership. |
| Late election, missing payment or exhausted lifetime limit | Do not claim satisfaction; report the specific failed condition and obtain advice on any available remedy. |

## Worked cases

All cases are hypothetical AUD workpapers, not factual defaults or whole-return tax assessments. Eligibility, values and source conditions are stipulated only within each case. Cases using 2026-27 future dates are illustrations under the checked provisions, subject to rechecking operative law when those dates occur. The blocks recompute arithmetic; they cannot prove eligibility, an election, fund acceptance or professional approval.

### Case 1: Net assets and an alternate gateway

Nadia, an Australian resident, contracts to sell an active business property on 30 November 2026 after 8 years. All amounts are stipulated net statutory values, after the required group and liability adjustments: premises $1.9 million, connected company underlying net assets $1.75 million and an unconnected investment portfolio $600,000. Her residence has market value $1.2 million and related debt $600,000. The hypothetical interest test is met for 50% of its area during 5 of 10 ownership years and zero for the other 5, including the current year. The supported area/time fraction is 25%, giving residence net inclusion $150,000 and MNAV $4.4 million. If only the portfolio instead becomes $2.5 million, MNAV is $6.3 million. That fails MNAV; it does not prove that all gateways fail. In a separate variant, substantiated year-end aggregated turnover of $1.9 million and current business status establish the turnover gateway, with the active-asset and other conditions still required. A $3.4 million prior-year amount and $3.1 million estimate alone would not establish the eventual actual turnover. [ss 152-10/15/20, 328-110](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

```oa-check
name: MNAV historical residence use and alternate turnover gateway
inputs:
  premises_net: 1900000
  connected_net: 1750000
  portfolio: 600000
  home_value: 1200000
  home_debt: 600000
  income_area: 0.5
  income_years: 5
  ownership_years: 10
  alternative_portfolio: 2500000
  mnav_limit: 6000000
  alternative_turnover: 1900000
  turnover_limit: 2000000
steps:
  home_fraction: income_area * income_years / ownership_years
  home_net_included: (home_value - home_debt) * home_fraction
  mnav: premises_net + connected_net + portfolio + home_net_included
  mnav_headroom: mnav_limit - mnav
  alternative_mnav: mnav - portfolio + alternative_portfolio
  mnav_excess: alternative_mnav - mnav_limit
  turnover_headroom: turnover_limit - alternative_turnover
expected:
  home_fraction: 0.25
  home_net_included: 150000
  mnav: 4400000
  mnav_headroom: 1600000
  alternative_mnav: 6300000
  mnav_excess: 300000
  turnover_headroom: 100000
```

### Case 2: Losses before discount and a real concession choice

A resident individual aged 58 has an eligible gain of $900,000 on an asset held for 8 years, current capital losses $100,000 and supported available prior capital losses $80,000. The 15-year exemption is unavailable. All Division 152 and discount predicates are stipulated. Earlier retirement exemption choices total $90,000. Losses leave $720,000, the 50% discount leaves $360,000 and the active asset reduction leaves $180,000. A valid written retirement exemption for $180,000 leaves nil from this gain and $230,000 lifetime retirement capacity. If the individual instead chooses out of the active asset reduction, fully exempting $360,000 leaves $50,000 lifetime capacity. Both routes require their conditions; the additional lifetime consumption is $180,000. There is no compulsory Division 152 super contribution at age 58. No flat-rate tax saving or automatic preference is inferred. [ss 102-5, 152-205/220/305/320](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

```oa-check
name: Capital losses and discount precede active asset and retirement choices
inputs:
  gain: 900000
  current_losses: 100000
  prior_losses: 80000
  prior_retirement: 90000
  lifetime_limit: 500000
steps:
  after_losses: gain - current_losses - prior_losses
  after_discount: after_losses * 0.5
  after_active_reduction: after_discount * 0.5
  retirement_choice: after_active_reduction
  net_capital_gain: after_active_reduction - retirement_choice
  retirement_remaining: lifetime_limit - prior_retirement - retirement_choice
  no_reduction_choice: after_discount
  no_reduction_remaining: lifetime_limit - prior_retirement - no_reduction_choice
  extra_lifetime_used: no_reduction_choice - retirement_choice
expected:
  after_losses: 720000
  after_discount: 360000
  after_active_reduction: 180000
  retirement_choice: 180000
  net_capital_gain: 0
  retirement_remaining: 230000
  no_reduction_choice: 360000
  no_reduction_remaining: 50000
  extra_lifetime_used: 180000
```

### Case 3: Under 55 contribution with and without a valid cap election

Marco is 48 immediately before making a retirement exemption choice in 2026-27. His eligible $600,000 gain is on a qualifying long-held asset; no losses apply and the general discount and active asset reduction are available. The remaining $150,000 is validly chosen for the retirement exemption and must be contributed at the later of choice and proceeds receipt. All dates in this illustration fall in 2026-27. Previous qualifying cap usage, after the required annual reconciliation, leaves $1,735,000 available before this contribution; no prior retirement exemption has been used. With an eligible contribution and timely signed NAT 71161, $150,000 uses the CGT cap and leaves $1,585,000. In the alternative of a missing/late election, the compulsory contribution alone does not establish a CGT cap exclusion: excluded amount is zero and $150,000 needs assessment under the non-concessional rules. That does not calculate excess-contributions tax. An October 2027 choice/contribution instead requires the 2027-28 cap and period law, not this sale-year cap. [ss 152-305, 292-100/105](https://www.legislation.gov.au/C2004A05138/2026-10-01/text); [NAT 71161](https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-cap-election).

```oa-check
name: Mandatory retirement contribution does not establish CGT cap election
inputs:
  gain: 600000
  index_amount: 1935000
  reconciled_prior_usage: 200000
  retirement_limit: 500000
steps:
  after_discount: gain * 0.5
  retirement_amount: after_discount * 0.5
  mandatory_contribution: retirement_amount
  available_cap: index_amount - reconciled_prior_usage
  remaining_cap_with_election: available_cap - mandatory_contribution
  retirement_remaining: retirement_limit - retirement_amount
  excluded_without_election: mandatory_contribution * 0
  ncc_without_election: mandatory_contribution - excluded_without_election
expected:
  after_discount: 300000
  retirement_amount: 150000
  mandatory_contribution: 150000
  available_cap: 1735000
  remaining_cap_with_election: 1585000
  retirement_remaining: 350000
  excluded_without_election: 0
  ncc_without_election: 150000
```

### Case 4: Shares and an income-only trust participation measure

Priya, a resident individual aged 58, owns 40% of one non-redeemable equal-rights share class for 5 years. Voting, dividend and capital rights are all 40%. Her MNAV is supported at $4.2 million. The object company and its modified statutory group have $1.6 million aggregated turnover. Its $2 million asset pool comprises $1.55 million active assets, $250,000 inherently connected business cash and $200,000 other assets; no later entities or purpose-injected assets exist. The supported 90% ratio and use history satisfy the applicable active period. A $700,000 share gain with no losses becomes $350,000 after discount and $175,000 after active asset reduction. With all retirement conditions and no prior usage, a $175,000 choice leaves nil and $325,000 lifetime capacity. In a separate discretionary-trust example, a beneficiary receives $200,000 of the year's $1 million income distribution and there is no capital distribution. The applicable income measure is 20%, not an invented zero capital measure; other stakeholder conditions still require proof. [ss 152-10(2), 152-40/55/70](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

```oa-check
name: Share asset ratio and applicable discretionary trust participation
inputs:
  active_assets: 1550000
  business_cash: 250000
  total_assets: 2000000
  share_gain: 700000
  retirement_limit: 500000
  beneficiary_income: 200000
  distributed_income: 1000000
steps:
  qualifying_assets: active_assets + business_cash
  active_ratio: qualifying_assets / total_assets
  after_discount: share_gain * 0.5
  retirement_amount: after_discount * 0.5
  net_capital_gain: retirement_amount - retirement_amount
  retirement_remaining: retirement_limit - retirement_amount
  trust_participation: beneficiary_income / distributed_income
expected:
  qualifying_assets: 1800000
  active_ratio: 0.9
  after_discount: 350000
  retirement_amount: 175000
  net_capital_gain: 0
  retirement_remaining: 325000
  trust_participation: 0.2
```

### Case 5: 15-year priority preserves losses and has a different super amount

Colin, a resident individual aged 62, sells his continuously owned 22-year business asset in connection with evidenced retirement. It was active for 16 years; all basic and 15-year conditions are stipulated. Capital proceeds are $2.1 million and the gain is $1.1 million. The whole gain is disregarded first, preserving $50,000 available capital losses and leaving the $500,000 retirement exemption lifetime limit unused. A proposed eligible 2026-27 personal contribution of $1,935,000 fits his fully available CGT cap, subject to all s 292-100 conditions, fund acceptance and timely election. The $165,000 remaining proceeds are not a direction to make another super contribution; their possible treatment requires separate evidence. The 15-year contribution category can concern proceeds, not merely the disregarded gain. [ss 152-105/215/330/430, 292-100(2)/105](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

```oa-check
name: 15-year exemption precedes losses and contribution can use proceeds
inputs:
  proceeds: 2100000
  gain: 1100000
  available_losses: 50000
  proposed_contribution: 1935000
  available_cgt_cap: 1935000
  retirement_limit: 500000
steps:
  disregarded_gain: gain
  included_gain: gain - disregarded_gain
  losses_preserved: available_losses
  cap_after_proposal: available_cgt_cap - proposed_contribution
  remaining_proceeds: proceeds - proposed_contribution
  contribution_above_gain: proposed_contribution - gain
  retirement_capacity_preserved: retirement_limit
expected:
  disregarded_gain: 1100000
  included_gain: 0
  losses_preserved: 50000
  cap_after_proposal: 0
  remaining_proceeds: 165000
  contribution_above_gain: 835000
  retirement_capacity_preserved: 500000
```

### Case 6: Replacement period and alternative recapture arithmetic

For planning only, assume qualifying rollover events on 15 March and 15 June 2027 in the same income year, with no earnout or extension. Under the checked s 104-190 rule, the common period starts 15 June 2026 and ends 15 June 2029, not 15 March 2029. A stipulated deferred amount is $180,000. At period end, a qualifying replacement has first-element cost $90,000, eligible acquisition incidental costs $10,000 and qualifying fourth-element expenditure $20,000. The current-law J6 mechanism would return a $60,000 shortfall and leave $120,000 deferred. In the alternative of no qualifying replacement, J5 would return $180,000; do not add both alternatives. If the sole qualifying asset later changes status after that $60,000 J6 recapture, the corresponding full J2 recapture would be $120,000, not $180,000 again. No future-year taxable gain, retirement relief, rollover eligibility or tax assessment is concluded: recheck operative law at the period end/later event and apply its conditions. [ss 104-185/190/197/198](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

```oa-check
name: Rollover expenditure shortfall and no duplicate recapture
inputs:
  deferred_gain: 180000
  first_element: 90000
  incidental_costs: 10000
  fourth_element: 20000
steps:
  qualifying_expenditure: first_element + incidental_costs + fourth_element
  j6_mechanism: deferred_gain - qualifying_expenditure
  remaining_deferred: deferred_gain - j6_mechanism
  alternative_j5_mechanism: deferred_gain
  later_full_j2_mechanism: deferred_gain - j6_mechanism
  total_j6_then_j2: j6_mechanism + later_full_j2_mechanism
expected:
  qualifying_expenditure: 120000
  j6_mechanism: 60000
  remaining_deferred: 120000
  alternative_j5_mechanism: 180000
  later_full_j2_mechanism: 120000
  total_j6_then_j2: 180000
```

### Case 7: Company allocation and the age at payment

A private company has an eligible $800,000 gain and no capital losses. It has no general CGT discount and the 15-year exemption is unavailable. After its active asset reduction, it validly chooses $400,000 retirement exemption, allocated in writing 75% to stakeholder A and 25% to stakeholder B, with all other conditions established. Prior lifetime choices were $50,000 for A and $120,000 for B. Proceeds were received on 10 December 2026 and the company chooses on 15 December: the ordinary statutory payment deadline is 22 December. Immediately before payment A is exactly 55 and B is 54. Required payments are $300,000 and $100,000; only B's payment must be contributed directly to super under s 152-325(7). Its fund notice and any CGT cap election remain separate requirements. Retirement limits remaining are $150,000 and $280,000. Choosing out of the reduction and allocating an $800,000 retirement amount in the same percentages would allocate $600,000 to A, exceeding A's $450,000 remaining limit by $150,000, so that proposed full choice cannot be made on these facts. [ss 152-205/220/305/315/320/325](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

```oa-check
name: Company retirement allocation lifetime limits and mandatory super
inputs:
  gain: 800000
  allocation_a: 0.75
  allocation_b: 0.25
  prior_a: 50000
  prior_b: 120000
  lifetime_limit: 500000
steps:
  retirement_choice: gain * 0.5
  payment_a: retirement_choice * allocation_a
  payment_b: retirement_choice * allocation_b
  required_super: payment_b
  remaining_a: lifetime_limit - prior_a - payment_a
  remaining_b: lifetime_limit - prior_b - payment_b
  no_reduction_a: gain * allocation_a
  no_reduction_a_excess: no_reduction_a - (lifetime_limit - prior_a)
expected:
  retirement_choice: 400000
  payment_a: 300000
  payment_b: 100000
  required_super: 100000
  remaining_a: 150000
  remaining_b: 280000
  no_reduction_a: 600000
  no_reduction_a_excess: 150000
```

### Case 8: Active duration and the exact asset-ratio boundary

Assume the statutory test periods equal the stipulated ownership durations, with no cessation or continuity modification. A property owned for 10 years was active in the owner's business for 4 years and then used solely for unrelated long-term rent for 6 years. It is short of the required 5 active years by one year. This conclusion follows the active-period test, not a rule that rent in a majority of ownership years always decides every asset. A separate 20-year asset active for 8 years exceeds the 7.5-year requirement by half a year. For a separate resident company with verified asset classifications and all relevant modified tests addressed, $1.6 million qualifying assets of $2 million meets the 80% point-in-time boundary exactly; $1,599,999 is one dollar short. The ratio alone does not prove historical active periods or other eligibility. [ss 152-35/40, 152-10(2)](https://www.legislation.gov.au/C2004A05138/2026-10-01/text).

```oa-check
name: Active duration and inclusive 80-percent boundary
inputs:
  short_ownership: 10
  short_active: 4
  long_active: 8
  long_required: 7.5
  total_assets: 2000000
  qualifying_at_boundary: 1600000
  qualifying_below: 1599999
steps:
  short_required: short_ownership * 0.5
  shortfall_years: short_required - short_active
  long_excess_years: long_active - long_required
  required_qualifying_assets: total_assets * 0.8
  boundary_ratio: qualifying_at_boundary / total_assets
  below_shortfall: required_qualifying_assets - qualifying_below
expected:
  short_required: 5
  shortfall_years: 1
  long_excess_years: 0.5
  required_qualifying_assets: 1600000
  boundary_ratio: 0.8
  below_shortfall: 1
```

## When to refuse or refer

| Code | Trigger | Required action and verbatim output |
|---|---|---|
| R-AU-SBC-1 | Gateway, control, valuation, active use, ownership rights, age or previous exemption usage is unresolved | Stop affected eligibility and dependent totals. List the missing evidence and questions for the reviewer; do not invent the higher-tax answer. Output: 'I cannot establish this concession from unsupported eligibility facts. The affected result is held for a qualified Australian reviewer pending the identified evidence.' |
| R-AU-SBC-2 | Written choice, statutory payment, fund acceptance, notice or cap election is missing, late or disputed | Hold the affected relief/cap exclusion and dependent filing output. Identify each deadline and obtain specialist advice on any available remedy. Output: 'I cannot treat the relief or CGT cap election as effective without evidence of the required choice, payment, fund conditions and timely notice. The affected result remains held for review.' |
| R-AU-SBC-3 | Earnout, non-arm's-length restructuring, contested main use, complex look-through or distribution rights cannot be established | Preserve the known facts and alternative computations; refer the unresolved legal/valuation decision. Output: 'I cannot determine this legal classification or valuation from the supplied facts. A qualified Australian specialist must resolve the identified issue before the affected result is finalised.' |
| R-AU-SBC-4 | Mixed/foreign residence, pre-CGT status, historical law or the 2027 transition lacks applicable sources | Stop the affected period calculation and route to the CGT/residence specialist. Do not infer reform application or a tax-minimising disposal date. Output: 'I cannot apply this position without verified authority for the requested period and residence facts. The affected calculation is held for a qualified Australian reviewer.' |
| R-AU-SBC-5 | Death, incapacity or Commissioner extension/determination is material | Verify evidence and the exact special rule. Do not assume an extension or medical/legal conclusion. Output: 'I cannot assume incapacity, a statutory exception or a Commissioner discretion. The affected position is held until the required evidence or decision is established.' |
| R-AU-SBC-6 | Filing/payment requested without qualified review, or source/record uncertainty remains | Deliver the provisional workpaper, unresolved items and reviewer brief; refuse to describe it as ready to file or pay. Output: 'These are working papers for a qualified Australian reviewer. I cannot remove that review or present an unresolved result as ready to file or pay.' |

Reviewer cash threshold: $0, a workflow control rather than a statutory tax threshold. Flag every gain, loss, concession claim, stakeholder payment and proposed super contribution regardless of amount or certainty, including a nil calculated balance. There is no de minimis amount for an unknown legal condition, false election or missed deadline. Flag every unresolved condition, failed reconciliation and time-sensitive action. Any estimate must be supported, permitted by the applicable rule and labelled with its effect. No factual default can cure an unresolved source condition.

## Filing and payment

This guide prepares a concession workpaper, not a separate Division 152 return or a universal payment date. Establish the claimant's entity return, CGT schedule requirement, approved fields, lodgement due date, payment date and software for the actual year. Route the final net capital gain to the appropriate individual, company, trust or partnership workflow only after reconciliation and review. The approved 2027 return schedules, electronic specifications and complete filing procedures have not been verified here. Do not invent a label or treat a contribution date as the CGT event date.

Make CGT choices under s 103-25 by the day the relevant return is actually lodged, subject to any further time actually allowed. Keep the retirement amount and entity stakeholder percentages in writing under s 152-315. Maintain a separate deadline register for Division 152 payments, s 292-100 contribution categories, the receiving fund's election delivery and any replacement-period monitoring. A calendar reminder is not proof of payment or election.

For the currently linked blank NAT 71161, revision 06.2022, map Section A to the receiving fund/member reference, B to the individual's details, C to a payer acting on the individual's behalf where relevant, D to the specific concession, elected amount and look-through earnout question, and E to the actual declaration, signature and date. The PDF has 3 pages. It warns that an election after contribution is invalid. The receiving fund, not the ATO, receives it. Keep actual tax identifiers, signatures and private account details in the authorised filing/fund process; use redacted references in these workpapers. An employer obligation does not automatically become an eligible personal contribution. Reconfirm the approved form and fund process before use. [ATO form and instructions](https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-cap-election).

Deliver all 4 universal outputs required by [workflow-base](../../foundation/workflow-base.md): working paper, reviewer brief, action list and review checklist. The working paper must identify the owner/user/claimant/stakeholder/contributor, source periods, every gateway, group and MNAV schedules, active periods, participation/look-through tests, gross gain/loss ordering and each concession choice. Include separate lifetime retirement and super CGT cap reconciliations, signed-choice/payment/election evidence and rollover monitoring. The brief must distinguish known results, permitted estimates, source gaps and decisions withheld. The checklist adds the checks below to the universal checks and retains qualified reviewer sign-off.

### Revision record

Version 1.3, 2 November 2026: corrected alternate gateways, grouping, active-use and participation conditions, separated retirement payments from super cap elections and their deadlines, qualified future-law application, added 8 recomputing cases and completed the topical workflow controls. Tier 2 and pending professional review remain applicable. Version 1.2 was the structural template migration; it did not supply substantive sign-off.

## Completion checklist

- [ ] Each requested period and event/choice/payment/contribution date has applicable primary sources, including amendments and transitional application.
- [ ] Asset owners, users, claimants, group rights, affiliates, previous trust distributions and all alternate gateway results are evidenced.
- [ ] MNAV uses supported market values, permitted debts/provisions, correct connected-interest treatment and historical residential income use.
- [ ] Active periods, main use, 80%/modified look-through, stakeholder and significant-individual conditions are established independently of arithmetic.
- [ ] The 15-year test precedes capital losses; losses precede the eligible discount and active asset reduction; company and J-event restrictions are respected.
- [ ] Every retirement amount, previous use, stakeholder allocation, age test, required payment and written choice is reconciled.
- [ ] Fund acceptance, personal-contribution category, contribution-year available CGT cap, applicable deadline and timely NAT 71161 are separately evidenced.
- [ ] Rollover is recorded as deferred, with the common replacement period, expenditure, monitoring and later-event source holds; no recapture is duplicated.
- [ ] Return/schedule/software and tax/payment calculations are verified for the actual year; no example is treated as final tax payable.
- [ ] All 4 universal outputs identify unresolved items and the qualified reviewer has checked and signed the final position.

## Sources

| Source | URL | Read on |
|---|---|---|
| ITAA 1997 compilation 268, C2026C00471; selected Div 152 basic conditions, MNAV, active use, participation, death and all 4 concessions; ss 152-10 to 152-430, including formula-image alternative text in s 152-125 | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html> | 2026-11-02; selected operative sections, not the whole volume; compilation period 2026-10-01 to 2026-12-01 |
| Same compilation, selected ss 103-25 and 104-185/190/197/198; gain/loss and discount ordering reused from the CGT source review, not a fresh whole-volume review | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html> | 2026-11-02; choice and J-event sections read for this guide; broader CGT review retains its own scope |
| Same compilation, ss 292-100/105 contribution categories, election and individual cap adjustments | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html> | 2026-11-02; selected sections only; statutory required-lodgement date distinguished from ATO summary |
| Same compilation, ss 328-110/115/120/125/130 business, turnover, control and affiliates | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html> | 2026-11-02; selected sections only |
| Tax Reform No. 1 Act 2026, Sch 1 items 77A-82; active asset reduction gateway amendments and assessment application | <https://www.legislation.gov.au/C2026A00071/latest/text> | 2026-11-02; selected amendment/application provisions re-read, not a fresh whole-Act review |
| ATO eligibility overview, updated 28 January 2026; alternate gateways and partnership rights | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/cgt-concessions-eligibility-overview> | 2026-11-02; operative gateway and event-condition passages |
| ATO CGT small business entity, updated 6 June 2023; turnover routes, inclusions, exclusions and grouping | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/cgt-small-business-entity-eligibility> | 2026-11-02; selected operative passages, checked with ss 328-110/115/120 |
| ATO affiliates and special passive-asset spouse/child conditions, updated 6 June 2023 | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/small-business-affiliates> | 2026-11-02; operative definitions and special-rule passages |
| ATO connected entities, direct/indirect control and conditional Commissioner discretion | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/entities-connected-with-you-and-control-relationships> | 2026-11-02; selected control and discretion passages |
| ATO MNAV, related liabilities, exclusions and historical residence use | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/maximum-net-asset-value-test> | 2026-11-02; selected operative passages and residence example; no reuse of its rounded example as an exact formula |
| ATO active asset test, durations, rental use and connected-user attribution | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/active-asset-test> | 2026-11-02; selected operative passages and use examples |
| ATO additional share/trust conditions, participation, modified control and weighted look-through | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-cgt-concessions-eligibility-conditions/additional-conditions-if-the-cgt-asset-is-a-share-or-trust-interest> | 2026-11-02; selected operative passages and ownership/look-through examples |
| ATO 15-year exemption, updated 6 June 2023; continuous ownership, stakeholder payments and contribution summary | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-15-year-exemption> | 2026-11-02; selected operative conditions, payment and super passages; follow s 292-100 on contribution deadline wording |
| ATO active asset reduction, updated 6 June 2023; order, choice out and trust beneficiary treatment | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-50-percent-active-asset-reduction> | 2026-11-02; operative order, choice and beneficiary passages |
| ATO retirement exemption, updated 6 June 2023; written choices, ages, instalments, payments and cap-election separation | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-retirement-exemption> | 2026-11-02; operative conditions, payment/contribution and death passages |
| ATO rollover, updated 4 September 2025; choice before replacement, common replacement period and J2/J5/J6 | <https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/small-business-cgt-concessions/small-business-roll-over> | 2026-11-02; selected operative period and recapture passages |
| ATO contributions caps, updated 11 September 2026; Table 6 CGT cap amounts and indexation explanation | <https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps?anchor=CGTcapamount> | 2026-11-02; selected CGT cap table, including 2026-27 and 2025-26; other super acceptance rules not reviewed |
| ATO CGT cap election instructions, updated 14 November 2016; currently linked blank NAT 71161 revision 06.2022, 3 pages | <https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-cap-election> | 2026-11-02; operative instructions and all 3 native-text PDF pages, including fields, recipient and timing warning |

Not yet confirmed: Qualified Australian sign-off, complete historical and later operative compilations, individual residence/retirement/incapacity and valuation facts, actual trust/company rights, fund acceptance and non-concessional capacity, remedies for late actions, Commissioner determinations/extensions, approved 2027 return forms/software and the complete substantive template standard across the wider catalogue. An editing date, capture or passing arithmetic check does not resolve these dependencies.

> Contributed by Ryan Duguid.

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
