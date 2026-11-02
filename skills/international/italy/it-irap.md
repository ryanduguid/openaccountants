---
name: it-irap
description: Use this skill whenever asked about Italian IRAP (Imposta Regionale sulle Attività Produttive), including whether a sole trader or self-employed professional owes it. Trigger on phrases like "IRAP", "imposta regionale", "IRAP professionista", "IRAP autonomo", "valore della produzione", "regional production tax Italy", or any question about IRAP obligations in Italy. IRAP is not due from individuals carrying on a business or profession since the 2022 tax period. Covers that scope rule, partnerships and professional associations, the standard 3.9% rate, valore della produzione netta and regional variations. ALWAYS read this skill before touching any Italy IRAP work.
jurisdiction: IT
category: international
tax_year: 2025
tax_year_notes: "Historical 2025 frontmatter retained. Inherited body mixes 2025 and 2026 assertions; 2026 updates and actual-year eligibility remain subject to the stated source and professional holds."
last_updated: 2026-11-03
version: 1.3
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IT Irap

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.



**Review boundary (1 November 2026):** this revision corrects the income-tax treatment of IRAP deductions. It preserves the earlier individual-liability and payment corrections. Rates, entity-specific bases, the complete amendment chain and actual filing readiness remain pending professional review. Do not calculate a deduction until the payer, period, payment and eligible cost components have been verified.

Retained statements marked unverified require source and professional review before any actual calculation, recommendation, filing or payment. Historical section numbers remain to preserve cross-references. Hypothetical checks below establish arithmetic under supplied assumptions only.

## Scope

This draft produces a bounded IRAP working paper and reviewer brief for the stated taxpayer groups and historical/mixed periods. It is not an actual return.

Historical 2025 frontmatter retained. Inherited body mixes 2025 and 2026 assertions; 2026 updates and actual-year eligibility remain subject to the stated source and professional holds.

### Skill Metadata

**Skill Metadata**

| Field | Value | Source or qualification |
| --- | --- | --- |
| Jurisdiction | Italy | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Jurisdiction Code | IT | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Primary Legislation | D.Lgs. 15 dicembre 1997, n. 446 (IRAP decree) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Supporting Legislation | L. 234/2021 art. 1, c. 8 (individuals out of scope from 2022); L. 190/2014 (Legge di Stabilità 2015); D.L. 73/2022 (IRAP reform); annual Legge di Bilancio | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Tax Authority | Agenzia delle Entrate (national) + Regioni (regional) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Contributor | Open Accountants | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Validated By | Pending -- requires validation by Italian commercialista | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Validation Date | Pending | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Skill Version | 1.3 | unverified: retained statement; scoped source checks below do not qualify this whole row |

### Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

### Step 1: Who Is Subject to IRAP? [T1]

- **Legislation**  -  D.Lgs. 446/1997, art. 2-3; L. 234/2021 art. 1, c. 8: from the tax period in progress at its entry into force, IRAP 'non è dovuta dalle persone fisiche esercenti attività commerciali ed esercenti arti e professioni'.  _(D.Lgs. 446/1997, art. 2-3; L. 234/2021 art. 1, c. 8)_

#### Subject to IRAP

**Subject to IRAP**

| Category | IRAP Applies? | Source or qualification |
| --- | --- | --- |
| Imprese individuali (sole proprietors with a business), 2022 onwards | **NO -- not due** | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Lavoratori autonomi (professionals), with or without employees or organisation, 2022 onwards | **NO -- not due** | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Regime forfettario taxpayers and contribuenti minimi | **NO -- not due** | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Società semplici, società in nome collettivo, società in accomandita semplice and equivalents | YES | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Associazioni tra professionisti (associations of individuals practising a profession together) | YES | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Società di capitali and enti | YES -- see `it-corporate-income-tax` for companies | unverified: retained statement; scoped source checks below do not qualify this whole row |

