---
name: de-crypto-tax
description: >
  Use this skill whenever asked about German cryptocurrency or digital asset taxation. Trigger on phrases like "Krypto Steuer", "crypto tax Germany", "Bitcoin Steuer", "§23 EStG Krypto", "private Veräußerungsgeschäft", "Haltefrist", "1-year holding period", "Freigrenze Krypto", "Staking Steuer", "Mining Steuer", "BMF Kryptowährungen", "Finanzamt crypto", "FIFO crypto Germany", "DeFi Steuer", "NFT Steuer Deutschland", "Anlage SO", "sonstige Einkünfte crypto", or any question about the income tax, capital gains, or trade tax treatment of cryptocurrency, tokens, or digital assets for German tax residents. Covers the BMF letter of 10 May 2022 (updated March 2025), §23 EStG holding period, Freigrenze, staking/lending/mining classification, FIFO method, and DeFi treatment. ALWAYS read this skill before touching any German crypto work.
version: 1.0
jurisdiction: DE
tax_year: 2025
category: international
depends_on:
  - de-income-tax
verified_by: pending
---

# German Crypto / Digital Assets Tax Skill v1.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Germany (Bundesrepublik Deutschland) |
| Tax | Einkommensteuer on crypto assets |
| Currency | EUR (all values must be converted at transaction date) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | EStG §23 Abs. 1 S. 1 Nr. 2 (private Veräußerungsgeschäfte), §22 Nr. 2 (sonstige Einkünfte), §22 Nr. 3 (sonstige Leistungen), §15 (gewerbliche Einkünfte) |
| Key authority | BMF-Schreiben vom 10. Mai 2022 (BStBl I 2022, S. 668) — "Einzelfragen zur ertragsteuerrechtlichen Behandlung von virtuellen Währungen und von sonstigen Token" (updated 6 March 2025) |
| BFH ruling | BFH IX R 3/22 (14 February 2023) — crypto assets are "andere Wirtschaftsgüter" under §23 |
| Tax authority | Finanzamt (local tax office) |
| Filing portal | ELSTER (elster.de) |
| Filing deadline | 31 July of the following year (with Steuerberater: end of February year after next) |
| Tax form | Anlage SO (Sonstige Einkünfte) for §23 gains; Anlage G for Gewerbliche Einkünfte |
| Validated by | Pending — requires sign-off by a German Steuerberater |
| Skill version | 1.0 |

### Core Rule: 1-Year Holding Period (Haltefrist)

```
IF held > 1 year (between Anschaffung and Veräußerung) → TAX-FREE
IF held ≤ 1 year → taxable as privates Veräußerungsgeschäft (§23 EStG)
```

This is the single most important rule in German crypto taxation.

### Freigrenze (Exemption Threshold)

| Period | Threshold | Type |
|---|---|---|
| From 2024 (VZ 2024 onwards) | EUR 1,000 per calendar year | Freigrenze (NOT Freibetrag) |
| 2023 and earlier | EUR 600 per calendar year | Freigrenze |

**Freigrenze vs Freibetrag:** A Freigrenze is a threshold — if total gains from ALL private sales transactions (crypto + other §23 assets) in the year are **less than** EUR 1,000, all gains are tax-free. If gains reach EUR 1,000 or more, the **entire amount** is taxable (not just the excess). This is fundamentally different from a Freibetrag (allowance) where only the excess is taxed.

### Tax Rates on Crypto Gains (Within Holding Period)

Crypto gains within the 1-year holding period are taxed at the personal income tax rate:

| Taxable income (EUR) | Marginal rate |
|---|---|
| 0 -- 12,096 | 0% (Grundfreibetrag) |
| 12,097 -- 17,443 | 14% -- 24% |
| 17,444 -- 66,760 | 24% -- 42% |
| 66,761 -- 277,825 | 42% |
| 277,826+ | 45% |

