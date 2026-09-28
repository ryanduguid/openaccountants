# The seven jurisdictions citing no authority — four of them had never been tried

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`scripts/list-source-mix.py` reports **seven jurisdictions with no authority citation at
all**: Madagascar (65 secondary citations), Angola (63), Mauritania (54), Laos (52),
São Tomé and Príncipe (39), Turkmenistan (36), Eritrea (29).

Three were already documented dead ends — `mf.gov.st` serves 91 characters,
`minfin.gov.tm` has no DNS, `mof.gov.er` resolves and never serves. **The other four had
no register entry at all.** A jurisdiction resting 50-odd citations entirely on
commercial summaries is a recorded exposure; a jurisdiction where nobody has *checked
whether the authority answers* is not the same thing, and the two were indistinguishable
in the count. Tested:

| Jurisdiction | Result | What it means |
|---|---|---|
| **Mauritania** | **`https://impots.gov.mr/DGI/` → 200, 82 KB.** Title *"Direction générale des impôts"*, with NIF and receipt verification services and press releases | **Reachable, and unused.** Two traps on the way: `www.impots.gov.mr` serves a **JavaScript redirect to a plain `http://` URL**, which an HTTPS-only proxy cannot follow; and the bare `/DGI` path 302s — the **trailing slash** is what returns the site |
| **Laos** | `www.mof.gov.la` → 200, 219 KB, live Ministry of Finance site (ກະຊວງການເງິນ, ສປປ ລາວ) with a **ກົດໝາຍ ແລະ ນິຕິກຳ** — "Laws and Legislation" — item in its own navigation | **Ministry live, its own laws link broken.** `https://www.mof.gov.la/laws&legal` returns a bare Apache **404**, to `curl` and to a real browser alike. The homepage is usable as an authority; the legislation section it advertises is not |
| **Angola** | `agt.minfin.gov.ao` → 301 to `/PortalAGT/`, 200 but **3 KB of markup and 5 characters of text** | A JavaScript shell. Not a dead host — needs a rendering browser, and has not been pursued further here |
| **Madagascar** | `impots.mg` and `www.impots.mg` → `curl: (60) unable to get local issuer certificate`, **and `--cacert /root/.ccr/ca-bundle.crt` does not fix it** | An origin serving an incomplete chain the bundle does not cover. Not fetched; verification left on |

**Four jurisdictions, four different situations, four different next steps** — and only
one of them ("the authority does not serve") is the thing the bare count implied. The
most useful of the four is Mauritania: a working national tax authority that fifty-four
citations have gone around, and the only reasons it looked unreachable were a
plain-`http` redirect target and a missing trailing slash.

**Madagascar is the third missing-intermediate wall today**, after `mjla.gov.om` and
`slvesnik.com.mk`. In both earlier cases the revenue authority carried the text the
ministry could not serve. That is now a standing first move rather than a fallback.

`list-source-mix.py` already prints the right caveat on its own output — *"This ranks
exposure, not diligence."* The corollary this adds: **a zero in that column is a question,
not an answer.** It says no authority link is present. It does not say why, and the four
whys here are not alike.

**Mauritania, qualified — the site is reachable and its content stops in 2020.** Having
established that `https://impots.gov.mr/DGI/` serves, the next question is what it
serves. Its downloads page carries dozens of official declaration forms in PDF and
Excel — IS (including a separate mining-company return), IRF, ITS, TVA, TOF, TSA,
patente, and an annual transfer-pricing declaration. Its news section carries the
*Code Général des Impôts 2020*, the Lois de finances for 2019 and 2020, and
*Arrêté Ministériel n°39/2020*.

**Every dated filename on that page is 2019 or 2020, and the only year appearing in its
text is 2020.** So the correct entry is narrower than "the authority works":

> `impots.gov.mr/DGI/` — **reachable, and authoritative for what it holds.** Good for
> **form existence, form structure and the 2020-vintage CGI**. Poor for **current rates
> and thresholds**, because nothing published there appears to postdate 2020. A 2025
> guide cannot be sourced to it for a rate without establishing that the rate has not
> moved in five years — which is a separate piece of work, not an inference.
> One caution: a link on that page points at `dgi.gtishow.com`, a contractor's host,
> which suggests parts of the site still resolve outside the government domain.

This is a correction to the entry written a few paragraphs above, made within the same
sitting. "Reachable" and "usable for the figure I need" are different findings, and the
first was recorded before the second was checked. **The gap between them is exactly where
an over-claim would have gone** — a note saying Mauritania's fifty-four secondary
citations can now be upgraded, when what is actually available is a set of 2020 forms.
