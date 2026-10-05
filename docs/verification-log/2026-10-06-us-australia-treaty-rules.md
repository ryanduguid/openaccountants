# US treaties: Australia rules

The Australia section gave every interest payment a 10% rate, every royalty
category 5%, and technical services a blanket art 7 zero rate. It omitted
parent-company relief and the RIC, REIT and listed Australian property trust
(LAPT) rules. This correction starts from `e5024e3`, advances
`us-major-partners` to version 1.5 and covers US-source income paid to
Australian residents for tax year 2025. It remains tier 2 and pending review.

I compared the [1982 Convention](https://www.irs.gov/pub/irs-trty/aus.pdf),
[original explanation](https://www.irs.gov/pub/irs-trty/austtech.pdf),
[2001 Protocol](https://home.treasury.gov/system/files/131/Treaty-Australia-Protocol-9-27-2001.pdf)
and [2003 Protocol explanation](https://home.treasury.gov/system/files/131/Treaty-Australia-Protocol-TE-3-5-2003.pdf).
The documents were retrieved from their official endpoints on 5 October 2026,
and the focused comparison finished on 6 October. The
[IRS index](https://www.irs.gov/businesses/international-businesses/australia-tax-treaty-documents)
still linked those four documents when read again. All four PDFs extracted
natively with pdf-inspector; no OCR was required.

| Document | Pages | SHA-256 |
| --- | --- | --- |
| Convention | 27 | `8ba3776cb1332ff4231a174c1b555782c812d0afff3a75ca6127246ba940902e` |
| Original explanation | 29 | `a971d8fb1f54974111fc68ba0d7ccbe3312437695f977308ef20c5e21eb4a332` |
| Protocol | 19 | `c2cc1c83ae3aa787b4b9f561fa3e96c3d3113ec40cd552491f7c9193d5bebd3d` |
| Protocol explanation | 41 | `d36ab1fb8f04324ea6d2f8422f93023545af9b5da9a0e208e108c9234c56446b` |

Protocol arts 6, 7 and 10 replace Convention arts 10, 11 and 16. Protocol
art 8 changes the royalty ceiling and replaces art 12(4)(a), retaining
paragraphs 4(b) and (c). Original arts 5, 14 and 27(2) remain relevant;
Protocol art 4 inserts art 7(9) on transparent-entity PE attribution.

| Earlier statement | Correction and primary pinpoint |
| --- | --- |
| No parent dividend category | Art 10(3) requires at least 80% voting power for twelve months ending on declaration, plus art 16(2)(c) qualification or an actual art 16(5) dividend-benefit grant. |
| Substantial dividends use 5% without fund limits | Art 10(2)(a) requires a company beneficially entitled and directly holding at least 10% voting power; art 10(4) separately restricts RIC/REIT and LAPT dividends. |
| Interest always uses 10% | Art 11(3) exempts specified governmental recipients and qualifying independent financial institutions; paragraphs 4, 6, 8 and 9 contain exceptions. Profits-linked interest in paragraph 9(a) has a 15% ceiling. |
| Royalties always use 5% | Classify under amended art 12(4); equipment rentals were removed, while know-how, ancillary assistance and contingent alienation remain. PE/fixed-base and excess-payment rules apply. |
| Technical services always use 0% | Enterprise profits can use art 7; individual independent services retain art 14 and its art 27(2) subject-to-tax limit; some knowledge/assistance payments use art 12. |
| No Australia PE row | Art 5 has distinct construction, seabed, equipment and supervision durations, alongside fixed-place, agency and goods-processing rules. |

The operative art 10(3) does not expressly require direct ownership, while
the US explanation of Protocol art 6 paragraph 3 describes it as direct.
The guide states both and treats indirect parent ownership as unverified.
The explanation's proportionate transparent-entity treatment for the
expressly direct 10% test is conditional and depends on the governing
agreement and source-state characterisation. Neither explanation was
silently substituted for the operative wording.

The LAPT look-through applies to corresponding portions when the responsible
entity knows or has reason to know of a unitholder with at least 5% of
beneficial interests. Protocol art 13(3) preserves old art 10 for qualifying
shares held on 26 March 2001, binding contracts entered into by that date,
and reinvestments of their ordinary or capital dividends. Those shares do
not automatically use the replacement article's look-through rule.

I compared these boundaries manually with the primary provisions, assuming
the other stated conditions are met. They are source comparisons, not a
taxpayer calculation or a financial parser test:

| Boundary | Source comparison |
| --- | --- |
| Company holding exactly 10% directly | Meets art 10(2)(a)'s ownership bound; below 10% does not. |
| Parent holding 80% for twelve months | Meets the numerical/duration bounds; ending on payment rather than declaration, or only general active-business eligibility, does not establish art 10(3) relief. Indirect ownership remains unverified. |
| REIT holder and diversification exactly at the stated bounds | At most 10% ownership with no property interest exceeding 10% gross value satisfies art 10(4)(c)(iii)'s bounds; exceeding either does not. Other alternatives must be checked separately. |
| Known LAPT unitholder at exactly 5% | Triggers art 10(4)(d)'s proportionate look-through; it does not deny every unitholder relief. The grandfather is checked first. |
| Independent qualifying financial institution with a back-to-back arrangement | Art 11(4)(a) restores the 10% ceiling; government and profits-linked categories retain their separate rules. |
| Individual present for exactly 183 days | Does not pass art 14's more-than-183-day limb. A regularly available fixed base or art 27(2) can still affect the result. |
| Construction exactly nine months | Does not pass art 5(2)(h)'s duration limb; more than nine does. Other PE grounds remain relevant. |
| Specified seabed activity exactly six months in 24 | Passes art 5(2)(i)'s duration bound. |
| Substantial equipment exactly twelve months | Does not pass art 5(4)(b)'s duration limb; more than twelve does, subject to the hire-purchase exclusion. |
| Project supervision exactly nine months in 24 | Does not pass art 5(4)(c)'s duration limb; more than nine does. |

[US Treasury's force statement](https://home.treasury.gov/news/press-releases/20035121658221021)
records exchange and entry on 12 May 2003. The live
[Australian Treasury table](https://treasury.gov.au/tax-treaties/income-tax-treaties)
records 13 May 2003. I have not certified that discrepancy resolved or
independently verified the Gazette mentioned in the plan review. Either
May date gives 1 July 2003 under Protocol art 13(2)'s withholding formula;
the difference does not change that start date.

The explanations contain apparent reference inconsistencies: the 2003
residence discussion names art 23 for LOB, although the Protocol replaces
art 16; its art 16(5) discussion also refers to paragraph 6. Its
publicly traded subsidiary discussion describes an every-class test,
where operative art 16(2)(c)(ii) uses aggregate vote and value. The guide
uses the operative routes and leaves claimant application to review.

The review covers the Australia section and its new PE row. The other
thirteen partner bodies and the exact disclaimer/CTA are protected.
The generators and existing checks verify schema, synchronisation,
derived output and accepted baseline findings; they do not certify
treaty interpretation or financial accuracy.

Named professional sign-off, claimant facts, current domestic tax and
withholding/refund procedures, reciprocal Australian treatment, a
bilateral or Australian resolution of the indirect-parent issue, complete
later-instrument and authentic-text comparison, taxpayer end-to-end
use and whole-corpus financial/network citation accuracy remain unverified.
Aikido code scanning is not applicable to this content-only correction.
