# Nicaragua — the legal database is live, and it is not the one the links point at

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Correcting the register entry above: the useful Nicaraguan authority is not the
tax administration but the **Digesto Jurídico Nicaragüense**
(`https://digesto.asamblea.gob.ni/`), the official consolidated legal digest,
which answers **200** and offers *Normas Jurídicas*, *Digestos Jurídicos* and a
documentary collection running from 1821.

`legislacion.asamblea.gob.ni` looks like the database and is not one. Over `http`
its `normaweb.nsf` is a Lotus Domino stub whose entire body is
`onload="window.location.href='http://www.asamblea.gob.ni'"` — a redirect with no
content; over `https` the connection resets. **A URL that looks like a database
endpoint can be a redirect with a database's name on it.**

The norms themselves sit behind `/consultas/normas/`, whose search is
JavaScript-driven — the static form exposes only a norm number and date ranges —
and whose documents are addressed as `shownorms.php?idnorm=<base64 of a numeric
id>`. `ni-company-formation.md` therefore stays on its commercial source for now,
but the gap is narrowed to **locating one code inside a working official database**
rather than finding an authority at all.
