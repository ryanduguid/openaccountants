# Source-availability register — Oman

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

| Host | Result |
|------|--------|
| `tms.taxoman.gov.om` | **Live and authoritative.** JavaScript application: `curl` returns markup with no readable content, so the laws index needs a rendering browser. Linked PDFs then fetch fine over `curl` with a referer. Carries the Income Tax Law, its Executive Regulation, the Top-up Tax Law (RD 70/2024), Chairman Decisions, and the superseded 1981/1989/2009 laws |
| `mjla.gov.om`, `www.mjla.gov.om` | **TLS chain incomplete.** `curl` fails with "unable to get local issuer certificate", and passing `--cacert /root/.ccr/ca-bundle.crt` does not fix it, so the origin is serving an incomplete chain the bundle does not cover. Not worked around — verification stays on. The Tax Authority carried the text anyway, so nothing was lost |

The general point: **the gazette is not the only authoritative publisher.** The
first attempt here went to the Ministry of Legal Affairs because that is where a
gazette lives, hit a certificate wall, and the answer was sitting on the tax
authority's own website the whole time. Search for the subject, not the publisher
you expect to hold it.
