# Angola — the authority was live all along, and it corroborated twelve rows

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

> **Superseded in part by the next section.** This records the state after the annex
> was read and before article 20(3) was. The hold described below was released on
> evidence, not dropped: the row citations now point at the gazette.

Angola was left above as "a JavaScript shell, not pursued further". Pursuing it took one
browser render.

`agt.minfin.gov.ao/PortalAGT/` is a fully working Angular application — it renders the
current date — with a real legislation tree: `legislacao/fiscal`, `/aduaneira`,
`/circulares`, `/instrutivos`, `/tributacao-especial`. The **Legislação Fiscal** page
serves **17 PDFs** hosted on `www.ucm.minfin.gov.ao`, the Ministry of Finance's document
repository. They download over plain `curl` with a referer.

The first one opened is the **Diário da República, I Série N.º 247, 30 December 2024** —
Angola's official gazette — carrying **Lei n.º 18/24**, the State Budget for 2025.

**Its Anexo I is the Tabela do IRT, and it matches the corpus on all twelve bands.**
`ao-income-tax.md` carried twelve IRT rows sourced entirely to a commercial summary.
Every escalão, every rate and every *parcela fixa* in the gazette annex corresponds —
including six unrounded fixed amounts (187,249 / 292,249 / 402,249 / 517,249 /
1,117,249 / 2,342,248). Six specific unrounded figures agreeing is not coincidence.

**Recorded as corroboration, not verification, and the distinction is load-bearing.**
The annex is headed *"TABELA DO IRT (**Proposta**)"*, and **article 20(3), which the annex
serves, was not read.** Whether "Proposta" is a drafting label left on an enacted annex
or means something requiring separate enactment cannot be settled from the annex alone.
So the row citations were left pointing at the commercial summary and a banner records
what the gazette shows. **Upgrading twelve citations on the strength of a matching table
whose heading says "proposal" is precisely the Burkina Faso move** — reading one document
and writing as though it settled the next.

**And the same gazette page carries a repeal and a suspension**, both flagged and neither
checked: Lei 18/24 revokes article 503 of the Código Aduaneiro, and **suspends the effect
of article 9(2) of the Código do Imposto sobre os Rendimentos do Trabalho** — the very
Code this guide is about. What article 9(2) provides has not been established.

Two things for the register:

- **Angola: reachable, current, and authoritative.** Unlike Mauritania, nothing here is
  frozen in 2020. A pack with 63 secondary citations and zero authority links had a live
  national gazette one browser render away. **"Needs a browser" is not a dead end; it is
  an unopened door**, and it stayed closed here only because the first `curl` returned
  five characters of text.
- **The gazette PDFs are pure scans** — zero extractable characters across eighteen
  pages, eighteen images on page one. Every figure was read from pages rendered at
  170–200 dpi, which is the same rule Oman's decree needed.
