---
name: va-customs-fees-reference
description: >
  Source-limited reference for Vatican City Law X of 22 August 2025,
  selected customs administration fees in Table V and 5 hypothetical
  component calculations. Separates import and invoice-certification
  charges from Italian VAT, preserves exemptions and current-law gaps
  and refuses actual preparation without a complete companion.
  Tier 2 draft for review; incomplete as an operational country skill.
jurisdiction: VA
category: international
tax_year: 2025
tax_year_notes: "Law X is dated 22 August 2025. Article 11 states entry into force on 1 September 2025, subject to specific application dates; Article 8 applies Table V from 1 December 2025. The original was retrieved on 31 October 2026 UTC. Retrieval is not a legal currency date. Later ordinances, exemption decisions, administration, underlying customs/VAT eligibility and actual assessment remain unresolved."
tier: 2
last_updated: 2026-11-02
version: 0.2
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Vatican City Customs Administration Fees Reference (v0.2)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Load with `workflow-base`. This is a dated reference within the **VA, Holy See** catalogue area. Its source is a law of the **State of Vatican City**. Those labels do not make every Holy See entity, person or transaction subject to identical treatment. **This reference is incomplete as an operational country skill.** It supports source explanations and the stated hypothetical components, not an actual liability, invoice, declaration, exemption, VAT treatment or payment.

Unknown law, an unresolved source condition or an incomplete mandatory companion slot is **HOLD**, before actual classification or calculation. Professional review cannot replace missing law.

This is the selected dated reference described in the source and period records below. Actual work remains subject to its complete companion, source conditions, refusal gates and professional review.

## Ask the client first

1. What obligation and period are requested, and is the work a dated source explanation or an actual engagement?
2. Which person, entity, residence, territorial and establishment facts determine the applicable scope?
3. Which activities, transactions, units, values and event dates are supported by redacted records?
4. Which operative sources, classifications, exemptions, amendments and case-specific decisions have been established?
5. Which prior-period, eligibility, input, deduction, credit, payment and other-component records affect this job?
6. Which complete companion content, professional reviewer, current forms and filing or collection directions are available?

### Intake and output extension

Ask once for obligation and period, explanation versus preparation, reviewer and complete companion, person/entity category, event and location/property, applicable sources/later provisions, exemption decision, goods/service category, origin, verified value/weight, origin documents or assessment, invoice basis, charge unit, other components and collection instructions. Use redacted references. Do not request identity documents, tax identifiers or bank details for these exercises.

The universal 4 logical outputs remain mandatory when a complete companion and all gates permit an engagement: working paper, reviewer brief, action list and review checklist. Extend the working paper with anonymous source ID, event, beneficiary/scope basis, source/table/date, exemption decision, item/category, base evidence, confirmed unit, exact arithmetic, rounding authority, component, other charges, reconciliation, Needs Input/refusal and reviewer flag. Use formulas for permitted calculations.

The brief must distinguish fees from VAT, State/Holy See scope, exemptions and exceptions, A/F/O interactions, currentness, valuation, rounding/aggregation, expenses and operational holds. Carry the same conditions into the action list and checklist. Before computation, a refusal produces only its message and scope trace. This guide authorises no contact, application, declaration, submission or payment.

## The method, step by step

### Stated figures and bases [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf)

The law calls these **diritti di segreteria**, described here as administration fees. This is not a finding about tax classification in another system. Invoice-certification percentages are not Italian VAT rates; payment does not establish eligibility for Italian VAT non-imposition. The underlying customs convention, treaty privileges and Italian VAT rules remain unqualified. [S1, Arts 1, 8; Table V]

