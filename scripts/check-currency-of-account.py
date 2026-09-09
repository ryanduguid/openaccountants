"""Flag a guide whose money is denominated in a currency its folder does not use.

Related to `check-jurisdiction-placement.py` but blind to a different error. That
one reads jurisdiction *names*; this one reads the unit the amounts are actually
written in. A guide can name the right country in every heading and still quote
its thresholds in the wrong money -- the sort of thing that happens when a file
is copied from a neighbour and the prose is updated but the tables are not.

Self-calibrating, like the placement checker: no hard-coded country-to-currency
map. Each folder's house currency is whichever ISO 4217 code its guides use most
as a unit of account, so jurisdictions that legitimately transact in a foreign
currency -- Ecuador, Panama, Montenegro, Kosovo, Zimbabwe -- calibrate to what
they actually use rather than to what a lookup table would predict.

Only a code sitting immediately beside a number counts. `EUR 12,000` and
`2,979,000 RUB` are units of account; "the EUR is the reporting currency" is
prose, and a three-letter token that is not an ISO code (TCA, ORC, PMK, NTA)
is a statute abbreviation, not money. Without both filters the output is
unreadable: an earlier version made Australia's house currency `PCG` and
Canada's `QTA`.

Only ISO codes are read, so a folder that writes its money as a symbol
throughout -- `Bs`, `R$`, `KSh`, `₦` -- is invisible here and needs a different
check. Bolivia was an outlier until its pension cap stopped being quoted in
US dollars; once the bolivianos went in, the folder no longer had enough
ISO-coded amounts to have a house currency at all.

Run over `skills/` this reports 10 outliers in 314 jurisdictions and, read in
context, every one is correct as written:

  * cross-border guides -- `uk-to-uae-relocation-tax` in AED,
    `china-to-singapore-relocation-tax` and `india-to-uae-singapore-nri-tax`
    in USD -- properly denominate in the destination currency;
  * company-formation guides quote registry fees in the currency the registry
    or its agents quote (Tonga, North Macedonia, Romania);
  * `au-smsf` matches `SAR` five times: the SMSF Annual Return, not the Saudi
    riyal. An ISO code that is also a domestic acronym is the residual false
    positive and there is no way to filter it without reading the line.

That is a clean result, recorded so the next person does not have to re-derive
it. The check is cheap; keep running it as jurisdictions are added.

Usage: python3 scripts/check-currency-of-account.py [skills]
"""
import os, re, collections, sys

ISO4217 = set("""AED AFN ALL AMD ANG AOA ARS AUD AWG AZN BAM BBD BDT BGN BHD BIF BMD BND
BOB BRL BSD BTN BWP BYN BZD CAD CDF CHF CLP CNY COP CRC CUP CVE CZK DJF DKK DOP DZD EGP
ERN ETB EUR FJD FKP GBP GEL GHS GIP GMD GNF GTQ GYD HKD HNL HRK HTG HUF IDR ILS INR IQD
IRR ISK JMD JOD JPY KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LYD MAD MDL
MGA MKD MMK MNT MOP MRU MUR MVR MWK MXN MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK
PHP PKR PLN PYG QAR RON RSD RUB RWF SAR SBD SCR SDG SEK SGD SHP SLE SOS SRD SSP STN SVC
SYP SZL THB TJS TMT TND TOP TRY TTD TWD TZS UAH UGX USD UYU UZS VES VND VUV WST XAF XCD
XOF XPF YER ZAR ZMW ZWG ZWL""".split())

BEFORE = re.compile(r'\b([A-Z]{3})\b[  ]?\*{0,2}[\d]')
AFTER  = re.compile(r'[\d][\d,\.]*[  ]?\b([A-Z]{3})\b')

def units(path):
    c = collections.Counter()
    txt = open(path, encoding='utf-8', errors='replace').read()
    for pat in (BEFORE, AFTER):
        for m in pat.finditer(txt):
            if m.group(1) in ISO4217:
                c[m.group(1)] += 1
    return c

def main(root):
    byjur = collections.defaultdict(collections.Counter)
    files = collections.defaultdict(dict)
    for dp, _, fns in os.walk(root):
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            parts = p.split(os.sep)
            if len(parts) < 3:
                continue
            u = units(p)
            if u:
                files[parts[2]][p] = u
                byjur[parts[2]].update(u)

    flags = 0
    for jur in sorted(byjur):
        modal, mn = byjur[jur].most_common(1)[0]
        # too few amounts, or too few guides, to call a house currency at all
        if mn < 5 or len(files[jur]) < 3:
            continue
        for p, u in sorted(files[jur].items()):
            top, tn = u.most_common(1)[0]
            if top != modal and tn >= 4 and u[modal] == 0:
                print('%-26s house=%-4s %-64s uses %s x%d' % (jur, modal, p, top, tn))
                flags += 1
    print('jurisdictions with a house currency: %d   outliers: %d' % (len(byjur), flags))
    return flags

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'skills')
