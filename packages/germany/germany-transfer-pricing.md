---
name: germany-transfer-pricing
description: Use this skill whenever asked about Germany transfer pricing rules, documentation requirements, or Verrechnungspreise compliance. Trigger on phrases like "transfer pricing Germany", "German TP documentation", "Verrechnungspreise", "master file Germany", "local file Germany", "CbCR Germany", "APA Germany", "§90 AO", "transaction matrix Germany", "BZSt", or any question about intercompany pricing for German entities.
version: 1.2
jurisdiction: DE
tax_year: 2025
tax_year_notes: "Retained historical 2025 reference with separately dated later-law notes; full historical and current-law currency remains unverified. Not requalified as a 2026 whole-guide computation."
last_updated: 2026-11-02
review_status: pending_review
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Transfer Pricing

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use the transfer-pricing-workflow-base to prepare documentation and referral working papers. The retained primary year is 2025. Current TP documentation thresholds, procedures, language acceptance, penalties, APA terms and safe-harbour claims are not requalified by the selected corporate-return deadline corrections.

Retained material marked unverified is for professional source review and must not be used to compute an actual liability, recommend an arrangement, register, file or pay. Structural conformance and hypothetical arithmetic do not establish legal currency or professional approval.

### Germany Transfer Pricing Skill v1.2



### Section 1 -- Quick Reference

**Quick Reference**

| Field | Value | Source or qualification |
| --- | --- | --- |
| Country | Germany (Federal Republic of Germany) | Retained context; see scope and source limits |
| Tax authority | Federal Central Tax Office (Bundeszentralamt für Steuern -- BZSt); local tax offices for audits | Retained context; see scope and source limits |
| Key TP legislation | §90(3) Abgabenordnung (AO -- General Tax Code); §1 Außensteuergesetz (AStG -- Foreign Tax Act) | unverified: inherited figure or assumption; professional/source qualification required |
| Documentation regulation | GAufzV (Gewinnabgrenzungsaufzeichnungsverordnung) | Retained context; see scope and source limits |
| OECD member? | Yes | Retained context; see scope and source limits |
| BEPS signatory? | Yes | Retained context; see scope and source limits |
| Effective date (current regime) | Three-tier approach from FYs beginning after 31 Dec 2016; major reforms from 1 Jan 2025 | unverified: inherited figure or assumption; professional/source qualification required |
| Currency | EUR | unverified: inherited figure or assumption; professional/source qualification required |
| Documentation language | German (English accepted for Master File in practice) | Retained context; see scope and source limits |
| Skill version | 1.2 | unverified: inherited figure or assumption; professional/source qualification required |

## Ask the client first

Confirm covered taxpayer and accounting period; associated parties and cross-border transactions; prior-year entity/group revenue and transaction volumes; transaction/extraordinary-event and audit/request dates; contemporaneous method, costs and comparable evidence; and actual BZSt forms, schema, submission and acknowledgment requirements.

## The method, step by step

### Section 2 -- Documentation Requirements

#### 2.1 Master File (Stammdokumentation)

**Master File**

| Item | Detail | Source or qualification |
| --- | --- | --- |
| Required? | Yes, if consolidated group revenue in prior FY ≥ EUR 100 million | unverified: inherited figure or assumption; professional/source qualification required |
| Format | OECD Annex I to Chapter V | Retained context; see scope and source limits |
| Filing | Submit within 30 days of audit order (from 1 Jan 2025) | unverified: inherited figure or assumption; professional/source qualification required |
| Language | German preferred; English accepted in practice | Retained context; see scope and source limits |

#### 2.2 Local File (Landesspezifische Dokumentation)

**Local File**

| Item | Detail | Source or qualification |
| --- | --- | --- |
| Required? | Yes, if related-party transaction thresholds exceeded | Retained context; see scope and source limits |
| Thresholds | Goods: EUR 6 million/year; Other transactions (services, IP, finance): EUR 600,000/year | unverified: inherited figure or assumption; professional/source qualification required |
| Format | Detailed arm's length analysis per transaction category | Retained context; see scope and source limits |
| Filing | On separate request during audit (30-day deadline from request, from 2025) | unverified: inherited figure or assumption; professional/source qualification required |

#### 2.3 Transaction Matrix (Aufzeichnungen über die Geschäftsbeziehungen)

From 1 January 2025 (Fourth Bureaucracy Reduction Act -- BEG IV):

