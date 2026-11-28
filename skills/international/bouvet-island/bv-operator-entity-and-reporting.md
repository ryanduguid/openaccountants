---
name: bv-operator-entity-and-reporting
description: >
  Bouvet Island operator routing for Norwegian company formation, corporate tax residence and reporting. Trigger on a Norwegian limited company, foreign operator, permanent establishment, tax return, annual accounts or beneficial owners for Bouvet activity.
jurisdiction: BV
category: international
tax_year: 2026
tax_year_notes: "Norwegian corporate income tax for 2026 and registration and reporting rules checked on 28 November 2026."
tier: 2
review_status: pending_review
last_updated: 2026-11-28
version: 0.1
depends_on:
  - workflow-base
---

# Bouvet Island operator registration and reporting

Load `workflow-base`. Record where the operator was formed, its legal form, business address, actual management, dates and places of work, contract parties and the treaty country if relevant. Check the operator's existing national obligations first. For a Bouvet-only operation, establish the territorial reach of each law before applying it. The Dependencies Act s 2 applies Norwegian private, criminal and procedural law and provides for extending other rules. The Justice Ministry's Bouvet white paper explains the test for each provision. [Dependencies Act, ss 1–2][dependencies] · [Justice Ministry white paper, ch 6.2.1][white-paper]

## Norwegian company and foreign operator registration

A private limited company formed under Norwegian law (AS) must register in the Register of Business Enterprises. For the provisions effective 1 January 2026, give notice before business begins and within 3 months of signing the formation document. The Companies Act requires at least NOK 30,000 share capital. Prepare the memorandum including articles and the relevant confirmation of paid-up capital. The register lists the coordinated notification and digital company formation routes. It requires a Norwegian street address or place name. Confirm that the address and filing documents for the proposed company will be accepted. [Business Register Act, ss 2-1 and 4-1][business-register] · [Commencement decision][commencement] · [Companies Act, ss 2-18 and 3-1][companies-act] · [Register a limited company][registry-as] · [Registry address guidance][registry-address]

For a foreign enterprise carrying on business in mainland Norway or on the Norwegian continental shelf, check registration as a Norwegian-registered foreign enterprise (NUF) under Business Register Act s 2-1(2). Use the register's NUF guidance for the proof of foreign registration and applicable documents. For a foreign operator working only on Bouvet, confirm the territorial application and address with the competent authority before assigning the NUF registration duty. Section 1-4 supplies a separate extension power for Svalbard and Jan Mayen. [Business Register Act, ss 1-4 and 2-1][business-register] · [Registry NUF registration duty][registry-nuf-duty] · [Registry NUF forms and documentation][registry-nuf]

## Corporate tax and filing

Test Norwegian corporate residence under Income Tax Act s 2-2(7)–(8). Formation under Norwegian company law or actual management in Norway can establish domestic residence, subject to the treaty residence rule. Check where day-to-day and board management occur. For a foreign resident, test whether the relevant activity is carried on or managed in Norway under s 2-3 and check the applicable treaty's territorial reach, permanent establishment test and attribution. Hold the corporate outcome for a Bouvet-only operation pending that evidence. [Income Tax Act, ss 2-2 and 2-3][income-tax] · [Tax Administration foreign enterprise guidance][foreign-tax] · [Permanent establishment guidance][pe]

The ordinary Norwegian corporate rate for 2026 is 22% of taxable income for companies covered by Income Tax Act s 2-36(2). Companies liable for financial activity tax on wages pay income tax at 25% in 2026. Check special regimes separately. A Norwegian AS subject to the ordinary filing timetable submits its 2026 corporate tax return by 31 May 2027 through accounting or annual settlement software. Keep the signed return and the Altinn receipt. Assess filing duties for a foreign operator on its actual facts and keep any Tax Administration decision on an exemption. [Storting tax decision for 2026, s 3-3][annual-tax] · [Company tax return guidance][tax-return] · [May 2027 filing calendar][tax-calendar]

