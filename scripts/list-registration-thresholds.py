"""List each jurisdiction's stated VAT/GST registration threshold.

The third field to get an outside pass, after the standard rate and the annual
return deadline. It is worth doing early because it decides whether a business
registers at all: a threshold stated too high tells a trader who must register
that they need not, and the penalty for late registration usually runs from the
date they crossed the real one, not from the date they found out.

Same shape as list-vat-rates.py and list-filing-deadlines.py. This dumps the
claim so it can be compared against a source outside the repository. It does not
check anything, and a number here is a claim to verify rather than a defect.

Read the output with two things in mind. A jurisdiction can hold several real
thresholds at once, and rows that disagree usually show that rather than an
error: a lower one for services than for goods, a separate figure for
non-residents supplying digital services, a voluntary-registration floor beneath
the compulsory ceiling, and in the EU a domestic threshold beside the 100,000
EUR cross-border SME figure. And a threshold that is moving gets stated twice on
purpose, with dates, which is the guide doing its job.

Usage: python3 scripts/list-registration-thresholds.py [--selftest]
"""
import os, re, sys, collections

LABEL = re.compile(
    r'\b(?:VAT|GST|BTW|IVA|TVA|consumption tax|sales tax|turnover)?\s*'
    r'registration threshold\b|\bVAT threshold\b|\bGST threshold\b'
    r'|\bthreshold for (?:VAT|GST) registration\b', re.I)

# The corpus writes money three ways: "ALL 10,000,000", "40,000 EUR", "$75,000".
# The trailing group catches "NGN 25 million", which without it reads as NGN 25
# and understates the threshold by a factor of a million.
# Case matters here and re.I cost a run. Making the whole pattern
# case-insensitive so it would accept "Million" also let [A-Z]{2,5} match
# ordinary words, and the column filled with ANY 12, THE 21, FROM 1, GROUP 3
# and BOX 9. The currency code stays uppercase; only the scale word varies.
# The corpus also attaches the multiplier: "NGN 25M", "TZS 100m", "LKR 80M",
# "NGN 1B". Without the single letters those read as 25, 100, 80 and 1, and the
# jurisdiction appeared to state its threshold two ways. Longer alternatives
# come first so "million" is never matched as a bare "m", and the trailing \b
# stops "25 Monthly" reading as 25 million.
SCALE = (r'(?:\s*\**\s*([Mm]illion|MILLION|[Mm]illions|[Mm]n|[Bb]n|[Bb]illion|'
         r'[Tt]housand|[Ll]akh|[Cc]rore|[MmBbKk])\b)?')
CODE_FIRST = re.compile(r'\b([A-Z]{2,5})\s?([\d][\d,]*(?:\.\d+)?)' + SCALE)
CODE_AFTER = re.compile(r'\b([\d][\d,]*(?:\.\d+)?)' + SCALE + r'\s?([A-Z]{2,5})\b')
# Ukraine's threshold is written ₴1,000,000 and the first symbol class had no
# hryvnia, so the line yielded nothing at all rather than a wrong number.
SYMBOL = re.compile(r'([€£$₹₽¥₦₩₴₺₪₫฿₼₾៛])\s?([\d][\d,]*(?:\.\d+)?)' + SCALE)

MULT = {'million': 10**6, 'millions': 10**6, 'mn': 10**6, 'm': 10**6,
        'bn': 10**9, 'billion': 10**9, 'b': 10**9, 'thousand': 10**3, 'k': 10**3,
        'lakh': 10**5, 'crore': 10**7}

# Codes that are not currencies. Statute and levy names sit right beside a
# number and were read as money: "VATA 1994", "NTA 2025", "STA 1990",
# "FRS 105", "SDL 5%", "FOP 3", "CAT 12", "NSIF 20,000".
NOT_MONEY = {'VAT', 'GST', 'BTW', 'IVA', 'TVA', 'SME', 'EU', 'PWC', 'ETA', 'NO',
             'CGT', 'PIT', 'CIT', 'SBE', 'ABN', 'TIN', 'VATA', 'NTA', 'STA',
             'FRS', 'FA', 'FY', 'SDL', 'FOP', 'CAT', 'NSIF', 'ITA', 'PAYE',
             'TY', 'AY', 'IRA', 'MTD', 'OECD', 'IFRS', 'NIC', 'UTR', 'AND'}

YEARISH = re.compile(r'^(19|20)\d\d$')


def _size(digits, scale):
    """The number, with any "million" or "bn" beside it folded in."""
    n = float(digits.replace(',', ''))
    if scale:
        n *= MULT[scale.lower()]
    return '{:,}'.format(int(n)) if n == int(n) else '{:,}'.format(n)


def _rate_not_money(line, end):
    """A percent sign right after the number means it was a rate."""
    return line[end:end + 1] == '%'


