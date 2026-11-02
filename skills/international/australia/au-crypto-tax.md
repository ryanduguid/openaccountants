---
name: au-crypto-tax
description: Use this skill whenever asked about Australian cryptocurrency taxation. Trigger on phrases like "crypto tax Australia", "Bitcoin CGT", "ATO crypto", "crypto capital gains", "personal use asset crypto", "staking income", "airdrop tax", "DeFi tax Australia", "crypto cost base", "crypto trading tax", "Coinbase tax", "Swyftx tax", "CoinSpot tax", "NFT tax Australia", or any question about how cryptocurrency is taxed by the ATO. This skill covers CGT treatment of crypto assets, the personal use asset exemption, trading vs investing distinction, staking and airdrop income, DeFi events, record-keeping requirements, and exchange-specific transaction patterns. ALWAYS read this skill before touching any Australian crypto tax work.
version: 1.8
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 investment/reward computations; historical returns and 2027-28 transitions require their own operative sources"
last_updated: 2026-11-02
review_status: pending_review
depends_on:
  - workflow-base
  - au-individual-return
  - au-capital-gains
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Crypto Tax v1.8

> **General reference only.** This guide supports a reviewable Australian crypto tax working paper. It does not establish a taxpayer's eligibility, an approved return field or a final tax liability. Obtain qualified Australian review before filing, paying or taking a position.

## Scope

Prepare a 2026-27 crypto transaction register, investment CGT calculation and separately classified reward or services income. All amounts are in AUD at the relevant transaction or derivation time. Include sales, swaps, spending, gifts, supported DeFi events, receipts, losses and continuing holdings. A bank withdrawal alone does not identify when an earlier crypto disposal occurred.

The investment method below assumes the taxpayer and asset are on capital account. Establish the activity first. A business, trading stock, an isolated commercial profit-making transaction, employment remuneration, salary sacrifice, a derivative or a foreign-currency instrument can require another method. Route business income and Division 35 to [au-sole-trader-schedule](au-sole-trader-schedule.md), employment/payroll to [australia-payroll](australia-payroll.md), salary sacrifice to [au-fbt](au-fbt.md), GST to [au-gst-bas](au-gst-bas.md) and currency classification to [au-forex-gains-losses](au-forex-gains-losses.md). Do not apply an investment discount to revenue income. [ATO, crypto assets used in business](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/crypto-assets-and-business/crypto-assets-used-in-business).

Residents who are not temporary residents generally account for worldwide income and capital gains. For foreign or temporary residents, establish income source, taxable Australian property, any CGT event I1 choice and treaty interaction separately. Crypto has no simple physical-location shortcut. Use [au-tax-residency](au-tax-residency.md) and [au-nonresident-cgt](au-nonresident-cgt.md). [ATO, crypto transactions and residency](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-asset-transactions-and-tax-residency).

For events from 1 July 2027, apply the operative transition, residency and asset conditions in [au-capital-gains](au-capital-gains.md), supported by the Acts and any intervening amendments. There is no universal reset, retained discount or minimum charge for every crypto holding. Historical airdrops also require the applicable source period. This guide does not automate an unresolved transition or draft-ruling position.

## Ask the client first

1. What entity, beneficial owner, tax residence and temporary-residence history apply, and which income year and event dates are requested?
2. Is the activity investment, business/trading stock, services/employment, a hobby or an isolated commercial transaction? What purpose, actual use and protocol rights support that classification?
3. Can the records identify every parcel, acquisition date, transaction, fee, AUD valuation and closing holding across all exchanges and wallets, including transfers and lost access?
4. Which rewards, airdrops, chain splits, NFTs, collateral, lending, liquidity, bridges, migrations and wrapping transactions occurred, and what rights existed before and after each?
5. What current and prior capital losses, other gains, reimbursements, insurance, recoveries, elections or personal-use conditions affect the calculation?
6. Which approved return period, filing capacity and software are being used, and which facts, source conditions or reviewer decisions remain unresolved?

## The method, step by step

### 1. Reconcile records before classifying

Collect exchange exports, public wallet addresses, counterparty identity or crypto address where applicable, transaction identifiers, timestamps and time zones, token quantities, AUD values and their sources, fees, bank movements and the transaction's purpose. Retain evidence identifying each disposed parcel and its costs. Reconstruct missing exports using available exchange, bank and blockchain records. An exchange software method label does not identify the actual asset sold. Do not substitute a FIFO, LIFO or consistency policy for parcel evidence without establishing that the proposed identification is supportable. [ATO, keeping crypto records](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records).

