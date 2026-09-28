# Verification log

Dated, first-person entries from the September 2026 verification pass over this corpus: what was checked against which outside source, what turned out to be wrong, what the checkers could and could not see, and the false starts. The methodology they apply is [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md), which held all of them as one 7,000-line file until 2026-09-28; each entry is the text as written on the day, under its own heading, dated by the commit that added it (one entry came from [COVERAGE.md](../COVERAGE.md)). Nothing here is re-verified when the guides change: an entry describes the tree on its date, and the guides and `docs/guide-migrations.json` say what happened since.

To add an entry, write `YYYY-MM-DD-<topic>.md` in this directory with the entry's title as its `#` heading, and add a row below; `tests/test_docs_links.py` fails on an entry that is not listed here, on a listed file that does not exist, and on any link that does not resolve.

| Date | Entry |
|---|---|
| 2026-09-09 | [Where the defects actually were](2026-09-09-where-the-defects-actually-were.md) |
| 2026-09-09 | [What the six VAT errors had in common](2026-09-09-what-the-six-vat-errors-had-in-common.md) |
| 2026-09-09 | [What "verified" means here, and what it does not](2026-09-09-what-verified-means-here-and-what-it-does-not.md) |
| 2026-09-09 | [A "last verified" date is a falsifiable claim](2026-09-09-a-last-verified-date-is-a-falsifiable-claim.md) |
| 2026-09-09 | [A guide can cite its source faithfully and still be incomplete](2026-09-09-a-guide-can-cite-its-source-faithfully-and-still-be.md) |
| 2026-09-09 | [Three ways a guide comes to name three heads, and what each costs to fix](2026-09-09-three-ways-a-guide-comes-to-name-three-heads-and-what-each.md) |
| 2026-09-09 | [Fixing a figure once is not fixing it](2026-09-09-fixing-a-figure-once-is-not-fixing-it.md) |
| 2026-09-09 | [One defect that needs no script](2026-09-09-one-defect-that-needs-no-script.md) |
| 2026-09-09 | [The article you find first may not be the article that governs](2026-09-09-the-article-you-find-first-may-not-be-the-article-that.md) |
| 2026-09-10 | [Most of the corpus's citations are secondary, and it shows](2026-09-10-most-of-the-corpus-s-citations-are-secondary-and-it-shows.md) |
| 2026-09-10 | [An allowlist can be wrong upwards, and that error never reports itself](2026-09-10-an-allowlist-can-be-wrong-upwards-and-that-error-never.md) |
| 2026-09-10 | [A citation can name the right statute and still mislead](2026-09-10-a-citation-can-name-the-right-statute-and-still-mislead.md) |
| 2026-09-10 | [The queue read 1, and that was the strongest evidence it was broken](2026-09-10-the-queue-read-1-and-that-was-the-strongest-evidence-it-was.md) |
| 2026-09-10 | [Reading the statute changes the answer, and twice it nearly changed it wrongly](2026-09-10-reading-the-statute-changes-the-answer-and-twice-it-nearly.md) |
| 2026-09-10 | [A second heuristic tried and discarded: denied-but-still-asserted](2026-09-10-a-second-heuristic-tried-and-discarded-denied-but-still.md) |
| 2026-09-10 | [A cited domain can stop being what the citation says it is](2026-09-10-a-cited-domain-can-stop-being-what-the-citation-says-it-is.md) |
| 2026-09-10 | [Legal information institutes are not a class](2026-09-10-legal-information-institutes-are-not-a-class.md) |
| 2026-09-10 | [Why so much of this corpus cites PwC: some authorities cannot be read](2026-09-10-why-so-much-of-this-corpus-cites-pwc-some-authorities.md) |
| 2026-09-10 | [When every number in a guide comes from one place](2026-09-10-when-every-number-in-a-guide-comes-from-one-place.md) |
| 2026-09-10 | [A total and its parts, asserted twice, in the shape nothing was reading](2026-09-10-a-total-and-its-parts-asserted-twice-in-the-shape-nothing.md) |
| 2026-09-10 | [A blind spot fixed, that turned out to be empty](2026-09-10-a-blind-spot-fixed-that-turned-out-to-be-empty.md) |
| 2026-09-10 | [Togo: five guides, one PDF, and eleven figures that did not survive it](2026-09-10-togo-five-guides-one-pdf-and-eleven-figures-that-did-not.md) |
| 2026-09-10 | [And the checker called the revenue authority a commercial host](2026-09-10-and-the-checker-called-the-revenue-authority-a-commercial.md) |
| 2026-09-10 | [The reader that said a document was empty when it had not read it](2026-09-10-the-reader-that-said-a-document-was-empty-when-it-had-not.md) |
| 2026-09-10 | [Cote d'Ivoire: the same levy, counted at two levels of the same tax](2026-09-10-cote-d-ivoire-the-same-levy-counted-at-two-levels-of-the.md) |
| 2026-09-10 | [The same checker, tried a second time, discarded a second time](2026-09-10-the-same-checker-tried-a-second-time-discarded-a-second-time.md) |
| 2026-09-10 | [Guinea-Bissau: a guide filed under a tax the country does not have](2026-09-10-guinea-bissau-a-guide-filed-under-a-tax-the-country-does.md) |
| 2026-09-10 | [Myanmar: the bands were right and three whole charges were missing](2026-09-10-myanmar-the-bands-were-right-and-three-whole-charges-were.md) |
| 2026-09-10 | [Armenia, again: the second reviewer finding that was wrong](2026-09-10-armenia-again-the-second-reviewer-finding-that-was-wrong.md) |
| 2026-09-10 | [Vietnam: the guide named a ministry that had been abolished](2026-09-10-vietnam-the-guide-named-a-ministry-that-had-been-abolished.md) |
| 2026-09-10 | [San Marino: the file said its own totals were wrong, and it was right](2026-09-10-san-marino-the-file-said-its-own-totals-were-wrong-and-it.md) |
| 2026-09-10 | [San Marino again: the framing was right, the tax was half-described, and the citations pointed at a law that does not set the rates](2026-09-10-san-marino-again-the-framing-was-right-the-tax-was-half.md) |
| 2026-09-11 | [Six-jurisdiction source review, September 2026](2026-09-11-six-jurisdiction-source-review-september-2026.md) |
| 2026-09-11 | [Sierra Leone concurrent update and review](2026-09-11-sierra-leone-concurrent-update-and-review.md) |
| 2026-09-11 | [Armenia — the authority was one form submission away](2026-09-11-armenia-the-authority-was-one-form-submission-away.md) |
| 2026-09-11 | [Guinea — reaching the authority and finding it does not publish the law](2026-09-11-guinea-reaching-the-authority-and-finding-it-does-not.md) |
| 2026-09-11 | [A source-availability register for the rest of the queue](2026-09-11-a-source-availability-register-for-the-rest-of-the-queue.md) |
| 2026-09-11 | [Cape Verde — the operator contradicts the summary, and the code stays out of reach](2026-09-11-cape-verde-the-operator-contradicts-the-summary-and-the.md) |
| 2026-09-11 | [Two ways to manufacture a false "unreachable", both hit in one sitting](2026-09-11-two-ways-to-manufacture-a-false-unreachable-both-hit-in-one.md) |
| 2026-09-11 | [Nicaragua — the legal database is live, and it is not the one the links point at](2026-09-11-nicaragua-the-legal-database-is-live-and-it-is-not-the-one.md) |
| 2026-09-11 | [Nicaragua — five layers to the text, and the Code contradicts the guide](2026-09-11-nicaragua-five-layers-to-the-text-and-the-code-contradicts.md) |
| 2026-09-11 | [What the Code says that the guide did not](2026-09-11-what-the-code-says-that-the-guide-did-not.md) |
| 2026-09-11 | [OHADA capital rules require the national provisions too](2026-09-11-ohada-capital-rules-require-the-national-provisions-too.md) |
| 2026-09-11 | [Myanmar — three sources, all dead, so the entry is closed rather than open](2026-09-11-myanmar-three-sources-all-dead-so-the-entry-is-closed.md) |
| 2026-09-11 | [Two countries were being governed by a treaty they never joined](2026-09-11-two-countries-were-being-governed-by-a-treaty-they-never.md) |
| 2026-09-11 | [The membership check, run against every other régime — and what it turned up instead](2026-09-11-the-membership-check-run-against-every-other-regime-and.md) |
| 2026-09-11 | [The corpus contains its VAT guides twice, and three of the copies disagree about who reviewed them](2026-09-11-the-corpus-contains-its-vat-guides-twice-and-three-of-the.md) |
| 2026-09-11 | [Delaware's income tax guide was the gross receipts guide](2026-09-11-delaware-s-income-tax-guide-was-the-gross-receipts-guide.md) |
| 2026-09-11 | [Reading article 24 without articles 25 to 28](2026-09-11-reading-article-24-without-articles-25-to-28.md) |
| 2026-09-11 | [Cape Verde, resolved — the missing document was a repealed one](2026-09-11-cape-verde-resolved-the-missing-document-was-a-repealed-one.md) |
| 2026-09-11 | [The gazette can be wrong, and the digits-and-words rule caught it first](2026-09-11-the-gazette-can-be-wrong-and-the-digits-and-words-rule.md) |
| 2026-09-11 | [The repeal check, generalised — and what it found in Nigeria](2026-09-11-the-repeal-check-generalised-and-what-it-found-in-nigeria.md) |
| 2026-09-11 | [India — the same check, and two errors that predate the new Act](2026-09-11-india-the-same-check-and-two-errors-that-predate-the-new-act.md) |
| 2026-09-11 | [OHADA — one uniform act, fourteen guides, six mutually exclusive answers](2026-09-11-ohada-one-uniform-act-fourteen-guides-six-mutually.md) |
| 2026-09-11 | [PR 21 review corrections, 11 September 2026](2026-09-11-pr-21-review-corrections-11-september-2026.md) |
| 2026-09-12 | [Kuwait — a contradiction about *treatment*, which no rate check can see](2026-09-12-kuwait-a-contradiction-about-treatment-which-no-rate-check.md) |
| 2026-09-12 | [The OHADA sweep over-claimed twice, and the review caught both](2026-09-12-the-ohada-sweep-over-claimed-twice-and-the-review-caught.md) |
| 2026-09-12 | [Generalising the Kuwait defect into a detector, and what it cost to make honest](2026-09-12-generalising-the-kuwait-defect-into-a-detector-and-what-it.md) |
| 2026-09-12 | [Oman — the mechanism was named, and the name was the wrong one](2026-09-12-oman-the-mechanism-was-named-and-the-name-was-the-wrong-one.md) |
| 2026-09-12 | [Source-availability register — Oman](2026-09-12-source-availability-register-oman.md) |
| 2026-09-12 | [`category` — the spec requires it, CI does not check it, and the docs already say so](2026-09-12-category-the-spec-requires-it-ci-does-not-check-it-and-the.md) |
| 2026-09-12 | [The review caught a defect the correction introduced — for the second time](2026-09-12-the-review-caught-a-defect-the-correction-introduced-for.md) |
| 2026-09-12 | [Netherlands — the detector's second hit, and the title year is not the commencement year](2026-09-12-netherlands-the-detector-s-second-hit-and-the-title-year-is.md) |
| 2026-09-12 | [591 guides carry two "Talk to a verified accountant" sections](2026-09-12-591-guides-carry-two-talk-to-a-verified-accountant-sections.md) |
| 2026-09-12 | [Spain — the guide had the statute in hand and read one thing out of it](2026-09-12-spain-the-guide-had-the-statute-in-hand-and-read-one-thing.md) |
| 2026-09-12 | [Thailand — the authority's own account, and three different ways a source fails](2026-09-12-thailand-the-authority-s-own-account-and-three-different.md) |
| 2026-09-12 | [Two small corpus-wide defects, one fixed and one measured](2026-09-12-two-small-corpus-wide-defects-one-fixed-and-one-measured.md) |
| 2026-09-12 | [North Macedonia — a citation that named no instrument, and a date wrong by a year](2026-09-12-north-macedonia-a-citation-that-named-no-instrument-and-a.md) |
| 2026-09-12 | [The Pillar Two sweep, closed out](2026-09-12-the-pillar-two-sweep-closed-out.md) |
| 2026-09-12 | [The detector, pointed somewhere else — and the guard that came from reading](2026-09-12-the-detector-pointed-somewhere-else-and-the-guard-that-came.md) |
| 2026-09-12 | [24 VAT guides give no signal that their jurisdiction has an e-invoicing regime](2026-09-12-24-vat-guides-give-no-signal-that-their-jurisdiction-has-an.md) |
| 2026-09-12 | [Germany — checking a guide that turned out to be right, and the one thing it did not cite](2026-09-12-germany-checking-a-guide-that-turned-out-to-be-right-and.md) |
| 2026-09-12 | [Running the repository's own checkers, and what their output is now worth](2026-09-12-running-the-repository-s-own-checkers-and-what-their-output.md) |
| 2026-09-12 | [A tier-1 guide, and where this work stops](2026-09-12-a-tier-1-guide-and-where-this-work-stops.md) |
| 2026-09-12 | [A scan that would have produced five findings, all of them wrong](2026-09-12-a-scan-that-would-have-produced-five-findings-all-of-them.md) |
| 2026-09-12 | [Where the defects actually were, measured rather than asserted](2026-09-12-where-the-defects-actually-were-measured-rather-than.md) |
| 2026-09-12 | [The seven jurisdictions citing no authority — four of them had never been tried](2026-09-12-the-seven-jurisdictions-citing-no-authority-four-of-them.md) |
| 2026-09-12 | [Angola — the authority was live all along, and it corroborated twelve rows](2026-09-12-angola-the-authority-was-live-all-along-and-it-corroborated.md) |
| 2026-09-12 | [Angola, part two — article 20(3) settled it, and the hold was worth three pages](2026-09-12-angola-part-two-article-20-3-settled-it-and-the-hold-was.md) |
| 2026-09-12 | [Croatia — the guess was right and the detector still gets no credit](2026-09-12-croatia-the-guess-was-right-and-the-detector-still-gets-no.md) |
| 2026-09-12 | [Madagascar — the Angola move, tried and failed, which is also a result](2026-09-12-madagascar-the-angola-move-tried-and-failed-which-is-also-a.md) |
| 2026-09-12 | [North Macedonia — closing an open flag turned into the largest single-guide upgrade yet](2026-09-12-north-macedonia-closing-an-open-flag-turned-into-the.md) |
| 2026-09-12 | [Burundi — the negative result was the point, and the recitals page paid for the trip](2026-09-12-burundi-the-negative-result-was-the-point-and-the-recitals.md) |
| 2026-09-12 | [The "no DNS at all" list was partly measured against the wrong hostnames](2026-09-12-the-no-dns-at-all-list-was-partly-measured-against-the.md) |
| 2026-09-12 | [Central African Republic — a 442-page tax code behind a hostname nobody had tried](2026-09-12-central-african-republic-a-442-page-tax-code-behind-a.md) |
| 2026-09-12 | [Djibouti — reachable, and frozen in 2011, which is the Mauritania result got right first time](2026-09-12-djibouti-reachable-and-frozen-in-2011-which-is-the.md) |
| 2026-09-12 | [Vanuatu — the guides cited a dead host for years, and two live authorities were never tried](2026-09-12-vanuatu-the-guides-cited-a-dead-host-for-years-and-two-live.md) |
| 2026-09-12 | [Nothing in this repo asked whether a cited host exists, so 1,254 of them were resolved](2026-09-12-nothing-in-this-repo-asked-whether-a-cited-host-exists-so-1.md) |
| 2026-09-12 | [South Africa — a previous correction moved the URL to a host that does not exist](2026-09-12-south-africa-a-previous-correction-moved-the-url-to-a-host.md) |
| 2026-09-12 | [Chasing the eleven dead hosts, and declining to fix nine of them the fast way](2026-09-12-chasing-the-eleven-dead-hosts-and-declining-to-fix-nine-of.md) |
| 2026-09-12 | [Myanmar — the IRD publishes its rates in Burmese, and the CT guide had only the middle of the range](2026-09-12-myanmar-the-ird-publishes-its-rates-in-burmese-and-the-ct.md) |
| 2026-09-12 | [Four of the repo's own checkers, four hits, zero defects — and one of them defends a correct table](2026-09-12-four-of-the-repo-s-own-checkers-four-hits-zero-defects-and.md) |
| 2026-09-12 | [Guinea: the door was unlocked, and the register said the building was empty](2026-09-12-guinea-the-door-was-unlocked-and-the-register-said-the.md) |
| 2026-09-12 | [Turkmenistan: the guide's highest rate was 20%, and the statute's is 50%](2026-09-12-turkmenistan-the-guide-s-highest-rate-was-20-and-the.md) |
| 2026-09-12 | [Laos: five guides built on a law that was repealed part-way through their tax year](2026-09-12-laos-five-guides-built-on-a-law-that-was-repealed-part-way.md) |
| 2026-09-12 | [Myanmar formation: the ministry serves nothing, its registry serves the statute](2026-09-12-myanmar-formation-the-ministry-serves-nothing-its-registry.md) |
| 2026-09-12 | [Correction: the "39-byte empty document" was two different numbers, and I merged them](2026-09-12-correction-the-39-byte-empty-document-was-two-different.md) |
| 2026-09-12 | [Laos: the personal income tax scale, and what "two rate tables" turned out to mean](2026-09-12-laos-the-personal-income-tax-scale-and-what-two-rate-tables.md) |
| 2026-09-12 | [Andorra: the half that was wrong, and the statute that never held the answer](2026-09-12-andorra-the-half-that-was-wrong-and-the-statute-that-never.md) |
| 2026-09-12 | [Croatia: the safe harbours are not in the Act, and the formulas are JPEGs](2026-09-12-croatia-the-safe-harbours-are-not-in-the-act-and-the.md) |
| 2026-09-12 | [North Macedonia: a gap that was bibliographic, not substantive](2026-09-12-north-macedonia-a-gap-that-was-bibliographic-not-substantive.md) |
| 2026-09-12 | [Oman: a deadline with no support, and an authority that cannot answer its own question](2026-09-12-oman-a-deadline-with-no-support-and-an-authority-that.md) |
| 2026-09-12 | [Djibouti: four rates right, both totals wrong, and a whole regime missing](2026-09-12-djibouti-four-rates-right-both-totals-wrong-and-a-whole.md) |
| 2026-09-12 | [Turkmenistan: the gate on a rate lives in a different statute](2026-09-12-turkmenistan-the-gate-on-a-rate-lives-in-a-different-statute.md) |
| 2026-09-12 | [Oman, second pass: a row this branch wrote was already over-general](2026-09-12-oman-second-pass-a-row-this-branch-wrote-was-already-over.md) |
| 2026-09-12 | [Oman, fourth pass: the correction was made in one guide and the error was still in the other](2026-09-12-oman-fourth-pass-the-correction-was-made-in-one-guide-and.md) |
| 2026-09-12 | [Oman payroll: five branches, three carried, and a 9% charge nobody mentioned](2026-09-12-oman-payroll-five-branches-three-carried-and-a-9-charge.md) |
| 2026-09-12 | [Oman amendment check, 12 September 2026](2026-09-12-oman-amendment-check-12-september-2026.md) |
| 2026-09-12 | [Turkmenistan pension, deduction and company-law follow-up, 12 September 2026](2026-09-12-turkmenistan-pension-deduction-and-company-law-follow-up-12.md) |
| 2026-09-12 | [Angola, Burundi and Djibouti statutory follow-up, 12 September 2026](2026-09-12-angola-burundi-and-djibouti-statutory-follow-up-12.md) |
| 2026-09-12 | [12 September 2026: CAR Finance Acts and North Macedonian return forms](2026-09-12-12-september-2026-car-finance-acts-and-north-macedonian.md) |
| 2026-09-12 | [12 September 2026: Andorra form 900 and correction of the earlier IGI correction](2026-09-12-12-september-2026-andorra-form-900-and-correction-of-the.md) |
| 2026-09-12 | [12 September 2026: Pakistan, UK and Ireland repeal and transition checks](2026-09-12-12-september-2026-pakistan-uk-and-ireland-repeal-and.md) |
| 2026-09-12 | [Kuwait Zakat consistency correction, 13 September 2026](2026-09-12-kuwait-zakat-consistency-correction-13-september-2026.md) |
