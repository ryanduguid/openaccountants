---
name: cc-super-guarantee
description: >
  Selected Cocos (Keeling) Islands employer superannuation guarantee rules for
  2026-27. Covers territorial application, employee and labour-contractor
  status, qualifying earnings and exclusions, annual employer ceiling,
  salary sacrifice, fund choice, contribution receipt, conditional deadlines
  and the Payday Super changeover. Use for island employer super, low
  earnings, annual-base crossings, new funds, out-of-cycle payments or
  late-contribution questions. Includes primary legislation, ATO guidance,
  fictional component calculations, remittance patterns and reviewer
  controls. This source-cited draft preserves both workflow bases and
  identifies missing programmes and operational requirements; it does not
  complete a payroll run, social-contribution engagement or country pack.
jurisdiction: CC
category: international
tax_year: 2026
tax_year_notes: "Primarily QE days from 1 July 2026 to 30 June 2027; saved old quarterly liabilities remain separate"
tier: 2
last_updated: 2026-10-21
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - social-contributions-workflow-base
  - cc-tax-system
verified_by: pending
---

# Cocos (Keeling) Islands: employer super guarantee for 2026-27

Load `workflow-base`, `social-contributions-workflow-base` and
`cc-tax-system`. Preserve profile confirmation, source and period gates,
refusals, the 4 universal outputs, all 5 social-domain outputs and their
checks. This selected employer superannuation guarantee (SG) companion
supports component working papers for a credentialed reviewer. Missing
mandatory sources, country slots, facts or runtime capabilities prevent a
complete financial deliverable. A payroll run also needs its payroll base
and country payroll rules. No comprehensive-country acceptance or
professional sign-off is claimed.

## Territorial application and period

Section 8E of the Cocos (Keeling) Islands Act 1955 extends Commonwealth
Acts of their own force unless an Act expressly provides otherwise. Its
territory framework is compilation 13 of 18 December 2020. [TERRITORY]

The SG Act extends to external territories included in its definition of
Australia. Section 6 adopts the income-tax meaning of geographical
Australia; section 960-505(1)(e) of the 1997 Act expressly includes
Cocos (Keeling) Islands. Work on the island is therefore not work outside
Australia merely because it is offshore from the mainland. Residence,
worker status and the particular payment still require their own tests.
[SG, sections 4, 6 and 8][SG]; [DICT, section 960-505][DICT]

The dictionary capture is compilation 267, effective 27 August to
30 September 2026, rather than a complete current consolidation. Selected
October amendment targets in Acts 71 and 86 of 2026 were checked and do
not replace the geographical definition used here. Reconcile operative
law for the engagement period and other tax regimes separately. An editing
date does not certify a complete current statute. [DICT]; [AMEND71]; [AMEND86]

For QE days from **1 July 2026**, Payday Super uses qualifying earnings
(QE) paid to or for an employee. The payment day controls even if the
work or arrangement predates commencement. Old quarters ending before
1 July 2026 retain their saved rules; see the transition section.
This guide's primary year is **1 July 2026 to 30 June 2027**, in AUD.
Do not roll its annual base into a later financial year. [PAYDAY, section 2
and Schedule 1 item 182][PAYDAY]; [RATES]

## Programmes and selected figures

Keep SG separate from income tax, Medicare, PAYG withholding, workers'
compensation, paid parental leave and any local or employment obligation.
Their coverage is not established by this SG calculation. The island's
GST geography also does not determine its SG geography. Route income-tax
and Medicare questions to `cc-income-tax` and territory boundaries to
`cc-tax-system`; those guides retain their own incomplete slots.

