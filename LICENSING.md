# Licensing

OpenAccountants is a **mixed-licence repository**. Two different licences apply,
depending on whether a file is *software* or a *tax Guide*.

## Which licence applies to what

| Files | Licence | Text |
|-------|---------|------|
| Software, tooling, docs, and project metadata — `mcp/`, `scripts/`, `tools/`, `plugins/`, `.claude-plugin/`, `docs/`, `.github/`, `Dockerfile`, and root config/meta files | **AGPL-3.0-only** | [`LICENSE`](LICENSE) / [`LICENSES/AGPL-3.0-only.txt`](LICENSES/AGPL-3.0-only.txt) |
| Tax Guides and their machine-readable exports — `skills/`, `packages/`, `workflows/`, `index.json`, `llms.txt`, `llms-full.txt` | **OA Guide License** (source-available) | [`LICENSES/LicenseRef-OA-Guide-License-1.0.txt`](LICENSES/LicenseRef-OA-Guide-License-1.0.txt) |
| The guides listed under [Guides under FSL-1.1-ALv2](#guides-under-fsl-11-alv2), with their copies under `packages/` | **FSL-1.1-ALv2** (source-available) | [`LICENSES/FSL-1.1-ALv2.txt`](LICENSES/FSL-1.1-ALv2.txt) |

The machine-readable exports (`index.json`, `llms.txt`, `llms-full.txt`)
reproduce the Guides, so they carry the **Guide License** — otherwise the Guide
content could be taken via the export while ignoring the licence.

This mapping is recorded for tooling in [`REUSE.toml`](REUSE.toml) following the
[REUSE](https://reuse.software) specification.

## What each licence means, in plain terms

**Software (AGPL-3.0-only).** You can use, modify, and self-host the MCP server
and tooling. If you run a modified version as a network service, AGPL requires
you to offer users its source. Commercial use is allowed; a separate commercial
licence is available if AGPL does not fit ([COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)).

**Guides (OA Guide License).** Free to read, use for your own taxes, use as a
professional reference for client work, quote, teach from, and contribute back.
A **separate commercial licence is required** to embed the Guides in a
commercial AI product, index them for commercial RAG, train models on them,
bulk-extract or redistribute the collection, or run a competing hosted Guide
service. Contact **info@openaccountants.com**.

## Why the repo is no longer "purely" open source

The Guides are the work that took the most effort and are the easiest to lift
wholesale into a proprietary AI product. Keeping the *code* open (AGPL) while
placing the *Guides* under a source-available licence is the deliberate,
supported way to keep the infrastructure open while controlling commercial reuse
of the content. GitHub may therefore report this repository as AGPL-3.0 with
additional/unknown licences — that is expected for a mixed-licence repo.

## Contributions

Contributions to this fork are accepted under the licence of the files they
change: AGPL-3.0-only for software, the OA Guide License for Guides and their
exports. Contributors keep their copyright. The upstream project's
[Contributor License Agreement](CLA.md), which grants Glimpse Ltd the right to
distribute contributions under both the AGPL and the Guide/commercial tracks,
governed the contributions made to upstream and is kept here for reference;
this fork does not collect it and cannot grant commercial licences to the
Guides, which remain Glimpse Ltd's to license.

## Third-party copyleft material

Some Guides under `packages/` incorporate third-party material made available
under a copyleft licence (AGPL-3.0 / GPL-3.0), with attribution (see the
`references.md` and provenance sections, e.g. Turkey, France, Poland, Brazil, and
several Canadian provinces). Copyleft material cannot be relicensed: any Guide
that contains or derives from it **remains under its original AGPL/GPL terms**,
notwithstanding the general mapping above. Apart from these and the guides under
FSL-1.1-ALv2 below, the Guide License applies to the rest of the Guides, which
are Glimpse Ltd's own work, work-for-hire, or covered by an accepted
[CLA](CLA.md).

## Guides under FSL-1.1-ALv2

The guides below were adapted by their author, Ryan Duguid, from his
repositories `ryanduguid/australian-accounting-skills` and
`ryanduguid/llm-tax-guardrails`, and remain under the Functional Source
License, Version 1.1, ALv2 Future License
([`LICENSES/FSL-1.1-ALv2.txt`](LICENSES/FSL-1.1-ALv2.txt)), notwithstanding the
general mapping above. That licence grants an additional Apache License 2.0
licence for each version from the second anniversary of the date it is made
available. Their copies under `packages/`, and any of their text reproduced in
the machine-readable exports, carry the same terms. Each guide states its
licence in its `license` front matter and keeps its copyright notice at the end
of its Sources section. `REUSE.toml` records the same paths.

- `skills/foundation/au-tasa-code-disclosure.md`
- `skills/international/australia/au-coal-lsl-levy.md`
- `skills/international/australia/au-director-penalties.md`
- `skills/international/australia/au-employee-share-schemes.md`
- `skills/international/australia/au-fuel-tax-credits.md`
- `skills/international/australia/au-managed-funds-amit.md`
- `skills/international/australia/au-objections.md`
- `skills/international/australia/au-primary-production.md`
- `skills/international/australia/au-private-rulings.md`
- `skills/international/australia/au-property-development.md`
- `skills/international/australia/au-restructure-rollovers.md`

## Effective date and prior releases

This structure is introduced on **2026-07-16**. Guide versions previously
distributed under AGPL-3.0 remain available under AGPL-3.0 for the copies already
distributed; this change is forward-looking and does not purport to revoke rights
already granted (see § 9 of the Guide License).
