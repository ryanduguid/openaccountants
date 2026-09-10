---
name: gw-income-tax
description: "Source-cited draft: personal income tax (Imposto Profissional) for Guinea-Bissau (tax year 2025) — rates, thresholds and rules read from the consolidated Código do Imposto Profissional. Unverified; pending local-accountant review."
jurisdiction: GW
tax_year: 2025
tax_year_notes: "Rates are those of Artigo 27º as given the wording of Lei nº 1/2021, art. 10º, in the DGCI's consolidated text (updated to 31-01-2021, with the LGT of 2022). Confirm against any later Lei do Orçamento before applying to a year after 2025."
last_updated: 2026-09-10
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guinea-Bissau Personal Income Tax — Imposto Profissional

> **This guide previously called the tax "IRPS — Imposto sobre o Rendimento das
> Pessoas Singulares" and cited an "IRPS statute" nine times. Guinea-Bissau has
> no such tax.** "IRPS" does not appear anywhere in the tax authority's own
> consolidated legislation. Personal income from work is taxed by the **Imposto
> Profissional**, whose Código was approved by **Decreto nº 23/83 de 6 de
> Agosto**; business profit is taxed separately by the **Contribuição
> Industrial**. IRPS is the name used in Cabo Verde, Mozambique and São Tomé,
> and it was applied to Guinea-Bissau by analogy. The rate bands below survived
> the reading unchanged — the error was in what the tax is called, what statute
> was cited for it, and, more seriously, the rules for applying it.

## 1. Scope

The Imposto Profissional taxes income from work in a single cédula, taxing
employees and public servants alike (Decreto nº 23/83, preamble (a)). Business
and industrial profit is outside it and falls under the **Código da Contribuição
Industrial** — see `gw-corporate-income-tax`.

## 2. Rates — Artigo 27º

