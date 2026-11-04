---
name: au-tpar
description: >
  Use this skill for Australian Taxable payments annual report (TPAR) working
  papers for 2026-27. Covers business and government reporting, cleaning,
  courier and road freight, IT, security, investigation, surveillance and
  construction services; the 10% reporting exemption and construction 50%
  tests; contractor details, cash payments, GST and no-ABN withholding;
  lodgment, non-lodgment advice, amendments and late penalties. Trigger on
  'TPAR', 'taxable payments reporting system', 'TPRS', 'contractor payments
  report', 'report subcontractor payments', 'cleaning contractors ATO report',
  'courier TPAR', 'IT services TPAR' and '28 August'. Prepare a source-cited
  draft for a qualified Australian reviewer, with unresolved facts and legal
  conditions held for input.
version: 1.3
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 payments; standard annual deadline in August 2027"
last_updated: 2026-11-04
review_status: pending_review
depends_on:
  - workflow-base
  - au-lodgment-deadlines-penalties
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Taxable Payments Annual Report v1.3

## Section 1 - Scope statement

This is a content companion to the universal workflow-base for an Australian
TPAR working paper and reviewer brief. It covers the reporting obligation,
service tests, contractor payment classification, payee aggregates and
correction route. It preserves the base's profile confirmation, source
conditions, refusals and 4 required outputs. No separate income tax domain
base applies to this information report. Load the lodgment companion for
broader deadline and penalty work, without overriding the specific rules below.

The primary period is payments made from 1 July 2026 to 30 June 2027. The source
review date is 4 November 2026. This is a Tier 2 source-cited draft awaiting a
qualified Australian practitioner's review. That date establishes selected
source checks, not the law or filing specifications for the remainder of the
period. Establish operative law, amendments, reporting format and any extension
for the requested period before preparing a report for use. Hold an unresolved
condition under R-AU-TPAR-SOURCE. Historical and other years need their own
verified figures and source versions.

This guide does not prepare or lodge an income tax return, BAS, payroll report,
no-ABN annual report or grant recipient's return. It does not decide worker
status, GST registration, foreign resident withholding or whether a grant is
NANE income without the relevant authority and evidence. Route those matters
to the applicable loaded guide and practitioner. A TPAR does not itself assess
tax or replace withholding, remittance or payment-summary obligations.

### Intake additions

Infer what the records establish, then confirm the profile once under the base.
Ask only for missing facts, grouping substantive questions within its limits:

1. What entity, ABN, reporting period and authorised reviewer are involved? Is
   the payer a business or a federal, state, territory or local government entity?
2. Which services does it supply, and which contractors deliver them on its
   behalf? Obtain contracts and invoices to distinguish services, goods,
   incidental services, employees and labour hire.
3. For each exemption category, what consideration was received for those
   services during the period? What is the relevant GST turnover, the date
   supplies began and any GST group membership? Obtain the measurement date,
   monthly turnover bridge and both candidate projection windows where relevant.
   Record the unresolved legal-period question described below.
4. For construction, obtain current-year income and activity evidence and
   immediately preceding-year income. Confirm the payer's ABN and contractor
   payments for construction services in the report year.
5. Obtain the full cash payment extract, bank reconciliation, supplier master,
   invoices, credit/refund records, ABN/entity changes, addresses, GST amounts,
   withholding, payment summaries and any prior annual reports. Obtain grant
   program/date, recipient ABN, supplier statements and NANE authority for a
   government report.
6. Which payments were excluded and why? Are any service classifications,
   foreign transactions, exemptions, overlapping reporting items or source
   records unresolved? Has a below-threshold entity chosen to report?
7. What channel, current specification, deadline/extension, original receipt
   and prior payee details apply? Is this an original report, omitted payee,
   amount amendment, payee-detail correction or non-lodgment advice?

Never request bank details merely because the ATO may ask for them. Collect
only what the authorised channel and engagement require. For a v3.0.1 file,
complete the optional payee telephone, BSB, account number and email fields
where the payer already holds that data: the specification's optional-field
rule says payers must complete such a field if the data is available. [S26]
This guide needs no real client data for its examples or repository checks.

## Section 2 - Filing requirements

### Determine the payer's obligation

| Payer/service | Required factual test and reporting route |
| --- | --- |
| Building and construction | Payer carries on a business primarily in this industry, has an ABN and pays for construction services. Primarily means current-year construction activity at or above the construction threshold, current-year construction income at or above it, or immediately preceding-year construction income at or above it. Prior-year activity alone is not a limb. [S2] [S5] |
| Cleaning | ABN holder supplies cleaning services and pays another entity wholly or partly for those services on its behalf. Apply the cleaning exemption separately. [S1] [S3] [S4] |
| Courier and road freight | ABN holder supplies either service and pays for them on its behalf. Combine courier and road freight receipts for this exemption category. [S1] [S3] [S17] |
| IT | ABN holder supplies IT services and pays for them on its behalf. Apply this category's exemption separately. [S1] [S3] |
| Security, investigation or surveillance | ABN holder supplies these services and pays for them on its behalf. Combine these services within their category, separately from the other categories. [S1] [S3] |
| Government | Federal, state, territory and local government entities report qualifying service payments. Federal, state and territory entities also report grants to ABN holders. Local government does not report grants under this item. The grant recipient ABN condition is not a blanket condition for service payments. Apply government exemptions separately. [S1] [S10] |

Construction reporting arises under TAA Schedule 1 Division 405 and regulation
70, rather than treating every business as a Division 396 reporter. Government
services/grants and the other business service categories arise under Schedule
1 section 396-55, including table items 1, 2 and 11 to 14 respectively. [S1] [S2]

The business service exemption is conditional: below-threshold receipts do not
exempt a transaction described in another section 396-55 table item, or a
transaction the entity has chosen to report within the permitted time. Giving
the report evidences that choice. Check both conditions before concluding that
no report is required. No general service exemption applies to government
reporting merely because a business test would have failed. [S3]

### Deadline, channel and corrections

Use the standard deadline and adjustment rule in the figures table. For this
period, the nominal date falls on a Saturday. The first following weekday is
Monday 30 August 2027; confirm any relevant public holiday, extension or
specific ATO direction before fixing the actual deadline. Do not leave an
unqualified nominal date in the brief, example conclusion or checklist. [S8] [S15]

Lodge through supported SBR software, a file meeting the current TPAR
specification, Online services for business, Online services for individuals
and sole traders, or a registered tax/BAS agent's supported channel. Save the
submitted report and receipt; a saved draft is not lodgment. Paper reports
are not accepted after 28 August 2025. The ATO's lodgment page describes
saved drafts and History receipts. Verify the current navigation rather than
assuming historical menu labels remain available. [S8]