| Programme or parameter | Selected 2026-27 treatment | Primary source |
|---|---|---|
| Ordinary employer SG | 12% of eligible QE after the annual-base rule; employer obligation, without an employee SG matching-share calculation in this guide | SG section 17A; RATES |
| Annual maximum contributions base | AUD 270,830 per employee, per employer, per financial year | SG section 10A(5)-(6); RATES |
| General earnings floor | No minimum earnings amount for an otherwise eligible adult worker; age and other exclusions still apply | ELIGIBILITY; SG; REG |
| Normal contribution period | Each QE day; fund receipt normally by the 7th business day after that day | SG sections 6 and 18C; DEADLINES |
| First eligible contribution extension | Conditional period ending on the 20th business day after the QE day | SG sections 6 and 18C(2) item 1 |
| Basic administrative uplift | 60% of the combined final shortfalls and notional earnings, subject to statutory reductions | SG section 19B; REG regulations 13A-13D |
| Choice loading | 25% of relevant non-compliant contributions, limited under section 20C | SG sections 20A and 20C |

Sources for this table: [SG]; [REG]; [RATES]; [ELIGIBILITY]; [DEADLINES].
The 12% rate is not Norfolk Island's conditional 2026-27 transition.
Item 189 of the Payday Super Act defines a Norfolk earnings subset;
it does not create an 11% concession for Christmas Island or Cocos
employment. If an engagement actually includes Norfolk earnings, resolve
that subset and its interaction with the cap separately. [PAYDAY, item 189][PAYDAY]

## Establish the contributor and earnings

Use a stable contributor reference. Establish the employer, actual
employment relationship, age at the relevant time, weekly hours where
required, residence, work locations, payment dates, earnings components,
annual earnings history and any applicable certificate. Confirm readiness
of reviewer-held registrations and fund details. Do not request TFNs,
bank details or identity documents through this workflow.

### Employee, contractor and self-employed status

Section 12 starts with ordinary employment and extends to specified
directors, labour contracts, performers, related services and office
holders. A contract wholly or principally for a person's labour can make
that person an SG employee. An invoice, ABN, contractor label or PAYG
classification alone does not settle SG status. Preserve the contract,
actual duties and labour/non-labour split for review. [SG, section 12][SG]

An otherwise eligible employee aged **18 or over** is covered regardless
of hours or amount earned. For someone under 18, the part-time exclusion
uses **not more than 30 hours per week**. The ATO requires actual weekly
hours, rather than averaging across a fortnight or month. Exactly 30
hours is not more than 30. Domestic or private work also has a separate
not-more-than-30-hours exclusion, regardless of age. Do not apply the
business-employee rule to a private household without that check.
[SG, sections 6 and 12(11)][SG]; [REG, regulations 11(f) and 12(1)(j)][REG];
[ELIGIBILITY]

A sole trader or partner does not owe employer SG merely on their own
business profit or drawings. That does not exempt employees they engage,
or a worker whose actual relationship meets section 12. A company paying
its working director needs the director/employee test; it is not the
same as sole-trader drawings. Personal or voluntary contribution rules
and their deduction/cap conditions are separate and remain uncomputed.
[SG, section 12][SG]; [ELIGIBILITY]

Temporary residence alone is not an exemption. Regulation 11 contains
narrow visa, appointment, seniority and other conditions for certain
foreign workers. Regulation 12 also addresses covered international
social security agreements and particular work outside Australia. Verify
the exact instrument, certificate, employer/employee residence and work
period before excluding anything. A bilateral agreement's existence or an
island address is insufficient. Where a cross-border decision is needed,
load its domain base and applicable country/agreement sources first.
[SG, sections 8, 12 and 15C][SG]; [REG, regulations 11-12][REG]; [ELIGIBILITY]

### Reconcile qualifying earnings

For each payment, reconcile gross-pay components to the actual section
10A categories and regulation 12 exclusions. Include overlapping categories
once. Ordinary time earnings (OTE) are not a universal synonym for gross
pay, taxable income or QE. [SG, sections 6 and 10A][SG]

