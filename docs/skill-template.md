# Frontmatter spec — the canonical reference

**This section is THE frontmatter spec for every skill/Guide file in this repo.** Other docs (`CLAUDE.md`, `CONTRIBUTING.md`) link here rather than restating it. CI enforces it: `scripts/validate-guides.py` hard-fails on malformed frontmatter, a missing `name`/`description`, a non-integer `tax_year`, a missing or invalid `tier` (must be 1 or 2), a missing or malformed `last_updated` (YYYY-MM-DD), a missing `jurisdiction` (except in a small allowlist of jurisdiction-agnostic directories, where it warns), a `depends_on` slug that no guide carries as its `name`, a `US` or `US-<state>` guide that does not name `us-circular-230-disclosure` in `depends_on` (exempt: the US foundation files, `skills/financial-reporting/` and the file templates), and a missing or duplicated closing CTA block (see [Closing CTA block](#closing-cta-block)).

## Required keys — CI fails without these

| Key | Format | Notes |
|-----|--------|-------|
| `name` | slug, `[country-or-topic]-[domain]`; unique across the repo. A US-state guide is `us-[state]-[topic]` and its file is `[name].md` | e.g. `malta-income-tax`, `us-ny-sales-tax` |
| `description` | 80-100 words | What it covers, entity types, jurisdiction, tax year, plus trigger phrases the AI should match |
| `jurisdiction` | ISO code | `MT`, `GB`, `DE`, `US`, `US-CA`, `GLOBAL`, `INTL`, `EU-27`. Required even when the folder path implies it. Quote `"NO"` because YAML 1.1 otherwise reads Norway's code as boolean `false`. A **warning**, not an error, inside the small allowlist of jurisdiction-agnostic directories |
| `category` | one of the [vocabulary below](#category-vocabulary) | The domain the guide covers, topic first and the tree's residual value otherwise (the rule is under the vocabulary). CI errors on a missing value and on one outside the list; every guide has carried one since 2026-09-29, so `index.json` and the MCP server's `category` filter cover the whole corpus |
| `tier` | `1` or `2` | `1` = **accountant-reviewed** (a named licensed accountant fully reviewed and signed off); `2` = **source-cited draft** (drafted from primary sources, awaiting review). These are the only two quality states |
| `last_updated` | `YYYY-MM-DD` | Date the content was last checked/edited. It must never move backwards |

## Expected, but not enforced

`tax_year` was previously listed as required. It is not: `scripts/validate-guides.py` checks its format when the key is present and does not test for its presence, and 74 guides omit it, mostly workflow bases that are genuinely year-agnostic. Write it on anything new, but do not treat its absence in an existing file as a validation failure.

| Key | Format | Notes |
|-----|--------|-------|
| `tax_year` | **bare integer**, e.g. `2025` | The year of the guide's **primary figures** (its coverage start year). It moves when the figures do: a guide whose rate tables are the 2026 figures says `tax_year: 2026`, and a guide that carries the 2025 figures with the 2026 ones noted beside them stays `2025`. CI errors on anything that is not an integer 2015-2035. Ranges, fiscal calendars, and qualifiers ("2025-26", "2026/27", "YA 2026", "2567 (2024)") go in `tax_year_notes`, never here |

## Optional keys

| Key | Format | Notes |
|-----|--------|-------|
| `tax_year_notes` | quoted string | The human-readable tax-year label when a bare year can't express it: `"2025-26"`, `"FY 2026-27 (AY 2027-28)"`, `"2025 (with confirmed 2026 figures noted)"` |
| `verified_by` | `pending` or `Name, Credential` | e.g. `Michael Cutajar, CPA (Malta)`. Stored identifier — the field name stays `verified_by` even though the display language is "reviewed". A real name here does **not** imply `tier: 1`; set `tier: 1` explicitly as well. CI errors if `tier: 2` carries a real `verified_by` |
| `reviewed_by` | `Name, Credential` | The accountant who signed the guide off (e.g. `Christopher Aryee, CPA` on the `skills/federal/` form guides). On a `tier: 2` guide the name records an accountant who contributed corrections (usually a "Verified rates & thresholds" block) without signing the whole guide off; it does not make the guide reviewed |
| `review_status` | `current` or `pending_review` | Review **freshness**, not assurance: `current` means the recorded sign-off covers the current text; `pending_review` means the guide awaits review, either because it is a draft or because a substantive edit superseded the reviewed text (a `tier: 1` guide edited after its sign-off keeps `tier: 1` and takes `pending_review`, and `PARTNERS.md` counts it as "edited since review"). CI errors on any other value and on `current` with `tier: 2`, since no review promoted the guide |
| `depends_on` | YAML list of slugs | Workflow base or country skill this loads on top of. Each slug must be the `name` of a guide that exists under `skills/` — CI errors on a dangling one. The generated `foundation.md` is not a guide; name `workflow-base` instead. Every `US` and `US-<state>` guide also names `us-circular-230-disclosure`; only the sole-proprietor content skills name `us-tax-workflow-base` |
| `version` | numeric dotted value, e.g. `0.1` | Content version, bumped on substantive change when present. Keep any body-heading version in step |

## Sync integrity rules

`last_updated` and a numeric `version` are monotonic content metadata: an edit
must not decrease either value. A substantive body change should advance the
date, the version, or both, and a heading such as `v1.1` must agree with the
frontmatter version.

These values are content metadata, not synchronization tokens:
`scripts/check-sync-integrity.py --strict-metadata` fails a pull request whose
body edit advances neither, and nothing else reads them as a version.

## Category vocabulary

These nineteen values are the whole vocabulary; `scripts/validate-guides.py` errors on any other. The counts are the corpus on 2026-09-29, when every guide was given a value by one rule.

**The rule.** The topic wins where the guide's name states one: `payroll`, `crypto` (and `nft-tax`), `formation` (and `incorporation`), `bookkeeping`, `invoicing` (`einvoice`, `e-invoicing`), `tax-optimization` (and `tax-planning`), `transfer-pricing`, `financial-statements` (and `financial-reporting`), and `orchestrator` for an intake, router or return-assembly file wherever it lives. Otherwise the guide takes its tree's residual value: `international` for a country guide (income tax, VAT and GST, social contributions, corporate tax, withholding, estimated tax), `federal` under `skills/federal/` (`state-tax` for the 50-state matrices and the sales-tax guides there), `state-tax` under `skills/us-states/`, `cross-border` under `skills/cross-border/`, and the directory's own value under `skills/foundation/`, `skills/verticals/`, `skills/integrations/`, `skills/patterns/`, `skills/intelligence/`, `skills/templates/` and `skills/financial-reporting/` (which takes `financial-statements`). A guide is filtered by `jurisdiction` for its geography, so the category says what it is about.

| Category | What it means | Guides |
|----------|---------------|--------|
| `international` | Country-level tax computation: income tax, VAT and GST, social contributions, corporate tax, withholding | 991 |
| `payroll` | Withholding, social security, payslips | 189 |
| `formation` | Entity types, registration, compliance | 167 |
| `state-tax` | US state tax, and the 50-state matrices | 150 |
| `orchestrator` | Router, intake and return-assembly files | 61 |
| `tax-optimization` | Legal tax reduction strategies, timing, deductions | 49 |
| `cross-border` | Multi-jurisdiction coordination, treaties, WHT, the US expat set | 42 |
| `crypto` | Cryptocurrency and digital asset taxation | 32 |
| `federal` | US federal tax | 31 |
| `financial-statements` | Annual accounts, reporting, audit, and the accounting standards under `skills/financial-reporting/` | 30 |
| `invoicing` | E-invoicing format, validation, transmission | 24 |
| `bookkeeping` | Chart of accounts, P&L, balance sheet | 22 |
| `foundation` | Workflow bases (domain-agnostic) and the US Circular 230 disclosure | 19 |
| `transfer-pricing` | TP documentation, arm's length, CbCR | 17 |
| `vertical` | Industry-specific accounting patterns | 14 |
| `integration` | Platform export formats, column mappings | 10 |
| `pattern` | Global vendor and expense patterns (`skills/patterns/`) | 9 |
| `template` | File templates (`skills/templates/`, the corridor template) | 6 |
| `intelligence` | Deadline, threshold and optimisation engines (`skills/intelligence/`) | 3 |

The legacy synonyms (`federal-tax`, `state`, `us-states`, `financial-reporting`, `patterns`) were normalised on 2026-09-29 and are rejected in frontmatter. The MCP server's `list_skills` still accepts them as `category` filters, for callers written before the change, and returns the guides that carry the canonical value (`federal`, `state-tax`, `financial-statements`, `pattern`).

## Closing CTA block

Every published guide ends with the `<!-- openaccountants-cta-block -->` marker followed by exactly one "Talk to a verified accountant" section — the block below, verbatim. The marker is what makes a bulk re-stamp idempotent. CI errors on a guide with no marker (exempt: the template directories `skills/templates/` and `skills/cross-border/treaty-corridors/_templates/`, and the platform guides in `skills/integrations/`, which are not tax guides) and on a guide with more than one such section; `python3 scripts/normalize-cta-block.py --apply` repairs both and bumps `last_updated`. The canonical text lives in `scripts/cta_block.py`.

```markdown
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
```

## Template

---

```yaml
---
name: [country-or-topic]-[domain]
description: >
  [One paragraph: what this skill covers, entity types, jurisdiction, tax year.
  Include trigger phrases the AI should match. Be specific about scope.]
jurisdiction: XX   # REQUIRED — MT, GB, DE, US, US-CA, GLOBAL, INTL, EU-27, etc.
category: international   # see the category vocabulary above
tax_year: 2025             # bare integer = coverage start year
tax_year_notes: "2025-26"  # optional — only when a bare year can't express it
tier: 2                    # 1 = accountant-reviewed | 2 = source-cited draft
last_updated: 2026-07-04   # YYYY-MM-DD
version: 0.1
depends_on:
  - [workflow-base-or-country-skill]
verified_by: pending       # or "Name, Credential" — stored field name stays verified_by
---
```

# [Skill Name] v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Jurisdiction is required.** Set `jurisdiction:` in frontmatter even when the folder path implies it (e.g. `skills/international/malta/` → still use `jurisdiction: MT`). The validator requires it, and the package build and the MCP server use it to place the guide.

## What this file is

**This file is a content skill that loads on top of a workflow base** (e.g. `us-tax-workflow-base`, `crypto-tax-workflow-base`, `bookkeeping-workflow-base`).

[Describe: what it computes, where it fits in the pipeline, what it does NOT cover.
Reference the upstream skills it depends on and the downstream skills that consume its output.]

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers:

- [What forms and schedules]
- [What entity types — sole prop, SMLLC, etc.]
- [What line items or computations]

This skill does NOT cover:

- [What's out of scope — reference which other skills handle it]

---

## Section 2 — Filing requirements

[Who must file, thresholds, deadlines. Cite the state statute or IRC section.]

---

## Section 3 — Rates and thresholds

[All dollar amounts, percentages, phase-outs for the tax year.
Each figure must have a primary source citation.]

| Item | Amount | Source |
|------|--------|--------|
| [Rate/threshold] | [$X] | [Statute § or Notice] |

---

## Section 4 — Computation rules

[Step-by-step computation logic. This is the core of the skill.
Write it so Claude can execute it mechanically.]

### Step 1 — [Name]

[Rule with citation]

### Step 2 — [Name]

[Rule with citation]

---

## Section 5 — Edge cases and special rules

[Unusual situations, exceptions, elections, safe harbors.
Each with a citation.]

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] All input figures trace to source documents
- [ ] Rates and thresholds match the tax year
- [ ] Computation follows the steps in Section 4
- [ ] Edge cases from Section 5 are checked
- [ ] Output format matches the base skill spec

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
