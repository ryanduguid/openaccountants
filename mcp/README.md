# OpenAccountants MCP Server

<!-- mcp-name: io.github.openaccountants/openaccountants-mcp -->

A read-only [Model Context Protocol](https://modelcontextprotocol.io/) server that gives Claude, Cursor, and any MCP client **on-demand access** to 134 countries + 51 US state packages of open-source accounting skills across 10 domains (tax, bookkeeping, payroll, e-invoicing, formation, financial statements, transfer pricing, tax optimization, cross-border, and more) — no manual file uploads.

## Why this exists

Without MCP, using OpenAccountants means downloading a country folder and dragging `.md` files into your LLM by hand, every conversation. With MCP, your AI assistant **discovers and fetches** the right skills automatically:

```
You:    "Help me set up a company in Malta and understand my tax obligations."
          ↓
Claude: calls list_jurisdictions → sees "malta"
Claude: calls list_files("malta") → foundation.md, malta-vat.md, malta-formation.md, …
Claude: calls get_file("malta", "malta-formation.md") → formation rules loaded
Claude: calls get_file("malta", "malta-vat.md") → VAT rules loaded
          ↓
Claude: walks you through entity selection, registration, and tax setup
```

Install once, configure once — skills are available in every conversation from that point on.

US states work the same way:

```
You:    "Help me with my California taxes. Here's my bank statement."
          ↓
Claude: calls list_jurisdictions → sees "us-ca"
Claude: calls list_files("us-ca") → federal + CA state skills
Claude: calls get_file("us-ca", "ca-income-tax.md") → state rules loaded
          ↓
Claude: now processes with federal AND California rules
```

Special packages are also available:

| Package | What's inside |
|---------|--------------|
| `_cross-border` | Multi-jurisdiction orchestrator, EU rules, OECD treaty defaults, 70+ treaty corridor WHT rates |
| `_verticals` | Industry-specific skills (developer, e-commerce, content creator, consultant, property investor, medical) |
| `_integrations` | Platform export formats (Xero, QuickBooks, Stripe, Wise, PayPal, Revolut, Amazon, Shopify, FreeAgent, Sage) |

## Tools

| Tool | Description |
|------|-------------|
| `list_jurisdictions` | Returns every jurisdiction slug that has at least one `.md` skill file under `packages/`. Includes country slugs (e.g. `malta`, `uk`) and US state slugs (e.g. `us-ca`, `us-tx`). |
| `list_files` | Given a jurisdiction slug (e.g. `malta`), returns the `.md` / `.json` filenames in that package. |
| `get_file` | Given a jurisdiction + filename, returns the full UTF-8 text of that skill file (capped at 2 MB). |

All access is **read-only** and **path-sandboxed** to the `packages/` directory.

## Quick start

### 1. Clone and install

Requires **Python 3.10+**.

```bash
git clone https://github.com/openaccountants/openaccountants.git
cd openaccountants
pip install ./mcp
```

Or with `uv` (recommended):

```bash
uv pip install ./mcp
```

### 2. Connect to your AI client

Pick **one** of the following.

#### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "openaccountants-mcp"
    }
  }
}
```

If installed in a virtualenv or with `uv`:

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/openaccountants/mcp", "openaccountants-mcp"]
    }
  }
}
```

#### Cursor

Add to `.cursor/mcp.json` in the project (or via Cursor Settings > MCP):

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "openaccountants-mcp"
    }
  }
}
```

#### Any other MCP client

Run `openaccountants-mcp` (or `python -m openaccountants_mcp`) as a **stdio** transport server.

### 3. Start chatting

> Help me with my 2025 taxes. Here's my bank statement.

or:

> I need to run payroll for my German employee. What are the withholding rates?

or:

> Help me set up a company in Singapore. What are my options?

The AI will call the MCP tools behind the scenes to load the right country and domain skills, then produce working papers, payslips, formation guides, or whatever output matches your request — all without you uploading a single file.

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENACCOUNTANTS_ROOT` | Auto-detected repo root (parent of `mcp/`) | Path to your OpenAccountants checkout. The server reads `$OPENACCOUNTANTS_ROOT/packages/`. |

## What changes vs manual upload

| Before (manual) | After (MCP) |
|------------------|-------------|
| Download folder, upload files by hand | One-time install, always available |
| Pick the right files yourself | Model discovers what's available |
| Repeat for every new conversation | Persistent — server always running |
| Can't easily switch countries mid-chat | Model calls `list_jurisdictions` and pivots |

## Smoke test

Run from the repo root to verify everything works:

```bash
python mcp/smoke_test.py
```

All checks should pass (path safety, tool outputs, jurisdiction count, US state discovery).

## Disclaimer

All skills and outputs are for informational and computational purposes only. Not tax, legal, or financial advice. Not a replacement for professional judgment. Content quality is [tiered (Q1-Q4)](../docs/QUALITY-TIERS.md) — most skills are **not** accountant-verified. Always have a qualified professional review before filing or acting upon.
