---
name: na-tax-overview
description: "Namibia's ordinary income tax system, including source, taxpayer types, currency, assessment periods and NamRA filing. Trigger on Namibian income source, tax residence, assessment year or tax administration."
jurisdiction: NA
category: international
tax_year: 2025
last_updated: 2026-11-28
version: 1.5
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Namibia tax system orientation

Load `workflow-base`. Identify the taxpayer, assessment year and source of each amount. The Namibia Revenue Agency (NamRA) administers national income tax through the Integrated Tax Administration System (ITAS). The domestic currency is the Namibia Dollar (NAD or N$). The South African rand is also legal tender in Namibia. Check the applicable conversion and reporting rules for amounts recorded in another currency. [NamRA income tax guidance][namra] · [NamRA ITAS tax pages][itas] · [Bank of Namibia Act, ss 37–39 and 45][bank-act]

## Tax territory and residence

The ordinary income tax base uses amounts from sources in Namibia or deemed by legislation to be in Namibia. Start with the income type and statutory source tests for persons and companies. Check the separate deemed-source rules for services and other payments with facts outside Namibia. Establish residence separately where it affects a deemed-source rule, non-resident withholding or treaty treatment. [Income Tax Act, ss 1, 5 and 15][income-law] · [NamRA general tax information][namra-guide]

## Taxpayer types and rates

Distinguish individuals, companies and any applicable special regime. For an ordinary individual year of assessment commencing on or after 1 March 2024, the first N$100,000 of taxable income is taxed at 0% and the top marginal rate is 37% above N$1,550,000. The general non-mining company rate is 30% for years of assessment commencing on or after 1 January 2025 under the 2024 amendment. Apply the relevant period and check sector-specific rates before calculating tax. [Income Tax Act, sch 4][income-law] · [Income Tax Amendment Act 4 of 2024][amendment]

The standard VAT rate is 15% on taxable supplies and imports. Determine the actual treatment and applicable period for the transaction separately. [VAT Act, s 6][vat-law] · [NamRA VAT guidance][namra-vat]

Use the guides for [individual income tax](na-income-tax.md), [corporate income tax](na-corporate-income-tax.md) and [VAT](na-vat-gst.md) for the relevant calculation or filing.

## Periods and filing

The ordinary assessment year for a person other than a company ends on the last day of February. For the 2025-26 individual period this is 28 February 2026. A company's assessment year generally follows its financial year. Record both the opening and closing dates before applying a rate or due date. [Income Tax Act, s 5][income-law]

For taxpayers filing under section 56(1), the ordinary return and related tax are due by 30 June following the assessment year, or by the last day of the seventh month after year-end for companies and taxpayers with business, professional or farming income. For those individuals with the usual February year-end this is 30 September. Check the return exceptions for eligible individuals, the applicable ITAS notice, filing and payment extensions and other payment obligations for the case. [Income Tax Act, s 56(1)–(5)][income-law] · [NamRA general tax information][namra-guide] · [NamRA individual ITAS guidance][itas-individual]

[income-law]: https://www.namra.org.na/documents/cms/uploaded/income-tax-act-24-of-1981-debf9c72ad.pdf
[amendment]: https://mfpe.gov.na/documents/76368/3405432/%238442%2B-%2BGov%2BN264%2BIncome%2BTax%2BAmendment%2BAct%2B4%2Bof%2B2024%2B16%2BSeptember.pdf/de116770-f305-5ef4-c71b-ab842fd55de9?t=1728304423431
[namra]: https://www.namra.org.na/tax-types/page/income-tax
[namra-guide]: https://www.namra.org.na/documents/cms/uploaded/information-brochure--general-tax-information--66d64f0d7f.pdf
[itas]: https://itas.namra.org.na/taxes
[itas-individual]: https://itas.namra.org.na/individual
[bank-act]: https://www.bon.com.na/CMSTemplates/Bon/Files/bon.com.na/81/8145f41a-768a-4690-9c9c-cf3c9cc24ec8.pdf
[vat-law]: https://www.namra.org.na/documents/cms/uploaded/valueadded-tax-act-10-of-2000-0d8c7ed7fc.pdf
[namra-vat]: https://www.namra.org.na/tax-types/page/value-added-tax-vat-30120

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
