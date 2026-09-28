# Kuwait Zakat consistency correction, 13 September 2026

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The remaining contradiction in `kuwait-tax.md` affected the quick-reference
table, section 5.3, the mixed-ownership example and the unlisted-company test.
They made listing a condition for Zakat, while the same file's first edge case
and `kw-corporate-income-tax.md` used the shareholding-company legal form.

The Ministry of Finance's indexed text of [Law No. 46 of 2006, Article
One](https://mof.gov.kw/Desicions/Decree/PDF/Law46_2006e.pdf) states the ordinary
annual 1% net-profit charge. Its title identifies public and closed shareholding
companies, also shown in the [Ministry's legislation
catalogue](https://www.mof.gov.kw/MOFDesicions/MOFDesicionsDetails.aspx). This
supports removing an exemption inferred solely from an unlisted status.

Both guides now use that scope consistently. The unlisted-company example asks
for the legal form before deciding liability. The mixed-ownership example
separates the ordinary CIT ownership test from the Zakat legal-form test and
leaves calculation-base exclusions and exemptions for verification. The
description no longer implies every Kuwaiti entity pays Zakat. The primary
source does not establish that every shareholding company owes the charge in
every period; the guides explicitly require checking exemptions and DMTT.

Direct HTTPS downloads from the Ministry's bare and www hosts failed with
connection resets, including a request through Python's certificate-verified
client. No complete PDF was obtained or parsed, and no TLS bypass was used.
The DMTT legislation download also failed. The evidence here is indexed primary
material, not a full reading of the law, implementing regulations or amendment
chain. Those limits and pending professional review remain in both guides.

Python 3.11 verification passed: 133 repository tests, 19 MCP tests, changed-guide
validation for 103 guides, and the deadline-rule check with zero disagreements.
Full validation passed for 1,953 guides and 5,072 generated frontmatter blocks,
with the five inherited missing-jurisdiction warnings in jurisdiction-agnostic
directories. Generated outputs were inspected by validation but remain untouched.