Plus Solidaritätszuschlag and Kirchensteuer where applicable. Crypto gains are NOT subject to Abgeltungsteuer (25% flat rate for capital gains on securities) — they are taxed at the full personal rate.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown holding period | Treat as ≤1 year (taxable) |
| Unknown acquisition cost | STOP — cannot compute |
| Unknown whether trading or private | Treat as Gewerblich (worst case — trade tax + income tax) |
| Unknown cost allocation method | Apply FIFO |
| Unknown whether staking extends holding period | Treat as NO extension (BMF confirmed: no 10-year extension for crypto) |

---

## Section 2 -- Classification of Crypto Activities

### 2.1 Private Individuals (Privatvermögen)

| Activity | Classification | Legislation | Tax Treatment |
|---|---|---|---|
| Buy and sell crypto (held ≤1 year) | Privates Veräußerungsgeschäft | §23 Abs. 1 S. 1 Nr. 2 EStG | Taxable at personal rate; Freigrenze EUR 1,000 |
| Buy and sell crypto (held >1 year) | Privates Veräußerungsgeschäft | §23 Abs. 1 S. 1 Nr. 2 EStG | TAX-FREE |
| Swap crypto-to-crypto | Veräußerung + Anschaffung | §23 EStG | Each swap is a taxable disposal; holding period restarts |
| Staking rewards received | Sonstige Einkünfte | §22 Nr. 3 EStG | Taxable at market value on receipt; own holding period starts at receipt |
| Lending income (interest) | Sonstige Einkünfte | §22 Nr. 3 EStG | Taxable at personal rate |
| Mining (private, small scale) | Sonstige Einkünfte | §22 Nr. 3 EStG | Taxable at market value on receipt |
| Airdrops (no service rendered) | Anschaffung at EUR 0 | — | Cost basis = 0; taxable on later disposal within 1 year |
| Airdrops (service rendered) | Sonstige Einkünfte | §22 Nr. 3 EStG | Taxable at market value on receipt |

### 2.2 Commercial Activity (Gewerbliche Einkünfte, §15 EStG)

If crypto activity qualifies as a Gewerbebetrieb (trade or business), it falls under §15 EStG instead of §23:

| Indicator | Suggests Gewerblich |
|---|---|
| Sustained, independent activity | Regular trading as primary occupation |
| Profit intent | Profit-making is the objective |
| Participation in general commerce | Operating an exchange, OTC desk, market-making |
| Mining at commercial scale | Dedicated hardware, significant electricity, consistent operation |
| NFT creation and regular sale | Business-like production and marketing |

**Consequences of Gewerblich classification:**
- No 1-year holding period exemption
- Gewerbesteuer (trade tax) applies in addition to income tax
- Full bookkeeping obligations (Buchführungspflicht)
- VAT registration and returns
- Annual losses can be used more flexibly (but Gewerbesteuer loss offset is limited)

### 2.3 Sonstige Einkünfte (§22 Nr. 3 EStG)

Staking, lending, and small-scale mining income falls under §22 Nr. 3:
- Freigrenze of EUR 256 per year (if total sonstige Leistungen are below this, all are tax-free)
- If EUR 256 or more, the ENTIRE amount is taxable
- Werbungskosten (directly related expenses) can be deducted

---

## Section 3 -- Holding Period Rules (Haltefrist)

### 3.1 Standard 1-Year Rule

The holding period runs from the date of Anschaffung (acquisition) to the date of Veräußerung (disposal). If it exceeds 1 year (366 days or more), the gain is tax-free.

### 3.2 No 10-Year Extension for Crypto

The BMF letter explicitly confirms: the 10-year extension of the holding period under §23 Abs. 1 S. 1 Nr. 2 S. 4 EStG does NOT apply to Kryptowerte (payment/currency tokens). This means:
- Using crypto for staking does NOT extend the holding period to 10 years
- Lending crypto does NOT extend the holding period to 10 years
- The standard 1-year holding period applies regardless of staking/lending

This was a major clarification in the May 2022 BMF letter, resolving significant uncertainty.