| Situation | Required route |
| --- | --- |
| Obligation does not arise | Document the tests and exclusions first. The ATO says non-lodgment advice can be submitted when no report is required, and should be lodged where no contractor payments for services and no grants to ABN holders were made. Submit it through the supported online service; retain its reference and history. Advice can cover multiple years or an expected future cessation, but does not exempt a transaction that must be reported. [S11] |
| Gross, GST or no-ABN withholding amount is wrong | Lodge an amended TPAR for the affected payee through the supported software or online amendment form. Keep all other payee details exactly as originally reported so the amount amendment matches the original. Preserve the original and corrected amounts. [S12] |
| Payee details are wrong, excluding amounts | Do not lodge an amount amendment merely to change identity/details. Send the ATO the old and correct details, reporting year and identifying payer information using the correction-message route on its amendment page. Agents use Practice mail; businesses use the specified secure-mail route. [S12] |
| Payee omitted from original report | Lodge another TPAR containing the payer information and new payee(s). Do not resend the unaffected original payees as new records. [S12] |
| Both amounts and identity are wrong, duplicate report or uncertain original identity | Reconcile the original receipt and obtain ATO/practitioner instructions for the sequence before sending. Keep the affected correction at Needs Input. [S12] |

A non-lodgment advice is not an amendment. Give each payee/year/ABN a traceable
original, additional or correction status and retain the submission receipt.

## Section 3 - Rates and thresholds

This is the single home for operative figures. Examples below apply these
values to stated hypothetical facts; they are not additional rate sources.

| Figure | Period/value and condition | Primary authority |
| --- | --- | --- |
| Report year | Cash payments from 1 July 2026 to 30 June 2027 | [S6] [S8] |
| Nominal deadline | 28 August after the report year; if a weekend or public holiday, the first business day after it. The 2027 date requires the holiday/extension confirmation above | [S8] [S15] |
| Business service exemption | Relevant receipts strictly less than 10% of relevant GST turnover, subject to the other-item and voluntary-choice conditions; equality is outside this exemption | [S3] section 5 |
| Relevant GST turnover | Current GST turnover at period end if supplies have been made for at least 12 months; otherwise projected GST turnover within the GST Act meaning, including grouping. Section 188-20 uses the measurement month and next 11 months; ATO explanatory guidance describes the following full financial year. Hold an unreconciled projected-period decision | [S3] section 3; [S4] [S17] [S23] [S24] |
| Construction threshold | 50% or more: current activity, current income or immediately preceding income; not prior activity. Other payer/payment conditions still apply | [S2] regulation 70(1), (4) |
| No-ABN small supply exception | Total payments for the same supply at or below $75 excluding GST. Aggregate actual and proposed payments for that supply; do not split invoices or instalments to obtain the exception | [S9] [S18] [S21] [S27]; TAA Schedule 1 section 12-190(4)(b) sets $50 or the higher amount prescribed for GST Act section 29-80(1); GST Regulations 2019 section 29-80.01 prescribes $75 |
| No-ABN withholding rate | Generally 47% of the payment where section 12-190 applies and no exception is established. The top rate is defined by regulation 5 and applied by regulation 38; verify the operative components for the payment date | [S2] [S19] |
| Reported amounts | Whole dollars for reported gross including GST and withheld tax, GST and no-ABN withholding. Fixed-width file specification v3.0.1 sections 6.61 to 6.63 truncate cents in the aggregated record amounts. Each numeric field is 11 digits, right justified and zero filled; gross must be greater than zero, with zero permitted for GST and withholding. Verify other channels separately | [S7] [S26] |
| FTL base | 1 penalty unit per 28 days or part overdue, capped at 5 units; apply the actual due date and assessment rules | [S13]; TAA Schedule 1 section 286-80 |
| Penalty unit | $364 for infringements on/after 1 July 2026; $330 from 7 November 2024 to 30 June 2026. Verify the applicable infringement period rather than assuming a guide date controls it | [S14] |
| Ordinary FTL multipliers | 2 for the section 286-80(3) medium-withholder, assessable-income or current-GST-turnover tests; 5 for section 286-80(4) large-withholder, assessable-income or current-GST-turnover tests | [S20] |
| Income/turnover limbs | More than $1 million and below $20 million for subsection (3); $20 million or more for subsection (4). Apply the statutory income year or GST turnover timing and precedence, not just a withholding label | [S20] |
| SGE FTL | 500 times the base only if section 286-80(4A) conditions apply, subject to (4B) and other applicable provisions. Do not automatically multiply every entity described as an SGE | [S20] |

These are reporting and penalty parameters. They are not a TPAR income tax rate
or a tax liability on contractor receipts. Internal reviewer thresholds below
are workflow controls, not statutory concessions.

## Section 4 - Computation rules

### Step 1 - Establish sources and the reporting unit

Confirm period, payer entity/ABN, government status and the loaded contract.
Read the operative authority and channel specification. Record source version,
passage and date checked. A current compilation landing page identifies the
instrument; it does not prove that every operative provision or commencement
was reviewed. Stop an affected position where law, commencement or filing
mapping is unresolved. Do not replace a source hold with a monetary default.

### Step 2 - Apply the appropriate service test

For a non-construction business category, reconcile the relevant consideration
received during the period and relevant GST turnover under [S3]. Include
service receipts whether employees or contractors supplied the customer's
service. Use the correct entity or GST group turnover. Do not substitute profit,
accrual revenue or an unreconciled 'business income' figure for the statutory
denominator. Document any GST and other statutory adjustments to both sides.
Compute the category percentage without rounding before comparing it with the
exemption boundary. Combine courier and road freight; keep other exemption
categories separate. A qualifying service business still needs a relevant
contractor payment before it has such a transaction to report. [S1] [S3] [S17]

Where supplies have been made for less than 12 months, [S3] imports projected
GST turnover within the GST Act meaning, measured at reporting-period end.
Section 188-20 uses the measurement month and next 11 months, including for a
GST group. The ATO web guidance and nonbinding LCR Appendix 1 instead describe
the following full financial year. At a June measurement, the ordinary calendar
windows are June to May and July to June respectively. The selected sources do
not explain a TPAR-specific shift or override. Do not present either period as
a reconciled legal conclusion or substitute the partial year's business income.
Obtain the monthly bridge for both windows, apply relevant exclusions such as
section 188-25 and fire R-AU-TPAR-SOURCE until the period is reconciled to
applicable authority. Supported forecast figures alone do not clear this legal
source hold. This is a gap in the inspected evidence, not a finding that no
reconciling authority exists elsewhere. [S3] [S4] [S17] [S24] [S25]

For construction, test the 3 distinct limbs in the figures table. Meeting the
prior income limb can require reporting in the following year even if current
income has fallen, provided the payer still meets the other conditions and
makes relevant payments in that year. A prior activity result alone does not
create that income look-back. Record the measure supporting current activity;
there is no invented universal headcount or hours proxy. [S2] [S5]

