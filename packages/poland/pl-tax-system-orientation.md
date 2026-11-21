---
name: pl-tax-system-orientation
description: >
  Read Poland's ordinary tax-system orientation for territorial reach,
  residence, taxpayer types, currency, assessment periods and tax authorities.
jurisdiction: PL
category: international
tax_year: 2026
tax_year_notes: "Ordinary Polish income-tax rules checked against legislation in force on 21 November 2026."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Poland tax-system orientation

Load `workflow-base`. Record the taxpayer's home and ties, the entity's legal form and place of management, each income source and the tax and accounting periods. Where a cross-border arrangement is involved, identify the taxpayer and any Polish permanent establishment before checking the treaty.

## Territorial reach

Polish-resident individuals and corporate income taxpayers generally account for income from Poland and abroad. Nonresidents account for Polish-source income. The statutory source lists include applicable business income from activity in Poland, including a Polish permanent establishment, and income from Polish immovable property. The individual list also covers employment performed in Poland irrespective of where the worker is paid. Check the applicable treaty and any domestic exemption or relief. [Personal Income Tax Act, arts 3 and 4a](https://eli.gov.pl/api/acts/DU/2026/592/text/U/D20260592Lj.pdf) · [Corporate Income Tax Act, art 3](https://eli.gov.pl/api/acts/DU/2026/554/text/U/D20260554Lj.pdf)

## Residence

An individual generally qualifies if their centre of personal or economic interests is in Poland or they spend more than 183 days in Poland during the tax year. A corporate income taxpayer generally qualifies if it has its registered office or management in Poland. Article 3(1a) includes cases where the entity's ongoing affairs are conducted in Poland in an organised and continuous manner. Where another country also claims residence, check the applicable treaty. [Personal Income Tax Act, arts 3 and 4a](https://eli.gov.pl/api/acts/DU/2026/592/text/U/D20260592Lj.pdf) · [Corporate Income Tax Act, art 3](https://eli.gov.pl/api/acts/DU/2026/554/text/U/D20260554Lj.pdf) · [Ministry of Finance, individual residence](https://podatki.gov.pl/en/tax-residence)

## Taxpayer types

A sole trader generally reports business income under the individual rules. A Polish limited liability company (*spółka z ograniczoną odpowiedzialnością*) is a corporate taxpayer. Limited partnerships and partnerships limited by shares with a seat or management in Poland are corporate taxpayers. A Polish general partnership (*spółka jawna*) can become a corporate taxpayer when its partners include someone other than a natural person and it fails to make the required disclosures. It is also a corporate taxpayer under art 1(7) if a Polish family foundation is a partner and it meets the Polish seat or management condition. For a transparent partnership, use the partners' rights to share in profit when allocating income and the corresponding costs. Check any foreign partnership against the statutory entity classification. [Corporate Income Tax Act, arts 1 and 5](https://eli.gov.pl/api/acts/DU/2026/554/text/U/D20260554Lj.pdf) · [Personal Income Tax Act, arts 5b, 8 and 10](https://eli.gov.pl/api/acts/DU/2026/592/text/U/D20260592Lj.pdf)

For a foreign trust, check the deed, residence, rights, beneficiaries and actual control. The controlled foreign entity definitions can include a foreign trust where the statutory conditions for the Polish taxpayer's rights or control are met. Check the separate Central Register of Beneficial Owners rules where a trustee or equivalent has a Polish seat or residence or enters a Polish business relationship or acquires Polish property on behalf of the trust. [Corporate Income Tax Act, art 24a](https://eli.gov.pl/api/acts/DU/2026/554/text/U/D20260554Lj.pdf) · [Personal Income Tax Act, art 30f](https://eli.gov.pl/api/acts/DU/2026/592/text/U/D20260592Lj.pdf) · [Ministry of Finance, register reporting](https://www.gov.pl/web/finanse/zgloszenie-informacji-do-centralnego-rejestru-beneficjentow-rzeczywistych)

## Currency

Poland uses the złoty (PLN). Under the Accounting Act, statutory books are kept in Polish and in Polish currency. For ordinary income amounts expressed in foreign currency, the income-tax statutes generally use the National Bank of Poland's average rate on the last working day before the income arises. Check the separate rules for expenses, withholding and exchange differences when applicable. [Accounting Act, art 9](https://eli.gov.pl/api/acts/DU/2026/522/text.pdf) · [Personal Income Tax Act, art 11a](https://eli.gov.pl/api/acts/DU/2026/592/text/U/D20260592Lj.pdf) · [Corporate Income Tax Act, art 12(2)](https://eli.gov.pl/api/acts/DU/2026/554/text/U/D20260554Lj.pdf)

## Assessment periods

Use the calendar year for ordinary individual income tax. The default corporate tax year is also the calendar year. A corporate taxpayer can generally specify a different period of 12 consecutive calendar months in its governing document. Check the first-year, change-of-year and mandatory book-closing rules before treating a period as 12 months. [Tax Ordinance, art 11](https://eli.gov.pl/api/acts/DU/2026/622/text/T/D20260622L.pdf) · [Corporate Income Tax Act, art 8](https://eli.gov.pl/api/acts/DU/2026/554/text/U/D20260554Lj.pdf)

## Responsible authorities

The National Revenue Administration (Krajowa Administracja Skarbowa, KAS) administers national taxes and customs duties. Identify the competent tax office for the type of taxpayer and filing. Municipal authorities administer local property tax and councils set local rates within the statutory framework. [National Revenue Administration, responsibilities](https://www.gov.pl/web/national-revenue-administration/about-us) · [Ministry of Finance, corporate filing and office](https://podatki.gov.pl/podatki-firmowe/cit/cit-klasyczny/informacje-podstawowe-cit-klasyczny) · [Ministry of Finance, property tax](https://podatki.gov.pl/podatki-lokalne/podatek-od-nieruchomosci/informacje-podstawowe)

## Fictional intake

A general partnership gains a new corporate partner during the year. Identify when the partners with profit rights changed, check the CIT-15J requirements and establish whether the partnership or the partners account for the income.

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
