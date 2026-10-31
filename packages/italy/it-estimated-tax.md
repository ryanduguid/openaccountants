---
name: it-estimated-tax
description: Use this skill whenever asked about Italian estimated income tax advance payments (acconti IRPEF) for self-employed individuals, freelancers, or professionisti. Trigger on phrases like "acconti IRPEF", "acconto imposta", "estimated tax Italy", "Italian advance tax", "primo acconto", "secondo acconto", "historical method", "forecast method", "metodo storico", "metodo previsionale", "F24 payment", or any question about advance income tax obligations under the TUIR. Covers the two-instalment schedule (40% by Jun 30 and 60% by Nov 30, or 50% and 50% for ISA taxpayers), historical vs forecast computation methods, the EUR 257.52 threshold (EUR 206 for ISA taxpayers), penalties for shortfall, and F24 payment procedures. ALWAYS read this skill before touching any estimated tax work for Italy.
version: 2.1
jurisdiction: IT
tax_year: 2025
last_updated: 2026-10-31
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IT Estimated Tax

## Section 1 -- Quick reference

**Section 1 quick reference table**

| Field | Value |
| --- | --- |
| Country | Italy |
| Tax | Income tax advance payments (acconti IRPEF / imposta sostitutiva) |
| Primary legislation | D.P.R. 917/1986 (TUIR); D.L. 444/1997 Art. 1; D.P.R. 435/2001 Art. 17; D.L. 124/2019 Art. 58 |
| Supporting legislation | D.Lgs. 241/1997 (F24); D.Lgs. 472/1997 (penalties); D.Lgs. 462/1997 |
| Authority | Agenzia delle Entrate |
| Portal | Agenzia delle Entrate online |
| Currency | EUR only |
| Payment schedule | Two instalments if EUR 257.52 or more: 40% by 30 June + 60% by 30 November. ISA taxpayers: two instalments if above EUR 206: 50% + 50%. Otherwise single instalment by 30 Nov |
| Computation basis | 100% of prior year IRPEF (rigo RN34) -- historical method |
| Minimum threshold | EUR 51.65 triggers obligation; EUR 257.52 (ISA taxpayers: above EUR 206) determines single vs two instalments |
| F24 codes | 4033 (primo acconto IRPEF), 4034 (secondo acconto IRPEF), 1790/1791 (forfettario) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Italian commercialista |
| Validation date | Pending |

**Instalment schedule summary**

| Condition | Schedule |
| --- | --- |
| Acconto above EUR 206, ISA taxpayer | 50% by the first instalment date + 50% by 30 November _(D.L. 124/2019 art. 58; D.L. 34/2019 art. 12-quinquies, c. 3-4)_ |
| Acconto EUR 257.52 or more, other taxpayer | 40% by 30 June + 60% by 30 November _(D.P.R. 435/2001 Art. 17(3))_ |
| Acconto > EUR 51.65 and up to EUR 206 (ISA taxpayer) or below EUR 257.52 (other taxpayer) | 100% by 30 November |
| Acconto <= EUR 51.65 | No advance payment required |

**Who is an ISA taxpayer.** A taxpayer who carries on, as a business or self-employment, an activity with an approved ISA, whether or not the ISA is applied, and declares revenue or fees within the limit in that ISA's approval decree. If those conditions are met, the rule also covers taxpayers in the regime forfettario or regime di vantaggio, those using other flat-rate income rules, those under another ISA exclusion, and partners in entities meeting the conditions. _(Agenzia delle Entrate press release, 12 November 2019, on Risoluzione 93/E; D.L. 124/2019 art. 58; D.L. 34/2019 art. 12-quinquies, c. 3-4; Redditi PF 2026, Fascicolo 1, rigo RN62 and Fascicolo 3, rigo RS430)_ Normattiva shows art. 58 and art. 12-quinquies in force to 31 December 2026. What governs acconti after that date was not confirmed, so recheck before computing a 2027 instalment.

**2026 first instalment date.** ISA taxpayers, those under an ISA exclusion, regime di vantaggio taxpayers and forfettari could pay the saldo and first acconto by 20 July 2026 without surcharge, or by 20 August 2026 with 0.80%. _(D.L. 89/2026 art. 6, as cited in the Agenzia delle Entrate calendar; the decree itself was not read)_ This moves the date only: paying 40% instead of 50% still leaves a shortfall of 10% of the acconto on the first instalment. Other years: check the Agenzia calendar.

