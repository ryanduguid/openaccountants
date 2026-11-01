---
name: germany-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Germany. Trigger on phrases like "set up a company in Germany", "GmbH formation", "UG gründen", "Handelsregister", "German company formation", "register a business Germany", "Gesellschaft mit beschränkter Haftung", "Unternehmergesellschaft", "German notary", "Gewerbeanmeldung", or any question about starting a business entity in Germany. Covers entity types (GmbH, UG, AG, GbR, KG), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on German company formation.
version: 1.1
jurisdiction: DE
tax_year: 2025
last_updated: 2026-11-01
review_status: pending_review
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Formation

## Germany Company Formation Skill v1.1

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Germany (Federal Republic of Germany) |
| Currency | EUR |
| Company registrar | Handelsregister (via local Amtsgericht / district court) |
| Key legislation | GmbH-Gesetz (GmbHG) — https://www.gesetze-im-internet.de/gmbhg/; Handelsgesetzbuch (HGB) — https://www.gesetze-im-internet.de/hgb/; Aktiengesetz (AktG) — https://www.gesetze-im-internet.de/aktg/ |
| Typical formation time | 3--6 weeks (notary to Handelsregister entry) |
| Corporate tax rate | ~30% effective in VZ 2026 (15% Körperschaftsteuer + 5.5% Solidaritätszuschlag on it, 0.825 points, + ~14% Gewerbesteuer); Körperschaftsteuer steps down from 14% in 2028 to 10% from 2032 (KStG s 23(1)) |
| Skill version | 1.1 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Einzelunternehmen (Sole Trader) | GmbH | UG (haftungsbeschränkt) | GbR / OHG / KG (Partnerships) | AG (Public Company) |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | Yes | Yes | GbR: No; OHG/KG: Yes | Yes |
| Liability | Unlimited | Limited to share capital | Limited to share capital | Unlimited (GbR/OHG); KG: limited for Kommanditist | Limited to share capital |
| Min. founders | 1 | 1 | 1 | 2 | 1 |
| Min. share capital | N/A | €25,000 | €1 | N/A | €50,000 |
| Min. paid-up at formation | N/A | €12,500 (50%) | 100% of stated capital | N/A | 25% (€12,500) |
| Tax treatment | Income tax | Corporate | Corporate | Partners taxed individually | Corporate |
| Notary required | No | Yes | Yes | No (except KG for Handelsregister) | Yes |
| Admin burden | Low | High | High | Low--Medium | Very High |

**Recommended default:** GmbH for established businesses; UG for bootstrapped startups with plan to convert to GmbH.

## Section 3 -- Registration Process

### Step 1: Draft Gesellschaftsvertrag (Articles of Association)

- **Musterprotokoll usage** — Use Musterprotokoll (standard template, §2 Abs. 1a GmbHG) for simple cases: max 3 founders, 1 Geschäftsführer, cash contributions only  _(§2 Abs. 1a GmbHG)_
- **Custom Satzung usage** — Custom Satzung for complex structures (multiple share classes, vesting, investor rights)

### Step 2: Notary Appointment (Beurkundung)

- **Notarisation requirement** — Articles must be notarised (§2 GmbHG)  _(§2 GmbHG)_
- **Video notarisation** — Video notarisation available since August 2022 for cash-only GmbH/UG
- **Notary prepares Handelsregister application** — Notary also prepares Handelsregister application

### Step 3: Open Bank Account and Deposit Capital

- **Geschäftskonto naming** — Open a Geschäftskonto in the name of "GmbH i.G." (in Gründung)
- **GmbH deposit requirement** — GmbH: deposit min. €12,500 (50% of €25,000 minimum)
- **UG deposit requirement** — UG: deposit 100% of stated share capital (min. €1)
- **Bank confirmation** — Obtain bank confirmation (Bankbestätigung) for notary

### Step 4: Handelsregister Filing

- **Electronic submission** — Notary submits electronically to the Amtsgericht
- **Registration fee** — €225 (cash contributions) or €360 (in-kind contributions) -- effective 1 June 2025  _(effective 1 June 2025)_
- **Legal existence date** — GmbH/UG legally exists from date of Handelsregister entry (§11 Abs. 1 GmbHG)  _(§11 Abs. 1 GmbHG)_