### 3.3 Holding Period Restarts on Swaps

Every crypto-to-crypto exchange is a disposal of the first asset and an acquisition of the second:
- The holding period of the disposed asset ends (gain/loss computed)
- The holding period of the newly acquired asset starts fresh
- This includes swaps like BTC → ETH, ETH → USDT, or any token exchange

---

## Section 4 -- Cost Basis and FIFO

### 4.1 FIFO Method (First In, First Out)

The BMF letter and Finanzamt practice accept FIFO as the standard method:

```
When disposing of crypto, the OLDEST units are treated as sold first.
```

| Method | Status |
|---|---|
| FIFO | Accepted; standard practice; BMF-endorsed |
| Specific identification (Einzelbetrachtung) | Theoretically possible if each unit is clearly identified (e.g. separate wallets per purchase) |
| Average cost (Durchschnittsmethode) | NOT standard for §23 EStG; may be challenged |
| LIFO | NOT accepted by BMF |

### 4.2 Cost Basis Calculation

```
Anschaffungskosten = Purchase price in EUR (at exchange rate on date)
                   + Exchange/trading fees
                   + Network/gas fees (if directly attributable)
                   + Other acquisition costs

Veräußerungspreis = Sale price in EUR (at exchange rate on date)
                  - Disposal costs (exchange fees, withdrawal fees)

Gain/Loss = Veräußerungspreis - Anschaffungskosten - Werbungskosten
```

### 4.3 Crypto-to-Crypto Swaps

For a swap (e.g. 1 ETH → 3,000 USDC):
- Disposal of ETH: proceeds = market value of 3,000 USDC in EUR on the date of swap
- Acquisition of USDC: cost basis = same EUR value
- If ETH was held <1 year: gain is taxable
- If ETH was held >1 year: gain is tax-free

---

## Section 5 -- Transaction Pattern Library

### 5.1 Taxable Event Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| BINANCE SELL, KRAKEN SELL, BITCOIN.DE VERKAUF | Disposal | Compute gain using FIFO; check holding period |
| COINBASE CONVERT, SWAP | Disposal + Acquisition | Two taxable events in one transaction |
| CRYPTO → FIAT withdrawal to bank | Disposal | Proceeds = EUR received |
| Payment for goods/services with crypto | Disposal | Proceeds = EUR value of goods/services |
| GIFT OF CRYPTO (to non-spouse) | Disposal at market value | Schenkungsteuer may also apply |

### 5.2 Income Event Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| STAKING REWARD, VALIDATOR REWARD, EARN | Sonstige Einkünfte (§22 Nr. 3) | Taxable at market value on receipt; Freigrenze EUR 256 |
| LENDING INTEREST, NEXO INTEREST, CELCIUS | Sonstige Einkünfte (§22 Nr. 3) | Interest from crypto lending |
| MINING PAYOUT, POOL REWARD | Sonstige Einkünfte or §15 | Depends on scale — private vs commercial |
| AIRDROP (no service) | Anschaffung at EUR 0 | Not immediately taxable; taxable on disposal <1 year |
| AIRDROP (service required) | Sonstige Einkünfte | Taxable at receipt |
| LIQUIDITY MINING, LP REWARD | Sonstige Einkünfte | Taxable at market value on receipt |

### 5.3 Non-Taxable Patterns

| Pattern | Treatment |
|---|---|
| Transfer between own wallets | NOT a disposal — no tax event |
| Transfer between own exchange accounts | NOT a disposal |
| Buying crypto with fiat | Anschaffung only — no tax event |
| Holding (no disposal) | No event until disposed |
| Disposal after >1 year holding | Tax-free (but should still be documented) |

---

## Section 6 -- DeFi-Specific Rules

### 6.1 Lending (Krypto-Verleih)

