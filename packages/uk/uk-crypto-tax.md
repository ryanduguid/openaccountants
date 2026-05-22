---
name: uk-crypto-tax
description: >
  Use this skill whenever asked about UK cryptocurrency or digital asset taxation. Trigger on phrases like "crypto tax UK", "Bitcoin UK tax", "HMRC crypto", "cryptoassets UK", "crypto capital gains UK", "staking tax UK", "mining tax UK", "NFT tax UK", "DeFi tax UK", "SA108 crypto", "crypto CGT", "bed and breakfasting crypto", "S104 pool", "crypto loss UK", "Coinbase UK tax", "Binance UK tax", "Revolut crypto UK", "crypto income UK", "DAC8 UK", "HMRC cryptoassets manual", or any question about the income tax, capital gains tax, or reporting treatment of cryptocurrency, tokens, or digital assets for UK tax residents. Covers HMRC's Cryptoassets Manual (CRYPTO10000+), S104 pooling, same-day and 30-day matching rules, DeFi lending/staking, NFTs, mining, and SA108 reporting. ALWAYS read this skill before touching any UK crypto work.
version: 1.0
jurisdiction: GB
tax_year: 2025
category: crypto
depends_on:
  - uk-capital-gains-sa108
  - uk-income-tax-sa100
verified_by: pending
---

# UK Crypto / Digital Assets Tax Skill v1.0

---

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Country | United Kingdom (England, Wales, Northern Ireland; Scotland has different income tax rates) |
| Tax | Capital Gains Tax (CGT) and Income Tax on cryptoassets |
| Currency | GBP (all values must be converted to GBP at the transaction date) |
| Tax year | 6 April – 5 April (2025/26 = 6 Apr 2025 – 5 Apr 2026) |
| Primary authority | HMRC Cryptoassets Manual (CRYPTO10000+); Taxation of Chargeable Gains Act 1992 (TCGA 1992); Income Tax Act 2007 (ITA 2007); Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005) |
| Tax authority | HM Revenue & Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online / Government Gateway |
| CGT annual exempt amount | £3,000 (2025/26) |
| CGT rates (individuals) | 18% (basic-rate taxpayer) / 24% (higher/additional-rate taxpayer) |
| Income tax rates (mining/staking) | 20% / 40% / 45% (England, Wales, NI) |
| Personal allowance | £12,570 (2025/26) |
| Cost basis method | Section 104 pooling (TCGA 1992 S104), subject to same-day and 30-day matching rules |
| Anti-avoidance | 30-day bed-and-breakfasting rule (TCGA 1992 S106A) |
| Reporting form | SA108 (Capital Gains Summary) supplementary to SA100 |
| Filing deadline | 31 January following end of tax year (31 Jan 2027 for 2025/26) for online filing |
| Exchange reporting | No mandatory exchange reporting yet; DAC8/CARF from 2026 |
| Validated by | Pending — requires sign-off by a UK chartered accountant or tax adviser |
| Skill version | 1.0 |

### HMRC Cryptoasset Classification (CRYPTO10000+)

| Asset Type | HMRC Classification | CGT Treatment | Income Tax Treatment |
|---|---|---|---|
| Exchange tokens (BTC, ETH, LTC) | Tokens used as means of payment | Subject to CGT on disposal | Mining/staking/airdrops = income |
| Utility tokens | Tokens providing access to a service | Subject to CGT on disposal | Trading profits = income if traded |
| Security tokens | Tokens providing rights like shares/debt | Subject to CGT on disposal | May also attract income tax on returns |
| Stablecoins (USDT, USDC) | Exchange tokens pegged to fiat | Subject to CGT on disposal (gain usually negligible) | N/A |
| NFTs | Non-fungible tokens | Subject to CGT on disposal | Creator sales = trading income |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown cost basis | Zero cost basis (maximises gain) — STOP if material |
| Unknown whether trading or investment | Treat as investment (CGT) unless clear badges of trade |
| Unknown token classification | Treat as exchange token (subject to CGT) |
| Unknown FMV at receipt | Use CoinGecko/CoinMarketCap daily close in GBP |
| Unknown whether income or capital DeFi return | Income (higher rate treatment) |
| Airdrop with no clear service performed | Income at FMV on receipt |

