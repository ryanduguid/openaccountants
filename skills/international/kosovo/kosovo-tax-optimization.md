---
name: kosovo-tax-optimization
description: Use this skill whenever asked about reducing tax in Kosovo, tax planning, or legal strategies to minimise tax for a self-employed person or small business in Kosovo. Trigger on phrases like "reduce tax Kosovo", "small business 3% Kosovo", "turnover tax Kosovo", "9% services tax", "sole proprietor vs company Kosovo", "0% dividend Kosovo", "save tax Kosovo", "tax planning Kosovo". This skill covers the small-business simplified turnover tax (3% trade / 9% services, under €30k for companies and €50k for sole proprietors), the 10% CIT option, the 0% dividend extraction, and the disguised-employment red line. ALWAYS read this skill before advising on any Kosovo tax optimisation.
version: 0.2
jurisdiction: XK
tax_year: 2025
last_updated: 2026-10-08
review_status: pending_review
depends_on: []
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kosovo Tax Optimization

## Kosovo Tax Optimization Skill v0.2

**Tier 2 — research-verified. Sources: [Law No. 06/L-105](https://www.atk-ks.org/wp-content/uploads/2019/09/LAW_NO.06_L-105.pdf) on Corporate Income Tax and [Law No. 05/L-028](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) on Personal Income Tax, as published in English by ATK (Tax Administration of Kosovo). Figures must agree with `kosovo-income-tax.md` / `kosovo-social-contributions.md`. NOT yet signed off by a Kosovo tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Kosovo |
| Currency | EUR |
| Headline levers | Small-business simplified turnover tax (3% / 9%, under €30k for companies, €50k for sole proprietors); **0% dividends**; 10% CIT |
| Corporate tax | 10% |
| Dividends | **0%** (exempt) |
| Anti-avoidance | Substance; disguised employment |

- **Country** — Republic of Kosovo
- **Currency** — EUR
- **Headline levers** — Small-business simplified turnover tax (3% / 9%, under €30k for companies, €50k for sole proprietors); **0% dividends**; 10% CIT
- **Corporate tax** — 10%
- **Dividends** — **0%** (exempt)
- **Anti-avoidance** — Substance; disguised employment

> **Kosovo combines a tiny small-business turnover tax with 0% dividends.** Corporate taxpayers under **€30,000** gross, and sole proprietors under **€50,000**, can pay a simplified quarterly turnover tax instead of tax on profit — and dividends are exempt from personal income tax ([Law No. 06/L-105](https://www.atk-ks.org/wp-content/uploads/2019/09/LAW_NO.06_L-105.pdf) arts. 35 and 38(2.1); [Law No. 05/L-028](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) arts. 8(1.26), 33 and 43(2.1)).

## Section 2 -- Small-Business Simplified Regime (under €30,000)

**Small-business simplified regime table**

| Activity | Quarterly turnover tax |
| --- | --- |
| Trade, transport, agriculture | **3%** of gross (min €37.50/quarter) |
| Services, professional, artisanal | **9%** of gross (min €37.50/quarter) |

- **Trade, transport, agriculture** — **3%** of gross (min €37.50/quarter)
- **Services, professional, artisanal** — **9%** of gross (min €37.50/quarter)
- **Eligibility ceiling for simplified regime** — €30,000 of annual gross income for a corporate taxpayer (Law No. 06/L-105 arts. 35(1) and 38(2.1)); €50,000 for a sole proprietor (Law No. 05/L-028 arts. 33(1) and 43(2.1)). The same 3% / 9% rates and €37.50 minimum apply under both laws.
- **Voluntary election of tax on profit** — A small business may elect to keep full books and be taxed on profit instead: 10% CIT for a company (Law No. 06/L-105 arts. 7 and 35(2)), or the graduated 0% / 8% / 10% PIT rates for a sole proprietor (Law No. 05/L-028 arts. 6 and 33(2)). It is beneficial only when real deductible expenses are high, and the choice binds for at least three further tax periods (Law No. 06/L-105 art. 35(3) to (4); Law No. 05/L-028 art. 33(3)). Model both.

## Section 3 -- Above €30,000 & Extraction

- **Above the ceiling** — A company above €30,000 pays 10% CIT on net profit; a sole proprietor above €50,000 pays PIT on net profit at the graduated rates (per `kosovo-income-tax.md`).  _(Law No. 06/L-105 arts. 7 and 35(1); Law No. 05/L-028 arts. 6 and 33(1))_
- **Dividends** — **0%** — exempt from PIT for resident and non-resident recipients, so profit extracts tax-free once CIT is paid  _(Law No. 05/L-028 art. 8(1.26))_
- **Interest** — 10% withholding  _(Law No. 06/L-105 art. 31(2); Law No. 05/L-028 art. 39(1))_
- **Rent** — 9% withholding  _(Law No. 06/L-105 art. 31(3); Law No. 05/L-028 art. 39(4))_
- **Royalties** — 10% withholding  _(Law No. 06/L-105 art. 31(2); Law No. 05/L-028 art. 39(1))_

## Section 4 -- Red Lines (do not cross)

- **Disguised employment** — Disguised employment: single-client sole proprietor under employer-like control → reclassification. AUDIT FLASH POINT.
- **Entity splitting** — Don't split a business across entities to stay under €30,000 (or €50,000) without substance.
- **9% services rate on gross vs the profit route** — The 9% services rate is on gross — for high-expense services, taxation on profit may be cheaper; don't default to the turnover tax blindly.

## PROHIBITIONS

- **Never present 3% for services** — NEVER present the 3% rate for services — services pay 9% of gross under the simplified regime.
- **Never ignore the ceiling** — NEVER ignore the €30,000 (company) or €50,000 (sole proprietor) ceiling.
- **Never present single-client work as safe self-employment** — NEVER present single-client work as safe self-employment.
- **Never contradict related skill rates** — NEVER contradict the rates in `kosovo-income-tax.md` / `kosovo-social-contributions.md`.
- **Never present optimisation as definitive advice** — NEVER present optimisation as definitive advice — route to a licensed Kosovo tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Kosovo) before acting upon.

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
