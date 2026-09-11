---
name: mk-corporate-income-tax
description: "Use this draft for questions about North Macedonian corporate profit tax, withholding, loss relief, the simplified regime and minimum global profit tax for tax year 2025. It cites the Public Revenue Office's Profit Tax Law, minimum-tax Act and corrected article 13(9) rulebook. The published domestic and other top-up returns have been examined field by field, including their formulas and instructions. The domestic form contains an unresolved additional-tax inconsistency, so its printed arithmetic must not be treated as a complete filing algorithm. Pending local-accountant review."
jurisdiction: MK
tax_year: 2025
last_updated: 2026-09-12
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# North Macedonia Corporate Income Tax

## Corporate profit tax rate and base

Every row in this section was sourced to a commercial summary until September 2026.
The Public Revenue Office publishes the consolidated **Закон за данокот на добивка**
(Profit Tax Law) as a 19-page PDF on its own regulation register, and everything below is
now read from that text — Службен весник на РМ бр. 112/14, 129/15, 23/16, 190/16, 248/18
and Службен весник на РСМ бр. 232/19, 275/19, 290/20, 151/21 and **199/23 of 25 September
2023**, which is the version in force.

- **Corporate profit tax rate** — **10%**. Article 2 of the Law, in one sentence: *"Стапката на данокот на добивка изнесува 10%."*  _([Закон за данокот на добивка, чл. 2](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Who is a taxpayer, and the residence test** — A **resident legal entity** deriving profit from activity **in the country and abroad** (art. 4(1)). Resident means an entity **established, or having its seat, in the territory** of North Macedonia (art. 4(2)). The test is incorporation or registered seat — **place of effective management does not appear in the Law**, so a company seated abroad but managed from Skopje is not made resident by article 4  _([Закон за данокот на добивка, чл. 4](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Non-profit organisations are outside profit tax, with a turnover trigger** — Associations, foundations, political parties, religious communities, the Red Cross, trade unions, chambers and similar bodies are **not profit-tax payers** (art. 4-а(1)), and membership fees, donations, grants, bequests, budget funding and dividends from companies they founded are non-taxable (art. 4-а(2)). But a body of that kind carrying on **economic activity** becomes liable to total-income tax once annual income from that activity exceeds **MKD 1,000,000** (art. 4-а(3))  _([Закон за данокот на добивка, чл. 4-а](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Tax base** — Accounting profit adjusted for non-deductible expenses and other tax adjustments under the Profit Tax Law  _(Law on Profit Tax)_
- **Tax on non-deductible expenses** — Non-deductible / non-business expenses are added to the tax base and effectively taxed at 10%  _(Law on Profit Tax)_
- **⚠ Loss carryforward is three years AND needs permission, applied for by 31 March** — A loss shown in the income statement, reduced by expenses disallowed in the tax balance, may be carried forward **up to three years** from the year it was shown (art. 19(1)), offset **starting with the oldest loss** (art. 19(2)). Two conditions change the answer: the right is **lost entirely** where the taxpayer's status changes by merger, acquisition, division, ownership transformation **or the like** (art. 19(3)); and the relief is available **only with Public Revenue Office approval**, on an application filed **no later than 31 March of the year following** the loss year (art. 19(4)), which the Office must decide within **60 days** (art. 19(5)). A guide that says "losses carry forward three years" and stops leaves a reader to miss the 31 March application and lose the relief outright  _([Закон за данокот на добивка, чл. 19](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Simplified regime — the two thresholds, exactly** — Companies classified as **small and micro traders**, and resident legal entities keeping accounts under the Companies Act, are **exempt** from the annual total-income tax where total income from any source does not exceed **MKD 3,000,000** (art. 32). Where total income is **MKD 3,000,001 to 6,000,000** they may **elect** to pay the annual total-income tax at **1%** of total income shown in the income statement (arts. 33(1), 34(2)), filed on form **„ДБ-ВП"**. **Banking, financial, insurance and games-of-chance activities are excluded** from the regime (arts. 31(2), 33(1)1). And the election **locks in for three years** including the year of payment, if income stays in that band (art. 33(2))  _([Закон за данокот на добивка, чл. 31–35](https://ujp.gov.mk/mk/regulativa/opis/295))_

### Withholding on payments to foreign legal entities — ten heads, four carve-outs

Chapter IV of the Law is headed *Задржување на данок на приход платен на странски правни
лица* and article 20(1) applies it to payments **to a foreign legal entity**. Everything
in it is confined to that case, which is what answers the resident-to-resident question
further down.

- **Who must withhold** — A **domestic legal entity**; a **domestic natural person registered to carry on an activity**; and a **non-resident foreign legal or natural person with a permanent establishment** in North Macedonia (art. 20(3)). The registered sole trader in that list is easy to miss. Tax is withheld and paid to the appropriate account **simultaneously with payment** of the income (art. 20(1))  _([Закон за данокот на добивка, чл. 20](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **The withholding is final for the foreign recipient** — Article 20(2): tax withheld on any income of a foreign legal entity **finally settles** that entity's liability for that income. There is no subsequent assessment to true it up  _([Закон за данокот на добивка, чл. 20(2)](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Ten enumerated heads, not eight and not three** — Article 21(1) lists: (1) dividends; (2) interest **from a resident**; (3) interest from a **non-resident with a PE** in North Macedonia where the interest is borne by the PE; (4) royalties paid **by a resident**; (5) royalties paid by a non-resident where borne by a PE; (6) entertainment or sporting activities **performed in** North Macedonia; (7) **management, consulting, financial and research-and-development services**, where paid by a resident or borne by a PE; (8) insurance or reinsurance premiums for **risks in** North Macedonia; (9) telecommunications services between North Macedonia and a foreign state; (10) **lease of immovable property** in North Macedonia. This guide carried the classic three until September 2026 and then eight; the statute splits interest and royalties each into a resident-paid limb and a PE-borne limb, so the enumeration is **ten** rate  _([Закон за данокот на добивка, чл. 21(1)](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **The rate is 10% on the gross, and "gross" is defined** — Article 22(1): tax is computed on **gross income** at **10%**. Article 22(2) defines gross as the income that **would have been paid** to the foreign entity had no tax been withheld. A net-of-tax contract therefore has to be grossed up, not treated as the base rate  _([Закон за данокот на добивка, чл. 22](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Four statutory carve-outs the guide did not carry** — Article 21(2): no withholding on (1) the **transfer of part of the profit of a PE** of a foreign legal entity in North Macedonia on which profit tax has already been paid; (2) interest on **debt instruments issued and/or guaranteed by the Government, the National Bank, and banks or other financial institutions acting as the Government's representative**; (3) interest on **deposits with a bank located in** North Macedonia; and (4) income from **brokerage or consulting on government securities in an international financial market**. This guide previously said only "government bond interest exempt", which is the narrowest reading of carve-out (2) and misses the other three  _([Закон за данокот на добивка, чл. 21(2)](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Treaty relief needs a certified form before payment, and the payer carries the shortfall** — A treaty rate caps the article 22 rate (art. 23(1)), but it applies only where the payer **holds the prescribed form certified by the foreign competent tax authority *and* by the Public Revenue Office**, or a Public Revenue Office exemption approval (art. 23(2)). If the payer applies the treaty without those conditions being met and too little tax is paid, **the payer must make good the difference** (art. 23(3)). The Office must grant or refuse within **30 days** (art. 23(5)), and must certify tax paid on a non-resident's request (art. 23(4)). The practical consequence: relief is a pre-payment formality, not a filing-season adjustment  _([Закон за данокот на добивка, чл. 23](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Annual withholding report — 15 February** — The withholding agent files one report a year on tax withheld, to the Public Revenue Office, **by 15 February of the year following** the year in which the withholding obligation arose  _([Закон за данокот на добивка, чл. 24(1)](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Dividends between resident companies — answered, and the condition is the operative part** — The flag previously on this row is discharged. Article 18: the tax base **is reduced** by dividend income derived from participation in the capital of **another taxpayer resident in North Macedonia**, **provided that income has been taxed at the taxpayer paying the dividend**. Two things follow. It is a **tax-base reduction**, not a withholding exemption — chapter IV never reached the case, because it is confined to foreign payees. And it is **conditional**: a dividend out of profits not taxed at the payer does not qualify  _([Закон за данокот на добивка, чл. 18](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Double tax treaty network — 49 agreements listed, which is not the same as 49 countries** — The Public Revenue Office's own *Меѓународни договори* register lists **49 double-taxation agreements**, counted from the register rather than taken from a summary. Treaty rates range 0%–15%, and the approval mechanics are article 23 above. **The count is of agreements, not of counterparties in force today**: one is with the *Сојузна Влада на Сојузна Република Југославија* — a state that no longer exists — and succession to it is a separate question the register does not answer  _([Public Revenue Office treaty register](https://ujp.gov.mk/mk/regulativa/pregled/tr/md))_
- **⚠ Annual profit-tax return — the Law fixes no calendar date** — Article 39(1): profit tax is determined and paid on form **„ДБ — даночен биланс за оданочување на добивка"**, submitted to the Public Revenue Office **within the deadline prescribed for filing the annual accounts under the Companies Act and the accounting regulations**. This guide previously said "by the end of February… (approx — confirm)" and cited the Profit Tax Law for it. **That date is not in the Profit Tax Law.** Whatever the correct date is, it has to be sourced to the Companies Act and accounting rules, which have not been read here. Transfer-pricing filers also attach annex **„П/ТЦ"** (art. 39(5))  _([Закон за данокот на добивка, чл. 39](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Advance payments are indexed to retail prices, and that is not a detail** — Article 40(1): monthly advances are **one twelfth** of the tax determined in the **previous year's** tax balance, **increased by the percentage of cumulative retail-price growth** in the Republic to 31 January of the following year against the previous year's average retail prices. Article 40(2): each advance is due **within 15 days after the end of each calendar month**. Article 40(3): a taxpayer who has donated under art. 30-а may reduce advances by the donation, capped at **50%** of the advance. Article 40(4): the advance obligation does **not** apply to the non-profits in art. 4-а(3) or to simplified-regime companies under art. 31  _([Закон за данокот на добивка, чл. 40](https://ujp.gov.mk/mk/regulativa/opis/295))_
- **Tax period** — The calendar year; where the taxpayer operated for less than a full calendar year, the period is that part of the year  _([Закон за данокот на добивка, чл. 38](https://ujp.gov.mk/mk/regulativa/opis/295))_

## Minimum global profit tax — a second charge, and it reaches back to fiscal 2024

Two sibling guides carried this and the file a reader opens for North Macedonian
corporate tax did not. Both cited it to KPMG and Mondaq, or to "OECD Pillar Two /
domestic implementing legislation" — which names no instrument. The Act is published
by the Public Revenue Office itself, and everything below is read from that text.

- **The instrument** — *Закон за минимален глобален данок на добивка* (Law on the
  Minimum Global Profit Tax), published in **Службен весник на РСМ бр. 3 од 3.1.2025**
  — Official Gazette of the Republic of North Macedonia **No. 3 of 3 January 2025**.
  Article 61: it enters into force **on the day of publication**, so 3 January 2025  _(Public Revenue Office register — https://ujp.gov.mk/mk/regulativa/opis/437)_
- **⚠ It applies to fiscal years beginning 1 January 2024 — a year before publication** —
  Article 59(1): *"Одредбите од овој закон се применуваат за фискалните години кои
  започнуваат на 1 јануари 2024 година."* The two sibling guides say "effective
  1 Jan 2025"; that is **wrong by a year** for every charge except the one below  _(Law on the Minimum Global Profit Tax, art. 59(1))_
- **The exception — the undertaxed profits rule starts a year later** — Article 59(2):
  articles 14, 15 and 16, which concern the *правило за помалку оданочена добивка*
  (undertaxed profits rule), apply to fiscal years beginning **1 January 2025**  _(art. 59(2))_
- **Who is in scope** — Constituent entities that are members of an MNE group **or of a
  large domestic group** — a purely domestic Macedonian group of sufficient size is
  caught — whose annual revenue in the ultimate parent's consolidated financial
  statements is **EUR 750,000,000 or more in at least two of the four fiscal years
  immediately preceding** the tested fiscal year, **including** the revenue of excluded
  entities under article 5(3). Where any of those years is longer or shorter than
  twelve months, the threshold is adjusted proportionally  _(art. 5(1)–(2))_
- **Minimum tax rate**: Article 4(15) defines *„Минимална даночна стапка"* as a rate of
  **петнаесет проценти (15 %)**, fifteen per cent, given in words and digits together  _(art. 4(15))_
- **All three charges are present** — the Act works with a *квалификуван домашен
  дополнителен данок* (qualified domestic top-up tax), the *правило за вклучување на
  добивката* (income inclusion rule) and the *правило за помалку оданочена добивка*
  (undertaxed profits rule). As elsewhere, the domestic top-up is the limb that reaches
  a Macedonian entity of a foreign-parented group  _(Law on the Minimum Global Profit Tax)_
- **The by-law article 60 required was made — on the deadline day itself** — Article 60
  gave the Minister of Finance until **31 December 2025** to adopt the secondary act under
  article 13(9). The *Правилник за начинот на пресметување и наплата на дополнителниот
  данок на добивка* is dated **31 December 2025** (no. 23-6896/1, signed in Skopje by the
  Minister of Finance), published in **Службен весник на РСМ бр. 270/2025 од 31.12.2025**
  with a corrigendum at **бр. 2/2026 од 5.01.2026**, and in force the day after
  publication (art. 13), so **1 January 2026**. Its own basis clause reads *"Врз основа на
  член 13 став (9) од Законот…"* — it is the article 13(9) act, not a different one  _([Public Revenue Office register](https://ujp.gov.mk/mk/regulativa/opis/441))_

### What the article 13(9) ordinance actually prescribes

- **Two return forms, and both are filed at zero** — The domestic charge uses *Пријава за
  квалификуван домашен дополнителен данок*, **образец „КДДД/П"** (arts. 3–4, Прилог 1);
  the income-inclusion and undertaxed-profits charges use *Пријава за дополнителен данок*,
  **образец „ДДД/П"** (arts. 8–9, Прилог 2). Both are filed electronically to the Public
  Revenue Office, and article 3 says in terms that the return **is filed even where the
  computed liability is "0"** — repeated for ДДД/П in article 8. A nil computation is not
  a reason not to file  _([Правилник, arts. 3, 4, 8, 9](https://ujp.gov.mk/mk/regulativa/opis/441))_
- **One designated filer for the whole Macedonian footprint** — Where two or more
  constituent entities of the same MNE or large domestic group are in North Macedonia,
  **one is designated** to file and makes a combined computation covering all of them
  (art. 3). The designation is notified to the Public Revenue Office electronically
  (art. 7)  _([Правилник, arts. 3 and 7](https://ujp.gov.mk/mk/regulativa/opis/441))_
- **Computation uses the Act and the OECD references**: Rulebook article 2 refers to
  adopted OECD models and rules. The Act also contains computation rules: article 29
  gives the top-up percentage, excess-profit and jurisdictional-tax formulas. Its
  positive-amount conditions must be applied when using the short formulas printed
  on the returns. The earlier assertion that no mechanics appear in Macedonian law
  was wrong. [Rulebook article 2](https://ujp.gov.mk/mk/regulativa/opis/441);
  [Act article 29](https://ujp.gov.mk/mk/regulativa/opis/437).
- **Two computational rules worth having exactly, and they apply to *both* returns** —
  Effective tax rate and top-up percentages are **rounded to four decimal places**. Amounts
  computed in foreign currency are converted to denars at the **middle rate published by the
  National Bank of the Republic of North Macedonia for the last month of the fiscal year**
  the return covers — not the year-end spot rate and not an average for the year. The rule
  appears **twice in identical terms**: article 5 for the КДДД/П return and article 10 for
  the ДДД/П return, so it is not specific to either  _([Правилник, arts. 5 and 10](https://ujp.gov.mk/mk/regulativa/opis/441))_
- **⚠ Article 1 lists four subject matters but there are only two forms** — Article 1
  announces rules for the qualified domestic top-up tax, the information return, the
  top-up tax return **and** the *домашен дополнителен данок* (domestic top-up tax) as a
  fourth head. **Articles 11 and 12 then collapse the fourth onto the first**: the return
  for the domestic top-up tax is filed **on the same образец „КДДД/П"** prescribed by
  article 3, and payment is made in the manner set out in articles 3, 4 and 5. A reader
  working from article 1 will look for a fourth form that does not exist  _([Правилник, arts. 1, 11 and 12](https://ujp.gov.mk/mk/regulativa/opis/441))_
- **The information return can be discharged abroad** — The closing paragraph of article 6
  relieves a local constituent entity of filing the *Пријава на информации* where the
  return has been filed by the **ultimate parent** or by a designated filing entity located
  in a jurisdiction with which North Macedonia has concluded a **qualifying competent
  authority agreement**. Note what this does *not* reach: articles 3 and 8 still require the
  **КДДД/П and ДДД/П returns** to be filed locally, and both are due **even at nil**  _([Правилник, arts. 3, 6 and 8](https://ujp.gov.mk/mk/regulativa/opis/441))_

> **Sources.** The Act (60 pages) and the article 13(9) *Правилник* (3 pages) were both
> read from the PDFs the Public Revenue Office publishes on its own regulation register at
> `ujp.gov.mk`, which carries a dedicated *Минимален глобален данок на добивка* category
> holding exactly these two instruments. The Official Gazette itself (`slvesnik.com.mk`)
> **fails certificate verification** — "unable to get local issuer certificate" — and
> passing the CA bundle does not fix it, so it was not fetched with verification disabled.
> The tax authority carried both texts anyway.
>
> **The corrigendum is incorporated in the text above.** An earlier pass recorded the
> corrigendum at Службен весник бр. 2/2026 of 5 January 2026 as unread. The PDF the Public
> Revenue Office serves **is the consolidated text as corrected** — its own masthead reads
> *"Службен весник на РСМ, бр.270/2025 од 31.12.2025 **и исправка** во Службен весник на
> РСМ, бр. 2/2026 од 5.01.2026 година"* — so every article stated above is the corrected
> wording, not the 31 December original.
>
> **What is still not established is the *delta*.** The consolidated text does not mark what
> changed, and the original бр. 270/2025 text was not obtained for comparison, so this guide
> can say the corrected text has been read in full but **cannot say what the corrigendum
> altered**. For a reader applying the ordinance that distinction does not matter — the text
> above is the operative one. It matters only to someone reconciling against a copy taken
> between 31 December 2025 and 5 January 2026.
>
### Published return fields checked on 12 September 2026

The three-page consolidated rulebook refers to Прилог 1 and Прилог 2 but does not
include their pages. The Public Revenue Office separately publishes the corresponding
[КДДД/П domestic return](https://www.ujp.gov.mk/files/attachment/0000/1611/KDDD-P.pdf)
and [ДДД/П other top-up return](https://ujp.gov.mk/files/attachment/0000/1610/DDD-P.pdf).
All three and two pages respectively, including their bilingual instructions, were
read from extracted text and individual 200 dpi images. Both state that the forms
apply from 1 January 2026. This is a review of those published forms, without a
byte-for-byte comparison with the original gazette annexes.

| Field | КДДД/П, jurisdiction calculation | ДДД/П |
|---|---|---|
| a | Qualified net income | Qualified net income |
| b | Adjusted covered taxes | Adjusted covered taxes |
| c | Effective rate, printed as `b/a` | Effective rate, printed as `b/a` |
| d | Minimum rate, preprinted 15% | Minimum rate, preprinted 15% |
| e | Top-up percentage, printed as `d-c` | Top-up percentage, printed as `d-c` |
| f | Substance-based income exclusion | Substance-based income exclusion |
| g | Domestic tax payable, printed as `(a-f)*e` | Excess profit, printed as `a-f` |
| h | Additional top-up tax | Additional top-up tax |
| i | No field | Domestic top-up tax paid at local jurisdiction level |
| j | No field | Top-up tax payable, printed as `g*e+h-i` |

КДДД/П also asks for the fiscal year, ultimate parent's name and tax ID, lead
entity's name and tax ID, the names and tax IDs of entities 2 and 3, and decisions,
exclusions and safe harbours with their validity periods. Page 2 repeats fields
a–g for the lead entity and entities 2 and 3, each with responsible-person and
telephone fields. The paper layout does not establish a three-entity group limit.
ДДД/П asks for the fiscal year and the names and tax IDs of the ultimate and
intermediate parents.

**Unresolved form conflict:** КДДД/П page 1 prints `g=(a-f)*e` and separately lists
additional top-up tax at h. Page 3 says to increase g by additional top-up tax, but
both languages refer to that addition as field g. Page 2 has no h field. Confirm
the required treatment with the Public Revenue Office before preparing a return
with additional top-up tax; this guide does not silently repair the official form.
The field-by-field evidence and statutory cross-references are in the methodology.

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
