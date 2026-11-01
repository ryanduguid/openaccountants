---
name: nz-acc-levies
description: Use this skill whenever asked about New Zealand ACC levies for self-employed individuals. Trigger on phrases like "ACC levy", "earner levy", "work levy", "CoverPlus", "CoverPlus Extra", "accident compensation", "ACC invoice", "classification unit", or any question about ACC obligations for sole traders in New Zealand. Covers earner levy, work levy by classification unit (CU), CoverPlus/CoverPlus Extra, maximum liable earnings, and payment schedules. ALWAYS read this skill before touching any NZ ACC work.
version: 2.1
jurisdiction: NZ
tax_year: 2025
last_updated: 2026-11-01
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NZ Acc Levies

## Section 1 -- Quick reference

**Quick reference fields**

| Field | Value |
| --- | --- |
| Country | New Zealand |
| Jurisdiction Code | NZ |
| Primary Legislation | Accident Compensation Act 2001 (AC Act) |
| Supporting Legislation | Injury Prevention, Rehabilitation, and Compensation Act 2001 |
| Authority | Accident Compensation Corporation (ACC) |
| Filing Portal | myACC for Business (myacc.acc.co.nz) |
| Tax Year | 2025 (1 April 2025 -- 31 March 2026) |
| Currency | NZD only |
| Maximum Liable Earnings | $152,790 (2025/26); $156,641 (2026/27); $142,283 was the 2024/25 figure |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by NZ chartered accountant |
| Validation Date | Pending |
| Skill Version | 2.1 |
| Confidence Coverage | Tier 1: earner levy rate, work levy computation, maximum liable earnings. Tier 2: CU selection, CoverPlus Extra, experience rating. Tier 3: claims management, dispute resolution, complex multi-business structures. |

Read this whole section before computing anything.

**ACC levy components (2025/26)**

| Levy | Who Pays | Rate |
| --- | --- | --- |
| Earner levy | All earners (including self-employed) | $1.67 per $100 (1.67%), GST inclusive; $1.75 per $100 from 1 April 2026 |
| Work levy | Self-employed only | Varies by classification unit (CU) |
| Working Safer levy | Self-employed | ~$0.08 per $100 |

**Illustrative work levy rates by CU (2025/26)**

| CU Code | Industry | Work Levy (per $100) |
| --- | --- | --- |
| 72100 | Computer consultancy | ~$0.08 |
| 69200 | Accounting services | ~$0.08 |
| 62000 | Software development | ~$0.09 |
| 52100 | General retail | ~$0.47 |
| 41100 | Building construction | ~$2.68 |
| 01600 | Dairy farming | ~$2.41 |
| 11200 | Forestry | ~$8.30 |

These rates are illustrative. Actual rates must be verified at acc.co.nz or on the client's ACC invoice.

Sources: Inland Revenue, earners' levy rates (rates include GST; maximum earnings $152,790 and maximum levy $2,551.59 for 2025/26; $156,641 and $2,741.22 for 2026/27), https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates ; ACC, minimum and maximum liable income for self-employed people ($49,365 to $152,790 for 2025/26; $50,501 to $156,641 for 2026/27), https://www.acc.co.nz/for-business/received-an-invoice/calculate-your-levies . ACC invoices show levy rates before GST and add GST, so the GST-exclusive earners' levy on an ACC invoice is the IRD rate divided by 1.15.

**CoverPlus vs CoverPlus Extra**

| Feature | CoverPlus (Default) | CoverPlus Extra |
| --- | --- | --- |
| Compensation basis | 80% of liable earnings (prior year IR3) | Agreed level chosen by client |
| Levy basis | Actual earnings | Chosen cover amount |
| Adjustment | Adjusted when IR3 filed | Fixed at agreed level |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown CU code | Flag for reviewer -- CU determines work levy rate |
| Unknown CoverPlus option | CoverPlus (default) |
| Unknown GST status | GST-registered (ACC adds GST to every levy invoice; claim it only if registered) |
| Unknown liable earnings | Use most recent IR3 figure |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Required inputs before computing ACC levy** — Before computing any ACC levy figure, you MUST know: 1. Self-employment status -- sole trader, partner, or shareholder-employee 2. Classification unit (CU) code -- determines work levy rate 3. Liable earnings -- net self-employment income from IR3 or IR7 4. CoverPlus or CoverPlus Extra -- which cover option is in place 5. Whether any experience rating applies -- claims history adjustment 6. Tax year -- ACC invoices based on prior year's earnings
- **PAYE employee only** — If the client is a PAYE employee only, STOP. Employer pays ACC levies for employees.