---

## Section 2 — Classification Rules: Capital Gains vs Income

### When CGT applies (most individual crypto users)

HMRC treats cryptoassets as property, not currency. Each disposal triggers a CGT computation. A "disposal" includes (CRYPTO22100):

- Selling tokens for fiat
- Exchanging tokens for a different type of token (crypto-to-crypto swap)
- Using tokens to pay for goods or services
- Giving away tokens (except to spouse/civil partner)

**NOT a disposal:**
- Transferring between own wallets
- Using a mixer/tumbler where same token type returned
- Gifting to spouse/civil partner (no gain, no loss — transferee inherits cost basis)

### When Income Tax applies

| Activity | Tax Treatment | Authority |
|---|---|---|
| Mining (hobbyist) | Miscellaneous income at FMV when received | ITTOIA 2005 S687; CRYPTO21200 |
| Mining (commercial/business) | Trading income; expenses deductible | ITTOIA 2005 Part 2; CRYPTO21200 |
| Staking rewards | Miscellaneous income at FMV when received | CRYPTO21200 |
| Airdrops (for service/action) | Miscellaneous income at FMV when received | CRYPTO21250 |
| Airdrops (unsolicited, no action) | Not income on receipt; CGT on disposal from zero cost | CRYPTO21250 |
| Employer pays salary in crypto | Employment income at FMV; PAYE/NIC applies | CRYPTO21100 |
| DeFi yield (income returns) | Miscellaneous income or trading income | CRYPTO61200 |

### Income Tax Rates (2025/26 — England, Wales, NI)

| Band | Taxable Income | Rate |
|---|---|---|
| Personal Allowance | Up to £12,570 | 0% |
| Basic rate | £12,571 – £50,270 | 20% |
| Higher rate | £50,271 – £125,140 | 40% |
| Additional rate | Over £125,140 | 45% |

Source: Finance Act 2025 s.2; GOV.UK Income Tax rates 2025/26.

---

## Section 3 — Capital Gains Tax Rate Table

### CGT Rates for Cryptoassets (2025/26)

| Taxpayer Status | Rate |
|---|---|
| Basic-rate taxpayer (gains within basic-rate band) | 18% |
| Higher-rate / additional-rate taxpayer | 24% |
| Trustees / personal representatives | 24% |
| Annual exempt amount (individuals) | £3,000 |
| Annual exempt amount (most trustees) | £1,500 |

Source: TCGA 1992; GOV.UK Capital Gains Tax rates and allowances (updated for 2025/26).

**Note:** Prior to 30 October 2024, rates were 10%/20%. For 2024/25, the year was split: 10%/20% (6 Apr – 29 Oct 2024) and 18%/24% (30 Oct 2024 – 5 Apr 2025). For 2025/26 onwards, the full year is 18%/24%.

### CGT Computation

```
Disposal proceeds (GBP at date of disposal)
  LESS: Allowable cost (from S104 pool, same-day rule, or 30-day rule)
  LESS: Incidental costs of disposal (exchange fees, gas fees)
  = Gain or (Loss)

Total gains for the year
  LESS: Allowable losses of the year
  LESS: Losses brought forward (only to reduce gains to annual exempt amount)
  LESS: Annual exempt amount (£3,000)
  = Taxable gains

Tax = Taxable gains × 18% or 24%
```

---

## Section 4 — Cost Basis: Section 104 Pooling and Matching Rules

HMRC requires a specific matching order for cryptoasset disposals (CRYPTO22200):

### Matching Order (mandatory priority)

| Priority | Rule | Reference |
|---|---|---|
| 1st | **Same-day rule** — match against tokens of the same type acquired on the same day | TCGA 1992 S105(1) |
| 2nd | **30-day rule (bed-and-breakfasting)** — match against tokens of the same type acquired within 30 days AFTER the disposal | TCGA 1992 S106A |
| 3rd | **S104 pool** — match against the average cost of the S104 pool of that token type | TCGA 1992 S104 |

### S104 Pool Mechanics

The S104 pool is a running weighted-average cost pool for each token type. Each time you acquire tokens, the pool quantity and pool cost increase. Each time you dispose of tokens (not matched by same-day or 30-day rules), the cost of disposal is the proportionate share of the pool cost.

