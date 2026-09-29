#!/usr/bin/env python3
"""Flag guides that carry a rate table but cite no tax authority or statute.

A rate table is the part of a guide a reader acts on, and it is the part that
has been wrong most often on this tree: Benin's IRPP bands (all five off, one
rate off, every one cited to an HR platform), Zambia's contribution table
(cited to a domain that now serves gambling SEO), Burundi's PIT bands (cited to
a platform, with the revenue office unreachable to check). What those had in
common was not a wrong number; it was that nothing in the guide pointed at the
body that sets the number. A summary can be right, and often is, but a guide
whose only sources are summaries has no way to be checked from inside.

So this is the sourcing floor: a guide with at least one rate table must cite
at least one tax authority, statutory body, official gazette or legislation
service (``oa_tools.sources.classify`` scores the host, on the government
suffixes and the maintained allowlist of authorities on bare national domains)
or a republisher of the primary text (Cornell's LII for the US Code). The
guide as a whole is the unit: the corpus cites in a sources section as often
as beside a row, so a per-row test would report guides that are doing it
right. One link anywhere in the guide clears every table in it.

What counts as a rate table: a markdown table with a column that holds a
percentage in at least three rows and in most of its rows (or in five rows
however long the table), and a run of bullets whose value is a rate on at
least three lines and on most of them (or on five). A bullet's value is a rate
when the percentage opens the line ("10% on the first 1,000"), closes it
("**Standard rate** -- 20%") or follows a label separator within forty
characters ("Dividends: 0% if the beneficial owner ..."); a percentage inside
the label or the prose ("**>50% from one platform:** diversify", "1.5% x
300,000 = 4,500") is not one. Bracket schedules, VAT-rate tables, contribution
tables, withholding matrices and the bullet-form schedules the six-file
country packs are written in ("Income TOP 12,001-30,000 -- 10%") qualify; a
quick-reference table or fact list with a rate on three of twenty rows does
not.

What this does not prove. A guide citing its revenue service's home page
beside a rate taken from a summary passes, and a guide whose one authority
link is dead passes (``check-cited-hosts.py`` is the resolver). The floor is
"could a reader get from this guide to the body that sets the rate", not
"did the author".

Usage: python3 scripts/check-sourcing-floor.py [dir ...]   (default: skills)

Gate: one finding per unsourced rate table or list, keyed on its first two
rows (the header and the first data row of a table, the first two bullets of
a list), so a table added to a guide already in the queue is a new finding
and a table that gains an authority link, or is removed, leaves a stale
entry. Exits 1 on a finding not listed in scripts/baselines/sourcing-floor.txt
and on an entry that no longer reproduces. --json, --baseline PATH,
--no-baseline and --update-baseline are described in
scripts/oa_tools/findings.py. ``skills/templates/`` and ``skills/integrations/``
(file templates and platform guides, not tax guides) are skipped.
"""
import os, re, sys, glob

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from oa_tools import findings, sources  # noqa: E402

PCT = re.compile(r'\d{1,2}(?:[.,]\d+)?\s*%')
BULLET = re.compile(r'^\s*[-*]\s+\S')
BULLET_MARK = re.compile(r'^\s*[-*]\s+')
#: A label separator: the percentage that follows one within forty characters
#: is the bullet's value ("**Standard rate** -- 20%", "Dividends: 0% if ...").
SEPARATOR = re.compile(r'(?:—|–|--|:|\|)')
#: A trailing citation, stripped before the line's end is examined.
CITATION = re.compile(r'(?:_\(.*\)_|\([^()]*\)|\[[^\]]*\]\([^)]*\))\s*$')
PCT_OPENS = re.compile(r'^\**\s*\d{1,2}(?:[.,]\d+)?\s*%')
PCT_CLOSES = re.compile(r'\d{1,2}(?:[.,]\d+)?\s*%\**\s*$')
KIND = {'table': 'rate table', 'list': 'rate list'}
SKIP = ('templates', '_templates', 'integrations')


def cells(row):
    return [c.strip() for c in row.strip().strip('|').split('|')]


