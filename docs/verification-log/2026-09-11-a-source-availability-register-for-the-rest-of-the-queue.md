# A source-availability register for the rest of the queue

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Having built a browser that clears bot challenges, the sensible next step was to
point it at every remaining queue jurisdiction at once rather than discover the
same dead ends one file at a time. The results below are **evidence about this
environment on 2026-09-10**, not a verdict on the sites themselves — a host that
does not answer here may be geo-restricted, may be blocking the egress proxy, or
may simply have been down. Recorded so the next person does not repeat the search.

**Live, and the authority publishes usable law**

- **Armenia** — `arlis.am` serves the consolidated Tax Code and the LLC Law in
  full text. Worked through above; the guide is rewritten on it.

**Live, but not the document the guide needs**

- **Guinea** — `dgi.gov.gn` clears its challenge in a browser and its library was
  read in full. It publishes finance laws, arrêtés and reports; **no Code Général
  des Impôts**. Covered above.
- **Nicaragua** (`dgi.gob.ni`), **Myanmar IRD** (`ird.gov.mm`), **Cape Verde
  Finance Ministry** (`mf.gov.cv`) — all answer HTTP 200 with real pages. Each is
  a *tax* authority, and each jurisdiction's queue entry is a **company formation**
  guide, whose authority is a companies registry or a commercial code. **Reaching
  an authority is not the same as reaching the right authority**, and these three
  are the best remaining leads precisely because the obstacle is now knowing which
  instrument to ask for rather than whether anyone will answer.

**Reached, and empty**

- **São Tomé and Príncipe** — `mf.gov.st` answers, with the title *"Under
  construction - Awesome site in the making!"* and **91 characters of body text**.
  Three guides sit on the queue behind a ministry site that has not been built.
  `impostos.st`, `minfinancas.st`, `mpf.gov.st` and `impostos.gov.st` have no DNS.

**Resolve but never serve — the browser failed too, so this is not a challenge**

- **Gabon** `dgi.ga` → 197.231.72.25; **Eritrea** `mof.gov.er` → 196.200.102.238;
  **Myanmar DICA** `dica.gov.mm` → 103.89.50.27. Each resolves, each refuses the
  connection to both a plain client and the browser. Note the split in Myanmar:
  the **tax** authority answers and the **companies registry** does not, and the
  registry is the one the formation guide needs.

**No DNS at all**

- Cuba `onat.gob.cu`; Djibouti `impots.dj` and `impots.gouv.dj`; Vanuatu
  `customsinlandrevenue.gov.vu`; Central African Republic `impots.cf`;
  Turkmenistan `minfin.gov.tm`.

**Deliberately not pursued**

- **Iraq** — a Cloudflare WAF deny, which is a firewall rule someone configured on
  purpose. It is left alone. The guide stays marked, and 13 of its 14 citations
  stay on one commercial host, because the alternative is evading a control the
  site owner chose to apply.

The distinction worth keeping is between the three states above: **no DNS** is a
dead address, **resolves-but-refuses** is a live address behind something, and
**answers-with-a-placeholder** is a live site with nothing in it. Only the first
is safely permanent; the other two are worth retrying from a different network
before a guide is written off, and none of the three is a reason to present a
commercial figure as though it were checked.
