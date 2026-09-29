---
name: japan-payroll
description: Use this skill whenever asked about Japanese payroll, income tax withholding (源泉徴収 gensen chōshū), social insurance (社会保険 shakai hoken), labour insurance (労働保険 rōdō hoken), or employer obligations in Japan. Trigger on phrases like "gensen choshu", "源泉徴収", "shakai hoken", "社会保険", "厚生年金", "kosei nenkin", "kenko hoken", "健康保険", "雇用保険", "koyou hoken", "労災保険", "rosai hoken", "年末調整", "nenmatsu chousei", "year-end adjustment", "standard monthly remuneration", "hyōjun hōshū getsugaku", "payslip Japan", "給与明細", "kyūyo meisai", "minimum wage Japan", "overtime Japan", "36 agreement", "子ども・子育て支援金", or any question about running payroll in Japan. ALWAYS read this skill before processing any Japanese payroll work.
version: 1.0
jurisdiction: JP
tax_year: 2026
last_updated: 2026-09-29
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Japan Payroll

## Japan -- Payroll Skill v1.0 (日本の給与計算)

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Japan (日本国) |
| Currency | JPY (¥) only |
| Tax year (income tax) | Calendar year (1 January -- 31 December) |
| Fiscal year (social insurance) | 1 April -- 31 March |
| Primary legislation | Income Tax Act (所得税法); Labour Standards Act (労働基準法); Health Insurance Act (健康保険法); Employees' Pension Insurance Act (厚生年金保険法); Employment Insurance Act (雇用保険法) |
| Tax authority | National Tax Agency (国税庁 NTA) |
| Social insurance authority | Japan Pension Service (日本年金機構); prefecture health insurance associations |
| Reporting system | 源泉徴収税額表 (withholding tax tables); 年末調整 (year-end adjustment) |
| Pay frequency | Monthly (most common, typically 25th or end of month) |
| Employer registration | Tax office (源泉徴収義務者) + Japan Pension Service + Hello Work (ハローワーク) |
| Validated by | Pending -- requires sign-off by a Japanese certified tax accountant (税理士) or social insurance labour consultant (社会保険労務士) |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (源泉徴収)

Japanese employers withhold income tax monthly using the NTA's published withholding tax tables (源泉徴収税額表 -- monthly table / 月額表). The tables include the 2.1% reconstruction surtax (復興特別所得税, in effect through 31 December 2037).

### Withholding Table Categories

**Withholding Table Categories**

| Column | Japanese | Criteria |
| --- | --- | --- |
| 甲 (Kō) | Primary employer | Employee has submitted 扶養控除等申告書 (dependency exemption declaration) |
| 乙 (Otsu) | Secondary employer | No declaration filed; flat 3.063% minimum or table rate |

- **甲 table lookup basis** — The 甲 table uses the employee's number of dependents (扶養親族等の数) to determine the withholding amount from a lookup table, not a formula.

### Reference: Individual Income Tax Brackets (Annual)

These are the annual rates applied at year-end adjustment (年末調整) or final return (確定申告). Monthly withholding approximates these progressively.

**Individual Income Tax Brackets (Annual)**

| Taxable Income (JPY) | Rate | Deduction |
| --- | --- | --- |
| 0 -- 1,950,000 | 5% | ¥0 |
| 1,950,001 -- 3,300,000 | 10% | ¥97,500 |
| 3,300,001 -- 6,950,000 | 20% | ¥427,500 |
| 6,950,001 -- 9,000,000 | 23% | ¥636,000 |
| 9,000,001 -- 18,000,000 | 33% | ¥1,536,000 |
| 18,000,001 -- 40,000,000 | 40% | ¥2,796,000 |
| 40,000,001+ | 45% | ¥4,796,000 |

Source: NTA Tax Answer No. 2260 所得税の税率 — https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm.

- **Reconstruction surtax and resident tax** — Plus 2.1% reconstruction surtax on calculated tax. Plus separate resident tax (住民税) at approximately 10% (municipal + prefectural), withheld from June of the following year.

### Employment Income Deduction (給与所得控除 -- 2026)

**Employment Income Deduction (2026)**

| Gross Employment Income (JPY) | Deduction |
| --- | --- |
| Up to 2,200,000 | ¥740,000 (minimum) |
| 2,200,001 -- 3,600,000 | Income × 30% + ¥80,000 |
| 3,600,001 -- 6,600,000 | Income × 20% + ¥440,000 |
| 6,600,001 -- 8,500,000 | Income × 10% + ¥1,100,000 |
| 8,500,001+ | ¥1,950,000 (cap) |