def enough(hits, rows):
    """A schedule: a rate on >= 3 rows and on most rows, or on 5 rows however long."""
    return hits >= 3 and (hits >= 0.6 * rows or hits >= 5)


def rate_line(line):
    """Whether a bullet's value is a rate (see the module docstring)."""
    content = BULLET_MARK.sub('', line).strip()
    while True:
        stripped = CITATION.sub('', content).strip()
        if stripped == content:
            break
        content = stripped
    if PCT_OPENS.match(content) or PCT_CLOSES.search(content):
        return True
    return any(PCT.search(content[m.end():m.end() + 40]) for m in SEPARATOR.finditer(content))


def rate_tables(lines):
    """``('table', header row, first data row)`` for each table with a column
    carrying a percentage on enough rows."""
    found, i = [], 0
    while i < len(lines):
        if not lines[i].strip().startswith('|'):
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].strip().startswith('|'):
            j += 1
        block, i = lines[i:j], j
        if len(block) < 5:                      # header + rule + >= 3 data rows
            continue
        data = [cells(r) for r in block[2:]]
        width = max(len(r) for r in data)
        for c in range(width):
            if enough(sum(1 for r in data if len(r) > c and PCT.search(r[c])), len(data)):
                found.append(('table', block[0].strip(), block[2].strip()))
                break
    return found


def rate_lists(lines):
    """``('list', first bullet, second bullet)`` for each bullet run whose
    value is a rate on enough lines."""
    found, i = [], 0
    while i < len(lines):
        if not BULLET.match(lines[i]):
            i += 1
            continue
        j = i
        while j < len(lines) and BULLET.match(lines[j]):
            j += 1
        run, i = lines[i:j], j
        if enough(sum(1 for line in run if rate_line(line)), len(run)):
            found.append(('list', run[0].strip(), run[1].strip()))
    return found


def label(kind, first, second):
    """The finding key: the kind plus the schedule's first two rows."""
    return '%s without a tax-authority or statute citation: %s / %s' % (KIND[kind], first, second)


def skipped(path):
    parts = path.replace(os.sep, '/').split('/')
    return any(part in SKIP for part in parts)


def scan(path):
    """(schedules, cited hosts, authority hosts) for one guide, or None when it is not one."""
    text = open(path, encoding='utf-8', errors='replace').read()
    if not text.startswith('---') or not re.search(r'^name:', text, re.M):
        return None
    lines = text.split('\n')
    schedules = rate_tables(lines) + rate_lists(lines)
    hosts = {h for h in sources.cited_hosts(text) if sources.classify(h) is not None}
    return schedules, hosts, {h for h in hosts if sources.statute_link(h)}


def main(argv=None):
    parser = findings.argument_parser('sourcing-floor', __doc__.split('\n\n')[0])
    args = parser.parse_args(argv)
    report = findings.Report('sourcing-floor', args)
    guides = tabled = unsourced = 0
    for root in args.roots:
        for path in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
            if skipped(path):
                continue
            scanned = scan(path)
            if scanned is None:
                continue
            guides += 1
            schedules, hosts, authority = scanned
            if not schedules:
                continue
            tabled += 1
            if authority:
                continue
            unsourced += 1
            cited = sorted(hosts)
            shown = ', '.join(cited[:4]) + (' ...' if len(cited) > 4 else '')
            sources_clause = 'the guide cites %d host(s), none a tax authority or statute%s' % (
                len(cited), (': ' + shown) if cited else '')
            for kind, first, second in schedules:
                summary = '%s without a tax-authority or statute citation (%s); %s' % (
                    KIND[kind], first, sources_clause)
                report.add(findings.Finding(
                    path, label(kind, first, second), summary,
                    detail={'kind': kind, 'rows': [first, second], 'hosts': cited},
                    text='%s\n    %s' % (path, summary)))
    report.note('\nguides scanned: %d; with a rate table or list: %d; '
                'without an authority or statute citation: %d (%d table(s) or list(s))'
                % (guides, tabled, unsourced, len(report.findings)))
    return report.finish()


if __name__ == '__main__':
    sys.exit(main())
