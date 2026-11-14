---
name: pt-social-contributions
description: Use this skill whenever asked about Portuguese self-employed social contributions (contribuições para a Segurança Social). Trigger on phrases like "Segurança Social trabalhador independente", "Portuguese social contributions", "declaração trimestral SS", "contribuições independente Portugal", or any question about social contribution obligations for a self-employed client in Portugal. Covers the 21.4% rate on 70% of relevant income, quarterly declaration, and first-year exemption. ALWAYS read this skill before touching any Portugal social contributions work.
version: 2.0
jurisdiction: PT
category: international
tax_year: 2025
last_updated: 2026-11-10
reviewed_by: Mário Jorge da costa Vale
review_status: pending_review
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

> This revision includes changes made after the recorded accountant review and awaits a new review.

# PT Social Contributions

## Portugal Social Contributions -- Self-Employed Skill v2.0

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Mário Jorge da costa Vale** on 2026-06-04; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Portugal (Portuguese Republic) |
| Authority | ISS (Instituto da Segurança Social) for contributions; AT (Autoridade Tributária) for tax |
| Primary legislation | Código Contributivo (Lei n.o 110/2009, art. 139-170) |
| Supporting legislation | Decreto Regulamentar 1-A/2011; annual updates via Portaria |
| Self-employed rate | 21.4% |
| Empresário em nome individual rate | 25.2% |
| Relevant income -- services | 70% of gross |
| Relevant income -- goods | 20% of gross |
| Minimum contribution | EUR 20.00/month in 2026 (ISS, Guia Prático 1009 v1.09); the Código updates it with the IAS (art. 163.º n.ºs 2 and 8), so recheck it every January; no minimum base without organized accounting |
| Minimum monthly base, organized accounting only (1.5x IAS) | EUR 783.75 in 2025 (IAS by Portaria n.º 6-B/2025/1); EUR 805.70 in 2026 (IAS by Portaria n.º 480-A/2025/1) |
| Maximum monthly base (12x IAS) | EUR 6,270.00 in 2025; EUR 6,445.56 in 2026 |
| First 12 months | No contributions until the first enquadramento takes effect: 1st day of the 12th month after the month activity started (art. 145.º n.º 1) |
| Declaration frequency | Quarterly |
| Payment frequency | Monthly (between the 10th and 20th of the following month) |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated by | Verified by Mário Jorge da costa Vale (CA - 85883) on 2026-06-04 |
| Validation date | Verified by Mário Jorge da costa Vale (CA - 85883) on 2026-06-04 |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Required inputs before computing** — Before computing, you MUST obtain: 1. Activity type -- trabalhador independente, empresário em nome individual, or profissional liberal? 2. Gross quarterly income (rendimento relevante) -- from the quarterly declaration 3. Year of activity -- first 12 months exempt from contributions 4. Any concurrent employment? -- reduced rate may apply 5. Category of services -- services (prestação de serviços) vs sales of goods (venda de bens)? 6. Does the client have an accountant (contabilidade organizada)? -- affects relevant income calculation. If income type (services vs goods) is unknown, STOP. The relevant income percentage differs.

### Refusal catalogue

- **R-PT-SOC-1 -- Cross-border EU worker** — Trigger: client is a Portuguese resident providing services in another EU state. Message: "Cross-border social insurance requires A1 certificate analysis under EU Regulation 883/2004. Escalate to qualified adviser."
- **R-PT-SOC-2 -- Pensioner reduced rates** — Trigger: self-employed pensioner asks about reduced contribution rate. Message: "Pensioner contribution rates require confirmation with ISS. Flag for reviewer."

### Prohibitions

