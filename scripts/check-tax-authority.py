"""Flag a guide naming a revenue authority its jurisdiction does not use.

The branch's clearest finding was that defects cluster in nouns, not numbers:
Malta's rate tables were exact to the cent while its form name, filing date and
statutory citation were all wrong. This checks one more noun -- which tax
authority a guide names -- on the theory that a guide copied from a neighbour
keeps the neighbour's agency the way a misfiled guide keeps its own currency.

Self-calibrating per folder, like `check-currency-of-account.py`: no
authority-to-country map, the folder's own usage decides what its house agency
is, and a guide using a different one with no mention of the house agency is
reported.

**Result: clean.** 8 outliers in 252 jurisdictions, and every one is a country's
legitimate second agency rather than a foreign one:

  * Germany -- `BMF` (Federal Ministry of Finance) and `BZSt` (Federal Central
    Tax Office) beside the local `Finanzamt`;
  * India -- `CBIC` in the e-invoicing guide beside `CBDT`, which is the correct
    split between indirect and direct taxes;
  * Italy -- `AdE` in the e-invoicing guide beside `INPS`;
  * Mexico -- `IMSS` in the IMSS guide beside `SAT`;
  * the treaty-corridor guides, which name the counterparty's authority by
    design.

Most countries run separate revenue and social-security agencies, so a second
agency is the normal case and this check can only find a *foreign* one.

**Two false-positive classes, both found the hard way and both excluded now.**
Acts are not agencies: with `ITA` in the list, Malta's house authority came out
as `ITA` on 51 uses of the Income Tax Act, and Nigeria's as `NTA` -- the Nigeria
Tax Act -- which then made the actual authority, `FIRS`, look like the outlier.
And a domestic term can collide with a foreign agency: Nigeria's `CRA` is the
Consolidated Relief Allowance, used 23 times in `ng-income-tax`, not the Canada
Revenue Agency. That is the same shape as Andorra's `Llei` matching `lei` in
`check-currency-of-account.py` -- an acronym is only evidence in a language and
a jurisdiction, so check what it means locally before believing it.

Usage: python3 scripts/check-tax-authority.py [skills]
"""
import argparse
import os, re, collections, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oa_tools.cli import directory
from oa_tools.guides import markdown_files, jurisdiction_group

AUTH = ['HMRC', 'IRS', 'ATO', 'SARS', 'MTCA', 'FTB', 'EDD', 'DIAN', 'AFIP', 'SUNAT',
        'SII', 'SAT', 'DGII', 'SIN', 'SRI', 'IRAS', 'LHDN', 'DGT', 'BIR', 'FBR',
        'ZIMRA', 'KRA', 'URA', 'TRA', 'ZRA', 'FIRS', 'GRA', 'RRA', 'ZATCA', 'AEAT',
        'AdE', 'DGFiP', 'URSSAF', 'INPS', 'INASTI', 'RSZ', 'SVB', 'Skatteverket',
        'Skatteetaten', 'SKAT', 'Vero', 'RSK', 'Finanzamt', 'BZSt', 'BMF', 'ФНС',
        'СФР', 'ZUS', 'NRA', 'ANAF', 'NAV', 'IRBM', 'ERCA', 'OBR', 'CNSS', 'CNAS',
        'ANSES', 'IMSS', 'CBIC', 'CBDT', 'FTS']
# Excluded deliberately, each having produced a false positive: ITA, NTA, STA and
# OTA are Acts; KSeF is a platform; CRA is Nigeria's Consolidated Relief Allowance
# as often as it is the Canada Revenue Agency. See the docstring.
PAT = re.compile(r'(?<![A-Za-z0-9])(' + '|'.join(re.escape(a) for a in
                 sorted(set(AUTH), key=len, reverse=True)) + r')(?![A-Za-z0-9])')


def main(root):
    byjur = collections.defaultdict(collections.Counter)
    files = collections.defaultdict(dict)
    for p, source_path in markdown_files(root):
        jur = jurisdiction_group(p, root)
        if jur is None:
            continue
        c = collections.Counter(
            PAT.findall(open(source_path, encoding='utf-8', errors='replace').read()))
        if c:
            files[jur][p] = c
            byjur[jur].update(c)

    flags = 0
    for jur in sorted(byjur):
        modal, mn = byjur[jur].most_common(1)[0]
        if mn < 10 or len(files[jur]) < 3:      # too little evidence for a house agency
            continue
        for p, c in sorted(files[jur].items()):
            top, tn = c.most_common(1)[0]
            if top != modal and tn >= 5 and c[modal] == 0:
                print('%-22s house=%-12s %-56s uses %s x%d' % (jur, modal, p, top, tn))
                flags += 1
    print('jurisdictions with a house authority: %d   outliers: %d' % (len(byjur), flags))
    return flags


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0], allow_abbrev=False)
    parser.add_argument('root', nargs='?', type=directory, metavar='DIR',
                        help="directory to scan (default: this checkout's skills)")
    args = parser.parse_args()
    main(args.root)
