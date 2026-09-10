---
name: cd-vat-gst
description: "Source-cited draft: value-added tax (TVA) for the Democratic Republic of the Congo, tax year 2025. Covers the 16% standard rate, the 8% reduced rate on listed foodstuffs and domestic air tickets, the zero rate on exports, the CDF 80,000,000 registration threshold and the option to register below it, the monthly return due on the fifteenth, the normalised electronic invoice, the restricted list of refundable credits and the credit carry-forward. Trigger on \"DRC VAT\", \"TVA RDC\", \"taxe sur la valeur ajoutée Congo\", \"DGI VAT return\", \"facture normalisée\", \"Congolese VAT threshold\". Read from the Code des Impôts; unverified, pending local-accountant review."
jurisdiction: CD
category: international
tax_year: 2025
tax_year_notes: "The rates in art. 35 are as amended by Loi de Finances n° 21/029 of 31 December 2021 and n° 22/071 of 28 December 2022; the threshold in art. 14 as amended by L.F. n° 14/002 of 31 January 2014 and n° 15/021 of 31 December 2015. The Code des Impôts consolidated to 2023 is the text read here."
last_updated: 2026-09-10
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DR Congo VAT / GST

> **The reduced rate was wrong by a factor of eight.** The previous version put
> the DRC's reduced VAT rate at **1%**, citing a commercial advisory firm. Article
> 35 of the Ordonnance-Loi instituting the tax, as amended in 2021 and 2022, sets
> it at **8%** — and the DGI's own August 2025 taxpayer leaflet says 8% too. Six
> of the seven citations in the previous version pointed at the same commercial
> blog post; none pointed at the statute. Everything below was read from the
> **Code des Impôts** as published by the DGI.

## 1. The rates — Ordonnance-Loi n° 10/001, art. 35

Article 35, *"modifié par la L.F n° 21/029 du 31 décembre 2021 et par la L.F n°
22/071 du 28 décembre 2022"*, sets three rates and no others.

| Rate | Applies to |
| ---: | --- |
| **16%** | *"taux normal : 16% applicable à toutes les opérations imposables à l'exclusion des opérations soumises au taux réduit ou au taux zéro"* |
| **8%** | A **tariff-line schedule** printed in the article itself — fresh, chilled and frozen bovine, porcine and poultry meat and edible offal; frozen tilapia and horse mackerel; dried and salted cod, tilapia, catfish, carp, eel, herring, anchovy, sardine and mackerel; husked (cargo/brown) rice and semi-milled or milled rice; and further lines — **plus the sale of air tickets on domestic air traffic** |
| **0%** | *"applicable aux exportations et opérations assimilées"* |