| Feature | Treatment |
|---|---|
| Lending crypto to a protocol/platform | Transfer of ownership = disposal? BMF says: depends on contract |
| Interest received | Sonstige Einkünfte (§22 Nr. 3) |
| Return of principal | If same tokens returned: not a new acquisition (continuation of holding period) |
| Holding period impact | NOT extended to 10 years (BMF confirmed) |

### 6.2 Liquidity Providing (AMM Pools)

| Feature | Treatment |
|---|---|
| Depositing into LP | May constitute disposal of the deposited tokens — position evolving |
| Receiving LP tokens | New asset with new cost basis and holding period |
| Withdrawal from LP | Disposal of LP tokens; reacquisition of underlying |
| Trading fees earned | Sonstige Einkünfte at receipt |
| Impermanent loss | Not a recognised deductible loss until actual disposal |

### 6.3 NFTs

| Scenario | Treatment |
|---|---|
| Buying NFT with crypto | Disposal of crypto (taxable if <1 year); acquisition of NFT |
| Selling NFT for crypto/fiat | Disposal of NFT; §23 applies if held <1 year |
| Creating and selling NFTs regularly | Potentially Gewerblich (§15) if business-like |
| NFT as collectible (rare, one-off) | §23 applies — private asset |

---

## Section 7 -- Worked Examples

### Example 1 -- Simple Buy and Sell Within 1 Year

**Input:** Bought 1 BTC on 1 March 2025 for EUR 40,000. Sold 1 BTC on 1 August 2025 for EUR 55,000. Exchange fees: EUR 100 (buy) + EUR 100 (sell). No other §23 gains.

**Computation:**
```
Anschaffungskosten: EUR 40,000 + EUR 100 = EUR 40,100
Veräußerungspreis: EUR 55,000 - EUR 100 = EUR 54,900
Gain: EUR 54,900 - EUR 40,100 = EUR 14,800

Holding period: 5 months (< 1 year) → TAXABLE
Freigrenze: EUR 14,800 ≥ EUR 1,000 → entire gain taxable
Tax: EUR 14,800 × personal marginal rate (e.g. 42%) = EUR 6,216
```

### Example 2 -- Held Over 1 Year (Tax-Free)

**Input:** Bought 2 ETH on 1 January 2024 for EUR 3,000. Sold 2 ETH on 5 January 2025 for EUR 7,000.

**Computation:**
```
Holding period: > 1 year → TAX-FREE
No entry needed on Anlage SO (but recommended to document)
```

### Example 3 -- FIFO Application

**Input:**
- 1 March 2025: Buy 0.5 BTC at EUR 40,000/BTC = EUR 20,000
- 1 June 2025: Buy 0.5 BTC at EUR 50,000/BTC = EUR 25,000
- 1 September 2025: Sell 0.5 BTC at EUR 55,000/BTC = EUR 27,500

**FIFO:** The 0.5 BTC sold on 1 September is matched to the 1 March purchase (oldest first).

```
Anschaffungskosten: EUR 20,000
Veräußerungspreis: EUR 27,500
Gain: EUR 7,500
Holding period: 6 months (< 1 year) → TAXABLE
```

### Example 4 -- Staking Income + Subsequent Disposal

**Input:** Received 0.1 ETH staking reward on 1 April 2025. Market value: EUR 350. Sold 0.1 ETH on 1 October 2025 for EUR 400.

**Computation:**
```
Step 1 — Staking income (§22 Nr. 3):
  EUR 350 (taxable as sonstige Einkünfte at receipt)
  If total §22 Nr. 3 income < EUR 256 → tax-free
  If ≥ EUR 256 → fully taxable

Step 2 — Disposal (§23):
  Cost basis: EUR 350 (market value at staking receipt)
  Proceeds: EUR 400
  Gain: EUR 50
  Holding period: 6 months → taxable
  (Add to other §23 gains for Freigrenze calculation)
```

### Example 5 -- Below Freigrenze

**Input:** Total §23 gains from all crypto sales in 2025: EUR 900. No other private sale transactions.

**Computation:**
```
Total gain: EUR 900 < EUR 1,000 Freigrenze
Result: ENTIRE EUR 900 is TAX-FREE
```

