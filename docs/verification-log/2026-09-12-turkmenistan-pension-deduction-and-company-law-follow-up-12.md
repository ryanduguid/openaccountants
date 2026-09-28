# Turkmenistan pension, deduction and company-law follow-up, 12 September 2026

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Parliament publishes the State Pension Insurance Law and Joint-Stock Companies Law.
The earlier inventory of the Tax Directorate's page was accurate for that page, but
did not establish that those statutes were unavailable from another official publisher.
The current Parliament publications also expose stale readings in this PR.

## Pension contributions and payroll

The [Pension Insurance Law](https://mejlis.gov.tm/single-law/218?lang=ru), articles
6–7 and 19–23, confirms 20% for covered employers and an additional 3.5% for the
professional pension stream. Article 20(4) sets a minimum 2% for voluntary pension
participation. The figures were right; describing the employee stream as
voluntary/mandatory was wrong. Article 19 specifies remuneration and exclusions
and has no upper wage ceiling for ordinary employees. Different insured categories
have different bases, so this does not support an uncapped rule for everybody.

Article 23(3) requires ordinary employer pension payment by the bank cash-withdrawal
or wage-transfer day. Article 21(2) separately requires the monthly declaration by
the 20th of the following month. The combined guessed 15th/20th deadline was removed.
Article 7(1) expressly addresses permanently resident foreign citizens and stateless
persons. Tax residency alone cannot establish pension coverage for every foreign hire.

## Personal deduction and income-tax collection

The [Tax Code](https://mejlis.gov.tm/single-code/10?lang=ru), article 188(1)(a), sets
the monthly personal deduction at one statutory base value for calculating taxes
and fees. Its current monetary value has not been verified. TMT 1,280 was removed
from both editable guides, without guessing a replacement. The handoff placed this
deduction with pension-law questions; its governing provision is in the Tax Code.
Searches for the operative base-value instrument did not establish a current amount.

Article 188(2) permits deductions for voluntary pension and medical insurance
contributions. Article 195(3) restricts employer-applied article 188 deductions to
the main employment and excludes its first incomplete month. Article 195(5) makes
withholding payable by the bank cash-withdrawal or income-transfer day, or the next
day for income in kind. Annual information is due by 20 January under article
195(9). These replaced the speculative following-month payment and monthly tax
reporting statements.

Article 187(5) also gives eligible young graduates entering employment a 50%
reduction of calculated tax for 12 months and 25% for the next 24 months. Article
192(1), amended in 2023, separately provides first/second/third-tax-year relief for
qualifying youth entrepreneurs with at least 75% of workers under 35. These are
conditional reliefs, not a progressive scale or a general lower rate.

The existing gambling correction labelled the activity as winnings while describing
charges per gaming machine, table and premises. Article 192(2) addresses individuals'
income from operating gambling activities. The heading now reflects that business
mechanism. The underlying daily amounts were retained from the earlier statutory check.

## Company capital: another correction withdrawn

The [current Law on Enterprises](https://mejlis.gov.tm/single-law/301?lang=ru), articles
26(5) and 29(4), uses 25 and 100 times the statutory tax base value. The earlier PR
correction used the minimum wage from an older Tax Directorate publication. That
formula is withdrawn. Fixed TMT 5,000/USD 20,000 capital claims still present below
the correction were also removed. Article 24's co-operative enterprise had been
translated as a partnership; the description now follows the Parliament text.

The [Joint-Stock Companies Law](https://mejlis.gov.tm/single-law/308?lang=ru), article
12, requires at least 200 times the statutory tax base value, half paid at registration
and full payment within 12 months. Initial shares go to founders, with no public
subscription at formation. The final review also read Law on Enterprises article
47: it requires at least 50% of founders' contributions after signing the founding
documents and before applying for registration, with the balance within one year
after registration. The first draft unnecessarily left this enterprise schedule
unverified. It also duplicated the 100-times capital row; the reviewed guide now
distinguishes the sole enterprise's 25-times base from the economic company's
100-times base.

Scope: read the pension contribution provisions, Tax Code articles 187(5), 188, 192
and 195, enterprise-form/capital provisions including article 47, and joint-stock capital provisions in the
Parliament HTML publications. This was not a full reread of every article of those
laws. Unrelated corporate tax and individual declaration findings were preserved.
The current statutory tax base value and the remaining consultancy-based formation
steps remain open. No generated packages were changed.

Source captures (12 September 2026; SHA-256):

- [tm-pension-law](https://mejlis.gov.tm/single-law/218?lang=ru): 204,871 bytes, `1b8df016d260ca01948f10f940314f2be70f171ca263eeab68d6609a776e7e7f`.
- [tm-tax-code](https://mejlis.gov.tm/single-code/10?lang=ru): 1,084,696 bytes, `17c0e65798f865818a82cab2b1c93b4b1af642e9ba829df58331bc1bccfcc3a4`.
- [tm-enterprises-law](https://mejlis.gov.tm/single-law/301?lang=ru): 162,012 bytes, `cef94c3439975fcac78a1426d499613c5d923c5cb7797f73873fd1f943d193dc`.
- [tm-jsc-law](https://mejlis.gov.tm/single-law/308?lang=ru): 239,263 bytes, `d425c92ee61aeb5c3b0831d599141cfbedf8bfef42e08f34ec147283beeaf0cc`.
