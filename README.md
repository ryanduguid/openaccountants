# OpenAccountants

> [!IMPORTANT]
> **Archived historical fork.** This repository is a point-in-time fork of
> [`openaccountants/openaccountants`](https://github.com/openaccountants/openaccountants),
> not an actively maintained or authoritative tax source. The guides, generated
> packages, badges, counts, hosted-service links, and examples below may be
> stale. GitHub Actions are disabled and no scheduled sync or publication runs
> from this fork. Use the upstream repository for current work.

<details>
<summary><strong>Conditions for reactivating this fork</strong></summary>

Only unarchive this repository when all of these conditions are met:

- a named maintainer owns releases, security response, and ongoing review;
- the authoritative guide corpus is identified and reconciled with upstream;
- a real, access-controlled sync destination replaces the retired publication path;
- unit, MCP, full-guide validation, and sync-integrity checks pass within documented bounds;
- every publication verifies the expected source commit before writing, so a stale job cannot overwrite newer work; and
- GitHub Actions are re-enabled only after the first maintenance change is reviewed.

</details>

Named, licensed accountants put their name, credential and review date on the tax guides in the upstream project. This fork does not publish or sync those guides.

[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-047857)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/openaccountants-mcp?label=openaccountants-mcp&color=047857)](https://pypi.org/project/openaccountants-mcp/)
[![smithery badge](https://smithery.ai/badge/info-ood9/openaccountants)](https://smithery.ai/servers/info-ood9/openaccountants)
[![GitHub stars](https://img.shields.io/github/stars/openaccountants/openaccountants?style=social)](https://github.com/openaccountants/openaccountants/stargazers)

<!-- oa-stats:start -->
Counts below were copied with the fork. They are not live on this repository.

**1,953 Guides** across **244 jurisdictions** · **171 accountant-reviewed** · **23 named accountants** · **7,332 questions answered** through connected AIs

<sub>Upstream figure dated 2026-08-22. Not refreshed here.</sub>
<!-- oa-stats:end -->

---

## Hosted product

The MCP endpoint, connect flow, and nightly stats belong to
[openaccountants/openaccountants](https://github.com/openaccountants/openaccountants)
and [openaccountants.com](https://www.openaccountants.com/). They are not
operated from this fork. A checkout of this tree still contains `packages/`,
`index.json`, and `mcp/` as they stood when the fork was taken.

---

## Two states, greppable honesty

Every Guide is in exactly one state — and the repo greps honestly:

| State | Meaning |
|---|---|
| **Accountant-reviewed** | A named, licensed accountant reviewed the complete Guide. Their name is in the frontmatter (`reviewed_by:`) and on [the public roster](VERIFIERS.md) |
| **Source-cited draft** | Written from primary legislation, every figure cited to its source — not yet professionally reviewed |

⚠️ **General reference, not advice.** Guides may be incomplete, outdated, or wrong for your facts. Have a qualified professional review outputs before filing, payment, or action.

---

## Accountant roster

Guide review happens on the upstream project. The roster file frozen in this
tree is [VERIFIERS.md](VERIFIERS.md). Do not treat it as current.

---

## Contributing

This fork is archived history. Send guide and code changes to
[openaccountants/openaccountants](https://github.com/openaccountants/openaccountants).

Upstream still edits `skills/` only; generated files regenerate there. See
[CONTRIBUTING.md](CONTRIBUTING.md) and [docs/REPO-LAYOUT.md](docs/REPO-LAYOUT.md).

---

## For developers

| What | Where |
|---|---|
| Guide source (per jurisdiction) | [`skills/`](skills/) |
| Per-country bundles (generated) | [`packages/`](packages/) |
| Machine-readable inventory | [`index.json`](index.json) |
| LLM entry point | [`llms.txt`](llms.txt) |
| Python MCP server | [`mcp/`](mcp/) · [PyPI](https://pypi.org/project/openaccountants-mcp/) |
| Repo architecture + sync | [`docs/REPO-LAYOUT.md`](docs/REPO-LAYOUT.md) · [`docs/WEBSITE-SYNC.md`](docs/WEBSITE-SYNC.md) |

API and platform integrations: [openaccountants.com/for-developers](https://www.openaccountants.com/for-developers)

---

## License

- **Code** (mcp/, scripts/, tools/): [AGPL-3.0](LICENSE)
- **Guide content**: OpenAccountants Guide License v1.0 — see [LICENSING.md](LICENSING.md); commercial options in [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)

**Contact:** info@openaccountants.com · [Security policy](SECURITY.md) · [Cite this repo](CITATION.cff)
