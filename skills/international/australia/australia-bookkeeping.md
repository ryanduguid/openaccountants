---
name: australia-bookkeeping
description: Use this skill whenever asked about Australian bookkeeping for sole traders, partnerships, or small companies. Trigger on phrases like "chart of accounts", "BAS", "GST codes", "bookkeeping", "profit and loss", "balance sheet", "AASB", "simplified disclosures", "Tier 2", "bank reconciliation", "expense categories", "revenue recognition", "depreciation", "instant asset write-off", "small business pool", "ABN", "ATO reporting", "activity statement", "accrual basis", "cash basis", "general ledger", or any question about day-to-day transaction recording, financial statement preparation, or account coding for an Australian business.
version: 1.0
jurisdiction: AU
tax_year: 2025
last_updated: 2026-08-20
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD ($) only |
| Financial year | 1 July – 30 June (standard); substituted accounting period available for companies |
| Accounting standards | AASB (full IFRS-based); AASB 1060 Simplified Disclosures (Tier 2); Special Purpose for non-reporting entities |
| Governing body | Australian Accounting Standards Board (AASB) |
| Tax authority | Australian Taxation Office (ATO) |
| Key legislation | Corporations Act 2001 (financial reporting Ch.2M); Income Tax Assessment Act 1936/1997; A New Tax System (GST) Act 1999 |
| GST registration threshold | $75,000 turnover ($150,000 for non-profits) |
| Small business entity threshold | Aggregated turnover < $10 million |
| BAS lodgement | Quarterly (most small businesses) or monthly ($20m+ turnover) |

## Section 2 -- Standard Chart of Accounts

Australian software (Xero, MYOB, QuickBooks) typically uses 3–4 digit codes. The structure below follows common Australian practice.

### Assets (1000–1999)

**Assets (1000–1999)**

| Code | Account | Type |
| --- | --- | --- |
| 1000 | Cash on Hand / Petty Cash | Current asset |
| 1010 | Business Bank Account | Current asset |
| 1020 | Savings Account | Current asset |
| 1030 | Term Deposits (< 12 months) | Current asset |
| 1050 | Undeposited Funds | Current asset |
| 1100 | Accounts Receivable (Trade Debtors) | Current asset |
| 1110 | Other Debtors | Current asset |
| 1120 | Prepayments | Current asset |
| 1150 | GST Receivable (Input Tax Credits) | Current asset |
| 1200 | Inventory / Stock on Hand | Current asset |
| 1300 | Land | Non-current asset |
| 1310 | Buildings | Non-current asset |
| 1311 | Accumulated Depreciation — Buildings | Contra asset |
| 1320 | Plant and Equipment | Non-current asset |
| 1321 | Accumulated Depreciation — Plant & Equipment | Contra asset |
| 1330 | Motor Vehicles | Non-current asset |
| 1331 | Accumulated Depreciation — Motor Vehicles | Contra asset |
| 1340 | Office Equipment | Non-current asset |
| 1341 | Accumulated Depreciation — Office Equipment | Contra asset |
| 1350 | Computer Equipment | Non-current asset |
| 1360 | Furniture and Fittings | Non-current asset |
| 1361 | Accumulated Depreciation — Furniture & Fittings | Contra asset |
| 1400 | Small Business Pool | Non-current asset |
