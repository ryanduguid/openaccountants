---
name: km-consumption-tax-reference
description: >
  Comoros taxe sur la consommation (TC) reference for a business in 2026. Gives
  the 10% rate and the 0%, 3%, 5%, 7.5% and 25% exceptions, the KMF 20,000,000
  turnover exemption and its importer limit, listed exemptions, territoriality,
  chargeability, invoices, monthly returns before the 15th, customs prepayment,
  interest, penalties and worked figures. Trigger on Comoros TC, CGI Art 149 or
  Union des Comores consumption tax. Refuses box-level returns, refunds and an
  assumed input credit, and holds the electronic filing route. This source-cited
  draft awaits local professional review and is not filing readiness.
jurisdiction: KM
category: international
tax_year: 2026
tax_year_notes: "2026 periods. CGI 2023 read with LFR 2023, an unpromulgated copy of LF 2024, and the tax articles of LFR 2025 and LF 2026. LFR 2024 and LF 2025 were checked only in part. Later instruments and arrêtés were not established."
tier: 2
last_updated: 2026-10-31
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - vat-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Comoros Consumption Tax Reference, 2026

Load this on top of `vat-workflow-base`. The Comoros levies a taxe sur la consommation (TC), not a tax called VAT, so do not import VAT mechanics the text does not state. This file answers the base's section 7 slots so far as the sources allow. **It is incomplete as a country skill.** Slots 3, 6, 7, 12, 13 and 15 have little or no Comorian source, so the base's missing-slot rule applies to box-level return preparation: refuse that. HOLD means the sources read do not establish the point, and no figure may be supplied for it from memory.

**Chain of law.** The latest consolidation read is the CGI 2023, to the 2023 finance law. Later laws were checked as follows, and only for changes to these articles.

| Law | Result for CGI Arts 139 to 152 | Limit |
|---|---|---|
| LFR 2023, Law 23-008/AU, Art 12 | Restates the rates and adds cement at 5% | Signed scan. Formally amends Law 20-012 Art 18(7), treated here as updating Art 152 (inference) |
| LF 2024, taken to be Law 23-019/AU, Arts 12 to 15 | No change to Arts 139 to 152; adds L.165 to L.170 and changes L.4 | Adopted text on a WTO host; no promulgated copy. Its identity is inferred from LF 2026 Art 14 |
| LFR 2024, Art 10 | Its article list excludes them | Selected clauses read |
| LF 2025 | No CGI section found | Search of OCR only |
| LFR 2025 and LF 2026 | No TC rate or base change found in their tax articles | LFR 2025 from an archive copy; LF 2026 partly OCR |

For the procedure book, no later change to L.96 to L.106 or L.115 was found. LF 2024 changes L.5 and L.31, which set the notice period behind L.98, and LF 2026 adds L.43 bis.

Amounts are in Comorian francs (KMF), which some laws write as FC.

## Slot 1: Standard rate

10% (CGI Art 152; LFR 2023 Art 12).

## Slot 2: Exception rates

| Rate | Supplies | Authority |
|---|---|---|
| 0% | First-necessity goods at import and domestically, as listed by ministerial arrêté | LFR 2023 Art 12 |
| 3% | Water and electricity; inter-island transport tickets | Art 12 |
| 5% | Restaurants; banking; fixed telephone; cement; international transport tickets | Art 12. Cement is not in CGI 2023 Art 152 |
| 7.5% | Mobile voice and data top-ups | Art 12 |
| 25% | Casino activities | Art 12 |

A further charge of KMF 50 a minute applies to incoming call termination. Operators return it by the 15th of each month with payment (Art 149 bis).

**First-necessity list.** The CGI note reproduces Arrêté 17-065/MFB/CAB of 19 September 2017: fresh or frozen meat and edible offal; poultry meat and offal; fresh or frozen fish; ordinary rice; cereal, wheat or meslin flour; sugar; medicines; first-age and second-age infant milk. HOLD whether a later arrêté replaced it, as LFR 2023 Art 12 says one 'définira la liste'. The 2017 arrêté rests on an older exemption limb, not the present 0% rate.