**Single-instalment boundary for ISA taxpayers.** A single payment applies when the first instalment would not exceed EUR 103 _(D.P.R. 435/2001 Art. 17(3))_. Rigo RN62 states the same test and puts the ISA first instalment at 50%, so the boundary is EUR 103 / 50% = EUR 206 _(Redditi PF 2026, Fascicolo 1, rigo RN62)_. This figure is derived: RN62 prints only EUR 257.52, which it explains as the 40% case. At exactly EUR 206 the first instalment is EUR 103, which does not exceed the limit, so the payment is single.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Historical vs forecast method | Use historical method (no penalty risk) |
| Regime unclear (ordinario vs forfettario) | Confirm before computing -- different codici tributo |
| ISA status unclear | Confirm before splitting -- determines 40%/60% or 50%/50%; flag for reviewer if unresolved |
| Primo acconto deferral | 0.40% maggiorazione applies for 30-day deferral to 30 July (ISA taxpayers and forfettari 2026: 20 August with 0.80%) |
| Addizionali regionali/comunali | Flag for reviewer -- separate advance obligations may apply |

## Section 2 -- Required inputs and refusal catalogue

- **Required inputs -- Minimum viable** — prior year IRPEF liability from Modello Redditi PF (rigo RN34 "Differenza") OR prior year imposta sostitutiva for regime forfettario, plus ISA status
- **Required inputs -- Recommended** — tax regime confirmation (ordinario vs forfettario), current year estimated income (if forecast method considered), ritenute d'acconto received
- **Required inputs -- Ideal** — complete prior year Modello Redditi PF, F24 payment history, Cassetto Fiscale data
- **Refusal policy if minimum is missing** — HARD STOP for historical method. Without rigo RN34, the historical method cannot be computed. If the client wants to use the forecast method, current year projections are needed -- flag for commercialista.
- **R-IT-ET-1 -- Cross-border income** — Trigger: client has foreign-source income affecting DTAA credit timing. Message: "Cross-border income interactions with Italian acconti are outside this skill."
- **R-IT-ET-2 -- Non-resident advance payments** — Trigger: non-resident client. Message: "Non-resident advance tax obligations have different rules."
- **R-IT-ET-3 -- Addizionali computation** — Trigger: client asks for detailed addizionale regionale/comunale advance computation. Message: "Addizionali advances are separate obligations with municipality-specific rates. Consult a commercialista."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as an IRPEF advance payment.

### 3.1 F24 IRPEF advance debits

**F24 IRPEF advance debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| F24, MODELLO F24, PAGAMENTO F24 | IRPEF acconto | Match with June/November timing and codice tributo |
| AGENZIA ENTRATE, AG ENTRATE | IRPEF acconto | Revenue agency payment |
| ACCONTO IRPEF, PRIMO ACCONTO, SECONDO ACCONTO | IRPEF acconto | Explicit description |
| CODICE 4033 | Primo acconto IRPEF | Specific codice tributo |
| CODICE 4034 | Secondo acconto IRPEF | Specific codice tributo |
| CODICE 1790 | Primo acconto forfettario | Imposta sostitutiva |
| CODICE 1791 | Secondo acconto forfettario | Imposta sostitutiva |

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely payment | Confidence |
| --- | --- | --- |
| 25 June -- 5 July | Primo acconto (40%; ISA taxpayers 50%) | High if F24 reference |
| 15 July -- 25 July 2026 | Primo acconto, ISA taxpayer or forfettario, no surcharge | High if F24 reference |
| 15 August -- 25 August 2026 | Primo acconto, ISA taxpayer or forfettario, deferred | High -- check for 0.80% surcharge |
| 25 July -- 5 August | Primo acconto with maggiorazione (deferred) | High -- check for 0.40% surcharge |
| 25 November -- 5 December | Secondo acconto (60%; ISA taxpayers 50%) | High |

### 3.3 Related but NOT IRPEF acconti

