[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/openaccountants-openaccountants-badge.png)](https://mseep.ai/app/openaccountants-openaccountants)

# OpenAccountants

Open-source tax computation skills for AI. **514 skills across 133 countries + 51 US state packages.**

Upload to Claude, ChatGPT, or any LLM with your bank statement — or connect via **[MCP](#mcp-server)** so your AI loads the right country's tax skills automatically. Get a working paper ready for your accountant and **cut your accounting bill by 80%.**

Your accountant charges by the hour. Most of that time is classifying transactions and filling forms. These skills do that work before the meeting. Your accountant reviews and signs off in 20 minutes instead of 3 hours.

**Website:** [openaccountants.com](https://openaccountants.com)

### Two ways to use OpenAccountants

| Method | How it works | Best for |
|--------|-------------|----------|
| **Manual upload** | Download your country's folder, drag `.md` files into Claude / ChatGPT / any LLM | Quick one-off use, any LLM |
| **MCP server** | Install once, add one line of config — your AI discovers and fetches skills automatically, every conversation | Developers, power users, Claude Desktop / Cursor |

Both methods use the same skill files. MCP just removes the manual step. See **[Quick start](#quick-start-60-seconds)** for uploads or **[MCP server](#mcp-server)** for the automated path.

## Known limitations

Read this before you trust any output.

- **LLMs hallucinate and misread.** These files steer the model; they do not guarantee correct numbers, classifications, or filings. Always have a qualified professional review before you act.
- **Tax law changes.** Rates, thresholds, and forms go out of date. The repo is a snapshot; [openaccountants.com](https://openaccountants.com) may be ahead of what you cloned.
- **Verification is tiered, not binary.** Most skills are **not** “accountant-verified on real client data.” We publish [Q1–Q4 tiers](docs/QUALITY-TIERS.md): **Q1** is the bar for that; **Q2** is research-verified to authority sites but not yet proven on real statements; **Q3** is AI-drafted with citations but not independently verified. **Many skills are Q3 or below** — check the tier for the file you use.
- **Coverage is uneven.** Only **eight** countries ship the full guided stack (VAT + income tax + SSC + walkthrough) in this repo; dozens more have multiple skills without that guided path; **many** jurisdictions are **VAT/GST-only** or partial. See **Coverage** below and each country folder’s README.

Honesty is the point: if you know where the gaps are, you can use the project safely. Skeptics welcome.

---

## Quick start (60 seconds)

### 1. Find your country

Everything you need is in one folder under `packages/`. Upload every file in that folder.

```
packages/
├── malta/           ← 9 files (VAT + income tax + SSC + guided intake)
├── uk/              ← 8 files
├── germany/         ← 7 files
├── ... 130+ more countries
├── us-ca/           ← Federal + California state skills
├── us-ny/           ← Federal + New York state skills
├── us-tx/           ← Federal + Texas state skills
├── ... 51 US state packages (all 50 states + DC)
```

**International users:** pick your country folder (e.g. `packages/malta/`).

**US users:** pick `packages/us-[your state code]/` (e.g. `packages/us-ca/` for California). Each state package bundles federal skills (Schedule C, SE, QBI, estimated tax, etc.) **plus** your state's income tax, sales tax, and specialty taxes. See the [US state index](packages/us/README.md) for the full list, or the [source coverage matrix](skills/us-states/README.md) for what each state includes.

For MCP users, US state packages appear as `us-ca`, `us-tx`, `us-ny`, etc. alongside country packages.

Contributors: all packages are **generated** from source files under `skills/` by `scripts/build-packages.py`. Edit the source, not the package. See [CONTRIBUTING.md](CONTRIBUTING.md).

### 2. Upload to your LLM

Open the folder for your jurisdiction under `packages/`. Upload **all** `.md` files.

Upload to:
- **Claude.ai** → Create a Project, add files as Project Knowledge
- **ChatGPT** → Attach files to a conversation or create a Custom GPT
- **Any other LLM** → Attach or paste the files

### 3. Attach your bank statement and go

Say:

```
Help me with my 2025 taxes. Here's my bank statement.
```

The AI will ask a few questions, classify every transaction, and produce a working paper for your accountant.

---

## Are you an accountant?

These skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a qualified professional to verify it.

**You don't need to use GitHub.** Just:

1. Find your country's folder under `packages/`
2. Check the rates against your tax authority's website
3. Email your corrections to **info@openaaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever format works for you

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://openaccountants.com).

Or if you prefer GitHub: fork, fix, PR. **Your name goes on the skill either way.**

> 133 countries need accountant reviewers. Pick yours at [`packages/`](packages/) and be the first verified professional for your jurisdiction.

---

## What's in each package

Every country folder contains:

| File | What it does | Same everywhere? |
|------|-------------|-----------------|
| `foundation.md` | Tells the AI HOW to work — conservative defaults, output format, classification contract | Yes |
| `intake.md` | Onboarding questions, refusal checks, document inference | Yes (country name filled in) |
| `[country]-vat.md` | VAT/GST/sales tax rules, supplier pattern library, form mappings | No — country-specific |
| `[country]-income-tax.md` | Income tax brackets, deductions, transaction patterns | No — country-specific |
| `[country]-ssc.md` | Social security / pension contributions | No — country-specific |
| `[country]-bookkeeping.md` | Chart of accounts, P&L/balance sheet format, expense classification | No — 13 countries |
| `[country]-einvoice.md` | E-invoicing format, mandatory fields, transmission, penalties | No — 15 countries |
| `[country]-payroll.md` | PAYE withholding, social security, payslips, filing | No — 15 countries |
| `[country]-formation.md` | Entity types, registration steps, costs, compliance | No — 13 countries |
| `[country]-financial-statements.md` | Annual accounts, reporting framework, filing, audit | No — 13 countries |
| `[country]-transfer-pricing.md` | TP documentation, arm's length, CbCR, penalties | No — 15 countries |
| `[country]-guided-intake.md` | Full guided experience with detailed inference (if available) | No — 13 countries have this |
| `[country]-return-assembly.md` | Cross-checks between VAT, IT, and SSC (if available) | No — 13 countries have this |

**Not every country has every file.** Some have only VAT. Some have VAT + income tax + SSC + bookkeeping + e-invoicing. Thirteen countries have the full guided experience. Check the README inside each country folder.

---

## Coverage

### Full guided experience (13 countries)

Upload all files, say "help me with my taxes," and the AI walks you through everything:

| Country | What you get |
|---------|-------------|
| **Malta** | VAT + TA24 income tax + Class 2 SSC + provisional tax + rental + crypto |
| **United Kingdom** | VAT100 + SA103/SA100 + NIC + student loan + SA105 rental + SA108 CGT + dividends |
| **Germany** | UStVA + Einkommensteuer + Sozialversicherung + Gewerbesteuer + rental + crypto |
| **Australia** | BAS + ITR + super + Medicare levy + rental + crypto |
| **Canada** | GST/HST + T1/T2125 + CPP/EI + 10 provincial returns + crypto |
| **India** | GST + ITR-3/4 + advance tax + professional tax + PF/ESI |
| **Spain** | IVA + IRPF + RETA + rental + Modelo 111 |
| **France** | TVA + impot sur le revenu + cotisations sociales + CFE + crypto + rental + capital gains |
| **Japan** | Consumption tax + income tax + social insurance + estimated tax + e-Tax |
| **Netherlands** | BTW + inkomstenbelasting + ZZP deductions + payroll tax |
| **Brazil** | IVA + IRPF + INSS + Simples Nacional + estimated tax |
| **Mexico** | IVA + ISR + IMSS + CFDI + estimated tax |
| **United States (CA)** | 1040 + Schedule C/SE + CA 540 + crypto |

### Multi-skill countries (23 countries)

VAT + income tax + social contributions. No guided intake, but the AI uses the universal intake flow:

Argentina, Austria, Belgium, Chile, Colombia, Czech Republic, Greece, Hungary, Ireland, Israel, Italy, Kenya, New Zealand, Nigeria, Norway, Poland, Portugal, Romania, Singapore, South Africa, South Korea, Sweden, Switzerland

### Bookkeeping skills (13 countries)

Chart of accounts, double-entry posting, P&L and balance sheet generation with country-specific formats:

Malta, UK, Germany, France, Italy, Spain, Netherlands, Belgium, Portugal, Sweden, Australia, Canada, Japan

### E-invoicing compliance (15 countries)

Format validation, mandatory field checks, transmission methods, and penalty regimes:

Italy, France, Germany, Spain, Poland, Portugal, Romania, Belgium, Greece, Hungary, India, Saudi Arabia, Mexico, Brazil, Malaysia

### Payroll (15 countries)

PAYE/withholding tables, social security computation, payslip generation, employer filing obligations:

Malta, UK, Germany, France, Italy, Spain, Netherlands, Belgium, Portugal, Sweden, Australia, Canada, Japan, India, Brazil

### Company formation (13 countries)

Entity type comparison, registration steps, capital requirements, costs, post-formation compliance:

Malta, UK, Germany, France, Italy, Spain, Netherlands, Portugal, Australia, Canada, Japan, India, Singapore

### Financial statements (13 countries)

Annual accounts preparation, reporting framework by entity size, year-end adjustments, filing and audit:

Malta, UK, Germany, France, Italy, Spain, Netherlands, Belgium, Portugal, Australia, Canada, Japan, India

### Transfer pricing (15 countries)

TP documentation, arm's length methods, CbCR thresholds, APA, penalties:

Malta, UK, Germany, France, Italy, Spain, Netherlands, Australia, Canada, Japan, India, Brazil, Singapore, South Africa, Mexico

### VAT/GST only (87 countries)

Consumption tax classification with country-specific supplier pattern libraries. From Albania to Zimbabwe.

---

## How the skills work

### The supplier pattern library

Every country skill contains a lookup table of local vendors. When the AI sees "BANK OF VALLETTA" or "DEUTSCHE TELEKOM" or "STRIPE PAYMENTS UK LTD" on your bank statement, it already knows the classification — no guessing.

### Three outcomes per transaction

| Outcome | What it means | What happens |
|---------|--------------|-------------|
| **Classified** | Documents carry enough info | Applied automatically, no flag |
| **Assumed** | Data missing, conservative default applied | Flagged for your reviewer with the assumption disclosed |
| **Needs Input** | Can't proceed without asking you | One targeted question |

### Conservative defaults

When uncertain, the system always assumes MORE tax, never less. Your accountant can override a conservative position. They can't easily undo an aggressive one.

---

## Quality tiers

Skills are **partially** verified at best unless you confirm the tier. **Q1** means practitioner sign-off on real data; most files are **not** Q1. Full definitions: [docs/QUALITY-TIERS.md](docs/QUALITY-TIERS.md).

| Tier | What it means |
|------|--------------|
| **Q1 — Accountant-verified** | Run against real bank statements. Multiple iterations. Licensed practitioner signed off. |
| **Q2 — Research-verified** | Every rate verified against tax authority websites. Not yet tested on real data. |
| **Q3 — AI-drafted** | Full structure and citations. Not independently verified. |

---

## MCP server

Instead of uploading files by hand, connect your AI client to OpenAccountants via the [Model Context Protocol](https://modelcontextprotocol.io/). Install once, configure once — every future conversation can pull the right country's skills automatically.

### How it works

```
You:    "Help me with my Malta taxes. Here's my bank statement."
          ↓
Claude: calls list_jurisdictions → sees "malta"
Claude: calls list_files("malta") → foundation.md, malta-vat.md, …
Claude: calls get_file("malta", "foundation.md") → full skill loaded
          ↓
Claude: processes your bank statement with the correct tax rules
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

Full setup details, `uv` instructions, and environment variables: [`mcp/README.md`](mcp/README.md).

---

## For developers

### Clone the repo

```bash
git clone https://github.com/openaccountants/openaccountants.git
```

### Repo structure

```
openaccountants/
├── packages/              ← Ready-to-use jurisdiction packages (START HERE)
│   ├── malta/
│   ├── uk/
│   ├── us-ca/
│   ├── us-ny/
│   └── ... 130 countries + 51 US states
├── skills/                ← Source files (for contributors)
│   ├── foundation/        ← Workflow bases: VAT, income tax, bookkeeping, e-invoicing, US tax
│   ├── federal/           ← US federal income tax / Schedule C / SE / QBI / etc.
│   ├── international/     ← Country-specific content (feeds build-packages.py)
│   ├── orchestrator/      ← Intake + assembly (incl. us-federal-return-assembly, us-ca-*)
│   ├── us-states/         ← US state tax skills (all 50 states + DC, by 2-letter code)
│   ├── cross-border/      ← Reverse charge, WHT, PE risk
│   ├── intelligence/      ← Deadlines, thresholds, optimisation
│   └── patterns/          ← Global vendor patterns
├── scripts/               ← Build tools
│   └── build-packages.py  ← Generates packages/ from skills/
└── docs/                  ← Planning docs, architecture, roadmaps
```

### Rebuild packages after editing skills

```bash
python3 scripts/build-packages.py
```

---

## Contribute

We maintain 514 skills across 133 countries. Tax law changes constantly — rates update, thresholds move, forms get revised. Contributions keep this accurate.

### Ways to contribute

| What | How | Impact |
|------|-----|--------|
| **Verify a rate** | Check a number against your tax authority's website, open a PR | Moves a skill from Q3 → Q2 |
| **Add bank patterns** | Add how transactions appear on your local bank statement | Every user in your country gets fewer misclassifications |
| **Fix an error** | Find a wrong rate or outdated threshold, submit the correction | Prevents bad working papers |
| **Add a skill** | Write a new income tax, payroll, or social security skill for your country | Fills a gap for every user in that jurisdiction |

### How to verify or fix a skill

1. Find your country under `packages/`
2. Compare rates against your tax authority's website
3. Fork, fix, PR — or email corrections to **info@openaccountants.com** in any format

### How to add a new skill

1. Use any existing skill as a template (e.g., `packages/malta/malta-income-tax.md`)
2. Follow the same structure: quick reference table, rate tables, worked example, conservative defaults
3. Cite your sources (tax authority URL, legislation reference, or open-source repo)
4. Submit a PR

### Credits

Every contributor is credited publicly on the skill file and at [openaccountants.com](https://openaccountants.com).

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

**Pull requests:** contributions are accepted under the [Contributor License Agreement (CLA.md)](CLA.md). You explicitly agree by ticking the CLA box in the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) when you open a PR.

---

## Disclaimer

All skills and outputs are for informational and computational purposes only. Not tax advice. Not a replacement for professional judgment. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date, verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Contact

**info@openaaccountants.com**

## License

Dual-licensed: [AGPL-3.0](LICENSE) for open-source use, [commercial license](COMMERCIAL_LICENSE.md) for proprietary products.

Contributions are licensed to the project under the [Contributor License Agreement](CLA.md); see [CONTRIBUTING.md](CONTRIBUTING.md) and the PR template for how you opt in.
