# Myanmar — the IRD publishes its rates in Burmese, and the CT guide had only the middle of the range

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`www.ird.gov.mm` answers 200 and is current. Its *tax-knowledge* section carries pages for
individuals, companies, the self-employed and co-operatives, with the rates written out in
Burmese prose. `mm-tax-overview.md` already cited the individual page; **`myanmar-ct.md`
cited no URL at all** — its sources line read *"Myanmar Commercial Tax Law (as amended).
IRD guidelines. Union Tax Law (annual rates)"*.

The guide knew the standard rate (5%) and the specific-goods band (8%–100%). The IRD's
Companies page gives **two lower rates it did not have**:

- **3%** on proceeds from constructing and selling buildings —
  *"အဆောက်အအုံများ ဆောက်လုပ် ရောင်းချခြင်းမှ ရောင်းရငွေများအပေါ်တွင် ကုန်သွယ်လုပ်ငန်းခွန် ၃ ရာခိုင်နှုန်း ကျသင့်ပါမည်။"*
- **1%** on proceeds from selling gold jewellery —
  *"ရွှေထည်လက်ဝတ်ရတနာများရောင်းချရငွေအပေါ်တွင် ကုန်သွယ်လုပ်ငန်းခွန် ၁ ရာခိုင်နှုန်း ကျသင့်ပါမည်။"*

**Both interact badly with rules the guide already had.** Its conservative default is
*"Unknown rate on a sale → 5%"*, which over-charges a construction sale by two thirds. And
its higher-rate row lists **gems** among the specific goods at 25%–100%, so a classifier
that sees "jewellery" and reaches for the gems band is wrong by a wide margin — gold
jewellery is the **1%** case. A guide can be right about the standard rate and the
penal rates and still mis-price the two sectors that sit below them.

Also added: for specific goods, **commercial tax is charged on proceeds inclusive of the
specific goods tax** — CT sits on top of SGT rather than beside it, which changes the base
and not just the rate.

**A reading note on the numerals.** The page writes figures in Burmese digits — ၃ is 3,
၁ is 1, ၂၂ is 22 — so every figure here was transliterated before being believed. The same
page gives corporate income tax at **၂၂% (22%)** on net profit, company capital gains at
**၁၀% (10%)**, and an oil-and-gas capital-gains scale of **40 / 45 / 50 per cent** across
three bands at MMK 100,000 million and 150,000 million. Those are **now written into
`mm-tax-overview.md`**, where the corporate rate and the commercial-tax rate had been
cited to a commercial summary and are now cited to the IRD.

**The oil-and-gas scale is the one that matters.** The overview gave capital gains as a
flat **10%** with an MMK 10,000,000 exemption. For companies in the **oil and natural gas
sector** the IRD gives a three-band scale — **40%** up to MMK 100,000 million, **45%** to
150,000 million, **50%** above — payable in the currency received. That is five times the
rate the overview carried, in the sector where a Myanmar asset sale is most likely to be
large enough for anyone to ask. The row now says both, and says which is which.
