---
name: ck-tax-system-orientation
description: >
  Orient Cook Islands tax work to residence, income source, individual and
  company rates, PAYE, value added tax and the Revenue Management Division.
jurisdiction: CK
category: international
tax_year: 2026
tax_year_notes: "Orientation checked 21 November 2026 against the 1 December 2025 consolidation, 2026 Acts list and 2026 filing calendar. Confirm the rules for the obligation and period."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Cook Islands tax-system orientation

Load `workflow-base`. Identify the taxpayer, income or supply, relevant island, transaction date and balance date. Use the Cook Islands Acts and the Collector's directions for the period. The law publisher's consolidation is dated 1 December 2025. Check later Acts, regulations and Orders when applying a rule to an actual obligation. [Official law publisher][LAW] · [Parliament Acts Library][ACTS]

## Residence and income source

For the income-source rules, an individual meets the ordinary residence test when their home is in the Cook Islands and they are personally present there for **more than 183 days in a 12-month period**. From 1 January 2023, a company is deemed resident if its directors exercise control in the Cook Islands, its place of effective management is there, or it is a Cook Islands company with at least 3 resident directors at a single point during the income year. Directors can exercise control in the Cook Islands even if some decisions occur overseas. Check the separate statutory definition of a Cook Islands company. [Income Tax Act 1997, ss 2 and 82][RESIDENCE] · [Definitions][DEFINITIONS]

Subject to the Act, income derived whilst resident is assessable whether sourced locally or abroad. Cook Islands-source income is assessable regardless of residence. For overseas employment income already subject to substantially similar foreign tax, the Collector may determine that the income is non-assessable under s 81. Obtain the Collector's position before relying on that outcome. [Income Tax Act, ss 80–81][SOURCE] · [Foreign salary and wages][FOREIGN]

## Direct tax and withholding

The ordinary company basic rate is 20% of taxable income for a company deemed resident and 28% for other ordinary companies. The schedule has a separate rule for overseas insurers. For individuals, check the applicable Schedule 1 bands. The Rarotonga and Pa Enua categories use separate residence and presence conditions under ss 44 and 44A for their deductions and rates. Apply their own tests even after determining Cook Islands residence under s 82. [Schedule 1 cl 2][COMPANY] · [Schedule 1 cls 3 and 3A][RAROTONGA] · [Pa Enua rates][PAENUA] · [Income Tax Amendment Act 2023, ss 4–7][ITA2023]

Check PAYE for employment payments and the separate withholding classification for relevant non-resident payments. Use `ck-paye` and `ck-company-tax-vat` for their documented conditions and open questions. [MFEM filing and forms][FORMS]

## Value added tax

The standard VAT rate is 15%. Classify taxable supplies by registered persons, goods imports and specified imported services under s 10. The Act also has exempt supplies, exempt importations and zero-rated supplies. The 2026 amendment took effect on 27 May 2026 and changes selected import exemptions. Confirm the operative Orders and facts for a registration or import decision. [Value Added Tax Act 1997, ss 10–11][VAT] · [Rates][VAT-RATE] · [2026 amendment][VAT2026] · [Parliament commencement record][COMMENCEMENT]

## Currency, periods and authority

The Cook Islands uses the New Zealand dollar (NZD). Confirm any tax-specific foreign currency conversion for the transaction before translating an amount. The standard income year is 1 January–31 December. A taxpayer can use an alternative annual balance date for the return with the Collector's consent under s 9. An annual income return is the general rule, subject to the Act, regulations and the Collector's limited relief under s 8. [Cook Islands Tourism currency guidance][NZD] · [Income Tax Act, ss 2 and 8–9][DEFINITIONS] · [Annual return][RETURN] · [Balance date election][BALANCE]

The Ministry of Finance and Economic Management's Revenue Management Division administers inland tax. Use its dated filing calendar for a standard December balance date and confirm any approved variations. The 2026 calendar lists the ordinary VAT and PAYE period as a calendar month, with filing and payment generally by the 20th of the following month, subject to the working-day adjustment. A qualifying VAT registrant may elect quarterly returns under s 15. [Inland Revenue][REVENUE] · [2026 tax calendar][CALENDAR] · [Value Added Tax Act, s 15][VAT-RETURNS]

## Fictional intake

A Cook Islands company makes sales on Rarotonga and pays a director who also works abroad. First establish company residence from control, effective management and director facts. Classify the sales and the director's payments separately. Confirm the company's balance date, VAT filing period and current reporting instructions before assigning deadlines.

[LAW]: https://cookislandslaws.gov.ck/
[ACTS]: https://parliament.gov.ck/parliamentary-business/acts/acts-library/
[DEFINITIONS]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S2_htm
[RESIDENCE]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S82_htm
[SOURCE]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S80_htm
[FOREIGN]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S81_htm
[COMPANY]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_ITA_ITA97_SCH1_CL2_htm
[RAROTONGA]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_ITA_ITA97_SCH1_CL3_htm
[PAENUA]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_ITA_ITA97_SCH1_CL3A_htm
[ITA2023]: https://parliament.gov.ck/wp-content/uploads/2023/09/Income-Tax-Amendment-2023-No.-03-1.pdf
[FORMS]: https://www.mfem.gov.ck/filing-forms
[VAT]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S10_htm
[VAT-RATE]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S11_htm
[VAT2026]: https://parliamentci.wpenginepowered.com/wp-content/uploads/2026/05/Value-Added-Tax-Amendment-Act-2026-No.-4.pdf
[COMMENCEMENT]: https://parliament.gov.ck/business-of-the-day/
[NZD]: https://cookislands.travel/travel-tips
[RETURN]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S8_htm
[BALANCE]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S9_htm
[REVENUE]: https://www.mfem.gov.ck/inland-revenue
[CALENDAR]: https://www.mfem.gov.ck/_files/ugd/dbdf40_615edacd5a584ebda8af0dfb535a3ea4.pdf
[VAT-RETURNS]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S15_htm

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
