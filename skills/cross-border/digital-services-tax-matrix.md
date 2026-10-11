---
name: digital-services-tax-matrix
description: "Use this skill when a digital services provider asks about country-level DST exposure, taxable revenue, user location, thresholds or filing. Trigger on digital services tax, DST nexus, DST scope, digital tax, Canada DST, UK DST, India equalisation levy, and DST sunset. It is a calendar 2025 reference with selected Canadian repeal, Indian cut-offs and UK rules checked on 8 October 2026. Other jurisdictions require fresh primary-source verification before computation. Covers historical applicability and practitioner review. Excludes corporate income tax, permanent establishment, VAT/GST, DAC7, Pillar One calculations and withholding tax."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2025
tax_year_notes: "2025 reference; selected Canada, India and UK checks on 2026-10-08; other jurisdictions not reverified"
last_updated: 2026-10-08
review_status: pending_review
depends_on:
  - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Digital Services Tax Matrix

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It provides a country reference for a freelancer, SaaS company or marketplace assessing Digital Services Tax (DST).

**Tax year coverage and verification boundary.** The reference period is **calendar 2025**, with earlier historical regimes identified separately. The Canadian repeal, Indian application cut-offs and selected UK rules below were checked on **8 October 2026**. Other country rows, proposed-law status, Pillar One and trade-measures statements are inherited 2025 material and have not been reverified. Confirm the applicable primary law and effective dates before using those entries for calculations or compliance. This is not a comprehensive current-law matrix.

Canada's repeal received Royal Assent on 26 March 2026 and is deemed effective on 20 June 2024. India's specified-services application ends before 1 April 2025, with a separate consideration cut-off; the e-commerce regime ends before 1 August 2024. These changes apply independently of Pillar One. See sections 2.2, 2.4 and 7 for the checked sources and limits.

**The reviewer is the customer of this output.** DST scope is contested per service line and changes with national budget cycles. Every output must be reviewed by a credentialed tax practitioner in the source country before filing.

## Section 1 — Scope statement

This skill covers:

- **Country references**, including historical or replacement regimes: Austria, Canada, France, Hungary (advertising tax), India (equalisation levy), Italy, Kenya, Nepal, Spain, Tanzania (digital service tax), Tunisia, Turkey, United Kingdom, Uganda, Vietnam (e-commerce platforms), Zimbabwe. Inclusion does not establish current applicability.
- **Proposed / pending DSTs** in: Brazil, Indonesia (already converted significantly into VAT on digital supplies), New Zealand (DST Bill paused 2024), Pakistan, Poland (paused), Slovakia (paused).
- **DST scope analysis** — what services fall within each regime.
- **User-location attribution methods** for revenue allocation.
- **Threshold tests** — global revenue, domestic revenue, MNE-group scope.
- **Filing and payment mechanics**.
- **Interaction with Pillar One Amount A** and the OECD's DST political commitments.

This skill does NOT cover:

- **VAT/GST on digital services** — see country VAT/GST skills and EU OSS skill (`eu-oss-digital.md`).
- **Permanent Establishment for digital business** — see `permanent-establishment-risk.md`.
- **EU DAC7 platform reporting** — see `dac7-platform-reporting.md` (forthcoming).
- **Pillar One Amount A computation** — see `pillar-one-amount-a-b.md` (forthcoming).
- **Withholding tax on royalties / technical services** to digital service providers — see `withholding-tax-matrix.md`.

## Section 2 — Country-by-country DST matrix

### 2.1 European entries

Only the selected UK propositions were checked on 8 October 2026. Other rows retain their inherited figures and require verification against the applicable statute.

