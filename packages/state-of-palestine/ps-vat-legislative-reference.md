---
name: ps-vat-legislative-reference
description: >
  Source-limited reference for selected VAT provisions in Palestinian
  Decree-Law 26/2024 and its 2026 amendment. Records the stated rate,
  ordinary goods and service tax points, input-tax conditions, registration,
  reports and changed administrative powers, with 5 hypothetical positions.
  Holds later law, applicable rates, territorial administration, prescribed
  forms, currency and precision before any actual calculation or filing.
  Tier 2 draft for professional review; incomplete as an operational skill.
jurisdiction: PS
category: international
tax_year: 2026
tax_year_notes: "Selected provisions of Decree-Law 26/2024, Gazette special issue 30 of 31 December 2024, and complete Decree-Law 11/2026 in a university-hosted gazette extract were read. The official catalogue displays commencement of the parent on 30 June 2025 and the amendment on 13 June 2026. Later instruments, actual territorial administration, prescribed forms and operational currency/precision remain unresolved. This is a dated legislative reference, not complete 2026 VAT or country coverage."
tier: 2
last_updated: 2026-11-02
version: 0.2
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Palestine VAT Legislative Reference (v0.2)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Load with `workflow-base`. This reference uses PS for the State of Palestine catalogue area. It makes no sovereignty or recognition determination. **It is incomplete as an operational country skill.** Its dated source explanations and hypothetical arithmetic do not establish an actual liability, refund, return or payment instruction.

Unknown law or administration is **HOLD**. A professional review flag cannot replace an operative source. Keep unresolved numeric fields unknown rather than zero and stop the affected calculation.

This is the selected dated reference described in the source and period records below. Actual work remains subject to its complete companion, source conditions, refusal gates and professional review.

### Period, territory and excluded obligations

S1 Art 124 says the law operates 6 months after publication. Its issue is dated 31 December 2024; S3 displays 30 June 2025. S2 Art 12 operates from issue, dated 13 June 2026, whilst Gazette 239 is dated 25 June 2026. Keep issue, publication, commencement and retrieval dates separate. Do not use the June publication date as S2's stated commencement or independently invent a month-counting rule.

For an engagement, establish the applicable territorial authority, legal and practical administration and the taxpayer's registration. **No conclusion is made about who currently assesses or collects in Gaza, or that this national text settles Gaza's operative regime.** Do not infer a general exemption, uniform administration or a retrospective liability from this reference.

Income tax, payroll, social contributions, customs, company formation, accounts and property taxes require separate guides. Financial institutions, non-profit institutions, exempt dealers, imports, exports, electronic and non-resident services, reverse-charge cases, real estate, construction, used-goods margins, related-party pricing, concessions and transitions require their complete applicable rules. They are excluded from these ordinary illustrations. Silence does not establish exemption.

### Source conditions before preparation

1. Obtain the operative law for the requested dates, authenticate S2's operative text and establish any amendments after it. Reconcile S1 and S2 at the article level.
2. Establish the actual collector and competent authority for the location, taxpayer, registration and transaction. An address, website or portal label is insufficient.
3. Obtain applicable Cabinet decisions and compatible continuing instructions. **S1 Art 2(2) permits the Cabinet, on the Minister's recommendation, to change or differentiate rates up to the Art 2(1) rate.** Art 2(3) also permits specified lump-sum regimes for small professions/services. The 16% printed in Art 2(1) is not an established universal current rate.
4. Check the 1985 accounting-books regime and the continuing instructions under Art 121. That article preserves prior instructions and decisions only so far as compatible; Art 123's repeals do not establish that all previous administration disappeared.
5. Establish classification, value, tax point, invoice and deduction eligibility, reporting period, accepted currency, conversion and precision. Obtain the currently approved forms and directions.

If any necessary condition is unresolved, fire `R-PS-SOURCE`, `R-PS-ADMIN` or the affected subject refusal before applying a rate or determining an actual amount. A factual profile confirmation cannot waive a source hold.

## Ask the client first

1. What obligation and period are requested, and is the work a dated source explanation or an actual engagement?
2. Which person, entity, residence, territorial and establishment facts determine the applicable scope?
3. Which activities, transactions, units, values and event dates are supported by redacted records?
4. Which operative sources, classifications, exemptions, amendments and case-specific decisions have been established?
5. Which prior-period, eligibility, input, deduction, credit, payment and other-component records affect this job?
6. Which complete companion content, professional reviewer, current forms and filing or collection directions are available?

