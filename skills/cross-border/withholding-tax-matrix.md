---
name: withholding-tax-matrix
description: Use this skill whenever a freelancer or small business receives or makes a cross-border payment and the question is whether withholding tax (WHT) applies. Trigger on phrases like "withholding tax", "WHT", "tax withheld", "double tax treaty", "treaty rate", "certificate of residence", "tax residency certificate", "form W-8BEN", "royalty withholding", "interest withholding", "TDS on services", or any request involving tax deducted at source on cross-border payments for services, royalties, or interest. This skill contains the withholding tax matrix for the top 30 country pairs, treaty rate lookups, certificate of residence requirements, and zero-WHT corridors. ALWAYS read this skill before advising on any cross-border withholding tax question.
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-09-29
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Withholding Tax Matrix

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Multi-jurisdiction (30 countries) |
| Primary Legislation | OECD Model Tax Convention on Income and on Capital; bilateral double taxation agreements |
| Scope | WHT on services (technical/professional fees), royalties (including software licences), and interest payments between freelancers and their clients across borders |
| Countries Covered | US, UK, DE, FR, IT, ES, NL, MT, AU, CA, IN, SG, JP, KR, AE, SA, BR, MX, IE, PT, CH, SE, DK, NO, AT, BE, PL, NZ, ZA, IL |
| Contributor | OpenAccountants |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: treaty rate lookups for covered country pairs, zero-WHT corridors. Tier 2: beneficial ownership, treaty eligibility, PE risk interaction. Tier 3: treaty shopping, LOB clauses, complex corporate structures. |

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a qualified tax professional.

## Step 0: Pre-Check Questions [T1]

- **Pre-check questions before using WHT matrix** — Before using the WHT matrix, you MUST know: 1. Where is the payer (client) tax-resident? This determines the source country and whose domestic WHT law applies. 2. Where is the payee (freelancer) tax-resident? This determines which treaty (if any) applies. 3. What is the nature of the payment? Services (technical/professional/management fees), royalties (software licences, IP), or interest. 4. Does a double tax treaty (DTA) exist between the two countries? If yes, treaty rates may reduce or eliminate WHT. 5. Has the payee obtained a Certificate of Tax Residence (CoR) from their home country? Required to claim treaty benefits. 6. Is there a risk of Permanent Establishment (PE) in the source country? If PE exists, different rules apply (see `permanent-establishment-risk.md`). ([T1])
- **Stop condition on unknown pre-check items** — If items 1-3 are unknown, STOP. Do not provide WHT guidance. ([T1])

## Step 1: Key Concepts [T1]

- **Domestic WHT Rate** — The rate a country charges by default on cross-border payments when no treaty applies. This is the "worst case" rate. ([T1])
- **Treaty WHT Rate** — The reduced rate available under a bilateral double tax treaty between the payer's and payee's countries. Requires the payee to claim treaty benefits (usually by providing a Certificate of Residence and/or specific forms). ([T1])
- **Zero-WHT Corridor** — A country pair where the treaty rate on a specific payment type is 0%. The payee receives the full gross amount with no deduction. ([T1])
- **Technical/Professional Services** — Fees for consulting, IT development, accounting, legal, engineering, management, and similar professional services. Some countries (notably India, Brazil) impose WHT on services; many developed countries do not. ([T1])
- **Royalties** — Payments for the use of intellectual property, patents, trademarks, copyrights, and importantly: software licences. The classification of software licence fees as "royalties" vs "business profits" is heavily disputed and varies by treaty. ([T1])
- **Interest** — Payments for the use of money (loans, deposits, deferred payment arrangements). ([T1])

## Step 2: WHT Matrix -- Professional/Technical Services [T1]

**How to read:** If your client is in [Source Country] and you (the freelancer) are in [Residence Country], the WHT rate on professional services is shown at the intersection.

