---
name: au-smsf
description: >
  Use this skill for Australian self-managed superannuation fund accounting, tax and compliance working papers for 2026-27 and the 2025-26 SMSF annual return. It covers trustee eligibility, fund residency, assessable contributions, exempt current pension income, NALI and NALE, contribution acceptance, pension minimums, transfer balance reporting, audits, levy and existing borrowing checks. Trigger on 'SMSF', 'self-managed super', 'SAR', 'ECPI', 'actuarial certificate', 'NALI', 'TBAR', 'minimum pension', 'bare trust' and 'SMSF audit'. Read the scope, source conditions and refusals before classifying transactions. It produces reviewer evidence and filing preparation; unresolved law, eligibility and procedures require Needs Input or qualified referral.
version: 1.5
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 calculations; 2025-26 SAR instructions; selected source conditions and unresolved evidence stated below"
last_updated: 2026-11-04
review_status: pending_review
depends_on:
  - workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Self-Managed Super Funds (SMSF) -- Accounting, Tax & Compliance Skill v1.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide prepares accounting, tax and compliance working papers for an Australian SMSF. Load [workflow-base](../../foundation/workflow-base.md) and its four output contracts. The reviewer is the customer: the result is a working paper, reviewer brief, action list and review checklist. Preparation does not authorise lodgment, payment, benefit release, an election or legal or financial product advice.

**Periods and source conditions.** Primary calculations are for 2026-27, 1 July 2026 to 30 June 2027. The filing instructions below concern the **2026 SAR for 2025-26**; do not reuse its labels for the 2027 SAR without reading that year's form. Check the law, amendments, application provisions, fund status and official instructions for the requested period. An editing date or successful page capture does not establish those conditions. The source table distinguishes selected readings, retained history and unresolved evidence.

