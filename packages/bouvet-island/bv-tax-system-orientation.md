---
name: bv-tax-system-orientation
description: >
  Bouvet Island tax-system orientation covering territory, residence, taxpayer types, Norwegian kroner, income periods and the authorities for ordinary 2026 wages and Norwegian operators. Trigger on work, payments, goods, tax residence or a company connected with Bouvet Island.
jurisdiction: BV
category: international
tax_year: 2026
tax_year_notes: "Ordinary wage and national tax orientation for income year 2026. Authorities checked on 28 November 2026."
tier: 2
review_status: pending_review
last_updated: 2026-11-28
version: 0.1
depends_on:
  - workflow-base
---

# Bouvet Island tax system orientation

Load `workflow-base`. Identify the person or entity, activity, work and other income dates, place of management and any movement of goods. Bouvet Island is a Norwegian dependency under section 1 of the Dependencies Act. For each tax or filing, establish the territorial reach of the law under section 2 and the relevant Act. The dependencies have no separate income tax area under the Norwegian Tax Administration's guidance. [Dependencies Act, ss 1–2][dependencies] · [Justice Ministry white paper, ch 6.2.1][white-paper] · [Skatte-ABC J-1-1][handbook]

## Residence and taxpayer type

A stay on Bouvet does not create tax residence there. Apply mainland residence rules to determine whether a person is Norwegian tax resident. For an existing mainland resident, the wage tax under the Jan Mayen Act goes to the mainland municipality of residence on 1 January in the income year. Establish a foreign worker's actual residence, source and treaty position separately. [Jan Mayen Tax Act, s 3][jan-tax] · [Skatte-ABC J-1-1][handbook] · [Income Tax Act, ss 2-1 to 2-3][national-tax]

Work remuneration during a continuous qualifying stay of at least 30 days can fall under the Jan Mayen Tax Act. The employer reporting guidance says more than 30 days. Confirm reporting for an exact 30-day stay with the Tax Administration before filing. Certain sickness benefits have their own conditions. Use the [wage tax and payroll guide](bv-wage-tax-payroll.md) for stay counting, payroll and contributions. [Jan Mayen Tax Act, ss 1–2][jan-tax] · [Svalbard Tax Act, s 2-2][svalbard-tax] · [Skatte-ABC J-1-2][handbook] · [Employer reporting guidance][amelding]

Classify a company or independent business separately. Check national residence, source and treaty conditions if the business has a Norwegian connection independent of its Bouvet activity. Use the [operator registration and reporting guide](bv-operator-entity-and-reporting.md) and obtain an authoritative determination for a foreign operator active only on Bouvet. [Income Tax Act, ss 2-2 and 2-3][national-tax] · [Dependencies Act, s 2][dependencies]

## Currency and periods

Norwegian tax calculations use Norwegian kroner (NOK). Use the conversion method for the specific payment or return when the original amount is in another currency. The ordinary Norwegian income period is the calendar year unless another rule applies, including the statutory non-calendar accounting-year provision. The 2026 Storting decision sets wage rates for income year 2026. An employer reports each month, and a continuous stay may span two income years. Determine the applicable income and reporting period for each payment. [Skatte-ABC on foreign currency][currency] · [Norwegian tax return currency guidance][conversion] · [Income Tax Act, s 14-1][period] · [Storting 2026 decision, ss 1 and 3][rates] · [Norwegian Tax Administration, a-melding][monthly]

## Authorities and territorial checks

The Svalbard Tax Office within the Norwegian Tax Administration handles taxpayers with income taxed under the Jan Mayen Act. Employers use the Norwegian a-melding to report qualifying wages and stays. Where national company obligations apply, use the Norwegian Tax Administration for tax filing and the appropriate Brønnøysund registers for companies and accounts. [Skatte-ABC J-1-1][handbook] · [Employer reporting guidance][amelding] · [Norwegian company tax return][company-return] · [Register a limited company][company-register] · [Register of Company Accounts][accounts]

Goods can cross a different statutory boundary. Use the [VAT, customs and excise guide](bv-vat-customs-excise-scope.md) to establish the areas and dates and the [land and activity permits guide](bv-land-and-permits.md) for reserve activity. Retain the source period, residence and entity facts, locations and evidence of any filing, payment or permit determination. Resolve the applicable law and actual procedures before assigning liability for a Bouvet-only non-wage case.

[dependencies]: https://lovdata.no/dokument/NL/lov/1930-02-27-3
[white-paper]: https://www.regjeringen.no/no/dokumenter/meld.-st.-33-20142015/id2415895/?ch=6
[jan-tax]: https://lovdata.no/dokument/NL/lov/1996-11-29-69
[svalbard-tax]: https://lovdata.no/dokument/NL/lov/1996-11-29-68
[handbook]: https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-J-1/skatteabc-J-1.001
[national-tax]: https://lovdata.no/lov/1999-03-26-14/kap2
[amelding]: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/spesielle-grupper/jan-mayen-og-de-norske-bilandene-i-antarktis/
[currency]: https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-V-1/skatteabc-V-1.011
[conversion]: https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/abroad/conversion-of-foreign-currency-into-norwegian-kroner/
[period]: https://lovdata.no/nav/lov/1999-03-26-14/kap14
[rates]: https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780
[monthly]: https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/
[company-return]: https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/companies/
[company-register]: https://www.brreg.no/en/limited-company/register-a-limited-company/
[accounts]: https://www.brreg.no/en/submission-of-annual-accounts/

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
