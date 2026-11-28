---
name: tr-tax-overview
description: "Türkiye's 2026 tax system, including individual domicile, full and limited corporate liability, tax periods, Turkish lira and Revenue Administration filing. Trigger on Turkish tax residence, income source, tax year or tax administration."
jurisdiction: TR
category: international
tax_year: 2026
last_updated: 2026-11-28
version: 1.2
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Türkiye tax system orientation

Load `workflow-base`. Identify the person or entity, source of income, calendar or accounting period and any filing obligation. The Revenue Administration (Gelir İdaresi Başkanlığı, GİB) administers national taxes. The currency is the Turkish lira (TRY, shown as TL in tax guidance). Check the applicable conversion and accounting rules for foreign currency amounts. [GİB tax calendar][calendar] · [Central Bank banknotes][central-bank] · [Tax Procedure Law, art 215][procedure]

## Tax territory and residence

For 2026, individuals domiciled in Türkiye or continuously present there for more than 6 months within a calendar year generally have full income tax liability. Temporary departures do not break the period. Article 5 excludes specified temporary foreign visitors and certain involuntary stays. Article 3 separately covers certain Turkish nationals abroad for Turkish organisations and qualifies the result where the host country taxes the income. Under full liability, consider domestic and foreign income. Under limited liability, apply the Turkish source tests to each income category. [Income Tax Law, arts 3–7][income-law]

Companies and other corporate taxpayers with a legal centre or business centre in Türkiye have full liability on domestic and foreign profits. The business centre is where business transactions are organised and managed in fact. If both centres are outside Türkiye, apply the limited liability rules to Turkish-source profits. Check the applicable permanent establishment, source, treaty and relief provisions before assigning an outcome for the case. [Corporate Tax Law, arts 1–3][corporate-law]

## Taxpayer types and ordinary rates

Separate personal income, corporate profits and transactions subject to VAT (KDV). For 2026, the individual tariff runs from 15% to 40%. The ordinary band limits are TRY 190,000, TRY 400,000, TRY 1,000,000 and TRY 5,300,000. The third limit is TRY 1,500,000 for wage income. Apply the schedule for the actual income and check any withholding or exemptions. [Income Tax Law, arts 2 and 103][income-law] · [GİB 2026 tariff][tariff] · [Personal income tax guide](turkey-pit.md)

The ordinary corporate rate is 25%. Verify the 30% rate for the specified financial and project businesses and any relevant reductions or minimum tax. Since 10 July 2023 the standard VAT rate has been 20%, with the specified 10% and 1% reduced rates. Check the dated classification of the supply before using a reduced rate. [Corporate Tax Law, arts 32 and 32/C][corporate-law] · [GİB corporate filing guidance][gib-corporate] · [VAT guide](turkey-vat.md) · [GİB VAT rate schedule][vat-rates]

## Periods and filing authorities

The ordinary individual income year is the calendar year. The ordinary corporate accounting period is also the calendar year. The tax procedure legislation provides for special accounting periods. Use the period-specific GİB calendar and the appropriate return service. [Income Tax Law, art 108][income-law] · [Corporate Tax Law, arts 14 and 16][corporate-law] · [Tax Procedure Law, art 174][procedure]

For the completed 2025 calendar year, GİB instructed individuals required to file an annual return to lodge it by 31 March 2026, with instalments due by 31 March and 31 July 2026. GİB listed 30 April 2026 for the ordinary corporate return and payment for calendar-year companies. Confirm the actual declaration and payment dates for the taxpayer's period, including 2026 returns due in 2027. Check the applicable VAT declaration type and period separately. [GİB 2025 individual return notice][individual-deadline] · [GİB 2025 company return notice][company-deadline] · [GİB tax calendar][calendar] · [Corporate income tax guide](tr-corporate-income-tax.md)

[income-law]: https://istanbul.gib.gov.tr/mevzuat/kanun/433
[corporate-law]: https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf
[procedure]: https://istanbul.gib.gov.tr/mevzuat/kanun/434
[central-bank]: https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%20EN/Main%20Menu/Banknotes
[calendar]: https://gib.gov.tr/vergi-takvimi
[tariff]: https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2Fgelir-vergisi-tarifeleri%2Fgelir-vergisi-tarifesi-2026.pdf
[gib-corporate]: https://gib.gov.tr/vergi-konulari/2/19_kurumlar-vergisinin-beyani/19/129/675
[vat-rates]: https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2Fkdv-oranlari.pdf
[individual-deadline]: https://gib.gov.tr/duyuru-arsivi/mevzuat/17408_2025_takvim_yili_gelir_vergisi_beyan_donemi_icin_son_gun_bugun
[company-deadline]: https://www.gib.gov.tr/duyuru-arsivi/mevzuat/17490_kurumlar_vergisi_beyan_donemi_icin_son_gun_30_nisan_2026

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