**Important:** Many developed countries do NOT withhold on service fees (indicated by "0/None" below). Countries that DO impose domestic WHT on services include India (20% on fees for technical services under s 115A, before treaty relief), Brazil (15-25%), South Africa (15% for management fees), and Korea (22% for certain services).

**WHT Matrix -- Professional/Technical Services**

| Source → | US | UK | DE | FR | IT | ES | NL | MT | IN | SG | AU | CA | JP | AE | CH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Payee ↓** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| US | -- | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| UK | 0 | -- | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| DE | 0 | 0 | -- | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| FR | 0 | 0 | 0 | -- | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| MT | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -- | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| AU | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | -- | 0 | 0 | 0 | 0 |
| IN | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -- | 0 | 0 | 0 | 0 | 0 | 0 |
| BR | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| SG | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | -- | 0 | 0 | 0 | 0 | 0 |
| ZA | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 |

**Notes:**
- **US, UK, DE, FR, NL, CH, SG, AU, CA, JP, AE** generally do NOT impose WHT on service fees under their domestic law. Treaty irrelevant for this payment type.
- The zeros in those columns assume the work is performed outside the source country. Several of them withhold on services performed on their territory by a non-resident (Canada 15% under Regulation 105, Japan 20.42%, Spain 24% under the IRNR, Italy 30% under art. 25 DPR 600/1973, the US 30% on US-source personal-services income unless a treaty exemption is claimed on Form 8233), and the treaty's independent-personal-services or business-profits article then decides. A payee row is never the source: an Indian or Brazilian freelancer paid by a client in one of those countries suffers no withholding there.
- **India** taxes fees for technical services paid to non-residents at 20% under s 115A(1)(b) of the Income-tax Act 1961 (Finance Act 2023; 10% before 1 April 2023), plus surcharge and the 4% cess, withheld under s 195. A treaty rate applies on a Tax Residency Certificate and Form 10F: 10% under the German, French, Maltese, Singaporean and South African treaties; 15% under the UK and US treaties (India–UK DTA Art. 13(2)(a); India–US DTA Art. 12(2)(a)), whose 10% is only for services ancillary to equipment rental.
- **Brazil** imposes 15% (general) or 25% (tax haven list) WHT on service fees (IRRF). Treaties may not eliminate this entirely.
- **AE (UAE) and SA (Saudi Arabia)** have 0% income tax (UAE) or 0% on non-resident services (Saudi, if no PE). Treaty is irrelevant for UAE.
- **Korea** imposes 22% WHT on certain personal services but many treaties reduce to 0% for independent personal services without a fixed base.

## Step 3: WHT Matrix -- Royalties (Including Software Licences) [T1]

**WHT Matrix -- Royalties (Including Software Licences)**

| Source → | US | UK | DE | FR | IT | ES | NL | MT | IN | SG | AU | CA | JP | AE | CH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Payee ↓** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| US | -- | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 15 | 0 | 5 | 0 | 0 | 0 | 0 |
| UK | 0 | -- | 0 | 0 | 5 | 0 | 0 | 0 | 15 | 8 | 5 | 0 | 0 | 0 | 0 |
| DE | 0 | 0 | -- | 0 | 5 | 0 | 0 | 0 | 10 | 0 | 5 | 0 | 0 | 0 | 0 |
| FR | 0 | 0 | 0 | -- | 5 | 0 | 0 | 0 | 10 | 0 | 5 | 0 | 0 | 0 | 0 |
| MT | 10 | 10 | 0 | 0 | 0 | 5 | 0 | -- | 10 | 0 | 10 | 0 | 10 | 0 | 0 |
| IN | 15 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | -- | 10 | 10 | 10 | 10 | 10 | 10 |
| SG | 30 | 8 | 0 | 0 | 5 | 5 | 0 | 0 | 10 | -- | 10 | 0 | 0 | 0 | 0 |
| AU | 5 | 5 | 5 | 5 | 10 | 5 | 5 | 10 | 10 | 10 | -- | 10 | 5 | 0 | 5 |
| BR | 30 | 15 | 15 | 15 | 15 | 10 | 15 | 15 | 15 | 15 | 15 | 15 | 12.5 | 15 | 10 |
| JP | 0 | 0 | 0 | 0 | 10 | 10 | 0 | 10 | 10 | 0 | 5 | 10 | -- | 0 | 0 |