- **The rates are MARGINAL, and the guide previously did not say so** — Art. 27º
  nº 3 states in terms that the percentages in column B *"representam **taxas
  marginais**, sendo cada uma delas válida dentro dos limites do correspondente
  escalão do rendimento"*, and art. 28º repeats it: *"As taxas previstas no
  artigo anterior aplicam-se apenas ao rendimento que excede o escalão máximo
  tributado pela taxa anterior."* A reader who applied the top 20% to a whole
  salary would overstate the tax several times over. The **parcela a abater**
  columns are the statutory shortcut for that computation — tax = rate × income
  − parcela a abater — and they reproduce it exactly at **seven of the eight**
  band boundaries. The eighth is the subject of the warning below  _(Código do Imposto Profissional, arts. 27º nº 3 and 28º — https://kontaktu.mef.gw/legislation)_

- **Employee schedule (trabalhadores por conta de outrem)** — Nine bands, given
  monthly and annually, with the deduction to abate at each step. There is **no
  0% band**: the first XOF of income is taxed at 1%  _(Código do Imposto Profissional, art. 27º nº 1, wording given by Lei nº 1/2021, art. 10º — https://kontaktu.mef.gw/legislation)_

| Monthly (XOF) | Annual (XOF) | Rate | Parcela a abater — monthly | Parcela a abater — annual |
| --- | --- | :---: | ---: | ---: |
| 0 – 41,667 | 0 – 500,004 | **1%** | 0 | 0 |
| 41,668 – 83,333 | 500,016 – 999,996 | **6%** | 2,083 | 24,996 |
| 83,334 – 208,333 | 1,000,008 – 2,499,996 | **8%** | 3,750 | 45,000 |
| 208,334 – 300,000 | 2,500,008 – 3,600,000 | **10%** | 7,917 | 95,004 |
| 300,001 – 400,500 | 3,600,012 – 4,806,000 | **12%** | 13,917 | 167,004 |
| 400,501 – 750,000 | 4,806,012 – 9,000,000 | **14%** | 37,947 | 455,364 |
| 750,001 – 1,100,000 | 9,000,012 – 13,200,000 | **16%** | 52,947 | 635,364 |
| 1,100,001 – 1,500,000 | 13,200,012 – 18,000,000 | **18%** | 74,947 | 899,364 |
| Above 1,500,000 | Above 18,000,000 | **20%** | 104,947 | 1,259,363 |

> **AUDIT FLASH POINT — the parcela a abater for band 6 is the one that belongs
> to a rate that no longer applies, and tax FALLS as income rises through XOF
> 400,501.**
>
> Testing tax = rate × income − parcela at every boundary, the two methods agree
> to within rounding at seven of eight. At the fifth-to-sixth boundary they do
> not:
>
> | | monthly | annual |
> | --- | ---: | ---: |
> | band 5 at its top (12%, parcela 13,917 / 167,004) | 34,143 | 409,716 |
> | band 6 at its start **at the current 14%** (parcela 37,947 / 455,364) | **18,123** | **217,478** |
> | band 6 at its start **at the superseded 18%** | 34,143 | 409,718 |
>
> The parcela reproduces continuity **exactly at 18%** — the rate this band
> carried under Lei nº 8/2020 — and not at the 14% substituted by Lei nº 1/2021,
> art. 10º. On its face the rate was cut and the parcela derived for the old
> rate was left in place, so a taxpayer who earns one franc more than XOF
> 400,500 a month pays **16,020 a month less** if the parcela is applied
> literally. Computing marginally from the bands instead (art. 28º) gives 34,143
> and no cliff.
>
> [RESEARCH GAP — reviewer to confirm with the DGCI which method governs, and
> whether a later Lei do Orçamento has restated the parcela for band 6. Do not
> quietly "correct" the published figure to 21,927: that is the value continuity
> would require, not a value the statute states.]  _(Código do Imposto Profissional, art. 27º nº 1 (Lei nº 1/2021 art. 10º) against art. 27º nº 1 as worded by Lei nº 8/2020 art. 17º — https://kontaktu.mef.gw/legislation)_
- **Self-employed and copyright income are on a DIFFERENT schedule** — Three
  bands, not nine, and the first band starts at 10% where an employee's starts
  at 1%. This is the single largest omission in the previous version, which
  presented the employee table as the personal income tax: a self-employed
  person on XOF 3,000,000 a year is in a 20% marginal band here, against 10% if
  the employee table were read across  _(Código do Imposto Profissional, art. 27º nº 2, wording given by Lei nº 8/2020, art. 17º and Lei nº 1/2021, art. 17º — https://kontaktu.mef.gw/legislation)_

| Monthly (XOF) | Annual (XOF) | Rate | Parcela a abater — monthly | Parcela a abater — annual |
| --- | --- | :---: | ---: | ---: |
| 0 – 183,333 | 0 – 2,199,996 | **10%** | 0 | 0 |
| 183,334 – 833,333 | 2,199,997 – 9,999,996 | **20%** | 18,333 | 220,000 |
| Above 833,333 | Above 9,999,996 | **25%** | 60,000 | 720,000 |

- **Occasional income of residents — 10%** — A flat rate on *rendimentos
  ocasionais*, outside both schedules above  _(Código do Imposto Profissional, art. 27º nº 4, wording given by Lei nº 2/2018 art. 9º, Lei nº 8/2020 art. 17º and Lei nº 1/2021 art. 17º — https://kontaktu.mef.gw/legislation)_
- **A superseded schedule circulates and should be recognised** — The wording
  given by **Lei nº 8/2020** ran 1 / 6 / 8 / 10 / 12 / **18 / 20 / 22 / 24**
  per cent over the same nine bands. It is struck through in the consolidated
  text. A source quoting 24% at the top is quoting the repealed version, not a
  different reading of the current one  _(Código do Imposto Profissional, art. 27º nº 1 as superseded — https://kontaktu.mef.gw/legislation)_

## 3. Exclusions and deductions

- **Pensions of XOF 200,000 a month or less are exempt** — Retirement and
  old-age pensions at or below that figure are outside the charge  _(Código do Imposto Profissional, art. 2º — https://kontaktu.mef.gw/legislation)_
- **Meal subsidies** — Excluded to the extent they do not exceed by more than
  50% the amount set in law, or, where none is set, the limits of reasonableness  _(Código do Imposto Profissional, art. 1º(b) — https://kontaktu.mef.gw/legislation)_
- **Cap on in-kind and similar prestações** — Together they may not exceed 30%
  of the worker's gross income  _(Código do Imposto Profissional, art. 1º nº 4 — https://kontaktu.mef.gw/legislation)_
- **Employee INPS contribution (8%) is deductible** in computing taxable
  employment income  _(Instituto Nacional de Previdência Social contribution rules (as described at [remotesolutionsafrica.com](https://remotesolutionsafrica.com/payroll-compliance-in-guinea-bissau-understanding-iur-irps-inps-and-nif-requirements/)) — not yet confirmed against the Código do Imposto Profissional)_
- **Two 10% caps on professional deductions** — The deduction at art. 13º nº 1(h)
  may not exceed 10% of the gross income of the activity, and those at (g) and (l)
  together are subject to the same 10% ceiling. Vehicle deductions are halved
  where the vehicle is used in the professional activity  _(Código do Imposto Profissional, art. 13º nos 4–6 — https://kontaktu.mef.gw/legislation)_

## 4. Withholding, payment and assessment

- **Employers withhold at source** — The entities named in art. 5º deduct the
  Imposto Profissional from every remuneration paid, including occasional
  remuneration  _(Código do Imposto Profissional, art. 18º — https://kontaktu.mef.gw/legislation)_
- **Remittance: within 10 days of month end** — The employer pays the withheld
  tax over by *guia* processed in triplicate, in the 10 days following the end
  of the month to which it relates. The previous version of this guide gave no
  remittance deadline at all  _(Código do Imposto Profissional, art. 29º — https://kontaktu.mef.gw/legislation)_
- **Payments on account** — Each payment on account is 25% of the last tax
  assessed at the start of the months concerned  _(Código do Imposto Profissional, art. 31º-A nº 2, added by Decreto nº 32/93 art. 2º — https://kontaktu.mef.gw/legislation)_
- **De minimis on assessment — XOF 2,000** — No assessment, corrective
  assessment or official annulment is made for an amount below XOF 2,000  _(Código do Imposto Profissional, art. 23º, wording given by Lei nº 3/2015 art. 13º — https://kontaktu.mef.gw/legislation)_
- **Annual return deadline** — 31 March of the year following the tax year
  ((approx — confirm; this figure is not in the Código do Imposto Profissional
  as consolidated and is carried from a secondary source))  _(Código Geral Tributário (as described at [taxatlas.io](https://taxatlas.io/country/guinea-bissau)))_
- **Individual residence test** — Habitual residence in Guinea-Bissau, or
  presence exceeding 183 days in the tax year ((approx — confirm; not located in
  the consolidated Código do Imposto Profissional, which defines the charge by
  the place the activity is exercised rather than by a day count))  _(Código Geral Tributário — https://kontaktu.mef.gw/legislation)_
- **Non-residents** — Taxed on Guinea-Bissau-source income, commonly by final
  withholding ((approx — confirm))  _(Código Geral Tributário — https://kontaktu.mef.gw/legislation)_

## 5. Penalties

- **Late or missing declarations** — Fine of XOF 50,000 to 300,000 for failure
  to file the declarations required by arts. 7º, 10º-A and 11º, or the fichas
  required by art. 5º  _(Código do Imposto Profissional, art. 37º, wording given by Lei nº 3/2015 art. 13º — https://kontaktu.mef.gw/legislation)_
- **Refusing to produce records** — XOF 100,000 to 300,000  _(Código do Imposto Profissional, art. 37º nº 3 — https://kontaktu.mef.gw/legislation)_
- **Any infraction not specifically provided for** — XOF 25,000 to 100,000  _(Código do Imposto Profissional, art. 37º nº 4 — https://kontaktu.mef.gw/legislation)_

## 6. What this replaces

| The guide said | The Código says |
| --- | --- |
| "IRPS — Imposto sobre o Rendimento das Pessoas Singulares", cited 9× | **Imposto Profissional**, Decreto nº 23/83; "IRPS" appears nowhere in Guinea-Bissau's consolidated tax legislation |
| Nine bands, 1%–20%, each "(approx — confirm)" | The same nine bands and rates — **correct**, and now sourced to art. 27º nº 1 as worded by Lei nº 1/2021 art. 10º |
| No statement of how the bands apply | **Marginal** rates (arts. 27º nº 3 and 28º), with a *parcela a abater* per band |
| One schedule, presented as the personal income tax | **Two** schedules: employees (9 bands from 1%) and self-employed / copyright (3 bands from 10%), plus 10% on occasional income |
| "some sources cite a 0% first band" | There is **no 0% band**; 1% applies from the first XOF |
| No remittance deadline | **10 days** after month end, by *guia* in triplicate (art. 29º) |
| Bands given with no *parcela a abater* | Both parcela columns reproduced — and the band-6 figure shown to be the one that fits the **superseded** 18%, not the current 14% |
| No pension rule | Pensions **≤ XOF 200,000/month exempt** |

Every figure above except those still marked "(approx — confirm)" was read from
the Direcção Geral das Contribuições e Impostos' own consolidated text, in which
superseded wording is struck through and each amending law is named in-line.

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