## Scope and base

TC applies to imports unless legally exempt, to purchase-and-resale, production and commercial or non-commercial services (Art 139). Under Art 140 it falls notably on:

1. total sales and works, all accessory charges included (packaging, transport, insurance, customs duties and taxes, agios);
2. brokerage, commissions, rebates, interest, discounts and agios received, ancillary receipts and profits;
3. service income;
4. CIF value of imports plus all customs-type entry charges;
5. goods delivered by a joint buying body to members, or by a head office to branches or independent retail outlets for sale, at no less than commercial value at the place of delivery;
6. imported goods first meant for sale and then used by the importer, at effective value at the place of import plus customs charges;
7. other products definitively acquired in the course of a taxable person's profession;
8. liberal professions' activities.

## Turnover exemption

Art 141(1) exempts businesses with turnover below KMF 20,000,000 excluding tax, 'excepté les entreprises comprises entre 15.000.000 KMF et 20.000.000 KMF non compris et qui sont importateurs'.

| Turnover excluding tax | Importer? | Result |
|---|---|---|
| Below 15,000,000 | No | Exempt |
| Below 15,000,000 | Yes | Exempt under Art 141(1)'s wording, and Art 139 taxes imports 'sauf exonérations légales'. HOLD how Customs collects or the exemption is proved at import: no rule on this was read |
| 15,000,000 up to but not including 20,000,000 | No | Exempt |
| 15,000,000 up to but not including 20,000,000 | Yes | Not exempt under this limb |
| 20,000,000 or more | Either | Not exempt under this limb |

The period over which turnover is measured is not stated in Art 141(1): HOLD wherever it could change the result (R-KM-2). Whether exactly 15,000,000 falls in the importer band turns on 'comprises entre', and the words 'non compris' follow 20,000,000. This draft treats 15,000,000 as inside the band, consistent with Art 91's 'supérieur ou égal à 15.000.000 KMF et inférieur à 20.000.000 KMF assujettis à la Taxe sur la Consommation' (inference). Art 141's evidence paragraph literally names limb 1 as well as limb 2, but export declarations cannot evidence a turnover exemption: HOLD that for limb 1.

LF 2026 L.4 ter also applies a 15% retention at the customs line, tied to the tax compliance certificate. It is not TC: R-KM-6.

## Other exemptions (Art 141)

| Limb | Exempt | Condition or limit |
|---|---|---|
| 2 | Products and directly linked services for export | Customs export declarations with the NIF, endorsed by Customs and kept with the accounts (paragraph after limb 3) |
| 3 | Deliveries and services for ships and aircraft to or from abroad | Excludes sport and pleasure craft. No stated evidence rule |
| 4 | Sales by retail fuel distributors | Petrol, gas oil, kerosene, motor oil, gas |
| 5 | Operations of legally constituted non-profit bodies | With philosophical, religious, political, patriotic, civic, union, educational, cultural or sporting aims |
| 6 | Fiscal stamps, stamped paper and postage stamps | At official value; postage stamps must be valid for postage in the Comoros |
| 7 | Occasional asset disposals by the State, public bodies and administrative public institutions | |
| 8 | Newspapers and periodicals | Not advertising or announcement receipts |
| 9 | Farmers', breeders', fishers' and market gardeners' produce | Processed farm produce only if wholly from the holding that changed its nature |
| 10 | Stated Central Bank operations | |
| 11 | Operations under contracts financed by external aid | |
| 12 | Private school fees | |
| 13 | Legal practice of medical professions | |
| 14 | Transfers of immovables and intangibles, and their letting, liable to registration duties | Not professional property lessors whose activity is such letting |
| 15 | Insurance subject to the insurance contract tax | |
| 16 | Lease payments and residual value under finance leases where the lessee paid TC on the equipment or immovables | The text gives the lessee 'déductibilité' and lets the lessor finance the TC, but states no mechanism: HOLD. Read with Law 12-011 Art 58, not read |

Investment, free zone and other special regimes are outside this file: R-KM-4.

## Territoriality and timing

