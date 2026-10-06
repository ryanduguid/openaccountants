# US treaties: Mexico rules

The Mexico section put banks and publicly traded bonds together at 10%,
described technical services as a 0% article 14 category and put 183 days
in the generic services PE column. It omitted the amended parent/pension
dividend relief, fund restrictions and several interest exceptions. The
existing ordinary dividend rows already named direct corporate investment;
their omission was the additional categories and conditions.

I started from merged main `0152342cd832340b5fc4611276c117e866ed9417`,
including the separately delivered Switzerland correction. This change
advances the guide from version 1.9 to 2.0, retains tax year 2025, tier 2
and `pending_review`, and replaces only the Mexico body and PE row/note,
with updated review scope and the normal generated copies. No Mexico
summary row is added.

I checked selected provisions of the [1992 convention][convention] and
[original Treasury explanation][explanation], the [typed 2002 draft][draft],
the [signed Senate Protocol][signed] and [2003 explanation][protocol-explanation].
The base convention PDF also contains the 1994 Additional Protocol, which
changes article 27 information exchange. I read the [2023 USMCA
arrangement][usmca] and both [August][august] and [December][december]
2005 transparent-entity agreements. December expressly supersedes August.
The [IRS treaty-document index][index] and [arrangement registry][registry]
were checked again on 6 October 2026. They still list the selected income-tax
documents and arrangements; this is not a complete instrument-inventory
certificate.

| Retained official PDF | SHA-256 |
| --- | --- |
| 1992 convention, including original and 1994 protocols | `8c2249a689da8067c9d2bc1ababae6f6e5c918a045ffdaa2c680afb730103114` |
| Original explanation | `b3e093bfe579bdb0967dbaaade51aea5a8f30f6b8ea66338037a1bc34709bc82` |
| Typed Treasury 2002 draft | `262056a89419985d5f550e774fcd8b7d8b00c9a5ba8118fc3adf0f560772bc97` |
| Protocol explanation | `b34da3f7407c9250ae3a15f09eff3a116981ada343bfc1637916cd80b052cb9c` |
| Signed Senate Treaty Document 108-3 | `5dadc86a0829815ed342b6c9d0bcd285fe01dfe439a786443313b33e1cc6f24e` |
| USMCA arrangement | `c56be7db0cd51cde6d88eed3366e5c6744d385d3e0ad60a15a306d38098173d7` |
| August 2005 agreement | `bc505c7a6291201ddb05c3e65539b177fb6280fb5302d010556c97c089acd928` |
| December 2005 agreement | `db560608bf602b02e97c425b4ca4d74fa457e3030906d64a4539753695ba9816` |

Seven PDFs extracted natively with PDF Inspector. The Senate document's
letters extracted natively, while ten operative pages needed offline OCR.
The first managed Linux OCR job stopped on its thermal guard after six
pages; a bounded one-CPU resume completed the other four with the guard
preserved. I then read all ten rendered English pages, physical pages 7
to 16, to compare the selected text and resolve the OCR defects in the
signature date and effective-article numbering. PDF Inspector does not
expose standalone page rendering, so the installed Poppler renderer was
used for images only. It reported missing Symbol/ArialUnicode display fonts;
the scanned operative images were legible. This is not an exact OCR
transcription or forensic signature certificate. The authentic Spanish
text was not compared.

The typed Treasury document says it was unsigned and presented on
25 November 2002. The signed image, Senate letters and [Treasury
announcement][force] establish signature on 26 November 2002. Treasury
records force on 3 July 2003, dividend amendments from 1 September 2003
and other amended provisions for periods from 1 January 2004. Signed
article VI expressly distinguishes article II dividends from articles I,
III, IV and V for the other effective-period rule. The USMCA PDF's date
lines are blank, including on visual inspection; 21 June 2023 is the IRS
registry's date, not a verified signature date on that PDF.

| Correction or boundary | Primary evidence |
| --- | --- |
| Ordinary 5% direct-company/10% ceilings; conditional parent and pension relief | Amended art 10(2)-(3); Protocol art II; 2003 explanation |
| Principal parent ownership wording remains unresolved | Signed art 10(3)(a) and distinct historical clause (i); explanation describes principal ownership as direct |
| RIC/REIT exclusions, REIT alternatives and dividend attribution | Amended art 10(4)-(5) |
| Bank/insurance loan and traded-security 4.9%, bank-paid/original-seller 10%, other interest 15% | Art 11(2); Protocol points 10(b), 15(b); original explanation |
| Loan-granted wording versus bank/insurance beneficial owner, including an assignee | Art 11(2)(a)(i); original explanation of art 11, with current authoritative interpretation unverified |
| Specified government, pension and public-lender interest; PE preservation versus REMIC exclusion | Art 11(4), (6); Protocol point 10(a); original explanation |
| Defined interest, debt/equity character, back-to-back, source and excess limits | Art 11(2), (5), (7)-(8); Protocol point 9 |
| Defined copyright/rights/know-how/equipment and contingent gains; royalty attribution/source/excess, with a source-wording gap | Art 12; Protocol point 11; original explanation of art 12; arts 6 and 8 boundaries |
| Enterprise profits versus an individual's fixed-base/presence rule; directional company extension | Arts 7 and 14; Protocol point 14; original explanation |
| More-than-six-month project/supervision threshold and separate PE grounds | Art 5(1)-(8) |
| Residence, saving clause, category-specific entitlement and USMCA references | Art 4, Protocol point 2(b), amended art 1, art 17 and 2023 arrangement |
| Transparent derivation and separate charitable exemption | December 2005 agreement; art 22(1) and original explanation |
| Branch-profit relief does not exempt excess-interest tax | Art 11A(2); amended art 11A(3), Protocol art III |
| Better conditions require consultation and an additional protocol | Amended Protocol point 8, not automatic importing of another treaty's rate |

