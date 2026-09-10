"""Find guides whose numbers all come from one place, and that place is not an authority.

Three jurisdictions failed the same way on this branch, and it was the same
shape each time: an entire table of rates and thresholds resting on a single
non-authority page.

  Benin    every IRPP band boundary cited to one HR platform. All five were
           wrong -- 60,000/150,000/250,000/500,000 against 50,000/130,000/
           280,000/530,000 in art. 142 of the code -- and band 4 was given as
           19% where the code says 20%.
  Zambia   the whole NAPSA and NHIMA contribution table, both rates, both
           splits and the ceiling, cited to one page on zambiaprice.com. That
           domain now serves gambling SEO, so the source cannot even be read.
  Burundi  every PIT band and the tax-free threshold cited to one HR platform,
           and obr.bi answers with a fatal error, so nothing can be checked.

Benin is the one that makes the case. Its figures were not marked uncertain and
they were not hedged. They were simply wrong, and the single shared source is
what a reader could have noticed without knowing any Beninese tax law.

WHAT IT MEASURES

Per guide: of the bullets that state a NUMBER and carry a citation URL, what
share point at one host. A guide where one host carries most of the numbers has
no second opinion anywhere in it -- if that source is wrong, stale, or gone, the
guide is wrong in every row at once and nothing internal contradicts it.

THE SPLIT THAT MATTERS

Concentration on a tax authority is not a finding: a guide citing the revenue
service for all twelve of its figures is a guide doing it right. Concentration
on a recognised tax publisher is weaker but honest -- a reader lands on tax
analysis and can see what it is, and much of this corpus is built that way for
jurisdictions whose authorities cannot be reached at all.

Reported first is the sharp end, the Benin case: one host carries the numbers
and it is neither an authority nor a recognised publisher.

WHAT IT IS NOT

It is not a defect detector and must never gate CI. A single-sourced guide is
not a wrong guide; it is a guide with no internal corroboration, which is a
statement about what a mistake would cost, not evidence that one was made. Most
of what it returns is correct. Always exits 0.

It also cannot see a guide that cites four different pages on the same HR
platform under four different hostnames, and it says nothing about whether the
number is right -- only about how many independent places it came from.

Usage: python3 scripts/list-single-source-blocks.py [--selftest]
                    [--min-facts N] [--share F] [--jurisdiction NAME] [--all]
"""
import os, re, sys, collections, importlib.util

_here = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_here, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_mix = _load('source_mix', 'list-source-mix.py')
_links = _load('statute_links', 'list-statute-links.py')

URL = re.compile(r'https?://[^\s)\]>"\'`]+')
HOST = re.compile(r'https?://([^/\s)\]>"]+)')
# A bullet that commits to a number: a percentage, a money amount, or a bare
# figure of three digits or more. "the 15th of the month" is a deadline, not a
# rate, but it is still a fact somebody sourced, so it counts.
NUMERIC = re.compile(r'\d+\s*%|\d+\.\d+\s*%|\b\d{1,3}(?:[.,]\d{3})+\b|\b\d{3,}\b'
                     r'|\b\d+(?:\.\d+)?\s*(?:percent|per\s*cent)\b')
BULLET = re.compile(r'^\s*[-*|]\s*\S')

# The corpus's own site and the booking link every guide ends with.
SELF = ('openaccountants.com', 'calendly.com')

SKIP_TREES = ('templates',)


def classify_host(host):
    """'authority' | 'publisher' | 'other' for a citation destination."""
    if _mix.classify(host) == 'authority':
        return 'authority'
    if _links.PUBLISHER.search(host):
        return 'publisher'
    return 'other'


def concentration(lines):
    """(total numeric facts cited, Counter of host -> count) for one guide."""
    hosts = collections.Counter()
    total = 0
    for line in lines:
        if not BULLET.match(line) or not NUMERIC.search(line):
            continue
        found = [h for h in (HOST.match(u).group(1) for u in URL.findall(line))
                 if not any(h == s or h.endswith('.' + s) for s in SELF)]
        if not found:
            continue
        total += 1
        # One bullet is one fact however many times its source is repeated in
        # the line; otherwise a bullet citing the same page twice would count
        # as two independent corroborations of itself.
        for h in set(found):
            hosts[h] += 1
    return total, hosts


