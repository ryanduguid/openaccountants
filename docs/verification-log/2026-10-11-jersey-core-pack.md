# Jersey: first sourced tax-topic pack

I added ten Jersey guides covering personal and corporate tax, GST and imports, payroll, social contributions, Pillar Two scope, company reporting, cross-border collection, property transactions and crypto classification. Each is a source-cited draft, `tier: 2`, with `pending_review`. This is the first Jersey pack in the fork; it is incomplete and has no named professional sign-off.

## Evidence and period

The [source register and coverage gaps](../../skills/international/jersey/references.md) record 35 successful, untruncated primary captures used by the guides, their source URLs and captured-text SHA-256 hashes. I read the relevant guidance sections and statutory provisions on 11 October 2026. Capture success does not establish that every provision of a page or law was audited.

The current Income Tax and company substance laws apply from 17 June 2026, the Companies Law from 30 September 2026 and the Stamp Duties Law from 1 January 2026. The guides label their annual numerical schedules 2026 and require point-in-time verification for earlier events. The personal return page offers the 2025 assessment return in the 2026 filing cycle; its current deadlines are not presented as a verified future-year timetable.

## Material decisions

The personal tax example compares the standard and marginal amounts and takes the lower result. It assumes the basic threshold only, with no credits, specialist reliefs or assessment rounding.

The corporate retailer example follows Income Tax Law Article 123L: compute tax as the difference between 20% of the relevant profit and 40% of its shortfall from the upper threshold, then derive the effective rate. This prevents a wrong result from interpolating the headline rate. Associated-company and period-length adjustments are identified separately.

Articles 120AB and 120AC qualify the generic company page's statement that every incorporated company must file an ordinary annual tax return. I checked the relevant MNE group definition, ordinary-tax exemption, part-year apportionment and disapplication of specified returns. The corporate, formation and Pillar Two guides require that classification before giving a return instruction. Registry and accounting obligations remain separate.

The employer schedule and Social Security Law support a 2.5% upper-band secondary contribution. The generic migration page says 2%; its conflicting figure is retained in the source register and is not used in the 2026 guide. ITIS includes long-term care, while employee Class 1 and employer secondary contributions are separate. The examples keep those amounts distinct.

The import de minimis is limited to qualifying personal goods from an unregistered retailer. The guides exclude business imports and distinguish GST already collected by an overseas retailer. Capital and inheritance tax descriptions do not erase stamp duty, LTT, EPTT or probate charges. Non-resident dividend conditions follow Article 118B, rather than a broader generic summary.

## Verification and limits

I recomputed the published examples using exact arithmetic and synthetic inputs: personal tax branches, retail boundaries and an equivalent tax expression, monthly contribution thresholds and caps, payroll deductions, domestic GST, landlord collection and both LTT examples. Four additional eligibility checks use exact fractions and integer comparisons for short, long, annual and unequal associated-retailer periods. The local receipt records 22 calculation groups. These checks verify the stated arithmetic and assumptions; they do not establish operational rounding or tax classification for a real taxpayer.

The plan consultation was recovered without a duplicate submission after a message-confirmation error. Its full answer was read, with independently recorded GPT-6 / Extra High picker evidence after Pro was unavailable. The source snapshot was reverified before accepting the answer. It recommended a sourced core with explicit gaps and no comprehensive-pack claim. The final publication review and repository gates are recorded with the PR.

Generated package intake and README templates asked for 2025 documents even when the source guide covered 2026. I changed the universal templates to request the user's tax or accounting period and removed the repeated qualification in the default professional-review disclaimer. The independent review also required the retail eligibility period adjustment, an accurate distinction between part-year residence and non-residence, and replacement of the generic website-verification claim. Those repairs preserve the intake's full-year personalised-preparation limit and explain access to specialist reference guides. The package trees were regenerated; Aikido was unavailable for the changed Python files.

Detailed Pillar Two mechanics, full relief and payment rules, Class 2 and long-term care assessment, non-monthly payroll, GST special regimes, formation fees, regulated reporting, treaty-specific benefits, transfer pricing, full property/probate schedules, parish rates and emerging crypto treatment remain outstanding. Passing repository checks or merging this batch does not close those gaps or confer professional review.
