# Angola, Burundi and Djibouti statutory follow-up, 12 September 2026

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

This pass checks the outstanding IRT and social-contribution questions. It does
not certify later amendment coverage, the countries' complete guides or the corpus.

## Angola: Group C article 9(2), monthly scope and Group B rates

- Read the gazette reproduction of Lei n.º 28/20, PDF pages 3–4, with PyMuPDF text
  extraction and individual pages at 200 dpi. Article 9(2) is retained unchanged;
  article 10(1) expressly makes Group A calculation monthly; article 16(2) sets
  Group B/C withholding at 6.5% and article 16(3) sets 25% on the taxable base not
  subject to withholding. The earlier Group B description as progressive withholding
  up to 25% was wrong. The earlier warning that the monthly period lacked statutory
  support is withdrawn. The annex's silence was insufficient evidence of a legal gap.
- Read the original article 9(2) in Lex.AO's transcription of Lei n.º 18/14. Its
  four-times-invoicing test substitutes non-withheld annual sales of goods and
  services as the Group C base. The original gazette download returned HTTP 403;
  no retry or alternative route around that denial was used. The wording is
  transcription-backed; a scan cross-check remains open.
- Retained the already-read Lei n.º 18/24 article 35(2) suspension of efficacy and
  the 2025 article 20 Group C rules. A suspension does not establish repeal or the
  rule for 2026. Retained the enacted 2025 table rather than substituting the older
  2020 annex. The twelve figures were not re-audited in this follow-up.
- Corpus search found the unsupported Group B description and article 9(2) gap in
  ao-income-tax only. The sibling payroll guide already described monthly IRT;
  no change was needed there. Residence and employee-return statements remain
  secondary-source claims, outside this specific statutory check.

## Burundi: schedule verified, original Code read, amendments still open

- INSS publishes at inss.gov.bi. Its Calcul des cotisations page confirms ordinary
  pension contributions of 6% employer and 4% employee, with monthly contributory
  earnings capped at BIF 450,000 per employee. The 3% employer occupational-risk
  charge uses a separate BIF 80,000 earnings cap. The previous wording could be
  read as a BIF 80,000 contribution cap; the maximum charge is BIF 2,400.
- The same schedule separately gives difficult-work pension rates of 8.8% employer
  and 5.8% employee, including military and police examples. Its remuneration base
  includes allowances and bonuses, excludes expense reimbursements and has a SMIG
  floor. The affiliation page independently corroborates ordinary rates and the
  pension cap. Commercial 6%/4%, 450,000 and 3%/80,000 figures were supported.
- Read the 2020 Code scan, PDF pages 1 and 30–32 at 200 dpi after confirming that
  all 49 pages have no extractable text. Contact sheets only located the provisions.
  The title page gives Loi n°1/12 du 12 mai 2020 in handwriting. Article 134 allows
  regime-specific caps; article 135 delegates rates to ordinances and allocates
  occupational-risk contributions entirely to employers. Article 139 sets payment
  monthly or quarterly as applicable, by the following month's 15th; article 141
  sets the matching declaration cycle. Article 145 leaves the employer liable for
  an employee share omitted when remuneration was paid.
- The Code does not itself supply the schedule's numerical rates and caps. A Code
  citation attached to a secondary rate was therefore inadequate even where the
  rate was right. The health 3% and training 1% claims remain unverified, with their
  regime and legal basis explicitly open; absence from this INSS schedule does not
  prove that no such levy exists.
- Laws 1/09 of 14 March 2022 and 1/05 of 30 April 2026 remain unread. The presidency's
  2026 page returned 404; the assembly's 2022 index timed out. Refworld's PDF access
  returned 403 and was not retried. P4H independently hosts the original public
  Code scan used here. Current INSS web guidance supports its published schedule,
  but this is not a completed check of the amendments or every public-sector regime.
- The earlier claim that rates could not be sourced because inss.bi failed is
  withdrawn. A failed assumed host did not establish the institution's availability.
  The already-read 2026/2027 Finance Act findings and their tax-year caveat remain.

## Djibouti: statutory healthcare split, ceiling and payment deadline

- Read Loi n°24/AN/14/7ème L article 16, PDF page 3, individually at 170 dpi after
  text extraction: 7% healthcare is split 5% employer and 2% employee. Read the
  2015 amendment, PDF pages 2–3 at 200 dpi: Law 109 changes articles 17 and 37,
  leaving article 16 untouched. This resolves the CNSS page's contradictory
  blanket assignment of healthcare to the employer. It does not require choosing
  between two inconsistent sentences by arithmetic alone.