Regulation 70(5) includes these activities performed on, or in relation to,
any part of a building, structure, works, surface or subsurface: alteration,
assembly, construction, demolition, design, destruction, dismantling, erection,
excavation, finishing, improvement, installation, maintenance, management of
building and construction services, modification, organisation of building
and construction services, removal, repair and site preparation. ATO examples
include cabinet making, landscaping, surveying, architectural drafting,
engineering, project management and equipment hire with an operator. ATO
guidance distinguishes maintenance/repair of tools and equipment and
testing/tagging tools from construction work [S5]; regulation 70(5) itself
lists maintenance and repair without that carve-out. Dry equipment hire is a
goods rental.
A hardware retailer arranging installation is not automatically primarily in
construction; a separate installation entity must apply its own facts. Each
principal and subcontractor tests its own obligation, rather than inheriting
the other's reporting conclusion. [S2] [S5]

For government, use the government service/grant rules, not business income
percentages. Check the exact payer exemption, including whether it applies to a
department, and the transaction exclusions. A non-exempt agency paying on behalf
of an exempt government entity can still need to report. Overseas service
providers can be reportable under this route: do not import the private business
foreign-work exclusion. Retain grant dates, program names, recipient ABNs,
supplier-statement status and an evidenced NANE indicator where required. [S10] [S7]

### Step 3 - Classify every source payment

| Position | Treatment and required evidence |
| --- | --- |
| Relevant contractor/subcontractor service | Include the qualifying cash payment, whether supplier is a sole trader, company, partnership or trust. The business must have engaged the supplier for the relevant service; another business's report does not substitute for this payer's obligation. [S5] [S6] |
| Mixed goods and services | Include the whole qualifying payment where service is more than incidental. Goods-only and incidental-service supplies are excluded under the applicable rule; do not discard all mixed invoices. Retain the contract/invoice basis. [S2] [S6] [S10] |
| Unpaid invoice at year end | Exclude from this year's cash extract and carry a link to the following year's payment. The invoice date alone does not allocate the year. [S6] |
| Employees, voluntary-agreement and labour-hire payments | Exclude the applicable PAYG/STP payments from mandatory business TPAR reporting; route to the appropriate reporting obligation. Worker status and the actual arrangement need evidence. [S6] |
| No ABN with withholding | First recognise the mandatory business reporting exclusion for Division 12 withholding: section 396-55 items 11 to 14 paragraph (b) for the service categories, and regulation 70(3) for construction, which excludes a 'withholding payment' within ITAA 1997 section 995-1(1) paragraph (a), even if the amount is not withheld. The ATO nevertheless permits the no-ABN annual information to be reported in either TPAR or the PAYG no-ABN annual report, once only. Record the expressly chosen annual route and reconcile gross, net and withheld separately. [S1] [S2] [S6] [S10] [S28] |
| Foreign resident payment | Business exclusions include foreign resident payments subject to PAYG foreign resident withholding and payments for work performed overseas. A foreign resident payment for work in Australia that is not subject to PAYG withholding is reportable. Verify source and withholding facts; government services have a distinct rule. [S6] [S10] |
| Same consolidated or MEC group | Apply the relevant business exclusion with evidence of actual group membership. Do not confuse income tax consolidation with GST grouping used in the exemption calculation. [S1] [S2] [S6] |
| Private or domestic project | Exclude a private owner's home payment from the business report under the applicable rule. Distinguish the business's service to a customer from the owner's personal expenditure. [S6] |
| Government services | Include qualifying service payments and mixed payments subject to the government exemptions. Goods-only, incidental services, specified payment channels/transactions and other exclusions require the government source, not a business checklist. [S10] |
| Government grants | Report qualifying grants by federal, state and territory entities to ABN holders. Local government grants, grants to individuals without an ABN and grants to other government entities fall outside the listed grant requirement. Establish the grant character and any specific exclusion. [S1] [S10] |
| Refund, credit, non-cash consideration, cancelled payment or unresolved duplicate | Keep the original item and reconciliation link. Confirm the operative rule and channel handling before netting, deleting or exporting an affected amount. No silent sign change or duplicate removal. [S1] [S9] |

For government services, [S10] lists payment-channel exclusions (including
specified BPAY, direct-debit, card and processor payments), payments to other
Australian government entities, specified utilities, employee travel,
commercial/hotel accommodation, leases of goods, licences and financial
supplies. Apply the exact conditions, including any administrative permission
to include an otherwise excluded item where exclusion would add burden. An
exclusion label without its facts is insufficient. Differentiate an agent
paying a government agency's funds from a property manager paying a
nongovernment client's funds. Preserve the actual payer relationship. [S10]

### Step 4 - Deal with no-ABN withholding separately

Establish section 12-190 and its exceptions using documents. The small supply
exception uses all payments for that supply. Other possible exceptions include
input-taxed supplies and supported supplier statements, subject to their
conditions. A business entitled to an ABN cannot use a hobby statement to
avoid quoting it. Do not rely on a statement known or reasonably suspected to
be false. A missing or suspect ABN is not a default permission to pay in full.
The parties may agree to defer payment whilst an ABN is obtained; full payment
on a promise of later quotation does not remove withholding. Non-cash
consideration can also require withholding and needs its own verified handling.
[S9] [S18] [S19]

Where withholding applies, compute from the payment using the verified rate,
retain the net payment and withheld liability, and give the no-ABN payment
summary at net payment or as soon as possible afterwards. Register/report/pay
through the required PAYG activity statement process. The chosen annual TPAR
route does not waive those duties. The ATO states that a GST input tax credit
cannot be claimed for payments withheld from under these rules; do not infer
an entitlement merely because an invoice shows GST. Keep those records
separate and route any GST/deduction consequences for proper review. [S9] [S19]

### Step 5 - Aggregate and reconcile

Keep one traceable row per source item, including excluded items with reasons.
Aggregate reportable annual amounts by report year and actual payee identity,
with separate ABN records if an ABN changed. Check ABN/name and GST registration
against the invoice and available ABN Lookup evidence; do not invent a valid
ABN or merge separate legal entities with similar names. The ATO asks for ABN
if known: genuine no-ABN reporting is not rejected solely for having no ABN.
Name, address and other required identifiers still need support. [S7]

For government grants, retain separate annual totals for each recipient and
grant program. Different programs paid to the same ABN must not be merged.
Payments under the same program to the same recipient may be reported
separately or aggregated; when aggregated, the grant date may be the end of
the relevant financial year. Keep the underlying payment dates either way.
Keep service payments and grants distinguishable in summaries and the
channel mapping rather than combining them into one undifferentiated payee
record. [S10]