**Transaction Matrix**

| Item | Detail | Source or qualification |
| --- | --- | --- |
| Content | Overview of all cross-border related-party transactions | Retained context; see scope and source limits |
| Submission | Within 30 days of audit order announcement | unverified: inherited figure or assumption; professional/source qualification required |
| Format | Standardized; clarified by BMF notice of 2 April 2025 | unverified: inherited figure or assumption; professional/source qualification required |

#### 2.4 Country-by-Country Report (CbCR)

**CbCR**

| Item | Detail | Source or qualification |
| --- | --- | --- |
| Threshold | Consolidated group revenue ≥ EUR 750 million (prior FY) | unverified: inherited figure or assumption; professional/source qualification required |
| Filing deadline | Within 12 months of end of FY | unverified: inherited figure or assumption; professional/source qualification required |
| Filing method | Electronic (XML) to BZSt | Retained context; see scope and source limits |
| Notification | Required from constituent entities | Retained context; see scope and source limits |
| Effective | FYs beginning after 31 December 2015 | unverified: inherited figure or assumption; professional/source qualification required |

### Section 3 -- Arm's Length Standard

#### 3.1 Definition

- **Arm's length principle**  -  Income of a taxpayer from cross-border transactions with related parties must be determined as if the transactions had been agreed between unrelated parties under comparable conditions (arm's length principle). Germany applies a "hypothetical arm's length test" where no comparable exists.  _(§1 AStG)_

#### 3.2 Accepted Methods

**Accepted Methods**

| Method | Accepted | Source or qualification |
| --- | --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes | Retained context; see scope and source limits |
| Resale Price Method (RPM) | Yes | Retained context; see scope and source limits |
| Cost Plus Method (CPM) | Yes | Retained context; see scope and source limits |
| Transactional Net Margin Method (TNMM) | Yes | Retained context; see scope and source limits |
| Profit Split Method (PSM) | Yes | Retained context; see scope and source limits |
| Hypothetical arm's length test | Yes (unique to Germany) | Retained context; see scope and source limits |

#### 3.3 Preferred Method

- **Preferred method**  -  Standard CUP is preferred where reliable comparables exist. The hypothetical arm's length test applies when no comparable transactions are available (particularly for unique intangibles and business restructurings).

#### 3.4 Range/Median

- **Range/median adjustment**  -  Tax authorities may use the median of the interquartile range for adjustments if taxpayer's result falls outside the arm's length range.

## Boundary and exception table

### Section 7 -- Advance Pricing Agreements (APA)

**APA**

| Item | Detail | Source or qualification |
| --- | --- | --- |
| Availability | Yes | Retained context; see scope and source limits |
| Types | Unilateral, Bilateral, Multilateral | Retained context; see scope and source limits |
| Governing authority | BZSt (coordinates with local tax office) | Retained context; see scope and source limits |
| Application fee | EUR 20,000 (simplified: EUR 10,000) | unverified: inherited figure or assumption; professional/source qualification required |
| Typical duration | 3-5 years prospective; rollback possible | unverified: inherited figure or assumption; professional/source qualification required |
| Processing time | 12-36 months (bilateral longer) | unverified: inherited figure or assumption; professional/source qualification required |
| Binding effect | Binding on tax authorities for covered period | Retained context; see scope and source limits |
| Annual reporting | Compliance reports required | Retained context; see scope and source limits |

### Section 8 -- Safe Harbours

Germany does not have broad statutory safe harbour rules.

**Safe Harbours**

| Area | Detail | Source or qualification |
| --- | --- | --- |
| Low-value intra-group services | OECD simplified approach (cost-plus 5%) generally accepted in practice | unverified: inherited figure or assumption; professional/source qualification required |
| Interest rates | No formal safe harbour; Bundesbank reference rates used as benchmarks | Retained context; see scope and source limits |
| Documentation thresholds | Below EUR 6m (goods) / EUR 600k (other), no Local File required but arm's length must still be demonstrated | unverified: inherited figure or assumption; professional/source qualification required |
| Small transactions | No statutory de minimis; all cross-border related-party transactions subject to arm's length principle | Retained context; see scope and source limits |

#### 8.1 Practical Implications of Documentation Thresholds

