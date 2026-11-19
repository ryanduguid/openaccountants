---
name: xero-integration
version: 1.1.0
category: integration
description: >
  Integration skill for Xero accounting software exports. Activate when the user uploads a Xero bank statement CSV,
  Xero invoice export or Xero report export (trial balance, ledger, aged listing, activity statement), or mentions
  Xero, bank statement import, or Xero CSV.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-11-20
---

# Xero Integration Skill v1.1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

Xero is a cloud-based accounting platform used primarily by small and medium businesses and their accountants. Headquartered in New Zealand, Xero is dominant in AU, NZ, and the UK, with growing adoption in the US, Canada, Singapore, Hong Kong, and South Africa. Xero provides invoicing, bank reconciliation, payroll (in some regions), expense claims, and financial reporting.

Users interact with Xero data in two main export contexts: **bank statement CSVs** (for importing transactions into Xero or exported from Xero) and **invoice/bill CSVs** (for bulk import/export of sales invoices and purchase bills).

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV | Bank statement import/export, invoice import/export, contact lists, chart of accounts |
| PDF | Individual invoices, statements, financial reports |
| Excel (XLSX) | Reports (P&L, Balance Sheet, Aged Receivables, Trial Balance) |
| Google Sheets | Reports (direct export option) |

Bank statement CSVs are the most common data a user will upload for bookkeeping purposes. Invoice CSVs are used for bulk operations. Report exports for accounting work (trial balance, ledgers, aged listings, activity statement, payroll) and the checks to run on them are in Sections 11 and 12.

---

## Section 3 — Column Mapping

### Bank Statement CSV

Xero reads bank statement CSVs **positionally**, not by header name. Column order is critical.

| Position | Column | Required | Meaning |
|----------|--------|----------|---------|
| A | Date | Yes | Transaction date. DD/MM/YYYY for UK/AU/NZ orgs, MM/DD/YYYY for US orgs. YYYY-MM-DD works universally. |
| B | Amount | Yes | Signed number. Positive = money in, negative = money out. No currency symbols, no thousand separators. |
| C | Payee | No | Counterparty name. Used for contact matching and bank rule triggers. |
| D | Description | No | Memo/narrative. Max 500 characters. Appears in transaction notes. |
| E | Reference | No | Check number, transaction ID, or external reference. |
| F | Cheque Number | No | For check transactions only. |

### Precoded Bank Statement CSV (extended format)

Adds three columns to the standard format for auto-classification:

| Position | Column | Required | Meaning |
|----------|--------|----------|---------|
| G | AccountCode | Precoded only | Must match a nominal code in the Xero chart of accounts exactly. |
| H | TaxType | Precoded only | Must match a Xero tax rate name exactly (e.g., "20% (VAT on Income)"). |
| I | ContactName | Precoded only | Must match an existing Xero contact name exactly. |

### Invoice/Bill Import CSV

| Column Header | Required | Meaning |
|---------------|----------|---------|
| ContactName | Yes | Must match an existing Xero contact or Xero creates a new one. |
| InvoiceNumber | Yes | Unique invoice identifier. Duplicates are rejected. |
| InvoiceDate | Yes | Date format must match org region settings. |
| DueDate | Yes | Must be on or after InvoiceDate. |
| Description | Yes | Line item description. |
| Quantity | Yes | Line item quantity. |
| UnitAmount | Yes | Line item price excluding tax. |
| AccountCode | Yes | Must match a Xero chart of accounts code. |
| TaxType | Recommended | Must match Xero tax rate name exactly. |
| Reference | No | PO number or external reference. |
| Currency | No | Three-letter ISO code (GBP, AUD, USD). |
| Total | Auto | Calculated by Xero from line items. |
| TaxTotal | Auto | Calculated from TaxType and amounts. |

Multi-line invoices: each line item is a separate CSV row. Rows with the same InvoiceNumber are grouped into one invoice.

---

## Section 4 — Transaction Type Codes

Xero does not use explicit transaction type codes in CSV imports. Transaction direction is determined by the sign of the Amount field:

| Sign | Meaning |
|------|---------|
| Positive (+) | Money received / deposit / credit to bank |
| Negative (-) | Money paid out / withdrawal / debit from bank |

During reconciliation inside Xero, transactions are categorized as: Spend Money, Receive Money, Transfer, or matched to existing invoices/bills.

---

## Section 5 — Fee Structure

Xero itself does not charge transaction fees that appear in exported data. Xero's subscription fees are billed separately and do not appear in bank statement exports.

Bank fees, payment processor fees, and other charges appear as regular negative-amount transactions in bank statement CSVs with the bank's own description.

---

## Section 6 — Tax-Relevant Fields

