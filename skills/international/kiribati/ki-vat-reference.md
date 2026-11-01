---
name: ki-vat-reference
description: >
  Kiribati value added tax reference for an ordinary taxable business in 2026.
  Gives the 12.5% and zero rates, the $100,000 registration test, exempt and
  zero-rated schedules as amended, input tax apportionment, tax invoices,
  quarterly returns and payment, imports, non-residents, refunds, interest,
  penalties and worked figures. Trigger on Kiribati VAT, form RET 020 or Kiribati
  Tax Division returns. Refuses voluntary registration, gambling, foreign suppliers
  and platforms, going concern transfers and return lodgement with imported
  services. This source-cited draft awaits local professional review and is not
  filing readiness.
jurisdiction: KI
category: international
tax_year: 2026
tax_year_notes: "2026 VAT periods. Act 14/2013 read with VAT Regulations 2014, Exempt Supplies Regulations 2016, VAT (Amendment) Act 2025 and Third Schedule Regulations 2025, the last 2 from 1 January 2026. Amending instruments from 2014 to 2024 other than those regulations are neither found nor excluded. Regulations called for by the 2025 Act not found. Revenue Administration Act 2013 read as enacted; commencement date and later amendments not established."
tier: 2
last_updated: 2026-10-31
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - vat-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kiribati VAT Reference, 2026

Load this on top of `vat-workflow-base`. This file answers its section 7 slots so far as the sources allow. **It is incomplete as a country skill.** Slots 6, 7 and 13 have little or no Kiribati source. Use this file for rates, treatment, dates and briefing a local adviser. HOLD means the sources read do not establish the point, and no figure may be supplied for it from memory.

**Citations.** 'Act' is the Value Added Tax Act 2013 (No. 14 of 2013). '2025 Act' is the Value Added Tax (Amendment) Act 2025, in force 1 January 2026 (s 2); its number field is blank on the copy read. 'Regs 2014' is the Value Added Tax Regulations 2014. '2016 Regs' is the Exempt Supplies Regulations 2016. '2025 Regs' is the Value Added Tax (Amendment of Third Schedule) Regulations 2025. 'RAA' is the Revenue Administration Act 2013.

**Reading limits that affect every section.**

- The Act, the 2025 Act, the 2016 Regs and the 2025 Regs survive as scans and were read through OCR. Pages 4, 9, 17, 23, 27, 30, 31, 37, 43, 44 and 48 of the Act, pages 4 and 12 of the 2025 Act, page 2 of the 2016 Regs and page 1 of the 2025 Regs were compared with page images. All other text of those instruments rests on OCR only. Regs 2014 pages 1, 2, 3, 6 and 14 were read as images, and its other pages as PDF text.
- No consolidation was found, so 'as amended' is assembled from each instrument.
- The Act says 'Board'. The 2025 Act says 'Commissioner' in amended sections and inserts no definition in its s 4. This guide keeps each source's word. HOLD who the Commissioner is. Neither the RAA memorandum, which on s 61 says 'lodging of documents with the Commissioner', nor IMF staff reports, which mention a 'tax commission', define the term.
- RAA s 1(2) starts that Act on a date notified in the Gazette. HOLD the date. The Tax Division's leaflets cite the RAA as operative.

All amounts are Australian dollars (Act s 48(1)). Foreign currency converts, for an import, at the rate applicable under the Customs Act for import duty and, otherwise, at the 'Reserve Bank of Australia mid-exchange rate' on the date the amount is taken into account (s 48(2)). No rounding rule was found: HOLD. The cents shown here are a drafting choice.

## Slot 1: Standard rate

12.5% on a taxable supply by a registered person, a taxable import and a supply of imported services (Act s 7(1), (3)(b)). The Act applies to supplies and imports on or after 1 January 2014 (s 1(2)). The 2025 Act's amendment of s 7 touches s 7(7) only, and no other section read changes the rate.

**Tax fraction:** r / (1 + r) (s 2). `0.125 ÷ 1.125 = 1/9` (computed), so tax-inclusive VAT is the amount divided by 9, as return boxes 5 and 11 do. Where no separate VAT is identified, value is A - (A x B), B being the tax fraction (s 17(4)).

## Slot 2: Reduced rate

None. Section 7(3) has only zero percent for a zero-rated supply and 12.5% otherwise.

## Slot 3: Return form

Form RET 020, 'Value Added Tax Return', is captured with 16 boxes. It is undated and cites 'VAT Act 2014'. Instructions exist in I-Kiribati only. The gist below is a reading of that text, not a certified translation.