_(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 35 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_

- **The 8% band is a closed tariff list, not a description** — The article
  enumerates the reduced-rate goods by **customs tariff position** (02.01, 02.02,
  02.03, 02.06, 02.07, 0303.23.00, 0305.51.00, 1006.20.00, 1006.30.00 and so on),
  each with its own `8%` entry. A general phrase such as "essential goods and
  agricultural inputs" — what the previous version offered — is not the test; the
  tariff position is  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 35 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Domestic air tickets are in the reduced band** — *"à la vente des billets
  d'avion sur le trafic aérien national"*. This limb has nothing to do with
  foodstuffs and was absent from the previous version entirely  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 35 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **The DGI's own leaflet agrees** — §VI of the DGI's August 2025 *La Taxe sur la
  Valeur Ajoutée — Notions essentielles à retenir*: *"1. Taux normal : 16%
  applicable à toutes les opérations imposables. 2. Taux réduit : 8% applicable à
  certains produits de première nécessité ainsi que la vente des billets d'avion
  sur le trafic aérien national. 3. Taux : 0% applicable aux exportations"*  _(DGI, La Taxe sur la Valeur Ajoutée — Notions essentielles à retenir, août 2025, §VI — https://dgi.gouv.cd/wp-content/uploads/2025/10/TVA-CORRIGE.pdf)_

## 2. Who is a taxable person — art. 14

- **The threshold is CDF 80,000,000, and it is inclusive** — *"Les personnes
  morales et physiques sont assujetties à la taxe sur la valeur ajoutée
  lorsqu'elles réalisent un chiffre d'affaires annuel **égal ou supérieur à**
  80.000.000 de Francs congolais."* The previous version said "exceeding CDF
  80,000,000", which wrongly puts a business at exactly 80,000,000 outside the
  tax. The statute puts it inside  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 14 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Turnover means turnover excluding VAT, measured on the prior year** — For
  existing businesses the test is the **previous year's** turnover; for new
  businesses, **forecast** turnover  _(Décret n° 011/42 du 22 novembre 2011, arts. 42 and 43 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Registering below the threshold binds you for two years** — A person under the
  threshold *"peut opter pour le régime de la taxe sur la valeur ajoutée"* by
  express application to the DGI. The option is *"définitive pendant deux ans
  suivant l'exercice de l'option"*, unless the DGI revokes it. The previous
  version described voluntary registration without the lock-in  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 14 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Falling below the threshold does not deregister you immediately** — *"l'assujetti
  conserve sa qualité les deux années suivant celle de la constatation de la
  diminution de son chiffre d'affaires"*  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 14 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **The Minister of Finance can move the threshold by arrêté** — so CDF 80,000,000
  is current only as at the last arrêté, and a reviewer should confirm no later
  one has moved it  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 14, final paragraph — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Imports are taxable at any value** — the threshold does not shelter them  _(Décret n° 011/42 du 22 novembre 2011, art. 45 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Public-law bodies are taxable persons, with a carve-out** — The State,
  Provinces, decentralised territorial entities and public bodies are subject to
  VAT, but *not* for *"l'activité de leurs services administratifs, sociaux,
  éducatifs, culturels et sportifs, lorsque leur non-assujettissement n'entraîne
  pas de distorsions dans les conditions de la concurrence"*  _(DGI, La Taxe sur la Valeur Ajoutée — Notions essentielles à retenir, août 2025, §II — https://dgi.gouv.cd/wp-content/uploads/2025/10/TVA-CORRIGE.pdf)_

> **[RESEARCH GAP — the liberal professions.]** The DGI's August 2025 leaflet
> states that members of the **liberal professions** are subject to VAT
> *"sans considération de leur chiffre d'affaires"* — regardless of turnover. That
> rule is **art. 44 of Décret n° 011/42**, and the consolidated Code prints it in
> square brackets marked ***"(Disposition désuète conformément à la L.F. n° 15/021
> du 31 décembre 2015)"*** — a provision the Code itself flags as spent. So the
> authority's current leaflet asserts a rule the authority's own consolidated code
> marks as superseded. **This guide does not state either way.** A reviewer must
> settle whether a Congolese architect, lawyer or accountant below CDF 80,000,000
> must register.
> _(Décret n° 011/42 du 22 novembre 2011, art. 44, and DGI leaflet août 2025 §II — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_

## 3. The taxable base

- **Everything received in consideration, plus subsidies and other taxes** —
  *"toutes les sommes, valeurs, biens ou services perçus en contrepartie de
  l'opération, y compris les subventions ainsi que tous les frais, impôts, droits
  et taxes de toute nature y afférente, à l'exclusion de la TVA elle-même"*. Note
  that **subsidies are in the base** and **other taxes are in the base** — only the
  VAT itself is out  _(DGI, La Taxe sur la Valeur Ajoutée — Notions essentielles à retenir, août 2025, §V — https://dgi.gouv.cd/wp-content/uploads/2025/10/TVA-CORRIGE.pdf)_
- **Self-supplies are taxable** — the charge reaches *"les livraisons de biens à
  soi-même, les prestations de services à soi-même et les importations"* as well as
  ordinary supplies  _(DGI, La Taxe sur la Valeur Ajoutée — Notions essentielles à retenir, août 2025, §IV — https://dgi.gouv.cd/wp-content/uploads/2025/10/TVA-CORRIGE.pdf)_
- **Territoriality** — a sale is in the DRC when the goods are on national
  territory at the moment of sale; immovable works when carried out in the
  country; services when the service rendered, the right assigned or the item hired
  is *used or exploited* in the country  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 22 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_

## 4. Non-established suppliers — a fiscal representative, not a reverse charge

The previous version described VAT on services from non-established providers as
being *"accounted for by the DRC recipient under a reverse-charge mechanism
(approx — confirm)"*. That is not the mechanism the statute uses.

- **The non-resident must appoint an approved representative** — A taxable person
  established or domiciled outside the DRC *"est tenu de désigner par lettre
  légalisée ou notariée, adressée à l'Administration des Impôts, un représentant
  agréé, résidant sur le territoire national, qui est **solidairement responsable**,
  avec lui, du paiement de la taxe"*  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 23 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **The customer pays only if no representative is appointed** — *"En cas de non
  désignation d'un représentant, la taxe sur la valeur ajoutée et, le cas échéant,
  les pénalités y afférentes sont payées par la personne cliente."* Customer
  liability is the **default remedy**, not the primary rule  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 23 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **One representative only** — a non-established taxable person may designate a
  single representative for all its DRC operations  _(Décret n° 011/42 du 22 novembre 2011, art. 40 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_

## 5. Returns, payment and the normalised invoice

- **Monthly, by the fifteenth, in duplicate, with payment** — *"Tout redevable de
  la taxe sur la valeur ajoutée est tenu de souscrire chaque mois, au plus tard le
  quinze du mois qui suit celui de la réalisation des opérations, une déclaration
  conforme au modèle prescrit par l'Administration. La déclaration doit être
  souscrite **en double exemplaire** et accompagnée du paiement de la taxe."* The
  previous version had the frequency and the date right and cited a commercial blog
  for both; the duplicate-copy and simultaneous-payment requirements were missing  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 60 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **A nil month is still a filing month** — *"La déclaration doit être souscrite
  même si aucune opération imposable n'a été réalisée au cours du mois concerné.
  Elle doit, dans ce cas, être revêtue de la mention « Néant »."*  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 60 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Imports are declared and paid before the goods are released** — *"En cas
  d'importation, la taxe sur la valeur ajoutée doit être déclarée et versée avant
  l'enlèvement de la marchandise"*, and at the border it is collected by **Customs**,
  not the DGI  _(Ordonnance-Loi n° 10/001 du 20 août 2010, arts. 61 and 62 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **The normalised electronic invoice is already obligatory, not a rollout** — Art.
  58, as amended by L.F. n° 22/071 of 28 December 2022, requires a taxable person
  supplying another taxable person to deliver *"une **facture normalisée produite
  par les dispositifs électroniques fiscaux** ou un document en tenant lieu"*. The
  previous version called this an "(approx — confirm)" modernisation plan  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 58 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **And it is a condition of deducting input tax** — art. 38 requires the tax to
  appear *"sur une facture normalisée ou un autre document en tenant lieu, dûment
  délivré par un assujetti et mentionnant son numéro impôt"*; on import, on the
  customs entry; on a self-supply, on a self-billed normalised invoice. Holding a
  non-compliant invoice costs the deduction  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 38 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Export deductions are not final until the export is proved** — deductions
  relating to exports become definitive only once the export is established by
  **customs documents** and by the documents evidencing **repatriation of the
  funds** under exchange-control rules  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 39 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **VAT mentioned on an invoice is owed whether or not you are registered** — art.
  59: any person who states VAT on an invoice is liable for it *"du seul fait de sa
  mention"*, and the recipient may not deduct it  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 59 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_

## 6. Credits and refunds — the default is carry-forward, not repayment

- **An excess of input tax is a credit carried forward, and it is neither
  refundable nor assignable** — art. 63: the excess *"constitue un crédit d'impôt
  imputable sur la taxe exigible du ou des mois suivants jusqu'à l'épuisement. Le
  crédit d'impôt **ne peut pas faire l'objet d'un remboursement** au profit de
  l'assujetti et ne peut être cédé."* The implementing decree repeats it at art.
  140, adding *"ni être cédé à un tiers"*  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 63, and Décret n° 011/42 du 22 novembre 2011, art. 140 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Repayment is confined to a closed list** — art. 64 allows a refund claim, on
  express application to the DGI, only to: **exporters**; **enterprises making heavy
  investments**; **mining and petroleum enterprises in the research or the
  development-and-construction phase**; enterprises **ceasing activity**; and
  **public establishments and public enterprises wholly owned by the State** whose
  invoiced VAT was withheld at source  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 64 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **"Heavy investment" has a figure** — *"les immobilisations corporelles acquises
  à l'état neuf nécessaires à l'exploitation de l'entreprise et dont la valeur du
  projet est au moins égale à **1.000.000.000,00 de Francs congolais**"*. The
  Minister of Finance may readjust this amount by arrêté  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 64 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **An exporter's refund is capped month by month** — the amount refundable is
  limited to VAT computed **at the standard rate on the month's exports**  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 64 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Extension and modernisation investments have a three-month window** — a claim
  limited to the tax borne on those fixed assets must be made within three months
  of acquisition  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 64 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_

## 7. Penalties specific to VAT

- **Late filing of a credit return: CDF 1,500,000 and 10% of the credit** — *"Le
  défaut de souscription d'une déclaration de la taxe sur la valeur ajoutée
  créditrice dans le délai est sanctionné par une amende de **1.500.000,00 Francs
  congolais** et par la perte d'une quotité de **10% du montant du crédit**"*  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 69 bis, created by L.F. n° 21/029 du 31 décembre 2021 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Late filing of a nil return: CDF 500,000**  _(Ordonnance-Loi n° 10/001 du 20 août 2010, art. 69 bis — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_
- **Improperly charged VAT: three times the tax** — art. 70, *"une amende fiscale
  égale au triple du montant de la taxe illégalement facturée"*; art. 71 applies
  the same triple penalty to a false invoice or a falsified invoice used to justify
  a deduction  _(Ordonnance-Loi n° 10/001 du 20 août 2010, arts. 70 and 71 — https://dgi.gouv.cd/wp-content/uploads/2025/10/CODE-DES-IMPOTS-2023.pdf)_

## 8. What this replaces

| The previous version said | The statute says |
| --- | --- |
| Reduced rate **1%** on "essential goods and agricultural inputs (approx — confirm scope)" | **8%**, on a **tariff-line schedule** printed in art. 35, **plus domestic air tickets** |
| Threshold: turnover **exceeding** CDF 80,000,000 | *"**égal ou supérieur à** 80.000.000"* — exactly 80,000,000 is **inside** the tax |
| Voluntary registration available below the threshold | True, but the option is **binding for two years** and falling below the threshold keeps you registered for **two more years** |
| Reverse charge on imported services (approx — confirm) | An **approved fiscal representative**, jointly and severally liable; the **customer** pays only where none is appointed |
| E-invoicing "being rolled out … (approx — confirm)" | The **facture normalisée from a fiscal electronic device** is already obligatory (art. 58) and is a **condition of deduction** (art. 38) |
| Monthly return by the 15th | Correct — and **in duplicate**, **with payment**, and **required even for a nil month** marked *« Néant »* |
| *nothing* | Excess input tax is a **carry-forward credit**, expressly **not refundable and not assignable** (art. 63) |
| *nothing* | Refunds are confined to a **closed list** (art. 64), with "heavy investment" defined as a project of at least **CDF 1,000,000,000** |
| *nothing* | Late credit return: **CDF 1,500,000 plus 10% of the credit** (art. 69 bis) |
| Six of seven citations to a commercial advisory blog | Every rule above is cited to the **Code des Impôts** published by the DGI |

The rates, threshold, representative rule, filing obligations, invoice
requirements, credit and refund rules and VAT penalties were read from the text
of Ordonnance-Loi n° 10/001 du 20 août 2010 and Décret n° 011/42 du 22 novembre
2011 as printed in the DGI's consolidated *Code des Impôts* (2023 edition). The
liberal-professions question in §2 is flagged as unresolved and was **not**
answered: the DGI's own 2025 leaflet and its own consolidated code disagree, and
nothing on the DGI site settles which governs. Rates set by *arrêté* rather than
by the Ordonnance-Loi — the threshold and the heavy-investment figure both being
adjustable that way — were not traced to a current arrêté.

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
