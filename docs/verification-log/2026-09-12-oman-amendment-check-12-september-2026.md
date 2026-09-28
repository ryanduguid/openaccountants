# Oman amendment check, 12 September 2026

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

This continuation started from 76c2f6c4, eight commits after the pasted handoff's
ec26165c. The intervening Oman corrections relied on an older English Law and
MD 30/2012. Reading their Arabic amendments reverses several of those findings.
The affected guides remain tier 2 and pending review.

## Four months was correct

The Tax Authority publishes the Arabic RD 118/2020 on the Arabic version of its
[Income Tax Law page](https://tms.taxoman.gov.om/portal/ar/income-tax-law-regulations).
The downloaded decree has ten pages, 295,139 bytes and SHA-256
`e5d2997217dec95c868555af344820f8e145e7e6a699afc0193b36422d1ddfcc`.
The text layer is damaged. Individual pages 1, 5 and 6 were read at 200 dpi.

The attached amendments' article II replaces Income Tax Law article 140 with a
four-month deadline. The page gives four as both `(٤)` and `أربعة`. Measure from
the earlier of the tax-year end and the relevant accounting-period end, using
the final accounting period where there is more than one. Decree article IV
applies that article to tax years starting on or after 1 January 2020.

The same amendment replaces articles 138 and 139. Article 138 now covers an
electronic amended return within 30 days after discovering an error or omission;
article 139 concerns the penalty treatment of an unintentional error corrected
under article 138. Article I replaces the provisional/final terminology with
an income return. Amended article 150 makes tax payable at the return deadline.
The branch's statements that four months was unsupported and that ordinary
taxpayers still need a separate provisional return were incorrect.

The small-enterprise deadline remains three months under article 159 bis 18,
with payment under article 159 bis 22. The Arabic consolidated Law, PDF pp. 66–67,
and the [Authority's FAQ, question 2](https://tms.taxoman.gov.om/portal/income-tax-faqs)
confirm this. The two guides now distinguish the ordinary and enterprise cases.

## The filing exemption had been repealed

The English MD 30/2012 PDF does contain the OMR 20,000 capital, OMR 100,000 income
and eight-employee filing exemption at articles 134–136. That reading of the old
text was accurate. It was an error to add the exemption as a current rule.

The Arabic MD 14/2019, attached amendments article IV(3), repeals sections two
and three of chapter one, part seven: the exemption from filing returns and
the exemption from attaching accounts. PDF p. 22 was read individually at
200 dpi and compared with the English Regulation's section headings and
articles on pp. 39–40. The Arabic amendment has 29 pages, 576,034 bytes and
SHA-256 `e7b5aaff54145d1196ac8dfe453e38c84925367be8c77c130c112c14a7bbdb33`.

## The SME limits and tax exemption can be read directly

Arabic consolidated Law p. 62 and the current English Law p. 87 both state the
article 159 bis basic limits: OMR 50,000 registered capital, OMR 100,000 gross
income and 15 average employees, subject to the activity and entity conditions.
The previous claim that the enterprise chapter states no such figures was wrong.

Law article 159 bis 5 and Regulation article 164 allow continued application
within a 20% capital increase, 50% income increase or ten extra average employees.
These give OMR 60,000, OMR 150,000 and 25. The Authority's FAQ gives the larger
figures as a general eligibility test, while the Regulation is worded as
continuation. The guide records that distinction and leaves initial eligibility
between the basic and enlarged limits for confirmation.

The Arabic Law clearly labels the 3% provision as article 159 bis 15. Its
exclusion is a tax exemption. Regulation articles 159–163 specify the alternative
conditions: a full-time managing owner or partner without another employment,
or at least two permanent Omani employees serving for six months in the tax year.
They also govern the choice between several owner-managed enterprises and the
evidence required with the return. Relevant Arabic Law pp. 62, 65–66 and
Regulation pp. 19–22 were read at 200 dpi. The industrial exemption also requires
article 118's five-year period and article 119's exemption decision; it is not a
permanent consequence of industrial status.

## A newer English consolidation has a separate omission

The English Law retrieved on 12 September 2026 has 120 PDF pages and expressly
identifies RD 118/2020 on p. 3. It is not the 102-page version described in the
handoff. Its hash is
`f7442e8364116a309744a2274b543e910c86b03bcb3e405f17df021f1726c3e0`.
It includes the SME limits and the amended enterprise-return provision.

However, physical PDF pages 77–78, also numbered 76–77 in print, jump from
article 133 to article 143. Text searches did not find article 140; inspection
at 200 dpi confirmed that the return provisions are missing from those pages,
rather than hidden in a picture. The Arabic decree supplies the operative text.
A document labelled as amended still needs a completeness check.

## Scope and checks

Updated `om-corporate-income-tax.md` and `om-tax-overview.md`, including their
descriptions and dates. Searched editable source guides for the rejected
four-month wording, provisional-return assertions and old exemption thresholds.
The historical passages above are retained with supersession notices.
No generated files were edited. The separate Top-up Tax Executive Regulation
remains unread. Only the relevant MD 14/2019 provisions were examined; the
remaining provisions and annexes are not represented as fully reviewed.
