# OpenAccountants

> [!NOTE]
> **This is a maintained fork.** `ryanduguid/openaccountants` carries the guide
> corpus of [`openaccountants/openaccountants`](https://github.com/openaccountants/openaccountants)
> as it stood before upstream rewrote its history, plus the corrections and
> tooling merged here since. The two repositories share no commits and nothing
> syncs between them in either direction. Changes land here through pull
> requests to this repository's `main`, gated by the checks in
> `.github/workflows/`; a change you also want in the upstream project needs a
> separate pull request there.
>
> Not operated from this fork: the hosted MCP endpoint and website at
> openaccountants.com, the `openaccountants-mcp` release on PyPI, the booking
> link in guide footers, and the platform sync bot. The MCP server in `mcp/`
> can be self-hosted from this checkout. Upstream's `agent-skills/` tree (guide
> copies in the Agent Skills `SKILL.md` format) is not carried here either: it
> was a hand-maintained third copy with no generator and was removed on
> 2026-09-28 (see [CHANGELOG.md](CHANGELOG.md)); `packages/` and the MCP
> server are the ways to consume the guides. Maintainer: [@ryanduguid](https://github.com/ryanduguid).

Named, licensed accountants put their name, credential and review date on the guides they reviewed. Those names travelled with the guides into this tree and are the basis of every "accountant-reviewed" count below. No review is re-performed here: a guide only becomes accountant-reviewed in this fork when a named, licensed accountant signs it off in a pull request.

[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-047857)](LICENSE)

<!-- oa-stats:start -->
**1,866 Guides** across **243 jurisdictions** · **164 accountant-reviewed** · **22 named accountants**

<sub>Derived from `index.json` in this checkout and verified by
`scripts/check-coverage-claims.py`. "Accountant-reviewed" and "named
accountants" use the index builder's own rule: an explicit `tier: 1` plus a
named reviewer. Counting every reviewer name in the corpus gives 28 people, but
most of those names sit on tier-2 guides, where the builder is explicit that a
name alone never implies sign-off — so 28 beside "164 accountant-reviewed"
would overstate the assurance. One tier-1 reviewer asked not to be named and is
excluded from the 22.</sub>

<sub>The upstream project also publishes a usage figure (7,332 questions
answered through connected AIs, dated 2026-08-22). It cannot be derived from
this checkout and this fork does not operate the hosted service, so it is not
restated here.</sub>
<!-- oa-stats:end -->

---

## Hosted product

The MCP endpoint, connect flow, bundle API and usage statistics belong to the
upstream project and [openaccountants.com](https://www.openaccountants.com/).
They are not operated from this fork. This tree contains everything needed to
use the guides without them: the per-jurisdiction bundles in `packages/`, the
inventory in `index.json`, and the self-hostable MCP server in `mcp/` (see
[mcp/README.md](mcp/README.md)).

---

## Two states, greppable honesty

Every Guide is in exactly one state — and the repo greps honestly:

| State | Meaning |
|---|---|
| **Accountant-reviewed** | A named, licensed accountant reviewed the complete Guide. Their name is in the frontmatter (`reviewed_by:`) and on [the roster](PARTNERS.md) |
| **Source-cited draft** | Written from primary legislation, every figure cited to its source — not yet professionally reviewed |

⚠️ **General reference, not advice.** Guides may be incomplete, outdated, or wrong for your facts. Have a qualified professional review outputs before filing, payment, or action.

---

## Accountant roster

Each guide's frontmatter (`tier: 1` with `reviewed_by`) is the record of who
reviewed what, and `index.json` derives the counts above from it.
[PARTNERS.md](PARTNERS.md) is generated from the index by
`scripts/build-partners.py` with the same rule (only `tier: 1` plus a named
reviewer counts; a name on a `tier: 2` guide is attribution, not review) and
lists the reviewers per person and per jurisdiction; CI fails when it is stale.
[VERIFIERS.md](VERIFIERS.md) is upstream's roster as of 2026-08-22 and is not
regenerated here, so where it disagrees with the frontmatter, the frontmatter
wins.

---

## Contributing

Pull requests to this repository are welcome: guide corrections, new guides,
tooling. Edit `skills/`, regenerate the derived trees, open a PR; CI checks the
frontmatter, the metadata bump, derived-tree freshness and the unit tests.
There is no contributor licence agreement here: a contribution is accepted
under the licence of the files it changes. Process: [CONTRIBUTING.md](CONTRIBUTING.md).
Which file to edit: [docs/REPO-LAYOUT.md](docs/REPO-LAYOUT.md).

---

## For developers

| What | Where |
|---|---|
| Guide source (per jurisdiction) | [`skills/`](skills/) |
| Per-country bundles (generated) | [`packages/`](packages/) |
| Machine-readable inventory | [`index.json`](index.json) |
| LLM entry point | [`llms.txt`](llms.txt) |
| Python MCP server, self-hostable | [`mcp/`](mcp/) (the [PyPI release](https://pypi.org/project/openaccountants-mcp/) is upstream's) |
| Repo architecture | [`docs/REPO-LAYOUT.md`](docs/REPO-LAYOUT.md); retired documents, upstream's sync contract among them, are in [`docs/archive/`](docs/archive/README.md) |
| How the guides are checked | [`docs/ACCURACY-METHODOLOGY.md`](docs/ACCURACY-METHODOLOGY.md) and the dated [verification log](docs/verification-log/README.md) |
| Accountant roster (generated) | [`PARTNERS.md`](PARTNERS.md), from `index.json` by `scripts/build-partners.py` |
| Reproduce CI locally | `python3 -m pip install -r requirements-dev.txt`, then `make check`; the targets are mapped to the CI jobs in [CONTRIBUTING.md](CONTRIBUTING.md#reproduce-ci-locally) |

---

## License

- **Code** (`mcp/`, `scripts/`, `tools/`, `plugins/`, `docs/`, `.github/`): [AGPL-3.0-only](LICENSE)
- **Guide content** (`skills/`, `packages/`, `workflows/`, `index.json`, `llms*.txt`): OpenAccountants Guide License v1.0, licensed by Glimpse Ltd — see [LICENSING.md](LICENSING.md); commercial options in [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)

**Contact:** the maintainer through [issues](https://github.com/ryanduguid/openaccountants/issues) · [Security policy](SECURITY.md) · questions about the Guide License and the commercial track go to its licensor, Glimpse Ltd (info@openaccountants.com) · [Cite this repo](CITATION.cff)
