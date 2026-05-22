---
name: uk-capital-gains-sa108
description: >
  Use this skill whenever asked about UK capital gains tax for individuals. Trigger on phrases like "SA108", "capital gains tax", "CGT UK", "annual exempt amount", "disposal", "chargeable gain", "crypto CGT UK", "share sale UK", "property disposal CGT", "PPR relief", "principal private residence", "BADR", "Business Asset Disposal Relief", "Entrepreneurs' Relief", "bed and breakfasting", "30-day rule", "Section 104 pool", "negligible value claim", "CGT losses", "60-day reporting", "residential property CGT", or any question about computing, filing, or reporting capital gains on the UK Self Assessment return. Covers SA108 form, CGT rates, reliefs, crypto as CGT asset, share matching rules, property CGT reporting, and loss treatment. ALWAYS read this skill before touching any UK CGT work.
version: 1.0
jurisdiction: GB
tax_year: 2025
category: international
depends_on:
  - uk-income-tax-sa100
verified_by: pending
---

# UK Capital Gains Tax (SA108) Skill v1.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | United Kingdom |
| Tax | Capital Gains Tax (CGT) |
| Currency | GBP only |
| Tax year | 6 April to 5 April |
| Primary legislation | Taxation of Chargeable Gains Act 1992 (TCGA 1992) |
| Supporting legislation | Finance Act 2025 (rate changes); TCGA ss. 1H, 1I (rates); TCGA s. 222-226 (PPR); TCGA s. 169H-169S (BADR); TCGA ss. 104, 106A, 107 (share matching) |
| Tax authority | HMRC |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline | 31 January following the tax year (SA return); 60 days for UK residential property (CGT on UK Property return) |
| SA108 form | Capital Gains Tax Summary supplementary pages to SA100 |
| HMRC crypto guidance | HMRC CG12100+ (Cryptoassets Manual) |
| Validated by | Pending — requires sign-off by a UK chartered accountant or licensed tax adviser |
| Skill version | 1.0 |

### CGT Rates (2024-25)

Two rate regimes applied within 2024-25 due to the Autumn Budget 2024 (30 October 2024):

**6 April 2024 to 29 October 2024:**

| Asset type | Basic rate | Higher rate |
|---|---|---|
| Residential property | 18% | 24% |
| Other assets (shares, crypto, etc.) | 10% | 20% |
| BADR qualifying gains | 10% | 10% |

**30 October 2024 to 5 April 2025:**

| Asset type | Basic rate | Higher rate |
|---|---|---|
| All assets (residential and other) | 18% | 24% |
| BADR qualifying gains | 10% | 10% |

### CGT Rates (2025-26)

| Asset type | Basic rate | Higher rate |
|---|---|---|
| All assets | 18% | 24% |
| BADR qualifying gains | 14% | 14% |

### Annual Exempt Amount

| Tax year | Individuals | Trustees |
|---|---|---|
| 2024-25 | £3,000 | £1,500 |
| 2025-26 | £3,000 | £1,500 |
| 2023-24 | £6,000 | £3,000 |
| 2022-23 | £12,300 | £6,150 |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown acquisition cost | STOP — cannot compute gain |
| Unknown whether PPR applies | Do NOT apply PPR (taxable in full) |
| Unknown residency status | STOP — affects CGT liability |
| Unknown whether basic or higher rate | Compute at higher rate (conservative) |
| Unknown whether disposal is connected persons | Treat as connected (market value rule applies) |

---

## Section 2 -- Computation Framework

### 2.1 Basic CGT Calculation

```
Disposal proceeds (or market value if gift/connected person)
Less: Allowable costs
  - Original acquisition cost
  - Incidental acquisition costs (stamp duty, legal fees, survey)
  - Enhancement expenditure (capital improvements)
  - Incidental disposal costs (estate agent, legal, advertising)
= Chargeable gain (or allowable loss)

Less: Annual Exempt Amount (£3,000)
= Taxable gain

Tax = Taxable gain × applicable rate (based on income band)
```

### 2.2 Rate Band Allocation

CGT rates depend on where the gain falls relative to the basic rate band:

```
Unused basic rate band = £50,270 - taxable income (after personal allowance)

If gain fits within unused basic rate band → basic rate CGT
If gain exceeds unused basic rate band → split: basic rate on amount within band, higher rate on excess
```

---

## Section 3 -- Share Matching Rules (Section 104 Pool)

UK share disposals follow strict matching rules in this priority order:

| Priority | Rule | Reference |
|---|---|---|
| 1 | Same-day acquisitions | TCGA s. 105(1) |
| 2 | Acquisitions within 30 days AFTER disposal (bed and breakfasting rule) | TCGA s. 106A |
| 3 | Section 104 pool (average cost of all shares held) | TCGA s. 104 |

### 3.1 Section 104 Pool

The Section 104 pool is a rolling average cost of all shares of the same class in the same company:

