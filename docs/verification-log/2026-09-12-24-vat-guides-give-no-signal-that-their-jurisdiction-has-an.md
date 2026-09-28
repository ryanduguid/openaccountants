# 24 VAT guides give no signal that their jurisdiction has an e-invoicing regime

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The surviving question was sharper than "is it mentioned": most of these packs carry a
**dedicated `*-einvoice.md` guide**, so a VAT guide not duplicating it is sound
structure. The defect is only where the VAT guide gives the reader **no pointer at all**.

Measured across every pack that has both: **24 of 35 VAT guides, in 15 jurisdictions,
never mention e-invoicing in any form.** Seven packs already do it properly — China,
India, Indonesia, Mexico, Poland, Romania, Saudi Arabia — which is what makes the other
fifteen a defect rather than a design choice. **The repository already has the
convention; it is applied to a third of the packs that need it.**

The fifteen include Italy (SdI), Hungary (RTIR), Poland, Portugal, Spain, France,
Belgium, Greece and Germany — jurisdictions with hard mandates and penalties attached.

**What was fixed, and the line that was deliberately not crossed.** A pointer was added
to all 24, and it is *only* a pointer: it names the pack's own e-invoicing guide, says
this guide does not cover the subject, and states in terms that **no claim about that
jurisdiction's regime is made**. Writing fifteen jurisdiction-specific mandate
descriptions from one sitting would repeat precisely the error the Kuwait review caught
— carrying a clause into many files on the strength of a pattern rather than a reading.
The pointer is true in all 24 cases because it asserts only what the repository's own
file tree already shows.

Each carries an `<!-- einvoice-xref -->` marker so a later pass is idempotent — and,
per the CTA lesson recorded above, that marker is only good from the moment it exists.
