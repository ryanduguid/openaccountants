# Madagascar — the Angola move, tried and failed, which is also a result

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Angola's lesson was that "needs a browser" is an unopened door. Madagascar is the largest
remaining zero-authority pack — **65 secondary citations, no authority** — so it got the
same treatment. It did not open, and the detail is worth keeping:

- **`impots.mg` has no DNS at all.** The earlier record says "503 on every attempt, two
  days apart", which was measured against a hostname that does not resolve. **`www.impots.mg`
  does** resolve, to 41.188.38.190 — so the earlier probe was partly testing the wrong name.
- It makes no difference to the answer. `https://www.impots.mg/` resets the connection;
  `http://www.impots.mg/` returns **503 with a 48-byte body**. The origin is down, not
  hiding behind JavaScript, and the 503 finding stands.
- **`mef.gov.mg` answers 200 — and is a Zimbra webmail login**, not a content site. It
  was not pursued past the front page.
- **`www.douanes.gov.mg` is live** (200, 72 KB) with a real `/textes/` legislation page.
  It is the **customs** authority; Madagascar's guides are income tax and VAT under the
  *Code Général des Impôts*, so it is the wrong tree, and its document list is rendered
  client-side in any case.

Recorded because the Angola result makes the opposite error tempting: one jurisdiction
opening with a browser is not evidence that the rest will. Madagascar is still genuinely
unreachable on the route its guides need, and the corrected detail — bare name NXDOMAIN,
`www` resolves, origin 503 — is what a future attempt should start from.
