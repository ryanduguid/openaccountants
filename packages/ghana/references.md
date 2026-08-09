---
name: ghana-references
jurisdiction: GH
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Ghana — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. Projects below are used as reference for tax rate data.

## taxcalculatorgh

- Repository: [Kessir/taxcalculatorgh](https://github.com/Kessir/taxcalculatorgh)
- License: verify before code reuse (no explicit license file)
- Stars: 32
- Language: JavaScript (Vue.js)
- Scope: Most popular Ghana income tax calculator on GitHub. Implements GRA PAYE (Pay As You Earn) monthly tax brackets with historical rate tables from 2021 through 2024. Includes SSNIT (Social Security) contribution calculation at 5.5%.
- Why it matters: Actively maintained with bracket updates tracking GRA announcements. 32 stars indicates real usage among Ghanaian developers and taxpayers.
- Integration approach: Monthly PAYE bracket tables and SSNIT rate used as reference for the income tax skill. Rate data (public domain tax law) incorporated with attribution.

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