- **Prohibitions list** — NEVER apply 21.4% to gross income directly -- the relevant income percentage (70% for services, 20% for goods) must be applied first. NEVER forget the first 12 months exemption for new self-employed. NEVER apply a minimum base of one IAS -- without organized accounting there is no minimum base, only the minimum contribution (EUR 20.00 in 2026), which applies even with zero income after the exemption period, unless the prior-year exemption in Section 6 applies. NEVER confuse the self-employed rate (21.4%) with the empresário rate (25.2%). NEVER present quarterly declaration income as the contribution base -- it must be converted to monthly. NEVER forget to clamp at the maximum of 12 x IAS (EUR 6,270.00 in 2025; EUR 6,445.56 in 2026). NEVER state that contributions are NOT tax-deductible -- they ARE deductible from IRS income. NEVER advise on concurrent employment exemption without verifying the 4 x IAS threshold.

## Section 3 -- Relevant income calculation

Legislation: Código Contributivo, art. 162

### Without organized accounting (sem contabilidade organizada)

**Relevant income percentages without organized accounting**

| Income type | Relevant income % |
| --- | --- |
| Prestação de serviços (services) | 70% of gross |
| Produção e venda de bens (goods); hotel, restaurant and similar activities declared as such (art. 162.º n.º 2) | 20% of gross |
| Mixed (services + goods) | Apply each % to respective category |

### With organized accounting (com contabilidade organizada)

- **Relevant income with organized accounting** — Relevant income = taxable profit (lucro tributável) of the prior calendar year (art. 162.º n.º 3).

### Quarterly to monthly conversion

- **Quarterly to monthly conversion formula** — quarterly_relevant_income = sum of relevant_income for the 3 months in the quarter monthly_relevant_income = quarterly_relevant_income / 3

## Section 4 -- Rates, base, and bounds (2025)

Legislation: Código Contributivo, art. 163, 168

### Contribution rates

**Contribution rates**

| Category | Rate |
| --- | --- |
| Trabalhador independente | 21.4% |
| Empresário em nome individual (with employees) | 25.2% |

### Base bounds

**Base bounds**

| Bound | Amount |
| --- | --- |
| Minimum monthly base, organized accounting only (1.5x IAS) | EUR 783.75 (2025); EUR 805.70 (2026) |
| Maximum monthly base (12x IAS) | EUR 6,270.00 (2025); EUR 6,445.56 (2026) |

- **Monthly base formula** — Without organized accounting: monthly_base = min(quarterly_relevant_income / 3, 12 x IAS): min(monthly_relevant_income, 6,270.00) for 2025 and min(monthly_relevant_income, 6,445.56) for 2026. With no income, or a contribution below the minimum (EUR 20.00 in 2026), the base is the one that gives the minimum contribution. With organized accounting: monthly_base = prior-year taxable profit / 12, at least 1.5 x IAS and at most 12 x IAS, fixed in October for the following calendar year (Código Contributivo art. 163.º n.ºs 1, 2, 3 and 5; IAS by Portaria n.º 6-B/2025/1 and Portaria n.º 480-A/2025/1). The bounds are fixed in IAS, so recompute them every January rather than storing the euro amounts.

## Section 5 -- Computation steps

### Step 5.1 -- Quarterly declaration

**Quarterly declaration schedule**

| Declaration period | Income period covered | Filing deadline |
| --- | --- | --- |
| January | Oct--Dec (prior year) | End of January |
| April | Jan--Mar | End of April |
| July | Apr--Jun | End of July |
| October | Jul--Sep | End of October |

### Step 5.2 -- Calculate monthly relevant income

- **Monthly relevant income calculation** — IF services_only (sem contabilidade): relevant_income = quarterly_gross x 70% / 3 ELIF goods_only: relevant_income = quarterly_gross x 20% / 3 ELIF mixed: relevant_income = (services_gross x 70% + goods_gross x 20%) / 3 ELIF contabilidade_organizada: relevant_income = prior_year_taxable_profit / 12

### Step 5.3 -- Apply bounds and calculate