def selftest():
    benin = [
        '- **IRPP band 1** - 0% up to 60,000  _(Code - https://rivermate.com/x)_\n',
        '- **IRPP band 2** - 10% to 150,000  _(Code - https://rivermate.com/x)_\n',
        '- **IRPP band 3** - 15% to 250,000  _(Code - https://rivermate.com/x)_\n',
        '- **IRPP top** - 30% above 500,000  _(Code - https://rivermate.com/x)_\n',
    ]
    total, hosts = concentration(benin)
    assert total == 4, total
    assert hosts['rivermate.com'] == 4, hosts
    assert classify_host('rivermate.com') == 'other'

    # a guide citing its own revenue service for everything is doing it right
    assert classify_host('frcs.org.fj') == 'authority'
    assert classify_host('taxsummaries.pwc.com') == 'publisher'

    # prose is not a fact bullet, and a bullet with no citation is not counted:
    # the measure is "of the numbers that ARE sourced, how many share a source"
    total, hosts = concentration([
        'Benin levies tax under the CGI, with 5 headline taxes.\n',
        '- **A rate** - 20%  _(no citation here)_\n',
        '- **B rate** - 30%  _(https://frcs.org.fj/x)_\n',
    ])
    assert total == 1, total

    # a bullet with no number is not a rate row
    total, _ = concentration(['- **Authority** - the DGI  _(https://x.com/a)_\n'])
    assert total == 0, total

    # one bullet citing the same host twice is ONE fact from ONE source, not a
    # fact corroborated twice
    _, hosts = concentration(
        ['- **Rate** - 20%  _(https://x.com/a and https://x.com/b)_\n'])
    assert hosts['x.com'] == 1, hosts

    # two different hosts on one bullet is corroboration, and counts as such
    _, hosts = concentration(
        ['- **Rate** - 20%  _(https://x.com/a; https://y.com/b)_\n'])
    assert hosts['x.com'] == 1 and hosts['y.com'] == 1, hosts

    # the CTA block every guide ends with is not a source
    total, _ = concentration(
        ['- Use it in your AI: https://www.openaccountants.com/connect 100\n'])
    assert total == 0, total
    print('selftest: 9 cases pass')


def main(argv):
    only = None
    if '--jurisdiction' in argv:
        only = argv[argv.index('--jurisdiction') + 1]
    min_facts = int(argv[argv.index('--min-facts') + 1]) if '--min-facts' in argv else 4
    share = float(argv[argv.index('--share') + 1]) if '--share' in argv else 0.75

    rows = collections.defaultdict(list)
    scanned = 0
    for dp, _, fns in os.walk('skills'):
        parts = dp.split(os.sep)
        if len(parts) > 1 and parts[1] in SKIP_TREES:
            continue
        if only and (len(parts) < 3 or parts[2] != only):
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(dp, fn)
            with open(path, encoding='utf-8', errors='replace') as fh:
                total, hosts = concentration(fh)
            if total < min_facts or not hosts:
                continue
            scanned += 1
            host, n = hosts.most_common(1)[0]
            if n / total < share:
                continue
            rows[classify_host(host)].append((n / total, n, total, host, path))

    for kind, heading in (
            ('other', 'ONE HOST CARRIES THE NUMBERS, AND IT IS NEITHER AN '
                      'AUTHORITY NOR A RECOGNISED PUBLISHER'),
            ('publisher', 'ONE RECOGNISED PUBLISHER CARRIES THE NUMBERS'),
            ('authority', 'ONE AUTHORITY CARRIES THE NUMBERS (this is the good case)')):
        got = sorted(rows[kind], key=lambda r: (-r[1], -r[0]))
        if not got:
            continue
        if kind != 'other' and '--all' not in argv:
            print('\n== %s: %d guides (pass --all to list) ==' % (heading, len(got)))
            continue
        print('\n== %s (%d) ==' % (heading, len(got)))
        for frac, n, total, host, path in got:
            print('  %3d/%-3d %3.0f%%  %-34s %s'
                  % (n, total, frac * 100, host[:34], path))

    print('\n== SUMMARY ==')
    print('guides with %d+ sourced numeric facts: %d' % (min_facts, scanned))
    for kind in ('other', 'publisher', 'authority'):
        print('  %-10s %4d guides where one host carries >=%.0f%% of them'
              % (kind, len(rows[kind]), share * 100))
    print('\nConcentration is not a defect. It is what a mistake in that one')
    print('source would cost: every number in the guide at once, with nothing')
    print('inside the guide to contradict it.')
    return 0  # never gates CI


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        sys.exit(main(sys.argv))