The partnership and association rows follow the IRAP 2026 instructions, section 2.2.1 (the copy read is marked 'BOZZA INTERNET'). **[T2]** An azienda coniugale run as a società is subject under the same section. Treatment of an impresa familiare was not confirmed from the sources read: flag for reviewer.

#### The "Autonomous Organisation" Test (Autonoma Organizzazione): tax periods before 2022 only [T2]

For an individual, this test matters only for a period before 2022, such as an open assessment or refund claim. It decides nothing for 2022 onwards. The case below was not reopened in the 2026-10-31 revision.

- **Landmark case**  -  Corte di Cassazione, Sezioni Unite, sent. 9451/2016 -- A professional (lavoratore autonomo) is subject to IRAP only if they have an "autonomous organisation" of production factors.  _(Corte di Cassazione, Sezioni Unite, sent. 9451/2016)_

**Autonomous Organisation Indicators**

| Indicator | Points Toward IRAP Liability | Source or qualification |
| --- | --- | --- |
| Employs staff (dipendenti or collaboratori) | YES -- strong indicator | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Uses significant capital goods (beni strumentali) beyond minimal/personal tools | YES | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Has a dedicated office/studio (not home-based) | Weak indicator alone | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Works purely with personal skills, no employees, minimal equipment | NO -- likely exempt | unverified: retained statement; scoped source checks below do not qualify this whole row |

**[T2] -- The boundary is fact-specific. If there is any doubt, flag for reviewer. The Cassazione case law is extensive but not perfectly bright-line.**

## Ask the client first

### Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Taxpayer type** [T1] -- individual (lavoratore autonomo or impresa individuale), società di persone, associazione professionale, or società di capitali? Individuals owe no IRAP for 2022 onwards.
2. **Tax period** [T1] -- 2022 onwards, or an earlier period under assessment or refund claim?
3. **Region of activity** [T1] -- rates vary by region
4. **ISA status** [T1] -- determines the acconto split (Step 5)
5. **Gross revenue and deductible IRAP costs** [T1]

**If the taxpayer type is unknown, STOP. IRAP liability depends on it.**

## The method, step by step

### Step 2: Standard Rate [T1]

- **Standard Rate**  -  3.90%  _(D.Lgs. 446/1997, art. 16)_
- **Regional rate adjustment limits**  -  Regions may increase or decrease the rate within statutory limits (typically +/- 0.92 percentage points)  _(D.Lgs. 446/1997, art. 16)_

#### Regional Rate Variations (2025 -- Selected Regions)

**Regional Rate Variations (2025 -- Selected Regions)**

| Region | Rate | Notes | Source or qualification |
| --- | --- | --- | --- |
| Standard (most regions) | 3.90% | Default rate | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Lombardia | 3.90% | Standard | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Lazio | 3.90% | Standard (some sectors higher) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Campania | 4.82% | Often applies maximum surcharge | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Calabria | 4.82% | Maximum surcharge | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Sicilia | 3.90% | Standard | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Trentino-Alto Adige | 2.98% | Reduced (autonomous region) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Friuli-Venezia Giulia | 2.98% | Reduced (autonomous region) | unverified: retained statement; scoped source checks below do not qualify this whole row |

**[T2] -- Regional rates change annually. Verify the specific region's current rate before computing.**

### Step 3: Tax Base (Valore della Produzione Netta) [T1]

- **Legislation**  -  D.Lgs. 446/1997, art. 5-5bis  _(D.Lgs. 446/1997, art. 5-5bis)_

#### For Società di Persone Carrying On a Business (art. 5-bis)

- **Valore della produzione netta (business partnerships)**  -  valore_produzione_netta = ricavi (revenue) + variazioni rimanenze (inventory changes) + altri proventi (other operating income) - costi della produzione (production costs) + costo del lavoro (labour costs added back) + interessi passivi (interest added back) + compensi occasionali (occasional compensation added back)  _(D.Lgs. 446/1997, art. 5-5bis)_
- **Key difference from income tax base**  -  IRAP base is NOT the same as income tax base. Labour costs, interest, and some other items are added back.  _(D.Lgs. 446/1997, art. 5-5bis)_