Reconcile gross including GST and withheld tax to the cash extract plus
withholding liabilities, excluding only evidenced classifications. Reconcile
GST and withholding separately. Preserve cents in source records and
reconciliation. For the fixed-width v3.0.1 file, first aggregate the supported
record amounts with source cents intact, then truncate cents from each gross,
GST and withholding field. Do not truncate each invoice before summing. Retain
a source-to-field cents bridge. The numeric fields accept no sign, decimal
point, comma or dollar symbol; reject a negative value, zero gross or width
overflow rather than dropping signs, digits or records. Resolve the underlying
refund or other classification and use a supported route. These selected file
rules do not establish the mapping or conversion of an SBR or online form.
Hold an unverified channel/version or unrepresentable record under
R-AU-TPAR-SOURCE. [S7] [S26]

Keep contractor name, address, ABN, gross, GST and withholding records and use
the ATO worksheet if software cannot produce the report. The ATO may request
phone, email or bank details; a v3.0.1 file includes those the payer already
holds, as described in the intake. An optional payee information statement can
tell contractors what was reported in whole dollars; there is no general
obligation to issue that statement for ordinary TPAR reporting. Keep the
separate no-ABN payment-summary duty above. [S7] [S8] [S26]

### Step 6 - Prepare the 4 reviewer outputs

Deliver the universal working paper, reviewer brief, action list and review
checklist. These are drafts for review, with no claim of actual lodgment.

Use the base's A to L transaction columns: A date, B counterparty/payee, C
description, D source gross amount, E classification code, F treatment,
G citation, H default flag, I default reason, J reviewer flag, K reviewer reason
and L exclusion/reason. Add named columns for payer/year, source file/row and source ID, paid date,
service category, payee name/address, ABN and identity history, source gross,
GST, no-ABN withheld, net cash, reporting gross, report status, annual-route
choice, channel/version, untruncated record totals, exported fields, cents
bridge, original receipt and amendment link. For government,
add grant date/program, supplier statement and evidenced NANE status. Record
this column map in both workbook and brief. Do not put a nonzero report amount
on an excluded row. Retain the source amount and exclusion reason.

Provide intake/period/source registers, transaction classification, turnover
and construction tests, payee summaries and an original/correction control
sheet. Build summaries from transaction formulas, not typed totals; reference
them in the channel field mapping. Apply the base's recalculation, completeness
and presentation checks. Reconcile to the source extract and prior receipts
before generating a filing field sheet. No working paper was prepared from
real records by the repository examples in this guide.

The brief adds: reporting-unit rationale; every test's numerator, denominator,
period, projection/group basis and exemption conditions; government route;
reportable/excluded cash bridge; gross/GST/withheld totals and payee count;
no-ABN annual-report choice; original/amendment/new-payee/detail-correction
route; source and holiday/specification holds; exact deadline and submission
status. Include the full refusal trace and an impact for every unresolved item,
using 'unknown' where it cannot be established. TPAR gross is information
reported, not tax payable. State withholding liabilities and potential
penalties separately from gross reporting differences.

The action list names the client/reviewer owner, missing evidence or decision,
actual deadline and impact. The checklist retains base sections A to E in
order, includes every flag/default/T2 decision and adds the topical checks
below to Section D, with Section E sign-off last. Do not mark reviewer agreement or a lodged status without evidence.

## Section 5 - Edge cases and special rules

### Topical refusal catalogue

Apply the base's R-REVIEWER-MISSING and R-CONTENT-MISMATCH as loaded. Before
classification/computation, test every code below and record cleared/fired
with the reason. A hold affects the unresolved position; unrelated supported
work may continue without labelling the report complete. Reproduce a fired
message verbatim.

| Code | Trigger | Verbatim output |
| --- | --- | --- |
| R-AU-TPAR-SOURCE | Requested period, operative law, projection/group source, reporting specification, money conversion or applicable deadline cannot be established | I cannot finalise the affected TPAR position because its period, applicable authority or reporting rule is not established. Keep it at Needs Input until the cited source condition is resolved. |
| R-AU-TPAR-CLASSIFICATION | Material payer/service, worker status, government exemption, threshold input or annual-report choice is unresolved | I cannot classify the affected TPAR item from the available facts. Obtain the missing evidence or reviewer decision before including or excluding it. |
| R-AU-TPAR-IDENTITY | Required payee identity or original correction matching information is missing or conflicting; a genuine no-ABN annual route alone does not trigger this | I cannot finalise the affected payee record because required identity or correction details are missing or inconsistent. Retain the source records and resolve the mismatch before export. |
| R-AU-TPAR-RECON | Source completeness, cash/GST/withholding reconciliation, duplicate reporting or annual totals do not reconcile | I cannot finalise this TPAR because its records or totals do not reconcile. Resolve the difference and repeat the affected checks before delivery. |
| R-AU-TPAR-AUTHORITY | Asked to submit, amend, message the ATO or mark a report lodged without the authorised engagement, practitioner review or receipt | I cannot submit or mark this TPAR as lodged without the required authority, professional review and submission evidence. I can prepare the supported working paper and list the outstanding actions. |

### Permitted factual defaults

These defaults never establish law, eligibility, elections, a payee's ABN or a
withholding exception. Ask the grouped factual question first where required.

| Situation | Permitted treatment, alternative and impact |
| --- | --- |
| Clearly documented zero GST or zero withholding on a supported item | Carry the explicit zero as a source fact. A blank field is unknown, not zero. If the document is incomplete, hold the affected field; no cash difference can be invented. |
| Optional TPAR payee information statement not requested | Prepare no optional statement unless required by the engagement. Annual report amounts do not change. This never removes a no-ABN payment-summary duty. |
| Reviewer has not chosen a voluntary below-threshold report or a no-ABN annual route | No election or annual-route default is permitted. Hold the affected decision; disclose the gross/withheld reporting swing from known amounts. |
| Missing paid date, service scope, GST group, projected turnover, ABN/name/address, government grant status or channel conversion | No factual default is permitted. Retain the item as Needs Input and quantify only the supported alternative effect. |

### Reviewer attention thresholds

These are internal review controls, not materiality waivers. Flag every
classification judgment, source hold, annual-route choice, government exemption,
ABN change, foreign payment, correction and default regardless of amount.
Escalate any nonzero withholding/penalty consequence or unreconciled difference
as high attention. Also flag a payee's annual reported gross of $10,000 or more,
or a proposed classification/correction changing reported gross by $1,000 or
more, even when the classification is certain. List smaller changes as well.
Order high flags by established cash effect, then reported gross effect;
unknown cash effect stays explicit and cannot be treated as zero. The reviewer
may tighten these controls but cannot use them to omit a required field or
source row.

### Penalty administration and safe harbour

