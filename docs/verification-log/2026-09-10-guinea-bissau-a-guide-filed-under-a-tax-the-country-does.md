# Guinea-Bissau: a guide filed under a tax the country does not have

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`gw-income-tax.md` sat at the very top of the single-source queue — **10 of 10**
numeric facts on one HR blog, every band marked "(approx — confirm)". It was
titled "Personal income tax (IRPS)" and cited an "Imposto sobre o Rendimento das
Pessoas Singulares (IRPS) statute" nine times.

Guinea-Bissau has no IRPS. The word appears **nowhere** in the tax authority's
own consolidated legislation. Income from work is taxed by the **Imposto
Profissional**, Código approved by Decreto nº 23/83 de 6 de Agosto; business
profit by the **Contribuição Industrial**; sales by the **IGV**. IRPS is the
Cabo Verde, Mozambique and São Tomé name, applied here by analogy — the same
shape as Kosovo citing its accreditation statute as its income tax law, and
harder to see, because the invented name is a real tax somewhere else.

## The bands were right, and almost nothing around them was

The nine bands and their rates — 1 / 6 / 8 / 10 / 12 / 14 / 16 / 18 / 20 per
cent — match art. 27º nº 1 exactly, as worded by Lei nº 1/2021 art. 10º. The
commercial source got them right, which is worth stating plainly: concentration
is exposure, not error. What it did not carry:

- **That the rates are marginal.** Art. 27º nº 3 says the percentages
  *"representam **taxas marginais**"* and art. 28º repeats it. The guide gave
  nine bare bands and no application rule. Applying 20% to a whole salary
  overstates the tax several times over.
- **A second schedule entirely.** Art. 27º nº 2 puts the self-employed and
  holders of copyright income on three bands — 10 / 20 / 25 — starting at 10%
  where an employee starts at 1%. The guide presented the employee table as *the*
  personal income tax.
- Occasional income at 10% (nº 4); pensions of XOF 200,000/month or less exempt;
  employer remittance within **10 days** of month end (art. 29º), where the guide
  gave no remittance deadline at all; the XOF 2,000 de minimis on assessment.

And the hedge the guide flagged against itself — *"some sources cite a 0% first
band"* — is settled: there is no 0% band, 1% applies from the first franc.

## Nine article numbers were wrong before they were checked

The first draft of the rewrite cited arts. 4º, 22º, 25º-A, 26º and 32º from
context — the shape of where such provisions usually sit. Resolving each against
the nearest preceding heading in the consolidated text gave arts. **1º, 2º, 13º,
31º-A and 37º**. Only art. 18º was right by guess. This is the Togo lesson
arriving in a new costume: there, two books bound in one PDF each numbered from
1; here, plausible article numbers written from habit. **A citation is a claim,
and the cost of checking it is one search.**

## The arithmetic found a defect in the statute

The schedule ships a *parcela a abater* — the amount subtracted from rate ×
income, the standard lusophone shortcut for a marginal computation. Testing it
at all eight band boundaries, it reproduces the marginal result exactly at seven.
At the fifth-to-sixth it does not:

| | monthly | annual |
| --- | ---: | ---: |
| band 5 at its top (12%, parcela 13,917 / 167,004) | 34,143 | 409,716 |
| band 6 at its start at the **current 14%** (parcela 37,947 / 455,364) | **18,123** | **217,478** |
| band 6 at its start at the **superseded 18%** | 34,143 | 409,718 |

The parcela is continuous **at 18%** — the rate the band carried under Lei nº
8/2020 — and not at the 14% substituted by Lei nº 1/2021. On its face the rate
was cut and the parcela derived for the old rate was left behind, so applying
the published figure literally makes tax **fall by 16,020 a month** as income
rises through XOF 400,501.

That is the Côte d'Ivoire lesson generalised. There, arithmetic settled which
column was which when a table extracted scrambled. Here it found something no
reading would: **the schedule is internally consistent everywhere except at the
one boundary an amending law moved.** It is recorded as a research gap naming
both methods, not "corrected" to the 21,927 that continuity would require —
that is a value the arithmetic implies, not one the statute states, and writing
it in would be inventing law to make a sum close.

## The classifier gap, predicted and then observed