| Component | Classification control |
|---|---|
| Ordinary hours, over-award payments, shift loading or commission | Test the section 6 OTE definition and section 10A categories. |
| Commissions, specified director remuneration and qualifying labour-contract payments | Section 10A expressly includes the specified categories; do not omit them solely because an old OTE report did. |
| Salary sacrifice reduction of qualifying earnings | Include the qualifying reduction under section 10A(1)(h), subject to its exclusions; do not count the same earnings twice. |
| Payment reversing a sacrificed contribution | Excluded under section 10A(3)(a). |
| Separately identified genuine overtime | Do not assume every payment is QE; reconcile ordinary hours and every other possible section 10A category before exclusion. |
| Unused sick, annual or long service leave lump sum on termination | Section 6 excludes the listed termination payments from OTE. Check whether another QE category applies before concluding. |
| Parental leave period payment | Regulation 12(1)(a) exclusion; a separate government contribution programme is not computed here. |
| Fringe benefit | Regulation 12(1)(f) exclusion using the FBT Act meaning; do not classify every cash allowance as a fringe benefit. |
| Community service or Australian Defence Force absence payment from the usual employer | Regulations 12(1)(b)-(c), (2)-(3) contain conditions and exceptions; annual, sick or long service leave relating to the period is not automatically excluded. |
| Particular overseas work, reserve remuneration or prescribed grant-funded payment | Verify the specific regulation 12 provision and evidence; do not extend its exclusion to all foreign, public sector or care-sector pay. |

[SG, sections 6 and 10A][SG]; [REG, regulations 11-12][REG]. An exclusion
from QE does not establish income-tax exemption, zero PAYG withholding,
absence of another programme or permission to ignore an employment award.
For an invoice, isolate the proved labour component. Do not apply 12%
mechanically to goods, expenses and labour combined. [ELIGIBILITY]

## Annual base and individual SG amount

Section 10A(5) derives the maximum from the basic concessional contributions
cap and charge percentage, then rounds it down to a multiple of **AUD 10**.
The ATO's applicable **2026-27 annual base is AUD 270,830**. This is an
employer SG base, not a person's combined concessional-contribution cap
across every employer and voluntary contribution. [SG]; [RATES]

Under section 10A(6), use the earnings history for **that employee and
that employer in the same financial year**. For the payment that would
cross the base, only the remaining amount up to the annual maximum counts
for the specified SG purposes. Subsequent payments are treated as nil
for those purposes, not as non-existent for income tax or every payroll
obligation. Keep pre-limit earnings and the applied limit visible.
Do not reuse the old quarterly maximum or invent a monthly cap or
starter/leaver proration. [SG, section 10A(6)][SG]

For an ordinary covered accumulation-fund case with all facts established:

1. Confirm the contributor profile, applicable law and QE payment day.
2. Classify each payment component, exclusions and salary sacrifice.
3. Total QE paid to or for that employee by that employer on the same day,
   without double counting overlapping categories.
4. Apply the annual-base crossing rule using the verified earnings ledger.
5. Multiply the resulting QE by **12%** for the individual SG amount.
6. Allocate eligible employer contributions under section 18C in receipt
   order, without reusing amounts applied to another QE day.
7. Reconcile any base shortfall, late allocation and remaining final
   shortfall separately from notional earnings, uplift and choice loading.
8. Verify fund choice, allocation information, actual receipt, calendar
   and any permitted longer period before assessing payment compliance.

[SG, sections 10A and 17A-18D][SG]. Missing year-to-date history means
Needs Input. Neither assume the employee is below the cap nor stop SG
on an unverified claim that the annual base has been reached.

An actual employer shortfall exemption certificate in force for the
employer, employee and QE day can invoke section 17B. A certificate for
another employer does not exempt this employer. High income or multiple
jobs alone does not supply a certificate. This guide does not prepare
an exemption application or infer its approval. [SG, section 17B][SG];
[ELIGIBILITY]

## Fund choice, receipt and allocation