```
Pool cost = total cost of all acquisitions
Pool quantity = total shares held
Average cost per share = Pool cost ÷ Pool quantity
```

On disposal: allowable cost = number of shares sold × average cost per share.

### 3.2 Bed and Breakfasting (30-Day Rule)

If you sell shares and repurchase the same shares within 30 days, the disposal is matched to the repurchase — NOT the Section 104 pool. This prevents crystallising a gain/loss while retaining the same economic position.

Applies to: shares, securities, crypto assets (per HMRC guidance CRYPTO22200).

---

## Section 4 -- Crypto Assets as CGT Assets

### 4.1 HMRC Position

HMRC treats cryptoassets as property for CGT purposes (not currency). Each disposal is a chargeable event.

| Event | CGT Treatment |
|---|---|
| Selling crypto for fiat (GBP, USD, etc.) | Disposal — gain/loss computed |
| Exchanging one crypto for another | Disposal of the first crypto |
| Using crypto to pay for goods/services | Disposal at market value |
| Gifting crypto | Disposal at market value |
| Transfer between own wallets | NOT a disposal |
| Receiving airdrop (no consideration given) | Acquisition at zero cost |
| Mining/staking rewards | Income when received; acquisition cost = income value |
| DeFi lending | Depends on terms — may or may not be disposal |

### 4.2 Crypto Matching Rules

Same as share matching rules: same-day → 30-day → Section 104 pool. Each crypto token type has its own pool (e.g. separate pools for BTC, ETH, SOL).

### 4.3 Crypto Reporting on SA108

From 2024-25, SA108 includes dedicated crypto boxes:
- Box 5.9A: Cryptoasset gains included in total gains
- Box 5.10A: Cryptoasset losses included in total losses

---

## Section 5 -- Principal Private Residence (PPR) Relief

### 5.1 Full PPR Relief

If a property has been your only or main residence throughout ownership, the entire gain is exempt from CGT.

### 5.2 Partial PPR Relief

| Period | Treatment |
|---|---|
| Periods of occupation as main residence | Exempt |
| Last 9 months of ownership (regardless of occupation) | Always exempt (deemed occupation) |
| Periods of absence due to employment (up to 4 years) | Exempt if resided before and after |
| Periods of overseas employment (any length) | Exempt if resided before and after |
| Letting relief | Up to £40,000 if part of PPR was let as residential accommodation |
| Garden/grounds | Exempt up to 0.5 hectares (or larger if appropriate to the property) |

### 5.3 PPR and Nominal Occupation

HMRC may challenge PPR claims where occupation was nominal (e.g. a few weeks). Must demonstrate genuine occupation as main residence — utility bills, electoral roll, correspondence address.

---

## Section 6 -- Business Asset Disposal Relief (BADR)

Formerly Entrepreneurs' Relief.

| Feature | Detail |
|---|---|
| Lifetime limit | £1,000,000 |
| Rate (2024-25) | 10% (on qualifying gains up to £1M) |
| Rate (2025-26) | 14% |
| Rate (2026-27) | 18% |
| Qualifying assets | Shares in a trading company (5% holding, 2-year ownership, officer/employee); sole trader/partnership business |
| Claim deadline | 1st anniversary of 31 January following tax year of disposal |
| Interaction with AEA | AEA used first; BADR applies to remaining gain |

---

## Section 7 -- 60-Day Property CGT Reporting

| Feature | Detail |
|---|---|
| Applies to | Disposals of UK residential property by UK residents (where CGT is due) and ALL disposals by non-residents |
| Deadline | 60 days from completion of the sale |
| Form | CGT on UK Property return (online HMRC service) |
| Payment | CGT due with the 60-day return (payment on account) |
| SA return | Still required — CGT on UK Property return is reported on SA108, with credit for CGT already paid |
| Penalty for late reporting | £100 (initial); further penalties accrue |
| Exemption from reporting | If no CGT due (e.g. full PPR relief applies) — reporting still recommended |

---

## Section 8 -- Losses

### 8.1 Loss Rules

| Rule | Detail |
|---|---|
| Current year losses | Must be set against gains of the same year (even if this wastes the AEA) |
| Brought-forward losses | Used only to reduce gains to the AEA level (not below) |
| Carry forward | Indefinite |
| Carry back | Only on death (to the 3 previous tax years) |
| Connected person losses | Can only be set against gains from disposals to the same connected person |
| Negligible value claim | Treat asset as disposed of and reacquired at negligible value — creates an allowable loss |
| Claim deadline | 4 years from end of tax year |

### 8.2 Reporting Losses

Losses must be reported to HMRC to be available for carry forward. Use SA108 or write to HMRC. Time limit: 4 years from end of the tax year in which the loss arose.

---

## Section 9 -- Transaction Pattern Library

