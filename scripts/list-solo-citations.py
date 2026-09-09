"""Rank statutory citations by how much damage one wrong citation would do.

This exists because of Portugal. `pt-nhr-ifici` named "Portaria n.º 187/2024" as
the regulatory basis of the IFICI regime in 24 places -- the frontmatter
description, the quick-reference legislation row, a section heading, the sources
list. Portaria 187/2024 is a Ministry of Health instrument approving the updated
specialist training programme for the ophthalmology medical internship. The
IFICI is regulated by Portaria 352/2024/1 of 23 December 2024.

A wrong figure is bad. A wrong CITATION is bad in a way nothing here could see:
it survives every check that compares numbers, it reads as authority, and anyone
who follows it lands on a document about eye surgery training. No check in this
repo confirms that a cited instrument exists, or that it governs what the guide
says it governs, and none can without a legal database.

WHAT THIS IS, AND WHAT IT IS NOT

It is a blast-radius ranking. It reports instruments cited many times in exactly
one guide and nowhere else in the corpus, ordered by count. It is NOT a defect
detector, and the distinction matters enough to put in the exit status: this
always exits 0 and must never gate CI.

The reasoning is only this. A guide leaning 25 times on an instrument no sibling
guide has ever mentioned has no corroboration inside the corpus. That is not
evidence the citation is wrong. It is a statement about cost: if it IS wrong, it
is wrong 25 times, in the description that routes questions to the guide and in
the sources list a reader checks.

Most of what it returns is correct and should stay correct. Paraguay's Ley
6380/19 appears 25 times in `paraguay-income-tax` and nowhere else because it is
the Paraguayan income tax law and Paraguay has one income tax guide. The same
goes for Nicaragua's Decreto 06-2019 and Oman's Royal Decree 52/2023. A
jurisdiction with a single guide on a topic will legitimately have solo
citations, and a high count there means the guide is doing its job.

So read this as a worklist for hand-verification, ordered by what it would cost
to be wrong, and verify the top of it against the issuing gazette rather than
against another secondary source. Portugal's wrong citation sat at the top of
this list at 24 occurrences before it was corrected.

THE CHECK THAT COULD NOT BE BUILT, AND WHY

The sharper signal would be the same instrument cited with conflicting dates --
"Portaria 352/2024/1, de 30 de julho" against "de 23 de dezembro" -- which is a
contradiction visible without leaving the repo. That was measured and abandoned:
of 395 distinct instrument citations in the corpus, only 14 carry a date at all,
and none of those 14 conflict.

That absence is worth more than the check would have been. This corpus cites
instruments by number and almost never by date, so there is nothing to
cross-verify. Adding "de 23 de dezembro de 2024" to a citation costs five words
and turns an unverifiable reference into one a checker can contradict -- the
same argument as writing down the zero in a withholding table, or writing down
the date a figure will go stale. Portugal's wrong citation carried a date, "de
30 de julho", and that date travelled with the wrong number through every one
of the 24 occurrences. Had a sibling guide dated the same Portaria correctly,
the conflict would have been mechanical.

Usage: python3 scripts/list-solo-citations.py [--selftest] [--min N]
"""
import os, re, sys, collections

# An instrument word followed by a number that looks like a legislative
# reference. Deliberately narrow: matching bare four-digit years or section
# numbers turned the output into noise about "Article 12" and "s766".
CITE = re.compile(
    r'\b(Portaria|Decreto[- ]Lei|Decreto|Lei|Ley|Legge|Loi|Act|Ordinance|Regulation|'
    r'Royal Decree|Real Decreto|PMK|Perpres|Notice|Rev\.? Proc\.?|T\.?D\.?)'
    r'[^\w\n]{0,4}(?:n\.?[º°o]?\.?\s*)?'
    r'(\d{1,4}[-/]\d{2,4}(?:/\d)?|\d{4}-\d{1,3})', re.I)

DEFAULT_MIN = 8


def citations_in(text):
    """Every instrument citation in `text`, normalised, with its count."""
    found = collections.Counter()
    for m in CITE.finditer(text):
        word = m.group(1).title().replace('-', ' ')
        found['%s %s' % (word, m.group(2))] += 1
    return found


def scan(root='skills'):
    """Return {citation: {path: count}}."""
    out = collections.defaultdict(collections.Counter)
    for dp, _, fns in os.walk(root):
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(dp, fn)
            with open(path, encoding='utf-8', errors='replace') as fh:
                for cite, n in citations_in(fh.read()).items():
                    out[cite][path] += n
    return out


def selftest():
    got = citations_in(
        'O IFICI e regulado pela Portaria n.º 352/2024/1, de 23 de dezembro, '
        'alterada pela Portaria n.º 52-A/2025. Ver tambem a Lei n.º 82/2023 '
        'e o Decreto-Lei 249/2009.')
    assert got['Portaria 352/2024/1'] == 1, got
    assert got['Lei 82/2023'] == 1, got
    assert got['Decreto Lei 249/2009'] == 1, got
    # "52-A/2025" has a letter in the number and is not matched; recorded rather
    # than chased, because widening the pattern to letters pulled in ordinary
    # hyphenated words followed by a year.
    assert 'Portaria 52-A/2025' not in got

    us = citations_in('See Rev. Proc. 2025-32 and Notice 2023-74; T.D. 10033 is final.')
    assert us['Rev. Proc. 2025-32'] == 1, us
    assert us['Notice 2023-74'] == 1, us

    # a section reference is not an instrument citation
    assert not citations_in('under s766 TCA 1997 and Article 12 of the Tax Code')
    # a bare year after an instrument word is not a reference number
    assert not citations_in('the Finance Act 2025 raised the rate')
    print('selftest: citation extraction passes')


def main(minimum=DEFAULT_MIN):
    found = scan()
    rows = []
    for cite, files in found.items():
        total = sum(files.values())
        if len(files) == 1 and total >= minimum:
            rows.append((total, cite, next(iter(files))))
    rows.sort(reverse=True)
    for total, cite, path in rows:
        print('%4dx  %-24s %s' % (total, cite, path))
    print()
    print('distinct instrument citations:', len(found))
    print('cited %d+ times in exactly one guide (verify these first):' % minimum,
          len(rows))
    print('This is a blast-radius ranking, not a defect report. Most entries are '
          'correct.')
    return 0  # never gates CI: a solo citation is not a finding


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        n = DEFAULT_MIN
        if '--min' in sys.argv:
            n = int(sys.argv[sys.argv.index('--min') + 1])
        sys.exit(main(n))