An eligible employer contribution ordinarily needs a complying fund or
RSA and sufficient information to allocate it to the employee. Sacrificed
contributions are excluded from the eligible employer-contribution
definition even though sacrificed earnings can enter QE. A trustee's
compliance statement addresses only its statutory presumption and has
exceptions; it does not prove timely receipt or correct allocation.
Defined-benefit, deceased-employee representative and conversion-notice
branches need their own section 18A-18B conditions. [SG]

For ordinary choice-covered accumulation contributions, establish:

- the employee's valid chosen fund; or
- if there is no chosen fund, the latest relevant Commissioner notification
  identifying a stapled fund; or
- if that notification says there is no stapled fund, the eligible employer
  default-fund route, including the applicable standard-choice-form,
  MySuper and insurance requirements.

Section 32C contains further public sector, successor-fund and instrument
branches. Verify the applicable branch rather than treating the above as
an exhaustive rule for every employee. Failure to provide a required
standard choice form on time can defeat the stapled/default compliance
route until the form is provided. [SG, sections 32C-32D and 32N-32NA][SG];
[REG, regulations 14-17][REG]

Section 32N generally requires a standard choice form within **28 days
of first commencing employment**, and identifies further request, ceased
choice and employer-fund-change events. Section 32NA contains exceptions,
including a valid timely choice and specified temporary-visa or scheme
cases. Do not assume every employee needs a new form every year or that
no form is ever needed because a fund account exists. Record the trigger,
applicable exception if any, form date and evidence. [SG]

A bank debit or clearing-house receipt is not proof that the employee's
fund received an allocatable contribution. Reconcile the remittance,
clearing-house report, fund acceptance, employee allocation and refunds
separately. A rejected, returned or unallocated amount cannot be marked
compliant merely because cash left the employer's account. [SG, sections
18A and 18C][SG]; [DEADLINES]

Section 18C can apply unused eligible contributions received in the
**12-month period ending the day before the QE day**, subject to all its
conditions. Apply contributions in receipt order and prevent double use
across QE days or late-period allocations. A contribution exceeding one
payday's amount is not a refund or automatically available credit for
every later payday. [SG, section 18C(1)][SG]

## Deadline calendar and longer periods

The usual period ends on the **7th business day after the QE day**.
The statutory business-day definition excludes Saturday, Sunday and a
public holiday for the whole of **any State, the ACT or the Northern
Territory**. A holiday elsewhere can therefore affect this employer's
calendar. Do not use only the island calendar or treat every local holiday
as a statutory excluded day. Establish authoritative holiday dates before
publishing an actual deadline. [SG, section 6][SG]; [DEADLINES]

| Longer-period branch | Conditions and endpoint |
|---|---|
| First eligible contribution | First to the particular complying fund/RSA after employment commenced/recommenced, or after ceasing eligible contributions to another fund/RSA: extended usual period, ending on business day 20 after the QE day. |
| Determined out-of-cycle QE | Section 18C(2) item 2 plus the determination conditions below: end of the usual period for the first subsequent standard QE day. |
| Exceptional circumstances | Employer and QE day must be covered by a Commissioner determination. Endpoint is the later of the extended usual period and the period of 20 business days starting on the day after the determination. |
| Overlapping due dates | Item 4 requires the relevant earlier contribution to have been applied for an earlier QE day. If the current usual period ends before that contribution's latest permitted receipt day, use that latest day under the statutory conditions. |

[SG, section 18C(2)][SG]; [REG, regulation 13][REG]; [DEADLINES]. These
are receipt periods, not permission to leave fund information unresolved.
Use the latest applicable endpoint where multiple items apply. Keep a
reason and evidence for each extension; do not grant all subsequent
paydays the first contribution's 20-business-day period automatically.

The **2026 out-of-cycle determination** covers specified allowances,
bonuses, commissions, loadings, payments in advance and back payments.
All these conditions must be established:

1. The employer has an established timing, pattern or schedule of QE
   payments for that employee.
2. The specified payment falls outside that established schedule.
3. A subsequent payment that is not out of cycle is actually made on the
   next day consistent with that established schedule.

Several out-of-cycle payments may occur between the first and subsequent
standard payment. An advance must satisfy the determination's definition
and is not a loan. An intermittent invoice, a payment merely labelled
'bonus' or a hoped-for next payday does not establish all conditions.
If the required next standard payment does not occur, do not retain the
extension on the basis of the label alone. [OUTOFCYCLE, sections 4-5][OUTOFCYCLE];
[SG, section 18C(2) item 2][SG]; [DEADLINES]

Natural disasters and widespread contribution-technology outages are
prescribed exceptional circumstances. An employer's individual cash-flow
problem, local delay or disaster label is not itself the required class
and period determination. Verify and retain the actual determination;
this guide does not assert that one covers a particular employer or day.
[REG, regulation 13][REG]; [SG, section 18C(4)][SG]; [DEADLINES]

## Late payments, SGC and disclosures

The individual SG amount, base shortfall, final shortfall and total
superannuation guarantee charge (SGC) are distinct. On-time eligible
allocations reduce the base shortfall. Late eligible allocations within
the statutory late period can reduce the final shortfall, but do not
automatically erase notional earnings, uplift or choice loading. Keep
assessment and receipt dates, historical allocations and changing
shortfall balances. [SG, sections 16B and 18C-19B][SG]; [CHARGE]

The selected SGC structure for a QE day comprises the totals of final
shortfalls, individual notional earnings, administrative uplift and choice
loading. Section 19A uses the GIC rate and its defined notional sum,
including the base shortfall and prior daily amounts. Do not calculate
interest solely on the latest unpaid principal or copy a fixed historical
interest rate. A complete charge needs the actual daily rates and dates,
assessment facts and applicable statutory adjustments. [SG]; [CHARGE]

Section 19B starts the uplift at **60%** of combined final shortfalls and
notional earnings. Regulations 13C-13D permit reductions:

- **20 percentage points** if the regulation's prior-24-month assessment
  and estimate conditions are met, with its transition beginning
  1 July 2026 for QE days through 30 June 2028; and
- **40, 35, 30 or 15 percentage points** for a valid voluntary disclosure
  lodged before assessment, respectively before the end of the 30-day
  period starting on the QE day, in the following period ending on day 60,
  in the following period ending on day 120, or later.

The assessment/estimate exclusions and validity requirements matter. Do
not assume the lowest rate because an employer says this is their first
late payment. Section 33 permits an approved-form voluntary disclosure
before the day of assessment; it is not the old compulsory quarterly SGC
statement. [SG, sections 19B and 33][SG]; [REG, regulations 13B-13D][REG];
[CHARGE]

Choice loading generally uses **25%** of relevant contributions failing
choice requirements, subject to statutory exceptions and the remaining
**AUD 1,200** limit per employer/employee notice period. That period can
cover multiple QE days; it is not a new annual or per-payday allowance.
Section 20D's failed-stapled-fund protection has specific notification,
no-chosen-fund, rejection and replacement-payment conditions. [SG, sections
20-20D][SG]; [CHARGE]

Before assessment, the ATO directs employers to pay missing contributions
to the fund promptly. After assessment, pay the charge to the ATO; section
36(4) makes it payable on the assessment day. Do not send an assessed
charge to the fund and call the ATO debt discharged. Later non-payment
can create further interest, notice and penalty consequences, which need
their own current sources and facts; no complete penalty computation is
supplied here. The first-year compliance approach does not repeal the
underlying SG obligation. [SG, sections 33 and 36][SG]; [CHARGE]

## Changeover and income-tax interaction