| Table V component | Figure and literal base | Condition retained |
| --- | --- | --- |
| **A. Goods imports** | **4%** of value shown by origin documents or, failing those, official assessment | Establish the import, value evidence, Article 2 exemptions, relocation exception and O interaction. No substitute invoice base or general 4% import-tax conclusion.  [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf) |
| **A. Postal parcel from abroad** | **EUR 2 fixed** for effects of use, haberdashery and objects up to EUR 50; goods above EUR 50 refer back to A's charges | Not a universal EUR 50 exemption. Category, value, parcel unit and O remain material. This overlapping postal case is not calculated here.  [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf) |
| **F. Listed goods** | **2%** of amount indicated in invoice | Complete list and exclusions below.  [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf) |
| **F. Italian bills for water, gas, electricity and telephone** | **1%** of amount resulting in invoice | Establish an eligible Italian bill; no extension to every utility or telecommunications service.  [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf) |
| **F. Registered movable goods, beni mobili registrati** | **5%** of amount resulting in invoice | Establish legal classification, not merely a bookkeeping asset-register entry.  [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf) |
| **F. Other goods/services subject to VAT in Italy and not contemplated in F** | **4%** of amount indicated in invoice | Both residual conditions apply. Distinct from A's 4% import charge.  [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf) |
| **O. Small imports of non-Italian-origin goods** | **EUR 12 fixed** instead of charges in preceding letters, where value is up to EUR 100 **and** weight up to 10 kg | Both conditions must exist. Origin is not merely shipment address. Do not mechanically add EUR 12 to A or ignore replacement wording. A/F/O and postal interactions remain held.  [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf) |

F's **2%** list is foodstuffs, cleaning materials, household-use objects **excluding appliances**, medicines and medical materials, books, magazines, paper, cardboard, printing ink **including toner**, printing work, stationery, worship objects and religious articles **excluding medals and souvenirs**, furniture and construction materials **including sanitary fittings**. Preserve each inclusion and exclusion. A broad household, medical or religious label is insufficient classification evidence. [S1, Table V(F), p 16]

F concerns invoice validation and certification for goods and services **ai fini della non imponibilità dell'IVA**. This records source wording, not eligibility, Italian supplier obligations, an invoice's tax basis or permission to omit VAT. Fee and VAT analysis require separate established authority. [S1, Table V(F), pp 16–17]

A and F each state upward rounding to the euro. The hypothetical examples use mathematical ceiling of **one already established fee component** to a whole euro. This short source wording does not establish every line, invoice, consignment, aggregation, credit or adjustment unit. Resolve the applicable unit and instructions before actual preparation. Do not round the input value or impose a blanket cent rule. [S1, Table V(A), p 15; F continuation, p 17]

### Conditional method [S1](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf)

1. **Establish content and sources.** Require a complete applicable workflow-base Section 7 companion, operative law, later table/collection changes and resolved period before actual preparation. This reference alone does not pass that gate. Unknown law produces Needs Input or refusal before classification.
2. **Separate events and scope.** Distinguish import A from invoice certification F. Establish person/entity, property, territory, activity, exemptions and decisions, relocation and special-entry interactions. Never infer VAT eligibility from a fee.
3. **Establish base and unit.** Retain origin documents or assessment for A, applicable invoice amount for F and confirmed assessment/aggregation unit. An unknown base, mixed category or unresolved VAT-inclusive/exclusive basis is held.
4. **Apply established categories.** Preserve F's complete list and exclusions. Residual 4% is not a default for unknown classification. Resolve O and other components before any whole-account output; missing charges are not zero.
5. **Reconcile permitted amounts.** Retain exact arithmetic, applicable upward-euro treatment, component and authorised adjustments separately. Reconcile to assessment/invoice. Establish current forms, collection route, collector, timing, FX, refunds and penalties before payable or filing output.

## Boundary and exception table

### Scope, exemptions and other components

Article 1 concerns specified Governatorate acts, documents and services, and goods introduced with customs and tax exemption into Vatican City and the zones referred to in Lateran Treaty Articles 15 and 16 and later agreements. It does not establish every beneficiary or privileged property, or a general exemption for business with the Vatican. The underlying treaty, 1930 customs convention and later agreements remain dependencies. [S1, Art 1, pp 1–2; Art 8, p 5]

Article 2 distinguishes:

- Acts in the direct interest of the Supreme Pontiff and for organs of the State of Vatican City, exempt under paragraph 1.
- Acts in the direct interest of Cardinals and organs of the Holy See, exempt under paragraph 2 from Articles 5, 8 and 9, **saving Table V(C), (O) and (N)**. Keep those exceptions and the distinct beneficiaries.
- Possible permanent or temporary exemption for acts in the interest of other institutions/entities by a specific presidential administrative provision. No such decision is supplied here. [S1, Art 2, p 2]

A separately exempts **A's charge** for used goods belonging to persons moving from abroad to Vatican City or qualifying privileged properties because of office, study or service. Used condition, ownership, residence or religious destination alone does not establish all conditions. Obtain the actual move, person, goods and destination evidence and applicable law. [S1, Table V(A), p 15]

Other Table V entries concern temporary export, customs operations, handling, railway, documents, lifting, official travel costs, packing, post, administration and export declarations. They are not converted into a whole-account method here. The final note says charges **other than F** are due in addition to any reimbursement of actual expenses for their operations. That exception to this note does not establish that every possible other cost of an F transaction is zero. [S1, complete Table V, pp 15–18]

General exemptions, commercial activities, special entries and later provisions require authoritative interpretation in an actual case. No automatic exemption, fee compounding, tax credit, deduction, refund, penalty or payment deadline is supplied. A percentage component cannot finalise a whole customs account.

### Defaults and reviewer attention

| Unknown | Permitted default |
| --- | --- |
| Law, period, table, customs/VAT authority or later change | None; source or VAT refusal |
| Beneficiary, scope, privilege, exemption or decision | None; scope refusal |
| Category, origin, value, weight, invoice base or unit | None; Needs Input or base refusal |
| Other charges, precision, FX, collection, adjustment, refund or penalty | None; operational refusal |

Flag every later permitted computed position for professional review. Internal cash threshold **EUR 0** is not statutory or permission to compute. Source and scope gates take precedence. Preserve authority, choices, rejected alternatives and cash effects only where law and facts permit calculation.

## Worked cases

### Five hypothetical component positions

These are **5 fully worked hypothetical component positions**, not operational customs or VAT results. For each exercise only, assume the dated rate/category, stated EUR base and exactly 1 assessment unit are established, no exemption or special replacement applies and mathematical ceiling to a whole euro is required. Assumptions establish no actual law or facts. Other charges are outside each exercise, **not zero**. [S1, Table V(A), (F)]

| Position | Complete hypothetical input and arithmetic | Ceiling component and limit |
| --- | --- | --- |
| A. Import | Established A value EUR 101; no exemption or O replacement; `101 × 0.04 = 4.04` | Ceiling EUR 5. Not a whole import account or Italian VAT amount. |
| B. Listed-goods certification | Established F books-invoice base EUR 100.10; `100.10 × 0.02 = 2.002` | Ceiling EUR 3. No VAT eligibility conclusion. |
| C. Utility certification | Established eligible Italian water-bill base EUR 50.25; `50.25 × 0.01 = 0.5025` | Ceiling EUR 1. No classification of every utility charge or input-tax basis. |
| D. Registered-movable certification | Established F registered-movable invoice base EUR 600.20; `600.20 × 0.05 = 30.01` | Ceiling EUR 31. Legal asset classification is assumed, not proved. |
| E. Residual certification | Established F residual category, subject to Italian VAT and outside other F categories; base EUR 100.25; `100.25 × 0.04 = 4.01` | Ceiling EUR 5. No residual default for an actual unknown item. |

Keep unrounded and illustrative rounded amounts. Negative bases, credit notes, mixed invoices, disputed exemptions and unknown aggregation need applicable authority. Do not sum these unrelated positions into a payable account.

### Recompute the retained hypothetical positions

The following blocks recompute 2 of the positions above using exactly their supplied premises. They are separate arithmetic exercises. The original classification, period, source, currency, precision and operational holds remain applicable. A nil or negative arithmetic component does not resolve an unknown liability or establish an exemption, refund or amount to pay.