I checked these numerical and classification boundaries directly against
the cited provisions. They are conditional rule comparisons, not claimant
calculations or withholding instructions.

Article 12(6)(a) requires both liability incurred in connection with the PE
or fixed base and the royalty borne by it. Subparagraph (b) refers only to
(a) not deeming source in either state, while Treasury's original explanation
describes place of use as residual after both payer residence and the PE/fixed
base rule. I preserve that wording difference as unresolved; place of use alone
does not settle treaty source for a resident payer in this draft.

| Boundary | Result under the cited provision |
| --- | --- |
| Direct corporate voting holding of 9.99% versus 10% | Only 10% meets art 10(2)(a)'s numerical element; recipient, entitlement and fund conditions remain |
| Parent owns 80% for twelve months ending on payment, but not declaration | Payment date does not replace art 10(3)(a)'s declaration date; ownership wording and additional routes remain |
| Pre-1 October 1998 indirect holding alone | Does not replace the principal current 80%/twelve-month test; indirect/transparent treatment under that principal test remains unresolved |
| RIC dividend received by an ordinary corporate parent | The 5% and parent exemption provisions are excluded; pension treatment has separate conditions |
| REIT pension/individual holding of 10% versus more than 10% | Only 10% satisfies that alternative's no-more-than-10% element; other paragraph 4(c) alternatives and requirements remain |
| Publicly traded REIT class and ownership of 5% versus more than 5% of any class | Only 5% satisfies that alternative's ownership element; public trading and other requirements remain |
| Pension LOB beneficiaries/members/participants exactly half versus more than half | Only more than half satisfies art 17(1)(e)'s numerical element, if there are any; no claimant is certified |
| Regularly and substantially traded bond versus merely bank-paid interest | The former is art 11(2)(a)(ii)'s 4.9% category; the latter is paragraph 2(b)(i)'s conditional 10% category |
| Bank originally granted a loan, but another person owns its interest | Origination does not establish relief under Treasury's beneficial-owner interpretation; the operative wording gap remains |
| Qualifying paragraph 4 interest attributable to a PE | Art 11(6) does not displace paragraph 4; REMIC excess inclusion separately excludes paragraphs 2-4 |
| Original seller transfers beneficial ownership of credit interest | Protocol point 10(b) requires classification by the transferee; it does not retain seller status automatically |
| Project or connected supervisory activity lasts exactly six months versus longer | Only the latter satisfies art 5(3); other PE grounds remain separate |
| Individual is present exactly 183 versus more than 183 aggregate days in twelve months | Only more than 183 meets the presence limb; the regularly used fixed-base limb and US-income limits are separate |
| US profits from same/similar goods sales outside the PE | Art 7(1)(b) can apply unless non-treaty-benefit reasons are demonstrated; the rule is not confined to direct PE attribution |
| Transparent entity income treated as a resident's income | Derivation still does not establish beneficial ownership, art 17 entitlement or dividend share ownership |
| US-resident royalty payer, use in Mexico and no relevant PE/fixed base | Treasury's explanation uses US payer residence; operative art 12(6)(b) refers only to subparagraph (a), so the wording difference remains unresolved |
| Third-state royalty payer, liability connected with a US PE and royalty borne by it, use in Mexico | Art 12(6)(a) assigns US source; both connection and bearing elements are required |
| Third-state royalty payer, US PE merely bears the amount without the required liability connection, use in Mexico | The paragraph (a) test fails; operative paragraph (b)'s place-of-use rule supplies Mexican source under these stated facts |
| Third-state royalty payer, no PE/fixed base in either state, use in the US | The residual place-of-use rule supplies US source under the stated facts |
| Amended art 11A(3) route satisfied | The exemption reaches paragraph 2(a) dividend-equivalent tax only; paragraph 2(b) excess interest remains separate |

Parent ownership, loan-assignee interpretation and the payer-residence/place-of-use
royalty-source wording remain unresolved.
Historical explanation statements about domestic law, foreign-tax-credit
classification, exchange jurisdictions and filing mechanics are not treated
as current 2025 law. Current domestic taxability/rates, source and branch
calculations, withholding/forms/refunds, institutional successors, claimant
facts, mixed-payment classification, complete later-instrument coverage,
Spanish comparison, reciprocal Mexican-source use, qualified professional
sign-off, taxpayer end-to-end use and whole-corpus financial/network
accuracy remain unverified. Repository and delivery checks belong in the
accompanying PR and do not establish financial accuracy.

[convention]: https://www.irs.gov/pub/irs-trty/mexico.pdf
[explanation]: https://www.irs.gov/pub/irs-trty/mexicotech.pdf
[draft]: https://home.treasury.gov/system/files/131/Treaty-Mexico-Pr2-10-26-2002.pdf
[signed]: https://www.congress.gov/108/cdoc/tdoc3/CDOC-108tdoc3.pdf
[protocol-explanation]: https://home.treasury.gov/system/files/131/Treaty-Mexico-Pr2-TE-3-5-2003.pdf
[usmca]: https://www.irs.gov/pub/fatca/mexico-competent-authority-arrangement-nafta.pdf
[august]: https://www.irs.gov/pub/newsroom/final_map_on_llc_8-26-2005_signed.pdf
[december]: https://www.irs.gov/pub/irs-lbi/restatment_mex_llc_map_12_22_05_final.pdf
[index]: https://www.irs.gov/businesses/international-businesses/mexico-tax-treaty-documents
[registry]: https://www.irs.gov/individuals/international-taxpayers/competent-authority-arrangements
[force]: https://home.treasury.gov/news/press-releases/js538