```
Pool cost per token = Total pool cost ÷ Total pool quantity
Cost of disposal = Tokens disposed × Pool cost per token
```

| Permitted Method | Status |
|---|---|
| S104 pooling (weighted average) | MANDATORY for most disposals |
| FIFO | NOT permitted (except for specific share identification — not applicable to crypto) |
| LIFO | NOT permitted |
| Specific identification | NOT permitted for crypto |

### What is included in cost basis

- Purchase price in GBP (converted at exchange rate on acquisition date)
- Exchange fees and commissions on acquisition
- Gas/network fees on acquisition (CRYPTO22280)
- Note: token fees paid as gas are themselves a disposal at market value

---

## Section 5 — DeFi, Staking, Mining, and Airdrops

### 5.1 DeFi Lending (CRYPTO61000+)

HMRC published DeFi guidance in February 2022 (Cryptoassets Manual CRYPTO61000 onwards) and consulted on reforms in August 2022.

| DeFi Activity | Tax Treatment | Key Question |
|---|---|---|
| Lending tokens to a protocol | **Disposal** if beneficial ownership transfers; **not a disposal** if beneficial ownership retained | Does the borrower/platform have free use of the tokens? |
| Receiving LP tokens in return | Exchange of tokens = disposal of deposited tokens, acquisition of LP tokens at FMV | CRYPTO61620 |
| Interest/yield received | Miscellaneous income at FMV on receipt (NOT interest — crypto is not money) | CRYPTO61200 |
| Withdrawal from protocol | Disposal of LP tokens, reacquisition of underlying | FMV at withdrawal |
| Impermanent loss | Crystallised on withdrawal — reflected in gain/loss on LP token disposal | No separate relief |

**Government consultation (2022):** Proposed elective regime to disregard DeFi disposals for CGT until economic disposal. Not yet enacted as of 2025/26 — current rules apply.

### 5.2 Staking

| Aspect | Treatment |
|---|---|
| Proof-of-stake validation rewards | Miscellaneous income at FMV when received (CRYPTO21200) |
| Cost basis of staking reward | FMV at receipt date (becomes acquisition cost for CGT) |
| Subsequent sale of staking reward | CGT on gain from FMV cost basis |
| Staking-as-a-service provider | Trading income; business expenses deductible |

### 5.3 Mining

| Aspect | Treatment |
|---|---|
| Hobby mining | Miscellaneous income at FMV when mined (CRYPTO21200) |
| Business mining | Trading income; expenses deductible (electricity, hardware depreciation, rent) |
| Cost basis of mined tokens | FMV at date mined |
| Subsequent sale of mined tokens | CGT on gain from FMV cost basis |

### 5.4 Airdrops (CRYPTO21250)

| Scenario | Treatment |
|---|---|
| Airdrop received in return for a service or action | Miscellaneous income at FMV on receipt |
| Unsolicited airdrop (no action required) | NOT income on receipt; zero cost basis; full gain taxable as CGT on disposal |
| Airdrop with negligible value | Record at zero; CGT on disposal |

### 5.5 Hard Forks

| Scenario | Treatment |
|---|---|
| New tokens from fork (e.g. BTC → BCH) | NOT a disposal of original tokens; new tokens received at zero cost (no acquisition cost) |
| Sale of forked tokens | Full proceeds = gain (zero cost basis) |
| Apportioning original cost | HMRC does not require cost apportionment for hard forks — new token cost = £0 |

---

## Section 6 — NFT Treatment

| Event | Tax Treatment |
|---|---|
| Purchase of NFT (collector) | Acquisition — record cost basis including gas fees |
| Sale of NFT (collector) | CGT on disposal (proceeds minus S104 pool cost of NFT) |
| Creation and primary sale of NFT (artist) | Trading income if business; miscellaneous income if one-off |
| Royalty income from secondary sales | Miscellaneous income at FMV on receipt |
| NFT-for-NFT swap | Disposal of both NFTs; each at FMV |
| NFT becomes worthless | Negligible value claim possible (TCGA 1992 S24(2)) — triggers loss |
| VAT on NFT | Potentially subject to VAT at 20% if seller is VAT-registered (digitally supplied service) |

