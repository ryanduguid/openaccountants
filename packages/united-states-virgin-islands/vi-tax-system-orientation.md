---
name: vi-tax-system-orientation
description: >
  Orient U.S. Virgin Islands tax work to mirror income tax, federal filing
  coordination and the territorial gross receipts tax.
jurisdiction: VI
category: international
tax_year: 2026
tax_year_notes: "Orientation checked 21 November 2026. Use the entity, reporting period and territorial form that apply to the case."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# U.S. Virgin Islands tax-system orientation

Load `workflow-base`. Identify the taxpayer, residence, sources, activities and tax year. The Virgin Islands Bureau of Internal Revenue (BIR) administers a territorial income tax based on U.S. income tax law under 48 USC § 1397. Federal law coordinates who files and pays to each authority and limits territorial tax reductions. Check any local incentive separately. [48 USC § 1397][MIRROR] · [26 USC § 932][COORD] · [26 USC § 934][LIMIT] · [BIR tax structure][STRUCTURE]

## Residence, source and individual returns

Apply the federal bona fide presence, tax home and closer connection tests and the source rules under 26 USC § 937. An individual who is a bona fide resident for the entire tax year generally files with BIR, includes worldwide income and identifies the sources. Report and fully pay the territorial liability to meet the federal income tax coordination rule. Attach BIR Form 1040INFO for non-Virgin Islands income. Check any separate federal self-employment filing. [26 USC § 932(c)][COORD] · [26 CFR § 1.937-1][RES] · [26 CFR § 1.937-2][SOURCE] · [IRS Publication 570, ch 3][PUB570] · [BIR Form 1040INFO][INFO]

A U.S. citizen or resident alien who does not meet the full-year bona fide test and has Virgin Islands-source income or income effectively connected with a Virgin Islands trade or business generally files the original U.S. return with the IRS and a signed copy with BIR. Attach Form 8689 to both returns to allocate the tax due to BIR. For joint returns check the greater adjusted gross income rule. Check the separate filing rules for a nonresident alien who is not a bona fide resident. [26 USC § 932(a)–(d)][COORD] · [26 CFR § 1.932-1][COORDREG] · [IRS Form 8689][ALLOCATION] · [IRS Publication 570, ch 3][PUB570]

## Taxpayer type and currency

Use U.S. dollars (USD). BIR generally treats corporations formed under Virgin Islands law as domestic and taxes their worldwide income. A corporation organised elsewhere, including in a U.S. state, is foreign for territorial income tax. Determine its Virgin Islands-source and effectively connected income and apply the corresponding return and rate rules. A U.S. S corporation election does not itself determine territorial treatment. [BIR tax structure][STRUCTURE] · [26 USC § 11][CORP]

## Assessment periods

An ordinary calendar-year individual income tax return is generally due 15 April of the following year, subject to the applicable tax-year notices and extensions. BIR's gross receipts instructions use Form 720 for monthly filers within 30 calendar days after the month ends. Form 720B for annual filers is generally due 30 January of the following year. Confirm eligibility before choosing the annual form, including when yearly receipts equal USD 225,000. [BIR Form 1040INFO][INFO] · [IRS Publication 570, ch 3][PUB570] · [BIR Form 720][GRT] · [BIR Form 720B][GRTA]

## Headline rates

The ordinary 2026 mirror individual income tax schedule uses marginal rates from 10% to 37%. The regular corporation rate under the mirror code is 21%. BIR describes a separate surcharge under 33 V.I.C. § 581 equal to 10% of the corporation's territorial income tax liability, yielding 23.1% where the full 21% rate and surcharge apply. [IRS Revenue Procedure 2025-32, s 4.01][RATES] · [26 USC § 11][CORP] · [BIR tax structure][STRUCTURE]

BIR gives a 5% gross receipts tax on taxable business receipts. Its annual instructions allow the first USD 9,000 per month for eligible businesses with yearly receipts below USD 225,000. The return instructions describe the tax as based on gross receipts before business expenses. Check coverage for business done in the territory even if the contractor lacks a physical presence there. [BIR Form 720][GRT] · [BIR Form 720B][GRTA] · [Governor's enactment notice for Bill 36-0063][CONTRACTORS]

[MIRROR]: https://uscode.house.gov/us/usc/119-136/t48/s1397/
[COORD]: https://uscode.house.gov/us/usc/119-142/t26/s932/
[LIMIT]: https://uscode.house.gov/us/usc/119-142/t26/s934/
[COORDREG]: https://www.ecfr.gov/current/title-26/section-1.932-1
[RES]: https://www.ecfr.gov/current/title-26/section-1.937-1
[SOURCE]: https://www.ecfr.gov/current/title-26/section-1.937-2
[PUB570]: https://www.irs.gov/publications/p570
[INFO]: https://bir.vi.gov/content/form/ee6facb3-7d15-4066-86db-c965152411d2/index.pdf
[ALLOCATION]: https://www.irs.gov/pub/irs-prior/f8689--2026.pdf
[STRUCTURE]: https://bir.vi.gov/content/booklets/tax_structure.pdf
[CORP]: https://uscode.house.gov/us/usc/119-142/t26/s11/
[RATES]: https://www.irs.gov/pub/irs-drop/rp-25-32.pdf
[GRT]: https://bir.vi.gov/content/form/24c5d5c8-3e07-4870-8996-ec3a2089c018/index.pdf
[GRTA]: https://bir.vi.gov/content/form/a04ea26e-6aab-477c-9fb7-6274198a3be1/index.pdf
[CONTRACTORS]: https://www.vi.gov/governor-bryan-signs-public-safety-health-and-economic-development-bills-into-law/

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
