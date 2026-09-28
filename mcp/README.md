# OpenAccountants MCP Server

<!-- mcp-name: io.github.openaccountants/openaccountants-mcp -->

A read-only [Model Context Protocol](https://modelcontextprotocol.io/) server that gives Claude, Cursor, and any MCP client **on-demand access** to the open-source accounting skills in a checkout of this repository — at the time of writing 1,835 skills from 187 country packages, 51 US state packages (50 states + DC) plus `us-federal`, 13 Canadian province/territory packages, and the `_cross-border`, `_verticals` and `_integrations` bundles, across tax, bookkeeping, payroll, e-invoicing, formation, financial statements, transfer pricing, tax optimization, cross-border and more — no manual file uploads.

> **Two MCPs, different surfaces.** This **self-hosted server** reads the open-source markdown in a checkout of this repository. The **hosted server** at `https://www.openaccountants.com/api/mcp` belongs to the upstream project: it reads the production database and exposes a larger surface that includes the **accountant-reviewed** tier, the `request_accountant_review` handoff (routes to a named licensed CPA/CA/EA with your working paper attached), `get_rates`, `list_verifiers`, `compare_jurisdictions`, and `plan_cross_border`. The hosted server is upstream's product; this self-hosted one is the open research base.

> **This fork.** The hosted endpoint is not operated from this fork (see the [root README](../README.md)), and a wheel built from `mcp/` here ships **only the server code — no guides**. Point `OPENACCOUNTANTS_ROOT` at a checkout of this repository, or install the server editable from one (`pip install -e ./mcp`); the working directory is not consulted. If it cannot find `packages/`, it logs a warning when it first builds the catalogue and every tool says so explicitly — an `error` field from `list_skills` / `search_skills`, `status: "error"` from `start`, a raised error from `get_skill` — instead of answering with an empty catalogue as if that were the corpus.

## Why this exists

Without MCP, using OpenAccountants means downloading a country folder and dragging `.md` files into your LLM by hand, every conversation. With MCP, your AI assistant **discovers and fetches** the right skills automatically:

```
You:    "Help me set up a company in Malta and understand my tax obligations."
          ↓
Claude: calls list_skills(jurisdiction="MT") → sees malta-formation, malta-vat-return, …
Claude: calls get_skill("malta-formation") → formation rules loaded
Claude: calls get_skill("malta-vat-return") → VAT rules loaded
          ↓
Claude: walks you through entity selection, registration, and tax setup
```

Install once, configure once — skills are available in every conversation from that point on.

US states work the same way. Federal guides carry `jurisdiction: US`, so `US-CA` returns only the California package's own skills; ask for `US` separately:

```
You:    "Help me with my California taxes. Here's my bank statement."
          ↓
Claude: calls list_skills(jurisdiction="US-CA") → ca-540-individual-return, california-sales-tax, ca-payroll, …
Claude: calls list_skills(jurisdiction="US")    → us-form-1040-individual-return, us-quarterly-estimated-tax, …
Claude: calls get_skill("ca-540-individual-return") → state rules loaded
          ↓
Claude: now processes with federal AND California rules
```

(Slugs come from each guide's `name:` frontmatter, not its file name: `packages/us-ca/ca-income-tax.md` is `ca-540-individual-return`.)

Special packages are also available:

| Package | What's inside |
|---------|--------------|
| `_cross-border` | 40 skills — multi-jurisdiction orchestrator, EU rules, OECD treaty defaults, 70+ treaty corridor WHT rates |
| `_verticals` | 14 industry-specific skills — banking, charity / nonprofit, construction, consultant, content creator, e-commerce, freelance developer, insurance, investment funds / REITs, medical, oil & gas, property investor, SaaS, shipping / aviation |
| `_integrations` | 10 platform export formats — Xero, QuickBooks, Stripe, Wise, PayPal, Revolut, Amazon, Shopify, FreeAgent, Sage |

## Tools

The self-hosted server exposes 6 read-only tools below. The hosted server at `https://www.openaccountants.com/api/mcp` is a superset — it adds `get_rates`, `list_jurisdictions`, `list_verifiers`, `compare_jurisdictions`, `plan_cross_border`, and the `request_accountant_review` handoff. Install the hosted MCP if you want the AI-to-human routing; install this one if you want the open research base.

| Tool | Description |
|------|-------------|
| `start` | **Front door.** Call first whenever a user asks for tax/accounting help. Takes optional `intent` (free text — e.g. `"taxes"`, `"VAT return"`, `"set up a company"`) and `jurisdiction` (e.g. `"MT"`, `"GB"`, `"US-CA"`). Returns either a clarification question or a ready-to-execute plan (`skills_to_load`, `expectations`, `next_action`, `guardrails`). |
| `list_skills` | List published skills with quality tier and reviewing accountant. Optional `jurisdiction` (ISO code, e.g. `MT`, `GB`, `US-CA`) and `category` filters. |
| `get_skill` | Given a skill `slug`, returns the full markdown plus a provenance/attribution footer. |
| `get_skill_sections` | Given a `slug`, returns the skill parsed into sections (`heading`, `content`, `level`) for step-by-step application. |
| `search_skills` | Keyword search across skill markdown (`query`, optional `jurisdiction`). Returns the matched section heading and a snippet. |
| `submit_feedback` | Build a pre-filled GitHub New Issue URL the user opens to submit feedback (skill problem, missing jurisdiction, bug, etc.). Takes `summary` plus optional `title`, `skill_slug`, `jurisdiction`, `rating`. Returns `github_url`, `title`, `body`, `labels`. No server-side auth — user submits under their own account. |

Skill access is **read-only** and **path-sandboxed** to the `packages/` directory; `submit_feedback` does not call GitHub itself, it only constructs a URL.

### The `start` flow

`start` is what makes the connector self-guiding. A typical session looks like:

```
User:    "Help me with my Malta taxes."
          ↓
Model:   start(intent="taxes", jurisdiction="MT")
          → { status: "ready",
              skills_to_load: [mt-freelance-intake, malta-income-tax, …],
              expectations: "I'll help you build a working paper for your accountant…",
              next_action: "Run the intake skill first, then classify transactions",
              guardrails: [...] }
          ↓
Model:   get_skill("mt-freelance-intake")  →  scope-check questions
Model:   get_skill("malta-income-tax")     →  rates, brackets, deductions
          ↓
Model:   walks the user through the working paper using the loaded skills
```

If the user only says "help me with my taxes" (no country), call `start(intent="taxes")` — you get back the list of jurisdictions that have a tax skill so you can ask which one applies. Same if only the country is known: `start(jurisdiction="MT")` returns the available categories for Malta.

## Prompts

Guided workflows that turn the skills into a tax engine, not just a library:

| Prompt | Arguments | Purpose |
|--------|-----------|---------|
| `tax-return` | `country`, `tax_year`, `entity_type` | Intake → transaction classification → working paper. |
| `vat-check` | `country`, `period` | Classify transactions for VAT/GST and build a return working paper. |
| `find-deductions` | `country`, `entity_type` | Review expenses and surface deductions the taxpayer is missing. |
| `compare-jurisdictions` | `countries`, `income`, `entity_type` | Side-by-side tax comparison for cross-border planning. |
| `skill-feedback` | `skill_slug`, `country` | Collect structured feedback on a skill after use. |
| `skill-review` | `skillSlug`, `scenario` | Load a skill's sections and apply them to one scenario. |

> Note: the on-disk server reads the open-source markdown in `packages/`. Most skill files don't carry a `jurisdiction` field, so it's inherited from the package directory (the folder name for `us-XX`/`ca-XX`, otherwise the code its siblings declare). Quality tier is derived from a file's explicit `tier` frontmatter: only `tier: 1` **plus** a named reviewer (`reviewed_by`, or the legacy `verified_by`) reports as accountant-verified. A reviewer name on its own no longer implies tier 1, and a non-tier-1 file's reviewer is not exposed as `verified_by`.

> **Canadian packages:** the `ca-XX/` provincial packages (`ca-on`, `ca-qc`, `ca-bc`, …) are checked in to this tree, so a clone needs no build step to serve them (after editing `skills/`, regenerate with `python3 scripts/build-packages.py`). Their guides declare `jurisdiction: CA` in frontmatter, and a declared code beats the folder name, so filter with `list_skills(jurisdiction="CA")` — `list_skills(jurisdiction="CA-ON")` currently returns nothing. Copies shared byte-for-byte by several provinces are listed once. `packages/canada/` holds only a README.

## Quick start

Three ways to install, easiest first.

### Option 1 — Hosted endpoint (upstream's; not operated from this fork)

Point any remote-capable MCP client at:

```
https://www.openaccountants.com/api/mcp
```

The hosted server is the upstream project's full product surface (live database, accountant-reviewed tier, `request_accountant_review`, `get_rates`, and more — see the note at the top). It is not run from this fork, and its behaviour may differ from the code in this tree.

### Option 2 — Install from PyPI (upstream's package)

Requires **Python 3.10+**. Upstream publishes `openaccountants-mcp` from a separate repository ([`openaccountants/openaccountants-mcp`](https://github.com/openaccountants/openaccountants-mcp)) that vendors a copy of `packages/`. This fork does not publish to PyPI, and a wheel built from this tree contains only the server code (see the note at the top), so if the server reports an empty catalogue, point it at a checkout:

```bash
pip install openaccountants-mcp
export OPENACCOUNTANTS_ROOT=/path/to/openaccountants   # a checkout containing packages/
```

Or run it directly with `uvx`:

```bash
OPENACCOUNTANTS_ROOT=/path/to/openaccountants uvx openaccountants-mcp
```

Then connect your AI client (next section) using the `openaccountants-mcp` command.

### Development install (clone the repo)

For contributors, or if you want the server to read your local, editable checkout:

```bash
git clone https://github.com/openaccountants/openaccountants.git
cd openaccountants
pip install -e ./mcp
```

Or with `uv`:

```bash
uv pip install -e ./mcp
```

Use an **editable** install (`-e`) or set `OPENACCOUNTANTS_ROOT`. A plain `pip install ./mcp` copies only the code into site-packages; the server then looks for `packages/` two directories above the installed module, whatever directory you launch it from, finds nothing, and reports an empty catalogue on every call (with a warning on stderr saying where it looked). `uv run --directory mcp openaccountants-mcp` from the repo root also works without installing anything.

The server reads `packages/` from the repo root (override with `OPENACCOUNTANTS_ROOT`, see environment variables below).

### Connect to your AI client

Pick **one** of the following.

#### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "openaccountants-mcp",
      "env": { "OPENACCOUNTANTS_ROOT": "/path/to/openaccountants" }
    }
  }
}
```

`OPENACCOUNTANTS_ROOT` is only required when the install is not editable (see above), but it never hurts: the server reads `$OPENACCOUNTANTS_ROOT/packages/`.

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
      "command": "openaccountants-mcp",
      "env": { "OPENACCOUNTANTS_ROOT": "/path/to/openaccountants" }
    }
  }
}
```

#### Claude Code plugin

The repo root is a Claude Code plugin marketplace (`.claude-plugin/marketplace.json`) with one plugin, `openaccountants`, that registers the same `openaccountants-mcp` stdio command and adds a `/openaccountants` slash command. Install the server first (`pip install -e ./mcp`, or any install plus `OPENACCOUNTANTS_ROOT` exported in the shell that launches Claude Code), then add the marketplace from your checkout.

#### Any other MCP client

Run `openaccountants-mcp` (or `python -m openaccountants_mcp`) as a **stdio** transport server.

### Start chatting

> Help me with my 2025 taxes. Here's my bank statement.

or:

> I need to run payroll for my German employee. What are the withholding rates?

or:

> Help me set up a company in Singapore. What are my options?

The AI will call the MCP tools behind the scenes to load the right country and domain skills, then produce working papers, payslips, formation guides, or whatever output matches your request — all without you uploading a single file.

## Docker (local development / self-hosting)

For contributors who'd rather iterate inside a container, the repo root ships a `Dockerfile` that builds the MCP server and runs it under FastMCP's Streamable-HTTP transport:

```bash
docker build -t openaccountants-mcp .
docker run --rm -p 127.0.0.1:8000:8000 -e MCP_HOST=0.0.0.0 openaccountants-mcp
# Point an MCP client at http://localhost:8000/mcp
```

The server itself defaults to the loopback address `127.0.0.1`. Docker's port
forwarder reaches the container through its network interface, so the local-only
Docker example above deliberately sets `MCP_HOST=0.0.0.0` **inside the container**
while binding the published host port to `127.0.0.1`. That keeps the endpoint
available only to local clients.

FastMCP validates the `Host` and `Origin` headers (its DNS-rebinding protection)
on its own **only for loopback binds**. With any other `MCP_HOST` it validates
nothing unless told what to accept, so a spoofed `Host` or `Origin` is served
like a genuine one. `MCP_ALLOWED_HOSTS` / `MCP_ALLOWED_ORIGINS` supply that list:
requests carrying another `Host` get HTTP 421 and a disallowed `Origin` gets
HTTP 403. The image ships with both set to the localhost patterns the example
above needs (`localhost:*,127.0.0.1:*,[::1]:*` and their `http://` forms), so the
`0.0.0.0` bind inside the container is as protected as a loopback bind. When you
bind beyond loopback without an allow-list, the server logs a warning at startup.

Remote network binding is an explicit operator choice, not a default. Name the
hosts clients will use (a trailing `:*` accepts any port) and, for browser-based
clients, their origins; non-browser MCP clients send no `Origin` header and are
always accepted:

```bash
MCP_TRANSPORT=streamable-http MCP_HOST=0.0.0.0 \
MCP_ALLOWED_HOSTS=mcp.example.com \
MCP_ALLOWED_ORIGINS=https://app.example.com \
openaccountants-mcp
```

The same variables apply to a loopback bind: a local reverse proxy that forwards
its public `Host` header to `127.0.0.1:8000` needs that name in
`MCP_ALLOWED_HOSTS`, or every request is answered with 421.

This package does not add an authentication layer. Only use a non-loopback
`MCP_HOST` behind an authenticated, TLS-terminating reverse proxy or equivalent
network controls; do not publish the raw MCP endpoint directly to the internet.

When fronted by a reverse proxy that strips an upstream path prefix (e.g. Caddy `uri strip_prefix /oamcp`), set `MCP_STREAMABLE_HTTP_PATH=/` so the endpoint mounts at the proxied root:

```bash
docker run --rm -p 127.0.0.1:8000:8000 \
  -e MCP_HOST=0.0.0.0 \
  -e MCP_STREAMABLE_HTTP_PATH=/ \
  openaccountants-mcp
```

The default stdio transport (`pip install ./mcp && openaccountants-mcp`) is unchanged.

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENACCOUNTANTS_ROOT` | Auto-detected repo root (two directories above the installed module, i.e. the parent of `mcp/` for an editable install) | Path to your OpenAccountants checkout. The server reads `$OPENACCOUNTANTS_ROOT/packages/`. An empty value counts as unset. When that directory is missing or holds no skill files, the server logs a warning and every tool reports the problem instead of serving an empty catalogue. |
| `MCP_TRANSPORT` | `stdio` | `stdio`, `streamable-http`, or `sse`. HTTP transports let remote MCP clients connect via a reverse proxy. |
| `MCP_HOST` | `127.0.0.1` | Bind host for HTTP transports. Set explicitly, for example to `0.0.0.0`, only when an authenticated reverse proxy or equivalent network boundary is intentionally exposing the service. |
| `MCP_PORT` | `8000` | Bind port for HTTP transports. |
| `MCP_STREAMABLE_HTTP_PATH` | `/mcp` | Path the Streamable-HTTP endpoint is mounted at. Set to `/` when behind a proxy that strips the upstream prefix. |
| `MCP_ALLOWED_HOSTS` | unset (FastMCP protects loopback binds itself; other binds validate nothing) | Comma-separated `Host` header values to accept on HTTP transports, e.g. `localhost:*,127.0.0.1:*` or `mcp.example.com`; `:*` accepts any port. Other hosts get HTTP 421. |
| `MCP_ALLOWED_ORIGINS` | unset | Comma-separated `Origin` header values to accept, e.g. `http://localhost:*`; only meaningful together with `MCP_ALLOWED_HOSTS`. Other origins get HTTP 403; requests without an `Origin` header are always accepted. |

## What changes vs manual upload

| Before (manual) | After (MCP) |
|------------------|-------------|
| Download folder, upload files by hand | One-time install, always available |
| Pick the right files yourself | Model discovers what's available |
| Repeat for every new conversation | Persistent — server always running |
| Can't easily switch countries mid-chat | Model calls `list_skills` / `search_skills` and pivots |

## Smoke test

Run from the repo root to verify everything works:

```bash
python mcp/smoke_test.py
```

All checks should pass (path safety, tool outputs, catalogue invariants — every skill file parsed, total = distinct slugs minus ambiguous ones — US state and federal discovery, and the explicit error every tool returns when `packages/` is missing). The unit tests live in `mcp/tests/` and run with `python -m pytest mcp/tests -q` (or `python -m unittest discover -s mcp/tests`); the HTTP tests start the server on a free port and check the 421/403 answers to spoofed `Host`/`Origin` headers.

## Disclaimer

All skills and outputs are for informational and computational purposes only. Not tax, legal, or financial advice. Not a replacement for professional judgment. Every skill is in one of [two tiers](../docs/QUALITY-TIERS.md) — **accountant-reviewed** (a licensed practitioner reviewed and signed off) or a **source-cited draft** (drafted from authoritative sources, awaiting review). Most skills are source-cited drafts. Always have a qualified professional review before filing or acting upon.
