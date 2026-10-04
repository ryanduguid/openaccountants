---
name: jordan-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Jordan General Sales Tax (GST) return for any client. Trigger on phrases like "Jordan GST", "Jordan VAT", "ISTD return", or any request involving Jordanian indirect tax. Jordan imposes GST at 16% under Law No. 6 of 1994, administered by ISTD. Multiple special rates exist (4%, 5%, 8%, 10%). ALWAYS read this skill before handling any Jordan GST work.
version: 2.1
jurisdiction: JO
category: international
tax_year: 2025
last_updated: 2026-10-04
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Jordan GST

## Section 1 -- Quick reference

**Quick reference field/value table**

| Field | Value |
| --- | --- |
| Country | Jordan (Hashemite Kingdom) |
| Standard rate | 16% |
| Special rates | 4% (telecoms), 5% (certain services), 8% (certain goods), 10% (certain goods/services) |
| Zero rate | 0% (exports, specified basic foodstuffs) |
| Exempt supplies | Financial services, medical, education, residential rental, unprocessed agricultural |
| Filing portal | https://www.istd.gov.jo |
| Authority | Income and Sales Tax Department (ISTD) |
| Currency | JOD (Jordanian Dinar) |
| Filing frequency | Monthly (turnover > JOD 1M); Bi-monthly (others) |
| Deadline | End of month following period |
| Mandatory registration | JOD 75,000 (goods), JOD 30,000 (services) |
| Primary legislation | General Sales Tax Law No. 6 of 1994 (as amended) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 16% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Jordan |

### Required inputs

- **Minimum viable input** — Bank statement for the period. Acceptable from Arab Bank, Housing Bank, Jordan Ahli Bank, Cairo Amman, Bank al Etihad, or any other Jordanian bank.  _(Section 2 -- Required inputs and refusal catalogue)_
- **Recommended input** — Sales invoices (Arabic required), purchase invoices for input claims.  _(Section 2 -- Required inputs and refusal catalogue)_

### Refusal catalogue

