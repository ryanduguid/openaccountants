# Kuwait — a contradiction about *treatment*, which no rate check can see

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The supranational idea that paid for itself on OHADA — find an instrument many
guides cite, and read them against each other — was pointed at the other large
régime in the corpus. The **GCC** is cited in 32 files across ten directories, more
than OHADA. It did not produce a misread instrument. It produced something the
corpus's own checks are structurally blind to.

Three Kuwait guides take two positions on the same rule:

- `kw-corporate-income-tax.md`: *"a flat 15% applies only to foreign (non-GCC)
  corporate bodies"*; *"companies wholly owned by Kuwaiti or GCC nationals are
  exempt from CIT"*; *"GCC companies are taxed only to the extent of non-GCC foreign
  ownership"*. **Cited.**
- `kw-tax-overview.md`: *"locally owned **and GCC-owned** companies instead bear a
  set of profit-based contributions"*. **Cited, and agrees.**
- `kuwait-tax.md`: *"**GCC nationals treated as foreign**"*; a worked example taxing
  a Saudi-owned business at 15%; and the prohibition *"**NEVER treat GCC nationals
  as Kuwaiti for CIT**"*. **Uncited, three times over — and the only one of the
  three that issues an imperative.**

A Saudi-owned company in Kuwait is either exempt or charged 15% depending on which
file a model loads, and the file that speaks most forcefully is the one with no
source behind it.

**A rate-level contradiction checker cannot see this.** Every file says 15%. They
agree on the number and disagree on *who it reaches*, and the corpus's earlier
self-contradiction pass — which compared rates — passed over it. The generalisable
form: **check what a rule applies to, not only what it is.** A guide can carry the
right figure with the wrong population attached, and OHADA's article 311 is the same
defect in the other direction — the right number attached to the wrong measure.

**Two against one, and the one is unsourced**, so the outlier is corrected rather
than merely flagged. That is as far as the evidence goes: the statutory basis for
treating GCC ownership as non-foreign is **asserted by every source here and quoted
by none**, and it stays a research gap.

## The same pack knew about a second charge and one file did not

`kw-corporate-income-tax.md` — the file whose whole subject is Kuwaiti corporate
income tax — described only the 1955 decree regime. Its two siblings both carry the
**Domestic Minimum Top-up Tax**: 15% on in-scope multinational groups with
consolidated revenue of EUR 750 million or more, for financial years beginning on or
after **1 January 2025**, under Decree-Law No. 157 of 2024 and Ministerial
Resolution No. 55 of 2025. The file was labelled `tax_year: 2025`.

This is the Nigeria and India shape a third time: **the pack knows, and the file
that will be read for the subject does not say.** It is now the most frequent defect
this work has found, and it is invisible to any check that looks at one file at a
time.

The interaction is the part worth keeping. **The CIT turns on who owns the company;
a Pillar Two top-up turns on the group's consolidated revenue.** Nationality does
not enter into the second at all, so a large GCC-owned group in Kuwait can be
**outside the CIT and inside the DMTT at once** — a combination no row in that guide
allowed for, and one that neither the ownership rule nor the top-up rule reveals on
its own.

## Register additions

- **`fatwa.gov.kw`** (Fatwa and Legislation Department) and **`mof.gov.kw`**
  (Ministry of Finance) — **resolve but never serve**, returning a 39-byte empty
  document to a plain client *and* to a real browser. Same class as Gabon, Eritrea
  and Myanmar's registry. Kuwait's guides therefore rest entirely on a commercial
  tax-summary host, and say so.
- **`gcc-sg.org`** (GCC Secretariat General) — live, answers 200, and its pages
  render to **171 characters of text**. Live and effectively empty, the São Tomé
  pattern with a working front page.
- **OHADA's `biblio.ohada.org`** — live and serving, added to the authority
  classifier. **`ohada.com` is not the same body** (the UNIDA association) and its
  copies sit behind a login; a selftest now asserts it does **not** classify as an
  authority, because the two names are one character apart and the mistake would be
  invisible.
