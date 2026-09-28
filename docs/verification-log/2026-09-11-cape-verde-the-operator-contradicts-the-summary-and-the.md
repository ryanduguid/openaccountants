# Cape Verde — the operator contradicts the summary, and the code stays out of reach

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Following the register's own advice — go to the legal gazette, not the tax
authority, when the guide is about company formation — Cape Verde produced one
correction and one well-mapped dead end.

**The Imprensa Nacional de Cabo Verde**, the state gazette publisher, describes
*Empresa no Dia* itself: incorporation of Sociedades Anónimas and Sociedades por
Quotas *"de forma imediata, no próprio dia"* at a staffed Casa do Cidadão counter,
with **eight separate interactions with the administration** — legal, fiscal,
social and labour — collapsed into one. The guide said the timeline was
"approximately 1 to 2 weeks (faster via the one-stop shop)", on a commercial host.
**The body that runs the service says same day.** The row now cites INCV and says
so, with the caveat that a longer estimate may be describing steps outside the
service rather than the incorporation.

The *Código das Empresas Comerciais* is another matter, and the search is recorded
because it went four layers deep and still failed:

- `casadocidadao.cv` — the operator's own domain — answers **200 with a 17-byte
  body**. Live, and empty.
- There is **no `boe.cv` or `bo.cv`**, despite INCV describing an electronic
  Boletim Oficial as a free and universal public service. *(This bullet was a
  false negative produced by guessing at hostnames. The gazette is at
  **`boe.incv.cv`** and is open, complete and free. See "Cape Verde, resolved"
  below.)*
- INCV's Boletim Oficial page **displays its own feed error**: *"SSL certificate …
  has expired"*. The publisher cannot reach its own gazette feed.
- `legis-palop.org`, the Portuguese-speaking African countries' legal database, is
  live but serves through an opaque `?load=NNNNN` application loader.

So the capital figures stay marked, with one addition a reviewer can act on
immediately: **the guide gives a Sociedade Anónima the same CVE 1 minimum capital
as a Sociedade por Quotas**. A public limited company sharing a private one's
statutory floor is unusual enough that the claim should not be relied on without
an article number. **Noticing that a figure is implausible is not the same as
knowing it is wrong** — it is flagged, not corrected, because the code that would
settle it could not be opened. *(It was opened later, and the flag was right for
the wrong reason — see "Cape Verde, resolved" below.)*
