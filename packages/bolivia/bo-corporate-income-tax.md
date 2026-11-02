---
name: bo-corporate-income-tax
description: >
  Bolivia corporate income tax (IUE) reference for ordinary Bolivian SA and
  SRL companies carrying on commercial or service activities, using primary
  material read on 3 November 2026. Covers the 25% rate, accounting-to-tax
  reconciliation, ordinary loss vintages, selected depreciation and domestic
  shareholder-interest restrictions, Formulario 500, F605 and the 2026 digital
  reporting changes. Includes the corrected December 2025 filing extensions.
  Trigger on Bolivia company tax, impuesto sobre las utilidades de las empresas,
  IUE corporate return, F500 or Bolivia company tax losses. Specialist regimes,
  actual interest calculations and unqualified cross-border positions require
  further source work and professional review.
jurisdiction: BO
category: international
tax_year: 2026
tax_year_notes: "Rules read as at 3 November 2026; December 2025 extension history is separately labelled. December 2026 closing figures and 2027 filing mechanics need later verification."
tier: 2
review_status: pending_review
last_updated: 2026-11-03
version: 0.1
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bolivia corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this reference to prepare documented IUE research and, after the source and workflow gates below are satisfied, working papers for a Bolivian professional reviewer. The supported ordinary profile is an SA or SRL with Bolivian commercial or service operations, required accounting records and a 31 December fiscal close. The statutory population is wider: Ley 843 articles 36-39 also cover other enterprises and foreign branches. Their inclusion in the law does not bring their specialist computations into this guide.

**Period and source gate.** The principal source is SIN's Ley 843 and DS 24051 compendium updated to 30 September 2026, with selected current filing resolutions and official instructions read on 3 November 2026. The compendium is an official reference compilation, not a substitute for Gaceta publication. Before an engagement computation, establish the operative statutes, amendments, regulations and administrative rules for the requested period, including any changes after the compilation date. Read the complete relied-on provisions and applicable exceptions. A read date or `tax_year: 2026` does not certify the whole year's law. A December 2026 return also requires closing-period UFV evidence and the 2027 filing rules, which this reference does not establish.

Load `workflow-base` and `corporate-income-tax-workflow-base` in full. Preserve all 26 corporate intake fields, the ordered computation, both sets of 18 checks, all global refusals, the 4 universal outputs and every corporate output. A missing required source, content slot, refusal message or calculation/delivery capability prevents a deliverable financial result. An unknown required slot is **Needs Input**, never a zero amount or an assertion that the regime does not exist.

This guide does not authorise an actual filing, payment or taxpayer-facing advice. Use redacted references. The reviewer retains legal names, NITs, identity documents, bank details and credentials and personally completes authentication, submission and payment. No factual default is authorised by this guide. Label the cases below as hypothetical; they do not resolve actual source conditions.

## Ask the client first

Read supplied records first, then combine the following facts with the corporate base's full intake in the universal profile confirmation:

1. **Entity, period and activity:** legal form, incorporation and tax residence, principal registered activity, fiscal close and any short period, residence dispute, cessation, liquidation or sector concession. Keep identifiers with the reviewer.
2. **Books and currencies:** approved financial statements, trial balance, complete ledgers, audit status, accounting framework, functional and presentation currencies, BOB filing reconciliation and the applicable SIN-approved technical accounting rules and UFV evidence.
3. **Income and adjustments:** Bolivia-source and other income, distributions received, transaction evidence, payroll/withholding support, provisions, donations, asset tax bases and first-use dates, paid taxes and interest. Obtain the facts establishing each exclusion or deduction.
4. **Prior periods:** loss vintages and unused balances tied to filed returns, ownership/reorganisation history, credit and payment evidence, unresolved assessments and prior annual gross income used for reporting obligations.
5. **Owners and cross-border activity:** shareholder loans and payment-date benchmarks, related-party flows, foreign services, overseas beneficiaries, branches, foreign tax, group revenue and any potential Pillar Two or other reporting overlay.
6. **Filing and reviewer:** F500/F605 registration and prior receipts, current filing instructions and calendar, exemption or incentive evidence, outstanding debts/notices and confirmation of professional review and authority to provide redacted data.

Confirm the inferred profile before classification or computation. A current tax audit or notice of deficiency fires **R-CIT-6** even if the user confirms the profile. Do not calculate first and add a controversy warning afterwards. Group remaining factual questions under the universal limit; the cash-floor filter is unavailable because this guide permits no missing-fact default.

## The method, step by step

### 1. Establish the source, entity and period [Ley 843, arts. 36-46](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf)

IUE applies to profits from annual financial statements adjusted under tax law. Ley 843 article 42 and DS 24051 article 4 identify Bolivian source by the location or economic use of assets and domestic activities, acts or facts, irrespective of nationality, residence or where contracts are made. An overseas invoice or customer does not by itself establish foreign-source income. Article 44 also addresses directors' remuneration and certain services supplied from abroad connected with Bolivian profits.

