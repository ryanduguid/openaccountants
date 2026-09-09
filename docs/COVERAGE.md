# Coverage — single source of truth

**This file is the canonical record of OpenAccountants coverage numbers.** Every other surface — GitHub README, repo About, the website, Smithery, MCP directories, release notes — should match the figures here. If they disagree, this file wins; fix the other surface.

_Last updated: 2026-06-07 · source: production database (skills served via the MCP server)._

> [!IMPORTANT]
> **The tables below count the production database, not this checkout.** They are
> a frozen upstream snapshot and they do not match this tree. Anything counting
> files here should use the section immediately below, which is derived from
> `index.json` and can be re-derived at any time.

## This repository (derived from `index.json`)

Regenerate with `python3 scripts/build-index.py`; the `counts` block at the top
of `index.json` carries the first three rows.

| Measure | This tree |
|---|---|
| Guide files indexed | **1,953** |
| Distinct `jurisdiction` codes | **244** |
| `tier: 1` (accountant-reviewed) | **171** |
| `tier: 2` (source-cited draft) | **1,782** |
| Distinct `reviewed_by` values | **29** (one spelling each; Aryee, Amiridze and Mat Hussin were previously recorded two ways and are now normalised to `Name, Credential`) |
| Country directories under `skills/international/` | **189** |
| US jurisdiction codes (`US` + 50 states + DC + `US-NY-NYC`) | **53** |
| Generated bundles under `packages/` | **256** |

US coverage is complete at state level: all 50 states plus DC are present.

> **Two numbers below are contradicted by this tree, and a maintainer needs to
> resolve which is right.** The table further down says Tier 1 lives on the
> "MCP server only (not in this repo)" and counts 85 of them — but this
> repository contains 171 guides carrying `tier: 1`, a named `reviewed_by` and
> `review_status: current`, and README.md's "greppable honesty" table says an
> accountant-reviewed Guide is identified by exactly that frontmatter. Either
> those 171 are genuinely reviewed and the Tier 1 row is wrong, or they are
> mislabelled. See also the 98 guides that carry a named `reviewed_by` while
> marked `tier: 2` — permitted by the enforced contract, but 94 of them also
> carry `review_status: current`, which means `tier: 1` everywhere else. See
> [QUALITY-TIERS.md](QUALITY-TIERS.md).

## Headline (use these)

| Claim | Number |
|---|---|
| Skills (published) | **1,098** |
| Jurisdictions | **192** |
| Rounded headline | **1,000+ skills across 192 jurisdictions** |

> When a headline needs round numbers, use **"1,000+ skills"** and **"192 jurisdictions"** (or **"130+ countries plus every US state"**). Do not invent other figures.

## Quality-state split

OpenAccountants has two quality tiers (see [QUALITY-TIERS.md](QUALITY-TIERS.md)). The distinction matters and should never be collapsed into a blanket "accountant-reviewed":

| Tier | What it means | Count | Where it lives |
|---|---|---|---|
| **Accountant-reviewed** (Tier 1) | A licensed practitioner has reviewed and signed off; name + credential on every output | **85** | **MCP server only** (not in this repo) |
| **Source-cited draft** (Tier 2) | Every rate/threshold/form drafted from authoritative sources, awaiting a full accountant review | **1,013** | **This repo** |

**Correct headline phrasing:** _"Source-cited drafts in this repo. Accountant-reviewed via the MCP connector."_

## Jurisdiction breakdown

| Level | Count |
|---|---|
| Country-level jurisdictions | **139** |
| US state-level codes (50 states + DC + federal) | **53** |
| **Total distinct jurisdictions** | **192** |

Notes:
- "130+ countries" is the safe rounded claim (139 country-level jurisdictions). **Do not say "every country"** — there are ~195 sovereign countries; we cover ~139.
- Canada is served at the federal level (`CA`) via the MCP; this repo additionally breaks Canada into province/territory packages.
- US is covered federally plus every state and DC.

## How to update this file

When skills are published or jurisdictions added, re-run the counts against the production database and update the tables above **and** the "Last updated" date. Then reconcile the README headline, repo About, and website to match.