### Intake, defaults and execution

Infer the requested obligation, period, location and administering authority, taxpayer and registration category, activities, counterparties, supply/delivery/payment dates, contract price terms, invoice/document dates, transaction values, input use and correction history. Confirm missing essential facts together at universal Step 4. Retain redacted stable source references; the reviewer keeps names, identifiers, credentials and payment details needed for administration.

Request the applicable law and directions, registration certificate, transaction contracts and invoices, delivery evidence, source ledgers, import or approved documents where relevant, prior reports and credits, written exemptions/extensions and prescribed forms. Reconcile every source item once; record exclusions and duplicates. Never infer registration or tax treatment solely from a bank narrative.

For ordinary established positions, calculate by source line and reconcile output, eligible input and totals. Keep status, rule, period, source, calculation and reviewer action with every position. Unresolved legal or administrative matters stop that branch; only factual ambiguity can be answered through the universal Step 6.5 process.

Permitted preparation defaults concern presentation only: retain source precision, keep uncertain classifications in HOLD and use stable redacted references. No default rate, exemption, input percentage, effective date, currency, exchange rate, deadline extension, form box or rounding method can replace missing authority.

## The method, step by step

### Dated ordinary rate [S1](https://info.wafa.ps/files/pdf/c279536c-71e8-4bae-9a2f-489631996b5e.pdf)

| Component and conditions | Amount | Reference period and limit | Source |
| --- | --- | --- | --- |
| Independently established ordinary standard-rate position under the selected parent provisions; actual applicable rate and every source condition remain held | 16% of the established tax-exclusive value | Selected dated legislative reference, including the retained 2026 amendment; no actual liability established | https://info.wafa.ps/files/pdf/c279536c-71e8-4bae-9a2f-489631996b5e.pdf |

### Selected rules and their boundaries [S1](https://info.wafa.ps/files/pdf/c279536c-71e8-4bae-9a2f-489631996b5e.pdf) [S2](https://maqam.najah.edu/media/uploads/2026/06/legislations/%D8%A7%D9%84%D8%B9%D8%AF%D8%AF_239_%D9%84%D9%84%D9%86%D8%B4%D8%B1-7-10.pdf)

#### Charge, value and tax point

- **Stated charge:** S1 Art 2(1) prints 16% on transactions in the state and imported goods, subject to the powers and source conditions above.
- **Ordinary transaction value:** Art 7 distinguishes property and service consideration. Property value includes specified compulsory payments and execution expenses, including commissions and interest. Combined property/service consideration must be separated on the invoice. Do not calculate on a bank deposit without reconciling the legally relevant consideration.
- **Advertised price:** Art 7(5) treats a presented or advertised price as tax-inclusive unless exclusion is expressly stated. A tax-inclusive amount cannot be multiplied by 16% as though it were a tax-exclusive base.
- **Place:** Arts 14–16 contain different property, intangible, service and financial-activity tests. A customer's address alone is not a complete place-of-supply analysis. Cross-border and special cases remain outside this method.
- **Liable person:** Art 17 identifies the seller for sales and service provider for services. This does not displace the special buyer, non-resident or electronic rules elsewhere.
- **Ordinary goods:** Art 26 links tax to delivery or placing goods at the buyer's disposal; staged delivery is addressed by the part delivered.
- **Ordinary services:** Art 28(1) uses receipt of consideration or completion, whichever is earlier, with staged-service provisions. Art 28(2) treats specially related pricing separately. Do not use an invoice or cash date as a universal tax point.
- **Special timing:** Arts 27 and 29–31 concern consignment, personal consumption, imports and construction. Do not force them into an ordinary-goods example.

The exemption and zero-rate schedules are not qualified in full here. Do not classify a supply as standard-rated merely because this reference does not identify its exemption.

#### Input tax and a credit position

S1 Art 36(1) permits deduction from tax due for input tax in an invoice issued for the operator, an import declaration or another approved document, subject to its stated documentation and naming requirements. It requires deduction within 6 months of the document's issue and states that it cannot be carried to the following financial year. Resolve the provision's application to the particular document and any credited balance before use. Do not turn 6 calendar months into 180 days or assume an accounting year.

Art 36(2) prohibits deduction for inputs used in exempt transactions. Art 36(3) has a distinct agricultural-manufacturing documentation provision. Arts 38–45 contain pre-registration, correction, land, gifts, vehicles, mixed-use, hospitality and employee-expense qualifications. A supplier invoice alone does not establish deductibility.

