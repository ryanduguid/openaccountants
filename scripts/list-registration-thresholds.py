"""List each jurisdiction's stated VAT/GST registration threshold.

The third field to get an outside pass, after the standard rate and the annual
return deadline. It is worth doing early because it decides whether a business
registers at all: a threshold stated too high tells a trader who must register
that they need not, and the penalty for late registration usually runs from the
date they crossed the real one, not from the date they found out.

Same shape as list-vat-rates.py and list-filing-deadlines.py. This dumps the
claim so it can be compared against a source outside the repository. It does not
check anything, and a number here is a claim to verify rather than a defect.

It keys on the phrase "registration threshold", so a jurisdiction that words it
another way does not appear. Malta is the case to remember: its Article 11
threshold of EUR 35,000 is in malta-vat-return, written as "the Article 11
threshold" and never as a registration threshold, so Malta shows nothing here
while stating the figure twice. The count below is jurisdictions using this
wording, not jurisdictions with a threshold.

Read the output with two things in mind. A jurisdiction can hold several real
thresholds at once, and rows that disagree usually show that rather than an
error: a lower one for services than for goods, a separate figure for
non-residents supplying digital services, a voluntary-registration floor beneath
the compulsory ceiling, and in the EU a domestic threshold beside the 100,000
EUR cross-border SME figure. And a threshold that is moving gets stated twice on
purpose, with dates, which is the guide doing its job.

Checked against an outside source so far. Two errors in eleven jurisdictions.

  * Egypt     WRONG, found by reading the column. Resolution No. 281 of 2025
              halved the threshold from EGP 500,000 to EGP 250,000 with effect
              from 1 January 2026, registration due by 31 March 2026 for anyone
              over it on 2025 revenue. eg-formation and eg-bookkeeping had the
              new figure; egypt-vat and eg-sme-tax did not.
  * Albania   WRONG by a factor of two. albania-tax-optimization gave the VAT
              threshold as ALL 5,000,000 (~EUR 40k) in four places, one of them
              a prohibition reading "NEVER ignore the ALL 5m VAT threshold".
              It is ALL 10,000,000, about EUR 96,200, with 15 days to apply.
              albania-income-tax had it right.

Random tranche of ten, drawn seed 20260909 from the 97 jurisdictions with a row.
Albania was the only error in it. Correct: Barbados BBD 200,000 (its BBD
16,666.67 is the same figure per month), Bosnia BAM 100,000 raised from 50,000
on 2 December 2023, Cameroon FCFA 100M for the regime reel and 50-100M for the
simplifie, Colombia 3,500 UVT stated as COP 174,296,500 and dated to 2025,
Ireland EUR 42,500 for services and EUR 85,000 for goods, Nepal NPR 5,000,000
for goods and 3,000,000 for services raised from 2,000,000 on 16 July 2024,
Tajikistan TJS 1,000,000, Tonga TOP 100,000.

Paraguay was in the draw and is not this field. Its row comes from
paraguay-payroll and is the PYG 80M IRP registration threshold, an income tax.
The guide is right; the column is reading past its own subject.

EU tranche, all eight that state one under this wording, against a single table
of member-state thresholds. Every one correct: Bulgaria BGN 100,000 (~EUR
51,000), Croatia EUR 60,000, Cyprus EUR 15,600, Estonia EUR 40,000, Ireland
EUR 42,500 and 85,000, Latvia EUR 50,000, Luxembourg EUR 50,000, Slovenia
EUR 60,000.

The interesting part was the EU states NOT in the column, because several state
a threshold under their own name for it.

  * France    WRONG, in 14 places across skills, agent-skills and the
              orchestrator. Franchise en base under art. 293 B CGI was given as
              EUR 36,800 for services (tolerance 39,100) and EUR 91,900 for
              goods (tolerance 101,000). Those are the pre-2025 figures. It is
              EUR 37,500 (tolerance 41,250) and EUR 85,000 (tolerance 93,500).
              Every worked example still holds at the new figures.
  * Germany   CORRECT. Kleinunternehmer under section 19 UStG at EUR 25,000
              prior year and EUR 100,000 current year.
  * Netherlands CORRECT. KOR at EUR 20,000.
  * Italy and Spain have no domestic VAT registration threshold, so their
    absence from the column is right. Italy's EUR 85,000 is the regime
    forfettario, a different thing.

France is the case for not trusting this column's coverage number. It states
its threshold in four files and none of them says "registration threshold", so
a reader watching only this output would have called France unstated rather
than wrong.

Still open: 102 jurisdictions use this wording, and 20 jurisdictions have now
been checked.

One known false positive, left in deliberately. The walk treats the third path
component as a jurisdiction and does not restrict itself to indirect-tax
material, so Oregon's corporate activity tax registration obligation matches the
generic threshold label and is reported under "or". It is a registration
threshold, just not a VAT or GST one. Filtering by slug would also drop real
sales-tax guides that do not say "vat" anywhere, so the reader is told instead:
a US-state row here is a registration threshold of some kind, and needs reading.

Usage: python3 scripts/list-registration-thresholds.py [--selftest]
"""
import os, re, sys, collections

LABEL = re.compile(
    r'\bregistration threshold\b|\bVAT threshold\b|\bGST threshold\b'
    r'|\bthreshold for (?:VAT|GST) registration\b', re.I)

