---
name: tw-nhi
description: >
  Use this skill whenever asked about Taiwan National Health Insurance (NHI) for self-employed individuals.
  Trigger on phrases like "NHI", "健保", "全民健康保險", "health insurance Taiwan", "supplementary premium",
  "二代健保", "Taiwan social insurance", or any question about NHI premiums, coverage, or payment obligations
  for self-employed persons in Taiwan. Covers mandatory enrollment, premium calculation, supplementary premiums,
  and payment methods. ALWAYS read this skill before touching any Taiwan NHI work.
version: 1.0
jurisdiction: TW
tax_year: 2025
category: international
---

# Taiwan National Health Insurance (NHI) — Self-Employed Skill v1.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Taiwan (Republic of China) |
| System | National Health Insurance (全民健康保險) |
| Authority | National Health Insurance Administration (NHIA / 衛生福利部中央健康保險署) |
| Website | nhi.gov.tw |
| Legal basis | National Health Insurance Act (全民健康保險法) |
| Coverage | Mandatory for all residents |
| General premium rate | **5.17%** of insured payroll (2025) |
| Supplementary premium rate | **2.11%** (二代健保補充保費) |
| Payment | Monthly, by bank transfer, convenience store, or auto-debit |

---

## Section 2 — Who must enroll

### Mandatory enrollment

All ROC nationals with household registration (戶籍) and foreign nationals with ARC holding valid employment or residency. No opt-out.

### Self-employed categories

| NHI Category | Description | Premium sharing |
|---|---|---|
| **Category 1, Group 4** | Self-employed with registered business (營利事業負責人) | Insured 100% |
| **Category 1, Group 5** | Professionals and technicians (專門職業及技術人員自行執業者) | Insured 100% |
| **Category 5** | Members of local association (區公所加保 — no employer) | Insured 60%, government 40% |

Self-employed without a registered business typically enroll through their local district office or occupational union (職業工會).

---

## Section 3 — Premium calculation

### General premium formula

```
Monthly premium = Insured payroll × 5.17% × (1 + number of dependents, max 3)
```

### Insured payroll grades (投保金額)

Self-employed declare income; NHIA assigns a payroll grade:

| Grade range | Monthly insured payroll (2025) |
|---|---|
| Grade 1 (minimum) | NT$27,470 |
| Grade 10 | NT$34,800 |
| Grade 20 | NT$45,800 |
| Grade 30 | NT$57,800 |
| Grade 40 | NT$72,800 |
| Grade 50 (maximum) | NT$219,500 |

Actual grades are set by the NHIA based on reported income. Self-employed through occupational unions use the union-declared grade.

### Example calculation

Self-employed, insured payroll NT$45,800, no dependents:
```
NT$45,800 × 5.17% × 1 = NT$2,368/month
```

With spouse as dependent:
```
NT$45,800 × 5.17% × 2 = NT$4,736/month
```

Maximum dependents counted: 3 (insured + 3 dependents = ×4 multiplier)

---

## Section 4 — Supplementary premium (二代健保補充保費)

### Rate: 2.11% on specified income types

The supplementary premium applies to income that exceeds certain thresholds, collected at source:

| Income type | Threshold | Rate |
|---|---|---|
| **Bonus income** (獎金) | Exceeds 4× monthly insured payroll | 2.11% on excess |
| **Part-time salary** (兼職所得) | Single payment > NT$20,000 | 2.11% |
| **Professional fees** (執行業務收入) | Single payment > NT$20,000 | 2.11% |
| **Rental income** (租金收入) | Single payment > NT$20,000 | 2.11% |
| **Interest income** (利息所得) | Single payment > NT$20,000 | 2.11% |
| **Dividend income** (股利所得) | Single payment > NT$20,000 | 2.11% |

### Cap

Maximum supplementary premium base per payment: NT$10,000,000.

### Collection mechanism

Payers (employers, banks, companies paying dividends) withhold supplementary premium at source and remit to NHIA.

Self-employed receiving the above income types: the payer deducts 2.11% before payment.

---

## Section 5 — Payment and deadlines

### Monthly premium payment

| Method | Details |
|---|---|
| **Auto-debit** (自動轉帳) | From bank or post office account |
| **Convenience store** | Print payment slip from NHI website |
| **Bank transfer** | To NHIA designated account |
| **Online** | Via NHI app or website |

### Due date

Premium is due by the **last day of the following month**. Late payment incurs 0.1% daily interest penalty.

### Annual adjustment

NHIA reviews insured payroll grades annually based on tax filing data. Grade may be adjusted up if reported income increased.

---

## Section 6 — Tax deductibility

NHI premiums (general + supplementary) are **fully deductible** from individual income tax:

- General premium: deduct as part of insurance expense (列舉扣除額 — 保險費), capped at NT$24,000/person for general insurance but **NHI has no cap** (unlimited deduction)
- Supplementary premium: deductible as paid

This makes NHI one of the most tax-efficient deductions available.

---

## Section 7 — Edge cases

### EC1: New business registration
Within 3 days of starting a business, must register with NHIA through the local health bureau or NHI group insurance office. Failure to register: retroactive premiums plus penalties.

### EC2: Multiple income sources
If self-employed AND employed, premiums are paid through the employer for the employment portion. Self-employment triggers supplementary premium on professional fees received.

### EC3: Income below minimum
If declared income is below minimum insured payroll (NT$27,470), premium is still calculated on the minimum grade. No exemption.

### EC4: Temporary departure from Taiwan
If abroad >6 months continuously, can apply to suspend NHI. Re-enrollment required upon return with a waiting period of 3 months (or pay retroactive premiums).

### EC5: Dependents
Spouse and direct relatives (parents, children) without their own employment can be enrolled as dependents under the self-employed person's NHI. Maximum 3 dependents counted for premium multiplication.

---

## Section 8 — Prohibitions

1. **NEVER** advise on medical coverage, benefits, or claims — this skill covers premiums and payment obligations only
2. **NEVER** calculate premiums without confirming the correct insured payroll grade
3. **NEVER** assume NHI can be opted out of — it is mandatory for all residents
4. **NEVER** treat supplementary premium as optional — it is withheld at source automatically
5. **REFUSE** questions about employer NHI obligations for companies with >5 employees — out of scope for self-employed skill

---

## Disclaimer

All rates and thresholds are based on 2025 NHIA published schedules. NHI rates are reviewed periodically and may change. This skill covers self-employed NHI obligations only — medical benefits, claims, and coverage questions are out of scope.

All outputs must be reviewed by a qualified tax professional (會計師) before filing.

*OpenAccountants — openaccountants.com*
