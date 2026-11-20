---
name: tk-eez-fishing-licence-fees-reference
description: >
  Tokelau exclusive economic zone fishing fee reference for the selected
  licence, vessel day, access-charge and regional agreement branches.
jurisdiction: TK
category: international
tax_year: 2023
tax_year_notes: "Selected rules in the official consolidation as at 21 September 2023, including the 28 March 2019 vessel day amendments. Recheck the requested period and vessel-specific instruments."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Tokelau EEZ fishing licence fees and access charges

Load `workflow-base`. Identify the vessel, licence issuer, gear and fishing activity, dates, area and any regional arrangement. This reference covers selected charges for foreign fishing craft in Tokelau’s exclusive economic zone (EEZ). Confirm the authorisation, paid access and vessel conditions before using the fee calculation. [Tokelau (Exclusive Economic Zone) Fishing Regulations 2012, regs 3 and 6–8](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html)

## Identify the licence branch

| Administrator licence | Fee on grant or renewal | Separate access requirements |
| --- | ---: | --- |
| Purse seine under regulation 16 | USD 7,500 to the Administrator | Fishing requires available vessel days. |
| Longline under regulation 20C | USD 5,000 to the Administrator | Fishing requires available vessel days. |
| General fishing vessel under regulation 21 | USD 5,000 to the Administrator | Fishing requires paid access for the period and compliance with the licence’s limits. |

The Administrator may refuse to grant the licence until its fee is paid. The longline licensing branch was inserted on 28 March 2019. Regulation 20C requires registration on the Longline Vessel Day Scheme register before a longline licence may be granted. The figures above come from the version as at 21 September 2023. [Regulations 17–18](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html#DLM4757007) · [Regulation 20C](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html#LMS178003) · [Regulations 20D–20E](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html#LMS178004) · [Regulations 21–23](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html#DLM4757009)

## Confirm the access amount

The Administrator’s strategies under regulations 20 and 20G provide for minimum vessel-day purchase pricing and conditions, which can vary with the purchase, and separately set buy-back terms. For general fishing vessels, regulation 25 permits the Administrator to set the periods and amounts of access charges. These can vary with time, circumstances or the vessel. Obtain the tariff, approvals, stated units and dates before calculating either amount. [Regulations 20 and 20G](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html) · [Regulation 25](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html#DLM4756646)

If an issuing agency notifies the Administrator of a qualifying regional fishery licence, regulation 27 treats it as a licence under the regulations for its validity period. Any EEZ access fee required by the licence or the governing agreement is payable by the owner to the Administrator under regulation 29. Verify the licence terms and agreement before recording the fee. Regulation 29A provides for forfeiture of that fee if the issuer cancels on a request under that regulation. [Regulations 27–29A](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html#DLM4756609)

## Fictional fees on separate vessels

Assume a purse seine licence is renewed under regulation 12 and a separate longline licence is granted under regulation 20C. On the stipulated statutory rules the fixed fees are USD 7,500 and USD 5,000, totalling USD 12,500. Confirm each vessel’s separate access entitlement and charges. [Regulations 17 and 20D](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html)

```oa-check
name: Tokelau fixed fees for one purse seine renewal and one longline grant
inputs:
  purse_seine_renewal: 7500
  longline_grant: 5000
steps:
  - fixed_licence_fees: purse_seine_renewal + longline_grant
expected:
  fixed_licence_fees: 12500
```

### General fishing vessel and separate access

Assume a different foreign fishing craft holds a general fishing licence under regulation 21. A renewal under regulation 12 attracts USD 5,000 under regulation 22. Assume a separate documented USD 1,800 access charge for the selected period under regulation 25. The fictional payments total USD 6,800. Confirm the actual access amount and terms for the vessel and period. [Regulations 12, 21–22 and 25](https://www.legislation.govt.nz/regulation/public/2012/0278/latest/whole.html)

```oa-check
name: Tokelau general fishing renewal and stipulated access charge
inputs:
  renewal_fee: 5000
  documented_access_charge: 1800
steps:
  - total_payments: renewal_fee + documented_access_charge
expected:
  total_payments: 6800
```

## Remaining coverage

Verify the period’s amendments, applicable Administrator strategy and charges, agreement, vessel classification, monitoring, payment channels and practitioner review. Reconcile purchases, days used, refunds and any operator or owner obligations against the actual licence and account records. The fees in this reference do not determine income tax treatment or a deduction.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