Keep pre-July quarters and new QE-day ledgers separate. Schedule 1 item
182 saves old quarterly liabilities and related rules, with the stated
late-payment-offset limitation. Items 185-186 govern eligible unused
pre-commencement amounts and contributions from **1-28 July 2026** where
the employee still has a June-quarter shortfall: apply the latter first
under the saved old rules, then only the unabsorbed remainder under the
new rules. Do not use the same contribution twice. A July payment for
June work is new-period QE without cancelling an old-quarter debt.
[PAYDAY, items 182-186][PAYDAY]

The annual SG base is not a personal deduction or contribution-cap safe
harbour. Employer contribution deductions, personal voluntary contributions,
salary sacrifice, excess contributions and high-income additional tax
need their own income-tax rules and confirmed facts. The Payday Act
repeals former sections 26-95 and 290-95 of the 1997 Act and contains
saved-old-law application provisions. Do not carry the old blanket SGC
non-deductibility rule into every post-July QE-day charge or infer that
every charge, penalty and interest amount is deductible. No deduction is
calculated by this companion. [PAYDAY, items 80, 92 and 183][PAYDAY]

## Worked component examples and classification patterns

All examples are fictional AUD for **2026-27**. Worker, earnings and
ordinary accumulation-fund facts are stipulated. There is no Norfolk
subset, defined benefit, cross-border certificate or rounding difference
unless stated. Examples demonstrate selected amounts or classifications,
not completed engagements. Any unresolved required input remains a hold.

| Fictional facts | Recomputed result or classification |
|---|---|
| Adult employee, eligible QE 2,000, prior annual QE 10,000 | Individual SG amount 240. Separate employer funding and receipt still need proof. |
| Eligible adult employee, QE only 100 | Individual SG amount 12; no assumed AUD 450 monthly floor. |
| Under-18 employee, exactly 30 actual hours in a week | Part-time exclusion; no SG on the excluded earnings. Do not average hours with another week. |
| Under-18 employee, 31 actual hours that week, eligible QE 620 | Individual SG amount 74.40, subject to the remaining coverage facts. |
| Private household worker, 30 hours, all work wholly domestic | Section 12(11) exclusion; do not apply the adult business-employee result. |
| Labour contract satisfies section 12(3); eligible labour 600 and separately proved goods 400 | Individual SG amount 72 on labour QE 600; not 120 on the total invoice merely because it is paid together. |
| Cash qualifying pay 1,800 plus qualifying earnings sacrificed 200 | QE 2,000; individual SG amount 240. Sacrificed contribution 200 does not reduce that employer SG amount to 40. |
| Same-day eligible QE payments 1,200 and 800 | QE day total 2,000; individual SG amount 240, without duplicating a commission already included. |
| Prior annual QE 270,000; current otherwise eligible payment 2,000 | Remaining annual base 830; individual SG amount 99.60; keep the payment's unmodified earnings visible. |
| Annual base already reached for that employer; later otherwise eligible QE 1,000 | Nil additional SG amount under the annual-base rule; other obligations remain separate. |
| Fresh annual ledger, eligible QE exactly 270,830 | Individual SG amount 32,499.60; do not round the statutory base up to create SG of 32,500. |
| Employer A has reached its base; employer B pays eligible QE 1,000 with a fresh verified ledger | Employer B's individual SG amount 120, absent its own valid certificate or exclusion. |
| Valid exemption certificate covers only employer A | It does not exempt employer B's payments. Verify each certificate's employer, employee, period and QE day. |
| Sole trader profit 50,000, no employees or qualifying labour/director relationship | No employer SG on the owner's stipulated profit; voluntary contribution and deduction questions remain separate. |
| Individual SG amount 240; on-time eligible contribution 200 | Base shortfall 40. If a later eligible 40 is applied before assessment, final shortfall can become nil; this does not establish nil total SGC. |
| Correct 240 sent to clearing house on the last permitted day; fund receipt unknown | Timing and compliance unresolved; no presumed timely receipt. |
| Unused eligible receipt 300; applied to first QE day's SG amount 240 | Remainder 60 can be considered under the statutory period/allocation conditions; it cannot be reused as 300 for a later day. |
| Off-cycle bonus 500 between established scheduled paydays; all determination conditions met | Individual SG amount 60; receipt deadline follows the first subsequent standard QE day's usual period. |
| Same bonus label, but next scheduled standard payment not made | The determination condition fails; do not assume the out-of-cycle extension. |
| New employee's first eligible contribution qualifies for item 1 | Use the 20-business-day endpoint; later paydays require their own item 4 or other extension evidence. |
| Mere irregular contractor invoice, no established pay schedule | Do not classify automatically as determined out-of-cycle QE. |
| Natural disaster affects employer, but no covering determination established | Hold the extension; the disaster label alone is insufficient. |
| Same-day no-interest/other-uplift example: relevant choice-failing contribution 240, full notice-period limit available | Choice loading 60 before any applicable statutory exception; no claim that this is total SGC. |
| Combined final shortfalls and notional earnings 100; no regulation 13 reductions | Basic uplift 60. With proved 20-point history reduction and 40-point valid timely disclosure reduction, uplift becomes nil. |
| Annual earnings history, fund-choice facts or holiday calendar missing | Needs Input for the affected amount or deadline; no default resolves it. |