The ATO describes warning by phone or in writing before applying an FTL
penalty, followed by a written penalty notice. A third-party data report such
as TPAR is not protected by the usual nil/refund late-lodgment practice.
Remission of all or part may be requested on the circumstances, ordinarily
after outstanding documents are lodged. A registered tax/BAS agent engagement
alone does not establish safe harbour: retain evidence that all relevant
information was supplied in time to enable on-time lodgment and that the
agent's failure was not reckless or an intentional disregard of tax law.
Record safe-harbour and remission separately; a refusal of one does not
automatically dispose of the other. [S13]

### Common errors to prevent

Do not apply the business exemption to construction, test courier and freight
separately, use prior-year activity as construction income, omit equality at
the construction boundary, use accruals for cash payments, drop mixed invoices,
combine distinct ABNs or assume no tax payable means no late-report penalty.
Do not conflate business and government exclusions, report no-ABN amounts in
both annual reports, lodge on paper, treat a saved draft as submitted or use an
amount amendment for every payee-detail correction.

### Worked positions

All entities and records below are hypothetical. Assume only the facts stated;
operative sources, integer-dollar channel mapping and qualified review still
need confirmation for a live report. The executable blocks check arithmetic,
not legal classification, filing or completeness.

#### Position 1 - Sparkle cleaning, retained A to F extract

Sparkle Commercial Cleaning Pty Ltd is GST registered and operates for the
whole of 2026-27. Its business income is $600,000 and receipts for cleaning
services are $90,000. For this hypothetical, a source reconciliation establishes
that the relevant GST turnover is also $600,000 and that $90,000 is the relevant
consideration received for the exemption. This equality is a stated fact,
not a permission to substitute income for GST turnover in another engagement.
The rest of its business sells cleaning products. Sparkle has an ABN and paid
contractors for cleaning on its behalf. The relevant exemption share is 15%,
so it is outside the below-threshold exemption. No other exemption applies.
[S1] [S3]

| Item | Source facts | Position |
| --- | --- | --- |
| A | ABN sole trader, GST registered, $44,000 paid for cleaning including $4,000 GST | Report gross $44,000, GST $4,000, withheld $0 |
| B | ABN company, not GST registered, $12,500 paid for cleaning | Report gross $12,500, GST $0, withheld $0 |
| C | Individual supplying cleaning as a business, no ABN quoted, $2,000 invoice paid in March 2027; no withholding exception applies | Withhold $940 at the verified rate, net cash $1,060. Mandatory business TPAR exclusion applies, but Sparkle expressly chooses the ATO-permitted TPAR annual route: gross $2,000, GST $0, withheld $940; no duplicate PAYG no-ABN annual report |
| D | Chemicals wholesaler, $8,000 paid for products only | Exclude goods-only payment with source amount and reason retained |
| E | ABN sole trader, $3,300 cleaning invoice dated 20 June 2027, paid 8 July 2027 | Exclude unpaid invoice from this year; link to 2027-28 payment/reporting review |
| F | Labour hire firm supplying 2 cleaners under an on-hire arrangement, $30,000 paid | Exclude from this TPAR; preserve the actual arrangement and correct PAYG reporting route |

On these supported facts and the expressly chosen annual route, report
3 contractors, gross $58,500, GST $4,000 and no-ABN withheld $940. Actual cash
to A, B and C is $57,560; adding the withholding liability restores gross.
Give C the separate payment summary at net payment or as soon as possible
afterwards and report/remit the withholding through the activity statement.
If the supported annual route were the PAYG no-ABN annual report instead,
TPAR would contain A and B only: 2 payees, gross $56,500, GST $4,000 and no-ABN
withheld $0. The $940 liability does not disappear. The annual-route choice
changes reported data, not the withholding amount. [S6] [S9] [S19]

The report is due under the verified deadline/adjustment rule in Section 2.
Hold submission until the qualified reviewer has checked the extract, annual
route, payee identity, actual deadline and channel mapping.

```oa-check
name: Sparkle cash gross and expressly chosen TPAR no ABN annual route
inputs:
  turnover: 600000
  cleaning: 90000
  a: 44000
  b: 12500
  c: 2000
  rate: 0.47
  gst_a: 4000
steps:
  share: cleaning / turnover * 100
  withheld: c * rate
  net_c: c - withheld
  gross: a + b + c
  net_cash: a + b + net_c
  gross_bridge: net_cash + withheld
  gst: gst_a
  alternate_tpar_gross: a + b
expected:
  share: 15
  withheld: 940
  net_c: 1060
  gross: 58500
  net_cash: 57560
  gross_bridge: 58500
  gst: 4000
  alternate_tpar_gross: 56500
```

#### Position 2 - Sparkle below the exemption boundary

Change only the relevant cleaning receipts to $50,000. The reconciled relevant
GST turnover remains $600,000, giving 8.333333...%. For this example the
transactions fall in no other section 396-55 item and Sparkle has not chosen
to report them. The business service exemption therefore applies. Sparkle may
submit non-lodgment advice because no report is required. The ATO's 'should
lodge' case, no contractor payments or grants, does not describe Sparkle, which
paid contractors. Do not lodge a nil report as an unexplained substitute. C's separate withholding, remittance and annual
information obligations still need their supported reporting route. The
alternative does not remove that liability. [S3] [S11]

```oa-check
name: Sparkle lower receipts with other exemption conditions stipulated
inputs:
  turnover: 600000
  cleaning: 50000
steps:
  share: cleaning / turnover * 100
  threshold_receipts: turnover * 0.1
  gap: threshold_receipts - cleaning
expected:
  share: 8.33333333
  threshold_receipts: 60000
  gap: 10000
```

#### Position 3 - Combined courier and freight at equality

A full-year ABN business has verified relevant GST turnover of $200,000,
courier consideration received of $12,000 and freight consideration received
of $8,000. It paid an ABN contractor $5,500, including $500 GST, for these
services on its behalf. The combined share is 10%, so the below-threshold
exemption does not apply. Testing the service receipts separately would give
6% and 4% and the wrong conclusion. Report this supported contractor payment
under the correct service category. [S1] [S3]

```oa-check
name: Courier and road freight combined at the exemption boundary
inputs:
  courier: 12000
  freight: 8000
  turnover: 200000
  gross: 5500
  gst: 500
steps:
  combined: courier + freight
  share: combined / turnover * 100
  courier_alone: courier / turnover * 100
  freight_alone: freight / turnover * 100
  net: gross - gst
expected:
  combined: 20000
  share: 10
  courier_alone: 6
  freight_alone: 4
  net: 5000
```

#### Position 4 - Construction prior income versus prior activity

An ABN construction payer has current construction income of $40,000 out of
$100,000, documented current construction activity of 40%, prior construction
income of $50,000 out of $100,000 and a current-year contractor construction
payment of $11,000 including $1,000 GST. The prior income limb meets the
threshold exactly; report the qualifying current payment, subject to normal
exclusions. If prior income were instead $40,000 and only prior activity were
60%, none of the stated limbs would be met. Do not carry the prior activity
measure into an invented look-back test. The reporting difference is $11,000,
not $11,000 tax. [S2] [S5]