- **Apply bounds and calculate contribution** — Without organized accounting: monthly_base = min(relevant_income, 12 x IAS): min(relevant_income, 6,270.00) for 2025 and min(relevant_income, 6,445.56) for 2026. With organized accounting: monthly_base = max(1.5 x IAS, min(relevant_income, 12 x IAS)): max(783.75, min(relevant_income, 6,270.00)) for 2025 and max(805.70, min(relevant_income, 6,445.56)) for 2026 (IAS by Portaria n.º 6-B/2025/1 and Portaria n.º 480-A/2025/1). monthly_contribution = monthly_base x 21.4%, or the minimum contribution (EUR 20.00 in 2026) if there is no income or that is lower

### Step 5.4 -- When the base takes effect

- **When the base takes effect** — The quarterly declaration sets the base for the month of the declaration and the following 2 months (art. 163.º n.º 1). Each month's contribution is paid between the 10th and 20th of the following month (art. 155.º n.º 2), so the April declaration sets April to June, paid in May to July.
- **Before the first declaration** — From the start of the enquadramento until the first quarterly declaration, the contribution is the minimum (EUR 20.00 in 2026), unless a base is already set for the period (art. 165.º n.ºs 1 and 2). The minimum also applies when a quarterly declaration is not delivered (ISS, Perguntas Frequentes v09).
- **Restart** — The enquadramento takes effect on the 1st day of the month activity restarts (art. 145.º n.º 3). A stop during the first 12 months suspends the count (art. 145.º n.º 4).
- **Early entry** — A client can ask at a January, April, July or October declaration to start before the 12th month. ISS, Perguntas Frequentes v09 and the G1 table of ISS, Guia Prático 1009 v1.09 give the 1st day of the month after filing; the Guia's D1 example gives the 1st day of the filing month. Confirm the month with ISS before stating one.
- **Organized accounting** — No quarterly declaration applies (art. 151.º-A n.º 7) and the base is fixed in October for the following January (art. 163.º n.º 3). The sources read do not say which base applies between the start of the enquadramento and the first October base: flag for reviewer, and do not state a month.

## Section 6 -- Payment schedule, exemptions, and tax deductibility

### Payment schedule

**Payment schedule**

| Obligation | Due date |
| --- | --- |
| Monthly contribution payment | Between 10th and 20th of the month after the one it relates to (art. 155.º n.º 2) |
| Payment method | Direct debit, ATM, or Segurança Social Direta portal |

- **Late payment** — Late payment: interest at legal rate + potential loss of benefits.

### Exemptions

- **First 12 months** — a new self-employed worker owes no contributions until the first enquadramento takes effect, on the 1st day of the 12th month after the month activity started (arts 145.º n.º 1 and 155.º n.º 1).
- **Prior-year minimum** — a worker can be exempt if, in January, it is confirmed that the prior year was paid only at the minimum contribution, because there was no income or the contribution would have been lower (ISS, Guia Prático 1009 v1.09).
- **Concurrent employment exemption** — if the self-employed person also has employment where the employer pays at least the minimum contribution base: If employment income >= IAS: self-employed contributions may be reduced or exempt. If self-employed relevant income >= 4 x IAS (EUR 2,090.00 in 2025; EUR 2,148.52 in 2026): exemption does NOT apply (Código Contributivo art. 157.º n.º 1 a))

### Tax deductibility

**Tax deductibility**

| Question | Answer |
| --- | --- |
| Are Segurança Social contributions deductible? | YES -- from gross income for IRS purposes |
| Classification | Category B deductions |
| When deductible? | In the year they are paid |

## Section 7 -- Organized accounting and recibos verdes

### Self-employed with organized accounting

- **Organized accounting profit rule** — Relevant income = prior-year taxable profit (not deemed %), and the monthly base is 1/12 of it. If that profit is negative or nil, the minimum base of 1.5 x IAS still applies. Once notified of the base, the client can ask for the quarterly regime instead (art. 164.º n.º 3). Confirm profit calculation methodology with contabilista. Flag for reviewer.

### Recibos verdes (green receipts) income

