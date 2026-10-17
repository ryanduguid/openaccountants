---
name: nf-tax-system
description: >
  Establish Norfolk Island's Australian tax application and territorial
  exceptions before choosing a taxpayer, tax period or mainland tax guide.
  Covers the income tax and Medicare reforms, island transactions versus
  mainland GST connections, business registration and withholding distinctions,
  capital gains transition conditions, and employer super routing for 2026.
  Use for Norfolk Island tax, ABN, GST, old offshore exemption or pre-reform
  asset questions. Includes primary legislation, authority guidance and
  classification examples. This source-cited reference holds unresolved
  local charges and substantive tax computations; it does not complete the
  country pack or replace the applicable workflow requirements.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Scope checked on 17 October 2026; Australian financial years and event-specific transition dates must be identified separately"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
---

# Norfolk Island: tax application and territorial exceptions

Establish the person or entity, residence, income or transaction, asset,
work location and event date before choosing a tax treatment. NF is the
catalogue identifier for Norfolk Island. Australian tax legislation applies
with particular territorial and transitional rules; an NF address alone
does not select every Australian tax or establish an exemption.

Load `workflow-base` and the relevant domain base and substantive references.
Preserve their source and period gates, confirmed profile, refusals, four
universal outputs and all applicable domain outputs and checks. This Tier 2
reference is not a complete country companion or permission to prepare a
financial result with missing mandatory sources or country slots.

## Income tax, Medicare and taxpayer classification

The Tax and Superannuation Laws Amendment (Norfolk Island Reforms) Act 2015
commenced on **1 July 2016**. Schedule 1 repealed the former territorial
income-tax exemption division, removed specified Norfolk Medicare levy
exclusions and generally applied its income-tax amendments for the
**2016–17 and later income years**. Do not use a pre-reform exemption or
historical Medicare ruling as a current blanket exclusion. [REFORM, section
2 and Schedule 1 items 1, 5–8 and 19][REFORM]

The current ATO Norfolk resident guidance identifies employment,
superannuation/pensions, investments, business/partnership/trust income,
foreign sources and crowdfunding as possible income categories. Deductions,
amounts excluded from assessable income, offsets and Medicare entitlement
need their own conditions. It states that a person entitled to Medicare
benefits may have to pay the levy. Neither Norfolk residence nor access to
health care alone supplies a levy calculation. [INDIVIDUAL]

For an actual return, establish individual or entity residence under the
applicable Australian law; income character and source; the income year;
available deductions and offsets; and the relevant rates and relief.
Treat company, trust, partnership and sole-trader positions separately.
This guide supplies no income-tax, company-tax or Medicare rate table.
An administering state's general table must be checked for the actual
Norfolk facts and period before use.

## Business registration and employee withholding

The ATO Norfolk business guidance requires attention to business structure,
tax file number readiness, business income/deductions, PAYG instalments and
records. Employment can add PAYG withholding and super obligations; fringe
benefits can add FBT registration. These obligations are separate from GST.
[BUSINESS]

Read the ATO's broad statement that an ABN is not required with its specific
business guidance: it identifies an ABN requirement for mainland trading,
online dealings and an employer required to register for FBT. Determine the
actual activity and registration route rather than treating every Norfolk
business as either automatically registered or unconditionally exempt.
[SCOPE]; [BUSINESS]

The Norfolk exception for payments to suppliers who do not quote an ABN
does not abolish employee PAYG withholding. The ATO worker guidance covers
employees, directors/office holders, labour hire and agreed withholding.
The employee's TFN declaration and pay circumstances affect withholding.
An ABN exception is not an employee TFN exception. Do not collect or submit
identifiers through this guide; record reviewer-held readiness instead.
[WORKERS]

The worker page says STP reports are due on or before payday and separates
payments outside STP. Actual withholding tables, reporting concessions,
finalisation, remittance periods, forms and corrections require a current
payroll analysis. Its general contractor description is not a finding that
every contractor is outside super: the SG Act expands employee status to
specified labour contracts. Use `nf-super-guarantee`. [WORKERS];
[SG, section 12][SG]

## Island transactions and mainland GST connections

The ATO records that the former Norfolk Island GST ceased on **1 July
2016**, and Australian GST does not apply to transactions on Norfolk
Island. Its scope guidance also excludes luxury car tax, wine equalisation
tax and fuel tax credits for island transactions. These are affirmative
territorial statements, not evidence that income tax, employer obligations
or local charges are absent. [SCOPE]; [GST]

A Norfolk business must separately consider supplies connected with the
Australian mainland, GST registration, taxable versus GST-free/input-taxed
supplies, and any input-credit conditions. Registration does not by itself
make its Norfolk sales taxable. Mainland suppliers' goods may be sold
GST-free only when the export conditions are met; a Norfolk destination
alone is not proof of export or an automatic refund. [GST]

The ATO mainland-transactions page contains separate refund, voluntary
registration, credit, backdating and BAS branches. This guide does not
select a registration threshold, credit entitlement, export deadline or
refund route for an actual transaction. It also does not establish customs,
excise, biosecurity, tourist refund or island tariff treatment. Acquire the
applicable primary rules and transaction evidence before computing or
describing any of those charges as absent.

