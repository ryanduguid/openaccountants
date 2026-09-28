# Start here

Pick the row that matches you. Every link below points at something in this checkout. The hosted service and website belong to the upstream project and are not operated from this fork; the [README](README.md) explains the fork's status.

| You are... | Go to |
|---|---|
| **Someone with a tax question and an AI assistant** | Open the folder for your jurisdiction under `packages/` (for example [`packages/malta/`](packages/malta/) or [`packages/us-ca/`](packages/us-ca/)), upload every file in it to your AI assistant, and follow the `README.md` inside the folder. Each folder is self-contained. |
| **An AI agent** | Read [`index.json`](index.json) to find what exists, then load the guide files from `packages/<jurisdiction>/`. [`llms.txt`](llms.txt) is the short agent-facing entry point and [`llms-full.txt`](llms-full.txt) lists every guide. |
| **An accountant** | What the two quality states mean and what a review involves: [README → Two states, greppable honesty](README.md#two-states-greppable-honesty) and [docs/QUALITY-TIERS.md](docs/QUALITY-TIERS.md). Who has reviewed what: [README → Accountant roster](README.md#accountant-roster) and [PARTNERS.md](PARTNERS.md). |
| **A contributor** | [CONTRIBUTING.md](CONTRIBUTING.md) for the process, [docs/skill-template.md](docs/skill-template.md) for the file format, and [docs/REPO-LAYOUT.md](docs/REPO-LAYOUT.md) for which file to edit and how to regenerate the derived trees. |
| **A developer** | [README → For developers](README.md#for-developers), the self-hostable MCP server in [mcp/README.md](mcp/README.md), and the guided workflows in [workflows/README.md](workflows/README.md). |
| **Checking whether you may reuse the content** | [LICENSING.md](LICENSING.md): the software is AGPL-3.0-only, the guides are under the source-available OA Guide License. |

**Not advice.** The guides are general reference material and may be incomplete, outdated, or wrong for your facts. Have a qualified professional review any output before filing, paying, or acting on it.
