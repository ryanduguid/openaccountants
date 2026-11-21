---
name: as-tax-system-orientation
description: >
  Orient American Samoa tax work to its separate territorial income tax,
  federal residence and filing coordination, withholding and import excise.
jurisdiction: AS
category: international
tax_year: 2026
tax_year_notes: "Orientation checked 21 November 2026 against the territorial Code, Public Law 38-07 and IRS Publication 570 (2025). Confirm tax-year-specific forms and deadlines."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# American Samoa tax-system orientation

Load `workflow-base`. Identify the taxpayer, legal form, tax year, places where services were performed and any ties to another jurisdiction. American Samoa is a U.S. territory with a separate income tax. A.S.C.A. § 11.0403 adopts the U.S. income tax rules in force on 31 December 2000 to the extent compatible with territorial law. Apply the local amendments in Title 11 Chapter 05, including Public Law 38-07, which generally fixes the adopted inflation-adjusted thresholds at their 2000 levels subject to territorial amendments. [A.S.C.A. §§ 11.0403 and 11.0501][ASCA] · [Public Law 38-07, §§ 1–2][PL]

## Residence, source and returns

Test federal bona fide residence under IRC § 937 and 26 CFR § 1.937-1. The tests address presence, tax home and closer connection. Presence can be established in several ways, including at least 183 days in the tax year. Check the year-of-move rules and any Form 8898 obligation. Determine income source separately. Compensation generally follows where the work was performed, subject to special rules. [IRC § 937][IRC937] · [Residence regulation][RES] · [Source regulation][SOURCE] · [IRS Publication 570, chs 1–2][PUB570]

| Individual's situation | Ordinary income tax filing starting point |
|---|---|
| U.S. citizen or national, or resident alien, and bona fide resident of American Samoa for the tax year | File the territorial return for worldwide income. If a federal return is required, check the IRC § 931 exclusion and Form 4563. Qualifying American Samoa income is generally excluded from federal gross income. Pay for services as an employee of the U.S. Government or one of its agencies is outside that exclusion. |
| U.S. citizen or resident alien with American Samoa-source income who is outside the bona fide resident rules | Generally file a U.S. return for worldwide income and a territorial return for American Samoa-source income. Check the federal foreign tax credit for territorial income tax. |
| Nonresident alien who is outside the bona fide resident rules and has American Samoa-source income | Generally report American Samoa-source income to the territory and apply the federal nonresident alien rules to any U.S. filing. |

Check part-year reporting under local § 11.0405 separately from the federal year-of-move rules. U.S. government employment, military status and other special circumstances can change the ordinary filing result. [A.S.C.A. § 11.0405][ASCA] · [26 CFR § 1.931-1][EXCLUDE] · [IRS Publication 570, American Samoa][PUB570] · [Form 4563][FORM4563]

## Ordinary taxes and withholding

Check the territorial schedules and exemptions for individuals. Section 11.0503 provides a 4% adjusted gross income comparison for the local individual minimum tax, with specified exceptions. The territorial corporate provisions modify the adopted IRC § 11 schedule. Check the separate 1% gross revenue minimum tax comparison for businesses, its start-up and nonprofit exceptions and its reorganisation rule. [A.S.C.A. §§ 11.0503 and 11.0533–11.0535][ASCA]

Classify territorial wage withholding under §§ 11.0403 and 11.0519–11.0526. Federal Social Security and Medicare need their own analysis. Use `as-oasdi-annual-wage-base-reference` and `as-medicare-ordinary-share-reference` for their documented scope. For goods entering the territory, check the applicable territorial import excise and customs rules by product and transaction date. [A.S.C.A. Title 11, chs 4–5][ASCA] · [GAO description of Customs, p 13][CUSTOMS] · [IRS Publication 570, Social Security and Medicare][PUB570]

## Currency, periods and authority

Work in U.S. dollars (USD) and confirm any tax-specific treatment of foreign amounts. Identify the tax year and accounting period before applying filing deadlines. The American Samoa Government Tax Office publishes the annual Form 390 for individuals. Confirm the territorial filing date and employer remittance periods for the year with that office. Check federal filing and payment separately when required, including any federal self-employment tax. [A.S.C.A. § 11.0404][ASCA] · [American Samoa Government Tax Office][TAX] · [IRS Publication 570, chs 3–4][PUB570]

## Fictional intake

A U.S. national works in Pago Pago for a private employer and receives interest from a U.S. bank. Establish bona fide residence and source the wages and interest separately. Determine whether a U.S. return is required and check the Form 4563 exclusion and available credit on the appropriate return.

[ASCA]: https://www.osas.as/copy-of-asac-2024-edition-5/10-title-15%E2%80%93parks-%26-rec.-%28.pdf%29
[PL]: https://www.osas.as/_files/ugd/4c56eb_eb2db15209f8444a9fddb4514683d559.pdf
[IRC937]: https://uscode.house.gov/us/usc/119-124/t26/s937/
[RES]: https://www.ecfr.gov/current/title-26/section-1.937-1
[SOURCE]: https://www.ecfr.gov/current/title-26/section-1.937-2
[EXCLUDE]: https://www.ecfr.gov/current/title-26/section-1.931-1
[PUB570]: https://www.irs.gov/publications/p570
[FORM4563]: https://www.irs.gov/forms-pubs/about-form-4563
[TAX]: https://www.americansamoa.gov/tax-office
[CUSTOMS]: https://www.gao.gov/assets/gao-10-638.pdf

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