While Germany has no formal safe harbour, the documentation thresholds effectively reduce compliance burden:
- Below EUR 6m goods / EUR 600k other: no Local File required
- Below EUR 100m group revenue: no Master File required
- However, the general obligation under §90 AO to cooperate with tax authorities remains
- Tax authorities can still challenge pricing even without formal documentation requirements

### Section 9 -- Recent Developments

**Recent Developments**

| Date | Development | Source or qualification |
| --- | --- | --- |
| January 2025 | BEG IV: Transaction matrix mandatory; shortened submission deadlines (30 days) | unverified: inherited figure or assumption; professional/source qualification required |
| April 2025 | BMF information sheet on transaction matrix content | unverified: inherited figure or assumption; professional/source qualification required |
| 2024 | Pillar Two (GloBE) implemented via Mindeststeuergesetz (MinStG) for FYs from 31 Dec 2023 | unverified: inherited figure or assumption; professional/source qualification required |
| Ongoing | Increased audit intensity on TP; digital audit tools deployed | Retained context; see scope and source limits |
| 2022 | §1 AStG reform: enhanced hypothetical arm's length test for function relocations | unverified: inherited figure or assumption; professional/source qualification required |
| Ongoing | OECD Pillar One Amount B: Germany monitoring implementation | Retained context; see scope and source limits |

## Worked cases

### Recomputing hypothetical components

These cases test arithmetic and the stated decision boundary only. All facts and unverified parameters are explicit assumptions. They do not establish entitlement or an actual tax, legal, investment or entity-choice recommendation.

#### Case 1

Assume, purely for arithmetic, EUR 100,000 eligible costs and a 5% markup. EUR 5,000 is added, giving EUR 105,000. This does not establish that 5% is an accepted German safe harbour or that these are eligible costs or comparable services.

```oa-check
name: DE hypothetical cost-plus arithmetic without safe-harbour qualification
inputs:
  assumed_eligible_costs: 100000
  assumed_markup: 0.05
steps:
  - markup_component: assumed_eligible_costs * assumed_markup
  - illustrative_price: assumed_eligible_costs + markup_component
expected:
  markup_component: 5000
  illustrative_price: 105000
```

#### Case 2

Compare the same assumed cost-plus EUR 105,000 with an unverified comparable price of EUR 110,000. The gap is EUR 5,000 or 5% of costs. The decision is to hold method selection and refer for comparability and legal review; the larger or smaller number alone cannot choose the method.

```oa-check
name: DE hypothetical comparator discrepancy requires referral
inputs:
  assumed_costs: 100000
  assumed_markup: 0.05
  unverified_comparable_price: 110000
steps:
  - cost_plus_candidate: assumed_costs * (1 + assumed_markup)
  - candidate_gap: unverified_comparable_price - cost_plus_candidate
  - gap_to_costs: candidate_gap / assumed_costs
expected:
  cost_plus_candidate: 105000
  candidate_gap: 5000
  gap_to_costs: 0.05
```

## When to refuse or refer

Refuse an actual-case output whilst any required source, period, taxpayer fact, classification, entitlement, instruction or submission condition is unresolved. Refer legal, tax and specialist issues to the appropriately qualified German professional.

## Filing and payment

### Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail | Source or qualification |
| --- | --- | --- |
| Transaction matrix | Submit within 30 days of audit order (from 2025) | unverified: inherited figure or assumption; professional/source qualification required |
| Master File | Submit within 30 days of audit order (from 2025) | unverified: inherited figure or assumption; professional/source qualification required |
| Local File | Submit within 30 days of separate request during audit | unverified: inherited figure or assumption; professional/source qualification required |
| Extraordinary transactions | Submit within 30 days of audit order | unverified: inherited figure or assumption; professional/source qualification required |
| CbCR | Annual electronic filing with BZSt | Retained context; see scope and source limits |
| CbCR notification | Annual notification to BZSt | Retained context; see scope and source limits |
| Corporate tax return | No separate TP disclosure form | Retained context; see scope and source limits |

### Section 5 -- Deadlines

**Deadlines**