For an already established ordinary position, retain output tax and each eligible input item separately, then subtract established eligible input tax. A negative arithmetic result is an **illustrative excess of input over output**, not an approved refund or permission to carry a balance.

Art 37(1) describes a written-request refund where input tax exceeds tax on transactions in the same reporting period, with a stated 60 **working day** period. The complete Art 37 also contains temporary-assessment, audit, investigation, indictment, settlement, accounting-book and time-bar conditions. It does not promise every credit is paid in 60 calendar days. No refund date, right, claim or carry-forward is determined by this guide.

#### Registration and invoices

Art 61(1) requires a person wishing to conduct business to register with the competent tax department. Art 61(4) provides an exempt-dealer registration category, excluding liberal professions, where the defined turnover does not exceed JOD 20,000 or its equivalent in legal circulating currency, or another amount determined under the law. **This is not a general no-registration threshold.** Art 1's turnover definition concerns prior-year transactions and excludes sale of fixed assets and equipment. Neither a current threshold nor a currency-conversion rate is established here; related protocol and implementing instruments remain unqualified.

Art 62 provides for a registration certificate identifying category and activity. Registration, temporary registration, grouping, change and cancellation are not interchangeable. S2 Art 6 replaces Art 69: the **Director-General** may register outside-state residents seeking to conduct business within it under conditions and guarantees set by Ministerial instructions. This does not remove Art 68's separate resident-agent provisions or establish an online registration procedure.

Arts 49–54 address invoice issue, timing, purchase evidence and correction. Art 49(1)'s form authority becomes the **Minister** under S2 Art 3(1). Art 50(1) states 14 days from the tax-charge time for a tax invoice; its second paragraph has a specific exception. Correction or cancellation is not an automatic permission to erase recorded tax. Current formats and correction directions are missing. No invented invoice fields or submission format is supplied.

#### Reports, payment and current form authority

- Art 75(1) requires monthly reporting from registration within 15 days of the following month, including inactivity. Art 75(3) permits a time-limited reporting exemption on conditions.
- Art 75(4) covers the first partial month. Art 75(5) permits a Director-approved temporary estimated report once in the financial year, followed by a final report within 30 days.
- Art 75(6) permits specified reporting postponements. The actual direction and its effect must be established; do not assume a reporting postponement also postpones payment.
- Art 75(7) requires totals by transaction/tax type and input-tax categories, including exempt transactions. Art 75(8) has a separate occasional-transaction report. Art 76 requires a supplementary report for omitted data.
- S2 Art 2 removes the Commissioner-General recommendation wording in Art 75(9). Electronic reporting still depends on the applicable Ministerial instructions.
- Art 79 requires specified records to be retained for 5 years. Other litigation, investigation or preservation duties were not qualified; this is not a destruction instruction.
- Art 89(1) requires collection and remittance when the periodic or temporary report is submitted. Other Art 89 paragraphs address imports, determinations and objection decisions separately.
- **Amended Art 118:** under S2 Art 10, the Director-General determines forms, electronic reports, accounting-book formats and other records after Ministerial approval; the Minister may issue instructions for their use. The actual approved models and box instructions were not obtained.

S2 also replaces Art 84 on objections and Art 96 on precautionary seizure. Its Art 84 includes payment of undisputed tax and a period for the committee to decide, not a new general time limit for lodging every appeal. This guide supplies no objection, enforcement, penalty, settlement or litigation procedure. Obtain the complete interacting rules before advice or calculation.

## Boundary and exception table

Apply every source-specific condition in the method and retained source library. Unknown law, classification or administration remains HOLD; no presentation default resolves it.

## Worked cases

### Hypothetical worked positions

The 5 examples assume an independently established ordinary standard-rate position to which 16% applies, correct tax points and value, and, where present, fully eligible same-period input tax satisfying every applicable documentary, registration, time and use condition. None resolves the source conditions above.

**CU** means a hypothetical common currency unit for arithmetic only. It is not a statutory reporting or payment currency. All arithmetic is exact at the displayed precision; no legal rounding rule is assumed. No real taxpayer, portal or bank data is used.