- **R-JO-1 -- Free zone complex** — Trigger: Aqaba Special Economic Zone operations. Message: "ASEZA has specific GST rules. Escalate to licensed practitioner."  _(Section 2 -- Required inputs and refusal catalogue)_
- **R-JO-2 -- Special Sales Tax** — Trigger: alcohol, tobacco, fuel subject to SST. Message: "SST is separate from GST and computed first. Escalate for combined computation."  _(General Sales Tax Law No. 6 of 1994 as amended to 2009 (ISTD English translation), art. 6 and Schedule 1 — https://istd.gov.jo/ebv4.0/root_storage/en/eb_list_page/gst_law.pdf)_

### 3.1 Jordanian banks (exempt -- exclude)

**Jordanian banks (exempt -- exclude)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ARAB BANK | EXCLUDE | Financial service, exempt |
| HOUSING BANK, ISKAN BANK | EXCLUDE | Same |
| JORDAN AHLI, CAIRO AMMAN | EXCLUDE | Same |
| BANK AL ETIHAD, CAPITAL BANK | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

**Government supplier patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ISTD, INCOME AND SALES TAX | EXCLUDE | Tax payment |
| CUSTOMS, JORDAN CUSTOMS | Check for import GST | Duty exclude; GST recoverable |
| SSC, SOCIAL SECURITY CORPORATION | EXCLUDE | Social contribution |

### 3.3 Utilities

**Utility supplier patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| JEPCO, EDCO, IDECO | Domestic 16% | Electricity |
| MIYAHUNA, WAJ | Domestic 16% | Water |
| ZAIN JORDAN, ORANGE JORDAN, UMNIAH | Domestic 4% | Telecoms at special rate |

### 3.4 SaaS

**SaaS supplier patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE | Reverse charge 16% | Non-resident service |
| AWS, ZOOM, SLACK | Reverse charge 16% | Non-resident |

### Example 1 -- Reverse charge on US SaaS

**Input:** `05.01.2026 ; SALESFORCE INC ; DEBIT ; Monthly CRM ; USD 200 ; JOD 142`

US entity. No GST. Reverse charge at 16%. Output and input both reported. Net zero.

### Example 2 -- Telecoms at 4%

**Input:** `10.01.2026 ; ZAIN JORDAN ; DEBIT ; Mobile plan ; -50.00 ; JOD`

Telecoms services at special 4% rate, not 16%.

### 5.1 Standard rate 16%

- **Standard rate default** — 16% general tax on the supply or importation of goods and services (art. 6) unless the supply is zero-rated, exempt or specifically listed at another rate.  _(General Sales Tax Law No. 6 of 1994 as amended to 2009 (ISTD English translation), art. 6 — https://istd.gov.jo/ebv4.0/root_storage/en/eb_list_page/gst_law.pdf)_

### 5.2 Special rates

- **Special rates description** — 4% telecoms (domestic), 5% certain services, 8% certain goods, 10% certain goods/services. Rate determined by ISTD schedules.  _(Section 5 -- Classification rules)_

### 5.3 Zero-rated (0%, input recoverable)

- **Zero-rated supplies** — Goods listed in Schedule 2; goods and services supplied to free zones, free cities and duty free shops or exported outside the Kingdom; supplies to bodies relieved from tax under art. 21 (art. 7). The guide's foodstuff list follows the Schedule 2 and Cabinet decisions in force.  _(General Sales Tax Law No. 6 of 1994 as amended to 2009 (ISTD English translation), art. 7 — https://istd.gov.jo/ebv4.0/root_storage/en/eb_list_page/gst_law.pdf)_

### 5.4 Exempt (no GST, no recovery)

- **Exempt supplies** — Goods and services listed in Schedule 3 are exempt (art. 7(b)): financial services, medical, education, residential rental (unfurnished), unprocessed agricultural produce and the other Schedule 3 items; no output tax and no input credit on attributable costs.  _(General Sales Tax Law No. 6 of 1994 as amended to 2009 (ISTD English translation), art. 7(b) and Schedule 3 — https://istd.gov.jo/ebv4.0/root_storage/en/eb_list_page/gst_law.pdf)_

### Output section

**GST return output section**

| Section | Description |
| --- | --- |
| Output GST at 16% | Standard-rated supplies |
| Output GST at special rates | 4%, 5%, 8%, 10% separately |
| Zero-rated | Exports and zero-rated supplies |
| Exempt | Exempt supplies |

### Input section

**GST return input section**

| Section | Description |
| --- | --- |
| Input GST on domestic purchases | Recoverable if taxable |
| Input GST on imports | Customs GST |
| Input GST adjustments | Blocked, apportionment |

### Net

- **Net GST calculation** — Output GST minus allowable input GST. Credit brought forward from prior period.  _(Section 6 -- GST return form structure)_

## Section 7 -- Reverse charge and imports

- **Reverse charge on non-resident services** — Services performed in the Kingdom by non-residents or by foreign firms without a Jordanian branch are treated as imported services: tax becomes due when payment is made and the recipient is liable to pay it (art. 9(e)). Self-assess at 16% and claim input tax where the service is for taxable supplies.  _(General Sales Tax Law No. 6 of 1994 as amended to 2009 (ISTD English translation), art. 9(e) — https://istd.gov.jo/ebv4.0/root_storage/en/eb_list_page/gst_law.pdf)_
- **Import of goods GST treatment** — Import of goods: GST on CIF plus customs duties. Collected by Jordan Customs. Recoverable if for taxable supplies.  _(GST Law No. 6/1994, reverse charge provisions)_

## Section 8 -- Deductibility and blocked input

- **Blocked input items** — Blocked: - Entertainment and hospitality - Motor vehicles for personal use - Non-business goods/services - Purchases related to exempt supplies - Gifts/donations (above limits)
- **Partial exemption** — Partial exemption: turnover-based apportionment. ISTD approval required.

## Section 9 -- Filing, deadlines, and penalties

**Filing categories and deadlines**

| Category | Period | Deadline |
| --- | --- | --- |
| Large taxpayers (> JOD 1M) | Monthly | End of following month |
| Others | Bi-monthly | End of month following bi-monthly period |

- **Bi-monthly periods and deadlines** — The general tax period is two months (one month for the special tax), with the start and end of periods set by the Director (art. 16). Returns and payment fall due by the end of the month after each period: Jan-Feb (31 Mar), Mar-Apr (31 May), May-Jun (31 Jul), Jul-Aug (30 Sep), Sep-Oct (30 Nov), Nov-Dec (31 Jan).  _(General Sales Tax Law No. 6 of 1994 as amended to 2009 (ISTD English translation), art. 16 — https://istd.gov.jo/ebv4.0/root_storage/en/eb_list_page/gst_law.pdf)_

**Violations and penalties**

| Violation | Penalty |
| --- | --- |
| Late filing | JOD 100-500 per return |
| Late payment | 4% first week; 1% per week after |
| Tax evasion | Fines and imprisonment |

### Edge cases

**EC1 -- Foreign SaaS.** Reverse charge at 16%. Net zero.

**EC2 -- Export of goods.** Zero-rated. Input recoverable.

**EC3 -- Telecom at 4%.** Not 16%.

**EC4 -- Free zone to domestic.** GST applies when goods leave free zone.

**EC5 -- Credit note.** Reduces output GST in period issued.

**EC6 -- Exempt financial services.** No output GST. Input not recoverable.

**EC7 -- Import of goods.** GST on CIF + duty. Recoverable.

### Test suite

**Test 1 -- Standard sale.** JOD 1,000 net. Expected: output GST JOD 160 (16%).

**Test 2 -- Export.** JOD 5,000 goods. Expected: 0% GST. Input recoverable.

**Test 3 -- Reverse charge.** UK consulting JOD 1,420. Expected: output JOD 227.20, input JOD 227.20.

**Test 4 -- Telecoms.** JOD 50,000 services. Expected: GST JOD 2,000 (4%).

**Test 5 -- Exempt supply.** Bank financial services JOD 100,000. Expected: no output GST. Input JOD 3,200 not recoverable.

**Test 6 -- Import.** Electronics CIF JOD 10,000 + duty JOD 1,000. Expected: GST base JOD 11,000, GST JOD 1,760.

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

### Out of scope -- direct tax

- Corporate income tax: 20% standard; banks 35%; telecoms 24%; mining 30%
- Personal income tax: progressive 5%-30%
- Social security: employer 14.25%, employee 7.5%

### Prohibitions

- NEVER apply a rate other than 0%, 4%, 5%, 8%, 10%, 16%
- NEVER allow input recovery on exempt supplies
- NEVER ignore reverse charge on non-resident services
- NEVER treat imports as zero-rated
- NEVER issue invoices without Arabic text
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without confirming correct period (monthly vs bi-monthly)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