## Capital gains: preserve the amended transition

The original 2015 reform Act proposed a June 2016 market-value/acquisition
transition. The Norfolk Island CGT Exemption Act 2016 amended that scheme
immediately after commencement of the reform Act. Do not copy the original
June rebasing formula as the current Norfolk rule. [REFORM, Schedule 1 item
18][REFORM]; [CGT2016, section 2 and Schedule 1][CGT2016]

Current Income Tax (Transitional Provisions) Act 1997 section 102-25(2)
requires all of the following:

- The entity was a prescribed person under the former exemption division
  because of Norfolk residence on or before **23 October 2015**.
- It acquired the asset on or before that day.
- The asset is not already a pre-CGT asset.
- A hypothetical CGT event immediately before **24 October 2015** would
  have produced a gain or loss disregarded because of that prescribed status.

When those conditions are met, Parts 3-1 and 3-3 apply to the asset with
references to **20 September 1985** read as **24 October 2015**. This is a
date substitution with legal conditions, not a universal market-value
rebasing or exemption for every asset a Norfolk resident owns. A mainland
or foreign asset requires its own historical prescribed-person and source
analysis. [TRANS, section 102-25(2)][TRANS]

Subsection (3)(b) removes the specified acquisition-date record requirement
for an asset to which subsection (2) applies. It does not remove every
recordkeeping obligation or establish that the subsection applies where
historical facts are unknown. Subsection (4)'s choice is expressly about
the **Cocos subsection (1)**, not an election to disapply Norfolk subsection
(2). Actual disposals, improvements/separate assets, succession, ordinary
income, other CGT rules and relief remain subject to further analysis.
[TRANS]

## Classification examples and review checks

These fictional cases select a source branch; they do not calculate a
person's tax:

| Stipulated facts | Record the result |
|---|---|
| A person relies on an old Norfolk offshore-income exemption for 2026 income | Apply the post-reform framework; establish the current taxpayer and income rules before any amount. |
| A Norfolk shop makes only island transactions and is registered for mainland GST dealings | The registration does not itself make the island sales subject to Australian GST. Check mainland-connected transactions separately. |
| A Norfolk employer says supplier no-ABN relief also removes employee PAYG withholding | Reject that inference; the supplier exception and employee withholding have different subjects. |
| An asset was acquired on 23 October 2015 and every subsection 102-25(2) condition is stipulated satisfied | Apply the statutory date substitution; do not import June 2016 market-value rebasing. |
| The same asset was first acquired on 24 October 2015 | The acquisition cutoff in subsection (2)(b) is not satisfied. Investigate ordinary CGT rules and other relief. |
| Acquisition is old enough but historical prescribed status or hypothetical exemption is unknown | Hold the transition; residence and acquisition date alone do not establish it. |
| A Norfolk resident works for an employer on the mainland | Use the actual employer/employee residence, work location and payment-day rules in `nf-super-guarantee`; residence alone does not select 11%. |
| No current island rates or fees ordinance is supplied | Record a source gap. Do not infer that all local charges are absent. |

Check the territory, taxpayer and event; historical versus operative law;
island versus mainland-connected activity; ABN versus employee TFN rules;
all CGT transition conditions; and the current SG payment day. Keep an
unknown required fact as Needs Input and an unresolved legal rule on hold.

## Sources, periods and outstanding coverage

Checked on 17 October 2026: the complete 2015 reform and 2016 CGT exemption
Acts; current section 102-25; the ATO Norfolk collection's resident,
business, GST and worker sections; and the selected SG sources identified
in `nf-super-guarantee`. The ATO sections carry their own update dates;
one collection download is not a single uniform law revision.

The ATO guidance supports Australian tax application with exceptions. It
does not establish that every Australian state tax or local Norfolk
ordinance applies, or that any omitted charge is absent. This batch leaves
substantive individual/corporate tax, comprehensive consumption/imports,
payroll, social programmes beyond selected SG rules, entity formation and
reporting, withholding/treaties/transfer pricing, property and transaction
charges, compliance and other special regimes open. No complete-country
credit, practitioner sign-off or engagement output package is claimed.

[REFORM]: https://www.legislation.gov.au/C2015A00053/asmade
[CGT2016]: https://www.legislation.gov.au/C2016A00020/asmade
[TRANS]: https://www.ato.gov.au/law/view/print?DocID=PAC%2F19970040%2F102-25
[SCOPE]: https://www.ato.gov.au/norfolk-island/norfolk-island-tax-and-super
[INDIVIDUAL]: https://www.ato.gov.au/norfolk-island/norfolk-island-residents-and-individual-tax
[BUSINESS]: https://www.ato.gov.au/norfolk-island/tax-for-businesses
[GST]: https://www.ato.gov.au/norfolk-island/tax-for-businesses/gst-transactions-with-mainland-australia
[WORKERS]: https://www.ato.gov.au/norfolk-island/tax-for-businesses/paying-your-workers
[SG]: https://www.legislation.gov.au/C2004A04402/2026-07-01/text

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