| Position | Complete arithmetic | Result and boundary |
| --- | --- | --- |
| 1. Expressly tax-exclusive ordinary supply, 1,000 CU; no input claim | `1,000 × 0.16 = 160.00`; `1,000 + 160 = 1,160.00` | 160 CU illustrative output tax and 1,160 CU gross. The classification and rate are assumptions, not findings |
| 2. Ordinary output with established eligible input tax | `5,000 × 0.16 = 800.00`; `800 - 320 = 480.00` | 480 CU illustrative output less input. The 320 is an already established eligible amount, not an inferred deduction from a payment |
| 3. Tax-inclusive ordinary price, 1,160 CU | `1,160 ÷ 1.16 = 1,000.00`; `1,160 - 1,000 = 160.00` | 1,000 CU base and 160 CU tax. Art 7(5) prevents treating the same inclusive price as an exclusive base |
| 4. Eligible inputs exceed ordinary output | `500 × 0.16 = 80.00`; `80 - 120 = -40.00` | 40 CU arithmetic excess of inputs; no refund, carry-forward, expiry or payable amount is determined |
| 5. Two reconciled ordinary lines and two eligible input items | `1,000 × 0.16 = 160.00`; `500 × 0.16 = 80.00`; `160 + 80 = 240.00`; `64 + 32 = 96.00`; `240 - 96 = 144.00` | 144 CU combined illustration. Retain both output and input lines. This does not permit combining taxpayers, registrations or periods |

If an input document is for an exempt transaction, the ordinary examples cannot turn it into a credit. If the price, tax point, registration, period, document, rate, currency or precision is unresolved, determine no actual amount. Use the relevant refusal.

### Recompute the retained hypothetical positions

The following blocks recompute 2 of the positions above using exactly their supplied premises. They are separate arithmetic exercises. The original classification, period, source, currency, precision and operational holds remain applicable. A nil or negative arithmetic component does not resolve an unknown liability or establish an exemption, refund or amount to pay.

```oa-check
name: PS position 1 assumed exclusive ordinary supply in CU
inputs:
  value: 1000
  rate: 0.16
steps:
  - output: value * rate
  - gross: value + output
expected:
  output: 160
  gross: 1160
tolerance: 0.000001
```

```oa-check
name: PS position 4 arithmetic input excess without refund inference
inputs:
  value: 500
  rate: 0.16
  eligible_input: 120
steps:
  - output: value * rate
  - output_less_input: output - eligible_input
expected:
  output: 80
  output_less_input: -40
tolerance: 0.000001
```

## When to refuse or refer

### Refusals

Retain every universal refusal. Add these topic-specific controls:

| Code | Trigger | Verbatim message |
| --- | --- | --- |
| `R-PS-SOURCE` | Operative source, authenticated amendment, later instrument, applicable rate or transition is unresolved | 'The operative VAT source chain for this position is not established. I can explain the dated reference, but I cannot determine an actual amount until the applicable authority is established.' |
| `R-PS-ADMIN` | Territorial authority, actual collector, registration or administration is unresolved, including a Gaza case | 'The competent VAT administration for this location and taxpayer is not established. I cannot infer it from the national text, an address or a portal.' |
| `R-PS-CLASS` | Place, person liable, exemption, zero rate, special regime, value or tax point is not established | 'This reference does not establish the requested supply treatment. Obtain the complete applicable classification and timing rules before calculation.' |
| `R-PS-INPUT` | Input eligibility, document, use, registration timing, time limit, financial year or credited-balance treatment is unresolved | 'The requested input-tax deduction is not established. I cannot treat an invoice or payment alone as an eligible credit or invent a carry-forward.' |
| `R-PS-REFUND` | Actual refund, objection, assessment, penalty, enforcement or litigation is requested | 'This reference supplies no complete refund or dispute workflow. I need the interacting operative provisions and administrative directions before preparing that position.' |
| `R-PS-FILING` | Reporting/payment instruction, approved form, electronic format, deadline direction or correction method is unresolved | 'The current reporting and payment instructions are not established. I cannot invent a form, box, extension or submission-ready output.' |
| `R-PS-PRECISION` | Actual currency, conversion, measurement or rounding is unresolved | 'The accepted currency, conversion or precision rule is not established. Hypothetical CU arithmetic cannot become a statutory reporting amount.' |

## Filing and payment

Actual filing, submission, payment and collection remain subject to the specific source conditions, complete companion content and refusal gates in this reference. Use the retained dated administration and form comparisons for explanation; they do not supply missing current directions or authorise an external action.

## Completion checklist

