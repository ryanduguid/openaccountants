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
totals, and units the parser drops (CNY 万). Triage before editing.

Usage:
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
for root in sys.argv[1:]:
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
