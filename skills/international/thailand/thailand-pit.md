---
name: thailand-pit
description: Use this skill whenever asked to prepare, review, or classify transactions for Thailand Personal Income Tax (ภาษีเงินได้บุคคลธรรมดา), PND.90/91 filing, or advise on Thai PIT deductions and credits. Trigger on phrases like "ภาษีเงินได้บุคคลธรรมดา", "Thai income tax", "PND.90", "PND.91", "ภ.ง.ด.90", "ภ.ง.ด.91", or any Thailand personal tax request. ALWAYS read this skill before touching any Thailand PIT work.
version: 1.2
jurisdiction: TH
tax_year: 2025
last_updated: 2026-11-10
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Thailand Pit

## Thailand Personal Income Tax (ภาษีเงินได้บุคคลธรรมดา) Skill v1.2

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Thailand (ราชอาณาจักรไทย) |
| Tax | ภาษีเงินได้บุคคลธรรมดา (Personal Income Tax — PIT) |
| Currency | THB (Thai Baht / บาท) |
| Tax year | Calendar year (1 Jan – 31 Dec); Thai year = Gregorian + 543 |
| Current tax year | พ.ศ. 2569 (2026 CE) is in progress; the latest year filed is พ.ศ. 2568 (2025 CE), returns due by 31 March 2026 on paper. Figures in this guide are for 2025 unless marked 2026 (RD, ภ.ง.ด.90 instructions for 2568: https://www.rd.go.th/fileadmin/tax_pdf/pit/2568/Ins90_241268.pdf) |
| Tax authority | กรมสรรพากร Revenue Department (RD) |
| Return forms | ภ.ง.ด.91 (salary only) / ภ.ง.ด.90 (all income types) |
| Filing portal | https://efiling.rd.go.th |
| Filing deadline | 31 March of following year (paper); 8 April (e-filing) |
| Withholding | ภาษีหัก ณ ที่จ่าย — cumulative method per §50(1) |
| Source credit | `ratanon97/ThaiTaxCalculator` (TH-2567.json) + `anurat/laravel-thai-tax` (MIT) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Thai-licensed CPA or tax consultant |
| Skill version | 1.2 |

## Section 2 — Progressive tax brackets (อัตราภาษีก้าวหน้า)

Tax is computed on **Net Taxable Income** (เงินได้สุทธิ) after all deductions.

**Progressive tax brackets**

| Net Taxable Income (THB) | Rate | Max tax in bracket |
| --- | --- | --- |
| 0 – 150,000 | 0% (exempt) | 0 |
| 150,001 – 300,000 | 5% | 7,500 |
| 300,001 – 500,000 | 10% | 20,000 |
| 500,001 – 750,000 | 15% | 37,500 |
| 750,001 – 1,000,000 | 20% | 50,000 |
| 1,000,001 – 2,000,000 | 25% | 250,000 |
| 2,000,001 – 5,000,000 | 30% | 900,000 |
| Over 5,000,000 | 35% | — |

- **Net Taxable Income formula** — Net Taxable Income = Total Income − Expenses − Deductions − Allowances

## Section 3 — Employment expense deduction (ค่าใช้จ่าย)

**Employment expense deduction**

| Income type | Deduction |
| --- | --- |
| Employment income (§40(1)–(2)) | 50% of income, max **100,000 THB** |

## Section 4 — Personal allowances (ค่าลดหย่อนส่วนตัว)

**Personal allowances**

| Allowance | Amount (THB) | Conditions |
| --- | --- | --- |
| Self (ส่วนตัว) | 60,000 | Everyone |
| Spouse (คู่สมรส) | 60,000 | Spouse has no income |
| Child (บุตร) | 30,000 per child | — |
| Child born 2018+ (2nd onward) | 60,000 per child | บุตรคนที่ 2 เป็นต้นไปที่เกิดตั้งแต่ปี 2561 |
| Parent care (บิดามารดา) | 30,000 per parent | Age 60+, income < 30,000/yr; max 4 parents |
| Disabled person care | 60,000 per person | — |

## Section 5 — Retirement savings group (กลุ่มเพื่อการเกษียณ)

- **Combined cap for retirement savings group** — Combined cap: 500,000 THB for all items in this group.

**Retirement savings group**

| Deduction | Individual limit | Notes |
| --- | --- | --- |
| Provident Fund (PVD / กองทุนสำรองเลี้ยงชีพ) | 15% of salary | — |
| Gov. Pension Fund (กบข.) | 15% of salary | Government employees |
| RMF (กองทุนรวมเพื่อการเลี้ยงชีพ) | 30% of income | — |
| SSF (กองทุนรวมเพื่อการออม) | Not in the RD's 2025 deduction list | Do not claim for 2025 purchases unless a current deduction is confirmed; for Thai ESG see Section 7 |
| Pension life insurance (ประกันบำนาญ) | 15% of income, max 200,000 | — |
| National Savings Fund (กอช.) | max 30,000 | — |

## Section 6 — Insurance & social security

**Insurance & social security**

| Deduction | Limit (THB) | Notes |
| --- | --- | --- |
| Life insurance (ประกันชีวิต) | 100,000 | Policy must be 10+ years |
| Spouse life insurance | 10,000 | Spouse has no income |
| Health insurance (ประกันสุขภาพ) | 25,000 | Combined with life insurance ≤ 100,000 |
| Parent health insurance | 15,000 | Parent income < 30,000/yr |
| Social security (ประกันสังคม) | Actual contributions paid | 2025: max 750/month (9,000/yr) on the THB 15,000 wage ceiling. 2026: max 875/month (10,500/yr) on the THB 17,500 ceiling from 1 January 2026, less where the temporary 3% regional rate applied (see `th-payroll-social`). Spouse's contributions deductible if the marriage lasted the whole year (RD 2568 instructions, item 12) |

## Section 7 — Other deductions

**Other deductions**

| Deduction | Limit (THB) | Notes |
| --- | --- | --- |
| Home loan interest (ดอกเบี้ยบ้าน) | 100,000 | Purchase/build residence |
| Easy E-Receipt 2.0 (2025) | 50,000 | Purchases 16 January to 28 February 2025 only, with an e-Tax Invoice or e-Receipt: up to 30,000 on any goods or services, plus up to 20,000 on OTOP goods and purchases from registered community or social enterprises (RD 2568 instructions, item 17). Not a standing deduction; check whether a scheme exists for 2026 |
| Thai ESG fund units | 30% of assessable income, max 300,000 for units bought 1 January 2024 to 31 December 2026 (max 100,000 otherwise) | Units bought 2024 to 2026 held at least 5 years; otherwise held at least 8 years (RD 2568 instructions, items 18.1 to 18.3) |
| Thai ESGX fund units | 30% of assessable income, max 300,000 | Units bought within 2 months of the fund's first offer and by 30 June 2025, held at least 5 years (RD 2568 instructions, item 19) |

## Section 8 — Donations (เงินบริจาค)

Deducted after all other deductions.

**Donations**

| Type | Multiplier | Cap |
| --- | --- | --- |
| Education / Sport / Social (การศึกษา/กีฬา) | 2× | 10% of net income after deductions |
| General donation (ทั่วไป) | 1× | 10% of net income after deductions |
| Political party (พรรคการเมือง) | 1× | 10,000 |

## Section 9 — Computation method

- **Computation method steps** — Step 1: Total assessable income Step 2: − Employment expense deduction (50%, max 100,000) Step 3: − Personal allowances (Section 4) Step 4: − Retirement savings (Section 5, combined max 500,000) Step 5: − Insurance & social security (Section 6) Step 6: − Other deductions (Section 7) Step 7: = Income before donations Step 8: − Donations (Section 8, capped at 10% of Step 7) Step 9: = Net Taxable Income (เงินได้สุทธิ) Step 10: Apply progressive brackets (Section 2) Step 11: − Withholding tax already paid (ภาษีหัก ณ ที่จ่าย) Step 12: = Tax payable / refund

## Section 10 — Worked example

**Scenario (2025 tax year):** Salaried employee, annual income 1,200,000 THB, single, no children, pays into PVD 10% of salary, has social security, life insurance 50,000.

**Worked example — net taxable income computation**

| Step | Description | Amount (THB) |
| --- | --- | --- |
| Total income | Salary | 1,200,000 |
| − Expense deduction | 50% capped at 100,000 | (100,000) |
| − Personal allowance | Self | (60,000) |
| − PVD | 10% × 1,200,000 = 120,000 | (120,000) |
| − Social security | 750 × 12 | (9,000) |
| − Life insurance | Actual premium | (50,000) |
| **Net taxable income** |  | **861,000** |

Tax computation on 861,000:

**Worked example — tax by bracket**

| Bracket | Taxable in bracket | Rate | Tax |
| --- | --- | --- | --- |
| 0 – 150,000 | 150,000 | 0% | 0 |
| 150,001 – 300,000 | 150,000 | 5% | 7,500 |
| 300,001 – 500,000 | 200,000 | 10% | 20,000 |
| 500,001 – 750,000 | 250,000 | 15% | 37,500 |
| 750,001 – 861,000 | 111,000 | 20% | 22,200 |
| **Total tax** |  |  | **87,200** |

If withholding tax paid during the year was 95,000 → refund of **7,800 THB**.

**Same facts in 2026:** social security is 875 × 12 = 10,500, so net taxable income is 859,500. Tax: 7,500 + 20,000 + 37,500 + (109,500 × 20% = 21,900) = **86,900**; with 95,000 withheld, refund of **8,100 THB**.

## Section 11 — Filing guidance

### Who must file?

- **Filing threshold — single** — An individual with no spouse must file when assessable income exceeds 60,000 THB a year, or 120,000 THB where the income is employment income under s. 40(1) only.  _(Revenue Code (Revenue Department English translation), s. 56(1) and (2) — https://www.rd.go.th/english/37749.html#section56)_
- **Filing threshold — married** — A married individual must file when assessable income exceeds 120,000 THB a year, or 220,000 THB where the income is employment income under s. 40(1) only.  _(Revenue Code (Revenue Department English translation), s. 56(3) and (4) — https://www.rd.go.th/english/37749.html#section56)_
- **Filing required even if no tax owed** — Even if no tax is owed (income within exempt bracket), filing is still required if above thresholds.  _(Revenue Code (Revenue Department English translation), s. 56 — https://www.rd.go.th/english/37749.html#section56)_

### Which form?

**Which form?**

| Form | Who |
| --- | --- |
| ภ.ง.ด.91 (PND.91) | Salary/wage income only (§40(1)) |
| ภ.ง.ด.90 (PND.90) | All income types (§40(1)–(8)) |

### Key dates

**Key dates**

| Event | Deadline |
| --- | --- |
| Tax year end | 31 December |
| Paper filing deadline | 31 March |
| E-filing deadline | 8 April |
| Mid-year filing (PND.94) for business income | 30 September |

### Documents needed

- เอกสาร 50 ทวิ (Withholding tax certificate) from employer
- Proof of deductions (insurance certificates, PVD statements, donation receipts)
- Bank statements for additional income sources

## Section 12 — Conservative defaults

When in doubt:

**Conservative defaults**

| Situation | Conservative position |
| --- | --- |
| Deduction eligibility unclear | Do NOT claim it; flag for reviewer |
| Income type ambiguous | Classify as assessable; flag for reviewer |
| Foreign income sourced | Include if remitted to Thailand in same year; flag |
| Donation receipt missing | Do not deduct; flag |

## Section 13 — Classification rules for bank statement

**Classification rules for bank statement**

| Pattern / Keyword | Classification | Form line |
| --- | --- | --- |
| เงินเดือน / Salary / Payroll | Employment income §40(1) | PND.91 line 1 |
| โบนัส / Bonus | Employment income §40(1) | PND.91 line 1 |
| ค่าเช่า / Rent received | Rental income §40(5) | PND.90 |
| เงินปันผล / Dividend | Investment income §40(4) | PND.90 (can elect final WHT) |
| ดอกเบี้ย / Interest income | Investment income §40(4) | PND.90 (can elect final WHT) |
| ค่านายหน้า / Commission | Service income §40(2) | PND.90 |
| ขายของออนไลน์ / E-commerce | Business income §40(8) | PND.90 |
| ฟรีแลนซ์ / Freelance | Professional income §40(6) | PND.90 |

## Section 14 — Sources

**Sources**

| Source | URL |
| --- | --- |
| Revenue Department (กรมสรรพากร) | https://www.rd.go.th |
| Tax brackets reference | Revenue Code §48, §50 |
| `ratanon97/ThaiTaxCalculator` | https://github.com/ratanon97/ThaiTaxCalculator |
| `anurat/laravel-thai-tax` (MIT) | https://github.com/anurat/laravel-thai-tax |

## *OpenAccountants — open-source accounting skills for AI*

*OpenAccountants — open-source accounting skills for AI*
*All outputs must be reviewed by a qualified professional before filing.*

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
