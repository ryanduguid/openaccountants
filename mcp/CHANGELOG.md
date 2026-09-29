# Changelog: openaccountants-mcp

The self-hosted MCP server in this directory, versioned separately from the
repository ([../CHANGELOG.md](../CHANGELOG.md) is the repository's line).
`openaccountants_mcp.__version__`, `pyproject.toml` and `server.json` carry the
same number, and `tests/test_metadata.py` fails when this file has no entry for
it. The PyPI release of this name is upstream's, built from a separate
repository; nothing here publishes to PyPI.

## [0.4.0] — 2026-09-29

### Paged, ranked, cached
- **`list_skills` pages.** New `limit` (1 to 1,000, default 100) and `offset` parameters; the response carries `total` (every skill the filters match), `returned`, `offset`, `limit` and `next_offset` (None on the last page), and `next_action` names the offset of the next page. An unfiltered call used to answer every skill in one 360 KB response.
- **`category` is compared case-insensitively**, as `jurisdiction` already was.
- **`search_skills` ranks from a cached corpus and caps its query.** The body of every catalogued skill is read once per process, kept with its lower-cased copy (about 33 MB each) and cleared with the catalogue, so a search no longer re-reads and re-parses 1,800 files (1.6 s per query before, tens of milliseconds now); the count and the snippet of a result come from that one snapshot, never from the live file. Results are ranked by how often the query occurs, a title match first, and carry `matches`; the response reports `total` (every skill that matches) beside the 25 `returned`. A query longer than 200 characters is refused.
- **The catalogue is the index.** `tests/test_catalogue_integrity.py` reads the repository's `index.json` and fails when an indexed guide is missing from the catalogue (the documented exclusions aside: the file templates, the state references file, and a workflow base no guide declares) or a catalogued slug is missing from the index. Until 2026-09-29 the build left 57 indexed guides out of `packages/`; the catalogue now holds 1,854 skills from 1,865 indexed guides, the three new `_financial-reporting`, `_patterns` and `_intelligence` bundles among them.
- **Container image.** The base image is pinned by digest (Dependabot proposes bumps); the dependencies are installed from `pyproject.toml` in their own layer before the package is copied; the server runs as an unprivileged `app` user; a `HEALTHCHECK` runs `python -m openaccountants_mcp.healthcheck`, healthy once the listener answers; the build context holds only `mcp/` and `packages/`; and the image sets `MCP_HOST=0.0.0.0` behind its localhost allow-list, so `docker run -p 127.0.0.1:8000:8000` works without an extra flag.
- The server's instructions no longer claim "130+ countries".

## [0.3.0] — 2026-09-28

> `pyproject.toml` and `server.json` carried 0.3.0 since the surface rewrite of 2026-05-25 without an entry; this one covers everything since 0.2.0.

### Honest about missing content
- **A server with no guides now says so.** A wheel built from this tree ships only the server code, so a non-editable `pip install ./mcp` (or any install not pointed at a checkout) used to serve an empty catalogue as if it were the corpus: `list_skills` answered `total: 0` and `start(intent, jurisdiction)` answered `status: "ready"` with nothing to load. The server now logs a warning when it builds the catalogue and `packages/` is missing or holds no skill files, and every tool reports it: `list_skills` / `search_skills` return an `error` field, `start` returns `status: "error"`, and `get_skill` / `get_skill_sections` raise with the same message (the directory it looked in, plus the fix: set `OPENACCOUNTANTS_ROOT` to a checkout, or install the server editable from one; the working directory is never consulted). An empty `OPENACCOUNTANTS_ROOT` counts as unset instead of resolving to the working directory.
- **Host/Origin validation for HTTP binds beyond loopback.** New `MCP_ALLOWED_HOSTS` / `MCP_ALLOWED_ORIGINS` (comma-separated, `:*` accepts any port) are passed to FastMCP as `transport_security`, so a spoofed `Host` gets HTTP 421 and a disallowed `Origin` HTTP 403. FastMCP only does this on its own for loopback binds; the server now warns at startup when `MCP_HOST` is not loopback and no allow-list is set. The Docker image defaults both to the localhost patterns its documented `-p 127.0.0.1:8000:8000 -e MCP_HOST=0.0.0.0` recipe needs.
- **Metadata that validates.** `server.json` now satisfies the registry schema it references (100-character `description`, `websiteUrl` instead of the unknown `homepage`, `repository.subfolder`); `openaccountants_mcp.__version__` exists; the AGPL-3.0-only text ships in the wheel (`LICENSE`, `license-files`). A test pins the three version numbers, the schema constraints, the licence file and this changelog entry together. The package description and `server.json` no longer quote guide or jurisdiction counts, which drifted from the tree within weeks.
- **Docs and plugin corrected.** `README.md` no longer claims the wheel bundles the guides or that `packages/ca-*` is not checked in; counts, the California example (`ca-540-individual-return`, federal guides under `US`) and the Canadian filter (`CA`) match the catalogue; a note explains what this fork does and does not operate. The Claude Code plugin called a `start_help()` tool that never existed and pointed at the hosted endpoint this fork does not run; it now uses `start()` and the self-hosted stdio command, and drops the hosted-only `request_accountant_review`. The smoke test checks catalogue invariants instead of a `> 300` floor against ~1,835 skills.
- **Catalogue integrity is tested on the committed tree.** `tests/test_catalogue_integrity.py` fails on an ambiguous or duplicate slug; the shared files in `packages/_shared/` are catalogued under their declared jurisdiction (`GLOBAL` when they declare none), so no slug changed jurisdiction when the packages were de-duplicated.

### Since 0.2.0 (already shipping as 0.3.0)
- Tool surface brought to parity with the hosted server: `list_skills`, `get_skill` (with provenance footer), `get_skill_sections`, `search_skills`, the six prompts, then `start` (guided front door) and `submit_feedback` (pre-filled GitHub issue URL), with `next_action` steering and compute guardrails on every read tool.
- HTTP transports (`MCP_TRANSPORT`, `MCP_HOST`, `MCP_PORT`, `MCP_STREAMABLE_HTTP_PATH`) and a root `Dockerfile`; the HTTP listener binds loopback unless told otherwise.
- Quality tier fails closed: only an explicit `tier: 1` plus a named reviewer reports as accountant-verified; `verified_by: pending` and reviewer names on tier-2 guides no longer do, and a tier-2 reviewer is not exposed as `verified_by`.
- Deterministic catalogue: malformed frontmatter is salvaged instead of dropping the guide, byte-identical package aliases collapse to one entry, `packages/us-federal/` wins over generated copies, and slugs whose packaged copies differ are omitted with a logged warning that `start` also surfaces (`python -m openaccountants_mcp.duplicate_slug_report` lists them). Catalogue reads are contained to `packages/`.
- `mcp` SDK dependency capped below 2.0 (2.x removes `mcp.server.fastmcp`).

## [0.2.0] — 2026-05-22

The PyPI release this changelog starts from. The repository changelog's 2.0.0
entry records the corpus changes that shipped alongside it: 13 cross-border
skills, five foundation bases, eight sector verticals, the Canada split and
the two-tier quality model.
