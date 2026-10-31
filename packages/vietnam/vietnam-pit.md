---
name: vietnam-pit
description: Use this skill whenever asked about Vietnam personal income tax (thuế thu nhập cá nhân / TNCN) for resident individuals, self-employed persons, or sole proprietors. Trigger on phrases like "thuế TNCN", "Vietnam income tax", "thuế thu nhập cá nhân", "giảm trừ gia cảnh", "biểu thuế lũy tiến", "progressive tax Vietnam", "personal deduction Vietnam", "dependent deduction Vietnam", "PIT Vietnam", or any question about computing or filing personal income tax in Vietnam. Covers the 2026 five-bracket progressive rate schedule (Luật số 109/2025/QH15), personal and dependent deductions, and filing obligations. ALWAYS read this skill before touching any Vietnam PIT work.
version: 1.0
jurisdiction: VN
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Vietnam Pit

## Vietnam Personal Income Tax (Thuế Thu Nhập Cá Nhân / TNCN) v1.0

## Section 1 — Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Vietnam (Cộng hòa Xã hội chủ nghĩa Việt Nam) |
| Tax | Thuế Thu Nhập Cá Nhân (TNCN — Personal Income Tax / PIT) |
| Currency | VND (Vietnamese Dong / đồng) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Primary legislation | Luật số 109/2025/QH15, amended by Luật số 09/2026/QH16 (in force 01/07/2026; residents' employment and business income from the 2026 tax period, art. 29); Luật Thuế Thu Nhập Cá Nhân No. 04/2007/QH12 (amended) for earlier periods |
| Tax authority | Tổng cục Thuế (General Department of Taxation — GDT) |
| Filing portal | etax.gdt.gov.vn / thuedientu.gdt.gov.vn |
| Filing deadline | Annual finalisation: 31 March of following year |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Vietnam-licensed tax agent (đại lý thuế) or CPA |
| Skill version | 1.0 |

## Section 2 — Progressive Tax Brackets (Biểu Thuế Lũy Tiến Từng Phần) — 2026

From the 2026 tax period, Vietnam moved from a 7-bracket to a **5-bracket** progressive tax system for residents' employment income under Luật số 109/2025/QH15, arts 8, 9 and 29. Business income does not use these brackets (Section 5).

### Monthly rates (applied to taxable income per month)

**Monthly rates table**  _(Tax period 2026 onwards. Luật số 109/2025/QH15, art. 9.2: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat109-2025.pdf)_

| Bracket | Monthly Taxable Income (VND) | Rate |
| --- | --- | --- |
| 1 | ≤ 10,000,000 | 5% |
| 2 | 10,000,001 – 30,000,000 | 10% |
| 3 | 30,000,001 – 60,000,000 | 20% |
| 4 | 60,000,001 – 100,000,000 | 30% |
| 5 | > 100,000,000 | 35% |

### Annual rates (applied to taxable income per year)

**Annual rates table**  _(Tax period 2026 onwards. Luật số 109/2025/QH15, art. 9.2: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat109-2025.pdf)_

| Bracket | Annual Taxable Income (VND) | Rate |
| --- | --- | --- |
| 1 | ≤ 120,000,000 | 5% |
| 2 | 120,000,001 – 360,000,000 | 10% |
| 3 | 360,000,001 – 720,000,000 | 20% |
| 4 | 720,000,001 – 1,200,000,000 | 30% |
| 5 | > 1,200,000,000 | 35% |

### Quick tax computation table (monthly)

**Quick tax computation table**  _(Tax period 2026 onwards; derived from Luật số 109/2025/QH15, art. 9.2)_

| If taxable income/month (VND) | Tax = |
| --- | --- |
| ≤ 10,000,000 | Income × 5% |
| 10,000,001 – 30,000,000 | 500,000 + (Income − 10,000,000) × 10% |
| 30,000,001 – 60,000,000 | 2,500,000 + (Income − 30,000,000) × 20% |
| 60,000,001 – 100,000,000 | 8,500,000 + (Income − 60,000,000) × 30% |
| > 100,000,000 | 20,500,000 + (Income − 100,000,000) × 35% |

## Section 3 — Deductions (Giảm Trừ Gia Cảnh) — 2026

### Personal and dependent deductions

**Personal and dependent deductions table**  _(Luật số 109/2025/QH15; googlesky/thue-2026 (MIT))_

| Deduction | Monthly (VND) | Annual (VND) | Notes |
| --- | --- | --- | --- |
| Personal deduction (giảm trừ bản thân) | 15,500,000 | 186,000,000 | Per taxpayer; automatic |
| Dependent deduction (giảm trừ người phụ thuộc) | 6,200,000 per dependent | 74,400,000 per dependent | Must register dependents with tax authority |

- **Previous values (pre-2026)** — Personal deduction was 11,000,000/month; dependent deduction was 4,400,000/month. The 2026 increase reflects Resolution 954/2020/UBTVQH14's CPI-triggered adjustment mechanism enacted via Luật số 109/2025/QH15.  _(Nghị quyết 954/2020/UBTVQH14; Luật số 109/2025/QH15)_

### Other deductions

**Other deductions table**

| Deduction | Amount | Notes |
| --- | --- | --- |
| Compulsory social insurance (BHXH) | 8% of salary | Employee's share — deducted before PIT |
| Compulsory health insurance (BHYT) | 1.5% of salary | Employee's share — deducted before PIT |
| Unemployment insurance (BHTN) | 1% of salary | Employee's share — deducted before PIT |
| Voluntary pension fund | Up to 1,000,000/month | If contributing to qualified fund |
| Charitable contributions | Actual amount | Donations to approved organisations only |

### Taxable income formula

- **Taxable Income formula** — Taxable Income = Gross Income − Compulsory insurance (BHXH + BHYT + BHTN) − Personal deduction (15,500,000/month) − Dependent deductions (6,200,000 × number of registered dependents/month) − Other allowable deductions

## Section 4 — Resident vs Non-Resident

**Resident vs Non-Resident table**

| Status | Definition | Tax treatment |
| --- | --- | --- |
| Tax resident | Present in Vietnam ≥ 183 days in a calendar year OR 12 consecutive months; OR has a regular abode in Vietnam | Worldwide income; progressive rates (Section 2) |
| Non-resident | Does not meet resident criteria | Vietnam-sourced income only; flat 20% on employment income |

## Section 5 — Income Categories (Các Khoản Thu Nhập Chịu Thuế)

**Income Categories table**

| Category | Rate | Notes |
| --- | --- | --- |
| Employment income (tiền lương, tiền công) | Progressive 5-bracket (Section 2) | Main category for salaried individuals |
| Business income (kinh doanh) | Exempt, % of revenue above the threshold, or 15%, 17% or 20% of income; never the 5-bracket schedule | Self-employed / sole proprietors; see below |
| Capital gains (chuyển nhượng vốn) | 20% on gains | Or 0.1% of transfer value for listed securities |
| Securities transfer | 0.1% of sale proceeds | Regardless of gain/loss |
| Real estate transfer (chuyển nhượng bất động sản) | 2% of transfer price | No deduction of cost basis |
| Royalties, franchises | 5% above VND 10,000,000 per contract |  |
| Lottery / prizes (trúng thưởng) | 10% above VND 10,000,000 |  |
| Inheritance / gifts | 10% above VND 10,000,000 |  |

### Business income of resident individuals and household businesses (tax period 2026 onwards)

Luật số 109/2025/QH15, art. 7 governs this income from the 2026 tax period (art. 29.2). The method depends on annual revenue:

**Business income methods table**  _(Tax period 2026. Luật số 109/2025/QH15, art. 7.2 and 7.3: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat109-2025.pdf; threshold in art. 7.1 as amended by Luật số 09/2026/QH16, art. 1: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/09-qh.signed.pdf; Nghị định 68/2026/NĐ-CP, arts 3 and 4: https://xdcs.cdnchinhphu.vn/446259493575335936/2026/3/6/68-2026-nd-cp-05032026-signed-17727673940151875228819.pdf, as amended by Nghị định 141/2026/NĐ-CP, art. 1.1, effective 01/01/2026: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/141-ndcp.signed.pdf)_

| Annual revenue (VND) | PIT |
| --- | --- |
| ≤ 1,000,000,000 | None. VAT is also not payable. Notify actual revenue to the tax authority by 31 January of the following year (Nghị định 68/2026/NĐ-CP, art. 8.1(a)) |
| > 1,000,000,000 to 3,000,000,000 | Taxpayer's choice: the rate below × (revenue − 1,000,000,000), or 15% × (revenue − related costs) |
| > 3,000,000,000 to 50,000,000,000 | 17% × (revenue − related costs) |
| > 50,000,000,000 | 20% × (revenue − related costs) |

**Rates on revenue above VND 1,000,000,000**  _(Tax period 2026. Luật số 109/2025/QH15, art. 7.3; activity lists in Nghị định 253/2026/NĐ-CP, art. 45.2 and Appendix: https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/16/469959-1784171413_v1_1784174315_signed.pdf)_

| Business activity | Rate |
| --- | --- |
| Distribution and supply of goods | 0.5% |
| Services; construction excluding materials | 2% |
| Asset leasing; insurance agency; lottery agency; multi-level sales agency | 5% |
| Manufacturing; transport; services tied to goods; food and beverage services; construction including materials | 1.5% |
| Digital content in entertainment, e-games, digital film, photos and music; digital advertising | 5% |
| Other business activities | 1% |

- **Real estate rental (other than accommodation)**: 5% × (rental revenue − 1,000,000,000), and the income method does not apply (Luật số 109/2025/QH15, arts 7.2 and 7.4; Nghị định 68/2026/NĐ-CP, art. 4.4 as amended).
- **Several trades or premises**: the VND 1,000,000,000 is deducted once a year across all of them, against the trade or premises the taxpayer chooses (Nghị định 68/2026/NĐ-CP, art. 4.3 as amended).
- **Keeping or changing method**: a taxpayer on the income method stays on it for 2 consecutive years. A taxpayer on the revenue method whose actual revenue exceeds VND 3,000,000,000 moves to the income method from the following year (Nghị định 68/2026/NĐ-CP, art. 4.5(d)).
- **Deadlines**: quarterly returns by the last day of the first month of the next quarter; monthly returns by the 20th of the next month; annual PIT finalisation by 31 March of the following year (Nghị định 68/2026/NĐ-CP, art. 8.3). These were not rechecked against Luật số 108/2025/QH15 and Nghị định 252/2026/NĐ-CP, which govern tax administration from 01/07/2026; confirm before filing.
- **VAT is separate**: above the threshold, VAT is charged on all revenue by the direct method, not only on the excess (Nghị định 68/2026/NĐ-CP, art. 3; VAT Law No. 48/2024/QH15, art. 12.2(c); see `vietnam-vat`).
- **Conflicting source**: a Government portal answer of July 2026 (https://baochinhphu.vn/sang-tao-noi-dung-so-doanh-thu-bao-nhieu-phai-nop-thue-102260716165956679.htm) quotes 2% for platform content revenue from 2026. Art. 7.3(đ) and Appendix item 4 of Nghị định 253/2026/NĐ-CP state 5% for digital content in the listed categories, which this guide follows. Unconfirmed: which content falls outside those categories. Thông tư 18/2026/TT-BTC was not read.
- **2025 and earlier**: a different regime applied, with a VND 100,000,000 threshold and tax on all revenue once it was exceeded (Thông tư 40/2021/TT-BTC, art. 4.2, as quoted in the same portal answer). This guide does not give the rates for those years.

## Section 6 — Filing and Payment

### Withholding (Khấu Trừ Tại Nguồn)

- **Employer withholding deadlines** — Employers withhold PIT monthly from employee salaries and remit to GDT by the 20th of the following month (monthly filers) or 30th of the month following the quarter (quarterly filers).

### Annual finalisation (Quyết Toán Thuế)

**Annual finalisation table**

| Who | Deadline | Notes |
| --- | --- | --- |
| Employers (on behalf of employees) | 31 March of following year | File form 05/QTT-TNCN |
| Individuals self-filing | 31 March of following year | File form 02/QTT-TNCN |
| Individuals with single employer, no additional income | May authorise employer to finalise | No separate filing needed |

### When individual must self-file

- Has income from 2+ sources and total additional tax > VND 100,000
- Receives income not subject to withholding
- Foreign-sourced income (residents only)
- Wishes to claim dependent deductions not registered with employer

## Section 7 — Worked Examples

All examples in this section use the 2026 tax period. Examples 1 to 3 use insurance caps from 1 July 2026 and Region I for the unemployment insurance cap.

### Example 1 — Single employee, no dependents

**Facts:** Monthly gross salary VND 40,000,000. No dependents.

**Computation:**
```
Gross salary:                       40,000,000
Less: BHXH (8%):                    -3,200,000
Less: BHYT (1.5%):                    -600,000
Less: BHTN (1%):                      -400,000
Less: Personal deduction:          -15,500,000
                                   -----------
Taxable income:                     20,300,000

Tax:
  First 10,000,000 × 5%  =            500,000
  Next 10,300,000 × 10%  =          1,030,000
                                   -----------
Total PIT/month:                     1,530,000
```

### Example 2 — Employee with 2 dependents

**Facts:** Monthly gross salary VND 60,000,000. Two registered dependents.

**Computation:**
```
Gross salary:                       60,000,000
Less: BHXH (8%, capped at 50,600,000): -4,048,000
Less: BHYT (1.5%, capped at 50,600,000): -759,000
Less: BHTN (1%, under the cap):       -600,000
Less: Personal deduction:          -15,500,000
Less: Dependent deductions (2×):   -12,400,000
                                   -----------
Taxable income:                     26,693,000

Tax:
  First 10,000,000 × 5%  =            500,000
  Next 16,693,000 × 10%  =          1,669,300
                                   -----------
Total PIT/month:                     2,169,300
```

**Insurance caps used, from 1 July 2026:** BHXH and BHYT on salary up to VND 50,600,000 (20 × VND 2,530,000; base salary in Nghị định 161/2026/NĐ-CP: https://xaydungchinhsach.chinhphu.vn/tu-01-7-chinh-phu-tang-luong-co-so-119260517100243881.htm); BHTN on salary up to VND 106,200,000 (20 × the Region I minimum wage of VND 5,310,000 in Nghị định 293/2025/NĐ-CP: https://xaydungchinhsach.chinhphu.vn/tu-1-1-2026-muc-luong-toi-thieu-duoc-tang-bao-nhieu-119251111091442629.htm). The multiples are in `vn-payroll-social`. Unconfirmed: that the social insurance reference level still equals the base salary after 1 July 2026.

### Example 3 — High income earner

**Facts:** Monthly gross salary VND 150,000,000. One dependent.

**Computation:**
```
Gross salary:                      150,000,000
Less: BHXH (8%, capped at 50,600,000): -4,048,000
Less: BHYT (1.5%, capped at 50,600,000): -759,000
Less: BHTN (1%, capped at 106,200,000): -1,062,000
Less: Personal deduction:          -15,500,000
Less: Dependent deduction (1×):     -6,200,000
                                   -----------
Taxable income:                    122,431,000

Tax:
  First 10,000,000 × 5%   =           500,000
  Next 20,000,000 × 10%   =         2,000,000
  Next 30,000,000 × 20%   =         6,000,000
  Next 40,000,000 × 30%   =        12,000,000
  Remaining 22,431,000 × 35% =      7,850,850
                                   -----------
Total PIT/month:                    28,350,850
```

### Example 4 — Sole trader, services, 2026

**Facts:** Consulting services. Annual revenue VND 2,000,000,000 and related costs VND 1,400,000,000 in 2026.

**Computation:**
```
Revenue method:
  Revenue above threshold:
    2,000,000,000 − 1,000,000,000 = 1,000,000,000
  PIT at 2%:                          20,000,000

Income method:
  Income:
    2,000,000,000 − 1,400,000,000 =   600,000,000
  PIT at 15%:                         90,000,000
```

The taxpayer may choose either method at this revenue level. Choosing the income method fixes it for 2 consecutive years. A taxpayer with revenue of VND 1,000,000,000 or less pays no PIT.

## Section 8 — Conservative Defaults

**Conservative Defaults table**

| Situation | Default Assumption |
| --- | --- |
| Unknown residency status | Treat as resident (progressive rates — higher tax) |
| Unknown number of dependents | Zero dependents (no deduction) |
| Dependent registration unclear | Do not claim deduction |
| Income category unclear | Employment income (progressive rates) |
| Insurance contribution cap unclear | Apply cap at statutory maximum |
| Allowance taxability unclear | Taxable (include in gross income) |
| Business vs employment income unclear | Employment income |

## Section 9 — Red Flag Thresholds

**Red Flag Thresholds table**

| Threshold | Value |
| --- | --- |
| HIGH single month tax discrepancy | VND 10,000,000 |
| HIGH annual under-withholding | VND 50,000,000 |
| MEDIUM unreported income source | Any additional source > VND 2,000,000/month |
| MEDIUM dependent claim without registration | Any amount |
| LOW rounding difference | VND 100,000 |

## Section 10 — Penalties

**Penalties table**

| Offence | Penalty |
| --- | --- |
| Late filing (quyết toán) | VND 2,000,000 – 25,000,000 |
| Late payment | 0.03% per day of unpaid tax |
| Under-declaration (underpayment) | 20% of underpaid amount |
| Tax evasion | 1× – 3× evaded tax + criminal liability |
| Failure to register dependents | Deduction denied + back-tax + interest |

## Section 11 — Exempt Income (Thu Nhập Miễn Thuế)

**Exempt Income table**

| Item | Notes |
| --- | --- |
| Real estate transfer between spouses, parents/children, siblings | Exempt |
| Inheritance/gift between immediate family | Exempt |
| Salary from night shift / dangerous work allowances | Per statutory schedule |
| One-off relocation allowance | Per statutory limits |
| Life insurance proceeds | Exempt |
| Severance pay per labour code | Exempt (up to statutory amount) |
| Interest on bank deposits | Exempt (5% withholding applies separately) |
| Scholarships | Exempt |

## Section 12 — Reference Material

### Key legislation

**Key legislation table**

| Topic | Reference |
| --- | --- |
| PIT Law | Luật Thuế TNCN No. 04/2007/QH12 (amended 2012, 2014) |
| 2026 bracket reform | Luật số 109/2025/QH15, arts 9 and 29: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat109-2025.pdf |
| Implementation decree | Nghị định 253/2026/NĐ-CP (in force 01/07/2026, replacing Nghị định 65/2013/NĐ-CP; residents' employment and business income from the 2026 tax period, art. 69): https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/16/469959-1784171413_v1_1784174315_signed.pdf |
| Business income | Luật số 109/2025/QH15, art. 7; Luật số 09/2026/QH16, art. 1; Nghị định 68/2026/NĐ-CP; Nghị định 141/2026/NĐ-CP |
| Circular guidance | Thông tư 111/2013/TT-BTC (as amended) |
| Deduction adjustment mechanism | Nghị quyết 954/2020/UBTVQH14 |
| Tax administration | Luật Quản lý Thuế No. 38/2019/QH14 |
| Social insurance | Luật BHXH No. 58/2014/QH13 |

### Open-source references

**Open-source references table**

| Repository | License | Scope |
| --- | --- | --- |
| [googlesky/thue-2026](https://github.com/googlesky/thue-2026) | MIT | 2026 PIT brackets and deduction amounts |
| [thangtd-0050/pit](https://github.com/thangtd-0050/pit) | Open source | Vietnam PIT calculator implementation |

### Known gaps

- Foreign tax credit computation for residents with overseas income — escalate
- Transfer pricing adjustments for related-party business income — escalate
- Expatriate tax equalisation — escalate
- Stock option / equity compensation — escalate
- Crypto / digital asset income — uncertain; escalate

### Self-check before finalisation

- [ ] Correct bracket schedule applied (2026 five-bracket system: 5%, 10%, 20%, 30%, 35%)?
- [ ] Business income kept off the bracket schedule, with the VND 1,000,000,000 threshold and the right method applied?
- [ ] Personal deduction at VND 15,500,000/month?
- [ ] Each dependent deduction at VND 6,200,000/month with registration confirmed?
- [ ] Compulsory insurance deducted before applying brackets?
- [ ] Insurance contribution caps applied correctly?
- [ ] All income sources identified and categorised?
- [ ] Withholding reconciled against annual liability?
- [ ] Filing deadline (31 March) noted?

## Section 13 — Changelog

**Changelog table**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | May 2026 | Initial release with 2026 five-bracket system per Luật số 109/2025/QH15 |
| 1.0 | 31 October 2026 | Corrected brackets 2 and 3 to 10% and 20%; replaced the business income section; recomputed the examples with current insurance caps |

## Prohibitions

- **Prohibitions list** — NEVER apply the old 7-bracket schedule for tax year 2026 onwards; NEVER apply the progressive brackets to business income; NEVER claim dependent deduction without confirmed registration; NEVER ignore compulsory insurance deductions when computing taxable income; NEVER apply resident rates to a confirmed non-resident; NEVER present calculations as definitive — direct to a licensed Vietnamese tax agent (đại lý thuế)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.

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
