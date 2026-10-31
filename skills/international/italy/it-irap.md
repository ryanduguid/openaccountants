---
name: it-irap
description: Use this skill whenever asked about Italian IRAP (Imposta Regionale sulle Attività Produttive), including whether a sole trader or self-employed professional owes it. Trigger on phrases like "IRAP", "imposta regionale", "IRAP professionista", "IRAP autonomo", "valore della produzione", "regional production tax Italy", or any question about IRAP obligations in Italy. IRAP is not due from individuals carrying on a business or profession since the 2022 tax period. Covers that scope rule, partnerships and professional associations, the standard 3.9% rate, valore della produzione netta and regional variations. ALWAYS read this skill before touching any Italy IRAP work.
jurisdiction: IT
category: international
tax_year: 2025
last_updated: 2026-10-31
version: 1.1
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IT Irap

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Italy |
| Jurisdiction Code | IT |
| Primary Legislation | D.Lgs. 15 dicembre 1997, n. 446 (IRAP decree) |
| Supporting Legislation | L. 234/2021 art. 1, c. 8 (individuals out of scope from 2022); L. 190/2014 (Legge di Stabilità 2015); D.L. 73/2022 (IRAP reform); annual Legge di Bilancio |
| Tax Authority | Agenzia delle Entrate (national) + Regioni (regional) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Italian commercialista |
| Validation Date | Pending |
| Skill Version | 1.0 |

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

## Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Taxpayer type** [T1] -- individual (lavoratore autonomo or impresa individuale), società di persone, associazione professionale, or società di capitali? Individuals owe no IRAP for 2022 onwards.
2. **Tax period** [T1] -- 2022 onwards, or an earlier period under assessment or refund claim?
3. **Region of activity** [T1] -- rates vary by region
4. **ISA status** [T1] -- determines the acconto split (Step 5)
5. **Gross revenue and deductible IRAP costs** [T1]

**If the taxpayer type is unknown, STOP. IRAP liability depends on it.**

## Step 1: Who Is Subject to IRAP? [T1]

- **Legislation** — D.Lgs. 446/1997, art. 2-3; L. 234/2021 art. 1, c. 8: from the tax period in progress at its entry into force, IRAP 'non è dovuta dalle persone fisiche esercenti attività commerciali ed esercenti arti e professioni'.  _(D.Lgs. 446/1997, art. 2-3; L. 234/2021 art. 1, c. 8)_

### Subject to IRAP

**Subject to IRAP**

| Category | IRAP Applies? |
| --- | --- |
| Imprese individuali (sole proprietors with a business), 2022 onwards | **NO -- not due** |
| Lavoratori autonomi (professionals), with or without employees or organisation, 2022 onwards | **NO -- not due** |
| Regime forfettario taxpayers and contribuenti minimi | **NO -- not due** |
| Società semplici, società in nome collettivo, società in accomandita semplice and equivalents | YES |
| Associazioni tra professionisti (associations of individuals practising a profession together) | YES |
| Società di capitali and enti | YES -- see `it-corporate-income-tax` for companies |

The partnership and association rows follow the IRAP 2026 instructions, section 2.2.1 (the copy read is marked 'BOZZA INTERNET'). **[T2]** An azienda coniugale run as a società is subject under the same section. Treatment of an impresa familiare was not confirmed from the sources read: flag for reviewer.

### The "Autonomous Organisation" Test (Autonoma Organizzazione): tax periods before 2022 only [T2]

For an individual, this test matters only for a period before 2022, such as an open assessment or refund claim. It decides nothing for 2022 onwards. The case below was not reopened in the 2026-10-31 revision.

- **Landmark case** — Corte di Cassazione, Sezioni Unite, sent. 9451/2016 -- A professional (lavoratore autonomo) is subject to IRAP only if they have an "autonomous organisation" of production factors.  _(Corte di Cassazione, Sezioni Unite, sent. 9451/2016)_

**Autonomous Organisation Indicators**

| Indicator | Points Toward IRAP Liability |
| --- | --- |
| Employs staff (dipendenti or collaboratori) | YES -- strong indicator |
| Uses significant capital goods (beni strumentali) beyond minimal/personal tools | YES |
| Has a dedicated office/studio (not home-based) | Weak indicator alone |
| Works purely with personal skills, no employees, minimal equipment | NO -- likely exempt |