**Related but NOT IRPEF acconti**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IVA, CODICE 6099, LIQUIDAZIONE IVA | EXCLUDE | VAT payment |
| INPS, CONTRIBUTI PREVIDENZIALI | EXCLUDE | Social security contribution |
| CODICE 1001, RITENUTE LAVORO | EXCLUDE | Employee withholding payment |
| IMU, TASI, TARI | EXCLUDE | Property/municipal taxes |
| SALDO IRPEF, CODICE 4001 | Flag for reviewer | Year-end balance, not advance |
| RAVVEDIMENTO | Flag for reviewer | Voluntary regularisation payment |
| ADDIZIONALE REGIONALE, ADDIZIONALE COMUNALE | EXCLUDE | Separate from IRPEF acconti |
| CODICE 1840, CODICE 1841 | EXCLUDE | Cedolare secca acconti, not IRPEF or forfettario |

## Section 4 -- Worked examples

### Example 1 -- Two-instalment, taxpayer not under ISA (historical method)

**Example 1 table**

| Instalment | Due date | Percentage | Amount |
| --- | --- | --- | --- |
| Primo acconto | 30 June 2025 | 40% | EUR 2,000 |
| Secondo acconto | 30 November 2025 | 60% | EUR 3,000 |
| **Total** |  | **100%** | **EUR 5,000** |

Prior year IRPEF (rigo RN34) = EUR 5,000.

### Example 1A -- Two-instalment, ISA taxpayer (historical method, 2026 acconti)

**Example 1A table**

| Instalment | Due date | Percentage | Amount |
| --- | --- | --- | --- |
| Primo acconto | 20 July 2026 | 50% | EUR 2,500 |
| Secondo acconto | 30 November 2026 | 50% | EUR 2,500 |
| **Total** |  | **100%** | **EUR 5,000** |

Prior year IRPEF (rigo RN34, tax year 2025) = EUR 5,000. Paying EUR 2,000 would leave the first instalment EUR 500 short.

### Example 2 -- Single instalment (below EUR 257.52)

**Input:** Prior year IRPEF (rigo RN34) = EUR 200.

**Output:** EUR 200 > EUR 51.65, so acconti are due. EUR 200 is below EUR 257.52, so single instalment: EUR 200 by 30 November.

### Example 3 -- Below minimum threshold

**Input:** Prior year IRPEF (rigo RN34) = EUR 40.

**Output:** EUR 40 <= EUR 51.65. No advance payment required.

### Example 4 -- Regime forfettario, activity with an approved ISA (2026 acconti)

**Example 4 table**

| Instalment | Due date | Codice tributo | Amount |
| --- | --- | --- | --- |
| Primo acconto | 20 July 2026 | 1790 | EUR 750 |
| Secondo acconto | 30 November 2026 | 1791 | EUR 750 |

Prior year imposta sostitutiva (tax year 2025, 5% new activity rate) = EUR 1,500.

### Example 5 -- Primo acconto deferral

**Input:** Client not under ISA cannot pay by 30 June. Defers to 30 July.

**Computation:** 0.40% maggiorazione on EUR 2,000 = EUR 8.00. Total payment by 30 July: EUR 2,008.00.

### Example 6 -- Bank statement classification

**Input line:** `30.06.2025 ; F24 TELEMATICO AGENZIA ENTRATE ; DEBIT ; COD 4033 ANNO 2025 ; -2,000.00 ; EUR`

**Classification:** Primo acconto IRPEF for 2025. Tax payment -- not a deductible business expense.

## Section 5 -- Computation rules

### 5.1 Historical method (metodo storico) -- default

- **Historical method formula** — acconto_base = prior_year_IRPEF (rigo RN34) total_acconto = acconto_base x 100% if isa_taxpayer and total_acconto > 206: primo_acconto = total_acconto x 50% secondo_acconto = total_acconto x 50% elif not isa_taxpayer and total_acconto >= 257.52: primo_acconto = total_acconto x 40% secondo_acconto = total_acconto x 60% elif total_acconto > 51.65: single_instalment = total_acconto (due 30 November) else: no_acconti_due

### 5.2 Forecast method (metodo previsionale) -- flag for reviewer

- **Forecast method formula** — estimated_current_IRPEF = tax_on_estimated_income - detrazioni - ritenute total_acconto = estimated_current_IRPEF x 100%
- **Forecast method risk** — Risk: if forecast underestimates actual IRPEF, a 25% penalty on the shortfall applies (Section 6.1). Always flag for commercialista.

### 5.3 Regime forfettario

