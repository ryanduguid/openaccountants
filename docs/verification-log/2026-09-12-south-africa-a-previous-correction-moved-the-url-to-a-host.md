# South Africa — a previous correction moved the URL to a host that does not exist

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The costliest hit was not a stale link. `za-income-tax.md` carried this, as a correction:

> *"Correct portal but URL is sarsefiling.gov.za / efiling.sars.gov.za. The
> www.sarsefiling.co.za address is the older registered domain that redirects, but for
> documentation use https://www.sarsefiling.gov.za or https://www.sars.gov.za."*

Every operative claim in it is backwards. **Neither `www.sarsefiling.gov.za` nor
`efiling.sars.gov.za` resolves at all.** `https://www.sarsefiling.co.za` answers 200,
redirects to `https://secure.sarsefiling.co.za/landing`, and serves a page titled **"SARS
eFiling"**. The redirect the note treats as evidence of retirement is the ordinary hop to
a login landing.

The shape matters more than South Africa. This was **a deliberate, reasoned correction**
— it named the alternative, explained why it was rejecting it, and told readers what to
use "for documentation". It was more confident than the row it replaced and more wrong,
and **no check in the repo could see it**, because every check assumed a citation's target
exists. Six files carried it (three guides, two `agent-skills` copies, and a duplicated
table row); all six now point at `www.sarsefiling.co.za`, and each says what it previously
said so the next reader can tell this was fixed rather than guessed at.

This is the third time on this branch that a correction has been the defect: Kuwait's
carried-along clause, North Macedonia's "eight heads" that was two short of the statute,
and now this. **A correction inherits the credibility of the sentence it sits in, and
raises it.** That is an argument for checking the replacement, not for correcting less.