```oa-check
name: VA position A assumed Table V category and whole euro ceiling
inputs:
  value: 101
  rate: 0.04
steps:
  - exact_component: value * rate
  - component: ceil(exact_component)
expected:
  exact_component: 4.04
  component: 5
tolerance: 0.000001
```

```oa-check
name: VA position F books assumed category and whole euro ceiling
inputs:
  value: 100.1
  rate: 0.02
steps:
  - exact_component: value * rate
  - component: ceil(exact_component)
expected:
  exact_component: 2.002
  component: 3
tolerance: 0.000001
```

## When to refuse or refer

### Topical refusals

Load the universal refusal catalogue unchanged. These additions stop affected actual computation. They do not permit invented partial returns or defaults for missing law.

| Code | Trigger | Verbatim output |
| --- | --- | --- |
| `R-VA-COMPANION` | Actual preparation without a complete applicable Section 7 companion | 'This reference is incomplete as an operational companion. I cannot determine an actual fee or prepare filing or payment output until a complete applicable companion and its source conditions are established.' |
| `R-VA-SOURCE` | Applicable law, period, table, amendment, exemption or collection provision unresolved | 'The applicable Vatican City fee authority or period is unresolved. I cannot classify or calculate an actual charge. Obtain the operative sources and resolve the legal conditions first.' |
| `R-VA-SCOPE` | Entity, person, property, territory, transaction or exemption scope unresolved | 'The applicable scope or exemption is not established. I cannot equate the Holy See with every Vatican City body, or infer eligibility from an address or entity label.' |
| `R-VA-VAT` | Italian VAT treatment sought from the fee table alone | 'This fee table does not establish Italian VAT treatment. I cannot infer VAT non-imposition, an exemption, a tax rate or supplier obligations from payment of an administration fee.' |
| `R-VA-BASE` | Category, value, weight, origin, invoice basis, rounding or aggregation unit unresolved | 'The category, base or charge unit is not established. I cannot replace it with a residual rate, a guessed value or an assumed rounding rule.' |
| `R-VA-OPERATION` | Whole-account, assessment, forms, collection, refund, adjustment or penalty unresolved | 'The operational treatment or other charge components are unresolved. I cannot present a payable amount or completed customs, filing or payment instructions from this reference.' |

## Filing and payment

Actual filing, submission, payment and collection remain subject to the specific source conditions, complete companion content and refusal gates in this reference. Use the retained dated administration and form comparisons for explanation; they do not supply missing current directions or authorise an external action.

## Completion checklist

Current format revision: v0.2, edited 2 November 2026. This migration preserves the earlier draft's dated source content and revision records. It does not refresh law or confer professional review. Carry all outstanding source and operational holds through the working paper, reviewer brief, action list and review checklist.

### Self-check additions

1. Complete content and operative period/table evidence exist before actual preparation. Retrieval and editing dates are not legal currency dates.
2. Article 11's general date has not replaced Article 8's Table V date. Article 3 later powers remain dependencies.
3. Holy See and Vatican City beneficiaries and privileged properties are not conflated.
4. Article 2 paragraphs and C/O/N exceptions, A's full relocation conditions and O's conjunctive value/weight replacement remain intact.
5. A and F keep distinct bases/events. No fee becomes an Italian VAT rate or eligibility ruling.
6. F's complete 2% list/exclusions, eligible Italian bills, registered-movable category and residual conditions are preserved.
7. Actual rounding is supported for the charge unit. No unknown line, consignment, credit or negative-base method is inferred.
8. Other components and reimbursement are not zero or silently combined. No component becomes a whole payable account.
9. Any permitted workbook recalculates without errors; all 4 outputs agree. Source resolution, arithmetic and professional sign-off remain distinct.

### Currency and revision

Version 0.1, edited 1 November 2026. Source is Law X dated 22 August 2025, not a comprehensive current consolidation. Initial limited reference with Table V context, selected figures and hypothetical components. No actual engagement, form, assessment, VAT treatment, declaration, submission or payment tested. It does not establish comprehensive VA coverage or professional verification.

