[![smithery badge](https://smithery.ai/badge/info-ood9/openaccountants)](https://smithery.ai/servers/info-ood9/openaccountants)

# OpenAccountants

**The open-source tax layer for AI agents.**

1,000+ skills across 190+ jurisdictions — research-verified, with an accountant-verified tier signed off by named CPAs/CAs/EAs. Works with Claude, ChatGPT, Cursor, Windsurf, and any MCP-compatible agent.

---

## What it does

```
You:    "I want to file my VAT return in Brazil."
          ↓  OA loads br-indirect-tax, brazil-vat, brazil-einvoice
AI:     Brazil indirect tax rules (PIS/COFINS/ICMS)
        Filing workflow, step-by-step
        Required documents checklist
        E-invoice compliance check
        ─────────────────────────────────────────
        Verified by Ariane Marrocos CRC/SP
        [Request accountant review →]
```

```
You:    "I'm a freelancer in South Africa. What do I owe?"
          ↓  OA loads za-income-tax, za-provisional-tax
AI:     ITR12 working paper
        Provisional tax schedule (IRP6 — Aug + Feb)
        Medical tax credits
        Retirement annuity deduction
        ─────────────────────────────────────────
        Verified by Werner Britz CA(SA)
        [Request accountant review →]
```

```
You:    "Help me set up a company in Malta."
          ↓  OA loads malta-formation, malta-income-tax, malta-vat-return
AI:     Entity type comparison (Ltd vs partnership vs sole trader)
        Registration steps + costs
        Post-formation compliance checklist
        ─────────────────────────────────────────
        Verified by Michael Cutajar CPA (Malta)
        [Request accountant review →]
```

---

**[Install via MCP →](https://www.openaccountants.com/connect)**   |   **[Browse skills →](https://www.openaccountants.com/skills)**   |   **[For accountants →](https://www.openaccountants.com/for-accountants)**

---

**Verified accountants:**
Werner Britz CA(SA) · Michael Cutajar CPA (Malta) · Ariane Marrocos CRC/SP · James Power (UK) · Mayur Deokar CA (India) · Rilia Putri CA (Indonesia) · Ashish Bista CA (Nepal) · Mário Vale CA (Portugal) · Mehran Habib (Saudi Arabia) · Amir Pelinkovic CPA (US)

---

## Two ways to use

| | MCP connector *(recommended)* | Manual upload from this repo |
|---|---|---|
| **What you get** | Accountant-verified skills, named-verifier attribution on every answer, AI-to-human handoff (`request_accountant_review` routes to a real CPA with your worksheet attached) | Research-verified drafts only — no verifier name, no handoff |
| **How** | Install once at [openaccountants.com/connect](https://www.openaccountants.com/connect) | Download a folder, drag `.md` files into your LLM |
| **Best for** | Anyone who wants to actually use OpenAccountants | Developers and accountants who want to audit, fork, or contribute |
| **Clients** | Claude.ai, ChatGPT (Business+), Cursor, Windsurf, Claude Desktop, Claude Code, any MCP-aware client | Any LLM that reads files |

**The MCP path is the canonical product.** This repo is the open research base that backs it.

---

## Quick start (60 seconds)

### 1. Find your jurisdiction

```
packages/
├── malta/           ← income tax + VAT + SSC + payroll + formation + bookkeeping
├── uk/              ← SA103/SA100 + VAT100 + NIC + CGT
├── germany/         ← Einkommensteuer + UStVA + payroll (fullest package)
├── brazil/          ← IRPF + PIS/COFINS + e-invoice + payroll
├── south-africa/    ← ITR12 + VAT + provisional tax
├── ... 130+ more countries
├── us-ca/           ← Federal Schedule C/SE + California state
├── us-ny/           ← Federal + New York state
├── ... 51 US state packages
├── ca-on/           ← Federal T1/T2125 + Ontario
├── ca-qc/           ← Federal + Quebec (incl. QST)
├── ... 13 Canadian province/territory packages
```

**New here?** Read [START-HERE.md](START-HERE.md) — scenarios, file lists, what to say to the AI.

**Canadian packages:** if `ca-on/`, `ca-qc/` etc. are missing, run `python3 scripts/build-packages.py` once.

### 2. Upload to your AI

- **Claude.ai** → Create a Project, add files as Project Knowledge
- **ChatGPT** → Attach files or create a Custom GPT
- **Any other LLM** → Attach or paste the files

### 3. Go

```
Help me with my 2025 taxes. Here's my bank statement.
Help me set up a company in Malta.
Run my payroll for this month.
Prepare my annual accounts.
Optimize my tax — what deductions am I missing?
Check my invoice compliance for EU e-invoicing.
```

The AI asks a few questions, loads the right skills, and produces a working paper for your accountant.

---

## Verified accountants

These licensed practitioners have reviewed and signed off skills for their jurisdictions. Their name appears on every answer the AI gives.

| Jurisdiction | Verifier | Skills | Profile |
|---|---|---|---|
| South Africa | Werner Britz CA(SA) | 5 | [profile](https://www.openaccountants.com/network/28a3ec1b-d699-4c5d-bb60-3114eedc59d0) |
| Malta | Michael Cutajar CPA (Malta) | 5 | [profile](https://www.openaccountants.com/network) |
| Brazil | Ariane Marrocos CRC/SP | 9 | [profile](https://www.openaccountants.com/network/366f5c0f-1afb-4332-b87b-9b6f912821aa) |
| United Kingdom | James Power | 15 | [profile](https://www.openaccountants.com/network/30b2f478-3a97-40c4-b435-0678829b487e) |
| India | Mayur Deokar CA | 13 | [profile](https://www.openaccountants.com/network/f4cb8476-a86d-4fd9-b536-9217e82ccf99) |
| Indonesia | Rilia Putri CA | 10 | [profile](https://www.openaccountants.com/network/ec70d43e-18c0-4b4e-b92c-4f8a22e10152) |
| Nepal | Ashish Bista CA | 5 | [profile](https://www.openaccountants.com/network/78ab67db-8f29-4746-8102-7b52d17309aa) |
| Portugal | Mário Vale CA | 9 | [profile](https://www.openaccountants.com/network/a26a63b7-343c-451b-8266-bb9d28bd7089) |
| Saudi Arabia | Mehran Habib | 9 | [profile](https://www.openaccountants.com/network/f9dbab51-2b89-451b-98f2-414b48fb4599) |
| United States | Amir Pelinkovic CPA | 16 | [profile](https://www.openaccountants.com/network/752ee18a-3843-434d-8426-457d3fa9706f) |
| Germany, Australia, Canada | Verification in progress | — | [Claim a jurisdiction →](https://www.openaccountants.com/onboarding/accountant) |

> Verified skills (Tier 1) are served via the MCP server with the verifier's name on every output. The research drafts in this repo are Tier 2.

---

## What's in each package

| File | What it does |
|------|-------------|
| `foundation.md` | Tells the AI how to work — conservative defaults, output format, classification rules |
| `intake.md` | Onboarding questions, refusal checks, document inference |
| `[country]-income-tax.md` | Income tax brackets, deductions, transaction patterns |
| `[country]-vat.md` | VAT/GST/sales tax rules, supplier patterns, form mappings |
| `[country]-ssc.md` | Social security / pension contributions |
| `[country]-payroll.md` | PAYE withholding, employer filing (15 countries) |
| `[country]-formation.md` | Entity types, registration, costs (13 countries) |
| `[country]-bookkeeping.md` | Chart of accounts, P&L, balance sheet (13 countries) |
| `[country]-financial-statements.md` | Annual accounts, reporting framework (13 countries) |
| `[country]-transfer-pricing.md` | TP documentation, arm's length, CbCR (15 countries) |
| `[country]-tax-optimization.md` | Legal deductions, timing strategies (14 countries) |
| `[country]-crypto-tax.md` | CGT on crypto, DeFi, staking, NFTs (22 countries + all US states) |
| `[country]-guided-intake.md` | Full guided experience (13 countries) |
| `[country]-return-assembly.md` | Cross-checks: VAT × IT × SSC (13 countries) |

**Special packages:** `_cross-border/` (37 skills) · `_verticals/` (14 industry skills) · `_integrations/` (10 platform skills: Xero, QuickBooks, Stripe, Wise, Shopify, and more)

---

## Coverage

### Full accounting suite (13 countries)

Tax + bookkeeping + payroll + formation + financial statements + transfer pricing + tax optimization:

Malta · UK · Germany · Australia · Canada · India · Spain · France · Japan · Netherlands · Portugal · Belgium · United States (CA)

### Multi-skill countries (~56 countries)

VAT + income tax + social contributions (and often more):

Argentina, Austria, Belgium, Brazil, Bulgaria, Chile, China, Colombia, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, Greece, Hong Kong, Hungary, Indonesia, Ireland, Israel, Kenya, Latvia, Lithuania, Luxembourg, Malaysia, Mexico, New Zealand, Nigeria, Norway, Pakistan, Panama, Peru, Philippines, Poland, Qatar, Romania, Saudi Arabia, Singapore, Slovakia, Slovenia, South Africa, South Korea, Sweden, Switzerland, Taiwan, UAE, and more.

### Crypto tax (22 countries + all 51 US states)

Malta, UK, Germany, France, Australia, Canada, Israel, India, Japan, Spain, Netherlands, Portugal, Italy, Singapore, Brazil, Mexico, Sweden, Belgium, Switzerland, South Korea, New Zealand, and every `us-<state>` package.

### VAT/GST only (65 countries)

Consumption tax classification with local supplier pattern libraries. From Albania to Zimbabwe.

Full coverage breakdown: [docs/QUALITY-TIERS.md](docs/QUALITY-TIERS.md)

---

## How the skills work

### The supplier pattern library

Every skill contains a lookup table of local vendors. When the AI sees "BANK OF VALLETTA" or "DEUTSCHE TELEKOM" or "STRIPE PAYMENTS UK LTD" on your bank statement, it already knows the classification — no guessing.

### Three outcomes per transaction

| Outcome | Means | What happens |
|---------|-------|-------------|
| **Classified** | Documents carry enough info | Applied automatically |
| **Assumed** | Data missing, conservative default applied | Flagged for your reviewer |
| **Needs Input** | Can't proceed without asking | One targeted question |

### Conservative defaults

When uncertain, the system always assumes MORE tax, never less. Your accountant can override a conservative position. They can't easily undo an aggressive one.

---

## MCP server

Install once, configure once — every future conversation pulls the right skills automatically.

```
You:    "Help me set up a company in Germany and understand payroll"
          ↓
Claude: list_jurisdictions → sees "germany"
        get_skill("germany-formation") → entity types, registration, costs
        get_skill("germany-payroll") → PAYE, social security, employer obligations
          ↓
Claude: walks you through entity choice, registration steps, payroll setup
```

### Install

```bash
git clone https://github.com/openaccountants/openaccountants.git
cd openaccountants
pip install ./mcp          # requires Python 3.10+
```

### Connect

**Claude Desktop** — add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "openaccountants-mcp"
    }
  }
}
```

**Cursor** — add to `.cursor/mcp.json` or via Settings > MCP:
```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "openaccountants-mcp"
    }
  }
}
```

Full setup, `uv` instructions, environment variables: [mcp/README.md](mcp/README.md)

---

## Are you an accountant?

Most skills are research-verified — drafted from primary legislation but awaiting a credentialed sign-off. Your review moves them to accountant-verified, and your name goes on every answer the AI gives.

**You don't need GitHub.** Just:

1. Find your country's folder under `packages/`
2. Check rates against your tax authority's website
3. Email corrections to **info@openaccountants.com** — any format works

Or: fork, fix, PR. **Your name on the skill either way.**

> 130+ countries need accountant reviewers. Pick yours at [openaccountants.com/for-accountants](https://www.openaccountants.com/for-accountants).

---

## Contribute

| What | How | Impact |
|------|-----|--------|
| **Verify a rate** | Check a number against your tax authority, open a PR | Strengthens a research-verified skill |
| **Fix an error** | Find a wrong rate or outdated threshold, submit the correction | Prevents bad working papers |
| **Add bank patterns** | Add how transactions appear on your local bank statement | Fewer misclassifications for every user in your country |
| **Add a tax skill** | Write an income tax, VAT, or SSC skill for your country | Fills a gap for every user in that jurisdiction |
| **Add a domain skill** | Bookkeeping, payroll, formation, financial statements, TP, or crypto | Expands the full accounting suite for your jurisdiction |
| **Add an industry vertical** | Vertical-specific guidance for a profession or business type | Targeted help for that industry |

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide. Every contributor is credited publicly on the skill and at [openaccountants.com](https://openaccountants.com).

**Pull requests:** contributions are accepted under the [Contributor License Agreement (CLA.md)](CLA.md).

---

## For developers

### Repo structure

```
openaccountants/
├── packages/              ← Ready-to-use jurisdiction packages (start here)
│   ├── malta/
│   ├── uk/
│   ├── us-ca/
│   └── ... 130 countries + 51 US states + 13 Canadian provinces
├── skills/                ← Source files (edit these, not packages/)
│   ├── foundation/        ← Workflow bases (universal, VAT, payroll, etc.)
│   ├── federal/           ← US federal skills
│   ├── international/     ← Country-specific skills
│   ├── cross-border/      ← WHT, PE risk, treaty corridors
│   ├── verticals/         ← Industry-specific
│   └── integrations/      ← Platform export formats
├── workflows/             ← 7 structured advisor workflow definitions
├── scripts/
│   └── build-packages.py  ← Generates packages/ from skills/
└── docs/
```

### Rebuild packages after editing skills

```bash
python3 scripts/build-packages.py
```

---

## Known limitations

- **LLMs hallucinate.** These files steer the model; they don't guarantee correct numbers. Always have a qualified professional review before filing.
- **Tax law changes.** Rates and thresholds go out of date. The repo is a snapshot; [openaccountants.com](https://openaccountants.com) may be ahead of what you cloned.
- **Coverage is uneven.** 13 countries have the full accounting suite; many jurisdictions have VAT only or partial coverage. Check each country folder's README.
- **Newer domains need more eyes.** Bookkeeping, payroll, formation, and financial statements skills are research-verified but have fewer accountant sign-offs than the core tax skills.

---

## Disclaimer

For informational and computational purposes only. Not tax advice. Not a replacement for professional judgment. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date, verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Contact

**info@openaccountants.com** · [openaccountants.com](https://openaccountants.com)

## License

Dual-licensed: [AGPL-3.0](LICENSE) for open-source use, [commercial license](COMMERCIAL_LICENSE.md) for proprietary products.

Contributions are licensed to the project under the [Contributor License Agreement](CLA.md) — see [CONTRIBUTING.md](CONTRIBUTING.md).
