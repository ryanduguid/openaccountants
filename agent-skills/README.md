# OpenAccountants — Tax & Accounting Skills for AI Agents

**781 tax and accounting skills across 119 jurisdictions, in the open [Agent Skills](https://agentskills.io) format.** Drop them into any skills-compatible agent (Hermes, Claude, Cursor, Gemini CLI, Goose, Copilot, and more) and your agent knows how to handle income tax, VAT/GST, payroll, corporate tax, formation, e-invoicing, crypto, and cross-border rules for the country you are working in.

Each skill is a folder with a `SKILL.md` (open standard: `name` + `description` + instructions). Your agent loads only the short description at startup and reads the full skill when a task calls for it (progressive disclosure), so you can keep the whole library on hand for a small context cost.

> Reviewed by named CPAs / CAs / EAs. Built and maintained at **[openaccountants.com](https://openaccountants.com)**.

---

## Two ways to use OpenAccountants

| | **These skills** (this repo) | **The MCP server** ([`openaccountants-mcp`](https://openaccountants.com)) |
|---|---|---|
| What | Procedural knowledge installed into your agent | Live tools your agent calls on demand |
| Best for | Working offline, portable know-how, any Agent Skills client | Always-current rates/thresholds, VAT-number checks, the named accountant who reviewed a Guide |
| How | Copy a skill folder into your agent | Add one MCP server |

They are complementary. **Install the skills for reach; connect the MCP for live, verified figures.** A skill tells the agent *how* to do the work; the MCP gives it *today's* numbers with a name behind them.

---

## Quality: two honest tiers

We do not pretend every skill is signed off. Each `SKILL.md` carries its tier in `metadata.quality`:

- **`accountant-reviewed`** — a named CPA / CA / EA reviewed the content. **13 skills today** (Malta, South Africa, US, Germany). These are the crown jewels.
- **`source-cited draft`** — AI-authored from primary sources, not yet reviewed by a credentialed accountant. Useful, cited, and clearly labeled as a draft.

Always confirm anything you file, pay, or amend with a qualified professional in the relevant jurisdiction. Every skill says so, up top.

### Accountant-reviewed skills

| Skill | Jurisdiction | Reviewed by |
|---|---|---|
| `malta-vat-return`, `malta-income-tax`, `malta-ssc`, `malta-tax-optimization`, `mt-estimated-tax` | Malta | Michael Cutajar, CPA (Malta) |
| `za-vat-return`, `za-income-tax`, `za-provisional-tax`, `south-africa-vat` | South Africa | Werner Britz, CA(SA) |
| `us-schedule-c-and-se-computation`, `us-sole-prop-bookkeeping`, `us-ca-freelance-intake` | United States | CPA-reviewed |
| `germany-vat-return` | Germany | CPA-reviewed |

---

## Install

A skill is just a folder. Copy the ones you want into your agent's skills directory.

**Hermes Agent** (Nous Research)
```bash
cp -r malta-vat-return ~/.hermes/skills/
# then, in Hermes:  /skills   (browse)   ·   /malta-vat-return   (invoke)
```

**Claude Code**
```bash
cp -r malta-vat-return ~/.claude/skills/     # personal, all projects
# or  .claude/skills/  inside a project
```

**Any other Agent Skills client** (Cursor, Gemini CLI, Goose, OpenCode, Copilot, …)
Point it at these folders, or copy them into that client's skills directory. See the client list at [agentskills.io/clients](https://agentskills.io/clients).

**Grab the whole library**
```bash
git clone https://github.com/openaccountants/openaccountants
cp -r openaccountants/agent-skills/*/ ~/.hermes/skills/   # or your agent's skills dir
```

### Add the live MCP too (recommended)
```jsonc
// Hermes / any MCP client — stdio
{ "mcpServers": { "openaccountants": { "command": "uvx", "args": ["openaccountants-mcp"] } } }
```
Now the agent has both the how-to (skills) and today's verified figures (MCP). See [`docs/ADD-TO-HERMES.md`](docs/ADD-TO-HERMES.md).

---

## Coverage

- **119 jurisdictions** — every major economy, all 50 US states, Canadian provinces.
- **Obligations** — income tax, corporate tax, VAT/GST, payroll & social contributions, formation, e-invoicing, crypto, cross-border (Pillar Two, CBAM, FATCA/CRS, DST), financial statements, and sector verticals.
- Workflow-base skills (e.g. `tax-workflow-base`, `vat-workflow-base`) encode the *method* — conservative defaults, citation discipline, refusal catalog — and are loaded alongside a content skill.

## How this is built

Generated from the OpenAccountants Guide library by [`scripts/build-agent-skills.py`](https://github.com/openaccountants/openaccountants), which converts each reviewed Guide into a spec-valid `SKILL.md`. Regenerated as Guides are reviewed and updated, so the accountant-reviewed count grows over time. Validated with [`skills-ref`](https://github.com/agentskills/agentskills/tree/main/skills-ref).

## License

- **Code / tooling:** AGPL-3.0-or-later
- **Skill content:** OpenAccountants Guide License v1.0

## Links

- Site & Guides: **[openaccountants.com](https://openaccountants.com)**
- MCP server: `openaccountants-mcp` (PyPI) · hosted at openaccountants.com
- The open standard: **[agentskills.io](https://agentskills.io)**

*General reference only. Not tax, legal, or accounting advice. Confirm with a qualified professional before you file, pay, or amend.*
