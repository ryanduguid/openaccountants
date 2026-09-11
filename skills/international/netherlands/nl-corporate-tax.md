---
name: nl-corporate-tax
description: Use this skill whenever asked about Dutch corporate income tax (vennootschapsbelasting / VPB) for BV entities. Trigger on phrases like "vennootschapsbelasting", "VPB aangifte", "corporate tax Netherlands", "BV belasting", "fiscal unity", "fiscale eenheid", "innovatiebox", "verliesverrekening", "carry forward losses", "DGA salary", "gebruikelijk loon", "deelnemingsvrijstelling", "participation exemption", "fiscal profit bridge", "commercial to fiscal result", "liquidatieverliesregeling", or any question about computing or filing corporate income tax for a Dutch BV or NV. Also trigger when preparing annual accounts-to-tax reconciliation, computing VPB liability, or advising on fiscal adjustments. This skill covers VPB rates, fiscal profit computation, loss relief, fiscal unity, the innovation box, participation exemption, DGA salary rules, filing deadlines, and penalties. ALWAYS read this skill before touching any Dutch corporate tax work.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-09-11
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NL Corporate Tax

## Netherlands Corporate Income Tax — Vennootschapsbelasting (VPB) v1.0

> **Based on work by [John in 't Hout (@johnhout)](https://github.com/johnhout/knowledge-work-belastingzaken)**, licensed under MIT. Adapted for the OpenAccountants format.

> **A second Dutch corporate tax has been in force since 31 December 2023, and
> this guide did not mention it.** The `description` above says *"ALWAYS read this
> skill before touching any Dutch corporate tax work"*, and until now the skill
> covered only the Wet Vpb 1969. An in-scope group working from it alone will
> compute VPB and stop, missing a separate charge under a separate Act with its
> own liability rules. Set out in *Section 7 — Wet minimumbelasting 2024* below,
> read from the consolidated text on `wetten.overheid.nl`.
>
> It does **not** replace the VPB. The two run alongside each other: the minimum
> tax tops up to a 15% effective rate, so the Wet Vpb 1969 rates in Section 1
> still govern the ordinary charge.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Tax | Vennootschapsbelasting (VPB) — corporate income tax |
| Currency | EUR only |
| Tax year | Financial year (typically calendar year; alternative book years allowed) |
| Primary legislation | Wet op de vennootschapsbelasting 1969 (Wet Vpb 1969) — **and, separately, the Wet minimumbelasting 2024** for in-scope groups, see Section 7 |
| Tax authority | Belastingdienst |
| Filing portal | Mijn Belastingdienst / Aangifte vennootschapsbelasting |
| Filing deadline | 5 months after end of financial year (1 June for calendar year); extension possible up to 5 additional months |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a qualified Dutch belastingadviseur or AA/RA accountant |
| Skill version | 1.0 |

### VPB Rates 2025 [T1]

**VPB Rates 2025**

| Taxable Profit (EUR) | Rate | Notes |
| --- | --- | --- |
| 0 — 200,000 | 19.0% | Lower bracket (schijf 1) |
| Over 200,000 | 25.8% | Upper bracket (schijf 2) |

- **VPB formula** — VPB = EUR 200,000 × 19% + (taxable profit − EUR 200,000) × 25.8%

**Rate history (for comparison/audit)**

| Year | Lower bracket | Lower rate | Upper rate |
| --- | --- | --- | --- |
| 2023 | EUR 200,000 | 19.0% | 25.8% |
| 2024 | EUR 200,000 | 19.0% | 25.8% |
| 2025 | EUR 200,000 | 19.0% | 25.8% |

### Fiscal Profit Bridge (Commercial → Fiscal) [T1]

**Fiscal Profit Bridge**

| Step | Adjustment | Direction |
| --- | --- | --- |
| 1 | Commercial net result (jaarrekening) | Starting point |
| 2 | Add back: non-deductible expenses (entertaining 73.5% non-deductible portion, fines, bribes) | + |
| 3 | Add back: excessive interest (earnings stripping — see below) | + |
| 4 | Deduct: participation exemption income (deelnemingsvrijstelling) | − |
| 5 | Apply: different depreciation rules (fiscal vs commercial) | ± |
| 6 | Apply: fiscal reserves (herinvesteringsreserve, etc.) | ± |
| 7 | Deduct: loss carry-forward (if applicable) | − |
| 8 | = Belastbaar bedrag (taxable amount) | Result |

### Earnings Stripping (Renteaftrekbeperking) [T1]

**Earnings Stripping**  _(Article 15b Wet Vpb 1969)_

| Rule | Value |
| --- | --- |
| Threshold | Higher of: EUR 1,000,000 or 20% of fiscal EBITDA |
| Scope | Net interest expense (interest paid − interest received) |
| Legislation | Article 15b Wet Vpb 1969 |

- **Non-deductible net interest carry-forward** — Net interest exceeding the threshold is non-deductible and carried forward indefinitely.  _(Article 15b Wet Vpb 1969)_

### Loss Relief (Verliesverrekening) [T1]

**Loss Relief**

| Direction | Rule |
| --- | --- |
| Carry-back | 1 year |
| Carry-forward | Indefinite, but limited per year |
| Annual cap | EUR 1,000,000 + 50% of taxable profit exceeding EUR 1,000,000 |

**Example:** If taxable profit before loss relief = EUR 3,000,000:
- Maximum utilisation = EUR 1,000,000 + 50% × (EUR 3,000,000 − EUR 1,000,000) = EUR 2,000,000

### Participation Exemption (Deelnemingsvrijstelling) [T1]

**Participation Exemption**  _(Articles 13–13l Wet Vpb 1969)_

| Requirement | Detail |
| --- | --- |
| Minimum holding | ≥ 5% of nominal share capital |
| Effect | Dividends and capital gains from qualifying participation are fully exempt |
| Legislation | Articles 13–13l Wet Vpb 1969 |
| Anti-abuse | Passive investment holdings excluded (beleggingsdeelneming) unless subject to ≥ 10% effective tax |

### Fiscal Unity (Fiscale Eenheid) [T1]

**Fiscal Unity**  _(Articles 15–15aj Wet Vpb 1969)_

| Requirement | Detail |
| --- | --- |
| Ownership | Parent holds ≥ 95% of shares in subsidiary |
| Jurisdiction | Both entities must be NL-resident (or deemed resident with NL PE) |
| Effect | Consolidated VPB return; intercompany results eliminated |
| Legislation | Articles 15–15aj Wet Vpb 1969 |
| Risk | If conditions cease to be met, unity breaks — potential recapture |

### Innovation Box (Innovatiebox) [T1]

**Innovation Box**  _(Article 12b Wet Vpb 1969)_

| Parameter | Value |
| --- | --- |
| Effective rate | 9.0% on qualifying innovation profits |
| Qualification | Profits from self-developed intangible assets (with WBSO declaration or patent) |
| Threshold | First EUR 25,000 qualifying profit exempt from regular VPB (drempel) |
| Legislation | Article 12b Wet Vpb 1969 |

### DGA Salary — Gebruikelijk Loon [T1]

**DGA Salary — Gebruikelijk Loon**  _(Article 12a Wet op de loonbelasting 1964)_

| Parameter | Value 2025 |
| --- | --- |
| Minimum salary | EUR 56,000 (2025) |
| Rule | DGA must receive at least the higher of: minimum threshold, 100% of comparable employees, or highest employee salary |
| Deviation | Allowed only if taxpayer demonstrates that a lower salary is "gebruikelijk" given circumstances |
| Legislation | Article 12a Wet op de loonbelasting 1964 |

### Key Deadlines [T1]

**Key Deadlines**

| Obligation | Deadline |
| --- | --- |
| Filing VPB return | 1 June (calendar year entities); extension up to 1 November |
| Provisional assessment request | Before end of financial year (to manage cash flow) |
| Objection (bezwaar) | 6 weeks after date on assessment |
| Payment final assessment | 6 weeks after date on assessment |

### Conservative Defaults [T1]

**Conservative Defaults**

| Situation | Default Assumption |
| --- | --- |
| Uncertain deductibility of expense | Non-deductible — flag for advisor |
| Participation exemption qualification unclear | Do NOT apply — include income; flag |
| Innovation box eligibility unclear | Do NOT apply — use standard rates; flag |
| Fiscal unity status unclear | Treat as standalone entity; flag |
| DGA salary below EUR 56,000 | Flag as non-compliant; compute at minimum |
| Loss carry-forward amount unconfirmed | Do NOT apply — flag for prior-year reconciliation |

### Red Flag Thresholds [T1]

**Red Flag Thresholds**

| Flag | Threshold |
| --- | --- |
| DGA salary below minimum | EUR 56,000 (2025) — compliance risk |
| Intercompany loan without documentation | Transfer pricing risk — flag |
| Net interest > EUR 1,000,000 | Earnings stripping analysis required |
| Holding with < 5% participation | Participation exemption denied — gains taxable |
| Fiscal unity entity becoming non-resident | Unity break risk — recapture |
| Profit > EUR 200,000 in lower bracket | Verify no profit splitting arrangements |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Annual accounts (jaarrekening) including profit & loss and balance sheet. Confirmation of entity type (BV/NV) and financial year.

**Recommended:** Trial balance, prior-year VPB assessment (aanslag), loss carry-forward schedule, details of intercompany transactions, shareholding structure.

**Ideal:** Complete administration including fixed asset register, loan documentation, WBSO declarations, fiscal unity decree, prior-year fiscal adjustments, transfer pricing documentation.

### Refusal Catalogue

- **R-VPB-1 — No annual accounts available.** — Cannot compute VPB without financial statements. Provide at minimum a trial balance and P&L statement.  _(R-VPB-1)_
- **R-VPB-2 — Entity structure unclear.** — Cannot determine standalone vs. fiscal unity treatment without confirmed shareholding structure. Escalate.  _(R-VPB-2)_
- **R-VPB-3 — Intercompany transactions without documentation.** — Transfer pricing risk. Cannot determine arm's length pricing without documentation. Flag for belastingadviseur.  _(R-VPB-3)_
- **R-VPB-4 — Innovation box claimed without WBSO.** — Cannot apply 9% rate without confirmed WBSO declaration or patent. Apply standard rates.  _(R-VPB-4)_
- **R-VPB-5 — Cross-border element present.** — International tax treaty analysis required. Stop and escalate to international tax specialist.  _(R-VPB-5)_

## Section 3 — Computation Workflow

### Step-by-Step VPB Computation

```
1. Start with commercial net result (per annual accounts)
2. Identify and add back non-deductible expenses:
   - Entertainment/representation: 73.5% non-deductible (or choose EUR 5,100 fixed amount)
   - Fines and penalties: 100% non-deductible
   - Bribes: 100% non-deductible
   - Excessive interest (earnings stripping): non-deductible portion
3. Apply fiscal depreciation differences:
   - Buildings: max depreciation to 100% WOZ value (own use) or 50% WOZ (investment)
   - Goodwill: max 10% per year fiscally
4. Apply participation exemption (if qualifying):
   - Remove dividends and gains from ≥5% participations
5. Apply innovation box (if WBSO/patent confirmed):
   - Separate qualifying profits; apply 9% rate
6. Determine taxable amount before loss relief
7. Apply loss carry-forward:
   - Max EUR 1,000,000 + 50% of excess
8. Compute VPB:
   - First EUR 200,000 × 19%
   - Remainder × 25.8%
9. Deduct provisional payments already made
10. = VPB payable / refundable
```

### Non-Deductible Expenses Detail

**Non-Deductible Expenses Detail**

| Category | Non-deductible portion | Alternative |
| --- | --- | --- |
| Food, drink, entertainment | 73.5% | OR fixed EUR 5,100/year non-deductible |
| Gifts > EUR 227 per recipient | Only portion above EUR 227 deductible per occasion | — |
| Fines (bestuurlijke boetes) | 100% | — |
| Bribes | 100% | — |
| VPB itself | 100% | — |
| Dividend distributions | 100% (not an expense) | — |

### Fiscal Depreciation Limits

**Fiscal Depreciation Limits**

| Asset | Fiscal Rule |
| --- | --- |
| Buildings (own use) | Depreciate to max 100% of WOZ value (bodemwaarde) |
| Buildings (investment) | Depreciate to max 50% of WOZ value |
| Goodwill | Max 10% per year (minimum 10-year life) |
| Other intangibles | Based on useful economic life |
| Tangible fixed assets | Based on economic life; no minimum |

## Section 4 — Filing Process

### VPB Return Sections (Aangifte Vpb)

**VPB Return Sections**

| Section | Content |
| --- | --- |
| General information | Entity, financial year, contact details |
| Fiscal balance sheet | Assets and liabilities at fiscal values |
| Fiscal P&L | Revenue, costs, and adjustments at fiscal treatment |
| Reconciliation | Commercial → fiscal bridge |
| Participation exemption | Details of qualifying holdings |
| Loss relief | Carry-back/carry-forward schedule |
| Innovation box | Qualifying profit computation |
| Fiscal unity | Consolidation details (if applicable) |

### Common Errors to Check

**Common Errors to Check**

| Error | Consequence |
| --- | --- |
| Forgot to add back entertainment costs | Understated taxable profit |
| Applied participation exemption to < 5% holding | Incorrectly excluded gains |
| Used commercial depreciation instead of fiscal | Incorrect taxable profit |
| Carried forward loss without applying cap | Excess deduction |
| DGA salary below EUR 56,000 without justification | Penalty risk on loonbelasting |
| Filed after deadline without extension | Estimated assessment (ambtshalve aanslag) and potential fine |

## Section 5 — Official Source Verification Requirements

Before any rate, threshold, or deadline is used in output:

1. Verify practical filing instructions on `belastingdienst.nl/vpb`
2. Verify statutory text on `wetten.overheid.nl` (Wet Vpb 1969)
3. Record exact URL and retrieval date (YYYY-MM-DD)
4. If source unavailable or conflicting: mark as **UNVERIFIED** and require professional confirmation

## Section 6 — Escalation Points

Escalate to a qualified belastingadviseur when:

- Fiscal unity formation, termination, or cross-border elements exist
- Transfer pricing disputes or documentation gaps
- Innovation box qualification is borderline
- Material uncertain tax positions (> EUR 50,000 impact)
- Mergers, demergers, or share transactions
- International dividend/royalty flows (withholding tax implications)
- Entity is part of a multinational group (Country-by-Country Reporting obligations)

## Section 7 — Wet minimumbelasting 2024 (Pillar Two minimum tax)

A separate Act from the Wet Vpb 1969, with its own scope, its own liability rules
and its own return. Read from the consolidated text at
[wetten.overheid.nl/BWBR0049111](https://wetten.overheid.nl/BWBR0049111/2026-04-11).

### Commencement

- **In force 31 December 2023**, first applying to reporting years (*verslagjaren*)
  beginning on or after **31 December 2023**  _(Wet minimumbelasting 2024, art. 17.1(1))_
- **Articles 15.1 and 15.2(A) are deferred to 31 December 2024.** Article 15.1 amends
  article 5.1 — the *onderbelastewinstbijheffing* — so the UTPR arm starts a year
  after the other two  _(art. 17.1(2))_

### Scope — and note it is not multinational-only

- **Threshold** — Applies to group entities of a *multinationale groep* **or a
  *binnenlandse groep*** — a purely domestic Dutch group is in scope too — where,
  per the ultimate parent entity's consolidated accounts, revenue is at least
  **EUR 750,000,000** per reporting year in **at least two of the four** reporting
  years immediately preceding, or of however many fewer years have preceded it  _(art. 2.1(1))_
- **The EUR 750,000,000 is computed inclusive** of the revenue of *uitgesloten
  entiteiten* (excluded entities under art. 2.2) as recorded in the ultimate parent's
  consolidated accounts, and is increased or reduced proportionally for a reporting
  year longer or shorter than twelve months  _(art. 2.1(2))_
- **Rate** — *minimumbelastingtarief:* **15%**  _(art. 1.2, definitions)_

### Three charges, three chapters — check all three

| Chapter | Charge | Who is liable |
| --- | --- | --- |
| 3 (arts. 3.1–3.2) | *Binnenlandse bijheffing* — domestic top-up | A group entity **established in the Netherlands** that is a **low-taxed group entity**. Where several in the same group qualify, the charge is levied **as if they were one taxpayer** _(art. 3.1(1)–(2))_ |
| 4 (arts. 4.1–4.3) | *Inkomen-inclusiebijheffing* — Income Inclusion Rule | A Netherlands-established group entity that is an **ultimate parent entity**, or an **intermediate parent entity** held by an ultimate parent in a third state _(art. 4.1(1))_ |
| 5 (arts. 5.1–5.2) | *Onderbelastewinstbijheffing* — UTPR | A Netherlands-established group entity, **not** an investment entity, in a multinational group containing low-taxed entities whose ultimate parent is excluded or in a third state _(art. 5.1(1))_ |

- **Do not reduce this to "the Netherlands has an IIR".** The domestic top-up in
  chapter 3 turns on the entity's own establishment in the Netherlands and on its
  being low-taxed — not on where the group's parent sits. It is the charge that
  reaches a Dutch subsidiary of a foreign-parented group, and such an entity is
  not reached by the IIR at all.

### Transitional CbCR safe harbour — the rate moves every year

- **Transitional rate (*overgangstarief*) for the reporting year** — reporting years
  beginning in **2023 or 2024: 15%**; **2025: 16%**; **2026: 17%**. A figure copied
  from an older note will be wrong for the current year  _(Wet minimumbelasting 2024, transitional safe-harbour provisions, art. 8.8)_

### The Act has been amended twice — check the consolidated text, not the original

Searching the title on `wetten.overheid.nl` returns five instruments, not one:

| Instrument | BWB | Consolidated to |
| --- | --- | --- |
| **Wet minimumbelasting 2024** | BWBR0049111 | 2026-04-11 |
| Wet aanpassing Wet minimumbelasting 2024 | BWBR0050585 | 2024-12-31 |
| **Tweede** wet aanpassing Wet minimumbelasting 2024 | BWBR0052033 | 2025-12-31 |
| Uitvoeringsbesluit minimumbelasting 2024 | BWBR0050584 | 2026-01-01 |
| Wet implementatie EU-richtlijn gegevensuitwisseling minimumbelasting | BWBR0052128 | 2026-04-11 |

Everything above is read from the **consolidated** BWBR0049111 as at 2026-04-11, which
already incorporates both amending Acts. The *Uitvoeringsbesluit* and the
information-exchange Act **have not been read for this guide** — filing and reporting
obligations in particular are not covered here.

> **Not covered, and material to a real engagement:** return and notification
> deadlines, the *Uitvoeringsbesluit*, the DAC9 information-exchange obligations, and
> the detailed safe-harbour conditions. Section 7 establishes *whether a group is in
> scope and which of the three charges reaches it*, not how to compute or file.

## Disclaimer

**⚠️ DISCLAIMER: This skill provides workflow support only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified Dutch belastingadviseur before filing. Tax rules change annually — verify all rates and thresholds against belastingdienst.nl before use.**

*OpenAccountants — open-source accounting skills for AI*
*openaccountants.com*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
