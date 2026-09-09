#!/usr/bin/env python3
"""Check the arithmetic asserted in guide worked examples.

Scans every guide for spans of the form `expr = expr [= expr]`, evaluates each
side, and reports any whose final asserted result does not follow. This catches
the class of error that no rate table can: a correct rate applied to produce a
wrong number, and worked examples left stale when a rate around them changed.

Deliberately conservative — it only reports a span when it is unambiguously
arithmetic, because a false positive costs a reviewer more than a miss:

  * operators must be whitespace-delimited, so `11,925-48,475` stays a range;
  * en dashes are always ranges, never subtraction;
  * the left side must be a real computation (two or more numbers and an
    operator), so `15% = $930` — which is missing its base — is skipped;
  * only the final `= answer` is checked, because earlier segments of a chain
    such as `(A - B) = C x r = D` are narrative restatement;
  * number format is detected per line, so European `1.234,56` and en-US
    `1,234.56` both parse.

Residual false positives are mostly parentheticals that hold the product
(`(1,728,000 - 1,325,127) x 46.29% (186,489.91) = ...`), cumulative running
totals, and units the parser drops (CNY 万).

**Triage by reading the guide around the line, never the line alone.** Two
flags in `skills/` were dismissed as artefacts on the shape of the line and
were real:

  * `bc-individual-return` -- "521 - (3.56% x $25,000) = $521 - $890 = $0" was
    filed as a credit-sign convention. It was the B.C. tax reduction computed
    against the whole of net income instead of the excess over the threshold,
    on a base that was $41 stale, and it told a taxpayer entitled to $562 that
    they got nothing.
  * `bs-income-tax` -- "3 x 4.333" looked like a fragment of a longer span. It
    was not; the example around it produced three mutually inconsistent
    monthly totals.

A third miss was structural rather than a triage error, and it was silent. An
answer written in bold -- `... = **487,450.80**` -- reached `eval` with the
asterisks still attached, `eval` raised, and the span was dropped without ever
being counted. Nothing in the output said so: the totals simply omitted it.
Stripping markdown emphasis before parsing took `skills packages agent-skills`
from 20,666 evaluated expressions to 23,402, so roughly one asserted sum in
eight had never been checked at all, and surfaced two real errors:

  * `ethiopia-social-contributions` -- `12,000 x 30% - 1,350 = 3,600 - 1,350 =
    2,550` is 2,250. The file's own band table and its sibling
    `ethiopia-payroll` both give 2,250; the wrong figure had propagated into
    net pay, the classification line, a fabricated bank-statement line and the
    test suite.
  * `serbia-payroll` -- `5,439,096 x 10% = 487,450.80` is 543,909.60, and the
    line beneath it subtracted to a negative and then used the positive. Both
    sat inside a worked example that banded the annual supplementary tax on
    gross income, which three guides in the pack modelled three different ways.

Prefer bolding the answer, not the whole expression; either way the parser now
sees through it.

Do not build a separate "base rate + levy = combined" checker on top of this;
it was tried and it is strictly worse. Contribution breakdowns are n-term sums
-- `10.67% + 1% + 1% = 12.67%` in Guatemala, `14% + 5.15% + 0.75% = 19.90%` in
Serbia -- and a two-term pattern truncates the third term and reports a
correct line as broken: 29 of its 142 hits were that, and every one was right.
The `expr = expr` span above already evaluates them with any number of terms.
The same trap caught a nominal-vs-effective checker, which assumed the
tax-inclusive identity `eff = nom / (1 - nom)`; the corpus mostly states
additive levies instead (Australia's 45% + 2% Medicare = 47%, Zimbabwe's 25%
x 1.03 AIDS levy = 25.75%), so 35 of its 38 pairs were correct and flagged. Every remaining flag in `skills/` has since been read in
context and each one holds: the FEIE example's $56,503 is the correct 2025 tax on $248,250, Iceland's
three terms sum exactly, Virginia's line states its own multiplicand
("on $186,750"), China's arithmetic is in 万, Brazil's and Portugal's decimals
are European, and Croatia's line self-verifies. That is the standard to meet
before calling one an artefact.

Usage:
    python3 scripts/check-arithmetic.py            # defaults to skills/
    python3 scripts/check-arithmetic.py skills
    python3 scripts/check-arithmetic.py skills packages agent-skills

Exit status is always 0: this is a review aid, not a gate.
"""
import os,re,sys,warnings
warnings.filterwarnings('ignore')
CUR='€£$¥₹'
CURWORD=re.compile(r'(?:EUR|GBP|USD|AUD|CAD|NZD|SGD|CHF|SEK|NOK|DKK|PLN|ZAR|INR|IDR|NPR|MYR|THB|PHP|VND|BRL|MXN|JPY|CNY|HKD|AED|SAR|ILS|TRY|RUB|UAH|KES|NGN|GHS|TZS|LKR|PKR|BDT|EGP|MAD|RON|CZK|HUF|ISK|GEL|Rp|Rs|RM)\.?')
SPAN=re.compile(r'[0-9(][0-9,\.\s%×x\*\+\-−/÷\(\)=' + CUR + r']*=[\s' + CUR + r']*[0-9,\.\s%×x\*\+\-−/÷\(\)=' + CUR + r']*[0-9%\)]')
OPSP=re.compile(r'\s[\*×x\+/÷]\s|\s[-−]\s')      # whitespace-delimited operator

