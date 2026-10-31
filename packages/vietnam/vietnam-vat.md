---
name: vietnam-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Vietnam VAT (thuế giá trị gia tăng / GTGT) return, classify transactions for Vietnamese VAT purposes, or advise on VAT registration and filing in Vietnam. Trigger on phrases like "thuế GTGT", "Vietnam VAT", "tờ khai thuế GTGT", "hóa đơn điện tử", "phương pháp khấu trừ", "phương pháp trực tiếp", or any Vietnam VAT request. ALWAYS read this skill before touching any Vietnam VAT work.
version: 2.0
jurisdiction: VN
tax_year: 2026
tax_year_notes: "The 8% reduced rate runs from 1 July 2025 to 31 December 2026. No extension was found as at 31 October 2026. From 1 January 2027, unless extended, supplies shown at 8% return to 10%."
last_updated: 2026-10-31
review_status: pending_review
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Vietnam VAT

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Vietnam (Cộng hòa Xã hội chủ nghĩa Việt Nam) |
| Tax | Thuế Giá Trị Gia Tăng (GTGT — VAT) |
| Currency | VND (Vietnamese Dong / đồng) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Standard rate | 10% (VAT Law 48/2024/QH15, art. 9.3) |
| Temporary reduced rate | 8% on supplies otherwise at 10%, from 1 July 2025 to 31 December 2026, except telecommunications, finance, banking, securities, insurance, real estate business, metal products, mineral products other than coal, and goods and services subject to special consumption tax other than petrol (Resolution 204/2025/QH15, art. 1.1, quoted in https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf, note 5; Decree 174/2025/ND-CP, art. 1 and Annexes I and II: https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/174nd.signed.pdf). Direct-method businesses instead reduce their % rate by 20% (Decree 174, art. 1.2(b)) |
| Reduced rate | 5% (clean water; fertilizer and plant protection products; agricultural services; unprocessed crop, livestock and aquatic products outside the exemption; medical equipment and medicines; teaching aids; children's toys and books; traditional performing arts; science and technology services; social housing) (VAT Law art. 9.2). See Section 5.2 |
| Zero rate | 0% (exports of goods and services; international transport) (VAT Law art. 9.1) |
| Exempt | The list in VAT Law art. 5, including credit, foreign exchange and securities services, life and health insurance, medical services, teaching and vocational training, land use right transfers, software products and services, and animal feed. See Section 5.4 |
| Revenue thresholds (not a registration threshold) | Household and individual businesses: no VAT at annual revenue of VND 1,000,000,000 or less, from 1 January 2026 (VAT Law art. 5.25 as amended by Law 09/2026/QH16, art. 2: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/09-qh.signed.pdf; Decree 68/2026/ND-CP, art. 3: https://xdcs.cdnchinhphu.vn/446259493575335936/2026/3/6/68-2026-nd-cp-05032026-signed-17727673940151875228819.pdf, as amended by Decree 141/2026/ND-CP, art. 1.1: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/141-ndcp.signed.pdf); above it, direct method. Enterprises: deduction method at annual revenue of VND 1,000,000,000 or more, otherwise direct method unless they opt in (VAT Law arts 11.2 and 12.2) |
| Tax authority | Tổng cục Thuế (General Department of Taxation — GDT) |
| Return forms | Mẫu 01/GTGT (monthly/quarterly, deduction method); Mẫu 04/GTGT (direct method) |
| Filing frequency | Monthly (if prior year revenue > VND 50 billion); quarterly (if ≤ VND 50 billion) |
| Filing deadline | Monthly: 20th of following month; Quarterly: 30th of month following quarter end |
| e-Invoice | Hóa đơn điện tử — mandatory since 2022 under Decree 123/2020 |
| Tax invoice (VAT invoice) | Hóa đơn GTGT — required for deduction method input credits |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Vietnam-licensed tax agent (đại lý thuế) or CPA |
| Skill version | 2.0 |

### Key return form lines (Mẫu 01/GTGT — Deduction method)

**Key return form lines**

| Line | Meaning |
| --- | --- |
| [26] | Taxable sales at 10% (doanh thu chịu thuế 10%) |
| [27] | Output VAT at 10% |
| [28] | Taxable sales at 5% |
| [29] | Output VAT at 5% |
| [30] | Zero-rated sales (xuất khẩu) |
| [31] | Exempt sales (không chịu thuế) |
| [32] | Total output VAT ([27]+[29]) |
| [33] | Total input VAT claimed (thuế GTGT đầu vào) |
| [34] | Non-deductible input VAT |
| [35] | Net input VAT ([33]−[34]) |
| [40] | VAT payable ([32]−[35]) |
| [41] | Excess credit carried forward |
| [42] | Net payable after prior credit |

Supplies at 8% are also listed on Form 01, Annex III of Decree 174/2025/ND-CP, filed with the return (art. 1.6). Unconfirmed: the line of Mẫu 01/GTGT that carries 8% sales, and whether the line numbers above match the current form. Check the form before filing.

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 10% until the supply is confirmed eligible for 8% |
| Rate on a purchase | The rate and VAT shown on the e-invoice (Decree 174, art. 1.3(a)) |
| Unknown whether 5% rate applies | 10% until confirmed |
| Unknown counterparty country | Domestic Vietnam |
| Unknown export qualification | Domestic 10% until evidence confirmed |
| Unknown business-use % | 0% input credit |
| Unknown whether e-invoice compliant | No input credit |
| Unknown B2B vs B2C for cross-border | Taxable at 10% (domestic consumption assumed) |

### Red flag thresholds

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single transaction | VND 50,000,000 |
| HIGH tax delta on single default | VND 5,000,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | VND 20,000,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — Bank statement for the period in CSV, PDF, or pasted text. Confirmation of VAT calculation method (deduction phương pháp khấu trừ or direct phương pháp trực tiếp) and MST (Mã số thuế — 10-digit tax code).
- **Recommended inputs** — Hóa đơn GTGT (VAT invoices) for all purchases, electronic invoices (hóa đơn điện tử) for sales, prior period return and excess credit carried forward.
- **Ideal inputs** — Complete ledger, export customs declarations (tờ khai hải quan), asset register, full invoice register.
- **Refusal if minimum missing** — SOFT WARN. No bank statement = hard stop. "Input VAT credits in Vietnam require compliant hóa đơn GTGT (VAT invoices) or hóa đơn điện tử. All credits are provisional pending invoice verification."

### Refusal catalogue

- **R-VN-1 — Direct method taxpayers (phương pháp trực tiếp)** — "Direct method taxpayers pay VAT on the value-added margin, not on gross output minus gross input. They cannot claim input credits in the same way. Confirm the calculation method before proceeding. This skill primarily covers the deduction method."
- **R-VN-2 — Businesses below VND 1 billion** — "A household or individual business with annual revenue of VND 1 billion or less pays no VAT (from 1 January 2026). An enterprise below VND 1 billion still pays VAT, by the direct method unless it opts into the deduction method. Confirm the business type and method before proceeding."
- **R-VN-3 — Partial exemption proration** — "If the business makes both taxable and exempt supplies, input VAT must be apportioned. Apportionment requires the taxable/total revenue ratio for the year. Out of scope without full-year data — escalate."
- **R-VN-4 — Real estate and construction** — "Real estate development and construction have special VAT treatment for housing and land. Out of scope — escalate to a licensed tax agent."
- **R-VN-5 — Foreign contractor withholding tax (FCT)** — "Foreign contractors providing services in Vietnam are subject to Foreign Contractor Tax (FCT = CIT + VAT withholding). FCT is different from the regular GTGT return. Out of scope."

## Section 3 — Supplier pattern library

Match by case-insensitive substring on counterparty name or reference. Most specific match wins. Fall through to Section 5 if no match.

Rates in this section are for supplies from 1 July 2025 to 31 December 2026. Eligibility was read from Decree 174/2025/ND-CP, Annexes I and II. For a purchase, the VAT on the e-invoice governs. From 1 January 2027, unless the reduction is extended, each row at 8% returns to 10%.

### 3.1 Vietnamese banks — fees and charges (exempt / exclude)

**Vietnamese banks**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VIETCOMBANK, NGÂN HÀNG NGOẠI THƯƠNG, VCB | EXCLUDE (fee lines) | Financial service — exempt from GTGT |
| BIDV, NGÂN HÀNG ĐẦU TƯ VÀ PHÁT TRIỂN | EXCLUDE (fee lines) | Same |
| VIETINBANK, NGÂN HÀNG CÔNG THƯƠNG, CTG | EXCLUDE (fee lines) | Same |
| AGRIBANK, NGÂN HÀNG NÔNG NGHIỆP | EXCLUDE (fee lines) | Same |
| TECHCOMBANK, TCB | EXCLUDE (fee lines) | Same |
| VPBANK, NGÂN HÀNG VIỆT NAM THỊNH VƯỢNG | EXCLUDE (fee lines) | Same |
| MB BANK, NGÂN HÀNG QUÂN ĐỘI | EXCLUDE (fee lines) | Same |
| ACB, NGÂN HÀNG Á CHÂU | EXCLUDE (fee lines) | Same |
| SACOMBANK | EXCLUDE (fee lines) | Same |
| TPBANK | EXCLUDE (fee lines) | Same |
| PHÍ DỊCH VỤ, LÃI SUẤT, INTEREST, FEE | EXCLUDE | Bank fee/interest — exempt |

### 3.2 Vietnamese government and statutory (exclude)

**Government/statutory**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TỔNG CỤC THUẾ, CỤC THUẾ, TAX AUTHORITY | EXCLUDE | Tax payment |
| THUẾ GTGT, THUẾ TNDN, THUẾ TNCN | EXCLUDE | Tax remittance |
| BẢO HIỂM XÃ HỘI, BHXH, SOCIAL INSURANCE | EXCLUDE | Social insurance |
| BẢO HIỂM Y TẾ, BHYT | EXCLUDE | Health insurance |
| HẢI QUAN, CUSTOMS | EXCLUDE | Customs duty |
| BHTN, BẢO HIỂM THẤT NGHIỆP | EXCLUDE | Unemployment insurance |

### 3.3 Vietnamese utilities (taxable at 5%, 8% or 10%)

**Utilities**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| EVN, TẬP ĐOÀN ĐIỆN LỰC, ĐIỆN LỰC | Input 8% | 8% | Electricity — not excluded from the reduction |
| CÔNG TY ĐIỆN LỰC (regional utilities) | Input 8% | 8% | Regional electricity distribution |
| SAWACO, HAWACO, CẤP NƯỚC (water company) | Input 5% | 5% | Clean water — reduced rate 5% |
| VIETTEL TELECOM | Input 10% | 10% | Telecom — standard rate; telecommunications excluded from 8% |
| VNPT, VIỄN THÔNG VIỆT NAM | Input 10% | 10% | Telecom — standard rate; telecommunications excluded from 8% |
| MOBIFONE | Input 10% | 10% | Mobile — standard rate; telecommunications excluded from 8% |
| VIETNAMOBILE | Input 10% | 10% | Mobile — standard rate; telecommunications excluded from 8% |
| GMOBILE | Input 10% | 10% | Mobile — standard rate; telecommunications excluded from 8% |

### 3.4 Transport and logistics

**Transport and logistics**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| VIETNAM AIRLINES, VNA, HÀNG KHÔNG VIỆT NAM | Check route | 0%/8% | International 0%; domestic 8% |
| VIETJET AIR, VIETJET | Check route | 0%/8% | International 0%; domestic 8% |
| BAMBOO AIRWAYS | Check route | 0%/8% | International 0%; domestic 8% |
| VIETRAVEL AIRLINES | Check route | 0%/8% | Domestic 8%; international 0% |
| ĐƯỜNG SẮT VIỆT NAM, VNR, RAILWAY | Input 8% | 8% | Rail — taxable |
| GRAB VIETNAM | Input 8% | 8% | Ride-hailing — taxable |
| BE (taxi app), BEE TAXI | Input 8% | 8% | Ride-hailing — taxable |
| GIAO HÀNG TIẾT KIỆM, GHTK | Input 8% | 8% | Courier — taxable |
| GIAO HÀNG NHANH, GHN | Input 8% | 8% | Courier — taxable |
| VIETTEL POST | Input 8% | 8% | Courier — taxable |
| VIETNAM POST, BƯU ĐIỆN (parcel) | Input 8% | 8% | Parcel services — taxable |
| VIETNAM POST, BƯU ĐIỆN (stamps) | Input 8% | 8% | Postal services are not in the VAT Law art. 5 exempt list |
| J&T EXPRESS VIETNAM | Input 8% | 8% | Courier — taxable |
| NINJA VAN VIETNAM | Input 8% | 8% | Courier — taxable |

### 3.5 Food and retail

**Food and retail**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| WINMART, VINMART, WINCOMMERCE | Input 8% | 8% | Supermarket — 8% on eligible goods; check invoice lines |
| BIG C VIỆT NAM (now GO!) | Input 8% | 8% | Hypermarket — 8% on eligible goods; check invoice lines |
| AEON VIỆT NAM | Input 8% | 8% | Department store — 8% on eligible goods; check invoice lines |
| BÁN LẺ (retail), NHÀ HÀNG (restaurant) | Input 8% | 8% | Reduced from 10% — taxable; alcohol, tobacco and sugary drinks stay at 10% |
| CO.OPMART, SAIGON CO.OP | Input 8% | 8% | Supermarket — 8% on eligible goods; check invoice lines |
| LOTTE MART VIỆT NAM | Input 8% | 8% | Hypermarket — 8% on eligible goods; check invoice lines |
| PHÂN BÓN, THUỐC TRỪ SÂU (fertilizers/pesticides) | Input 5% | 5% | Agricultural inputs — reduced 5% |

### 3.6 SaaS — local Vietnamese suppliers (exempt, 8% or 10%)

**SaaS local**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| MISA, PHẦN MỀM MISA | Check invoice | Exempt/8% | Software products and services are exempt (VAT Law art. 5.21); no input VAT if the invoice shows none |
| FAST ACCOUNTING | Check invoice | Exempt/8% | Same as MISA |
| VIETTEL CLOUD | Input 8% | 8% | Cloud services — 8%, unless invoiced as telecommunications (10%) |
| VNPT CLOUD | Input 8% | 8% | Cloud services — 8%, unless invoiced as telecommunications (10%) |
| VTC PAY | Input 10% | 10% | Vietnamese payment — taxable; financial services excluded from 8% |

### 3.7 SaaS — international suppliers (foreign contractor tax / FCT note)

Foreign digital service providers in Vietnam: a business buyer on the deduction method may be required to withhold and pay on the supplier's behalf (VAT Law art. 4.3 and 4.4). Input VAT is then supported by the tax payment document rather than a Vietnamese VAT invoice, subject to the art. 14 conditions (VAT Law art. 11.1(c): https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf; Decree 181/2025/ND-CP, art. 25: https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/181nd.signed.pdf). This is complex — flag for specialist review.

**International SaaS suppliers**

| Pattern | Notes |
| --- | --- |
| GOOGLE (Workspace, Ads, Cloud) | FCT applies — flag; may be registered via Google's Vietnam registration |
| MICROSOFT (365, Azure) | FCT may apply — check if Vietnam entity invoices |
| META, FACEBOOK ADS | FCT applies — flag |
| ZOOM, SLACK, NOTION, OPENAI | FCT applies — flag for specialist |
| AWS | FCT applies — flag |

### 3.8 Payment processors (exempt fees)

**Payment processors**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VNPAY (phí giao dịch) | EXCLUDE | Payment processing fee — exempt |
| MOMO (phí) | EXCLUDE | E-wallet fee — exempt |
| ZALOPAY (phí) | EXCLUDE | Payment fee — exempt |
| PAYOO (phí) | EXCLUDE | Payment fee — exempt |

### 3.9 Internal transfers and exclusions

**Internal transfers**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CHUYỂN KHOẢN NỘI BỘ, INTERNAL | EXCLUDE | Internal movement |
| VAY VỐN, TRẢ NỢ, LOAN | EXCLUDE | Loan principal |
| LƯƠNG, TIỀN LƯƠNG, SALARY | EXCLUDE | Wages — outside VAT scope |
| CỔ TỨC, DIVIDEND | EXCLUDE | Out of scope |
| ĐẶT CỌC, DEPOSIT | EXCLUDE | Deposit — out of scope until applied |
| RÚT TIỀN, ATM | Tier 2 — ask | Default exclude |

## Section 4 — Worked examples

Six classifications from a hypothetical Ho Chi Minh City-based IT consultant, all dated April 2026 and so inside the 8% period. Format: Vietcombank (VCB) transaction history.

### Example 1 — Domestic B2B revenue (8%)

**Input line:**
`15/04/2026  Nhận chuyển khoản  CÔNG TY TNHH ABC TECHNOLOGY  ND: HD GTGT SO 001/2026  +108,000,000  VND`

**Reasoning:**
Incoming VND 108,000,000 from a Vietnamese company for IT consulting. IT consulting is not in Annex I or II of Decree 174, so 8% applies in April 2026; confirm it is not a software service, which is exempt (VAT Law art. 5.21). Gross VND 108,000,000 includes VAT. Net = VND 100,000,000 (doanh thu chịu thuế) + VND 8,000,000 output GTGT. An electronic VAT invoice (hóa đơn GTGT điện tử) showing 8% must be issued and transmitted to GDT. Report on the return and on Form 01, Annex III of Decree 174.

**Classification:** Output VAT 8% — VND 8,000,000. Net sales: VND 100,000,000.

### Example 2 — Export service (zero-rated)

**Input line:**
`22/04/2026  Nhận ngoại tệ  ACME CORPORATION USA  Technical consulting Q1/2026  +USD 5,000 (VND 125,000,000)`

**Reasoning:**
USD receipt from a US company for services. Zero-rated if the service is provided directly to a foreign entity and consumed outside Vietnam. Evidence: contract with the foreign entity and a non-cash payment document (Decree 181/2025/ND-CP, art. 18.2). Report VND 125,000,000 on line [30] (zero-rated). Output VAT: VND 0. Conservative default: 10% if export status cannot be confirmed.

**Classification:** Zero-rated exports — VND 125,000,000. Output VAT: VND 0.

### Example 3 — Water utility (5% reduced rate)

**Input line:**
`10/04/2026  Thanh toán tự động  SAWACO - CẤP NƯỚC SAIGON  Tiền nước tháng 3/2026  -2,100,000  VND`

**Reasoning:**
Water bill from SAWACO (Saigon Water Corporation). Clean water is subject to 5% reduced rate VAT. Gross VND 2,100,000. Net = VND 2,000,000 + VND 100,000 input VAT at 5%. SAWACO issues a compliant electronic invoice — input credit of VND 100,000 claimable. Report on line [33] (input VAT).

**Classification:** Input VAT 5% — VND 100,000. Net expense: VND 2,000,000.

### Example 4 — Domestic courier (8%)

**Input line:**
`08/04/2026  Thanh toán  GIAO HÀNG NHANH GHN  Phí vận chuyển tháng 3/2026  -10,800,000  VND`

**Reasoning:**
Courier services from GHN (Giao Hàng Nhanh). Courier services are not in Annex I or II of Decree 174, so 8% applies in March 2026. Gross VND 10,800,000. Net = VND 10,000,000 + VND 800,000 input VAT. GHN is a major registered provider — electronic invoice should be available. Input credit of VND 800,000 claimable pending invoice verification.

**Classification:** Input VAT 8% — VND 800,000. Net expense: VND 10,000,000.

### Example 5 — Exempt financial service

**Input line:**
`01/04/2026  Lãi tiền gửi  Vietcombank  Lãi tháng 3/2026  +250,000  VND`

**Reasoning:**
Bank deposit interest. Interest income is exempt from VAT in Vietnam. EXCLUDE from the VAT return entirely. This is passive income — not a supply of goods or services for VAT purposes. No output VAT. Note: if the business has significant exempt income, a proration of input VAT may be required.

**Classification:** EXEMPT — exclude from GTGT return. Note any proration implications.

### Example 6 — International software (FCT flag)

**Input line:**
`05/04/2026  Thanh toán quốc tế  GOOGLE IRELAND LIMITED  Google Workspace April 2026  -3,300,000  VND`

**Reasoning:**
Payment to Google Ireland for cloud services. This triggers the Foreign Contractor Tax (FCT) rules in Vietnam. A business buyer on the deduction method may have to withhold and pay on the supplier's behalf (VAT Law art. 4.3 and 4.4), and the tax payment document then supports input VAT if the art. 14 conditions are met (VAT Law art. 11.1(c); Decree 181/2025/ND-CP, art. 25). Unconfirmed: the VAT and CIT components for this supply, and whether 8% applies. This is a complex area. Flag for specialist: confirm whether Google has registered directly in Vietnam or whether the buyer must withhold.

**Classification:** Tier 2 — FLAG for specialist. FCT rules may apply. Do not claim input credit until registration status and the tax payment document are confirmed.

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 10% and temporary rate 8%

- **Standard rate** — 10% (Default rate for goods and services not on the 0% or 5% lists, including services supplied by foreign providers without a permanent establishment through e-commerce and digital platforms)  _(VAT Law No. 48/2024/QH15 as amended, art. 9.3, consolidated text 12/VBHN-VPQH: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf)_
- **Temporary reduced rate** — 8% from 1 July 2025 to 31 December 2026 on goods and services otherwise at 10%. Excluded and staying at 10%: telecommunications; finance, banking, securities and insurance; real estate business; metal products; mineral products other than coal (Decree 174 Annex I lists these by product code); and goods and services subject to special consumption tax other than petrol (Annex II). A supply exempt or at 5% under the VAT Law gets no reduction. Invoice shows "8%"; the buyer claims the VAT shown  _(Resolution 204/2025/QH15, arts 1.1 and 2, quoted in 12/VBHN-VPQH, notes 5 and 9; Decree 174/2025/ND-CP, arts 1 and 2: https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/174nd.signed.pdf)_
- **Direct-method businesses in the same period** — % rate reduced by 20% when invoicing an eligible supply, with the reduction noted on the sales invoice  _(Decree 174/2025/ND-CP, art. 1.2(b) and 1.3(b))_
- **After 31 December 2026** — Resolution 204 and Decree 174 end on that date. No extension was found as at 31 October 2026; this is an absence of a result, not proof. Recheck before applying a rate to a later supply.

### 5.2 Reduced rate 5%

- **Reduced rate** — 5% (Applies to: clean water for production and domestic use, excluding bottled water; fertilizer, ore for fertilizer, plant protection products and livestock growth stimulants; dredging, crop-care and primary processing services for agriculture; crop, planted forest, livestock and aquatic products unprocessed or only ordinarily pre-processed, other than those exempt under art. 5.1; certain latex, jute, rattan and similar goods and newsprint; offshore fishing vessels and specialised farm machinery; medical equipment, medicines and their ingredients; teaching aids; traditional and folk performing arts; children's toys and books not exempt under art. 5.15; science and technology services; social housing.)  _(VAT Law No. 48/2024/QH15, art. 9.2)_

### 5.3 Zero rate — exports

- **Zero rate exports** — 0% (Services are zero-rated if supplied directly to a foreign organisation or individual, or in a non-tariff zone for export production, and consumed outside Vietnam, with a contract and a non-cash payment document. Art. 9.1(d) lists cases that never qualify, including technology transfer abroad, credit, and postal and telecommunications services.)  _(VAT Law No. 48/2024/QH15, art. 9.1; Decree 181/2025/ND-CP, art. 18.2: https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/181nd.signed.pdf)_

### 5.4 Exempt supplies

- **Exempt supplies** — Include: credit services and lending, securities business, capital transfers, debt sales, foreign exchange and derivatives (art. 5.9); life, health, agricultural and reinsurance services (art. 5.8); medical and veterinary services listed in art. 5.10; funeral services (art. 5.11); teaching and vocational training (art. 5.13); land use right transfers (art. 5.7); public-owned housing sold to its tenant (art. 5.5); public passenger transport by bus, tram and inland waterway (art. 5.16); technology transfer, intellectual property transfer, and software products and services (art. 5.21); animal feed (art. 5.3); and goods and services of household and individual businesses at or below the revenue threshold (art. 5.25). Read art. 5 for the full list of 27 items.  _(VAT Law No. 48/2024/QH15, art. 5)_

### 5.5 Deduction method (phương pháp khấu trừ)

- **Deduction method** — Business establishments, other than household and individual businesses, with full accounting and invoicing and annual revenue ≥ VND 1 billion, or that opt in, use the deduction method: Output VAT − Input VAT = Net VAT payable. Input credits require compliant hóa đơn GTGT (VAT invoices) or hóa đơn điện tử.  _(VAT Law No. 48/2024/QH15, art. 11; Decree 181/2025/ND-CP, art. 21)_

### 5.6 Direct method (phương pháp trực tiếp)

- **Direct method** — On value added, for gold, silver and gemstones: Tax = VAT rate × (selling price − purchase price). On revenue, for enterprises and cooperatives with annual revenue below VND 1 billion that have not opted in, household and individual businesses above the VND 1 billion exemption, and other listed taxpayers: Tax = % rate × revenue, at 1% for distribution and supply of goods, 5% for services and construction excluding materials, 3% for manufacturing, transport, services tied to goods and construction including materials, and 2% for other activities, each reduced by 20% on eligible supplies until 31 December 2026. No input credit mechanism. File using Form 04/GTGT.  _(VAT Law No. 48/2024/QH15, art. 12; Decree 174/2025/ND-CP, art. 1.2(b))_

### 5.7 e-Invoice requirements

- **e-Invoice requirements** — From 1 July 2022, all registered businesses must issue electronic invoices (hóa đơn điện tử) registered with the GDT portal. Required fields: seller's MST (tax code), buyer's MST, invoice date, goods/service description, quantity, unit price, net amount, VAT rate, VAT amount, total. Paper invoices no longer accepted for new issuances.

### 5.8 Filing deadlines

**Filing deadlines**

| Filer | Period | Due date |
| --- | --- | --- |
| Monthly filer (revenue > VND 50B) | Monthly | 20th of following month |
| Quarterly filer (revenue ≤ VND 50B) | Quarterly | 30th of month following quarter |
| Annual settlement | Calendar year | 31 March following year |

### 5.9 Penalties

**Penalties**

| Offence | Penalty |
| --- | --- |
| Late filing | VND 2,000,000–25,000,000 |
| Late payment | 0.03% per day of unpaid tax |
| Tax evasion | 1×–3× evaded tax + criminal liability |
| False invoice | Administrative + potential criminal |

## Section 6 — Tier 2 catalogue

### 6.1 Foreign contractor tax (FCT) on international services

- **FCT on international services** — **What it shows:** Payment to a foreign service provider. **What's missing:** Whether the foreign supplier has registered in Vietnam directly or whether FCT withholding applies. **Conservative default:** Flag — do not claim input credit until status confirmed. **Question to ask:** "Has this foreign supplier registered for VAT in Vietnam? Do they issue Vietnamese electronic invoices? If not, FCT withholding may be required."

### 6.2 Export qualification for services

- **Export qualification for services** — **What it shows:** Revenue from a foreign client. **What's missing:** Whether the service was consumed outside Vietnam, paid by a non-cash method, and the counterparty is a foreign entity. **Conservative default:** 10% domestic rate. **Question to ask:** "Was this service entirely consumed outside Vietnam? Is the client a foreign entity? Is there a contract and a non-cash payment record?"

### 6.3 Reduced rate confirmation (5% items)

- **Reduced rate confirmation** — **What it shows:** Purchase that might qualify for 5% (e.g., water, agricultural inputs, books). **What's missing:** Confirmation of specific product category. **Conservative default:** 10%. **Question to ask:** "What exactly was purchased? Is it on the 5% reduced rate list (clean water, fertilizer, medical equipment, books, etc.)? If not, does the e-invoice show 8% or 10%?"

### 6.4 Partial exemption — businesses with mixed supplies

- **Partial exemption** — **What it shows:** Business making both taxable and exempt sales (e.g., IT consulting + financial advisory). **What's missing:** The taxable/total revenue ratio for the period. **Conservative default:** 0% credit on shared overhead costs. **Question to ask:** "What proportion of your sales are taxable vs. exempt? Provide a monthly revenue breakdown."

### 6.5 VAT on vehicle expenses

- **VAT on vehicle expenses** — **What it shows:** Vehicle purchase, lease, fuel, or maintenance. **What's missing:** Whether the vehicle is used exclusively for business and whether input VAT is claimable. **Conservative default:** 0% input credit. **Question to ask:** "Is this vehicle registered in the company's name and used exclusively for business? VAT on personal-use or mixed vehicles is limited."

## Section 7 — Excel working paper template

```
VIETNAM VAT WORKING PAPER — BẢNG TÍNH THUẾ GTGT
Kỳ khai thuế (Period): ____________  MST: ____________

A. THUẾ ĐẦU RA (OUTPUT VAT)
  A1. Doanh thu chịu thuế 10% (net)           ___________
  A2. Thuế đầu ra 10% (A1 × 10%)              ___________
  A2a. Doanh thu chịu thuế 8% (net)           ___________
  A2b. Thuế đầu ra 8% (A2a × 8%)              ___________
  A3. Doanh thu chịu thuế 5% (net)            ___________
  A4. Thuế đầu ra 5% (A3 × 5%)                ___________
  A5. Xuất khẩu 0% (net)                      ___________
  A6. Doanh thu không chịu thuế (net)         ___________
  A7. Tổng thuế đầu ra (A2 + A2b + A4)        ___________

B. THUẾ ĐẦU VÀO (INPUT VAT)
  B1. Mua hàng chịu thuế 10% (net)            ___________
  B2. Thuế đầu vào 10% (B1 × 10%)             ___________
  B2a. Mua hàng chịu thuế 8% (net)            ___________
  B2b. Thuế đầu vào 8% (B2a × 8%)             ___________
  B3. Mua hàng chịu thuế 5% (net)             ___________
  B4. Thuế đầu vào 5% (B3 × 5%)               ___________
  B5. Thuế nhập khẩu đã nộp                   ___________
  B6. Tổng thuế đầu vào (B2+B2b+B4+B5)       ___________
  B7. Thuế đầu vào không được khấu trừ        ___________
  B8. Thuế đầu vào được khấu trừ (B6−B7)      ___________

C. THUẾ PHẢI NỘP
  C1. Chênh lệch thuế (A7 − B8)               ___________
  C2. Thuế còn được khấu trừ kỳ trước         ___________
  C3. Thuế GTGT phải nộp (C1 − C2)            ___________
  C4. Hoặc: Thuế còn được khấu trừ (nếu C1<C2) ___________

REVIEWER FLAGS:
  [ ] Hóa đơn điện tử confirmed for all input credits?
  [ ] Export evidence available for zero-rated sales?
  [ ] FCT status confirmed for all international service payments?
  [ ] 5% rate items correctly identified?
  [ ] 8% applied only to eligible supplies dated to 31 December 2026, and Annex III form prepared?
  [ ] Proration calculated for any exempt supplies?
```

## Section 8 — Bank statement reading guide

### Common Vietnamese bank statement formats

**Bank statement formats**

| Bank | Key columns | Date format | Amount |
| --- | --- | --- | --- |
| Vietcombank VCB | Ngày GD, Nội dung, Phát sinh nợ (debit), Phát sinh có (credit), Số dư | DD/MM/YYYY | VND (no decimals typically) |
| BIDV | Ngày, Mô tả, Số tiền ghi nợ, Số tiền ghi có, Số dư | DD/MM/YYYY | VND |
| Vietinbank | Ngày giao dịch, Nội dung, Số tiền, Số dư | DD/MM/YYYY | VND |
| Techcombank | Thời gian, Mô tả giao dịch, Số tiền ghi nợ, Số tiền ghi có, Số dư | DD/MM/YYYY | VND |
| MB Bank | Ngày, Nội dung giao dịch, Phát sinh, Số dư | DD/MM/YYYY | VND |

### Key Vietnamese banking terms

**Banking terms**

| Vietnamese | Meaning | Classification hint |
| --- | --- | --- |
| Nhận chuyển khoản | Incoming wire transfer | Potential revenue |
| Thanh toán / Chuyển khoản | Outgoing payment | Potential expense |
| Nhận ngoại tệ | Foreign currency receipt | Potential export |
| Lãi tiền gửi | Deposit interest | Exempt |
| Phí dịch vụ | Service fee | Bank charge — exempt |
| Số dư | Balance | Running balance — ignore |
| Nội dung | Transaction description / narrative | Key classification field |
| Thuế GTGT | VAT | Tax payment — exclude |
| Rút tiền ATM | ATM withdrawal | Tier 2 — ask |
| Thanh toán tự động | Auto-payment | Subscription/utility |

## Section 9 — Onboarding fallback

If the client provides a bank statement but cannot answer all questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark Tier 2 items as "PENDING — reviewer must confirm"
4. Generate working paper with flags

```
VIETNAM GTGT ONBOARDING — CÂU HỎI TỐI THIỂU
1. Mã số thuế (MST — 10-digit tax code)?
2. Phương pháp tính thuế: khấu trừ (deduction) hay trực tiếp (direct)?
3. Kỳ khai thuế: theo tháng hay theo quý?
4. Doanh thu năm trước (for determining monthly vs. quarterly)?
5. Có doanh thu xuất khẩu (zero-rated) không?
   Nếu có: paid in foreign currency? Hợp đồng với đối tác nước ngoài?
6. Có dịch vụ quốc tế (Google, Microsoft, etc.) không?
   Có hóa đơn GTGT từ nhà cung cấp nước ngoài không?
7. Số thuế GTGT còn được khấu trừ kỳ trước (excess credit carried forward)?
8. Có doanh thu không chịu thuế (exempt supplies) không?
```

## Section 10 — Reference material

### Key legislation

**Key legislation**

| Topic | Reference |
| --- | --- |
| VAT Law | Luật Thuế GTGT No. 48/2024/QH15 (in force 1 July 2025), amended by Laws 90/2025/QH15, 149/2025/QH15 and 09/2026/QH16; consolidated text 12/VBHN-VPQH: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf |
| Detailed rules | Decree 181/2025/ND-CP: https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/181nd.signed.pdf; Circular 69/2025/TT-BTC (not read) |
| VAT rates | VAT Law Article 9 |
| Temporary 8% rate | Resolution 204/2025/QH15; Decree 174/2025/ND-CP: https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/174nd.signed.pdf |
| Exempt supplies | VAT Law Article 5 |
| Calculation methods | VAT Law Articles 10–12 |
| Household and individual businesses | Decree 68/2026/ND-CP: https://xdcs.cdnchinhphu.vn/446259493575335936/2026/3/6/68-2026-nd-cp-05032026-signed-17727673940151875228819.pdf; Decree 141/2026/ND-CP: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/141-ndcp.signed.pdf |
| e-Invoice | Decree 123/2020/ND-CP; Circular 78/2021/TT-BTC |
| Export zero-rating | VAT Law Article 9.1; Decree 181/2025/ND-CP Articles 17–18 |
| Foreign contractor tax | Circular 103/2014/TT-BTC |
| Revenue thresholds | VAT Law Articles 5.25, 11.2 and 12.2 |
| Penalties | Law on Tax Administration No. 38/2019/QH14 |

### Known gaps

- Foreign Contractor Tax (FCT) computation — complex; escalate to specialist
- Partial exemption proration — requires full-year data; escalate
- Real estate and construction VAT — escalate
- Non-commercial import VAT — escalate
- Agricultural cooperative special rules — escalate
- Any extension of the 8% rate past 31 December 2026 — recheck
- Current Mẫu 01/GTGT line numbers, including the line for 8% sales — check the form

### Self-check before filing

- [ ] All hóa đơn điện tử (e-invoices) transmitted to GDT for sales
- [ ] All input credits supported by compliant electronic invoices
- [ ] Export zero-rating supported by contracts + FX transfer evidence
- [ ] FCT implications flagged for all international service payments
- [ ] 5%, 8% and 10% rates correctly applied by supply and date
- [ ] Form 01, Annex III of Decree 174 filed for 8% supplies
- [ ] Prior period excess credit correctly carried forward

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, FCT note, no inline tier tags |
| 2.0 | 31 October 2026 | Added the temporary 8% rate; rebased on VAT Law 48/2024/QH15 and its decrees; moved the examples to April 2026 |

## Prohibitions

- NEVER claim input VAT credit without a compliant hóa đơn điện tử (e-invoice)
- NEVER zero-rate a service without confirming foreign consumption + contract + non-cash payment
- NEVER apply 8% to an excluded supply, or to any supply after 31 December 2026 without a confirmed extension
- NEVER use the deduction method for a direct-method taxpayer
- NEVER ignore FCT implications for international service payments
- NEVER present calculations as definitive — direct to a licensed Vietnamese tax agent (đại lý thuế)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.

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
