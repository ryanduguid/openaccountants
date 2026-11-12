---
name: km-consumption-tax-reference
description: "Source-cited draft for Comoros taxe sur la consommation (TC) in 2026. Covers existing rates, scope, exemptions, invoices, returns, customs prepayment, penalties and examples; refuses box-level returns, refunds and assumed input credits. Electronic filing remains held. Includes selected original 2014 AUSCGIE decisions and audit appointments, 2017 AUDCIF accounting rules and the 2017 professional framework effective from 2018. Trigger on Comoros TC, annual accounts, audit standards, ethics or quality assurance. Later law, full standards and tool editions, sector rules, national procedures and current eligibility remain open. Pending qualified review; no filing readiness."
jurisdiction: KM
category: international
tax_year: 2026
tax_year_notes: "2026 periods. CGI 2023 read with LFR 2023, an unpromulgated copy of LF 2024, and the tax articles of LFR 2025 and LF 2026. LFR 2024 and LF 2025 were checked only in part. Later instruments and arrêtés were not established."
tier: 2
last_updated: 2026-11-12
version: 0.7
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

## Annual company reporting under the 2014 AUSCGIE

Comoros is an OHADA member. This company-law reference is separate from the consumption-tax workflow. It summarises selected provisions of the original 2014 AUSCGIE; later amendments have not been verified. Confirm the law applicable to the company’s actual period before using a deadline. [OHADA member states](https://www.ohada.org/les-etats-membres-de-lohada/)

The revised AUSCGIE took effect on **5 May 2014**. The following rules address
annual SARL and SA decisions and commercial-company registry deposits.
[OHADA company law register](https://www.ohada.org/droit-des-societes-commerciales-et-du-gie/)

- **SARL annual meeting.** The annual ordinary general meeting must take place
  within **6 months after the financial year closes**. The managers may ask the
  competent court for an extension. [AUSCGIE, articles 347 and 348](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=86)
- **SA annual meeting.** The ordinary general meeting must take place at least
  once a year, within **6 months after the financial year closes**, subject to
  an extension by court decision. [AUSCGIE, article 548](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=133)
- **Sole-member companies.** The sole shareholder of an SA takes the annual
  ordinary decisions within **6 months after the financial year closes** and
  records them in minutes kept in the company's archives. Article 347 applies
  these sole-member decision rules to a SARL, with the exceptions it specifies.
  [AUSCGIE, article 347](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=86),
  [articles 558 to 560](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=135)
- **Deposit of annual accounts.** A commercial company must deposit the prior
  year's annual financial statements with the RCCM in the state of its
  registered office **within the month following approval** by the competent
  body. If approval is refused, a copy of the refusal decision must be deposited
  within the same period. [AUSCGIE, article 269, pages 65 and 66](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=65)

For example, for a multi-member SARL with a **31 December 2025** year-end, the
ordinary annual meeting is due by **30 June 2026**, subject to a court extension.
Track the RCCM deposit deadline from the actual approval decision. Record the
national tax-return deadline separately. The current registry filing method,
fees, applicable accounting and audit rules and any sector-specific obligations
still need verification. [AUSCGIE, articles 269 and 348](https://biblio.ohada.org/doc_num.php?explnum_id=3974)

## Selected accounting rules under the 2017 AUDCIF

This reference summarises selected provisions of the original AUDCIF adopted on
26 January 2017. Article 113 expressly fixes commencement at **1 January 2018**
for individual entity accounts and **1 January 2019** for consolidated accounts,
combined accounts and IFRS statements. It also contains a general
publication-based clause; the dates here come from its express commencement
paragraph. Verify later amendments, accounting-standard updates and the rules
for the entity's actual period before use.
[AUDCIF, article 113, PDF page 53](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=53)

### Scope and accounting regime

Articles 1 and 2 impose accounting duties on entities within their scope,
including commercial companies, and exclude entities governed by public
accounting rules. Article 5 establishes SYSCOHADA but excludes credit
institutions, microfinance institutions, financial-market participants, insurers
and reinsurers, social security and welfare bodies and non-profit entities
from that accounting system. Exclusion from SYSCOHADA does not by itself exempt
an entity from the AUDCIF's accounting duties. Verify the applicable sector or
non-profit framework separately.
[AUDCIF, articles 1, 2 and 5, PDF pages 16 and 17](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=16)

- **Normal system.** Article 11 makes the normal system the default, subject
  to the size exception. Its annual statements comprise a balance sheet, income
  statement, cash flow statement and notes.
  [AUDCIF, articles 8, 11 and 26, PDF pages 18, 19 and 25](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=18)
- **Minimal cash system (SMT).** Under article 13, small entities use SMT unless
  they opt otherwise. Eligibility requires annual turnover excluding tax
  **below CFA 60,000,000 for trading, CFA 40,000,000 for craft and similar
  activities or CFA 30,000,000 for services**, or the equivalent in the member
  state's legal currency. These are accounting thresholds, not tax-regime
  thresholds. Check activity classification, any election and the applicable
  local-currency equivalent before selecting SMT. Article 28 requires a balance
  sheet, income statement and notes based on cash accounting, taking changes
  in inventories, receivables and debts into account when material.
  [AUDCIF, articles 13 and 28, PDF pages 20 and 25](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=20)
- **Listed entities and public offerings.** Article 8 requires annual IFRS
  statements in addition to the other annual statements for entities whose
  securities are exchange-listed or which seek financing through a public
  offering. The IFRS statements are for financial markets and do not determine
  distributable profit. Group-accounting requirements need a separate assessment.
  [AUDCIF, article 8, PDF pages 18 and 19](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=19)

### Annual timetable and records

Article 7 sets an ordinary **12-month calendar accounting year**, with specific
first-year and liquidation exceptions. Article 23 requires annual statements to
be drawn up (*arrêtés*) **within 4 months after year-end**, with that date
mentioned whenever they are transmitted. This drawing-up date is distinct from
shareholder approval, an RCCM deposit and a national tax-return deadline.
[AUDCIF, articles 7 and 23, PDF pages 18 and 24](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=24)

Under article 71, the governing or management bodies draw up an inventory,
annual statements and a management report, with a social report where
applicable. The management report covers the past year, prospects, liquidity
and financing, and significant events after year-end up to its preparation.
Where statutory auditors exist, the documents go to them **at least 45 days
before the ordinary general meeting**. Article 70 addresses auditors appointed
voluntarily or mandatorily; it does not establish that every entity must appoint
one. Verify appointment duties and exemptions for the legal form and sector.
[AUDCIF, articles 70 and 71, PDF pages 39 and 40](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=39)

Article 16 requires an accounting procedures and organisation manual, updated
periodically. Article 17 addresses the official language, legal currency,
double-entry records, dated supporting documents and inventory controls.
Article 19 lists the journal, general ledger, general trial balance and
inventory book. SMT bookkeeping follows its own provisions in article 21.
Article 24 requires accounting books or equivalent documents and supporting
vouchers to be retained for **10 years**. It does not set the starting point
for that period in its text; verify that point and any additional national
retention rules before destroying records.
[AUDCIF, articles 16 to 24, PDF pages 20 to 24](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=20)

For an ordinary **31 December 2025** year-end, the article 23 drawing-up
deadline gives **30 April 2026**. Record shareholder approval, any auditor
communication and RCCM deposit as separate steps under their own rules.
This example does not establish the national tax deadline.
[AUDCIF, article 23](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=24)

The complete SYSCOHADA annexes, subsequent standard-setting decisions, detailed
recognition and measurement, group accounts, sector and non-profit frameworks,
legal-form audit requirements, national submission procedures and fees, and
qualified local review remain outstanding. These selected provisions do not
establish complete reporting coverage or filing readiness.

## Selected statutory audit rules under the 2014 AUSCGIE

This reference reads selected provisions of the original revised AUSCGIE,
adopted on 30 January 2014 and effective from **5 May 2014**. Check later
amendments, national professional rules, sector requirements and the entity’s
actual period before applying them. These appointment tests are separate
from the accounting-regime tests in the AUDCIF section.
[AUSCGIE, article 920, PDF page 226](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=226)

### SARL: size test, other appointments and term

Under article 376, a SARL must appoint at least one statutory auditor if it
meets at least 2 of these 3 conditions at financial year-end:

- balance sheet total **above CFA 125,000,000**;
- annual turnover **above CFA 250,000,000**;
- permanent workforce **above 50 people**.

Each test uses a strict excess: equality does not satisfy that condition.
The article states annual turnover without specifying an excluding-tax basis
in this passage. Do not import the AUDCIF’s SMT turnover definition. Verify
the legal-currency treatment before using these CFA amounts in a non-CFA state.
[AUSCGIE, article 376, PDF page 93](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=93)

Article 376 also provides for the obligation to cease when the company has
not met 2 conditions during the 2 financial years preceding expiry of the
auditor’s term. A single below-threshold year does not establish that this
rule applies. Other SARLs may appoint voluntarily, and holders of at least
one tenth of the capital may ask a court to appoint an auditor. A size test
that is not triggered therefore does not establish that no auditor is needed.
[AUSCGIE, article 376](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=93)

Article 379 sets a term of **3 financial years**, initially by holders of
more than half the capital. If that majority is not obtained, and unless the
statutes provide otherwise, appointment is by a majority of votes cast,
regardless of the proportion of capital represented.
[AUSCGIE, article 379, PDF page 94](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=94)

### SA: mandatory appointment and different terms

Article 694 provides for statutory audit in every SA. Article 702 requires
one principal auditor and one substitute for an SA that does not make a
public offering, and at least **2 principal auditors and 2 substitutes**
for an SA that does. This is not the SARL size test.
[AUSCGIE, articles 694 and 702, PDF pages 161 and 163](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=163)

Under articles 703 to 705, the initial auditor and substitute are designated
in the statutes or by the constitutive general meeting, with a term of
**2 financial years**. Appointment during the company’s life is by the
ordinary general meeting, with a term of **6 financial years**. Article 705
links expiry to the meeting deciding on the relevant second or sixth year’s
accounts. A replacement serves the predecessor’s remaining term under
article 706. If the meeting omits renewal or replacement, article 709
continues the mission until the next annual ordinary meeting unless the
auditor expressly refuses. Check these rules before treating a term as lapsed.
[AUSCGIE, articles 703 to 709, PDF pages 163 and 164](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=164)

### SAS: size test and additional triggers

Article 853-13 permits voluntary appointments and requires at least one
auditor when 2 of the same 3 year-end size conditions above are met. It also
requires an auditor for an SAS that controls one or more companies, or is
controlled by one or more companies. Article 174 defines control as the
effective holding of decision-making power. Do not treat a small SAS as
exempt without checking those relationships. Article 853-13 includes the
2-year pre-expiry cessation rule, a court-request route for holders of at
least one tenth of the capital and certification by an auditor of the
president’s statement of accounts for a capital increase by offsetting
claims against the company when it has no auditor. Treat that transaction-specific
certification separately from the ongoing appointment tests.
[AUSCGIE, articles 174 and 853-13, PDF pages 45, 209 and 210](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=209)

### Practitioner eligibility and a worked boundary

Article 377 directs SARL selection to articles 694 onwards. Article 695
requires registration with the professional order where one exists in the
registered-office state. Article 696 provides a court-of-appeal list route
where no order exists: experts must be registered beforehand on a list drawn
up by a commission attached to a court of appeal in the state. Independence
and incompatibilities must also be
checked, including articles 378 and 697 to 700. These references do not
verify a particular practitioner’s eligibility or the current national lists.
[AUSCGIE, articles 377, 378 and 694 to 700, PDF pages 93 and 161 to 163](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=161)

For a hypothetical SARL at a **31 December 2025** year-end, a balance-sheet
total of **CFA 126,000,000**, annual turnover of **CFA 250,000,000** and a
permanent workforce of **51** meet the balance-sheet and workforce conditions.
The turnover condition is not met at equality. There are 2 qualifying
conditions, so the original article 376 requires an auditor. This example
does not establish later-law applicability, currency conversion or sector rules.
[AUSCGIE, article 376](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=93)

Record the legal form, year-end figures, control relationships, existing
appointment and term, any court order and applicable national or sector
requirements. Later law, detailed audit standards and procedures, professional
registration and qualified local review remain outstanding. These selected
appointment rules do not establish complete reporting coverage or filing readiness.

## Selected professional framework under the 2017 OHADA Regulation

This reference reads the signed 3-page facsimile of Regulation
**01/2017/CM/OHADA**, adopted on **8 June 2017** and effective from
**1 January 2018** under article 9. The facsimile is reproduced by
OHADA.com, a secondary host. Authenticity and byte equality against an
issuer copy and Gazette publication date have not been established. The
issuer’s linked attachments could not be downloaded in this pass. Its
publication notice corroborates the adoption date,
commencement and broad scope. This does not establish later amendments,
current tool editions or national professional eligibility.
[Regulation, article 9, PDF page 3](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=3),
[issuer’s notice](https://www.ohada.org/mise-en-ligne-du-reglement-portant-harmonisation-des-pratiques-des-professionnels-de-la-comptabilite-et-de-l-audit-dans-les-etats-membres-de-l-ohada/)

### Audit standards and other professional engagements

Articles 1 and 2 cover professional standards, practical guides, ethics and
quality assurance across the member states. Article 2 expressly leaves the
organisation and functioning of professional accountancy orders outside
this Regulation. It does not replace national registration rules or establish
that a particular practitioner may act.
[Regulation, articles 1 and 2, PDF page 1](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=1)

Article 3 requires professionals performing statutory or contractual audits
in a member state to apply international auditing standards, called ISA and
described in the original text as published by IFAC. The auditor must comply
with the AUDCIF and all ISA relevant to the audit. For statutory auditors,
the AUSCGIE’s additional requirements and application rules also apply.
These performance requirements are separate from the legal-form tests that
determine whether an auditor must be appointed.
[Regulation, article 3, PDF pages 1 and 2](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=1)

Article 4 establishes Tome 1 for audit and statutory audit. It does not
replace reading the full relevant ISA, their application material and the
state’s applicable legal and regulatory provisions. Article 5 establishes
Tome 2 for other professional engagements, including accounts presentation,
limited reviews, related services and assurance engagements. It also recalls
additional AUSCGIE requirements where applicable. Its use does not replace
reading the full relevant standards and application material.
Do not classify every professional engagement as an ISA audit.
[Regulation, articles 4 and 5, PDF page 2](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=2)

### Ethics, quality assurance and tool versions

Article 6 establishes an OHADA ethics code for contractual and statutory
audit, other professional engagements and professional accountants working
in enterprises and other organisations. It says the code draws on the IFAC
ethics code and the AUSCGIE. That wording does not by itself establish
automatic adoption of the latest international code or identify the current
OHADA code edition.
[Regulation, article 6, PDF pages 2 and 3](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=3)

Article 7 requires the professional orders, individually or collectively,
to establish a quality assurance mechanism addressing the ISA, relevant
AUSCGIE duties and article 6 ethics rules. Professionals implement the
system under the quality assurance manual. The Regulation does not supply
a detailed inspection programme or verify its operation in a particular state.
Article 8 provides for regular updating of the articles 4 to 7 tools by the
Permanent Secretariat on the Commission’s recommendation. Obtain the
applicable guides, code and manual and trace their versions before use.
[Regulation, articles 7 and 8, PDF page 3](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=3)

For a hypothetical engagement after 1 January 2018, a contractual audit
falls within original article 3 even though it is not a statutory audit.
A limited review is a different engagement addressed by article 5. First
record the engagement type, territory, period, applicable full standards,
additional statutory duties, professional registration and tool editions.
This example does not establish current-law applicability or practitioner
eligibility. Later law, complete standards and tools, national implementation
and qualified local review remain outstanding. These selected provisions
do not establish complete reporting coverage or audit readiness.

## Retrieved OHADA ethics and quality tools

**Evidence period:** issuer-hosted files retrieved on 12 November 2026,
with their stated historical bases. The issuer's 7 March 2018 notice reports
CNC adoption of the named professional tools on 8 December 2017. That
notice does not identify the adopted files by hash. The current tools page
links editable originals; retrieval does not establish that these bytes
equal the adopted versions or remain operative for a later engagement.
[OHADA adoption notice](https://www.ohada.org/mise-en-ligne-des-outils-d-harmonisation-des-pratiques-des-professionnels-de-la-comptabilite-et-de-l-audit/)
[Issuer tools page](https://www.ohada.org/en/practical-tools-for-implementing-isa-standards/)

### The retrieved Code's stated basis

The retrieved Code's preamble identifies a May 2015 IESBA basis, including
April 2015 changes applicable from April 2016. Footers say 'Version après
atelier'. These labels do not establish final adoption or current OHADA
applicability.
[Issuer-hosted Code, preamble and footer, rendered page 5](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Section 100 covers principles and their application in practice and
business. Its 5 principles are integrity, objectivity, professional
competence and due care, confidentiality and professional behaviour.
Threats include self-interest, self-review, advocacy, familiarity and
intimidation. It requires assessing threats and appropriate safeguards.
If threats cannot be reduced acceptably, the professional must refuse
or cease the service, or resign in the employed-professional case.
[Code, section 100, rendered pages 6 and 7](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Section 140 continues confidentiality after the relationship ends.
Exceptions include legally permitted disclosure authorised by the client
or employer, disclosure required by law and a professional duty or right
to disclose. Verify the actual authority and recipient; this selected
summary does not establish complete confidentiality or independence
compliance.
[Code, section 140, rendered pages 10 and 11](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Quality manual and remaining verification

The retrieved quality manual is labelled January 2018. Its preamble
describes a system based on ISA, ISA 220 and ISQC 1 and an institutional
quality assurance arrangement proposed for implementation. These words
do not establish that an order operates that arrangement, or identify
the quality-management requirements applicable to a current engagement.
The Parts 1 and 2 file ends with a Part 3 cover and a following page with
no substantive text; the complete substantive Part 3 has not been
verified here.
[Issuer-hosted quality manual, cover, preamble and ending, rendered pages 1, 5, 37 and 38](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Manuel-Syste%CC%80me-Assurance-Qualite%CC%81-Partie-1-et-2.docx)

Tomes 1 and 2 were also retrieved from the issuer's tools page.
Their substantive provisions and applicable editions remain unverified
in this addition. Obtain the complete standards, guides, code and quality
manual applicable to the actual period, trace adoption and later
amendments, and check national professional and sector rules. An issuer
notice about cooperation or a meeting agenda cannot substitute for an
adopted instrument. Qualified local review, actual professional eligibility
and complete reporting coverage remain outstanding.

## Additional provisions in the retrieved OHADA Code

Use these selected provisions as a historical reference when checking a
professional engagement or financial reporting role. The issuer-hosted Code
retrieved on 12 November 2026 states a May 2015 IESBA basis, including
April 2015 changes applicable from April 2016, and carries 'Version après
atelier' footers. Those dates do not establish the commencement, final adopted
identity or current applicability of this OHADA file.
[Code, preamble and footer, rendered page 5](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Professionals in practice

Section 200 prohibits knowingly undertaking activities incompatible with the
fundamental principles. Section 210 requires assessing threats when accepting
a client or engagement or changing appointments, with appropriate safeguards.
If client-acceptance threats cannot be reduced acceptably, refuse the
relationship. It recommends periodic reconsideration for recurring
engagements. Assess the team's ability to obtain the necessary competence
and the justification for relying on an expert. Assess threats from accepting a replacement before knowing all relevant facts.
Direct contact with the incumbent or other means may be needed; refuse if
threats cannot be eliminated or reduced acceptably. The incumbent's
confidentiality duties and the legal context still apply.
[Code, sections 200 and 210, rendered pages 12 and 13](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Section 220 requires identifying conflicts before accepting a new relationship
or engagement, assessing threats and appropriate safeguards and refusing or
resigning if threats cannot be eliminated or reduced acceptably.
Assess the necessary disclosure and whether explicit client consent is
needed; protect confidentiality. Section 230 treats a second opinion based
on different facts or insufficient evidence as a possible competence and
due-care threat. If communication with the incumbent is refused, assess
whether giving the opinion is appropriate in the circumstances.
[Code, sections 220 and 230, rendered pages 13 and 14](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Section 240 addresses low fees that threaten performance to applicable
standards and possible threats from contingent and referral fees; assess
threats and safeguards. Section 250 prohibits discrediting the profession
when promoting services. Section 260 requires assessing gifts and hospitality.
For offers a reasonable informed third party would regard as trivial,
it permits a conclusion that they arise in the ordinary course of business
without specific intent to influence decisions or obtain information. Refuse offers where threats cannot be eliminated
or reduced acceptably.
[Code, sections 240 to 260, rendered pages 15 and 16](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Section 270 permits custody of client money or assets only where law
authorises it, subject to additional legal duties. Keep those assets
separate, use them only for their intended purpose, account to entitled
persons and comply with applicable custody and accounting rules. Enquire
appropriately into their origin and the related legal obligations.
Section 280 requires assessing objectivity threats from interests or
relationships and applying appropriate safeguards.
[Code, sections 270 and 280, rendered pages 16 and 17](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Professionals employed in business

Sections 300 and 310 address incompatible activities and pressures threatening
the fundamental principles. Section 320 requires the responsible preparer or
approver to ensure general purpose financial statements comply with applicable
reporting standards. Assess pressure to associate with misleading information
and apply safeguards. If threats cannot be reduced acceptably, refuse to be
or remain associated; take steps to disassociate on discovering an unwitting
association.
[Code, sections 300 to 320, rendered pages 43 and 44](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Section 330 requires sufficient specific training or experience, or the
ability to acquire it, for significant tasks. Do not intentionally misrepresent
competence to the employer; seek appropriate expert advice and assistance when needed.
Section 340 requires assessing threats from financial interests and prohibits
manipulating information or using confidential information for personal
advantage. Section 350 requires assessing offered inducements by their nature,
value and intention and applying appropriate safeguards. It prohibits offering
inducements to influence another's professional judgement improperly and
requires following the Part A conflict-resolution principles and
recommendations when the employer pressures the professional to offer an
unethical inducement.
[Code, sections 330 to 350, rendered pages 45 and 46](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Remaining verification

This selection does not complete the Code. The selected independence and
definitions references below do not reconcile all provisions or exceptions. Establish
the final adopted files, later amendments, requirements for the actual period,
national and sector rules and the professional's eligibility. Complete
financial reporting, audit and quality-management coverage and qualified
local review remain outstanding.

## Retrieved OHADA Code audit-independence reference

Check independence against the adopted rules for the actual engagement.
The following is a selected historical reference to section 290 of the
issuer-hosted Code retrieved on 12 November 2026. Its preamble states a
May 2015 IESBA basis, including April 2015 changes applicable from April 2016;
the file also contains later editorial references and 'Version après atelier'
footers. Neither retrieval nor these labels proves final adopted-byte identity,
OHADA commencement or current applicability.
[Code, preamble and section 290, rendered pages 5, 17 and 26](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Framework and engagement boundaries

Section 290 requires independence of mind and in appearance. Identify and
assess threats and apply necessary safeguards. If threats cannot be reduced
acceptably, eliminate the circumstances or relationship, refuse the audit or
end it. Network firms must be independent of other network firms' audit
clients. The file's public-interest-entity discussion contains a workshop
decision referring to accounting rules then under revision; verify the
applicable classification rather than treating that discussion as a current
national classification.
[Code, rendered pages 17 and 18](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

For listed clients, the stated client boundary includes all related entities,
unless otherwise indicated; for other clients it includes controlled related
entities. Document independence conclusions, supporting discussions, safeguards
and significant judgements that safeguards are unnecessary. Independence
covers the engagement and financial-statement periods, with assessment of
earlier relationships and services. A merger or acquisition requires reassessment.
Where a prohibited interest cannot reasonably end by the transaction date,
continued appointment at governance's request has conditions: end it as soon
as reasonably possible and within 6 months, exclude the affected person from
the audit team and engagement quality review and implement and discuss
appropriate transitional measures.
[Code, rendered pages 19 to 21](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

A breach requires ending, suspending or eliminating its cause and addressing
its consequences. Check legal requirements, notify relevant firm personnel, assess the breach
and address governance and regulatory communications as specified. Document
the response. Ending the audit
may be necessary; the text also addresses remedial action and specific
conditions for inadvertent financial-interest breaches.
[Code, rendered pages 21 to 23](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Interests and employment

The firm, audit-team members and their immediate families must not hold direct
financial interests or material indirect interests in the audit client.
Other partners, staff and known relationships have further conditions.
Loans or guarantees from an audit client that is a bank or financial institution
are prohibited outside normal lending procedures, terms and conditions.
Loans or guarantees from an audit client that is neither a bank nor a financial
institution, and loans or guarantees to any audit client, have exceptions
requiring immateriality for all specified parties; ordinary deposit and brokerage accounts have a normal commercial
terms condition. Close business, family and personal relationships require
their separate prohibition or threat assessment.
[Code, rendered pages 22 to 24](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Employment negotiations must be notified under firm procedures. The file's
public-interest-entity examples require, after a key audit partner leaves
that role, the client to have issued audited statements covering at least
12 months, without that partner on the relevant audit team; a former firm
chief executive has a separate 12-month condition after leaving that role.
Temporary staff assignments must be short, avoid prohibited services and
leave management responsibility with the client. Recent client employment
and service as a client director or executive have separate restrictions.
Reconcile these Code examples with applicable statutory appointment and
employment restrictions.
[Code, rendered pages 24 to 26 and 34 to 35](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

For a public-interest audit, the file limits service as a key audit partner
to 7 years and states a 2-year cooling period, changing to 5 years for
financial years beginning on or after 15 December 2018. It refers to an
IESBA May 2017 staff Q&A for transition details, not verified here.
The defined role includes the engagement partner, quality reviewer and
other audit partners making key decisions or significant judgements.
These are the file's statements, not confirmation of the rule for a current
appointment.
[Code, rendered pages 26 and 47](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Other services and fees

The firm must not assume client management responsibility. Client management
must retain significant decisions, competent oversight, evaluation of results
and responsibility for resulting actions. The file distinguishes services
and public-interest status:

- Routine or mechanical bookkeeping for other audit clients requires reducing
  self-review threats to an acceptable level. Public-interest clients have a prohibition, with a
  limited division/related-entity exception involving routine work, staff
  outside the audit team and the stated materiality conditions.
- Valuations for other clients are prohibited where both material and highly
  subjective; public-interest clients have a material-impact prohibition.
- Tax-return preparation generally avoids an independence threat where management
  retains responsibility and significant judgements. Tax calculations for
  accounting entries require safeguards for other audit clients; material
  entries for public-interest clients are prohibited. Tax planning requires
  assessment and safeguards. Court representation on material tax disputes
  is prohibited, with an ongoing advisory role distinguished.
- Internal-audit work must not involve management responsibility. Specified
  material financial-reporting IT design or implementation requires safeguards
  for other clients and is prohibited for public-interest clients.
- Litigation support involving valuations follows valuation restrictions.
  Other litigation support and transaction legal advice require assessment.
  Legal representation has a materiality distinction and serving as general
  counsel is prohibited.
- Recruitment requires safeguards, with specified public-interest leadership
  recruitment prohibited. Corporate-finance advice has assessment requirements,
  a prohibition where the stated accounting-treatment and material-impact
  conditions make self-review threats unacceptable and a ban on promoting,
  dealing in or underwriting the audit client's shares.

[Code, rendered pages 26 to 31](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Fee dependence requires assessment. For a public-interest client and related
entities exceeding 15% of firm fees for 2 consecutive years, disclose this
to governance, discuss safeguards and implement appropriate safeguards.
The file requires assessment and review before the opinion where the threshold
is significantly exceeded or exceeded each year. The file expects the firm to require payment
before issuing the audit report; assess persistent unpaid fees and safeguards. Contingent audit fees are prohibited; non-assurance contingent
fees have specified prohibitions and other cases require threat assessment and implementation of safeguards.
Key audit partners must not be evaluated or remunerated based on their ability to sell
non-assurance services to their audit clients; ordinary partner profit-sharing
arrangements are not intended to be prohibited.
[Code, rendered pages 31 and 32](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Remaining verification

The file also addresses trivial gifts, actual or probable litigation and
restricted-use reports. It refers restricted-report modifications to IESBA
paragraphs 290.500–290.514; those underlying provisions remain unverified.
Its OHADA supplement reproduces statutory eligibility and incompatibility
rules, including 5-year restrictions and related-entity extensions.
Use the complete applicable Act for appointment checks: the shorter article
698 extract on page 23 omits items included on page 34.
[Code, rendered pages 23 and 33 to 35](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

This selection does not establish complete independence compliance.
Reconcile definitions, exceptions, referenced IESBA provisions, the operative
statutes, later amendments, national and sector rules and actual professional
eligibility. The selected section 291 and definitions reference below does
not complete the remaining Code provisions. Complete reporting and
quality-management requirements, adopted versions and qualified local review
remain outstanding.

## Retrieved OHADA Code other-assurance and definitions reference

The following is a selected historical reference to section 291 and definitions in the issuer-hosted Code retrieved on 12 November 2026. Its preamble states a May 2015 IESBA basis, including April 2015 changes applicable from April 2016; workshop footers and later editorial references remain. Final adopted-byte identity, OHADA commencement and current applicability are unproved. [Code, rendered pages 5, 35, 47](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Other assurance: scope and independence

Section 291 expressly concerns assurance other than audits and limited reviews. It distinguishes assertion-based engagements, where the responsible party measures or evaluates the subject matter and supplies an assertion to users, from direct-reporting engagements, where the practitioner measures or evaluates it or obtains a responsible-party representation unavailable to users. The subject-matter information reaches users through the assurance report in the latter case. Both involve a practitioner, responsible party and intended users. [Code, rendered pages 35, 37](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

The firm and team must be independent of the responsible party: the party responsible for subject-matter information in an assertion-based engagement, potentially also responsible for the subject matter, or the subject matter in direct reporting. The file identifies restricted relationships with client directors, executives and people significantly influencing that information. In direct reporting, assess threats the firm has reason to believe arise from network-firm interests and relationships. For multiple responsible parties, assess each relationship for a threat that is more than trivial and inconsequential in the information's context. [Code, rendered pages 35, 36](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Modified independence requirements for certain reports restricted in use or distribution require intended users to understand the purpose, subject-matter information and report limitations and explicitly agree to the modifications. This passage does not establish a general exemption from independence. [Code, rendered page 35](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Document independence conclusions and supporting discussions, threats and necessary safeguards, including substantial analysis concluding that safeguards are unnecessary because a threat is already acceptable. Independence covers both the engagement and subject-matter periods. For a breach, end, suspend or eliminate the offending interest or relationship, address consequences, comply with applicable legal duties and consider customary or required regulatory communication. Assess significance and objectivity; end the engagement if necessary. Where remedial action is considered satisfactory, communicate the breach and proposed action to the responsible party or governance. Document the breach, actions, discussions and regulatory exchanges. [Code, rendered pages 36, 37](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Independence includes mind and appearance. Identify and assess threats and apply necessary safeguards. If threats cannot be reduced acceptably, eliminate the circumstances or relationship, refuse the engagement or end it. [Code, rendered page 37](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Interests, relationships and services

The firm, assurance-team members and immediate family must not hold direct or material indirect financial interests in the client. The prohibition also specifies an entity holding a material direct or indirect financial interest in an entity with a majority holding in that client. Assess known interests held by other partners, staff, their immediate families and people closely connected to team members. For prohibited interests received by the firm, team members or their immediate families through inheritance, gift or merger, dispose immediately, or reduce an indirect holding until the remainder is immaterial. [Code, rendered pages 37, 38](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Loans or guarantees to the firm, team or immediate family from a client that is a bank or financial institution cannot be accepted outside normal lending procedures, terms and conditions. Loans or guarantees to them from a client that is neither a bank nor a financial institution require immateriality to all identified parties. Their loans or guarantees to any assurance client also require immateriality to all identified parties. Ordinary commercial terms are required for the stated no-threat treatment of deposit or brokerage accounts. [Code, rendered page 38](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Close business relationships have an insignificance exception whose wording refers to the firm, client or its management; reconcile that wording before applying it. Ordinary competitive purchases generally create no threat, but their nature or scale can do so. A person cannot join the team if immediate family is a client director, executive or employee significantly influencing accounting records or financial statements. Other specified close personal relationships require threat assessment and safeguards where necessary. [Code, rendered pages 38, 39](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

When a former team member or partner joins the client in a specified senior or influential role, assess familiarity or intimidation and apply necessary safeguards; the person must cease participation in the firm's business or professional activities. Policies must require team members to notify the firm when entering employment negotiations with the client; assess threats and apply necessary safeguards on notification. A person holding a specified client role during the assurance-report period cannot join the team. Earlier employment may create threats for which safeguards must be implemented. [Code, rendered pages 39, 40](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

The firm cannot assume management responsibilities within the assurance engagement. A management responsibility undertaken in another client service must be unrelated to both the subject matter and subject-matter information. The firm must ensure management retains significant judgements and decisions: the client designates a competent, experienced person to take responsibility for decisions and supervision of the work, evaluates the work's adequacy and accepts responsibility for resulting action. Other services concerning subject-matter information require assessment of involvement and whether safeguards can reduce unacceptable self-review threats. [Code, rendered pages 40, 41](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Fees, gifts and disputes

A large proportion of firm fees or an individual partner's managed revenue from an assurance engagement creates a threat requiring assessment and safeguards where necessary. The file expects the firm to require payment before issuing the assurance report; if fees remain unpaid afterwards, assess threats and apply necessary safeguards. [Code, rendered page 41](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Direct or indirect contingent fees for assurance are prohibited. For another service to the assurance client, contingent fees are prohibited where its outcome and fee depend on a present or future judgement concerning a matter significant to the subject-matter information; safeguards cannot reduce that threat acceptably. Other contingent-fee cases require threat assessment and implementation of safeguards. Gifts from the client are prohibited for the firm and team unless trivial and inconsequential. Actual or probable litigation requires assessment and necessary safeguards. [Code, rendered pages 41, 42](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

### Selected definitions affecting scope

The glossary's firm includes a sole practitioner, partnership or company and controlling or controlled entities. A network is a larger cooperative structure clearly directed to profit/cost sharing or shared ownership, control, management, quality policies, strategy, brand or significant professional resources; a network firm is a firm or entity in that network. [Code, rendered pages 47, 51](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

An engagement team includes partners and staff working on the engagement and people engaged by the firm or a network firm to perform assurance procedures, excluding engaged external experts. The separate assurance-team definition also reaches people within the firm directly influencing the outcome, including relevant supervision/remuneration, technical consultation and quality-control roles. Audit and review teams have their own definitions, including direct influencers in network firms. These distinctions need reconciliation before deciding the reach of a particular prohibition. [Code, rendered pages 48, 49](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Immediate family means a spouse or equivalent and dependants. Close family means parents, children and siblings outside immediate family. Direct financial interests include directly owned and controlled interests, including discretionary third-party management, and beneficial interests through intermediaries whose investment decisions can be controlled or influenced. Indirect interests involve beneficial ownership without that control or influence. Financial interests also include debt instruments, acquisition rights/obligations and directly linked derivatives. Contingent fees depend on a transaction outcome or service result; fees fixed by courts or other public authorities are excluded from that definition. [Code, rendered pages 49, 50](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Listed entities are those whose shares, units or bonds are listed or traded on a recognised exchange or equivalent body. A listed audit client includes its related entities; an unlisted audit client includes related entities it directly or indirectly controls. Public-interest entities include listed entities and entities designated by law/regulation or required to follow listed-entity audit-independence rules. This definition does not establish any area's current classification. [Code, rendered pages 47, 48](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Related entities include: a controller for which the client is material; a direct investor with significant influence and a holding material to it; an entity the client controls; an investee in which the client or its controlled entity has a direct interest conferring significant influence, with the stated materiality to the client and controlled entity; and a sister entity where both it and the client are material to their common controller. Preserve these direction and materiality conditions. [Code, rendered page 48](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

Assurance is a conclusion intended to increase the confidence of intended users other than the responsible party in subject-matter evaluation against criteria. An audit is reasonable assurance about financial statements under the applicable framework and may be statutory. A limited review uses procedures short of audit evidence and a conclusion on whether anything has come to the practitioner's attention indicating material non-conformity with the applicable framework. The glossary defines a professional accountant by IFAC-member-body membership; that is not proof of national eligibility. An engagement partner must have appropriate professional, legal or governmental authority where needed. An engagement quality-control review objectively assesses significant judgements and report conclusions before or at report issue. [Code, rendered pages 47, 50, 51](https://www.ohada.org/wp-content/uploads/2020/10/OHADA-Code-de%CC%81thique-des-professionnels-de-la-comptabilite%CC%81-et-de-laudit.docx)

This selection does not complete the glossary, Code, operative-law checks or reporting coverage. Reconcile final adoption, amendments, underlying IESBA references, national/sector eligibility, actual-period standards and qualified local review before reliance.

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
