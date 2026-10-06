# Contributing to OpenAccountants (this fork)

Thanks for your interest in contributing. This is `ryanduguid/openaccountants`, a maintained fork of `openaccountants/openaccountants`; the [README](README.md) explains the relationship. Contributions land here through pull requests. There is no website submission form, no platform sync and no contributor licence agreement in this fork. A change you also want in the upstream project needs a separate pull request there, under upstream's own process.

## Who can contribute

Anyone. You don't need to be an accountant to write a skill. You need to know your country's rules well enough to cite the statutes — whether that's tax rates, payroll obligations, e-invoicing specs, or company formation steps. Licensed accountants can then review what you wrote (see [Review](#review)).

## How to contribute a skill

1. Fork this repo
2. Create your skill in the appropriate **source** directory (`skills/federal/`, `skills/us-states/[code]/`, `skills/international/[country]/`, etc.)
3. Follow the [skill template](docs/skill-template.md)
4. Regenerate the derived trees and commit them with your change (`make build`):
   `python3 scripts/build-packages.py && python3 scripts/build-index.py && python3 scripts/build-partners.py && python3 scripts/build-llms-full.py`
5. Open a PR with a description of what tax forms/schedules the skill covers

> **Important:** write in `skills/**`, never by hand in `packages/`, `index.json`, `PARTNERS.md` or `llms-full.txt` — those are generated. But do commit the regenerated copies: nothing else rebuilds them, and CI fails when the committed copies are stale (`guard-derived-trees` rebuilds `packages/`, `index.json` and `llms-full.txt`; the coverage gate re-renders `PARTNERS.md`). One exception: **`packages/us-federal/`** (the federal rates JSONs and their runbook) is hand-authored and may be edited directly. Renaming or deleting a guide needs an entry in `docs/guide-migrations.json` (`from`, `to` or null, `slug`, `replacement`) in the same change, with every reference repointed to the replacement slug; the sync-integrity gate fails an unrecorded deletion or rename.

## Repo layout

`skills/` is the editable source; `packages/` is generated from it by `scripts/build-packages.py` (each package holds its own files and lists the shared ones, which live once in `packages/_shared/`; the hand-authored `packages/us-federal/` holds the federal rates JSONs); `index.json` at the repo root is the machine-readable inventory of every Guide. The one-page canonical answer to "which file do I edit?" is [docs/REPO-LAYOUT.md](docs/REPO-LAYOUT.md).

## No website sync

This fork has no sync with openaccountants.com in either direction: nothing here publishes to the platform, and nothing on the platform writes into this repository. `jurisdiction:` in the frontmatter is still required (the validator checks it). Upstream's retired sync contract is kept for the record in [docs/archive/WEBSITE-SYNC.md](docs/archive/WEBSITE-SYNC.md).

## Skill structure and frontmatter

**The canonical spec for skill files — required/optional frontmatter keys, formats, the `category` vocabulary, and the body section order — is [docs/skill-template.md](docs/skill-template.md).** Don't restate it; follow it. CI validates required guide schema with `scripts/validate-guides.py` and synchronization metadata with `scripts/check-sync-integrity.py`; citation quality and body structure still require reviewer judgment. Two structural rules the validator also enforces: every `depends_on` slug must be the `name` of a guide that exists, and every guide ends with exactly one `<!-- openaccountants-cta-block -->` CTA section (`python3 scripts/normalize-cta-block.py --apply` repairs a missing or duplicated block; templates and `skills/integrations/` are exempt).

One-line summary: YAML frontmatter (`name`, `description`, `jurisdiction`, `category`, `tax_year`, `tier`, `last_updated`, plus optional keys), then a body that runs scope → filing requirements → rates with citations → step-by-step computation rules → edge cases → self-checks → disclaimer.

All domain skills for a country live in the same directory (e.g., `skills/international/germany/` contains tax, bookkeeping, payroll, formation, financial statements, transfer pricing, tax optimization, and e-invoicing). The build script detects them by filename suffix and bundles the appropriate workflow base automatically.

## Quality standards

