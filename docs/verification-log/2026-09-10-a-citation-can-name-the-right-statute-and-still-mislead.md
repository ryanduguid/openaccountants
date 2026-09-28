# A citation can name the right statute and still mislead

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`scripts/list-statute-links.py` looks at markdown links whose **clickable text**
names an instrument. The corpus writes `[Instrument name](where I read about
it)`, which is honest as far as it goes — 944 links do it — but it means the
anchor text describes the law and the destination is something else entirely.

Most of the time that is harmless: a reader who clicks `[Income Tax Act]` and
lands on PwC can see immediately what they are looking at. The checker leaves
those alone. What it reports is the sharp end — links where the destination was
neither a tax authority nor a recognised tax publisher. `[Code Général des
Impôts (Bénin) — IRPP barème]` went to an HR platform's country page. `[OHADA
Uniform Act on Commercial Companies]` went to a corporate-services firm.
`[Civil Code of Curaçao, Book 2]` went to a law firm's marketing site.

The figures beside them may be perfectly correct. The citation is still telling
the reader something untrue about where it came from, and — like Portugal's
wrong Portaria — it survives every check that compares numbers, because there
is no number in it to compare.

The fix is presentational and safe: move the instrument name out of the anchor
so the link says where it goes. `[Code Général des Impôts (Bénin)](rivermate)`
becomes `Code Général des Impôts (Bénin) (as described at [rivermate.com](…))`.
Nothing about the tax changes; the reader stops being told they are clicking
through to a statute. Run `python3 scripts/list-statute-links.py` for the
current count; it was 305 across 53 jurisdictions when the queue opened.

**Two blind spots in that checker, found by testing it rather than reading it.**
Both were false negatives, which is the kind that survives — a checker that
under-reports looks clean.

The first was a one-word slip: on a line with several links, `return` where
`continue` belonged, so scanning stopped at the first link that did not name an
instrument. Thirty-nine lines in the corpus start with a plain link, and every
statute link after one was invisible. It happened to change no count on today's
corpus, which is exactly why it would have lasted.

The second was worse, because it was a gap in what the checker knew rather than
a slip in how it looped. The instrument vocabulary was `Act|Code|Law|Ordinance|
Decree|Loi|Código|Ley|…` — the words a common-law and francophone reader
reaches for. Ethiopia and Eritrea legislate by **Proclamation** and by nothing
else. Every statutory citation in both guides was therefore out of scope, and
Eritrea alone accounted for 18 of them, all pointing at commercial tax-data
sites. A vocabulary drawn from the legal systems you already know will silently
exempt the ones you do not. Adding `Proclamation`, `Regulation`, `Lei`, `Legge`
and `Resolution` found 27 more. `Order`, `Rules`, `Bill`, `Statute`,
`Constitution`, `Notification` and `Circular` were measured too and left out —
each is either ambiguous in English or absent from the corpus.

**And one false positive, which is the kind that gets caught.** The British
Virgin Islands' two `[National Health Insurance Regulations]` links go to
`vinhi.vg`, which the checker called a marketing site. It is the scheme itself:
its bulletin of 12 September 2024 sets the US$102,000 ceiling and the 3.75% +
3.75% split the guide quotes, over its own contact details. Same class as
NCCPL, FRCS and BURS — the body that computes and collects the charge,
publishing the table it collects under. BVI's two best citations were about to
be filed as defects. `vinhi.vg` is now a recognised authority in
`list-source-mix.py`, which also lifts BVI out of the zero-authority list.

**So the whole queue was audited destination by destination before a single
link was converted, and 45 of the 305 were wrong — 15%.** Nine were bodies
that compute and collect the charge the guide quotes: Burundi's `obr.bi`,
Curaçao's `svbcur.org`, the national insurance boards of Trinidad, the BVI and
the Bahamas, South Sudan's social insurance fund (on free hosting, which is
why it looked like a brochure), Liechtenstein's `llv.li`, Finland's `prh.fi`.
Two more were recognised publishers under another name — Legal 500 and
Bloomberg Tax.

Tonga is the one worth spelling out. Its links point at PDFs on a trade
portal, which reads like a brochure site. The PDF is the **Consumption Tax Act
CAP. 26.02, 2016 Revised Edition**, 31 pages, and s.5(3)(a) says "The rate of
Consumption Tax shall be 15 per cent" — the exact figure the guide cites. The
link was already doing what its anchor promised, and the checker was about to
recommend rewriting it.

**A heuristic was tried here and thrown away, which is worth recording.** The
idea was to exempt a link when the URL path echoes words from the anchor, on
the theory that the destination is then the instrument itself. It exempted
nine links and eight were wrong: a blog post *about* Ethiopia's amendment
Proclamation, a country page that happened to contain "tome" and "principe".
And it missed Tonga — the very case that prompted it — because the anchor was
short enough that only one word overlapped. String overlap between a label and
a URL does not test whether a document is a statute. It is the same mistake as
testing a file-level claim with a line-level pattern: **scope the test to the
claim.** Checking what the domain actually is does test it, and costs one
fetch.
