---
name: au-amending-individual-income-tax-return-period
description: >
  Use this skill for Australian working papers that correct an assessed income tax return of an individual or sole trader for 2026-27 and earlier years. It covers section 170 amendment items, prescribed 4-year circumstances, small and medium business self-amendments, limits on amending amended assessments and extensions. It also covers shortfall amounts, false or misleading statement and reasonably arguable penalties, increases, voluntary disclosure reductions and request channels. Trigger on 'amend my tax return', 'amendment period', 'section 170', 'item 3A', 'shortfall amount', 'voluntary disclosure' and 'reasonably arguable'. Objections, entities and final tax amounts require review.
jurisdiction: AU
version: 1.5
category: international
tax_year: 2026
tax_year_notes: "2026-27 framework; verify the law for each notice, statement and disclosure date"
last_updated: 2026-11-03
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Amending an individual income tax return in Australia v1.5

> **General reference only.** Prepare a working paper for a qualified Australian reviewer. This source-cited draft does not establish a person's amendment period, penalty outcome, approved return field or final tax liability. Obtain professional review before requesting an amendment, making a disclosure, filing, paying or taking a position.

## Scope

Prepare an amendment working paper for an Australian individual, including a sole trader, whose income tax assessment has issued. Cover the ITAA 1936 s 170 amendment item, the original and amended notice chain, the corrected liability and any shortfall amount, the administrative penalty position under TAA 1953 Schedule 1 Division 284 and the request channel. Use AUD and supported figures. [ITAA 1936 s 170](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).

Load [workflow-base](../../foundation/workflow-base.md) and [income-tax-workflow-base](../../foundation/income-tax-workflow-base.md). This guide does not compute tax. Recompute the corrected return with [au-individual-return](au-individual-return.md), [au-deductions-offsets](au-deductions-offsets.md), [au-medicare-levy](au-medicare-levy.md) and the relevant topic guide, such as [au-capital-gains](au-capital-gains.md). Route lodgement deadlines and failure-to-lodge penalties to [au-lodgment-deadlines-penalties](au-lodgment-deadlines-penalties.md), residence to [au-tax-residency](au-tax-residency.md), partnership returns to [au-partnerships](au-partnerships.md) and trust returns to [au-trust-distributions](au-trust-distributions.md). Companies, trusts, partnerships, super funds and other entities are outside scope; the ATO directs them to its business and super amendment material. Objections, extensions of time to object, Part IVC proceedings, shortfall and general interest charges, and penalty remission are referred.

The ITAA 1936 compilation read here is compilation 193 (C2026C00454), in force from 1 October 2026 with no unincorporated amendments recorded. The TAA 1953 compilation is compilation 227 (C2026C00468), in force from 1 October 2026 to 1 July 2027. The Income Tax Assessment (1936 Act) Regulations 2025 apply to years of income starting on or after their 1 October 2025 commencement; the repealed 2015 Regulation continues to apply to earlier years. Item 3A applies only to assessments issued after Schedule 3 of the Treasury Laws Amendment (2024 Tax and Other Measures No. 1) Act 2024 commenced on 1 January 2025, for income years starting on or after 1 July 2024. Verify the applicable compilation and instrument for each notice, statement and disclosure date, including historical years.

## Ask the client first

1. Who is the taxpayer, in what capacity, and for which income year? During that year, did they carry on a business, hold a partnership or trust interest, or act as a trustee?
2. When did the Commissioner give notice of the original assessment, by what channel, and what evidence shows it? List every amended notice, its date and the particulars it changed.
3. For the year, what was the aggregated turnover of the individual's business, and of any partnership or trust in which they were a partner or beneficiary, under each applicable small business entity route, including connected entities and affiliates? Was the trustee of any such trust a full self-assessment taxpayer?
4. Could any prescribed circumstance apply, such as associate transactions, Division 7A deemed dividends, foreign-source income, unidentified foreign transaction income, employee share scheme interests or a listed integrity provision? Has the ATO started an examination, asked for consent to extend a period or obtained a court order?
5. Which particulars are wrong, does each correction increase or decrease the liability or a credit, and which records support the corrected figures?
6. Did the original position follow ATO advice, general administrative practice or an approved publication, or did a registered agent make it after receiving all relevant information? Has the ATO notified an examination or published a disclosure deadline, and has any part of the shortfall already been disclosed or identified by the ATO?

## The method, step by step

### Figures and periods register

This register consolidates the checked periods and amounts. The numbered steps explain their conditions. A figure does not establish a person's facts or the operative law for an unverified date.