- Every amount, percentage, and threshold must have a primary source citation (statute, tax authority guidance, or official rate schedule)
- Computation rules must be mechanical — the AI should be able to follow them step by step
- Scope must be explicit — what's covered and what's deferred to other skills
- **US skills** name `us-circular-230-disclosure` (in `skills/foundation/`, the scope-neutral Circular 230 disclosure) in `depends_on`: every guide whose `jurisdiction` is `US` or `US-<state>` does, and `scripts/validate-guides.py` errors on one that does not (the two US foundation files, the US GAAP guides under `skills/financial-reporting/` and the file templates are exempt). `us-tax-workflow-base` is the sole-proprietor workflow, with a refusal catalogue that excludes payroll, corporate and foreign taxpayers, so only the content skills written for that workflow load it
- **International skills** load on top of `foundation.md` + `intake.md` (generated by `build-packages.py`); in `depends_on`, name the source guide `workflow-base` (the universal base that `foundation.md` condenses), not the generated file
- **Income tax skills** (individuals, sole traders, freelancers) load on top of `income-tax-workflow-base` (in `skills/foundation/`); corporate income tax skills load on top of `corporate-income-tax-workflow-base`
- **Social contributions skills** load on top of `social-contributions-workflow-base` (in `skills/foundation/`)
- **Bookkeeping skills** load on top of `bookkeeping-workflow-base` (in `skills/foundation/`)
- **E-invoicing skills** load on top of `einvoice-workflow-base` (in `skills/foundation/`)
- **Payroll skills** load on top of `payroll-workflow-base` (in `skills/foundation/`)
- **Formation skills** load on top of `company-formation-workflow-base` (in `skills/foundation/`)
- **Financial statements skills** load on top of `financial-statements-workflow-base` (in `skills/foundation/`)
- **Transfer pricing skills** load on top of `transfer-pricing-workflow-base` (in `skills/foundation/`)
- **Tax optimization skills** are standalone — no separate workflow base; they follow the universal `workflow-base.md`
- **Crypto tax skills** load on top of `crypto-tax-workflow-base` (in `skills/foundation/`)
- **Cross-border skills** load on top of `cross-border-workflow-base` (in `skills/foundation/`)
- **Vertical skills** (industry-specific) and **integration skills** (platform-specific) are standalone in `skills/verticals/` and `skills/integrations/`
- Citation format: for US, cite IRC sections, state statutes, or IRS notices; for international, cite the relevant tax authority and legislation

## Where to put your files

### Quick reference — common cases

| You're writing… | Put it here | Example |
|-----------------|-------------|---------|
| Country-specific (Malta crypto, UK VAT, Germany payroll) | `skills/international/[country]/` | `skills/international/malta/mt-crypto-tax.md` |
| US federal | `skills/federal/` | `skills/federal/us-crypto-tax.md` |
| US state | `skills/us-states/[code]/` | `skills/us-states/ny/us-ny-it-201-resident-return.md` |
| Global / cross-border (not one country) | `skills/cross-border/` + `jurisdiction:` in frontmatter | `skills/cross-border/oecd-model-treaty-defaults.md` with `jurisdiction: INTL` |
| Industry vertical (developer, e-commerce) | `skills/verticals/` + `jurisdiction: GLOBAL` | `skills/verticals/freelance-developer.md` |
| Platform integration (Stripe, Xero) | `skills/integrations/` + `jurisdiction: GLOBAL` | `skills/integrations/stripe-integration.md` |
| If unsure | Same folder as related skills + **`jurisdiction: XX`** in frontmatter | `jurisdiction: JP`, `MT`, `GLOBAL`, `US`, `US-CA`, etc. |

**Rule:** Folder path is the primary signal. Frontmatter `jurisdiction:` is the backup — use it even when the folder makes it obvious.

### Full directory map

