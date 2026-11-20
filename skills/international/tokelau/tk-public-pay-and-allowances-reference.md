---
name: tk-public-pay-and-allowances-reference
description: >
  Dated Tokelau public-sector payroll reference for the 2022 remuneration
  scale adjustment and the older General Fono age-pension guidelines.
jurisdiction: TK
category: international
tax_year: 2022
tax_year_notes: "Uses the 1–3 November 2022 General Fono decisions and their record of guidelines endorsed on 4 July 2019. Obtain later decisions and the applicable employment instrument."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Tokelau public pay and allowances

Load `workflow-base`. Identify the employer, employment contract, position, applicable pay scale and pay period. The 2016 compilation of the Public Service Rules 2004 identifies the Tokelau Administration as the national public-service employer. Rule 4 assigns decisions on public-service positions, pay and other payments to the General Fono and refers to the public-service manual and express contract terms. In November 2022 the Fono referred a draft replacement for village consultation and later endorsement. Verify enactment and the applicable manual for the pay period. [Public Service Rules 2004, rr 2–4](https://www.paclii.org/tk/legis/consol_act_2016/psr2004201/) · [General Fono decisions, 1–3 November 2022, item 5, pp 25–28](https://www.mfat.govt.nz/assets/OIA/OIA-2023/OIA-28717-Tokelau-Briefings-27-July-2023.pdf)

## Verify the scale before applying the 2022 adjustment

The General Fono agreed to a 10% increase in wage and salary levels within the remuneration framework, effective 1 October 2022. The decision excluded overall remuneration under contracts outside the scale and called for annual cost-of-living review. Confirm the authorised scale, classification and contract for the period. [General Fono decisions, item 9, pp 35–36](https://www.mfat.govt.nz/assets/OIA/OIA-2023/OIA-28717-Tokelau-Briefings-27-July-2023.pdf)

A fictional in-scale position has an applicable prior gross fortnightly rate of NZD 1,000. Assume the entire pay period falls after commencement and the scale was implemented as decided. The adjusted rate is NZD 1,100 before tax and other deductions.

```oa-check
name: Tokelau 2022 in-scale fortnightly gross pay
inputs:
  prior_rate: 1000
  increase_rate: 0.10
steps:
  - adjusted_rate: prior_rate * (1 + increase_rate)
expected:
  adjusted_rate: 1100
```

An outside-scale contract has a fictional gross fortnightly rate of NZD 1,250 and no independent variation for that period. The in-scale decision contributes zero to its pay adjustment. Document the actual contract and any separate variation.

```oa-check
name: Tokelau 2022 outside-scale contract
inputs:
  contract_rate: 1250
  applicable_scale_increase: 0
steps:
  - gross_rate: contract_rate * (1 + applicable_scale_increase)
expected:
  gross_rate: 1250
```

## Check the allowance authority separately

The November 2022 minutes reproduce guidelines endorsed on 4 July 2019. The older-age pension guidelines describe a nationally budgeted allowance, fortnightly payment through payroll and village monitoring. They give age 60 and Tokelau residence as conditions, describe restrictions for absence and for travellers in receipt of New Zealand or Australian superannuation, and describe the payments as tax exempt. The earnings option in the appendix means the payment authority needs to be checked where a person continues working. The November 2022 minutes note differences amongst villages and direct a policy review. Obtain the current approved policy, any later direction and the charging provision before determining eligibility, concurrent pay, exemption or a deduction. [General Fono decisions, item 6 appendix and item 8, pp 29–31 and 35](https://www.mfat.govt.nz/assets/OIA/OIA-2023/OIA-28717-Tokelau-Briefings-27-July-2023.pdf)

Record the payroll channel and budget funding of the allowance separately from any employee or employer contribution. The revenue statistics record no social security contributions in the relevant OECD category for the July 2024 to June 2025 reporting period. Confirm any compulsory or contractual contribution under its own instrument. [OECD revenue statistics, Table 4.35, national statistics office data](https://www.oecd.org/en/publications/revenue-statistics-in-asia-and-the-pacific-2026_065aa566-en/full-report/country-tables-tax-revenues-2000-2024_b895f288.html)

## Remaining coverage

Obtain the current salary schedules, final public-service rules and pension policy outcome, and verify the employer, deductions, tax reporting and actual remuneration and residency facts. Apply the historical adjustment only to the stipulated in-scale period. Practitioner review remains pending.

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
