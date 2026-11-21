---
name: pr-tax-system-orientation
description: >
  Orient Puerto Rico tax work to territorial income tax, federal filing
  coordination and the sales and use tax.
jurisdiction: PR
category: international
tax_year: 2026
tax_year_notes: "Orientation checked 21 November 2026. Use the forms and any relief for the tax year in question."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Puerto Rico tax-system orientation

Load `workflow-base`. Identify the taxpayer, tax year, residence, each income source and each municipality where the business operates. The Departamento de Hacienda administers Puerto Rico's own Internal Revenue Code and the local income tax return. Use the federal Internal Revenue Code to decide separately what to file with the IRS. [Puerto Rico Internal Revenue Code][CODE] · [IRS Publication 570, ch 3][PUB570]

## Residence and source

Puerto Rico's code generally treats individuals domiciled there as resident and presumes residence upon 183 days of presence during the calendar year. Federal bona fide residence under 26 USC § 937 applies the federal presence, tax home and closer connection tests. Work through both sets of rules. [Puerto Rico code, s 1010.01(a)(30)][CODE] · [26 CFR § 1.937-1][RES]

The Puerto Rico return for a resident generally covers worldwide income. Under 26 USC § 933, an individual who is a bona fide resident for the entire tax year generally excludes Puerto Rico-source income from federal gross income. Pay from the U.S. Government or its agencies for employment falls outside the exclusion. A narrower rule can apply to pre-move Puerto Rico-source income for a qualifying U.S. citizen who ceases residence after at least 2 years of bona fide residence. Apply the federal and local source rules separately. Check any U.S. filing requirement, self-employment tax, credit and corresponding limitation. [Puerto Rico code, ss 1031.01, 1035.01 and 1091.01][CODE] · [26 USC § 933][EXCLUSION] · [26 CFR § 1.937-2][SOURCE] · [IRS Publication 570, chs 2–4][PUB570]

## Taxpayer type and currency

Use U.S. dollars (USD). Distinguish individuals, regular corporations, corporations subject to special regimes and pass-through entities. Check an LLC's Puerto Rico tax classification and elections before using individual, corporation or pass-through rules. Non-resident individuals and foreign corporations have separate rules, including for income effectively connected with a Puerto Rico trade or business. [Puerto Rico code, ss 1010.01, 1022.01, 1078.01–1078.02 and ch 9][CODE] · [Hacienda corporation filing instructions][CORP]

## Assessment periods

The ordinary Puerto Rico income tax deadline is 15 April after a calendar year or the 15th day of the fourth month after a fiscal year. Check special returns, extensions and the year's official instructions. Hacienda's 2025 individual and ordinary corporation filings use electronic Form 482 and Form 480.2, respectively. Keep local and federal filings and their deadlines separate. [Puerto Rico code, s 1061.16][CODE] · [Hacienda Form 482 instructions][IND] · [Hacienda corporation filing instructions][CORP]

## Headline rates

The Puerto Rico normal individual schedule starts at zero through USD 9,000 of net taxable income and reaches 33% on the excess over USD 61,500. Apply the separate adjustments and any year-specific relief before determining liability. The normal regular corporation rate is 18.5% of normal net taxable income for years beginning after 31 December 2018. Test the separate corporation surtax and alternative minimum tax where applicable. [Puerto Rico code, ss 1021.01–1021.02 and 1022.01–1022.03][CODE] · [Hacienda Form 482 instructions][IND] · [Hacienda 2025 relief circular][RELIEF]

The ordinary sales and use tax (IVU) is 11.5% on taxable items, comprising 10.5% territorial and 1% municipal. Certain designated professional and intermerchant services have separate 4% rules. Registered merchants ordinarily file and remit territorial monthly IVU by the 20th of the following month through SURI. From the July 2026 period, the consolidated SURI return also covers municipal IVU for participating municipalities, with separate territorial and municipal payments. Bayamón, Carolina, Guaynabo, Mayagüez and San Juan retain their own municipal filing and payment procedures. [Hacienda ordinary IVU guidance][IVU] · [Hacienda services circular][SERVICES] · [Hacienda municipal IVU circular][MUNICIPAL]

[CODE]: https://hacienda.pr.gov/sites/default/files/codigo_de_rentas_internas_2011_segun_enmendado_28.08.2026.pdf
[PUB570]: https://www.irs.gov/publications/p570
[EXCLUSION]: https://uscode.house.gov/us/usc/119-142/t26/s933/
[RES]: https://www.ecfr.gov/current/title-26/section-1.937-1
[SOURCE]: https://www.ecfr.gov/current/title-26/section-1.937-2
[IND]: https://hacienda.pr.gov/sites/default/files/inst_individuos_2025_27_feb_26.pdf
[CORP]: https://hacienda.pr.gov/publicaciones/carta-circular-de-rentas-internas-num-26-06-cc-ri-26-06
[RELIEF]: https://hacienda.pr.gov/publicaciones/carta-circular-de-rentas-internas-num-26-10-cc-ri-26-10
[IVU]: https://hacienda.pr.gov/publicaciones/determinacion-administrativa-num-17-06
[SERVICES]: https://hacienda.pr.gov/publicaciones/carta-circular-de-rentas-internas-num-20-33-cc-ri-20-33
[MUNICIPAL]: https://hacienda.pr.gov/publicaciones/carta-circular-de-rentas-internas-num-26-13-cc-ri-26-13

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
