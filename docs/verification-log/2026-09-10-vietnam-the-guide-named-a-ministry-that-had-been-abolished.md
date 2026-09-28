# Vietnam: the guide named a ministry that had been abolished

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The single-source queue put `vn-company-formation.md` near the top — 11 of its 12
citations went to one commercial host, with the underlying laws named but not
read. Vietnam is not a thin jurisdiction where nobody has checked; it is one of
the most-read pages in the corpus. That is what made it worth opening.

Three of its statements had stopped being true, and one whole regime was missing.

**The registration authority.** The guide said the Enterprise Registration
Certificate is "issued by the provincial Department of Planning and Investment".
The Ministry of Planning and Investment was merged into the Ministry of Finance
in 2025 and the provincial departments went with it. Decree 168/2025/NĐ-CP art.
20(1) puts the Business Registration Authority in the **Sở Tài chính**, the
Department of Finance. The National Business Registration Portal settles it
without needing the decree at all: its own footer reads *"Bản quyền thuộc Bộ Tài
chính"*. A reader following the old guide is looking for a building that is not
there.

**The annual business licence fee.** The guide listed the *lệ phí môn bài* at
"VND 1,000,000 to VND 3,000,000 per year based on registered charter capital" as
a live recurring cost. Resolution 198/2025/QH15 art. 10(7) is one sentence long:
*"Chấm dứt việc thu, nộp lệ phí môn bài từ ngày 01 tháng 01 năm 2026."* The
charge ended, and with it the declaration. The band description was also wrong on
its own terms — VND 1,000,000 was never a charter-capital band, it was the rate
for branches, representative offices and business locations.

**The 90-day capital rule.** Correct as far as it went, and it did not go far
enough: art. 47(2) excludes the time spent transporting or importing contributed
assets and completing ownership-transfer formalities. For a contribution in cash
the guide was right; for imported plant or real property it understated the
deadline.

**The regime that was missing.** Law No. 76/2025/QH15, in force 1 July 2025,
built a beneficial-owner register into Vietnamese company law: a definition
(art. 4(35)), a standing duty to collect and update (art. 8(5a)), a dossier item
for every company form (arts. 20–22), required fields down to ethnicity and
gender (art. 25(5)), notifiable changes (art. 31(1)(c)), anti-money-laundering
access (art. 33(1a)) and five-year retention past dissolution (art. 216(1)(h)).
The guide had no trace of any of it. Its transitional rule is the practical
point: a company registered before 1 July 2025 files the information at its
**next** registration change, so the obligation arrives silently, attached to
whatever routine filing comes first.

## What the fetching cost, and why it is worth writing down

Three of the four government hosts holding the primary texts were awkward in a
different way, and the workarounds are reusable:

- **The relay closes long transfers mid-flight.** A 626 KB `.doc` arrived in
  four truncated pieces. Resuming with `curl -C -` finished it — and *corrupted*
  it, because the server ignores `Range` and restarts from zero, so the resumed
  bytes appended a second copy. The file that ended up 650 KB against an
  expected 627 KB was the tell. A single unresumed request with a long timeout
  is the fix; a resumed file that is *larger* than expected is never complete.
- **Signed PDFs are scans.** `datafiles.chinhphu.vn` serves the official signed
  text of both the Law on Enterprises 2020 and Decree 362/2025 — as images.
  4.4 MB in, 70 characters of text out. The gazette's own DOCX would have
  answered, but its CDN host is not in the TLS bundle.
- **`vbpl.vn`, the Ministry of Justice's national legal database, returns 403 to
  everything**, root and file paths alike. So does `ssa.gov`, which matters
  beyond Vietnam: `gw-payroll-social.md` cites the SSA's *Social Security
  Programs Throughout the World* for Guinea-Bissau's contribution ceiling, and
  that citation cannot be checked from this network at all.

The consequence is recorded in the guide rather than hidden: arts. 46(1) and
47(2) were read in an English translation, not in Vietnamese, and arts. 111(1),
113(1) and 188 were not re-read at all. They stay marked, with a research gap
naming exactly which articles a reviewer still has to confirm. **Getting three
things right and saying plainly which fourth thing you could not reach beats
quietly promoting all four.**

Corpus effect, re-measured rather than carried forward: authority citations
2,765 → **2,787**, secondary 4,733 → **4,728**. `vn-company-formation.md` is off
the single-source queue; `vn-tax-overview.md` and `vn-payroll-social.md` remain
on it, both concentrated on PwC, which is a recognised publisher rather than an
unknown one.
