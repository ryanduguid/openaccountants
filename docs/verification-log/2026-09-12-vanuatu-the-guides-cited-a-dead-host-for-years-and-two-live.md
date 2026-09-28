# Vanuatu — the guides cited a dead host for years, and two live authorities were never tried

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Vanuatu came off the same hostname sweep. The register had `customsinlandrevenue.gov.vu`
under "no DNS at all" — **correctly**, that name really does not resolve — but the corpus
**cites it 17 times**, and nobody had asked what else Vanuatu publishes. Two authorities
answer:

- **`www.vfsc.vu`** — the Financial Services Commission, with a `/legislation/` page
  serving **183 PDFs**, including the ***International Companies Act* [CAP. 222],
  Consolidated Edition 2026** (75 pages, clean text).
- **`www.vnpf.com.vu`** — the National Provident Fund, serving the ***VNPF Act* [CAP. 189],
  Consolidated Edition 2026** (29 pages, clean text).

Both are **2026 consolidations**. Unlike Djibouti or Mauritania, nothing here is frozen.

**The corporate guide's key row was sourced to a travel-and-relocation website**, and
reading section 118 changed the answer in a way no summary would carry:

- **The two sentences of s. 118(1) do not carry the same condition.** The business licence
  fee exemption applies *"unless carrying on business in Vanuatu"*; the income, profits,
  capital gains and distributions exemption in the very next sentence is stated **without**
  that qualifier, and it reaches the **shareholder** as well as the company.
- **⚠ The Act gives two contradictory durations for the same exemptions.** Section 118(4):
  *"twenty years from the date of its registration"*. Section 118(5): *"remains in force
  until 31 December 2099"*. Both are in the consolidated edition. A company registered in
  2002 is out of time under (4) and has seventy-three years left under (5). The natural
  reading is that (5) was meant to replace (4) and the consolidator left both — **that
  inference is written down as an inference and not asserted**. The guide previously
  implied there was nothing here to resolve.
- Also added: the estate/inheritance/succession/gift exemption, the stamp-duty exemption
  with its **real-property carve-out**, and the exchange-control exemption with its two
  express carve-backs for transfers touching Companies Act companies (ss. 118(3A), (6)).
- Two drafting defects recorded rather than tidied: **two subsections both numbered (2)**,
  and a **stray closing quotation mark** at the end of (5).

**The payroll guide's figures were right and its two open questions are now answered.**
The 12% / 6% / 6% split it carried from an employer page and a newspaper is confirmed by
**ss. 25(1) and 25(1A)** of the Act. What the statute added:

- **s. 25(2): a VT 3,000 monthly floor, tested per employer.** The guide asked to "confirm
  any minimum/maximum earnings limits". The floor is per employer, so someone with two
  small jobs can fall below it twice; **no maximum appears in s. 25**.
- **s. 26(1): by the end of the following month.** The guide asked to "confirm exact day of
  month" — the Act fixes a month-end, not a day.
- **s. 26(2): a 5% surcharge for each month *or part of a month*** — a day late costs a
  full 5%.
- **s. 30(2): contributions split 50% retirement / 25% investment / 25% medi-save**,
  accumulating only from 1 January 2008.
- **s. 46**: Fund income, interest, withdrawals and *every instrument executed by the Fund*
  are exempt from all taxes, levies or charges **by statute** — not merely by consequence
  of Vanuatu having no income tax.

**And one live dead link.** The employer-registration row cites
`employmentvanuatu.gov.vu`, which resolves to **192.0.2.1** — TEST-NET-1, the RFC 5737
documentation range, never routed. That is not a site that went down; it is an address
that was never a site. It is now flagged in the row itself. The lesson generalises past
Vanuatu: **a citation can be well-formed, plausible, on a `.gov` domain, and point at
nothing at all**, and no check in this repo looks at whether a cited host resolves.