**Law changes and routing.** Division 296 applies from 2026-27 under the Treasury Laws Amendment (Building a Stronger and Fairer Super System) Act 2026 and the separate Imposition Act. Member tax is outside this guide; fund earnings, attribution and reporting still require attention in section 5.3. Employer Payday Super obligations, receipt deadlines and exceptions belong to [au-super-guarantee](au-super-guarantee.md); the SMSF's allocation period is a separate rule. The general-expense NALE provisions use twice the non-arm's-length shortfall, subject to the statutory NALC calculation, and apply from 2018-19. For existing LRBAs, establish the arrangement date, asset definition and transitional treatment before applying the current business-real-property condition. Section 7 applies the amendment's actual commencement and maintaining/refinancing/acquisition exceptions, alongside the PCG's paired-date summary. [ATO Division 296](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/about-division-296-tax-for-smsfs); [LCR 2021/2](https://www.ato.gov.au/law/view/document?docid=COG/LCR20212/NAT/ATO/00001); [SIS Act s 67A](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67A).

Annual member caps and general transfer-balance figures have one home in [au-rates-2026-27](au-rates-2026-27.md); member contribution rules and employer SG are in [au-super-guarantee](au-super-guarantee.md). Route the small-business CGT cap election to [au-small-business-cgt](au-small-business-cgt.md), general CGT ordering to [au-capital-gains](au-capital-gains.md), member return consequences to [au-individual-return](au-individual-return.md) and residence questions to [au-tax-residency](au-tax-residency.md). A sibling link is not proof that its facts have been verified for this engagement.

**Scope boundary.** Do not recommend investments, products, pension commencement or commutation, contribution strategies, SMSF suitability or transaction structuring. This is this guide's hard scope limit. ASIC distinguishes licensed or authorised financial services from particular accounting, tax and other exemptions, subject to their conditions and warnings; the former specific accountants' exemption ended on 1 July 2016. Do not describe all SMSF services as requiring the practitioner personally to hold an AFSL. [ASIC INFO 216](https://www.asic.gov.au/for-finance-professionals/afs-licensees/apply-for-an-afs-licence/limited-financial-services/afs-licensing-requirements-for-accountants-who-provide-smsf-services).

This is a Tier 2 source-cited draft in the ryanduguid fork. The legacy closing block is retained as required; it does not mean that the upstream website publishes or verifies this fork's changes or that a professional has signed off this version.

## Ask the client first

1. Which fund, accounting year and SAR year are being prepared, and what proves Australian fund residence, ordinary central management and control, active-member status and complying status? Identify overseas trustees, management and contributions.
2. Who are the members, trustees and directors, what are their relationships and employment arrangements, and what do the deed, appointments, declarations, capacity and disqualification checks show?
3. What are each member's age, account phase, personal transfer balance history and verified total super balances at the relevant dates, including other funds? What contribution and benefit receipt/payment evidence exists?
4. Which assets, related parties, loans, leases, valuations, distributions and services appear in the trial balance, and what proves market terms, asset ownership, capacity and the income nexus?
5. Which ECPI method is legally available, what pension documents and actual payments support it, and what actuarial, audit and tax records establish every claimed condition or exception?
6. What are the fund's registration, lodgment, payment, RNN, prior-year and agent-program history, actual ATO due dates, audit completion, pending notices and proposed elections? Who will review and authorise each action?

### Evidence pack

#### Required inputs

**Minimum viable** -- trust deed and member list, trustee type (individual vs corporate), member ages and account phases (accumulation / retirement), trial balance or bank statements, prior-year SAR, and each member's TSB at 30 June 2026.

**Recommended** -- actuarial certificate (if proportionate), 30 June market valuations with evidence, contribution and pension payment schedules per member, TBAR lodgment history, LRBA loan agreement and amortisation schedule, investment strategy with last review date.

**Ideal** -- signed trustee declarations (NAT 71089), audit workpapers and prior auditor management letters, deed history including pension documentation, lease agreements for any related-party tenancy, insurance policy schedule.

## The method, step by step

### Section 1 -- Quick reference

**Run these steps in order.** (1) Confirm the fund, period and source conditions. (2) Check trustee eligibility, residence and complying status. (3) Reconcile bank, investment, contribution, pension and member records to the trial balance. (4) Separate assessable contributions, ordinary income, capital gains/losses and each NALI stream. (5) Establish ECPI eligibility and method, then apply the relevant income exclusion and deduction rules. (6) Compute taxable income, the statutory NALC and remaining low-tax component without mixing arm's-length losses into NALI. (7) Reconcile member cap flags, TBAR and Division 296 inputs without computing prohibited member taxes. (8) Reconcile fund tax, permitted offsets, instalments and levy to the correct SAR. (9) Deliver the four review outputs and follow Filing and payment only after authorisation.

| Field | Period and condition | Primary source or figure owner |
|---|---|---|
| Fund and period | Australian SMSF; 2026-27 calculations, 2026 SAR for 2025-26 filing | [ATO 2026 instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions) |
| Residence and complying status | Establish both before applying concessions; neither follows merely from an ABN | [s 295-95](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-95) |
| Low-tax component | 15% for a complying fund, after exemptions, deductions and component separation | [ATO fund tax](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed) |
| Discounted capital gains | One-third discount where eligible and asset held at least 12 months; losses and exclusions apply first | same |
| ECPI | Section 4.2 method, asset, benefit, payment and evidence conditions | [ss 295-385](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-385), [295-390](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-390) |
| NALC / non-complying income | 45%; do not confuse NALI with the final taxable NALC or compute non-complying asset amounts without review | [ATO fund tax](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed), [s 295-545](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-545) |
| No-TFN contributions | Additional 32% for a complying fund, with the statutory legacy-interest exception; the acceptance test is separate | [s 295-610](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-610), [ATO fund tax](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed) |
| Supervisory levy | Use the year-specific section D labels L, M and N and new/continuing/winding-up conditions in Filing and payment | [ATO 2026 section D](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13) |
| SAR due dates | Apply the fund's category, earlier notices, deferrals and separate payment date; Filing and payment below | [ATO 2026 lodging/payment](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return) |
| Audit | Appoint an approved SMSF auditor at least 45 days before the return due date; final signed report before lodging | [SIS Act s 35C](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/35C), [SIS Reg 8.02A](https://www.legislation.gov.au/F1996B00580/latest/text) |
| Members and trustee eligibility | Maximum 6; single-member, employee, representative and continuity conditions in section 3 | [SIS Act s 17A](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/17A) |
| Concessional / non-concessional caps | Annual cap and bring-forward figures are linked rather than repeated; verify prior-year balances and history | [au-rates-2026-27](au-rates-2026-27.md), [ATO caps](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps) |
| General / personal transfer balance cap | Annual general figure has one home; member's actual personal cap and account history govern | [au-rates-2026-27](au-rates-2026-27.md), [au-super-guarantee](au-super-guarantee.md) |
| Pension minimums | Section 6.1 age table, balance, rounding and commencement conditions | [SIS Regulations Schedule 7](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| TBAR | Quarterly event reporting for all SMSFs, subject to event and special-authority deadlines | [ATO TBAR rules](https://www.ato.gov.au/forms-and-instructions/superannuation-transfer-balance-account-report-instructions/when-to-lodge) |
| Existing LRBA checks | Section 7 safe-harbour terms, independent arm's-length evidence and application conditions; no structuring | [PCG 2016/5](https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001), [s 67A](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67A) |
| Division 296 | Fund-level earnings/attribution/reporting flag, not member-liability computation; section 5.3 | [ATO SMSF Division 296](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/about-division-296-tax-for-smsfs) |
| Corporate trustee cost | Section 3.2 gives the current proprietary special-purpose annual-review fee and eligibility check; verify the actual statement and fee date | [ASIC special-purpose companies](https://www.asic.gov.au/for-business-and-companies/companies/register-a-company/special-purpose-companies) |

**Conservative factual defaults and source stops**

| Ambiguity | Treatment and reviewer consequence |
|---|---|
| ECPI method, benefit prescription or certificate exception unknown | Needs Input; do not assume proportionate treatment, segregation or a certificate exemption |
| Minimum pension payment not verified | Hold the affected ECPI claim and obtain payment evidence; test each pension separately |
| Member TSB or cap history unknown | Hold carry-forward/bring-forward and member-cap conclusions; ask for dated evidence from all relevant funds |
| Related-party transaction or service | Flag for the s 65 / s 66 / Part 8 / NALI screen before classification; no assumed exception |
| Valuation support missing | Needs Input on the affected asset, member balance, cap and return positions |
| Contribution close to year end | Establish actual fund receipt and legal contribution character; a payer bank label is insufficient |
| Auditor appointment or completion unknown | Establish appointment date, actual due date and final signed report before treating the SAR as lodgeable |
| Member age or release condition unknown | Hold acceptance, pension and benefit conclusions; never assume a lawful release |
| Residence, complying status, operative law or filing procedure unresolved | Needs Input or referral; a higher-tax assumption cannot establish unknown law |

**Residency gate.** Section 295-95 requires establishment in Australia or an Australian asset, ordinary Australian central management and control and the active-member conditions. Apply the statutory temporary-absence rule and each relevant membership/contribution test. Australian-superannuation-fund status alone does not prove all complying-status conditions. Overseas management, residence or contributions require review before applying concessions; do not automatically direct a wind-up. [s 295-95](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-95); [ATO residency](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/setting-up-an-smsf/check-your-smsf-is-an-australian-super-fund).

### Section 3 -- Fund structure and registration

#### 3.1 Definition of an SMSF (SIS Act s 17A)

- **Maximum 6 members**, increased from 4 on 1 July 2021. Check every applicable condition in s 17A, including the representative exceptions.
- **Individual trustees:** ordinarily every member is a trustee and every trustee a member. A single-member fund has 2 individual trustees: the member and another person who is a relative **or** whose employee the member is not.
- **Corporate trustee:** ordinarily every member is a director and every director a member. A single-member fund may have the member as sole director, or 2 directors including the member; the other director must be a relative **or** the member must not be that director's employee.
- The member-to-member employee restriction has a relative exception. Apply the extended employee provisions in s 17A, including their single-member operation; do not replace the statutory tests with a simple payroll-name comparison.
- A trustee/director must not be remunerated for trustee duties. Section 17B permits specified other-capacity services only where the person is appropriately qualified, holds necessary licences, performs them in the ordinary course of a business offering similar services to the public and charges no more than an arm's-length amount. Preserve the separate Public Trustee-related statutory alternatives.
- No person acts **whilst disqualified**. Check s 120, appointment eligibility and the ATO register; a pending application does not itself remove disqualification. A specific waiver under s 126D has conditions and does not override other disqualifying grounds.
- Section 17A(3) permits particular substitutions: the deceased member's legal personal representative for the specified death-benefit period, a representative for legal disability or under an enduring power of attorney, and a parent/guardian for a minor in the statutory circumstances. The substitute must actually occupy the required trustee/director position; possession of a document alone is insufficient.

Sources: [SIS Act s 17A](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/17A), [s 17B](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/17B), [s 120](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/120) and [s 126D](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/126D).

#### 3.2 Individual vs corporate trustee

| Factor | Individual trustees | Corporate trustee |
|---|---|---|
| Ongoing company cost | No company annual review fee merely for acting individually | A qualifying proprietary special-purpose company has a $70 annual-review fee from 1 July 2026; verify special-purpose status, the actual annual statement and the fee table for the review date. Other company fees and professional costs are separate. [ASIC current annual-review fee table](https://www.asic.gov.au/for-business-and-companies/forms-and-fees/all-fees/fees-for-commonly-lodged-documents) |
| Membership change | Review and retitle assets as legally required | Company remains owner; update directors and other required registrations |
| Administrative penalties | Each person who contravenes the relevant duty can be liable personally | Check which duty and person contravened; where the body corporate is liable, directors are jointly and severally liable for its penalty under s 169 |
| Single-member structure | Needs a second eligible trustee | Sole director, or the qualifying two-director structure in section 3.1 |
| Death/incapacity and succession | Test permitted representative substitutions and continuity rules | Directorship and representation still require lawful appointments; continuity is not automatic |

Section 17A(4) provides a limited continuity period ending at the earlier of RSE-licensee appointment and 6 months after the fund would otherwise cease to qualify. Under subsection (5), it generally does not apply if admitting a new member was a reason for failure, except for the purposes of s 29J. Do not treat this as a blanket grace period for any breach or assume death/incapacity automatically destroys the structure. [s 17A(3)-(5)](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/17A).

Worked case 5 preserves the original 60-unit comparison using a dated hypothetical unit input. Use the penalty-unit home in [au-lodgment-deadlines-penalties](au-lodgment-deadlines-penalties.md); check the relevant provision, contravening person, offence date and any remission rather than applying one figure to every breach. [SIS Act s 166](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/166), [s 169](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/169).

#### 3.3 Registration checklist (new fund)

1. Establish the deed, lawful trustees/directors and initial trust assets. Distinguish legal establishment from merely obtaining identifiers.
2. Each new trustee/director signs approved declaration NAT 71089 within 21 days. Existing trustees/directors must ensure an incoming person signs. An education-direction case has its own 21-day requirement after course completion. Retain the declaration **whilst relevant and for at least 10 years**, and make it available for regulator inspection. [s 104A](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/104A).
3. Complete the TFN/ABN process and distinguish it from the SIS s 19 election to be regulated, ordinarily made within 60 days after establishment. The election is irrevocable; verify the approved process and any extension rather than treating every registration step as the same deadline. [s 19](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/19).
4. Establish a fund bank account and keep fund money/assets separate under reg 4.09A. Check the actual legal title and trustee capacity. [SIS Regulations](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html).
5. Establish working electronic service address, bank and SuperStream details for applicable contributions and rollovers. Apply the relevant exceptions and employer obligations in [au-super-guarantee](au-super-guarantee.md); do not assume an ESA proves a valid transaction.
6. Formulate, regularly review and give effect to an investment strategy addressing risk/return, diversification, liquidity, existing/prospective liabilities and whether to insure members. An annual documented review and significant-event review are working-paper controls, not a substitute for the statutory 'regularly' requirement. [reg 4.09](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html).
7. If no assets were held, apply the written cancellation/RNN process and conditions in Filing and payment. No assets does not itself cancel a filing obligation; the winding-up exception matters.

### Section 4 -- Fund taxation (ITAA 1997 Div 295)

#### 4.1 Rate structure

| Income class | Treatment | Primary source and conditions |
|---|---|---|
| Assessable contributions | Normally 15% in a complying fund; verify employer, salary-sacrifice and deductible personal contribution classification and any valid s 290-170 notice | [ATO: How SMSFs are taxed](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed); the member cap assessment is separate |
| Ordinary accumulation earnings | Normally 15%, after permitted deductions, losses and offsets | [ATO: How SMSFs are taxed](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed); classify interest, rent, dividends and trust income separately |
| Discount-eligible fund capital gain | The fund discount is one-third, not the individual's 50%; a 15% rate on the discounted gain gives 10% of the gross gain only in the simple accumulation example without other adjustments | [ATO: How SMSFs are taxed](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed); verify the asset was owned for at least 12 months, losses, NALI and ECPI treatment |
| ECPI | Exempt only to the extent the chosen statutory method and all conditions apply | [ss 295-385](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-385) and [295-390](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-390); Section 4.2 |
| Non-arm's length component | 45%; distinguish actual NALI and the capped general-expense calculation | [ATO: How SMSFs are taxed](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed), [s 295-545](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-545); Section 4.3 |
| Non-complying fund | Generally 45% on taxable income; the previously complying or previously foreign fund inclusions are additional assessable amounts, not automatically 45% of every asset | [ATO: How SMSFs are taxed](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed), [s 295-320](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-320) |
| No-TFN contributions | Additional 32% for a complying fund or 2% for a non-complying fund where the no-TFN rules apply, producing 47% total in either case; test the legacy exception separately | [ATO: How SMSFs are taxed](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed), [ss 295-610](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-610) and [295-615](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-615); Section 5.1 |

For a fund that was complying in the previous year and is non-complying in the current year, [s 295-325](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-325) measures the additional inclusion using asset market values just before the current year, less the specified post-June-1983 crystallised undeducted contributions and contributions segment for current members so far as not deducted and not deductible. Obtain the actual components and the notice; do not substitute total assets or assume every non-complying fund has this same inclusion.

A complying fund's eligible Australian franking credits can offset tax and any excess can be refundable. Verify entitlement, including the qualified-person/holding-period rules, and gross up the income where required. The blanket refund rule does not extend to non-complying funds; nor are New Zealand imputation credits Australian franking credits. [s 67-25](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/67-25), [2026 SAR section D, E1](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13).

Capital losses ordinarily offset capital gains, not other income. Preserve eligible carried-forward losses and separate non-arm's length losses in the return working paper. A gain or loss on a segregated current pension asset is generally disregarded under [s 118-320](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-320), but subsection (2) disapplies that exclusion to a gain that would be NALI if assessable. Do not erase a NALI gain on the strength of the pension asset label. A later TFN can support an offset for extra no-TFN tax paid in one of the previous 3 income years, subject to entitlement; use the actual first-quotation year and [2026 SAR section D, E2](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13), rather than assuming an automatic refund.



#### 4.2 ECPI -- exempt current pension income

**Establish eligibility before choosing a method.** Identify the retirement-phase benefits, asset support, account balances, pension standards, year and any disregarded-small-fund-assets rule. Neither an unknown method nor a high exempt percentage permits an assumed exemption.

**Segregated current pension assets, s 295-385.** The statutory asset definition has an actuarial-certificate route and a separate prescribed-benefit route. The latter depends on liabilities throughout the year being for prescribed retirement-phase income-stream benefits; regulation 295-385.01 prescribes allocated, market-linked and account-based benefits and the specified death-benefit rights. Check the actual benefit against the legislation. Assets beyond the relevant supporting account-balance value are excluded. Do not say every segregated pension is certificate-free. The income exemption excludes NALI and Subdivision 295-C amounts, including assessable contributions. Check capital gains/losses separately under s 118-320. [s 295-385(1)-(6)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-385); [reg 295-385.01](https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html).

**Whole-year method choice.** Section 295-385(8)-(10) permits a whole-year choice to treat assets as non-segregated where its conditions are met, including a time when all interests are retirement-phase interests. It excludes the specified whole-year retirement-phase and whole-year DSFA situations. Record the lawful choice and evidence; no unrestricted election is available. [s 295-385](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-385).

**Proportionate ECPI, s 295-390.** Use the statutory average-liability proportion for eligible unsegregated income. Obtain the required actuarial evidence before lodgment. The section includes valuation alternatives and a prescribed-benefit exception; do not claim an exception without establishing its actual prescription and conditions. NALI and assessable contributions are excluded. Apportion expenses by their proper nexus; costs of earning exempt income are generally not deductible, whilst specific deduction provisions can differ. [s 295-390](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-390); [ATO fund tax and deductions](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed).

**Disregarded small fund assets, s 295-387.** The fixed prior-year TSB test is **over $1.6 million**, not an indexed transfer balance cap. Apply all predicates: the statutory small-fund condition, a retirement-phase super interest during the year, the person's prior-year-end TSB and retirement-phase-recipient status and their interest in this fund during the year. The exception concerns assets that would otherwise be segregated current pension assets throughout the year. A bare '100% retirement phase' label is insufficient. If assets are DSFA they cannot be segregated current pension assets; obtain the applicable proportionate evidence. [s 295-387](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-387).

**Minimum-payment condition.** Verify each pension's actual payment standards. A shortfall ordinarily prevents ECPI for that pension for the year, subject to the limited ATO exception in section 6.1. Do not automatically deny every other pension's exemption. [ATO minimum-payment exception](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/paying-smsf-benefits/income-stream-pension-rules-and-payments/exception-to-minimum-pension-payment-requirements).

#### 4.3 NALI and NALE -- **AUDIT FLASH POINT**

**AUDIT FLASH POINT**

1. Identify the scheme, parties, dealing and relevant income. Section 295-550 has distinct routes for excessive income, specific non-arm's-length expenditure, private-company dividends, non-fixed trust entitlements and fixed entitlements. A private-company dividend, and income attributable to it, is NALI unless consistent with arm's-length dealing after applying the statutory share-value, cost, dividend and other factors. Do not assume all private dividends are NALI. The conditional unfranked-dividend comparison remains in worked case 7. [s 295-550(1)-(7)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-550).

2. For specific expenditure, establish its nexus to each income stream and period. Non-arm's-length acquisition costs, including financing, can affect asset income and a later disposal gain despite subsequent arm's-length refinancing. A non-acquisition expense whose nexus is limited to a particular year's income does not automatically taint later years. Do not generalise that all maintenance or renovation discounts leave disposal gains unaffected: the ruling distinguishes property management from substantial renovation. [LCR 2021/2, paras 17-21 and examples 4, 9 and 11](https://www.ato.gov.au/law/view/document?docid=COG/LCR20212/NAT/ATO/00001).

3. For a qualifying general expense under s 295-550(8), NALI is **2 × (arm's-length expense − amount actually incurred)**. If no expense is incurred, subsection (9) uses twice the expected expense. This is expenditure with the requisite general income nexus, not expenditure relating to particular assets. Accountancy and actuarial costs for complying with or managing income-tax affairs, ordinarily deductible under s 25-5, are excluded from the ruling's listed general-expense examples. Classify the actual service, not its invoice heading. The NALE amendments operate from 2018-19; large APRA funds' expenditure exemption does not remove their other NALI rules. [s 295-550(8)-(9)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-550); [LCR 2021/2, paras 6B-8C, 19-21](https://www.ato.gov.au/law/view/document?docid=COG/LCR20212/NAT/ATO/00001).

4. Compute the SMSF's **NALC**, not merely the general-expense NALI amount. Under s 295-545(2A), take the lesser of: (a) other/specific NALI less its attributable deductions, **plus** general-expense NALI; and (b) taxable income **minus** assessable contributions **plus** deductions attributable to those contributions. Do not deduct the actual general expense again from the twice-shortfall amount. The remaining taxable income is the low-tax component. Apply the appropriate component rates after this calculation; NALI is not sheltered by ECPI. [s 295-545](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-545); [LCR 2021/2, paras 6B-7, 20A](https://www.ato.gov.au/law/view/document?docid=COG/LCR20212/NAT/ATO/00001).

5. Establish the service provider's capacity and commercial dealing. Unpaid work genuinely performed as trustee, including the original own-equipment example, does not itself create NALE. Weigh charging, material business equipment, required professional qualifications/licences and business insurance. Minor incidental business-equipment use alone is not decisive. An ordinary commercial staff discount, available to all staff and uninfluenced by the trustee, can remain arm's length; independently decided pro bono work can too. Non-commercial undercharging by the trustee's firm is different. [LCR 2021/2, paras 44-60](https://www.ato.gov.au/law/view/document?docid=COG/LCR20212/NAT/ATO/00001).

6. The historical PCG 2020/5 general-expense compliance approach is not an enduring exemption. Verify its covered periods and exclusions before using it for a historical year; do not apply transitional relief to 2026-27. [PCG 2020/5](https://www.ato.gov.au/law/view/document?docid=COG/PCG20205/NAT/ATO/00001).

### Section 5 -- Contributions

#### 5.1 Acceptance (SIS Reg 7.04)

| Condition | Fund acceptance and action | Official source |
|---|---|---|
| Member under 75 | Employer and member contributions may be accepted subject to all other rules; acceptance and a personal deduction are different tests | [reg 7.04(1)](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Member 75 or older | Ordinary table permits mandated employer and downsizer contributions; the grace window and statutory special rules below must be considered | same |
| Grace window | Non-mandated employer and non-downsizer member contributions can be received **on or before 28 days after the end of the month the member turns 75** | [reg 7.04(1A)](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html) |
| No member TFN quoted | Do not accept ordinary member contributions; the regulation expressly excepts PPL superannuation contributions. Mandated employer no-TFN taxation is a separate question | [reg 7.04(2)](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Amount received inconsistently with the specified acceptance rules | Return within 30 days of awareness, subject to the TFN-quoted-within-30-days exception and the regulation's permitted adjustments. Do not confuse this return rule with contribution allocation | [reg 7.04(4)-(5)](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Special timing / earnout cases | Subregulations (6) and (6A) contain additional conditions for a contribution relating to an earlier eligible period and specified CGT look-through earnout amounts; refer before relying on either | [reg 7.04](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html) |

A complying fund's additional no-TFN tax is 32%. Section 295-610 excludes an amount where the super interest existed before 1 July 2007 and the relevant contributions included in assessable income for the year do not exceed $1,000. Worked case 9 preserves the eligible employer-contribution illustration. The tax exception does not override reg 7.04 acceptance rules. Section 295-615 defines when a TFN is quoted or taken to be quoted. Use the separate no-TFN offset entitlement and 3-prior-year conditions in 2026 SAR section D, E2; do not assume merely receiving a TFN guarantees a refund. [s 295-610](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-610), [s 295-615](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-615).

**Personal deductions and special contributions.** Acceptance does not prove deductibility. For a contribution made from the day the member turns 67 through the day 28 days after the end of their 75th-birthday month, s 290-165(1A) requires gainful employment for at least 40 hours in a 30-consecutive-day period in that income year, or the qualified recent-retiree exception. That exception requires the corresponding work in the previous income year, prior-year-end TSB below $300,000 and satisfaction of both previous-use restrictions in paragraphs (b)(iii)-(iv). It is not a fresh exemption every year. Apply the displayed remedial-power modification for covered employees where relevant, and refer before relying on it. A person under 18 at year end also needs the specified business or employee income condition; contributions after the statutory maximum-age window are not deductible. [s 290-165](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/290-165). The valid notice of intent, acknowledgement and other deduction conditions remain separate; see [au-super-guarantee](au-super-guarantee.md).

For a **downsizer contribution**, use the age and individual amount home in [au-rates-2026-27](au-rates-2026-27.md), applied **per person** and subject to the actual proceeds and previous eligible contributions. Section 292-102 additionally requires the relevant Australian dwelling interest held by the person/spouse immediately before disposal, the qualifying main-residence CGT treatment (including its stated pre-CGT alternative), the 10-year ownership/land/replacement-dwelling conditions, and a dwelling other than a caravan, houseboat or mobile home. Contribute within 90 days of the change of ownership unless the Commissioner allows longer, and provide the approved choice to the fund at or before contributing. Check the previous-property choice restrictions and same-interest/related-spousal-interest qualifications; a simple once-only label must not erase those qualifications. The proceeds cap takes both spouses' relevant contributions into account. [s 292-102](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/292-102). Reg 7.04 expressly accommodates downsizer contributions beyond the ordinary age limit. Apply the verified cap, deduction and TSB treatment below only after establishing those eligibility conditions.

A qualifying downsizer contribution is neither a concessional nor a non-concessional contribution, so it does not use either ordinary contribution cap. It is not deductible. A member's existing TSB does not prevent an otherwise eligible downsizer contribution, but the contribution remains part of their TSB when that balance is calculated; do not confuse this with a transfer-balance-cap exemption. Use the applicable balance date and valuation rules. [LCR 2018/9 paragraphs 5-12](https://www.ato.gov.au/law/view/document?docid=COG/LCR20189/NAT/ATO/00001), [s 292-90(2)(c)(iiia)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/292-90), [s 290-167](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/290-167), [ss 307-230](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/307-230) and [307-230A](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/307-230A).

The indexed small-business CGT cap, qualifying 15-year/retirement proceeds, approved election at/before payment, statutory contribution deadline and remaining lifetime capacity belong to [au-small-business-cgt](au-small-business-cgt.md), which retains those operative conditions. Do not route work-test or full downsizer eligibility to a sibling that supplies only general contribution rules.

**Allocation timing is separate.** For an SMSF contribution **not made to a defined benefit interest**, reg 7.07H ordinarily requires allocation within 28 days after month end, or a longer period reasonable in the circumstances. Establish and document any longer period. This is not a rule allowing all invalid contributions to be retained or rejected on that same timetable. The ordinary three-business-day rule for other funds and employer Payday Super receipt rules do not replace this SMSF allocation rule. [reg 7.07H](https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO SMSF allocation explanation](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/managing-superstream/how-payday-super-affects-smsfs).

#### 5.2 Caps (2026-27)

Annual concessional/non-concessional caps, bring-forward bands, annual general transfer-balance cap and indexed amounts have one home in [au-rates-2026-27](au-rates-2026-27.md). Member contribution mechanics belong to [au-super-guarantee](au-super-guarantee.md). Verify the current [ATO contributions caps](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps), prior 30 June TSB, every fund's contributions, existing bring-forward period and previous usage before using an owner figure.

Preserve the separate conditions: carry-forward uses up to 5 prior years' unused concessional cap and its prior-year TSB eligibility test; non-concessional bring-forward depends on the relevant prior-year TSB band and eligibility history, and is not automatically available merely because a contribution is below the annual cap. The original 2026-27 and 2025-26 annual figures and all four bring-forward bands are routed to the owner instead of repeated here.

**Excess flows.** Excess concessional contributions enter the member's assessable income with a 15% non-refundable offset; the fund's correctly classified assessable contribution is not undone by member excess status. Worked case 3 preserves the member/fund distinction, release fraction, election and authority process. The excess concessional contributions charge applied for 2013-14 through 2020-21 and ceased from 1 July 2021; do not add it to a current-year ECC calculation. Correct real fund-reporting errors through the applicable complete adjustment/amendment process, rather than deleting a correct contribution. [s 291-15](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/291-15), [ATO concessional contributions cap](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap).

Excess **non-concessional** contributions have a separate member determination and election. The ordinary 60-day choice is irrevocable. Option 1 releases all the excess plus 85% of ATO-calculated associated earnings; the associated earnings are included in the member's taxable income with a 15% non-refundable offset. Option 2 retains the excess and subjects it to ENCC tax, currently 47%; it does not merely leave the amount taxed as ordinary fund earnings. A processed authority ordinarily requires the fund to pay the ATO within 10 business days. If no election is received, the ATO ordinarily applies option 1, with the stated defined-benefit-only exception applying option 2. Associated earnings use the ATO proxy calculation, not necessarily the fund's actual return. Insufficient releasable money, another-fund election and defined-benefit situations require their specific instructions. Refer the member's choice and calculation; do not release funds before the valid authority or assume general NCC-cap figures establish the excess. [ATO NCC cap, excess and release options](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/non-concessional-contributions-cap).

The original June-quarter/July employer-contribution proposal is not applied as law. Refresh its legislative status with [au-super-guarantee](au-super-guarantee.md) and primary parliamentary sources before relying on any exclusion; the old 31 October status is retained in Sources.

#### 5.3 Member surcharges -- flag, never compute

- **Division 293:** the ATO assesses the tax to the member, separately from fund contributions tax. Route its income components, threshold, contribution calculation and assessment/release treatment to [au-super-guarantee](au-super-guarantee.md). Flag the member issue; do not compute their liability here.
- **Division 296:** route indexed member thresholds/rates to [au-rates-2026-27](au-rates-2026-27.md). The ATO describes a tax on taxable super earnings plus an additional component for very large balances; do not add the original combined higher-rate shorthand on top of the first rate. For 2026-27, the closing TSB test applies; later years can use opening or closing TSB. Division 296 disregards the specified LRBA amounts in TSB. An interest below the large-balance threshold in this SMSF does not exclude a member with other super interests. Ask for those interests. Member tax is assessed to the individual and may be paid personally or released under the applicable process; this guide does not compute it.
- **Fund duties remain.** The SMSF calculates Division 296 fund earnings, attributes relevant earnings to each in-scope member and reports from the 2026-27 SAR onwards. Attribution differs for accumulation and defined-benefit interests. An actuary is generally required subject to actual exceptions, including nil earnings and the qualifying single-member conditions in reg 296-65.03(6); verify each condition before claiming an exception. If omitted, an ATO notice requires amendment; an agent generally receives it through Online services for agents. Obtain dated market values, member balances and supporting calculations. Escalate the fund-level calculation and attribution rather than omitting the reporting duty.
- **Small-fund CGT adjustment choice.** The choice covers all **CGT assets** held at the end of 30 June 2026, ordinarily directly held, with the custodian/tax-look-through treatment described by the ATO. It adjusts the first cost-base/reduced-cost-base element to that date's market value and the other existing elements to nil for Division 296 fund earnings only, without changing ordinary fund income tax. The choice is irrevocable and due by the 2026-27 SAR lodgment due date. Check the actual approved-form information; the September newsroom also describes using another format containing the same information. The ATO says it need not be submitted. Keep the choice and each affected asset's cost-base records in English or convertible form for 5 years after certainty that no further CGT event can occur for any covered asset. Verify the full statutory election and record conditions before acting.
- **Currency stop.** The captured ATO pages describe guidance under development in June/September 2026. That is historical publication context, not proof that guidance remains unpublished today. Establish current operative guidance and the 2027 SAR fields before any fund-level calculation or filing; unresolved evidence requires Needs Input. No Division 296 member-tax calculation is authorised by this guide.

Sources: [ATO About Division 296 tax for SMSFs](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/about-division-296-tax-for-smsfs); [ATO September newsroom](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-newsroom/division-296-tax-the-latest-for-smsfs); [Income Tax Assessment Regulations, reg 296-65.03](https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html); [Treasury Laws Amendment Act 2026, Schedule 1](https://www.legislation.gov.au/C2026A00008/asmade/2026-03-13/text/original/epub/OEBPS/document_1/document_1.html).

### Section 6 -- Pensions

#### 6.1 Account-based pension minimums

Compute the Schedule 7 amount from the relevant account balance and age at 1 July, or at commencement in the commencement year. Account balance can require the higher withdrawal benefit under the Schedule's definition. The formula is account balance multiplied by the percentage factor. These are the ordinary current factors; the temporary reductions listed for earlier years do not apply to 2026-27.

| Age at the relevant date | Percentage factor | Primary source |
|---|---|---|
| Under 65 | 4% | [SIS Regulations, Schedule 7](https://www.legislation.gov.au/F1996B00580/latest/text) |
| 65-74 | 5% | [Schedule 7](https://www.legislation.gov.au/F1996B00580/latest/text) |
| 75-79 | 6% | [Schedule 7](https://www.legislation.gov.au/F1996B00580/latest/text) |
| 80-84 | 7% | [Schedule 7](https://www.legislation.gov.au/F1996B00580/latest/text) |
| 85-89 | 9% | [Schedule 7](https://www.legislation.gov.au/F1996B00580/latest/text) |
| 90-94 | 11% | [Schedule 7](https://www.legislation.gov.au/F1996B00580/latest/text) |
| 95 or more | 14% | [Schedule 7](https://www.legislation.gov.au/F1996B00580/latest/text) |

For a commencement after 1 July, pro-rate for days that include and follow the commencement day. A commencement on or after 1 June requires no payment for that financial year. Round the amount to the nearest $10, rounding an exact $5 upwards. [Schedule 7, clauses 1, 3-5](https://www.legislation.gov.au/F1996B00580/latest/text). Reconcile actual pension payments by 30 June to bank and member receipt evidence; a journal entry alone does not establish payment. Retain the pension terms, condition of release and commencement documents. A non-retirement-phase TRIS earns no ECPI and has a 10% maximum; the minimum-payment exception does not cure exceeding that maximum. [ATO pension exception guidance](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/paying-smsf-benefits/income-stream-pension-rules-and-payments/exception-to-minimum-pension-payment-requirements).

**Shortfall and continuation.** Test each pension separately. Without the exception, an underpaid pension ceases for income tax purposes at the start of the year and loses ECPI for that interest for the whole year; payments are treated as lump sums. Do not assume a later payment cures this, an unaffected member's pension also fails or old pension documents automatically restart a complying income stream. Refer the cessation, fresh commencement documentation, component values and any transfer balance credits/debits and TBAR corrections for qualified review.

The ATO exception requires an honest mistake causing a small underpayment or circumstances outside the trustee's control, otherwise available ECPI if relevant, a timely catch-up that would have met the prior-year minimum and consistent prior-year treatment for all other purposes. A small underpayment is no more than one-twelfth of that pension's annual minimum. **If it exceeds one-twelfth, write to the ATO**, including where the asserted cause was outside the trustee's control; the outside-control branch does not justify self-assessing this larger shortfall. Prior use through self-assessment or Commissioner discretion also requires an application. [ATO: conditions, small underpayment and requesting the exception](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/paying-smsf-benefits/income-stream-pension-rules-and-payments/exception-to-minimum-pension-payment-requirements).

For an honest error, the ATO generally treats payment within 28 days after awareness as as soon as practicable. For an outside-control cause, the comparable period starts when the trustee is in a position to be aware. Confirm the payment occurred in the following income year and met the other conditions; do not merge those awareness tests. With no prior use and all conditions met, self-assessment can be available. Otherwise obtain ATO consideration rather than recording relief as granted. An application should identify every affected pension, factor, minimum, amount paid, shortfall, discovery date and cause, with fund and member payment evidence, liquidity at year end, prior failures/concessions, prevention measures and the tax difference with and without relief. [ATO exception guidance](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/paying-smsf-benefits/income-stream-pension-rules-and-payments/exception-to-minimum-pension-payment-requirements).

#### 6.2 Transfer balance cap and TBAR

Use the general cap home in [au-rates-2026-27](au-rates-2026-27.md) and the member's actual ATO transfer balance account. The general cap is not the member's personal cap; proportionate indexation depends on their history.

All SMSFs report transfer balance events quarterly, with the ordinary report due within 28 days after quarter end. No event means no nil report. Earlier deadlines can override the quarterly cycle: a voluntary commutation in response to an excess transfer balance determination is reported within 10 business days after the end of its month; a response to a commutation authority is due within 60 days of its issue, using the notice's actual due date. [ATO: event-based reporting](https://www.ato.gov.au/forms-and-instructions/superannuation-transfer-balance-account-report-instructions/when-to-lodge). The quarterly rule has applied to all SMSFs since 1 July 2023, without the earlier balance-based annual-reporting distinction.

Identify retirement-phase commencements and values, commutations including pre-rollover commutations and excess corrections, relevant LRBA repayment value shifts and personal injury/structured settlement contributions. Ordinary pension payments and investment earnings are not themselves reportable transfer balance events. Reconcile event dates, identifiers and values, including other funds; mismatched reporting can generate an incorrect excess determination. Do not postpone an authority response until quarter end, nor treat a commutation authority as an instruction to withdraw an amount without checking its terms. [ATO: event-based reporting](https://www.ato.gov.au/forms-and-instructions/superannuation-transfer-balance-account-report-instructions/when-to-lodge).



### Section 7 -- Investment and prohibited-transaction rules

| Control | Accounting/compliance check | Primary source |
|---|---|---|
| Sole purpose | Check the permitted core and ancillary purposes, including retirement/death benefits. Escalate current member enjoyment of fund property, art or wine; the guide does not authorise private use | [SIS Act s 62](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/62) |
| Member/relative assistance | Do not make a loan or give financial assistance using fund resources to a member or relative. A proposed temporary loan is not an exception. Classify any contravention and the liable person before applying a penalty | [s 65](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/65), [s 166](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/166) |
| Related-party acquisitions | Apply the prohibition and exact exception, including listed securities or business real property at market value and the limited in-house-asset exception. Market value alone does not authorise every related-party asset or transaction | [s 66](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/66) |
| In-house assets | Identify related-party loans, investments and leases and all statutory exclusions. Apply the acquisition restriction as well as the 30 June market-value ratio. The 5% limit is not permission to lend to a member. If the year-end ratio exceeds the limit, prepare and carry out the statutory disposal plan during the next income year. A business-real-property lease exclusion requires its actual statutory conditions | [s 71](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/71), [s 82](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/82) and Part 8 |
| Borrowing | Escalate an overdraft, margin loan or other borrowing outside an established exception. Short-term beneficiary-payment and securities-settlement exceptions have narrow purpose, amount and timing conditions; they are not general cash-flow facilities. A documented LRBA needs a single acquirable asset, compliant holding/recourse terms and permitted repairs, refinancing and replacements | [s 67](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67), [s 67A](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67A), [s 67B](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67B) |
| Market value | Use objective supportable evidence for the annual market-value accounts; investigate property, private companies and unlisted trusts rather than carrying forward an unsupported amount | [SIS Reg 8.02B](https://www.legislation.gov.au/F1996B00580/latest/text) |
| Strategy and asset separation | Give effect to and regularly review the investment strategy, addressing risk, return, cash flow, diversification, liquidity, liabilities and member insurance. Document significant-event reviews and an annual review as a working-paper control; annual frequency is not a substitute for the regulation's regular-review duty. Keep fund money/assets separate | [SIS Regs 4.09 and 4.09A](https://www.legislation.gov.au/F1996B00580/latest/text) |

**LRBA date and terms.** The business real property condition in s 67A(2)(c) is subject to the [Tax Reform No. 1 Act 2026, Schedule 5 items 1-2 and commencement table item 7](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html). It applies to arrangements entered into on or after **10 August 2026** under which money is borrowed, or borrowings are maintained, for acquiring assets. It does not apply to such an arrangement **to the extent** that it maintains or refinances a borrowing under another arrangement entered into before commencement, or the asset acquisition happens under an arrangement entered into before commencement. The statutory note expressly preserves the latter branch even where settlement occurs after commencement. This is an exception to the new business-real-property amendment, not permission to disregard the other s 67A conditions. Obtain both arrangement and acquisition records and review later changes; do not assume every refinancing, replacement asset or altered arrangement qualifies. [PCG 2016/5 footnote 1](https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001), updated 19 October 2026, summarises the paired-date position. New structuring remains R-AU-SF-3.

PCG safe harbours are an ATO compliance approach, not a substitute for SIS compliance. Falling outside them does not automatically make the arrangement non-arm's length: retain evidence of comparable commercial terms and refer the NALI question. Apply all relevant terms throughout the borrowing:

| Existing documented LRBA | Safe-harbour terms to check | Primary source |
|---|---|---|
| Real property | Current-year variable rate 9.35% for 2026-27 (2025-26: 8.95%); 70% maximum LVR; 15-year maximum total term, with previous borrowing duration deducted on refinancing; permitted fixed period no more than 5 years; registered mortgage; monthly principal and interest repayments; written executed agreement | [ATO LRBA rates](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/other-super-rates-and-thresholds), [PCG 2016/5, Table 1](https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001) |
| Collection of listed shares/units | Current-year variable rate 11.35% for 2026-27 (the real-property rate plus 2 percentage points); 50% maximum LVR; 7-year maximum total term with previous borrowing duration deducted on refinancing; permitted fixed period no more than 3 years; registered charge/mortgage or similar security; monthly principal and interest repayments; written executed agreement | [ATO LRBA rates](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/other-super-rates-and-thresholds), [PCG 2016/5, Table 2](https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001) |

For fixed rates use the permitted May-before-commencement basis and subsequent transition rules in the relevant PCG table, rather than resetting an eligible fixed loan to today's variable rate. The guideline specifies monthly compounding. Test the aggregate borrowing and the applicable valuation date for LVR, not a fresh annual valuation chosen to make the ratio pass. These checks do not establish that acquiring the asset, the LRBA or related-party terms are lawful.



### Section 8 -- Compliance calendar (2025-26 SAR season, 2026-27 year)

| Timing | Obligation and evidence | Primary source |
|---|---|---|
| Not later than 45 days before the required SAR lodgment day | Appoint an approved SMSF auditor registered with ASIC. An earlier required SAR date brings appointment forward | [SIS Act s 35C](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/35C), [SIS Reg 8.02A](https://www.legislation.gov.au/F1996B00580/latest/text) |
| Audit preparation and before SAR lodgment | Provide relevant documents; a written auditor request under s 35C has a 14-day response period. The auditor's report is due within 28 days after all relevant documents have been provided. The annual report must be completed and signed before lodging; obtain a required actuarial certificate before lodging the proportionate ECPI claim | [s 35C](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/35C), [reg 8.03](https://www.legislation.gov.au/F1996B00580/latest/text), [2026 lodgment instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return), [s 295-390](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-390) |
| Each transfer balance event | Record the event immediately; use Section 6.2 for the quarterly and earlier report deadlines and authority responses | [ATO TBAR instructions](https://www.ato.gov.au/forms-and-instructions/superannuation-transfer-balance-account-report-instructions/when-to-lodge) |
| SAR filing and payment | Establish the actual self-preparer/agent category, earlier notices, deferrals, separate payment date and supervisory levy branch in Filing and payment below | [2026 lodgment instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return) |
| Year end, including 30 June 2027 for 2026-27 | Evidence pension payments, asset market values, in-house-asset ratio and relevant member/fund balance snapshots; apply each rule's own date and balance definition for caps, DSFA and Div 296 | [SIS Regulations](https://www.legislation.gov.au/F1996B00580/latest/text), [s 295-387](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-387), [ATO Div 296](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/about-division-296-tax-for-smsfs) |

### Section 9 -- Common breach patterns

| Pattern in the file | Provision/control | Consequence to assess | Action |
|---|---|---|---|
| EFT to a member described as a loan or temporary transfer | [s 65](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/65) | Administrative penalty incidence depends on the contravening duty/person; auditor reporting requires its actual criteria | Escalate and document repayment/interest and rectification advice. Repayment does not erase a breach or permit retrospective classification as a benefit; R-AU-SF-5 |
| Related-party investments/leases above the permitted year-end ratio | [ss 71](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/71), [82](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/82) and Part 8 | Compliance/penalty exposure and the required reduction plan; an enforceable undertaking is possible, not an automatic outcome | Confirm exclusions and ratio, and arrange the statutory plan and disposal by the end of the next income year |
| Overdraft, margin loan or other borrowing outside a proved exception | [s 67](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67) | Borrowing prohibition and potential penalties | Refer immediately for lawful clearance and rectification; preserve documents |
| TBAR late or absent | Section 6.2 | Inaccurate excess determinations, penalties or compliance action | Reconcile all missed events and the member's ATO account; use the actual notice deadlines |
| Proportionate ECPI claimed without a required actuarial certificate | [s 295-390](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-390) | Claim cannot be assumed valid; tax consequences require recomputation | Stop the claim, obtain the required certificate before lodgment and refer a lodged error for a complete amendment |
| Contributions above the member's applicable cap | [Div 291](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/291-15) / Div 292 | Member ECC/ENCC determination, additional personal tax and release process | Reconcile all funds, unused caps and bring-forward history. Diary the determination/election date, distinguish the fund's release-authority deadline and refer the member's choice |
| Benefit paid without a condition of release | s 62 / SIS Reg 6.17 | Illegal early access can produce member tax, penalties, disqualification and fund non-compliance | Refuse to endorse the payment as lawful; retain evidence and refer under R-AU-SF-5 |
| Personal use of a fund asset, such as a holiday-house stay | [s 62](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/62) | Sole-purpose compliance action and any separately established NALI exposure | Escalate, document the use/cessation and obtain rectification advice; do not assume a later market-rent payment cures it |



## Worked cases

All amounts below are hypothetical. The examples recompute arithmetic after the stated legal facts have been established; they do not prove eligibility or replace the reviewer's source checks. Annual member figures are inputs for the dated example, with their general home in [au-rates-2026-27](au-rates-2026-27.md). Fund tax treatments are in Section 4, pension factors in Section 6 and the 2026 SAR levy in Filing and payment.

### 1. Mixed earnings, ECPI and a discounted gain

Preserve the original 2026-27 planning example: 2 members, one accumulation account and one valid retirement-phase account-based pension, unsegregated assets and a valid actuarial certificate supporting a 60% exempt proportion. Assume every minimum payment is met, no NALI, the gain qualifies for the fund discount, no other losses/credits/PAYG instalments and the full general administration expense has the stated assessable/exempt-income apportionment. Rent $32,000, interest $8,000 and unfranked dividends $10,000 total $50,000; a $30,000 share gain follows a 3-year holding; assessable employer/salary-sacrifice contributions are $30,000 and administration $4,000.

The $259 levy is an **assumed planning input for this 2026-27 illustration**, preserving the original vector. It is verified for a continuing fund's 2026 SAR, not a confirmed 2027 SAR amount. Confirm that later return's levy and labels before treating this as a filing calculation. On the stated assumptions the net capital gain is $20,000, ECPI $42,000, deductible administration $1,600, taxable income $56,400 and gross tax $8,460. Adding the assumed levy gives $8,719 before offsets, instalments or other adjustments. The gain's taxable share is $8,000 and its tax $1,200, or 4% of the gross gain; without ECPI the simple effective rate would be 10%. Contributions are not sheltered by ECPI. [ss 295-385](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-385), [295-390](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-390), [ATO SMSF tax](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed).

```oa-check
name: Mixed ECPI planning vector with an expressly assumed future levy
inputs:
  rent: 32000
  interest: 8000
  unfranked_dividends: 10000
  gross_gain: 30000
  exempt_proportion: 0.6
  contributions: 30000
  administration: 4000
  tax_rate: 0.15
  assumed_levy: 259
steps:
  net_gain: gross_gain * (1 - 1 / 3)
  ordinary: rent + interest + unfranked_dividends
  earnings_base: ordinary + net_gain
  ecpi: earnings_base * exempt_proportion
  deductible_admin: administration * (1 - exempt_proportion)
  taxable: contributions + earnings_base - ecpi - deductible_admin
  gross_tax: taxable * tax_rate
  planning_total: gross_tax + assumed_levy
  gain_taxable: net_gain * (1 - exempt_proportion)
  gain_tax: gain_taxable * tax_rate
  gain_effective_percentage: gain_tax / gross_gain * 100
expected:
  net_gain: 20000
  ordinary: 50000
  earnings_base: 70000
  ecpi: 42000
  deductible_admin: 1600
  taxable: 56400
  gross_tax: 8460
  planning_total: 8719
  gain_taxable: 8000
  gain_tax: 1200
  gain_effective_percentage: 4
```

### 2. Non-commercial general administration expense

Assume the trustee's firm supplies income-related general administration in 2026-27 in its business capacity. The $1,000 charge against a $3,500 arm's-length amount is proved non-commercial, not a commercial all-staff discount, genuine pro bono arrangement or trustee-capacity work. It is not solely income-tax affairs expenditure under s 25-5. Assume taxable income $90,000, assessable contributions $30,000, no deductions attributable to those contributions and no other NALI: the statutory contribution-adjusted limit is $60,000. Twice the $2,500 expense difference is $5,000 and the limit does not bind. Tax on that component is $2,250 compared with $750 at the low rate, an additional $1,500 of income tax, **not a separate penalty**. Do not subtract the actual expense again from the twice-difference amount. [ss 295-545](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-545), [295-550](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-550), [LCR 2021/2](https://www.ato.gov.au/law/view/document?docid=COG/LCR20212/NAT/ATO/00001).

```oa-check
name: General NALE with non-binding statutory contribution-adjusted limit
inputs:
  arm_expense: 3500
  actual_expense: 1000
  taxable_income: 90000
  assessable_contributions: 30000
  contribution_deductions: 0
  other_nali: 0
  high_rate: 0.45
  low_rate: 0.15
steps:
  shortfall: arm_expense - actual_expense
  twice_difference: 2 * shortfall
  statutory_limit: taxable_income - assessable_contributions + contribution_deductions
  nalc: min(other_nali + twice_difference, statutory_limit)
  high_tax: nalc * high_rate
  low_rate_comparison: nalc * low_rate
  additional_income_tax: high_tax - low_rate_comparison
  ordinary_net_gain: 30000 * (1 - 1 / 3)
  ordinary_gain_tax: ordinary_net_gain * low_rate
  conditional_high_rate_comparison: ordinary_net_gain * high_rate
expected:
  shortfall: 2500
  twice_difference: 5000
  statutory_limit: 60000
  nalc: 5000
  high_tax: 2250
  low_rate_comparison: 750
  additional_income_tax: 1500
  ordinary_net_gain: 20000
  ordinary_gain_tax: 3000
  conditional_high_rate_comparison: 9000
```

The final 3 lines preserve the original separate capital-gain arithmetic. A $30,000 discount-eligible accumulation gain without NALI gives a $20,000 net gain and $3,000 simple tax. Applying 45% to that same $20,000 gives $9,000 **only if that is independently established as the applicable non-arm's-length component**. This is not a general CGT/NALI classification rule. Acquisition/financing, asset management and renovation expenditure require their own nexus analysis; a prior maintenance discount does not automatically determine a later sale. Unpaid trustee-capacity work can be outside NALE, but using one's own equipment alone does not prove that capacity. Section 4.3 retains these distinctions.

### 3. Excess concessional contributions and the member's election

For 2026-27 assume $40,000 employer/SG/salary-sacrifice contributions, no other funds or special adjustments, a prior 30 June TSB of $600,000 and no available carry-forward increase. Use the verified $32,500 annual cap as this example's dated input. The fund ordinarily taxes all assessable contributions at 15%; the $7,500 excess is a separate member inclusion with a 15% non-refundable offset. The assumed effective marginal rate is 39%, made up of 37% and 2% Medicare purely for this illustration; do not infer that rate from contribution amounts alone. The simplified extra member tax is $1,800, subject to the member's actual tax position and offset availability. [ATO concessional contributions cap and ECC process](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap), [s 291-15](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/291-15).

```oa-check
name: ECC member illustration separate from fund contributions tax
inputs:
  contributions: 40000
  annual_cap: 32500
  fund_rate: 0.15
  assumed_member_rate: 0.39
  offset_rate: 0.15
  release_fraction: 0.85
steps:
  fund_tax: contributions * fund_rate
  excess: max(0, contributions - annual_cap)
  member_gross: excess * assumed_member_rate
  member_offset: excess * offset_rate
  simplified_extra_tax: member_gross - member_offset
  maximum_release: excess * release_fraction
expected:
  fund_tax: 6000
  excess: 7500
  member_gross: 2925
  member_offset: 1125
  simplified_extra_tax: 1800
  maximum_release: 6375
```

A member can elect to release up to 85% of the excess, here $6,375. Full eligible release prevents the corresponding ECC counting towards the NCC cap; a partial/non-release can leave some or all counted against the member's applicable NCC capacity. Use that member's cap, bring-forward history and determination, not a universal NCC amount. The ordinary election period is 60 days; later online availability is not a guaranteed extension. After a processed election the fund has 10 business days to send the required amount to the ATO under the release authority. Do not pay the member directly or amend correct original fund contributions merely because the member exceeded a cap. Correct a real reporting error through the appropriate adjustment/amendment process. Refer the member's irreversible release choice for advice. [ATO ECC instructions](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap).

### 4. Pension shortfall requires an ATO application

Assume a valid retirement-phase pension for a member aged 76 at 1 July 2026, relevant Schedule 7 balance $480,000 and no higher withdrawal-benefit adjustment. The 6% factor gives $28,800; actual qualifying payments by 30 June 2027 are $22,000, leaving $6,800. One-twelfth is $2,400. [Schedule 7](https://www.legislation.gov.au/F1996B00580/latest/text), [ATO exception guidance](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/paying-smsf-benefits/income-stream-pension-rules-and-payments/exception-to-minimum-pension-payment-requirements).

```oa-check
name: Pension shortfall exceeds the small-underpayment amount
inputs:
  balance: 480000
  minimum_factor: 0.06
  paid: 22000
steps:
  annual_minimum: balance * minimum_factor
  shortfall: annual_minimum - paid
  small_underpayment_limit: annual_minimum / 12
  excess_over_small_limit: shortfall - small_underpayment_limit
expected:
  annual_minimum: 28800
  shortfall: 6800
  small_underpayment_limit: 2400
  excess_over_small_limit: 4400
```

**Decision:** write to the ATO; do not self-assess continuation even if the asserted cause was outside the trustee's control. Assemble the cause, awareness/payment dates, otherwise available ECPI, liquidity, catch-up evidence and prior concession history in Section 6.1. Without relief, the interest loses ECPI for the year and the $22,000 payments are treated as lump sums for income tax purposes; refer any fresh pension documentation and transfer balance reporting. A shortfall no greater than $2,400 still requires every other condition and no prior-use bar. Payment alone is insufficient.

### 5. Penalty incidence depends on the contravening person

Assume one established s 65 contravention attracting the 60-unit administrative penalty, a $364 unit applicable at the contravention date, no remission and 2 individual trustees each separately liable. Their combined liability is $43,680. If the corporate trustee is the contravening person liable for that one penalty, its 2 directors are jointly and severally liable for $21,840 under s 169, rather than each being assigned a duplicate corporate penalty. This does not decide a director's separate contravention of a duty addressed to that director. These assumed findings must be established before using the comparison; use Section 3.2 and the penalty-unit home for the actual case. [ss 166](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/166) and [169](https://www.ato.gov.au/law/view/document?docid=PAC/19930078/169).

```oa-check
name: Conditional individual versus corporate s65 penalty incidence
inputs:
  penalty_units: 60
  dated_unit_amount: 364
  liable_individual_trustees: 2
  corporate_contraventions: 1
steps:
  one_penalty: penalty_units * dated_unit_amount
  individual_total: one_penalty * liable_individual_trustees
  corporate_total: one_penalty * corporate_contraventions
expected:
  one_penalty: 21840
  individual_total: 43680
  corporate_total: 21840
```

### 6. Nil general expense and a binding NALC limit

Assume a proved non-commercial business-capacity general service with arm's-length fee $3,500 and actual fee nil. Taxable income is $1,700, assessable contributions $1,000, deductions attributable to those contributions $100 and other NALI nil. Twice the shortfall is $7,000 but the statutory contribution-adjusted limit is $800. NALC is $800, the low-tax component $900 and gross tax $495 before offsets/levy. The actual nil expense is not a further deduction. This tests the cap and zero-charge case, not whether free trustee work is NALE. [ss 295-545](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-545), [295-550](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-550).

```oa-check
name: Nil general fee with binding contribution-adjusted NALC limit
inputs:
  arm_expense: 3500
  actual_expense: 0
  taxable_income: 1700
  contributions: 1000
  contribution_deductions: 100
  other_nali: 0
steps:
  twice_difference: 2 * (arm_expense - actual_expense)
  statutory_limit: taxable_income - contributions + contribution_deductions
  nalc: min(other_nali + twice_difference, statutory_limit)
  low_component: taxable_income - nalc
  gross_tax: nalc * 0.45 + low_component * 0.15
expected:
  twice_difference: 7000
  statutory_limit: 800
  nalc: 800
  low_component: 900
  gross_tax: 495
```

### 7. Private-company dividend classification changes the rate

Assume an unfranked $10,000 private-company dividend, no deductible costs, ECPI, losses, other income or offsets. For the complying accumulation fund, an arm's-length dividend produces simple tax of $1,500. If the dividend is instead proved NALI and $10,000 is the applicable NALC after the statutory calculation, tax is $4,500. The $3,000 difference is conditional on that classification; private-company status alone does not settle it. [s 295-550(2)-(3)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-550).

```oa-check
name: Conditional unfranked private dividend comparison
inputs:
  unfranked_dividend: 10000
  ordinary_rate: 0.15
  nalc_rate: 0.45
steps:
  ordinary_tax: unfranked_dividend * ordinary_rate
  conditional_nalc_tax: unfranked_dividend * nalc_rate
  tax_difference: conditional_nalc_tax - ordinary_tax
expected:
  ordinary_tax: 1500
  conditional_nalc_tax: 4500
  tax_difference: 3000
```

### 8. Decision: commercial staff discount or non-commercial general fee

Two hypothetical files both have $60,000 taxable income after the actual $1,000 fee, no assessable contributions and no other NALI. File A proves an ordinary commercial discount available to eligible staff on those terms, so the arm's-length price for that transaction is $1,000. File B proves a business-capacity non-commercial general administration service for which the arm's-length price is $3,500. Subject to all statutory conditions, A has no twice-difference NALI; B has $5,000 NALC. Gross tax is $9,000 versus $10,500. The $1,500 difference is a classification comparison, not authority to choose a price or a tax strategy. [LCR 2021/2, capacity and commercial-discount examples](https://www.ato.gov.au/law/view/document?docid=COG/LCR20212/NAT/ATO/00001).

```oa-check
name: Commercial discount compared with proved non-commercial general fee
inputs:
  taxable_income: 60000
  actual_fee: 1000
  commercial_arm_price: 1000
  noncommercial_arm_price: 3500
steps:
  a_twice_difference: 2 * (commercial_arm_price - actual_fee)
  b_twice_difference: 2 * (noncommercial_arm_price - actual_fee)
  a_nalc: min(a_twice_difference, taxable_income)
  b_nalc: min(b_twice_difference, taxable_income)
  a_tax: a_nalc * 0.45 + (taxable_income - a_nalc) * 0.15
  b_tax: b_nalc * 0.45 + (taxable_income - b_nalc) * 0.15
  difference: b_tax - a_tax
expected:
  a_twice_difference: 0
  b_twice_difference: 5000
  a_nalc: 0
  b_nalc: 5000
  a_tax: 9000
  b_tax: 10500
  difference: 1500
```

**Decision:** obtain the eligibility, ordinary commercial terms, capacity and services evidence first. If those facts are missing, hold classification and refer; do not label every firm discount NALE, every free service trustee-capacity work or every general expense asset-specific NALI.

### 9. Legacy employer contribution and separate no-TFN tax

Assume a complying fund receives $1,000 assessable mandated employer contributions for a member whose interest existed before 1 July 2007, with no other relevant contributions for that year. All statutory legacy-exception conditions are met, so ordinary contributions tax is $150 with no additional no-TFN tax. This is not an ordinary member contribution permitted without a TFN. As a separate comparison where the legacy exception does not apply, additional tax is $320 and total tax $470. A non-complying fund subject to the no-TFN tax instead pays $450 ordinary tax plus $20 additional tax, also $470. All figures exclude levy and offsets. [ss 295-610](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-610), [295-615](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-615), [2026 SAR section D, J](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13).

```oa-check
name: No-TFN legacy exception and compliance-status comparison
inputs:
  employer_contribution: 1000
  ordinary_complying_rate: 0.15
  additional_complying_rate: 0.32
  ordinary_noncomplying_rate: 0.45
  additional_noncomplying_rate: 0.02
steps:
  ordinary_complying_tax: employer_contribution * ordinary_complying_rate
  legacy_total: ordinary_complying_tax
  additional_if_not_excepted: employer_contribution * additional_complying_rate
  complying_total_if_not_excepted: ordinary_complying_tax + additional_if_not_excepted
  ordinary_noncomplying_tax: employer_contribution * ordinary_noncomplying_rate
  additional_noncomplying_tax: employer_contribution * additional_noncomplying_rate
  noncomplying_total: ordinary_noncomplying_tax + additional_noncomplying_tax
expected:
  ordinary_complying_tax: 150
  legacy_total: 150
  additional_if_not_excepted: 320
  complying_total_if_not_excepted: 470
  ordinary_noncomplying_tax: 450
  additional_noncomplying_tax: 20
  noncomplying_total: 470
```



### 10. Tax losses first absorb net exempt income

For a separate 2025-26 illustration, assume prior tax losses $30,000, ECPI $20,000, related exempt-income expenses $2,000 and current assessable income exceeding other deductions by $50,000. Net exempt income is $18,000, leaving $12,000 of prior losses deductible against the current assessable surplus, not $10,000. Assume all loss eligibility rules hold and no other adjustments. [2026 SAR Section C, tax-loss example and totals](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-c-deductions-and-non-deductible-expenses-item-12).

```oa-check
name: Prior tax losses reduced by net exempt income rather than gross ECPI
inputs:
  prior_losses: 30000
  ecpi: 20000
  related_exempt_expenses: 2000
  assessable_surplus: 50000
steps:
  net_exempt_income: ecpi - related_exempt_expenses
  remaining_losses: max(0, prior_losses - net_exempt_income)
  deductible_losses: min(remaining_losses, assessable_surplus)
expected:
  net_exempt_income: 18000
  remaining_losses: 12000
  deductible_losses: 12000
```

## When to refuse or refer

Stop the affected calculation or action when a required fact, source condition or scope requirement is unresolved. Mark that position Needs Input, document the exact evidence needed and identify the reviewer. Do not replace an unresolved legal rule with a more conservative guess.

### Refusal catalogue

**R-AU-SF-1: financial product and investment advice.** Refuse recommendations about investments, SMSF suitability, contribution strategy or whether to start/commute a pension. Message: 'This guide covers accounting, tax and compliance preparation only. Refer personal financial product advice to an appropriately licensed or authorised adviser.' This is a hard guide boundary; ASIC's exemptions and warnings remain conditional, and the former specific accountants' exemption ended on 1 July 2016. [ASIC INFO 216](https://www.asic.gov.au/for-finance-professionals/afs-licensees/apply-for-an-afs-licence/limited-financial-services/afs-licensing-requirements-for-accountants-who-provide-smsf-services).

**R-AU-SF-2: in-specie/off-market valuation.** Refuse to invent the value of a contributed or transferred asset. Message: 'Obtain qualified market-value evidence and review the acquisition and contribution rules before recording the transfer.' Independence/valuation requirements depend on the asset and applicable rule; neither a related-party estimate nor a market value alone establishes s 66 compliance.

**R-AU-SF-3: LRBA structuring.** Refuse to establish a holding trust, draft loan terms or design a related-party LRBA. Message: 'I can classify payments on an existing documented arrangement and check its PCG terms. Refer establishment, refinancing, replacement and transitional legal questions before acting.' Apply the commencement and transitional exceptions in Section 7 for affected real property; do not assume all old arrangements or refinancings are exempt.

**R-AU-SF-4: related-party acquisition or lease design.** Refer before implementing a proposed purchase from, investment in or lease with a member/related party. Message: 'Check the precise s 66 exception, market-value evidence, in-house asset conditions and sole-purpose rule before any step.' An exception for listed securities, business real property or specified in-house assets is not a general related-party permission.

**R-AU-SF-5: early access or temporary borrowing.** Refuse to facilitate a benefit without a documented condition of release or a temporary member loan. Message: 'This can involve illegal early access, member tax, penalties, disqualification and fund non-compliance. Refer immediately; do not backdate or relabel it.' The previously complying fund's asset-related tax inclusion is conditional under Section 4.1, not automatically a percentage of all assets. Compassionate-release approval uses the ATO process; this guide does not authorise a payment. Preserve possible promoter consequences for legal review rather than stating an automatic penalty.

**R-AU-SF-6: winding up.** Refer the sequence of benefit payments/rollovers, final accounts, audit, SAR/levy and deregistration to the qualified practitioner. Message: 'Prepare the evidence and reconciliation; obtain authority and advice before any irreversible step.' The new-and-wound-up levy branch in Filing and payment is distinct from a continuing fund's final return.

**R-AU-SF-7: death benefit disputes and BDBNs.** Refer death benefit directions, binding nomination validity and competing claims to a superannuation/estate lawyer. Message: 'Do not determine the payee or implement disputed directions through this accounting guide.'

### Calculation and filing stops

- Do not compute a member's Div 293/296 liability here; preserve the fund's separate Div 296 earnings, attribution and reporting work in Section 5.3.
- Do not claim ECPI until method, asset status, minimum payments and any required actuarial certificate are established. Do not substitute the individual CGT discount or erase a potentially NALI segregated-asset gain.
- Do not treat NALI/NALC as ordinary low-tax income or duplicate a general NALE deduction; reconcile the actual statutory component and return route.
- Do not accept a related-party value without sufficient market evidence or describe a member payment as lawful without a proved condition of release.
- Do not assume a member's personal transfer balance cap equals the general cap.
- Do not lodge, or describe a SAR as lodgeable, before the audit and required certificates/declarations are complete. No output in this guide authorises lodgment, payment, release or an election.
- Do not present hypothetical figures as a definitive tax result or mark a source gap cleared because an arithmetic test passed.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The source-cited version described here is the ryanduguid fork. The retained platform closing block does not establish that these changes are published or verified on the upstream website, or that an accountant has approved them.

## Filing and payment

### Choose the correct return and lodgment category

These instructions concern the **2026 SAR for 2025-26**, not the future 2027 SAR for the primary planning year. Read the [2026 instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return) and the actual ATO/agent due-date record. A SAR is ordinarily required even with no tax payable. No assets is not self-executing cancellation or RNN: obtain the written ATO outcome and check the winding-up exception and subsequent-year conditions before omitting a return.

| Category, 30 June balancer | 2026 SAR lodgment | Payment if required | Official source/qualification |
|---|---|---|---|
| Self-preparer: new registrant or prior return overdue at 30 June 2026, excluding an approved deferral | 31 October 2026 | 1 December 2026 | [2026 instructions, self-preparers](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return); earliest applicable category wins |
| Self-preparer: taxable large/medium entity in 2025-26 | 31 January 2027 | 1 December 2026 | [2026 instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return); do not substitute the agent table's prior-return test |
| Other self-preparers | 28 February 2027 | 28 February 2027 | [2026 instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return), unless directed otherwise |
| Agent client: earlier outstanding-return, prosecution/notified early category | 31 October 2026 | 1 December 2026 | [Registered-agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds); actual earlier notice controls |
| Agent client: large/medium taxpayer whose 2025 return was taxable | 31 January 2027 | 1 December 2026 | [Agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds), unless required earlier |
| Agent client: applicable large/medium non-taxable or new category, or new SMSF | 28 February 2027 | 28 February 2027 | [Agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds); read its exact prior-year/RNN/new-entity conditions |
| New SMSF reviewed by ATO at registration | 31 October 2026 | Check the actual notice/agent record | [ATO SAR guidance](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/lodge-smsf-annual-returns); first-year ordinary date does not override notified early filing |
| Agent client: total income in 2024-25 above $2 million | 31 March 2027 | 31 March 2027 | [Agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds), unless required earlier |
| Remaining eligible continuing agent clients | 15 May 2027 | 15 May 2027 | [Agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) |
| Eligible May-date client with both years non-taxable or refundable, excluding large/medium taxpayers and consolidated head companies | 5 June 2027 concession | 5 June 2027 concession | [Agent program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds); this is a penalty-waiver concession, **not a new statutory lodgment due date** |

Use the earlier actual due date and any valid deferral. If a due date falls on a weekend or public holiday, the ATO allows the next business day for lodgment/payment; verify the applicable holiday rather than silently assuming a state. The agent table also covers companies and NFSA taxpayers whose special notice-of-assessment rules do not become SMSF rules. A first return after RNN also needs the specific ATO date check. [ATO SAR guidance](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/lodge-smsf-annual-returns).

### Map the working paper to the 2026 SAR

Use the form's instructions in sequence and reconcile every member and supporting schedule, not just the final tax figure.

| Working-paper result | 2026 return route | Official instructions |
|---|---|---|
| Identity, first/amended/final status, auditor and ECPI method | Section A, items 1-10; reconcile the audit report and fund status. Verify the actual form's year where a web question contains an inconsistent year | [Section A](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-a-smsf-information-items-1-to-10) |
| Income, contributions, actual NALI and ECPI | Section B item 11; actual net private dividends/trust/other NALI use U1/U2/U3 as applicable; ECPI Y must match Section A item 10 A; reconcile member contribution reporting | [Section B](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-b-income-item-11) |
| General-expense twice-difference amount | Do **not** insert this calculated amount at U1/U2/U3/U or another Section B label. Take it into account in the Section D T1 lesser-of NALC calculation; eligible actual general expenses remain deductions in Section C | [Section B](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-b-income-item-11), [Section D T1](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13) |
| Deductions and tax losses | Section C item 12, including taxable income/loss O; separate income classes and deductions, apply prior-year losses first against net exempt income (with the related expense adjustment) and retain non-arm's-length losses separately | [Section C](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-c-deductions-and-non-deductible-expenses-item-12), [lodgment instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return) |
| Fund tax, no-TFN tax, offsets, credits, instalments and levy | Section D item 13 in sequence. A, T1, J, T5 and I are mandatory. Use zero where required, not blanks. A is zero when Section C O is a loss. Reconcile eligible offsets/refunds before S amount due/refundable | [Section D](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13) |
| Other information and declarations | Complete applicable remaining sections/schedules. All trustees/directors authorise the return, document that authority and review the audit; an authorised person signs the agent declaration where relevant | [Sections J/K](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-j-and-k-other-information-and-declarations) |

### Supervisory levy and payment

The following table is the **2026 SAR** levy home. Use the return's printed L and its precise new/wound-up branch; do not infer that a newly created and wound-up fund pays the continuing fund's nil final levy.

| Fund's 2025-26 status | L | M | N | Net levy | Primary source |
|---|---:|---:|---:|---:|---|
| Existing and not wound up | $259 | blank/zero | blank/zero | $259 for 2026-27 | [2026 Section D, Table 9](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13) |
| New and not wound up | $259 | blank/zero | $259 | $518 for 2025-26 and 2026-27 | [2026 Section D, Table 9](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13) |
| New and wound up that year | $259 | blank/zero | blank/zero | $259 for 2025-26 | [2026 Section D, Table 9](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13); use this table's special branch |
| Existing and wound up | $259 | $259 | blank/zero | nil | [2026 Section D, Table 9](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13) |

The levy is payable even where there is no tax liability, subject to the applicable return/RNN status. Reconcile S with tax, permitted credits/refunds, PAYG and L-M+N. Payment must reach the ATO by the actual payment due date using the correct fund PRN; receipt can take up to 4 business days to appear on the account. GIC can apply to overdue debt; its common rate/mechanics belong to [au-lodgment-deadlines-penalties](au-lodgment-deadlines-penalties.md). The statutory due date for a 30 June balancing fund is ordinarily 1 December, but the applicable ATO program dates above must be checked separately. Lodgment itself deems the assessment; an ordinary SAR does not produce a notice of assessment. [2026 lodgment/payment instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return).

### Lodge or amend only after approval

Obtain the completed signed audit report, any required actuarial certificate, valuations, member reconciliations, declarations, reviewer sign-off and explicit lodgment authority. SBR-enabled software supports ordinary electronic returns, but the 2026 instructions require paper for their specified no-asset/liability case (subject to wind-up), no-assessable-income case, deductions claimable without assessable income and combined NALI/arm's-length-loss case. Do not assume every SAR can be lodged electronically. Attach the required schedules, including CGT, trust income and relevant elections/loss/PAYG schedules where applicable; SMSFs are excluded from the 2026 RTP-schedule expansion. For paper use the original NAT 71226 form and the specified GPO Box 9845 address with capital city/postcode; retain a copy. [2026 lodgment instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return).

For an amendment, lodge the **whole return**, mark the amendment question Yes at Section A item 5 and complete all original and corrected members/sections. The complete amendment replaces the original; do not send only changed amounts, a correction letter or an individual-return amendment form. Use an allowed full-return channel: Secure mail in Online services for business, the permitted agent software/agent service or the specified paper return/address. Confirm acceptance, revised tax, credits and payment/recovery consequences and retain the reconciliation. [2026 amendment instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return).

If the SAR is 2 weeks overdue, the ATO guidance says regulation details will be removed from Super Fund Lookup. That **can restrict** contributions and rollovers; it is not a proved universal refusal by every employer or APRA fund. Diary correction and verify restored status after processing. [2026 lodgment instructions](https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return).

## Completion checklist

Deliver the four workflow-base outputs: the working paper, reviewer brief, action list and review checklist. The working paper reconciles fund/members, income/capital gains, contributions, ECPI, deductions, NALI/NALC, fund tax and return/payment mapping. Link each result to its evidence, legal conditions, assumptions and source date, and list each hypothetical/planning input separately from verified facts.

The reviewer brief identifies scope/year, method choices, alternatives considered, unresolved facts and source gaps, breach/ATO-application positions and the person authorised to decide each. The action list assigns an owner and due date to evidence requests, audit/certificate work, corrections, authority responses and any later filing/payment. The review checklist records reconciliation and legal-source checks actually completed, what was not checked and the required sign-offs.

Confirm that all 5 or more live positions have their own evidence, analysis and outcome; a missing input blocks that position rather than licensing an invented result. Keep each original case/subject available through the method, an owner link or an explicit source hold. Recompute applicable worked cases, check source/pack parity after generation and retain the reviewed version and signed approvals. A successful build or arithmetic check establishes only that check's scope. No completion status certifies taxpayer facts, professional reliance, filing acceptance, current website deployment or the entire Australia corpus.



## Sources

The rows record selected primary-source passages read on 4 November 2026, including the preceding research pass. They do not certify the whole instrument or taxpayer eligibility. A successful fetch, search snippet, sibling link or update date is not a completed legal review. The Register identified SIS Regulations compilation F2026C00541, C159, from 1 July 2026. The separate income-tax regulations latest-version metadata was also checked, but its full contents were not reviewed.

| Source | URL | Read on |
|---|---|---|
| Upstream skill template; Template and frontmatter contracts; current blob 3bb4ee6cd4a402bb506c1d05e3e5a571bce5268f | <https://github.com/openaccountants/openaccountants/blob/main/docs/skill-template.md> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 17A; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/17A> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 17B; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/17B> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 19; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/19> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 35C; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/35C> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 104A; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/104A> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 120; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/120> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 166; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/166> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 65; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/65> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 66; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/66> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 67A; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67A> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 71; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/71> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 82; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/82> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-95; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-95> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-385; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-385> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-387; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-387> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-390; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-390> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-550; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-550> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-610; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-610> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-615; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-615> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 169; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/169> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 126D; Selected operative sections for the duties and conditions discussed; not the whole Act | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/126D> | 2026-11-04 |
| LCR 2021/2 / Legal database; Selected relevant guidance/conditions | <https://www.ato.gov.au/law/view/document?docid=COG/LCR20212/NAT/ATO/00001> | 2026-11-04 |
| How Payday Super affects SMSFs / Australian Taxation Office; Selected relevant guidance/conditions | <https://www.ato.gov.au/businesses-and-organisations/super-for-employers/managing-superstream/how-payday-super-affects-smsfs> | 2026-11-04 |
| About Division 296 tax for SMSFs / Australian Taxation Office; Selected relevant guidance/conditions | <https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/about-division-296-tax-for-smsfs> | 2026-11-04 |
| Division 296 tax the latest for SMSFs / Australian Taxation Office; Dated news history; not evidence that guidance remains draft | <https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-newsroom/division-296-tax-the-latest-for-smsfs> | 2026-11-04 |
| Exception to minimum pension payment requirements / Australian Taxation Office; Selected relevant guidance/conditions | <https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/paying-smsf-benefits/income-stream-pension-rules-and-payments/exception-to-minimum-pension-payment-requirements> | 2026-11-04 |
| Other super rates and thresholds / Australian Taxation Office; Selected relevant guidance/conditions | <https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/other-super-rates-and-thresholds> | 2026-11-04 |
| Lodge SMSF annual returns / Australian Taxation Office; Selected relevant guidance/conditions | <https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/lodge-smsf-annual-returns> | 2026-11-04 |
| Companies and super funds / Australian Taxation Office; Selected relevant guidance/conditions | <https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds> | 2026-11-04 |
| AFS licensing requirements for accountants who provide SMSF services / ASIC; Selected relevant guidance/conditions | <https://www.asic.gov.au/for-finance-professionals/afs-licensees/apply-for-an-afs-licence/limited-financial-services/afs-licensing-requirements-for-accountants-who-provide-smsf-services> | 2026-11-04 |
| Special purpose companies / ASIC; Special-purpose status/declaration only; fee verified separately in the current ASIC annual-review table | <https://www.asic.gov.au/for-business-and-companies/companies/register-a-company/special-purpose-companies> | 2026-11-04 |
| Fines and penalties / ASIC; Selected relevant guidance/conditions | <https://www.asic.gov.au/penalties> | 2026-11-04 |
| Check your SMSF is an Australian super fund / Australian Taxation Office; Selected relevant guidance/conditions | <https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/setting-up-an-smsf/check-your-fund-is-an-australian-super-fund> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-545; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-545> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 291-15; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/291-15> | 2026-11-04 |
| PCG 2016/5 / Legal database; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=COG/PCG20165/NAT/ATO/00001> | 2026-11-04 |
| Contributions caps / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps> | 2026-11-04 |
| How to lodge and pay your SMSF annual return / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/how-to-lodge-and-pay-your-smsf-annual-return> | 2026-11-04 |
| Instructions to complete your SMSF annual return 2026 / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026> | 2026-11-04 |
| How SMSFs are taxed / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/self-managed-super-funds-smsf/smsf-administration-and-reporting/how-smsfs-are-taxed> | 2026-11-04 |
| Superannuation Industry (Supervision) Regulations 1994 - Federal Register of Legislation; Selected relevant sections/labels only | <https://www.legislation.gov.au/F1996B00580/latest/text> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-325; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-325> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 118-320; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-320> | 2026-11-04 |
| PCG 2020/5 / Legal database; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=COG/PCG20205/NAT/ATO/00001> | 2026-11-04 |
| Treasury Laws Amendment (Building a Stronger and Fairer Super System) Act 2026, Schedule 1 item 24; IT(TP)AA ss 296-50 and 296-55, small-fund CGT choice and records | <https://www.legislation.gov.au/C2026A00008/asmade/2026-03-13/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-04 |
| Section A: SMSF information – items 1 to 10 / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-a-smsf-information-items-1-to-10> | 2026-11-04 |
| Section B: Income – item 11 / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-b-income-item-11> | 2026-11-04 |
| Section D: Income tax calculation statement – item 13 / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-d-income-tax-calculation-statement-item-13> | 2026-11-04 |
| Section J and K: Other information and declarations / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-j-and-k-other-information-and-declarations> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 67-25; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/67-25> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 295-320; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/295-320> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 291-20; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/291-20> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 62; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/62> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 67; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 67B; Selected relevant sections/labels only | <https://www.ato.gov.au/law/view/document?docid=PAC/19930078/67B> | 2026-11-04 |
| Concessional contributions cap / Australian Taxation Office; Selected relevant sections/labels only | <https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap> | 2026-11-04 |
| SIS Regulations 1994, Schedule 7; Schedule 7, including formula image alt text, age factors, prorating, rounding and historical reductions | <https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-04 |
| SIS Regulations 1994, selected operating regulations; Regs 4.09, 4.09A, 7.04, 7.07H, 8.02A, 8.02B and 8.03 | <https://www.legislation.gov.au/F1996B00580/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html> | 2026-11-04 |
| ITAA 1997 s 290-165; Age/work-test provision and displayed remedial-power note; Firecrawl after local-reader failure | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/290-165> | 2026-11-04 |
| ATO, When to lodge a TBAR; Quarterly rule, earlier commutation deadlines and authority response | <https://www.ato.gov.au/forms-and-instructions/superannuation-transfer-balance-account-report-instructions/when-to-lodge> | 2026-11-04 |
| Section C: Deductions and non-deductible expenses – item 12 / Australian Taxation Office; Section C tail: deduction totals, mandatory O, prior-year losses first applied against net exempt income | <https://www.ato.gov.au/forms-and-instructions/self-managed-superannuation-fund-annual-return-2026-instructions/instructions-to-complete-your-smsf-annual-return-2026/section-c-deductions-and-non-deductible-expenses-item-12> | 2026-11-04 |
| Legal database - View: Principal legislation: SECTION 292-102; Operative downsizer conditions, proceeds cap and approved choice timing | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/292-102> | 2026-11-04 |
| Non-concessional contributions cap / Australian Taxation Office; Excess contribution election, associated earnings, tax and authority alternatives | <https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/non-concessional-contributions-cap> | 2026-11-04 |
| LCR 2018/9, ATO; Paragraphs 1-12; current consolidated scope, caps, deductibility and TSB; not the full ruling | <https://www.ato.gov.au/law/view/document?docid=COG/LCR20189/NAT/ATO/00001> | 2026-11-04 |
| ITAA 1997 s 292-90; Subsection (2)(c)(iiia), downsizer non-concessional exclusion | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/292-90> | 2026-11-04 |
| ITAA 1997 s 290-167; No deduction for a qualifying downsizer contribution | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/290-167> | 2026-11-04 |
| ITAA 1997 s 307-230; Current balance components and structured-settlement modification | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/307-230> | 2026-11-04 |
| ITAA 1997 s 307-230A; Balance-value hierarchy and prescribed-value conditions | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/307-230A> | 2026-11-04 |
| Treasury Laws Amendment (Tax Reform No. 1) Act 2026; Commencement table item 7 and Schedule 5 items 1-2, including maintaining/refinancing and pre-commencement acquisition exceptions; not the rest of the Act | <https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-04 |
| ASIC, Fees for commonly lodged documents; Hydrated annual-review table: proprietary special-purpose company, 1 July 2026, $70; separate public and upfront rows not substituted | <https://www.asic.gov.au/for-business-and-companies/forms-and-fees/all-fees/fees-for-commonly-lodged-documents> | 2026-11-04 |

### Provenance and retained history

This revision retains the original fund/trustee scope, intake evidence, seven referral gates, tax/ECPI/NALI subjects, contribution acceptance/caps/surcharges, pension/transfer-balance controls, investments, calendar, breach patterns, four numeric examples and penalty/dividend/no-TFN comparisons. It corrects their conditions and source attribution, supplies recomputing cases and adds the workflow-base return/reviewer outputs. Annual member caps, general transfer-balance amounts, employer SG and common penalty/interest figures are routed to their existing guide homes.

The old text claimed ATO figures checked on 20 August 2026, LRBA rates/limits and the Div 296 choice on 11 October 2026, and reporting/allocation/agent dates on 31 October 2026. Those are retained as historical statements, not a new verification receipt. The page-level rows above replace any blanket claim that every figure was verified. Retained references include SIS Act ss 35D, 82-85, ITAA Divs 290-294, TD 2014/7, TR 93/17 and ATO asset-valuation/pension/benefit guidance; a retained title alone is not proof those full documents were read in this revision.

Not yet confirmed: The original claim that Div 296 guidance is still draft is not established by dated news; verify the current approved forms, final guidance, regulations, attribution certificate conditions and filing implementation before a live calculation or election. The 2027 SAR and levy are not confirmed by 2026 instructions; case 1 deliberately retains $259 only as a hypothetical future-year planning input. The 2026 Section A web amendment question displays a 2025 year whilst the main 2026 amendment instructions specify 2026; verify the actual published form/software before filing. Full current-law/application review, asset-specific valuation/NALE nexus, profession-specific advice exemptions, auditor contravention-reporting thresholds, early-access/promoter consequences, special/legacy regimes, every source-linked full instrument and taxpayer facts have not all been verified here. No named accountant has signed off this version, and no statement here establishes website publication, filing acceptance or complete Australia-corpus integrity.

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
