"""Find a named regime two guides in one jurisdiction cite to different provisions.

A wrong statutory citation is invisible to every other check here. The rate is
right, the arithmetic is right, the deadline is right -- and the authority under
it is a different article, so a reviewer who follows the citation reads the
wrong law and a practitioner who relies on it cites the wrong basis in a filing.

Within a folder, take lines that mention exactly one named regime or form token
(capitals with digits: TA24, VAT201, BIR60, CT1) and exactly one statutory
provision (Art./Section/§), then report a token two different guides attach to
different provisions. Requiring exactly one of each keeps the pairing honest;
a line naming three sections tells you nothing about which belongs to what.

Run over `skills/` this returns 7 rows. Five are the standing false positive:
a return form appears on many lines discussing many different provisions, so
`CT1`, `VAT201`, `AR1`, `CG1` and `BIR60` collect the section numbers of
whatever topic the line was about. A form that is a *container* for a whole
return will always do this; a form that is a *regime* will not.

Two were real, both in Malta, and both settled against the outlier guide by
the tax authority's own publications:

  * **TA24.** `mt-rental-income` gave the 15% final tax on gross rents as ITA
    Article 31E in eight places -- primary legislation, the core-rules heading,
    the related-party rule and the source table. It is **Article 31D**: MTCA
    titles its page "Rental Income Taxed at 15% - Article 31D of the Income Tax
    Act", and the TA24 form is headed "PAYMENT OF 15% TAX ON RENTAL INCOME
    Article 31D". `malta-income-tax` had it right in seven places.
  * **TA22.** `malta-ssc` and `malta-tax-optimization` gave the part-time
    regime as ITA Article 4C. It is **Article 90A** plus the Part-Time Work
    Rules (S.L. 123.39), which is what `malta-income-tax` cites, with a
    subsection (90A(2)) and a legislation.mt link -- the specificity that marks
    a citation someone actually looked up.

Where guides disagree, prefer the one that cites a subsection, names the
subsidiary rules, or links the statute. A bare article number with neither is
the one to doubt.

Usage: python3 scripts/check-statute-citations.py [skills]
"""
import os, re, collections, sys

TOKEN = re.compile(r'(?<![A-Za-z0-9])((?:[A-Z]{2,6}\d{1,3}[A-Z]?)|(?:[A-Z]{3,6}))(?![A-Za-z0-9])')
CITE = re.compile(r'(?:Art(?:icle|\.)?|Sec(?:tion|\.)?|§|s\.)\s?(\d{1,4}[A-Z]{0,2}(?:\(\d+\))?)', re.I)
STOP = {'NEVER', 'ALWAYS', 'STOP', 'NOTE', 'TRUE', 'FALSE', 'YES', 'NO', 'AND', 'THE',
        'FOR', 'NOT', 'VAT', 'GST', 'PIT', 'CIT', 'TAX', 'SSC', 'USD', 'EUR', 'GBP',
        'ITA', 'CGI', 'IRS', 'ATO', 'CFR', 'MTCA', 'PWC', 'KPMG', 'EY', 'BDO', 'RSM',
        'OECD', 'EU', 'UK', 'US', 'HMRC', 'CRA', 'SARS', 'IRD'}


def main(root):
    pairs = collections.defaultdict(lambda: collections.defaultdict(set))
    for dp, _, fns in os.walk(root):
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            parts = p.split(os.sep)
            if len(parts) < 3:
                continue
            for line in open(p, encoding='utf-8', errors='replace'):
                cs = set(CITE.findall(line))
                if len(cs) != 1:              # one provision, no ambiguity
                    continue
                toks = {t for t in TOKEN.findall(line)
                        if t not in STOP and any(c.isdigit() for c in t)}
                if len(toks) != 1:            # one named regime, no ambiguity
                    continue
                pairs[parts[2]][toks.pop()].add((cs.pop().upper(), p))

    hits = 0
    for jur in sorted(pairs):
        for tok, obs in sorted(pairs[jur].items()):
            if len({c for c, _ in obs}) > 1 and len({f for _, f in obs}) > 1:
                print('%-16s %-8s ' % (jur, tok) + ' | '.join(
                    '%s (%s)' % (c, os.path.basename(f)) for c, f in sorted(obs)))
                hits += 1
    print('named regimes two guides cite to different provisions:', hits)
    return hits


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'skills')