#### For Società Semplici and Professional Associations (art. 8)

- **Valore della produzione netta (professional associations)**  -  valore_produzione_netta = compensi (fees/revenue) - costi inerenti (inherent costs, including amortisation) + costo del personale + interessi passivi. The last 2 are added back only if included in costi inerenti, because art. 8 excludes employee costs and passive interest from the deduction.  _(D.Lgs. 446/1997, art. 8)_

#### Simplified Computation for Small Businesses (Art. 5-bis)

- **Simplified computation option**  -  Businesses that opt for simplified accounting (contabilità semplificata) can compute IRAP on the difference between revenue and costs as reported for income tax, with specific add-backs.  _(Art. 5-bis)_

#### Step 4.1 -- Verify IRAP liability

- **Verify IRAP liability logic**  -  IF individual AND tax_period >= 2022: IRAP = 0 (not due, L. 234/2021 art. 1, c. 8) ELIF individual AND tax_period < 2022: flag for reviewer ELSE: proceed to calculation

#### Step 4.2 -- Compute valore della produzione netta

- **Compute VPN logic**  -  # For business partnership: vpn = revenue + inventory_changes + other_income - production_costs + labour_costs_addback + interest_addback # For professional association: vpn = fees - deductible_costs + employee_costs_addback + interest_addback

#### Step 4.3 -- Apply deductions

- **Apply deductions logic**  -  # Deduction for employees (deduzione per dipendenti) # Various cuneo fiscale deductions for permanent employees vpn_adjusted = vpn - employee_deductions

#### Step 4.4 -- Apply regional rate

- **Apply regional rate logic**  -  IRAP = vpn_adjusted × regional_rate (typically 3.90%)

#### Step 4.5 -- IRAP deductions from the income-tax base

These deductions reduce the eligible income-tax base, not IRAP itself and not income tax euro for euro. The labour-related deduction and the 10% deduction have different statutory predicates. Apply Step 7 before using either; neither is a universal deduction for all IRAP payments.

### Step 7: Tax Deductibility of IRAP [T2]

[Article 6(1) of D.L. 185/2008](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2008-11-29;185~art6!vig=) and [Article 2 of D.L. 201/2011](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art2!vig=) provide separate income-tax deductions for IRAP determined under the specified Articles 5, 5-bis, 6, 7 and 8 of D.Lgs. 446/1997.

| Route | Statutory condition and limit | Source or qualification |
| --- | --- | --- |
| Labour-related IRAP | Article 2(1) of D.L. 201/2011 addresses IRAP attributable to the taxable component of employee and assimilated labour costs, net of the specified Article 11 deductions. It applies from the tax period in progress on 31 December 2012. It does not authorise an unconditional deduction of the entire wage bill or every IRAP payment. | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 10% IRAP deduction | Article 6(1) of D.L. 185/2008 concerns the portion notionally attributable to passive interest and similar charges, net of active interest and similar income. The statutory amount is 10% of IRAP under that provision, not a deduction of every 'other component' and not a flat labour-cost deduction. | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Payment and computation | The provisions refer to Article 99(1) TUIR, whose ordinary rule deducts eligible other taxes in the period of payment. The taxpayer's income category, amounts actually paid, statutory IRAP limits and interaction between deductions must be established before a numerical claim. | unverified: retained statement; scoped source checks below do not qualify this whole row |

The complete Article 11 deduction calculation, apportionment, overlapping deductions, refunds, historical payments and return boxes are not qualified here. Do not add the 2 routes automatically or claim the same cost twice. Identify the entity paying IRAP and the income-tax return claiming relief. Individuals carrying on businesses or professions owe no IRAP for 2022 onwards under the scope rule above; that does not decide relief for an earlier payment.

