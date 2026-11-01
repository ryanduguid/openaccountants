---
name: tf-kerguelen-crozet-fishing-duty-reference
description: >
  Source-limited reference for fishing duties on toothfish, rays and grenadiers
  caught in the Kerguelen and Crozet exclusive economic zones in the 2026-27
  campaign. Records the published per-kilogram amounts, statutory ceiling,
  campaign and reporting provisions and 5 hypothetical calculations. Holds
  legal application, chargeable weight, quota adjustments, precision, assessment
  and filing until the required authority and records are established. Tier 2
  draft for professional review; incomplete as an operational country skill.
jurisdiction: TF
category: international
tax_year: 2026
tax_year_notes: "The 2026-27 fishing campaign named in A-2026-119 of 22 October 2026. Selected units of A-2026-82 of 26 August 2026 and A-2016-103 of 28 September 2016 were read. CRPM L958-2 and L958-4 to L958-6 were read in the official consolidated HTML displayed for 31 October 2026. Publication, notification, entry into force, later amendments and individual authorisations have not been fully established. This is not coverage of a general calendar or income tax year."
tier: 2
last_updated: 2026-11-01
version: 0.3
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kerguelen and Crozet Fishing Duty Reference, 2026-27

Load with `workflow-base`. This reference records selected fishing-duty sources for the French Southern Territories catalogue area, TF. **It is incomplete as an operational country skill.** The examples are hypothetical arithmetic, not assessments or payment instructions. Establish the source conditions below before an engagement calculation. An unresolved condition is **HOLD**, with no liability, payable amount or completed filing output determined.

## Scope and period

The narrow scope is the duty on quantities of légine australe (*Dissostichus eleginoides*), the rays named in A-2026-119 and grenadiers (*Macrourus* spp.) caught in the exclusive economic zones off Kerguelen and Crozet for the 2026-27 campaign. Retain the scientific identity and the exact zone in the records. A common fish name alone does not establish the legal species category.

This guide does not cover fishing in other TAAF waters, Saint-Paul and Amsterdam, the Îles Éparses, Adélie Land, Clipperton or other countries. It does not authorise fishing, establish quota entitlement or provide the full fisheries, environmental, export or vessel-compliance regime. Income tax, contribution directe territoriale, payroll, social contributions, VAT, customs, tourist and mooring levies, company formation and financial reporting need separate content and sources. Silence here establishes no exemption.

The levy order is dated 22 October 2026 and names the 2026-27 campaign. The technical order's Art 8(1) states a campaign from 1 September to 31 August of the following year, with gear out of the water and sectors declared free before 31 August at 23:59. Its footnote specifies UTC+4. Art 8(2) also requires a Kerguelen closure period, with exact dates in annual authorisation decisions. These are fishing-calendar provisions, not an established duty payment deadline. Do not treat 1 September, the order's signature date, its upload month or its retrieval date as a proven legal application date for a liability. Publication, notification and the applicable transition must be checked. [S3, S4]

## Primary source library and reading limits

