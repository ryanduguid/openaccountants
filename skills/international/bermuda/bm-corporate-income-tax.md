---
name: bm-corporate-income-tax
description: "Source-cited draft: corporate income tax for Bermuda (2026 reference) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BM
category: international
tax_year: 2026
tax_year_notes: "Administration checked through 14 November 2026; use the group fiscal year and operative law. Retained detailed tax-base examples remain unverified."
last_updated: 2026-11-14
version: 1.5
review_status: pending_review
tier: 2
depends_on:
  - corporate-income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bermuda Corporate Income Tax

## Corporate income tax (Pillar Two CIT)

Apply the [current system screening](bm-tax-overview.md#corporate-income-tax-screening) before a corporate-tax conclusion. It covers group consolidation, the 2-of-4-year revenue lookback, entity exclusions/elections, limited international footprint, fiscal periods and tax assurances. The charging provisions apply from 1 January 2025; the current captured consolidated Act includes listed amendments through 2026:25 (operative 29 July 2026). No company is exempt solely because it is incorporated in Bermuda or holds an assurance certificate.

**Detailed calculation boundary.** The retained loss, economic-transition adjustment and other tax-credit details below have not been fully reconciled against the current amendment chain. Mark any computation using those details **Needs Input** until its topic-specific review is complete. The separate filing/payment procedure below supports only its stated administrative decisions; it does not validate the underlying tax, credit, foreign-exchange or interest calculation.

- **Corporate income tax charge:** 15% of the Bermuda Constituent Entity Group’s net taxable income, less applicable foreign tax credits under Part 4. Section 4(3) imposes joint and several liability across Bermuda constituent entities of the same in-scope MNE Group. This is not a tax on gross revenue. [Consolidated CIT Act, s 4](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)
- **CIT effective date** — Fiscal years beginning on or after 1 January 2025  _(Corporate Income Tax Act 2023 (https://www.gov.bm/CIT))_
- **Group revenue threshold:** generally at least EUR 750 million in the UPE’s consolidated financial statements in at least 2 of the 4 immediately preceding fiscal years, subject to s 11 special rules, s 13 and relevant elections. Threshold satisfaction alone does not settle liability. [CIT Act, ss 2 and 8–15A](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) · [Full screening](bm-tax-overview.md#corporate-income-tax-screening)
- **Outside the charge:** determine in-scope group and Bermuda constituent-entity/group status before concluding that s 4 does not charge CIT. This is not proof of the absence of every other tax or foreign-country liability. [CIT Act, ss 4 and 8–15A](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)
- **CIT tax base:** ss 5–6 and 20–46 govern the detailed income, loss and adjustment computation. The retained summary of an 80% loss limitation is not an unconditional rule: current s 6(8) contains a separate shock-loss mechanism. The detailed computation and its evidence remain **Needs Input**; do not apply 15% directly to book income. [CIT Act](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)
- **Shared workflow boundary:** the corporate workflow base supplies controls, not Bermuda law. The EUR 750 million threshold does not itself authorise a Bermuda GloBE top-up calculation: General Guidance v2 states that GloBE rules are not incorporated by reference unless expressly stated. Establish each applicable domestic or foreign Pillar Two rule separately. The base’s sector refusals still apply; screening a non-corporate entity under the Act does not permit its computation through a corporation-only workflow. Detailed computation remains **Needs Input** under the boundary above. [General Guidance v2, p 5](https://www.cita.bm/assets/documents/2026-11-13-13-18-25-CIT%20Guidance%20Notes%20(General)%20V2.pdf)
- **Economic Transition Adjustment (ETA)** — A Bermuda Constituent Entity included in a group in its first fiscal year beginning on or after 1 January 2025 adjusts taxable income for the fair value of its assets and liabilities (excluding goodwill) at 30 September 2023, with the adjustments capped at 80% of the relevant amount and intangibles amortised over the first ten fiscal years  _(Corporate Income Tax Act 2023 (2023:35), Bermuda Laws Online, s 33 — https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Corporate%20Income%20Tax%20Act%202023)_
- **Entity exclusions and elections:** apply s 10’s defined excluded-entity categories and subsidiary ownership/activity conditions; investment funds and real-estate vehicles are not all automatically excluded. Section 9(2)(b)’s under-80%-by-value exclusion is subject to election. Sections 9(4) and 10(4) identify five-year elections; current ss 49(6) and 49A contain revocation provisions. Check the facts and election history. [CIT Act, ss 2, 9–10, 49 and 49A](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf)
- **Dividend withholding:** the prior 0%/none claim remains a current primary-evidence gap. Do not use it as a verified rate. [Evidence boundary](bm-tax-overview.md#claims-still-requiring-evidence)
- **Interest and royalty withholding:** each prior 0%/none claim remains a current primary-evidence gap. Keep the categories separate and do not output zero. [Evidence boundary](bm-tax-overview.md#claims-still-requiring-evidence)
## CIT registration, filing and payment

### Scope, period and inputs

This procedure is checked through 14 November 2026 against the [Administrative Regulations][admin], including BR 118/2025 and [BR 87/2026][amend], the [CIT Act][act] and current CITA materials. The regulations commenced on 2 June 2025; the listed amendments operated from 12 December 2025 and 14 August 2026 respectively. The current s 46D penalty provisions reflect Act 2026:25, operative 29 July 2026. Use the version governing the actual event for an earlier default; do not apply the current procedure retrospectively merely because it appears in the consolidation. BR 87/2026 adds prescribed form/manner requirements to regs 26(5) and 32(3); those amendments do not replace their numerical response periods.

Complete the [system screening](bm-tax-overview.md#corporate-income-tax-screening) first. Record the statutory UPE fiscal year, each Bermuda Constituent Entity (BCE), group composition, TINs, designated Filing BCE, authorised submitter, elections, tax and payment information, earlier filings/notices and any Agency variation or clearance. The calendar-year fallback in the Act's fiscal-year definition is conditional; a BCE's separate accounting year is not automatically the group's fiscal year. Missing scope, election, tax, holiday or notice facts are **Needs Input**. This procedure plans compliance; it does not validate the retained taxable-income, loss, ETA, credit or foreign-exchange computations.

### Registration and responsibility

- Under regs 6–7, the Filing BCE registers no later than 10 days before payment of a required instalment. Each other BCE registers no later than 90 days before the group's original return due date. The Agency may extend or vary registration timing. Required registration updates follow within 90 days of a change to information specified by the Agency; failure to update is treated as failure to register. Do not invent a Filing BCE deadline where the required-instalment trigger does not arise; obtain the applicable Agency requirement.
- A qualifying declaration to the Registrar can engage reg 7(3)'s protection: no registration default unless the Agency notifies incompleteness/further details and the entity fails to comply within 90 days. This is not permission to assume registration complete. Confirm every relevant BCE/TIN and current group composition before preparing the return. [I-101, §§1.3.1–1.3.3][i101]
- Each group designates a member as Filing BCE under reg 9; a sole BCE is automatically designated. If a multi-entity group fails to designate by the earlier of the original return due date or an instalment payment, the Agency designates. Designation continues unless modified or revoked with Agency approval. The Filing BCE files and pays for the group under regs 10 and 23; responsibility is not allocated to a convenient entity without evidence. Authorisation, actual registration and successful submission remain taxpayer-specific facts.

### Payments and instalment information are separate

Apply regs 10–19 before placing payments on a calendar:

| Control | Current rule |
|---|---|
| Ordinary instalment dates | First: last day of the fiscal year's eighth month. Second: fifteenth day of its twelfth month, subject to reg 12's exceptions. |
| Short fiscal year | More than 32 but less than 52 weeks: no second instalment. At most 32 weeks: neither instalment. Reg 12(2)(b) and (3)(b) separately address groups consisting exclusively of BCEs with the specified short periods of BCE status; check every member and the exact conditions. |
| Small tax amount | No first or second instalment if the group's statutory **tax**, rather than book profit or a remaining cash balance, is less than USD 10,000. Exactly USD 10,000 is not within this exception. It does not remove the return or final-payment requirement. Reg 2 imports the USD-denominated definition of tax from CIT s 46B(1). [CIT Act][act] |
| Advance information | Reg 10A normally requires information for each instalment even if its amount is nil. The express exceptions are the relevant reg 12(2)/(3) short-period exclusion or the s 7 de minimis exemption election. Reg 12(4)'s USD 10,000 payment exception is not itself an information-filing exception. |
| Information deadline | For instalments due on or before 31 December 2025, reg 10A(6)(a) specifies 31 January 2026 for both information filings, subject to the business-day rule, and disapplies reg 10A(3). Otherwise use the respective instalment payment deadline. |
| Final payment | All tax due is payable by the **original** return due date under reg 17. Filing late, amending a return or receiving an assessment does not provide a fresh payment deadline. |
| Business days | Reg 3(4) moves a non-business-day deadline to the first following Bermuda business day. Check Bermuda public holidays as well as weekends. |

Instalment amounts are not simply unconditional percentages of an estimated annual liability. Regs 13–14 contain alternative calculation methods, relevant elections/disclosures and distributable-tax-credit reductions; regs 10, 12 and 15–16 govern application and allocation of payments. Keep the calculation **Needs Input** until the relevant tax base, credits, method, elections and payment dates are verified. A nil instalment form does not establish a nil tax liability.

The [current return page][returns] labels Form 001 as **2025 only** and directs FY2026 onward to Form 002 in CITA Online. [I-002][i002] expressly refers to fiscal years ending in 2026 and thereafter. Its published procedure requires an authorised person to submit for the Filing BCE, supporting information for the reported instalment and, for an amendment, a new Form 002 with an accompanying explanation. This is a public instruction, not evidence of an executed filing. The [calendar last published 5 June 2026][calendar] still labels its instalment-information columns 'Form 001', including fiscal years ending in 2026; use the current year-specific form instructions rather than treating that older column heading as form authority.

Reg 10A(9) prohibits filing or amending an instalment-information form **after the earlier of** actual filing of the group's return and its original due date. Availability of the 2025 web form does not override this cutoff. Reg 10A(3) does not apply to the instalments covered by reg 10A(6)(a), due on or before 31 December 2025. Otherwise, incomplete/incorrect information is not deemed filed before complete/correct submission; if it is corrected fully within 14 days of Agency notification under reg 10A(4), the deemed date is the notification date. For reg 10A(3), reg 10A(8) dates an amended form to its original filing if amended before Agency notification, or after notification where the original was not incomplete/incorrect in the Agency's opinion; in other cases it uses the amendment filing date. Preserve the original filing, notice, completion and amendment timestamps; a new upload is not automatically timely. If the cutoff has passed, the permitted remedy is **Needs Input** from the Agency.

Under reg 11, payments/refunds are in US dollars; Bermuda-dollar payments need prior Agency consent. Obtain payment instructions through the official Agency route and retain evidence of the amount credited, date, fiscal year and group allocation. Do not infer settlement from form submission or a bank instruction. Reg 16 generally uses the date funds are credited to the Agency's designated account for an instalment payment, with separate allocation rules for other payments. Early payment and making good a missed payment are permitted; late payment does not erase interest or penalties. Underpayment interest follows regs 16, 18–19 and includes daily compounding. The applicable BMA-based annual rate, payment applications and complete computation remain **Needs Input** unless separately verified. A discretionary written overdue-payment agreement under reg 34 does not stop continuing interest or change tax/penalties.

### Return, schedules and completion

Reg 23 requires a return for each BCE Group and fiscal year, filed by its Filing BCE, including the required authority and correctness/completeness declaration. Nil tax does not itself remove filing. The Agency may dispense with a return following reg 33 clearance; cessation or dissolution alone is not clearance. Reg 33's qualifying exit facts, conditions and indemnity must be established.

The original deadline is the end of the tenth month following fiscal-year end, adjusted under reg 3(4). For a 31 December 2025 year-end, CITA's [30 October 2026 advisory][advisory] confirms **2 November 2026** for the CIT return; the [published calendar][calendar] gives the same CIT return/final-payment date. This is a specific fiscal-period example. Check the applicable period and any actual Agency notice instead of copying it to another year. The public return page's generic reference to the November deadline is not a deadline for every taxpayer or fiscal year.

The [return page][returns] and July 2026 [I-101][i101]/[I-102][i102], Chapter 1, require:

1. Form 100, the CIT Online Return, **and** the appropriate primary schedules uploaded before submission. Form 100 alone does not satisfy filing. Inaccurate, incomplete or inconsistent primary schedules can also leave the obligation unsatisfied.
2. **One** primary schedule set: S-101 standard or S-102 simplified. S-102 requires **all** of: the s 7(1) de minimis election; the s 33(8) election not to apply ETA for every BCE member; the s 6(6) election permanently disregarding all opening loss-carryforward and net taxable-loss allocations for every BCE member; and no tax payments or distributable tax credit benefits applied to BCE members for that year. Eligible groups may still choose S-101. Do not make or assume a permanent election merely to choose a shorter form; assess its substantive effect separately.
3. Relevant secondary schedules with S-101. I-101 §1.1.3 makes S-103 conditional on the opening-loss allocation/period and election facts, and S-104 conditional on the relevant foreign-parent tax allocation, with the stated nil-charge exception. Do not attach both primary sets, assume every standard return needs every secondary schedule or drop required schedules because summary figures appear unchanged. Detailed loss/foreign-credit calculations and the associated form instructions remain separately unverified.
4. Required supporting statements, authorised declaration and submission evidence. I-101 §1.1.4 lists additional documents for relevant amended returns, SAC/ISAC elections and supplemental disclosures. Record the Agency's submission acknowledgement/status and the actual attached versions when filing is carried out; this guide does not attest portal acceptance or satisfaction of the obligation.

### Corrections, records and notices

Keep these clocks separate. Obtain the notice, actual filing date, original due date, governing version and any Agency consent/extension before determining an actual deadline. [Administrative Regulations, regs 24–32][admin]

| Event | Current rule |
|---|---|
| Taxpayer amendment | Reg 25(2) uses the **later of** its applicable branches: ordinary return, 3 years after the original due date; reg 24 notice-required return, 12 months after filing under that notice. Reg 25(3) permits the specified Agency-consented enquiry amendment or agreed extension. |
| Agency correction of obvious errors/omissions | Reg 26: within 3 years after actual return filing. Taxpayer notice rejecting it in the prescribed form/manner within 90 days of the correction notice makes it ineffective. This is not the taxpayer-amendment clock. |
| Books and records | Reg 27: sufficient records for every BCE until the fifth anniversary of actual return filing. An agreed assessment extension beyond that date extends retention to 1 year after the extended assessment period ends. |
| Ordinary enquiry/assessment period | Reg 28: 4 years after the original due date for an on-time return, or actual filing for a late return; agreement can extend it. The enquiry must close or the proposed-assessment notice issue within the applicable period; starting an enquiry alone is insufficient. Amendment alone does not change it. No time limit for an unfiled return, fraud or intentional misstatement. |
| Proposed assessment | Reg 32: prescribed submissions within 60 days of the notice date. This is not a court-appeal deadline. |

An amended return requires the amended Form 100, all relevant primary/secondary schedules using the applicable original or amended versions, the amended-status designation and a statement describing the substantive changes. This applies even if a schedule changes without changing Form 100's summary amounts. I-101 §1.4 and I-102 §1.4 describe the public procedure. Reg 25(4) applies Part 3's original over/underpayment dates and interest rules; amendment does not restart them. An Agency notice under reg 24 can require an outstanding return within its specified period without relieving earlier penalties or interest; the Agency need not first request a return before assessing.

Current CIT s 46D can impose civil penalties for late returns and required information. Preserve reasonable-excuse conditions and s 46B's Agency assessment/notice safeguards, including the 28-day written-response opportunity after a penalty warning. The current late-return schedule distinguishes its first 5 months from later months. The separate advance-information penalty ends at the earliest statutory event, including filing the group return or its original due date; it is not an unlimited monthly charge until information arrives. Do not compute a historical default using the current schedule without its operative chain. Tax, interest, penalties and the required conditions are separate. Section 46H's offence requires intentional failure continuing **beyond** 6 months, not ordinary lateness or exactly 6 months. A permitted amendment is not automatically a qualified amended return for s 46E; enquiry timing matters. [CIT Act, ss 46B, 46D–46J][act]

Section 48 provides a Supreme Court appeal right, but this review has not established the procedural filing deadline. Mark it **Needs Input**; do not substitute the 60-day assessment-response or 28-day penalty-warning period. Detailed penalty amounts, refund/set-off/interest computations, payment-channel execution, individual taxpayer notices/relief and authenticated portal steps remain separate verification work.

### Manual controls and reviewer output

The following are hypothetical source-based controls, not executed taxpayer, consuming-model or portal tests:

- A group with nil tax and no clearance still needs its return. A full-year group with statutory tax of USD 9,999 has no instalment payment under reg 12(4), but that fact alone does not remove reg 10A information, the return or final payment.
- A 32-week year meets reg 12(3)'s instalment exception; a 33-week year below 52 weeks meets only the stated second-instalment exception. Apply the corresponding information exception separately; do not infer one from an unverified entity-status period.
- A 31 December 2025 year-end uses the published 2 November 2026 return/final-payment date. For a 30 November 2026 year-end, the current CITA banner/calendar gives 16 November 2026 for its second instalment; current I-002 directs a fiscal year ending in 2026 to Form 002, despite the older calendar's Form 001 heading.
- An outstanding 2025 instalment form found after the earlier return-filing/original-deadline cutoff does not become permissible because the web form is still available. Hold the remedy for the Agency.
- A de minimis election alone does not establish S-102 eligibility; missing all-member elections or an applied tax payment requires the standard-route/eligibility analysis. Never waive losses merely to simplify filing.
- Form 100 without the required schedules is incomplete. A corrected schedule with unchanged summary amounts still requires the amended return components and explanation.
- A late-filed ordinary return keeps its taxpayer-amendment clock tied to the original due date; the Agency-correction and late-return assessment clocks use actual filing. An unfiled return does not acquire the ordinary four-year limitation.
- A proposed assessment, penalty warning and court appeal are 3 different procedures. Preserve the 60-day and 28-day conditions and hold the unverified court clock.

Return a source/period register, scope and Filing BCE evidence, separate payment/information/return calendars, form/election/attachment decision, payment application record, correction/record-retention/notice tracker and unresolved-input list. Retain the original sources and submission versions. No whole-topic completion or practitioner sign-off follows from this procedure.

[admin]: https://www.cita.bm/assets/documents/2026-10-13-09-30-44-Corporate%20Income%20Tax%20(Administrative)%20Regulations%202025%20NEW.pdf
[amend]: https://www.cita.bm/assets/documents/2026-08-31-09-19-12-Corporate%20Income%20Tax%20(Administrative)%20Amendment%20Regulations%202026.pdf
[act]: https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf
[returns]: https://www.cita.bm/corporate-income-tax-return1
[i002]: https://www.cita.bm//assets/images/files/Form_002_Instructions.pdf
[i101]: https://www.cita.bm//assets/images/files/Form%20I-101_Instructions%20for%20the%20Standard%20CIT%20Return%20Schedules%20(July%202026).pdf
[i102]: https://www.cita.bm//assets/images/files/Form%20I-102_Instructions%20for%20the%20Simplified%20CIT%20Return%20Schedules%20(July%202026).pdf
[calendar]: https://www.cita.bm//assets/images/files/Filing%20&%20Payment%20Deadlines%2005.06.2026.pdf
[advisory]: https://www.cita.bm/news/cita-online-upcoming-filing-deadline

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