**[T2] -- The boundary is fact-specific. If there is any doubt, flag for reviewer. The Cassazione case law is extensive but not perfectly bright-line.**

## Step 2: Standard Rate [T1]

- **Standard Rate** — 3.90%  _(D.Lgs. 446/1997, art. 16)_
- **Regional rate adjustment limits** — Regions may increase or decrease the rate within statutory limits (typically +/- 0.92 percentage points)  _(D.Lgs. 446/1997, art. 16)_

### Regional Rate Variations (2025 -- Selected Regions)

**Regional Rate Variations (2025 -- Selected Regions)**

| Region | Rate | Notes |
| --- | --- | --- |
| Standard (most regions) | 3.90% | Default rate |
| Lombardia | 3.90% | Standard |
| Lazio | 3.90% | Standard (some sectors higher) |
| Campania | 4.82% | Often applies maximum surcharge |
| Calabria | 4.82% | Maximum surcharge |
| Sicilia | 3.90% | Standard |
| Trentino-Alto Adige | 2.98% | Reduced (autonomous region) |
| Friuli-Venezia Giulia | 2.98% | Reduced (autonomous region) |

**[T2] -- Regional rates change annually. Verify the specific region's current rate before computing.**

## Step 3: Tax Base (Valore della Produzione Netta) [T1]

- **Legislation** — D.Lgs. 446/1997, art. 5-5bis  _(D.Lgs. 446/1997, art. 5-5bis)_

### For Società di Persone Carrying On a Business (art. 5-bis)

- **Valore della produzione netta (business partnerships)** — valore_produzione_netta = ricavi (revenue) + variazioni rimanenze (inventory changes) + altri proventi (other operating income) - costi della produzione (production costs) + costo del lavoro (labour costs added back) + interessi passivi (interest added back) + compensi occasionali (occasional compensation added back)  _(D.Lgs. 446/1997, art. 5-5bis)_
- **Key difference from income tax base** — IRAP base is NOT the same as income tax base. Labour costs, interest, and some other items are added back.  _(D.Lgs. 446/1997, art. 5-5bis)_

### For Società Semplici and Professional Associations (art. 8)

- **Valore della produzione netta (professional associations)** — valore_produzione_netta = compensi (fees/revenue) - costi inerenti (deductible costs) + costo del personale (employee costs added back)  _(D.Lgs. 446/1997, art. 5-5bis)_

### Simplified Computation for Small Businesses (Art. 5-bis)

- **Simplified computation option** — Businesses that opt for simplified accounting (contabilità semplificata) can compute IRAP on the difference between revenue and costs as reported for income tax, with specific add-backs.  _(Art. 5-bis)_

### Step 4.1 -- Verify IRAP liability

- **Verify IRAP liability logic** — IF individual AND tax_period >= 2022: IRAP = 0 (not due, L. 234/2021 art. 1, c. 8) ELIF individual AND tax_period < 2022: flag for reviewer ELSE: proceed to calculation

### Step 4.2 -- Compute valore della produzione netta

- **Compute VPN logic** — # For business partnership: vpn = revenue + inventory_changes + other_income - production_costs + labour_costs_addback + interest_addback # For professional association: vpn = fees - deductible_costs + employee_costs_addback

### Step 4.3 -- Apply deductions

- **Apply deductions logic** — # Deduction for employees (deduzione per dipendenti) # Various cuneo fiscale deductions for permanent employees vpn_adjusted = vpn - employee_deductions

### Step 4.4 -- Apply regional rate

- **Apply regional rate logic** — IRAP = vpn_adjusted × regional_rate (typically 3.90%)

### Step 4.5 -- Deductions from IRAP itself

- **Deductions from IRAP itself** — A portion of IRAP attributable to labour costs is deductible from IRPEF/IRES: - 10% of IRAP paid is deductible from income tax base (as per D.L. 201/2011) - Additional deduction for IRAP on employee costs  _(D.L. 201/2011)_

## Step 5: Payment Schedule [T1]

- **Legislation** — D.Lgs. 446/1997, art. 30-31  _(D.Lgs. 446/1997, art. 30-31)_

**Payment Schedule**  _(D.Lgs. 446/1997, art. 30-31)_

