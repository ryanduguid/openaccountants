---
name: tanzania-payroll
version: 0.3
description: Use this skill whenever asked about Tanzania payroll processing for employed persons. Trigger on phrases like "Tanzania payroll", "PAYE Tanzania", "TRA PAYE", "NSSF contribution", "PSSSF", "SDL Tanzania", "Skills Development Levy", "WCF Tanzania", "Workers Compensation Fund", "ITX 300.01.E", "net salary Tanzania", "tax withholding Tanzania", "employer NSSF", "minimum wage Tanzania", "gross to net Tanzania", "salary calculation Tanzania", "TZS payroll", "Tanzanian Shilling salary", "non-resident PAYE Tanzania", "Zanzibar PAYE", or any question about computing employee pay, income-tax (PAYE) withholding, or social-security and payroll levies for Tanzania-based employees. This skill covers PAYE income-tax withholding by the employer, NSSF/PSSSF social security, the Skills Development Levy (SDL), the Workers Compensation Fund (WCF), minimum wage, and filing obligations to TRA / NSSF / WCF. ALWAYS read this skill before processing any Tanzania payroll.
jurisdiction: TZ
category: payroll
tax_year: 2026
last_updated: 2026-10-11
reviewed_by: Baraka Cassian
review_status: pending_review
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tanzania Payroll

## Tanzania Payroll Skill v0.3
> **Accountant-reviewed (`tier: 1`).** Baraka Cassian reviewed the rates and thresholds in this guide against the cited authorities on 2026-06-12; the reviewed figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29), and the sign-off is recorded in the frontmatter (`reviewed_by`, `review_status: current`) and on the roster in `PARTNERS.md`. Until 2026-09-29 this banner still read "Tier 2 (research-verified), not yet accountant-verified", the draft label the guide carried before that review. **Not covered by the review:** items flagged for further clarification were excluded, so the figures below that still carry the `[RESEARCH GAP — reviewer to confirm]` marker (notably the full sectoral minimum-wage schedule, the floating late-payment interest rate, and any NSSF wage ceiling) remain unconfirmed; a licensed Tanzanian tax practitioner / accountant must reconcile those before any output that depends on them is presented as final.
>
> **Edited since review (2026-10-11).** Citations now point to the statutes and the agencies' own publications instead of a secondary tax summary: the Income Tax Act, Cap 332 (the Revised Edition 2023 published by TRA, "ITA" below), the Tax Administration Act, Cap 438 ("TAA"), the National Social Security Fund Act, Cap 50, the Public Service Social Security Fund Act 2018, the Vocational Education and Training Act, Cap 82, the Workers Compensation Act, Cap 263, the Labour Institutions (Minimum Wage for Private Sector) Order, 2025 (GN 605A/2025), and TRA's "Pay As You Earn", SDL and penalties pages and its "Taxes and Duties at a Glance 2025/2026" booklet (July 2025). The sources changed four statements: PAYE is computed on pay after the employee's contribution to an approved retirement fund (ITA s.61; TRA PAYE page), so Examples 2 to 4, the template formula and Tests 2 to 4 are recomputed; the motor vehicle benefit halves for a vehicle more than five years old (ITA Fifth Schedule); Zanzibar's SDL is 4% for employers with four or more employees, not 5% (TRA booklet, section 5.0); and Section 7 now reproduces the monthly rates of the Second Schedule to GN 605A/2025 in full, which closes that research gap. The NSSF wage-ceiling gap is closed by the NSSF Act's First Schedule, which applies the contribution to every complete shilling of wages. The late-payment interest rate stays a time-varying figure: TAA s.3 defines the statutory rate as the prevailing Bank of Tanzania discount rate. These edits are not covered by the 2026-06-12 sign-off.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | United Republic of Tanzania (Mainland; Zanzibar PAYE rates identical) |
| Currency | Tanzanian Shilling (TZS) only |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) (ITA s.20(1)) |
| Income tax | YES — PAYE (Pay-As-You-Earn), progressive 0% / 8% / 20% / 25% / 30%, employer-withheld monthly (TRA; Income Tax Act, Cap. 332) |
| Non-resident employment income | **15%** withheld from the gross employment income of a non-resident employee, treated as final (ITA First Schedule para 4(a)(ii); TRA — Pay As You Earn) |
| Tax authority | TRA (Tanzania Revenue Authority) |
| Social security authority | NSSF (private sector) / PSSSF (public sector) |
| Payroll levies | SDL — Skills Development Levy (3.5%, employer-only, ≥10 staff); WCF — Workers Compensation Fund (0.5%, employer-only) |
| PAYE + SDL monthly deadline | **7th day of the following month** (ITA s.109(1); TRA — SDL/PAYE) |
| NSSF monthly deadline | **Within one month of the salary month** (i.e. by end of the following month) (NSSF Act ss.12(3) and 14(1); NSSF) |
| HESLB loan deduction | **15%** of the monthly salary of each Higher Education Students' Loans Board beneficiary, remitted by the **15th** of the following month (HESLB Act, Cap. 178) |
| WCF monthly deadline | **Within the following month** (e.g. July contributions by 31 August) (WCF) |
| Annual individual return | Within **6 months of year-end** (ITA s.117); statement of estimated tax by the first instalment date, 3 months into the year of income (ITA s.114); a resident whose only income is employment income withheld by the employer under s.104 need not file (ITA s.118) |
| Key legislation | Income Tax Act (Cap. 332); NSSF Act; PSSSF Act; Vocational Education & Training Act (SDL); Workers Compensation Act |
| Payment form | **ITX 300.01.E — Employment Taxes Payment Credit Slip** (PAYE + SDL); **NSSF/CON.5** (NSSF schedule) |
| Filing portal | TRA online portal (IDRAS / e-filing); NSSF online; WCF online (www.wcf.go.tz) |
| Validated by | Pending -- requires sign-off by a licensed Tanzanian tax practitioner |
| Skill version | 0.2 |

> Figures are cited to the Income Tax Act, Cap 332 (R.E. 2023), the NSSF Act, Cap 50, the PSSSF Act 2018, the Workers Compensation Act, Cap 263, GN 605A/2025 and the TRA, NSSF and WCF official sites (read 10-11 October 2026).

## Section 2 -- Income Tax Withholding (PAYE — Pay-As-You-Earn)

