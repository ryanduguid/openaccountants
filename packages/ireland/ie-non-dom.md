---
name: ie-non-dom
description: >
  Use this skill for any question about Ireland's non-dom tax rules. Trigger on: "Ireland non-dom", "Irish non-domiciled", "remittance basis Ireland", "move to Ireland tax", "Irish tax foreign income", "Ireland domicile tax", "not domiciled Ireland", "Irish resident non-dom", "Ireland foreign dividends tax", "Irish non-dom CGT". Covers non-dom eligibility, remittance basis, Irish-source income treatment, CGT for non-doms, and comparison with UK non-dom.
version: 1.0
jurisdiction: IE
tax_year: 2025
tier: 2
last_updated: 2026-06-12
category: international
---

# Ireland — Non-Domicile Status — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

---

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Country | Ireland |
| Non-dom benefit | Remittance basis on foreign income and gains |
| Minimum tax | None (unlike Malta) |
| Irish-source income | Taxed in full regardless of domicile |
| Foreign income (not remitted) | Not taxed in Ireland |
| Capital gains on Irish assets | 33% |
| Capital gains on foreign assets (non-dom) | Remittance basis — taxed only if remitted |
| Primary legislation | Taxes Consolidation Act 1997 (TCA), s.18-29 |
| Tax authority | Revenue Commissioners (revenue.ie) |
| Verified by | Pending — Irish tax adviser sign-off required |

---

## Section 2 — Who is Non-Dom in Ireland?

**Domicile** in Ireland follows general law (not tax law):
- **Domicile of origin**: derived from father's domicile at birth
- **Domicile of choice**: acquired by residing in a country with indefinite intent to remain

A foreign national living in Ireland who was born outside Ireland typically retains their foreign domicile of origin **unless** they form a definite intention to live in Ireland permanently and indefinitely.

**Residency**: Separate from domicile. An individual is **ordinarily resident** in Ireland after 3 consecutive years of Irish tax residence. "Ordinary residence" affects how long you remain taxable after departing Ireland.

---

## Section 3 — Remittance Basis: What Is Taxed

For an Irish **resident** who is **non-domiciled**:

| Income/Gain type | Tax treatment |
|---|---|
| Income arising in Ireland | **Taxed in full** — Irish rates |
| Employment income from Irish employer | **Taxed in full** |
| Foreign income remitted to Ireland | **Taxed** at Irish rates |
| Foreign income NOT remitted to Ireland | **Not taxed** in Ireland |
| Capital gains on Irish assets | **33%** — taxed regardless |
| Capital gains on foreign assets, remitted | **Taxed at 33%** |
| Capital gains on foreign assets, NOT remitted | **Not taxed** |

**"Remittance"**: broadly interpreted — includes bringing money/assets to Ireland, using foreign income/gains to pay Irish debts, or acquiring property in Ireland with foreign funds.

---

## Section 4 — Clean Capital

Funds accumulated **before** becoming Irish tax resident are **not remittances** when brought to Ireland. These are "clean capital." Maintaining separate accounts for pre-Irish-residence capital vs post-residence income is strongly recommended.

---

## Section 5 — Ordinary Residence: The Trap

After 3 years of Irish tax residence, a person becomes **ordinarily resident**.

An **ordinarily resident** individual who **leaves Ireland** remains taxable on their worldwide income (not just Irish-source) for **3 years** after departure — except:
- Foreign employment income (if duties performed wholly outside Ireland)
- Certain foreign-source income that is not remitted

**Implication**: Moving to Ireland and then leaving after a few years doesn't immediately terminate Irish tax obligations. This is similar to the UK's rule but differently structured.

---

## Section 6 — CGT: 33% on Irish Assets

Irish CGT rate: **33%** on gains above the annual exemption.

| Item | Rate/Amount |
|---|---|
| CGT rate | 33% |
| Annual exemption (individual) | €1,270 |
| Entrepreneur Relief | 10% on qualifying business disposals (up to €1M lifetime) |

Irish assets = Irish shares, Irish property, Irish business goodwill. A non-dom individual pays 33% CGT on gains from Irish assets regardless of domicile status.

---

## Section 7 — Comparison with UK Non-Dom

| Feature | Ireland | UK (from April 2025) |
|---|---|---|
| Regime | Domicile-based remittance | 4-year FIG for new residents (domicile rules transitioning out) |
| Duration | Indefinite while non-dom | 4 years maximum FIG exemption |
| Minimum tax | None | None |
| Irish/UK source taxed in full | Yes | Yes |
| Annual exemption (CGT) | €1,270 | £3,000 |

---

## Section 8 — Sources

- Taxes Consolidation Act 1997, Part 34 (residence, ordinary residence, domicile)
- Revenue: revenue.ie/en/life-events-and-personal-circumstances/moving-to-ireland/
- Revenue: IT4 — Residence, Ordinary Residence and Domicile

> **Working paper only.** Irish domicile determination is fact-specific and can have significant estate tax implications in addition to income tax. Engage a qualified Irish tax adviser.

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