[SG]; [REG]; [OUTOFCYCLE]; [RATES]; [ELIGIBILITY]; [DEADLINES]; [CHARGE].
For remittance matching, distinguish an allocatable fund receipt, clearing
house settlement, refund, employee salary sacrifice, ATO assessed charge
and unrelated PAYG/Medicare or insurance payment. Match using stable
references, amount, date, fund and contributor evidence. An amount or bank
narrative alone does not establish programme, employee or QE-day allocation.

## Reviewer outputs, checks and remaining slots

Preserve all universal and social-domain outputs. For a supported component
working paper, identify the following rather than implying that a correct
percentage supplies the whole engagement:

| Required output | Minimum SG-specific evidence |
|---|---|
| Contribution computation schedule | Stable contributor/employer reference, classification, period, QE components/exclusions, unmodified annual ledger, capped QE and individual SG amount. |
| Remittance reconciliation | Expected amount, actual eligible receipt, allocation order, clearing-house status, refunds, unused credits, base/final shortfalls and unmatched items. |
| Filing and payment calendar | Actual QE day, normal endpoint, each evidenced extension, holiday sources, receipt status and any assessment/disclosure event. |
| Reviewer brief | Source versions, unresolved eligibility, other programmes, missing facts, assumptions, charge/choice/deduction holds and decisions required. |
| Contribution register | Contributor status, employer, programme, confirmed periods, certificate and reviewer-held readiness references; no sensitive identifiers. |

Check every amount against source and year; age/hours; employee/contractor
status; geography/residence; QE and exclusions; annual limit per employer;
same-day totals; sacrifice included once but excluded as eligible employer
funding; certificates; fund choice; receipt/allocatability; contribution
order and no double use; deadlines/extensions; separate shortfall/charge;
changeover; currency/rounding; all outputs and outstanding slots.

Section 79 requires records explaining transactions and acts, including
shortfall documents. Keep them in English or readily convertible into
English so liability can be readily ascertained. Retain them for **5 years after
preparation/obtaining or completion of the related transactions/acts,
whichever is later**, subject to its statutory exceptions. This is not
permission to collect sensitive identifiers in the working conversation
or to delete records automatically at that point. [SG, section 79][SG]