**Notes:**
- **Intra-EU royalties** are generally 0% under the EU Interest and Royalties Directive (2003/49/EC) for associated companies. This does NOT automatically apply to unrelated freelancers -- the directive requires a 25% shareholding relationship.
- **US domestic WHT on royalties** is 30% (IRC §§ 871(a) and 881(a)), reduced by treaty on Form W-8BEN. The US has no income tax treaty with Singapore or Brazil, so the 30% stands for those payees; the US–Malta DTA (2008) Art. 12 gives 10%; the US–Spain DTA as amended by the 2013 Protocol (in force 27 November 2019) gives 0%.
- **UK–Singapore and UK–Malta.** The UK withholds 20% on royalties (ITA 2007 s 906) and on yearly interest (s 874); the UK–Singapore DTA (1997) as amended by the 2012 Protocol reduces royalties to 8% (Art. 12) and interest to 5% (Art. 11), and the UK–Malta DTA (1994) reduces both to 10% (Arts. 11 and 12). Malta itself exempts royalties and interest paid to non-residents (Income Tax Act art. 12(1)(c)), and Singapore's domestic 10% on royalties (ITA 1947 s 45A) falls to 8% for a UK payee. The Australia–Singapore DTA (1969, as amended) Art. 10 leaves royalties at 10% in both directions.
- **India** taxes royalties and fees for technical services paid to non-residents at 20% under s 115A(1)(b) (Finance Act 2023; 10% before 1 April 2023), plus surcharge and the 4% cess, and s 206AA applies 20% where the payee has no PAN. Treaties cap it at 10% (Germany, France, Malta, Singapore, South Africa) or 15% (UK Art. 13(2)(a); US Art. 12(2)(a); 10% for equipment royalties under both) on a TRC and Form 10F.
- **Software licences:** Many countries dispute whether a software licence fee is a "royalty" (subject to WHT) or "business profits" (no WHT without PE). OECD position: payment for a software copy for personal use = business profits (no WHT). Payment for the right to reproduce/distribute = royalty (WHT may apply). [T2]

## Step 4: WHT Matrix -- Interest [T1]

**WHT Matrix -- Interest**

| Source → | US | UK | DE | FR | NL | MT | IN | SG | AU | CA | JP | CH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Payee ↓** |  |  |  |  |  |  |  |  |  |  |  |  |
| US | -- | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 10 | 0 | 0 | 0 |
| UK | 0 | -- | 0 | 0 | 0 | 0 | 15 | 5 | 10 | 10 | 10 | 0 |
| DE | 0 | 0 | -- | 0 | 0 | 0 | 10 | 0 | 10 | 10 | 10 | 0 |
| FR | 0 | 0 | 0 | -- | 0 | 0 | 10 | 0 | 10 | 10 | 10 | 0 |
| MT | 10 | 10 | 0 | 0 | 0 | -- | 10 | 0 | 10 | 10 | 10 | 0 |
| IN | 15 | 15 | 0 | 0 | 0 | 0 | -- | 15 | 15 | 15 | 10 | 0 |
| SG | 30 | 5 | 0 | 0 | 0 | 0 | 15 | -- | 10 | 10 | 10 | 0 |
| AU | 10 | 10 | 0 | 0 | 0 | 0 | 15 | 10 | -- | 10 | 10 | 0 |