General reference only. Verify authoritative applicable law, reviewed translation and administration with a qualified professional before reliance. Unresolved conditions remain Needs Input or the refusal.

## Sources

The table records the original reading evidence. A retrieval or capture is not a reading date. A reading bound is not an exact day. The retained library below controls extent, host, translation and source qualifications; formatting adds no new legal-source reading.

| Source | URL | Read on |
| --- | --- | --- |
| S1. Law X, 22 August 2025, with tables | https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf | Exact reading day unrecorded; retrieved 2026-10-31 UTC; stated complete units read and image-checked |
| S2. General index | https://vaticanstate.va/it/stato-e-governo/legislazione-e-normativa/normativa-generale.html | 2026-10-31 UTC; bounded independent read-only check |
| S2. page 2 | https://vaticanstate.va/it/stato-e-governo/legislazione-e-normativa/normativa-generale.html?start=20 | 2026-10-31 UTC; bounded independent read-only check |
| S2. other-matters index | https://vaticanstate.va/it/stato-e-governo/legislazione-e-normativa/normativa-altre-materie.html | 2026-10-31 UTC; bounded independent read-only check |

### Scope, period and source library

The computation scope is Table V(A)'s import percentage and Table V(F)'s invoice-certification percentages. Other Table V provisions and general powers are included to prevent a component being mistaken for a whole account. Judicial, notarial, road-traffic and other administrative fee calculations are outside scope. Income tax, consumption tax, payroll, pensions, formation, reporting, property and other cross-border obligations need separate content. No general tax absence or exemption follows.

| Source | Extent actually read | Qualification and limits |
| --- | --- | --- |
| **S1. [Law X, 22 August 2025, with tables](https://vaticanstate.va/phocadownload/Legge%20X%20sui%20diritti%20segreteria%20e%20Tabelle%20Diritti%20Segreteria.pdf)** | Complete Articles 1–11 on PDF pp 1–6 read natively for context. Relied general provisions: Articles 1–3, 8 and 11; containing images pp 1, 2, 5 and 6 checked. Complete Table V, pp 15–18, read natively and against all 4 images. Other tables are not qualified for computation. | Fresh HTTPS HTTP/1.1 retrieval, verified TLS, 31 October 2026 UTC: 1,626,691 bytes, SHA256 `79aad60c737c733b67e918bde81bf1533cfc77834be691654fb08a3deb7642c7`. Officially hosted Italian text, not a separately authenticated original or current consolidation. English descriptions are working translations requiring review. |
| **S2. [General index](https://vaticanstate.va/it/stato-e-governo/legislazione-e-normativa/normativa-generale.html), [page 2](https://vaticanstate.va/it/stato-e-governo/legislazione-e-normativa/normativa-generale.html?start=20) and [other-matters index](https://vaticanstate.va/it/stato-e-governo/legislazione-e-normativa/normativa-altre-materie.html)** | Independent bounded read-only check on 31 October 2026 UTC: complete title lists of 20, 18 and 9 entries respectively and 4 narrow public searches. | Law X and tables are listed with the 22 August 2025 date. No amendment-status, operative-date or actual publication-date field established. No later amendment or implementation instrument located in that check. No raw-body hash or transport headers supplied. This is not exhaustive current-law proof. |

Article 11 states entry into force on **1 September 2025** and application from that date unless otherwise provided. Article 8 specifically applies **Table V from 1 December 2025**. Do not substitute general commencement for the table's application date. These dates describe the retained law, not continuing currency for a later engagement. [S1, pp 5–6]

Article 11 describes deposit and publication channels; the actual dates of each publication step have not been established here. Article 3 permits the President of the Governatorate to update tables, modify or suppress charges and introduce charges by ordinance, and to establish collection methods by provision where the law does not do so. Obtain applicable later instruments and period evidence before actual preparation. S2's negative result does not establish their absence. [S1, pp 2, 6]

Not yet confirmed: the complete operative chain and requested-period application, unresolved source conditions and administrative directions, exact reading days where unrecorded and professional verification. Retain every specific evidence gap, refusal and filing hold identified above.

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