def norm(tok, euro=False):
    s=tok
    # 1.234,56 -> European, unambiguous
    if re.fullmatch(r'\d{1,3}(\.\d{3})+,\d+',s): return s.replace('.','').replace(',','.')
    # 1.234.567 -> two or more dot groups can only be thousands
    if re.fullmatch(r'\d{1,3}(\.\d{3}){2,}',s):   return s.replace('.','')
    # a SINGLE dot group (57.143) is ambiguous: decimal in en-US text, thousands in
    # European text. Only read it as thousands when the line proves European style.
    if re.fullmatch(r'\d{1,3}\.\d{3}',s):
        return s.replace('.','') if euro else s
    if re.fullmatch(r'\d{1,3}(,\d{3})+\.\d+',s): return s.replace(',','')
    if re.fullmatch(r'\d{1,3}(,\d{3})+',s):    return s.replace(',','')
    # `5,20` is a decimal in European text and thousands nowhere sane
    if re.fullmatch(r'\d+,\d{1,2}',s):        return s.replace(',','.') if euro else s.replace(',','')
    return s.replace(',','')

# Known blind spot, left deliberately. A running computation written across
# punctuation and prose — "$368,000 - $199,200 = $168,800; minus $15,750 SD =
# $154,200" — is not evaluated: the span extractor stops at the semicolon and
# the "SD" label, and the second step is never checked. Relaxing the extractor
# to reach across them was tried and cost 13 new false positives in skills/
# without catching the case, so it stays out. That class is covered instead by
# comparing the two federal trees against each other, which is how the example
# above was actually found.

EURO=[False]
def to_py(side):
    s=side
    for c in CUR: s=s.replace(c,' ')
    # unspaced en/em dash between digits = range, not minus -> kill the span
    if re.search(r'\d\s*[–—]\s*\d', s) and not re.search(r'\d\s[–—]\s\d', s): return None
    if re.search(r'[–—]', s): return None
    s=re.sub(r'\s([-−])\s',' - ',s)
    s=re.sub(r'\s([×x\*])\s',' * ',s)
    s=re.sub(r'\s([/÷])\s',' / ',s)
    s=s.replace('×',' * ').replace('÷',' / ')
    s=re.sub(r'\d[\d,\.]*\d|\d', lambda m: norm(m.group(0), euro=EURO[0]), s)
    s=re.sub(r'([\d\.]+)\s*%', r'(\1/100)', s)
    s=re.sub(r'\)\s*\(', ') * (', s)
    s=re.sub(r'(\d)\s*\(', r'\1 * (', s)
    s=re.sub(r'\)\s*(\d)', r') * \1', s)
    if not re.fullmatch(r'[\d\.\s\*\+\-/\(\)]+', s or ''): return None
    if s.count('(')!=s.count(')'): return None
    return s

