---
name: fr-tax-system-orientation
description: >
  French income and corporation tax orientation for territorial reach,
  fiscal domicile, taxpayer type, currency, periods and authorities.
jurisdiction: FR
category: international
tax_year: 2026
tax_year_notes: "Dated ordinary rules including the fiscal domicile amendment in force from 16 February 2025. Check the versions in force for the relevant income year or accounting period."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# France tax system orientation

Load `workflow-base`. Record the taxpayer's fiscal domicile, where the activities took place, the source of each amount, the applicable treaty and the year or accounting period.

## Territorial reach

Individuals with a French fiscal domicile generally come within income tax on worldwide income. Individuals with a fiscal domicile outside France generally come within charge on French-source income. Check the source categories and any treaty allocation. For individual income tax, check metropolitan France, including Corsica, and the 5 overseas departments. Confirm the rules for other overseas jurisdictions separately. For corporation tax, art 209(I) generally covers profits from enterprises operated in France, specified French-source amounts and profits allocated to France by a tax treaty. Check the statutory exceptions for the facts. [Code général des impôts (CGI), arts 4 A and 4 bis](https://www.legifrance.gouv.fr/codes/id/LEGIARTI000006302200/) · [CGI, art 164 B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031815417/2026-07-09) · [CGI, art 209](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048847486/2026-09-30) · [DGFiP, France and overseas jurisdictions](https://www.impots.gouv.fr/international-particulier/questions/aupres-de-qui-dois-je-declarer-mes-revenus)

## Residence

For individuals, check the household or principal place of stay, principal professional activity and centre of economic interests. One applicable domestic criterion can establish French fiscal domicile. The version of art 4 B in force from 16 February 2025 excludes persons meeting the criteria in art 4 B(1)(a)–(c) whom the applicable treaty treats as non-resident in France. Check the separate public-service rule where relevant. For a company, record the registered office, actual management and places of business. Establish treaty residence under the applicable treaty and determine which profits France can tax under art 209. [CGI, art 4 B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051202565/2026-09-07) · [DGFiP, individual fiscal domicile](https://www.impots.gouv.fr/particulier/suis-je-bien-non-resident) · [CGI, art 209](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048847486/2026-09-30)

## Taxpayer types

An individual sole trader generally reports the relevant business profits under individual income tax. Check any election under art 1655 sexies that gives the business corporate-tax treatment. For eligible partnerships under art 8, the members are taxed on their share under the applicable regime. For entities within art 206, determine the corporation tax obligations. For a foreign-law trust, identify the settlor, trustee, beneficiaries, distributed income and reporting triggers. Article 120(9) addresses distributions of income, with effective availability to the taxpayer relevant to taxation. Check arts 792-0 bis and 1649 AB separately for transfer and reporting rules. [CGI, art 1655 sexies](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053543064/2026-06-24) · [CGI, arts 8 and 8 quinquies](https://www.legifrance.gouv.fr/codes/id/LEGIARTI000006302200/) · [CGI, art 206](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373514/2026-09-03) · [CGI, art 120](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006307284) · [Conseil d'État, 13 March 2026, no 500318](https://www.legifrance.gouv.fr/ceta/id/CETATEXT000053670135) · [CGI, art 792-0 bis](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054335294/2026-06-30) · [CGI, art 1649 AB](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041578431/2026-09-09)

## Currency

The euro (EUR) is the currency. The Commercial Code requires the accounting documents it covers to be prepared in euro. Identify the applicable tax conversion date and method for each foreign amount and retain the source and calculation. [Council Regulation (EC) No 974/98, arts 1a and 2 and Annex](https://eur-lex.europa.eu/eli/reg/1998/974/2026-01-01/eng) · [Code de commerce, art L123-22](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006219327/2026-07-06)

## Assessment periods

The ordinary individual income-tax year is the calendar year. For business profits, record the accounting period that closes in the year and check the rules for a shorter or longer period, multiple closings or no closing. Article 209 gives a separate first-period rule for a new corporation-tax business that prepares no balance sheet in its first calendar year. Keep the applicable filing and payment dates with the period. [CGI, arts 12 and 36–37](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006069577/2026-08-01) · [CGI, art 209](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048847486/2026-09-30)

## Responsible authorities

The Direction générale des Finances publiques (DGFiP) administers individual and company income taxes through the applicable tax office. The Direction générale des Douanes et Droits indirects (DGDDI) handles customs formalities. DGFiP ordinarily administers import VAT for identified VAT taxpayers, with defined operations remaining with DGDDI. Confirm the responsible service for the transaction. [DGFiP, functions](https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/dgfip_presentation_fr.pdf) · [DGFiP, import VAT and competent service](https://bofip.impots.gouv.fr/export/pdf/357923)

## Fictional intake

An individual establishes a home in France and continues managing a business activity in another country. Record dates, home and professional facts, economic interests, the applicable treaty, income sources and the relevant accounting periods before deciding where to report the amounts.

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
