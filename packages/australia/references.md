---
name: australia-references
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "Reference catalogue snapshot; not an annual tax computation"
tier: 2
last_updated: 2026-11-05
version: 1.4
description: >
  Use this catalogue to locate Australian tax and accounting reference projects:
  PolicyEngine Australia, Quick Tax Calc, AU Tax Legislation Corpus, Payday Super
  Checker and ATO Benchmark Compare. It records their stated purpose, licence
  qualifications and possible role in a verification workflow. Use it when
  selecting a reference implementation, legislation retrieval source or local
  comparison tool. The catalogue does not calculate tax, certify a project's
  current accuracy or grant permission to incorporate its material. Check the
  exact version, source-data rights, licence and proposed use independently
  before relying on or reusing a listed project.
---

# Australia — Related Open-Source and Source-Available Projects v1.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

OpenAccountants uses different licences for software and guides. [LICENSING.md](../../../LICENSING.md) maps software to AGPL-3.0-only and guides and their exports to the source-available OA Guide License. It preserves the original AGPL/GPL terms for guides containing or derived from third-party copyleft material. Earlier copies already distributed under AGPL retain those rights.

Before incorporating material, check its exact licence, the proposed use and the destination file's terms. Attribution alone does not establish compatibility or satisfy every licence obligation. The projects below are references; their listing is not a blanket permission to incorporate them. This describes repository policy, not a determination of ownership or infringement.

## Ask the client first

- Which project and exact version is being considered?
- What is the proposed use and destination?
- What licence and source-data rights apply?
- Which claims need independent verification?

## The method, step by step

### PolicyEngine Australia

- Repository: [PolicyEngine/policyengine-au](https://github.com/PolicyEngine/policyengine-au)
- License: AGPL-3.0
- Language: English
- Scope: Full Australian tax-benefit microsimulation model covering personal income tax, Medicare levy, HECS-HELP repayment thresholds, and superannuation rules.
- Why it matters: Comprehensive, actively maintained microsimulation with detailed modelling of Australian tax and transfer policy. Strong validation source for PIT brackets, offsets, and levy calculations.
- Integration approach:
  - Check the applicable AGPL terms and preserve third-party copyleft rights for any derivative material; the general OA Guide License mapping does not replace them.
  - Use as a validation reference for income tax brackets, Medicare levy surcharge thresholds, HECS-HELP repayment rates, and superannuation contribution caps.

### Quick Tax Calc

- Repository: [zorfling/quick-tax-calc](https://github.com/zorfling/quick-tax-calc)
- License: verify before reuse
- Language: English
- Scope: ATO individual tax rates calculator.
- Why it matters: Lightweight reference for Australian individual income tax rate schedules.
- Integration approach:
  - Reference for tax bracket calculations and rate verification against ATO published tables.
  - Treat as reference-only until the licence is confirmed.

### AU Tax Legislation Corpus

- Repository: [ryanduguid/au-tax-legislation-corpus](https://github.com/ryanduguid/au-tax-legislation-corpus)
- License: Functional Source License 1.1, ALv2 Future License (FSL-1.1-ALv2); excludes a Competing Use
- Language: English
- Scope: Builds a provenance-rich corpus of in-force Commonwealth tax legislation (ITAA 1936/1997, GST Act, TAA 1953, FBTAA and related Acts) from the Federal Register of Legislation, with exact compilation identifiers attached to every extract.
- Why it matters: Guides in this pack cite sections of the ITAA 1997/1936 and TAA 1953. This corpus lets a retrieval system verify each citation against the in-force compilation text rather than trusting secondary summaries.
- Integration approach:
  - Check the FSL-1.1-ALv2 terms, including the Competing Use exclusion, for the relevant software and any separate rights in source data or reproduced content before reuse.
  - Use as the primary-source verification layer when reviewing or updating any Australian guide's legislative citations.
- Disclosure: maintained by an OpenAccountants contributor (ryanduguid).

### Payday Super Checker

- Repository: [ryanduguid/australian-accounting: payday-super-checker](https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker)
- License: Functional Source License 1.1, ALv2 Future License (FSL-1.1-ALv2); excludes a Competing Use
- Language: English
- Scope: Checks Australian super contributions against the payday-super deadlines (7 business days from payday, from 1 July 2026) and estimates SG charge exposure on late contributions.
- Why it matters: Direct validation companion to `au-super-guarantee`. The payday-super regime change is the highest-stakes AU payroll change of 2026, and deadline arithmetic (business days, fund-receipt basis) is easy to get wrong.
- Integration approach:
  - Check the FSL-1.1-ALv2 terms, including the Competing Use exclusion, for the relevant software and any separate rights in source data or reproduced content before reuse.
  - Use to sanity-check worked examples in `au-super-guarantee` and `australia-payroll`.
- Disclosure: maintained by an OpenAccountants contributor (ryanduguid).

### ATO Benchmark Compare

- Repository: [ryanduguid/australian-accounting: ato-benchmark-compare](https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare)
- License: Functional Source License 1.1, ALv2 Future License (FSL-1.1-ALv2); excludes a Competing Use
- Language: English
- Scope: Compares profit and loss figures against the ATO small business benchmarks locally, with the working shown.
- Why it matters: The ATO uses industry benchmarks to select small businesses for review; comparing a sole trader's expense ratios before lodgment is a practical risk screen that complements `au-sole-trader-schedule`.
- Integration approach:
  - Check the FSL-1.1-ALv2 terms, including the Competing Use exclusion, for the relevant software and any separate rights in source data or reproduced content before reuse.
  - Reference for adding a benchmark-screen step to sole trader workflows.
- Disclosure: maintained by an OpenAccountants contributor (ryanduguid).

## Worked cases

No tax computation is performed by this project catalogue. Validate a proposed use against the selected project, its exact version, licence and primary-source evidence.

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.

## Sources

| Source | URL | Read on |
|---|---|---|
| Retained citation | <https://github.com/PolicyEngine/policyengine-au> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://github.com/zorfling/quick-tax-calc> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://github.com/ryanduguid/au-tax-legislation-corpus> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare> | Not re-read for this format update; see retained provenance |

Not yet confirmed: A complete page-level source/read-date audit and independent legal review have not been performed for this structural update. Existing dates and qualifications retain their original scope. This is a project reference catalogue, not a tax calculation. Project currency, licences and suitability require their own checks.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