| What you're editing | Source directory |
|---------------------|-----------------|
| US federal skills | `skills/federal/` |
| US state skills | `skills/us-states/[two-letter code]/` |
| International country skills (all domains) | `skills/international/[country-slug]/` |
| Foundation workflow bases | `skills/foundation/` (bundled into packages by the build) |
| Cross-border / treaty corridor rules | `skills/cross-border/` (subdirectory `treaty-corridors/` for WHT rates) |
| Industry vertical skills | `skills/verticals/` |
| Platform integration skills | `skills/integrations/` |
| Financial reporting (IFRS / US GAAP treatment) | `skills/financial-reporting/` (bundled as `packages/_financial-reporting/`) |
| Transaction pattern libraries | `skills/patterns/` (bundled as `packages/_patterns/`) |
| Deadline engine, threshold alerts, optimisation advisor | `skills/intelligence/` (bundled as `packages/_intelligence/`) |
| Orchestrator files (router, intake, assembly) | `skills/orchestrator/` (a country's `<code>-freelance-intake.md` and `<code>-return-assembly.md` are copied into its package) |

After editing, run the generators (`make build`, or `python3 scripts/build-packages.py && python3 scripts/build-index.py && python3 scripts/build-partners.py && python3 scripts/build-llms-full.py`) and commit the regenerated `packages/`, `index.json`, `PARTNERS.md` and `llms-full.txt` together with your source change. CI rebuilds them and fails on any difference; `python3 scripts/validate-guides.py --derived-only` and `python3 scripts/check-coverage-claims.py` run the same checks locally.

If you add a `references.md` to a country's source directory, it will be included in the generated package automatically.

## Reproduce CI locally

Every check CI runs has a `make` target, so a green `make check` means a green pull request:

```
python3 -m pip install -r requirements-dev.txt   # or: make install
make check                                       # validate + sync-check + test: everything CI gates
```

`requirements-dev.txt` installs PyYAML (the only dependency the generators and the validator have), pytest, openpyxl (the workbook tools) and the MCP server in editable mode. CI installs only `scripts/requirements-validation.txt` plus `./mcp`, per job.

| Target | What it runs | CI job |
|---|---|---|
| `make build` | the four generators: `scripts/build-packages.py`, `scripts/build-index.py`, `scripts/build-partners.py`, `scripts/build-llms-full.py` | none: you commit the output |
| `make validate` | `scripts/validate-guides.py`: the frontmatter contract and derived-tree freshness | `validate.yml` |
| `make sync-check` | `scripts/check-sync-integrity.py --mode audit --strict-metadata` from the merge base with `origin/main` (fetch it first, or pass `BASE=<rev>`) | `sync-integrity.yml`, `compare` |
| `make checkers` | the six gate checkers (`check-arithmetic.py`, `check-bracket-tables.py`, `check-expired-rules.py`, `check-fact-conflicts.py`, `check-coverage-claims.py`, `check-sourcing-floor.py`) against `scripts/baselines/`, plus `check-cited-hosts.py --selftest` | `validate.yml`, `gate-checkers` |
| `make baselines` | rewrites the four baselines from the current tree, for use after reading the findings your change added or fixed | none: you commit the result |
| `make test` | `unittest discover` over `tests/` and `mcp/tests/` | `sync-integrity.yml`, `unit-tests` |
| `make check` | `validate`, `sync-check`, `checkers` and `test` | all of the above |

A gate checker fails on a finding its baseline does not list and on a baseline entry that no longer reproduces. If your change fixes an arithmetic error, a repeated bracket rate, an expired rule or a conflicting figure, its baseline entry goes stale: run `make baselines` and commit the smaller file. If your change adds a finding, fix the guide, or, when you have read the finding and it is a false positive, record it the same way and say so in the pull request. `CLAUDE.md` ("Checks") has the details and the flags each checker takes (`--json`, `--baseline`, `--no-baseline`, `--update-baseline`).

`make help` lists the targets. Without `make` (Windows), run the commands the table names: `make -n <target>` prints them exactly. In Windows PowerShell, set `$env:PYTHONUTF8 = "1"` before running checks with redirected output so they can print Unicode guide text. Run everything from the repository root; the review aids under `scripts/` resolve paths relative to the working directory and report nothing from anywhere else.

Shared code for the scripts lives in `scripts/oa_tools/` (repository paths, guide discovery, the frontmatter reader in tolerant and strict form). A hyphenated script name cannot be imported, so put anything two scripts need there rather than copying it; each script puts its own directory on `sys.path` before importing it, which is what lets the tests load scripts by file path.

## Review

Pull requests are reviewed here, on GitHub. A guide is a **source-cited draft** (`tier: 2`) until a named, licensed accountant has reviewed the complete guide and signs it off in a pull request that sets `tier: 1` and puts their name and credential in `reviewed_by`; see [docs/QUALITY-TIERS.md](docs/QUALITY-TIERS.md). Maintainers do not set `tier: 1` on anyone's behalf, and a reviewer name on a `tier: 2` guide does not make it reviewed.

## Versions and tags

[CHANGELOG.md](CHANGELOG.md) keeps one version line, the repository's; the MCP server package has its own in [mcp/CHANGELOG.md](mcp/CHANGELOG.md). Work lands under `## [Unreleased]`. A release moves those entries under a `## [X.Y.Z] — YYYY-MM-DD` heading, merges, and tags the merge commit on `main`:

```
git tag -a vX.Y.Z <merge commit> -m "X.Y.Z" && git push origin vX.Y.Z
```

Bump the major version when a slug, a path under `skills/` or the `packages/` layout changes (consumers pin those), the minor version for new guides or tooling, the patch version for corrections alone. A guide's own `version:` is per file and unrelated.

## Licensing of contributions

This is a mixed-licence repository: software is **AGPL-3.0-only** and the Guides are under the source-available **OA Guide License** (see [LICENSING.md](LICENSING.md)). This fork does not collect a contributor licence agreement. By opening a pull request you confirm that the contribution is your own work or that you have the right to submit it, and you agree that it is licensed under the licence of the files it changes: AGPL-3.0-only for software, the OA Guide License for guides and their exports. You keep your copyright. [CLA.md](CLA.md) is the upstream project's agreement with Glimpse Ltd, kept for reference; it is not collected here and does not apply to contributions made to this fork.

## Credit

Your name is on the commit and the pull request. A reviewer's name goes in the guide's frontmatter as described under [Review](#review).
