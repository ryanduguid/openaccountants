---
name: bq-tax-system
description: >
  Identify the tax framework for Bonaire, Sint Eustatius and Saba in 2026.
  Use before selecting a BES tax, taxpayer, authority, period or island
  ordinance. Explains statutory territorial definitions, residence, currency,
  national tax branches, local taxing powers and transitional liabilities.
  Maps the substantive BES companions and separates a power to levy from
  an adopted charge. Includes primary legislation and worked classification
  cases. This source-cited draft holds unverified island ordinances, customs
  detail and unresolved legal application. Load with the universal workflow
  base and applicable domain references; professional review remains required.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Ordinary 2026 assessment and statutory system scope; establish the version applicable to each event"
tier: 2
last_updated: 2026-11-21
version: 0.8
review_status: pending_review
depends_on:
  - workflow-base
---

# Bonaire, Sint Eustatius and Saba: tax-system scope

Identify the island, person or entity, activity, asset, event date and legal
instrument before selecting a tax table. The catalogue label BQ groups three
public bodies; it does not make their island ordinances identical. Load
`workflow-base`, the applicable domain base and substantive BES companions.
Preserve source gates, confirmed profile, refusals, four universal outputs
and all domain outputs/checks. This Tier 2 reference does not establish a
complete country pack or a complete financial output package.

## Territory, residence and money

Belastingwet BES articles 1.1–1.3 apply the defined BES taxes to Bonaire,
Sint Eustatius and Saba. The definition includes the specified seabed,
subsoil and resource installations beyond territorial waters, subject to
international rights and the stated sea-boundary law. Bonaire includes
Klein Bonaire. The statute distinguishes the land Netherlands, European
Netherlands and BES. It does not treat Curaçao, Aruba or Sint Maarten as BES.
Select the actual applicable jurisdiction rather than copying a European
Netherlands or neighbouring-island table. [B1, articles 1.1–1.3][B1]

Article 1.5 determines individual residence and entity establishment from
the circumstances. It contains a home-port rule for crews of BES-based
ships and aircraft. A postal address, nationality, incorporation certificate
or bank account alone is not the complete residence analysis. Entity
qualification under the distribution-tax rules needs its separate tests and
any required decision; use `bq-corporate-tax`. [B1]

The public bodies' currency is the United States dollar, divided into one
hundred cents. The currency law permits USD or the dollar symbol. This does
not prescribe every tax's rounding or a conversion rate for foreign receipts.
Keep source currency, valuation date, applicable conversion method and
statutory rounding separate. [MONEY, articles 1–2][MONEY]

## National taxes and companion references

Article 1.2 lists property tax, distribution tax, general expenditure tax
(ABB), transfer tax and gambling tax. Article 1.3's defined BES taxes also
include income tax, payroll tax and the statutory minimum-tax branch.
This list is not an assertion that customs, excise or contributions are absent.
The commencement decree expressly identifies a separate Customs and Excise
Act. Determine each applicable charge independently. [B1]; [START]

| Question | Reference and boundary |
|---|---|
| Personal income, own home, business or non-resident income | `bq-income-tax`; establish chargeable income, deductions, year and taxpayer status. |
| Entity residence, distributions, deemed European Netherlands treatment or minimum tax | `bq-corporate-tax`; incorporation alone does not establish exemption from profit taxation elsewhere. |
| Employer withholding and social or health charges | `bq-payroll` and `bq-social-contributions`; withholding and insurance coverage have different tests. |
| Supplies, services, imports, warehousing and recovery | `bq-abb`, `bq-customs-valuation`, `bq-excise` and `bq-warehouses-hde`; establish each separate charge, regime and operative condition. An ABB exemption does not establish a customs exemption or HDE admission. |
| Annual property, ground tax or acquisition | `bq-property-tax`, `bq-bonaire-ground-tax` and `bq-transfer-tax`; separate annual liability, island additions and transaction tax. |
| Gaming operator or prize | `bq-gambling-tax`; establish the licence, statutory taxpayer, base and period. |
| Inheritance, gift or personal goods arriving on an island | `bq-inheritance-gifts` for succession/gift-tax scope and `bq-personal-import-relief` for selected moving, inherited/student goods, parcels, gifts and baggage exemptions. Relief from one charge does not establish relief from another. |
| Foreign income, allocation or double-tax relief | `bq-double-tax-relief`; establish the actual instrument, covered tax, direction and relief conditions. |
| Registration, records, filing, payment, remedies or penalties | `bq-tax-compliance` for general procedure, `bq-customs-clearance` for declarations/release, `bq-customs-debt-remedies` for selected customs debt/security/refunds/remedies, and `bq-penalties-corrections` for selected administrative penalties and correction routes. Establish the actual branch, decision, event and clock; local-tax adaptations still apply. |
| Entity creation or accounts | `bq-formation` and `bq-financial-statements`; a tax computation does not complete legal formation or reporting. |

