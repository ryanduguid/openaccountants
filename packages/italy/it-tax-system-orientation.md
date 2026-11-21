---
name: it-tax-system-orientation
description: >
  Read Italy's ordinary tax-system orientation for territorial reach,
  residence, taxpayer types, currency, assessment periods and tax authorities.
jurisdiction: IT
category: international
tax_year: 2026
tax_year_notes: "Ordinary Italian income taxes for 2026. The new consolidated income tax text applies from 1 January 2027."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Italy tax-system orientation

Load `workflow-base`. Record the taxpayer's residence and presence, the legal form, the location of management, each income source and the accounting period. For 2026, use Presidential Decree 917/1986 (TUIR). The replacement text under Legislative Decree 117/2026 generally applies from 1 January 2027. [Government explanation of the TUIR transition](https://www.programmagoverno.gov.it/it/approfondimenti/riforme-di-rilievo-del-governo/riforme-governo-meloni/riforma-fiscale/testo-unico-delle-imposte-sui-redditi-tuir/)

## Territorial reach

Individuals resident in Italy generally account for domestic and foreign income. An individual who is nonresident accounts for income sourced in Italy under the domestic rules. An ordinary resident company generally accounts for business income from all sources. Nonresident commercial companies and entities are generally assessed on Italian-source income, excluding amounts subject to final withholding or a substitute tax under art 151. For an Italian permanent establishment, identify the profits and losses attributable to it under art 152. Check any domestic exclusion and applicable treaty separately. [TUIR, arts 3, 23, 81 and 151–152](https://www.normattiva.it/eli/id/1986/12/31/086U0917/CONSOLIDATED/20261120) · [Ministry of Economy and Finance, TUIR index](https://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?id=%7B31D694E8-4398-4030-873B-FEAF5A6647F9%7D)

## Residence

An individual generally qualifies if for more than half the tax period, counting fractions of a day, they have a civil-law residence or domicile in Italy or are physically present there. For this purpose domicile looks to the principal centre of personal and family relationships. Entry in the resident population register for more than half the period creates a rebuttable presumption. A company or covered entity generally qualifies if its registered office, place of effective direction or principal place of ordinary management is in Italy for more than half the tax period. Italian partnerships have a corresponding rule. Check the facts and applicable treaty for dual-residence cases. [TUIR, arts 2, 5 and 73](https://www.normattiva.it/eli/id/1986/12/31/086U0917/CONSOLIDATED/20261120) · [Revenue Agency, individual residence](https://agenziaentrate.gov.it/portale/web/english/residence-for-tax-purposes) · [Revenue Agency, Circular 20/E announcement](https://www.fiscooggi.it/sites/default/files/file/2024/11/045_Com.%20st.%20Circolare%20residenza%20fiscale%2004.11.24.pdf)

## Taxpayer types

A sole trader generally reports business income under the individual rules. Income of a resident ordinary partnership such as an SNC or SAS is attributed to each partner according to their profit share, regardless of receipt. An ordinary resident SRL or SpA is a corporate income taxpayer. A trust can fall within the corporate income tax rules. Where the trust has identified beneficiaries for income-tax purposes, art 73(2) allocates the income to them in their relevant shares or, if unspecified, equally. Review the deed, any enforceable income rights, trust residence and the treatment of each distribution before filing. [TUIR, arts 5 and 73](https://www.normattiva.it/eli/id/1986/12/31/086U0917/CONSOLIDATED/20261120) · [Revenue Agency, trust income in the 2026 filing instructions](https://infoprecompilata.agenziaentrate.gov.it/portale/web/guest/quadro-rl)

## Currency

Italy uses the euro (EUR). Statutory accounts within Civil Code art 2423 are presented in whole euros, with a separate option to present the notes in thousands of euros. Retain support for the conversion of foreign amounts and check the rules for the transaction and the return. [Civil Code, art 2423 through Legislative Decree 139/2015, art 6](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=6&atto.articolo.sottoArticolo=1&atto.articolo.tipoArticolo=0&atto.codiceRedazionale=15G00153&atto.dataPubblicazioneGazzetta=2015-09-04)

## Assessment periods

The ordinary individual income tax period is the calendar year. For corporate income tax, use the financial or management period specified by law or the entity's constituent document. Use the calendar year if neither fixes a duration or the specified duration is 2 years or more. Check any special rule if the entity changes its period or enters liquidation. [TUIR, art 7](https://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&id=%7B31D694E8-4398-4030-873B-FEAF5A6647F9%7D&codiceOrdinamento=0000000000000070000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&articolo=Articolo%207) · [TUIR, art 76](https://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&id=%7B31D694E8-4398-4030-873B-FEAF5A6647F9%7D&codiceOrdinamento=0000000000000760000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&articolo=Articolo%2076)

## Responsible authorities

The Revenue Agency (Agenzia delle Entrate) administers national individual and corporate income tax. Check the region and municipality for any applicable personal income tax surcharge. The Customs and Monopolies Agency (ADM) handles customs. [Revenue Agency, individual income tax](https://agenziaentrate.gov.it/portale/web/english/residence-for-tax-purposes) · [Finance Department, regional surcharges](https://www1.finanze.gov.it/finanze2/dipartimentopolitichefiscali/fiscalitalocale/addregirpef/download/tabella.htm) · [Finance Department, municipal surcharges](https://www1.finanze.gov.it/finanze2/dipartimentopolitichefiscali/fiscalitalocale/nuova_addcomirpef/download/tabella.htm) · [Customs and Monopolies Agency](https://www.adm.gov.it/portale/en/)

## Fictional intake

An individual moves to Italy, holds an interest in a resident SNC and receives a foreign trust payment. Work through the residence tests, obtain the partnership allocation and determine the nature of the trust payment under the deed before choosing the return treatment.

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