| Payment | Deadline |
| --- | --- |
| Saldo (balance for prior year) + 1st acconto (advance for current year) | **30 June** (or 30 July with 0.40% surcharge). ISA taxpayers 2026: 20 July without surcharge, or 20 August with 0.80% _(D.L. 89/2026 art. 6, as cited in the Agenzia delle Entrate calendar)_ |
| 2nd acconto (second advance for current year) | **30 November** |

### Advance Payment (Acconti)

**Advance Payment (Acconti)**

| Method | Amount |
| --- | --- |
| Historical method (metodo storico) | 100% of prior-year IRAP, split 40% (1st) / 60% (2nd); ISA taxpayers 50% / 50% _(D.L. 124/2019 art. 58; D.L. 34/2019 art. 12-quinquies, c. 3-4; IRAP 2026 instructions, section 5.2)_ |
| Forecast method (metodo previsionale) | Based on estimated current-year IRAP |

- **Acconti calculation formula** — Not ISA: 1st_acconto = prior_year_IRAP × 40% (due 30 June) 2nd_acconto = prior_year_IRAP × 60% (due 30 November). ISA taxpayer: 1st_acconto = prior_year_IRAP × 50%, 2nd_acconto = prior_year_IRAP × 50%.
- **Minimum IRAP threshold for advance payments** — Partnerships and associations: EUR 51.65 (If prior-year IRAP <= EUR 51.65: no advance payments required.) Other taxpayers: EUR 20.66.  _(IRAP 2026 instructions, section 5.2)_

## Step 6: IRAP Declaration [T1]

- **Legislation** — D.Lgs. 446/1997, art. 19  _(D.Lgs. 446/1997, art. 19)_

**IRAP Declaration obligations**  _(D.Lgs. 446/1997, art. 19)_

| Obligation | Detail |
| --- | --- |
| Form | Dichiarazione IRAP (filed with income tax return) |
| Deadline | Follows the filer's income-tax return, and the two rules differ. **Individuals and partnerships (Redditi PF/SP):** 31 October of the following year, so 2 November 2026 for FY2025 because 31 October is a Saturday. **Companies (Redditi SC):** the last day of the **10th month** after the tax period closes, which lands on the same 31 October only for a calendar-year company. A company with a non-calendar period counts ten months from its own close |
| Filing | Telematic (via Entratel or Fisconline) |

## Step 7: Tax Deductibility of IRAP [T1]

- **Legislation** — D.L. 201/2011, art. 6  _(D.L. 201/2011, art. 6)_

**Deductions from IRAP**  _(D.L. 201/2011, art. 6)_

| Deduction | Amount |
| --- | --- |
| IRAP on labour costs (cuneo fiscale) | Fully deductible from IRPEF base |
| IRAP on other components | 10% of total IRAP paid is deductible from IRPEF base |
| Regional tax deduction | Applied in the Redditi PF declaration |

## Step 8: Edge Case Registry

### EC1 -- Freelance professional, no employees, minimal equipment [T1]

**Situation:** Avvocato (lawyer) working alone from home with a laptop and phone.
**Resolution:** IRAP not due for 2022 onwards, because the client is an individual (L. 234/2021 art. 1, c. 8). No autonomous organisation analysis is needed.

### EC2 -- Professional with one employee [T1]

**Situation:** Architect practising as an individual with one part-time employee (segretaria).
**Resolution:** IRAP not due for 2022 onwards. Employees do not change this for an individual (L. 234/2021 art. 1, c. 8). An architect practising through an association or società is subject to IRAP.

### EC3 -- Regime forfettario [T1]

**Situation:** Client is under regime forfettario (flat-rate tax regime).
**Resolution:** IRAP not due. No declaration, no payment.

### EC4 -- Sole proprietor with a shop [T1]

**Situation:** Impresa individuale operating a retail shop with two employees.
**Resolution:** IRAP not due for 2022 onwards, because the owner is an individual (L. 234/2021 art. 1, c. 8). The same shop run through an s.n.c. or s.a.s. is subject to IRAP.

### EC5 -- Multiple regions [T2]

**Situation:** Client has business activity in both Lombardia and Campania.
**Resolution:** IRAP must be apportioned between regions based on where value is produced (typically by employee/payroll location). Each region's rate applies to its portion. [T2] -- confirm apportionment methodology.

### EC6 -- IRAP and IRPEF interaction [T1]