| Box | Form label | Instruction, in gist |
|---|---|---|
| 1 | Total Sales and Income including VAT | All sales, including zero-rated and exempt, and VAT-inclusive sales to Government even where VAT is withheld |
| 2 | Zero-Rated Supplies | Exports and other Third Schedule supplies |
| 3 | Exempt Supplies | Second Schedule supplies, such as uncooked rice and wheat flour |
| 4 | Box 1 less boxes 2 and 3 | Sales bearing VAT |
| 5 | Box 4 divided by 9 | VAT for the quarter |
| 6 | Adjustments to VAT Collected | Corrections; needs the Board's permission or an explanatory letter first |
| 7 | Boxes 5 and 6 | Total VAT Collected |
| 8 | Total Purchases and Expenses including VAT | Excludes the cost of imports and VAT paid to Customs |
| 9 | Non-creditable Acquisitions | Purchases with no VAT, such as uncooked rice or purchases from unregistered businesses; salaries and wages may go here |
| 10 | Box 8 less box 9 | |
| 11 | Box 10 divided by 9 | |
| 12 | VAT on Imports Paid to Customs | |
| 13 | Government Withheld VAT | VAT withheld by Government, so that it is not paid twice |
| 14 | Adjustments to VAT Paid | Corrections as for box 6; also the 'one off' import duty credit on documentary evidence (inference: Act s 54(4), a transitional rule from VAT's introduction, so check its dates before any use in 2026) |
| 15 | Boxes 11, 12, 13 and 14 | Total VAT Paid |
| 16 | Difference between boxes 7 and 15 | Box 7 larger: VAT to pay. Box 15 larger: VAT credit |

**HOLD:**

- The form has no line for component B of s 29 (VAT on imported services) and no apportionment line. It appears to predate the 2025 Act (inference).
- Box 9's instruction names only purchases with no VAT, but boxes 8 to 11 would credit every other purchase. Inference from its label, 'Non-creditable Acquisitions': entertainment and other s 26 purchases, and purchases wholly for exempt supplies (Regs 2014 reg 8(1)(b)), also go in box 9.
- The form has no line for credit brought forward. Box 16 says 'VAT credit', whilst its instruction says 'refund' ('okiriko'). Apply s 30: carry forward first, and do not treat a box 16 credit as an immediate refund. Ask the Tax Division where to enter credit brought forward.
- The form says 'Please include any late payment penalties for this period with your payment'. RAA s 68(4) makes a person liable for penalty only once it is assessed and served. Apply s 68(4) and flag the wording.
- Do not assign imported services or apportioned credit to a box without the Tax Division's instruction. See R-KI-7.
- No form was found for the s 38(2) liability notice.
- Box 1 asks for all sales and income, and boxes 2 and 3 remove only zero-rated and exempt supplies. Applied literally to receipts outside VAT, such as sales through a foreign branch, box 5 would overstate output tax. Do not map these automatically: ask the Tax Division.

## Slot 4: Portal

No online filing system was found in the sources. The form says 'Return to Internal Revenue Board', P.O. Box 67, Bairiki, Tarawa, and the guidelines say a completed return is filed at the Tax office, signed by the owner or an authorised person with a consent letter. Documents must be delivered 'by personal delivery or normal post to an office of the Board' (RAA s 58; Regs 2014 reg 13), so post is available. The Board may establish electronic filing (RAA s 60); no procedure was found: HOLD electronic filing.

## Slot 5: Deadlines

| Item | Rule | Source |
|---|---|---|
| VAT period | 3 months ending on the last day of March, June, September and December | Act s 2 |
| Return | 'within 15 days after the end of the period' | Act s 38(1), renumbered by 2025 Act s 27 |
| Payment | 'payable by the due date for filing the VAT return' | Act s 39(1) |
| Unregistered business, imported services (from 1 January 2026) | Liability notice within 15 days after the period; payment by the same date. The notice counts as a tax return and self-assessment return | Act ss 38(2), (3), 39(3); 2025 Act ss 27, 28 |
| Taxable import | At the time of import | Act s 39(2) |
| Government withholding | The Government entity pays within 15 days after the calendar month of its payment | Act s 43(1) |
| Final return on cancellation | Within 15 days after the cancellation date | Act s 11(5)(b) |
| Weekend or public holiday | The next business day | RAA s 61 |
| Extension to file | Apply before the due date; 'does not change the date for payment' | RAA s 15 |

For the 2026 periods: 15 January 2026 (a Thursday) for December 2025; 15 April 2026 (a Wednesday) for March; 15 July 2026 (a Wednesday) for June; 15 October 2026 (a Thursday) for September; 15 January 2027 (a Friday) for December. No holiday calendar was read, so check each date against RAA s 61.

**Administrative conflict:** the due-dates leaflet's filing table says 'after end of the month' for the quarterly return, whilst its payment table says quarter. The filing obligations leaflet and guidelines say quarter. Act s 38(1) governs.

## Accounting basis (HOLD on unpaid invoices)

Output tax is 'the VAT received' (s 2), component A of s 29 is output tax 'received or deemed to have been received', and credit is allowed in the period the input tax 'is paid' (s 25(2)). The Explanatory Memorandum says net VAT is 'accounted for on a payments basis' (p 48). Yet s 7(4) says liability arises at the time of supply, which is the earlier of invoice and payment (s 14(1)). Section 7(4) itself continues that the VAT is accounted for under s 39(1), which refers to net VAT under s 29, so it leads back to the 'received' test. Section 22(1) treats lay-by output tax as 'received' on delivery, and 'received' includes amounts applied on the person's behalf (s 2). Inference: an invoice unpaid at quarter end does not yet enter the return. Against that, box 1 asks for 'Total Sales and Income' and reg 8(1)(c) tests supplies 'made' in the period, so neither clearly follows receipts. Have the Tax Division confirm this. The worked examples assume receipts and payments in the same period.

## Registration

**Must apply (Act s 8(1)):**

- (a) at the beginning of any 12 month period, on reasonable grounds to expect taxable supplies in that period will exceed the threshold;
- (b) at the end of any 12 month or lesser period in which they exceed it;
- (c) a Government entity that has commenced to 'make taxable supplies' (2025 Act s 9(1), replacing 'undertake an enterprise').

**Threshold:** $100,000 (s 8(2), not amended). Exactly $100,000 does not exceed it (inference from 'exceed'). The test is taxable supplies, so zero-rated supplies count and exempt supplies do not (inference from s 7(3)(a)). The guidelines' '$100,000.00 sales' is looser: follow s 8.

**Ignored in the test:** sale of a capital asset, and supplies made solely on selling all or part of the enterprise or permanently ceasing it (s 8(3)). The Board may have regard to an associate's supplies (s 8(4)). Section 8(6), which counted imported services, is repealed from 1 January 2026 (2025 Act s 9(2)).

**Application and effect:** approved form, within 7 days of becoming required (s 8(5)). The Board must register a person who fails to apply (s 9(2)). Effect is from the beginning of the first VAT period after the person was required to apply, or a later time on the certificate (s 9(4)). The guidelines say registration 'could be dated back' to when the business reached $100,000. That wording does not match s 9(4); follow the Act and flag it. A person required to apply who has not done so in time is already a 'registered person' (s 2).

**Voluntary registration: not available on the text.** 'Only persons who are required to apply for registration under section 8 can be registered' (s 9(5), not amended). See R-KI-1.

**Tenders:** an unregistered bidder for a Government tender quotes inclusive of VAT and, if the award requires registration, charges VAT on related taxable supplies (s 48A; 2025 Act s 34). Its 'section 9' reference looks like an error for s 8 (inference).

**After registration:**

- Display the certificate, if carrying on the enterprise at physical premises (s 10(1) as amended).
- Specify registration details on any website and social media account used for the enterprise (s 10(2) as substituted).
- Notify in writing within 21 days any change in contact details, places of business (including opening or closing branches or divisions, or a change of internet address or social media account), bank details or the nature of the enterprise (s 10(3)).
- A branch enterprise registers once, except Government entities (s 46).

**Cancellation, as amended (2025 Act s 11):**

- A registered person must notify if it 'has ceased to make taxable supplies', in the approved form, within 7 days, stating the date and whether it intends to make taxable supplies within 12 calendar months (s 11(1), (2)).
- The Commissioner must cancel on notice or on own motion, unless satisfied the cessation is only temporary (s 11(3)).
- Effect is from the date in the notice (s 11(4)).
- The person ceases to hold out as registered, including on websites and social media, files a final return and pays within 15 days, and returns the certificate (s 11(5)).
- Inventory on which credit was allowed is a deemed taxable supply, with output tax equal to that credit (s 12), except for input tax unpaid at cancellation. Input tax paid after cancellation on that inventory gets no credit (Regs 2014 reg 4).
- Excess credit not applied under s 30 at the cancellation date must be claimed in the approved form before cancellation takes effect, or that excess 'lapses' (s 11A; 2025 Act s 12).

**HOLD, falling below the threshold:** the substituted s 11(1) to (3) drops the former limb for turnover below the threshold, yet the 2025 Explanatory Memorandum says s 11 provides a notification procedure where annual value falls below the threshold. Text and memorandum differ. See R-KI-6.

## Taxable supply, place, time and value

**Taxable supply:** a supply, other than an exempt supply, made in Kiribati in the course or furtherance of an enterprise (s 2). An enterprise excludes employment and hobbies (s 3(2)). From 2026, 'Kiribati' includes the archipelago waters, territorial sea and exclusive economic zone (2025 Act s 4(6)).

**Goods and services, from 2026:** money and digital currency are outside goods and services. Transmitted products are services (2025 Act s 4(4), (13)). 'Digital currency' depends on regulations not found: R-KI-8. **HOLD:** 2025 Act s 4(12) puts hire or lease of goods in 'supply of goods', whilst new s 14(5)(b)(i) still speaks of a supply of services by way of a lease of goods.

**Place, goods:** delivered or made available in Kiribati, or in Kiribati when transportation commences (s 15, now s 15(1)).

**Place, services:** the supplier's enterprise from which the services are supplied is in Kiribati (s 16(1)). Section 16(2), as amended, covers a non-resident without a fixed place of business: services performed in Kiribati, services directly related to immovable property in Kiribati, remote services to a resident of Kiribati, inbound tourism products and related agency or booking services, and certain telecommunications services (2025 Act s 15).

**Time:**

- The earlier of invoice date and any payment (s 14(1)).
- Associates or gifts: delivery of goods or completion of services (s 14(2)).
- Vending and metered devices: when the coin, note or token is taken out (s 14(3)).
- Periodic supplies: successive supplies, each at the earlier of due date and receipt (s 14(4), (5) as substituted).
- Lay-by: delivery (s 22(1)).

**Value:** the price (s 17(1)), being money and the fair market value of anything in kind, plus taxes, duties, levies, fees and charges other than VAT, less discounts accounted for at the time of supply (s 5(1)). Other rules:

- Fair market value applies to a below-value or free supply to an associate who cannot credit the whole input tax (s 17(2)).
- Otherwise no price means zero value (s 17(3)).
- Goods applied to private or exempt use after credit are a deemed supply, with output tax equal to the credit, except for input tax then unpaid. Input tax paid after first private or exempt use gets no credit (s 19; Regs 2014 reg 5).
- Mixed supplies: an incidental supply follows the principal supply (s 13(1)). Other single supplies are split by fair market value (Regs 2014 reg 3). The formula is A x B/C, being the total price, times the fair market value of the separate supply, over the sum of those values (reg 3, page image). The Board may allow another reasonable treatment (reg 3(4)).

**Vouchers, lay-by and hire purchase:**

- Issuing a monetary voucher is not a supply. On redemption for a taxable supply, other than a zero-rated one, the voucher amount splits by the tax fraction (s 21(2), (3)).
- From 2026, an unused or expired voucher is a supply of services at expiry; a registered supplier's value is the unused amount less the tax fraction of it (s 21(3A); 2025 Act s 19).
- Cancelling a lay-by and keeping money is a supply of services with the VAT treatment the goods would have had (s 22(2); 2025 Act s 20).
- Hire purchase agreements now include a finance lease as defined in the Income Tax Act 2023 (2025 Act s 4(5)). That Act was not read, so HOLD the treatment of credit charges under ss 5(2) and 13(2).

**Pricing:** to an unregistered person, prices are VAT-inclusive, with a sign or invoice notice, and invoices state whether the supply is taxable or exempt and the rate (s 37). Government entities within para (a) of the definition withhold VAT on supplies to them, which discharges the supplier (s 43).

## Exempt supplies

The Second Schedule para (1) now reads as follows. Do not read the Act's printed list alone.

| Item | Source |
|---|---|
| Financial services, not debt collection, factoring or custody services | Sch 2 para (1)(a), (3) |
| Precious metal: gold at least 99.5, silver 99.9, platinum 99.0 fineness | (1)(b), (3) |
| Donated goods or services by a non-profit body, being goods or services gifted to the body and intended for use in carrying out its purposes; the body must be carried on for charitable or religious purposes, with no income or assets conferring a private benefit | (1)(c), (3) |
| Sale or long-term lease (over 50 years) of residential premises, other than new; 'new' includes premises created by a substantial renovation of a building | (1)(d), (3) |
| Lease of residential premises, other than for a term under 2 months | (1)(e) |
| Holiday or hotel accommodation on terms consistent with a landlord and tenant agreement, at least 2 continuous months | (1)(f) |
| Unimproved land; education services, being education provided by the institutions listed, such as a school, college or university, so a private tutor needs checking | (1)(g), (h), (3) |
| Medical, dental or nursing services 'by a registered person under the Medical Services Act' | (1)(i) |
| Medicine that only a registered pharmacist may sell | (1)(j), (3) |
| Uncooked rice; uncooked wheat flour; kerosene; a bicycle or parts; bicycle repair services; a mosquito net; benzol (benzene); oil No. 50; an exercise book | (1)(k) to (s), Regs 2014 reg 19 |
| All services supplied by SOEs listed in the First Schedule of the State Owned Enterprises Act, and by Councils established under the Local Government Act | para (1)A, 2016 Regs reg 4, deemed from 1 January 2016 |

- A supply both zero-rated and exempt is zero-rated only (Sch 2 para (2)).
- The 2016 Regs reach services, so goods sold by an SOE or Council do not fall under para (1)A (inference). HOLD the SOE list, which was not held.
- 'Oil No. 50' has no definition in the sources: HOLD.
- **Conflict on SOEs:** IMF Country Report 26/099, not law, says 'the VAT (Amendment) Act requires SOEs to pay VAT' and that exemptions in SOE-specific laws create inconsistencies. No amendment or repeal of para (1)A appears in the 2025 Act as read. Apply the text and have the Tax Division confirm before relying on the exemption. The same report says the RAA is under review.
- An exemption in another Act or agreement does not exempt from VAT unless this Act provides it (s 50(2)).

## Zero-rated supplies

**Part I (exports):** an export of goods with documentary proof acceptable to the Board; consumable stores for an aircraft or ship leaving Kiribati or a fishing vessel going outside Kiribati waters; goods and services for temporarily imported goods; services for use or consumption outside Kiribati with documentary proof; telecommunications services supplied by a resident telecommunications supplier to a non-resident telecommunications supplier, or initiated from outside Kiribati; international transport services, not ancillary transport services; and a fishing licence used principally to make exports of fish (Sch 3 Part I; Regs 2014 reg 20(a)). Goods re-imported, or to be re-imported, do not qualify under para (1)(a) or (b) only (para (2)).

**Part II:**

- a going concern transfer on written agreement and the para (1) conditions (R-KI-4);
- transportation of passengers in Kiribati by bus, truck or taxi, 'other than by a tour operator' (Regs 2014 reg 20(b));
- from 1 January 2026, maternity pads, menstrual cups, pads and liners, menstrual underwear, tampons and other such products, but not a product not 'exclusively for menstrual health or hygiene use' (2025 Regs reg 3).

Zero rating of the menstrual products is an inference: the Regulations insert them in Part II, whose heading and introductory words make its supplies zero-rated. **Numbering conflict:** the 2025 Regs insert a new para (2) after 'paragraph 1(d)' although Regs 2014 reg 20 already added a para (2). Both appear to stand (inference).

## Conflict with the August 2024 leaflet

The leaflet says it is compiled from the Act, Regs 2014 and the 2016 Regs. Its rice, flour, kerosene, bicycle, mosquito net, benzol, oil No. 50 and exercise book items, and its 4 litre, 2.25 litre and $200 private use figures, trace to Regs 2014 regs 18 and 19, and its SOE and Council item traces to the 2016 Regs. On those items the printed Schedules are out of date and the leaflet is right. **Differences remain and are held. Apply the instrument text and flag each:**

| Point | Leaflet | Instrument |
|---|---|---|
| Precious metal | 'does not include jewellery' | Gold, silver and platinum 'in any form' at the fineness stated; jewellery is not mentioned |
| Medical services | No provider limit | 'by a registered person under the Medical Services Act' |
| Passenger or crew goods, non-commercial up to AUD $200 | Not in the VAT list; in the excise list | Sch 1 para (1)(a)(i), not removed by reg 18 |
| Who gets the traveller allowance | 'International travelers' | 'a passenger or a member of a crew of a ship or aircraft' (Sch 1 para (1)(a)) |
| Telecommunications | 'made by a person physically outside of Kiribati' | Initiated while physically outside Kiribati |
| Menstrual products | Absent (it predates them) | 2025 Regs |
| Hotel accommodation | 2 continuous months or more | Also 'terms consistent with a landlord and tenant agreement' (Sch 2 para (1)(f)) |
| Services used outside Kiribati | No proof condition | 'documentary proof acceptable to the Board' (Sch 3 para (1)(e)) |
| Goods and services for repair of temporarily imported goods | Used in the repair | Goods must be wrought into them or be consumable stores, and services 'directly in connection with' them (Sch 3 para (1)(c), (d)) |

This table lists the differences found and may not be exhaustive.

Regs 2014 reg 1 starts the Regulations with the Act, on a date before they were made. They are dated 10 April 2014, handwritten on page 14 (page image). Section 51(3) gives retrospective effect only to transitional regulations. This affects early 2014 only: HOLD for those periods.

## Input tax

**Entitlement:** credit for input tax on a creditable acquisition to the extent it was for making taxable supplies, as determined at the time of acquisition (s 25(1)). A creditable acquisition is a taxable supply by another registered person, a taxable import or, from 2026, a supply of imported services (s 2; 2025 Act s 4(2)). Zero-rated supplies are taxable supplies (s 7(3)(a)).

**Timing and documents:** allowed when paid, but not until the person holds a tax invoice, bill of entry or other Customs document, debit or credit note, or recipient-created tax invoice (s 25(2) to (4)). A missed claim may be made in a later return, 'within 12 months after the VAT period in which the credit arose' (s 25(5); 2025 Act s 22).

**Denied:**

- entertainment, meaning food, beverages, tobacco, amusement, recreation or hospitality, unless provided in the ordinary course of an entertainment enterprise and not to an associate or employee, or provided whilst the recipient is away from home for the enterprise (s 26(1)(a), (2));
- club, association or society membership or entry of a sporting, social or recreational nature (s 26(1)(b));
- any credit for a foreign supplier (s 26(1A));
- creditable acquisitions for taxable gambling supplies (Regs 2014 reg 6(4)).

No passenger vehicle block appears in s 26.

**Apportionment (Regs 2014 reg 8):** the leaflet's 80% and 20% footnote traces here.

- Wholly taxable: full credit (reg 8(1)(a)).
- Wholly non-taxable: none (reg 8(1)(b)).
- Mixed: A x B/C (page image). A is mixed input tax for the VAT period, B the value of all taxable supplies, and C the value of all supplies other than through an enterprise outside Kiribati (reg 8(1)(c)).
- B/C 'more than 0.80': full credit on component A (reg 8(2)(a)).
- B/C 'less than 0.20': none (reg 8(2)(b)).
- Exactly 0.80 or 0.20: apportion (inference from the wording; the leaflet agrees).

The test uses values for each VAT period, whereas the leaflet speaks of 'sales'; use values. No annual adjustment was found.

**Other credits:**

- New registrants: in the first return, input tax paid on goods held at registration for making taxable supplies, if held as inventory at the end of the day before registration, acquired in a creditable acquisition no more than 4 months before registration, with documentary evidence satisfactory to the Board that input tax was paid (s 27(1)). Stock sold before registration does not qualify.
- Second-hand goods: only for a 'second-hand goods supplier', a registered person whose enterprise 'principally involves the re-supply of second-hand goods in substantially the same state' (s 20(5)). An ordinary trader gets no credit on a purchase from an unregistered seller. The dealer's taxable supply must be by way of a sale or exchange, of goods bought from an unregistered person and previously used by an unregistered person in Kiribati, resold in substantially the same state, and their supply to the dealer must not be exempt or zero-rated (s 20(1), (5); 2025 Act s 18). Deemed input tax is the tax fraction of the price, credited when the resale occurs (s 20(2)). The dealer keeps a record whose contents depend on regulations not found (s 20(4)). The Act's trade-in rule is s 20(3).

## Tax invoices and records

From 2026, a registered person making a taxable supply 'to another person' issues the original tax invoice at the time of supply, with the particulars in the Regulations (s 32(1) substituted; before 2026, only to registered persons). Other than for gambling (Regs 2014 reg 6(5)):

- **Full tax invoice (reg 9(1)):** 'TAX INVOICE' prominently; names, addresses and taxpayer identification numbers of both parties; serial number and issue date; description with quantity or volume, and supply date; price and VAT.
- **Under $500 between registered persons (reg 9(2)):** a shorter form.

**HOLD:** reg 9 predates the wider duty and asks for a recipient's taxpayer identification number that an unregistered customer may lack. No later regulation was found. Do not treat an invoice to an unregistered customer as compliant until the Tax Division confirms the approved form.

**Credit and debit notes:** on an adjustment event (s 28(6), s 33), with reg 10 particulars. Adjustment events are cancellation, a fundamental alteration, a price change and a return of goods. Tax effect, in the period of the event or of receiving the note (use with the box 6 and 14 hold in Slot 3):

- VAT under-accounted: the excess is output tax of the supplier (s 28(1)), and a recipient holding a debit note gets credit (s 28(2)).
- VAT over-accounted: the supplier gets a credit (s 28(3)), and a recipient holding a credit note has output tax (s 28(4)).
- Unregistered recipient: no supplier credit until the excess is repaid to the recipient (s 28(5)).

**Requests:** a registered recipient asks in writing within 60 days and the supplier complies within 14 days (s 35). **One original only:** a marked copy for a lost original (s 36(1)). **Agents:** s 34.

**Records:** the documents in s 36(3) and the books in Regs 2014 reg 12, including VAT accounts, ledgers, invoices, cash register rolls and bank statements, kept in Kiribati, in English, for 7 years after the tax period (RAA s 13). Issued documents are kept in chronological order (s 36(4)). The leaflet's 'after the tax year' differs from 'tax period': follow the RAA.

## Interest, penalties and offences

| Item | Rule | Source |
|---|---|---|
| Late payment interest | 'the greater of $10 or interest at the rate of 15% per annum', or a prescribed rate, from due date to payment; no prescribed rate found | RAA s 34(1) |
| Late payment penalty | 15% of unpaid tax, excluding penalty | RAA s 64 |
| Late filing | $30 per month or part, up to $500 each failure (the leaflets omit the cap) | RAA s 63 |
| Records | 75% if knowing or reckless, otherwise 20%, of tax for the period; AUD$100 if none | RAA s 65 |
| Tax shortfall | 75% if knowing or reckless, otherwise 20%; plus 10 points on a second and 25 on a third or later application; less 10 points on voluntary disclosure. None if the person could not reasonably be expected to know the statement was false, on a reasonably arguable position in a self-assessment (not one contrary to a public ruling in force), or on a clerical or similar error; interest can still run | RAA s 66(2) to (7) |
| Failure to apply for registration | Double the VAT payable, without reasonable excuse, for the period from the day the person was first required to apply to the earlier of filing an application or registration by the Board on its own motion | Act s 44, now s 44(1), page image checked |
| Wrongly seeking, or failing to seek, cancellation | $500 | s 44(2) |
| Failing to provide, or wrongly issuing, a tax invoice, credit or debit note | $100 first; $500 for second and later | s 44(3), (4) |
| Sections 10, 11(5)(a) or (c), 37, 41A or 35, or VAT representative | $100 | s 44(5) |
| Offences, s 45(1) list | Up to $5,000, or 2 years, or both | Act s 45(1), page image checked |
| Smuggling offences | Up to $100,000, or 10 years, or both | Act s 45(2), page image checked |
| RAA offences ss 69 to 77, including late filing and failure to withhold | Up to $5,000, or 2 years, or both | RAA s 81(1) |

- A penalty applies only once assessed and served (RAA s 68(4), (5)), is barred after conviction for the same act (s 68(2)) and is refunded if prosecution starts (s 68(3); Act s 45(3)).
- Assessments may be amended within 6 years, and at any time for fraud or wilful neglect (RAA s 21(3)).
- Appeals go to the Board within 60 days of service of the assessment (RAA s 25(2)(b)), or later if the Board accepts that reasonable cause prevented timely lodgement (s 25(3)), and to the Tribunal within 90 days of service if there is no agreement with the Board within 30 days of lodging, or the Board does not accept the notice as valid. The Tribunal may extend the time on written application, and the applicant serves a copy on the Board within 7 days of lodging (RAA s 26(1) to (4)).
- A part payment applies to tax, then penalty, then interest (RAA s 33(1)).
- Interest is simple (RAA s 34(4)). 'Tax' includes penalty (RAA s 2), and the memorandum says interest applies to late penalty.
- The Board may remit penalty, except s 66 penalty, on application or its own motion with the Minister's approval (RAA s 68(7), (8)).
- A taxpayer may apply for more time to pay (RAA s 31). The Board may assess a non-filer on best judgment (RAA s 19) and has a closure power over repeat non-filers (RAA s 41). These were noted, not worked through.

**HOLD:**

- The 2025 Act adds s 44(2) to (5) but does not amend s 45, so the same conduct has a civil and a criminal route. RAA s 68(9) bars both, or penalty under more than one provision, for the same act. Which route applies is the Board's choice on the sources read.
- Section 44(2)(b) still says 'apply for cancellation', whilst s 11 now says notify.
- RAA s 34 gives no daily method. Counting interest per day on a 365 day year is a drafting assumption.

## Refunds

- **Excess credit:** carried forward to the next period and the next, earliest first; any amount still uncredited is refunded on written application in the approved form under the RAA (s 30(1), (2)). The memorandum says 2 VAT periods (p 48).
- **Time limit from 2026:** 'within 1 year after the end of the second VAT period', or the uncredited amount 'is reduced to zero' (s 30(4), (5); 2025 Act s 24). Inference: the second period is the second of the carry-forward periods.
- **Regular excess:** where excess credits are 'a regular feature' of the enterprise, the Board must refund within 30 days after filing, on written application (s 30(3)). The memorandum's example is an exporter (p 48). Section 30(4) names only s 30(1)(b).
- **Overpaid tax:** claim within 3 years of the end of the tax period (RAA s 42). HOLD whether this can reach a credit reduced to zero under s 30(5). Inference: it cannot, as that is not tax paid in excess.
- **Cancellation:** s 11A above.
- **Diplomats, international organisations, aid contractors:** s 31; Regs 2014 reg 11 (R-KI-5).

## Imports

- **Exempt imports (Sch 1, as amended by reg 18):** by a passenger or crew member, non-commercial goods up to AUD $200, not more than 200 cigarettes or 250 grams of tobacco products, a combination of not more than 250 grams, not more than 4 litres of wine and 2.25 litres of other alcohol; ship and aircraft stores; a single consignment 'for private use up to a maximum value of' AUD $200; diplomatic and international organisation imports to the extent provided; goods whose supply in Kiribati would be exempt or zero-rated; and goods on which no customs duty is payable under the Ministry's exemption policy, which was not held (HOLD its contents).
- **Value:** customs value, plus services treated as part of the import, 'including' freight and insurance from 2026, plus duty, excise and other charges other than VAT (s 24(1); 2025 Act s 21, which the memorandum calls CIF). Goods re-imported after export for repair, renovation or improvement: the increase in value, only if their form or character and their ownership have not changed; otherwise s 24(1) applies (s 24(2)).
- **Collection:** by the Comptroller of Customs at import (ss 39(2), 40). Bill of entry supports credit (s 25(4)(a)).
- **Electronically ordered goods:** not a taxable import where a registered supplier or platform has collected the VAT in advance (s 2 as amended). The supplier gives Customs documentation specified in Regulations not found (s 39(4)).
- **HOLD:** Regs 2014 reg 14(b) cites Customs Act sections and $500 and $20 limits, but the Customs Act reference is now 2019 (2025 Act s 4(3)). Those section numbers were not checked.

## Imported services and non-residents (from 1 January 2026)

**Imported services:** a supply to a registered person or unregistered business, by a person outside Kiribati with no place of business there, that is not a taxable supply only because it is not made in Kiribati and would be taxable if it were (s 6(1) as amended). Former para (e) is gone, so a fully taxable registered person is now within it. Section 18 is repealed.

- **Unregistered business:** 'total value of all supplies made in Kiribati in any 12-month period exceeds $100,000', and not registered. The definition's 'all supplies' reaches exempt supplies (inference). Its 'registered business' is undefined.
- **Liability:** the recipient accounts (s 7(7) as amended). A registered person prepares a recipient-created tax invoice at the time of supply (s 32(2)) and includes the VAT in component B (s 29). Credit follows if the service is for taxable supplies (ss 2, 25(1), 25(4)(e)). The result is nil net for a fully taxable person if payment and the period coincide, because credit follows payment (s 25(2)) whilst component B uses the period (inference); the form has no line for it.
- **Unregistered recipient business:** liability notice and payment (ss 38(2), 39(3)). No credit route appears, because creditable acquisitions belong to registered persons (inference).
- **Value:** the price under s 17(1) (inference, as s 18 is repealed). Internal services from an overseas branch: fair market value at completion, unless the supply would be exempt (s 6(2) to (4)).
- **Notice to the supplier:** the recipient must notify a remote supplier in writing that it is liable, at or before the time of supply (s 41A). Without notice, the supplier treats the supply as not imported services (s 16(2D)).

**Foreign suppliers and platforms:** ss 15(2), (3), 16(2) to (2D), 16A, 26(1A), 41 and 48(3) to (5). Residence uses at least 2 of 6 indicators (s 16(2A)). The substituted s 41 removes the general duty on non-residents without a fixed place to appoint a representative: the Commissioner may require security on reasonable grounds of expected non-compliance, then a representative if the supplier fails. Regs 2014 reg 15 still refers to 'non-resident' for s 41: HOLD. See R-KI-3.

## Slot 6: Supplier patterns (partial)

The base requires 25 entries. The sources name classes, not bank-statement payees. This slot is not met.

| Pattern | Treatment | Source |
|---|---|---|
| Listed SOE, Council: services | Exempt; no credit | para (1)A |
| Bank, insurer: financial services | Exempt; debt collection, factoring and custody are not | Sch 2 |
| Bus, truck, taxi, not a tour operator | Zero-rated | Sch 3 Part II |
| International sea or air carrier | Zero-rated transport | Sch 3 Part I |
| Customs: VAT on import | Box 12, with Customs document | ss 25(4)(a), 40 |
| Government department paying a registered supplier | Withholds; box 13 | s 43 |

## Slots 7 to 10, 12 to 15

- **Slot 7, exclusions:** employment is outside an enterprise (s 3(2)(a)), and the instructions let wages go in box 9. Money is outside goods and services (s 2). No local bank patterns were found.
- **Slot 8, refusals:**
  - R-KI-1: treating a person as able to register voluntarily (s 9(5)).
  - R-KI-2: gambling supplies (Regs 2014 reg 6) and prepaid telecommunications cards (reg 7).
  - R-KI-3: foreign suppliers, electronic distribution platforms and electronically ordered goods.
  - R-KI-4: going concern transfers (Sch 3 Part II para (1)).
  - R-KI-5: diplomatic, international organisation and aid project refunds or cards (s 31; reg 11).
  - R-KI-6: cancellation for turnover below the threshold, without the Board's confirmation.
  - R-KI-7: lodgement-ready returns for a period with imported services or apportioned credit, or using boxes 6 or 14.
  - R-KI-8: digital currency and tax avoidance determinations (s 47).
- **Slot 9, questions:** taxable supplies in the last 12 months and expected in the next 12; associates; imported services and their use; exempt share of supplies; entertainment purpose; Government customers; invoice or cash timing.
- **Slot 10, defaults:** keep input tax out where the document is missing (s 25(3)) or entertainment use is unknown. This is a drafting choice, not Kiribati law.
- **Slot 12, template:** the 16 boxes in Slot 3.
- **Slot 13, red flags:** no source. Use the base's general flags without a local figure.
- **Slot 14, inputs:** sales and purchase records, tax invoices, bills of entry, withheld VAT records, prior period credit.
- **Slot 15:** no source.

## Slot 11: Worked examples (fictional)

Tarawa Bluewave Traders Ltd is registered. Prices include VAT unless stated. Receipts and payments fall in the period. The base's bank-statement requirement is not met.

**Tax-inclusive sale to a walk-in customer, $1,125:** `1,125 ÷ 9 = 125.00` VAT; value `1,125 - 125 = 1,000.00` (s 17(4)); check `1,000 × 12.5% = 125.00`.

**Import of stock for taxable sales, VAT paid to Customs and bill of entry held:** customs value $14,000; freight and insurance not already in it $1,000; duty $1,000. Value `14,000 + 1,000 + 1,000 = 16,000` (s 24(1)). VAT `16,000 × 12.5% = 2,000.00`.

**Quarter to 31 March 2026, form RET 020:**

| Box | Working | Amount |
|---|---|---|
| 1 | `90,000 + 11,250 + 15,000 + 8,000 = 124,250` (retail; Government sale; exports; uncooked rice) | 124,250.00 |
| 2 | Exports | 15,000.00 |
| 3 | Uncooked rice | 8,000.00 |
| 4 | `124,250 - 15,000 - 8,000 = 101,250` | 101,250.00 |
| 5 | `101,250 ÷ 9 = 11,250` | 11,250.00 |
| 7 | No adjustment in box 6 | 11,250.00 |
| 8 | `27,000 + 9,000 + 4,500 = 40,500` (taxable purchases; wages; uncooked rice stock) | 40,500.00 |
| 9 | `9,000 + 4,500 = 13,500` | 13,500.00 |
| 10 | `40,500 - 13,500 = 27,000` | 27,000.00 |
| 11 | `27,000 ÷ 9 = 3,000` | 3,000.00 |
| 12 | The import above | 2,000.00 |
| 13 | `11,250 ÷ 9 = 1,250` | 1,250.00 |
| 15 | `3,000 + 2,000 + 1,250 = 6,250` | 6,250.00 |
| 16 | `11,250 - 6,250 = 5,000`: VAT to pay, by 15 April 2026 | 5,000.00 |

Check by s 29, excluding withheld VAT from A: `(11,250 - 1,250) - (3,000 + 2,000) = 5,000`.

**Apportionment test for that quarter:** taxable value `(101,250 - 11,250) + 15,000 = 105,000`; all supplies `105,000 + 8,000 = 113,000`; `105,000 ÷ 113,000 = 0.929`, more than 0.80, so full credit on any mixed input tax (reg 8(2)(a)). This reaches component A only: the quarter assumes none of the $27,000 purchases relates wholly to the rice sales, which reg 8(1)(b) would deny.

**Apportionment at a lower share:** mixed input tax $900; B $70,000; C $100,000. `70,000 ÷ 100,000 = 0.70`; `900 × 0.70 = 630.00` credit.

**Offshore consultant with no place of business in Kiribati, giving a remote service used wholly for taxable supplies, price $4,000, the s 6(1) conditions being met (classify first; services performed in Kiribati are not this case):** `4,000 × 12.5% = 500.00` in component B; net `500 - 500 = 0` if credit of $500.00 arises in the same period. That rests on what 'paid' means for s 25(2) when the recipient accounts for the VAT itself, which is not settled: HOLD the nil result until the Tax Division confirms it (R-KI-7). The recipient-created tax invoice and s 41A notice remain mandatory; only their particulars are unsettled.

**Second-hand goods:** Tarawa Bluewave, a general trader, gets no credit under s 20. A separate fictional dealer, Betio Reuse Traders Ltd, whose enterprise principally resells second-hand goods, buys goods for $900 from an unregistered seller who used them in Kiribati, the purchase is not of an exempt or zero-rated kind, and it sells them as a taxable supply in the same state: `900 ÷ 9 = 100.00` deemed input tax, on resale (s 20(2)).

**Late example:** VAT of $5,000 due 15 April 2026, return and payment on 10 July 2026, 86 days late.

- Interest: `5,000 × 15% × 86 ÷ 365 = 176.71`, which is more than $10.
- Late payment penalty: `5,000 × 15% = 750.00`.
- Late filing: `3 × 30 = 90.00` (2 full months and part of a third).
- Conditional total: `5,000 + 176.71 + 750 + 90 = 6,016.71`.

This is not an assessed amount. It assumes interest counted daily on a 365 day year, and assessment and service of the penalties (RAA s 68(4)). No interest is shown on the penalties because they are due only on the date in the notice (RAA s 68(6)); interest would run if they stayed unpaid after it. No holiday shift is assumed.

## Delivery holds

Tier 2 draft pending review by a Kiribati adviser. It establishes no filing readiness. Output is a working paper. Its 2026 completeness depends on the gaps below and on the RAA's commencement and amendments, so check the Gazette and any consolidation first. Not read or not found: instruments called for by the 2025 Act (digital currency, second-hand records, Customs documentation, updated invoice particulars); any amending instrument from 2014 to 2024 other than Regs 2014 and the 2016 Regs; any instrument after the 2025 Act; the Income Tax Act 2023, State Owned Enterprises Act, Customs Act 2019, Excise Act 2013 and the Ministry's customs exemption policy; rulings and administrative practice.

## Sources

Retrieval date: 31 October 2026. Local copies were read that day, captured from these URLs on 28 and 30 October 2026.

- [Value Added Tax Act 2013](https://tax.gov.ki/wp-content/uploads/2024/09/Value-Added-Tax-Act-No.14-of-2013.pdf)
- [Value Added Tax (Amendment) Act 2025](https://www.president.gov.ki/images/Gazettes/2025/Value_Added_Tax_Amendment_Act_2025.pdf)
- [Value Added Tax Regulations 2014](https://tax.gov.ki/wp-content/uploads/2024/09/VAT-Regulation.pdf)
- [Exempt Supplies Regulations 2016](https://tax.gov.ki/wp-content/uploads/2024/09/2016-Exempt-Supplies-Regulation-for-Sect-51-of-VAT-Act-2013.pdf)
- [Value Added Tax (Amendment of Third Schedule) Regulations 2025](https://www.president.gov.ki/images/Gazettes/2026/VAT_Regulation.pdf)
- [Revenue Administration Act 2013](https://www.paclii.org/ki/legis/num_act/raa2013256/), PacLII, a non-official host, as enacted
- [IMF Country Report 26/099](https://www.elibrary.imf.org/view/journals/002/2026/099/article-A001-en.xml), secondary and not law, for the SOE conflict only
- Tax Division: [Exempt and zero-rated supplies, August 2024](https://tax.gov.ki/wp-content/uploads/2025/05/Exempt-0-rated-supplies_AUG-2024-1.pdf); [VAT return form](https://tax.gov.ki/wp-content/uploads/2025/05/VAT-Return-Form.pdf); [VAT return instruction](https://tax.gov.ki/wp-content/uploads/2025/05/Kiribati-VAT-return-instruction.pdf); [Guidelines and obligations](https://tax.gov.ki/wp-content/uploads/2025/05/Guidelines-Obligations-for-VAT-Registered-Businesses.pdf); [Due dates, offences and penalties](https://tax.gov.ki/wp-content/uploads/2024/09/Due-Dates-Offences-Panalties.pdf); [Due dates poster](https://tax.gov.ki/wp-content/uploads/2024/09/Due-Dates-Public-Notice-Poster.pdf); [Filing obligations](https://tax.gov.ki/wp-content/uploads/2024/09/Filing-Obligations-new.pdf)

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
