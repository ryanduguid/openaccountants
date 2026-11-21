---
name: gu-tax-system-orientation
description: >
  Orient Guam tax work to mirror income tax, bona fide residence, filing
  coordination and business privilege tax.
jurisdiction: GU
category: international
tax_year: 2026
tax_year_notes: "Orientation checked 21 November 2026. The ordinary retail and service business privilege tax rate changed on 1 October 2026. Confirm the activity, period and form."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Guam tax-system orientation

Load `workflow-base`. Identify the taxpayer, territory, reporting period, activities and sources of income. Guam is a U.S. territory. Its territorial income tax applies the U.S. income tax laws under 48 USC § 1421i, with statutory substitutions and exclusions. Check the corresponding territorial provisions for an individual, company or other entity and the correct year's income tax forms. [48 USC § 1421i(a)–(e)][MIRROR] · [Guam Department of Revenue and Taxation forms][FORMS]

## Residence, source and returns

For individuals, apply the presence, tax home and closer connection tests for bona fide residence under IRC § 937 and 26 CFR § 1.937-1. At least 183 days in the tax year is one way to meet the presence test. Determine source separately. The place of performance generally determines the source of compensation, subject to special rules. Review the year-of-move rules, Form 8898 and joint filing based on the facts. [IRC § 937][IRC937] · [Residence regulation][RES] · [Source regulation][SOURCE] · [IRS Publication 570][PUB570]

A bona fide resident generally files a Guam return for worldwide income. Properly filing and fully paying that liability generally satisfies the individual's U.S. federal income tax return and payment obligation. A U.S. citizen or resident alien outside the Guam bona fide resident rules generally reports worldwide income to the IRS. The 2026 Form 5074 instructions require a qualifying U.S. filer to attach it where adjusted gross income is at least USD 50,000 and gross income from Guam or the CNMI meets the USD 5,000 threshold. A nonresident alien outside the bona fide resident rules may have separate source-based returns. Check the exceptions and federal self-employment tax separately. [26 CFR § 1.935-1][COORD] · [IRS Publication 570, Guam][PUB570] · [2026 Form 5074, p 3][FORM5074]

## Business privilege tax and other obligations

Business privilege tax (BPT) applies separately from the Guam territorial income tax. For ordinary retail sales of tangible property and service businesses not otherwise specifically taxed, the rate was 4.5% from 1 October 2025 through 30 September 2026 and is 4% from 1 October 2026. The base is statutory gross proceeds or gross income for the activity. Special rates, deductions or exemptions can apply. Identify the activity before using an ordinary rate, especially for wholesale, construction, finance, gaming and insurance. [Public Law 38-136, ch I § 2 and 11 GCA § 26202(a), (c)–(j)][BPT]

Guam also administers use tax, hotel occupancy tax and product-specific excises. Check the relevant activity and any exemption. For employees, assess income tax withholding and federal payroll obligations separately. Use `gu-oasdi-annual-wage-base-reference` and `gu-medicare-ordinary-share-reference` for their documented scope. [Guam DRT GRT filing instructions][GRT] · [IRS Publication 570, ch 4][PUB570]

## Currency, periods and authority

Work in U.S. dollars (USD) and check any conversion required for the return. Identify the income tax year and accounting period, then use the Department of Revenue and Taxation calendar and the applicable form. Ordinary monthly BPT returns and payments are due by the 20th of the following month, subject to the applicable due-date adjustments. DRT requires electronic BPT filing and provides separate form samples for periods before and from October 2026. [Guam DRT calendar][CAL] · [Forms and publications][FORMS] · [GRT filing instructions][GRT]

## Fictional intake

A consulting business provides services in Guam during September and October 2026. Identify which amounts belong in each reporting period under its accounting method. Check the applicable BPT category before using the October rate, and determine where the owner files individual income tax independently.

[MIRROR]: https://uscode.house.gov/us/usc/119-142/t48/s1421i/
[IRC937]: https://uscode.house.gov/us/usc/119-124/t26/s937/
[RES]: https://www.ecfr.gov/current/title-26/section-1.937-1
[SOURCE]: https://www.ecfr.gov/current/title-26/section-1.937-2
[COORD]: https://www.ecfr.gov/current/title-26/section-1.935-1
[PUB570]: https://www.irs.gov/publications/p570
[FORM5074]: https://www.irs.gov/pub/irs-prior/f5074--2026.pdf
[BPT]: https://guamlegislature.gov/38th_Guam_Legislature/Public_Laws_38th/Public%20Law%2038-136.pdf
[FORMS]: https://www.guamtax.com/forms/index.html
[GRT]: https://www.guamtax.com/help/pops/instructions.html
[CAL]: https://www.guamtax.com/info/calendar.html

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