| Field | Location | Notes |
|-------|----------|-------|
| TaxType | Invoice CSV, Precoded bank CSV | Must exactly match a configured Xero tax rate (e.g., "20% (VAT on Income)", "Tax on Purchases", "GST on Income", "BAS Excluded"). |
| TaxAmount | Invoice CSV | Per-line-item tax amount. Auto-calculated if TaxType is set. |
| TaxTotal | Invoice CSV | Invoice-level total tax. |
| AccountCode | Invoice CSV, Precoded bank CSV | Determines which P&L/BS account and indirectly which tax treatment applies. |

Xero tax rate names are region-specific. UK orgs use VAT rates, AU/NZ orgs use GST rates, US orgs use sales tax rates. The TaxType string must be copied verbatim from Settings > Tax Rates in the user's Xero org.

---

## Section 7 — Multi-Currency Handling

Xero supports multi-currency on paid plans. In CSV exports:

- Bank statement CSVs are always in the currency of the bank account they belong to. No currency column exists in the standard format.
- Invoice CSVs include an optional `Currency` column (three-letter ISO code). If omitted, the org's base currency is assumed.
- Exchange rates are managed inside Xero, not in the CSV. Xero applies the rate from its feed or a manually entered rate at reconciliation time.
- Unrealised and realised currency gains/losses are calculated by Xero automatically and posted to a Currency Gains/Losses account.

When processing a user's Xero CSV that contains foreign-currency transactions, note that the amounts are already in the bank account's currency — no conversion is needed at the CSV level.

---

## Section 8 — Reconciliation Tips

1. **Date format is the #1 import failure.** Confirm the user's Xero region before processing. UK/AU/NZ = DD/MM/YYYY. US = MM/DD/YYYY. When in doubt, use YYYY-MM-DD (works everywhere).
2. **Column order matters more than column names.** Xero reads positionally. If a bank CSV has Description in column A and Date in column B, the import will silently misread everything.
3. **No opening/closing balance rows.** Remove any summary rows, running balance columns, or opening/closing balance lines before import. Xero calculates balances internally.
4. **Max 1,000 transactions per file.** Split larger datasets into multiple files by date range.
5. **Duplicate detection is weak.** Xero checks for duplicate imports within the same bank account using date + amount + payee, but edge cases slip through. Cross-check after import.
6. **Bank rules accelerate reconciliation.** If the user has set up bank rules in Xero, many transactions will auto-match. Precoded CSVs bypass rules entirely by specifying the account directly.

---

## Section 9 — Common Gotchas

1. **Wrong sign convention.** Some bank CSVs use positive for debits and negative for credits (the opposite of what Xero expects). Always verify: positive = money IN.
2. **Comma in amounts.** Xero expects a period as the decimal separator and no thousand separators. "1,234.56" breaks the import; use "1234.56".
3. **Currency symbols in Amount.** "$100.00" fails. Use "100.00".
4. **AccountCode typos in precoded CSVs fail silently.** Xero skips the precoding for that row without warning. The transaction imports but without the account assignment.
5. **TaxType must be an exact string match.** "VAT on Income" is not the same as "20% (VAT on Income)". Copy from Xero's tax rate settings exactly.
6. **Line breaks in Description.** Carriage returns inside a description field break the CSV parser. Ensure descriptions are single-line.
7. **UTF-8 encoding required.** Non-UTF-8 files cause character corruption, especially with accented names or currency symbols in descriptions.

---

## Section 10 — Sample Data

### Bank Statement CSV (standard)

```csv
Date,Amount,Payee,Description,Reference
15/03/2026,2500.00,Acme Ltd,Invoice 1042 payment,INV-1042
16/03/2026,-64.99,Adobe Inc,Creative Cloud monthly subscription,SUB-2251
16/03/2026,-1200.00,HMRC,VAT Q4 2025 payment,VAT-Q4
17/03/2026,890.50,Widget Corp,Project consulting fee March,PO-8891
18/03/2026,-45.00,Vodafone UK,Mobile phone March,DD-MOB
18/03/2026,-12.50,Barclays,Monthly account fee,BANKFEE
19/03/2026,150.00,John Smith,Expense reimbursement,EXP-034
20/03/2026,-3200.00,Jane Doe,Salary March 2026,PAY-MAR
```

### Invoice Import CSV

```csv
ContactName,InvoiceNumber,InvoiceDate,DueDate,Description,Quantity,UnitAmount,AccountCode,TaxType,Currency
Acme Ltd,INV-1042,01/03/2026,31/03/2026,Web development services,40,62.50,200,20% (VAT on Income),GBP
Widget Corp,INV-1043,05/03/2026,04/04/2026,SEO audit report,1,890.50,200,20% (VAT on Income),GBP
Widget Corp,INV-1043,05/03/2026,04/04/2026,Keyword research addon,1,200.00,200,20% (VAT on Income),GBP
```

