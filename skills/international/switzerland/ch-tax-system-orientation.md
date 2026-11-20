---
name: ch-tax-system-orientation
description: >
  Read Switzerland's ordinary tax-system orientation for territorial reach, residence,
  taxpayer types, currency, assessment periods and tax authorities.
jurisdiction: CH
category: international
tax_year: 2026
tax_year_notes: "Ordinary 2026 provisions including the federal direct tax consolidation of 2 September 2026. Confirm the applicable period, canton, commune and treaty."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Swiss tax-system orientation

Load `workflow-base`. Record the taxpayer, federal tax connection, canton and commune, income source, tax period and any treaty. Check cantonal and communal rules for the relevant location.

## Territorial reach

For direct federal tax, individuals and legal entities with a personal connection generally have unlimited liability. That base excludes foreign businesses, permanent establishments and real estate, subject to statutory allocation and relief rules. A taxpayer without personal connection is liable on the Swiss items specified for economic connection, including qualifying Swiss business or property income. Check the rules for rate determination and treaty allocation separately. [Federal Direct Tax Act, arts 4–6 and 50–52](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/fr/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-fr-pdf-a.pdf)

## Residence

An individual's personal connection can arise from Swiss tax domicile or a qualifying stay. Domicile can arise from living in Switzerland with the intention of remaining or a special legal domicile under federal law. A stay qualifies from at least 30 days with gainful activity or at least 90 days without it, without a substantial interruption. Check the exception for a person who keeps a foreign domicile and is in Switzerland solely for study or institutional treatment. A legal entity has a personal connection if its registered office or effective administration is in Switzerland. [Federal Direct Tax Act, arts 3 and 50](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/fr/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-fr-pdf-a.pdf)

## Taxpayer types

A sole trader includes income from independent business in their personal tax. Partners in a simple partnership, general partnership or limited partnership include their respective shares in their own taxable amounts. A Swiss AG, GmbH or cooperative is a separate legal-person taxpayer. For a trust, assess the deed, retained powers, nature of beneficiary rights and settlor's domicile at creation. Federal guidance adopts the Swiss Tax Conference approach. A revocable trust is attributed to the settlor. A qualifying irrevocable fixed-interest trust generally attributes interests to beneficiaries. The treatment of an irrevocable discretionary trust depends in part on the settlor's domicile at creation and when a beneficiary receives or acquires a fixed claim to a distribution. [Federal Direct Tax Act, arts 10, 18 and 49](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/fr/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-fr-pdf-a.pdf) · [Swiss Tax Conference Circular 30, sections 4–5](https://www.ssk-csi.ch/fileadmin/dokumente/kreisschreiben/KS_30_d.pdf) · [Federal Tax Administration, Circular 20](https://www.estv.admin.ch/de/kreisschreiben-direkten-bundessteuer)

## Currency

The currency unit is the Swiss franc (CHF). A legal person preparing annual accounts in a foreign currency converts taxable net profit into CHF using the average selling exchange rate for the tax period. Check the separate cantonal capital-tax conversion if relevant. [Currency and Payment Instruments Act, art 1](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2000/186/20200101/fr/pdf-a/fedlex-data-admin-ch-eli-cc-2000-186-20200101-fr-pdf-a.pdf) · [Federal Direct Tax Act, art 80(1bis)](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/fr/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-fr-pdf-a.pdf) · [Federal Tax Administration, conversion rates](https://www.estv.admin.ch/fr/denomination-du-capital-en-monnaie-etrangere-fonctionnelle)

## Assessment periods

An individual's federal income-tax period is the calendar year. Independent business income generally uses the accounts closed in that period. A legal person's tax period is its financial year, with accounts closed each calendar year except the year of formation and with additional closure rules for particular events. Check the rules for a part-year liability or a change of location. [Federal Direct Tax Act, arts 40–41 and 79–80](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/fr/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-fr-pdf-a.pdf)

## Responsible authorities

Cantons assess and collect direct federal tax under federal supervision. Cantonal law governs cantonal and communal direct taxes within the federal harmonisation framework. The Federal Tax Administration handles domestic and acquisition VAT. The Federal Office for Customs and Border Security handles import VAT and customs. [Federal Direct Tax Act, art 2](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/fr/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-fr-pdf-a.pdf) · [Direct Taxes Harmonisation Act, arts 1–2](https://www.fedlex.admin.ch/eli/cc/1991/1256_1256_1256/fr) · [Federal Tax Administration, Swiss tax system](https://www.estv.admin.ch/fr/le-systeme-fiscal-suisse-brochure) · [Federal Office for Customs and Border Security, VAT](https://www.bazg.admin.ch/en/value-added-tax-and-import-tax-companies)

## Fictional intake

A Swiss GmbH has a 30 June year end and keeps its accounts in euros. The owner lives in another canton and earns foreign rental income personally. Identify the company's tax period and CHF exchange rate, then assess the owner's residence and foreign property rules separately.

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