Source period: the cited deduction provisions were read in the versions displayed on 1 November 2026. [Article 99](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art99!vig=2025-12-31) was also read as at 31 December 2025. This does not qualify the replacement-code chain for 2027.

## Boundary and exception table

### Step 8: Edge Case Registry

#### EC1 -- Freelance professional, no employees, minimal equipment [T1]

**Situation:** Avvocato (lawyer) working alone from home with a laptop and phone.
**Resolution:** IRAP not due for 2022 onwards, because the client is an individual (L. 234/2021 art. 1, c. 8). No autonomous organisation analysis is needed.

#### EC2 -- Professional with one employee [T1]

**Situation:** Architect practising as an individual with one part-time employee (segretaria).
**Resolution:** IRAP not due for 2022 onwards. Employees do not change this for an individual (L. 234/2021 art. 1, c. 8). An architect practising through an association or società is subject to IRAP.

#### EC3 -- Regime forfettario [T1]

**Situation:** Client is under regime forfettario (flat-rate tax regime).
**Resolution:** IRAP not due. No declaration, no payment.

#### EC4 -- Sole proprietor with a shop [T1]

**Situation:** Impresa individuale operating a retail shop with two employees.
**Resolution:** IRAP not due for 2022 onwards, because the owner is an individual (L. 234/2021 art. 1, c. 8). The same shop run through an s.n.c. or s.a.s. is subject to IRAP.

#### EC5 -- Multiple regions [T2]

**Situation:** Client has business activity in both Lombardia and Campania.
**Resolution:** IRAP must be apportioned between regions based on where value is produced (typically by employee/payroll location). Each region's rate applies to its portion. [T2] -- confirm apportionment methodology.

#### EC6 -- IRAP and income-tax interaction [T2]

**Situation:** A partnership or professional association asks whether an IRAP payment reduces income tax.
**Resolution:** Identify the payer, period, payment and eligible net labour or interest components under Step 7. Do not apply 10% universally, deduct the full wage bill or add both deductions automatically. Stop the numerical claim until their interaction and the relevant income-tax return treatment are verified.

#### EC7 -- First year of activity [T1]

**Situation:** New s.n.c., started in April 2025.
**Resolution:** IRAP applies from the first year of activity (no first-year exemption like CFE in France). Advance payments based on forecast method (no prior year). First payment with saldo by 30 June 2026.

#### EC8 -- Cessation mid-year [T1]

**Situation:** Partnership closes its business in August 2025.
**Resolution:** IRAP applies on valore della produzione for the period of activity (Jan-Aug). Final declaration follows the Step 6 deadline; [T2] -- confirm any liquidation rule. No advance payments for the following year.

#### EC9 -- Contribuente minimo switching to ordinary [T1]

**Situation:** Individual client was contribuente minimo and switches to ordinary regime in 2022 or later.
**Resolution:** IRAP remains not due, because the client is still an individual.

## Worked cases

### Step 9: Test Suite

#### Test 1 -- Individual professional, 2025

**Input:** Freelance consultant, individual, tax year 2025, EUR 80,000 fees, EUR 15,000 costs.
**Expected output:** IRAP = EUR 0. Not due (L. 234/2021 art. 1, c. 8), and the result is the same with employees or a studio.

#### Test 2 -- Professional association

**Input:** Association of dentists with 2 employees, studio rental, EUR 200,000 fees, EUR 60,000 deductible costs, EUR 40,000 employee costs.
**Expected output:** VPN = EUR 200,000 - EUR 60,000 + EUR 40,000 = EUR 180,000. Less employee deductions (assume EUR 15,000): EUR 165,000. IRAP = EUR 165,000 x 3.90% = EUR 6,435.

#### Test 2A -- Professional association with a loan

**Input:** As Test 2, with EUR 5,000 of loan interest included in the EUR 60,000 deductible costs.
**Expected output:** VPN = EUR 200,000 - EUR 60,000 + EUR 40,000 + EUR 5,000 = EUR 185,000. Less employee deductions (assume EUR 15,000): EUR 170,000. IRAP = EUR 170,000 x 3.90% = EUR 6,630.