## Annual accounts and beneficial owners

For a Norwegian AS subject to accounts filing, adopt the annual accounts and any required annual report within 6 months of year-end. For a 31 December 2026 year-end, adopt them by 30 June 2027. Send the annual accounts and applicable attachments to the Register of Company Accounts within 1 month of adoption. For a calendar-year company the register lists 31 July of the following year as the deadline to avoid the statutory late fee. Check the distinct foreign branch rules before applying this timetable to an NUF. Keep the accounts receipt separate from the corporate tax return receipt. [Accounting Act, s 3-1][accounts-adoption] · [Companies Act, s 5-5][companies-act] · [Accounting Act, ss 8-2 and 8-3][accounts-act] · [Submission of annual accounts][accounts]

A Norwegian AS within the beneficial-owner regime registers its position within 14 days of public registration, including when it has no beneficial owners. Update the register promptly and within 14 days of a change covered by s 9. Retain the ownership and control evidence. Check the registry's limited company guidance for direct and indirect control before naming individuals. [Beneficial Owners Register Act, ss 2 and 9][bo-act] · [Registry deadlines][bo-deadline] · [Beneficial owners in a limited company][bo-as]

## Evidence to obtain

For the Bouvet-only case, confirm the territorial registration and tax position, accepted local address, treaty and permanent establishment outcome, and exact filing, fees and payment instructions. Retain the entity, tax, registry and permit determinations with the transaction records. Use the [Bouvet Island wage tax and payroll](bv-wage-tax-payroll.md) and [land and activity permits](bv-land-and-permits.md) guides for those obligations.

[dependencies]: https://lovdata.no/dokument/NL/lov/1930-02-27-3
[white-paper]: https://www.regjeringen.no/no/dokumenter/meld.-st.-33-20142015/id2415895/?ch=6
[business-register]: https://lovdata.no/dokument/NL/lov/2025-06-20-106
[commencement]: https://lovdata.no/LTI/forskrift/2025-06-20-1119
[companies-act]: https://lovdata.no/dokument/NL/lov/1997-06-13-44
[registry-as]: https://www.brreg.no/en/limited-company/register-a-limited-company/
[registry-address]: https://www.brreg.no/en/limited-company/make-changes-to-your-limited-company/
[registry-nuf-duty]: https://www.brreg.no/en/other-types-of-organisation/norwegian-registered-foreign-business-nuf/duty-to-register-with-the-register-of-business-enterprises-for-nuf/
[registry-nuf]: https://www.brreg.no/en/other-types-of-organisation/norwegian-registered-foreign-business-nuf/how-to-register-a-foreign-business/
[income-tax]: https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_2
[foreign-tax]: https://www.skatteetaten.no/en/business-and-organisation/foreign/tax-returns-and-tax-assessment-notices/tax-liability/
[pe]: https://www.skatteetaten.no/en/business-and-organisation/foreign/tax-returns-and-tax-assessment-notices/permanent-establishment/
[annual-tax]: https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747/KAPITTEL_3
[tax-return]: https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/companies/
[tax-calendar]: https://www.skatteetaten.no/en/business-and-organisation/start-and-run/deadlines-certificates-and-accounting/deadlines-and-tasks/
[accounts-adoption]: https://lovdata.no/dokument/NL/lov/1998-07-17-56/KAPITTEL_3
[accounts-act]: https://lovdata.no/dokument/NL/lov/1998-07-17-56/KAPITTEL_8
[accounts]: https://www.brreg.no/en/submission-of-annual-accounts/
[bo-act]: https://lovdata.no/dokument/NL/lov/2019-03-01-2
[bo-deadline]: https://www.brreg.no/en/beneficial-owners/
[bo-as]: https://www.brreg.no/en/beneficial-owners/beneficial-owners-in-a-limited-company/

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