**Notes:**
- **US domestic WHT on interest** is 30% (no treaty), before the portfolio-interest exemption of IRC §§ 871(h) and 881(c), which takes most interest on registered debt held by an unrelated non-bank lender out of withholding altogether. Treaty rates range from 0% (UK, DE, FR, NL; Canada since the Fifth Protocol, in force 15 December 2008; Japan since the 2013 Protocol, in force 30 August 2019; Spain since the 2013 Protocol, in force 27 November 2019) to 15% (India, Art. 11(2)(b) of the India–US DTA; 10% for bank loans). No treaty covers Singapore or Brazil, so the 30% stands unless the portfolio-interest exemption applies; the US–Malta DTA gives 10% (Art. 11).
- **DE, FR, NL, CH and MT** withhold nothing on ordinary loan interest paid to a non-resident (Germany only on profit-linked or convertible instruments, France only to non-cooperative states, the Netherlands only under the 2021 conditional withholding tax on payments to low-tax jurisdictions, Switzerland only on bank deposits and bonds, Malta not at all under Income Tax Act art. 12(1)(c)), so a treaty rate above zero in those columns never bites.
- **India** withholds under s 195 at the rates in force (20% plus surcharge and cess under s 115A(1)(a) for foreign-currency loans; more for rupee loans); the treaties cap it at 15% (UK Art. 12, US Art. 11, Singapore Art. 11, Australia Art. 11; 10% for bank lenders) or 10% (Germany, France, Netherlands, Malta, Japan, Switzerland). Singapore's domestic 15% (ITA 1947 s 45) falls to 5% for a UK lender under Art. 11 of the UK–Singapore DTA.
- **Intra-EU interest** is generally 0% under the EU Interest and Royalties Directive for associated companies (same 25% shareholding requirement as royalties).
- **UK** abolished domestic WHT on interest for most payments. Treaty rarely needed.
- **AE and SA** have 0% income tax, so no WHT on interest.

## Step 5: How to Claim Treaty Benefits [T1]

### General Process

- **General process to claim treaty benefits** — 1. Obtain a Certificate of Tax Residence (CoR) from your home country's tax authority. This proves you are tax-resident and entitled to treaty benefits. 2. Provide the CoR to the payer before or at the time of payment. Many countries accept CoR for the current or preceding tax year. 3. Complete any required forms specific to the source country (see table below). 4. The payer applies the treaty rate (or 0%) instead of the domestic rate. 5. If WHT is already deducted at the higher domestic rate, the payee can file a refund claim with the source country's tax authority.

### Country-Specific Forms [T1]

**Country-Specific Forms**

| Source Country | Form Required | Purpose |
| --- | --- | --- |
| US | W-8BEN (individuals) / W-8BEN-E (entities) | Claim treaty benefits on US-source income |
| UK | None typically required for services; DT-Individual for other income types | Treaty claim |
| DE | No standard form for services; Freistellungsantrag for royalties/interest | Application for exemption from WHT |
| IN | Form 10F + CoR + Tax Residency Certificate (TRC) | Claim treaty rate under Section 90 |
| AU | No standard form; CoR from home country sufficient for treaty claim | Treaty claim |
| CA | NR301 (individuals) / NR302 (entities) | Declaration of eligibility for benefits under a tax treaty |
| JP | Application for Income Tax Convention (Form 1-7 depending on type) | Treaty claim, submitted via payer to tax office |
| BR | No standard form; CoR + apostille or consular certification required | Treaty claim (limited treaty network) |
| KR | Application for Non-Resident WHT Exemption | Treaty claim via payer's withholding agent |

## Step 6: Zero-WHT Corridors [T1]

The following country pairs have 0% WHT on professional/technical services under treaty (or because domestic law does not impose WHT on services):

**Zero-WHT Corridors**