#### Test 3 -- Business partnership (s.n.c.), standard rate

**Input:** Retail s.n.c., revenue EUR 300,000, production costs EUR 200,000, labour EUR 50,000, interest EUR 5,000. Lombardia.
**Expected output:** VPN = EUR 300,000 - EUR 200,000 + EUR 50,000 + EUR 5,000 = EUR 155,000. Less employee deductions (assume EUR 20,000): EUR 135,000. IRAP = EUR 135,000 x 3.90% = EUR 5,265.

#### Test 4 -- Regime forfettario

**Input:** Auto-entrepreneur equivalent, regime forfettario, EUR 50,000 revenue.
**Expected output:** IRAP = EUR 0 (exempt).

#### Test 5 -- High-rate region (Campania)

**Input:** Professional association in Campania, VPN EUR 100,000.
**Expected output:** IRAP = EUR 100,000 x 4.82% = EUR 4,820.

#### Test 6 -- Advance payments

**Input:** Prior-year IRAP = EUR 8,000.
**Expected output:** Not ISA: 1st acconto (30 June) = EUR 8,000 x 40% = EUR 3,200. 2nd acconto (30 November) = EUR 8,000 x 60% = EUR 4,800. ISA taxpayer: EUR 4,000 and EUR 4,000.

#### Test 7 -- Low IRAP, no advances

**Input:** Prior-year IRAP = EUR 40.
**Expected output:** Below EUR 51.65 threshold. No advance payments required. Only saldo due.

### Recomputing checks under supplied assumptions

The association comparison retains the stated EUR 15,000 employee deduction and assumed 3.90% rate; inclusion of loan interest in costs is an explicit switch. In Tests 2/2A and this comparison, the EUR 60,000 cost total includes the EUR 40,000 employee costs. In the loan variant, that same EUR 60,000 total also includes EUR 5,000 loan interest; it is not an additional expense. These are hypothetical inputs, not validated regional rates, eligible deductions or an actual assessment. The difference is EUR 195 when the supplied EUR 5,000 interest add-back applies.

The payment decision compares ordinary 40%/60% and ISA 50%/50% splits on the same supplied prior-year IRAP. Establish ISA scope and the actual payment calendar before selecting either route; the first-payment difference is EUR 800. The individual case uses a supplied not-due switch for an individual from 2022, not a model that infers legal status.


```oa-check
name: Association base with and without included loan interest, assumed inputs
inputs:
  fees: 200000
  costs: 60000
  employee_addback: 40000
  employee_deduction: 15000
  interest_addback: 5000
  assumed_rate: 0.039
steps:
  - vpn: fees - costs + employee_addback
  - adjusted: vpn - employee_deduction
  - tax: adjusted * assumed_rate
  - loan_vpn: vpn + interest_addback
  - loan_adjusted: loan_vpn - employee_deduction
  - loan_tax: loan_adjusted * assumed_rate
  - increment: loan_tax - tax
expected:
  vpn: 180000
  adjusted: 165000
  tax: 6435
  loan_vpn: 185000
  loan_adjusted: 170000
  loan_tax: 6630
  increment: 195
```


```oa-check
name: Advance split decision after ISA eligibility has been established
inputs:
  prior_irap: 8000
  ordinary_first_rate: 0.4
  ordinary_second_rate: 0.6
  isa_first_rate: 0.5
  isa_second_rate: 0.5
steps:
  - ordinary_first: prior_irap * ordinary_first_rate
  - ordinary_second: prior_irap * ordinary_second_rate
  - isa_first: prior_irap * isa_first_rate
  - isa_second: prior_irap * isa_second_rate
  - first_payment_difference: isa_first - ordinary_first
expected:
  ordinary_first: 3200
  ordinary_second: 4800
  isa_first: 4000
  isa_second: 4000
  first_payment_difference: 800
```


