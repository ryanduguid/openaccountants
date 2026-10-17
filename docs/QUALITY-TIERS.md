# OpenAccountants — Skill Quality Tiers

Quality tiers record a guide's review status. Check its scope, period, sources
and unresolved conditions before deciding whether it supports the intended use.

Every published guide uses one of **two tiers**: accountant-reviewed or source-cited draft.

---

## The two tiers

| Tier | Label | What it means | Legacy identifier |
|------|-------|--------------|-------------------|
| **1** | **Accountant-reviewed** | The guide records a practitioner's sign-off. Read its scope, date, reviewer attribution and separate `review_status`; substantive edits may await renewed review. The tier alone does not establish current law or suitability for an engagement. | `accountant-verified` |
| **2** | **Source-cited draft** | The guide provides cited research within its declared scope and identifies unresolved conditions. It awaits full accountant review. Bounded references may leave mandatory operational requirements unresolved. | `research-verified` |

> **Display label vs. stored identifier.** The machine identifiers do not change: frontmatter still uses `tier: 1|2` and `verified_by:`, and legacy badges/enums still say `accountant-verified` / `research-verified`. What changed is the **display language**: Tier 1 is written as **"accountant-reviewed"** and Tier 2 as **"source-cited draft"** everywhere a human reads it. This doc is the mapping between the two.

---

## What the tiers record

### Accountant-reviewed (Tier 1)

- The guide records a reviewer in `reviewed_by` or the legacy `verified_by` field, including a withheld-name attribution where applicable. [PARTNERS.md](../PARTNERS.md) lists the recorded reviewers. Verify credentials and the engagement scope independently; this fork does not certify upstream onboarding.
- Read the recorded sign-off and any test evidence for the text and period it covers. The tier does not prove that every guide was used with client data, filed repeatedly or reviewed annually.
- A substantive edit can leave a Tier 1 guide at `pending_review`. Its previous sign-off does not certify the changed text or every later change to a shared dependency.

### Source-cited draft (Tier 2)

- Follow the canonical template and applicable workflow contracts below.
- Material rates, thresholds, forms, deadlines and legal positions require period-appropriate primary sources. Secondary summaries can corroborate those sources.
- Research supports only the guide's declared scope. Read its source limits, completion register and operational holds; publication does not establish comprehensive research or country coverage.
- The professional reviewer must resolve applicable source, fact and delivery conditions before filing or acting on an output. A draft cannot replace that review.

---

## The standard skill format

Use [skill-template.md](skill-template.md) for frontmatter and body requirements,
with [CONTRIBUTING.md](../CONTRIBUTING.md) for the applicable foundation bases.
The loaded universal and domain contracts govern execution order, confirmation,
refusals, outputs and checks. Country content supplies the substantive rules and
source conditions. A VAT return outline does not prescribe formation or
financial-statement sections.

State the supported scope, period and primary sources. Include reproducible
examples, edge cases, checks and the required disclaimer and canonical contact
block. Identify incomplete mandatory slots and hold unsupported operational
work. Within-guide rule confidence is separate from the overall quality tier.

---

## Current inventory

**1,924 Guides** across **248 jurisdictions** · **164 accountant-reviewed** · **22 named accountants**

Derived from `index.json` with the one counting rule in `scripts/oa_tools/roster.py`: a guide is accountant-reviewed when it carries `tier: 1` and a reviewer's name, and a named accountant is such a reviewer who did not ask to be anonymous. `scripts/check-coverage-claims.py` fails CI when this line drifts from the tree; [COVERAGE.md](COVERAGE.md) carries the full derived table.

### Accountant-reviewed (Tier 1)

164 guides in this tree carry `tier: 1` with a named reviewer, across 23 `reviewed_by` values. One of those values is "A licensed accountant (name withheld at their request)", on 14 guides, which is why 23 reviewers are 22 named accountants. [PARTNERS.md](../PARTNERS.md), generated from the index by `scripts/build-partners.py`, lists them per reviewer and per jurisdiction. List the guides with:

```
python3 -c "import json;d=json.load(open('index.json'));print('\n'.join(sorted(g['slug']+'  '+g['reviewed_by'] for g in d['guides'] if str(g.get('tier'))=='1')))"
```

The list is derived from each skill's explicit `tier: 1` plus its reviewer name (`reviewed_by`, or the legacy `verified_by` — a stored identifier that keeps its spelling). To add a new accountant-reviewed skill, set **both** `tier: 1` and the reviewer's name and credential, then regenerate the canonical inventory with `python3 scripts/build-index.py` — the tier and verifier land in `index.json`. The enforced rule is field-specific: `tier: 2` must not carry a real `verified_by` — that combination is a validation error. A real `reviewed_by` on a `tier: 2` guide is *not* rejected (see `check_quality_metadata` in `scripts/validate-guides.py` and its test), because `reviewed_by` has also been used as a plain authorship/attribution field (on the hand-authored `packages/us-federal/` guides, until they were retired in favour of `skills/federal/` on 2026-09-28). 99 guides sit in that permitted state, a named `reviewed_by` with `tier: 2`: the name records an accountant who contributed corrections (usually a "Verified rates & thresholds" block) without signing the whole guide off, and none of them counts as reviewed anywhere in this repository. Credential numbers are held at openaccountants.com and appear on a skill page only when the practitioner opts in.