```oa-check
name: Construction prior income equality and alternative below it
inputs:
  current: 40000
  current_total: 100000
  prior: 50000
  prior_total: 100000
  alternative_prior: 40000
  gross: 11000
  gst: 1000
steps:
  current_share: current / current_total * 100
  prior_share: prior / prior_total * 100
  alternative_share: alternative_prior / prior_total * 100
  ex_gst: gross - gst
expected:
  current_share: 40
  prior_share: 50
  alternative_share: 40
  ex_gst: 10000
```

#### Position 5 - Supplies began part way through the year

An ABN security business began making supplies late in the report year. Relevant
consideration received is $20,000; partial-year business income is $40,000. Its
supported forecast is $205,000 for the following full financial year (July 2027
to June 2028) and $195,000 for the measurement month and next 11 months (June
2027 to May 2028). The windows share July 2027 to May 2028, so the forecasts
imply June 2028 supplies $10,000 above June 2027. These are stipulated
monthly-bridge totals, not established legal denominators. The alternative
shares are 9.756...% and 10.256...%; dividing by partial-year income instead
gives 50%. Assume relevant contractor payments and that the other-item and
voluntary-choice conditions are met. The full-year forecast would fall below
the exemption boundary; the other window would exceed it and fail the strict
less-than test.
Keep the exemption decision at Needs Input under R-AU-TPAR-SOURCE until the
period conflict is reconciled. Do not choose a window to obtain a desired
reporting result. A supported supply-start date and forecasts cannot settle
the legal-period question. [S3] [S4] [S17] [S24]

```oa-check
name: Conflicting projected periods leave the exemption decision held
inputs:
  receipts: 20000
  partial_income: 40000
  next_full_year: 205000
  measurement_month_and_next_eleven: 195000
steps:
  full_year_share: receipts / next_full_year * 100
  other_window_share: receipts / measurement_month_and_next_eleven * 100
  incorrect_income_share: receipts / partial_income * 100
  june_increase: next_full_year - measurement_month_and_next_eleven
expected:
  full_year_share: 9.75609756
  other_window_share: 10.25641026
  incorrect_income_share: 50
  june_increase: 10000
```

#### Position 6 - Local government services and grants

A non-exempt local council pays an ABN contractor $11,000 including $1,000 GST
for a service with no applicable transaction exclusion. It also pays a
$20,000 grant to an ABN community entity. Report the qualifying service gross
and GST. Do not report the grant under the government grant item because the
payer is a local governing body. For an otherwise identical non-exempt state
government payer, assume the grant meets the grant rule with no exclusion:
service gross $11,000 plus grant $20,000 gives total gross $31,000, with GST
$1,000 on the service and $0 on this stipulated grant. Do not infer a recipient
GST or income tax outcome from the grant's reporting status. [S1] [S10]

```oa-check
name: Government service and grant amounts under stipulated payer routes
inputs:
  service: 11000
  service_gst: 1000
  grant: 20000
steps:
  local_gross: service
  state_gross: service + grant
  grant_difference: state_gross - local_gross
  reported_gst: service_gst
expected:
  local_gross: 11000
  state_gross: 31000
  grant_difference: 20000
  reported_gst: 1000
```

If that state payer's $20,000 grant total instead comprises Program A payments
of $6,000 on 10 October 2026 and $4,000 on 1 March 2027, plus Program B of
$10,000 on 2 May 2027 to the same ABN, keep Program A and B separate. An
aggregated Program A record is $10,000 with the permitted 30 June 2027 grant
date; Program B retains its $10,000 and payment date. Keep the service amount
separate in the mapping. The grant totals still add to $20,000; a single
merged $20,000 grant record would lose required program information. [S10]

```oa-check
name: Government grant program totals stay separate for the same recipient
inputs:
  program_a_first: 6000
  program_a_second: 4000
  program_b_payment: 10000
  service: 11000
  service_gst: 1000
steps:
  program_a: program_a_first + program_a_second
  program_b: program_b_payment
  grant_total: program_a + program_b
  all_gross: service + grant_total
  reported_gst: service_gst
expected:
  program_a: 10000
  program_b: 10000
  grant_total: 20000
  all_gross: 31000
  reported_gst: 1000
```

#### Position 7 - Cash cut-off and changed ABN

A qualifying payer has paid the same trading brand $4,400 including $400 GST
under one supported legal entity/ABN and $6,600 including $600 GST under its
successor entity/ABN. Keep 2 payee records, gross $11,000 and GST $1,000 in
total. A separate $3,300 June invoice paid in July is outside this year's
$11,000 and is linked to the next year's review. Confirm the legal entity
change rather than assuming the brand name identifies a single payee. [S6] [S7]

```oa-check
name: Changed entity ABNs and next year cash cut off
inputs:
  first: 4400
  first_gst: 400
  successor: 6600
  successor_gst: 600
  deferred: 3300
steps:
  current_gross: first + successor
  current_gst: first_gst + successor_gst
  all_source_gross: current_gross + deferred
  next_year: deferred
expected:
  current_gross: 11000
  current_gst: 1000
  all_source_gross: 14300
  next_year: 3300
```

#### Position 8 - Conditional FTL illustration

Assume a verified actual deadline, exactly 113 overdue days and a statutory
base-category entity with no multiplier or safe-harbour relief. Assume the
applicable unit is the value in the figures table. The ceiling calculation
gives 5 units and a potential base penalty of $1,820 before any remission.
A separate verified subsection (3) multiplier would give $3,640; subsection
(4) would give $9,100. Do not select a multiplier from these numbers or
assume an assessed debt exists. Establish income/turnover/withholder facts,
SGE conditions, safe harbour and the ATO notice independently. [S13] [S14] [S20]

```oa-check
name: Conditional late report base and separately established multipliers
inputs:
  overdue_days: 113
  period_days: 28
  cap: 5
  unit: 364
steps:
  units: min(ceil(overdue_days / period_days), cap)
  base: units * unit
  medium_if_established: base * 2
  large_if_established: base * 5
expected:
  units: 5
  base: 1820
  medium_if_established: 3640
  large_if_established: 9100
```

#### Position 9 - Aggregate before fixed-width file truncation

Two supported payments to the same ABN-quoting, GST-registered payee have
gross amounts $1,234.75 and $345.65, including GST of $112.25 and $31.42 shown
on the invoices, with no withholding. These are hypothetical invoice facts for
file conversion. The annual totals are gross $1,580.40, GST $143.67 and
withheld $0. Under v3.0.1, export 1580 and 143 in the zero-filled gross and GST
fields, and an all-zero withheld field, which the specification accepts.
Truncating each gross payment first would give 1579 and understate the record
by $1. Retain the source cents and both conversion differences. This example
does not validate an SBR or online-form conversion or a complete lodgment
file. [S26]

