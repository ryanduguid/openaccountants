# Nothing in this repo asked whether a cited host exists, so 1,254 of them were resolved

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Vanuatu's employer-registration row cited `employmentvanuatu.gov.vu`. It resolves to
**192.0.2.1** — TEST-NET-1, the RFC 5737 documentation range, never routed. That is not a
site that went down; it is an address that was never a site. Every other check here asks
whether a citation *says* the right thing. None asks whether the thing it points at
exists. So: extract every hostname cited anywhere in `skills/**` and `agent-skills/**`,
and resolve it.

**The first pass returned 42 failures out of 1,272 hosts. Eleven of them were real.**
Getting from one number to the other is the whole exercise, and each step removed a class
of false accusation:

| Step | Effect |
|---|---|
| Retry three times | **3 removed** — `isap.sejm.gov.pl`, `www.ird.gov.mm`, `www.qhrm.io` resolved on a second attempt. Three false accusations avoided by waiting 0.4 seconds |
| Try `www`/bare and parent | **23 reclassified** as *deep-link* — the subdomain has no address but the authority's domain does. A different and much weaker finding than a dead domain |
| Skip URL templates | **2 removed** — Brazil documents `https://nfe.sefaz{UF}.{domain}/...`; a regex that stops at `{` invents the host `nfe.sefaz` and reports a defect in a correct line |
| Validate the hostname | **16 removed** — see below |

**That last row is the one worth keeping.** The extractor's stop-set did not include
markdown emphasis or CJK punctuation, so it produced:

- `www.sarsefiling.co.za**`, from `**https://www.sarsefiling.co.za**` — the checker
  reported as dead **the very host I had just verified live and corrected six files to
  point at**. Eight hits of this shape, including four Nigerian professional bodies.
- `etax.chinatax.gov.cn）完成提交。本技能不替代法定审计、税务鉴证或专业税务师事务所服务。` —
  China's guides write `（https://etax.chinatax.gov.cn）` with full-width parentheses, and
  a whole sentence of Chinese came through as a "hostname". Eight hits.

**So the naive version's strongest grade was 41% precise (11 of 27), and its most
confident output was a fabrication about a host I had personally opened in a browser
minutes earlier.** The fix is not a longer stop-set — guessing where a hostname ends is
how the bug got in — but validating every candidate against what a hostname can be:
ASCII letters, digits, hyphens, dots. Anything else is the extractor's fault and must
never reach the report. Both failure modes are pinned in the selftest with the real corpus
text that produced them.

**What the surviving eleven are**, and the honest caveat that goes with them:
`cabinet.salyk.kz`, `its.jszxbs.cn`, `sessi.gos.pk`, `www.e-govern.ad`, `www.lstc.la.gov`,
`www.mohurd.gov.cn`, `www.petakner.am`, `www.shgjj.com`, `www.tax.gov.bm`,
`www.upravaprihoda.gov.me`, and `www.sarsefiling.gov.za`. The last is expected — that file
now names it in prose *as* the dead host. **A name that fails here may be geo-restricted,
served only inside the country, or behind split-horizon DNS.** Three of the eleven are
Chinese and one Kazakh, which is exactly where that caveat bites hardest. The script says
so in its own output rather than leaving the reader to infer it.
