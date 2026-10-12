# Anguilla: registration references and publication controls

The Anguilla draft's publication review identified incorrect GST registration references and conflicting consumer instructions. This batch corrects those references, source and period checks, fork provenance and document requests. It does not establish a complete current-law chain or professional sign-off.

## Statutory references checked

I checked physical pages 18 to 20, printed pages 47 to 49, of the [General Services Tax Act 2025](https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf). The captured PDF has SHA-256 `28322c5fe3bd8264911edfbf8ff6c7ce0b77216beb0949227fb376f8d043fc04`. Fresh offline OCR and all three page images support these corrections:

- Ordinary actual-test and expected-test effective dates are in sections 11(4)(a) and 11(4)(b).
- Section 11(3) allows the Comptroller to register a person who failed to apply from the date determined by the Comptroller. The guide no longer describes an unrestricted retrospective power.
- Section 10(2) addresses related persons or persons acting in concert. Section 10(3) values supplies under section 15.
- Section 10(4) requires the Comptroller to be satisfied about the cessation or capital-replacement condition.
- Sections 10(6), (7) and (8) cover State/statutory bodies, auctioneers and accommodation providers.

The guide remains a dated enacted-2025 reference. The XCD 300,000 equality rule and its numerical illustrations are retained. Later amendments, specialised classifications, rounding and authority notices still require applicable sources before an engagement calculation.

## Consumer instructions

The MCP full-guide and section responses, five calculation prompts, `start`, server instructions and shared workflow now require the requested period, guide scope, operative primary law and guide-specific source conditions before an engagement calculation. Unknown law requires Needs Input or the guide's refusal. A factual default must be expressly permitted by the guide under established law; it cannot replace missing legal authority. Dated reference explanations and labelled hypothetical examples remain usable within their assumptions.

Full and section responses expose the source year as an integer or null and source notes as a string. The fields describe coverage, not legal currency, and are absent from list/search summaries. The retrieval footer identifies the configured package catalogue and recorded review status. It no longer claims that fetching a reference performed a calculation or that an upstream webpage supplies the loaded fork revision.

The compressed foundation and generated intake/README requests require relevant redacted records. Users can provide invoices without bank statements. Transaction dates, amounts, tax charged and necessary accounting facts are retained; bank/account identifiers, tax file numbers, credentials, actual identity documents and unrelated personal details must be excluded.

## Provenance boundary

The canonical referral block identifies this fork and labels upstream links as optional separate services. Only the two Anguilla guides and the substantively edited shared `workflow-base` are restamped in this batch. A source-path inventory still finds 1,871 Markdown files containing the legacy always-current claim. That wider migration remains unfinished; this batch does not clear the catalogue's provenance claims.

GST version 0.2 and monthly USL version 0.3 remain Tier 2 with pending review. The USL substantive rules still use the unofficial consolidation as at 31 December 2022 and require applicable official law or authoritative confirmation before an engagement calculation. The package's other tax topics remain partial or missing.

## Verification and limits

The new contract checks failed on the preceding implementation and passed after the repair: 29 MCP tool tests and 24 package-generator tests. They check delivered instructions, schema types, review metadata and generated document requests. All four generators ran successfully; the three tracked files in the protected hand-authored `packages/us-federal` retained their hashes. Counts remain 1,889 guides, 245 jurisdiction labels, 164 accountant-reviewed guides and 22 named accountants.

All fourteen repository checks passed on the first repaired revision. The root suite ran 391 tests: 382 passed and nine were skipped, comprising eight Makefile tests because `make` is unavailable and one Windows short-path test because the filesystem has no distinct alias. The MCP suite passed 95 tests and the documentation suite passed five. Existing arithmetic, bracket, expired-rule, fact-conflict and sourcing queues remain unresolved; these checks found no new findings. Independent review then found two surviving workflow claims about legal currency and upstream verification, plus an inconsistent version heading. This follow-up corrects those passages and related documentation; affected checks and a fresh independent financial final are required for the resulting revision. Live client refusal adherence, taxpayer outputs, current-law completeness and professional sign-off remain unverified. Aikido is unavailable under the recorded tool/authentication blocker. The previously denied Anguilla HTML privacy packet and workbook extraction are excluded without retry or an equivalent scan.