```oa-check
name: Annual record amounts truncate after aggregation for the fixed width file
inputs:
  gross_a: 1234.75
  gross_b: 345.65
  gst_a: 112.25
  gst_b: 31.42
  withheld_a: 0
  withheld_b: 0
steps:
  gross_total: gross_a + gross_b
  gst_total: gst_a + gst_b
  withheld_total: withheld_a + withheld_b
  gross_field: floor(gross_total)
  gst_field: floor(gst_total)
  withheld_field: floor(withheld_total)
  wrong_gross_field: floor(gross_a) + floor(gross_b)
  gross_cents_bridge: gross_total - gross_field
  gst_cents_bridge: gst_total - gst_field
  wrong_gross_difference: gross_field - wrong_gross_field
expected:
  gross_total: 1580.40
  gst_total: 143.67
  withheld_total: 0
  gross_field: 1580
  gst_field: 143
  withheld_field: 0
  wrong_gross_field: 1579
  gross_cents_bridge: 0.40
  gst_cents_bridge: 0.67
  wrong_gross_difference: 1
```

## Section 6 - Self-checks

### Review Checklist Items

Retain all universal checks and the named topical refusal trace. Before
presenting any supported working paper, confirm:

- [ ] Period, payer/ABN, authorised reviewer, law and current channel are established.
- [ ] Correct construction, service-category or government route is documented.
- [ ] GST turnover, grouping, relevant consideration, supply-start date and projection windows are supported; the projected-period conflict is resolved to authority or explicitly held; no rounded percentage changed a boundary result.
- [ ] Construction equality and all 3 limbs are tested, with no prior-activity look-back and no automatic next-year obligation without qualifying payments.
- [ ] Courier and road freight are combined; other exemption categories, overlapping items and voluntary reporting are handled explicitly.
- [ ] Every source item is retained exactly once as classified, excluded or held, with a reason and source link; unresolved rows prevent a final report.
- [ ] Cash cut-off, gross including GST and withholding, source cents, record aggregation and channel/version field mapping reconcile; fixed-width truncation follows aggregation, with unsupported values held.
- [ ] Each actual payee/ABN is separately supported; changes, addresses and original correction identities are checked.
- [ ] Materials-only/incidental-service, employee, labour hire, group, foreign and private exclusions use the applicable payer rule.
- [ ] Government services, grant-program separation/date treatment, exemptions, supplier statements and NANE indicators have their own evidence.
- [ ] No-ABN withholding exceptions and the annual-report choice are established; no annual duplication and no omission of payment-summary/activity-statement duties.
- [ ] Original, amount amendment, detail correction, additional payee and non-lodgment advice routes are distinguished and tied to receipts.
- [ ] Actual weekend/public-holiday-adjusted deadline and extensions are verified; drafts and prepared files are not called lodged.
- [ ] Base 4 outputs, formula recalculation, flags/defaults/refusals and reviewer checklist are complete; failed checks remain explicit.
- [ ] Hypothetical arithmetic checks are not presented as source, channel, professional or live-filing assurance.

### Sources and currency

The selected passages identified below were checked on 4 November 2026. A
retrieved page is not proof that every linked document, example or operative
provision was read. The legislation register identified current TAA
compilation C2026C00468 (in force from 1 October 2026) and regulations
F2026C00849 (27 August 2026); selected operative provisions were read,
not the whole Acts, commencement history or all future amendments. LCR 2019/4
Appendix 1 is explanatory material, not part of its binding public ruling.
The exemption instrument itself supplies the exemption conditions. Verify the
GST Act definitions and requested-period application for a live calculation.

| ID and primary source | Read date and scope |
| --- | --- |
| [S1] Taxation Administration Act 1953 | 4 November 2026: Current compilation identity; selected Schedule 1 sections 396-55 and 405-5 via the ATO legal database. Not a full Act/commencement review. |
| [S2] Taxation Administration Regulations 2017 | 4 November 2026: Current compilation identity and operative regulations 5, 38 and 70, including construction tests/exclusions. |
| [S3] TPRS Reporting Exemptions for Certain Entities Determination 2019 | 4 November 2026: Register current/in-force identity; sections 1 to 5 in the complete operative instrument text. |
| [S4] ATO: Work out if you need to lodge | 4 November 2026: Selected service/payment tests, combined categories and short-year explanation. |
| [S5] ATO: Building and construction services | 4 November 2026: Selected tests, definitions, separate entities, subcontracting, retail and equipment examples. |
| [S6] ATO: Payments businesses need to report | 4 November 2026: Selected cash, mixed-payment, exclusion and no-ABN annual-route passages. |
| [S7] ATO: Contractor details | 4 November 2026: Selected identity, changed ABN, whole-dollar gross/GST/withheld, optional details and government fields. |
| [S8] ATO: Lodge your TPAR | 4 November 2026: Selected due date, channels, paper cessation, records and receipt instructions. |
| [S9] ATO: Withholding if ABN is not provided | 4 November 2026: Selected threshold, payment-summary, deferred-payment, GST credit and non-cash passages. |
| [S10] ATO: Government payments | 4 November 2026: Selected service/grant scope, entity/transaction exemptions, overseas services, grant-program aggregation/date treatment, supplier statements and annual-route passages. |
| [S11] ATO: Non-lodgment advice | 4 November 2026: Selected scope, years, future cessation, confirmation and channel instructions. |
| [S12] ATO: Amend a lodged TPAR | 4 November 2026: Selected amount amendments, payee-detail correction, omitted-payee and online steps. |
| [S13] ATO: Failure to lodge on time penalty | 4 November 2026: Selected base, multipliers, third-party report, warning, remission and safe-harbour passages. |
| [S14] ATO: Penalty units | 4 November 2026: Selected unit amounts and commencement periods. |
| [S15] ATO: Due dates for lodging and paying | 4 November 2026: Selected first-business-day adjustment for weekends/public holidays. |
| [S16] ATO: TPAR overview | 4 November 2026: Selected overview of payers, contractor entity types and annual deadline. |
| [S17] LCR 2019/4 | 4 November 2026: Selected explanatory Appendix 1 paragraphs 58 to 66 and cited footnotes. This appendix is not part of the binding public ruling. |
| [S18] TR 2002/9 | 4 November 2026: Selected no-ABN exceptions/aggregation discussion. Historical rate examples do not establish the current rate. |
| [S19] ATO: Statement by a supplier | 4 November 2026: Selected exceptions, invalid statements, current general rate, activity statement and payment-summary duties. |
| [S20] TAA Schedule 1 section 286-80 | 4 November 2026: Selected multiplier limbs and SGE conditions. Additional applicable provisions still require engagement review. |
| [S21] TAA Schedule 1 section 12-190 | 4 November 2026: Selected subsection (4) supply aggregation and exceptions; read with current supplier guidance. |
| [S22] ATO Software Developers: TPRS | 4 November 2026: Reporting-authority distinction, regulation 70 and specification discovery; selected linked technical specification passages are recorded at [S26]. |
| [S23] GST Act section 188-15 | 4 November 2026: Selected current-turnover period, exclusions and GST group provisions in subsections (1) and (2). |
| [S24] GST Act section 188-20 | 4 November 2026: Selected projected-turnover period, exclusions and GST group provisions in subsections (1) and (2); no TPAR-specific period reconciliation was established. |
| [S25] GST Act section 188-25 | 4 November 2026: Projected-turnover exclusions for capital assets, cessation and substantial permanent reduction. |
| [S26] ATO TPAR electronic reporting specification v3.0.1 | 4 November 2026: Specification page marked Current, published/modified 8 June 2021. Selected general amount rules, record table 16, sections 6.61 to 6.66, 6.69 and section 9 amendments. The older non-amount-change statement does not displace the current [S12] details-correction procedure. No complete exporter, SBR/UI mapping or future-period availability was validated. |
| [S27] A New Tax System (Goods and Services Tax) Regulations 2019 | 4 November 2026: Compilation F2025C01015, section 29-80.01 ($75 for GST Act subsection 29-80(1)), read with TAA Schedule 1 section 12-190(4)(b). |
| [S28] ITAA 1997 section 995-1 | 4 November 2026: Paragraph (a) of the 'withholding payment' definition, used by regulation 70(3). |