- **Regime forfettario computation** — 50%/50% split where the activity has an approved ISA and revenue is within its limit; 40%/60% otherwise. Same deadlines, with the 2026 dates in Section 1. Use codici tributo 1790/1791. Base = prior year imposta sostitutiva, NOT IRPEF. Same thresholds: EUR 51.65, and EUR 206 under the ISA split or EUR 257.52 under the 40%/60% split.  _(Agenzia delle Entrate press release, 12 November 2019, on Risoluzione 93/E; Redditi PF 2026, Fascicolo 1, codici tributo)_

### 5.4 Maggiorazione for deferral

- **Maggiorazione for deferral** — Primo acconto can be deferred by 30 days (to 30 July) with a 0.40% surcharge. Beyond 30 July: ravvedimento operoso applies. ISA taxpayers and forfettari for 2026: 20 August with 0.80% (Section 1).

## Section 6 -- Penalties and interest

### 6.1 Sanzione for insufficient/omitted acconti

**Sanzione table**

| Violation | Base penalty |
| --- | --- |
| Omitted advance payment | 25% of unpaid amount |
| Insufficient advance payment | 25% of shortfall |

For violations from 1 September 2024. The 25% is halved for payment within 90 days, and within 15 days it falls further to one fifteenth of the halved rate per day of delay. _(D.Lgs. 471/1997 art. 13(1); D.Lgs. 87/2024 art. 5(1), as noted in Normattiva)_ Normattiva shows arts. 13 of D.Lgs. 471/1997 and 472/1997 in force to 31 December 2026; recheck for later violations.

### 6.2 Ravvedimento operoso (voluntary regularisation)

**Ravvedimento operoso table**

| Timing | Reduced penalty |
| --- | --- |
| Within 14 days | 0.0833% per day (max 1.17%) |
| Within 30 days | 1.25% (1/10 of 12.5%) |
| Within 90 days | 1.39% (1/9 of 12.5%) |
| Within annual return deadline | 3.125% (1/8 of 25%) |
| After annual return deadline | 3.57% (1/7 of 25%) |
| After a schema d'atto [T2] | 4.17% (1/6 of 25%), only on the conditions in art. 13(1)(b-ter) |

For violations from 1 September 2024. The percentages are computed from the base penalty in Section 6.1 and the fractions in D.Lgs. 472/1997 art. 13(1)(a) to (b-ter); the Agenzia's own table was not read. Ravvedimento is unavailable once the conditions in art. 13(1) are no longer met, such as after a formally notified audit.

- **Legal interest rate 2025** — 2.5% per annum for 2025, subject to MEF decree

### 6.3 Ravvedimento formula

- **Ravvedimento formula** — amount_due = unpaid_tax + (unpaid_tax x reduced_penalty%) + interest interest = unpaid_tax x (legal_rate / 365) x days_late

## Section 7 -- F24 payment procedure

### 7.1 Codici tributo

**Codici tributo table**

| Code | Description |
| --- | --- |
| 4033 | IRPEF -- Primo acconto |
| 4034 | IRPEF -- Secondo acconto |
| 1790 | Imposta sostitutiva forfettario -- Primo acconto |
| 1791 | Imposta sostitutiva forfettario -- Secondo acconto or single instalment |

### 7.2 Filing steps

- **Filing steps** — 1. Access Agenzia delle Entrate portal or use intermediario abilitato 2. Complete Sezione Erario of F24 with codice tributo, anno di riferimento (2025), importo 3. Submit electronically (F24 telematico) -- mandatory for amounts > EUR 1,000 or with compensazioni 4. Retain the ricevuta telematica

### 7.3 Compensazione (offsetting)

- **Compensazione rules** — Tax credits can be offset against acconti via F24. Horizontal compensation for credits > EUR 5,000 requires visto di conformita.

## Section 8 -- Edge cases

No prior year return. No acconti due under historical method. Tax settled entirely with the 2025 return in 2026.

No IRPEF acconti due (prior year was imposta sostitutiva). May still owe imposta sostitutiva acconti if switch happens after primo acconto deadline. Flag for commercialista.

Single instalment by 30 November. Two-instalment split applies only when acconto REACHES EUR 257.52, or for an ISA taxpayer EXCEEDS EUR 206 (Section 1).

