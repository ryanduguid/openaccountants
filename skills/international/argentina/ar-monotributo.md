---
name: ar-monotributo
description: Use this skill whenever asked about the Argentine Monotributo simplified tax regime. Trigger on phrases like "monotributo", "regimen simplificado", "AFIP", "DAS monotributo", "categorias monotributo", "impuesto integrado", "monotributista", or any question about the unified monthly payment, category thresholds, or obligations for small self-employed individuals in Argentina. Covers the unified monthly payment (impuesto integrado + aportes jubilatorios + obra social), revenue-based categories (A through K), and exclusion rules. ALWAYS read this skill before touching any Argentine Monotributo work.
version: 2.0
jurisdiction: AR
tax_year: 2026
last_updated: 2026-10-31
reviewed_by: Maria Valeria Benvenuti
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AR Monotributo

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Argentina |
| Tax | Monotributo unified payment (impuesto integrado + SIPA pension + obra social) |
| Currency | ARS only |
| Tax year | Calendar year |
| Primary legislation | Ley 24.977 (Monotributo, Regimen Simplificado para Pequenos Contribuyentes), as amended |
| Supporting legislation | RG AFIP; Decreto reglamentario |
| Tax authority | Administracion Federal de Ingresos Publicos (AFIP) / ARCA |
| Filing portal | Monotributo portal via AFIP web (afip.gob.ar) |
| Filing deadline | Monthly DAS by the 20th; recategorization by February 5 and August 5 (ARCA, Recategorización) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by an Argentine contador publico |
| Skill version | 2.0 |

### Categories and Monthly Amounts (values from 1 August 2026)

