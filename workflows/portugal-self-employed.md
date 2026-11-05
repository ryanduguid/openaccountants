# Portugal Self-Employed Tax Workflow

**MCP prompt name:** `portugal-self-employed`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/PT`

## Trigger phrases

- "self-employed in Portugal"
- "NHR Portugal"
- "IFICI"
- "IRS Portugal"
- "recibos verdes"
- "Portugal freelancer taxes"
- "trabalhador independente"
- "simplified regime Portugal"
- "moving to Portugal taxes"
- "digital nomad Portugal"

## What it produces

- IRS Modelo 3 / Anexo B working paper (simplified or organized accounts regime)
- NHR / IFICI application deadline flag and benefit analysis
- Social contributions computation (Social Security — TSU)
- VAT position (IVA) — threshold, exemption, periodic returns
- Simplified vs organized accounts regime comparison

## Skills to load

From the PT bundle:
- `pt-income-tax` — IRS rates, brackets, Anexo B simplified regime coefficients
- `pt-nhr-ifici` — NHR/IFICI special tax regime rules
- `pt-social-contributions` — TSU self-employed contribution base and rate
- `portugal-vat-return` — IVA exemption threshold, periodic returns

Rates and thresholds in the phases below come from these guides. The hosted bundle does not carry them all: if one is not loaded, fetch it from `packages/portugal/` in this repository before computing, and never fall back on a remembered figure.

## 6-phase structure

### Phase 1 — Intake
Confirm: residency status (Portuguese tax resident?), year of first Portuguese residency, income sources (service, professional, rental, foreign-source), gross revenue, whether NHR/IFICI has been applied for, VAT registration status.

### Phase 2 — NHR/IFICI flag
If newly resident in Portugal: take IFICI (successor to NHR from 2024) eligibility, the application deadline and the rate on qualifying income from `pt-nhr-ifici`. Flag the deadline.

### Phase 3 — IRS computation
Simplified regime: take the coefficient for each income type from `pt-income-tax`. Net income = gross × coefficient. Apply the progressive IRS rates in the same guide. Alternatively: organized accounts regime (actual income − actual expenses), mandatory above the turnover limit in that guide.

### Phase 4 — Social contributions (TSU)
Relevant income is set at each quarterly declaration from income in the 3 preceding months, at the service and goods percentages in `pt-social-contributions`; the monthly base is 1/3 of that amount. Organised accounts instead use the prior year's taxable profit, with their own minimum base (Código Contributivo arts 162.º and 163.º). Take the contribution rate, first-year exemption and maximum base from the guide; the floor outside organised accounts is the minimum contribution in art. 163.º n.º 2.

### Phase 5 — VAT (IVA)
Registration exemption (CIVA art. 53.º): take the turnover threshold and conditions for the year from `portugal-vat-return`. If registered: quarterly or monthly returns; take the standard rate for the mainland, Azores or Madeira from the same guide.

### Phase 6 — Handoff
Recommend review by a Portuguese TOC (Técnico Oficial de Contas). Route to: https://www.openaccountants.com
