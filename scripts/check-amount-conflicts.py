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

Result on `skills/`: **3 rows, and all three are correct.** One label covering
two different things is the standing false-positive class, and each row is a
different flavour of it.

  * Morocco. The CPU regime caps commercial/industrial/artisanal turnover at
    MAD 2,000,000 and the auto-entrepreneur regime caps the same category at
    MAD 500,000. Two regimes, one label, both already flagged "verify current
    value".
  * South Korea. 기본공제 is KRW 1,500,000 per person against income tax, and
    the crypto guide's KRW 2,500,000 is the separate annual deduction for
    virtual asset income. Two taxes, one label.
  * The Canadian folder. BC registers for PST at CAD 10,000 and Saskatchewan at
    CAD 30,000. Two provinces in one folder, one label.

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

**What it structurally cannot see, established by a case it missed.** Labels
are matched exactly after normalising, so one fact written under two names is
two facts to this checker. Albania stated its VAT registration threshold as
ALL 10,000,000 in `albania-income-tax` under the label "VAT registration
threshold" and as ALL 5,000,000 in `albania-tax-optimization` under "VAT
threshold". Five million apart, in one pack, and this reported nothing, because
"vat threshold" and "vat registration threshold" normalise to different keys.
`scripts/list-registration-thresholds.py` found it at once, because it keys on
the field rather than on the words the guide happened to use. Where a field
matters, list the field; a label-matching checker is a cheaper net with a
hole in it.

The minimum label length was three words and is now two, which is what made
"vat threshold" eligible at all. It costs four extra rows corpus-wide and all
four were read and are correct.

Usage: python3 scripts/check-amount-conflicts.py [skills]
       python3 scripts/check-amount-conflicts.py --selftest
"""
import os, re, collections, sys

ROW = re.compile(r'^\s*\|\s*([^|]{6,70}?)\s*\|\s*([^|]{1,70}?)\s*\|\s*$')
BULL = re.compile(r'^\s*-\s+\*\*([^*]{6,70}?)\*\*\s*[—-]+\s*(.{1,70})')
AMT = re.compile(r'(?<![\d.,])(\d{1,3}(?:[,\.]\d{3})+(?:\.\d+)?|\d{4,})(?![\d.,%])')
YEAR = re.compile(r'^(19|20)\d\d$')


def amounts(val):
    """Money on the line, with bare years dropped.

    A four-digit run with no thousands separator is usually a year, and the
    checker was reporting Nigeria as disagreeing with itself over a
    registration threshold of "2019" against "2020" (those are Finance Act
    years) and the UK over a dividend allowance of "2007" against "2025".
    A genuine amount of exactly 2,025 units would be missed; a citation year
    beside a threshold is far commoner.
    """
    return [a for a in AMT.findall(val) if not YEAR.match(a)]
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
                if len(l.split()) < 2:
                    continue
                amts = amounts(val)
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


def selftest():
    """The cases that shaped the filters, including the one still missed."""
    assert amounts('EGP 500,000 annual turnover') == ['500,000']
    # a citation year beside a threshold is not the threshold
    assert amounts('N25,000,000 under FA 2019') == ['25,000,000']
    assert amounts('rates unchanged since 2007') == []
    # two words is now enough of a label
    assert len(norm('| VAT threshold |'.strip('| ')).split()) == 2
    assert canon('7200.00') == canon('7,200')
    print('selftest: 5 cases pass')


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        main(sys.argv[1] if len(sys.argv) > 1 else 'skills')
