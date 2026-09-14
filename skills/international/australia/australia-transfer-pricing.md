---
name: australia-transfer-pricing
description: Use this skill whenever asked about Australia transfer pricing rules, documentation requirements, or ATO transfer pricing compliance. Trigger on phrases like "transfer pricing Australia", "Australian TP documentation", "ATO transfer pricing", "master file Australia", "local file Australia", "CbCR Australia", "APA Australia", "Subdivision 815", "International Dealings Schedule", "IDS", "significant global entity", or any question about intercompany pricing for Australian entities.
version: 1.0
jurisdiction: AU
tax_year: 2025
last_updated: 2026-09-14
review_status: pending_review
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Transfer Pricing

## Australia Transfer Pricing Skill v1.0

Australia Transfer Pricing Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax authority | Australian Taxation Office (ATO) |
| Key TP legislation | Subdivision 815-B, Income Tax Assessment Act 1997 (ITAA 1997) |
| Documentation | Subdivision 284-E, Schedule 1, *Taxation Administration Act 1953* (TAA 1953), for special penalty documentation. Subdivision 815-D ITAA 1997 applies the TP rules to trusts and partnerships |
| CbCR legislation | Subdivision 815-E ITAA 1997 |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Currency | AUD |
| Documentation language | English |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 General Documentation (All Taxpayers)

**General Documentation (All Taxpayers)**

| Item | Detail |
| --- | --- |
| General records | Keep records required by the general tax record-keeping rules. These duties remain separate from the special TP penalty-documentation rules |
| Special TP documentation | Subdivision 284-E does not itself mandate preparing or keeping this documentation. Meeting it is necessary to rely on a reasonably arguable position (RAP) for the relevant penalty treatment |
| Timing and content for that treatment | Prepare before lodging the relevant return, in English or readily accessible and convertible into English. Explain the application or non-application of Subdivision 815-B or 815-C and consistency with the relevant guidance |
| Penalty relevance | Without compliant records, RAP is unavailable for that treatment. Having records does not itself prove RAP |