# "Registration threshold" alone is not this field. Guatemala's employer IGSS
# registration threshold is one worker, cited to "Acuerdo JD 1529", and the
# column reported Guatemala as registering for VAT at 1,529 Jordanian dinars.
#
# Requiring an indirect-tax name on the line was tried and cost eight
# jurisdictions. China states its threshold inside china-vat.md without
# repeating the word, and Andorra's is an IGI threshold, IGI being Andorra's
# VAT under a name this list would never have guessed. Enumerating every
# country's word for its own indirect tax is a game you lose quietly.
#
# So the rule is the other way round: reject a social-security registration,
# which is the thing that actually misfired, and let the rest through.
SOCIAL = re.compile(r'\b(IGSS|INSS|IMSS|CNSS|NSSF|NAPSA|NSITF|SSC|PRSI|ZUS|INPS|'
                    r'AVS|CPF|EPF|SOCSO|GOSI|NIS|social security|social insurance|'
                    r'social contribution|employer registration|pension fund|'
                    r'health insurance|workers|employees)\b', re.I)

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
# Slovakia writes its VAT limits "50 000 eur" and "62 500 eur": a space for the
# thousands separator and a lowercase code. Both rows matched the threshold
# label and yielded no amount, so Slovakia was simply absent from the output.
#
# The obvious fix is re.I on CODE_AFTER, and it is the wrong one -- the comment
# above records what that cost the first time, when [A-Z]{2,5} started matching
# ordinary words and the column filled with ANY 12 and THE 21. So the lowercase
# form gets its own pattern with an explicit list of codes instead of a
# character class, which cannot match a word by accident.
LOWER_CODES = ('eur|usd|gbp|chf|sek|nok|dkk|pln|czk|huf|ron|bgn|hrk|isk|try|rub|uah|'
               'inr|cny|jpy|krw|sgd|myr|thb|php|idr|vnd|aud|nzd|cad|zar|ngn|kes|ghs|'
               'mad|egp|aed|sar|qar|ils|brl|mxn|ars|clp|cop|pen|uyu')
CODE_AFTER_LOWER = re.compile(
    r'\b([\d][\d  ,]*(?:\.\d+)?)' + SCALE + r'\s?(' + LOWER_CODES + r')\b')
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
             'TY', 'AY', 'IRA', 'MTD', 'OECD', 'IFRS', 'NIC', 'UTR', 'AND',
             # Ordinary words that are all-caps in a heading or an emphasised
             # cell. They only reach here when the source shouts, which is why
             # the earlier re.I experiment filled the column with them.
             # ALL is deliberately NOT here: it is the Albanian lek, and adding
             # it removed Albania's VAT threshold -- a figure corrected on this
             # same branch. The selftest caught it because that line is a
             # fixture. Check any word added here against the ISO 4217 list.
             'ANY', 'THE', 'FROM', 'BOX', 'GROUP', 'OVER', 'PER',
             'NOTE', 'SEE', 'FOR', 'WITH'}

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
    for m in CODE_AFTER_LOWER.finditer(line):
        digits = m.group(1).replace(' ', '').replace('\u00a0', '').replace('\u202f', '')
        if YEARISH.match(digits) or _rate_not_money(line, m.end(1)):
            continue
        out.append('%s %s' % (m.group(3).upper(), _size(digits, m.group(2))))
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


def threshold_in(line, slug=''):
    """The amounts on a line that states a registration threshold, else None."""
    if not LABEL.search(line):
        return None
    if SOCIAL.search(line) or SOCIAL.search(slug.replace('-', ' ')):
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
         '(goods) for voluntary registration |', ['CNY 500,000'], 'china-vat'),
    ]
    # Malta's SSC registration threshold is a different field too
    assert threshold_in('- **Registration threshold** - Self-employment income above EUR 910/year '
                        'triggers SSC registration obligation.', 'malta-ssc') is None
    # a social-security registration threshold is a different field, and its
    # citation number is not a sum of money
    assert threshold_in('- **T1-11 Employer IGSS registration threshold** - Employer IGSS '
                        'registration threshold = 1 worker since 17 Jan 2023 (Acuerdo JD 1529)') is None
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
         ['LKR 80,000,000', 'LKR 20,000,000'], 'sri-lanka-vat'),
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
    for case in cases:
        line, want = case[0], case[1]
        slug = case[2] if len(case) > 2 else ''
        got = threshold_in(line, slug)
        assert got == want, 'read %r from: %s' % (got, line[:70])
    # a line about something else is not a threshold, even with money on it
    assert threshold_in('Annual revenue BSD 30,000. Below VAT threshold.') is not None
    assert threshold_in('| Filing deadline | 31 October of the following year |') is None
    # "20% VAT" is a rate, not an amount, and must not be read as money
    assert threshold_in('| VAT registration threshold | none; every trader registers |') is None
    # Slovakia writes it "50 000 eur": space separator, lowercase code. Both
    # rows matched the label and returned nothing until this was added.
    assert amounts_in('| Mandatory VAT registration | 50 000 eur of turnover |') == ['EUR 50,000']
    assert amounts_in('| Voluntary registration | 62 500 eur |') == ['EUR 62,500']
    # and ALL stays a currency code, not the ordinary word
    assert amounts_in('| VAT registration threshold | Turnover > ALL 10,000,000 |') == ['ALL 10,000,000']
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
                got = threshold_in(line, fn[:-3])
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