### 9.1 Disposal Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| SHARE SALE, STOCK SALE, BROKER PAYOUT | Disposal — compute gain/loss | Match using share matching rules |
| PROPERTY SALE, SOLICITOR COMPLETION FUNDS | Disposal — compute gain/loss | 60-day reporting required for residential |
| BINANCE WITHDRAWAL, COINBASE SELL, CRYPTO SALE | Disposal — compute gain/loss | Match using crypto pool rules |
| GIFT OF SHARES, GIFT OF PROPERTY | Disposal at market value | Gift = disposal at MV for CGT |
| LIQUIDATION DISTRIBUTION, COMPANY WIND-UP | Disposal — capital distribution | May qualify for BADR if trading company |
| EIS DISPOSAL, SEIS DISPOSAL | Check relief conditions | May be exempt if held ≥3 years |

### 9.2 Acquisition Cost Evidence

| Pattern | Classification |
|---|---|
| SHARE PURCHASE, BROKER BUY | Acquisition cost (add dealing fees) |
| STAMP DUTY, SDLT | Incidental acquisition cost |
| SOLICITOR FEES (acquisition) | Incidental acquisition cost |
| SURVEY, VALUATION (on purchase) | Incidental acquisition cost |
| RENOVATION (capital improvement) | Enhancement expenditure |

---

## Section 10 -- Worked Examples

### Example 1 -- Share Disposal (2024-25, After 30 Oct)

**Input:** Sold 1,000 shares on 15 November 2024 for £25,000. Section 104 pool average cost: £10 per share. No same-day or 30-day matching. Basic rate taxpayer with £5,000 unused basic rate band.

**Computation:**
```
Proceeds:        £25,000
Cost (1,000 × £10): £10,000
Gain:            £15,000
Less AEA:        £3,000
Taxable gain:    £12,000

Rate (post-30 Oct): 18% basic / 24% higher
Basic rate portion: £5,000 × 18% = £900
Higher rate portion: £7,000 × 24% = £1,680
Total CGT:       £2,580
```

### Example 2 -- Crypto Disposal

**Input:** Sold 0.5 BTC on 1 February 2025 for £20,000. BTC Section 104 pool: 2 BTC at average cost £8,000 per BTC. No same-day or 30-day match.

**Computation:**
```
Proceeds:         £20,000
Cost (0.5 × £8,000): £4,000
Gain:             £16,000
Less AEA:         £3,000
Taxable gain:     £13,000
Rate (post-30 Oct): 18%/24% depending on income
```

### Example 3 -- PPR with Letting Relief

**Input:** Owned house 10 years. Lived in it for 6 years, let it for 4 years. Total gain £200,000.

**Computation:**
```
Exempt (PPR): 6 years + last 9 months = 6.75 years
Total ownership: 10 years
PPR fraction: 6.75/10 = 67.5%
PPR exempt: £200,000 × 67.5% = £135,000
Chargeable: £200,000 - £135,000 = £65,000
Letting relief: lower of (a) £40,000, (b) PPR exempt amount, (c) chargeable letting gain = £40,000
Chargeable after letting relief: £65,000 - £40,000 = £25,000
Less AEA: £3,000
Taxable: £22,000
```

### Example 4 -- BADR Qualifying Disposal (2024-25)

**Input:** Sole trader sells business for £500,000 gain. Owned >2 years. Claims BADR.

**Computation:**
```
Gain: £500,000
Less AEA: £3,000
Taxable: £497,000
BADR rate: 10% (2024-25)
CGT: £49,700
```
Within £1M lifetime limit. Deduct £500,000 from remaining lifetime allowance.

---

## Section 11 -- Edge Cases

### 11.1 Non-Residents
From April 2015, non-UK residents are liable to CGT on disposals of UK residential property. From April 2019, extended to all UK land and property (including commercial). Non-residents get the same AEA as UK residents.

### 11.2 Bed and ISA
Selling shares and immediately repurchasing within an ISA wrapper: the 30-day rule does NOT apply to ISA acquisitions. The disposal is matched to the Section 104 pool, and the ISA acquisition starts with a fresh cost base.

### 11.3 Spouse Transfers
Transfers between spouses/civil partners are at no gain/no loss. The receiving spouse inherits the original cost base. This can be used to utilise both AEAs.

### 11.4 Death
No CGT on death. Assets pass to the estate at market value at date of death (probate value). This effectively wipes out any accrued gain.

---

## PROHIBITIONS

- NEVER compute CGT without knowing the acquisition cost — STOP and request evidence
- NEVER apply PPR relief without confirming genuine occupation
- NEVER ignore the 30-day bed and breakfasting rule for shares and crypto
- NEVER forget the 60-day reporting requirement for UK residential property disposals
- NEVER apply pre-30 October 2024 rates (10%/20%) to disposals after 30 October 2024
- NEVER exceed the £1M BADR lifetime limit
- NEVER treat transfers between own crypto wallets as disposals
- NEVER carry back losses (except on death)
- NEVER waste the AEA by offsetting brought-forward losses below £3,000
- NEVER present CGT computations as definitive — always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
