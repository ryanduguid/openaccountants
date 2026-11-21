---
name: mp-tax-system-orientation
description: >
  Orient Northern Mariana Islands tax work to the territorial income tax,
  residence and return coordination, wage tax and business gross revenue tax.
jurisdiction: MP
category: international
tax_year: 2026
tax_year_notes: "Orientation checked 21 November 2026 against federal and Commonwealth legislation and published forms. Confirm the form, local obligation and reporting period."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Northern Mariana Islands tax-system orientation

Load `workflow-base`. Identify the taxpayer, tax year, Commonwealth income sources and entity or activity. The Commonwealth of the Northern Mariana Islands (CNMI) applies a mirror income tax under Covenant § 601 and 4 CMC §§ 1701–1702. Covenant § 602 authorises additional Commonwealth taxes and limits territorial income tax rebates to CNMI-source income. Apply the Northern Marianas Territorial Income Tax (NMTIT), local taxes and rebate rules to their own bases. [Covenant §§ 601–602][COVENANT] · [4 CMC §§ 1701–1702][NMTIT] · [4 CMC § 1708][REBATE]

## Individual residence, source and coordination

For bona fide residence, check the presence, tax home and closer connection tests under IRC § 937 and 26 CFR § 1.937-1. One presence test uses at least 183 days during the tax year. Check year-of-move rules and any Form 8898 obligation. Determine source separately. Compensation generally follows where the work was performed, subject to special rules. [IRC § 937][IRC937] · [Residence regulation][RES] · [Source regulation][SOURCE] · [IRS Publication 570, chs 1–2][PUB570]

A bona fide resident generally reports worldwide income on the CNMI income tax return. Proper filing and full payment there generally discharge the corresponding U.S. federal income tax obligation. A U.S. citizen or resident alien outside the CNMI bona fide resident rules generally files a worldwide return with the IRS. Check the 2026 Form 5074 instructions if adjusted gross income is at least USD 50,000 and gross income from Guam or the CNMI meets the USD 5,000 threshold. Check separate rules for a nonresident alien, joint filers and any federal self-employment obligation. This coordination concerns income tax. Review the separate Commonwealth Chapter 2 return even where the taxpayer files an income tax return with the United States. [26 CFR § 1.935-1][COORD] · [IRS Publication 570, CNMI][PUB570] · [2026 Form 5074, p 3][FORM5074] · [2026 Form 1040NMI, p 2][WAGES-FORM]

## Commonwealth taxes

Chapter 2 imposes a wage and salary tax and an earnings tax. The statutory schedule and 2026 Form 1040NMI show a zero band through USD 1,000 and rates from 2% to 9% on the applicable base. Use the applicable band on that base and check deductions, exemptions and credits separately. The form instructions distinguish Chapter 2 from the NMTIT return. Check federal Social Security and Medicare separately with the applicable rules, including `mp-oasdi-annual-wage-base-reference` and `mp-medicare-ordinary-share-reference`. [4 CMC §§ 1201–1207][WAGES] · [2026 Form 1040NMI][WAGES-FORM]

For a business, establish entity type and scope for NMTIT, then test business gross revenue tax (BGRT). The ordinary annual schedule uses the applicable rate on total taxable gross revenue, with a zero band through USD 5,000 and rates from 1.5% to 5%. Check pooling of taxable activities under § 1301(b), exemptions and special rules before applying it. The Department of Finance publishes Form OS-3105 for monthly BGRT. Check any distinct construction, import, occupancy or product tax for the transaction. [4 CMC § 1301][BGRT] · [Department of Finance forms][FORMS]

## Currency, periods and authority

Work in U.S. dollars (USD). Establish the tax year and accounting period before assigning any deadline. The Division of Revenue and Taxation publishes year-specific NMTIT, Chapter 2, business and withholding forms. Use its instructions for annual and periodic returns. Check income source before estimating a territorial rebate and confirm the eligible rebate base under § 1708. [Department of Finance forms][FORMS] · [4 CMC § 1708][REBATE]

## Fictional intake

A U.S. citizen who lives outside the Commonwealth does temporary work on Saipan. Confirm the source of the wages, whether the federal de minimis exception applies and where the income tax return belongs. Check separately whether the work creates a Chapter 2 filing or withholding obligation.

[COVENANT]: https://cnmilaw.gov/covenant
[NMTIT]: https://cnmilaw.gov/commonwealth-code/3421
[REBATE]: https://cnmilaw.gov/docs/cmc_section/T4/1708.pdf
[IRC937]: https://uscode.house.gov/us/usc/119-124/t26/s937/
[RES]: https://www.ecfr.gov/current/title-26/section-1.937-1
[SOURCE]: https://www.ecfr.gov/current/title-26/section-1.937-2
[COORD]: https://www.ecfr.gov/current/title-26/section-1.935-1
[PUB570]: https://www.irs.gov/publications/p570
[FORM5074]: https://www.irs.gov/pub/irs-prior/f5074--2026.pdf
[WAGES]: https://cnmilaw.gov/commonwealth-code/3358
[WAGES-FORM]: https://finance.gov.mp/division-forms/revenue-taxation/2026/f1040nmi--2026.pdf
[BGRT]: https://cnmilaw.gov/docs/cmc_section/T4/1301.pdf
[FORMS]: https://finance.gov.mp/forms.php

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