These references carry their own verification limits. Loading every named
file does not fill an unresolved legal method, source or mandatory country
slot. Nor does it confer an accountant's sign-off.

There is no universal period or due date for every tax. For example, annual
ground-tax ownership uses the start of the calendar year, while licensed
gaming operators use assigned periods and other prize branches use specified
events. Establish the actual assessment year, accounting period and event
before using a companion's deadline. [FIN, article 43][FIN];
`bq-gambling-tax`; `bq-tax-compliance`

## Ordinary assessment and authorities

The Belastingdienst Caribisch Nederland administers the national taxes. Use the island's designated authority for an adopted island charge. Domestic individual taxpayers generally report worldwide income. Foreign individual taxpayers are chargeable on specified BES-source income. A sole trader's business income normally goes in the individual return. An entity within the BES distribution regime ordinarily accounts for distribution tax on proceeds such as dividends. A different residence classification can engage European Netherlands corporate tax. Check each entity's eligibility, any required decision and the separate minimum-tax rules. [BES income tax][IB] · [Domestic taxpayers][RES] · [Distribution tax guidance][DIST] · [National tax administration][BCN]

For 2026, the ordinary individual tariff is 29.4% through USD 53,198 of the taxable amount and 38.4% above it, subject to the statutory table and any applicable adjustments. Apply the tax-free amount separately. The general distribution tax rate is 7.5% from 1 January 2025. For 2026, ordinary ABB on goods supplied by producers or imported is 8% on Bonaire and 6% on Sint Eustatius and Saba. Ordinary services are 6% and 4% respectively. Special categories and exemptions use their own rules. [2026 indexation, art XII][INDEX] · [2025 tax plan, art I(C)][DISTLAW] · [2026 ABB handbook, ch 9][ABB]

Individual assessment is annual. The authority's 2025 return notice gave 18 May 2026 as the filing deadline. For another year, check the actual invitation and any extension. A qualifying distribution triggers the distribution tax procedure. The authority generally issues ABB returns quarterly, subject to the assigned period and any special case. Check which separate event determines a property, transfer or island charge. [2025 income tax return notice][DUE] · [Distribution tax guidance][DIST] · [ABB filing periods][ABBP]

## Island taxing powers and actual ordinances

FinBES article 40 requires an island ordinance to introduce, amend or abolish
an island tax. Article 41 requires the relevant taxpayer, object, event, base,
rate, commencement/cessation and collection provisions. Article 42 limits
island taxation to its specified categories **except taxes authorised by
other laws**. Its freedom over bases and rates is subject to statutory
constraints and exceptions. An enabling provision, budget forecast or public
payment page alone does not prove that a particular rate was validly adopted
for the event. [FIN, articles 40–42][FIN]

| FinBES provision | Permitted category; actual liability still requires its legal conditions |
|---|---|
| 43–52 | Specified own-home/business ground tax and additions to national property tax. These are separate bases; an addition is a percentage of the national tax principal under article 50. |
| 53 | Tourist stays by persons not registered as residents, with the specified provider and recovery rules. |
| 54–55 | Motor-vehicle rental and holding taxes, with distinct taxable events and rate conditions. |
| 56 | Parking and parking permits; the vehicle-holder presumptions and exceptions are not a general employer or visitor tax. |
| 57–57a | Solid-waste and wastewater charges tied to their statutory activities and, for wastewater, specified environmental-law duties. |
| 58–61 | Dogs, public advertising, objects on/in/above public land, and port or anchoring use. |
| 62–64 | Specified public property/facility use and services, treated as island taxes. Estimated receipts from these fees may not exceed estimated relevant costs, including the permitted replacement reserve. |

[FIN]