HMRC treats NFTs the same as any other cryptoasset for CGT purposes (CRYPTO22100). The same S104 pooling and matching rules apply per individual NFT (each unique NFT is its own asset — no pooling between different NFTs).

---

## Section 7 — Reporting Requirements

### 7.1 Self Assessment Forms

| Form | Purpose |
|---|---|
| SA100 | Main Self Assessment tax return |
| SA108 | Capital Gains Summary supplementary page |

### 7.2 When SA108 is required

You must file SA108 if any of the following apply (2025/26):
- Total disposal proceeds from all assets exceed £50,000
- Chargeable gains before losses exceed £3,000 (the annual exempt amount)
- You wish to claim an allowable capital loss
- Losses brought forward are being used

### 7.3 Key Deadlines

| Deadline | Date |
|---|---|
| End of tax year 2025/26 | 5 April 2026 |
| Paper SA100 filing deadline | 31 October 2026 |
| Online SA100 filing deadline | 31 January 2027 |
| Payment deadline | 31 January 2027 |
| Payments on account | 31 January and 31 July |

### 7.4 Exchange Reporting

As of 2025/26, there is **no mandatory exchange reporting** obligation in the UK for crypto platforms. However:
- **DAC8 (EU)** and **CARF (OECD)** will require crypto-asset service providers to report user transaction data to HMRC from **2026**
- HMRC can and does issue information notices to UK exchanges under existing powers
- Voluntary disclosure is strongly recommended

### 7.5 Record-Keeping

| Requirement | Detail |
|---|---|
| Retention period | At least 5 years after the 31 January filing deadline (effectively ~6 years from end of tax year) |
| Records to maintain | Full transaction logs from all exchanges, wallet addresses, S104 pool calculations, staking/mining logs, DeFi protocol records |
| Format | CSV exports preferred; screenshots acceptable as backup; on-chain records (block explorer links) recommended |

---

## Section 8 — Loss Offset and Carry-Forward Rules

### 8.1 Capital Losses

| Rule | Detail | Authority |
|---|---|---|
| In-year offset | Allowable losses MUST be set against gains of the same tax year first | TCGA 1992 S2 |
| Carry-forward | Unused losses can be carried forward indefinitely | TCGA 1992 S2(2) |
| Carry-forward limitation | Carried-forward losses can only reduce gains to the annual exempt amount (£3,000) | TCGA 1992 S3 |
| Carry-back | NOT permitted (except on death) | — |
| Reporting deadline | Losses MUST be reported to HMRC within **4 years** of the end of the tax year in which they arose | TCGA 1992 S16(2A) |
| Negligible value claim | For tokens that become worthless — treated as disposal and reacquisition at negligible value, crystallising a loss | TCGA 1992 S24(2) |

### 8.2 Income Losses (Mining/Trading)

- Trading losses from crypto mining/staking business may be offset against other income under ITA 2007 S64
- Miscellaneous income losses can only offset miscellaneous income of the same type

### 8.3 Critical: 4-Year Loss Claim Window

If you do not report a capital loss within 4 years of the end of the tax year in which it arose, the loss is permanently lost. For a loss arising in 2025/26, the deadline is 5 April 2030.

---

## Section 9 — Anti-Avoidance: Bed-and-Breakfasting and Wash Sale Rules

### 9.1 The 30-Day Rule (TCGA 1992 S106A)

If a taxpayer disposes of tokens and reacquires tokens of the **same type** within **30 days** after the disposal, the disposal is matched to the reacquisition (not the S104 pool). This prevents:

- Selling to crystallise a loss and immediately rebuying
- Selling to use the annual exempt amount and immediately rebuying

| Element | Detail |
|---|---|
| Window | 30 calendar days after the disposal |
| Scope | Same token type only (selling BTC and buying ETH within 30 days is fine) |
| Effect on loss | Loss is effectively deferred — cost of reacquired tokens takes on the cost of the original disposal |
| Workaround ("Bed and ISA") | Sell, rebuy inside a spouse's account or ISA wrapper — but HMRC may challenge if artificial |

### 9.2 Same-Day Rule (TCGA 1992 S105)

If tokens are both acquired and disposed of on the same day, the disposal is matched to the same-day acquisition first.

### 9.3 General Anti-Abuse Rule (GAAR)

