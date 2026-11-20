---
name: se-tax-system-orientation
description: >
  Read Sweden's ordinary tax-system orientation for territorial reach, residence,
  taxpayer types, currency, assessment periods and tax authorities.
jurisdiction: SE
category: international
tax_year: 2026
tax_year_notes: "Ordinary 2026 provisions. Check the applicable period, statutory commencement and any treaty."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Swedish tax-system orientation

Load `workflow-base`. Record where the taxpayer lives or is established, the taxpayer's legal form, the type and source of each amount, the tax period and any treaty.

## Territorial reach

Individuals and entities with unlimited Swedish tax liability are liable on income from Sweden and abroad, subject to domestic exemptions and treaty limits. Individuals with limited liability are charged only on income within the applicable provisions, including certain earnings, income from a Swedish permanent establishment or property and specified gains. Foreign legal entities generally have limited liability. Their taxable items include profit from a Swedish permanent establishment and income from Swedish property. Check separate non-resident withholding rules where relevant. [Income Tax Act 1999:1229, ch 3 ss 8–20 and ch 6 ss 3–4, 7 and 11](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/) · [Swedish Tax Agency, income tax liability](https://www.skatteverket.se/privat/skatter/arbeteochinkomst/sabeskattasdinlon/skattskyldighet)

## Residence

An individual generally has unlimited liability if domiciled in Sweden, regularly staying there or previously domiciled there and still substantially connected. Skatteverket treats a stay of at least 6 consecutive months as regular, allowing for short absences. Test substantial ties using factors including a year-round home, family and business connections. For 5 years after leaving, Swedish citizens and people who were domiciled or regularly staying there for at least 10 years have to show that substantial ties have ended. A legal person is Swedish for this purpose by registration or, when unregistered, by the board's seat or comparable circumstances. Apply any treaty residence rules separately. [Income Tax Act 1999:1229, ch 3 ss 3 and 7 and ch 6 s 3](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/) · [Swedish Tax Agency, income tax liability](https://www.skatteverket.se/privat/skatter/arbeteochinkomst/sabeskattasdinlon/skattskyldighet)

## Taxpayer types

A sole trader reports business income in the individual return. A Swedish partnership (handelsbolag, including a kommanditbolag) allocates income to its partners for income tax. An ordinary Swedish limited company (aktiebolag) pays tax on its own taxable result. For a foreign trust, compare its terms to the relevant Swedish legal form before assigning income or distributions. In HFD 2024 not. 22, powers to change trustees and appoint beneficiaries were material to whether the assets formed an independent pool comparable to a Swedish family foundation. [Income Tax Act 1999:1229, ch 2 s 2, ch 5 ss 1–3, ch 6 ss 3–4 and ch 13 ss 1–2](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/) · [Swedish Tax Agency, sole trader return](https://www.skatteverket.se/servicelankar/otherlanguages/inenglish/businessesandemployers/declaringtaxesbusinesses/incometax/incometaxreturnsforsoletraders.4.676f4884175c97df41913f3.html) · [Supreme Administrative Court, HFD 2024 not. 22](https://www.domstol.se/hogsta-forvaltningsdomstolen/avgoranden2/2024/143880/)

## Currency

The Swedish krona (SEK) is the currency unit. Eligible businesses may keep accounts in euros, with special rules for converting amounts for income tax and VAT. Record the currency and conversion basis for each foreign amount. [Riksbank Act 2022:1568, ch 4 s 1](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20221568-om-sveriges-riksbank_sfs-2022-1568/) · [Currency conversion for euro accounts Act 2000:46, ss 1 and 5–8](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-200046-om-omrakningsforfarande-vid_sfs-2000-46/)

## Assessment periods

Individuals generally use the calendar year. An eligible bookkeeping sole trader with a lawful different accounting year uses it for the business activity. Legal persons generally use their accounting year, with a calendar-year rule for businesses outside the Bookkeeping Act. An applicable Swedish partnership profit share belongs to the partner's tax year ending with or next after the partnership's year. The latter statutory rule excludes income in the capital category for individual partners. [Income Tax Act 1999:1229, ch 1 ss 13–15](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/)

## Responsible authorities

Skatteverket handles ordinary tax registration, assessment and returns. Tullverket handles customs declarations and duties. A VAT-registered importer generally reports import VAT to Skatteverket. Importers outside VAT registration generally pay it to Tullverket. [Swedish Tax Agency, company returns](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/incometax/filingataxreturnforalimitedcompanyoraneconomicassociation.4.676f4884175c97df4191467.html) · [Swedish Customs, import VAT](https://www.tullverket.se/foretag/internationellhandel/importeravaror/omtullarochavgifter/importmoms.4.7df61c5915510cfe9e7ec44.html)

## Fictional intake

A person lives in Sweden, receives foreign income and joins a Swedish partnership with a year ending before their individual year. Identify Swedish and foreign income, confirm the partnership share and reporting year, then check any domestic exemption or treaty relief.

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