`review_status` is a separate axis, review **freshness**: `current` means the recorded sign-off covers the text as it stands, and `pending_review` that the guide awaits a review, either because it is a draft or because a substantive edit superseded the reviewed text (the guide keeps its `tier: 1`, and [PARTNERS.md](../PARTNERS.md) counts it as "edited since review" against its reviewer). The validator rejects any other value and rejects `current` on a `tier: 2` guide, since no review promoted it; until 2026-09-29, 93 tier-2 guides carried that combination, which reads as "reviewed" on every other surface, and a reader could not tell from the frontmatter alone. The field is in `index.json` and in the MCP catalogue (`list_skills`, `get_skill`) alongside `tier`, which alone says whether a guide is accountant-reviewed. The spec is the `review_status` row of [skill-template.md](skill-template.md).

### Source-cited drafts (Tier 2)

There are 1,760 Tier 2 guides among the 1,924 indexed guides. These inventory
counts do not establish comprehensive country coverage or a completed source
chain for every draft. Read each guide's date, cited sources, scope and open
conditions. See [COVERAGE.md](COVERAGE.md) for the derived inventory and
[COUNTRY-COVERAGE.md](COUNTRY-COVERAGE.md) for country-presence limits.

---

## What the user sees on a skill

```
┌─────────────────────────────────────────────┐
│  Malta VAT Return v1.0                      │
│  ████████████ ACCOUNTANT-REVIEWED           │
│                                             │
│  Reviewed by: [Practitioner + credential]   │
│  Tested against: Real client data           │
│  Last updated: [Date]                       │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  France VAT Return (CA3) v0.1               │
│  ▓▓▓▓▓▓▓▓░░░░ SOURCE-CITED DRAFT            │
│                                             │
│  Sources: impots.gouv.fr, PWC, EU TEDB      │
│  Research date: April 2026                  │
│  Awaiting accountant review                 │
│  Help review: openaccountants.com/verify    │
└─────────────────────────────────────────────┘
```

---

## How a skill moves from source-cited draft to accountant-reviewed

Follow [CONTRIBUTING.md, Review](../CONTRIBUTING.md#review). A named, licensed
practitioner reviews the complete guide and its applicable sources, makes any
corrections, tests representative cases and signs it off in a pull request
setting `tier: 1` and their name and credential in `reviewed_by`. Maintainers
review and merge that contribution; they do not set Tier 1 on a practitioner's
behalf. A name on a Tier 2 guide or corrections submitted without that complete
sign-off do not promote it. Use redacted representative records for agent work;
do not submit private client data as repository or model inputs.

---

## Authoritative research sources

Use applicable statutes, regulations and tax-authority publications as primary
authority for the requested period. The directories below are starting points;
commercial summaries provide corroboration and cannot replace missing primary
law. Verify the actual source and its scope before relying on it.

### Global / multi-jurisdiction

| Source | URL pattern | What it covers |
|--------|------------|----------------|
| **Deloitte Tax Guides** | dits.deloitte.com | VAT/GST rates, thresholds, compliance |
| **EY Worldwide Tax Guide** | ey.com/en_gl/tax-guides | Country-by-country tax overviews |
| **KPMG Tax Rates Online** | kpmg.com/tax-rates | Corporate / individual / indirect tax rates |
| **OECD Tax Database** | oecd.org/tax/tax-policy | Standardised cross-country tax data |

### European Union

| Source | URL | What it covers |
|--------|-----|----------------|
| **EU TEDB** (Taxes in Europe Database) | ec.europa.eu/taxation_customs/tedb | Official EU VAT rates for all 27 Member States |
| **EC VAT Information Exchange System** | ec.europa.eu/taxation_customs/vies | VAT number validation |
| **VAT Expert Group publications** | ec.europa.eu | Directive interpretations |

### Country-specific tax authorities

| Country | Authority | URL |
|---------|-----------|-----|
| **UK** | HMRC | gov.uk/government/organisations/hm-revenue-customs |
| **Canada** | CRA | canada.ca/en/revenue-agency |
| **Australia** | ATO | ato.gov.au |
| **New Zealand** | IRD | ird.govt.nz |
| **Ireland** | Revenue | revenue.ie |
| **Germany** | BZSt / Finanzamt | bzst.de, elster.de |
| **France** | DGFiP | impots.gouv.fr |
| **Italy** | Agenzia delle Entrate | agenziaentrate.gov.it |
| **Spain** | AEAT | agenciatributaria.es |
| **Netherlands** | Belastingdienst | belastingdienst.nl |
| **Portugal** | AT | portaldasfinancas.gov.pt |
| **Belgium** | SPF Finances | finances.belgium.be |
| **Poland** | KAS | podatki.gov.pl |
| **India** | GSTN / CBDT | gst.gov.in, incometax.gov.in |
| **Japan** | NTA | nta.go.jp |
| **Singapore** | IRAS | iras.gov.sg |
| **South Korea** | NTS | nts.go.kr |
| **Brazil** | RFB | gov.br/receitafederal |
| **Mexico** | SAT | sat.gob.mx |
| **UAE** | FTA | tax.gov.ae |
| **South Africa** | SARS | sars.gov.za |
| **Kenya** | KRA | kra.go.ke |
| **Nigeria** | FIRS | firs.gov.ng |

### US state tax authorities

Each state has an online portal. Search "[State] department of revenue" for the canonical URL. Major examples:

| State | Authority | URL |
|-------|-----------|-----|
| **California** | CDTFA | cdtfa.ca.gov |
| **New York** | DTF | tax.ny.gov |
| **Texas** | Comptroller | comptroller.texas.gov |
| **Florida** | DOR | floridarevenue.com |
| **Illinois** | IDOR | tax.illinois.gov |
| **Washington** | DOR | dor.wa.gov |

---

## Disclaimer

Quality tiers describe the review status of a skill, not a guarantee that any specific output is correct. LLMs hallucinate, tax law changes, and individual circumstances vary. Every output must be reviewed by a qualified professional before filing.