Source: NTA Tax Answer No. 1410 給与所得控除 — https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm. These are the amounts for 2026 and 2027 (令和8年分・令和9年分; in force from 1 December 2026 and applied to the whole of 2026 through the year-end adjustment); for incomes from ¥691,000 to under ¥2,200,000 the employment income is set by the special table on that page (from ¥741,000 to under ¥2,191,000: income minus ¥740,000). For 2025 (令和7年分) the minimum was ¥650,000 up to ¥1,900,000, then income × 30% + ¥80,000 to ¥3,600,000 and the same bands above. Until 2026-09-29 this table carried the 2020-2024 schedule (¥550,000 up to ¥1,625,000 and a 40% band to ¥1,800,000) under a 2026 heading.

### Year-End Adjustment (年末調整)

- **Year-end adjustment process** — Employers must perform nenmatsu chōsei in December for all 甲 employees. This reconciles monthly withholding to the actual annual tax liability, accounting for insurance deductions, spouse/dependent deductions, and housing loan credits. The employer refunds or collects the difference in the December (or January) payroll.

## Section 3 -- Social Security: Employee Deductions (社会保険 / 労働保険)

Japanese social insurance premiums are split approximately 50/50 between employer and employee (except workers' compensation which is employer-only and child allowance contribution which was employer-only until 2026).

### Employee Share of Social Insurance (2026)

**Employee Share of Social Insurance (2026)**

| Premium | Employee Rate | Basis | Ceiling |
| --- | --- | --- | --- |
| Health insurance (健康保険) | ~4.925% (Tokyo) | Standard monthly remuneration (SMR) | Grade 50: ¥1,390,000/month |
| Long-term care insurance (介護保険) | ~0.810% | SMR | Same as health; ages 40--64 only |
| Welfare pension (厚生年金) | 9.150% | SMR | Grade 32: ¥650,000/month |
| Employment insurance (雇用保険) | 0.50% (from Apr 2026) | Total wages | No ceiling |
| Child-rearing support (子ども・子育て支援金) | 0.115% (from Apr 2026) | SMR | Same as health |

Sources: 協会けんぽ FY2026 prefectural rates (Tokyo 9.85%; nursing care 1.62%; child-rearing support 0.23%, from the April 2026 premium) — https://www.kyoukaikenpo.or.jp/about/business/insurance_rate/rate_prefectures/r08; 日本年金機構 厚生年金保険料額表 (18.3%) — https://www.nenkin.go.jp/service/kounen/hokenryo/ryogaku/ryogakuhyo/20200825.html; 厚生労働省 雇用保険料率 FY2026 (general business 13.5/1,000: employee 5.0, employer 8.5) — https://www.mhlw.go.jp/content/001692566.pdf.

- **Prefecture variation note** — **Health insurance rates vary by prefecture and insurer.** The Tokyo rate shown (9.85% total / 4.925% employee) is illustrative. Each prefecture's Kyōkai Kenpō (協会けんぽ) publishes its own rate.

### Standard Monthly Remuneration (標準報酬月額)

- **Standard Monthly Remuneration (SMR)** — Social insurance premiums are based on the SMR, a standardised salary grade (not actual pay). SMR is determined in September each year (算定基届 santei kiso todoke) based on April--June average earnings. Changes mid-year only occur with significant salary changes (随時改定 zuiji kaitei -- ≥2 grade change sustained over 3 months).

### Bonus Premiums

- **Bonus premium caps** — Social insurance premiums also apply to bonuses at the same rates, subject to annual caps: - Health insurance: ¥5,730,000 cumulative annual cap on bonus - Welfare pension: ¥1,500,000 per single bonus payment

## Section 4 -- Social Security: Employer Contributions

### Employer Share of Social Insurance (2026)

**Employer Share of Social Insurance (2026)**

| Premium | Employer Rate | Notes |
| --- | --- | --- |
| Health insurance (Tokyo) | ~4.925% | Same as employee |
| Long-term care insurance | ~0.810% | Same as employee (ages 40--64) |
| Welfare pension | 9.150% | Same as employee |
| Child allowance contribution (子ども・子育て拠出金) | 0.360% | Employer-only; on SMR |
| Child-rearing support (子ども・子育て支援金) | 0.115% | From Apr 2026; same as employee |
| Employment insurance | 0.85% (from Apr 2026) | Higher than employee share |
| Workers' compensation (労災保険) | 0.30% (typical office) | Employer-only; rate varies by industry (0.25%--8.8%) |

### Total Indicative Employer Cost (2026, Tokyo, Age 40--64)

**Total Indicative Employer Cost (2026, Tokyo, Age 40--64)**

| Component | Rate |
| --- | --- |
| Health + long-term care | 5.735% |
| Welfare pension | 9.150% |
| Child allowance + child-rearing support | 0.475% |
| Employment insurance | 0.850% |
| Workers' compensation (office) | 0.300% |
| **Total employer social insurance** | **~16.51%** |

- **Under-40 employer cost** — For employees under 40 (no long-term care): approximately 15.70%.

## Section 5 -- Minimum Wage and Overtime

### Minimum Wage

- **Minimum wage system** — Japan has no single national minimum wage. Each prefecture sets its own rate annually, and each rate takes effect on its own date between early October and early December. The national weighted average was ¥1,121/hour for FY2025 and is ¥1,177/hour (¥1,176.93) for FY2026.

**Minimum Wage by Prefecture (FY2025 and FY2026)**

| Prefecture | FY2025 rate (JPY/hour) | In force from | FY2026 rate (JPY/hour) | In force from |
| --- | --- | --- | --- | --- |
| Tokyo | ¥1,226 | 3 Oct 2025 | ¥1,280 | 1 Oct 2026 |
| Kanagawa | ¥1,225 | 4 Oct 2025 | ¥1,279 | 1 Oct 2026 |
| Osaka | ¥1,177 | 16 Oct 2025 | ¥1,231 | 1 Oct 2026 |
| Aichi | ¥1,140 | 18 Oct 2025 | ¥1,195 | 1 Oct 2026 |
| Fukuoka | ¥1,057 | 16 Nov 2025 | ¥1,114 | 4 Oct 2026 |
| Okinawa | ¥1,023 | 1 Dec 2025 | ¥1,086 | 2 Dec 2026 |

Source: 厚生労働省 地域別最低賃金の全国一覧 (the FY2026 list, and the revision history from FY2002 to FY2026 in the workbook linked on the same page) — https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/minimumichiran/index.html. The FY2025 rate applies until the FY2026 rate takes effect in the prefecture.

The government targets ¥1,500/hour by the late 2020s.

### Overtime (Labour Standards Act)

**Overtime premium rates**

| Category | Premium Rate | Legal Basis |
| --- | --- | --- |
| Regular overtime (> 8 hrs/day or > 40 hrs/week) | 125% (25% premium) | Art. 37(1) |
| Overtime exceeding 60 hrs/month | 150% (50% premium) | Art. 37(1) proviso |
| Late-night work (22:00--05:00) | 125% (25% premium) | Art. 37(4) |
| Overtime + late-night | 150% (25% + 25%) | Combined |
| Statutory holiday work (法定休日) | 135% (35% premium) | Art. 37(1) |
| Statutory holiday + late-night | 160% (35% + 25%) | Combined |

Source: 労働基準法 (Labour Standards Act) art. 37 — para. 1 (overtime and statutory-holiday work, with the proviso of at least 50% for overtime beyond 60 hours in a month) and para. 4 (work from 22:00 to 05:00, at least 25%) — https://laws.e-gov.go.jp/law/322AC0000000049. The 25% overtime and 35% statutory-holiday premiums are set by Cabinet Order No. 5 of 1994 (労働基準法第三十七条第一項の時間外及び休日の割増賃金に係る率の最低限度を定める政令) — https://laws.e-gov.go.jp/law/406CO0000000005. The 60-hour rate has applied to every employer, small businesses included, since 1 April 2023. Family allowances, commuting allowances and the other pay named in the Ministry's ordinance are left out of the wage the premium is computed on (art. 37 para. 5).

### 36 Agreement (三六協定)

- **36 Agreement requirement** — Overtime requires a written labour-management agreement (36 Agreement) filed with the Labour Standards Inspection Office. Limits:

**36 Agreement limits**

| Limit | Standard | Special Clause |
| --- | --- | --- |
| Monthly | 45 hours | Under 100 hours (incl. holiday work) |
| Annual | 360 hours | Up to 720 hours |
| Multi-month average | -- | Must not exceed 80 hrs/month over any 2--6 month window |

- **36 Agreement violation penalty** — Violations can result in penalties of up to ¥300,000 fine or 6 months imprisonment.

Source: 労働基準法 art. 36 paras. 4 to 6 (the 45-hour and 360-hour limits; the special clause of up to 720 hours a year, with the month above 45 hours allowed in at most 6 months a year, under 100 hours in any month including holiday work, and an average of at most 80 hours a month over any 2 to 6 consecutive months including holiday work) and art. 119 item 1 (up to 6 months' imprisonment or a fine of up to ¥300,000 for breaching para. 6 or art. 37) — https://laws.e-gov.go.jp/law/322AC0000000049.

## Section 6 -- Mandatory Benefits

### Annual Paid Leave (年次有給休暇)

**Annual Paid Leave schedule**

| Years of Service | Days Granted |
| --- | --- |
| 0.5 years | 10 days |
| 1.5 years | 11 days |
| 2.5 years | 12 days |
| 3.5 years | 14 days |
| 4.5 years | 16 days |
| 5.5 years | 18 days |
| 6.5+ years | 20 days (maximum) |

Source: 労働基準法 art. 39 para. 1 (10 days after 6 months' service with at least 80% attendance), para. 2 (the table of additional days for each year of service), para. 3 (a proportionate number for employees working few days a week) and para. 7 (at least 5 days a year fixed by the employer where 10 or more are due), and art. 115 (2-year limitation) — https://laws.e-gov.go.jp/law/322AC0000000049.

- **Attendance and usage requirements** — Requires 80% attendance in the preceding year. Employers must ensure employees take at least 5 days per year. Unused leave expires after 2 years.

### Maternity Leave (産前産後休業)

- **Maternity leave provisions** — - Pre-birth: 6 weeks (14 weeks for multiple pregnancy) - Post-birth: 8 weeks (mandatory) - Benefit: approximately 67% of daily wage from health insurance (出産手当金) - Lump-sum birth allowance: ¥500,000 (出産育児一時金)

### Childcare Leave (育児休業)

- **Childcare leave provisions** — Up to the child's first birthday (extendable to 2 years if daycare unavailable). Benefit: 67% of wage for first 180 days, then 50%, from employment insurance. Social insurance premiums are exempt during leave.

### Sick Leave

- **Sick leave provisions** — No statutory paid sick leave in Japan. Employers typically provide 3--10 days contractually. Health insurance provides injury/sickness allowance (傷病手当金) at 2/3 of daily wage from the 4th day of absence, for up to 18 months.

### Retirement Allowance (退職金)

- **Retirement allowance customary practice** — Not legally required but deeply customary. Approximately 80% of large employers and 70% of SMEs offer some form of retirement benefit (lump sum, defined benefit, or defined contribution pension).

## Section 7 -- Payslip Requirements

Employers must provide a pay statement (給与明細書 kyūyo meisai-sho) each pay period under the Income Tax Act and Labour Standards Act.

### Mandatory Payslip Contents

- **Mandatory payslip contents** — - Employee name - Pay period and payment date - Base salary (基本給) - All allowances itemised (commuting 通勤手当, overtime 時間外手当, housing 住宅手当, etc.) - Gross pay - Deductions itemised: - Health insurance premium - Long-term care insurance premium (if applicable) - Welfare pension premium - Employment insurance premium - Income tax withholding (所得税) - Resident tax (住民税) -- withheld June through May - Net pay - Working hours and overtime hours

### Resident Tax (住民税)

- **Resident tax mechanics** — Resident tax is calculated by the municipality based on prior-year income. The municipality sends the employer a notification in May with monthly withholding amounts for June through the following May (special collection / 特別徴収). This is a flat amount per month, not percentage-based.

## Section 8 -- Filing Obligations

### Monthly Withholding Tax Payment

**Monthly Withholding Tax Payment due dates**

| Employer Size | Due Date |
| --- | --- |
| Standard | 10th of the following month |
| Small employer (≤ 10 employees, with approval) | Semi-annually: 10 July (Jan--Jun) and 10 January (Jul--Dec) |

- **Payment method** — Payment via bank transfer or e-Tax (国税電子申告 e-Tax).

### Year-End Adjustment (年末調整)

**Year-End Adjustment deadlines table**

| Task | Deadline |
| --- | --- |
| Collect employee declarations (扶養控除等申告書, 保険料控除申告書, etc.) | November--December |
| Perform year-end adjustment calculation | December payroll |
| Issue withholding tax slip (源泉徴収票) to employees | 31 January |
| File 法定調書合計表 (statutory report summary) to tax office | 31 January |
| Submit 給与支払報告書 (salary payment report) to municipality | 31 January |

### Social Insurance Reporting

**Social Insurance Reporting deadlines**

| Report | Deadline | Authority |
| --- | --- | --- |
| 算定基届 (annual SMR determination) | 1--10 July | Japan Pension Service |
| 月額変更届 (mid-year SMR change) | Promptly upon qualifying change | Japan Pension Service |
| 賞与支払届 (bonus payment notification) | Within 5 days of bonus payment | Japan Pension Service |
| 労働保険年度更新 (annual labour insurance update) | 1 June -- 10 July | Labour Bureau |

### Penalties

**Penalties table**

| Violation | Consequence |
| --- | --- |
| Late withholding tax payment | 5%--10% additional tax (不納付加算税) + delinquency tax (延滞税) |
| Failure to withhold | Employer liable for full tax amount |
| Overtime limit violation (36 Agreement) | Up to ¥300,000 fine or 6 months imprisonment |
| Failure to grant minimum 5 days paid leave | Up to ¥300,000 fine per violation |
| Failure to enrol in social insurance | Up to 6 months imprisonment or ¥500,000 fine; retroactive enrolment + premiums |

## Section 9 -- Common Payroll Patterns

### Pattern 1 -- Standard Monthly Employee (Tokyo, Age 35)

Monthly salary ¥350,000. No dependents (甲 column, 0 dependents). Commuting allowance ¥15,000/month (non-taxable up to ¥150,000/month).

1. Health insurance: ¥350,000 × 4.925% = ¥17,238
2. Welfare pension: ¥350,000 × 9.15% = ¥32,025
3. Employment insurance: ¥365,000 × 0.50% = ¥1,825 (on total wages incl. commuting)
4. Child-rearing support: ¥350,000 × 0.115% = ¥403
5. Income tax: per monthly table 甲, 0 dependents, ¥350,000 minus social insurance = ~¥8,250
6. Resident tax: per municipality notification (e.g., ¥18,000/month)
7. Net pay: ¥350,000 + ¥15,000 - deductions ≈ ¥287,259

Employer additionally pays: ¥17,238 (health) + ¥32,025 (pension) + ¥1,260 (child allowance) + ¥403 (child-rearing) + ¥3,103 (employment ins.) + ¥1,095 (workers' comp) = ~¥55,124

### Pattern 2 -- Bonus Payment (Summer/Winter)

Employee with SMR grade ¥350,000 receives ¥700,000 summer bonus.

1. Health insurance: ¥700,000 × 4.925% = ¥34,475
2. Welfare pension: ¥700,000 × 9.15% = ¥64,050 (under ¥1,500,000 per-bonus cap)
3. Employment insurance: ¥700,000 × 0.50% = ¥3,500
4. Income tax: per bonus withholding table (賞与に対する源泉徴収税額の算出率の表) -- rate based on prior month's social-insurance-deducted salary
5. No resident tax on bonus (already covered by monthly flat amount)

### Pattern 3 -- Mid-Year Salary Change (随時改定)

Employee's base salary increases from ¥300,000 to ¥350,000 in April. If the new SMR grade is 2+ grades different from the current grade, the employer files a 月額変更届. New SMR takes effect from July. Social insurance premiums update from the July payroll.

### Pattern 4 -- Employee on Childcare Leave

Social insurance premiums (both employee and employer shares) are exempt during childcare leave. Employment insurance premiums are not charged on zero-pay months. The employee receives childcare leave benefits from employment insurance (67% for first 180 days, 50% thereafter).

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills table**

| Skill | Interaction |
| --- | --- |
| payroll-workflow-base | Provides generic payroll processing steps; this skill adds Japan-specific rules |
| japan-bookkeeping | Payroll journals: salaries + ER social insurance to P&L; net pay + withholding tax + social insurance payable to BS |
| japan-consumption-tax | No consumption tax on salaries; commuting allowances are non-taxable for income tax but included in employment insurance base |
| japan-corporate-tax | Employer social insurance contributions and retirement allowance provisions are deductible expenses |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