Match transfers between the same owner's wallets and distinguish them from transfers that end beneficial ownership or create replacement rights. Reconcile opening units plus acquisitions and receipts less disposals and fees paid in tokens to closing units. Investigate gaps and duplicate imports. A transaction missing from the bank feed can still be a disposal; a repeated exchange and wallet entry can be the same transaction.

Convert values to AUD at the relevant time, recording the rate, source and valuation method. For a swap, establish the value of the received property. Where that cannot be determined, the ATO permits the supported market value of the disposed crypto for the capital proceeds. If neither is supported, return Needs Input. Missing price data is not evidence of nil value. [ATO, swaps](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-to-crypto-exchange-or-swap); [AUD valuation](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-asset-transactions).

### 2. Identify the asset, event, character and time

| Transaction or receipt | Treatment and conditions | Primary source |
|---|---|---|
| Sell for fiat, swap, spend or gift an investment asset | Identify the disposal and event time; a swap disposes of the old asset and acquires a new asset. Gifts require the applicable market-value substitution rule | [ATO transactions](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-asset-transactions); [ITAA 1997 ss 104-10 and 116-30](https://www.legislation.gov.au/C2004A05138/latest/text) |
| Own-wallet transfer or exchange deposit | No A1 change of ownership only where beneficial ownership stays with the same taxpayer. Establish custody rights; the label SEND or DEPOSIT is insufficient | [ITAA 1997 s 104-10(2)](https://www.legislation.gov.au/C2004A05138/latest/text) |
| Staking/consensus reward | Ordinarily income at receipt value under the described reward arrangements; retain the receipt-date acquisition value for later CGT. Determine actual receipt/derivation; a claim button is not a universal timing rule | [ATO staking and airdrops](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops) |
| Airdrop | Classify its reason and activity before deciding income. Business, services and other income-producing receipts differ from a nonbusiness unsolicited receipt, gift, windfall or hobby. Record acquisition and supported receipt value for later CGT | [ATO staking and airdrops](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops) |
| Crypto for employment or services | Determine the correct employment, business or other income category and derivation time. A valid salary sacrifice may instead be a property fringe benefit. Record the later asset basis; do not automatically put every receipt in Other income | [ATO payments](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-assets-payments-relating-to-employment-or-services); [business guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/crypto-assets-and-business/crypto-assets-used-in-business) |
| NFT creation, acquisition, sale or commission | Identify the rights represented, use and activity. Trading stock, business receipts, isolated commercial profits, capital assets and personal use differ. Creation outside a business does not establish CGT treatment; an NFT without artwork rights is not automatically a collectable | [ATO NFTs](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/non-fungible-tokens) |

Frequency, size, organisation, profit purpose, repetition and the taxpayer's conduct inform the activity classification; no one exchange label or holding period decides it. An isolated transaction can produce ordinary income without a business. Apply Division 35 before offsetting an individual's business loss against other income; its income measure, tests, exceptions and discretion are in [au-sole-trader-schedule](au-sole-trader-schedule.md). [ATO business guidance](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/crypto-assets-and-business/crypto-assets-used-in-business); [TR 92/3 paras 6-16](https://www.ato.gov.au/law/view/document?docid=TXR/TR923/NAT/ATO/00001).

**Airdrop source status.** The live ATO page updated 19 August 2026 distinguishes non-income receipts from services and other income-producing receipts. An older print/search extract saying every established-token airdrop is ordinary income does not establish the current result. TR 2026/D1 remains a draft: its exclusions include consideration exchanges, liquidity rewards, non-arm's-length arrangements and rebasing. Its proposed application for initial allocations differs from other receipts. Do not cite it as final or automatically amend a historical return. [Draft TR 2026/D1, paras 9, 16-21 and 66](https://www.ato.gov.au/law/view/document?docid=DTR/TR2026D1/NAT/ATO/00001).

### 3. Establish cost base, reduced cost base and fees

For an ordinary A1 disposal, a gain is capital proceeds exceeding cost base; a loss is reduced cost base exceeding proceeds. Proceeds between the 2 bases produce neither. Other events have their own formulas. Use [au-capital-gains](au-capital-gains.md) for the statutory elements, adjustments and event ordering. [ITAA 1997 ss 104-10, 110-25, 110-35 and 110-55](https://www.legislation.gov.au/C2004A05138/latest/text).

| Cost or amount | Control |
|---|---|
| Acquisition consideration | Record AUD consideration or the applicable substituted acquisition value, with parcel quantity and date |
| Acquisition/disposal commission or exchange fee | Include only eligible statutory costs of the relevant asset; reconcile gross consideration, fee and net settlement. Do not deduct a disposal fee from proceeds and also include it in cost base |
| Gas, approval/revocation or wallet-transfer fee | Identify the asset, event and eligible statutory element. A network payment is not automatically deductible or part of the next asset's cost base; spending a fee token may itself require a disposal calculation |
| Spread | Use the actual documented consideration; do not add a separately estimated spread already embedded in it |
| Portfolio/tax software | Distinguish investment management, private use and managing tax affairs; test any deduction separately under [au-deductions-offsets](au-deductions-offsets.md). Do not automatically capitalise it in every parcel |
| Missing acquisition records | Reconstruct records. If unresolved, mark the affected gain and dependent totals Needs Input. Missing records do not establish a zero cost base |

These are controls applying the cited statutory elements, not assurances that every fee qualifies. Keep any unsupported deduction or allocation unresolved for review.

### 4. Test exemptions, losses and discount in order

| Item | 2026-27 rule and conditions | Primary source |
|---|---|---|
| Personal-use gain threshold | First cost-base element $10,000 or less, only where the actual personal-use definition is met. The statute says '$10,000 or less'; exactly $10,000 meets only the amount test | [ITAA 1997 s 118-10(3)](https://www.legislation.gov.au/C2004A05138/latest/text) |
| Personal-use classification | Assess main use when disposed of across the ownership history. Short holding supports the facts; it is not an independent mandatory statutory condition. Investment, profit-making and business use do not become personal use merely because goods are bought | [ATO personal use](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-asset-as-a-personal-use-asset); [ITAA 1997 s 108-20](https://www.legislation.gov.au/C2004A05138/latest/text) |
| Personal-use capital loss | Disregarded, including when the gain threshold would not exempt a gain. It cannot reduce other gains or be carried forward | [ITAA 1997 s 108-20(1)](https://www.legislation.gov.au/C2004A05138/latest/text) |
| Individual/trust discount | Generally 50% for an eligible discount gain in this period, with at least 12 months between acquisition and event and all other conditions met. Exclude the acquisition and event days when testing the holding period. Trust attribution and foreign/temporary-residence rules require separate analysis | [ITAA 1997 ss 115-10, 115-25 and 115-100](https://www.legislation.gov.au/C2004A05138/latest/text); [ATO discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount) |
| Other entities | A complying superannuation entity generally uses the exact one-third discount where eligible. An ordinary company has no discount; a life insurance company's complying-superannuation-asset exception requires the CGT guide's separate conditions | [ITAA 1997 ss 115-10 and 115-100](https://www.legislation.gov.au/C2004A05138/latest/text) |
| Capital losses | Remove disregarded gains/losses first. Apply eligible current-year losses, then supported prior-year losses oldest first, before discount. Keep collectable restrictions, loss origin years and entity restrictions. Capital losses cannot offset ordinary rewards or salary | [ITAA 1997 ss 102-5, 102-10 and 108-10](https://www.legislation.gov.au/C2004A05138/latest/text); [ATO losses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/using-capital-losses-to-reduce-capital-gains) |

**Source discrepancy.** The current personal-use page says 'less than $10,000'. Section 118-10(3) is inclusive; use the statute at the boundary and record the difference. Amount alone never establishes personal use. Gift cards, fiat conversion, prepaid cards and payment intermediaries also require the page's separate conditions; spending investment returns privately does not qualify.

Compute each event before aggregation. Where the current-year loss-allocation choice exists, compare permitted allocations, including non-discount gains first. Do not subtract capital losses from an already discounted total. Preserve any exempt gain outside the loss pool and carry losses forward with their origin and restrictions. Use the CGT guide for all cross-asset losses, trust attribution and concessions.

Individual marginal rates, Medicare levy conditions and whole-return offsets belong in [au-rates-2026-27](au-rates-2026-27.md), [au-medicare-levy](au-medicare-levy.md) and [au-individual-return](au-individual-return.md). A net capital gain or an ordinary crypto receipt is an assessable component, not a final tax bill. Do not apply a flat combined marginal/Medicare rate to every client.

### 5. Treat exchange labels as prompts to inspect records

| Illustrative label | Reconciliation and classification |
|---|---|
| Coinbase BUY/SELL/CONVERT, Swyftx BUY/SELL/SWAP, CoinSpot MARKET BUY/SELL/SWAP | Establish actual quantities, gross consideration, fees, parcel and valuation; ordinary investment swaps dispose of one asset and acquire another |
| EARN/LEARN, AFFILIATE, REFERRAL, STAKING or AIRDROP | Establish the activity, entitlement and receipt character under step 2; a label alone does not establish ordinary income or exclude it |
| SEND/RECEIVE/EXTERNAL WALLET | Match both sides, fees and continuing beneficial ownership; investigate unmatched transfers |
| AUD DEPOSIT/WITHDRAWAL or withdrawal to bank | Reconcile the fiat movement to earlier activity; it does not itself replace the disposal record |
| On-chain swap, LP deposit/withdrawal, reward, bridge, NFT mint or APPROVE/REVOKE | Inspect actual rights, consideration and fees under this guide's event and boundary tables |

The labels are illustrative inherited patterns, not verified current export schemas or exchange fee schedules. Use actual exports and contract notes. No fixed CoinSpot fee rate or automatic net-proceeds convention is supported here. A buy may establish an acquisition; a sale/convert or fee-token payment can separately establish a disposal. Reconcile once for each actual event, avoiding duplicate wallet and exchange entries.

## Boundary and exception table

| Situation | Required treatment or hold | Primary source |
|---|---|---|
| Lending, borrowing or collateral | Determine whether beneficial ownership ends, replacement rights arise or liquidation disposes of an asset. Calling a transaction a loan or collateral does not prove no event. Identify the most specific A1, E2, C2 or H2 event from terms and actual operation | [ATO DeFi](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto) |
| Liquidity deposit/withdrawal and periodic DeFi reward | Apply the page's rights/asset exchange and market-value rules for deposits/withdrawals; separately classify periodic rewards as assessable income at receipt value where applicable | [ATO DeFi](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto) |
| Smart-contract wrapping/unwrapping | TD 2026/D2 proposes C2 treatment for specified lock/mint/burn/release arrangements. Check its scope, exclusions, event time and replacement basis. It remains a draft; custodian or other arrangements need their own analysis | [Draft TD 2026/D2 paras 1-5 and 8-22](https://www.ato.gov.au/law/view/document?docid=DXT/TD2026D2/NAT/ATO/00001) |
| Bridge or token migration | Establish the actual rights and operative authority; do not assume disposal, no disposal or zero basis from the label. Hold unresolved treatment as Needs Input | [ATO DeFi](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto) |
| Investor chain split | Identify whether an asset continues the original rights. A qualifying new investor asset has no receipt income and zero acquisition cost base, with a new holding period; original rights may instead end in a C2 event if no asset continues them. Business treatment differs | [ATO chain splits](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-chain-splits) |
| Lost/stolen assets | Establish ownership, permanent loss, recoverability, event date and reduced cost base. Account for insurance/compensation and test any rollover conditions separately; a falling price or temporary loss of access is insufficient | [ATO loss/theft](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/loss-or-theft-of-crypto-assets) |
| Exchange external administration | Establish the continuing asset/right, distributions and event timing. Do not realise a loss from suspended withdrawals or a devaluation alone. Partial recoveries may reduce basis or later produce gains depending on the asset and event | [ATO administration](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-exchanges-and-platforms-under-administration) |
| Mining | Determine whether a business is carried on; business-mined assets are trading stock with opening/closing stock requirements. Scale alone does not establish the character. Refer any unconfirmed nonbusiness acquisition basis or income treatment before computing | [ATO mining](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/crypto-assets-and-business/crypto-mining) |
| Margin, futures, options or another derivative | Read the contract and determine revenue/capital character, applicable instrument rules and any separate disposal of funding crypto. An isolated trade or a speculative label is not a statutory exemption. Refer unresolved instrument treatment | [TR 92/3 paras 6-16](https://www.ato.gov.au/law/view/document?docid=TXR/TR923/NAT/ATO/00001) |

The DeFi page's unwrapping example calls the burnt asset ETH. The surrounding rule and TD 2026/D2 identify the wrapped token being burnt. Follow the documented contract mechanism and record this source typo; do not treat it as proof that the underlying and wrapped tokens are one asset.

## Worked cases

All cases are hypothetical arithmetic workpapers in AUD for 2026-27. Facts, eligibility and valuations are assumed only within each case, not defaults for an actual client. No case computes a whole-return tax liability. The oa-check blocks recompute amounts; they cannot establish the factual or legal predicates.

### Case 1: Swap proceeds, fee and loss before discount

A resident individual held an investment parcel from 3 March 2023 to its swap on 15 October 2026. It cost $10,000 plus $100 eligible acquisition commission. The received tokens have supported market value $16,000. A separate $150 disposal commission is an eligible cost of the old asset only; no other acquisition cost is assumed for the new parcel. Gross gain is $5,750. Apply a supported unused prior capital loss of $500 before the eligible 50% discount: net capital gain $2,625. New tokens have a $16,000 first cost-base element and a new acquisition date. Using $15,850 net consideration as proceeds as well as adding the $150 fee to cost base would understate the gain by $150. [ITAA 1997 ss 102-5, 104-10, 110-25/35 and 115-100](https://www.legislation.gov.au/C2004A05138/latest/text); [ATO swap valuation](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-to-crypto-exchange-or-swap).

```oa-check
name: Crypto swap gross proceeds and fee counted once
inputs:
  purchase: 10000
  acquisition_fee: 100
  disposal_fee: 150
  received_value: 16000
  prior_loss: 500
steps:
  old_cost_base: purchase + acquisition_fee + disposal_fee
  gross_gain: received_value - old_cost_base
  after_losses: gross_gain - prior_loss
  net_capital_gain: after_losses * 0.5
  new_first_element: received_value
  wrong_gross_gain: received_value - disposal_fee - old_cost_base
  understatement: gross_gain - wrong_gross_gain
expected:
  old_cost_base: 10250
  gross_gain: 5750
  after_losses: 5250
  net_capital_gain: 2625
  new_first_element: 16000
  wrong_gross_gain: 5600
  understatement: 150
```

### Case 2: Personal use is a factual decision, with an inclusive amount boundary

Compare 3 resident individual's positions with disposal value $13,000 and no fees or other gains/losses. In the first, records establish genuine personal use, direct use to acquire personal goods and a first cost-base element exactly $10,000. The $3,000 gain is disregarded under s 118-10(3). In the second, the same $10,000 holding was an investment and was held for less than 12 months: the $3,000 gain is assessable without discount. In the third, genuine personal use is established but the first element is $10,001 and the asset was held for less than 12 months: the amount exemption fails and the $2,999 gain is not disregarded. The exemption cannot be chosen merely to improve the result; actual use decides. [ITAA 1997 ss 108-20, 115-25 and 118-10(3)](https://www.legislation.gov.au/C2004A05138/latest/text).

```oa-check
name: Personal use versus investment and exact threshold
inputs:
  first_element: 10000
  above_threshold: 10001
  disposal_value: 13000
steps:
  first_gain: disposal_value - first_element
  personal_disregarded: first_gain
  personal_included: first_gain - personal_disregarded
  investment_included: first_gain
  above_threshold_included: disposal_value - above_threshold
  investment_difference: investment_included - personal_included
expected:
  first_gain: 3000
  personal_disregarded: 3000
  personal_included: 0
  investment_included: 3000
  above_threshold_included: 2999
  investment_difference: 3000
```

### Case 3: A later capital loss does not cancel staking income

A resident investor receives 200 additional staking-reward tokens on 1 August 2026, each worth $2.50. The supported reward arrangement produces $500 ordinary income and a $500 acquisition basis. The investor sells all the reward tokens on 1 October 2026 for $300, with no fees or other gains/losses; the reduced cost base is also $500. The $200 capital loss cannot deduct against the $500 reward income. Carry the $200 loss forward; net capital gain is zero. A price fall without a disposal would not itself realise the loss. [ATO staking/reward basis](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops); [ITAA 1997 ss 102-10 and 104-10](https://www.legislation.gov.au/C2004A05138/latest/text).

```oa-check
name: Staking receipt income and later capital loss
inputs:
  tokens: 200
  receipt_price: 2.5
  proceeds: 300
steps:
  ordinary_income: tokens * receipt_price
  reduced_cost_base: ordinary_income
  capital_loss: reduced_cost_base - proceeds
  loss_used_against_income: 0
  ordinary_income_retained: ordinary_income - loss_used_against_income
  capital_loss_carried: capital_loss
  net_capital_gain: 0
expected:
  ordinary_income: 500
  reduced_cost_base: 500
  capital_loss: 200
  loss_used_against_income: 0
  ordinary_income_retained: 500
  capital_loss_carried: 200
  net_capital_gain: 0
```

### Case 4: Equal airdrop value, different receipt character

Compare 2 documented resident nonbusiness receipts of 200 established tokens worth $5 each on 1 August 2026. One is unsolicited, with no services, business or other income-producing activity. The other is consideration for services outside a business. Under the current ATO guidance, the first has no ordinary income on receipt; the second has $1,000. Both have a supported $1,000 first cost-base element. Each parcel is later sold on capital account on 1 December 2026 for $1,200 with no fees, other gains/losses or discount. The capital gain is $200 in each case. The included ordinary-income-plus-capital-gain components are $200 versus $1,200; this is not final taxable income or tax. [ATO staking and airdrops, receipt character and valuation](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops). Do not extend these facts to the draft's excluded arrangements or an unverified historical period.

```oa-check
name: Unsolicited airdrop versus services reward
inputs:
  tokens: 200
  receipt_price: 5
  proceeds: 1200
steps:
  receipt_value: tokens * receipt_price
  unsolicited_income: 0
  services_income: receipt_value
  each_capital_gain: proceeds - receipt_value
  unsolicited_components: unsolicited_income + each_capital_gain
  services_components: services_income + each_capital_gain
  difference: services_components - unsolicited_components
expected:
  receipt_value: 1000
  unsolicited_income: 0
  services_income: 1000
  each_capital_gain: 200
  unsolicited_components: 200
  services_components: 1200
  difference: 1000
```

### Case 5: A supported investor chain split has a real zero basis

A resident individual receives a qualifying new investor asset in a chain split on 21 August 2025; the original asset continues with its existing $10,000 basis. The new asset is sold on 15 September 2026 for $4,200, with no fees, other gains/losses or restrictions. Its zero acquisition cost base is established by this chain-split fact pattern, not by missing records. The new asset's gross gain is $4,200 and eligible discounted net capital gain $2,100. Its holding period starts at the split. Do not transfer the original $10,000 basis to it, and do not use this result for business stock or a migration where the original rights end. [ATO chain splits](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-chain-splits).

```oa-check
name: Investor chain split new asset basis
inputs:
  proceeds: 4200
  new_basis: 0
  original_basis: 10000
steps:
  receipt_income: 0
  new_gross_gain: proceeds - new_basis
  net_capital_gain: new_gross_gain * 0.5
  original_basis_retained: original_basis
expected:
  receipt_income: 0
  new_gross_gain: 4200
  net_capital_gain: 2100
  original_basis_retained: 10000
```

### Case 6: Conditional wrapping and unwrapping in one income year

For this illustration only, a qualified reviewer confirms the actual arrangement falls within the smart-contract pattern described in draft TD 2026/D2 and adopts its proposed C2 analysis for a resident investor. ETH held since 2019 has $10,000 cost base. It is wrapped on 1 August 2026 into WETH worth $30,000: gain $20,000, with new WETH basis $30,000. On 1 November 2026 the WETH is burnt to receive new ETH worth $28,000: reduced cost base $30,000, loss $2,000 and new ETH basis $28,000. No fees, other gains/losses or restrictions apply. Apply the $2,000 current-year loss before discounting the eligible old-ETH gain: net capital gain $9,000. Discounting first and then subtracting the loss would incorrectly give $8,000. This conditional case is not legal approval of the draft or a default for bridges, custodians or an unidentified protocol. [ATO DeFi](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto); [draft TD 2026/D2 paras 8-22](https://www.ato.gov.au/law/view/document?docid=DXT/TD2026D2/NAT/ATO/00001).

```oa-check
name: Conditional wrapping loss before discount
inputs:
  original_cost: 10000
  wrapping_value: 30000
  unwrapping_value: 28000
steps:
  wrapping_gain: wrapping_value - original_cost
  weth_basis: wrapping_value
  unwrapping_loss: weth_basis - unwrapping_value
  gain_after_loss: wrapping_gain - unwrapping_loss
  net_capital_gain: gain_after_loss * 0.5
  new_eth_basis: unwrapping_value
  wrong_net_gain: wrapping_gain * 0.5 - unwrapping_loss
  understatement: net_capital_gain - wrong_net_gain
expected:
  wrapping_gain: 20000
  weth_basis: 30000
  unwrapping_loss: 2000
  gain_after_loss: 18000
  net_capital_gain: 9000
  new_eth_basis: 28000
  wrong_net_gain: 8000
  understatement: 1000
```

### Missing records or suspended withdrawals

A wallet shows a disposal but the acquisition parcel cannot yet be reconstructed. Do not assign zero basis or omit it: record the event and return Needs Input for its gain and dependent annual totals. Separately, an exchange suspends withdrawals but a claim against it still exists. Do not realise a capital loss from the suspension alone. Obtain the rights, administration and recovery evidence before choosing an event and date. These are qualitative holds, not additional recomputing cases.

## When to refuse or refer

| Code | Trigger | Required response |
|---|---|---|
| R-AU-CRYPTO-RECORDS | Parcel, ownership, event date or valuation cannot be supported after reconstruction | Hold the affected gain and dependent totals as Needs Input; list the missing records |
| R-AU-CRYPTO-CHARACTER | Capital/revenue, services/employment, personal use, residency, source or TAP treatment is unresolved | Do not assume taxable or exempt; obtain the missing facts and qualified classification |
| R-AU-CRYPTO-RIGHTS | DeFi, bridge, migration, custody, NFT or derivative rights lack an established event and authority | Refer the arrangement and retain its transactions/holdings in reconciliation; do not silently omit them |
| R-AU-CRYPTO-LOSS | Permanent loss, administration event or compensation remains unresolved | Hold the loss and dependent totals; a value fall or suspension is insufficient |
| R-AU-CRYPTO-PERIOD | Historical source operation, draft status, 2027 transition or approved filing fields are unresolved | Establish the operative period and source before finalising that position |
| R-AU-CRYPTO-RELIANCE | Asked to file, pay or present the result as definitive without qualified review | Provide the reviewable workpaper and unresolved items; do not claim professional sign-off |

**Permitted defaults.** A blank fee, cost, date, residence or market value is not zero. No default establishes a legal event, exemption, income character or eligibility. An explicitly requested sensitivity may use disclosed hypothetical inputs, but remains separate from the supported position. Record each refusal as cleared or fired, every assumption and each required reviewer decision.

**Reviewer attention.** Flag unmatched transfers, duplicates, quantity differences, material unsupported valuations, inconsistent parcel selections, changed rights, unconfirmed source periods and any difference between income recognition and cash realised. A materiality threshold for the reviewer is not authority to delete an event or suppress a refusal. Do not make a final monetary result dependent on an undisclosed assumption.

**Delivery.** Produce a transaction worksheet containing asset/right, beneficial owner, counterparty identity/address where applicable, event/time, quantity, parcel, AUD proceeds, cost and reduced cost base, fee allocation, classification, loss origin, discount eligibility, source and unresolved dependencies. Supply a separate income ledger and holdings reconciliation. The brief records taxpayer/period, source/read scopes, assumptions, draft positions, reviewer decisions and comparative impacts. The action list names who supplies each missing item and its verified deadline. Any sensitivity must be visibly separated from filing totals.

## Filing and payment

1. Confirm the taxpayer, return period and capacity. Use myGov-linked ATO online services/myTax for a supported individual return or the registered agent's approved channel. Company, trust and fund returns use their own schedules. The ATO crypto CGT page links current individual myTax capital-gain instructions and paper Item 18 for the **2026 return**; that is not verification of the 2026-27 form or its software fields. [ATO reporting routes](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/how-to-work-out-and-report-cgt-on-crypto).
2. Transfer supported capital gain, net capital gain and loss carry-forward workpapers to the matching approved fields only after checking that period's instructions. Establish any CGT schedule requirement. Map ordinary receipts to the correct employment, business or other-income category; staking guidance names Other income, but that does not settle every services receipt's field. Reconcile each amount to the ledgers and avoid double inclusion of the same receipt value.
3. Obtain qualified review, resolve refusals and validate the approved form/software. Preserve lodgment confirmation, the submitted version and its reconciliation. Do not automate final filing fields that have not been verified for the requested year.
4. Establish the actual lodgment deadline, agent programme or extension under [au-lodgment-deadlines-penalties](au-lodgment-deadlines-penalties.md). The old generic 31 October statement does not establish every taxpayer's due date. After processing, check the notice of assessment, payment reference and payment due date. Lodgment and payment dates differ. No payment or lodgment is executed by this guide.
5. Keep crypto records for 5 years from the latest relevant preparation/obtaining, completed transaction/act and CGT-event year, and long enough to cover an assessment's amendment period, usually 2 or 4 years. Keep evidence in English or translatable to English, including acquisition records while holdings continue and loss/election records needed in later years. [ATO record retention](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records).

## Completion checklist

- [ ] Entity, residence, period, activity and actual rights are established.
- [ ] Every exchange/wallet feed is reconciled once to holdings and supported parcels, fees and AUD values.
- [ ] Ordinary income, exempt/disregarded amounts, capital gains/losses and trading stock are separately classified.
- [ ] Personal-use, loss restrictions, holding period and residency conditions are evidenced; losses precede discounts.
- [ ] No zero basis, nil fee, no-event, exemption or liability was invented from missing facts.
- [ ] Draft sources, historical periods and future reforms have their own applicable treatment or an explicit hold.
- [ ] Worksheet, income ledger, reconciliation, brief and action list expose every unresolved dependency and reviewer decision.
- [ ] Approved return fields, schedule, deadline, lodgment confirmation and later assessment/payment steps are verified for the actual period before use.
- [ ] Qualified Australian review is recorded for the client's facts. This Tier 2 guide remains pending review.

## Sources

| Source | URL | Read on |
|---|---|---|
| Crypto transactions and AUD valuation | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-asset-transactions) | 2 November 2026: disposal categories and AUD conversion |
| Crypto swaps | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-to-crypto-exchange-or-swap) | 2 November 2026: received/disposed asset valuation alternatives and examples |
| Crypto and tax residency | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-asset-transactions-and-tax-residency) | 2 November 2026: resident/temporary/foreign income source, TAP and I1 choice |
| Personal use | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-asset-as-a-personal-use-asset) | 2 November 2026: use/history, amount language, losses, intermediaries and examples; threshold conflict with s 118-10(3) recorded above |
| Staking and airdrops | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/staking-rewards-and-airdrops) | 2 November 2026: receipt character, valuation, hobby/services/unsolicited examples and draft reference; page updated 19 August 2026 |
| TR 2026/D1 | [Draft ruling](https://www.ato.gov.au/law/view/document?docid=DTR/TR2026D1/NAT/ATO/00001) | 2 November 2026: selected scope/exclusions, paras 11-21 and 66; not a final ruling or full ruling review |
| DeFi and wrapping | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/decentralised-finance-and-wrapping-crypto) | 2 November 2026: lending/rights, liquidity, periodic rewards and wrapping/unwrapping; token-name typo recorded above |
| TD 2026/D2 | [Draft determination](https://www.ato.gov.au/law/view/document?docid=DXT/TD2026D2/NAT/ATO/00001) | 2 November 2026: selected paras 1-5 and 8-22, mechanism, exclusions, event timing and proposed effect; not final |
| NFTs | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/non-fungible-tokens) | 2 November 2026: rights/use, business/commissions, personal use, collectables example and GST routing |
| Chain splits | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/crypto-chain-splits) | 2 November 2026: new/continuing rights, investor basis/holding period, no-continuation C2 and business qualification |
| Loss/theft | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/loss-or-theft-of-crypto-assets) | 2 November 2026: evidence/recoverability, reduced cost base, compensation and potential rollover |
| Exchange administration | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-exchanges-and-platforms-under-administration) | 2 November 2026: continuing rights, finalisation and staged recovery examples |
| Employment/services payments | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/transactions-acquiring-and-disposing-of-crypto-assets/crypto-assets-payments-relating-to-employment-or-services) | 2 November 2026: direct/third-party receipts, valuation and later asset basis |
| Mining | [ATO](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/crypto-assets-and-business/crypto-mining) | 2 November 2026: business/trading stock and GST routing; no universal hobby basis established |
| Crypto in business | [ATO](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/crypto-assets-and-business/crypto-assets-used-in-business) | 2 November 2026: investment/stock, business indicators, salary sacrifice and services; page updated 1 October 2026 |
| Isolated commercial profits | [TR 92/3](https://www.ato.gov.au/law/view/document?docid=TXR/TR923/NAT/ATO/00001) | 2 November 2026: selected paras 5-9 and 13-16; not a full ruling or derivative review |
| Crypto CGT reporting | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/how-to-work-out-and-report-cgt-on-crypto) | 2 November 2026: event/method and current filing routes; its 2026 form link is not verification of a 2027 form |
| Crypto records | [ATO](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/keeping-crypto-records) | 2 November 2026: records/reconstruction and retention, read during the preceding CGT check |
| Current ITAA 1997 | [Compilation 268, Volume 3](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) | 2 November 2026: selected ss 102-5, 104-10, 108-10/20, 110-25/35/55, 115-10/25/100, 116-30 and 118-10/20 in current compilation; not the whole Act. Identity C2026C00471, in force 1 October to 1 December 2026, checked through the official API |
| CGT discount and losses | [ATO discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount); [losses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/using-capital-losses-to-reduce-capital-gains) | 2 November 2026: holding period/entity/residence and current/prior loss order during the preceding CGT check |

**Revision 1.8, 2 November 2026.** Reconciled selected crypto primary sources, replaced blanket protocol/NFT/mining and fee assumptions, separated employment/business and capital treatment, retained uncertain positions as holds and added 6 recomputing cases. Current source conflicts and draft status are explicit. This is not whole-law or client eligibility certification.

Not yet confirmed: Qualified Australian sign-off, full historical source operation and actual taxpayer eligibility remain outstanding. Approved 2026-27 forms, exact field/box identifiers, schedule triggers, software transfer precision and individual deadlines need period-specific verification before filing. Current exchange export schemas/fee schedules and blanket FIFO/LIFO approval are unverified; the inherited fixed CoinSpot 0.1% and automatic next-transaction gas allocation were unsupported. The former universal zero-basis hobby-mining/migration rules, automatic CGT for every nonbusiness NFT creator and generic one-off-derivative exception are not established by the sources read; these positions require actual facts and specialist authority. Division 775 classification for stablecoins/other tokens is not settled by the Bitcoin determinations. Draft TR 2026/D1 and TD 2026/D2, initial-allocation historical application, excluded/rebasing arrangements, mixed residence and 2027 transitions must not be presented as final law. Actual contracts, valuations, loss restrictions, source amendments from 1 December 2026 and approved return procedures remain review dependencies.

> Contributed by Ryan Duguid.

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