def ev(side):
    p=to_py(side)
    if not p or not p.strip(): return None
    try:
        v=eval(p,{'__builtins__':{}},{})
        return float(v)
    except Exception: return None

def close(a,b):
    m=max(abs(a),abs(b))
    if m>1e14: return True
    return abs(a-b)<=max(0.51,m*0.011)

bad=[];checked=0
# Run bare, this used to walk nothing and print "expressions evaluated: 0,
# mismatches: 0", which reads exactly like a clean pass. The file above warns
# that a filter silently discarding input reports a run it has not earned, and
# an empty argv was doing that to the whole script. Defaults to skills/ now,
# as every other check-*.py here does.
for root in (sys.argv[1:] or ['skills']):
    for dp,dn,fn in os.walk(root):
        if '.git' in dp: continue
        for f in sorted(fn):
            if not f.endswith('.md'): continue
            p=os.path.join(dp,f)
            for i,line in enumerate(open(p,encoding='utf-8',errors='replace'),1):
                if '=' not in line: continue
                if re.search(r'\b(min|max|round|floor|ceil|if|where|up to|per|of the)\b',line,re.I): continue
                EURO[0]=bool(re.search(r'\d\.\d{3},\d|\d+,\d{1,2}\b(?!\d)', line)) and not re.search(r'\d,\d{3}(?!\d)', line)
                for cell in line.split('|'):
                    cell=CURWORD.sub(' ',cell)
                    # `**` around a bolded answer is markdown, not exponentiation;
                    # left in place it makes eval raise and the span is dropped in
                    # silence. A real operator is whitespace-delimited (OPSP), so
                    # an asterisk touching a digit is emphasis too.
                    cell=cell.replace('**','')
                    cell=re.sub(r'\*(?=[\d(])|(?<=[\d%)])\*', ' ', cell)
                    for m in SPAN.finditer(cell):
                        span=m.group(0)
                        sides=[s for s in span.split('=') if s.strip()]
                        if len(sides)<2: continue
                        # first side must be a real computation: >=2 numeric literals AND an operator
                        lits=re.findall(r'\d[\d,\.]*', sides[0])
                        if len(lits)<2 or not OPSP.search(sides[0]): continue
                        # every later side must be a single literal or a computation
                        if any(not s.strip() for s in sides[1:]): continue
                        pct_rhs = '%' not in sides[0] and re.fullmatch(r'[\s]*[\d\.,]+\s?%[\s]*', sides[-1])
                        if pct_rhs:
                            sides=[s.replace('%','') for s in sides]
                        vals=[ev(s) for s in sides]
                        if pct_rhs and vals and all(v is not None for v in vals):
                            # `A / B = R%`: the left is a ratio, the right a percentage.
                            # `a + b + c = R%`: both are already percentages.
                            if '/' in sides[0] and abs(vals[0]) <= 1.0001:
                                vals=[vals[0]*100]+list(vals[1:])
                        if any(v is None for v in vals): continue
                        if all(v==0 for v in vals): continue
                        # The asserted claim is the final `= answer`. Earlier segments of a
                        # chain ("(A - B) = C x r = D") are narrative restatement, not a
                        # claim that A-B equals C*r.
                        if len(re.findall(r'\d[\d,\.]*', sides[-1]))!=1: continue
                        checked+=1
                        if not close(vals[-2],vals[-1]):
                            bad.append((p,i,span.strip(),vals))
print(f'expressions evaluated: {checked}')
print(f'mismatches: {len(bad)}\n')
for p,i,span,vals in bad:
    print(f'{p}:{i}\n    {span}\n    -> {[round(v,2) for v in vals]}')
