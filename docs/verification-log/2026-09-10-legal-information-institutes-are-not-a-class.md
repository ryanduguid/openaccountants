# Legal information institutes are not a class

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Reading the statute-link queue's destinations turned out to be a way of asking
the authority allowlist what it was missing, and it named four: `u.ae` ("The
Official Platform of the UAE Government"), `nssfug.org` (Uganda's NSSF, the
statutory fund that collects the charge), `eswatinilii.org` and `namiblii.org`.

The last two are the interesting ones, because the obvious move — treat LIIs as
a class — is wrong in both directions. The test this repo uses is whether the
domain belongs to the body that makes, administers or collects the charge, *or
publishes the official text of the law*. Applied to three LIIs:

| Site | Run by | On the list? |
|---|---|---|
| EswatiniLII | "the Judiciary of eSwatini" | yes |
| NamibLII | "the Law Reform and Development Commission" | yes |
| ZambiaLII | SAIPAR, "an independent, educational and development oriented research centre", collecting cases "indirectly from the Zambian judiciary" | **no** |

Three sites, near-identical front pages, same software, same movement — and the
test splits them. Adding them wholesale would have credited a research centre's
republication as the official law; skipping them wholesale would have kept two
state publishers scored as marketing sites.

`onrc.ro` and `registrucentras.lt` are almost certainly authorities too. Both
were left off, because both answer a script with a rejection and neither could
actually be read. Adding a domain because its name and reputation fit is exactly
how `manao.mg` got onto this list in the first place.