### Refusal catalogue

- **R-NZ-ACC-1 -- Claims management** — Trigger: client asks about managing an ACC claim or rehabilitation. Message: "ACC claims management and rehabilitation are outside this skill's scope. Please contact ACC directly at 0800 101 996."
- **R-NZ-ACC-2 -- Dispute resolution** — Trigger: client disputes an ACC levy or classification. Message: "ACC levy disputes and CU reclassification require direct engagement with ACC. This skill cannot advise on dispute procedures. Please escalate to a qualified NZ chartered accountant."
- **R-NZ-ACC-3 -- Complex multi-business structures** — Trigger: client has multiple business entities with different CUs. Message: "Multi-entity ACC structuring requires case-specific analysis. Please escalate to a qualified NZ chartered accountant."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to ACC. Match by case-insensitive substring.

### 3.1 ACC levy payments

**ACC levy payments patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACC, ACCIDENT COMPENSATION | ACC LEVY PAYMENT | Annual or instalment levy payment |
| ACC LEVY, ACC INVOICE | ACC LEVY PAYMENT | Same |
| ACC COVERPLUS, COVERPLUS EXTRA | ACC LEVY PAYMENT | CoverPlus or CoverPlus Extra invoice payment |

### 3.2 ACC provisional invoicing

**ACC provisional invoicing patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACC PROVISIONAL, ACC ESTIMATE | PROVISIONAL LEVY | Based on most recent known earnings; adjusted once IR3 processed |
| ACC ADJUSTMENT, ACC REFUND | LEVY ADJUSTMENT | Difference between provisional and actual; may be refund or additional charge |

### 3.3 GST treatment

**GST treatment pattern**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACC + GST component visible | GST INPUT CLAIM | ACC levies are GST-exclusive; GST is on every CoverPlus invoice; GST component claimable if GST-registered |

### 3.4 IRD payments (income return triggers ACC)

**IRD payment patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRD, INLAND REVENUE NZ | TAX PAYMENT | IR3 filing triggers ACC levy calculation |
| IR3 FILED | ACC TRIGGER | Once IR3 processed, ACC issues or adjusts invoice |

## Section 4 -- Levy computation rules

### 4.1 Levy computation steps (Tier 1)

**Levy computation steps**  _(AC Act 2001, Schedule 1)_

| Step | Action |
| --- | --- |
| 4.1 | Determine liable earnings = net self-employment income from IR3; a full-time earner (over 30 hours a week on average) below the minimum liable income ($49,365 for 2025/26; $50,501 for 2026/27) is levied on the minimum |
| 4.2 | Cap earnings at maximum liable earnings ($152,790 for 2025/26; $156,641 for 2026/27) if applicable |
| 4.3 | Earner levy = liable earnings x $1.67 / $100 (2025/26, GST inclusive; $1.75 for 2026/27) |
| 4.4 | Work levy = liable earnings x work levy rate for CU / $100 |
| 4.5 | Working Safer levy = liable earnings x $0.08 / $100 |
| 4.6 | Total ACC levy = earner levy + work levy + Working Safer levy |
| 4.7 | GST: the earner levy rate in step 4.3 already includes GST; work and Working Safer levy rates are GST-exclusive; ACC adds GST whether or not the client is GST-registered; only a registered person can claim it |

### 4.2 CoverPlus (Default) (Tier 1)

- **CoverPlus compensation basis** — Compensation basis: 80% of liable earnings (based on prior year IR3). Levies adjusted when tax return is filed.

### 4.3 CoverPlus Extra (Tier 2)

- **CoverPlus Extra compensation basis** — Compensation basis: agreed level chosen by self-employed person. Levy basis: chosen cover amount (not actual earnings). Must sign CoverPlus Extra agreement with ACC. Flag for reviewer: can result in higher or lower cover than actual earnings. Advise client to review annually.

## Section 5 -- Payment and invoicing

### 5.1 Invoicing (Tier 1)

**Invoicing details**

| Detail | Value |
| --- | --- |
| Invoice timing | ACC sends invoice after IR3 is filed (typically September-November) |
| Payment options | Single payment, or instalments (2, 4, or monthly by arrangement) |
| Due date | As stated on ACC invoice (typically 30 days from issue) |
| Late payment | Penalties and interest apply |

### 5.2 Provisional invoicing (Tier 1)

- **Provisional invoicing process** — If the IR3 has not yet been filed, ACC issues a provisional invoice based on the most recent known earnings. Adjusted once actual return is processed. Client may receive refund or additional invoice.

## Section 6 -- GST and deductibility

