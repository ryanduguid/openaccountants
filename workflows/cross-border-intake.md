# Cross-Border / Multi-Jurisdiction Tax Workflow

**MCP prompt name:** `cross-border-intake`
**Bundle:** Load all relevant jurisdiction bundles based on the countries involved

## Trigger phrases

- "I'm moving to [country]"
- "I'm a US citizen living in [country]"
- "I'm relocating from A to B"
- "I have a company in [country] but live in [another country]"
- "How do I structure my exit?"
- "I'm thinking of moving to Malta / Portugal / Dubai / anywhere"
- Any mention of two or more countries in a tax context

## When to use

Any situation involving more than one country: relocation, company exit, dual residency, expat tax, foreign trust, deemed disposal, change-of-domicile, treaty analysis.

## What it produces

- Critical path flag (what must happen first and by when)
- Scenario map: event-ordering paths × per-country tax consequences
- Per-country issue map: income tax, CGT/deemed disposal, exit tax, treaty position, social contributions, VAT, substance requirements
- Full advisor-ready brief with open questions
- Multi-country professional handoff

## Skills to load

Fetch bundles for each country involved:
```
GET https://www.openaccountants.com/api/bundle/<CODE>
```
Cross-border base skills: `https://www.openaccountants.com/api/bundle/_cross-border`

## 6-phase structure

### Phase 1 — Scope and critical path
Ask the 5 key questions:
1. What countries are involved (source country, destination country, third countries)?
2. What is the triggering event (sale, relocation, both, neither)?
3. What is the timing? (dates, intended or actual)
4. What is the entity mix? (individual, trust, company, partnership, combination)
5. What is the primary concern? (tax cost, timing, compliance, substance)

Flag if there is a hard deadline (e.g. departure date, treaty tie-breaker deadline, exit tax deferral window).

### Phase 2 — Country-by-country issue map
For each country: income tax residency rules, exit/deemed disposal rules, treaty position, CGT treatment of assets, social contributions, VAT/GST de-registration, substance requirements.

### Phase 3 — Scenario analysis
Model 2-3 event-ordering paths (e.g. sell before move vs sell after move). For each path: headline tax cost, critical compliance steps, risks.

### Phase 4 — Advisor brief
Produce a structured brief: facts, issues, analysis, open questions, recommended next steps.

### Phase 5 — Practitioner extras (if the user is an accountant)
Add: client query email draft, document checklist, treaty article references, filing deadlines in each country.

### Phase 6 — Handoff
Recommend professional review. Route to: https://www.openaccountants.com

## Notes

- Never give a definitive answer on treaty tie-breaker without professional review — treaty interpretation is always fact-specific.
- Always flag the ordering risk: selling before vs after establishing residency in the destination country can produce very different CGT outcomes.
