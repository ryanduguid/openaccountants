---
name: cz-tax-system-orientation
description: >
  Read Czechia's ordinary tax-system orientation for territorial reach,
  residence, taxpayer types, currency, assessment periods and tax authorities.
jurisdiction: CZ
category: international
tax_year: 2026
tax_year_notes: "Ordinary Czech income-tax rules checked against legislation in force on 21 November 2026."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Czechia tax-system orientation

Load `workflow-base`. Record the taxpayer's presence and home, the entity's legal form and place of management, each source of income and the period covered. Retain the dated facts used to determine residence and treaty treatment.

## Territorial reach

Income tax generally covers domestic and foreign income of Czech-resident individuals and corporate taxpayers. A nonresident accounts for Czech-source income. Section 22 specifies sources including income from a Czech permanent establishment, services or employment carried on in Czechia under the relevant rule and income from Czech immovable property. Check any applicable treaty before calculating tax on a cross-border item. [Income Taxes Act, §§ 2, 17 and 22](https://e-sbirka.gov.cz/sb/1992/586?zalozka=text) · [Financial Administration, starting a business](https://financnisprava.gov.cz/cs/dane/zivotni-situace/zacinate-podnikat)

## Residence

An individual is generally resident if they have a permanent home in Czechia in circumstances indicating an intention to live there permanently or spend at least 183 days in Czechia during the calendar year. Count each started day of presence and combine separate stays. A person in Czechia solely to study or receive medical treatment is a nonresident under § 2(3). A corporate income taxpayer generally qualifies through its seat or place of management. A taxpayer without legal personality established under Czech law is presumed to have its seat in Czechia. Check treaty residence where both countries can claim the taxpayer. [Income Taxes Act, §§ 2 and 17](https://e-sbirka.gov.cz/sb/1992/586?zalozka=text) · [General Financial Directorate, 2026 residence guidance](https://financnisprava.gov.cz/assets/cs/prilohy/ms-prime-dane/GFR_met_informace_danova_rezidence_2026_FS.pdf)

## Taxpayer types

A sole trader accounts for self-employment income under the individual rules. Limited liability companies and joint-stock companies are ordinarily corporate taxpayers. A general commercial partnership (*veřejná obchodní společnost*) is taxed at entity level only on income subject to special-rate withholding within § 18b(1). Its partners account for their respective shares of the tax base or loss. The general partners of a limited partnership (*komanditní společnost*) account for their respective shares and the entity's base is reduced by the share allocated to them. [Income Taxes Act, §§ 7, 17, 18b, 20 and 23](https://e-sbirka.gov.cz/sb/1992/586?odkazId=27452113)

A Czech-law trust fund (*svěřenský fond*) is a corporate income taxpayer. For income tax, the statute treats a distribution as coming first from fund profits and then from other property. Check the deed, the residence and rights of each participant and the treatment of the receipt. Apply the appropriate entity classification to an arrangement formed abroad. [Income Taxes Act, §§ 17, 21c and 21f](https://e-sbirka.gov.cz/sb/1992/586?odkazId=207450421)

## Currency

The ordinary accounting currency is the Czech koruna (CZK). An eligible accounting entity may use EUR, USD or GBP if that currency is its functional currency under § 24a. A corporate taxpayer using a foreign accounting currency converts relevant booked items appearing in the income-tax return into CZK at the tax conversion rate for the last day of the relevant period. Check § 38 separately for unbooked items and the rules applicable to individuals. [Accounting Act, § 24a](https://e-sbirka.gov.cz/sb/1991/563?zalozka=text) · [Income Taxes Act, §§ 38 and 38ba](https://e-sbirka.gov.cz/sb/1992/586?odkazId=207450421)

## Assessment periods

The individual income-tax period is the calendar year. For corporate income tax, § 21a recognises the calendar year, a financial year and specified periods for reorganisations or accounting periods longer than 12 consecutive months. The ordinary accounting period is 12 consecutive months. An eligible entity moving to a financial year generally notifies its income-tax office at least 3 months before the planned change or the end of the current period, whichever is earlier. Check the separate rules for new entities and reorganisations. [Income Taxes Act, §§ 16b and 21a](https://e-sbirka.gov.cz/sb/1992/586?odkazId=27452113) · [Accounting Act, § 3](https://e-sbirka.gov.cz/sb/1991/563?zalozka=text)

## Responsible authorities

The Financial Administration of the Czech Republic administers domestic income tax through the relevant tax office. The Customs Administration handles import duties. Check the office with jurisdiction based on the taxpayer's address, seat or relevant permanent establishment and use the Financial Administration's filing service where applicable. For corporate income tax of a Czech-law trust fund, the competent authority is the Financial Office for the Capital City of Prague, through its Prague 7 workplace. [Financial Administration Act, §§ 1, 8, 10 and 12](https://e-sbirka.gov.cz/sb/2011/456?odkazId=214785777) · [Financial Administration, allocation of tax offices](https://financnisprava.gov.cz/cs/dane/zivotni-situace/zacinate-podnikat) · [Financial Administration, trust funds](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pravnicke-osoby/sverensky-fond) · [Corporate income-tax filing](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pravnicke-osoby/obecne-informace) · [Customs Administration, responsibilities](https://celnisprava.gov.cz/en/Pages/Customs-Administration-of-the-Czech-Republic.aspx)

## Fictional intake

A Czech limited partnership draws up accounts in EUR and allocates part of its result to a general partner. Verify the functional currency first, record the partner's profit share and apply § 38 to booked amounts included in the corporate return.

A Czech-law trust fund has a trustee in Brno. Use the Prague 7 workplace for the fund's corporate income tax.

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