| Country | Rate | Global revenue threshold | Domestic revenue threshold | Effective from | Statute |
| --- | --- | --- | --- | --- | --- |
| **Austria** | 5% | EUR 750m worldwide | EUR 25m Austrian online ad revenue | 1 Jan 2020 | Digitalsteuergesetz 2020 |
| **France** | 3% | EUR 750m worldwide digital services | EUR 25m France-attributable digital services | 1 Jan 2019 | CGI Article 299 et seq., Loi 2019-759 |
| **Hungary** (advertising tax) | 0% (suspended through 31 Dec 2025) | HUF 100m Hungarian ad revenue | n/a (no global threshold) | 2014; rate currently 0% but the regime remains in force | Act XXII of 2014 |
| **Italy** | 3% | EUR 750m worldwide | EUR 5.5m Italian digital services revenue | 1 Jan 2020 | Legge 145/2018 Art. 1 commi 35-50, as amended |
| **Spain** | 3% | EUR 750m worldwide | EUR 3m Spanish digital services revenue | 16 Jan 2021 | Ley 4/2020 Impuesto sobre Determinados Servicios Digitales (IDSD) |
| **Turkey** | 7.5% (President may set 1%–15%) | TRY-translated EUR 750m globally; TRY 20m Turkey | n/a (combined) | 1 Mar 2020 | Law 7194 |
| **United Kingdom** | Ordinary charge: 2% | Group digital services revenues exceeding GBP 500m | UK digital services revenues exceeding GBP 25m; separate GBP 25m allowance | 1 Apr 2020 | [Finance Act 2020, ss 46–48 and 61](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml); thresholds and allowance proportionately reduced for a period shorter than a year |

### 2.2 Americas: Canadian repeal

The former Canadian DST is retained for historical context and refund review. It is not a current filing or payment instruction.