The comment beside `dgbf.ci` in `list-source-mix.py` ended: *"the next one will
arrive the same way."* It did, on the next jurisdiction opened. `mef.gw`,
`dgci.mef.gw` and `kontaktu.mef.gw` — a finance ministry, its tax directorate,
and the portal serving the consolidated codes with superseded wording struck
through — all classified as commercial. Bare ccTLD, no `gov` label.

One thing was different this time, and it is the point of writing predictions
down: the allowlist entry went in **with** the citation change rather than after
it. Togo and Côte d'Ivoire each pushed the corpus's secondary count *up* by
citing their own revenue authority, and the fix trailed the finding by a commit.
Guinea-Bissau did not: authority citations rose 2,705 → 2,724 and secondary fell
4,767 → 4,757 in the same change. The shape is a bare ccTLD, not a language —
Togo and Côte d'Ivoire were francophone, this one is lusophone.

## The same jurisdiction's VAT guide: every figure right, and the tax half-described

`gw-vat-gst.md` was the next guide on the queue — **9 of 9** facts on one
commercial host. Unlike the income-tax guide, its framing was correct and so was
every number: 19% standard, 10% reduced, 0% exports, thresholds of FCFA
40,000,000 and 10,000,000. All confirmed against arts. 18.º, 37.º and 38.º of the
Código do IVA (Lei nº 4/2022, Boletim Oficial nº 8, 4th supplement, 25 February
2022). **Concentration is exposure, not error**, and this is the second guide in
one jurisdiction to prove it.

What a rate table cannot tell you is how the tax operates, and that is what was
missing:

- **The simplified regime is a turnover tax, not a reduced VAT.** 5% of the value
  of supplies with **no input deduction at all**, and its invoices give the buyer
  **no right of deduction**, which the invoice must say (arts. 38.º nos 2–3,
  39.º). The guide called it "a simplified VAT scheme".
- **A domestic withholding with no trace in the guide.** A normal-regime buyer
  must withhold **the entire IVA** charged on an invoice from a simplified-regime
  supplier, or from a normal-regime supplier the director-general has designated
  a *contribuinte de risco* (art. 7.º nº 3). A buyer who pays such an invoice
  gross has underpaid the state.
- **Non-residents must appoint a fiscal representative**, who is the debtor for
  the tax and must be named to the counterparty *before* the operation, with the
  represented person jointly and severally liable (art. 33.º).
- **Filing**: normal regime monthly by the **15th**, nil returns mandatory
  (art. 31.º); simplified regime **quarterly**, last working day of April, July,
  October and January (art. 42.º). The guide had "monthly ((approx — confirm))"
  and nothing at all for the simplified regime — right for one regime, silent for
  the other.
- **A 30% flat surcharge** on imports by anyone on the monthly list of IVA
  non-declarants (Lei nº 4/2022 art. 6.º).
- Below FCFA 10,000,000 a person is exempt from IVA **and** subject to a single
  small-taxpayer tax *"em termos a fixar por lei"* (art. 45.º) — not simply
  outside the system.

Two smaller things the reading settled. The IGV it replaced also stood at 19%, so
the guide's "replaced the former 19% general sales tax" was right — but the IGV
carried a **15% band on electricity and water** that the IVA does not, so it is
not a like-for-like swap. And the Code's own art. 37.º nº 6 points to *"o regime
de pequenos contribuintes previstos no artigo 46º"* when that regime is art. 45.º
and art. 46.º is *Garantias* — recorded as a gap against the Boletim Oficial
text rather than silently renumbered.

**The citation discipline held better the second time, and still not well
enough.** Writing the guide, seven article numbers were again put down from
context; resolving each against the nearest heading corrected **three** — the
partial-deduction rule is art. 23.º not 27.º, taxpayer-initiated payment is
art. 25.º not 29.º, administration-initiated payment art. 26.º not 30.º — and one
number I could not confirm was softened rather than asserted. Three wrong out of
seven, against eight out of nine an hour earlier, because this time some headings
had been read directly rather than inferred. The rule that works is not "be more
careful"; it is **resolve every article number mechanically before writing it
down**.

Guinea-Bissau's secondary share moved the corpus across a boundary: authority
citations 2,724 → **2,746**, secondary 4,757 → **4,750**, and the corpus's
secondary share from 64% to **63%**. Only `gw-payroll-social.md` is left on the
single-source queue for this jurisdiction.

---
