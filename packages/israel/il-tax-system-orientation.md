---
name: il-tax-system-orientation
description: >
  Israel's ordinary 2025 tax system, covering territorial income scope, individual and company residence, taxpayer type, currency, the tax year and filing authorities. Trigger on Israeli tax residence, income source or annual return routing.
jurisdiction: IL
category: international
tax_year: 2025
tax_year_notes: "Ordinary income tax for the 2025 tax year. The 2025 return services were checked on 28 November 2026."
tier: 2
review_status: pending_review
last_updated: 2026-11-28
version: 0.1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - workflow-base
---

# Israel tax system orientation

Load `workflow-base`. Identify the person or entity, income category, locations of the activities or assets and the dates involved. For 2025, section 2 of the Income Tax Ordinance applies to the listed income of Israeli residents derived in Israel or abroad and to the listed income of non-residents derived in Israel. Establish source for each item and check the relevant treaty, statutory relief and territorial rules before determining liability. [Income Tax Ordinance, ss 2 and 4A][ordinance] · [Israel Tax Authority, income tax][income-tax]

## Residence and taxpayer type

An individual's domestic residence depends on their centre of life. Consider family, economic and social connections, including permanent home, where the individual and their family live, regular work and economic interests. Residence is presumed if they spent at least 183 days in Israel in the tax year, or at least 30 days in that year and at least 425 days across that year and the previous 2. Any part of a day counts. The individual or the assessing officer may rebut either presumption. If claiming non-residence despite meeting a presumption, check the filing requirement and the 2025 return's Form 1348 schedule. [Income Tax Ordinance, s 1][ordinance] · [Israel's residence criteria submitted to the OECD][residence] · [2025 Form 1301 service and Form 1348][individual-return]

Under the ordinary domestic company tests, a company is resident if incorporated in Israel or its business is controlled and managed in Israel. Section 1 has a limited exception to the control and management test for specified circumstances involving a qualifying new or veteran returning resident. Establish the legal form and any special classification before choosing a return. Where a return is required, the Tax Authority provides Form 1301 for individuals and business owners whose business is unincorporated, and Form 1214 for companies. [Income Tax Ordinance, s 1][ordinance] · [Israel Tax Authority, company tax presentation, pp 11–13][entity-residence] · [Israel's residence criteria submitted to the OECD][residence] · [2025 Form 1301 service][individual-return] · [2025 Form 1214 service][company-return]

## Currency and periods

Report ordinary income tax amounts in new Israeli shekels (NIS). For foreign amounts, confirm the conversion rule and date for each item. The ordinary 2025 tax year runs from 1 January to 31 December 2025. Check for an approved special accounting period under section 7 and use the filing instructions for the taxpayer and period. [Bank of Israel, banknotes and coins][currency] · [Income Tax Ordinance, ss 6–7 and 240A][ordinance] · [Tax Authority Circular 9/2004, foreign currency conversion][conversion] · [2025 Form 1301][form-1301]

## Authorities and next checks

Use the Israel Tax Authority's income tax services for the ordinary annual return. Check its separate VAT, customs and real estate taxation services for transactions that may fall under those regimes. Use the [annual income tax return guide](il-income-tax-returns.md), [company tax guide](il-corporate-tax.md), [VAT guide](israel-vat.md) and [customs guide](il-customs-duty.md) to find the relevant topic, then check the period and applicable rules. Confirm any treaty residence, withholding or relief, precise filing deadline and payment instructions separately. [Israel Tax Authority, 2025 individual return service][individual-return] · [2025 company return service][company-return] · [Tax Authority glossary][glossary]

[ordinance]: https://www.btl.gov.il/Laws1/00_0103_000000.pdf
[income-tax]: https://www.gov.il/en/departments/topics/income_tax_israel_tax_authority/govil-landing-page
[residence]: https://www.oecd.org/content/dam/oecd/en/topics/policy-issue-focus/aeoi/israel-residency.pdf
[individual-return]: https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals
[entity-residence]: https://www.gov.il/BlobFolder/unit/decentralized-autonomous-organizations-committee/he/Vaadot_ahchud_DAO_presentation-taxes.pdf
[company-return]: https://www.gov.il/he/service/reporting-and-payment-annual-tax-report-2025-companies
[currency]: https://boi.org.il/en/economic-roles/banknotes-and-coins/
[conversion]: https://www.gov.il/BlobFolder/policy/income-tax-professional-inst-9-2004-2/he/Policy_IncomeTaxInst_hoz9-2004.pdf
[form-1301]: https://www.gov.il/BlobFolder/service/reporting-and-payment-2025-annual-tax-report-for-individuals/he/Service_Pages_Income_tax_annual-report-2026_itc1301-2025.pdf
[glossary]: https://www.gov.il/en/pages/taxes-glossary

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
