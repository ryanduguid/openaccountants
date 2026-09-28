# Two ways to manufacture a false "unreachable", both hit in one sitting

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The register above is only worth having if its verdicts are about the sites rather
than about this environment's configuration. Two faults found immediately after
publishing it would each have produced convincing, entirely false entries. Both
are recorded because **a tooling failure and a dead host look identical from the
outside** — an empty page and a note saying it could not be loaded.

**1. The proxy port moved and the drivers hardcoded the old one.** The container
restarted; the egress proxy came back on a different port. Every browser driver
carried the previous port as a literal, so each fetch returned *"Problem loading
page"* — the exact signature recorded for Gabon, Eritrea and Myanmar's registry.
Nicaragua's National Assembly was written off on that basis and is, in fact, fine.

The tell was a **contradiction between two tools**: `curl` reached the host and
returned a Cloudflare challenge while the browser could not reach it at all. That
is backwards — the browser is the more capable client. **When the weaker tool
succeeds where the stronger one fails, suspect the stronger one's configuration
before you conclude anything about the host.** Every driver now reads
`process.env.HTTPS_PROXY` instead of a literal.

The register's own entries survive this, because those tests ran **before** the
restart, on the port that was then correct. That is a fact about timing rather
than a defence of the method: had the restart come an hour earlier, three
jurisdictions would have been recorded as dead on the strength of a stale port.

**So they were re-tested rather than left resting on that.** With the corrected
proxy and `https://` throughout: Gabon `dgi.ga` and Myanmar's `dica.gov.mm` still
never load; Eritrea's `mof.gov.er` still returns *"Problem loading page"*; and São
Tomé's `mf.gov.st` still answers **202** with *"Under construction - Awesome site
in the making!"* and 91 characters of body. Every entry holds. **Publishing a
claim, finding two ways it could have been wrong, and then re-running it is the
cheap half of the work** — the expensive half was noticing the tools disagreed.

**2. The proxy tunnels HTTPS only, and government sites still link `http://`.**
`digesto.asamblea.gob.ni` returned **405 with a 465-byte body** through the
browser. The body is not from the site — it is the proxy saying *"this proxy only
accepts HTTPS CONNECT tunnels."* Every link to the Digesto on the Assembly's own
home page is `http://`, so following the site's own navigation produces a
plausible-looking failure at the first hop. **The same URL over `https://` returns
200 and 46 KB.**

So a scheme the site itself publishes is enough to make a live authority look
dead. **Rewrite `http://` to `https://` before recording any failure**, and read
the error body rather than the status code — a 405 that explains itself is not a
site rejecting you.