| Country | Status | Historical context | Authority |
| --- | --- | --- | --- |
| **Canada** | Act and Regulations repealed; repeal deemed effective on 20 June 2024 | Former 3% tax on certain digital services revenues; former thresholds, attribution and catch-up mechanics are not verified here | [CRA repeal guidance](https://www.canada.ca/en/services/taxes/excise-taxes-duties-and-levies/digital-services-tax.html); [Budget 2025 Implementation Act, No. 1, SC 2026 c 3, ss 126–128](https://www.laws-lois.justice.gc.ca/eng/AnnualStatutes/2026_3/page-20.html) |

### 2.3 Other inherited country entries

These rows include historical, replacement and DST-like regimes. Their figures and current status were not reverified in the selected checks. India's checked application cut-offs are in section 2.4.

| Country | Rate | Threshold | Effective from | Statute |
| --- | --- | --- | --- | --- |
| **Kenya** | 1.5% (DST repealed 25 Dec 2024 and replaced by Significant Economic Presence Tax — SEPT — at 6% effective 27 Dec 2024) | No global threshold; KES 5m local | DST: 1 Jan 2021–24 Dec 2024; SEPT: from 27 Dec 2024 | Finance Act 2020, Finance Act 2024 |
| **Nepal** | 2% | NPR 2m | Mar 2022 | Finance Act 2022 |
| **Tanzania** | 2% | n/a | 1 Jul 2022 | Finance Act 2022 |
| **Tunisia** | 3% | n/a | 1 Jan 2020 | Loi de Finances 2020 |
| **Uganda** | 5% (DST on non-resident digital service providers) | UGX 150m | 1 Jul 2023 | Tax Procedures Code (Amendment) Act 2023 |
| **Zimbabwe** | 5% | n/a (broad scope) | 1 Jan 2019 | Income Tax Act §12B |
| **Pakistan** | 5% (DST on digital marketplaces under §6A ITO) | n/a; subject to FBR-administered de minimis | 1 Jul 2024 | Income Tax Ordinance §6A as inserted by Finance Act 2024 |
| **Vietnam** | Various rates by service line (combined VAT + CIT under Decree 91/2022/NĐ-CP for non-resident platforms; effective DST-like CIT typically 5%) | n/a | 1 Jan 2022 | Decree 91/2022 |

### 2.4 Repealed or paused

**Repealed or paused**

| Country | Status |
| --- | --- |
| **Belgium** | Bill never enacted; politically paused |
| **Czech Republic** | DST bill withdrawn 2021 |
| **New Zealand** | DST Bill paused 2024 pending Pillar One |
| **Norway** | Never enacted |
| **Poland** | Paused pending Pillar One |
| **Slovakia** | Paused |
| **Canada DST** | Repealed retrospectively; see section 2.2 and the refund provisions in section 7.5 |
| **India specified-services levy** | Section 163(3)(a) applies only to specified services provided before 1 April 2025. Section 165(3), inserted by Finance Act 2025 s 146, separately excludes consideration received or receivable on or after that date. Only 1 January to 31 March 2025 is a potentially relevant 2025 service window, subject to the charging provisions and consideration test. [Section 163](https://www.incometaxindia.gov.in/w/section-163-84); [2025 amendment](https://www.incometaxindia.gov.in/w/section-146-76) |
| **India e-commerce levy** | Section 163(3)(b) covers supplies or services made, provided or facilitated from 1 April 2020 to before 1 August 2024. Historical rates, thresholds and compliance mechanics require their applicable primary provisions before calculation. [Section 163](https://www.incometaxindia.gov.in/w/section-163-84) |
| **Kenya DST (1.5%)** | Repealed 25 December 2024 (replaced by SEPT 6%) |

## Section 3 — Scope (taxable services)

The taxable services definition is the single most contested element. Major categories:

**Service-category reference.** Other countries' classifications are inherited and unverified. Canada and India require the historical/status treatment above. For the UK, revenues must arise in connection with a defined digital services activity; the labels below do not create a standalone advertising or data-sale charge. [Finance Act 2020, ss 40–45](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml).

| Service category | UK | FR | IT | ES | AT | TR | CA | IN (historical) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Online advertising** (sale of ad targeted at users in country) | In connection with a defined activity, including qualifying associated advertising | Yes | Yes | Yes | Yes (sole) | Yes | Repealed | Historical assessment only |
| **Sale of user data** | Check connection with a defined activity | Yes | Yes | Yes | No | Yes | Repealed | Historical assessment only |
| **Online intermediation / marketplace** (matching buyers/sellers) | Subject to the statutory online-marketplace definition and exclusions | Yes | Yes | No | No | Yes | Repealed | Historical assessment only |
| **Streaming and digital content** (Netflix-style subscriptions to users in country) | The content label alone does not determine a digital services activity | No | No | No | No | Yes | Repealed | Historical assessment only |
| **Search engine** | Subject to the statutory search-engine definition | Yes | Yes (within ads) | Yes (within ads) | Yes (within ads) | Yes | Repealed | Historical assessment only |
| **Social media platforms** | Subject to the statutory social-media definition | Yes | Yes | Yes | No | Yes | Repealed | Historical assessment only |

- **Inherited carve-out examples.** Payment services, own-goods e-commerce and direct B2B SaaS are unverified examples here. They do not establish a DST exemption, VAT/GST liability or current country treatment. Check the applicable primary definitions, exclusions and separate VAT/GST provisions before reaching those conclusions.

## Section 4 — User-location attribution

### 4.1 The general principle

- **Revenue attribution.** Verify whose location matters and how revenue is attributed under each applicable regime. Multiple users in different countries do not establish an automatic pro-rata allocation. For the UK, apply the specific cases and exceptions in [Finance Act 2020 s 41](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml).

### 4.2 Country-specific attribution rules

**Country-specific attribution rules**  _(see per-row citations)_

| Country | Method |
| --- | --- |
| **UK** | An individual user is one it is reasonable to assume is normally in the UK; other users must be established there. Revenue attribution follows the specific marketplace, advertising and other cases, exclusions and allocation rules in s 41. [Finance Act 2020, ss 41 and 44](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml) |
| **France** | User is located in France if used the device in France during the calendar year. CGI Art. 299 ter |
| **Italy** | User device located in Italy; for ad targeting, indicators include IP, payment, user account country. D.M. 23/06/2022 |
| **Spain** | User device located in Spain; reasonable means including IP, payment instrument, billing address. Reglamento IDSD |
| **Austria** | Online advertising received on a device with an Austrian IP address. Digitalsteuergesetz §1 |
| **Turkey** | Service provided via Turkish IP address or paid from a Turkish bank or card. Communiqué 2020 |
| **Canada** | No current attribution calculation under the repealed Act. Former-law attribution is not verified here; see section 2.2. |
| **India** | Historical assessment requires the relevant regime's definitions and charging provisions. Do not use e-commerce attribution under s 165A as a generic specified-services test. See section 2.4. |

### 4.3 Mixed-jurisdiction transactions

- **Mixed-jurisdiction transactions.** Identify the relevant service line, user and attribution rule separately for each applicable regime. Check whether the domestic rule attributes the whole amount or requires an allocation. Do not impose a common pro-rata formula across countries. Unverified country mechanics require primary-source review before modelling exposure.

For UK online marketplaces, check whether a claim for relief on a relevant cross-border transaction is available under [Finance Act 2020 s 50](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml). Its conditions and adjustments must be checked before assuming the same revenues bear an unrelieved charge in both countries.

## Section 5 — Computing DST liability

First record the transaction period, service type, legal applicability and verification status. Do not compute a current Canadian DST liability from historical rates. Indian historical computations and cross-boundary transactions require the missing charging, collection and transition material identified in section 7.7. Unverified entries require source verification before calculation.

### Step 1 — Determine the group's threshold conditions

- **Group threshold test.** Apply each verified regime's group definition and revenue measures. The UK requires group digital services revenues exceeding GBP 500m and UK digital services revenues exceeding GBP 25m, with proportionate reductions for short periods. Total group revenue or the EUR 750m CbCR threshold is not a substitute. [Finance Act 2020, ss 40 and 46](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml). Other countries' group definitions and threshold bases need their own primary checks.

### Step 2 — Determine taxable revenue

- **Determine taxable revenue.** Apply the verified service definition and country attribution rules. For the UK ordinary charge, take the group's UK digital services revenues, deduct the GBP 25m allowance (proportionately reduced for a short period), calculate 2% and allocate the group amount between liable members according to their revenue proportions. Check any relevant s 50 relief claim first. [Finance Act 2020, ss 47 and 50](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml).

### Step 3 — Apply rate

- **Ordinary liability.** Apply the verified regime's rate to its legally defined base after applicable allowances and relief. The UK alternative charge below is a separate calculation.

### Step 4 — Loss / deduction relief

- **UK elected alternative charge.** A valid return election specifies one or more categories: social media, internet search engines or online marketplaces. Apportion UK revenues and the allowance by category. For each category, let R be its apportioned UK revenues and TR the total; its allowance proportion is R/TR and net revenues are the excess over that share of GBP 25m. For an elected category, the operating margin is (R − E)/R, or nil where R does not exceed E. E comprises relevant operating expenses under s 49, with its exclusions and attribution rules. The taxable amount is 0.8 × operating margin × net revenues; do not multiply that result by a further 2%. Non-elected categories use 2% of net revenues. Add the category amounts and allocate the group amount between liable members. Adjust the allowance for a short period and check s 50 relief where applicable. [Finance Act 2020, ss 48–50](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml).
- The 2025 draft describes France, Italy and Spain as disallowing general expense deductions because DST is a turnover tax. This claim and other countries' relief were not checked; verify the applicable primary law before using them.

### Step 5 — Translation and payment

- **Currency translation and payment.** For UK groups with non-sterling consolidated accounts, use the accounting policies and exchange rates applied in preparing those accounts, as required by [HMRC's return guidance](https://www.gov.uk/guidance/submit-a-digital-services-tax-return). Verify other countries' methods and keep payment and return deadlines separate.

## Section 6 — Filing mechanics and deadlines

**Filing mechanics and deadlines**  _(see per-row citations)_

| Country | Filing portal | Deadline (annual) | Instalments |
| --- | --- | --- | --- |
| **UK** | HMRC online DST return | Return: within 12 months after the DST accounting period; payment: within 9 months and one day | Use the verified payment deadline. No quarterly percentage schedule is substantiated here. [HMRC return](https://www.gov.uk/guidance/submit-a-digital-services-tax-return); [HMRC payment](https://www.gov.uk/guidance/pay-your-digital-services-tax); [Finance Act 2020 s 51](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml) |
| **France** | DGFiP forms n° 3310-A-SD and n° 3310-CA3 | 25 October for prior calendar year | One instalment in April + one in October (50% each based on prior year) |
| **Italy** | Agenzia delle Entrate F24 form | 16 May (for prior calendar year) | Single payment |
| **Spain** | Modelo 490 | Quarterly (last 20 days of month after quarter end) | Quarterly payments |
| **Austria** | Form U30 via FinanzOnline | Last day of month after the month service was provided (monthly) | Monthly |
| **Turkey** | Monthly DST return (Beyanname Hizmet Vergisi Dijital) | Last day of following month | Monthly |
| **Canada** | CRA automatically closes DST accounts | Tax and related obligations under the repealed Act no longer apply | Refund treatment in section 7.5; [CRA guidance](https://www.canada.ca/en/services/taxes/excise-taxes-duties-and-levies/digital-services-tax.html) |
| **India** (historical equalisation levy) | Check the applicable historical statement and correction provisions | Historical filing, remittance and assessment obligations are unresolved here | Cessation of application does not establish cancellation of historical compliance obligations; see section 7.7 |

For a UK DST accounting period ending 31 December 2025, the date-rule illustration gives payment on 1 October 2026 and a return deadline of 31 December 2026. Under [Finance Act 2020 s 56](https://www.legislation.gov.uk/ukpga/2020/14/part/2/data.xml), a group's return duty continues for subsequent periods unless HMRC directs otherwise; falling below the thresholds alone does not end that duty. Other countries' combined deadline cells above have not been verified or separated into return and payment rules.

## Section 7 — Edge cases and special rules

### 7.1 Pillar One Amount A — DST sunset commitments

- **Inherited 2025 Pillar One account, not reverified.** The draft describes commitments under the OECD/G20 IF Statement of October 2021 and a 2024 Multilateral Convention text to remove DSTs, and refrain from new DSTs, upon Amount A entering into force. That political account does not establish that any particular domestic DST remains in force. The instruments, commitments and current status require primary-source verification before use.

This inherited Pillar One account has not been reverified. It does not override Canada's enacted repeal or India's statutory application cut-offs, neither of which depends on Amount A entering into force. Verify each regime's status separately.

### 7.2 US §301 retaliatory tariffs

- **US §301 retaliatory tariffs** — USTR investigations have concluded (against multiple countries) that DSTs unreasonably discriminate against US digital companies. Most tariffs were suspended pending Pillar One. Tariff risk remains live if DSTs continue post-Amount A.  _([T2])_

### 7.3 India: distinct application cut-offs

The specified-services and e-commerce regimes have separate boundaries in [Finance Act 2016 s 163(3)](https://www.incometaxindia.gov.in/w/section-163-84). Specified services must be provided before 1 April 2025; e-commerce supplies or services must be made, provided or facilitated before 1 August 2024. The [Finance Act 2025 s 146 amendment](https://www.incometaxindia.gov.in/w/section-146-76) separately inserts s 165(3), excluding specified-services consideration received or receivable on or after 1 April 2025.

Record both service timing and when consideration was received or became receivable. A later cash settlement does not, by itself, settle when an amount was receivable. Prepayments, adjustments and cross-boundary cases need the applicable primary provisions and transaction facts. Do not convert these cut-offs into a blanket statement about all outstanding historical obligations.

### 7.4 Kenya DST → SEPT transition

- **Kenya DST to SEPT transition** — The 1.5% DST was repealed by the Tax Laws (Amendment) Act 2024 effective 25 December 2024 and replaced with the Significant Economic Presence Tax (SEPT) at 6% effective 27 December 2024. SEPT applies to non-resident persons whose income from the provision of a service is derived from or accrued in Kenya through a digital marketplace. The 6% rate applies on gross turnover; SEPT is creditable against any Kenya CIT for the same business activity (which is rare for non-residents without PE).  _(Tax Laws (Amendment) Act 2024)_

### 7.5 Canada: retrospective repeal and refunds

The [Budget 2025 Implementation Act, No. 1, SC 2026 c 3](https://www.laws-lois.justice.gc.ca/eng/AnnualStatutes/2026_3/page-20.html) received Royal Assent on 26 March 2026. Sections 126 and 127 repeal the Digital Services Tax Act (enacted by SC 2024 c 15, s 96) and its Regulations, with both repeals deemed effective on 20 June 2024. This deemed repeal date is not an assertion of the former Act's original commencement date.

Under s 128, qualifying amounts paid before Royal Assent that would otherwise count as DST tax, penalty, interest or another amount must be refunded, with prescribed interest from receipt until refund. Do not calculate a refund without the applicable interest rules, rate history and payment facts. [CRA](https://www.canada.ca/en/services/taxes/excise-taxes-duties-and-levies/digital-services-tax.html) states that tax and related obligations under the Act no longer apply and accounts close automatically. These statements concern the repealed DST regime; they do not determine unrelated Canadian tax liabilities.

### 7.6 Group-level vs entity-level

For the UK, the responsible member submits group returns under [HMRC's guidance](https://www.gov.uk/guidance/submit-a-digital-services-tax-return), while s 47 allocates liability between relevant persons and s 56 provides the continuing-return duty. Verify other regimes' filing arrangements separately; do not assume every country requires an in-country group entity to file.

### 7.7 India: historical compliance questions

The checked cut-off provisions do not establish the complete historical rates, thresholds, payer scope, deduction timing, remittance, statement or correction rules. Read the relevant versions of ss 164, 165, 165A, 166, 166A and the statement provisions, applicable Equalisation Levy Rules and transition material before giving an operational historical answer. Any income-tax deduction-disallowance claim also needs its applicable income-tax provision. Those details are unresolved here; the former withholding and disallowance instructions have been withdrawn. Cessation must not be treated as proof that historical statements, assessments or remittances were cancelled.

### 7.8 VAT / GST overlap

Establish any VAT/GST liability, collection obligation and credit or offset from the applicable primary provisions. Do not infer these from a DST service classification. No general VAT/GST collection, gross-revenue or no-netting rule is verified here.

## Section 8 — Output specification

Every conclusion in the reviewer brief must be supported by verified primary law for the relevant period. Where that support is missing, record the matter as unresolved. Do not use an inherited table or general example to establish a classification, exemption, attribution, liability or deadline.

The reviewer brief must include:

1. **Period, applicability and verification status** for each regime, with the supporting authority; then its verified group and revenue tests.
2. **In-scope services analysis** using verified country-specific primary definitions; identify unverified classifications separately.
3. **User-location attribution computation** — methodology applied, supporting data.
4. **Liability computation** only for a verified applicable regime, in the required currency; identify unresolved calculations separately.
5. **Payment schedule** supported by the relevant authority; do not generate the discarded UK quarterly percentages.
6. **Separate return and payment calendar** with primary references and any continuing-return duty.
7. **Pillar One Amount A status update** — note if any DST has sunset triggered.
8. **Historical India compliance and Canadian refund questions**, with missing provisions or facts identified; no automatic current withholding or retrospective payment instruction.
9. **Reviewer questions** — open items flagged as [T2] or [T3].

## Section 9 — Self-checks

Before delivering output, verify:

- [ ] Each classification, exemption, attribution, calculation and deadline supported by verified primary law for the relevant period; unsupported conclusions recorded as unresolved.
- [ ] Period and legal applicability established before using any rate or threshold.
- [ ] Group definition and revenue measure verified for each regime; UK digital services revenue distinguished from total group revenue.
- [ ] In-scope services tested against the specific country scope (not assumed by analogy).
- [ ] User-location attribution applied per the country's prescribed indicators.
- [ ] Country-specific allowances (e.g., UK GBP 25m) deducted before rate applied.
- [ ] Loss / safe harbour relief considered (UK margin-based alternative).
- [ ] Currency translation method per country.
- [ ] Return and payment dates separated; any instalment schedule supported by applicable authority.
- [ ] India service and consideration dates recorded; unresolved historical obligations and cross-boundary cases identified.
- [ ] Canada treated under enacted retrospective repeal and refund provisions, with no current DST filing or payment instruction.
- [ ] UK continuing-return duty checked separately from current-period thresholds.
- [ ] Pillar One Amount A status checked before relying on long-term DST liability.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 10 — Prohibitions

- **Do not** assume an exemption from VAT/GST means DST does not apply — they are independent regimes.
- **Do not** allocate revenue using a single country's attribution method to compute another country's DST.
- **Do not** treat the OECD Pillar One IF statement as a binding sunset until Amount A actually enters into force.
- **Do not** advise on structuring to escape DST scope (e.g., moving the contracting entity outside the group) without confirming anti-avoidance rules in each affected country.
- **Do not** revive Canadian DST liability from the repealed Act or condition its repeal on Pillar One.
- **Do not** treat India's application cut-offs as cancellation of every historical compliance obligation, or use cash settlement alone to resolve the consideration test.
- **Do not** present inherited country entries or this guide's edit date as comprehensive current-law verification.

## Section 11 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. DST regimes change with each national budget and the Pillar One political process. Every output must be reviewed and signed off by a credentialed practitioner in each source country before any DST return is filed.

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
