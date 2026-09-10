---
name: references
description: Primary source references and related open-source projects for Argentina.
version: 1.1
jurisdiction: AR
tax_year: 2025
last_updated: 2026-09-10
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

# References

> **This file previously contained Vietnam's references, in full.** Under a
> `jurisdiction: VN` frontmatter, in the Argentina directory, it listed two
> Vietnamese personal-income-tax repositories and cited *Luật số 109/2025/QH15*,
> *Luật Thuế TNCN No. 04/2007/QH12* and *Thông tư 111/2013/TT-BTC* — under the
> heading *"Vietnam — Related Open-Source Projects"*. All 32 other `references.md`
> files carry the jurisdiction code of the directory they sit in; this was the only
> mismatch.
>
> **The real Argentine content was never lost.** It survived in
> `agent-skills/argentina-references/`, the hand-maintained tree that CLAUDE.md
> describes as inheriting nothing from `skills/`. Independence cuts both ways: a
> tree that does not receive corrections also does not receive corruptions, so when
> one copy is wrong **the parallel tree is the first place to look**. The projects
> below are restored from it rather than rewritten.

## National tax authority

- **ARCA — Agencia de Recaudación y Control Aduanero** is the federal tax and
  customs authority, created by Decreto 953/2024 in place of AFIP. Its portal
  identifies itself as ARCA throughout and the former `afip.gob.ar` domain now
  resolves to the same site  _(ARCA, portal principal — https://www.arca.gob.ar/landing/default.asp)_

## Related open-source projects

OpenAccountants is AGPL-3.0. AGPL-3.0 and LGPL-3.0 are compatible licences.
Projects below can be incorporated with attribution.

### pyafipws

- **reingart/pyafipws** — Repository: https://github.com/reingart/pyafipws. Licence: LGPL-3.0. Language: Python. Scope: *Factura Electrónica AFIP y otros servicios web* — interfaces, tools and apps for Argentina's government web services (SOAP, COM/DLL, PDF, DBF, XML, JSON). The definitive open-source Argentine e-invoicing library. Integration: LGPL-3.0, compatible — web-service integration patterns, e-invoice generation and authentication flows are directly reusable for Argentine tax-compliance automation  _(https://github.com/reingart/pyafipws)_

### PyARCA

- **GeraCollante/PyARCA** — Repository: https://github.com/GeraCollante/PyARCA. Licence: LGPL-3.0. Language: Python. Scope: *CLI para facturación electrónica Monotributo (ARCA/ex-AFIP)*, a fork of pyafipws focused on Monotributo invoicing. Integration: LGPL-3.0, compatible — reference for Monotributo-specific invoicing workflows and ARCA interactions. **Its own scope line names the authority as "ARCA/ex-AFIP"**, which corroborates the rename above from a source independent of the authority itself  _(https://github.com/GeraCollante/PyARCA)_

## Key legislative sources

The Argentine guides in this pack cite the Impuesto a las Ganancias, IVA and
Monotributo régimes and ARCA's *Resoluciones Generales*. [RESEARCH GAP — this file
does not yet list the consolidated texts and RG numbers those guides rely on. A
reviewer should populate it from ARCA's own *Biblioteca Electrónica*, and the
per-guide citations should then point at entries here.]

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