---

## Section 11 — Report exports for accounting work

Sections 3 to 10 cover import CSVs. Report exports are a different input: a trial balance, ledger, aged listing or activity statement exported for a workpaper. Xero exports reports as PDF, Microsoft Excel or Google Sheets ([Xero Central, Export and print a report](https://central.xero.com/s/article/Export-or-print-a-report), read 19 November 2026); a report has no CSV option, so for a CSV-only tool save the recalculated Excel sheet as CSV UTF-8 and keep account codes as text (`090` keeps its leading zero).

**Export manifest.** For every export record the organisation (or an approved pseudonym), report name, generation time, as-at date or date range, cash or accrual basis, tracking and other filters, whether drafts are included, currency and any other report option. Two totals from exports with different settings can agree without measuring the same thing; record a total whose basis the headers do not show as unresolved.

**Formula cells.** Xero Central says a report exported to Excel with formulas can show some amounts as 0.00 until editing is enabled in Excel. A script or library that reads the cached values may see those zeros. Recompute totals from the detail rows, or recalculate in Excel and save before another tool reads the file.

| Need | Report | What to check |
|------|--------|---------------|
| Balances at a date | Trial Balance | By default the debit and credit year to date columns show, for revenue and expense accounts, the movement from the first day of the financial year to the report date, and for asset, liability and equity accounts the cumulative balance at that date. Optional month columns show the movement from the first day of the month to the report date, with no carry forward. Accounts with nil balances are not shown. Multicurrency organisations see base currency at the report date's rate ([Xero Central, Trial Balance report](https://central.xero.com/s/article/Trial-Balance-report-new-version), read 19 November 2026) |
| Balances over a period | Trial Balance by Date Range | A separate report; do not substitute one for the other |
| Transaction lines behind a balance | General Ledger Detail, Account Transactions | A summary report carries movements only and cannot support a tie-out |
| Debtor or creditor support | Aged Receivables Detail, Aged Payables Detail | Run as at the period end, not 'current'. The Summary variants total by contact only |
| BAS support | Activity Statement, with its transaction tabs | The GST basis follows the GST settings, not the trial balance's cash or accrual choice; record both |
| Payroll and super | Payroll Activity Summary, Superannuation Accrual, Superannuation Payments | Accruals and payments are different views; payday super timing needs both |

Xero Central describes each report in the last 4 rows (read 20 November 2026): [General Ledger Detail](https://central.xero.com/s/article/General-Ledger-Detail-report), [Account Transactions](https://central.xero.com/s/article/Account-Transactions-report-New), [Aged Receivables Detail](https://central.xero.com/s/article/Aged-Receivables-Detail-report-New), [Aged Payables Detail](https://central.xero.com/s/article/Aged-Payables-Detail-report-New), the activity statement's transactions and its GST accounting method ([Simpler BAS](https://central.xero.com/s/article/The-Simpler-Business-Activity-Statement), [BAS settings](https://central.xero.com/s/article/Select-your-BAS-settings)), [Payroll Activity Summary](https://central.xero.com/s/article/Payroll-Activity-Summary-report), [Superannuation Accrual](https://central.xero.com/s/article/Superannuation-Accrual-report) and [Superannuation Payments](https://central.xero.com/s/article/Superannuation-Payments-report). Report options differ by region and user role; confirm each option in the organisation before relying on it.

**API reach.** The Accounting API's report endpoints are 1099 (US only), Aged Payables By Contact, Aged Receivables By Contact, Balance Sheet, Bank Summary, BAS Report (Australia only: lists published BAS reports, and a ReportID retrieves one), Budget Summary, Executive Summary, GST Report (New Zealand only), Profit And Loss and Trial Balance. `Reports/TrialBalance` takes only `date` (as at) and `paymentsOnly` (cash transactions only) and returns the month to that date with YTD values: columns Debit, Credit, YTD Debit and YTD Credit ([Xero Developer, Accounting API Reports](https://developer.xero.com/documentation/api/accounting/reports), read 19 November 2026). No endpoint returns Trial Balance by Date Range or General Ledger Detail; a figure assembled from transaction records is a reconstruction and the manifest says so.

---

## Section 12 — Completeness checks: run on every report export

Stop and re-export on a failure; never patch a figure to make a check pass.

1. **Both trial balance pairs balance.** Total debits equal total credits for the year to date pair and, where shown, the month pair. A truncated or filtered export usually fails here first.
2. **Totals are recomputed, not read.** Drop section headings and `Total` rows before summing, recompute each total from the account rows and agree it to any total the report supplies.
3. **Control accounts tie.** An aged listing run at the same date and basis agrees to its control account in the trial balance. Keep repeated contact rows until the underlying items explain them.
4. **Errors are not zeros.** A report that shows an empty result together with an error is unavailable evidence, not proof of nil activity.
5. **GST basis of a Profit and Loss export (AU).** Compare revenue with an independently reconciled GST-exclusive control for the same accounts, period and basis. Within 1% of the control is consistent with a GST-exclusive export; within 1% of 1.1 times the control is consistent with a GST-inclusive one, which needs a GST-exclusive re-export; anything else, or no control, is undetermined. The 1.1 factor holds only for wholly taxable supplies: GST is 10% of the value of a taxable supply (GST Act s 9-70), and the value is the price less the GST, as the Act's example of a $22,000 price with a $20,000 value shows (s 9-75). Mixed GST treatments need an account-level reconciliation. The test indicates the export's likely basis; confirm it from the report settings or a re-export. It says nothing about any supply's tax treatment.

### Example 1 — Trial balance, complete and truncated

A fabricated year to date trial balance with month columns: 4 debit and 3 credit account rows. In the second export the last credit row (Sales, $9,800) is missing, so the year to date pair is out by exactly that amount.

```oa-check
name: Xero trial balance movement and year to date pairs (fabricated)
inputs:
  month_debit_total: 12500
  month_credit_total: 12500
  ytd_bank: 46300
  ytd_receivables: 18000
  ytd_rent: 24000
  ytd_wages: 96000
  ytd_payables: 7400
  ytd_capital: 167100
  ytd_sales: 9800
steps:
  - month_difference: month_debit_total - month_credit_total
  - ytd_debits: ytd_bank + ytd_receivables + ytd_rent + ytd_wages
  - ytd_credits: ytd_payables + ytd_capital + ytd_sales
  - ytd_difference: ytd_debits - ytd_credits
  - truncated_ytd_difference: ytd_debits - (ytd_payables + ytd_capital)
expected:
  month_difference: 0
  ytd_debits: 184300
  ytd_credits: 184300
  ytd_difference: 0
  truncated_ytd_difference: 9800
```

### Example 2 — A GST-inclusive Profit and Loss export (AU)

A fabricated wholly taxable business: the exported revenue is $121,000 and the reconciled GST-exclusive control is $110,000. The export is 10% away from the control and 0% away from 1.1 times it, so it reads as GST-inclusive: ask for a GST-exclusive re-export. Dividing by 1.1 gives the exclusive amount; dividing by 11 gives only the GST.

```oa-check
name: GST basis test on a Xero Profit and Loss export (fabricated)
inputs:
  exported_revenue: 121000
  exclusive_control: 110000
steps:
  - gap_to_exclusive_percent: abs(exported_revenue - exclusive_control) / exclusive_control * 100
  - gap_to_inclusive_percent: abs(exported_revenue - exclusive_control * 1.1) / (exclusive_control * 1.1) * 100
  - exclusive_amount: exported_revenue / 1.1
  - gst_component: exported_revenue / 11
expected:
  gap_to_exclusive_percent: 10
  gap_to_inclusive_percent: 0
  exclusive_amount: 110000
  gst_component: 11000
```

---

## Sources

| Source | URL | Read on |
|---|---|---|
| Xero Central, Export and print a report | <https://central.xero.com/s/article/Export-or-print-a-report> | 2026-11-19; PDF, Excel and Google Sheets formats; formula amounts showing 0.00 |
| Xero Central, Trial Balance report | <https://central.xero.com/s/article/Trial-Balance-report-new-version> | 2026-11-19; year to date and month columns, nil balances, multicurrency, Trial Balance by Date Range |
| Xero Developer, Accounting API Reports | <https://developer.xero.com/documentation/api/accounting/reports> | 2026-11-19; report endpoints, TrialBalance parameters and columns, BAS Report (Australia only) |
| Xero Central, report articles (General Ledger Detail, Account Transactions, Aged Receivables and Payables Detail, Simpler BAS, BAS settings, Payroll Activity Summary, Superannuation Accrual, Superannuation Payments) | <https://central.xero.com/s/article/General-Ledger-Detail-report> and the others linked in Section 11 | 2026-11-20; what each report shows; GST accounting method sets the activity statement's basis |
| A New Tax System (Goods and Services Tax) Act 1999, compilation 96 (C2026C00081), ss 9-70 and 9-75 | <https://www.legislation.gov.au/C2004A00446/latest/text> | 2026-11-19; GST is 10% of value; $22,000 price, $20,000 value example |

Sections 1 to 10 were not re-read against these sources.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
