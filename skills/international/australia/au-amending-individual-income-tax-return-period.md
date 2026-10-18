---
name: au-amending-individual-income-tax-return-period
description: >
  Establish how Australian individuals and sole traders request or receive
  income-tax assessment amendments, including ordinary periods, conditional
  business self-amendments and restrictions after amended notices. Use for
  correcting assessed income, deductions, offsets, notice dates and missing
  facts before professional review. Distinguishes the original notice,
  later notices and the route-specific amendment period. Includes prior
  source-cited penalty, reasonably arguable position and disclosure material,
  whose separate provenance must be checked before use. Preserves topical
  refusals and applicable workflow outputs. Requires the taxpayer, year,
  statutory qualifications and complete notice chain. This draft is not
  an objection procedure or a completed financial review.
jurisdiction: AU
version: 1.3
category: international
tax_year: 2026
last_updated: 2026-10-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Amending an individual income tax return in Australia

An income-tax assessment can be amended following a taxpayer request or an ATO review. Establish the taxpayer, capacity, income year, correct substantive tax treatment, original notice and every amended notice before selecting the applicable period or calculating a correction. A new amended notice does not automatically restart an unrestricted period for the whole return. [ITAA 1936, section 170](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).

**Scoped v1.3 revision, 18 October 2026:** this revision verifies selected amendment-period routing and notice-chain safeguards. The penalty percentages, thresholds, historical ruling/PDF material, form details and other financial content below retain their 11 October provenance; they have not received a new full financial review. Verify the operative law and facts for the requested period before applying them.

Load workflow-base and income-tax-workflow-base with the applicable country references. Preserve source and period gates, the confirmed profile, refusals, four universal outputs and all domain outputs and checks. Missing mandatory facts remain Needs Input; unresolved law remains held. The reviewer retains sensitive identifiers and signing information and personally handles submission. A correction schedule alone is not a completed financial package.

## Who this is for

Individuals, including sole traders, who need to correct an already-assessed income tax return, and their agents. The ATO's individuals time-limit page directs businesses and super entities to its separate "Time limits for business and super amendments" material instead, so entity amendments are outside this Guide. Partnerships and trusts are covered here only to the extent that the reasonably arguable position threshold in the table below is quoted for them; their own lodgement and amendment processes are not covered.

## Rates, thresholds and deadlines

**Amendment time limits table**  _(https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments)_

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments |
| Ordinary individual period where section 170 item 1 applies | 2 years | Subject to every statutory qualification and prescribed exclusion. Eligible business self-amendments use the conditional four-year table below, not this row alone. |
| ATO-initiated amendment | Select the actual section 170 branch | Two years is the ordinary item 1 period; other items, particular-matter amendments and special powers can differ. Item 3A is a conditional taxpayer-requested route, not an unrestricted four-year ATO review. |
| Amendment outside the time limit | Permitted in exceptional circumstances | Page gives "when evasion or fraud has occurred" as an example of exceptional circumstances |
| Out of time to amend | Objection may be required instead | Page states that if you are out of time to amend your assessment "you may need to lodge an objection instead", and that an extension of time to lodge an objection may be available in some circumstances |

**Reasonably arguable penalty, thresholds and voluntary disclosure table**  _(https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements)_

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements |
| Base penalty amount (BPA) — position on an income tax law that is not reasonably arguable | 25% of the shortfall amount | Applies where the resulting shortfall amount exceeds the threshold below |
| Reasonably arguable threshold — taxpayers other than partnerships and trusts | Greater of $10,000 or 1% of income tax payable worked out based on their tax return | Page's own wording for "other taxpayers"; the same 1% test is applied to PRRT payable and to Australian IIR/UTPR tax payable where relevant |
| Reasonably arguable threshold — partnerships and trusts | Greater of $20,000 or 2% of the entity's net income (if any) worked out based on its return | Page's own wording |
| Voluntary disclosure reduction to the BPA | BPA may be reduced by 20%, 80% or, in some cases, to nil | Page states the BPA "will generally be reduced if you voluntarily tell us about the error" and that the reduction depends on when you tell the ATO and the shortfall amount |
| Adjustment for aggravating circumstances | BPA can be increased | Page lists having "attempted to prevent or obstruct" the ATO from finding out about the shortfall amount or the false or misleading nature of the statement |