Tanzania **does** levy personal income tax on employees. The employer is the **withholding agent**: it deducts PAYE monthly from payroll and pays it to TRA within seven days after the end of the month, with the monthly withholding statement (ITA s.109(1)-(2); TRA's calendar states the **7th of the following month**), using form **ITX 300.01.E** (TRA — SDL/PAYE). The brackets below are expressed on **MONTHLY taxable employment income in TZS**, which is gross pay less the employee's contribution to an approved retirement fund (NSSF or PSSSF): the contribution reduces total income under ITA s.61, and TRA applies the same reduction in monthly withholding, capped at the statutory contribution (TRA — Pay As You Earn, "How contributions made to approved retirement funds are treated").

### PAYE Progressive Table — Monthly Taxable Income (resident, CONFIRMED)

**PAYE Progressive Table — Monthly Taxable Income (resident, CONFIRMED)**  _(ITA First Schedule para 1(1), the annual scale substituted by Finance Act 2021 s.25 and divided by twelve; TRA — Income tax for individuals (`tra.go.tz/page/income-tax-for-individuals`))_

| Monthly taxable income (TZS) | Marginal rate | Tax (cumulative at top of band) |
| --- | --- | --- |
| 0 – 270,000 | **NIL** | TZS 0 |
| 270,001 – 520,000 | **8%** of excess over 270,000 | TZS 20,000 |
| 520,001 – 760,000 | **20%** of excess over 520,000 | 20,000 + 48,000 = TZS 68,000 |
| 760,001 – 1,000,000 | **25%** of excess over 760,000 | 68,000 + 60,000 = TZS 128,000 |
| Over 1,000,000 | **30%** of excess over 1,000,000 | — |

Note: the lowest taxed band is **8%** (a secondary calculator source that stated 9% is incorrect; the First Schedule and TRA both give 8%).

- **Annual tax-free threshold** — TZS 3,240,000 (= 270,000 × 12)  _(TRA)_
- **Top marginal rate** — 30%  _(ITA First Schedule para 1(1); TRA)_
- **Zanzibar PAYE rates** — TRA publishes the same monthly scale for Mainland and Zanzibar (its booklet heads the table "Tanzania Mainland and Zanzibar"); First Schedule para 1(7) lets the Minister set a different Zanzibar rate in consultation with Zanzibar's finance minister, so check TRA's Zanzibar table for the year  _(TRA — Income tax for individuals; TRA booklet 2025/2026 section 4.0; ITA First Schedule para 1(7))_

**Subtract-method constants (resident)**

| Band (TZS) | Rate | Subtract (TZS) |
| --- | --- | --- |
| 270,001 – 520,000 | 8% | 21,600 |
| 520,001 – 760,000 | 20% | 84,000 |
| 760,001 – 1,000,000 | 25% | 122,000 |
| 1,000,001+ | 30% | 172,000 |

*Continuity check (subtract constants tie out to the cumulative column):*
- At 520,000 → 0.08 × 520,000 − 21,600 = 41,600 − 21,600 = **TZS 20,000**. Tie out.
- At 760,000 → 0.20 × 760,000 − 84,000 = 152,000 − 84,000 = **TZS 68,000**. Tie out.
- At 1,000,000 → 0.25 × 1,000,000 − 122,000 = 250,000 − 122,000 = **TZS 128,000**. Tie out.
- Band entry 1,000,001 → 0.30 × 1,000,001 − 172,000 = **TZS 128,000.30** ≈ continuous with 128,000. Tie out.

### Non-resident employment income

**Non-resident employment income table**

| Item | Detail | Source |
| --- | --- | --- |
| Non-resident PAYE | **15%** of payments to a non-resident employee, withheld by the employer | ITA First Schedule para 4(a)(ii) |
| Nature | Treated as **final**: a non-resident whose only Tanzanian income is such employment need not file a return | TRA — Pay As You Earn ("Specific rates applicable to certain categories of employees"); ITA s.118(b); TRA booklet 2025/2026 section 4.0 |
| Non-full-time directors | Director's fees are withheld at **15%**, and the tax is not final | ITA s.7(2)(h) and First Schedule para 4(a)(iii); TRA — Pay As You Earn |

### Benefits in kind (taxable employment income)

Benefits in kind are employment income, valued at market value unless the Act quantifies them (Income Tax Act, Cap. 332, s.7 read with s.27). Add the monthly share of the annual value to taxable pay before applying the PAYE table.

**Car benefit — annual taxable value**  _(ITA s.27(1)(a) and Fifth Schedule; TRA booklet 2025/2026 section 4.0(b))_

| Engine size | Vehicle less than 5 years old | Vehicle more than 5 years old |
| --- | --- | --- |
| Not exceeding 1,000 cc | TZS 250,000 | TZS 125,000 |
| Above 1,000 cc to 2,000 cc | TZS 500,000 | TZS 250,000 |
| Above 2,000 cc to 3,000 cc | TZS 1,000,000 | TZS 500,000 |
| Above 3,000 cc | TZS 1,500,000 | TZS 750,000 |

The age runs from manufacture (TRA booklet). The benefit is nil where the employer claims no deduction or relief for the ownership, maintenance or operation of the vehicle (ITA s.27(1)(a)).

- **Housing** — The lower of the market rental value and the higher of (i) 15% of the employee's total annual income excluding the housing and (ii) the expenditure the employer claims on the premises.  _(Income Tax Act, Cap. 332, s.27(1)(c))_
- **Preferential (low-interest) loan** — The benefit is the difference between interest at the Bank of Tanzania statutory rate and the interest actually charged.  _(Income Tax Act, Cap. 332, s.27)_
- **Other benefits** — The market value of the benefit.  _(Income Tax Act, Cap. 332, s.7 with s.27)_

### Withholding mechanism

- PAYE is **withheld monthly by the employer** from payroll and paid to TRA within seven days after the end of the month, the **7th** of the following month on TRA's calendar, on form **ITX 300.01.E** via the TRA online portal (ITA s.109(1); TRA — SDL/PAYE).
- Annual: final individual return due within **6 months of year-end** (ITA s.117); a statement of estimated tax is due by the first instalment date, within **3 months of the start of the year of income** (relevant for individuals with non-employment income) (ITA ss.113-114; TRA — Income tax for individuals).

## Section 3 -- NSSF Social Security (Private Sector — Employee + Employer)

Private-sector employees contribute to the **National Social Security Fund (NSSF)**. The employer deducts, schedules and pays both the employer and employee shares (NSSF — Rate of contributions).

### NSSF Contribution (basis: gross monthly salary)

**NSSF Contribution (basis: gross monthly salary)**  _(NSSF Act, Cap 50, ss.12-14 and First Schedule; NSSF — Rate of contributions)_

| Item | Total | Employer | Employee | Basis | Source |
| --- | --- | --- | --- | --- | --- |
| NSSF | **20%** | **10%** (≥ 10%) | **10%** (≤ 10%) | Gross monthly salary (every complete shilling of wages) | NSSF Act First Schedule; NSSF — Rate of contributions |

- **Total contribution basis** — Total contribution is 20% of the employee's gross monthly salary, a joint employer/employee contribution  _(NSSF)_
- **Employee share cap and splits** — The First Schedule sets the statutory contribution at twenty cents per complete shilling of wages and the share the employer may deduct from wages at ten cents, so the employee's share must not exceed 10% and the employer covers at least 10%. The common arrangement is 10% / 10%. The employer may also pay the full 20%, or other splits (e.g. 15% employer / 5% employee) are permitted provided the employee share ≤ 10%  _(NSSF Act ss.12-13 and First Schedule; NSSF — Rate of contributions)_
- **No statutory wage ceiling/floor** — The First Schedule applies the contribution to every complete shilling of wages with no upper or lower limit, and the NSSF rate page states a straight percentage of gross salary  _(NSSF Act First Schedule; NSSF — Rate of contributions)_
- **Filing form** — NSSF/CON.5 (schedule of contributing employees)  _(NSSF)_
- **NSSF deadline** — Pay within one month after the end of the month the contributions relate to (i.e. by the end of the following month); a late payment attracts a 5% penalty for each month or part-month, which the Board may remit  _(NSSF Act ss.12(3) and 14(1), (3); NSSF — Rate of contributions)_

*Column check (default split):* employer 10% + employee 10% = **20%** total. Tie out.

### PSSSF (Public Sector)

**PSSSF (Public Sector) table**  _(Public Service Social Security Fund Act 2018, s.18)_

| Item | Total | Employer | Employee | Source |
| --- | --- | --- | --- | --- |
| PSSSF | **20%** of monthly salary | 15% | 5% | PSSSF Act 2018, s.18(1)-(2) |

- **PSSSF applicability** — The Public Service Social Security Fund (PSSSF) applies to public-service employees, not the typical private employer. The contribution is 20% of the member's monthly salary: 5% deducted by the employer from the member's salary and 15% contributed by the employer to the member's account, or such amounts as the Minister determines by order in the Gazette after an actuarial valuation  _(PSSSF Act 2018, s.18(1)-(2))_

*Column check:* employer 15% + employee 5% = **20%** total. Tie out.

## Section 4 -- SDL — Skills Development Levy (Employer-only)

**SDL table**  _(Vocational Education and Training Act, Cap 82, s.14 (headcount of ten from Finance Act 2021 s.81); TRA — Skills Development Levy)_

| Item | Rate | Who pays | Basis | Threshold | Source |
| --- | --- | --- | --- | --- | --- |
| SDL | **3.5%** | Employer only | Total gross emoluments for the month | Employers with **≥ 10 employees** | VETA Act s.14; TRA — Skills Development Levy |

- **SDL basis clarification** — 3.5% of the total gross emoluments paid to all employees in the month: salaries, wages, payments in lieu of leave, fees, commissions, bonuses, gratuity and subsistence, travelling, entertainment or other allowances. Pay at intervals other than a month is converted to its monthly equivalent. (TRA's page and booklet state 3.5%; older material still shows the former 4% Mainland rate.)  _(TRA — Skills Development Levy)_
- **SDL headcount threshold** — Only employers with 10 or more employees are liable for SDL  _(TRA)_
- **SDL collection and form** — Collected by TRA; same payment form ITX 300.01.E  _(TRA)_
- **SDL deadline** — 7th day of the month following the payroll month (same as PAYE)  _(TRA)_
- **No liability, no return** — An employer not liable to SDL (fewer than 10 employees, or exempt) does not file SDL returns  _(TRA booklet 2025/2026 section 5.0(iii); Vocational Education and Training Act, Cap 82, as amended by Finance Act 2023)_
- **SDL in Zanzibar** — 4% of the monthly gross emoluments, payable by employers with four or more employees; the 3.5% rate and the ten-employee threshold are Mainland figures, and only exemptions (a) to (d) and (g) of the Mainland list apply in Zanzibar  _(TRA booklet 2025/2026 section 5.0(ii); TRA — Skills Development Levy)_

## Section 5 -- WCF — Workers Compensation Fund (Employer-only)

**WCF table**  _(Workers Compensation Act, Cap 263, ss.74-75; WCF — Michango (`wcf.go.tz/pages/contribution`))_

| Item | Rate | Who pays | Basis | Sector | Source |
| --- | --- | --- | --- | --- | --- |
| WCF | **0.5%** | Employer only | Monthly employee earnings (basic salary plus fixed allowances) | Private **and** public | WCA s.74; WCF — Michango |

- **WCF rate harmonisation** — 0.5% of the employer's monthly wage bill — the same rate now applies to both private and public sector (the previously differentiated 1% private / 0.5% public rates have been harmonised to 0.5%). The Act sets the tariff as a percentage of annual earnings fixed by the Board and lets the Minister cap the earnings assessed; no cap is published  _(WCA s.74(1), (7); WCF — Michango)_
- **WCF filing** — Filed/paid online at www.wcf.go.tz  _(WCF)_
- **WCF deadline** — Monthly, payable within the month or the following month (e.g. July contributions by 31 August). Quarterly/semi-annual/annual schedules are possible with Director-General approval; late payment bears interest of 2% of the unpaid amount per month  _(WCA s.75; WCF — Michango)_

## Section 6 -- Combined Employer / Employee Payroll Burden

For a **private employer with ≥ 10 employees** (so SDL applies), on a resident employee using the default NSSF 10%/10% split:

**Combined Employer / Employee Payroll Burden table**

| Item | Employee | Employer | Basis |
| --- | --- | --- | --- |
| PAYE | 0–30% progressive (withheld) | (withholding agent) | monthly taxable income (gross less employee NSSF) |
| NSSF | 10% | 10% | gross |
| SDL | — | 3.5% | total gross emoluments (≥ 10 staff) |
| WCF | — | 0.5% | gross wage bill |

- **Employer on-cost above gross salary** — 10% (NSSF) + 3.5% (SDL) + 0.5% (WCF) = 14% of gross for employers with ≥ 10 staff
- **Fewer than 10 employees on-cost** — If the employer has fewer than 10 employees, SDL does not apply. The employer on-cost is then NSSF 10% + WCF 0.5% = 10.5% of gross. PAYE and NSSF still apply in full.
- **HESLB loan beneficiaries** — The employer deducts 15% of the monthly salary of each Higher Education Students' Loans Board beneficiary and remits it by the 15th of the following month; failing to deduct or remit on time costs the employer a penalty of 10% of the monthly deduction. It is an employee deduction, not an employer cost, and it comes after PAYE.  _(Higher Education Students' Loans Board Act, Cap. 178)_

## Section 7 -- Minimum Wage (Private Sector)

Tanzania has **no single national minimum wage** — minimum wages are **sectoral**.

**Minimum wage instrument/structure table**  _(Labour Institutions (Minimum Wage for Private Sector) Order, 2025, GN 605A/2025, paras 1, 2, 4 and 7 and Schedules; TanzLII)_

| Item | Detail | Source |
| --- | --- | --- |
| Current order | **Labour Institutions (Minimum Wage for Private Sector) Order, 2025 (GN 605A/2025)**, made under s.39(1) of the Labour Institutions Act, published 13 October 2025 and in force **from 1 January 2026**; revokes the 2022 order (GN 687/2022) | GN 605A/2025, paras 1 and 7 |
| Scope | All employees and employers in the private sector; an employee already paid above the new rate keeps the higher wage with the same employer | GN 605A/2025, paras 2 and 6 |
| Structure | Sixteen sectors or areas (First Schedule) with hourly, daily, weekly, fortnightly and monthly rates for each sub-sector (Second Schedule); the monthly rate is the minimum for the sub-sector and may be improved by contract or collective agreement | GN 605A/2025, para 4 and Schedules |

### Sectoral minimum wages (TZS/month) — GN 605A/2025 Second Schedule

**Sectoral minimum wages (TZS/month)**  _(GN 605A/2025, Second Schedule, monthly column; the order also prints hourly, daily, weekly and fortnightly rates)_

| Sector | Sub-sector | Monthly minimum (TZS) |
| --- | --- | --- |
| 1. Agricultural | (a) Crop or animal production and related undertakings | 175,000 |
| 1. Agricultural | (b) Forestry and deforestation of trees | 185,000 |
| 1. Agricultural | (c) Fishing and fish farming or aquaculture | 300,000 |
| 2. Health | (a) Hospital | 250,000 |
| 2. Health | (b) Health centre | 240,000 |
| 2. Health | (c) Polyclinic | 240,000 |
| 2. Health | (d) Dispensary | 230,000 |
| 2. Health | (e) Pharmacy | 240,000 |
| 3. Communications | (a) Programme, advertising and media | 289,000 |
| 3. Communications | (b) Telecommunication services | 644,000 |
| 3. Communications | (c) Call centre | 380,000 |
| 4. Domestic work | (a) Domestic workers employed by diplomats and major businessmen | 328,000 |
| 4. Domestic work | (b) Domestic workers employed by entitled officers | 265,000 |
| 4. Domestic work | (c) Domestic workers not residing in the employer's household (other than (a) and (b)) | 160,000 |
| 4. Domestic work | (d) Other domestic workers | 80,000 |
| 5. Hotel and hospitality | (a) Five star and four star hotels | 375,000 |
| 5. Hotel and hospitality | (b) Three star hotels | 225,000 |
| 5. Hotel and hospitality | (c) One and two star hotels, lodgings and guest houses, bars and restaurants | 195,000 |
| 5. Hotel and hospitality | (d) Tourist luggage porter | 225,000 |
| 5. Hotel and hospitality | (e) Tour guide | 320,000 |
| 5. Hotel and hospitality | (f) Hunting and related activities | 200,000 |
| 6. Private security | (a) International companies | 292,000 |
| 6. Private security | (b) Domestic companies | 197,000 |
| 7. Energy | (a) International companies | 765,900 |
| 7. Energy | (b) Domestic companies | 297,000 |
| 8. Transport and shipping | (a) Aviation services | 498,000 |
| 8. Transport and shipping | (b) Freight clearing and forwarding | 464,000 |
| 8. Transport and shipping | (c) Inland transport services | 398,500 |
| 8. Transport and shipping | (d) Postal and courier services | 287,500 |
| 9. Construction | (a) Contractors Class I | 515,000 |
| 9. Construction | (b) Contractors Class II to IV | 464,500 |
| 9. Construction | (c) Contractors Class V to VII | 398,500 |
| 10. Mining | (a) Mining and prospecting | 695,000 |
| 10. Mining | (b) Primary mining licence | 397,600 |
| 10. Mining | (c) Dealer licence | 595,000 |
| 10. Mining | (d) Brokers licences | 333,500 |
| 11. Private schools | (a) Pre-primary and primary schools | 276,500 |
| 11. Private schools | (b) Secondary schools | 281,300 |
| 11. Private schools | (c) Colleges or vocational training institutes | 281,500 |
| 11. Private schools | (d) Higher education institutions | 300,700 |
| 12. Trade and finance | (a) Business | 200,500 |
| 12. Trade and finance | (b)(i) Commercial banks | 733,000 |
| 12. Trade and finance | (b)(ii) Community services banks | 698,400 |
| 12. Trade and finance | (b)(iii) Micro credit financial services | 699,000 (printed "699,0000" on TanzLII; the hourly rate of 3,585 supports 699,000 — confirm against the gazette) |
| 12. Trade and finance | (b)(iv) Insurance companies | 699,700 |
| 12. Trade and finance | (b)(v) Other financial institutions | 699,500 |
| 13. Industrial | — | 200,000 |
| 14. Sport, arts, entertainment and gaming | — | 287,500 |
| 15. Waste collection, processing and disposal | — | 188,500 |
| 16. Any other sector or area not specified | — | 175,000 |

The lowest monthly rate is TZS 80,000 (other domestic workers) and the highest TZS 765,900 (international energy companies). Placing an employee in the right sub-sector (hotel star rating, contractor class, international versus domestic company) is a judgement for the reviewer; the order's definitions (para 3) treat forestry, fishing and primary processing as agriculture and define mining by the Mining Act.

## Section 8 -- Conservative Defaults

**Conservative Defaults table**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Residency status | Assume **resident** (progressive table) only if confirmed; if status unknown, FLAG | Non-resident is flat 15% final — materially different |
| NSSF split | Use **10% employee / 10% employer** | Default; employee share capped at 10% |
| Headcount unknown (for SDL) | Compute **without** SDL but FLAG; never silently apply 3.5% | SDL applies only at ≥ 10 employees |
| Headcount ≥ 10 confirmed | Apply **SDL 3.5%** (employer) | Statutory once threshold met |
| Public vs private sector | Default **private** (NSSF + SDL + WCF); switch to PSSSF if public | PSSSF only for public-sector staff |
| NSSF wage ceiling | Apply 20% on **full gross** (no cap) | The NSSF Act's First Schedule applies the contribution to every complete shilling of wages |
| Tax year | Default to **2026** brackets/rates | Skill tax_year is 2026 |
| Currency | Tanzanian Shilling (TZS) | Local currency |
| Minimum-wage sub-sector unknown | Do NOT pick a figure — request the sub-sector and use GN 605A/2025 | Sectoral; no national floor |

When an input is missing or ambiguous, apply the **conservative** assumption (the one that does NOT understate withholding/contributions) and FLAG it for the reviewer.

### Required inputs before computing payroll

1. Gross monthly salary in TZS (and any non-cash/benefit components).
2. **Residency status** (resident → progressive; non-resident → flat 15% final).
3. Sector / sub-sector (drives the minimum-wage check under GN 605A/2025).
4. **Number of employees** on the payroll (drives SDL liability at ≥ 10).
5. Whether the employer is **private (NSSF)** or **public (PSSSF)**.
6. NSSF split if non-standard (employer may pay full 20%; employee share ≤ 10%).
7. Tax/fiscal year (2026 vs later schedules).
8. Pay frequency.

### Refusal catalogue — DO NOT compute, refuse and request input

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| No gross salary provided | REFUSE — request salary in TZS |
| Residency status unknown | REFUSE — resident vs non-resident changes PAYE entirely (progressive vs flat 15%) |
| Request to omit PAYE, NSSF, SDL or WCF to "save money" | REFUSE — statutory; escalate to accountant |
| Request to apply SDL where headcount is < 10 | REFUSE — SDL only applies at ≥ 10 employees |
| Request to apply SDL at 4% | REFUSE — TRA-confirmed rate is 3.5% |
| Request to set an exact minimum-wage figure without the sub-sector | REFUSE — sectoral; request sub-sector and use GN 605A/2025 |
| Self-employed / non-employment income mixed in | REFUSE payroll path — route to a Tanzania income-tax skill (annual return) |
| Definitive "this is your exact tax" assertion requested | REFUSE — outputs are estimates pending accountant sign-off |

## Section 10 -- Transaction / Payment Pattern Library (deterministic)

Classify bank-statement lines deterministically. Match case-insensitively; longest/most-specific pattern wins. Tanzanian statements appear in **English and Kiswahili**.

### Salary credits (money arriving in an employee account)

**Salary credits table**

| Pattern (case-insensitive) | Classification |
| --- | --- |
| `SALARY`, `MSHAHARA`, `MISHAHARA`, `PAYROLL`, `NET PAY` | Net salary payment |
| `MALIPO YA MSHAHARA`, `WAGE`, `TRANSF.* [employer]` | Net salary payment |
| `NSSF REFUND`, `MAREJESHO NSSF` | NSSF refund/adjustment — not income |
| `TRA REFUND`, `PAYE REFUND` | PAYE refund/adjustment — not income |

### Employer debits (money leaving the employer account)

**Employer debits table**

| Pattern | Classification |
| --- | --- |
| `TRA`, `PAYE`, `ITX 300`, `KODI`, `WITHHOLDING TAX` | PAYE withholding remitted to TRA (ITX 300.01.E) |
| `SDL`, `SKILLS DEVELOPMENT LEVY`, `TOZO YA UJUZI` | Skills Development Levy remitted to TRA (3.5%, ≥ 10 staff) |
| `NSSF`, `MICHANGO NSSF`, `CON.5`, `PENSION` | NSSF contribution (employer + employee shares) |
| `PSSSF` | PSSSF contribution (public-sector) |
| `WCF`, `FIDIA YA WAFANYAKAZI`, `WORKERS COMPENSATION` | Workers Compensation Fund (0.5%, employer-only) |
| `NET WAGES`, `MALIPO YA MISHAHARA`, `SALARY RUN`, `DISBURSEMENT` | Net wages disbursed to employees |

## Section 11 -- Worked Examples

> All figures use the **2026** resident PAYE table and 2026 contribution rates. PAYE is computed on gross pay less the employee NSSF share (ITA s.61; TRA — Pay As You Earn). Default NSSF split is 10% employee / 10% employer. SDL (3.5%) is shown only where the employer has ≥ 10 staff. WCF (0.5%) and SDL are employer-only and do **not** reduce employee net pay. Amounts rounded to the shilling.

### Example 1 — Low earner below the PAYE threshold

**Inputs:** Gross salary TZS 250,000/month. Resident. NSSF 10%/10%.

- NSSF employee 10% × 250,000 = **TZS 25,000**.
- PAYE base = 250,000 − 25,000 = 225,000 ≤ 270,000 → PAYE **TZS 0**.
- **Employee deductions total** = 0 + 25,000 = **TZS 25,000**.
- **Net pay** = 250,000 − 25,000 = **TZS 225,000**.

*Bank line example:* `MSHAHARA — JANUARY` credit **TZS 225,000**.

### Example 2 — Earner in the 8% PAYE band

**Inputs:** Gross salary TZS 400,000/month. Resident. NSSF 10%/10%.

- NSSF employee 10% × 400,000 = **TZS 40,000** (deducted before PAYE, ITA s.61).
- PAYE base = 400,000 − 40,000 = **TZS 360,000**, in the 8% band → 0.08 × 360,000 − 21,600 = 28,800 − 21,600 = **TZS 7,200**.
  - Verify by band: 0.08 × (360,000 − 270,000) = 0.08 × 90,000 = **7,200**. Tie out.
- **Employee deductions total** = 7,200 + 40,000 = **TZS 47,200**.
- **Net pay** = 400,000 − 47,200 = **TZS 352,800**.

### Example 3 — Mid earner in the 20% PAYE band

**Inputs:** Gross salary TZS 700,000/month. Resident. NSSF 10%/10%.

- NSSF employee 10% × 700,000 = **TZS 70,000**.
- PAYE base = 700,000 − 70,000 = **TZS 630,000**, in the 20% band → 0.20 × 630,000 − 84,000 = 126,000 − 84,000 = **TZS 42,000**.
  - Verify by bands: 20,000 (up to 520k) + 0.20 × (630,000 − 520,000) = 20,000 + 22,000 = **42,000**. Tie out.
- **Employee deductions total** = 42,000 + 70,000 = **TZS 112,000**.
- **Net pay** = 700,000 − 112,000 = **TZS 588,000**.

### Example 4 — Higher earner in the 30% PAYE band

**Inputs:** Gross salary TZS 1,500,000/month. Resident. NSSF 10%/10%.

- NSSF employee 10% × 1,500,000 = **TZS 150,000**.
- PAYE base = 1,500,000 − 150,000 = **TZS 1,350,000**, in the 30% band → 0.30 × 1,350,000 − 172,000 = 405,000 − 172,000 = **TZS 233,000**.
  - Verify by bands: 128,000 (up to 1,000k) + 0.30 × (1,350,000 − 1,000,000) = 128,000 + 105,000 = **233,000**. Tie out.
- **Employee deductions total** = 233,000 + 150,000 = **TZS 383,000**.
- **Net pay** = 1,500,000 − 383,000 = **TZS 1,117,000**.

### Example 5 — Employer total cost of the mid earner (TZS 700,000, ≥ 10 staff)

Building on Example 3 (gross TZS 700,000), private employer with ≥ 10 employees:

**Employer cost table**

| Employer cost item | Computation | Amount (TZS) |
| --- | --- | --- |
| Gross salary | — | 700,000 |
| NSSF employer 10% | 10% × 700,000 | 70,000 |
| SDL 3.5% | 3.5% × 700,000 | 24,500 |
| WCF 0.5% | 0.5% × 700,000 | 3,500 |
| **Total employer cost** | sum | **798,000** |

*Check:* 700,000 + 70,000 + 24,500 + 3,500 = **798,000**. Tie out.
(Employer-on-top burden = TZS 98,000 = **14%** of gross.)

### Example 6 — Non-resident employee (flat 15% final)

**Inputs:** Non-resident, Tanzania-source employment income TZS 700,000/month.

- PAYE = flat **15% × 700,000 = TZS 105,000** (final tax; no further return).
- Net of PAYE = 700,000 − 105,000 = **TZS 595,000**.

> NSSF may still apply to a non-resident working in Tanzania depending on the engagement; the **15% PAYE is a final income-tax**, separate from any social-security liability. Confirm NSSF applicability for the specific contract with the reviewer.

## Section 12 -- Tier 1 Rules (hard, non-negotiable)

- **Rule 1** — PAYE is employer-withheld monthly and remitted to TRA by the 7th of the following month on ITX 300.01.E; never skip it for salaried staff  _(TRA)_
- **Rule 2** — Deduct the employee's NSSF or PSSSF contribution from gross pay first (ITA s.61; TRA), then apply the subtract-method constants exactly (21,600 / 84,000 / 122,000 / 172,000) to that PAYE base. The lowest taxed band is 8%, not 9%.
- **Rule 3** — Non-residents pay a flat 15% final tax on Tanzania-source employment income — never apply the progressive table to a confirmed non-resident  _(ITA First Schedule para 4(a)(ii); TRA — Pay As You Earn)_
- **Rule 4** — NSSF is 20% total (default 10%/10%); the employee share must not exceed 10%  _(NSSF Act First Schedule; NSSF)_
- **Rule 5** — SDL (3.5%) is employer-only and applies only at ≥ 10 employees; the rate is 3.5%, not 4%  _(TRA)_
- **Rule 6** — WCF (0.5%) is employer-only and applies to both private and public sector  _(WCF)_
- **Rule 7** — PAYE + SDL share the 7th-of-next-month deadline; NSSF and WCF are due within the following month  _(TRA; NSSF; WCF)_
- **Rule 8** — Minimum wage is sectoral under GN 605A/2025 (in force 1 Jan 2026) — there is no national floor; use the employee's sub-sector rate
- **Rule 9** — Every output is an estimate pending licensed-accountant sign-off

## Section 13 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue table**

| Question | Why it needs a reviewer |
| --- | --- |
| Minimum-wage sub-sector classification (GN 605A/2025) | The Second Schedule is reproduced in Section 7; placing an employee in the right sub-sector (hotel star rating, contractor class, international versus domestic company) is a judgement call |
| Late-payment interest rate | The statutory rate is the prevailing Bank of Tanzania discount rate (TAA s.3), compounded monthly (TAA s.76); read the rate for the period from the Bank of Tanzania |
| Non-resident NSSF liability | Depends on the specific contract / secondment arrangement |
| Non-standard NSSF splits (e.g. 15%/5%, employer pays full 20%) | Permitted provided employee share ≤ 10%; depends on employer policy |
| Treatment of benefits in kind / allowances in the PAYE and NSSF base | Edge cases not fully nailed from primary sources |

## Section 14 -- Excel Working Paper Template

Suggested layout (one row per employee per month):

**Excel Working Paper Template table**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Gross monthly salary (TZS) | input |
| C | Resident? (Y/N) | input |
| D | Headcount ≥ 10? (Y/N) | input (drives SDL) |
| E | PAYE (monthly) | resident: nested IF on the PAYE base `(B-F)` (subtract constants); non-resident: `=B*15%` |
| F | NSSF employee | `=B*10%` |
| G | Employee deductions | `=E+F` |
| H | Net pay | `=B-G` |
| I | NSSF employer | `=B*10%` |
| J | SDL (employer) | `=IF(D="Y", B*3.5%, 0)` |
| K | WCF (employer) | `=B*0.5%` |
| L | Total employer cost | `=B+I+J+K` |

- **Resident PAYE formula for column E (2026, monthly)** — =IF((B-F)<=270000,0, IF((B-F)<=520000, (B-F)*0.08-21600, IF((B-F)<=760000, (B-F)*0.20-84000, IF((B-F)<=1000000, (B-F)*0.25-122000, (B-F)*0.30-172000))))
- **Non-resident PAYE formula** — =B*0.15 (flat, final)

## Section 15 -- Bank Statement / Terminology Reading Guide

**Terminology guide table**

| Term (English / Kiswahili) | Meaning |
| --- | --- |
| Salary / Mshahara (pl. Mishahara) | Salary / wage |
| Malipo ya mshahara | Salary payment |
| PAYE | Pay-As-You-Earn income-tax withholding |
| TRA (Tanzania Revenue Authority) / Mamlaka ya Mapato Tanzania | Tax authority |
| Kodi | Tax |
| ITX 300.01.E | Employment Taxes Payment Credit Slip (PAYE + SDL) |
| NSSF / Mfuko wa Hifadhi ya Jamii | National Social Security Fund (private sector) |
| PSSSF | Public Service Social Security Fund (public sector) |
| NSSF/CON.5 | NSSF schedule of contributing employees |
| SDL / Tozo ya Maendeleo ya Ujuzi | Skills Development Levy (3.5%, employer-only, ≥ 10 staff) |
| WCF / Mfuko wa Fidia kwa Wafanyakazi | Workers Compensation Fund (0.5%, employer-only) |
| Net pay / Malipo halisi | Take-home pay after deductions |
| Mkazi / Asiye mkazi | Resident / non-resident (15% flat final PAYE) |

## Section 16 -- Onboarding Fallback

If the engagement lacks key data:

1. **No prior payroll register available** → request the last 3 months of payroll and TRA/NSSF/WCF receipts to back-solve the rates actually applied.
2. **Unknown residency** → do not compute PAYE; confirm resident vs non-resident first (progressive vs flat 15% final).
3. **Unknown headcount** → default SDL OFF, FLAG; confirm before the first remittance (SDL at ≥ 10).
4. **Unknown sector** → do not assert a minimum wage; request the sub-sector and check GN 605A/2025.
5. **Year ambiguity** → default 2026 table/rates; switch only for periods in a later year of income.
6. **Public vs private** → confirm; PSSSF (public) vs NSSF (private) change the contribution path.

## Section 17 -- Filing, Forms & Deadlines

**Filing, Forms & Deadlines table**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year ending 31 Dec | ITA s.20(1) |
| PAYE | Withheld and paid to TRA **monthly**, within seven days after the end of the month (the **7th** of the following month), with the monthly withholding statement, on **ITX 300.01.E** via the TRA online portal (IDRAS) | ITA s.109(1)-(2); TRA — SDL/PAYE |
| SDL | Paid to TRA **monthly**, by the **7th** of the following month, on **ITX 300.01.E** (employers with ≥ 10 employees) | TRA — Skills Development Levy |
| Employer statements and certificates | Monthly withholding statement within seven days after the end of the month (ITA s.109(2), which replaced the six-monthly statement the reviewer cited from s.84(2) of the 2019 edition); a withholding certificate to each employee for the year by **30 January**, or within 30 days of the employment ending (ITA s.110(3)); an SDL half-year certificate reconciling the monthly returns (TRA — SDL) | ITA ss.109-110 (R.E. 2023); TRA — Skills Development Levy |
| HESLB | 15% of each loan beneficiary's monthly salary, remitted by the **15th** of the following month | HESLB Act, Cap. 178 |
| NSSF | Declared on **NSSF/CON.5** and paid **within one month** of the salary month | NSSF — Rate of contributions |
| WCF | Paid online (`wcf.go.tz`) **within the following month** (e.g. July → by 31 August); other schedules with DG approval | WCF |
| Annual individual return | Within **6 months of year-end**; estimate within **3 months of start of year of income** | ITA ss.114 and 117; TRA — Income tax for individuals |
| Registration | Any person conducting business must register with TRA and obtain a **TIN**; PAYE/withholding registration is part of business registration | TRA |

## Section 18 -- Penalties & Interest

Governed by TRA rules (TRA — Interest, penalties & offences).

**Penalties & Interest table**

| Item | Detail | Source |
| --- | --- | --- |
| Currency point | **TZS 20,000** (official TRA value) | TRA |
| Interest on late payment of tax | Charged at the **statutory rate**, the prevailing Bank of Tanzania discount rate, **compounded monthly** (variable; TRA publishes no fixed %) | TAA ss.3 and 76; TRA |
| Failure to file return / pay on time | Per month (or part-month) the failure continues: the **higher of** (a) **2.5%** of tax assessed less tax already paid, or (b) **5 currency points (TZS 100,000)** for an individual / **15 currency points (TZS 300,000)** for a body corporate | TAA s.78; TRA |

> **Reviewer input.** The exact interest percentage is **not** a fixed figure — the statutory rate is the prevailing Bank of Tanzania discount rate (TAA s.3), compounded monthly (TAA s.76). Read the rate for the period from the Bank of Tanzania before quoting any number.

## Section 19 -- Reference Material

**Reference Material table**

| Topic | Figure | Source |
| --- | --- | --- |
| PAYE NIL band | 0 – 270,000 TZS/month (annual TZS 3,240,000) | ITA First Schedule para 1(1); TRA |
| PAYE bands | 8% / 20% / 25% / 30% at 520k / 760k / 1,000k edges, applied to gross less the employee's retirement contribution | ITA s.61 and First Schedule para 1(1) (Finance Act 2021 s.25); TRA |
| Non-resident PAYE | 15% flat, final | ITA First Schedule para 4(a)(ii); TRA — Pay As You Earn |
| NSSF | 20% total (default 10% ee / 10% er), gross; employee share ≤ 10% | NSSF Act ss.12-14 and First Schedule; NSSF |
| PSSSF (public) | 20% of monthly salary (5% ee / 15% er) | PSSSF Act 2018 s.18 |
| SDL | 3.5% employer-only, total gross emoluments, ≥ 10 employees | VETA Act s.14; TRA |
| WCF | 0.5% employer-only, gross wage bill, both sectors | WCA ss.74-75; WCF |
| PAYE / SDL deadline | 7th of following month (ITX 300.01.E) | TRA |
| NSSF deadline | Within one month of salary month (NSSF/CON.5) | NSSF |
| WCF deadline | Within the following month | WCF |
| Annual return | Within 6 months of year-end | ITA s.117 |
| Currency point | TZS 20,000 | TRA |
| Minimum wage | Sectoral (GN 605A/2025 Second Schedule, in force 1 Jan 2026); no national floor; TZS 175,000 for unlisted sectors | GN 605A/2025 |

Key authorities: Income Tax Act, Cap 332, R.E. 2023 (TRA copy: https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf); Tax Administration Act, Cap 438 (https://tanzlii.org/akn/tz/act/2015/10); NSSF Act, Cap 50 (https://tanzlii.org/akn/tz/act/1997/28); PSSSF Act 2018 (https://tanzlii.org/akn/tz/act/2018/2); Workers Compensation Act, Cap 263 (https://tanzlii.org/akn/tz/act/2008/20); GN 605A/2025 (https://tanzlii.org/akn/tz/act/gn/2025/605a); TRA pages "Pay As You Earn" (https://tra.go.tz/page/pay-as-you-earn), "Income Tax for Individuals" (https://www.tra.go.tz/page/income-tax-for-individuals), "Skills Development Levy (SDL)" (https://www.tra.go.tz/page/skills-development-levy-sdl) and "Interest, Penalties & Offences" (https://www.tra.go.tz/page/interest-penalties-offences), and TRA's "Taxes and Duties at a Glance 2025/2026" (https://www.tra.go.tz/images/uploads/pages/TAXES_AND_DUTIES_AT_A_GLANCE_2025_2026.pdf); NSSF, "Rate of Contributions" (https://www.nssf.go.tz/pages/rate-of-contributions); WCF, "Michango" (https://www.wcf.go.tz/pages/contribution).

## Section 20 -- Test Suite

Each test recomputes end-to-end. Expected values use the 2026 resident PAYE table applied to gross less the employee NSSF share, and 2026 rates
(NSSF 10%/10%).

- **Test 1 - Sub-threshold earner** — Gross TZS 250,000/mo, resident. Expected: PAYE = TZS 0; NSSF employee TZS 25,000; net TZS 225,000.  _(Section 20 -- Test Suite)_
- **Test 2 - 8% band** — Gross TZS 400,000/mo, resident. NSSF employee TZS 40,000; PAYE base 360,000; PAYE TZS 7,200; net TZS 352,800.  _(Section 20 -- Test Suite)_
- **Test 3 - 20% band** — Gross TZS 700,000/mo, resident. NSSF employee TZS 70,000; PAYE base 630,000; PAYE TZS 42,000; net TZS 588,000.  _(Section 20 -- Test Suite)_
- **Test 4 - 30% band** — Gross TZS 1,500,000/mo, resident. NSSF employee TZS 150,000; PAYE base 1,350,000; PAYE TZS 233,000; net TZS 1,117,000.  _(Section 20 -- Test Suite)_
- **Test 5 - Employer cost** — Gross TZS 700,000/mo, ≥ 10 staff. NSSF employer TZS 70,000; SDL TZS 24,500; WCF TZS 3,500; total employer cost TZS 798,000 (burden 14% of gross).  _(Section 20 -- Test Suite)_
- **Test 6 - Non-resident** — TZS 700,000/mo Tanzania-source. PAYE = TZS 105,000 (15% flat, final); net of PAYE TZS 595,000.  _(Section 20 -- Test Suite)_
- **Test 7 - Bracket continuity** — At a monthly PAYE base of 520,000 → PAYE TZS 20,000; at 760,000 → PAYE TZS 68,000; at 1,000,000 → PAYE TZS 128,000 (subtract constants 21,600 / 84,000 / 122,000 / 172,000 tie out).  _(Section 20 -- Test Suite)_
- **Test 8 - SDL threshold guard** — An employer with 9 employees computing SDL is WRONG — SDL applies only at ≥ 10. With ≥ 10 it is 3.5%, never 4%.  _(Section 20 -- Test Suite)_
- **Test 9 - Rate guard** — Applying 9% as the lowest taxed band is WRONG — the lowest taxed band is 8%.  _(Section 20 -- Test Suite)_
- **Test 10 - Minimum-wage refusal** — Asserting a single national minimum wage → REFUSE; minimum wage is sectoral (GN 605A/2025) — request the sub-sector.  _(GN 605A/2025)_

## PROHIBITIONS

- **PAYE withholding obligation** — NEVER skip PAYE withholding for salaried employees — the employer is the legal withholding agent.  _(PROHIBITIONS)_
- **Lowest band rate guard** — NEVER apply the 9% lowest band — the TRA-confirmed lowest taxed band is 8%.  _(PROHIBITIONS)_
- **PAYE base** — NEVER compute PAYE on gross pay — deduct the employee's statutory NSSF or PSSSF contribution first (ITA s.61; TRA).  _(PROHIBITIONS)_
- **Non-resident flat rate rule** — NEVER apply the resident progressive table to a confirmed non-resident — they pay a flat 15% final.  _(PROHIBITIONS)_
- **SDL applicability and rate** — NEVER apply SDL where the employer has fewer than 10 employees, and NEVER use 4% — SDL is 3.5%.  _(PROHIBITIONS)_
- **NSSF employee share cap** — NEVER let the employee NSSF share exceed 10% — the employee share is capped at 10% (total 20%).  _(PROHIBITIONS)_
- **WCF/SDL employer-only** — NEVER treat WCF or SDL as employee deductions — both are employer-only.  _(PROHIBITIONS)_
- **NSSF wage ceiling assumption** — NEVER cap the NSSF base — the NSSF Act's First Schedule applies the contribution to every complete shilling of wages.  _(PROHIBITIONS)_
- **Minimum wage sectoral rule** — NEVER assert a single national minimum wage — it is sectoral under GN 605A/2025; use the sub-sector rate.  _(PROHIBITIONS)_
- **Late-payment interest floating rate** — NEVER quote a fixed late-payment interest percentage — it floats with the Bank of Tanzania discount rate.  _(PROHIBITIONS)_
- **Estimated computation disclaimer requirement** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Tanzanian accountant.  _(PROHIBITIONS)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax practitioner in Tanzania) before implementation.

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