- **Recibos verdes income treatment** — This IS self-employed income. Standard 70% relevant income rule applies. All recibos verdes amounts are reported in the quarterly declaration.

## Section 8 -- Edge case registry

### EC1 -- First year of activity

Situation: Client opened activity in March 2025, first enquadramento, no organized accounting. Resolution: No contributions through February 2026; the enquadramento takes effect on 1 March 2026. First contribution month: March 2026, at the minimum (EUR 20.00), because no declaration has set a base yet; payment due 10--20 April 2026. First quarterly declaration: by 30 April 2026, on January to March income. It sets the base for April, May and June 2026, so the first contribution on that base is April's; payment due 10--20 May 2026.

### EC2 -- Low services income

Situation: Client provides services with quarterly gross EUR 1,000. Resolution: Relevant income = EUR 1,000 x 70% / 3 = EUR 233.33/month. No minimum base applies. Monthly contribution = EUR 233.33 x 21.4% = EUR 49.93.

### EC3 -- Very high income

Situation: Client earns EUR 30,000/quarter from services. Resolution: Relevant income = EUR 7,000/month. Capped at EUR 6,270.00 (2025). Monthly contribution = EUR 6,270.00 x 21.4% = EUR 1,341.78.

### EC4 -- Mixed services and goods

Situation: Client earns EUR 6,000 from services and EUR 15,000 from goods in the quarter. Resolution: Relevant income = (EUR 6,000 x 70% + EUR 15,000 x 20%) / 3 = EUR 2,400/month. Contribution = EUR 2,400 x 21.4% = EUR 513.60.

### EC5 -- Concurrent employment, exemption applies

Situation: Client employed at EUR 1,200/month, self-employed quarterly services EUR 2,000. Resolution: Self-employed relevant income = EUR 466.67/month (below 4 x IAS). Employment exemption applies. Contributions = EUR 0.

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified contabilista certificado must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified contabilista. Document gap.
```

## Section 10 -- Test suite

### Test 1 -- Standard services, mid-range

Input: Quarterly gross services EUR 9,000, no employment, established. Expected output: Relevant income = EUR 2,100/month. Contribution = EUR 449.40/month. Annual: EUR 5,392.80.

### Test 2 -- Low income, no minimum base

Input: Quarterly gross services EUR 1,500. Expected output: Relevant income = EUR 350/month. Base = EUR 350. Contribution = EUR 74.90/month.

### Test 3 -- Maximum base applies

Input: Quarterly gross services EUR 30,000. Expected output: Relevant income = EUR 7,000/month. Capped at EUR 6,270.00 (12 x IAS 2025). Contribution = EUR 1,341.78/month.

### Test 4 -- First year exempt

Input: Activity opened 4 months ago, quarterly gross EUR 12,000. Expected output: Exempt (within first 12 months). Contributions = EUR 0.

### Test 5 -- Goods-only income

Input: Quarterly gross goods sales EUR 20,000, no employment. Expected output: Relevant income = EUR 1,333.33/month. Contribution = EUR 285.33/month.

### Test 6 -- Concurrent employment, exemption applies

Input: Employment salary EUR 1,500/month, self-employed quarterly services EUR 2,000. Expected output: Self-employed relevant income = EUR 466.67/month (below 4 x IAS). Exemption applies. Contributions = EUR 0.

### Test 7 -- Empresário em nome individual

Input: Sole proprietor with employees, quarterly services EUR 15,000. Expected output: Rate = 25.2%. Relevant income = EUR 3,500/month. Contribution = EUR 882.00/month.

### Test 8 -- Minimum contribution

Input: Established in 2026, no organized accounting, no income in the quarter, prior-year exemption not applicable. Expected output: Contribution = EUR 20.00/month.

### Test 9 -- Organized accounting, minimum base

Input: Organized accounting, base set for 2025, prior-year taxable profit EUR 6,000. Expected output: EUR 500/month is below 1.5 x IAS, so base = EUR 783.75. Contribution = EUR 167.72/month.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
