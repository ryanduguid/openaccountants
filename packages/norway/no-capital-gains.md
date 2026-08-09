---
name: no-capital-gains
description: >
  Norway capital gains tax: 22% rate, shield deduction (skjermingsfradrag) on shares,
  shareholder model, exit tax. Trigger on: "Norway CGT", "capital gains Norway",
  "Norway 22% capital gains", "skjermingsfradrag", "shareholder model Norway",
  "sell shares Norway", "Norway aksjer skatt", "Norway exit tax shares".
version: 1.0
jurisdiction: "NO"
tax_year: 2025
tier: 2
last_updated: 2026-06-12
category: international
---

# Norway Capital Gains Tax — v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Quick reference

| Item | Value |
|---|---|
| CGT rate | **22%** flat (ordinary income rate) |
| Shares: shield deduction | Yes — skjermingsfradrag reduces taxable gain |
| Legislation | Skatteloven (§10-30 to §10-37 for shares) |
| Tax authority | Skatteetaten (skatteetaten.no) |

---

## Shares — shareholder model (aksjonærmodellen)

Norway's shareholder model taxes gains on shares at 22%, but first allows a
**shield deduction (skjermingsfradrag)** — a risk-free return on invested capital
that is not taxed.

```
Taxable gain = Actual gain − Shield deduction
Shield deduction = Cost base × Shield rate (approximately 2%–3% per year)
```

The shield deduction accumulates annually and can be used against dividends or gains.
Unused shield deduction carries forward.

**Effective rate** on investment gains: 22% on the gain above the shield deduction.

---

## Real property

Gains from sale of **primary residence** are **exempt** if:
- You have owned the property for at least 1 year, AND
- You have used it as your primary residence for at least 1 of the last 2 years

Gains from other real property (rental, holiday property): taxed at 22%.

---

## Exit tax

When a Norwegian tax resident **emigrates** and holds shares with unrealised gains
exceeding NOK 500,000, Norway may impose an **exit tax** on those gains.

- Exit tax is assessed on departure
- Payment can be deferred if moving to an EEA country (must post security)
- Deferred tax becomes due after 12 years or if shares are sold

---

## Sources

- Skatteloven, §10-30 to §10-37 (shareholder model)
- Skatteetaten: skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities

> Working paper only. The shield deduction calculation requires the annual rates
> published by Skatteetaten. Have a qualified Norwegian tax adviser (autorisert
> regnskapsfører / skatterådgiver) review.

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