Current format revision: v0.2, edited 2 November 2026. This migration preserves the earlier draft's dated source content and revision records. It does not refresh law or confer professional review. Carry all outstanding source and operational holds through the working paper, reviewer brief, action list and review checklist.

### Output and self-check additions

When source conditions are satisfied, extend all 4 universal logical components: working paper, reviewer brief, action list and review checklist. Do not deliver a return or payment file from these illustrations. A HOLD output identifies the missing source and next evidence needed, with unresolved amounts left unknown.

The working paper retains source-line links, taxpayer/registration and period partitions, value inclusivity, supply/tax dates, rate authority, output/input distinctions, document/use/time tests, current amendment mapping, source precision and every refusal. The reviewer brief explains unresolved law and the limits of translations. The action list identifies forms, directions and factual evidence still needed without requesting unnecessary identifiers.

Before delivery verify:

1. The exact applicable period, location, authority and registration are established.
2. S2's amendments are applied; repealed Art 119 and the removed definition have not supplied current authority.
3. The 16% reference has not displaced Cabinet powers, later rates or a special regime.
4. Every source item appears once; all exclusions and unknown values are explicit.
5. Value inclusivity, place, person liable and tax point are independently supported.
6. Each input satisfies the applicable evidence, use, registration and time conditions; 6 months has not become 180 days.
7. Output less input reconciles without manufacturing a refund or carry-forward.
8. Reports, payment, formats, deadline directions and precision have operative sources; no illustrative CU flows into filing fields.
9. All calculations recalculate, source references resolve and HOLD positions remain held.
10. The professional reviewer and every universal check/refusal remain in place.

### Topic reference map

This maps partial topic coverage. It is not the mandatory companion-skill contract in workflow-base Section 7 and does not claim operational completion.

| Topic lens | Evidence here | Remaining condition |
| --- | --- | --- |
| 1. Year and residence | Stated enactment dates; Art 1 definitions | Actual VAT periods, income-tax residence cross-reference and territory/administration |
| 2. Income and deductions | VAT value and selected input-tax rules | Income-tax treatment outside scope |
| 3. Rates | Art 2 stated 16% and Cabinet powers | Applicable current rate, special regimes and directions |
| 4. Reliefs and credits | Selected Arts 36–45 and held refund | Complete exemption/zero schedules, eligibility and implementation |
| 5. Category/source treatment | Selected ordinary supply rules | Complete special, financial, non-profit and cross-border treatment |
| 6. Documentation | Invoices, registration and records | Current approved models, directions and source completeness |
| 7. Calculation | 5 conditional ordinary illustrations | Actual classification, eligible inputs, currency and precision |
| 8. Contributions | None | Separate social/payroll sources and content |
| 9. Patterns | Reconciliation and stable source references | Qualified transaction data and classifications |
| 10. Filing | Selected monthly report and payment provisions | Administration, form, box, electronic and deadline directions |
| 11. Refusals | 7 topic-specific gates plus universal controls | Apply all, without waiving unknown law |
| 12. Precision | Exact hypothetical arithmetic only | Authorised currency, conversion and rounding |
| 13. Examples | 5 hypothetical positions | No actual liability or filing acceptance |

## Sources

The table records the original reading evidence. A retrieval or capture is not a reading date. A reading bound is not an exact day. The retained library below controls extent, host, translation and source qualifications; formatting adds no new legal-source reading.

| Source | URL | Read on |
| --- | --- | --- |
| S1. Decree-Law 26/2024, VAT | https://info.wafa.ps/files/pdf/c279536c-71e8-4bae-9a2f-489631996b5e.pdf | Exact reading day unrecorded; specified complete units read |
| S2. Decree-Law 11/2026, amending Decree-Law 26/2024 | https://maqam.najah.edu/media/uploads/2026/06/legislations/%D8%A7%D9%84%D8%B9%D8%AF%D8%AF_239_%D9%84%D9%84%D9%86%D8%B4%D8%B1-7-10.pdf | Exact reading day unrecorded; complete university-hosted 4-page extract read and image-checked |
| S3. Official parent-law catalogue card | https://mjr.ogb.gov.ps/Decrees/Details/33829/ | Exact reading day unrecorded; complete catalogue card read in independent public-browser check |
| S4. Official amendment catalogue card | https://mjr.ogb.gov.ps/Decrees/Details/34270/ | Exact reading day unrecorded; complete catalogue card read in independent public-browser check |

### Scope and source library