```oa-check
name: Individual from 2022, not-due route is supplied rather than inferred
inputs:
  hypothetical_base: 80000
  assumed_rate: 0.039
  liability_switch: 0
steps:
  - hypothetical_product: hypothetical_base * assumed_rate
  - irap_due: hypothetical_product * liability_switch
expected:
  hypothetical_product: 3120
  irap_due: 0
```

## When to refuse or refer

### PROHIBITIONS

- NEVER apply IRAP to regime forfettario taxpayers
- NEVER charge IRAP to an individual carrying on a business or profession for 2022 onwards, with or without employees (L. 234/2021 art. 1, c. 8)
- NEVER apply the 40%/60% acconto split without confirming the taxpayer is outside the ISA rule
- NEVER use the income tax base as the IRAP base -- they are different (labour costs and interest are added back for IRAP)
- NEVER apply the standard 3.90% rate without checking the specific region -- rates vary
- NEVER claim an IRAP deduction without identifying the applicable labour or net-interest route, the eligible amount and its income-tax treatment under Step 7
- NEVER use the autonomous organisation test for a period from 2022 onwards; for an earlier period, examine the factual circumstances (employees, beni strumentali)
- NEVER present IRAP advance payments as optional -- they are mandatory if prior-year IRAP exceeds EUR 51.65
- NEVER ignore the employee cost add-back -- it is a fundamental difference from income tax computation
- NEVER advise on multi-region apportionment without flagging for reviewer

## Filing and payment

### Step 5: Payment Schedule [T1]

- **Legislation**  -  D.Lgs. 446/1997, art. 30-31  _(D.Lgs. 446/1997, art. 30-31)_

**Payment Schedule**  _(D.Lgs. 446/1997, art. 30-31)_

| Payment | Deadline | Source or qualification |
| --- | --- | --- |
| Saldo (balance for prior year) + 1st acconto (advance for current year) | **30 June** (or 30 July with 0.40% surcharge). ISA taxpayers 2026: 20 July without surcharge, or 20 August with 0.80% _(D.L. 89/2026 art. 6, as cited in the Agenzia delle Entrate calendar)_ | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 2nd acconto (second advance for current year) | **30 November** | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Advance Payment (Acconti)

**Advance Payment (Acconti)**

| Method | Amount | Source or qualification |
| --- | --- | --- |
| Historical method (metodo storico) | 100% of prior-year IRAP, split 40% (1st) / 60% (2nd); ISA taxpayers 50% / 50% _(D.L. 124/2019 art. 58; D.L. 34/2019 art. 12-quinquies, c. 3-4; IRAP 2026 instructions, section 5.2)_ | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Forecast method (metodo previsionale) | Based on estimated current-year IRAP | unverified: retained statement; scoped source checks below do not qualify this whole row |

- **Acconti calculation formula**  -  Not ISA: 1st_acconto = prior_year_IRAP × 40% (due 30 June) 2nd_acconto = prior_year_IRAP × 60% (due 30 November). ISA taxpayer: 1st_acconto = prior_year_IRAP × 50%, 2nd_acconto = prior_year_IRAP × 50%.
- **Minimum IRAP threshold for advance payments**  -  Partnerships and associations: EUR 51.65 (If prior-year IRAP <= EUR 51.65: no advance payments required.) Other taxpayers: EUR 20.66.  _(IRAP 2026 instructions, section 5.2)_

### Step 6: IRAP Declaration [T1]

- **Legislation**  -  D.Lgs. 446/1997, art. 19  _(D.Lgs. 446/1997, art. 19)_

**IRAP Declaration obligations**  _(D.Lgs. 446/1997, art. 19)_

