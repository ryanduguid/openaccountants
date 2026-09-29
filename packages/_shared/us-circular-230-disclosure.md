---
name: us-circular-230-disclosure
description: "Scope-neutral Circular 230 disclosure that every US guide in this library carries by dependency. States that the US guides are reference material and drafting aids for a credentialed practitioner (Enrolled Agent, CPA or attorney admitted to practice before the IRS), that they are not tax advice to any taxpayer and not a reliance opinion for penalty protection, and that a practitioner who gives written advice or signs a return with their help stays bound by Treasury Department Circular No. 230 sections 10.22, 10.34 and 10.37. It carries no workflow, intake, refusal catalogue or tax figures, so it loads beside a US guide on any subject: individual, business, payroll, corporate, partnership, estate, international or state. Trigger: loaded as a dependency of every US guide; read it when asked whether output built on a US guide is written advice, or whether it may go to a taxpayer or into a return."
version: 0.1
jurisdiction: US
category: foundation
last_updated: 2026-09-29
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Circular 230 Disclosure

## What this file is

Every guide whose jurisdiction is `US` or `US-<state>` names this file in `depends_on`, so a reader that loads any US guide loads the disclosure below with it. The file is deliberately narrow. It carries no workflow, no intake, no refusal catalogue and no tax figures, so it fits a guide on any US subject, whatever the taxpayer: an individual, a sole proprietor, a partnership, a corporation, an employer, an estate or a foreign-owned entity.

The sole-proprietor workflow (intake, working papers, the global refusal catalogue) lives in `us-tax-workflow-base`. Only the guides written for that workflow load it, because its refusals exclude the taxpayers other guides serve.

## The disclosure

> **Circular 230 disclosure.** The US guides in this library are reference material and drafting aids for a credentialed practitioner: an Enrolled Agent, a CPA or an attorney admitted to practice before the IRS. They are not tax advice to any taxpayer, and they are not a reliance opinion for penalty-protection purposes unless a guide says so expressly. A practitioner who gives written advice, or signs a return, with the help of a guide stays bound by Treasury Department Circular No. 230: due diligence as to accuracy (§10.22), the standards for tax returns and other documents (§10.34) and the requirements for written advice (§10.37). Reliance on the advice of others is reasonable only if it is in good faith and the practitioner knows of no reason it should not be relied on (§10.37(b)). A taxpayer must not use output built on a guide to avoid penalties without a practitioner's sign-off.

## How to use it

- **In output.** When output built on a US guide is addressed to a taxpayer, or may be used for a return, state the disclosure above or its substance in that output.
- **Guide-specific statements.** A guide that carries its own Circular 230 statement, such as the one in `us-form-1040-individual-return` or `us-section-1202-qsbs`, keeps it. That statement adds to this file for that guide, and where a guide asks for more, follow the guide.
- **What this file does not do.** It does not decide whether a given output is written advice within §10.37: the practitioner who issues the output decides that. It does not refuse any engagement.

## Sources

- Treasury Department Circular No. 230 (31 CFR Part 10), §10.22, Diligence as to accuracy — https://www.ecfr.gov/current/title-31/section-10.22.
- §10.34, Standards with respect to tax returns and documents, affidavits and other papers — https://www.ecfr.gov/current/title-31/section-10.34.
- §10.37, Requirements for written advice — https://www.ecfr.gov/current/title-31/section-10.37.

## Provenance

Written on 2026-09-29 from the eCFR text of §§10.22, 10.34 and 10.37 (current through 2026-09-25) and from the two Circular 230 statements already in the library, in `us-section-1202-qsbs` and in section 20.3 of `us-form-1040-individual-return`. It has not been reviewed by a credentialed practitioner.

<!-- openaccountants-cta-block -->

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
