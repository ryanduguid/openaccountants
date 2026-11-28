---
name: sj-jan-mayen-payroll-scope-reference
description: >
  Jan Mayen payroll for 2026 ordinary work and qualifying sickness benefits. Covers continuous stays, wage rates, National Insurance, a-melding and ordinary withholding remittance. Trigger on work or a worker stay on Jan Mayen, including a split stay or a stay across year-end.
jurisdiction: SJ
category: international
tax_year: 2026
tax_year_notes: "Jan Mayen income year 2026. Current guidance and enacted rates checked on 28 November 2026."
tier: 2
review_status: pending_review
last_updated: 2026-11-28
version: 0.1
depends_on:
  - workflow-base
---

# Jan Mayen ordinary wage and payroll reference

Load `workflow-base`. Record the worker and employer, where work was done, dates on Jan Mayen and away, travel dates, remuneration and payment dates, tax residence and evidence of Norwegian National Insurance membership. For Svalbard, use the [Svalbard wage reference](sj-svalbard-wage-reference.md). See the [tax system orientation](sj-tax-system-orientation.md) for the different territories.

## Determine whether the wage rule applies

The Jan Mayen Tax Act applies Svalbard wage withholding and the duration condition in Svalbard Tax Act section 2-2 to qualifying remuneration for work during a continuous stay on Jan Mayen of at least 30 days. Count presence on the island and exclude travel days to and from it. A departure ends the continuous count. Start a new count on the next stay. A stay can continue across 31 December. Presence establishes the duration test. Identify the wages attributable to qualifying work and the relevant income year separately. For shorter stays, test other applicable law. [Jan Mayen Tax Act, ss 1–2][jan] · [Svalbard Tax Act, s 2-2][svalbard] · [Skatte-ABC, J-1-2][handbook] · [Skatte-ABC, S-23-3.4][stays]

The sickness benefit route has separate conditions. The employee must be on Jan Mayen during the certified sickness period, the continuous stay must last at least 30 days and the employee must have been actively working there when the right to sickness benefit arose. Verify the actual claim before applying the wage rule to a benefit. For a mainland tax resident, the tax goes to the municipality of residence on 1 January of the income year. The Svalbard Tax Office handles taxpayers under the Jan Mayen Act. [Jan Mayen Tax Act, ss 1 and 3][jan] · [Skatte-ABC, J-1-1 and J-1-2][handbook]

## Ordinary rates for income year 2026

The 2026 annual wage tax rates are 8% through 12 times the National Insurance base amount, G, and 22% on the excess. Use the last G fixed for the income year for the annual threshold. From 1 May 2026 G is NOK 136,549 and 12 G is NOK 1,638,588. The combined 2026 value of qualifying free board and lodging is NOK 151 per day. Keep the annual calculation separate from the employer's withholding and payment sequence during the year. [Svalbard Tax Act, ss 3-1 and 5-2][svalbard] · [Storting tax decision, ss 1 and 3][rates] · [NAV basic amounts][nav] · [2026 valuation regulation, s 1][valuation]

When Norwegian National Insurance applies, the 2026 ordinary employee contribution is 7.6% on the applicable wage base. The employer rate is zero on wages taxed under the Jan Mayen Act. Check statutory membership and any exception before calculating or reporting a contribution. Determine the treatment of other wages separately. [Storting National Insurance decision, s 7][contributions] · [Jan Mayen contribution regulation][regulation] · [Skatte-ABC, J-1-5 and J-1-6][handbook]

## Report and pay the ordinary withholding

Use the a-melding Jan Mayen and Antarctic dependencies scheme for the qualifying payment. Record the stay with the required unique ID, start date, end date and description at least once per stay. Use ‘Jan Mayen og bilandene’ for withholding and ‘Betalt trygdeavgift til Jan Mayen’ for any worker contribution. The ordinary monthly deadline is the 5th, with the next business day applying when the 5th falls on a weekend or public holiday. The employer guidance says more than 30 days. At exactly 30 qualifying days, record the statutory inclusion and obtain the Tax Administration's filing or correction instructions before submitting. [Employer reporting guidance][filing] · [Monthly deadlines][deadline] · [Svalbard Tax Act, s 2-2][svalbard]

From the January 2026 reporting period, report the total withholding for each distinct wage payment date (‘sum forskuddstrekk per lønnsutbetalingsdato’) along with the date (‘lønnsutbetalingsdato’). Enter a separate total and date for each payment date in the period. [2026 withholding reporting changes][payment-date]

The Tax Administration's S-23-7.17.5 expressly applies the ordinary mainland payment deadline to withholding on Jan Mayen. From 1 January 2026, the statutory ordinary deadline is the first business day after wage payment. Check applicable exceptions, the payment reference and the actual remittance instructions before payment. [Skatte-ABC, S-23-7.17.5][payment] · [Tax Payment Act, ss 10-10 and 10-11][payment-act]

## Check the boundaries

| Fictional stay | Review result |
|---|---|
| 28 days on Jan Mayen and 2 days travelling to and from it | Count 28 days. Check other applicable law. |
| 17 days on Jan Mayen, a trip away, then another 18 days | Test 2 separate stays. Neither meets the duration threshold. |
| Exactly 30 counted consecutive days on Jan Mayen | The statutory duration threshold is met. Confirm how to report before filing. |
| A 32-day counted continuous stay across 31 December | The statutory duration threshold is met. Check wages, withholding and the annual periods separately. |

Obtain case evidence for short stays, mixed locations, foreign residence, treaties, sickness benefits, contribution membership, youth exemptions and refunds, deductions, special payment and holiday handling, multiple employers, overlapping pay periods and actual calculation or settlement. Keep the payroll record and the authority's response for a boundary case.

[jan]: https://lovdata.no/lov/1996-11-29-69
[svalbard]: https://lovdata.no/dokument/NL/lov/1996-11-29-68
[handbook]: https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-J-1
[stays]: https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-S-23/skatteabc-S-23.041/skatteabc-S-23.045
[rates]: https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780
[nav]: https://www.nav.no/grunnbelopet
[valuation]: https://lovdata.no/dokument/LTI/forskrift/2025-12-15-2559
[contributions]: https://lovdata.no/dokument/LTI/forskrift/2025-12-18-2748
[regulation]: https://lovdata.no/dokument/SF/forskrift/1997-12-22-1432
[filing]: https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/rettleiinga-til-a-meldinga/sarskilde-grupper/jan-mayen-og-dei-norske-bilanda-i-antarktis/
[deadline]: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/frister-og-betaling-i-a-meldingen/
[payment-date]: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/nye-frister-for-betaling-av-forskuddstrekk-og-utleggstrekk
[payment]: https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-S-23/skatteabc-S-23.058/skatteabc-S-23.083
[payment-act]: https://lovdata.no/dokument/NL/lov/2005-06-17-67/KAPITTEL_4

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