[S1]: https://www.legislation.gov.au/C1953A00001/latest/text "Taxation Administration Act 1953"
[S2]: https://www.legislation.gov.au/F2017L01227/latest/text "Taxation Administration Regulations 2017"
[S3]: https://www.legislation.gov.au/F2019L00864/latest/text "TPRS Reporting Exemptions for Certain Entities Determination 2019"
[S4]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar "ATO: Work out if you need to lodge"
[S5]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/building-and-construction-services "ATO: Building and construction services"
[S6]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/payments-businesses-need-to-report-in-their-tpar "ATO: Payments businesses need to report"
[S7]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/tpar-contractor-details-to-report "ATO: Contractor details"
[S8]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar "ATO: Lodge your TPAR"
[S9]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-suppliers/withholding-if-abn-not-provided "ATO: Withholding if ABN is not provided"
[S10]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/work-out-if-you-need-to-lodge-a-tpar/payments-government-entities-need-to-report-in-their-tpar "ATO: Government payments"
[S11]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/tpar-non-lodgment-advice "ATO: Non-lodgment advice"
[S12]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report/lodge-your-tpar/amend-a-lodged-tpar "ATO: Amend a lodged TPAR"
[S13]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty "ATO: Failure to lodge on time penalty"
[S14]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units "ATO: Penalty units"
[S15]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying "ATO: Due dates for lodging and paying"
[S16]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report "ATO: TPAR overview"
[S17]: https://www.ato.gov.au/law/view/document?docid=COG/LCR20194/NAT/ATO/00001 "LCR 2019/4"
[S18]: https://www.ato.gov.au/law/view/document?docid=TXR/TR20029/NAT/ATO/00001 "TR 2002/9"
[S19]: https://www.ato.gov.au/forms-and-instructions/statement-by-supplier-not-quoting-an-abn "ATO: Statement by a supplier"
[S20]: https://www.ato.gov.au/law/view/document?docid=PAC/19530001/Sch1-286-80 "TAA Schedule 1 section 286-80"
[S21]: https://www.ato.gov.au/law/view/document?docid=PAC/19530001/Sch1-12-190 "TAA Schedule 1 section 12-190"
[S22]: https://softwaredevelopers.ato.gov.au/TPRS "ATO Software Developers: TPRS"
[S23]: https://www.ato.gov.au/law/view/document?DocID=PAC/19990055/188-15 "GST Act section 188-15"
[S24]: https://www.ato.gov.au/law/view/document?DocID=PAC/19990055/188-20 "GST Act section 188-20"
[S25]: https://www.ato.gov.au/law/view/document?DocID=PAC/19990055/188-25 "GST Act section 188-25"
[S26]: https://softwaredevelopers.ato.gov.au/sites/default/files/2021-06/Taxable_payments_annual_report_specification_v3.0.1.docx "ATO TPAR electronic reporting specification v3.0.1"
[S27]: https://www.legislation.gov.au/F2019L00417/latest/text "A New Tax System (Goods and Services Tax) Regulations 2019"
[S28]: https://www.ato.gov.au/law/view/document?docid=PAC/19970038/995-1 "ITAA 1997 section 995-1"

Retained provenance: the preceding guide recorded source checks on
27 September 2026, with whole-dollar and weekend rules checked on
31 October 2026. Those dates retain their historical scope. This revision
adds the selected current reads above; it does not turn the historical
statements into full page or full law certification. The 2012 amending
regulation cited in the earlier guide is historical origin; current
construction reporting is referenced to regulation 70 of the 2017 Regulations.

Still requiring engagement verification: complete current-law/commencement
review for the report period; GST turnover facts and the projected-period
conflict; current channel/version availability and mappings beyond the selected
v3.0.1 fields; complete file validation and amendment matching; actual holiday
and extension; every source record and exclusion; independent professional review.
The examples and local repository checks do not supply those facts or sign-off.

### Revision history

- v1.3, 4 November 2026: Reorganise to the template and universal companion
  contract. Correct construction look-back/equality, GST turnover and exemption
  conditions, government grants, correction routes and FTL qualification.
  Preserve Sparkle A to F and the alternative with explicit annual-route facts.
  Add 10 executable arithmetic cases, intake, refusals, defaults, thresholds,
  reviewer outputs and selected source/read provenance. Hold the projected-period
  source conflict and document selected fixed-width aggregation/truncation rules.
  Use the canonical fork CTA. Second read: complete held optional v3.0.1 payee
  fields, quote the non-lodgment advice trigger, add regulation 70(3), 70(5)
  and GST Regulations pinpoints, and make the Position 5 and 9 inputs plausible.
- v1.2, 2 November 2026: Retained structural update and source qualifications;
  prior recorded check dates are preserved above.

## Section 7 - Disclaimer

General reference only. This guide is a source-cited draft and computation aid,
not tax, legal or financial advice or a lodged report. A qualified Australian
practitioner must establish the facts and operative law, review the service
tests, contractor extract, reporting route and outputs, and approve them before
use. ATO data matching can expose an omitted or misclassified contractor.
An editing date, passed arithmetic check or general approval is not a recorded
professional sign-off on an engagement. Contributed by Ryan Duguid.

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