A sale is in the Comoros when made on terms of delivery there; another operation is when the service, right or leased object is used or exploited there (Art 143). Taxable operations are caught even if the actual taxpayer's domicile or seat is abroad (Art 142).

| Event | Chargeable (Art 144) |
|---|---|
| Import | On crossing the customs line |
| Goods | On handover to the customer, even with deferred or instalment pricing |
| Liberal professions, including fees and commissions | On receipt of the price |
| Industrial, commercial or craft services and building works | Chargeable event on performance; tax due on receipt of advances, instalments and final settlement |

## Customs prepayment and credit (HOLD beyond imports)

TC paid at Customs is 'un acompte de l'impôt qui doit être versé à la suite de la première transaction ou opération taxable'. Importers attach to the monthly return a list of imports already taxed in the month before the sale, with customs documents, so the final charge can be calculated. 'En aucun cas, la régularisation ne peut aboutir à un remboursement de la taxe perçue à l'importation' (Art 150).

The text establishes this advance for TC paid at import; reading it as an offset against the final charge, goods by goods, is inference. **It does not establish a general credit for TC on domestic purchases or services:** HOLD and refuse to model one (R-KM-3). Art 141(16) uses 'déductibilité' only for finance leases. L.41 deducts supplementary taxes on simultaneous audits, an audit adjustment rather than an input credit.

## Slot 3: Return form

The return is monthly and in duplicate on the administration's model. It shows total operations and the detail of taxable ones for the previous month (Art 149). Two copies, 2 payment slips and the tax go to the tax Recette (Art 150). A business with several establishments files one return at the Recette for its seat or main establishment (Art 151). No box list was found: refuse box-level preparation (R-KM-1).

## Slot 4: Portal (HOLD)

The sources conflict on timing and do not name a platform.

- LF 2024 Art 13 (L.4): Art 149 returns optional electronically in 2024 and 2025; 'A partir du 1er janvier 2026, les déclarations d'impositions se feront obligatoirement par voie électronique'.
- LF 2026 (L.10 bis to undecies): defines e-filing and e-payment on an official platform, with commencement 'à une date fixée par Arrêté'. No arrêté was found.
- LF 2026 L.10 ter makes e-filing 'obligatoire, par paliers fixés par une décision du Directeur Général des Impôts', phased by taxpayer size, and L.10 octies(3) allows exceptional counter filing. No such decision was found, so the business's category is the question for the tax office.
- CGI Art 150 still describes deposit at the Recette.

Later text probably controls the platform rules, but this is unresolved (inference). Confirm the route with the tax office, and do not state that paper or electronic filing alone is valid.

## Slot 5: Deadlines

