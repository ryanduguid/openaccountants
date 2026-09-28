# The "no DNS at all" list was partly measured against the wrong hostnames

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Madagascar produced a small correction that turned out to be a pattern: the register's
"503 on every attempt" was measured against `impots.mg`, **which has no DNS**, while
`www.impots.mg` resolves. That is a wrong-hostname error, not a site failure, and it cost
nothing to check whether it had happened elsewhere. A DNS sweep over alternative hostnames
for every remaining single-source jurisdiction:

| Recorded as | Actually resolves |
|---|---|
| CAR `impots.cf` — no DNS | **`finances.gouv.cf`** → 83.166.138.102 |
| Djibouti `impots.dj`, `impots.gouv.dj` — no DNS | **`ministere-finances.dj`** → 197.241.17.172 |
| Cuba `onat.gob.cu` — no DNS | **`www.onat.gob.cu`**, and **`www.gacetaoficial.gob.cu`** — www only, bare names dead |
| Vanuatu `customsinlandrevenue.gov.vu` — no DNS | **`doft.gov.vu`**, **`parliament.gov.vu`** |

Four of the six entries under "No DNS at all" were **testing names that were never the
ministry's**. The corrected picture: CAR and Djibouti answer 200 with real content; Cuba's
two hosts resolve but **reset the connection**; Vanuatu's two fail certificate
verification with "unable to get local issuer certificate" even with the CA bundle, and
were **not** retried with verification disabled.

That does not rescue every jurisdiction. It rescued two, and one of them was worth the
whole sweep.