| Measure | Period, amount or boundary | Official source |
|---|---|---|
| Ordinary individual period, s 170(1) item 1 | Within 2 years after the day the Commissioner gives notice of the assessment. It does not apply if, in that year, the individual carries on a business, unless the individual is a small or medium business entity; is a partner in a partnership carrying on a business, unless the partnership is one; or is a trust beneficiary, unless the trust is one or its trustee is a full self-assessment taxpayer. It also does not apply to the trustee capacity, where it is reasonable to conclude that a scheme was entered into or carried out for the sole or dominant purpose of the individual obtaining a scheme benefit for that year, or in a prescribed circumstance | [s 170(1)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| Default period, item 4 | Within 4 years after the day notice is given where items 1, 2 and 3 do not apply | same |
| Small or medium business self-amendment, item 3A | Within 4 years after the day notice is given if the individual is a small or medium business entity for the year, item 1 applied and its period has ended, and the individual applies in the approved form before the 4-year period ends. The Commissioner amends to give effect to the decision on that application; it is not an unrestricted 4-year ATO review period | same; [TLAA 2024 Sch 3](https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html) |
| Item 3A application | Assessments issued after Schedule 3 commenced on 1 January 2025, for income years starting on or after 1 July 2024 | [TLAA 2024 s 2, Sch 3 item 6](https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html) |
| Small / medium business entity | Aggregated turnover less than $10 million under the applicable route / not a small business entity, but would be one if $50 million replaced $10 million in Subdivision 328-C and the s 328-110(5)(b) reference to a small business entity were to an entity covered by the medium business entity definition | [s 170(14)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html); [ITAA 1997 s 328-110](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) |
| Fraud or evasion; review, appeal or objection | Any time under items 5 and 6 | [s 170(1)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| Amending an amended assessment | Items 1, 2, 3 and 4: not after the original assessment's limited amendment period ends. Item 3A: not after 4 years from the original notice. A refreshed period covers only the particular and direction in s 170(3): 2 years after the later notice where item 1, 2, 3 or 3A applied to the original assessment, otherwise 4 years. After a s 170(3) increase about a particular, no later s 170(3) reduction about that particular is allowed | [s 170(2)-(4)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| Extensions | A taxpayer application in the approved form before the limited amendment period ends. A private ruling application before it ends, where the Commissioner then makes the ruling because of that application; the amendment gives effect to the ruling. During an unfinished examination: a Federal Court order on the Commissioner's application before the period ends, extending it for a specified period where taxpayer action or inaction made completing the examination in time not reasonably practicable, or inappropriate; or the taxpayer's written consent, to a request made before the period ends, to extending it for a specified period. Either can be repeated. The limited amendment period means the item 1, 2, 3 and 4 and s 170(3) periods, not item 3A | [s 170(5)-(8), (14)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| Prescribed circumstances excluding item 1 | Only s 14 items whose column 1 names paragraph (f) of item 1. 2026-27: the 2025 Regulations items 1 to 6, 8 to 11, 14 and 15, including an associate transaction in the assessment year that has income tax consequences, is relevant to an amount in the assessment and is not at arm's length or involves $200,000 or more of income, deductions or capital proceeds, and $200,000 or more of foreign-source assessable income across the entity, its affiliates and connected entities. Years starting before 1 October 2025: the 2015 Regulation items 1 to 5A, 6 to 9, 12 and 13. Items limited to companies and trustees, such as foreign control or non-residence, 10 or more connected entities or affiliates, and research and development, do not exclude item 1 | [2025 Regulations ss 2, 14, 23](https://www.legislation.gov.au/F2025L01060/asmade/2025-09-09/text/original/epub/OEBPS/document_1/document_1.html); [2015 Regulation s 14](https://www.legislation.gov.au/F2015L01415/2022-12-09/2022-12-09/text/original/epub/OEBPS/document_1/document_1.html) |
| Objection period for a s 175A assessment objection | 2 years after notice where item 1, 2, 3 or 3A applies, otherwise 4 years. For an objection to an amended assessment, the later of that period measured from notice of the assessment it amended and 60 days after notice of the amended assessment, limited to the alterations and additions. An extension of time is a separate request | [TAA s 14ZW(1)(aa)](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| False or misleading statement with a shortfall | Base penalty amount (BPA): intentional disregard 75%, recklessness 50%, failure to take reasonable care 25% of the shortfall amount or part | [TAA Sch 1 s 284-90(1) items 1-3](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| False or misleading statement without a shortfall | 60, 40 or 20 penalty units for the same 3 behaviours | [s 284-90(1) items 3A-3C](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Position that is not reasonably arguable | 25% of the shortfall amount or part, only where that amount is more than the reasonably arguable threshold | [ss 284-75(2), 284-90(1) item 4](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Reasonably arguable threshold | Individual: greater of $10,000 or 1% of income tax payable worked out on the basis of the return. Trust or partnership: greater of $20,000 or 2% of net income; this applies through items 5 and 6 to a beneficiary's or partner's shortfall arising from the trust or partnership | [s 284-90(3)](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Increase | 20% for obstruction, for not telling the Commissioner within a reasonable time after becoming aware of the shortfall or false statement after it was made, or for a previous BPA: under items 1 to 3 for items 1 to 3, under items 3A to 3C for those items, and under the same item for items 4 to 6A | [s 284-220(1)](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Accepted-way reduction | BPA reduced to the extent caused by a treatment that agreed with Commissioner advice, general administrative practice or an approved publication | [s 284-224](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Voluntary disclosure reduction | Before the day the Commissioner tells the taxpayer that an examination is to be made or, if a public request for disclosure about a scheme or transaction that applies to the taxpayer's affairs sets an earlier day, before that earlier day: 80% where the shortfall amount or part is $1,000 or more, nil where it is less than $1,000, and nil for a false or misleading statement without a shortfall. After an examination notice: 20% where telling can reasonably be estimated to save significant time or resources | [s 284-225](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Penalty formula | BPA + BPA × (increase % − reduction %) | [s 284-85](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |

### 1. Establish the taxpayer, year and notice chain

Identify the taxpayer, capacity and income year, and each business, partnership, trust and scheme fact that s 170(1) item 1 tests. Record when the Commissioner gave notice of the original assessment, with the evidence. The statute measures each period after the day notice is given. The ATO's individuals page says the period starts the day after the notice is sent and gives a myGov email example. Do not convert a message date into the statutory giving date, or compute an expiry date, without the delivery evidence and the applicable time-computation rule; hold a borderline date for the reviewer.

Record every amended notice and the particulars it changed. An amended assessment is an assessment (ITAA 1936 s 173), but s 170(2) to (4) limit how it can be amended. Do not restart the whole-return period from the latest notice. [ITAA 1936 ss 170, 173](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html); [ATO time limits](https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments).

### 2. Select the section 170 item

Apply item 1 only after testing each of its exclusions for the year, including each regulation item whose column 1 names paragraph (f) of item 1. An individual excluded by paragraph (a), (b), (d), (e) or (f) falls to item 4. The trustee capacity is tested under item 3 and is outside this guide. Test small and medium business entity status under every applicable s 328-110 route. For the medium test, substitute $50 million for $10 million in Subdivision 328-C and read the s 328-110(5)(b) reference to a small business entity as one to a medium business entity; connected entities and affiliates follow that Subdivision.

Item 3A gives a small or medium business entity a conditional second window. The Commissioner may amend within 4 years after the original notice if the individual applies in the approved form before the 4-year period ends and the item 1 period has ended; an application made during the item 1 period is covered by s 170(5) instead. Item 3A lets the Commissioner give effect to the decision on that application; it is not an unrestricted 4-year ATO review period. Item 3A is not a limited amendment period, so the s 170(5) extension for a timely application does not carry an item 3A decision past 4 years. A timely application in the approved form during an item 1 or item 4 period does allow the Commissioner to amend after that period ends. The ATO page says sole traders 'will have 4 years' for 2024-25 and later years; it does not state the statutory conditions, so apply the statute. Item 3A is unavailable for 2023-24 and earlier years and for assessments issued before 1 January 2025.

Items 5 and 6 allow amendment at any time for fraud or evasion, and to give effect to a review, appeal or objection. Section 170(9) allows 4 years after the profit or loss of certain multi-year operations is ascertained. Section 170(9D) to (12) allow amendment at any time for listed provisions and circumstances, some only in one direction. Check whether one applies to the particular; do not treat it as a general extension. Transfer pricing, research and development and CGT matters can have different amendment periods; refer them. [ITAA 1936 s 170](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html); [2025 Regulations s 14](https://www.legislation.gov.au/F2025L01060/asmade/2025-09-09/text/original/epub/OEBPS/document_1/document_1.html).

### 3. Correct the assessment and quantify any shortfall

Recompute the whole return for each corrected particular with the return and topic guides. Taxable income, offsets, losses, Medicare levy and study loan repayment income can all move, so a deduction does not produce a refund equal to the deduction multiplied by one marginal rate. Do not invent missing expenses, dates or valuations; hold incomplete items before submission.

A shortfall amount arises where a tax-related liability worked out on the basis of a statement is less than it would be if the statement were not false or misleading, or where a credit is more than it would be. A correction that reduces the liability is not a shortfall amount. If one year has both favourable and unfavourable corrections, keep separate schedules and refer any netting or penalty interaction to the reviewer. The amendment request is itself a statement, so it must be complete and correct. Where an amendment reduces a liability, s 172 treats the reduction as never payable for the general and shortfall interest charges, unless a later amendment reinstates the liability for that particular; the interest calculations themselves are referred. [TAA Sch 1 s 284-80](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [ITAA 1936 s 172](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html); [ATO penalty page](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements).

### 4. Test liability for each penalty

A false or misleading statement in a material particular attracts a penalty under s 284-75(1) unless an exception applies. The taxpayer is not liable under that subsection if the taxpayer and any agent took reasonable care. The safe harbour also applies where a registered tax or BAS agent made the statement after receiving all relevant taxation information and did not act with intentional disregard or recklessness; the taxpayer bears an evidential burden that the information was given.

Neither the reasonable care exception nor the safe harbour covers s 284-75(2). That penalty applies where an income tax law was treated as applying in a way that was not reasonably arguable, and the resulting shortfall amount is more than the reasonably arguable threshold. An amount equal to the threshold does not meet it. The threshold applies separately to each non-identical matter; identical matters are combined, but similar distinct items are not. The position is judged when the statement was made and need not have been documented then; the taxpayer can demonstrate it when a shortfall is identified. Behaviour and reasonable arguability are reviewer conclusions. [TAA Sch 1 ss 284-75, 284-90](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [MT 2008/2 paras 52, 57-62](https://www.ato.gov.au/law/view/document?docid=MXR/MT20082/NAT/ATO/00001).

### 5. Work out the base penalty amount and its adjustments

Apply the BPA item for the established behaviour or position. If 2 or more items apply, use the one producing the greatest BPA. Significant global entity and Applicable MNE Group doubling rules are referred. Reduce the BPA to the extent it was caused by a treatment that agreed with Commissioner advice, general administrative practice or an approved publication.

Increase the BPA by 20% for obstruction, for not telling the Commissioner within a reasonable time after becoming aware of the shortfall or false statement after it was made, or for a previous BPA under the matching items in s 284-220(1). Reduce it for a voluntary disclosure in the approved form. Before the day the Commissioner tells the taxpayer that an examination is to be made or, if a public request for disclosure about a scheme or transaction that applies to the taxpayer's affairs sets an earlier day, before that earlier day, the reduction is 80% where the shortfall amount or part is $1,000 or more and to nil where it is less than $1,000. A disclosed false or misleading statement without a shortfall is reduced to nil. After an examination notice, it is 20% only where telling can reasonably be estimated to save the Commissioner significant time or resources; the Commissioner may treat a later disclosure as made before the notice. Then apply the s 284-85 formula.

A debit amendment request not prompted by ATO action will usually be a voluntary disclosure. Several disclosures for the same period are added together for the $1,000 test. A part the Commissioner had already identified does not qualify. Remission is a separate Commissioner discretion. The Commissioner must give written notice of the penalty and the reasons for it; reasons are not required if all of it is remitted. A penalty assessment can be objected to under Part IVC. [TAA Sch 1 ss 284-85 to 284-225, 298-10](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [MT 2012/3 paras 35-37, 81-89, 112](https://www.ato.gov.au/law/view/document?docid=MXR/MT20123/NAT/ATO/00001); [MT 2008/2 paras 23-26](https://www.ato.gov.au/law/view/document?docid=MXR/MT20082/NAT/ATO/00001); [PS LA 2012/5](https://www.ato.gov.au/law/view/document?docid=PSR/PS20125/NAT/ATO/00001).

### 6. Lodge the request and reconcile the result

Wait until the original return is processed. Choose a channel: ATO online services through myGov or the ATO app, a registered tax agent through the Practitioner Lodgment Service or the agent form, the paper form for individuals, or a letter with the required content and declaration. Online, overwrite each affected label with the correct amount rather than entering the adjustment. A self-completed paper form must be signed. The ATO charges no fee. Its processing estimates, about 15 business days online and up to 90 business days in writing, are not guarantees, so lodge well before any period ends. [ATO request channels](https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/how-to-request-an-amendment-to-your-tax-return). More than one request can be made within a period. [ATO time limits](https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments).

When the amended notice issues, compare it with the working paper: tax difference, credits, interest, penalties, payment date and effects on later years. Retain the request, acknowledgement, notice and the evidence for each corrected figure.

## Boundary and exception table

| Situation | Required treatment |
|---|---|
| Notice date or delivery evidence is missing or conflicting | Hold the period. Do not substitute the income-year end, the lodgement date or the latest amended notice. |
| Business, partnership, trust, trustee or scheme facts are unknown | Hold item selection; do not assume item 1. |
| Aggregated turnover is near $10 million or $50 million, or the turnover route is unclear | Reconstruct under Subdivision 328-C and hold the item 1 exclusion and item 3A result. |
| A prescribed circumstance may apply | Check the regulation for that income year; treat the item 4 period as possible until resolved. |
| An item 3A application is close to the 4-year end | Flag it as urgent: no s 170(5) extension applies. An objection to the original assessment is usually out of time and needs an extension of time. Once the item 3A amendment issues, an objection limited to its alterations or additions can be lodged within 60 days after its notice. Refer the route to the reviewer. |
| An earlier amended assessment changed the same particular | Apply s 170(2) to (4) to that particular and direction; never restart the whole return. |
| The ATO has started an examination, asked for consent to extend or sought a court order | Refer before any consent or response is given. |
| One year has both favourable and unfavourable corrections | Keep separate schedules; refer netting and penalty interaction. |
| Behaviour, reasonable arguability, safe harbour or accepted-way treatment is disputed | Present the alternative calculations; the reviewer decides. |
| Fraud or evasion is suspected | Stop and refer for specialist and legal advice. |
| A scheme shortfall amount under Subdivision 284-C may arise | Refer: its increase rules differ, and a disclosure before an examination reduces its BPA by 80% even below $1,000, never to nil (TAA Sch 1 ss 284-220(2), 284-225(4)). |
| Transfer pricing, research and development, CGT or a provision listed in s 170(9) to (12) is involved | Refer the amendment period; do not apply the item 1 or item 4 period alone. |

## Worked cases

All cases are hypothetical AUD working papers, not factual defaults or assessments. Behaviour, positions, turnover and dates are stipulated only within each case. Tax figures come from the relevant return workflow, not from this guide. The blocks recompute arithmetic; they cannot prove a notice date, behaviour, reasonable arguability or professional approval.

### Case 1: Voluntary debit amendment before any examination

Mei, a resident employee, finds that her 2026-27 return omitted rental income. The return workflow gives an assessed liability of $18,400 and a corrected liability of $21,150, so the shortfall amount is $2,750. The reviewer concludes she failed to take reasonable care, giving a BPA of 25%, $687.50. She has no previous BPA, did not obstruct the ATO, learnt of the error only after lodging and tells it within a reasonable time after becoming aware. Her online debit amendment, not prompted by ATO action, is accepted as a voluntary disclosure in the approved form before any examination notice, and no public request for disclosure set an earlier day. Because the shortfall is $1,000 or more, the BPA is reduced by 80% to $137.50. If the ATO had notified an examination before she became aware, and her later disclosure saved significant time, the 20% reduction would leave $550. If she had not told the ATO within a reasonable time after becoming aware, and made no qualifying disclosure, the 20% increase would make it $825. Remission and shortfall interest are separate. [TAA Sch 1 ss 284-80, 284-85, 284-90, 284-225](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

```oa-check
name: Reasonable care BPA with an 80% or 20% disclosure reduction
inputs:
  assessed_liability: 18400
  corrected_liability: 21150
  reasonable_care_rate: 25
  increase_pct: 0
  late_increase_pct: 20
  before_notice_reduction: 80
  after_notice_reduction: 20
steps:
  shortfall: corrected_liability - assessed_liability
  bpa: pct(shortfall, reasonable_care_rate)
  penalty_before_notice: bpa + pct(bpa, increase_pct - before_notice_reduction)
  penalty_after_notice: bpa + pct(bpa, increase_pct - after_notice_reduction)
  penalty_late_no_disclosure: bpa + pct(bpa, late_increase_pct)
expected:
  shortfall: 2750
  bpa: 687.50
  penalty_before_notice: 137.50
  penalty_after_notice: 550
  penalty_late_no_disclosure: 825
```

### Case 2: Two disclosures for one year and the $1,000 test

Tom's 2026-27 return contains 2 errors he later finds. He has no previous BPA, did not obstruct the ATO, learnt of both errors only after lodging and tells it within a reasonable time. Before any examination notice, and with no public request for disclosure setting an earlier day, he voluntarily discloses an overclaimed deduction. The shortfall is $640 and the reviewer finds a failure to take reasonable care, so the BPA of $160 is reduced to nil. Later, still before any examination, he discloses a second shortfall of $520 for the same year with the same behaviour. The disclosures for the period total $1,160, which is $1,000 or more, so the first reduction must be revised. On the combined amount the BPA is $290 and the 80% reduction leaves $58. Both errors are stipulated to be in the same return statement. If the reviewer treats them as separate statements, a BPA for the later statement can attract the 20% previous-BPA increase, subject to any remission. [PS LA 2012/5 paras 119-122](https://www.ato.gov.au/law/view/document?docid=PSR/PS20125/NAT/ATO/00001). [TAA Sch 1 s 284-225(3)](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [MT 2012/3 paras 35-37](https://www.ato.gov.au/law/view/document?docid=MXR/MT20123/NAT/ATO/00001).

```oa-check
name: Disclosures for one period are added for the 1000 dollar test
inputs:
  first_shortfall: 640
  second_shortfall: 520
  nil_threshold: 1000
  reasonable_care_rate: 25
  nil_reduction: 100
  standard_reduction: 80
steps:
  first_bpa: pct(first_shortfall, reasonable_care_rate)
  first_only_penalty: first_bpa - pct(first_bpa, nil_reduction)
  total_disclosed: first_shortfall + second_shortfall
  amount_over_threshold: total_disclosed - nil_threshold
  combined_bpa: pct(total_disclosed, reasonable_care_rate)
  combined_penalty: combined_bpa - pct(combined_bpa, standard_reduction)
expected:
  first_bpa: 160
  first_only_penalty: 0
  total_disclosed: 1160
  amount_over_threshold: 160
  combined_bpa: 290
  combined_penalty: 58
```

### Case 3: Reasonably arguable threshold for an individual

Raj's 2026-27 return shows income tax payable of $1,250,000. One per cent is $12,500, which exceeds $10,000, so his reasonably arguable threshold is $12,500. He took reasonable care, so no s 284-75(1) penalty applies, but the reviewer concludes one position was not reasonably arguable. If that position produced a shortfall of exactly $12,500, it is not more than the threshold and item 4 does not apply. If it produced $30,000, item 4 applies and the BPA is $7,500. For a different individual with income tax payable of $300,000, 1% is $3,000 and the threshold is $10,000. [TAA Sch 1 ss 284-75(2), 284-90(1), (3)](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [MT 2008/2 paras 58-61](https://www.ato.gov.au/law/view/document?docid=MXR/MT20082/NAT/ATO/00001).

```oa-check
name: Reasonably arguable threshold must be exceeded
inputs:
  tax_payable: 1250000
  other_tax_payable: 300000
  dollar_floor: 10000
  threshold_pct: 1
  equal_shortfall: 12500
  larger_shortfall: 30000
  position_rate: 25
steps:
  one_percent: pct(tax_payable, threshold_pct)
  threshold: max(dollar_floor, one_percent)
  equal_excess: equal_shortfall - threshold
  larger_excess: larger_shortfall - threshold
  larger_bpa: pct(larger_shortfall, position_rate)
  other_one_percent: pct(other_tax_payable, threshold_pct)
  other_threshold: max(dollar_floor, other_one_percent)
expected:
  one_percent: 12500
  threshold: 12500
  equal_excess: 0
  larger_excess: 17500
  larger_bpa: 7500
  other_one_percent: 3000
  other_threshold: 10000
```

### Case 4: Associate sale moves an employee to the 4-year item

Lena, an employee with no business, partnership or trust interests, sells 2 parcels of listed shares to a stipulated associate under one 2026-27 contract. The capital proceeds are $120,000 and $95,000. The transaction involves associates, has income tax consequences and is relevant to her assessment. Its CGT events have total capital proceeds of $215,000, which is $200,000 or more, so item 1 of the 2025 Regulations s 14 prescribes the circumstance. Item 1 of s 170(1) therefore does not apply and the item 4 period is 4 years after notice; the objection period is also 4 years. In a variant at arm's length with total proceeds of $195,000, where no party includes or deducts $200,000 or more, this regulation item is not met, but every other item still needs checking. [2025 Regulations s 14 item 1](https://www.legislation.gov.au/F2025L01060/asmade/2025-09-09/text/original/epub/OEBPS/document_1/document_1.html); [TAA s 14ZW(1)(aa)](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

```oa-check
name: Associate transaction proceeds against the prescribed 200000 dollar circumstance
inputs:
  first_parcel_proceeds: 120000
  second_parcel_proceeds: 95000
  variant_proceeds: 195000
  prescribed_amount: 200000
  item_4_years: 4
  item_1_years: 2
steps:
  total_proceeds: first_parcel_proceeds + second_parcel_proceeds
  margin_over_prescribed: total_proceeds - prescribed_amount
  variant_margin: variant_proceeds - prescribed_amount
  extra_years: item_4_years - item_1_years
expected:
  total_proceeds: 215000
  margin_over_prescribed: 15000
  variant_margin: -5000
  extra_years: 2
```

### Case 5: A medium business sole trader and the item 3A window

Sam is a sole trader. Under every applicable s 328-110 route, his 2025-26 aggregated turnover is established at $14.2 million, with no route giving a lower figure. That is not less than $10 million, so he is not a small business entity; it is less than $50 million, so he is a medium business entity. Item 1 is not excluded by his business, and no other exclusion applies, so the ordinary period is 2 years after notice. His original notice issued in 2026, after 1 January 2025, so item 3A can apply. If he applies in the approved form during year 3 after notice, the Commissioner can decide and amend only until 4 years after the original notice; no s 170(5) extension applies. If his turnover had been $55 million under every applicable route, item 1 would not apply, item 4 would give 4 years, and a timely application could be decided after that period. [ITAA 1936 s 170(1), (5), (14)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html); [TLAA 2024 Sch 3 item 6](https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html).

```oa-check
name: Small and medium business entity tests for item 3A
inputs:
  aggregated_turnover: 14200000
  alternative_turnover: 55000000
  sbe_limit: 10000000
  mbe_limit: 50000000
  item_3a_years: 4
  item_1_years: 2
steps:
  sbe_headroom: sbe_limit - aggregated_turnover
  mbe_headroom: mbe_limit - aggregated_turnover
  alternative_mbe_headroom: mbe_limit - alternative_turnover
  item_3a_extra_years: item_3a_years - item_1_years
expected:
  sbe_headroom: -4200000
  mbe_headroom: 35800000
  alternative_mbe_headroom: -5000000
  item_3a_extra_years: 2
```

## When to refuse or refer

| Code | Trigger | Required action and verbatim output |
|---|---|---|
| R-AU-AMD-1 | Notice date, delivery evidence, capacity, business, trust, scheme or turnover facts needed to select the s 170 item are missing | Hold the period and dependent deadlines; list the evidence needed. Output: 'I cannot establish the amendment period from the supplied facts. The period and any deadline are held for a qualified Australian reviewer pending the identified evidence.' |
| R-AU-AMD-2 | The period may have ended, an item 3A application is near its end, or an objection or extension of time may be needed | Stop the deadline conclusion and refer. Output: 'I cannot confirm that an amendment is still available or choose between an amendment and an objection. A qualified Australian reviewer must decide the route before the deadline.' |
| R-AU-AMD-3 | The taxpayer is a company, trust, partnership, super fund or other entity, or entity returns must also be amended | Route the entity work. Output: 'This guide covers individuals and sole traders only. The entity amendment must be prepared under the applicable entity guidance and reviewed separately.' |
| R-AU-AMD-4 | Behaviour, reasonable arguability, safe harbour, accepted-way treatment or voluntariness is disputed | Present alternative calculations without choosing the conclusion. Output: 'I cannot determine the penalty behaviour or position from these facts. The alternative penalty calculations are held for a qualified Australian reviewer.' |
| R-AU-AMD-5 | Fraud or evasion, a scheme shortfall amount, an ATO examination, a consent request, a court order, significant global entity status or a remission request is involved | Stop the affected work and refer. Output: 'This matter needs specialist advice. I will not prepare a response, consent or disclosure strategy without a qualified Australian adviser.' |
| R-AU-AMD-6 | Filing or payment is requested without qualified review, or source or record uncertainty remains | Deliver the provisional working paper, unresolved items and reviewer brief only. Output: 'These are working papers for a qualified Australian reviewer. I cannot remove that review or present an unresolved amendment as ready to lodge or pay.' |

Reviewer cash threshold: $0, a workflow control rather than a statutory threshold. Flag every corrected particular, shortfall, credit change, penalty calculation and deadline regardless of amount, including a nil penalty after a reduction. No factual default can cure an unresolved notice date, item selection or behaviour conclusion. Any estimate must be supported, permitted and labelled with its effect.

## Filing and payment

This guide prepares an amendment working paper, not a return or a final assessment. The reviewer or taxpayer lodges the request through an authorised channel. Keep tax file numbers, bank details, signatures and declarations in that channel; use redacted references in these working papers. The ATO's letter route requires those details and specific declarations, so the reviewer must handle a letter. Route any additional tax, interest or penalty payment, and any refund, through the amended notice and the applicable payment workflow. Do not invent a due date.

Deliver all 4 universal outputs required by [workflow-base](../../foundation/workflow-base.md): working paper, reviewer brief, action list and review checklist. The working paper must show the notice chain, the selected s 170 item and its excluded alternatives, regulation checks, turnover status, each corrected particular, the recomputed liability, any shortfall amount, the BPA, increases, reductions and the formula result. The brief must separate established results, permitted estimates, source gaps and withheld decisions. The checklist adds the checks below to the universal checks and retains qualified reviewer sign-off.

### Revision record

Version 1.5, 3 November 2026: re-read s 170, the 2025 and 2015 Regulations, Schedule 3 of the 2024 amending Act, TAA s 14ZW and Division 284, and the current ATO pages and rulings. Corrected the item 3A conditions and its exclusion from s 170(5), added refreshed-period, extension and prescribed-circumstance rules, replaced the general disclosure summary with the statutory 80%, nil and 20% conditions, added all 3 increase triggers, the safe harbour and the s 284-85 formula, and added 5 recomputing cases. An independent recomputation confirmed the cases and led to narrowing the prescribed circumstances to the regulation items that name item 1(f), the item 3A application timing, the objection period for amended assessments and the nil reduction without a shortfall. A second review added the s 328-110(5)(b) substitution, the scheme shortfall referral and the s 170(7) conditions. A third review set the voluntary disclosure deadline to the earlier of the 2 days, completed the associate transaction conditions and limited the late-telling increase to awareness after the statement. The 2018 ATO page on privately owned and wealthy groups was removed because it concerns entities outside this guide. The 2019 point-in-time PS LA 2012/5 PDF was replaced with the current practice statement. Tier 2 and pending professional review remain. Version 1.4 was a structural template migration without substantive sign-off.

## Completion checklist

- [ ] The taxpayer, capacity, income year and applicable compilation and regulation are recorded.
- [ ] The original notice and every amended notice are evidenced, with the particulars each changed.
- [ ] Each s 170(1) item 1 exclusion, prescribed circumstance and turnover status is resolved, and items 3A and 4 are tested.
- [ ] Limits on amending amended assessments, refreshed periods and extensions are applied per particular.
- [ ] The corrected return is recomputed in full; no adjustment is multiplied by a single marginal rate.
- [ ] Any shortfall amount is separated from favourable corrections, with netting referred.
- [ ] Penalty behaviour, reasonable arguability, safe harbour and accepted-way treatment are reviewer conclusions with evidence.
- [ ] The BPA, each increase and each reduction follow ss 284-90 to 284-225 and the s 284-85 formula.
- [ ] The channel, signature and declaration requirements are met, and processing time is allowed for.
- [ ] All 4 universal outputs list unresolved items, and the qualified reviewer has checked and signed the final position.

## Sources

| Source | URL | Read on |
|---|---|---|
| ITAA 1936 compilation 193, C2026C00454; ss 170, 172, 173 and 174 | <https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html> | 2026-11-03; selected sections only; in force from 2026-10-01, no unincorporated amendments recorded |
| TAA 1953 compilation 227, C2026C00468; s 14ZW(1)(aa) | <https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-03; selected paragraph only; compilation period 2026-10-01 to 2027-07-01 |
| Same compilation, Schedule 1 ss 284-75 to 284-90 and 284-220 to 284-225, including the s 284-85 formula alternative text | <https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html> | 2026-11-03; selected sections only |
| Treasury Laws Amendment (2024 Tax and Other Measures No. 1) Act 2024, s 2 and Schedule 3 | <https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-03; commencement and Schedule 3 amendments and application |
| Income Tax Assessment (1936 Act) Regulations 2025, ss 2, 14, 22 and 23 | <https://www.legislation.gov.au/F2025L01060/asmade/2025-09-09/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-03; as made, the only registered version |
| Income Tax Assessment (1936 Act) Regulation 2015, final compilation 8, F2022C01160; s 14 | <https://www.legislation.gov.au/F2015L01415/2022-12-09/2022-12-09/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-03; s 14 items 1 to 13 read |
| ITAA 1997 compilation 268, C2026C00471; s 328-110 | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html> | 2026-11-02; reused from the small business CGT source review |
| ATO time limits on tax return amendments, updated 24 April 2026 | <https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments> | 2026-11-03; full page |
| ATO how to request an amendment, updated 28 October 2026 | <https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/how-to-request-an-amendment-to-your-tax-return> | 2026-11-03; full page |
| ATO amend your tax return entry page | <https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return> | 2026-11-03; navigation only |
| ATO penalties for false or misleading statements, updated 22 June 2026 | <https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements> | 2026-11-03; full page; statute followed where the page summarises |
| MT 2008/2, consolidated 20 August 2025 | <https://www.ato.gov.au/law/view/document?docid=MXR/MT20082/NAT/ATO/00001> | 2026-11-03; paras 23-26, 52 and 56-62 |
| MT 2012/3, consolidated 20 August 2025 | <https://www.ato.gov.au/law/view/document?docid=MXR/MT20123/NAT/ATO/00001> | 2026-11-03; paras 24-26, 33-37, 81-89 and 104-112 |
| PS LA 2012/5, version of 20 August 2026 | <https://www.ato.gov.au/law/view/document?docid=PSR/PS20125/NAT/ATO/00001> | 2026-11-03; BPA table and history; full statement not reviewed |

Not yet confirmed: Qualified Australian sign-off; the giving of notice and time computation for actual delivery channels; s 170(9) to (12) and the listed provisions in detail; MT 2008/1 behaviour standards; netting of favourable and unfavourable corrections in one statement; penalty unit values; shortfall and general interest charges; remission; objections and extensions of time; entity amendments; and later compilations. An editing date, capture or passing arithmetic check does not resolve these dependencies.

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