**Situation:** Client asks if IRAP reduces income tax.
**Resolution:** 10% of IRAP paid is deductible from IRPEF taxable income. Additionally, the portion of IRAP on employee costs (cuneo fiscale deductions) is fully deductible from IRPEF base.

### EC7 -- First year of activity [T1]

**Situation:** New s.n.c., started in April 2025.
**Resolution:** IRAP applies from the first year of activity (no first-year exemption like CFE in France). Advance payments based on forecast method (no prior year). First payment with saldo by 30 June 2026.

### EC8 -- Cessation mid-year [T1]

**Situation:** Partnership closes its business in August 2025.
**Resolution:** IRAP applies on valore della produzione for the period of activity (Jan-Aug). Final declaration follows the Step 6 deadline; [T2] -- confirm any liquidation rule. No advance payments for the following year.

### EC9 -- Contribuente minimo switching to ordinary [T1]

**Situation:** Individual client was contribuente minimo and switches to ordinary regime in 2022 or later.
**Resolution:** IRAP remains not due, because the client is still an individual.

## Step 9: Test Suite

### Test 1 -- Individual professional, 2025

**Input:** Freelance consultant, individual, tax year 2025, EUR 80,000 fees, EUR 15,000 costs.
**Expected output:** IRAP = EUR 0. Not due (L. 234/2021 art. 1, c. 8), and the result is the same with employees or a studio.

### Test 2 -- Professional association

**Input:** Association of dentists with 2 employees, studio rental, EUR 200,000 fees, EUR 60,000 deductible costs, EUR 40,000 employee costs.
**Expected output:** VPN = EUR 200,000 - EUR 60,000 + EUR 40,000 = EUR 180,000. Less employee deductions (assume EUR 15,000): EUR 165,000. IRAP = EUR 165,000 x 3.90% = EUR 6,435.

### Test 3 -- Business partnership (s.n.c.), standard rate

**Input:** Retail s.n.c., revenue EUR 300,000, production costs EUR 200,000, labour EUR 50,000, interest EUR 5,000. Lombardia.
**Expected output:** VPN = EUR 300,000 - EUR 200,000 + EUR 50,000 + EUR 5,000 = EUR 155,000. Less employee deductions (assume EUR 20,000): EUR 135,000. IRAP = EUR 135,000 x 3.90% = EUR 5,265.

### Test 4 -- Regime forfettario

**Input:** Auto-entrepreneur equivalent, regime forfettario, EUR 50,000 revenue.
**Expected output:** IRAP = EUR 0 (exempt).

### Test 5 -- High-rate region (Campania)

**Input:** Professional association in Campania, VPN EUR 100,000.
**Expected output:** IRAP = EUR 100,000 x 4.82% = EUR 4,820.

### Test 6 -- Advance payments

**Input:** Prior-year IRAP = EUR 8,000.
**Expected output:** Not ISA: 1st acconto (30 June) = EUR 8,000 x 40% = EUR 3,200. 2nd acconto (30 November) = EUR 8,000 x 60% = EUR 4,800. ISA taxpayer: EUR 4,000 and EUR 4,000.

### Test 7 -- Low IRAP, no advances

**Input:** Prior-year IRAP = EUR 40.
**Expected output:** Below EUR 51.65 threshold. No advance payments required. Only saldo due.

## PROHIBITIONS

- NEVER apply IRAP to regime forfettario taxpayers
- NEVER charge IRAP to an individual carrying on a business or profession for 2022 onwards, with or without employees (L. 234/2021 art. 1, c. 8)
- NEVER apply the 40%/60% acconto split without confirming the taxpayer is outside the ISA rule
- NEVER use the income tax base as the IRAP base -- they are different (labour costs and interest are added back for IRAP)
- NEVER apply the standard 3.90% rate without checking the specific region -- rates vary
- NEVER forget the 10% IRAP deduction from IRPEF -- it materially reduces income tax
- NEVER use the autonomous organisation test for a period from 2022 onwards; for an earlier period, examine the factual circumstances (employees, beni strumentali)
- NEVER present IRAP advance payments as optional -- they are mandatory if prior-year IRAP exceeds EUR 51.65
- NEVER ignore the employee cost add-back -- it is a fundamental difference from income tax computation
- NEVER advise on multi-region apportionment without flagging for reviewer

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