**PS LA 2012/5 base penalty amounts by behaviour table**  _(https://www.ato.gov.au/law/view/pdf?DocId=PSR%2FPS20125%2FNAT%2FATO%2F00001&filename=law%2Fview%2Fpdf%2Fpsr%2Fps2012-005c5.pdf&PiT=20191025000001)_

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ato.gov.au/law/view/pdf?DocId=PSR%2FPS20125%2FNAT%2FATO%2F00001&filename=law%2Fview%2Fpdf%2Fpsr%2Fps2012-005c5.pdf&PiT=20191025000001 |
| BPA — intentional disregard of a taxation law by the entity or their agent | 75% of the shortfall amount or part | Practice statement PS LA 2012/5 table of base penalty amounts |
| BPA — recklessness by the entity or their agent as to the operation of a taxation law | 50% of the shortfall amount or part | Practice statement PS LA 2012/5 table of base penalty amounts |
| BPA — failure by the entity or their agent to take reasonable care to comply with a taxation law | 25% of the shortfall amount or part | Practice statement PS LA 2012/5 table of base penalty amounts; the behaviours considered are those exhibited at the time of, or in connection to the making of, the statement |

**MT 2008/2 base penalty amount and threshold example table**  _(https://www.ato.gov.au/law/view/document?docid=MXR%2FMT20082%2FNAT%2FATO%2F00001)_

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ato.gov.au/law/view/document?docid=MXR%2FMT20082%2FNAT%2FATO%2F00001 |
| BPA under subsection 284-90(1) for a penalty imposed under subsection 284-75(2) | 25% of the shortfall amount, or the part of it, that resulted from taking a position on the law that was not reasonably arguable | MT 2008/2 paragraphs 24 and 57 |
| Threshold worked through in MT 2008/2 Example 1 | Greater of $10,000 or 1% of the income tax payable | On the example's facts (tax payable of $50,000) the 1% figure is $500, so the $10,000 limb applied and a $7,000 shortfall did not meet the threshold |

**Four-year business amendment period table**  _(https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/privately-owned-and-wealthy-groups/what-you-should-know/tailored-engagement/assessments-and-amendment-periods)_

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/privately-owned-and-wealthy-groups/what-you-should-know/tailored-engagement/assessments-and-amendment-periods |
| Standard ATO amendment period for most businesses in privately owned and wealthy groups | Four years | Page states the exception is where evidence of fraud or evasion is found, in which case there is no time limit; it also notes different amendment-period rules can apply in some transfer pricing, research and development and capital gains tax cases |

**Sole trader four-year amendment period table**  _(https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments; https://www.ato.gov.au/law/view/document?docid=PAC/19360027/170)_

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments and https://www.ato.gov.au/law/view/document?docid=PAC/19360027/170 |
| Sole traders, 2024-25 and later income years | 4 years | Taxpayer-requested amendment under item 3A of subsection 170(1) ITAA 1936: an application in the approved form within four years, after the ordinary two-year period has ended; applies to assessments issued after 1 January 2025 for income years starting on or after 1 July 2024. Item 3A also expresses a power to amend within four years; do not assume a timely request automatically permits processing after that deadline. It is not an unrestricted four-year ATO review period |
| Sole traders, 2023-24 and earlier income years | Ordinarily 2 years where item 1 applies | Check all qualifications, prescribed exclusions and special powers; sole-trader status alone does not establish the period. |
| Trigger for the period | The relevant statutory notice-giving event | The statute measures the period after that event; verify the actual notice and time-computation/day-adjustment rules. Do not substitute income-year end or automatically reset to a later notice. |
| Further amendments after an amended assessment | Restricted | Subsections 170(2) to (4) limit later amendments and allow particular matters to be revisited only in specified circumstances; business, partnership, trust and avoidance circumstances can take an individual outside the two-year category |

## The method, step by step

1. Identify what the correct assessment should be and quantify the difference between the correct tax liability or credit entitlement and the amount calculated on the information already given — this difference is the "shortfall amount" as defined on the ATO false or misleading statements page (https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements).
2. Establish the relevant section 170 item and every qualification for the taxpayer and income year. Use the ordinary individual table and, where applicable, the conditional item 3A business table. Record when notice of the original assessment was given, every amended notice and the particular matters changed. Apply subsections 170(2), (2A) and (3)-(4) before selecting any later clock; do not restart the ordinary whole-return period from the latest amended notice. Check the actual giving/service evidence and applicable day adjustments. An amendment request and an objection have distinct requirements and can have different periods. Objections retain the referral below.
3. If within the limit, request the amendment through the ATO's amend your tax return process (https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return); step 13 lists the channels.
4. Treat the amendment request itself as a statement to the ATO. The false or misleading statements page states that the penalty can arise from a statement made in a tax return, activity statement or amendment request that results in a shortfall amount, so the request must be complete and correct (https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements).
5. Test whether penalty exposure arises. The same page states that generally there is no penalty where the taxpayer or agent took reasonable care in making the statement, or where the tax law was applied in a way that agrees with ATO advice, published statements or general administrative practices — but notes that reasonable care does not prevent a separate penalty for taking a position that is not reasonably arguable.
6. Where the position depended on an arguable view of the law, work the two-limb test in the tables: the position must fail the reasonably arguable standard and the shortfall amount must exceed the threshold for the taxpayer type, as MT 2008/2 works through in its examples (https://www.ato.gov.au/law/view/document?docid=MXR%2FMT20082%2FNAT%2FATO%2F00001).
7. Prepare the supporting argument and evidence for the position. MT 2008/2 states at paragraph 52 that the general administrative penalty provisions do not require an entity to document their reasonably arguable position at the time the statement is made, and that although the position is determined as at the time the statement was made, the entity has the opportunity to demonstrate its position when a shortfall amount is identified (https://www.ato.gov.au/law/view/document?docid=MXR%2FMT20082%2FNAT%2FATO%2F00001).
8. Make the disclosure voluntarily rather than waiting for ATO contact, because the false or misleading statements page states the BPA will generally be reduced if the taxpayer voluntarily tells the ATO about the error, with the reduction depending on timing and the shortfall amount (https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements).
9. On receipt of a penalty, check the notice. MT 2008/2 states the Commissioner is required under section 298-10 to give written notice of any liability for an administrative penalty and the reasons for it, except where a decision is made to remit all of the penalty (https://www.ato.gov.au/law/view/document?docid=MXR%2FMT20082%2FNAT%2FATO%2F00001).
10. If the client is out of time to amend, or is dissatisfied with a penalty assessment, use the objection route: the individuals time-limit page directs out-of-time taxpayers to lodge an objection (https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments), and MT 2008/2 notes that under subsection 298-30(2) an entity dissatisfied with an assessment of penalty may object in the manner set out in Part IVC of the TAA (https://www.ato.gov.au/law/view/document?docid=MXR%2FMT20082%2FNAT%2FATO%2F00001).
11. Recalculate every related item before submitting: taxable income, offsets, capital losses, Medicare levy and study loan repayment income can all move. A deduction added to a return does not produce a refund equal to the deduction multiplied by one marginal rate.
12. Separate a favourable correction from a tax shortfall. An understated liability or overstated entitlement can create a shortfall amount; a correction that reduces tax is not a shortfall. Do not invent missing expenses, dates or valuations; mark incomplete items for resolution before submission.
13. Choose the channel: ATO online services (in myGov linked to the ATO, select Manage tax returns, then Amend beside the income year), a registered tax agent, the paper amendment form, or a letter containing the required information. Enter the correct totals for the affected labels rather than replacing a total with the adjustment. A paper request must be signed by the taxpayer, the ATO charges no fee, and processing times are estimates, not a guarantee that a request completes before a deadline. Retain the submitted request and its acknowledgement (https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/how-to-request-an-amendment-to-your-tax-return).
14. When the amended assessment issues, compare it with the reconciliation prepared at step 1: the tax difference, interest, penalties, credits, payment date and any effect on later returns. Retain the assessment and the evidence behind each corrected figure.

## Ask the client first

- What is the taxpayer's capacity and income year, which section 170 item and regulation applies, when was the original notice given, and what are the dates and changed particulars of every later assessment? Record the complete notice chain and evidence rather than using the newest notice date as an automatic restart.
- Does the amendment increase or decrease the tax liability, and does it create a shortfall amount as the ATO defines it?
- What is the income tax payable on the return as lodged, so the greater-of threshold for a not reasonably arguable position can be worked out?
- Was the original position based on a view of the law, ATO advice, a published ATO statement or a general administrative practice, and can that be produced?
- Has the ATO already contacted the client about this year (review, audit or information request), which affects whether a disclosure is voluntary and the level of reduction?
- Is the client also a partner in a partnership or a beneficiary of a trust whose return would need amending, which brings the higher partnership and trust threshold into play?

## When to refuse or refer

- Amendments for companies, trusts, partnerships, superannuation funds and other business or super entities — the ATO's individuals page directs these to its separate business and super amendment time limits material.
- Cases where fraud or evasion is in issue, where the individuals page states the ATO may amend outside the ordinary time limit; these need specialist and often legal advice.
- Objections, extension-of-time requests to object, and Part IVC proceedings, including objections against penalty assessments — the process and lodgement periods are not covered by the pages relied on here.
- Requests for remission of penalty and for penalty relief, and the calculation of interest charges on a shortfall — the pages read for this draft state that penalty can be remitted where fair and reasonable but no remission figures or interest rates were taken from an allowed host for this Guide.
- Significant global entities and entities in an Applicable MNE Group, where the ATO pages describe a different base penalty and a penalty multiplier for IIR/UTPR or DMT statements.
- Amendments involving transfer pricing, research and development or capital gains tax where the ATO states different amendment-period rules can apply.

## Sources

- https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html (current section 170, qualifications and amended-assessment limits)
- https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html (Schedule 3 commencement/application and conditional self-amendments)
- https://www.legislation.gov.au/F2025L01060/asmade/2025-09-09/text/original/epub/OEBPS/document_1/document_1.html (section 14 exclusions and sections 22-23 retained prior-year regulations)
- https://www.legislation.gov.au/F2015L01415/2022-12-09/2022-12-09/text/original/epub/OEBPS/document_1/document_1.html (retained section 14 and section 27 application conditions)
- https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments (amendment time limits table)
- https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements (reasonably arguable penalty, thresholds and voluntary disclosure table)
- https://www.ato.gov.au/law/view/pdf?DocId=PSR%2FPS20125%2FNAT%2FATO%2F00001&filename=law%2Fview%2Fpdf%2Fpsr%2Fps2012-005c5.pdf&PiT=20191025000001 (PS LA 2012/5 base penalty amounts by behaviour table)
- https://www.ato.gov.au/law/view/document?docid=MXR%2FMT20082%2FNAT%2FATO%2F00001 (MT 2008/2 base penalty amount and threshold example table)
- https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/privately-owned-and-wealthy-groups/what-you-should-know/tailored-engagement/assessments-and-amendment-periods (four-year business amendment period table)
- https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return (amendment process entry point, cited in the method)
- https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/how-to-request-an-amendment-to-your-tax-return (channels, signature and fee rules, cited at step 13)
- https://www.ato.gov.au/law/view/document?docid=PAC/19360027/170 (section 170 ITAA 1936: amendment periods, item 3A four-year sole trader period, subsections 170(2) to (4))

Drafted by OpenAccountants. Not yet reviewed or approved by a named accountant.

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
