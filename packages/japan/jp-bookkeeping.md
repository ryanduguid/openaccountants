---
name: jp-bookkeeping
description: >
  Use this skill whenever asked about bookkeeping or journal entries for a self-employed individual in Japan. Trigger on phrases like "bookkeeping Japan", "仕訳", "journal entry", "帳簿", "double-entry bookkeeping", "複式簿記", "general ledger", "勘定科目", "chart of accounts", "経費の記帳", "CSV import", "receipt recording", "レシート", "bank statement classification", "消費税区分", "tax classification", "家事按分", "business-personal split", "depreciation entry", "減価償却", "trial balance", "残高試算表", "settlement entries", "決算整理仕訳", or any question about recording transactions, classifying expenses, or maintaining books for a Japanese sole proprietorship. This skill covers the chart of accounts, journal entry patterns, consumption tax classification, CSV/receipt import workflows, and settlement adjustments. ALWAYS read this skill before touching any Japanese bookkeeping work.
version: 1.0
jurisdiction: JP
tax_year: 2025
category: international
depends_on:
  - jp-income-tax
  - jp-consumption-tax
---

# Japan Bookkeeping (帳簿記帳) -- Self-Employed Skill v1.0

> **Based on work by [Kazuki Nagata (@kazukinagata)](https://github.com/kazukinagata/shinkoku)**, licensed under MIT. Adapted for the OpenAccountants format.

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Japan (日本) |
| Bookkeeping Standard | Double-entry (複式簿記) for blue return JPY 650,000 deduction |
| Fiscal Year | Calendar year (January 1 -- December 31) |
| Currency | JPY only |
| Legislation | Income Tax Act (所得税法), Consumption Tax Act (消費税法) |
| Tax Authority | National Tax Agency (国税庁 NTA) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Japanese 税理士 (Zeirishi) |
| Skill version | 1.0 |

### Why This Matters

| Bookkeeping Method | Blue Return Deduction | Requirements |
|---|---|---|
| Double-entry (複式簿記) + e-Tax | JPY 650,000 | Full general ledger, P/L, B/S, e-Tax filing |
| Double-entry + paper filing | JPY 550,000 | Full general ledger, P/L, B/S |
| Simplified bookkeeping (簡易簿記) | JPY 100,000 | Cash book, expense ledger |
| White return (白色申告) | JPY 0 | Minimal records |

---

## Section 2 -- Chart of Accounts (勘定科目マスタ)

### Account Code Structure

| Range | Category | Japanese |
|---|---|---|
| 1xxx | Assets | 資産 |
| 2xxx | Liabilities | 負債 |
| 3xxx | Equity | 純資産 |
| 4xxx | Revenue | 収益 |
| 5xxx | Expenses | 費用 |

### 1xxx -- Assets (資産)

#### Current Assets (流動資産)

| Code | Account Name | Japanese | Usage |
|---|---|---|---|
| 1001 | Cash | 現金 | Petty cash on hand |
| 1002 | Ordinary deposit | 普通預金 | Business bank account |
| 1003 | Checking deposit | 当座預金 | Business checking account |
| 1004 | Time deposit | 定期預金 | Business fixed deposit |
| 1010 | Accounts receivable | 売掛金 | Invoiced but unpaid sales |
| 1020 | Notes receivable | 受取手形 | Received promissory notes |
| 1030 | Inventory | 棚卸資産 | Stock, work-in-progress |
| 1040 | Advance payments | 前払金 | Prepayments for goods/services |
| 1041 | Prepaid expenses | 前払費用 | Insurance/rent paid in advance |
| 1050 | Temporary payments | 立替金 | Amounts paid on behalf of others |
| 1060 | Suspense payments | 仮払金 | Unclassified payments pending |
| 1070 | Other receivables | 未収入金 | Non-trade receivables |
| 1080 | Loans receivable | 貸付金 | Loans to others |
| 1090 | Provisional consumption tax | 仮払消費税 | Input CT paid (general method only) |

#### Fixed Assets (固定資産)

| Code | Account Name | Japanese | Useful Life (typical) |
|---|---|---|---|
| 1100 | Buildings | 建物 | 22-47 years |
| 1101 | Building fixtures | 建物附属設備 | 3-18 years |
| 1110 | Machinery | 機械装置 | 4-17 years |
| 1120 | Vehicles | 車両運搬具 | 6 years (standard) |
| 1130 | Tools and equipment | 工具器具備品 | 4-15 years |
| 1140 | Land | 土地 | Not depreciable |
| 1150 | Software | ソフトウェア | 3-5 years |
| 1160 | Lump-sum depreciation assets | 一括償却資産 | 3 years (uniform) |

#### Owner's Account (事業主勘定)

| Code | Account Name | Japanese | Usage |
|---|---|---|---|
| 1200 | Owner's draws | 事業主貸 | Business funds used personally |

### 2xxx -- Liabilities (負債)

| Code | Account Name | Japanese | Usage |
|---|---|---|---|
| 2001 | Accounts payable | 買掛金 | Unpaid purchases |
| 2010 | Notes payable | 支払手形 | Issued promissory notes |
| 2020 | Short-term borrowings | 短期借入金 | Loans due within 1 year |
| 2030 | Accrued expenses | 未払金 | Unpaid operating expenses |
| 2031 | Accrued liabilities | 未払費用 | Accrued but unpaid expenses |
| 2040 | Advance receipts | 前受金 | Payments received before delivery |
| 2050 | Withholding deposits | 預り金 | Withheld income tax, social insurance |
| 2060 | Suspense receipts | 仮受金 | Unclassified receipts pending |
| 2070 | Accrued consumption tax | 未払消費税 | CT due from final return |
| 2080 | Accrued business tax | 未払事業税 | Enterprise tax payable |
| 2100 | Long-term borrowings | 長期借入金 | Loans due after 1 year |

### 3xxx -- Equity (純資産)

| Code | Account Name | Japanese | Usage |
|---|---|---|---|
| 3001 | Capital | 元入金 | Opening capital (adjusted at year-start) |
| 3010 | Owner's contributions | 事業主借 | Personal funds used for business |
| 3020 | Pre-deduction income | 控除前所得金額 | Blue return pre-deduction income |

### 4xxx -- Revenue (収益)

| Code | Account Name | Japanese | CT Classification | Usage |
|---|---|---|---|---|
| 4001 | Sales | 売上 | Taxable (課税) | Primary business revenue |
| 4010 | Sales returns/discounts | 売上値引・戻り | Taxable | Returns, discounts |
| 4100 | Interest income | 受取利息 | Non-taxable (非課税) | Bank interest |
| 4110 | Miscellaneous income | 雑収入 | Taxable | Non-core business income |
| 4120 | Personal consumption | 家事消費等 | Taxable | Self-consumption of business goods |

### 5xxx -- Expenses (費用)

| Code | Account Name | Japanese | CT Classification | Notes |
|---|---|---|---|---|
| 5001 | Purchases | 仕入 | Taxable | Cost of goods |
| 5100 | Taxes and dues | 租税公課 | Out of scope | Business tax, stamps, property tax |
| 5110 | Packing and shipping | 荷造運賃 | Taxable (10%) | |
| 5120 | Utilities | 水道光熱費 | Taxable (10%) | Home office: apportion |
| 5130 | Travel and transportation | 旅費交通費 | Taxable (10%) | IC card records acceptable |
| 5140 | Communication | 通信費 | Taxable (10%) | Phone, internet; apportion if mixed |
| 5150 | Advertising | 広告宣伝費 | Taxable (10%) | |
| 5160 | Entertainment | 接待交際費 | Taxable (10%) | Document attendees and purpose |
| 5170 | Insurance | 損害保険料 | Non-taxable | Business insurance only |
| 5180 | Repairs | 修繕費 | Taxable (10%) | |
| 5190 | Consumables | 消耗品費 | Taxable (10%) | Items under JPY 100,000 |
| 5200 | Depreciation | 減価償却費 | Out of scope | Year-end adjustment entry |
| 5210 | Welfare | 福利厚生費 | Taxable | Not for sole proprietor personally |
| 5220 | Salaries | 給料賃金 | Out of scope | Employee wages |
| 5230 | Subcontracting | 外注工賃 | Taxable (10%) | |
| 5240 | Interest expense | 利子割引料 | Non-taxable | Loan interest |
| 5250 | Rent | 地代家賃 | Taxable (10%) | Business premises; residential is non-taxable |
| 5260 | Bad debts | 貸倒金 | Out of scope | |
| 5270 | Miscellaneous | 雑費 | Taxable (10%) | Bank fees, minor items |
| 5280 | Family employee wages | 専従者給与 | Out of scope | Blue return family employees |
| 5290 | Books and subscriptions | 新聞図書費 | Taxable | Newspapers (subscription) at 8% reduced |
| 5300 | Training | 研修費 | Taxable (10%) | |
| 5310 | Service fees | 支払手数料 | Taxable (10%) | Bank transfer fees, payment processor fees |
| 5320 | Vehicle expenses | 車両費 | Taxable (10%) | Fuel, parking, tolls |
| 5330 | Meeting expenses | 会議費 | Taxable | |
| 5340 | Membership dues | 諸会費 | Taxable (10%) | Industry associations |
| 5350 | Lease payments | リース料 | Taxable (10%) | |
| 5360 | Office supplies | 事務用品費 | Taxable (10%) | |
| 5370 | Software expenses | ソフトウェア費 | Taxable (10%) | SaaS subscriptions under JPY 100,000 |

---

## Section 3 -- Consumption Tax Classification Rules

### Four Requirements for Taxability

A transaction is subject to consumption tax only if ALL four conditions are met:

1. **Domestic transaction** -- occurs within Japan
2. **Performed by a business** -- as part of business operations
3. **For consideration** -- payment is received/made
4. **Transfer of goods, lease of assets, or provision of services**

### Classification Decision Tree

```
Is the transaction domestic? ─── No ──→ Out of scope (不課税) or Export exempt (免税)
        │
       Yes
        ↓
Is it by a business for consideration? ─── No ──→ Out of scope (不課税)
        │
       Yes
        ↓
Is it listed as non-taxable (非課税)? ─── Yes ──→ Non-taxable
        │
       No
        ↓
Taxable (課税) at standard 10% or reduced 8%
```

### Reduced Rate (8%) Items

| Category | Examples | Rate |
|---|---|---|
| Food and beverages (takeout) | Groceries, takeout meals, deliveries | 8% |
| Subscription newspapers | Print newspapers delivered 2+ times/week | 8% |

**NOT reduced rate (10%):** Alcohol, dine-in meals, catering, e-newspapers, bottled water from tap.

### Home Office Apportionment (家事按分)

These accounts commonly require business-personal splitting:

| Account | Apportionment Method |
|---|---|
| Utilities (水道光熱費 5120) | Floor area ratio or time-based ratio |
| Communication (通信費 5140) | Business usage time ratio |
| Rent (地代家賃 5250) | Floor area ratio |
| Vehicle expenses (車両費 5320) | Business mileage ratio |

**NTA guidelines:** The apportionment method must be reasonable, documented, and applied consistently year to year. Typical range for full-time home workers: 20-50%.

---

## Section 4 -- Common Journal Entry Patterns

### 4.1 Revenue Entries

**Client payment received (売上入金):**
```
Debit:  1002 普通預金 (Ordinary deposit)     110,000
Credit: 4001 売上 (Sales)                    110,000
Memo: ○○社 Web制作費 Invoice #2025-001  CT: 10%
```

**Invoiced but unpaid (売掛金計上):**
```
Debit:  1010 売掛金 (Accounts receivable)    110,000
Credit: 4001 売上 (Sales)                    110,000
Memo: ○○社 コンサル料 Invoice #2025-002  CT: 10%
```

**Subsequent collection of receivable:**
```
Debit:  1002 普通預金                        110,000
Credit: 1010 売掛金                          110,000
Memo: ○○社 Invoice #2025-002 入金
```

**Payment with withholding (源泉徴収あり):**
```
Debit:  1002 普通預金                         89,790
Debit:  1070 未収入金 (Withholding credit)    10,210
Credit: 4001 売上                            100,000
Memo: △△社 デザイン料 10.21% withholding  CT: 10%
```

### 4.2 Expense Entries

**Expense from business account (事業用口座から):**
```
Debit:  5190 消耗品費 (Consumables)            5,500
Credit: 1002 普通預金                          5,500
Memo: Amazon ワイヤレスキーボード  CT: 10%
```

**Expense paid from personal funds (事業主借):**
```
Debit:  5130 旅費交通費 (Travel)               1,200
Credit: 3010 事業主借 (Owner's contribution)   1,200
Memo: JR 新宿→渋谷 Client meeting roundtrip  CT: 10%
```

**Business funds used personally (事業主貸):**
```
Debit:  1200 事業主貸 (Owner's draw)          50,000
Credit: 1002 普通預金                         50,000
Memo: Personal living expense withdrawal
```

**SaaS subscription (月額サービス):**
```
Debit:  5370 ソフトウェア費 (Software)         2,200
Credit: 1002 普通預金                          2,200
Memo: Adobe Creative Cloud monthly  CT: 10%
```

**Rent with home office apportionment (家事按分あり):**
```
Debit:  5250 地代家賃 (Rent) -- 30% business   36,000
Debit:  1200 事業主貸 -- 70% personal          84,000
Credit: 1002 普通預金                         120,000
Memo: 家賃 1月分 按分率30%  CT: 10% (business portion)
```

### 4.3 Social Insurance & Tax Payments

**National pension (国民年金):**
```
Debit:  1200 事業主貸                         16,590
Credit: 1002 普通預金                         16,590
Memo: 国民年金保険料 4月分
```
*National pension is an income deduction (所得控除), NOT a business expense. Record as owner's draw.*

**National health insurance (国民健康保険):**
```
Debit:  1200 事業主貸                         35,000
Credit: 1002 普通預金                         35,000
Memo: 国民健康保険料 1期分
```
*Same treatment -- income deduction, not business expense.*

**Income tax / resident tax payments:**
```
Debit:  1200 事業主貸                        150,000
Credit: 1002 普通預金                        150,000
Memo: 所得税 確定申告分 -- not deductible
```

### 4.4 Fixed Asset Entries

**Asset purchase under JPY 100,000 (少額減価償却):**
```
Debit:  5190 消耗品費                         88,000
Credit: 1002 普通預金                         88,000
Memo: Printer purchase -- immediate expense  CT: 10%
```

**Asset purchase JPY 100,000--299,999 (blue return special expensing):**
```
Debit:  5200 減価償却費                      250,000
Credit: 1130 工具器具備品                    250,000
Memo: MacBook Air -- blue return immediate expensing (aggregate ≤ JPY 3M)
```

**Asset purchase JPY 300,000+ (standard depreciation):**
```
Purchase:
Debit:  1130 工具器具備品                    350,000
Credit: 1002 普通預金                        350,000
Memo: Desktop PC  CT: 10%

Year-end depreciation (declining balance, 4-year, rate 0.500):
Debit:  5200 減価償却費                      175,000
Credit: 1130 工具器具備品                    175,000
Memo: PC depreciation Y1 (350,000 × 0.500)
```

---

## Section 5 -- Depreciation Rules (減価償却)

### Methods Available

| Method | Japanese | Default For |
|---|---|---|
| Declining balance | 定率法 | Most assets for sole proprietors |
| Straight-line | 定額法 | Buildings acquired after April 2016 |

### Common Useful Lives and Rates

| Asset | Useful Life | Declining Balance Rate | Straight-Line Rate |
|---|---|---|---|
| Personal computers | 4 years | 0.500 | 0.250 |
| Servers | 5 years | 0.400 | 0.200 |
| Office furniture (metal) | 15 years | 0.133 | 0.067 |
| Office furniture (wood) | 8 years | 0.250 | 0.125 |
| Motor vehicles (standard) | 6 years | 0.333 | 0.167 |
| Software (purchased) | 5 years | 0.400 | 0.200 |
| Software (internally developed) | 3 years | 0.667 | 0.333 |

### Expensing Thresholds

| Acquisition Cost | Treatment |
|---|---|
| Under JPY 100,000 | Expense immediately (少額減価償却資産) |
| JPY 100,000 -- 199,999 | Option: 3-year uniform depreciation (一括償却資産) |
| Under JPY 300,000 (blue return) | Option: immediate expensing, aggregate limit JPY 3,000,000/year |
| JPY 300,000+ | Standard depreciation over useful life |

### Rounding

All depreciation amounts are rounded down to the nearest JPY 1 (1円未満切捨て). Business-use apportionment is also rounded down to JPY 1.

---

## Section 6 -- Settlement Adjustments (決算整理仕訳)

At year-end (December 31), record the following adjustments:

### 6.1 Depreciation (減価償却)

Record annual depreciation for all fixed assets. See Section 5 for rates.

### 6.2 Prepaid Expenses (前払費用)

If insurance, rent, or subscriptions are paid in advance beyond December 31:
```
Debit:  1041 前払費用                         XX,XXX
Credit: 5250 地代家賃 (or other expense)      XX,XXX
Memo: January rent paid in December -- reverse to next year
```

### 6.3 Accrued Expenses (未払費用)

For expenses incurred but not yet paid by December 31:
```
Debit:  5120 水道光熱費                       XX,XXX
Credit: 2031 未払費用                         XX,XXX
Memo: December electricity bill -- to be paid in January
```

### 6.4 Inventory (棚卸)

If you hold physical inventory, count and value it at December 31:
```
Year-end inventory:
Debit:  1030 棚卸資産                        XXX,XXX
Credit: 5001 仕入 (Purchases)               XXX,XXX
Memo: Closing inventory valuation
```

### 6.5 Bad Debt Allowance (貸倒引当金)

Blue return filers may set aside an allowance for doubtful accounts (up to 5.5% of receivables for certain businesses):
```
Debit:  5260 貸倒金                          XX,XXX
Credit: (Allowance account)                  XX,XXX
Memo: Bad debt allowance year-end
```

### 6.6 Consumption Tax Settlement (消費税の精算)

For general method (本則課税) taxpayers, settle provisional CT accounts:
```
Debit:  2070 未払消費税                      XXX,XXX
Credit: 1090 仮払消費税                      XXX,XXX
Memo: CT settlement -- net payable transferred
```

---

## Section 7 -- Data Import Workflows

### 7.1 CSV Bank Statement Import

**Workflow:**
1. Export CSV from your bank (see bank formats in `jp-income-tax` skill, Section 8)
2. Identify columns: date (日付/取引日), description (摘要/内容), debit (支払/出金), credit (入金/預入), balance (残高)
3. Classify each transaction using the pattern library in `jp-income-tax` skill, Section 3
4. Generate journal entries and review before recording
5. Check for duplicates if importing from multiple sources

### 7.2 Receipt / Invoice Processing

**For each receipt or invoice:**
1. Extract: date, vendor, amount, tax amount, item description
2. Determine account code based on expense category
3. Check for qualified invoice elements (T-number, rate-separated amounts) if claiming input tax credit
4. Record the journal entry
5. Store the receipt image/PDF for record retention (7 years for blue return filers)

### 7.3 Account Code Estimation Rules

| Transaction Description Pattern | Suggested Account |
|---|---|
| 電車, バス, タクシー, JR, 新幹線 | 5130 旅費交通費 |
| Amazon, ヨドバシ, ビックカメラ | 5190 消耗品費 or 5360 事務用品費 |
| ドコモ, au, ソフトバンク, 楽天モバイル | 5140 通信費 |
| NURO, フレッツ, インターネット | 5140 通信費 |
| 東京電力, ガス, 水道 | 5120 水道光熱費 |
| 家賃, 賃料, オフィス | 5250 地代家賃 |
| Adobe, Microsoft, Google Workspace | 5370 ソフトウェア費 |
| Google Ads, Meta Ads, 広告 | 5150 広告宣伝費 |
| 振込手数料, 決済手数料 | 5310 支払手数料 |
| 飲食, レストラン, 接待 | 5160 接待交際費 or 5330 会議費 |

---

## Section 8 -- Validation Checklist

Before closing the books for the year, verify:

- [ ] All bank transactions reconcile with the general ledger
- [ ] Accounts receivable balance matches outstanding invoices
- [ ] Accounts payable balance matches unpaid bills
- [ ] Depreciation is recorded for all fixed assets
- [ ] Home office apportionment is consistent with prior year
- [ ] National pension and health insurance are NOT recorded as business expenses
- [ ] Owner's draws and contributions balance is reasonable
- [ ] Consumption tax classification is correct for all entries
- [ ] Inventory is counted and valued (if applicable)
- [ ] Trial balance (残高試算表) debits = credits
- [ ] B/S: total assets = total liabilities + equity

---

## Section 9 -- Record Retention Requirements

| Document Type | Retention Period | Notes |
|---|---|---|
| General ledger (総勘定元帳) | 7 years | Blue return requirement |
| Journal (仕訳帳) | 7 years | Blue return requirement |
| Cash book (現金出納帳) | 7 years | |
| Invoices issued (請求書控え) | 7 years | |
| Invoices received (請求書) | 7 years | Must retain qualified invoices for input tax credit |
| Receipts (領収書) | 7 years | |
| Bank statements (通帳) | 7 years | |
| Contracts (契約書) | 7 years | |
| Withholding certificates (源泉徴収票) | 7 years | |

**Electronic bookkeeping (電子帳簿保存法):** From January 2024, electronic transaction records (e-invoices, e-receipts) must be stored electronically. Paper printouts alone are no longer sufficient for electronic transactions.

---

## PROHIBITIONS

- NEVER record national pension (国民年金) or health insurance (国民健康保険) as a business expense -- they are income deductions (所得控除), recorded through owner's draws (事業主貸)
- NEVER record income tax or resident tax as a business expense -- they are not deductible
- NEVER allow a debit/credit mismatch in any journal entry
- NEVER use an account code not in the chart of accounts without explicit confirmation
- NEVER skip the home office apportionment for mixed-use expenses
- NEVER claim input tax credit (仕入税額控除) without a qualified invoice (from October 2023 onward, subject to transitional measures)
- NEVER apply the 8% reduced rate to dine-in meals, alcohol, or catering
- NEVER auto-record entries without explicit confirmation from the taxpayer
- NEVER present bookkeeping outputs as final -- all entries should be reviewed by a 税理士

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a 税理士 or equivalent licensed practitioner in Japan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
