---
name: references
description: "Reference entry for Argentine tax research and electronic invoicing. Identifies ARCA as the federal tax and customs authority and lists pyafipws and PyARCA as external software references for government web services and Monotributo invoicing. Use when locating Argentine source material, checking an AFIP-to-ARCA reference or assessing an invoicing integration. The consolidated legislative texts and resolution numbers remain a documented research gap. Consult each tax guide and the authority before relying on a rule. Check the actual upstream licence and OpenAccountants licensing policy before copying or distributing third-party material."
version: 1.2
jurisdiction: AR
tax_year: 2025
last_updated: 2026-09-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

# References

## National tax authority

- **ARCA — Agencia de Recaudación y Control Aduanero** is the federal tax and
  customs authority, created by Decreto 953/2024 in place of AFIP. Its portal
  identifies itself as ARCA throughout and the former `afip.gob.ar` domain now
  resolves to the same site  _(ARCA, portal principal — https://www.arca.gob.ar/landing/default.asp)_

## Related open-source projects

OpenAccountants uses separate licences for software and Guides. See
[LICENSING.md](../../../LICENSING.md). These projects are references, not blanket
permission to copy their code or documentation. Check the upstream licence for
the material and intended use; attribution alone does not satisfy every licence
condition.

### pyafipws

- **reingart/pyafipws**: Repository: https://github.com/reingart/pyafipws. Licence: LGPL-3.0. Language: Python. Scope: *Factura Electrónica AFIP y otros servicios web*: interfaces, tools and apps for Argentina's government web services (SOAP, COM/DLL, PDF, DBF, XML, JSON). Reference for web-service integration, e-invoice generation and authentication flows; assess reuse against the upstream licence  _(https://github.com/reingart/pyafipws)_

### PyARCA

- **GeraCollante/PyARCA**: Repository: https://github.com/GeraCollante/PyARCA. Licence: LGPL-3.0. Language: Python. Scope: *CLI para facturación electrónica Monotributo (ARCA/ex-AFIP)*, a fork of pyafipws focused on Monotributo invoicing. Reference for Monotributo-specific invoicing workflows and ARCA interactions; assess reuse against the upstream licence  _(https://github.com/GeraCollante/PyARCA)_

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
