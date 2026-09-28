# Spain — the guide had the statute in hand and read one thing out of it

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`es-corporate-tax.md` cites **Ley 7/2024** three times: once in Quick Reference as
*"Ley 7/2024 (reform)"*, and twice as the authority for its 2025 rate tables. It
contains **zero** mentions of the Impuesto Complementario — which the same Ley 7/2024
creates.

This is a distinct shape from the five before it. Nigeria, India, Kuwait, Oman and the
Netherlands were all *"the pack knows and the file that will be read does not say"*.
Here nothing else in the pack knew either. **The file cited the right statute and took
one thing out of it.** A citation is evidence the source was reached, not evidence it
was read to the end — and the check that catches this is not a cross-file comparison
but asking, of a statute a guide already cites, *what else is in it?*

Getting to the text needed the same form-driving as the Netherlands, and one wrong turn
worth recording. `BOE-A-2024-26695` looked like the obvious identifier and **is a
Congress resolution about an unrelated decree-law**; Ley 7/2024 is `BOE-A-2024-26694`,
one lower. A guessed identifier fails exactly like a guessed hostname: it returns a
real, well-formed document that is not the one you wanted. The BOE search also has to
be driven through its form — its field is `dato[2]`, and a hand-built query string
using `dato[0]` returns a page with zero results rather than an error.

What the consolidated text gives:

- **The commencement date is not the date it takes effect from.** *Entrada en vigor*
  is **22 December 2024**; disposición final 22ª makes it take effect for tax periods
  **beginning on or after 31 December 2023** — reaching back behind its own entry into
  force — with the UTPR from periods beginning on or after 31 December 2024. Reading
  the BOE header date alone gives the wrong answer for a 2024 period.
- **The rate is a difference, not a charge.** *«la diferencia positiva entre el tipo
  impositivo mínimo del 15 por ciento y el tipo impositivo efectivo calculado a nivel
  jurisdiccional»*. "15%" stated bare, as in the earlier Kuwait row, invites the reader
  to apply 15% to profit.
- **Three modalities**, and the Act's own preamble names them: *nacional*, *primario*,
  *secundario* — the first two from the income inclusion rule, the third the UTPR. The
  *nacional* modality is what reaches an entity **located in Spanish territory**. Third
  jurisdiction in a row where the charge that actually reaches a local subsidiary is
  not the one a summary would name.
- **Grupos nacionales de gran magnitud** are in scope — a wholly Spanish group, as in
  the Netherlands and unlike Oman.
- **The foral point the guide's own structure demanded.** This guide has a Foral
  Territories rate table. The Impuesto Complementario has *separate foral instruments*
  — Navarra's is **Ley Foral 18/2025, de 22 de diciembre** (BOE-A-2026-3911). Adding
  the state charge without saying that would have left a foral-domiciled reader
  applying the wrong instrument.
- The Ley has been modified twice and was last consolidated 25 July 2025; the
  **Reglamento** is *Real Decreto 252/2025, de 1 de abril* (BOE-A-2025-6598) and has
  not been read. Both recorded as gaps.

**Running tally on the two-of-four test.** Oman art. 2, Kuwait, and the Netherlands
art. 2.1(1) all state the EUR 750m threshold as *at least two of the four immediately
preceding* periods. Spain's preamble states the EUR 750m figure without that
qualification, so the operative article is where it must be confirmed before the
two-of-four wording is asserted for Spain — and it is **not** asserted in the guide.
Three confirmations do not make a fourth.