Use accrual allocation under article 46, subject to its exception for the exigibility of profits on instalment sales. Verify the exception before replacing accrual with a cash convention. The principal registered activity determines the applicable fiscal close, as the [SIN activity guidance](https://siatinfo.impuestos.gob.bo/index.php/actividades-economicas) explains. Do not choose a convenient close or assume that every incorporated entity uses December.

### 2. Use the conditioned figures [Ley 843 and DS 24051](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf)

The following are reference rules read in the 2026 sources. Every row retains its conditions; the amounts in worked cases are fictional inputs.

| Item | Amount or rule and conditions | Period | Official source and exact short wording |
| --- | --- | --- | --- |
| Ordinary IUE | 25% of net taxable profit, after the applicable adjustments and eligible losses; specialist rates and overlays require separate qualification | 2026 reference | Ley 843 art. 50: 'veinticinco por ciento (25%)'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Ordinary loss carryforward | Following 3 years; no indexation. This row does not apply the special new productive venture, mining or hydrocarbon rules | 2026 reference | Ley 843 art. 48: 'hasta los tres (3) años siguientes'; 'no serán objeto de actualización'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Buildings | 40 years, 2.5% annual coefficient; exclude land and verify article 26 ownership/valuation conditions | 2026 reference | DS 24051 arts. 20-26 and art. 22 annex: 'Edificaciones', '40 años', '2,5%'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Office furniture | 10 years, 10% annual coefficient; admitted tax basis, business use and first-use apportionment required | 2026 reference | DS 24051 art. 22 annex: 'Muebles y enseres de oficina', '10 años', '10,0%'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| General machinery; equipment/installations | 8 years, 12.5% annual coefficient, within the corresponding annex classifications; separate special sector rules | 2026 reference | DS 24051 art. 22 annex: 'Maquinaria en general'; 'Equipos e instalaciones'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Motor vehicles | 5 years, 20% annual coefficient; tax basis, actual business use and first-use apportionment required | 2026 reference | DS 24051 art. 22 annex: 'Vehículos automotores', '5 años', '20,0%'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Computing equipment | 4 years, 25% annual coefficient; tax basis, actual business use and first-use apportionment required | 2026 reference | DS 24051 art. 22 annex: 'Equipos de Computación', '4 años', '25,0%'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| First-use depreciation | Count from use in income production; the initial month counts as a full month. Apply months/12 to the annual amount | 2026 reference | DS 24051 art. 22: 'El mes inicial en todos los casos, se tomará como mes completo'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Repairs and improvements | Repairs up to 20% of the asset value are deductible under art. 22; above that, capitalise the improvement and depreciate over the remaining useful life | 2026 reference | DS 24051 art. 22: 'veinte por ciento (20%) del valor del bien'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Paid intangible | Amortisation over 5 years from exploitation, for an admitted acquired intangible for which a price was paid | 2026 reference | DS 24051 arts. 18(e) and 27: 'cinco (5) años'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Domestic owner/shareholder loan interest | Apply the payment-date BCB active bank rate restriction and the limit of 30% of interest paid by the company to third parties in the same year. Necessary business purpose and evidence remain required | 2026 reference | DS 24051 art. 18(k): 'treinta por ciento (30%)'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Ordinary annual return and payment | Within 120 days following the applicable fiscal close, subject to verified current extensions and calendar rules | 2026 reference, not a verified 2027 filing date | DS 24051 art. 39: 'ciento veinte (120) días posteriores al cierre'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Additional financial reporting | Annual sales/gross income at or above Bs 1,700,000 triggers the additional package. Prior threshold history must also be tested | 2026 reporting amendment | RND 102600000014, sole article II replacing art. 7(b): 'iguales o mayores a Bs1.700.000'. https://www.impuestos.gob.bo/wp-content/uploads/2026/04/RND-102600000014.pdf |
| Omission of payment penalty | Statutory starting fine of 60% of the UFV-updated omitted tax, subject to art. 165, cure/reduction provisions and any applicable relief. Do not automatically apply it to every late filing | 2026 reference | Ley 2492 art. 165 and related DS 27310 art. 42 text: 'sesenta por ciento (60%)'. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf |

### 3. Reconcile the books to tax [Ley 843, art. 47; DS 24051, arts. 6-31](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf)

Start with approved profit before tax and identify what that figure already includes. Trace every adjustment to a ledger row and the operative tax provision. A deductible expense already charged in the accounts is not deducted a second time.

| Position | Treatment and necessary conditions |
| --- | --- |
| Source income | Determine Bolivian source under arts. 42-44 and DS art. 4. DS art. 31 excludes foreign-source income and distributions received from another enterprise subject to IUE from the combined result. Prove the conditions; do not turn this into an exemption for every dividend or overseas receipt |
| Ordinary costs | Ley art. 47 and DS arts. 7-8 and 15 require a connection to obtaining taxable profit or maintaining its source and adequate original evidence. DS art. 8 also cross-refers to banking evidence requirements. Verify the current transaction-level banking rules before claiming an affected deduction |
| Private expenditure and owner withdrawals | Add back private support/withdrawals and payments outside the admitted remuneration rules: Ley art. 47 and DS art. 18(a), (l) |
| Payroll and directors | Apply the payment, actual-service, payroll, social contribution and withholding conditions in Ley art. 47 and DS arts. 11-12. Directors' remuneration has a separate restriction. A ledger description alone does not prove compliance |
| Tax charges | IUE itself is not deductible. DS art. 14 permits IT actually paid, but excludes IT settled using the IUE payment credit. Avoid deducting a tax that was not paid in the required manner |
| IVA and ICE | DS art. 14, including the DS 5563/2026 addition, conditionally addresses unrecoverable IVA and separately invoiced unrecoverable ICE. Determine recoverability and operation type before treating either as a cost. Do not import a blanket indirect-tax disallowance |
| Fines and late-payment charges | DS art. 14 disallows the tax fines and penalties identified there. Separate the legal nature of each charge before adjustment; do not assume every commercial compensatory payment is a tax penalty |
| Provisions and bad debts | Add back unauthorised reserves under Ley art. 47 and DS art. 18(g). The specific bad-debt deduction/provision in DS art. 17 needs its own evidence, history and collection conditions; a book expected-credit-loss estimate alone is insufficient |
| Donations and exemptions | Ordinary SA/SRL status does not establish an exemption. Apply Ley art. 49 and DS arts. 5 and 18(f) only after the complete qualification and limit are verified. Otherwise hold the claim; do not infer that a generous payment is deductible |
| Depreciation and intangible amortisation | Reverse book charges and replace them with the admitted tax charges under DS arts. 20-27. Keep land, business-use allocation, prior years, first use, disposals, revaluations and special regimes separate. Prior-year omitted depreciation cannot simply be caught up in the current year under art. 20 |
| Interest | Establish business purpose under DS art. 13 and the specific owner/shareholder restrictions under art. 18(k). This is not a generic 30% EBITDA rule. Foreign loans and unresolved benchmark evidence are outside supported computation |
| Inventory | Apply DS art. 9's supported valuation method and closing adjustments. A change requires prior administrative authorisation. Do not assume an accounting method change automatically changes the tax method |

DS articles 36-38 require Spanish-language statements in bolivianos and address tax valuation and constant-currency adjustment. Article 48 and the [2026 reporting amendment](https://www.impuestos.gob.bo/wp-content/uploads/2026/04/RND-102600000014.pdf) require the technical accounting rules brought into force by express administrative authority. Establish those operative rules, NC3/other applicable standards and the necessary UFV series before an actual adjustment. A nominal profit-only computation is not a substitute. The examples assume their tax bases and adjustments have already been established under the applicable rules.

### 4. Apply supported loss vintages [Ley 843, art. 48](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf)

Maintain a schedule by origin year, original tax loss, amounts previously used, remaining amount and final eligible year. For the ordinary rule, use the following 3 years without indexation. A 2022 ordinary loss therefore has a 2023-2025 window; it is not available in 2026. A 2024 ordinary loss has a 2025-2027 window, subject to proving its unused balance and the applicable entity/period conditions.

The old indefinite indexed carryforward wording still appears in DS article 32. Do not use it to override the later Ley article 48. The Tax Code's [article 5 hierarchy](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf) is relevant to this conflict. Special productive undertakings, mining/hydrocarbons, reorganisations, transfers of losses and ownership changes require separate source qualification. No carryback, group offset or transferred balance is established by this ordinary schedule.

Apply only validated available losses against the relevant profit, then the ordinary rate. Track the used and remaining amounts separately. Do not index the ordinary loss because asset tax bases use an inflation mechanism.

### 5. Reconcile tax, benefits and payments without duplication

Compute the supported ordinary liability from the established taxable base. The current source work does not qualify credits, reduced activity rates, sector surcharges, R&D/IP incentives, branch remittances, foreign tax credits, investment relief or group relief for an actual claimant. Identify each potential regime and obtain its complete operative authority before applying it. An unused slot is not proof of a zero rate or no entitlement.

Keep benefit eligibility, benefit utilised, tax liability after benefits and verified payments as separate stages under the corporate base. Do not deduct a payment or credit twice. DS article 14's treatment of IT settled with IUE is relevant to the companion IT computation; it is not authority to subtract IT from the IUE liability. Reconcile current and deferred tax under the separately established reporting framework; this reference supplies no independent DTA recognition or deferred-tax measurement rule.

### 6. Screen related parties and economic substance

[Ley 843 articles 45, 45 bis and 45 ter](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf) require comparable independent-party pricing and permit adjustments between linked parties. The linkage definition includes participation in management, control, administration or capital and common participation. Related companies' separate records must permit determination of the Bolivian-source result.

[Tax Code article 8](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf) addresses economic reality, manifestly inappropriate legal forms and simulation. Do not treat formal documentation as sufficient evidence of substance. An aggressive position fires R-CIT-7.

Transfer-pricing documentation thresholds, foreign payment character, treaty eligibility, permanent establishments, CFC/hybrid rules, foreign tax relief and Pillar Two enactment/status require verified companions and period-specific authority. Load `transfer-pricing-workflow-base` when applicable and qualify its country content before work. The group-revenue screen in the corporate base does not establish any Bolivian top-up tax. All required cross-border, Pillar Two and disclosure outputs remain required when applicable; hold the result until their source conditions are resolved.

## Boundary and exception table

| Facts or required slot | Action |
| --- | --- |
| Ordinary SA/SRL, domestic commercial/services profile | Proceed only after period, source, records, refusals and technical accounting gates are satisfied |
| New productive undertaking, finance/insurance, extraction, shipping/aviation, charity, special zone, exemption, incentive or reduced-rate claim | Obtain the applicable specialist sources and content. Apply any fired corporate refusal and R-BO-CIT-SCOPE; do not extend ordinary examples |
| Branch, foreign beneficiary, treaty, foreign loan or other cross-border position | Qualify the necessary specialist computation, withholding and documentation. Do not derive remittance tax by applying 25% to a guessed base |
| Carryback, loss transfer, ownership change, reorganisation or group relief | Needs Input pending the applicable source and eligibility rules; no ordinary loss schedule authorises the claim |
| R&D/IP, investment, withholding or foreign tax credit; payment/instalment claim | Qualify eligibility, caps, ordering and evidence before giving a financial result; no presumed zero slot |
| CFC, hybrid mismatch, BEAT/GILTI equivalent, QDMTT/IIR/UTPR or domestic top-up | Obtain current country authority and relevant overlays. Do not assert that an unresearched regime is absent |
| Debt, late return, omission fine, relief, objection, audit or limitation period | Use a separate procedural review, including Ley 1733/2026 and subsequent implementation where relevant; a fired R-CIT-6 stops computation |
| Missing current UFV/technical accounting, filing precision, source or required workflow capability | Needs Input and R-BO-CIT-SOURCE or R-BO-CIT-TOOLS as applicable; no deliverable financial result |

The [Ley 1733 text](https://www.impuestos.gob.bo/wp-content/uploads/2026/05/L17332051NCPP.pdf) establishes exceptional debt relief and also amends other provisions. SIN's [16 September 2026 notice](https://www.impuestos.gob.bo/index.php/nota_prensa/el-gobierno-amplia-el-plazo-de-regularizacion-tributaria-hasta-el-31-de-diciembre-de-2026/) reports an extension under DS 5708. This guide does not qualify eligibility, elections, payment plans, withdrawal of proceedings or the operative extension instrument for an actual debt. Ordinary penalty arithmetic cannot replace that review.

## Worked cases

These are fictional reference cases, with all stated source, basis, payment and eligibility conditions assumed established for the illustration only. Amounts are BOB. Decimal arithmetic below verifies the examples; it does not establish SIN box precision, UFV conversions or an actual filing result.

### Case 1: reconcile profit without deducting expenses twice

An ordinary service SRL has approved profit before tax of Bs 200,000. That profit already includes ordinary deductible operating expenses of Bs 60,000, private expenses of Bs 12,000, a nondeductible tax fine of Bs 8,000 and book depreciation of Bs 30,000. It also includes Bs 10,000 of established foreign-source income and Bs 10,000 of distributions from another enterprise subject to IUE. The separately established deductible tax depreciation is Bs 40,000. There are no losses, benefits or payments in this illustration.

Under Ley articles 42 and 47 and DS articles 14, 18, 20-22 and 31, add back the private costs, tax fine and book depreciation, then subtract the tax depreciation and the 2 qualifying excluded receipts. Taxable profit is Bs 190,000 and IUE is Bs 47,500. The Bs 60,000 operating expenses remain within the starting profit; subtracting them again would understate taxable profit.

```oa-check
name: Bolivia ordinary IUE reconciliation, fictional 2026
inputs:
  profit_before_tax: 200000
  private_expenses: 12000
  tax_fine: 8000
  book_depreciation: 30000
  tax_depreciation: 40000
  foreign_source_income: 10000
  qualifying_distribution: 10000
steps:
  - taxable_profit: profit_before_tax + private_expenses + tax_fine + book_depreciation - tax_depreciation - foreign_source_income - qualifying_distribution
  - iue: taxable_profit * 0.25
expected:
  taxable_profit: 190000
  iue: 47500
```

### Case 2: decide which loss vintage can be used

An ordinary company's 2026 adjusted profit before losses is Bs 120,000. Its verified unused losses are Bs 60,000 from 2022 and Bs 80,000 from 2024, with no special regime or reorganisation. Ley article 48's following-3-year rule excludes the 2022 balance from 2026. The validated 2024 balance can reduce profit to Bs 40,000, giving IUE of Bs 10,000 and no remaining 2024 loss. Applying both vintages would incorrectly reduce the base to zero and understate IUE by Bs 10,000. No inflation uplift is applied to either ordinary loss.

```oa-check
name: Bolivia loss-vintage decision, fictional 2026
inputs:
  profit_before_losses: 120000
  eligible_2024_loss: 80000
  expired_2022_loss: 60000
steps:
  - used_loss: min(profit_before_losses, eligible_2024_loss)
  - taxable_profit: max(0, profit_before_losses - used_loss)
  - iue: taxable_profit * 0.25
  - remaining_2024_loss: eligible_2024_loss - used_loss
  - incorrect_base_if_expired_loss_used: max(0, profit_before_losses - eligible_2024_loss - expired_2022_loss)
  - underpayment_from_wrong_vintage: iue - incorrect_base_if_expired_loss_used * 0.25
expected:
  used_loss: 80000
  taxable_profit: 40000
  iue: 10000
  remaining_2024_loss: 0
  incorrect_base_if_expired_loss_used: 0
  underpayment_from_wrong_vintage: 10000
```

### Case 3: replace book depreciation with a first-use tax charge

A company first uses computing equipment in July 2026, wholly in taxable business. Its established admitted closing tax cost, including all required adjustments, is Bs 40,000. No accelerated or other special treatment applies. DS article 22 and its annex give the ordinary 25% annual coefficient, with 6 months of use in this year. The deduction is Bs 5,000. If the accounts already charged Bs 8,000, add that back and deduct Bs 5,000, a net positive tax-base adjustment of Bs 3,000. At the ordinary rate its isolated tax effect is Bs 750 before any loss or other interaction. This case does not calculate the underlying UFV adjustment.

```oa-check
name: Bolivia computing equipment first use, fictional 2026
inputs:
  admitted_tax_cost: 40000
  annual_rate: 0.25
  months_in_use: 6
  book_charge: 8000
steps:
  - tax_depreciation: admitted_tax_cost * annual_rate * months_in_use / 12
  - net_addback: book_charge - tax_depreciation
  - isolated_tax_effect: net_addback * 0.25
expected:
  tax_depreciation: 5000
  net_addback: 3000
  isolated_tax_effect: 750
```

### Case 4: apply the domestic shareholder-interest limits

A company paid Bs 18,000 interest on a necessary domestic shareholder loan and charged it in profit. The properly evidenced payment-date BCB rate test would allow Bs 15,000. It paid Bs 20,000 interest to third parties in the same year. Under DS article 18(k), the additional third-party-interest limit is Bs 6,000. Deduct only Bs 6,000 of the shareholder interest, adding back Bs 12,000. Its isolated ordinary-rate tax effect is Bs 3,000 before other interactions. This case assumes the benchmarks and all other deduction conditions are verified; it is not a foreign-loan or EBITDA calculation.

```oa-check
name: Bolivia domestic shareholder interest, fictional 2026
inputs:
  shareholder_interest: 18000
  amount_allowed_by_bcb_rate_test: 15000
  third_party_interest_paid: 20000
steps:
  - third_party_linked_limit: third_party_interest_paid * 0.30
  - deductible_shareholder_interest: min(shareholder_interest, amount_allowed_by_bcb_rate_test, third_party_linked_limit)
  - addback: shareholder_interest - deductible_shareholder_interest
  - isolated_tax_effect: addback * 0.25
expected:
  third_party_linked_limit: 6000
  deductible_shareholder_interest: 6000
  addback: 12000
  isolated_tax_effect: 3000
```

### Case 5: choose the reporting package at the exact threshold

Consider 2 newly operating ordinary companies with no inherited or earlier reporting obligation and otherwise identical facts. Their established annual sales/gross income under RND 101800000004 article 3(a) is Bs 1,699,999 and Bs 1,700,000 respectively. The first enters amended article 7(a)'s F605 information branch. The second reaches article 7(b) and must also supply the additional information and signed PDF reports described below. The difference is Bs one. A zero IUE liability would not itself remove these reporting duties. If either company has an earlier threshold history, stop this simplified decision and apply the persistence provision to that history.

```oa-check
name: Bolivia reporting threshold equality, fictional 2026
inputs:
  lower_company_gross_income: 1699999
  threshold: 1700000
steps:
  - gap_to_additional_reporting: threshold - lower_company_gross_income
  - higher_company_gross_income: lower_company_gross_income + gap_to_additional_reporting
expected:
  gap_to_additional_reporting: 1
  higher_company_gross_income: 1700000
```

The block checks the amounts, not the legal branch selection. The reviewer must check '<' against 'equal to or above' and the history conditions against the actual resolution.

### Case 6: separate the historical return and supporting-document dates

For an ordinary 31 December 2025 close, RND 102600000014 as corrected gives 4 May 2026 for the IUE return and payment, whilst its separate supporting-document extension remains 29 May 2026. A company cannot delay the tax return/payment until 29 May merely because its financial reporting package is due then. For a 31 December 2026 close, neither historical date answers the question: obtain the applicable 2027 instructions and calendar. Late or disputed historical obligations require the separate debt/procedure review above.

## When to refuse or refer

Run the universal catalogue and **all R-CIT-1 through R-CIT-12** from the loaded corporate base. Emit their exact canonical messages and retain the full cleared/fired trace. Profile confirmation or willingness to accept a high tax figure cannot waive a refusal.

The following country catalogue adds explicit stops. On a fired country trigger, output the code followed by its message verbatim and recommend a qualified Bolivian practitioner. If a refusal occurs before computation, supply its scope/refusal trace; do not create a partially classified return or a normal financial output package.

| Code | Trigger | Exact message |
| --- | --- | --- |
| R-BO-CIT-SOURCE | A required operative source, period rule, technical accounting treatment, form precision or other mandatory content slot is unresolved | I cannot compute this Bolivia corporate tax result because a required period-specific source or rule is unresolved. Obtain the applicable primary authority and evidence with a qualified Bolivian practitioner before continuing. |
| R-BO-CIT-SCOPE | A requested computation needs a specialist regime or branch outside this guide's qualified ordinary-company rules | This Bolivia corporate tax computation needs specialist rules outside this guide's qualified scope. Load and verify the applicable content and consult a qualified Bolivian practitioner before computing. |
| R-BO-CIT-AMBIGUITY | More than 10 grouped factual questions remain under the universal ambiguity process | More than 10 grouped factual questions remain unresolved. The records need review by a qualified Bolivian practitioner before this corporate tax computation can continue. |
| R-BO-CIT-TOOLS | A required calculation, workbook recalculation or delivery capability is unavailable | A required calculation, recalculation or delivery capability is unavailable. I cannot provide a deliverable Bolivia corporate tax result until the workflow's required tools and checks are available. |

No cash floor or missing-fact default is permitted. Flag every judgement, source limitation, deadline uncertainty and unresolved item for the reviewer. Do not invent a materiality threshold that suppresses a required source condition. R-REVIEWER-MISSING and R-CONTENT-MISMATCH remain available under their loaded universal messages.

## Filing and payment

### F500 and F605 are separate obligations

For a company otherwise subject to the annual IUE declaration, [DS 24051 article 40](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf) requires the return even when all income for the year is exempt or the year produces a loss. A loss or exemption does not itself remove the filing obligation. Under article 39, payment is required only where applicable; do not infer a payment merely from the obligation to file. For the supported ordinary bookkeeping profile, use F500 after checking the requested year's instructions and form.

SIN's [official F500 instructions](https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-a-las-utilidades-de-las-empresas/500-iue-contribuyentes-obligados-a-llevar-registros-contables) identify Formulario 500 and Rubro 1 for the ordinary commercial/service bookkeeping profile. They direct filing through SIAT en Línea, Módulo Declaraciones Juradas > Declaración Jurada. These undated live instructions establish that route, not an annual box-level schema or an authenticated portal test. Obtain the requested year's exact form version, tax-field mapping, precision and rounding before producing filing figures. The reviewer supplies identifiers and signs/submits personally.

[RND 101800000004 article 8](https://unumlex.impuestos.gob.bo/wp-content/uploads/2022/02/RND-No-101800000004-Estados-Financieros.docx-MOD3.pdf) sets the ordinary financial-document transmission period at 120 days after close, separately from the IUE return/payment under DS article 39. Verify current exceptions for each obligation. The Tax Code's [article 4 time rules](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf) distinguish calendar and working-day periods and address a non-working final day. Do not label the ordinary 120-day period as 120 working days or derive an actual deadline without the applicable calendar.

Under [RND 102600000014, sole article II](https://www.impuestos.gob.bo/wp-content/uploads/2026/04/RND-102600000014.pdf), ordinary bookkeeping taxpayers below Bs 1,700,000 annual sales/gross income send through SIAT/F605:

1. Trial balance of sums and balances.
2. Balance sheet.
3. Income statement.
4. Accumulated results/equity statement.
5. Changes in financial position/cash flow statement.
6. Notes.
7. Valued physical inventory.
8. Loss compensation information where the benefit applies.

At or above that threshold, also send Información Tributaria Complementaria and attach the signed PDF financial statements, external audit opinion, tax opinion, minimum tax procedures report and complementary tax information. RND 101800000004 article 3(a)'s gross-income definition extends beyond VAT-taxable invoiced sales to the other recurring and exceptional receipts described there. Reconcile that definition rather than substituting net taxable profit or cash bank deposits.

The additional-package obligation established in a year 'subsistirá hasta la siguiente gestión fiscal' in which the specified threshold is not reached. Establish the prior history and the period in which the duty ceases under the applicable text and official instructions. This guide does not resolve a taxpayer's falling-income transition by assuming immediate exemption from the reports.

RND 102600000014 repeals the old resolution's articles 4-6 and the specified physical-audit submission requirement. Do not reuse the old physical-delivery checklist merely because it remains in the older consolidation. Its transitional provision also addresses documents physically submitted before publication for the December 2025 close; qualify that fact before demanding duplicate PDFs. Transfer-pricing studies and F601 follow separate applicability rules and the amended transmission provisions, which this ordinary-company guide does not qualify in full.

### Keep each extension tied to its close and obligation

| Fiscal close | Obligation | Express extension | Official source |
| --- | --- | --- | --- |
| 31 December 2025 | IUE return and payment | 4 May 2026, correcting the original 29 May date | RND 102600000014 additional first provision and its errata. https://www.impuestos.gob.bo/wp-content/uploads/2026/04/RND-102600000014.pdf ; https://www.impuestos.gob.bo/wp-content/uploads/2026/04/Fe-de-Erratas-RND-1026000000141.pdf |
| 31 December 2025 | Specified digital financial statements, annual report, transfer-pricing study and F601, as applicable | 29 May 2026 | RND 102600000014 additional second provision. https://www.impuestos.gob.bo/wp-content/uploads/2026/04/RND-102600000014.pdf |
| 30 June 2026 | IUE return/payment and the specified digital statements/annual report/transfer-pricing information, as applicable | 30 November 2026 | RND 102600000043, sole article I-II. This is a different activity-close branch. https://www.impuestos.gob.bo/wp-content/uploads/2026/10/RND-43.pdf |

None of these rows establishes the due date for a December 2026 close. Maintain separate return, tax payment, financial-document and specialist-information entries, with extension authority and reviewer evidence. The ordinary annual-payment rule does not establish a separate instalment or provisional-payment schedule; qualify any such obligation or claim before reliance.

### Late obligations need their own computation

[Tax Code article 47](https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf) addresses omitted tax expressed in UFV plus interest and conversion at payment. Its rate stages are 4% annually through the fourth year of delay, 6% in the fifth through seventh years and 10% from the eighth year, under the article's precise periods and related DS 2993 methodology. These are not a flat percentage of the original boliviano balance. The captured extraction damages the interest formula, so this guide supplies no executable arrears formula or actual debt calculation. Verify the complete formula, day counts, partial-payment method, official UFV values and applicable relief first.

Article 165's omission fine, formal-duty penalties, articles 156-157 cure/reductions and Ley 1733 relief are distinct questions. An audit or notice still triggers R-CIT-6. The SIN page headed as an interest rate through December 2026 has body text referring to December 2016; do not use that heading to certify a current rate. No universal fixed late-filing fine or automatic relief eligibility is established here.

## Completion checklist

Before an actual engagement output, retain all universal and corporate base requirements and add these checks:

- [ ] Confirmed ordinary entity/activity/period, principal registered close and source coverage, including later amendments and any applicable incentive or sector branch.
- [ ] Required technical accounting and currency rules, UFV inputs, asset tax bases, form precision and current filing instructions are established; no source hold is treated as a factual default.
- [ ] PBT ties to the approved statements. Every source item appears once, with an adjustment/exclusion reason, source citation and reviewer flag; ordinary expenses are not deducted twice.
- [ ] Foreign-source and intercompany-distribution exclusions meet the exact conditions. Payroll, banking evidence, indirect tax recoverability, interest and asset deductions are supported.
- [ ] Ordinary losses use proven vintages and balances without indexation; the old DS article 32 wording has not replaced the later statute. Any transfer/special rule is separately qualified.
- [ ] Credits, relief and payments are established and used once, with unused amounts tracked. Required cross-border, Pillar Two, disclosure and current/deferred-tax outputs are completed under verified sources or the financial result is held.
- [ ] F500 and F605 use the correct period and package. Gross-income history is checked, including equality and persistence. Return/payment and document dates have separate current authority.
- [ ] The universal and corporate 18-check sets pass. The refusal trace includes every loaded code. All 26 corporate intake fields and mandatory content slots are resolved for the engagement.
- [ ] Produce the recalculated Excel working paper, reviewer brief, action list and review checklist, plus all corporate summary, computation, cross-border/Pillar Two, deferred-tax, supporting-schedule, reviewer-question and filing-assembly components. Preserve identifiable components if combined into fewer files.
- [ ] Workbook rows retain the universal A-L field mapping, evidence references, default/attention flags and exclusion reasons; include asset, loss, benefit/payment, currency, reporting-threshold and filing schedules. Read all reported figures from verified recalculation. Missing tools prevent delivery.
- [ ] A qualified Bolivian practitioner reviews the result before any filing or reliance. Until then, this Tier 2 guide remains `pending_review`; no professional sign-off is claimed.

Revision: v0.1, 3 November 2026, adds the ordinary IUE reference and separately labelled filing history. Hypothetical examples do not constitute a reviewed client computation.

## Sources

Only the specified units were read; a long compilation has not been reviewed in its entirety. Primary source text and its applicable amendments prevail over a simplified example or an undated portal summary.

| Source | URL | Read on and scope |
| --- | --- | --- |
| SIN, Ley 843 and DS 24051, updated 30 September 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf | 2026-11-03: IUE arts. 36-51, selected related amendment notes; DS arts. 1-4, 6-33, 35-40 and 48 as relied on above, selected ordinary asset rows in art. 22 annex. Special exemption/incentive and later remittance notes are not fully qualified; official reference compendium, not Gaceta certification |
| SIN, Ley 2492 compendium, updated 30 September 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/2.-LEY-N%C2%B0-2492-09-26-2.pdf | 2026-11-03: arts. 4-5, 8, 47 and its displayed methodology notes, selected 156-157 and 165/related DS text. Formula extraction damaged; no actual arrears method qualified |
| RND 102600000014, 16 April 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/04/RND-102600000014.pdf | 2026-11-03: full 5-page resolution, including digital package, threshold/history, extensions and repeals |
| Errata to RND 102600000014 | https://www.impuestos.gob.bo/wp-content/uploads/2026/04/Fe-de-Erratas-RND-1026000000141.pdf | 2026-11-03: full page; corrects first additional provision to 4 May and the fourth provision's cross-reference |
| RND 102600000043, 28 October 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/RND-43.pdf | 2026-11-03: full 2-page resolution; only June 2026 close extension |
| RND 101800000004, prior SIN consolidation | https://unumlex.impuestos.gob.bo/wp-content/uploads/2022/02/RND-No-101800000004-Estados-Financieros.docx-MOD3.pdf | 2026-11-03: arts. 1-3 and 8-12 for definitions, transmission period and framework; read with the 2026 amendments, not as current authority for repealed physical requirements |
| SIN/SIAT, Formulario 500 instructions | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/impuesto-a-las-utilidades-de-las-empresas/500-iue-contribuyentes-obligados-a-llevar-registros-contables | 2026-11-03: full undated live text on entities, rubros and SIAT route; not a requested-year box/rounding specification or authenticated test |
| SIN/SIAT, Actividades Económicas | https://siatinfo.impuestos.gob.bo/index.php/actividades-economicas | 2026-11-03: principal-activity fiscal-close guidance and activity groups; actual registered profile still needed |
| Ley 1733, 27 May 2026, official text | https://www.impuestos.gob.bo/wp-content/uploads/2026/05/L17332051NCPP.pdf | 2026-11-03: extracted 7-page text, arts. 1-3 and additional/final provisions; debt-relief procedure, exact numbered-column alignment and implementation remain outside qualified computation |
| SIN, debt-relief extension notice, 16 September 2026 | https://www.impuestos.gob.bo/index.php/nota_prensa/el-gobierno-amplia-el-plazo-de-regularizacion-tributaria-hasta-el-31-de-diciembre-de-2026/ | 2026-11-03: full substantive notice identifying DS 5708; its operative instrument and actual claimant eligibility are not qualified here |

**Not yet confirmed:** Complete requested-period Gaceta/amendment chain; operative SIN-approved technical accounting standards and all UFV/FX series and transformations for an actual computation; exact form boxes/rounding, holiday calendar and December 2026 close's 2027 filing instructions; banking-evidence implementation; shareholder-loan benchmarks and foreign LIBOR successor treatment; actual exemption/donation, bad-debt, incentive and special-sector eligibility; branch/outbound withholding and treaties; credits, instalments, carryback, group relief, loss-transfer/ownership restrictions, CFC/hybrid and Pillar Two status; complete formal penalties, undamaged interest/partial-payment formula, limitation and debt-relief procedures and DS 5708 implementation; falling-income reporting transitions; a named Bolivian professional's review of this version. Resolve every applicable required item before a financial result; do not treat this list as evidence that a regime is absent.

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
