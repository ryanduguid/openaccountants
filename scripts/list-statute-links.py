"""Find links whose clickable text names a statute but whose destination is not one.

`[Code Général des Impôts (Bénin) — IRPP barème](https://www.rivermate.com/...)`
renders as a link labelled with the Beninese tax code and lands the reader on an
HR platform's country page. The figure beside it may be perfectly correct; the
citation is still telling the reader something untrue about where it came from,
and it survives every check that compares numbers.

This is the Portugal harm made measurable: a citation that reads as authority
and is not. Portugal's was a wrong instrument number; this is the right
instrument name pointing at the wrong kind of document.

WHAT IS AND IS NOT REPORTED

The corpus's convention is `[Instrument name](where I read about it)`, and that
convention is not itself a defect — naming the governing Act and citing a
summary of it is honest, and 944 links do it. So a destination that is a
recognised tax publisher (PwC, KPMG, Chambers, Lexology and the like) is not
reported: a reader who clicks lands on tax analysis and can see what it is.

Reported is the sharp end: the destination is neither a tax authority nor a
recognised tax publisher. Relocation consultancies, HR platforms, corporate
services firms, a bank's trade portal. A reader clicking those has no signal
that they have left the law behind.

It ranks, it does not accuse. The fix is usually to move the instrument name out
of the anchor text, not to find a new source. Always exits 0.

Usage: python3 scripts/list-statute-links.py [--selftest] [--jurisdiction NAME]
"""
import os, re, sys, collections, importlib.util

_spec = importlib.util.spec_from_file_location(
    'source_mix', os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'list-source-mix.py'))
_mix = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mix)

LINK = re.compile(r'\[([^\]]{4,160})\]\((https?://[^)\s]+)\)')
# An instrument, in the languages and legal systems this corpus cites in.
# Ethiopia and Eritrea legislate by Proclamation and nothing else, so leaving
# the word out hid 21 links -- every statutory citation those two guides make.
# Measured and left out: Order (25 anchors, 0 hits), Rules, Bill, Statute,
# Constitution, Notification, Circular. Each is either ambiguous in English or
# absent from the corpus; add one when a guide actually cites it.
STATUTE = re.compile(r'\b(?:Act|Code|Law|Ordinance|Decree|Uniform Act|Loi|'
                     r'C[oó]digo|Codice|Gesetz|Ley|Lei|Legge|Decreto|'
                     r'Proclamation|Regulations?|Reglamento|Resolution|'
                     r'Statutory Instrument|S\.I\. No)\b')
HOST = re.compile(r'https?://([^/\s)\]>"]+)')

# Publishers whose pages a reader can recognise as commentary. Landing on one of
# these from a statute-named link is a convention, not a trap.
PUBLISHER = re.compile(r'pwc|kpmg|deloitte|ey\.com|bakermckenzie|chambers|'
                       r'grantthornton|pkf|bdo|crowe|mazars|lexology|ibfd|'
                       r'orbitax|taxsummaries|practiceguides', re.I)

SKIP_TREES = ('us-states', 'foundation', 'templates', 'patterns')


def misleading(line):
    """[(anchor, host)] for links that name a statute and land somewhere else."""
    out = []
    for m in LINK.finditer(line):
        anchor, url = m.group(1), m.group(2)
        if not STATUTE.search(anchor):
            continue  # not `return`: a later link on the same line still counts
        host = HOST.match(url).group(1)
        if _mix.classify(host) != 'secondary' or PUBLISHER.search(host):
            continue
        out.append((anchor, host))
    return out


def selftest():
    # the trap: the tax code is the link text, an HR platform is the destination
    got = misleading('- **Rate** - 30% _([Code Général des Impôts (Bénin) — '
                     'IRPP barème](https://www.rivermate.com/guides/benin))_')
    assert got and got[0][1] == 'www.rivermate.com', got

    # the convention, not reported: a recognised publisher is visibly commentary
    assert not misleading('_([Income Tax Act](https://taxsummaries.pwc.com/x))_')
    assert not misleading('_([Income Tax Act](https://practiceguides.chambers.com/x))_')

    # an authority destination is the thing done right
    assert not misleading('_([Value Added Tax Act 1991](https://frcs.org.fj/vat))_')
    assert not misleading('_([Tax Code](https://lex.uz/en/docs/4674902))_')

    # a link that names no instrument is out of scope however odd its target
    assert not misleading('See the [country guide](https://www.rivermate.com/benin)')

    # a trap behind an ordinary link on the same line. 39 lines in the corpus
    # put a plain link first; scanning must not stop at the first non-statute.
    got = misleading('See the [country guide](https://www.rivermate.com/benin) and '
                     '[Code Général des Impôts](https://www.rivermate.com/guides/benin)')
    assert got and got[0][1] == 'www.rivermate.com', got
    print('selftest: 7 cases pass')


def main(only=None):
    hits = collections.defaultdict(list)
    for dp, _, fns in os.walk('skills'):
        parts = dp.split(os.sep)
        if len(parts) < 3 or parts[1] in SKIP_TREES:
            continue
        if only and parts[2] != only:
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(dp, fn)
            with open(path, encoding='utf-8', errors='replace') as fh:
                for n, line in enumerate(fh, 1):
                    for anchor, host in misleading(line):
                        hits[parts[2]].append((path, n, anchor, host))
    for jur, rows in sorted(hits.items(), key=lambda kv: -len(kv[1])):
        print('%-26s %d' % (jur, len(rows)))
        if only:
            for path, n, anchor, host in rows:
                print('    %s:%d\n      [%s]\n      -> %s' % (path, n, anchor, host))
    print()
    print('links naming a statute but landing on neither an authority nor a '
          'recognised tax publisher:', sum(len(v) for v in hits.values()),
          'across', len(hits), 'jurisdictions')
    print('The fix is usually to move the instrument name out of the anchor '
          'text, not to find a new source.')
    return 0  # never gates CI: a citation convention is not a defect


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        j = None
        if '--jurisdiction' in sys.argv:
            j = sys.argv[sys.argv.index('--jurisdiction') + 1]
        sys.exit(main(j))