def amounts_in(line):
    """Every money amount on the line, normalised to "CODE amount"."""
    out = []
    for m in CODE_FIRST.finditer(line):
        code = m.group(1).upper()
        if code in NOT_MONEY or YEARISH.match(m.group(2)) or _rate_not_money(line, m.end(2)):
            continue
        out.append('%s %s' % (code, _size(m.group(2), m.group(3))))
    for m in CODE_AFTER.finditer(line):
        code = m.group(3).upper()
        if code in NOT_MONEY or YEARISH.match(m.group(1)) or _rate_not_money(line, m.end(1)):
            continue
        out.append('%s %s' % (code, _size(m.group(1), m.group(2))))
    for m in SYMBOL.finditer(line):
        if _rate_not_money(line, m.end(2)):
            continue
        out.append('%s%s' % (m.group(1), _size(m.group(2), m.group(3))))
    # keep the order they appear, without repeats
    seen, uniq = set(), []
    for a in out:
        if a not in seen:
            seen.add(a)
            uniq.append(a)
    return uniq


def threshold_in(line):
    """The amounts on a line that states a registration threshold, else None."""
    if not LABEL.search(line):
        return None
    got = amounts_in(line)
    return got or None


def selftest():
    """Real lines from the corpus, in each of the three ways it writes money."""
    cases = [
        ('| VAT registration threshold | Turnover > ALL 10,000,000 (register within 15 days); '
         'standard VAT 20% [PwC; tatime.gov.al] |', ['ALL 10,000,000']),
        ('- **VAT registration threshold** - Mandatory registration once taxable turnover '
         'exceeds 40,000 EUR in a calendar year; EU-wide SME cross-border threshold 100,000 EUR.',
         ['EUR 40,000', 'EUR 100,000']),
        ('| GST registration threshold | $75,000 turnover ($150,000 for non-profits) |',
         ['$75,000', '$150,000']),
        ('| Registration threshold (general) | CNY 500,000/year (services); CNY 500,000/year '
         '(goods) for voluntary registration |', ['CNY 500,000']),
    ]
    # an ordinary English word is not a currency code. This is the real Ukraine
    # line, and under re.I it yielded GROUP 3 as a sum of money.
    assert threshold_in('| Key levers | (1) Regime choice - single tax (\u0454\u0434\u0438\u043d\u0438\u0439 '
                        '\u043f\u043e\u0434\u0430\u0442\u043e\u043a) Group 3 vs general system; (2) \u20b41,000,000 VAT '
                        'threshold; (3) Diia City for IT |') == ['\u20b41,000,000']
    scaled = [
        # "NGN 25 million" is not NGN 25
        ('| VAT registration threshold | NGN 25 million of annual taxable turnover |',
         ['NGN 25,000,000']),
        ('| VAT registration threshold | Turnover above S$1 million in a calendar year |',
         ['$1,000,000']),
        # the corpus also attaches the multiplier
        ('- **VAT registration threshold** - N25m taxable turnover in the trailing 12 months, '
         'per NGN 25M under the NTA 2025', ['NGN 25,000,000']),
        ('- **Registration threshold** - LKR 80M/year or LKR 20M/quarter (Mandatory registration)',
         ['LKR 80,000,000', 'LKR 20,000,000']),
        ('| **Phase 3** | Smaller taxpayers above the VAT registration threshold (NGN 25M to '
         'NGN 1B) | **2026** |', ['NGN 25,000,000', 'NGN 1,000,000,000']),
        # a bare M must not swallow the start of the next word
        ('- **VAT registration threshold** - NGN 25 Monthly filing applies above it',
         ['NGN 25']),
        # a statute name is not a currency, and a rate is not an amount
        ('- **VAT registration threshold** - NGN 25,000,000 under the NTA 2025; the SDL is 5% '
         'and is unrelated  _(VATA 1994)_', ['NGN 25,000,000']),
    ]
    cases = cases + scaled
    for line, want in cases:
        got = threshold_in(line)
        assert got == want, 'read %r from: %s' % (got, line[:70])
    # a line about something else is not a threshold, even with money on it
    assert threshold_in('Annual revenue BSD 30,000. Below VAT threshold.') is not None
    assert threshold_in('| Filing deadline | 31 October of the following year |') is None
    # "20% VAT" is a rate, not an amount, and must not be read as money
    assert threshold_in('| VAT registration threshold | none; every trader registers |') is None
    print('selftest: %d cases pass' % len(cases))


def main():
    out = collections.defaultdict(collections.Counter)
    for dp, _, fns in os.walk('skills'):
        parts = dp.split(os.sep)
        jur = parts[2] if len(parts) >= 3 else ''
        if jur in ('orchestrator', 'cross-border', 'verticals', 'integrations') or not jur:
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            for line in open(os.path.join(dp, fn), encoding='utf-8', errors='replace'):
                got = threshold_in(line)
                if got:
                    for a in got:
                        out[jur][a] += 1

    for jur in sorted(out):
        counts = out[jur]
        flag = '  <-- more than one figure' if len(counts) > 1 else ''
        print('%-26s %s%s' % (jur, ', '.join('%s (%d)' % (a, n)
                                             for a, n in counts.most_common()), flag))
    print('jurisdictions stating a registration threshold:', len(out))


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        main()
