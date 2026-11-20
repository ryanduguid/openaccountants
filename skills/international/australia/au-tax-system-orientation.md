---
name: au-tax-system-orientation
description: >
  Australian income tax orientation for territorial scope, residence, taxpayer
  type, currency, income years and the responsible revenue authorities.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "Income tax law as compiled on 1 October 2026. Verify the provisions and any transition that apply to the actual period."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Australia tax system orientation

Load `workflow-base`. Record the taxpayer, where each activity takes place, the income and accounting periods, the currency and the tax that applies. Check federal, state, territory and local obligations separately.

## Territorial reach

An Australian resident's assessable income generally includes ordinary and statutory income from Australian and foreign sources, subject to the applicable exclusions. A foreign resident generally includes Australian-source ordinary and statutory income and any additional amounts a provision includes on another basis. Check temporary-resident treatment, specific capital gains provisions, withholding and treaties separately. For the 1997 Act, geographical Australia includes Norfolk Island, the Coral Sea Islands Territory, Ashmore and Cartier Islands, Christmas Island, Cocos (Keeling) Islands, Heard Island and the McDonald Islands and the offshore area defined by reference to the petroleum and greenhouse gas storage law. The GST Act sets a separate indirect tax zone, with specific offshore rules. [Income Tax Assessment Act 1997, ss 6-5 and 6-10](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [Income Tax Assessment Act 1997, s 960-505](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html) · [GST Act, s 195-1](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html)

## Residence

For an individual, check ordinary residence, Australian domicile unless the Commissioner is satisfied that the permanent place of abode is overseas, actual presence for more than half the income year and the specified Commonwealth superannuation schemes. The presence test has an exception when the Commissioner is satisfied that both the usual place of abode is overseas and the person does not intend to become resident. The superannuation test can also cover a spouse or a child under 16. A company is resident if incorporated in Australia, or if it carries on business in Australia and either its central management and control is in Australia or Australian-resident shareholders control its voting power. Check any applicable treaty and record when residence changes. [Income Tax Assessment Act 1936, s 6(1)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [ATO, individual residency](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/your-tax-residency)

## Taxpayer types

Identify the individual who carries on a sole trade or the company that derives its own income. An ordinary partnership reports income and its partners account for their respective shares under ss 91 and 92. Corporate limited partnerships can be treated as companies under Division 5A. For a trust, identify the beneficiary's present entitlement, legal disability and residence and any provision that assesses the trustee. [Income Tax Assessment Act 1997, ss 4-1 and 4-10](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [Income Tax Assessment Act 1936, Divisions 5, 5A and 6](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/pdf/2)

## Currency

The Australian dollar (AUD) is the monetary unit. Section 960-50 generally requires translation into Australian currency for income tax. Check the prescribed time and method and any applicable functional currency choice under s 960-60. Keep the source, date and calculation for each conversion. [Currency Act 1965, s 8](https://www.legislation.gov.au/C1965A00095/2016-10-21/2016-10-21/text/original/epub/OEBPS/document_1/document_1.html) · [Income Tax Assessment Act 1997, ss 960-50 and 960-60](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html)

## Assessment periods

The standard reporting year runs from 1 July to 30 June. Section 4-10 specifies which income year relates to the financial year, including the previous-financial-year rule for companies. Check whether the Commissioner approved a substituted accounting period under s 18 and any special opening or closing period. Obtain the separate GST and PAYG reporting periods and the actual lodgment dates. [Income Tax Assessment Act 1997, s 4-10](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [Income Tax Assessment Act 1936, s 18](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [Income Tax Assessment Act 1997, s 995-1](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html) · [ATO, substituted accounting periods](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/large-business/compliance-and-governance/entities-with-a-substituted-accounting-period)

## Responsible authorities

The Commissioner of Taxation administers federal income tax through the ATO. The Australian Border Force handles customs clearance and usually collects import GST at clearance unless the importer has an approved deferral. Identify the state or territory revenue office for duties, payroll tax or land tax, and the council for any local rates. [Income Tax Assessment Act 1936, s 8](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) · [ABF, GST and other taxes on imports](https://www.abf.gov.au/importing-exporting-and-manufacturing/importing/cost-of-importing-goods/gst-and-other-taxes) · [Australian Government, tax registrations](https://business.gov.au/registrations/register-for-taxes/tax-registration-for-your-business) · [Australian Government, property taxes](https://business.gov.au/finance/tax/taxes-on-your-property)

## Fictional intake

Assume an Australian-incorporated trading company hires staff in Victoria and brings in supplies priced in US dollars. Check Australian-resident company treatment first. Confirm whether the company has an approved substituted accounting period, record the transaction dates and applicable currency conversions and identify the separate ABF clearance, ATO reporting and Victorian payroll tax work. Confirm the rates, filing obligations and thresholds in the relevant guides.

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
