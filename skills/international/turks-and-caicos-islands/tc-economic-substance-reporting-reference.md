---
name: tc-economic-substance-reporting-reference
description: >
  Dated Turks and Caicos Islands economic substance reporting reference for domestic-entity classification, statutory returns and notices, accounting periods, evidence retention and selected administrative penalties.
jurisdiction: TC
category: international
tax_year: 2025
tax_year_notes: "Selected Cap 16.19 provisions and regulations with the changes commenced on 12 March 2025."
tier: 2
last_updated: 2026-11-21
version: 0.1
depends_on:
  - workflow-base
---

# Turks and Caicos Islands economic substance reporting reference

Load `workflow-base`. Identify the accounting period, entity type, business activities, tax residence evidence and the applicable version of the Companies and Limited Partnerships (Economic Substance) Ordinance. Ordinance 38 of 2024 commenced on 12 March 2025 and introduced a separate domestic-entity notice. This guide uses those changes and selected provisions of the earlier revised text. [Cap 16.19](https://www.tcifsc.tc/assets/documents/16.19-Companies-and-Limited-Partnerships-Economic-Substance-Ordinance-20241113124513.pdf) · [Ordinance 38 of 2024](https://www.tcifsc.tc/assets/documents/38-of-2024---Companies-and-Limited-Partnerships-Economic-SubstanceAmendment-Ordinance-2024-20251113100126.pdf) · [Commencement notice](https://publishing.gov.tc/agc/component/edocman/10-of-2025-commencement-notice-2025-companies-and-limited-partnerships-economic-substance-amendment-ordinance-2024/fdocument?Itemid=9999)

## Classify the filing branch

1. Check whether a TCI company or TCI limited partnership qualifies as a domestic entity under amended section 2. It must conduct business only in the Islands within the statutory definition and be outside an MNE group. For a company, individuals ordinarily resident in the Islands must beneficially own the majority of the shares or stock entitled to vote at a general meeting. For a limited partnership, partners ordinarily resident in the Islands must be entitled to the majority of the profits. Check exceptions to carrying on business in the Islands and the full MNE group definition before concluding. [Ordinance 38 of 2024, s 3](https://www.tcifsc.tc/assets/documents/38-of-2024---Companies-and-Limited-Partnerships-Economic-SubstanceAmendment-Ordinance-2024-20251113100126.pdf)
2. A domestic entity gives the Competent Authority a section 11A notice for each accounting period, including whether it carries on a relevant activity. Companies attach the certificate of incorporation and a copy of the register of members filed with the Financial Services Commission. Limited partnerships attach the partnership agreement and partner list. Check any other evidence required and the time, form and manner set by the Competent Authority. [Ordinance 38 of 2024, s 6](https://www.tcifsc.tc/assets/documents/38-of-2024---Companies-and-Limited-Partnerships-Economic-SubstanceAmendment-Ordinance-2024-20251113100126.pdf)
3. A TCI company, TCI limited partnership or registered foreign company falling within the amended definition of TCI entity files the section 10 return with the Competent Authority for each accounting period. The definition excludes a domestic entity. The return enables residence and, where relevant, substance assessment. A finding that the entity has no relevant activity does not remove the section 10 return requirement. For a claimed foreign tax residence, check section 3 and the evidence in regulation 5(4), including a tax authority certificate or equivalent or other evidence acceptable to the Competent Authority. [Cap 16.19 ss 3 and 10 and reg 5](https://www.tcifsc.tc/assets/documents/16.19-Companies-and-Limited-Partnerships-Economic-Substance-Ordinance-20241113124513.pdf) · [Ordinance 38 of 2024, ss 3–4](https://www.tcifsc.tc/assets/documents/38-of-2024---Companies-and-Limited-Partnerships-Economic-SubstanceAmendment-Ordinance-2024-20251113100126.pdf)

## Set the period and retain support

Regulation 2 gives a 1 January to 31 December ordinary reporting period or a different 12-month period approved on application. Check the first-period rules, the 30 June and 1 July cut-off and any approval. The selected regulation 5(5) gives the section 10 return a deadline no later than 3 months after the final day of the accounting period. Verify the operative deadline and any period-specific direction before relying on it. The section 11A domestic notice follows the time specified by the Competent Authority. [Cap 16.19 regs 2 and 5(5)](https://www.tcifsc.tc/assets/documents/16.19-Companies-and-Limited-Partnerships-Economic-Substance-Ordinance-20241113124513.pdf) · [Ordinance 38 of 2024, s 6](https://www.tcifsc.tc/assets/documents/38-of-2024---Companies-and-Limited-Partnerships-Economic-SubstanceAmendment-Ordinance-2024-20251113100126.pdf)

Section 10(3) requires the section 10 filer to retain documents relating to the required information for 6 years after the relevant period ends. Track any separate written notice under section 11. Under amended sections 10(4), 11(6) and new section 12A, a determination of specified non-filing or failure to provide requested information can lead to an administrative penalty of up to $20,000. Verify the actual notice, amount, applicable deadlines and review rights before giving advice. [Cap 16.19 ss 10–11](https://www.tcifsc.tc/assets/documents/16.19-Companies-and-Limited-Partnerships-Economic-Substance-Ordinance-20241113124513.pdf) · [Ordinance 38 of 2024, ss 4–7](https://www.tcifsc.tc/assets/documents/38-of-2024---Companies-and-Limited-Partnerships-Economic-SubstanceAmendment-Ordinance-2024-20251113100126.pdf)

## Fictional filing examples

These companies are already incorporated in the Islands and have 100 identical shares entitled to vote. For both examples, the company conducts business only in the Islands within the statutory definition and is outside an MNE group. Establish real beneficial ownership, residence and applicable law separately.

### Resident beneficial owners hold a majority

Suppose persons ordinarily resident in the Islands beneficially own 60 of the 100 voting shares. Their 60% share meets the amended majority condition. On the stated facts the company uses the section 11A domestic notice. Confirm the Competent Authority's time and evidence requirements before submission. [Ordinance 38 of 2024, ss 3 and 6](https://www.tcifsc.tc/assets/documents/38-of-2024---Companies-and-Limited-Partnerships-Economic-SubstanceAmendment-Ordinance-2024-20251113100126.pdf)

```oa-check
name: Majority of voting shares held by resident beneficial owners
inputs:
  resident_voting_shares: 60
  all_voting_shares: 100
steps:
  - resident_share_percent: resident_voting_shares / all_voting_shares * 100
  - percentage_points_above_half: resident_share_percent - 50
expected:
  resident_share_percent: 60
  percentage_points_above_half: 10
```

### Exactly half the voting shares and a calendar year period

Suppose the same class has 50 voting shares beneficially held by persons ordinarily resident in the Islands and 50 held by other persons. Exactly half falls short of a majority, so the company follows section 10 on these facts. For an ordinary period ending 31 December 2025, assume the selected regulation applies without a different approved period, extension or calendar adjustment. The 3-month deadline is 31 March 2026. The 6-year section 10 record period runs to 31 December 2031. [Cap 16.19 s 10 and regs 2 and 5(5)](https://www.tcifsc.tc/assets/documents/16.19-Companies-and-Limited-Partnerships-Economic-Substance-Ordinance-20241113124513.pdf) · [Ordinance 38 of 2024, s 3](https://www.tcifsc.tc/assets/documents/38-of-2024---Companies-and-Limited-Partnerships-Economic-SubstanceAmendment-Ordinance-2024-20251113100126.pdf)

```oa-check
name: Exact half ownership and record retention year
inputs:
  resident_voting_shares: 50
  all_voting_shares: 100
  period_end_year: 2025
  retention_years: 6
steps:
  - resident_share_percent: resident_voting_shares / all_voting_shares * 100
  - retention_end_year: period_end_year + retention_years
expected:
  resident_share_percent: 50
  retention_end_year: 2031
```

## Remaining coverage

Determine first-period or transition treatment for the actual entity. Establish the current notice and return channels, accepted evidence, extensions and receipts. Apply the relevant-activity and substance tests separately, including investment-fund exclusions, foreign residence, pure equity holding entities, high-risk intellectual property and outsourcing. Confirm current penalties and appeal procedure. Keep actual identifiers and documents in authorised client systems.

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
