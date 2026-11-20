---
name: ca-tax-system-orientation
description: >
  Canada income tax orientation for territorial reach, residence, taxpayer type,
  reporting currency, assessment periods and federal, provincial and territorial agencies.
jurisdiction: CA
category: international
tax_year: 2026
tax_year_notes: "Uses the cited 2026 federal consolidations. Check the applicable amendment, tax year and provincial or territorial law for the actual case."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Canada tax system orientation

Load `workflow-base`. Record the person or entity, residence facts, jurisdiction of each activity, currency and reporting period. Identify each applicable tax and its administrator before choosing a return or rate.

## Territorial reach

Part I of the federal Income Tax Act charges residents on taxable income for the year. A non-resident can be liable on taxable income earned in Canada if the person was employed in Canada, carried on business in Canada or disposed of taxable Canadian property at any time in that year or a previous year. Read Division D for the calculation and Part XIII separately for covered payments to non-residents. Section 255 also includes specified licensed offshore seabed and subsoil and the seas and airspace above them for the related exploration or exploitation activities. For provincial and territorial corporate income tax, identify the permanent establishment and relevant allocation. [Income Tax Act, ss 2, 115, 212 and 255](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/FullText.html) · [CRA, provincial and territorial corporation tax](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax.html)

## Residence

For individuals, document ordinary residence and significant residential ties. The sojourner rule generally deems a person resident throughout the tax year after at least 183 days of sojourning in Canada during that year. Check the other deeming rules and any treaty before deciding. For corporations, check the statutory incorporation and continuance rules. Common-law residence can also follow where central management and control is actually exercised. A person who would otherwise be resident in Canada may be deemed non-resident under s 250(5) if an applicable treaty treats them as resident solely in the other country, subject to the statutory exception. [Income Tax Act, s 250](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html) · [CRA, individual residence](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/determining-your-residency-status.html) · [CRA, corporation residence](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/businesses-international-non-resident-taxes/residency-a-corporation.html)

## Taxpayer types

Identify the individual operating a sole proprietorship, the corporation taxed on its own income, the partners or the trust. Section 96 computes partnership results using a separate-person assumption to determine amounts for the partners. Section 104(2) generally treats a trust as an individual in respect of trust property. Check the trust definition, exceptions and reporting separately. [Income Tax Act, ss 2, 96 and 104](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/FullText.html)

## Currency

The monetary unit is the Canadian dollar (CAD). Section 261 generally requires Canadian currency for Canadian income tax results and sets the relevant spot-rate conversion. Confirm any applicable exceptions, including whether a qualifying functional-currency election is in effect. Record the source and date of each conversion. [Currency Act, s 3](https://laws-lois.justice.gc.ca/eng/acts/C-52/section-3.html) · [Income Tax Act, s 261](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-261.html)

## Assessment periods

Section 249 generally uses a calendar year for individuals, the fiscal period for corporations and Canadian resident partnerships and the accounting period for a graduated rate estate. A corporate fiscal period ordinarily cannot exceed 53 weeks. Confirm any special or deemed year-end. Use the separate reporting period for GST/HST and the correct period for withholding and payroll. [Income Tax Act, s 249](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.html) · [Income Tax Act, s 249.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html) · [CRA, fiscal periods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/fiscal-period-income-tax-purposes.html)

## Responsible authorities

The Canada Revenue Agency administers federal income tax and administers provincial and territorial income tax under agreements. Quebec administers its own individual and corporate income tax. Alberta administers its own corporate income tax through Tax and Revenue Administration. For commercial imports, the Canada Border Services Agency assesses and collects duties and import taxes through CARM. Identify the responsible administration separately for GST/HST, QST, or a provincial sales tax. [Canada Revenue Agency Act, s 5](https://laws-lois.justice.gc.ca/eng/acts/C-10.11/section-5.html) · [CRA, provincial and territorial individual tax](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/provincial-territorial-tax-credits-individuals.html) · [CRA, provincial and territorial corporation tax](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax.html) · [Alberta corporate income tax](https://www.alberta.ca/corporate-income-tax) · [CBSA commercial imports](https://www.canada.ca/en/border-services-agency/services/carm.html)

## Fictional intake

Assume a Canadian-incorporated corporation has permanent establishments in Alberta and Ontario, a 30 September fiscal year-end and commercial imports. Start with federal corporate income tax and the Ontario allocation on the federal return. Check the separate Alberta corporate return and the allocation between provinces. Record the corporation's year-end and the relevant CARM and GST/HST periods. Check whether a functional-currency election exists before converting any foreign records. The actual tax, dates, registrations, exemptions and allocation require the relevant guides and current source verification.

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
