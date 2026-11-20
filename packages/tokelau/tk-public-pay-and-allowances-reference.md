---
name: tk-public-pay-and-allowances-reference
description: >
  Dated Tokelau public-sector payroll reference for the 2022 remuneration
  scale adjustment, earlier General Fono age-pension guidelines and employer
  funding for legacy public-service superannuation members.
jurisdiction: TK
category: international
tax_year: 2022
tax_year_notes: "Uses the 1–3 November 2022 General Fono decisions and their record of guidelines endorsed on 4 July 2019. Also cites dated GSF legislation and funding advice from 1 July 2026 for established members. Obtain later decisions and the applicable employment instrument."
tier: 2
last_updated: 2026-11-21
version: 0.2
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

Record the payroll channel and budget funding of the allowance separately from any employee or employer contribution. The cash-basis revenue statistics report zero receipts in the OECD social security contributions category for the July 2024 to June 2025 reporting period. Confirm any compulsory or contractual contribution under its own instrument. [OECD revenue statistics, Table 4.35, national statistics office data](https://www.oecd.org/en/publications/revenue-statistics-in-asia-and-the-pacific-2026_065aa566-en/full-report/country-tables-tax-revenues-2000-2024_b895f288.html)

## Check legacy Government Superannuation Fund membership

Section 50B allowed specified existing permanent officers in the Tokelau Public Service to elect into Part 2A of New Zealand’s Government Superannuation Fund (GSF), subject to conditions and a Tokelau cut-off of 21 October 1995. Section 2C provides for recognition of specified Tokelau employment by Order in Council, subject to its conditions. The 2001 employer order recognised the Tokelau Employment Commission as successor employer from 1 July 2001. Confirm the employee’s actual membership, applicable scheme and employer. The July 2016 General Fono decision to form a committee for a Tokelau superannuation scheme records a planning decision. Confirm any later scheme enactment and commencement separately. [Government Superannuation Fund Act 1956, ss 2C and 50B](https://www.legislation.govt.nz/act/public/1956/0047/latest/whole.html) · [Tokelau (Employer for Tokelau Public Service) Order 2001, cls 2–3](https://www.legislation.govt.nz/regulation/public/2001/0098/1.0/whole.html) · [General Fono decisions, July 2016, item 17](https://www.tokelau.org.nz/site/tokelau/files/2016Docs/GF%20Decision%20Signed%20072016.pdf)

The 2025 GSF valuation gives an employer contribution rate of 18.5% of contributor salary from 1 July 2026, excluding employer superannuation contribution tax (ESCT), for the specified funding employers of Part 2 or Part 2A contributors in the Tokelau, Cook Islands and Niue public services. The actuarial advice addresses salaries payable from money other than public money. Section 95(2) sets the funding mechanism and allows a ministerial direction for a lesser amount. Check the Authority’s rate and payment timing for the employer, the salary base and any ESCT before posting. Confirm any employee deduction separately and use the Authority’s directions for transfer timing under section 95A. [Government Superannuation Fund 2025 actuarial valuation, pp 24 and 30–31](https://www.gsfa.govt.nz/publications/actuarial-valuations/gsf-actuarial-valuation-report-2025.pdf) · [Government Superannuation Fund Act 1956, ss 95 and 95A](https://www.legislation.govt.nz/act/public/1956/0047/latest/whole.html)

For a fictional eligible member with NZD 5,000 in contributor salary and an employer whose applicable rate is confirmed at 18.5%, the employer amount is NZD 925 before ESCT. Determine employee deductions and any tax separately.

```oa-check
name: Tokelau legacy GSF employer amount before ESCT
inputs:
  contributor_salary: 5000
  employer_rate_excluding_esct: 0.185
steps:
  - employer_amount_excluding_esct: contributor_salary * employer_rate_excluding_esct
expected:
  employer_amount_excluding_esct: 925
```

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