The GAAR (Finance Act 2013 Part 5) may apply to artificial crypto tax avoidance arrangements.

---

## Section 10 — Worked Examples

### Example 1 — Simple BTC Sale, CGT Computation

**Input:** UK tax resident. Bought 2 BTC at £20,000 each in January 2024. Sold 1 BTC at £45,000 in August 2025. No other disposals. Exchange fees: £50 on acquisition, £75 on disposal. Basic-rate taxpayer.

**Computation:**
```
S104 pool:
  2 BTC acquired at £20,000 each = £40,000 + £50 fees = £40,050
  Pool cost per BTC = £40,050 ÷ 2 = £20,025

Disposal of 1 BTC:
  Proceeds:          £45,000
  LESS disposal fees: £75
  Net proceeds:      £44,925
  LESS S104 cost:    £20,025
  Gain:              £24,900

  LESS annual exempt amount: £3,000
  Taxable gain:       £21,900

  CGT at 18% (basic-rate):  £3,942

S104 pool after disposal: 1 BTC, cost £20,025
```

### Example 2 — 30-Day Rule Blocks Loss

**Input:** UK tax resident. S104 pool: 5 ETH, total cost £10,000 (£2,000 per ETH). Sells 5 ETH at £1,500 each (£7,500) on 1 November 2025. Rebuys 5 ETH at £1,600 each (£8,000) on 20 November 2025 (within 30 days).

**Computation:**
```
Without 30-day rule:
  Proceeds: £7,500, Cost: £10,000, Loss: (£2,500)

With 30-day rule (mandatory):
  Disposal matched to 30-day reacquisition
  Proceeds: £7,500
  Matched cost: £8,000 (the reacquisition cost)
  Loss: (£500)

  The loss is DEFERRED — the new S104 pool now holds 5 ETH at cost £10,000
  (£8,000 reacquisition + £2,000 excess from original pool minus matched amount)

  Net effect: loss is deferred, not eliminated
```

### Example 3 — Staking Income + Subsequent CGT

**Input:** UK tax resident. Received 0.5 ETH staking rewards over 2025/26. Total FMV at each receipt: £1,800. Sold 0.5 ETH in March 2026 at £2,200. Higher-rate taxpayer.

**Computation:**
```
Income tax on staking (miscellaneous income):
  £1,800 × 40% (higher rate) = £720

Cost basis of staked ETH: £1,800

CGT on disposal:
  Proceeds:    £2,200
  Cost basis:  £1,800
  Gain:        £400

  If within annual exempt amount (£3,000): no CGT
  Total tax: £720 income tax only
```

---

## Self-Checks

- [ ] Have all disposals been identified (sells, swaps, crypto-to-crypto, payments for goods/services)?
- [ ] Have same-day and 30-day matching rules been applied before the S104 pool?
- [ ] Is the S104 pool maintained separately for each token type?
- [ ] Have mining/staking/airdrop receipts been included as income?
- [ ] Has the £3,000 annual exempt amount been applied correctly?
- [ ] Have losses been reported within the 4-year window?
- [ ] Is the correct CGT rate applied (18% or 24%) based on the taxpayer's total income?
- [ ] Are all values converted to GBP at the transaction date?
- [ ] Has SA108 been completed if thresholds are exceeded?
- [ ] Have DeFi transactions been analysed for beneficial ownership transfer?

---

## PROHIBITIONS

- NEVER assume crypto is tax-free in the UK — disposals are subject to CGT
- NEVER apply FIFO, LIFO, or specific identification — the UK REQUIRES S104 pooling with same-day and 30-day matching
- NEVER treat crypto-to-crypto swaps as non-taxable — they ARE disposals (CRYPTO22100)
- NEVER treat staking/mining income as capital gains — it is income (CRYPTO21200)
- NEVER ignore the 30-day bed-and-breakfasting rule when matching disposals
- NEVER forget to convert all values to GBP at the transaction-date exchange rate
- NEVER allow losses to go unreported beyond the 4-year claim window
- NEVER treat transfers between own wallets as disposals
- NEVER classify DeFi returns as "interest" — crypto is not money (CRYPTO61200)
- NEVER present crypto tax positions as definitive — always label as estimated and flag for professional review

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
