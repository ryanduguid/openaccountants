---
name: rw-tax-overview
description: "Rwanda's 2025 tax system, including individual and company residence, tax territory, currency, periods and Rwanda Revenue Authority filing. Trigger on Rwandan tax residence, income source, tax year or tax administration."
jurisdiction: RW
category: international
tax_year: 2025
last_updated: 2026-11-28
version: 1.2
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rwanda tax system orientation

Load `workflow-base`. Identify the taxpayer, tax period, income source and filing obligation. The Rwanda Revenue Authority (RRA) administers national income tax. Record amounts in Rwandan francs (RWF, shown as FRW in the legislation). Check the applicable conversion and reporting rules if the original records are in another currency. [RRA service charter][service] · [Income Tax Law, art 14][income-tax]

## Territory and residence

For 2025, article 4 treats an individual as resident if they have a permanent residence or habitual abode in Rwanda, represent Rwanda abroad as a Rwandan national or spend at least 183 days in Rwanda in aggregate during the tax period. A separate test uses presence in the assessment period and stays exceeding 122 days in each of the 2 preceding periods. Check the exact travel facts under article 4(5). A non-individual is resident if established under Rwandan law or effectively managed in Rwanda at any time in the tax period. [Income Tax Law, art 4][income-tax]

For a 2025 permanent residence or effective management case, establish the operative rules for that period. The 2019 order was made under Law 016/2018, and article 70 of the 2022 law limited earlier consistent orders to 12 months from publication on 28 October 2022. The Gazette order that took effect on 25 September 2026 treats a place in Rwanda where an individual usually stays as a permanent residence. For a non-individual, any 1 of 4 conditions can establish effective management in Rwanda under that order. Check day-to-day control or management, where shareholder meetings take place, where accounts are kept and whether the main shareholders or directors are resident in Rwanda. [2019 ministerial order][order-2019] · [Income Tax Law, arts 4 and 70–73][income-tax] · [Ministerial Order 009/26/10/TC, arts 1, 2 and 5][order-2026]

For ordinary income tax, assess domestic and foreign income for a resident and Rwanda-source income for a non-resident. Apply the statutory source rules to each payment, including cross-border services. Verify any permanent establishment, exemption, treaty relief and foreign tax credit separately. [Income Tax Law, arts 6, 7, 11 and 46][income-tax] · [RRA personal income tax guidance][rra-pit]

## Taxpayer types and rates

Distinguish employment and other personal income, an individual business and a corporate taxpayer. In the ordinary personal real-profit regime for 2025, annual taxable income bands run from 0% to 30%. The bands end at RWF 720,000, RWF 1,200,000 and RWF 2,400,000. The ordinary corporate rate is 28% under the 2023 amendment. Check the separate small-business and special regimes, including the 2025 corporate exemptions. Use the [individual income tax guide](rwanda-income-tax.md) and [corporate income tax guide](rw-corporate-income-tax.md) for the separate calculations. [Income Tax Law, arts 11, 12, 14 and 44][income-tax] · [2023 amendment, art 2][income-2023] · [2025 amendment, art 3][income-2025] · [RRA personal income tax guidance][rra-pit]

The ordinary VAT rate is 18%. Confirm the actual supply, period, registration and filing frequency before applying that rate. The RRA describes monthly and quarterly VAT returns, due within 15 days of the applicable period end. Check payroll withholding and remittance separately. [2025 RRA VAT guide][vat] · [RRA service charter][service] · [Payroll guide](rwanda-payroll.md)

The 2025 income tax amendment added a 1.5% tax on gross Rwanda-source revenue of companies supplying qualifying digital services with substantial national presence. Its implementation depends on the designated services and procedures in a ministerial order. Confirm the operative definitions and procedures before assigning liability or a filing date. [2025 amendment, arts 5 and 8][income-2025]

## Periods and filing

The ordinary income tax period runs from 1 January to 31 December. A corporate taxpayer keeping accounts on a generally accepted basis can ask the Minister in writing to approve another 12-month period for sound reasons. The RRA required ordinary calendar-year 2025 declarations and payment by 31 March 2026. Check the taxpayer's filing obligation and the approved timetable for a special period or other exception. [Income Tax Law, arts 8–10][income-tax] · [2023 amendment, art 1][income-2023] · [RRA tax-period guidance][rra-period] · [RRA 2025 filing notice][rra-deadline]

[income-tax]: https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf
[income-2023]: https://www.rra.gov.rw/fileadmin/user_upload/LAW_AMENDING_THE_INCOME_TAX_LAW_of_2022.pdf
[income-2025]: https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_the_2022_Income_Tax_May_2025.pdf
[order-2019]: https://www.rra.gov.rw/fileadmin/user_upload/aho_umusoreshwa_atuye.pdf
[order-2026]: https://www.minijust.gov.rw/fileadmin/user_upload/Minijust/Official_gazettes_2/____2026_Igazeti_ya_Leta/__NZERI-September-Septembre/OG_n___Special_of_25.09.2026__MO__IMISORO.pdf#page=39
[service]: https://www.rra.gov.rw/en/rra-service-charter-iv
[rra-pit]: https://www.rra.gov.rw/en/taxes-fees/domestic-taxes/income-tax/personal-income-tax-pit-1
[rra-period]: https://www.rra.gov.rw/en/taxes-fees/domestic-taxes/income-tax/income-tax-period
[rra-deadline]: https://www.rra.gov.rw/en/details?cHash=89083cca38d715a1f45d7dd5ad0a47f9&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=2967
[vat]: https://www.rra.gov.rw/fileadmin/user_upload/VAT__EN_2025.pdf

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
