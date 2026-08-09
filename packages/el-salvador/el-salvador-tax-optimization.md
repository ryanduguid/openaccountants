---
name: el-salvador-tax-optimization
description: >
  Use this skill whenever asked about reducing tax in El Salvador, tax planning, or legal strategies to minimise tax for a business or self-employed person. Trigger on phrases like "reduce tax El Salvador", "foreign source income exempt", "territorial taxation El Salvador", "tech incentive 15 years", "El Salvador dividends 5%", "free trade zone", "save tax El Salvador", "tax planning El Salvador". This skill covers the foreign-source-income exemption (territorial reform), the 15-year tech (software/AI/cybersecurity) income-tax exemption, dividend treatment, free-trade-zone incentives, and the anti-avoidance red lines. ALWAYS read this skill before advising on any Salvadoran tax optimisation.
version: 0.1
jurisdiction: SV
tier: 2
last_updated: 2026-06-12
category: tax-optimization
depends_on: []
verified_by: pending
---

# El Salvador Tax Optimization Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Tier 2 — research-verified. Sources: Ministerio de Hacienda, PwC El Salvador, EY (2024 ISR reform alert). Figures must agree with `el-salvador-income-tax.md` / `el-salvador-social-contributions.md` / `el-salvador-payroll.md`. NOT yet signed off by a Salvadoran tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Republic of El Salvador |
| Currency | USD |
| Headline levers | **Foreign-source income exemption**; **15-year tech income-tax holiday**; free-trade zones; dividend treatment |
| Dividends | **5%** withholding (25% to tax havens); not re-taxed in the individual's hands if ISR already paid at corporate level |
| Investment income (domestic) | 10% flat |
| Anti-avoidance | Source rules; incentive eligibility; substance |

> **El Salvador's standout levers:** a 2024 reform **exempts foreign-source income** (dividends, capital gains, interest from foreign securities/instruments), and a **15-year income-tax + municipal-tax exemption** for software/AI/cybersecurity/data-analytics businesses.

---

## Section 2 -- Foreign-Source Income Exemption (territorial reform)

- Following the **2024 ISR reform**, **dividends, capital gains, interest and similar income from foreign securities/financial instruments are NOT subject to Salvadoran income tax.** (EY) Major for residents with international portfolios/income. **AUDIT FLASH POINT — confirm the income genuinely qualifies as foreign-source under the reform.**

---

## Section 3 -- Tech & Investment Incentives

| Incentive | Detail |
|---|---|
| Tech sector | Software development, **AI, cybersecurity, data analytics** businesses can get a **15-year income-tax exemption** on profits + 15-year municipal-tax exemption. |
| Free-trade zones | New qualifying investments can have **tax-free dividend distributions for up to 10 years** and other exemptions. |
| Major new investments | Full exemptions above certain thresholds under special regimes. **[RESEARCH GAP — reviewer to confirm the qualifying thresholds and application process.]** |

---

## Section 4 -- Dividends & Domestic Extraction

- **Dividends: 5%** withholding (definitive); **25%** if paid to a tax-haven jurisdiction.
- Individuals are **not** re-taxed on dividends where the company already paid corporate ISR.
- Domestic investment income: **10%** flat.
- Standard self-employed ISR per `el-salvador-income-tax.md` (Art. 37 table; cuotas fijas 212.12 / 720 / 3,462.86).

---

## Section 5 -- Red Lines (do not cross)

- **Source rules:** the foreign-income exemption applies to genuinely foreign-source income — don't relabel Salvadoran-source income.
- **Tech / FTZ incentives** require genuine qualifying activity and the proper certification.
- **Tax-haven payments** attract the 25% dividend rate — structure accordingly, legitimately.

---

## PROHIBITIONS

- NEVER assert the foreign-source exemption without confirming the income qualifies under the 2024 reform.
- NEVER claim the 15-year tech holiday without genuine qualifying activity + certification.
- NEVER contradict the rates/tables in `el-salvador-income-tax.md` / `el-salvador-social-contributions.md` / `el-salvador-payroll.md`.
- NEVER present [RESEARCH GAP] figures as confirmed, nor optimisation as definitive advice — route to a licensed Salvadoran tax adviser.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed contador/abogado in El Salvador) before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

---

<!-- openaccountants-cta-block -->

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://www.openaccountants.com/network).

<!-- openaccountants-mcp-cta -->

## The accountant-verified version lives in the connector

This file is the open, **research-grade draft**. The **accountant-verified**
version of this skill is **not published to GitHub** — it is delivered free
through the OpenAccountants MCP connector, where your AI agent loads the
verified rules together with the name of the accountant who signed them off.

**→ Install the free connector:** <https://www.openaccountants.com/connect>
**MCP endpoint:** `https://www.openaccountants.com/api/mcp`