| Item | Deadline | Source or qualification |
| --- | --- | --- |
| Documentation preparation | Contemporaneous; must be available when audit begins | Retained context; see scope and source limits |
| Transaction matrix + Master File submission | 30 days from audit order (audits from 1 Jan 2025) | unverified: inherited figure or assumption; professional/source qualification required |
| Local File submission | 30 days from separate request | unverified: inherited figure or assumption; professional/source qualification required |
| Extraordinary transactions | 30 days from audit order | unverified: inherited figure or assumption; professional/source qualification required |
| CbCR filing | 12 months after end of FY | unverified: inherited figure or assumption; professional/source qualification required |
| Corporate tax return | For the relevant calendar-year return, normally 7 months after the calendar year; eligible listed returns prepared by an engaged authorised adviser normally run to the last day of February in the second following calendar year, subject to early call and the statutory exceptions (AO § 149(2)-(4)) | https://www.gesetze-im-internet.de/ao_1977/__149.html ; https://www.gesetze-im-internet.de/ao_1977/__108.html (calendar return only) |

Do not derive the corporate return date from an arbitrary financial year-end or treat it as the TP-documentation submission deadline. Apply the actual period and notice, [AO § 108](https://www.gesetze-im-internet.de/ao_1977/__108.html) and the applicable transition rules. The qualified [EGAO article 97 § 36](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html) pandemic provisions supply no automatic VZ 2026 extension. [AO § 149](https://www.gesetze-im-internet.de/ao_1977/__149.html) requires the adviser and return conditions; its early-call period is 4 months after notification and cannot shorten subsection (2). The ordinary resident GmbH/UG calendar-year VZ 2026 profile and its filing holds are in [de-corporate-income-tax](de-corporate-income-tax.md).

### Section 6 -- Penalties

**Penalties**

| Offence | Penalty | Source or qualification |
| --- | --- | --- |
| Non-submission or unusable documentation | 5-10% surcharge on income adjustment (minimum EUR 5,000 per transaction) | unverified: inherited figure or assumption; professional/source qualification required |
| Late submission of documentation | EUR 100/day (minimum), up to EUR 1,000,000 | unverified: inherited figure or assumption; professional/source qualification required |
| Non-submission of transaction matrix | EUR 5,000 minimum surcharge | unverified: inherited figure or assumption; professional/source qualification required |
| Late/missing CbCR | Up to EUR 10,000 | unverified: inherited figure or assumption; professional/source qualification required |
| Late/missing CbCR notification | Up to EUR 10,000 | unverified: inherited figure or assumption; professional/source qualification required |
| Adverse estimation | Tax authorities may estimate income to taxpayer's disadvantage | Retained context; see scope and source limits |
| Burden of proof | Shifts to taxpayer where documentation is inadequate | Retained context; see scope and source limits |

## Completion checklist

### Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction | Source or qualification |
| --- | --- | --- |
| germany-bookkeeping | TP documentation builds on general bookkeeping records; related-party disclosures | Retained context; see scope and source limits |
| de-corporate-income-tax | Ordinary resident GmbH/UG corporate income tax and trade-tax companion; its scope and operational holds apply | Retained context; see scope and source limits |
| germany-vat | TP adjustments may affect customs value and import VAT | Retained context; see scope and source limits |
| CbCR | Risk assessment tool used by BZSt to select audit targets | Retained context; see scope and source limits |
| Financial statements | HGB/IFRS related-party disclosures must be consistent with TP positions | Retained context; see scope and source limits |

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

Confirm the workflow base and output specification; retain all original refusal codes; trace each material input to evidence; establish the period and each source condition; recompute components; separate assumptions, unresolved items and nominal ceilings from actual entitlements; obtain professional review and all required filing/registration confirmations before acting.

## Sources

The table distinguishes previously evidenced complete or selected readings from inherited citations whose reading date is not established. No new source reading is claimed. A recorded reading does not establish every historical application, amendment, incorporated rule or actual-case condition.

| Source | URL | Read on |
| --- | --- | --- |
| ao_1977 __108.html: Complete unit; actual holidays/appointments not established; retained text including printed footnotes read in the prior qualification | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-11-01 |
| aoeg_1977 art_97__36.html: Complete unit; no automatic VZ 2026 extension; retained text including printed footnotes read in the prior qualification | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-11-01 |
| ao_1977 __149.html: Complete unit; actual notice/adviser/return facts not established; retained text including printed footnotes read in the prior qualification | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-11-01 |

Not yet confirmed: complete TP law/current application, master/local file and CbCR thresholds, entity versus group tests, audit-trigger and extraordinary-transaction rules, document language, penalties, APA fees/availability/timing, OECD or German safe harbours, actual comparables and method selection, notification/return forms, schema, fields, acknowledgments and operational acceptance. The selected corporate-return deadline sources do not qualify these separate TP claims.

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