### Step 5: Gewerbeanmeldung (Trade Registration)

- **Registration requirement** — Register with local Gewerbeamt (§14 GewO)  _(§14 GewO)_
- **Fee** — €15--€65 depending on municipality

### Step 6: Tax Registration (Steuerliche Erfassung)

- **Fragebogen** — Complete Fragebogen zur steuerlichen Erfassung via ELSTER
- **Steuernummer** — Obtain Steuernummer from local Finanzamt
- **USt-IdNr** — Apply for USt-IdNr. (VAT identification number) if trading intra-EU

### Step 7: Transparenzregister (Beneficial Ownership Register)

- **Registration requirement** — Register beneficial owners with Transparenzregister (§20 GwG)  _(§20 GwG)_
- **Mandatory since 2021** — Mandatory since 2021 (no longer automatic from Handelsregister)

### Step 8: Further Registrations

- **IHK membership** — IHK (Chamber of Commerce) -- mandatory membership, automatic upon Gewerbeanmeldung
- **Berufsgenossenschaft** — Berufsgenossenschaft (employer's liability insurance, §192 SGB VII) -- mandatory even without employees  _(§192 SGB VII)_

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up at Filing | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| GmbH | €25,000 | €12,500 (50%) | Before Handelsregister filing | Permitted (triggers higher registration fee of €360) |
| UG (haftungsbeschränkt) | €1 | 100% of stated capital | Before Handelsregister filing | NOT permitted (§5a GmbHG) |
| AG | €50,000 | 25% (€12,500) | Before registration | Permitted (independent valuation required) |

Sources: GmbHG § 5 Abs. 1 (EUR 25,000) — https://www.gesetze-im-internet.de/gmbhg/__5.html; § 7 Abs. 2 (a quarter of each share, and in total at least half of the minimum capital, before registration) — https://www.gesetze-im-internet.de/gmbhg/__7.html; § 5a (UG: full payment, no contributions in kind) — https://www.gesetze-im-internet.de/gmbhg/__5a.html; AktG § 7 (EUR 50,000) — https://www.gesetze-im-internet.de/aktg/__7.html; § 36a (at least a quarter of the lowest issue price) — https://www.gesetze-im-internet.de/aktg/__36a.html.

- **UG statutory reserve:** Under [GmbHG § 5a(3)](https://www.gesetze-im-internet.de/gmbhg/__5a.html), reserve one quarter of annual surplus after reducing it by the previous year's loss carryforward; reserve use is restricted by that subsection. Subsections (1)–(4) cease to apply when the company increases its share capital to at least the § 5(1) minimum (§ 5a(5)). Merely accumulating that amount in reserves does not supply the capital-increase trigger or establish an automatic conversion. The UG designation may be retained. The capital-increase procedure requires separate qualification.

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | GmbH (EUR) | UG (EUR) | Notes |
| --- | --- | --- | --- |
| Notary fee (Musterprotokoll) | €115--€300 | €60--€150 | Based on GNotKG; scales with capital |
| Notary fee (custom Satzung) | €470--€1,500 | €300--€800 | VC-ready structures at higher end |
| Handelsregister fee | €225 | €225 | €360 if in-kind contributions |
| Gewerbeanmeldung | €15--€65 | €15--€65 | Municipality-dependent |
| Share capital deposit | €12,500 (min.) | €1 (min.) | Stays in company as working capital |
| Steuerberater (initial setup) | €500--€1,500 | €500--€1,500 | Tax registration and ELSTER |
| **Total (excl. capital)** | **€1,300--€3,600** | **€800--€2,800** |  |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (EUR) |
| --- | --- |
| IHK membership | €150--€500/year (minimum assessment) |
| Berufsgenossenschaft | From €100/year |
| Steuerberater | €2,000--€10,000/year |
| Annual accounts disclosure or deposit | Current register charges not qualified here; verify before budgeting |
| Handelsregister changes | €90--€180 per entry |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Jahresabschluss (annual accounts preparation) | Normally the first 3 months of the following business year; eligible small companies may use the first 6 months only if consistent with orderly business (conditions below) | Legal representatives; HGB § 264(1) |
| Offenlegung (disclosure) | Normally no later than 1 year after the reporting date; HGB § 264d companies have a maximum of 4 months | Electronic transmission to the Unternehmensregister operator; HGB § 325 |
| Körperschaftsteuererklärung (corporate tax return) | Apply the calendar-period, adviser and early-call conditions below | Finanzamt |
| Gewerbesteuererklärung (trade tax return) | Apply the calendar-period, adviser and early-call conditions below | Competent Finanzamt (tax-measurement return) |
| Umsatzsteuervoranmeldung (VAT returns) | Monthly or quarterly | Finanzamt |
| Gesellschafterliste (shareholder list) | Update and file with Handelsregister on any change | Handelsregister |
| Transparenzregister | Update within 14 days of beneficial ownership changes | Transparenzregister |

**Accounts preparation and disclosure:** [HGB § 264(1)](https://www.gesetze-im-internet.de/hgb/__264.html) sets the preparation periods above. Small companies need not prepare a management report, but the 6-month preparation period is conditional on orderly business. Small status under [HGB § 267](https://www.gesetze-im-internet.de/hgb/__267.html) requires at least 2 of 3 limits not to be exceeded: EUR 7.5 million balance sheet, EUR 15 million turnover over the preceding 12 months and 50 average employees. Apply the reporting-date rules, normal 2-consecutive-year requirement, new-formation/conversion exceptions and calculation rules in subsections (4)–(6). A company within [HGB § 264d](https://www.gesetze-im-internet.de/hgb/__264d.html) is always large; this definition includes an application for admission of securities to an organised market. The incorporated securities/market definitions and actual entity facts need separate verification. [EGHGB article 93](https://www.gesetze-im-internet.de/hgbeg/art_93.html) makes the specified 17 April 2024 threshold versions mandatory for financial years beginning after 31 December 2023 and permits the specified package as a whole for years beginning after 31 December 2022. Do not apply the newer thresholds to an earlier period without its applicable text.

[HGB § 325](https://www.gesetze-im-internet.de/hgb/__325.html) concerns the established/adopted annual accounts and other documents insofar as required; changes also require disclosure. Transmission time determines timeliness. The exception for a late supervisory-board report or AktG § 161 declaration does not generally extend the annual-accounts deadline. [EGHGB article 88(2)](https://www.gesetze-im-internet.de/hgbeg/art_88.html) applies the specified 1 August 2022 versions to financial years beginning after 31 December 2021; the financial year’s start, rather than the submission date, controls that transition. Earlier periods require their applicable earlier text. [HGB § 8b](https://www.gesetze-im-internet.de/hgb/__8b.html) distinguishes accounting disclosures from corporate notices in the Bundesanzeiger. Check the conditional group exemption in § 264(3), small/micro/medium disclosure relief in [§ 326](https://www.gesetze-im-internet.de/hgb/__326.html) and [§ 327](https://www.gesetze-im-internet.de/hgb/__327.html), and the [§ 267a](https://www.gesetze-im-internet.de/hgb/__267a.html) micro-company criteria before choosing documents or permanent deposit. Preparation obligations and disclosure relief are separate. These notes do not establish the complete document package, audit obligation, register charges, filing interface or actual filing readiness.

For the relevant ordinary calendar-year company returns, [AO § 149(2)–(4)](https://www.gesetze-im-internet.de/ao_1977/__149.html) normally gives 7 months after the calendar year. Eligible listed returns prepared by an engaged authorised adviser normally run to the last day of February in the second following calendar year. A valid early call sets 4 months after notification and cannot shorten the ordinary subsection (2) period. Apply statutory exceptions, actual notices and [AO § 108(3)](https://www.gesetze-im-internet.de/ao_1977/__108.html) to a period ending on a weekend or public holiday; authority-set appointments have a separate rule in [AO § 108(5)](https://www.gesetze-im-internet.de/ao_1977/__108.html). The qualified pandemic modifications in [EGAO article 97 § 36](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html) do not establish an extension for VZ 2026. For the ordinary resident GmbH/UG VZ 2026 calendar-year profile, use the conditional dates and filing holds in [de-corporate-income-tax](de-corporate-income-tax.md). Other compliance rows require separate current-period verification before use; actual filing readiness remains held.

The trade-tax return concerns assessment of the tax-measurement amount under [GewStG § 14a](https://www.gesetze-im-internet.de/gewstg/__14a.html); [AO § 22(1)](https://www.gesetze-im-internet.de/ao_1977/__22.html) identifies the competent Finanzamt, including a special rule for specified foreign-based construction businesses. [GewStG § 1](https://www.gesetze-im-internet.de/gewstg/__1.html) provides for municipal levy. Assessment of the measurement amount is distinct from levy and collection; AO § 22(2)–(3) addresses cases involving Finanzamt collection or Länder revenue. Case-specific competence, allocation, submission method and actual notices require separate verification.

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Required documents** — - Handelsregisterauszug (commercial register extract) - Gesellschaftsvertrag (articles of association) - Notarised appointment of Geschäftsführer - ID (passport/Personalausweis) for all directors and shareholders (25%+) - Proof of address for all beneficial owners - Business plan or description of activities

### Typical Timeline

- **Traditional banks** — Traditional banks: 2--4 weeks (KYC process)
- **Neo-banks** — Neo-banks (Qonto, Penta/Qonto, Finom): 1--5 days
- **i.G. stage note** — Note: account can be opened in "GmbH i.G." stage before Handelsregister entry

### Common Banks

- Deutsche Bank, Commerzbank, Sparkasse, Volksbank (traditional)
- Qonto, Finom, N26 Business (digital)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident Geschäftsführer allowed? | Yes -- no residency requirement |
| Minimum German-resident director? | No legal requirement (but practical for banking and tax) |
| Video notarisation for foreigners? | Available since 2022 for cash-only formations; requires EU-compatible eID |
| Apostille requirements | Foreign documents require apostille or legalisation + certified German translation |
| Physical presence required? | Not strictly; power of attorney (Vollmacht) accepted for notary appointment |
| Foreign ownership restrictions | None for GmbH; specific sectors (defence, critical infrastructure) may require approval under AWV |

## Section 9 -- Common Mistakes and Refusals

- **R-DE-F1 -- UG with €1 capital and no plan** — While legally possible, forming a UG with only €1 capital is impractical. Banks may refuse to open accounts, and the entity cannot cover basic operating costs. Always advise a minimum of €2,000--€5,000 for credibility and operations.  _(R-DE-F1)_
- **R-DE-F2 -- Trading before Handelsregister entry** — The GmbH does not legally exist until entered in the Handelsregister. The Geschäftsführer is personally liable for obligations incurred during the 'i.G.' period. Flag this risk clearly.  _(R-DE-F2)_
- **R-DE-F3 -- Missing Transparenzregister filing** — Since 2021, automatic transfer from Handelsregister no longer applies. Failure to file with Transparenzregister can result in fines up to €150,000.  _(R-DE-F3)_
- **R-DE-F4 -- Sacheinlage in UG** — In-kind contributions (Sacheinlage) are prohibited for UG formations under §5a GmbHG. Only cash contributions are permitted.  _(R-DE-F4, §5a GmbHG)_
- **R-DE-F5 -- Ignoring Berufsgenossenschaft** — Registration with the Berufsgenossenschaft is mandatory even if the GmbH has no employees. Non-registration is an Ordnungswidrigkeit.  _(R-DE-F5)_

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Draft articles / Musterprotokoll | 1--5 days | Day 1--5 |
| Notary appointment | 1--7 days | Day 2--12 |
| Open bank account (i.G.) and deposit capital | 1--3 weeks | Day 9--33 |
| Notary files with Handelsregister | 1 day | Day 10--34 |
| Handelsregister entry | 1--3 weeks | Day 17--55 |
| Gewerbeanmeldung | 1--3 days | Day 18--58 |
| Tax registration (ELSTER) | 2--6 weeks | Day 32--100 |
| Transparenzregister | 1--2 days | Day 33--102 |
| **Ready to trade** |  | **~4--8 weeks** |

The main bottleneck is Handelsregister processing time, which varies significantly by court district.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