Cannot pay by 30 June: defer to 30 July with 0.40% surcharge. Beyond 30 July: ravvedimento operoso. ISA taxpayers and forfettari for 2026: 20 July without surcharge, 20 August with 0.80%.

If forecast method used and actual IRPEF exceeds the forecast, 25% penalty on the shortfall applies (reducible via ravvedimento).

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Prior year IRPEF (rigo RN34) or imposta sostitutiva confirmed
- [ ] Correct threshold applied (EUR 51.65 / EUR 257.52; ISA taxpayers EUR 206)
- [ ] ISA status confirmed and the matching split applied (50%/50% or 40%/60%)
- [ ] Method identified (historical vs forecast) with flag for forecast
- [ ] Correct codici tributo (4033/4034 for IRPEF, 1790/1791 for forfettario)
- [ ] Ravvedimento rates current for the applicable period
- [ ] Regime forfettario vs ordinario correctly distinguished
- [ ] Maggiorazione noted if deferral is relevant
- [ ] Compensazione visto threshold checked
- [ ] Due dates confirmed with weekend/holiday adjustments
- [ ] Output labelled as estimated until commercialista confirms

## Section 10 -- Test suite

### Test 1 -- Two-instalment, not under ISA

**Input:** Prior year IRPEF (RN34) = EUR 5,000. Taxpayer not under ISA.
**Expected:** Primo acconto = EUR 2,000 (30 Jun). Secondo acconto = EUR 3,000 (30 Nov). Total = EUR 5,000.

### Test 1A -- Two-instalment, ISA taxpayer

**Input:** Prior year IRPEF (RN34) = EUR 5,000. ISA taxpayer, 2026 acconti.
**Expected:** Primo acconto = EUR 2,500 (20 Jul 2026). Secondo acconto = EUR 2,500 (30 Nov 2026). Total = EUR 5,000.

### Test 2 -- Single instalment

**Input:** Prior year IRPEF = EUR 200.
**Expected:** Single instalment EUR 200 by 30 November.

### Test 2A -- ISA taxpayer between EUR 206 and EUR 257.52

**Input:** Prior year IRPEF = EUR 240. ISA taxpayer, 2026 acconti.
**Expected:** Primo acconto = EUR 120 (20 Jul 2026). Secondo acconto = EUR 120 (30 Nov 2026).

### Test 3 -- Below minimum

**Input:** Prior year IRPEF = EUR 40.
**Expected:** No acconti due.

### Test 4 -- Forfettario

**Input:** Prior year imposta sostitutiva = EUR 1,500. Activity with an approved ISA, 2026 acconti.
**Expected:** Primo = EUR 750 (code 1790). Secondo = EUR 750 (code 1791).

### Test 5 -- Deferral with maggiorazione

**Input:** Primo acconto EUR 2,000, taxpayer not under ISA, deferred to 30 July.
**Expected:** Maggiorazione = EUR 8.00. Total = EUR 2,008.00.

### Test 6 -- First year

**Input:** First year of activity. No prior return.
**Expected:** No acconti due under historical method.

### Test 7 -- Ravvedimento (30-day late)

**Input:** Secondo acconto EUR 3,000 paid 25 days late.
**Expected:** Penalty = 1.25% x EUR 3,000 = EUR 37.50 (violation from 1 September 2024). Plus interest at legal rate.

## Prohibitions

- NEVER compute acconti without confirming the prior year IRPEF liability (rigo RN34)
- NEVER use forecast method without flagging for commercialista and warning about 25% penalty
- NEVER confuse IRPEF acconti (4033/4034) with imposta sostitutiva acconti (1790/1791)
- NEVER apply the 40%/60% split without confirming the taxpayer is outside the ISA rule
- NEVER ignore the EUR 257.52 threshold (EUR 206 for ISA taxpayers) for single vs two-instalment determination
- NEVER forget the 0.40% maggiorazione when deferring primo acconto to July
- NEVER present acconto amounts as definitive -- advise confirmation with commercialista

## Sources

- [Agenzia delle Entrate, acconti](https://www.agenziaentrate.gov.it/portale/schede/pagamenti/imposte-sui-redditi/cosa-imposte-sui-redditi).
- [D.L. 124/2019 art. 58](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2019-10-26;124~art58!vig=).
- [D.L. 34/2019 art. 12-quinquies](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2019-04-30;34~art12quinquies!vig=).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
