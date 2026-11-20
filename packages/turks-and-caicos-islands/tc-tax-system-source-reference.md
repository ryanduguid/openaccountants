---
name: tc-tax-system-source-reference
description: >
  Dated Turks and Caicos Islands tax-system reference for territorial reach, residence, taxpayer and remitter roles, legal tender, reporting periods and responsible authorities. Trigger on a Turks and Caicos tax overview, residence, USD, customs authority or the period for a sector tax.
jurisdiction: TC
category: international
tax_year: 2024
tax_year_notes: "Selected 2014 currency, 2018 customs and financial services and 2021 tourism tax texts, the October 2024 customs authority transition and separately dated 2026 income tax and administrative evidence."
tier: 2
last_updated: 2026-11-20
version: 0.1
depends_on:
  - workflow-base
---

# Turks and Caicos Islands tax-system source reference

Load `workflow-base`. Use this reference to identify the governing regime and the source to check for the date in question. The selected revisions and commencement notices have separate cutoffs. Establish the operative text and any applicable exemption, direction or delegation before determining liability, filing or payment.

## Territory, residence and who accounts for tax

| Question | Dated source and routing |
| --- | --- |
| Is ordinary domestic income tax in scope? | As checked through 10 November 2026, the Islands had no domestic personal or corporate income tax. There was no return or calculation for either. The territory's tax residence statement confirms the absence of domestic income tax residence criteria. Establish foreign tax residence and obligations under the relevant country's law. Check domestic transaction taxes, employer and contributor obligations, licensing and reporting separately. [Ministry of Finance CRS compliance guidance](https://gov.tc/ftie/images/docs/crs/Compliance%20for%20Financial%20Institutions.pdf) · [Territory's tax residence statement](https://www.oecd.org/content/dam/oecd/en/topics/policy-issue-focus/aeoi/turks-caicosislands-residency.pdf) · [Attorney General's annual laws](https://agc.gov.tc/agc/laws/annual) |
| Is there an outward financial transfer? | In the text revised 31 March 2018, the Domestic Financial Services Sales Tax (DFSST) charge under section 4 concerns fees for a transfer through a licensed financial institution within the Islands to a party outside the Islands. The customer bears the tax and the institution accounts for it. Check the licensing definition in section 2 and the customer exemptions for a non-resident person or a company registered as an exempted company under the law cited in section 5. Establish residence and company status for this provision and the transaction date. [Cap 19.16 ss 2, 4–5 and 7](https://agc.gov.tc/agc/component/edocman/19-16-domestic-financial-services-sales-tax-ordinance-2/fdocument?Itemid=9999) |
| Is the customer staying at qualifying accommodation? | In the text revised 31 March 2021, ordinary accommodation under Part III covers specified services provided in the Islands in the course of the qualifying lodging business. Test the premises and guest under sections 2–3 and the charge and exceptions under sections 6–8. The guest is chargeable and the proprietor normally accounts for and pays the tax. Where the proprietor is non-resident, section 9(2) substitutes a resident agent who acted in the qualifying business whilst the proprietor remains non-resident. Section 9(3) separately requires the non-resident proprietor to notify the Permanent Secretary, Finance of agents for the specified business. Check all-inclusive stays and day passes under Part IV, including its modifications to the other applicable Parts. [Cap 19.09 ss 2–3, 6–11 and 20](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf) |
| Are goods entering the Islands? | The customs text revised 31 March 2018 includes the territorial sea in the definition of the Islands. Section 3 has timing rules for sea and air arrivals, with a separate rule for prohibited or restricted goods. Identify the importer under section 2, including the ownership, possession or beneficial interest limb whilst goods remain in customs charge. For the selected home-use entry branch, section 69(2)(a) takes the tariff rate in force when the entry is delivered to the proper officer, subject to the Ordinance's exceptions. Check the separate tariff and relief instruments. [Cap 19.04 ss 2–3 and 69–70](https://customs.gov.tc/webuploads/doclib/19.04%20Customs%20Ordinance.pdf) |

## Currency

In the Currency Ordinance revised 31 December 2014, section 2 values one Crown at one United States dollar. Section 3 makes qualifying US notes legal tender for any amount and sets separate limits for qualifying US coins and Crowns. Section 4 treats monetary transactions as made in the Islands' legal tender unless expressly made in another country's currency. Record the transaction currency and check the applicable tax valuation and payment rules for the period. [Currency Ordinance, Cap 19.03 ss 2–4](https://www.gov.tc/agc/component/edocman/19-03-currency-ordinance-2/fdocument?Itemid=9999)

## Periods and authorities

- **DFSST.** Section 9 of the 2018 revision requires the institution to return and remit within 15 days after each month ends. It includes a rule for fees the institution was unable to recover. The July 2026 Inland Revenue notice lists DFSST among the monthly remittances for which it sends forms and reminders. Check the return period and the statute that applies to it. [Cap 19.16 s 9](https://agc.gov.tc/agc/component/edocman/19-16-domestic-financial-services-sales-tax-ordinance-2/fdocument?Itemid=9999) · [Inland Revenue notice](https://www.premier.gov.tc/revenue/news/inland-revenue-department-introduces-automated-monthly-remittance-forms)
- **Ordinary accommodation.** Section 24(1) of the 2021 revision uses the month in which the guest departs on completing the stay. The proprietor sends the return and corresponding remittance to the Permanent Secretary, Finance within 21 days of month-end, subject to subsection (2). That subsection permits an exceptional extension or instalments for payment. Section 27 provides a separate default assessment power. [Cap 19.09 ss 24 and 27](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf)
- **Customs.** The 2018 revision names the Collector of Customs. From 15 October 2024, section 5 of the Border Force Ordinance assigns customs administration and revenue collection to the Director General. Section 11 directs that references to the Collector and the Collector's powers, duties and functions be read accordingly, subject to the empowering provision. Check the office or delegated officer for the particular action and its date. [Cap 19.04 s 4](https://customs.gov.tc/webuploads/doclib/19.04%20Customs%20Ordinance.pdf) · [Ordinance 26 of 2024 ss 5, 7 and 11](https://www.gov.tc/agc/component/edocman/26-of-2024-border-force-ordinance-2024-2/fdocument?Itemid=9999) · [Legal Notice 45 of 2024](https://www.gov.tc/agc/component/edocman/45-of-2024-border-force-ordinance-2024-commencement-notice-2024/fdocument?Itemid=9999)

## Apply the source to the event

A guest completes a qualifying ordinary accommodation stay in March. Under the selected text, start with the March return and the section 24 rule. If the proprietor lived overseas, establish residence and whether a resident agent acted in the qualifying business before assigning responsibility. A reminder email does not establish the liable person or vary the statutory payment rule. [Cap 19.09 ss 9 and 24](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf)

Ordinary goods arrive by sea and a home-use entry is delivered later. In the selected customs text, section 3(2) uses the earlier of the vessel entering port limits and the goods being unloaded in the Islands. Use the separate delivery-of-entry event under section 69(2)(a) if that branch applies. Check the tariff and competent officer before using either date in a duty or enforcement decision. [Cap 19.04 ss 3 and 69](https://customs.gov.tc/webuploads/doclib/19.04%20Customs%20Ordinance.pdf)

## Remaining coverage

Establish the full amendment and subsidiary legislation chain for the requested date, including any current currency, tariff, sector exemption and procedural rules. For the customs post-clearance audit amendment, obtain the Gazette publication required by section 1 and reconcile the offices named in the new section 93A with the Border Force transition. Separate guides cover selected sector taxes, business formation and licensing and social contributions. [Customs (Amendment) Act 2026, Act 17 ss 1 and 3](https://www.gov.tc/agc/component/edocman/17-of-2026-customs-amendment-act-2026/fdocument?Itemid=9999)

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