- Read Arrêté n°2015-605 article 1, PDF page 1 at 200 dpi. Pensions have no ceiling;
  other regimes have an FDJ 400,000 monthly earnings ceiling. The previous pass
  correctly rejected a pension ceiling but missed the other-regime ceiling.
  Its correction to 21.7% combined and 15.7% employer on all remuneration was
  itself incomplete. The guide now applies uncapped 4% pension shares separately
  from the capped 11.7% employer and 2% employee non-pension shares.
- The family rate and pension split are published by CNSS. Work injury at 1.2%
  remains an explicitly identified arithmetic inference: combined healthcare and
  injury 8.2%, less the statutory 7% healthcare. No claim is made that the webpage
  separately quotes the 1.2% rate. The published floors of FDJ 15,850 and 20,000
  coexist with the non-pension ceiling; the earlier floor-versus-ceiling framing
  concealed that possibility.
- The CNSS employer page states monthly payment within the first ten days of the
  following month and a declaration at each period end even without payment. It
  cites the 1969 regulation as amended in 1989. The guide's unverified monthly
  15th was replaced. A dated fourth-quarter 2021 payment notice does not establish
  the general current monthly deadline. The original 1989 text and employer-specific
  quarterly coverage remain unverified.
- Read all five operative articles of Law 111/2015 on recovery, PDF page 2 at
  200 dpi. Its 15-day period follows a formal default notice; it does not set the
  ordinary monthly remittance deadline. This was a false lead, not corroboration
  of the old payroll row. The ITS article 287 deadline and 2011-Code currency gap
  remain separate and unchanged.

## Retrieval evidence

The following files were retrieved over ordinary verified HTTPS on 12 September
2026. Hashes identify the exact source bytes read; they do not establish currency.

| Source | Bytes | SHA-256 |
|---|---:|---|
| [ao-irt-2020.pdf](https://www.bancoeconomico.ao/media/3172/lei28-20-22dejulhoalteracoescirt.pdf) | 626803 | `e4bb587ee3738a34b76965974b3737f04b3b678614ee54cef543a04a59548353` |
| [bi-inss-contributions.html](https://inss.gov.bi/comment-un-travailleur-est-il-affilie-a-linss/) | 179899 | `5f54c6598d674239db56789bff55fbeed74759e676b45788ae1ff9343ece59c7` |
| [bi-inss-calculation.html](https://inss.gov.bi/calcul-des-cotisations/) | 176875 | `c7425a7f3f5141bd628ca71ef4bd610b0c9261182ae5889771362fb4a4bed985` |
| [bi-social-code2020.pdf](https://p4h.world/app/uploads/2023/02/CODE20de2020Protection20Sociale20du20Burundi.x24228.pdf) | 20765493 | `efd5045dc3848881b07a59b52c892c1cd834ffb4d39fd56f7fade6396b6756c2` |
| [dj-amu-2014.pdf](https://cnss.dj/storage/2016/10/Loi_n24AN147eme_L_Portant_creation_de_lamu.pdf) | 247533 | `2fa2d54c497872bd77dc4d5660a2a5af1760e9f28c9cf87451832fbaf773caaa` |
| [dj-cnss-base2015.pdf](https://cnss.dj/storage/2016/10/ARR_N_2015_605_PR_MTRA.pdf) | 406085 | `7e990d56d35206d9e205f682d09f9faa0323cc5d52272440cec9ef0c98fd0e8d` |
| [dj-amu-amend2015.pdf](https://cnss.dj/storage/2016/10/LOI_N_109_AN_2015_7_EME_LOI.pdf) | 172511 | `282a117cc13b72d3d0507127b97ee6b905619a6773ca8877e2a1c95672ab5dfe` |
| [dj-cnss-employer.html](https://cnss.dj/espace-employeur/) | 197678 | `4745e9410c1ca33bc3aaba392f91bea7cf16505712634d179169b8d73c176298` |
| [dj-cnss-collection2015.pdf](https://cnss.dj/storage/2016/10/LOI_N_111_AN_2015_7EME_L.pdf) | 136256 | `e4274e70140b2ea52bbd4f312f9319de96351c760895d8427dbe6485b9e85b9a` |