### 6.1 GST treatment (Tier 1)

- **GST treatment on ACC levies** — ACC levies are GST-exclusive. ACC's CoverPlus invoice shows the GST included, whether or not the self-employed person is GST-registered. A GST-registered person can claim the GST component as input tax on the GST return. Source: ACC, Understand your CoverPlus invoice, https://www.acc.co.nz/for-business/received-an-invoice/explaining-your-invoice/coverplus-invoice.

### 6.2 Income tax deductibility (Tier 1)

- **Deductibility of ACC levies** — ACC levies paid are deductible business expenses for income tax purposes. The earner levy and work levy are both deductible against business income.

## Section 7 -- Edge case registry

### EC1 -- Multiple business activities (Tier 2)

Situation: Client runs a software consultancy (CU 72100) and a construction side business (CU 41100).
Resolution: ACC assigns the CU based on the primary activity (>50% of time or income). If roughly equal, ACC may split or assign higher-risk CU. Flag for reviewer.

### EC2 -- First year of self-employment (Tier 1)

Situation: Client started freelancing in March 2025. No prior-year IR3.
Resolution: ACC will estimate levies or use the minimum. Once first IR3 is filed, levies are recalculated and adjusted.

### EC3 -- Self-employed AND employee (Tier 1)

Situation: Client has PAYE employment and a freelance side business.
Resolution: Earner levy on total earnings (both sources combined, up to maximum). Work levy applies only to self-employment income. PAYE employer covers work levy for employment income.

### EC4 -- Earnings exceed maximum (Tier 1)

Situation: Consultant earns $200,000 net self-employment income.
Resolution: Levies calculated on $152,790 (2025/26 maximum), not $200,000. Weekly compensation if injured is also capped.

### EC5 -- Client disputes CU classification (Tier 2)

Situation: Client classified as "building construction" but primarily does office-based project management.
Resolution: Client can apply to ACC for CU reclassification. CU determines work levy rate and can significantly affect costs. Flag for reviewer.

### EC6 -- GST on ACC levies (Tier 1)

Situation: GST-registered sole trader receives ACC invoice.
Resolution: ACC levies are GST-exclusive. ACC adds GST to the invoice. GST component is claimable as input tax.

## Section 8 -- Reviewer escalation protocol

When a Tier 2 situation is identified:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified NZ chartered accountant must confirm before advising client.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified NZ chartered accountant. Document gap.
```

## Section 9 -- Test suite

### Test 1 -- Standard software consultant

Input: CU 72100, liable earnings $120,000, work levy rate $0.08/100.
Expected output (2025/26): Earner levy: $2,004.00 (GST inclusive). Work levy: $96.00 and Working Safer: $96.00 (excl. GST), plus GST $28.80. Invoice total: ~$2,224.80 incl. GST.

### Test 2 -- High earner hitting cap

Input: CU 69200, liable earnings $200,000, 2025/26 maximum $152,790.
Expected output: Capped at $152,790. Earner levy: $2,551.59 (GST inclusive). Work levy: $122.23 and Working Safer: $122.23 (excl. GST), plus GST $36.67. Invoice total: ~$2,832.72 incl. GST.

### Test 3 -- Builder (high-risk CU)

Input: CU 41100, liable earnings $80,000, work levy rate $2.68/100.
Expected output (2025/26): Earner levy: $1,336.00 (GST inclusive). Work levy: $2,144.00 and Working Safer: $64.00 (excl. GST), plus GST $331.20. Invoice total: ~$3,875.20 incl. GST.

### Test 4 -- Low-income first-year freelancer

Input: CU 72100, liable earnings $25,000, part-time (30 hours a week or less on average), 2025/26.
Expected output: Earner levy: $417.50 (GST inclusive). Work levy: $20.00 and Working Safer: $20.00 (excl. GST), plus GST $6.00. Invoice total: ~$463.50 incl. GST. If full-time, levies are calculated on the $49,365 minimum instead.

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER assume work levy rates are the same for all industries -- they vary significantly by classification unit
- NEVER calculate levies on earnings above the maximum liable earnings cap
- NEVER confuse CoverPlus (default, based on actual earnings) with CoverPlus Extra (agreed amount)
- NEVER omit the earner levy -- it applies to ALL earners, not just self-employed
- NEVER forget GST treatment -- ACC levies are GST-exclusive; ACC adds GST to every invoice; only registered persons claim it
- NEVER use a work levy rate without verifying it against the current ACC levy guidebook or invoice
- NEVER present calculations as definitive -- always label as estimated and direct client to ACC or a qualified NZ chartered accountant

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