| Source | Text actually read and provenance | Limit |
| --- | --- | --- |
| **S1. Code rural et de la pêche maritime (CRPM), [TAAF section](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006071367/LEGISCTA000024395243/), particularly [L958-6](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032361278)** | Complete L958-2 and L958-4 to L958-6 read in the official consolidated HTML. The page displayed 'En vigueur au 31 octobre 2026'; L958-4 to L958-6 displayed versions effective from 1 July 2016. Two basic Firecrawl HTML captures were requested live on 31 October 2026 UTC after the local public route returned 403. | Provider Markdown, not the original HTTP body; TLS is not observable through that route. The underlying amending ordinance and every cross-referenced provision were not separately qualified. No complete fisheries or enforcement-law review. |
| **S2. [A-2016-103 of 28 September 2016](https://taaf.fr/content/uploads/2019/09/JO-71_3eme-trimestre-2016.pdf), Journal officiel TAAF n° 71 of 30 September 2016** | Complete order, including recitals and Arts 1–8, read in native text and against original PDF pages 38–39, printed pages 36–37. Fresh official file matched the retained file: 4,085,923 bytes, SHA256 `85d5e80b4c904f87024816e2eadf005b05f118378da7587be91b18bb0b9c286b`. | The 120-page issue was not read in full. Native extraction interleaves adjacent columns and orders; the original images establish this order's boundaries. A-2016-98 was not separately read. |
| **S3. [A-2026-119 of 22 October 2026](https://taaf.fr/content/uploads/2026/10/A-2026-119-droits-de-peche-legine-2026-2027-EKg-net.pdf)** | Complete 2-page order, recitals, Arts 1–4 and signature read using offline OCR and original page images. Fresh official file matched the retained file: 115,244 bytes, SHA256 `7510dbd26a43b8f5dd2f248250b2667d9c2260a3de238a6af610a2efeec6a626`. | Art 4 directs publication and notification. Their completion and legal effect were not established. The applicable consultative opinion required by L958-6, or a qualified legal determination of that requirement's application to S3, is also unresolved. S2's 2016 opinion does not by itself establish compliance for S3; this gap is not proof that S3 is invalid. The filename's 'net' does not replace the operative articles' 'kilogramme capturé'. |
| **S4. [A-2026-82 of 26 August 2026](https://taaf.fr/content/uploads/2026/08/A-2026-82-prescriptions-techniques-peche-legine-2026-2027.pdf)** | Official 28-page PDF, 2,888,686 bytes, SHA256 `90612cc1da070d85db41f660f144ef27625f3b28e701ded13b51364d3800ce42`, retrieved with verified TLS on 31 October 2026 UTC. Selected complete units checked against images: title and date on p 1, Arts 1–6 on p 2, Art 8 and its time-zone footnote on p 3, Arts 19 and 21 on p 7, Arts 40–42 and signature on p 16 and complete Annex 8 on pp 26–27. | Native text was empty. Offline OCR covered all 28 pages; only the named units are qualified here. OCR rotated pp 17–18; those pages are not relied on. The fisheries management plan, individual decisions, other technical provisions and prescribed Excel models were not fully qualified. English readings are working translations. |

S2 is an **arrêté**, not a décret. S3 expressly cites it and repeats the 10% formula, providing a positive 2026 connection rather than relying solely on a failed repeal search. This does not establish an exhaustive amendment chain. S4 Art 41 repeals A-2025-70 from entry into force of S4; it does not state a calendar entry-into-force date. S4 Art 42 directs publication. Do not infer that either provision repeals S2 or settles S3's application date.

## Figures in the sources

| Rule | Figure or method | Source and qualification |
| --- | --- | --- |
| Toothfish for the 2026-27 campaign | €1.82 per kilogram captured | S3 Art 1; scope and source conditions apply |
| Rays for the 2026-27 campaign | €0.30 per kilogram captured | S3 Art 2; retain the species listed in S3's title |
| Grenadiers for the 2026-27 campaign | €0.42 per kilogram captured | S3 Art 3, *Macrourus* spp. in title |
| Statutory duty ceiling | €1,820 per tonne captured, with the amount fixed by species by order of the administrator superior after the specified consultative opinion | S1 L958-6; this is a ceiling, not a universal tariff |
| General percentage formula | 10% of average sale prices observed over the 12 months preceding the campaign's first opening day | S2 Art 1, repeated in S3's recital; it is not 10% of the operator's current sales turnover |
| Historical exception | 9% for the 2016-17 toothfish campaign, using the 12 months before 31 August 2016 | S2 Art 2; do not carry this percentage into 2026-27 |
| Toothfish with VDK weight below 1 kg | Duty multiplied by 3, within the L958-6 maximum | S2 Art 3. VDK is the processed presentation described there, not an assumed captured-weight definition. Actual application is held |
| Vessel quota exceeded | Duty on quantities caught multiplied by 3, within the L958-6 maximum | S2 Art 4; allocation, affected quantity and interaction with Art 3 are held |
| Sale-price history unavailable | Percentage applied to sale prices observed after the campaign | S2 Art 5; it does not authorise inventing prices or replacing S3's fixed amounts |
| Possible default or late-payment penalty | Duty may be increased by 40% for the stated declaration or payment breaches | S1 L958-6. This is discretionary wording; no automatic charge or combined penalty is calculated |
| Recovery period stated in L958-6 | Until the end of the third year following the year in which duty should have been paid | S1 L958-6; interruptions, extensions, procedure and a particular case's deadline are not established |

S2 Art 6 requires duty amounts to be fixed by order. S3's recitals describe species-specific average prices from 2025-26 declared sales of products in net weights. Those price inputs do not change its operative tariff denominator to invoice, landed or processed net kilograms. Do not independently recompute an official rate as 10% of a supplied sale price.

## Position rules and source conditions

### 1. Establish legal application before calculation

For an engagement, establish the requested campaign, species, waters, authorisation holder and vessel. Obtain the operative duty and technical orders, the applicable consultative opinion or a qualified legal determination of that requirement's application to S3, publication and notification evidence, later amendments and any individual decisions affecting the case. Reconcile applicable authority with the engagement's capture dates. Resolve the underlying statutory and subordinate-law dependencies. If the chain or application is unknown, fire `R-TF-SOURCE` before classification or calculation. A professional-review flag does not cure unknown law.

S1 L958-4 applies the section to the territory, waters under French sovereignty and the stated economic zones; L958-5 requires an authorisation for fishing, marine-animal hunting and exploitation of marine products. These broad provisions do not extend S3's particular tariffs to every such activity or place. S4 Art 2 requires a vessel authorisation for a selected operator and compliance with the named management plan and technical rules. This reference neither grants nor verifies an authorisation.

### 2. Reconcile species, zone, campaign and weight

Keep one stable record reference for each source catch item, plus vessel, authorisation, capture date, zone, scientific species, product presentation, measured weight and unit, weighing evidence, controller's record, any conversion and its authority. Record a stated zero separately from missing data. An unidentified species or zone is Needs Input, not a zero-rated or excluded catch.

S4 Art 19 establishes transformation coefficients for equivalent live weight of catches weighed on board. The controller determines them by voyage, zone and product type. It supplies distinct fallback rules for measurement failure and inability to calculate, and requires a signed, stamped duplicate summary at voyage end. Art 21 deals with incidental catches by voyage, species and product type without a zone distinction and refers to Art 19's alternatives. Do not substitute one generic coefficient, confuse the fallback triggers or assume an invoice's net weight is captured weight.

The selected provisions do not completely establish how every product presentation, release, discard, donation, loss, transhipment, weighing correction or conversion enters the duty assessment. Obtain the applicable duty methodology, controller records and assessment instructions. Until the particular chargeable quantity and precision are established, fire `R-TF-WEIGHT`. A filename containing 'net', a sale weight or a permitted fishing-data coefficient alone does not close that gate.

### 3. Separate ordinary tariff arithmetic from adjustments

Once legal application and chargeable quantity are established, the ordinary tariff arithmetic is quantity in captured kilograms multiplied by the matching S3 species rate, with quantities and amounts retained by vessel, campaign, zone and category. Combine totals only where the established assessment rules permit. Do not net one vessel's quota against another's or carry a quota between campaigns from this guide.

S2 Arts 3–4 require separate checks for sub-1 kg VDK toothfish and quota exceedance, subject to the statutory ceiling. An unchanged ordinary toothfish tariff does not establish that a small-fish or over-quota case needs no classification or report. Do not assume that both triggers produce a 9-fold duty, that all catches are necessarily the excess quantity or that the ceiling eliminates other sanctions. The quantity affected, overlap, assessment method and treatment under later law are unresolved. Fire `R-TF-ADJUSTMENT` for a real adjustment, breach, correction, refund or enforcement case.

The arithmetic conversion €1,820 per tonne divided by 1,000 kilograms is €1.82 per kilogram. That equality does not establish a rounding rule, an independent payable amount or how a cap and a penalty interact. Do not add the possible 40% penalty mechanically or treat it as a monthly rate.

### 4. Payment and reporting remain separate

L958-6 states that duty is paid at the end of each campaign when the authorisation beneficiary lodges the catch declaration. It is assessed on a statement made enforceable by the administrator superior. The source does not give this reference a fixed calendar payment day, a current filing form, portal, payment reference, instalment method or rounding instruction. Do not turn the fishing campaign's last day into a remittance deadline.

S4 Art 4 requires voyage data requested by TAAF or its embarked agents and identifies Annex 7 documents as mandatory. Annex 8 is a separate complete set of in-campaign reporting directions. Its item 1 includes:

- Appendix 2: landed weighing details by size category and fishing zone, following the certified landing, within one week after each voyage's landing.
- Appendix 5: a monthly table of sales since the campaign began, including toothfish and other marketed catches, under the 'before the 4th of each month' heading. A no-sales email is sufficient but still necessary where there were no sales in the previous month.

Annex 8 item 3 says Excel models will be supplied at the campaign's start, except Appendix 8 for genetic-analysis results. The models are to be completed without altering their structure; a missing option is to be raised with DPQM before modification. The actual models were not obtained. These reporting directions are not a substitute for the statutory catch declaration or enforceable duty statement. Do not invent columns, form boxes, a submission channel or an acceptance result. Fire `R-TF-FILING` for actual filing, payment, form completion or deadline advice until those requirements are established.

## Conservative defaults and reviewer attention

No default is authorised for law, campaign, species, zone, authorisation, captured weight, conversion, quota, adjustment, precision, deadline or template. Missing facts or documents require Needs Input. A missing record is not a zero. Preserve all source rows with a reason when an item cannot be classified.

For this reference, flag every computed position for professional review, regardless of amount. Any positive amount has a reviewer-attention threshold of €0. This is an internal review threshold, not a statutory exemption or materiality rule. Unknown law or an unmet source condition stops the affected work regardless of value. Quantify alternative factual outcomes only where both treatments and the arithmetic are established; otherwise state that the financial effect is unknown.

## Hypothetical worked positions

All 5 examples assume, solely for illustrating the cited ordinary S3 tariff arithmetic, that the stated kilograms are already established chargeable captured quantities for an authorised in-scope vessel in the named campaign. They assume no small-fish, quota, correction or enforcement issue and no further rate or assessment adjustment. They do not resolve the publication, weight, precision, form or payment holds. The amounts are unrounded exact arithmetic at the displayed precision, not filing amounts or duty determined for an engagement. No actual taxpayer or vessel data is used.

| Example | Hypothetical facts and rule | Complete arithmetic | Result and limit |
| --- | --- | --- | --- |
| 1. Toothfish | 1,000 kg, S3 Art 1 | `1,000 × 1.82 = 1,820.00` | €1,820.00 illustrative ordinary duty. It equals the arithmetic equivalent of S1's ceiling for one tonne, without deciding any adjustment or penalty |
| 2. Listed rays | 250 kg of a species named in S3, Art 2 | `250 × 0.30 = 75.00` | €75.00 illustration. A different ray species cannot be classified from this label alone |
| 3. Grenadiers | 175 kg of *Macrourus* spp., S3 Art 3 | `175 × 0.42 = 73.50` | €73.50 illustration; product weight must not be substituted for captured weight |
| 4. Separate species in one hypothetical schedule | 2,000 kg toothfish, 300 kg listed rays and 50 kg grenadiers, S3 Arts 1–3 | `2,000 × 1.82 = 3,640.00`; `300 × 0.30 = 90.00`; `50 × 0.42 = 21.00`; `3,640.00 + 90.00 + 21.00 = 3,751.00` | €3,751.00 combined arithmetic. Retain the 3 species lines; no actual aggregation or assessment acceptance is established |
| 5. Two identified ordinary toothfish catch lines | 400 kg and 600 kg, each independently satisfying the assumptions, S3 Art 1 | `400 × 1.82 = 728.00`; `600 × 1.82 = 1,092.00`; `728.00 + 1,092.00 = 1,820.00`; `(400 + 600) × 1.82 = 1,820.00` | Both arithmetic routes give €1,820.00. This tests a reconciliation, not permission to combine vessels, zones, campaigns or quota positions |

If instead a source says only '1,000 kg net product', Example 1 cannot be applied: the chargeable captured quantity and conversion are not established. No duty is determined. If the vessel's quota or a small-fish condition is unresolved, the ordinary examples cannot be used to determine the adjustment or a final charge.

## Topical refusal catalogue

Use these exact messages when their triggers apply. Retain the universal base's reviewer and content-mismatch refusals and trace all loaded codes. A refusal before computation produces the refusal and scope trace, not a partly completed return.

| Code | Trigger | Verbatim message |
| --- | --- | --- |
| `R-TF-SOURCE` | Operative law, application, applicable consultative opinion or qualified determination of that requirement, publication, notification, later amendments or necessary legal authority is unresolved | 'The operative source chain for this fishing-duty calculation is not established. I can explain the dated reference, but I cannot determine a liability until the applicable law and its application are established.' |
| `R-TF-PERIOD` | Requested campaign differs from 2026-27 or cannot be established | 'This reference covers selected 2026-27 Kerguelen and Crozet fishing-duty provisions. I need the applicable campaign sources before preparing a different or unidentified period.' |
| `R-TF-SCOPE` | Species, waters, activity, authorisation or another obligation falls outside the qualified scope | 'The requested activity or obligation is outside this fishing-duty reference. Establish the applicable authorisation and sources or load the relevant content before calculation.' |
| `R-TF-WEIGHT` | Chargeable quantity, weight presentation, conversion, valuation or precision is unresolved | 'The chargeable captured quantity or its measurement and precision are not established. I cannot substitute net product, sale or landed weight or invent a conversion or rounding rule.' |
| `R-TF-ADJUSTMENT` | Real small-fish, quota, breach, correction, refund, penalty or enforcement case | 'This reference does not establish the complete adjustment or enforcement treatment for this case. No adjusted duty, refund, penalty or final charge is determined.' |
| `R-TF-FILING` | Actual declaration, payment, form completion, filing deadline or submission requested without the required qualified administrative chain | 'The current assessment, declaration and payment requirements are not established for this case. I can list the missing requirements, but cannot produce a completed filing or payment instruction.' |
| `R-TF-AMBIGUITY` | More than 10 grouped factual questions remain across the workflow | 'More than 10 grouped factual questions remain. Obtain the missing records and a credentialed practitioner's scoping review before continuing this preparation.' |

## Intake and workflow additions

Follow the universal sequence: read the redacted records, infer the profile, obtain its confirmation, run refusals, perform only supported work, resolve factual questions, build the required outputs, check and deliver. Silence is not profile confirmation. Do not request repeated approval for routine preparation steps. This reference is not an engagement and contains no confirmed profile.

Infer the campaign, vessel and authorisation holder, waters, scientific species, product form, catch and landing dates, quantities, units, source documents and requested obligation. Confirm missing essential facts in the same profile round trip. Use stable redacted references. The reviewer retains names, identifiers, credentials, signing tokens and bank or payment details needed for administration.

Before actual preparation, request the operative and later orders, applicable consultative opinion or qualified determination of that requirement, publication and notification evidence, individual vessel and quota decisions, catch and controller records, weight and conversion evidence, relevant assessment directions, enforceable statements, prior declarations or corrections and the prescribed campaign models. Group factual questions, reuse answered facts and distinguish unknown law from facts the user can provide. A reviewer cannot waive a source hold by confirming a profile.

## Output extension

The universal 4 logical outputs remain mandatory after the source gates have been met: a recalculated working paper, reviewer brief, action list and review checklist. This guide adds no permission to deliver a partially classified filing when a gate fails. A refusal requires the exact message, evidence gap, affected scope and refusal trace.

For later supported preparation, add a catch schedule with a stable record reference, capture date, campaign, vessel, authorisation reference, zone, scientific species, product presentation, source weight and unit, validated captured weight, conversion and evidence, quota and small-fish checks, applicable tariff and source, unrounded arithmetic, legally required precision, adjustment treatment, assessment reference and reconciliation status. Keep the universal citation, default, attention and exclusion fields identifiable. Do not invent official codes. Reconcile source counts and quantities without silently deleting, netting or duplicating items.

The reviewer brief must separate tariff arithmetic, unresolved or established adjustments, assessed duty and payment status. An illustration must never populate a payable or filing box. Record the relevant original language, translation limit and each source's actual reading extent. The action list identifies each missing source or record, who must supply it, the established deadline if any and the financial effect where known. Add the topical checks below to the review checklist, with an explicit reviewer decision for every flag and source condition. No filing-ready bottom line exists under an unresolved hold.

## Self-check additions and Review Checklist Items

1. Campaign, waters, scientific species, authorisation and vessel match the qualified scope and established law.
2. Source application, applicable consultative opinion or qualified determination of that requirement, publication, notification, later law and individual decisions are documented; a retrieval date has not supplied commencement.
3. Every source catch item appears once, with an exclusion reason where applicable; missing values have not become zeroes.
4. Captured, equivalent live, processed, landed and sold weights remain distinguishable. Conversion evidence and the appropriate trigger and fallback are recorded.
5. Each species rate cites the matching S3 article. The 10% formula has not become a turnover tax and the historical 9% has not been carried forward.
6. Small-fish, quota, overlap, cap, breach, correction and penalty issues are resolved by the applicable authority or refused. No 9-fold, automatic 40% or monthly penalty has been invented.
7. Precision, timing, prescribed models, catch declaration and enforceable assessment are established independently. A fishing date or monthly sales report has not become a payment instruction.
8. Workbook formulas recalculate without errors and reconcile by species, vessel, campaign and source record. Illustrative amounts cannot flow into actual filing or payment fields.
9. The brief, action list, checklist and workbook agree; every loaded refusal code, default and reviewer flag is traced. Professional sign-off is distinct from arithmetic verification.

## Topic reference map and revision

| Topic lens | This version |
| --- | --- |
| 1. Scope | Narrow campaign, waters, species and duty scope stated; other topics remain outside it |
| 2. Period | Dated source coverage; legal application and later chain held |
| 3. Figures | Fixed amounts, formula, cap and distinct historical and penalty provisions cited |
| 4. Sources | 4 named source groups with reading and provenance limits |
| 5. Positions | Conditional decision sequence; actual classification and calculation held until authority and quantities are established |
| 6. Refusals | 7 topical codes, plus the loaded universal catalogue |
| 7. Defaults | None authorised for unresolved substantive facts or law |
| 8. Reviewer thresholds | All computed positions flagged; internal €0 threshold, no statutory significance |
| 9. Examples | 5 complete hypothetical ordinary-tariff positions; no operational or filing acceptance |
| 10. Outputs | Universal package and catch-schedule extension specified; administrative preparation remains incomplete |
| 11. Intake | Campaign, authority, vessel, species, weight and assessment records specified |
| 12. Checks | Topical reconciliation, source, weight, adjustment and filing checks added |
| 13. Currency and revision | v0.3, edited 1 November 2026; public sources captured 31 October 2026 UTC |

The table maps this reference’s topics. It does not reproduce the workflow-base Section 7 contract or declare its mandatory operational slots complete. In particular, period application, legal and weight conditions and administrative preparation remain held. Presence of this reference would not constitute comprehensive TF topic coverage or professional verification.

Version 0.1: initial unpublished source-limited draft. It records the 2026-27 order, the 2016 formula and selected statutory and technical context, with explicit law, weight, adjustment, precision and filing holds. No actual engagement, workbook, declaration, payment or submission was tested.

Version 0.2 made the consultative-opinion dependency explicit. Version 0.3 corrects the topic-map label and revision note without changing the substantive rules, examples or holds.

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