### Example 6 -- Just Over Freigrenze

**Input:** Total §23 gains: EUR 1,050.

**Computation:**
```
Total gain: EUR 1,050 ≥ EUR 1,000 Freigrenze
Result: ENTIRE EUR 1,050 is TAXABLE (not just the EUR 50 excess)
Tax: EUR 1,050 × marginal rate
```

---

## Section 8 -- Record-Keeping Requirements

| Requirement | Detail |
|---|---|
| Retention period | 10 years (Steuerliche Aufbewahrungspflicht for Gewerblich; recommended for all) |
| Required records | Full transaction history from all exchanges and wallets, date/time/amount/price for each trade, FIFO calculation ledger |
| Recommended tools | CoinTracking, Blockpit, Accointing, CryptoTaxCalculator (German-compliant) |
| Proof of holding period | Exchange timestamps, wallet transaction hashes (Blockchain explorer) |
| Burden of proof | On the taxpayer — Finanzamt can request full documentation |
| MiCA / DAC8 | From 2026, exchanges must report user transaction data to German tax authorities |

---

## Section 9 -- Edge Cases

### 9.1 Hard Forks
- Original coin: holding period continues unchanged
- New forked coin: Anschaffungskosten = EUR 0; new holding period starts from the fork date
- Disposal of forked coin within 1 year: full proceeds are gain (zero cost basis)

### 9.2 Lost Private Keys / Inaccessible Wallets
If crypto is permanently lost (provably inaccessible), a Wertloser Wirtschaftsgut claim may be possible — but the Finanzamt requires strong proof. Lost access alone (forgotten password) is typically not sufficient; the asset technically still exists on-chain.

### 9.3 Margin / Leverage Trading
Leveraged trading positions are treated as derivatives. The tax treatment depends on the specific instrument (CFD, perpetual, futures). Losses from Termingeschäfte have been limited to EUR 20,000 per year offset since 2021 (§20 Abs. 6 S. 5 EStG), though this is under legal challenge.

### 9.4 Crypto Wages / Salary Paid in Crypto
If an employer pays salary in crypto, it is taxable as Einkünfte aus nichtselbständiger Arbeit (§19 EStG) at the market value on the payment date. The employee's cost basis for the crypto = the income value. Normal §23 holding period rules apply to subsequent disposal.

---

## Section 10 -- Filing on Anlage SO

| Line | Content |
|---|---|
| Zeile 41 | Bezeichnung des veräußerten Wirtschaftsguts (e.g. "Bitcoin", "Ethereum") |
| Zeile 42 | Art des Wirtschaftsguts: "anderes Wirtschaftsgut" |
| Zeile 43 | Veräußerungspreis (disposal proceeds in EUR) |
| Zeile 44 | Anschaffungskosten + Werbungskosten |
| Zeile 45 | Gewinn/Verlust (gain or loss) |
| Zeile 49 | Summe der Gewinne und Verluste aus privaten Veräußerungsgeschäften |

Multiple disposals can be aggregated per asset type. Attach a detailed FIFO calculation as Anlage (supporting schedule).

---

## PROHIBITIONS

- NEVER assume crypto gains are always tax-free in Germany — only gains after the 1-year holding period are exempt
- NEVER confuse Freigrenze with Freibetrag — if total gains reach EUR 1,000, the ENTIRE amount is taxable
- NEVER apply Abgeltungsteuer (25% flat rate) to crypto — crypto gains are taxed at the personal income tax rate
- NEVER extend the holding period to 10 years for staking/lending — the BMF letter explicitly excludes this
- NEVER ignore crypto-to-crypto swaps as taxable events — each swap is a disposal and acquisition
- NEVER use LIFO for cost basis — FIFO is the accepted method
- NEVER classify all mining as private — commercial-scale mining is Gewerblich
- NEVER present crypto tax computations as definitive — always label as estimated and flag for Steuerberater review

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