| Corridor | WHT on Services | WHT on Royalties | WHT on Interest |
| --- | --- | --- | --- |
| US ↔ UK | 0% | 0% | 0% |
| US ↔ DE | 0% | 0% | 0% |
| US ↔ NL | 0% | 0% | 0% |
| UK ↔ DE | 0% | 0% | 0% |
| UK ↔ FR | 0% | 0% | 0% |
| UK ↔ NL | 0% | 0% | 0% |
| DE ↔ FR | 0% | 0% | 0% |
| DE ↔ NL | 0% | 0% | 0% |
| SG ↔ UK | 0% | 8% | 5% |
| SG ↔ NL | 0% | 0% | 0% |
| MT ↔ UK | 0% | 0% from Malta, 10% from the UK | 0% from Malta, 10% from the UK |
| MT ↔ DE | 0% | 0% | 0% |
| CH ↔ UK | 0% | 0% | 0% |
| AE ↔ (any) | 0% (no income tax) | 0% | 0% |
| IE ↔ UK | 0% | 0% | 0% |

**The "golden corridors" for freelancers:** US-UK, US-DE, UK-DE, UK-NL. These pairs have zero WHT on all three categories. SG-UK and MT-UK are zero on services only: the UK–Singapore treaty leaves 8% on royalties and 5% on interest, and the UK–Malta treaty 10% on both when the UK is the source.

## Step 7: Practical Guidance for Freelancers [T1]

### If your client is in [country] and you are in [country]:

- **Client in US, you in UK:** 0% WHT on services. No form required for services (W-8BEN for royalties/interest). You receive 100% of the invoice.
- **Client in US, you in India:** 0% WHT when the work is performed outside the US: the fee is foreign-source income outside Chapter 3 withholding (IRC § 861(a)(3); Treas. Reg. § 1.1441-4(a)), so give the client Form W-8BEN to document foreign status and invoice 100%. Work performed in the US is US-source: 30% withholding unless Form 8233 claims Art. 15 of the India–US DTA (independent personal services: no fixed base and under 90 days in the US).
- **Client in India, you in UK:** 15% WHT on fees for technical services (India–UK DTA Art. 13(2)(a); the domestic rate is 20% plus surcharge and cess under s 115A, withheld under s 195). Provide Form 10F + UK CoR. You receive 85%; claim credit in UK via self-assessment.
- **Client in India, you in US:** 15% WHT on fees for included services (India–US DTA Art. 12(2)(a)). Provide Form 10F + US CoR. You receive 85%; claim foreign tax credit on Form 1116.
- **Client in Germany, you in Malta:** 0% WHT on services (Germany does not impose WHT on service fees). You receive 100%.
- **Client in Brazil, you in any country:** 15% IRRF on service fees (25% if payee is in a "tax haven"). Limited treaty network. You receive 85%; claim credit in home country.
- **Client in UAE, you in any country:** 0% (UAE has no income tax). You receive 100%.
- **Client in Singapore, you in India:** 10% WHT likely on technical services under India-SG treaty if service performed from India; 0% if performed entirely from Singapore and paid there.

## PROHIBITIONS

- **Prohibitions list** — 1. NEVER assume a treaty exists between two countries without verifying. 2. NEVER apply treaty rates without the payee having a valid Certificate of Tax Residence. 3. NEVER advise a client that WHT "doesn't apply" when the source country's domestic law imposes WHT -- the treaty merely reduces the rate, and treaty benefits must be claimed. 4. NEVER ignore the distinction between "business profits" (Art 7, usually no WHT without PE) and "royalties" (Art 12, WHT may apply) when classifying software licence payments. 5. NEVER assume that paying WHT in the source country eliminates the tax obligation in the residence country -- the residence country taxes worldwide income and provides a credit for WHT paid. 6. NEVER provide specific treaty rate advice for country pairs not covered in this matrix -- escalate [T3].

## Edge Cases

### EC1 -- Treaty shopping / Limitation on Benefits (LOB) [T3]

**Situation:** A freelancer is tax-resident in Country A but channels payments through an entity in Country B (which has a more favourable treaty with the source country) to reduce WHT.
**Resolution:** This is treaty shopping. Many modern treaties (especially US treaties) contain LOB clauses that deny treaty benefits if the recipient is not the "beneficial owner" or does not meet the LOB test. Escalate to tax professional. Do not advise.