| Obligation | Detail | Source or qualification |
| --- | --- | --- |
| Form | Dichiarazione IRAP (filed with income tax return) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Deadline | Follows the filer's income-tax return, and the two rules differ. **Individuals and partnerships (Redditi PF/SP):** 31 October of the following year, so 2 November 2026 for FY2025 because 31 October is a Saturday. **Companies (Redditi SC):** the last day of the **10th month** after the tax period closes, which lands on the same 31 October only for a calendar-year company. A company with a non-calendar period counts ten months from its own close | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Filing | Telematic (via Entratel or Fisconline) | unverified: retained statement; scoped source checks below do not qualify this whole row |

## Completion checklist

Confirm payer and period, source-version and legal scope, regional rate, eligible deductions, ISA status and actual deadlines. Reconcile inputs and payments to documents. Present unresolved amounts and return mechanics to the professional; do not mark a filing or payment ready. Preserve the different bases and predicates of the 2 income-tax deduction routes.

## Sources

| Source | URL | Read on | Reading extent and qualification |
| --- | --- | --- | --- |
| DPR 435/2001 Article 17 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:2001-12-07;435~art17!vig= | 2026-11-01 | Historical independent source check; Complete retained article and updates; relative deferral only, not universal actual-date or ISA clearance |
| D.L. 201/2011 Article 2 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art2!vig= | 2026-11-01 | Historical independent source check; Complete retained article and updates; labour-attributable route; Article 11 calculations and interaction held |
| D.L. 185/2008 Article 6 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2008-11-29;185~art6!vig= | 2026-11-01 | Historical independent source check; Complete retained article and updates; separate net-interest route; actual payments and refunds held |
| L. 234/2021 Article 1(8) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2021-12-30;234~art1!vig= | 2026-11-01 | Historical independent source check; Paragraph 8 with header and adjacent bounds only; not whole Article 1 |
| D.Lgs. 446/1997 Article 30 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art30!vig= | 2026-11-01 | Historical independent source check; Complete retained article and updates; regional, monthly and payer-specific qualifications remain |
| D.Lgs. 446/1997 Article 3 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art3!vig= | 2026-11-01 | Historical independent source check; Complete retained article and updates; literal update-70 typo retained; direct L. 234 paragraph 8 checked |
| Agenzia payment calendar | https://www1.agenziaentrate.gov.it/servizi/scadenzario/main.php?chi=3997&come=507&cosa=11521&entroil=30-06-2026&op=4 | Not established in retained evidence | Captured page, reading date not established; Captured administrative lead; exact reading day and full operative extension chain not established |
| TUIR Article 99, historical | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art99!vig=2025-12-31 | 2026-11-01 | Historical independent source check; Complete retained article and update 115 as at 31 December 2025; actual deductible payments held |
| L. 113/2026 Article 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2026-06-25;113~art1!vig= | 2026-11-01 | Historical independent source check; Complete retained article and notes including repeal/savings; conversion annex and later extension chain unread |
| D.L. 89/2026 Article 6, historical | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-05-22;89~art6!vig=2026-05-23 | 2026-11-01 | Historical independent source check; Complete historical article and notes, 23 May-27 June representation only; subsequent operative chain held |
| Inherited Cassazione and IRAP instructions references | unverified: exact official URL not established in this packet | Not established in retained evidence | Cassazione 9451/2016 and the BOZZA INTERNET instructions remain bounded inherited references, not a new full-source reading |

These reading dates identify the historical independent source check of retained text. They do not claim a new reading, original acquisition day, whole-law coverage or current-law verification.

Not yet confirmed: complete historical/current amendment chains and regional rates; all taxpayer-specific bases and Article 11 deductions; the interaction and actual use of income-tax deductions; the full operative 2026 deadline extension chain and return boxes; Cassazione and instruction reading dates; professional review and actual filing readiness.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The upstream project is maintained at [openaccountants.com](https://www.openaccountants.com). This fork's migrated version and recorded review status are maintained in [ryanduguid/openaccountants](https://github.com/ryanduguid/openaccountants); upstream services do not publish or verify this fork's changes.

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