| Duty | Deadline | Authority |
|---|---|---|
| Declaration of existence | Within 15 days of starting operations | Art 145 |
| Cessation | Within 10 days | Art 146 |
| Monthly return and payment | Before the 15th of the month for the previous month (payment date inferred from Art 150's deposit with the return) | Arts 149, 150 |
| Call termination return and payment | By the 15th of the month for the previous month | Art 149 bis |
| Wholesalers' and semi-wholesalers' annual statement of buyers | Before 31 January | Art 136 |
| Exporters', distillers' and local produce merchants' annual statement | Before 31 January | Art 137 |

'Before the 15th' excludes the 15th itself on its wording. Art 205, in the registration title, extends deadlines falling on a non-working day 'dans tous les cas où la présente codification fixe un délai'; its reach to Art 149 is unresolved: HOLD.

## Invoices and records

A taxable person supplying goods or services issues an invoice or equivalent showing: name, exact address and NIF; the customer's name, address and NIF; date and serial number; description and quantity; amount excluding tax; TC rate and amount; amount including tax. **An invoice not showing the tax is treated as tax-inclusive** (Art 148).

Records follow Art 41. A numbered day book records each operation daily without gaps or erasures, separating taxable operations by rate from others. Cash operations of up to KMF 5,000 each, tax included, may be entered as a daily total if supported by cash slips or till rolls (Art 147). Art 41(2) also requires a cash register for commercial activities at KMF 20,000,000 or more. Failing to produce reliable accounts can lead to office rectification (Art 147(6)). An invoice omitting the tax is still arguably 'incomplète' under L.103 despite Art 148 (inference).

## Non-resident suppliers

Where a supplier of services is not domiciled in the Comoros, the recipient self-assesses TC on its monthly return (Art 149). The article states no limit on who the recipient is. It presupposes a recipient who files that return (inference): HOLD a recipient who does not. Art 130's outbound remuneration tax base is 'hors taxe sur la consommation'. LF 2024 Art 13 also requires foreign taxpayers active without a seat to appoint an accredited tax representative, with conditions set by arrêté, which was not found.

## Interest and penalties

| Event | Consequence | Authority |
|---|---|---|
| Late payment | Interest of 10% a month of delay, capped at 50% of the principal debt. Starts on the first day of the month after an assessment notice is received, the day after the legal return date (any month begun counting in full) or the day after the legal due date. Ends on the last day of the month of payment. L.115 does not define a month: HOLD whether L.96's definition applies | L.115 |
| Under-declaration leading to reassessment | Interest of 10% per month of '30 jours ouvrables', capped at 50%, on the reassessed duties, until the last day of the month of notification. L.96 starts the day after the return 'a été déposée'; L.99 starts the day after 'dépôt légal'. These differ for an early or late return: HOLD the start date and any computation (R-KM-5). Under L.99 any month begun counts in full; HOLD whether the working-day definition reaches L.99 | L.96, L.99 |
| Same, 'en sus de l'intérêt de retard' | 50% good faith; 100% bad faith; 150% fraud | L.97 |
| No return after formal notice | Office assessment, plus 100%; 150% on repetition. LF 2026 L.43 bis allows office assessment 'sans mise en demeure préalable' in its own cases | L.98 |
| Nil return not filed after formal notice | KMF 10,000 | L.100 |
| Late or manifestly wrong registration, or registration amendments not lodged on time | KMF 20,000 | L.101 |
| No NIF | Minimum levy of 5% of turnover; other bars | L.102 |
| NIF missing from an invoice | 10% of the invoice amount | L.102 |
| No invoice, or a wrong or incomplete invoice issued, received or used by a professional | Fine of 100% of the transaction value | L.103 |
| Sale without invoice between taxable persons | Buyer liable for TC, alone or jointly with a known seller, plus a 100% fine; the fine falls only on the seller if the buyer reports the seller ('l'acheteur le dénonce') | L.104 |
| Art 136 or 137 statement late | KMF 200,000; each omission or error KMF 20,000 | L.106 |
| Relief | L.157 bars a settlement on interest and on TC collected but not paid over. L.160: 'Aucune remise ou modération ne peut être accordée sur la taxe sur la consommation' | L.157, L.160 |

These are source provisions, not findings. L.96 and L.97 cumulate on their text. How they relate to L.115 on one debt is not settled: R-KM-5. LF 2024 Art 13 adds consumption tax enquiry powers at L.165 to L.170.

## Refunds

Art 150 bars a refund of import TC on regularisation. L.23 and L.117 presuppose refunds without giving a TC procedure. A claim that tax was over-assessed goes through the contentious dégrèvement route (L.131 onward, L.136), not read for this file: refer it.

## Slots 6, 7, 9, 10 and 12 to 15

- **Slot 6, supplier patterns:** no source. HOLD.
- **Slot 7, exclusions:** no local list. Classify from Arts 139 to 141 only.
- **Slot 8, refusals:**
  - R-KM-1: box-level return preparation.
  - R-KM-2: any business whose exemption could change with the measuring period, or customs collection and proof for an exempt importer below 15,000,000.
  - R-KM-3: any credit other than the Art 150 import advance, including the finance lease 'déductibilité', or a refund, except that an over-assessment claim is referred.
  - R-KM-4: investment code approvals, free zones, public contract rules and external aid contracts, without the instrument.
  - R-KM-5: computing a combined interest and penalty total.
  - R-KM-6: excise-type taxes on petroleum and rice, the LF 2026 customs retention, and other taxes.
- **Slot 9, questions:** annual turnover and period; importer status; NIF; nature of each receipt against Art 140; rate class; customs documents; recipient status for non-resident services.
- **Slot 10, defaults:** use 10% only once the supply is positively classified as standard-rated; if an exception, exemption or the first-necessity list could apply, HOLD. With an invoice silent on tax, treat it as tax-inclusive, as Art 148 requires, and flag L.103. The 10% step is a drafting choice under the base's section 2, not Comorian law.
- **Slots 12, 13, 15:** no source.
- **Slot 14, inputs:** sales and purchase records, the day book, invoices, customs declarations, NIF, and any arrêté or approval relied on.

## Slot 11: Worked examples (fictional)

Invented figures for Moroni Bluewave Trading SARL, in KMF.

| # | Facts | Working | Assumption |
|---|---|---|---|
| 1 | Taxable sales of 4,000,000 excluding tax at 10% | `4,000,000 × 10% = 400,000` | Not exempt; full month |
| 2 | Restaurant receipts of 2,000,000 excluding tax | `2,000,000 × 5% = 100,000` | Rate 5% |
| 3 | Mobile top-ups of 1,000,000 excluding tax | `1,000,000 × 7.5% = 75,000` | Rate 7.5% |
| 4 | Invoice for 11,000 at 10% with no tax shown | Tax-inclusive: `11,000 × 10 / 110 = 1,000`; net `10,000` | Art 148; L.103 exposure not displaced (inference) |
| 5 | Import CIF 3,000,000; customs-type charges 500,000; rate 10% | `(3,000,000 + 500,000) × 10% = 350,000` | Art 140(4) |
| 6 | Sales of 4,000,000 excluding tax, tax 400,000; import advance 350,000 on those goods | `400,000 − 350,000 = 50,000` | Art 150 advance read as an offset (inference); timing as listed there |
| 7 | Advance of 350,000 exceeds tax of 300,000 | Excess `50,000`, not refunded on regularisation; carry-forward held | Art 150; R-KM-3 |
| 8 | Tax of 400,000 unpaid; 3 months begun | `400,000 × 10% × 3 = 120,000`; cap `400,000 × 50% = 200,000` | L.115 start point assumed; a month counted as a calendar month (assumption) |
| 9 | Tax of 400,000 unpaid; 7 months begun | `400,000 × 10% × 7 = 280,000`; capped at `200,000` | L.115; same assumptions |
| 10 | Importer with turnover of 17,000,000 | No Art 141(1) exemption | Period assumed annual; R-KM-2 if the period could change the result |

## Delivery holds

Tier 2 draft pending review by a Comorian adviser. It establishes no filing readiness. These remain open: the promulgated LF 2024, later arrêtés, the current first-necessity list, the e-filing commencement, forms, ruling practice and non-working-day rules. A retrieval date does not certify current law. Output is a working paper.

## Sources

Checked on 31 October 2026. [Code général des impôts 2023](https://justice.gouv.km/wp-content/uploads/2025/03/comores-cgi-2023.pdf), Arts 41, 91, 130, 133 to 157, 205, L.23, L.41, L.95 to L.117, L.131 to L.136, L.157 and L.160, from OCR and the PDF text layer; the pages for these articles were not checked as images. [LFR 2023, Law 23-008/AU](https://finances.gouv.km/wp-content/uploads/2024/12/Decret_N%C2%B023-064PR_portant_Promulgation_de_la_loi_de_Finances_Rectificative_2023.pdf), Art 12 by page image. [LF 2024 text](https://www.wto.org/english/thewto_e/acc_e/com_e/WT_ACC_COM_50_LEG1.pdf), WTO accession document, adopted 27 November 2023, not a promulgated copy. [LF 2026, Law 25-020/AU](https://finances.gouv.km/wp-content/uploads/2026/01/Decret-N%C2%B026-003PR-du-16-jan-2026-portant-Prom-Loi-25-020AU-portant-Loi-de-Finan.pdf), pp 1 to 16, partly OCR. LFR 2025, Law 25-019/AU, pp 1 and 9, archive copy because the official link returned 404. Not found: the Comorian tax office's own site `dgi.gouv.km` failed DNS on 31 October 2026.

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
