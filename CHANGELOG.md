# Changelog

All notable changes to OpenAccountants will be documented in this file.

## [Unreleased]

### Changed
- **US-state guides live in the `us-<code>-` namespace.** Twenty-one state codes are also ISO country codes in use here, so `de-income-tax` was Delaware and Germany, `ar-`, `co-` and `ma-income-tax` likewise, and the MCP catalogue dropped all four rather than guess; four more slugs were carried by two files inside one state folder. Every state guide's `name` and file are now `us-<code>-<topic>` (`us-ny-sales-tax`), the namespace the packages (`us-ny/`), the jurisdiction codes (`US-NY`) and the state orchestrators already used: 172 slugs renamed, every `depends_on` and prose reference repointed, and each guide whose body changed had its `last_updated` or `version` advanced under the strict-metadata rule. `scripts/validate-guides.py` now errors on a duplicate `name` anywhere in the tree and on a state guide outside the namespace; `mcp/tests/test_catalogue_integrity.py` reads the committed tree and fails on any ambiguous or duplicate slug (1,810 slugs, none dropped). Six state guides that sat unpackaged in `skills/orchestrator/` (California's LLC fee and PTE tax, New York's payroll, PTET and Article 9-A, Texas's margin tax) moved into their state folders and are packaged for the first time.
- **Deleting or renaming a guide is recorded.** `scripts/check-sync-integrity.py --strict-metadata` refused every deletion or rename under `skills/` with "requires an explicit human-reviewed migration" and offered no way to provide one. `docs/guide-migrations.json` is that record: one entry per path (`from`, `to` or null, `slug`, `replacement`), reviewed in the pull request that adds it; the gate accepts a deletion or rename that the change adds to the record (an entry already present at the base authorises nothing, so a guide recreated at a migrated path needs its own review), requires a recorded move's destination to be a guide in the candidate, and still applies the metadata rules to a renamed guide whose body changed. This migration's 275 entries are the first.
- **The alias country folders are merged.** `uae` (six guides, among them the tier-1 `uae-vat`) joined `united-arab-emirates`, `bvi` joined `british-virgin-islands`, `im` joined `isle-of-man`, the 16 provincial guides in the mis-slugified `ca-chartered-accountant` joined `canada/<province>/`, `cura-ao` and `s-o-tom-and-pr-ncipe` are `curacao` and `sao-tome-and-principe`, and the three federal-level guides in `international/us` (capital gains, non-resident CGT, tax residency) joined `skills/federal/` and are shared into every US package. `packages/us/` is now an index of the 51 state packages, like `packages/canada/`. `build-packages.py` takes a folder's code from the jurisdiction its guides declare when `DIR_TO_CODE` lacks it, instead of its first two letters: `british-virgin-islands` had been titled "Brazil".
- **`packages/` no longer repeats a file per package.** A file that several packages need (the universal `foundation.md`, the workflow bases from `skills/foundation/`, the US federal set from `skills/federal/`, the federal Canadian set, the core orchestrators, the EU VAT base) is written once to `packages/_shared/`, and each package folder holds only its own files. 3,696 of the 5,954 markdown files under `packages/` were such copies: a one-line edit to a base touched up to 170 of them, and the federal set stood in the tree 51 times over. Each package's `README.md` now lists the shared files it needs, `packages/bundles.json` records the same composition for tools (`{package: {jurisdiction, name, files, shared}}`), and `scripts/build-bundle.py` (`make bundle JURISDICTION=<package>`) assembles a package and its shared files into one upload-ready folder under `dist/bundles/`. `packages/_shared/README.md` states each file's source and how many packages list it. The MCP server catalogues the shared files under their declared jurisdictions, so no slug changed jurisdiction; a shared guide that declared none would be `GLOBAL`, never the code its neighbours declare most. `build-packages.py --us-only` is gone (a partial build cannot describe the whole tree) and an unknown option is now refused; `skills/cross-border/README.md` and `skills/verticals/README.md` are no longer copied into the bundles as if they were guides. `tests/test_build_bundle.py` pins the assembler and, on the committed tree, that every listed file exists, every package file is listed, every shared file is used and no guide is checked in twice.

