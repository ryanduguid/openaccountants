"""Find a labelled money amount two guides in one jurisdiction state differently.

`check-fact-conflicts.py` does this for percentages. Amounts are the other half
and are just as consequential: a registration threshold, a contribution ceiling
or a personal allowance stated one way in one guide and another way in its
sibling gives a different answer depending on which file an agent loads.

Only cross-guide disagreement is reported. Inside a single guide one label
routinely carries several amounts by design -- a band table has one row per
band, a comparison table one column per year, a payroll guide one ceiling per
filing status -- and reporting those buried the signal: 46 rows same-file
against 1 cross-file.

Result on `skills/`: **1 row, and it is correct.** Morocco's CPU regime caps
commercial/industrial/artisanal turnover at MAD 2,000,000 while the
auto-entrepreneur regime caps the same category at MAD 500,000. Two regimes,
one label, both right, and both already carrying a "verify current value" flag.
Two different regimes sharing a label is the standing false-positive class.

**The checker's own blind spot, recorded because it produced the only other
hit and the hit was wrong.** The row pattern matched `| label | value |`
without anchoring to the end of the line, so a three-column comparison table --
`| Concessional cap | $30,000 | $32,500 |` -- was read as two columns and the
later year silently dropped. That made `au-rates-2026-27` look as though it
capped non-concessional contributions at $120,000 while `au-super-guarantee`
said $130,000. Both guides in fact carry both figures and agree. The pattern is
now anchored with `\\s*$`.

That is the third checker in this branch whose own conservatism was blindness
rather than caution -- `check-arithmetic.py` dropped every bolded answer,
`check-currency-of-account.py` matched `lei` inside Catalan `Llei`. A filter
that silently discards input reports a clean run it has not earned, so prefer
one that is noisy and read the noise.

Usage: python3 scripts/check-amount-conflicts.py [skills]
"""
import os, re, collections, sys

ROW = re.compile(r'^\s*\|\s*([^|]{6,70}?)\s*\|\s*([^|]{1,70}?)\s*\|\s*$')
BULL = re.compile(r'^\s*-\s+\*\*([^*]{6,70}?)\*\*\s*[—-]+\s*(.{1,70})')
AMT = re.compile(r'(?<![\d.,])(\d{1,3}(?:[,\.]\d{3})+(?:\.\d+)?|\d{4,})(?![\d.,%])')
KEY = re.compile(r'\b(threshold|cap|ceiling|allowance|limit|exemption|'
                 r'minimum wage|deduction|band|bracket|base|floor)\b', re.I)


def norm(lab):
    lab = re.sub(r'\*+|`', '', lab).strip().lower()
    lab = re.sub(r'\s*\(.*?\)\s*', ' ', lab)
    lab = re.sub(r'[^a-z0-9 ]+', ' ', lab)
    return re.sub(r'\s+', ' ', lab).strip()


def canon(a):
    """Compare 7200 and 7200.00 as one value, not two."""
    a = a.replace(',', '')
    return ('%g' % float(a)) if a.count('.') == 1 else a.replace('.', '')


def main(root):
    facts = collections.defaultdict(lambda: collections.defaultdict(set))
    for dp, _, fns in os.walk(root):
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            parts = p.split(os.sep)
            if len(parts) < 3:
                continue
            for line in open(p, encoding='utf-8', errors='replace'):
                m = ROW.match(line) or BULL.match(line)
                if not m:
                    continue
                lab, val = m.group(1), m.group(2)
                if not KEY.search(lab):
                    continue
                l = norm(lab)
                if len(l.split()) < 3:
                    continue
                amts = AMT.findall(val)
                if len(amts) != 1:          # one amount, no ambiguity
                    continue
                facts[parts[2]][l].add((canon(amts[0]), p))

    hits = 0
    for jur in sorted(facts):
        for lab, obs in sorted(facts[jur].items()):
            srcs = {f for _, f in obs}
            if len({v for v, _ in obs}) < 2 or len(srcs) < 2:
                continue
            # each guide must be internally single-valued, else it is a band or
            # year table and the disagreement is with itself, not its sibling
            if not all(len({v for v, f in obs if f == x}) == 1 for x in srcs):
                continue
            print('%-18s %-40s ' % (jur, lab[:40]) + ' | '.join(
                '%s (%s)' % (v, os.path.basename(f)) for v, f in sorted(obs)))
            hits += 1
    print('labelled amounts two guides in one jurisdiction state differently:', hits)
    return hits


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'skills')