Identify the island's promulgated ordinance, amendments, tariffs, effective
date, taxable period, exemptions and administrator. The same enabling law
does not establish the same visitor fee, port tariff or waste charge on
all three islands. The Bonaire ground-tax reference is not a Saba or
Sint Eustatius tariff. This batch does not supply missing island ordinances.

FinBES article 67 generally applies Belastingwet BES chapters I and VIII to
island taxes with its officer and ordinance substitutions, **excluding the
article 43(1)(b) property-tax additions from that general clause**. Article 69
permits assessment, payment on return or another method, and excludes
remittance on return. The surrounding local provisions contain further
adaptations. Do not copy national filing, collection or remedy instructions
without reading those provisions and the actual ordinance. Actual local
deadline and form mapping remains held. [FIN, articles 67 and 69][FIN]

## Transition and classification cases

Wet geldstelsel BES article 13b preserves specified pre-transition rights,
obligations and legal relationships. Its temporary continuation of the old
tax instruments is tied to the transition period ending on 1 January 2011
in article 13a. An old provision's continued presence in a consolidated
text does not by itself make its former charge applicable to a new 2026
event, and the end of that period does not extinguish saved liabilities.
The commencement decree separately brought the new tax framework into
operation. [MONEY, articles 13a–13b][MONEY]; [START]

The following fictional cases test classification, not tax amounts or an
actual ordinance's validity:

| Stipulated facts | Result to record |
|---|---|
| A Saba visitor tariff is supplied only as a Bonaire web page | Hold the Saba charge; locate Saba's actual legal basis and period. |
| National property tax is 1,000 and a valid ordinance is stipulated to impose additions of 20% of that principal | The additions component is 200 and the combined components are 1,200. The stipulated 20% is fictional, not an island rate. Do not apply it to property value. |
| A general enabling provision exists but no adopted ordinance or tariff is established | No amount or exemption is inferred; record the missing legal source. |
| A new gift occurs in 2026 and an old succession-tax text is found | Check the temporary continuation and current scope; use `bq-inheritance-gifts` for residence and other-tax exposures. |
| A liability is stipulated to have arisen before transition | Preserve its saved-law analysis rather than applying a new-event absence conclusion. |

Check the correct territory and person; actual residence; separate national
and island charges; adopted law versus permission to levy; exact taxable
period; tax principal versus asset value; and saved versus new liabilities.
Unknown mandatory conditions remain Needs Input or a hold under the loaded
workflow. A blank tax cell is not affirmative evidence of an absent tax.

## Primary sources and limits

Checked on 17 October 2026: Belastingwet BES articles 1.1–1.5; the currency
law's articles 1–2 and 13a–13b; FinBES articles 40–65, 67 and 69; and the
complete commencement decree and explanatory note. On 21 November 2026 the ordinary rates, filing and authority routes above were rechecked.
Use the companion guides for case-specific tax detail. The
Invoeringswet's current and original chapter II articles II–V read
`[vervallen]`; they are not the source of the temporary continuation rules.

This guide does not complete customs/excise, island ordinance/tariff coverage,
all special regimes, live authority routing, forms or operational engagement
testing. No filing, payment, identity submission, private records or
practitioner sign-off was used.

[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[MONEY]: https://wetten.overheid.nl/BWBR0028551/2012-07-01
[FIN]: https://wetten.overheid.nl/BWBR0028151/2023-01-01
[START]: https://zoek.officielebekendmakingen.nl/stb-2010-848.html
[IB]: https://english.belastingdienst-cn.nl/topics/tax-individuals/income-tax
[RES]: https://english.belastingdienst-cn.nl/topics/tax-individuals/income-tax/domestic-taxpayers
[DIST]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/opbrengstbelasting/veel-gestelde-vragen-en-antwoorden-qa
[BCN]: https://english.belastingdienst-cn.nl/organisation/belastingdienst-caribisch-nederland
[INDEX]: https://zoek.officielebekendmakingen.nl/stcrt-2025-40487.html
[DISTLAW]: https://zoek.officielebekendmakingen.nl/stb-2024-436.html
[ABB]: https://papiamentu.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/abb/manual-algemene-bestedingsbelasting/index/handboek-abb-versie-april-2026.pdf
[DUE]: https://english.belastingdienst-cn.nl/latest/news/2026/march/04/income-tax-return-2025
[ABBP]: https://english.belastingdienst-cn.nl/topics/tax-business/algemene-bestedingsbelasting---businesses/filing-algemene-bestedingsbelasting

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