The narrow illustrative method concerns ordinary supplies whose standard-rate classification, taxable value, tax point and eligible input tax have already been independently established. It does not classify every supply or establish that the stated 16% applies to an engagement.

| Source | Qualified reading | Limits |
| --- | --- | --- |
| **S1. [Decree-Law 26/2024, VAT](https://info.wafa.ps/files/pdf/c279536c-71e8-4bae-9a2f-489631996b5e.pdf), Gazette special issue 30, 31 December 2024** | Fresh official WAFA-hosted issue: 581,198 bytes, SHA256 `29eda2aa6b614daee463dcfe3d4a9524edfca529f30b87d0f7e5356da6d9d6bb`, verified TLS, matching the earlier retained issue. Complete relied units read in native text: Art 1, Arts 2–8, 14–17, 26–31, 35–61, 62–69, 71–80, 88–90 and 119–124. Relied unit boundaries and the precise image checks are stated below. | The 72-page issue and 124-article law were not read in full. Other laws and cross-references were not qualified. The source contains extraction artefacts; the original images control. Arabic-to-English readings are working translations requiring qualified review. |
| **S2. [Decree-Law 11/2026, amending Decree-Law 26/2024](https://maqam.najah.edu/media/uploads/2026/06/legislations/%D8%A7%D9%84%D8%B9%D8%AF%D8%AF_239_%D9%84%D9%84%D9%86%D8%B4%D8%B1-7-10.pdf), Gazette 239, 25 June 2026** | Complete 4-page gazette extract, recitals, Arts 1–12 and signature read in native text and against all 4 page images. Fresh copy: 211,942 bytes, SHA256 `efaf5393f056cdc3e843016575bc103eb1e1c8ca146aa8d76f0b26945265d108`, verified TLS. Art 12 says effective from issue; signature is dated 13 June 2026. | University-hosted copy. The official catalogue links a PDF, but the original server returned a challenge on the initial request and the single permitted recovery attempt. No original-server PDF hash or complete Gazette 239 was obtained. Do not silently equate transport from this host with official-server authentication. |
| **S3. [Official parent-law catalogue card](https://mjr.ogb.gov.ps/Decrees/Details/33829/)** | Independent read-only source check read the complete card through the public browser route, HTTP 200: parent labelled in force/amended, commencement 30 June 2025 and S2 listed as an amendment. | No retained body hash. A catalogue card is evidence of the publisher's record, not an exhaustive later-law or territorial-enforcement check. |
| **S4. [Official amendment catalogue card](https://mjr.ogb.gov.ps/Decrees/Details/34270/)** | Independent read-only source check read the complete card through the public browser route, HTTP 200: DL 11/2026, Gazette 239, issue and commencement 13 June 2026, labelled in force. | Same catalogue and retention limits as S3. Current local collection practice was not established. |

S1's complete relied units are on PDF pp 31–35, 37, 40–41, 44–55, 58 and 70–71, printed pages 2 fewer. Original images were checked for pp 31–35, 37, 40–41, 44–45, 50, 54–55, 58 and 70–71. Native text on pp 46–49, 51–53 supplies the named complete units there; their images were not separately checked. Only Art 26 is relied on from p 40; Art 24 starts on p 39, which was read, but its property regime is excluded. Only Arts 27–31 are relied on from p 41; Art 32 continues beyond that page and is not a qualified zero-rate schedule here. Art 70 starts on p 52 and continues on p 53; it was incidentally read but is not used to determine a registration change.

**Correction control:** S1's Art 1 definition of Commissioner-General of Revenues and old administrative references cannot be used unchanged after S2. S2 Art 2 removes that definition; Arts 2–5 redistribute or remove specified powers, Arts 6–10 replace particular operative provisions and Art 11 repeals S1 Art 119. An older consolidated-looking text is not sufficient without these amendments.

### Remaining evidence and review

The official original of S2, complete later-law and Cabinet/Ministerial instructions, compatible earlier directions, 1985 accounting-books regime, full exemption/zero schedules, special regimes, actual territorial enforcement, Gaza collector, current forms and electronic submission, accepted currency, exchange method and rounding were not established. Protocol and other cross-border instruments were not qualified. Penalties, appeals, enforcement and actual refund/carry-forward consequences remain outside preparation scope.

A professional must check the Arabic readings, source identity and every operative dependency before reliance. Tier 2 pending_review status does not establish accountant verification, comprehensive country coverage or filing readiness.

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