**Categories and Monthly Amounts (values from 1 August 2026)**  _(ARCA, Montos y categorías vigentes, https://www.afip.gob.ar/monotributo/categorias.asp, opened 31 October 2026)_

| Cat. | Max Annual Revenue (ARS) | Max Area | Max Annual Energy | Max Annual Rent (ARS) | Impuesto Integrado, Services (ARS/month) | Impuesto Integrado, Goods (ARS/month) | Aportes SIPA (ARS/month) | Obra Social (ARS/month) | Total, Services (ARS/month) | Total, Goods (ARS/month) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 12,009,410.45 | 30 m2 | 3,330 kW | 2,792,886.15 | 5,585.77 | 5,585.77 | 18,246.86 | 25,694.55 | 49,527.18 | 49,527.18 |
| B | 17,595,182.74 | 45 m2 | 5,000 kW | 2,792,886.15 | 10,612.98 | 10,612.98 | 20,071.55 | 25,694.55 | 56,379.08 | 56,379.08 |
| C | 24,670,494.31 | 60 m2 | 6,700 kW | 3,816,944.41 | 18,246.86 | 16,757.32 | 22,078.71 | 25,694.55 | 66,020.12 | 64,530.58 |
| D | 30,628,651.43 | 85 m2 | 10,000 kW | 3,816,944.41 | 29,790.79 | 27,742.67 | 24,286.58 | 30,535.56 | 84,612.93 | 82,564.81 |
| E | 36,028,231.33 | 110 m2 | 13,000 kW | 4,841,002.66 | 55,857.73 | 44,313.79 | 26,715.24 | 37,238.48 | 119,811.45 | 108,267.51 |
| F | 45,151,659.41 | 150 m2 | 16,500 kW | 4,841,002.66 | 78,573.20 | 57,719.64 | 29,386.76 | 42,824.25 | 150,784.21 | 129,930.65 |
| G | 53,995,798.87 | 200 m2 | 20,000 kW | 5,771,964.69 | 142,995.76 | 71,497.87 | 41,141.46 | 46,175.72 | 230,312.94 | 158,815.05 |
| H | 81,924,660.37 | 200 m2 | 20,000 kW | 8,378,658.45 | 409,623.31 | 204,811.64 | 57,598.04 | 55,485.33 | 522,706.68 | 317,895.01 |
| I | 91,699,761.90 | 200 m2 | 20,000 kW | 8,378,658.45 | 814,591.79 | 325,836.71 | 80,637.26 | 68,518.81 | 963,747.86 | 474,992.78 |
| J | 105,012,519.20 | 200 m2 | 20,000 kW | 8,378,658.45 | 977,510.14 | 391,004.07 | 112,892.16 | 76,897.46 | 1,167,299.76 | 580,793.69 |
| K | 126,610,838.75 | 200 m2 | 20,000 kW | 8,378,658.45 | 1,368,514.20 | 456,171.40 | 158,049.02 | 87,882.82 | 1,614,446.04 | 702,103.24 |

Services and goods share these categories. Ley 27.743 replaced Arts. 8, 11 and 20 of the Ley 24.977 annex: all activities now run from A to K, and exclusion for revenue applies above Category K, not above Category H for services.  _(Ley 27.743, Arts. 87-89, https://servicios.infoleg.gob.ar/infolegInternet/anexos/400000-404999/401268/norma.htm)_

Maximum unit price for sales of goods: ARS 716,840.77 in every category. The obra social amount is per affiliate; each adherent adds the same amount.  _(ARCA, Montos y categorías vigentes)_

The statute adjusts these amounts semi-annually, and recategorization falls in February and August. These are the values ARCA showed on 31 October 2026, in force from 1 August 2026: confirm the current table before relying on any figure.  _(Ley 27.743; ARCA, Recategorización)_

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown activity type | Services (same revenue ceilings; equal or higher monthly payment than goods in every category) |
| Unknown category | Highest category that fits revenue (highest payment) |
| Unknown obra social election | Enrolled |
| Unknown unit price limit | Assume limit applies |
| Unknown employee count | Zero |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- gross revenue for the last 12 months, activity type (services vs goods), and current Monotributo category.

**Recommended** -- commercial premises area, electricity consumption, annual rent paid, unit price of goods, number of employees, obra social enrollment status, prior recategorization history.

**Ideal** -- AFIP portal data export, complete electronic invoice register (Factura C), bank statements for the 12-month rolling period.

### Refusal Catalogue

- **R-AR-1 -- Regimen General** — Revenue exceeds the maximum Monotributo threshold. Client must be in the Regimen General (IVA + Ganancias). This skill does not cover the general regime.
- **R-AR-2 -- Sociedades** — Companies (SRL, SA, SAS) file under different regimes. This skill covers individual Monotributistas only.
- **R-AR-3 -- Exclusion transition planning** — Transition from Monotributo to Regimen General involves retroactive effects and complex planning. Escalate to contador publico.
- **R-AR-4 -- Foreign income with CEPO** — Foreign exchange regulations (CEPO) affecting receipt of foreign-source income require specialist analysis. Escalate.

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns (Credits on Bank Statement)**

| Pattern | Tax Label | Treatment | Notes |
| --- | --- | --- | --- |
| CLIENT PAYMENT, TRANSFERENCIA | Monotributo revenue | Include in 12-month rolling revenue | Core income |
| MERCADO PAGO, MP COBRO | Monotributo revenue | Include | Platform receipts |
| FACTURA C COBRO | Monotributo revenue | Include | Invoice collection |
| EXPORTACION SERVICIOS, FACTURA E | Monotributo revenue (export) | Include in revenue threshold | Must issue Factura E |
| TRANSFERENCIA PROPIA, AHORRO | EXCLUDE | Internal transfer | Between own accounts |
| DEVOLUCION, REINTEGRO | Check | May reduce revenue | Refund -- verify if net or gross |
| SUBSIDIO, PLAN SOCIAL | EXCLUDE | Government transfer | Not Monotributo revenue |
| INTERESES, PLAZO FIJO | EXCLUDE | Financial income | Not Monotributo activity income |

### 3.2 Expense Patterns (Debits on Bank Statement)

**Expense Patterns (Debits on Bank Statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AFIP DAS, MONOTRIBUTO, VEP | Monthly unified payment | Impuesto integrado + SIPA + obra social |
| PAGO FACIL, RAPIPAGO (AFIP) | DAS payment via payment network | Same |
| DEBITO AUTOMATICO AFIP | Automatic DAS deduction | Same |
| INGRESOS BRUTOS, IIBB | Provincial gross receipts tax | Separate obligation -- not covered |
| PERSONAL, SUPERMERCADO, ALQUILER | EXCLUDE | Personal expense |

Monotributo does NOT require expense tracking (no deductions). However, these patterns help identify the DAS payment and operational context:

### 3.3 Platform-Specific Patterns

**Platform-Specific Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MERCADO LIBRE, ML VENTA | Revenue | Goods sale via marketplace |
| PEDIDOS YA, RAPPI | Revenue | Delivery platform income |
| PAYPAL, WISE, PAYONEER | Revenue (foreign) | Must issue Factura E; verify CEPO compliance |
| STRIPE PAYOUT | Revenue (foreign) | Same |

## Section 4 -- Worked Examples

All amounts in these examples use the ARCA table in force from 1 August 2026. Annual costs assume those values hold for 12 months; they are illustrative because ARCA revises the table.

### Example 1 -- Standard Services Freelancer, Category D

**Input:** Freelance consultant, annual revenue ARS 30,000,000, services only. No commercial premises, so area, energy and rent do not apply.

**Computation:**
- Category D (revenue <= 30,628,651.43)
- Monthly payment: ARS 84,612.93 (impuesto integrado 29,790.79 + aportes 24,286.58 + obra social 30,535.56)
- Annual cost: ARS 1,015,355.16

### Example 2 -- Low-Income Category A

**Input:** Freelance tutor, annual revenue ARS 10,000,000. No commercial premises, so area, energy and rent do not apply.

**Computation:**
- Category A (revenue <= 12,009,410.45)
- Monthly payment: ARS 49,527.18
- Annual cost: ARS 594,326.16

### Example 3 -- Goods Seller, Category I

**Input:** Online retailer, annual revenue ARS 90,000,000, premises 80 m2, unit price ARS 50,000.

**Computation:**
- Category I (revenue <= 91,699,761.90, above the Category H ceiling of 81,924,660.37)
- Must verify premises area, electricity, rent are within limits
- Monthly payment: ARS 474,992.78 (impuesto integrado 325,836.71 + aportes 80,637.26 + obra social 68,518.81)

### Example 4 -- Exclusion Trigger

**Input:** Services freelancer, 12-month revenue ARS 130,000,000.

**Classification:**
- Exceeds Category K ceiling (126,610,838.75), which applies to services and goods alike
- EXCLUDED from Monotributo
- Must register for Regimen General (IVA + Ganancias)
- ESCALATE to contador publico

### Example 5 -- Recategorization Needed

**Input:** Currently Category B. Trailing 12-month revenue = ARS 20,000,000. No commercial premises, so area, energy and rent do not apply.

**Computation:**
- Exceeds Category B (17,595,182.74) but within Category C (24,670,494.31)
- Must recategorize to C at next semi-annual window
- New monthly payment (services): ARS 66,020.12

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Monotributo Structure

- **Monotributo structure** — The Monotributo is a unified monthly payment replacing income tax (Ganancias), VAT (IVA), pension contributions (SIPA), and health coverage (obra social) with a single fixed monthly amount determined by category.  _(Ley 24.977, Art. 6-11)_

### 5.2 Category Determination

- **Category determination** — Category is determined by the highest of: (a) gross revenue in the last 12 months, (b) commercial premises area, (c) electricity consumption, (d) rent paid. These parameters apply to services and goods alike where the activity is carried on in premises; a taxpayer without premises disregards area, and area is not considered in cities under 40,000 inhabitants (with some exceptions). Maximum unit price applies to goods only.  _(Ley 24.977 annex, Art. 8, as replaced by Ley 27.743, Art. 87; ARCA, Parámetros)_

### 5.3 Recategorization

- **Recategorization** — Semi-annual recategorization (February and August), up to the 5th of the month, based on the last 12 months of activity. Those whose category stays the same, or with under 6 months of activity, take no action. ARCA may recategorize of its own motion where purchases, expenses or bank credits exceed the category's revenue limit.  _(ARCA, Recategorización, https://www.afip.gob.ar/monotributo/ayuda/recategorizacion.asp, opened 31 October 2026)_

### 5.4 Factura C Requirements

- **Factura C requirements** — Monotributo invoices must be Factura C (no IVA discrimination). Must include: CUIT of issuer, current category letter, description of service/goods, total amount, and CAE from AFIP's online invoicing system. For exports: Factura E.

### 5.5 Physical Parameter Limits

- **Physical parameter limits** — From 1 August 2026: premises area from 30 m2 (Cat A) to 200 m2 (Cat G to K); electricity consumed from 3,330 kW to 20,000 kW; annual rent from ARS 2,792,886.15 (Cat A) to ARS 8,378,658.45 (Cat H to K). Unit price, goods only: max ARS 716,840.77 per unit.  _(Ley 24.977 annex, Art. 8; ARCA, Montos y categorías vigentes)_

### 5.6 Payment and Compliance

- **Payment and compliance** — Payment deadline: 20th of each month. Methods: VEP, debito automatico, Pago Facil/Rapipago. Electronic invoicing is mandatory (Factura C). Annual informativa required for some categories.

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Revenue Approaching Category Ceiling

Freelancer in Category D with 11 months of revenue at ARS 29,500,000 (Category D ceiling from 1 August 2026: ARS 30,628,651.43). If 12-month rolling revenue exceeds Category D ceiling, must recategorize to E at next semi-annual window. If exceeds all ceilings, exclusion applies. Flag for reviewer to monitor and advise.

### 6.2 Mixed Services and Goods

Services and goods now share the same revenue ceilings, so mixed activity no longer changes the ceiling. It affects which impuesto integrado column applies and whether the unit price limit applies. The rule for choosing the column for a mixed taxpayer has not been confirmed at source. Flag for reviewer.

### 6.3 Client Receives Income from Abroad

Foreign-source income IS included in Monotributo revenue thresholds. Client must issue Factura E (exportacion de servicios). Currency conversion at official rate. Flag for reviewer -- foreign exchange regulations (CEPO) may affect receipt of funds.

### 6.4 Voluntary Departure from Monotributo

- **Voluntary departure from Monotributo** — Can voluntarily renounce Monotributo and register for IVA + Ganancias. Effective from the first day of the month following renunciation. Cannot return to Monotributo for 3 years.

## Section 7 -- Excel Working Paper Template

```
ARGENTINA MONOTRIBUTO -- Working Paper
Period: [12-month rolling period]

A. REVENUE DETERMINATION
  A1. Gross revenue (last 12 months)              ___________
  A2. Activity type (services / goods / mixed)     ___________
  A3. Premises area (m2)                           ___________
  A4. Electricity consumption (kW)                 ___________
  A5. Annual rent paid (ARS)                       ___________
  A6. Max unit price of goods (ARS) -- goods only  ___________

B. CATEGORY DETERMINATION
  B1. Revenue-based category                       ___________
  B2. Premises-based category                      ___________
  B3. Final category (highest of B1, B2)           ___________

C. MONTHLY PAYMENT
  C1. Impuesto integrado                           ___________
  C2. Aportes jubilatorios                         ___________
  C3. Obra social                                  ___________
  C4. TOTAL MONTHLY DAS                            ___________

D. ANNUAL COST
  D1. C4 x 12                                     ___________

REVIEWER FLAGS:
  [ ] Revenue verified against AFIP invoicing data?
  [ ] Recategorization window approaching?
  [ ] Physical parameters within limits?
  [ ] Foreign income included in revenue?
  [ ] Approaching exclusion threshold?
```

## Section 8 -- Bank Statement Reading Guide

### Argentine Bank Statement Formats

**Argentine Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| Banco Nacion, Banco Provincia | PDF, CSV | Fecha, Descripcion, Debito, Credito, Saldo |
| Galicia, BBVA, Santander | CSV, PDF | Fecha, Concepto, Importe, Saldo |
| Brubank, Uala, Naranja X | CSV | Fecha, Descripcion, Monto |
| Mercado Pago | CSV, PDF | Fecha, Detalle, Monto |
| Wise, Payoneer | CSV | Date, Description, Amount, Currency |

### Key Argentine Banking Terms

**Key Argentine Banking Terms**

| Term | Classification Hint |
| --- | --- |
| TRANSFERENCIA RECIBIDA | Incoming payment -- likely revenue |
| DEBITO AUTOMATICO | Regular outgoing -- check if DAS |
| COMPRA CON DEBITO | Point-of-sale purchase |
| EXTRACCION ATM | Cash withdrawal |
| PLAZO FIJO | Term deposit interest |
| MERCADO PAGO | Could be income or expense |
| VEP AFIP | Tax payment |

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- ARGENTINA MONOTRIBUTO
1. What is your CUIT?
2. Are you currently registered as Monotributista?
3. What is your current category?
4. Activity type: services, goods, or both?
5. Gross revenue in the last 12 months?
6. Do you have commercial premises? Area in m2?
7. Do you have employees?
8. Are you enrolled in obra social?
9. Do you invoice foreign clients (Factura E)?
10. Date of last recategorization?
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Monotributo structure | Ley 24.977, Art. 6-11 |
| Category table | Ley 24.977 annex, Art. 8, as replaced by Ley 27.743, Art. 87; current values in ARCA, Montos y categorías vigentes |
| Physical parameters | Ley 24.977 annex, Art. 8, as replaced by Ley 27.743, Art. 87 |
| Recategorization | Ley 24.977, Art. 9 |
| Exclusion rules | Ley 24.977 annex, Art. 20-21; Art. 20(a), (b) and (j) as replaced by Ley 27.743, Art. 89 (Category K) |
| Payment deadlines | Ley 24.977, Art. 31 |
| Factura C requirements | RG AFIP facturacion electronica |
| Factura E (exports) | RG AFIP exportacion de servicios |

### Monotributo Social

Monotributo Social is a reduced-cost version for vulnerable populations, cooperatives, and social economy workers. Different eligibility criteria. Reduced or zero impuesto integrado. Verify eligibility with AFIP or social services.

### Late Payment Consequences

Interest accrues on unpaid amounts. After prolonged non-payment, AFIP may suspend the CUIT and the client loses obra social coverage. Must regularize through AFIP's payment plan system (Mis Facilidades).

## PROHIBITIONS

- NEVER allow Monotributo for revenue exceeding the maximum category threshold -- client must be in Regimen General
- NEVER issue Factura A or B from a Monotributo taxpayer -- Monotributo uses Factura C (or E for exports)
- NEVER discriminate IVA on a Monotributo invoice -- IVA is embedded in the unified payment
- NEVER ignore physical parameters where the activity is carried on in premises -- revenue alone is insufficient
- NEVER treat Monotributo amounts as fixed forever -- they are updated semi-annually by AFIP
- NEVER allow a client excluded from Monotributo to continue making Monotributo payments
- NEVER ignore the 3-year lockout when voluntarily leaving Monotributo
- NEVER present calculations as definitive -- always label as estimated and direct client to a contador publico

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico or equivalent licensed practitioner in Argentina) before filing or acting upon.

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
