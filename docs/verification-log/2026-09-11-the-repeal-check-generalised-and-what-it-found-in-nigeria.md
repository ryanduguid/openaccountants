# The repeal check, generalised — and what it found in Nigeria

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Cape Verde raised the question the corpus was not asking: *is the instrument this
figure is attributed to still in force?* Asking it across the corpus produced 265
distinct citations of pre-2015 instruments, most of them perfectly current —
Ireland's TCA 1997, Singapore's ITA 1947, Australia's Medicare Levy Act 1986. Age
is not the signal. The signal is a **known wholesale replacement**, and two large
packs had one: India's Income-tax Act, 2025 (in force from 1 April 2026) and
Nigeria's Nigeria Tax Act 2025 (in force from 1 January 2026).

Both packs already knew. That turned out to be the problem.

## One-way supersession notices

`ng-personal-income-tax.md` states that `ng-income-tax.md` should be *"treated as
deprecated for tax-rule purposes"* and loaded only for its bank-narration patterns.
`ng-vat.md` v2.0 states that it is a *"consolidated rewrite merging
ng-vat-return.md … and nigeria-vat.md"*, refreshed for NTA 2025. **In all three
cases the notice appears only in the file doing the superseding.** The superseded
files carried no sign of it, and two of them still opened with *"ALWAYS read this
skill before touching any Nigerian income tax work"* and the equivalent for VAT.

Selection is by description. A model matching "Nigeria income tax", "PITA" or
"self-assessment Nigeria" reaches the deprecated file as readily as the canonical
one, and nothing inside it says to stop. `ng-income-tax.md` was still teaching
PITA's 7%–24% scale, the Consolidated Relief Allowance and the 1% minimum tax —
all three superseded from 1 January 2026 by the Fourth Schedule to the Nigeria Tax
Act 2025 (0% to ₦800,000, then 15/18/21/23/25%), which abolishes the minimum tax
and replaces the CRA.

**A deprecation notice belongs in the deprecated file.** Written anywhere else it
is a note to maintainers, not a guard. The corpus-wide scan for this pattern found
fifteen files naming another guide in a supersession-flavoured sentence; twelve
were ordinary cross-references in READMEs and "see also" lines, and the three that
mattered were all in Nigeria.

## Two Acts, one gazette, one day, and the same words meaning different things

Chasing the Nigerian VAT threshold produced a sharper finding than a stale figure.
`ng-vat.md`'s reviewed block carried the registration threshold **twice, at two
figures** — NGN 25,000,000 (Finance Act 2019) and NGN 100m (NTA 2025) — while its
body applied only the first, including in a refusal rule instructing the agent to
stop work below ₦25 million. Reading both 2025 Acts from Official Gazette No. 117
of 26 June 2025 showed that neither citation locates the rule correctly:

- **The Nigeria Tax Act 2025 has no turnover threshold for VAT at all.** Section
  147 charges 7.5% on the value of all taxable supplies, and the exempt list in
  section 185 has no turnover limb.
- **The relief is in the Nigeria Tax Administration Act 2025, section 22.** The
  monthly-return obligation in s.22(1) *"shall not apply to a small business"*, and
  s.22(5) describes that exemption as covering *"registration, charging of tax on
  its taxable supplies and filing of returns"*.
- **"Small Business" is defined in the Administration Act** as gross turnover of
  ₦100,000,000 or less with total fixed assets not more than ₦250,000,000 —
  **"provided that any business providing professional services shall not be
  classified as a small business"**.
- **The Tax Act's own "small company"** — the same two limbs, and the gateway to
  the 0% corporate rate in s.56 — **carries no such proviso.**

So the same two numbers mean different things depending on which tax is in issue,
and the proviso that decides it appears in one Act and not the other. Every Nigeria
guide in this corpus is written for *"self-employed individuals, sole traders,
partnerships or small companies"* — a population largely inside the
professional-services proviso, and therefore outside the VAT exemption at any
turnover. **The single most important qualifier for the pack's own audience was in
none of its files.**

Three habits follow:

- **Find the rule, not the number.** A threshold recorded without its operative
  provision cannot be checked when the law moves, and cannot be applied to a
  taxpayer the provision excludes.
- **A charging Act and an administration Act are two documents.** When a
  jurisdiction splits them, an obligation cited to the charging Act should be
  treated as unverified until it is found there.
- **A definition shared by two statutes is not one definition.** Where the same
  term is defined twice, read both before carrying a conclusion from one tax to
  another.

## A reviewed fact can carry a citation the Act does not support

`ng-vat-return.md` is tier 1, reviewed and signed. Its generated block records *"VAT
registration exemption threshold (annual turnover) — NGN 25,000,000 or less
(NIGERIAN TAX ACT 2025)"*. The figure is real — it is the Finance Act 2019 test —
but **it is not in the Act cited**, and the file's standing instruction *"NEVER
require VAT registration for businesses below NGN 25,000,000"* is wrong for any
2026 period and wrong at every turnover for a professional-services business.

The reviewer's name attaches to the figures they checked, which were the figures of
the year they checked them. **A signature is not a subscription**: it does not
follow the law forward, and it does not make a re-attributed citation true. Where a
generated block is wrong about where a rule lives, the durable fix is upstream in
the facts; what a guide can do meanwhile is say so, in the file, above the block.
