# Frontmatter spec — the canonical reference

**This section is THE frontmatter spec for every skill/Guide file in this repo.** Other docs (`CLAUDE.md`, `CONTRIBUTING.md`) link here rather than restating it. CI enforces it: `scripts/validate-guides.py` hard-fails on malformed frontmatter, a missing `name`/`description`, a non-integer `tax_year`, a missing or invalid `tier` (must be 1 or 2), a missing or malformed `last_updated` (YYYY-MM-DD), a missing `jurisdiction` (except in a small allowlist of jurisdiction-agnostic directories, where it warns), a `depends_on` slug that no guide carries as its `name`, and a missing or duplicated closing CTA block (see [Closing CTA block](#closing-cta-block)).

## Required keys — CI fails without these

| Key | Format | Notes |
|-----|--------|-------|
| `name` | slug, `[country-or-topic]-[domain]`; unique across the repo. A US-state guide is `us-[state]-[topic]` and its file is `[name].md` | e.g. `malta-income-tax`, `us-ny-sales-tax` |
| `description` | 80-100 words | What it covers, entity types, jurisdiction, tax year, plus trigger phrases the AI should match |
| `jurisdiction` | ISO code | `MT`, `GB`, `DE`, `US`, `US-CA`, `GLOBAL`, `INTL`, `EU-27`. Required even when the folder path implies it. Quote `"NO"` because YAML 1.1 otherwise reads Norway's code as boolean `false`. A **warning**, not an error, inside the small allowlist of jurisdiction-agnostic directories |
| `tier` | `1` or `2` | `1` = **accountant-reviewed** (a named licensed accountant fully reviewed and signed off); `2` = **source-cited draft** (drafted from primary sources, awaiting review). These are the only two quality states |
| `last_updated` | `YYYY-MM-DD` | Date the content was last checked/edited. It must never move backwards |

## Expected, but not enforced

These two were previously listed as required. They are not: `scripts/validate-guides.py` does not test for their presence, and much of the corpus omits them. Write them on anything new, but do not treat their absence in an existing file as a validation failure — and do not bulk-add them to close a gap that CI never asserted.

| Key | Format | Notes |
|-----|--------|-------|
| `category` | one of the vocabulary below | Domain the skill covers. **Not checked by CI at all**, and absent from roughly two-thirds of the corpus (1,210 of 1,926 guides as at 2026-09-10), so a join on it silently drops most files. The count drifts as guides are edited — nothing keeps it honest, so re-measure before quoting it |
| `tax_year` | **bare integer**, e.g. `2025` | The **coverage start year**. CI checks the *format* when the key is present and errors on anything that is not an integer 2015-2035, but does not require the key — 72 guides omit it, mostly workflow bases that are genuinely year-agnostic. Ranges, fiscal calendars, and qualifiers ("2025-26", "YA 2026", "2567 (2024)") go in `tax_year_notes`, never here |

## Optional keys

| Key | Format | Notes |
|-----|--------|-------|
| `tax_year_notes` | quoted string | The human-readable tax-year label when a bare year can't express it: `"2025-26"`, `"FY 2026-27 (AY 2027-28)"`, `"2025 (with confirmed 2026 figures noted)"` |
| `verified_by` | `pending` or `Name, Credential` | e.g. `Michael Cutajar, CPA (Malta)`. Stored identifier — the field name stays `verified_by` even though the display language is "reviewed". A real name here does **not** imply `tier: 1`; set `tier: 1` explicitly as well. CI errors if `tier: 2` carries a real `verified_by` |
| `reviewed_by` | `Name, Credential` | The accountant who signed the guide off (e.g. `Christopher Aryee, CPA` on the `skills/federal/` form guides). On a `tier: 2` guide the name records an accountant who contributed corrections (usually a "Verified rates & thresholds" block) without signing the whole guide off; it does not make the guide reviewed |
| `review_status` | `current` or `pending_review` | Review **freshness**, not assurance: `current` means the recorded sign-off covers the current text; `pending_review` means the guide awaits review, either because it is a draft or because a substantive edit superseded the reviewed text (a `tier: 1` guide edited after its sign-off keeps `tier: 1` and takes `pending_review`, and `PARTNERS.md` counts it as "edited since review"). CI errors on any other value and on `current` with `tier: 2`, since no review promoted the guide |
| `depends_on` | YAML list of slugs | Workflow base or country skill this loads on top of. Each slug must be the `name` of a guide that exists under `skills/` — CI errors on a dangling one. The generated `foundation.md` is not a guide; name `workflow-base` instead |
| `version` | numeric dotted value, e.g. `0.1` | Content version, bumped on substantive change when present. Keep any body-heading version in step |

## Sync integrity rules

`last_updated` and a numeric `version` are monotonic content metadata: an edit
must not decrease either value. A substantive body change should advance the
date, the version, or both, and a heading such as `v1.1` must agree with the
frontmatter version.

These values are content metadata, not synchronization tokens:
`scripts/check-sync-integrity.py --strict-metadata` fails a pull request whose
body edit advances neither, and nothing else reads them as a version.

## Category vocabulary (the real one)

This is the vocabulary actually in use across the repo's guides (by count), not an aspirational list. Use these for new files:

| Category | What it means | Approx. usage |
|----------|---------------|---------------|
| `international` | Country-level tax computation (income tax, VAT, SSC) | ~757 |
| `foundation` | Universal workflow base (domain-agnostic) | ~198 |
| `orchestrator` | Router / intake / assembly files | ~110 |
| `federal` | US federal tax | ~104 |
| `payroll` | Withholding, social security, payslips | ~82 |
| `tax-optimization` | Legal tax reduction strategies, timing, deductions | ~64 |
| `cross-border` | Multi-jurisdiction coordination, treaties, WHT | ~54 |
| `transfer-pricing` | TP documentation, arm's length, CbCR | ~43 |
| `state-tax` | US state tax | ~40 |
| `formation` | Entity types, registration, compliance | ~39 |
| `financial-statements` | Annual accounts, reporting, audit | ~39 |
| `bookkeeping` | Chart of accounts, P&L, balance sheet | ~39 |
| `invoicing` | E-invoicing format, validation, transmission | ~30 |
| `crypto` | Cryptocurrency and digital asset taxation | ~30 |
| `vertical` | Industry-specific accounting patterns | ~28 |
| `integration` | Platform export formats, column mappings | ~20 |

Legacy synonyms still present in older files — do **not** use for new files: `federal-tax` (use `federal`), `state` / `us-states` (use `state-tax`), `financial-reporting` (use `financial-statements`), plus stragglers `template`, `pattern(s)`, `intelligence`.

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