The special documentation treatment does not remove general record-keeping or mandatory CBC filing obligations. See [PS LA 2014/2 paragraphs 8AM to 8AT](https://www.ato.gov.au/law/view/document?docid=%22PSR%2FPS20142%2FNAT%2FATO%2F00001%22).

### 2.2 Three-tier documentation: CBC reporting entities

For periods starting on or after 1 July 2019, test CBC reporting entity status separately from significant global entity (SGE) status. A CBC reporting entity is a CBC reporting parent or a member of its accounting-consolidated or notional listed company group. The parent's annual global income must be at least AUD 1 billion. Individuals cannot be CBC reporting parents or entities.

CBC reporting entities form a subset of SGEs. Investment-entity consolidation exceptions can apply differently, so the SGE test alone is insufficient. CBC reporting for an income year is triggered by status in the previous income year. Establish the relevant period, applicable exemptions and which documents must be lodged before assigning the following duties. See [ATO CBC reporting entity rules](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/public-business-and-international/country-by-country-reporting-entities).

**Three-tier documents, where required**

| Document | Detail |
| --- | --- |
| Master File | OECD Annex I format; filed electronically |
| Local File | Australian-specific format (Short Form available for smaller dealings) |
| CbC Report | OECD Annex III format |
| Filing deadline | Within 12 months of end of income year |
| Filing method | Electronic lodgment with ATO |

### 2.3 International Dealings Schedule (IDS)

**International Dealings Schedule (IDS)**

| Item | Detail |
| --- | --- |
| Required? | Yes, for all taxpayers with material international related-party dealings |
| Filing | Annually with the corporate tax return |
| Content | Summary of related-party transactions, methods used, documentation status |

### 2.4 Short Form Local File

- **Short Form Local File availability**: First establish CBC reporting obligations under section 2.2. Then use the relevant year's local-file instructions to determine whether the short form alone is sufficient or full local-file information is required. Group income or SGE status alone does not determine this.

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length standard definition** — Subdivision 815-B: Where conditions between entities in international dealings differ from arm's length conditions, and an entity gets a "transfer pricing benefit," the taxable income is adjusted to reflect arm's length conditions.  _(Subdivision 815-B ITAA 1997)_

### 3.2 Accepted Methods

**Accepted Methods**

| Method | Accepted |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes |
| Resale Price Method (RPM) | Yes |
| Cost Plus Method (CPM) | Yes |
| Transactional Net Margin Method (TNMM) | Yes |
| Profit Split Method (PSM) | Yes |
| Other reliable methods | Yes (method flexibility) |

### 3.3 Preferred Method

- **Preferred method approach** — No statutory hierarchy. ATO follows OECD "most appropriate method" approach. CUP preferred where reliable comparables exist.  _(unsure)_

### 3.4 Self-Assessment

- **Self-assessment system** — Australia operates a self-assessment system -- taxpayers must determine and apply arm's length conditions without prior ATO approval.  _(unsure)_

### 3.5 Unresolved country requirements

The foundation workflow requires the following country-specific fields. They remain unresolved in this guide:

| Required field | Missing information |
| --- | --- |
| Benchmarking requirements | Australian versus regional comparables, acceptable databases and refresh frequency for the relevant transaction and period |
| Currency and exchange rates | The AUD output label does not establish whether to use spot, average or year-end rates, or the official rate source for each calculation |

Obtain the applicable Australian source and document the selected approach before benchmarking or converting amounts. Record these gaps in the reviewer brief and leave the affected analysis pending. Do not invent comparables, default the exchange-rate basis or mark the documentation complete or ready for filing while either required field is unresolved. The foundation's data, method and ten completion checks remain mandatory.

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| International Dealings Schedule (IDS) | Filed with income tax return |
| Master File (where required under CBC rules) | Electronic lodgement within 12 months of year-end, subject to applicable exemptions or extensions |
| Local File (where required under CBC rules) | Electronic lodgement within 12 months of year-end, subject to applicable exemptions or extensions |
| CbC Report (where required under CBC rules) | Electronic lodgement within 12 months of year-end, subject to applicable exemptions or extensions |
| Reportable Tax Position (RTP) | Large taxpayers must disclose TP positions |
| Income tax return | Annual self-assessment |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| Special TP documentation for RAP treatment | Before lodging the relevant income tax return; see section 2.1. This is not a universal mandatory filing deadline |
| IDS filing | With income tax return (varies by entity type; generally 15 January for large) |
| Master/Local/CbC Report | Where required under section 2.2, 12 months after end of income year, subject to applicable exemptions or extensions |
| Income tax return (companies) | Generally due by 15 January following year (for 30 June year-end) with extensions |

## Section 6 -- Penalties

### 6.1 Transfer Pricing Shortfall Penalties

**Transfer Pricing Shortfall Penalties**

| Scenario | Penalty Rate |
| --- | --- |
| RAP, no sole or dominant tax purpose | Base penalty: 10% of transfer-pricing shortfall |
| RAP, sole or dominant tax purpose | Base penalty: 25% |
| No RAP, no sole or dominant tax purpose | Base penalty: 25% |
| No RAP, sole or dominant tax purpose | Base penalty: 50% |
| Adjustment for specified conduct or previous penalty | Increase base penalty by 20% under s 284-220 where a condition applies; the increase is not cumulative |
| Voluntary disclosure | Apply any reduction under s 284-225 according to timing and conditions |
| SGE increase | Double the adjusted penalty where the entity is an SGE **and has no RAP**, for relevant years starting on or after 1 July 2015 |
| Remission | A separate decision can leave the penalty unchanged or remit it partly or fully. RAP alone does not guarantee nil |

These rates apply where the scheme shortfall exceeds the reasonably arguable threshold and the other penalty conditions are met. The threshold is the greater of $20,000 and 2% of net income for a trust or partnership; for other entities, the greater of $10,000 and 1% of income tax payable. A shortfall at or below the threshold does not attract this TP penalty.

For a $100,000 shortfall above the threshold, RAP gives a **$10,000** base penalty without a sole or dominant tax purpose, or **$25,000** with that purpose. Apply adjustments and remission separately. The ATO's likely nil-remission example requires a reasonable good-faith compliance attempt, best efforts to document the treatment and no tax avoidance purpose. See [PS LA 2014/2 paragraphs 5C to 5E, 8E to 8I and 10A to 12M](https://www.ato.gov.au/law/view/document?docid=%22PSR%2FPS20142%2FNAT%2FATO%2F00001%22).

### 6.2 Documentation Impact

- **Documentation impact on RAP**: Without records meeting Subdivision 284-E, an entity cannot rely on RAP for the relevant transfer-pricing penalty treatment. Compliant records permit consideration of RAP; they do not establish it. See section 2.1.

### 6.3 Failure to Lodge (SGEs)

**Failure to Lodge (SGEs)**

| Offence | Penalty |
| --- | --- |
| Failure to lodge a required Local File, Master File, or CbC Report | Up to AUD 825,000 per failure |
| Shortfall interest charge | Applies on underpaid tax |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance pricing arrangements (APA)**: Procedure is set out in [PS LA 2015/4](https://www.ato.gov.au/law/view/document?DocID=PSR/PS20154/NAT/ATO/00001&PiT=99991231235958). TR 95/23 was withdrawn on 10 March 2011. PCG 2019/1 addresses inbound-distributor compliance risk and refers to PS LA 2015/4 for APA procedures; it is not the general APA procedure. See the [withdrawal notice](https://www.ato.gov.au/law/view/document?LocID=%22TXR%2FTR9523%2FNAT%2FATO%22&PiT=20201210000001) and [PCG 2019/1 paragraph 58](https://www.ato.gov.au/law/view/view.htm?docid=%22cog/pcg20191/nat/ato/00001%22).

| Item | Detail |
| --- | --- |
| Availability | Yes (well-established program) |
| Types | Unilateral, Bilateral, Multilateral |
| Governing guidance | PS LA 2015/4; see the [ATO APA program](https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/in-detail/pricing/advance-pricing-arrangements/advance-pricing-arrangement-apa-program) |
| Application | To ATO; Expression of Interest followed by formal application |
| Duration | Typically 3-5 years prospective; rollback possible |
| Fees | No formal fee |
| Processing time | 12-24 months (bilateral may be longer) |
| Annual compliance report | Required |
| Critical assumptions | APA subject to critical assumptions; non-compliance may revoke |

## Section 8 -- Safe Harbours

**Safe Harbours**

| Area | Detail |
| --- | --- |
| Low-value intra-group services | Mark-up approach accepted (5% cost-plus per OECD simplified approach) |
| Low-level inbound/outbound loans | Interest-rate safe harbours available (PCG guidance) |
| Small taxpayers (turnover < AUD 50m) | Low-risk dealings may have simplified documentation |
| Distributors with limited related-party dealings | Materiality-based simplification |
| Management/technical services | Threshold-based simplification |

ATO publishes Practical Compliance Guidelines indicating risk zones for various transaction types.

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| 2024-2025 | Updated Local File instructions (Part A and Part B) |
| 2024 | Enhanced ATO compliance focus on intangibles and financial transactions |
| 10 December 2024 | Pillar Two primary legislation received royal assent. Detailed subordinate rules were registered on 23 December 2024. The IIR and domestic minimum tax apply to fiscal years starting from 1 January 2024; UTPR starts from 1 January 2025. Application dates are separate from enactment. See [ATO Pillar Two implementation](https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/in-detail/multinationals/global-and-domestic-minimum-tax) |
| 2022 | Multinational Tax Integrity Package -- increased penalties for SGEs |
| Ongoing | ATO PCGs on profit allocation to permanent establishments |
| Ongoing | OECD Amount B: Australia participating in design; implementation timeline TBC |
| Ongoing | Tax Avoidance Taskforce targeting multinationals |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| australia-bookkeeping | TP documentation relies on Australian accounting records |
| australia-corporate-tax | TP adjustments directly affect taxable income |
| australia-gst | TP adjustments may affect customs value and GST on imports |
| Thin capitalisation | Separate rules limit debt deductions; interact with TP for financial transactions |
| Diverted Profits Tax (DPT) | 40% rate for diverted profits; TP documentation relevant |
| CbCR | ATO uses CbCR for risk-based audit selection |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