### Removed
- **60 duplicate guides**, each in favour of the reviewed, versioned or newer copy, with every reference repointed and each pair recorded in `docs/guide-migrations.json`: 24 code-prefixed VAT/GST twins in country folders (`ch-vat-return` beside `switzerland-vat` and the like, each a re-export of its full-name sibling with the slug as its H1; the kept copies include the tier-1 `uae-vat`, `portugal-vat-return` and `india-gst`); 26 full-name state files that had a code-prefixed sibling (`alabama-sales-tax.md` beside `al-sales-tax.md`); the three same-slug pairs inside one state folder (Florida sales and use tax keeps Rob Hoffman's tier-1 copy; Texas and Washington keep the v1.0 copies); the `ny-nyc/` copy of the NYC UBT guide, which no package built (the `US-NY-NYC` code goes with it); and six copies of state guides under `skills/orchestrator/` that no package built. The index counts 1,867 guides across 243 jurisdictions; the 164 accountant-reviewed are unchanged.
- **The 28 hand-authored twins in `packages/us-federal/`.** Every one duplicated a `skills/federal/` guide of the same name, and the index listed both under one slug, so the 1,955 guide count carried 28 twins. `packages/us-federal/` held all 28 as `tier: 2` with `verified_by: pending`; `skills/federal/` holds seven of them as `tier: 1` reviewed by Christopher Aryee, CPA, and the other 21 as `tier: 2` with a named reviewer. The MCP server served the `us-federal` copy by precedence, so a client got the older, lower-tier text. Where the pairs disagreed on a labelled value, `skills/federal/` was the more current (the 2026 OBBBA estate column, the §174A wording, the post-OBBBA §250 percentage); the one figure only `us-federal` stated, the GILTI and NCTI effective rates, is ported into `skills/federal/us-gilti-fdii-beat.md` (v1.1). `packages/us-federal/` keeps `rates.2025.json`, `rates.2026.json` and `ANNUAL-UPDATE-RUNBOOK.md`, still hand-authored and still guarded against deletion; the validator now allows deleting a guide there only when `skills/federal/` holds a file of the same name. `scripts/check-tree-divergence.py` and `scripts/check-federal-tree-drift.py`, which compared the two trees, go with them. The index now counts 1,927 guides; the 164 accountant-reviewed are unchanged, because the twins were never the reviewed copies.
- **`agent-skills/`**, the hand-maintained third copy of the guides in the Agent Skills (`SKILL.md`) format, together with `scripts/check-agent-skills-drift.py`, which measured how far it had drifted. Its README said it was generated by a `scripts/build-agent-skills.py` that never existed in this tree. 780 of its 781 folders duplicated a `skills/` guide at a fraction of the length; its labels called 13 guides accountant-reviewed where `skills/` records 94 of the same guides as `tier: 1`; nothing in this fork consumed it (the README, `START-HERE.md`, `llms.txt`, the MCP server and the plugin manifests never mentioned it); and every fact fix had to be written twice, which 20 commits since 2026-09-09 did by hand. `skills/` is the source and `packages/` the generated bundles. An Agent Skills export can be generated from `skills/` if a consumer appears; the last revision carrying the old tree is the parent of this change. The four Pakistan guides that told maintainers to mirror a correction into the tree lose that note, and the checkers that scanned or compared it (`check-cited-hosts.py`, `check-tree-divergence.py`, `check-guide-references.py`) now cover `skills/` alone.

## [0.3.0] — 2026-09-28 (mcp package version)

> Tracks the `openaccountants-mcp` package version. `mcp/pyproject.toml` and `mcp/server.json` have carried 0.3.0 since the surface rewrite of 2026-05-25 without an entry here; this one covers everything in the self-hosted MCP server since 0.2.0.

### Honest about missing content
- **A server with no guides now says so.** A wheel built from this tree ships only the server code, so a non-editable `pip install ./mcp` (or any install not pointed at a checkout) used to serve an empty catalogue as if it were the corpus: `list_skills` answered `total: 0` and `start(intent, jurisdiction)` answered `status: "ready"` with nothing to load. The server now logs a warning when it builds the catalogue and `packages/` is missing or holds no skill files, and every tool reports it: `list_skills` / `search_skills` return an `error` field, `start` returns `status: "error"`, and `get_skill` / `get_skill_sections` raise with the same message (the directory it looked in, plus the fix: set `OPENACCOUNTANTS_ROOT` to a checkout, or install the server editable from one; the working directory is never consulted). An empty `OPENACCOUNTANTS_ROOT` counts as unset instead of resolving to the working directory.
- **Host/Origin validation for HTTP binds beyond loopback.** New `MCP_ALLOWED_HOSTS` / `MCP_ALLOWED_ORIGINS` (comma-separated, `:*` accepts any port) are passed to FastMCP as `transport_security`, so a spoofed `Host` gets HTTP 421 and a disallowed `Origin` HTTP 403. FastMCP only does this on its own for loopback binds; the server now warns at startup when `MCP_HOST` is not loopback and no allow-list is set. The Docker image defaults both to the localhost patterns its documented `-p 127.0.0.1:8000:8000 -e MCP_HOST=0.0.0.0` recipe needs.
- **Metadata that validates.** `mcp/server.json` now satisfies the registry schema it references (100-character `description`, `websiteUrl` instead of the unknown `homepage`, `repository.subfolder`); `openaccountants_mcp.__version__` exists; the AGPL-3.0-only text ships in the wheel (`mcp/LICENSE`, `license-files`). A test pins the three version numbers, the schema constraints, the licence file and this changelog entry together.
- **Docs and plugin corrected.** `mcp/README.md` no longer claims the wheel bundles the guides or that `packages/ca-*` is not checked in; counts, the California example (`ca-540-individual-return`, federal guides under `US`) and the Canadian filter (`CA`) match the catalogue; a note explains what this fork does and does not operate. The Claude Code plugin called a `start_help()` tool that never existed and pointed at the hosted endpoint this fork does not run; it now uses `start()` and the self-hosted stdio command, and drops the hosted-only `request_accountant_review`. The smoke test checks catalogue invariants instead of a `> 300` floor against ~1,835 skills.

### Since 0.2.0 (already shipping as 0.3.0)
- Tool surface brought to parity with the hosted server: `list_skills`, `get_skill` (with provenance footer), `get_skill_sections`, `search_skills`, the six prompts, then `start` (guided front door) and `submit_feedback` (pre-filled GitHub issue URL), with `next_action` steering and compute guardrails on every read tool.
- HTTP transports (`MCP_TRANSPORT`, `MCP_HOST`, `MCP_PORT`, `MCP_STREAMABLE_HTTP_PATH`) and a root `Dockerfile`; the HTTP listener binds loopback unless told otherwise.
- Quality tier fails closed: only an explicit `tier: 1` plus a named reviewer reports as accountant-verified; `verified_by: pending` and reviewer names on tier-2 guides no longer do, and a tier-2 reviewer is not exposed as `verified_by`.
- Deterministic catalogue: malformed frontmatter is salvaged instead of dropping the guide, byte-identical package aliases collapse to one entry, `packages/us-federal/` wins over generated copies, and slugs whose packaged copies differ are omitted with a logged warning that `start` also surfaces (`python -m openaccountants_mcp.duplicate_slug_report` lists them). Catalogue reads are contained to `packages/`.
- `mcp` SDK dependency capped below 2.0 (2.x removes `mcp.server.fastmcp`).

## [2.3.0] — 2026-07-16

### Mixed-licence restructure (Guides move to a source-available licence)

- **Split code from content.** Software (`mcp/`, `scripts/`, `tools/`, `plugins/`) is now **AGPL-3.0-only**; the Guides (`skills/`, `packages/`, `workflows/`, `index.json`, `llms*.txt`) move to the new source-available **OA Guide License** (`LICENSES/LicenseRef-OA-Guide-License-1.0.txt`). Commercial embedding / RAG / model-training / bulk redistribution of the Guides now requires a commercial licence. See [`LICENSING.md`](LICENSING.md).
- **Removed `LICENSE-ADDITIONAL.md`** (the Section 7 output-attribution additional term), which was causing GitHub to report "unknown licenses" and reached beyond what GPL §7 reliably permits.
- **Standardised on `AGPL-3.0-only`** (was a mix of `AGPL-3.0` / `AGPL-3.0-or-later`) across `glama.json`, `mcp/pyproject.toml`, `CITATION.cff`, and the plugin manifest.
- **Renamed** `COMMERCIAL_LICENSE.md` → `COMMERCIAL-LICENSING.md` and rewrote it for the two-track model.
- **Added `REUSE.toml`** for machine-readable per-path licence mapping.
- **Added a CLA status check** (`.github/workflows/cla.yml`).

> **Note:** Guides that incorporate third-party AGPL/GPL material remain under those copyleft terms; the Guide License applies to the rest (see [`LICENSING.md`](LICENSING.md) § "Third-party copyleft material").

## [2.2.0] — 2026-07-04

### Metadata everywhere, docs that agree with each other

- **Complete frontmatter metadata on all 1,007 Guides**, with strict CI enforcement so a Guide can no longer merge with missing or malformed frontmatter ([PR #54](https://github.com/openaccountants/openaccountants/pull/54)).
- **Docs coherence pass**: one canonical frontmatter spec that all contributor docs point at, plus community health files ([PR #53](https://github.com/openaccountants/openaccountants/pull/53)).
- **UK Guides gained structured rate tables**, and the README got an animated demo ([PR #51](https://github.com/openaccountants/openaccountants/pull/51)).
- **`tax_year` normalized** to one consistent format across every Guide ([PR #52](https://github.com/openaccountants/openaccountants/pull/52)).

## [2.1.0] — 2026-07-04

### First professional OBBBA review: 33 corrections by Christopher Aryee, CPA

A licensed US CPA reviewed the four core US federal form Guides (1040, 1120, 1065, 1041) against the One Big Beautiful Bill Act and returned 33 sourced corrections: rates, thresholds, and statutory citations. All applied in [PR #45](https://github.com/openaccountants/openaccountants/pull/45), with the full red-line public. Highlights: §174A domestic R&D immediate expensing, §163(j) EBITDA add-back restored, new permanent GILTI/FDII rates, §6698 penalty $255, §199A stays 20%, SALT $40k cap, §1202 phased exclusion. Each Guide now carries `reviewed_by: Christopher Aryee, CPA` and a changelog.

### Repo overhaul (trust + machine-readability)

- **`index.json`** at repo root: machine-readable inventory of every Guide (slug, jurisdiction, tier, reviewed_by, last_updated), generated by `scripts/build-index.py`.
- **CI validation** (`.github/workflows/validate.yml`): frontmatter checks, index freshness, and a guard against deleting the hand-authored `packages/us-federal/` on every PR.
- **Fixed a data-destruction bug** in `scripts/build-packages.py`: a full rebuild used to wipe `packages/us-federal/` (which has no generator) — it is now protected.
- **`llms.txt` corrected** (its repo map was wrong) and **`llms-full.txt` added** for AI crawlers; `CLAUDE.md` gained a "for AI agents landing here" fast path.
- **One source-of-truth story** across CONTRIBUTING/CLAUDE/llms/docs: `skills/` is the editable source, `packages/` is generated from it, `packages/us-federal/` is hand-authored. See `docs/REPO-LAYOUT.md`.
- README rebuilt: honest quality states (source-cited draft / accountant-reviewed), Partners table with public proof links, 2-step install, reconciled counts.
- Internal strategy drafts removed from `docs/`; vestigial folders pruned.

## [0.2.0] — 2026-05-22 (mcp package version)

> Tracks the `openaccountants-mcp` PyPI package version. The repo as a whole is on v1.x; this entry summarises the changes that ship with the v0.2.0 MCP release.

### New universal cross-border skills (13)
- `pillar-two-globe-minimum-tax` — OECD GloBE 15% minimum tax (IIR, UTPR, QDMTT, SBIE, safe harbours)
- `dac6-mdr-reportable-arrangements` — EU DAC6 + UK MDR + OECD model
- `fatca-crs-automatic-exchange` — FATCA + CRS + DAC2 + CARF/DAC8
- `cbam-carbon-border-adjustment` — EU Carbon Border Adjustment Mechanism
- `digital-services-tax-matrix` — 25+ in-force DSTs incl. Canada DST 2024
- `ifrs-local-gaap-reconciliation` — IFRS ↔ US GAAP / HGB / FRS 102 / OIC / PCG / Ind AS / ASBE / J-GAAP / CPC / ASPE
- `saf-t-realtime-ereporting-matrix` — SAF-T + global e-invoicing + EU ViDA
- `ip-patent-box-matrix` — 18+ IP regimes with OECD MNA mechanics
- `free-zones-sez-matrix` — 50+ zones across UAE, Saudi, China, India, LatAm, EU, Africa
- `rd-tax-credits-matrix` — 25+ R&D regimes incl. UK merged RDEC, US §174
- `wealth-tax-matrix`, `inheritance-estate-gift-matrix`, `stamp-duty-matrix`, `property-transfer-tax-matrix`, `tax-controversy-map-apa`

### New foundation workflow bases (5)
Corporate income tax, statutory audit, customs/duties, excise, wealth/estate.

### New sector verticals (8)
Banking, insurance, shipping/aviation tonnage tax, funds/REITs, oil & gas, charity/nonprofit, SaaS/digital, construction.

### New pattern library files (4)
Global cloud infrastructure, productivity tools, ad platforms, marketplaces + banking fees.

### Canada split
Canada is now split into 13 per-province/territory packages (`packages/ca-ab/` through `packages/ca-yt/`) mirroring the US-state model. Three new territory skills added (Yukon, NWT, Nunavut). `packages/canada/` is now a thin index page.

### Quality tier simplification
Collapsed from four tiers (Q1-Q4) to two: **accountant-verified** and **research-verified**. `docs/QUALITY-TIERS.md` rewritten. Manifest at `skills/manifest.json` regenerated by new `scripts/build-skills-manifest.py` (auto-derives quality from skill frontmatter).

### Usability
- New `START-HERE.md` with 17 persona-driven scenarios routing users to the right files
- Domain index READMEs added in `skills/cross-border/`, `skills/verticals/`, `skills/foundation/`, `skills/patterns/`
- Top-level README updated with prominent "Start here" section

### Infrastructure docs
- `docs/TEMPORAL-VERSIONING-SPEC.md` — schema for time-bounded tax rates (Level 3 of intelligence roadmap)
- `docs/CORRECTION-FEEDBACK-LOOP-SPEC.md` — practitioner correction capture & moat-building (Level 6)

### License
LICENSE split — canonical AGPL-3.0 stays in `LICENSE`, custom Section 7 attribution + commercial licensing terms moved to `LICENSE-ADDITIONAL.md`. Restores GitHub auto-detection. `glama.json` now declares the SPDX identifier explicitly.

### Totals
- 748 skill files (up from 713)
- 199 packages (51 US states + 13 Canada + 132 international + 3 special)

---

## [1.0.0] — 2026-04-14

### The initial release

**371 tax skills across 134 countries.** Upload to any LLM with your bank statement.

#### Skills
- 185 consumption tax skills (VAT/GST/sales tax) — verified against tax authority websites
- 45 income tax skills — brackets, deductions, transaction pattern libraries
- 50 social contribution skills — SSC/NIC/pension/health with payment pattern libraries
- 14 estimated tax skills — advance payments, provisional tax, quarterly instalments
- 5 cross-border skills — reverse charge, withholding tax matrix, PE risk, OSS, exports
- 5 transaction pattern files — 120+ global vendor patterns for instant classification
- 3 intelligence skills — deadline engine, threshold alerts, optimisation advisor

#### End-to-end jurisdictions
Complete guided experience (intake → classification → computation → assembly → review):
Malta, United Kingdom, Germany, Australia, Canada, India, Spain, United States (California)

#### Architecture
- Per-jurisdiction packages in `packages/` — self-contained, upload to any LLM
- Universal foundation + intake (same for every country)
- Country-specific content skills with local supplier/transaction pattern libraries
- Malta v2.0 structure: tiers as sections (Classified/Assumed/Needs Input), not inline tags
- Build script generates packages from source skills

#### Quality
- **Accountant-verified**: Malta VAT/IT/SSC, Germany VAT, US federal bookkeeping/SE
- **Research-verified**: everything else — drafted from authoritative sources (tax-authority publications and primary legislation), awaiting credentialed sign-off
- Deep research caught 200+ errors across 100+ countries during research verification