### EC2 -- Permanent Establishment risk [T2]

**Situation:** A freelancer from Country A works on-site in Country B for extended periods. The client in Country B asks whether WHT applies.
**Resolution:** If the freelancer has created a PE in Country B (see `permanent-establishment-risk.md`), the income may be taxed as business profits attributable to the PE, not as service fees subject to WHT. PE taxation and WHT are mutually exclusive for the same income. Flag for professional review.

### EC3 -- Beneficial ownership challenged [T2]

**Situation:** A freelancer invoices through a personal services company in a different country. The source country challenges the treaty claim on the basis that the company is not the "beneficial owner" of the income.
**Resolution:** Beneficial ownership requires that the recipient has the right to use and enjoy the income, not merely act as a conduit. If the personal services company is a genuine entity with substance, treaty benefits should apply. If it is a shell, they may be denied. Flag for professional review.

### EC4 -- WHT on software-as-a-service (SaaS) subscriptions [T2]

**Situation:** A freelancer pays for a SaaS tool (e.g., cloud software) from a foreign provider. The domestic tax authority of the freelancer's country considers this a "royalty" and requires WHT.
**Resolution:** The OECD position is that payments for standard SaaS subscriptions (no transfer of copyright, no reproduction rights) are business profits, NOT royalties. However, India (Explanation 4 to Section 9(1)(vi)) and some other countries treat SaaS payments as royalties subject to WHT. Check the source country's domestic law position. Flag T2.

### EC5 -- No treaty exists between the two countries [T1]

**Situation:** A freelancer in Country A receives payment from a client in Country B, but no bilateral tax treaty exists.
**Resolution:** The domestic WHT rate of the source country applies in full. No reduction available. The freelancer claims a foreign tax credit in their home country (subject to that country's credit rules). If the domestic rate exceeds the home country's credit capacity, the excess WHT is a real cost.

## Test Suite

### Test 1 -- US client, UK freelancer, consulting services

**Input:** US company pays GBP 10,000 to UK freelancer for software consulting.
**Expected:** 0% WHT. US does not impose domestic WHT on service fees. No W-8BEN needed for service fees (only for royalties/interest/dividends). UK freelancer receives 100%.

### Test 2 -- Indian client, Maltese freelancer, technical services

**Input:** Indian company pays EUR 5,000 to Maltese freelancer for software development.
**Expected:** India domestic WHT on technical services = 10% (with PAN). India-Malta DTA rate on fees for technical services = 10%. WHT = EUR 500. Maltese freelancer receives EUR 4,500. Claims EUR 500 credit on Malta tax return.

### Test 3 -- Brazilian client, German freelancer, management consulting

**Input:** Brazilian company pays EUR 20,000 to German freelancer for management consulting.
**Expected:** Brazil domestic WHT (IRRF) = 15% on service fees. Brazil-Germany DTA may not eliminate services WHT. WHT = EUR 3,000. German freelancer receives EUR 17,000. Claims credit in Germany.

### Test 4 -- UAE client, any freelancer

**Input:** UAE company pays USD 15,000 to a French freelancer for design services.
**Expected:** 0% WHT. UAE has no income tax. French freelancer receives 100%. France taxes the income as part of worldwide income.

### Test 5 -- US client, Indian freelancer, software royalty

**Input:** US company pays USD 50,000 to Indian company for software licence (reproduction rights).
**Expected:** US domestic WHT on royalties = 30%. US-India treaty rate = 15% (royalties). Indian company provides W-8BEN-E. WHT = USD 7,500. Indian company receives USD 42,500. Claims credit in India.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. Treaty rates are subject to change through protocol amendments and renegotiations. Always verify current treaty text before relying on any rate. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

If you would like a licensed accountant to review your cross-border tax position, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.

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
