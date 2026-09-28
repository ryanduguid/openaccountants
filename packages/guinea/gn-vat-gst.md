---
name: gn-vat-gst
description: "Source-cited draft: VAT (TVA) for Guinea — the 18% rate, the 10th-of-the-month return under art. 373 sexies I, the Tableau des déductions, e-Tax/SAFIG e-invoicing under art. 383.V and the three-month refund condition, read from loi de finances 2025. Pending local-accountant review."
jurisdiction: GN
tax_year: 2025
last_updated: 2026-09-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guinea VAT / GST

## Value Added Tax (TVA)

> **The filing deadline was wrong, and the statute that fixes it is a 2025 one.**
> Every row below was sourced to a commercial VAT-guide site. **Loi de finances 2025
> (loi ordinaire L/2024/023/CNT)** re-enacts four of the CGI's VAT provisions
> outright, and the authority publishes its own rate table for the rate itself. What
> those sources give, and where they differ from this guide, is set out below.
>
> _([Loi de finances 2025](https://dgi.gov.gn/wp-content/uploads/2025/01/LOI-DE-FINANCES-INITIALE-2025_compressed.pdf); [Système Fiscal Guinéen au 31 mars 2021](https://dgi.gov.gn/wp-content/uploads/2021/04/Syst%C3%A8me-Fiscal-Guin%C3%A9en-mars-2021.pdf))_

- **VAT / GST — Value Added Tax (TVA) standard rate** — 18 percent, referred by the authority to **article 373 CGI (LF 2016 and 2017)** (Yes — Value Added Tax (TVA) applies at a standard rate)  _([Système Fiscal Guinéen au 31 mars 2021, row 15 — art. 373 CGI](https://dgi.gov.gn/wp-content/uploads/2021/04/Syst%C3%A8me-Fiscal-Guin%C3%A9en-mars-2021.pdf))_
- **Zero-rated supplies — exports and international transport** — The authority's table gives the 0% rate as applying to *"les exportations et les transports internationaux"*. **International transport was missing from this guide**, which gave exports alone percent  _([Système Fiscal Guinéen au 31 mars 2021, row 15 — art. 373 CGI](https://dgi.gov.gn/wp-content/uploads/2021/04/Syst%C3%A8me-Fiscal-Guin%C3%A9en-mars-2021.pdf))_
- **Exempt supplies** — Certain essential goods and services are exempt (no VAT charged, no input recovery)  _(Code Général des Impôts (CGI) — Taxe sur la Valeur Ajoutée (TVA) (https://quaderno.io/guides/guinea-vat-guide/))_
- **VAT registration threshold (turnover)** — GNF 1,000,000,000 annual turnover (businesses above this are subject to VAT). ⚠ The relief this describes is the **franchise regime of article 359 CGI**, which loi de finances 2025 identifies as the exception to monthly filing but does not restate; the threshold figure below remains unread against the article and its citation is a sales-tax-rate page that does not state a threshold at all (approx — confirm) GNF  _(Code Général des Impôts (CGI), art. 359 — franchise regime; figure as described at [tradingeconomics.com](https://tradingeconomics.com/guinea/sales-tax-rate))_
- **Return frequency** — Monthly  _([Loi de finances 2025, art. 13 — art. 373 sexies I CGI](https://dgi.gov.gn/wp-content/uploads/2025/01/LOI-DE-FINANCES-INITIALE-2025_compressed.pdf))_
- **⚠ Filing deadline — the 10th of each month, not 15 days after month-end** — **Article 373 sexies I CGI, as re-enacted by loi de finances 2025, article 13**: taxable persons who do **not** benefit from the article 359 franchise must complete and deliver a VAT return to their assessing office (*service de rattachement fiscal*) **"au plus tard le 10 de chaque mois"**. This guide gave 15 days after month-end — five days that do not exist. The heading under which the amendment sits is *Dispositions relatives à l'échéance de déclaration de la Déclaration Mensuelle Unique (DMU)*  _([Loi de finances 2025, art. 13 — art. 373 sexies I CGI](https://dgi.gov.gn/wp-content/uploads/2025/01/LOI-DE-FINANCES-INITIALE-2025_compressed.pdf))_
- **The return must carry a deductions schedule** — **Article 373 sexies V**, as amended by loi de finances 2025, article 25: the VAT return must be accompanied by a ***Tableau des déductions*** recapitulating, for the **preceding month's** deductible transactions: invoice numbers and dates; each supplier's name, business name, permanent Numéro d'Identification Fiscale and VAT registration key; the nature of the good or service; the payment date for services; the deductible VAT on each invoice; for imports, the customs VAT assessment slip; and purchases from both taxable and non-taxable persons in the preceding month  _([Loi de finances 2025, art. 25 — art. 373 sexies V CGI](https://dgi.gov.gn/wp-content/uploads/2025/01/LOI-DE-FINANCES-INITIALE-2025_compressed.pdf))_
- **Filing is electronic, on e-Tax/SAFIG, and that is now mandatory for everything** — **Article 373 sexies II** (loi de finances 2025, art. 25) requires taxable persons to use the declaration forms available online on the **e-Tax/SAFIG** platform. More broadly, **article 1001 bis I.2** provides that *"toutes les déclarations adressées à l'Administration doivent être communiquées par voie électronique"*, and I.1 gives emails between the administration and taxpayers the same probative value as paper. A document made available on e-Tax and notified by email is **deemed received five clear days after dispatch**  _([Loi de finances 2025, arts. 23 and 25 — arts. 1001 bis and 373 sexies II CGI](https://dgi.gov.gn/wp-content/uploads/2025/01/LOI-DE-FINANCES-INITIALE-2025_compressed.pdf))_
- **⚠ E-invoicing — invoices go to the portal or through the API** — **Article 383.V CGI, as amended by loi de finances 2025, article 27**: *"La facture est saisie manuellement sur le portail e-Tax, soit transmise automatiquement via l'API e-TVA de la plateforme SAFIG."* Guinea therefore operates invoice-level reporting with a manual portal route and an automatic API route. (The enacted text omits the first *soit* of the *soit … soit* pair; the either/or sense is not in doubt.) The DGI has run public information spots on *eFacturation* in Pular, Malinké and Kpelle  _([Loi de finances 2025, art. 27 — art. 383.V CGI](https://dgi.gov.gn/wp-content/uploads/2025/01/LOI-DE-FINANCES-INITIALE-2025_compressed.pdf); [dgi.gov.gn](https://dgi.gov.gn/))_
- **Refunds — three consecutive months of credit, and the claim must be electronic** — **Article 388.I CGI, as amended by loi de finances 2025, article 28**: every refund claim must be transmitted *"exclusivement de manière dématérialisée"* on e-Tax/SAFIG, by a taxable person within article 387.II **who has been in a VAT credit position for three (3) consecutive months**  _([Loi de finances 2025, art. 28 — art. 388.I CGI](https://dgi.gov.gn/wp-content/uploads/2025/01/LOI-DE-FINANCES-INITIALE-2025_compressed.pdf))_
- **⚠ VAT fraud is a criminal offence carrying a four-billion-franc fine** — **Article 1186.III CGI** (loi de finances 2025, art. 21): the *délit d'escroquerie en matière de TVA* is punished by a fine of ***quatre milliards* (GNF 4,000,000,000)** and **five years' imprisonment**, to be pronounced by the competent tribunal. Words and digits agree. For scale, the neighbouring offences are far smaller: organising collective refusal of tax costs **GNF 25,000,000 and one year** (art. 1184.I) and inciting the public to refuse or delay payment **GNF 10,000,000 and three months** (art. 1185.I). Prosecution in each case is brought before the competent tribunal **on the complaint of the tax administration**, so these are not penalties the administration can impose of its own motion  _([Loi de finances 2025, art. 21 — arts. 1184–1186 CGI](https://dgi.gov.gn/wp-content/uploads/2025/01/LOI-DE-FINANCES-INITIALE-2025_compressed.pdf))_
- **Reverse charge** — On B2B supplies by non-residents, the Guinea business customer self-accounts for VAT (reverse charge)  _(Code Général des Impôts (CGI) — Taxe sur la Valeur Ajoutée (TVA) (https://quaderno.io/guides/guinea-vat-guide/))_
- **Non-resident registration** — Non-resident suppliers must register through a local fiscal representative  _(Code Général des Impôts (CGI) — Taxe sur la Valeur Ajoutée (TVA) (https://quaderno.io/guides/guinea-vat-guide/))_

Guinea applies a Value Added Tax (Taxe sur la Valeur Ajoutée, TVA) at a single standard rate, with exports and international transport zero-rated and certain essential supplies exempt. Returns are monthly, due by the 10th, and filed electronically.

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