| Mandatory social-country slot | Verified scope and outstanding work |
|---|---|
| 1. Programmes and shares | Employer SG rate and selected charge components supplied. Complete inventory and treatment of health, unemployment, accident and other programmes remains open. |
| 2. Bases | Selected QE/OTE, employee and exclusion rules supplied. Personal/voluntary and other programme bases remain open. |
| 3. Floors and ceilings | Selected earnings-floor, annual SG base and employer separation supplied. Cross-border, certificate application and special-scheme interactions need case-specific sources. |
| 4. Contributor categories | Ordinary employees, selected contractors/directors, age/domestic exclusions and self-employed distinction supplied. Full foreign-worker and special-scheme determinations remain conditional. |
| 5. Registration | Reviewer-held employer/fund readiness and choice evidence required. Complete registration identifiers, portals and authority procedures remain unverified. |
| 6. Declarations and payment | Selected receipt deadlines, extensions, voluntary disclosure and assessment distinction supplied. Current forms, actual holiday mapping, STP and all operational filing requirements remain open. |
| 7. Penalties and interest | Selected SGC structure, uplift and choice controls supplied. Actual daily rates, complete penalty/notice machinery and remedies remain open. |
| 8. Income-tax interaction | No automatic deduction inferred; transition and separate income-tax source gate supplied. Actual deduction/cap calculations remain open. |
| 9. Payment patterns | Selected fund/clearing-house/refund/charge patterns supplied; ambiguous remittances require evidence. |
| 10. Refusals and defaults | Missing law, QE, annual history, certificate, fund, receipt or deadline inputs require Needs Input/hold. No country default is authorised. |
| 11. Currency and rounding | Examples use AUD and exact cents; statutory annual base rounds down to AUD 10. Operational fractional-cent contribution/charge rules and any foreign-currency conversion remain unverified. |
| 12. Worked cases | Employee, low earnings, annual ceiling, self-employed and remittance boundary components supplied. No model-executed full contribution engagement, multi-programme or filing test is claimed. |

The selected rules do not satisfy every mandatory slot. Obtain the missing
primary law, facts, forms and capabilities before a complete financial
result. Preserve exact tool-unavailable refusal messages from the bases
where they apply. Do not fill gaps with a mainland assumption, an invented
island exemption, a zero rate or a claim of comprehensive coverage.

## Sources and verification limits

Checked **21 October 2026**: the live Register identified SG Act compilation
**78**, effective **1 July 2026**, and SG Regulations compilation **8**,
effective **1 July 2026**, as latest. Selected provisions were read for
territory/definitions, employee/QE status, annual base, contributions,
shortfalls, choice, disclosure, assessments and records. The out-of-cycle
determination was read in full. ATO eligibility was updated **15 July
2026**, rate/base guidance **17 April 2026**, deadline guidance **29 September
2026** and current-charge guidance **21 June 2026**. Do not use a mixed-year
ATO illustration to override the Act's payment-day commencement.

The historical territory Acts and dictionary limits are stated above.
No full delegated-instrument inventory, all-programme survey, actual
employer determination, return, payroll, declaration, bank transaction,
professional sign-off or completed financial review is claimed. Recheck
volatile law and operational guidance before engagement use.

[SG]: https://www.legislation.gov.au/C2004A04402/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html
[REG]: https://www.legislation.gov.au/F2018L01289/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html
[PAYDAY]: https://www.legislation.gov.au/C2025A00057/asmade/2025-11-06/text/original/epub/OEBPS/document_1/document_1.html
[OUTOFCYCLE]: https://www.legislation.gov.au/F2026L00784/asmade/2026-06-24/text/original/epub/OEBPS/document_1/document_1.html
[RATES]: https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee
[DEADLINES]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/payment-deadlines-for-payday-super
[ELIGIBILITY]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/work-out-if-you-have-to-pay-super
[CHARGE]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/missed-or-late-payday-super-payments/what-happens-if-you-dont-pay-super-correctly
[TERRITORY]: https://www.legislation.gov.au/C1955A00034/2020-12-18/2020-12-18/text/original/epub/OEBPS/document_1/document_1.html
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[AMEND71]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[AMEND86]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html

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
