# Add OpenAccountants to Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) (Nous Research) is a self-improving agent with a skills system and a built-in MCP catalog. OpenAccountants plugs into both. Do either or, ideally, both.

## 1. Skills (procedural know-how, offline)

Hermes reads Agent Skills from `~/.hermes/skills/`.

```bash
# one skill
cp -r malta-vat-return ~/.hermes/skills/

# or the whole library
git clone https://github.com/openaccountants/agent-skills
cp -r agent-skills/*/ ~/.hermes/skills/
```

In Hermes:
```
/skills                 # browse installed skills
/malta-vat-return       # invoke by name
```
Hermes loads each skill's short description at startup and pulls the full `SKILL.md` only when a task matches, so the whole tax library costs very little context.

## 2. MCP server (live, verified figures)

Add the OpenAccountants MCP so Hermes can pull today's rates, thresholds, deadlines, VAT-number validation, and the named accountant who reviewed a Guide.

**Stdio (local):**
```jsonc
{
  "mcpServers": {
    "openaccountants": { "command": "uvx", "args": ["openaccountants-mcp"] }
  }
}
```

Or add it from Hermes' built-in **MCP catalog** if listed, or point Hermes at the hosted server at `openaccountants.com`.

Once connected, Hermes has tools like `search_skills`, `get_skill`, `get_deadlines`, `list_verifiers`, and `validate_vat_number` across 134 countries + 51 US states.

## Why both

- **Skills** = the *method*: how to classify a transaction, apply conservative defaults, cite the source, and produce reviewer-ready output. Portable, works offline, installs into every Agent Skills client.
- **MCP** = the *live numbers*: this year's rate, this jurisdiction's threshold, the named CPA/CA/EA behind it. Always current.

A skill tells Hermes how to do German VAT; the MCP tells it the rate in force today and who verified it.

## Quality, honestly

Each skill's `metadata.quality` is either `accountant-reviewed` (a named professional signed off) or `source-cited draft` (AI-authored from primary sources, not yet reviewed). Always confirm anything you file with a qualified professional.

---
Built at [openaccountants.com](https://openaccountants.com). Open standard: [agentskills.io](https://agentskills.io).
