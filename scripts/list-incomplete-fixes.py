"""Find values you removed in one place that still stand elsewhere in the file.

This is not a corpus checker. Every other script here scans `skills/` and knows
nothing about who is running it. This one reads your own diff and asks a
question only the author can be asked: you just decided a figure was wrong --
did you catch every copy of it?

WHY IT EXISTS

Pakistan's income tax guide had the wrong top-of-table salaried rate. Fixing the
table left nine other places saying the old thing, three of them operative,
including the section heading directly above the corrected table. That was
caught by hand, late, in a second pass. The pattern then repeated: `pk-cgt`
carried the pre-FA-2024 non-filer wording in four satellites after its table was
rewritten, and three Bulgaria guides described the 2026 Budget Act as an
unadopted draft in fourteen places while their own prohibitions section already
recorded it as gazetted.

A guide is not a database row. The same figure appears in the frontmatter
description, a quick-reference table, a narrative section, a worked example, a
prohibition and a provenance note. Editing the table is the easy half. The half
that hurts is that an agent loading the guide reads the satellite, not the row
you fixed -- and a satellite that disagrees with a corrected table is worse than
the original error, because now the file contradicts itself and the reader has
no way to tell which side is current.

WHAT IT DOES

For each file changed in the diff, it collects the numeric values (percentages,
money amounts, bare numbers with separators) that appear on removed lines and
NOT on any added line -- values the edit decided against. Then it looks for
those values in the parts of the file you did not touch. Each surviving line is
printed with its number so you can read it before deciding.

WHAT IT IS NOT

It ranks, it does not accuse, and it always exits 0. Most of what it returns is
correct and must stay:

  - **Dated worked examples.** Bolivia's Form 610 example is computed at the
    2025 minimum wage of Bs 2,750 and says so, with a July 2025 due date. The
    fix that removed Bs 16,500 from a blank worksheet template was right to
    leave the example alone. Re-rating a correct 2025 example at 2026 figures
    makes it wrong.
  - **The other side of a supersession.** The UK guide's GBP 9,013.80 survived
    because the removal was from a speculative 2026-27 projection that had
    copied the 2025-26 result; the figure belongs in the 2025-26 computation
    it was computed for.
  - **A figure that is right in one cohort and wrong in another.** Pakistan
    charges 45% at the top of the non-salaried slab and 35% at the top of the
    salaried one. Removing 45% from a securities row says nothing about the
    property row below it.

So read the surviving lines. Do not batch-edit them.

THE BUG THIS SHIPPED WITH, AND WHAT IT COST

The first version matched values as plain substrings. Fiji's withholding guide
was flagged because a removed "0%" matched inside "10%" two lines down. That is
a false positive that costs a real minute of reading to dismiss, and at corpus
scale it would have buried the true positives. Values are now matched on word
boundaries, with the percent sign part of the token. Recorded rather than
quietly fixed, because the same mistake is available to anyone extending the
pattern list below.

Usage: python3 scripts/list-incomplete-fixes.py [--base origin/main] [--selftest]
"""
import re, subprocess, sys, collections

# A value worth tracking: a percentage, or a number with a decimal point or a
# thousands separator. Bare small integers are excluded deliberately -- "3" and
# "12" appear in every guide as section numbers, month counts and list items,
# and tracking them produced nothing but noise.
VALUE = re.compile(r'\d[\d,]*\.?\d*\s?%|\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+\.\d+')

DEFAULT_BASE = 'origin/main'


def normalise(value):
    """'15 %' and '15%' are the same value; '1,077' and '1077' are not.

    Whitespace before a percent sign varies across the corpus and carries no
    meaning. Thousands separators are left alone: a guide that writes 1077 and
    a guide that writes 1,077 are quoting different source conventions, and
    collapsing them would match across unrelated figures.
    """
    return value.replace(' ', '')


def token_pattern(value):
    """A regex matching `value` as a whole token, not as a substring.

    This is the Fiji fix. '0%' must not match inside '10%', and '15' must not
    match inside '150' or '2015'. The percent sign is a non-word character, so
    \\b after it would sit in the wrong place -- the guard has to be an explicit
    "not a digit, comma or dot" on both sides.
    """
    return re.compile(r'(?<![\d.,])' + re.escape(value.rstrip('%')) +
                      (r'\s?%' if value.endswith('%') else r'(?![\d.,])'))


def parse_diff(text):
    """Return {path: (removed_values, added_values, touched_line_numbers)}.

    `touched_line_numbers` are line numbers in the NEW file that the diff
    added, so a surviving occurrence inside a hunk you just wrote is not
    reported back to you as something you missed.
    """
    files = collections.defaultdict(
        lambda: {'removed': collections.Counter(), 'added': collections.Counter(),
                 'touched': set()})
    path, new_line = None, 0
    for line in text.splitlines():
        if line.startswith('+++ b/'):
            path, new_line = line[6:], 0
            files[path]  # materialise even if the hunk turns out empty
        elif line.startswith('@@'):
            m = re.search(r'\+(\d+)', line)
            new_line = int(m.group(1)) if m else 0
        elif path is None:
            continue
        elif line.startswith('-') and not line.startswith('---'):
            for v in VALUE.findall(line):
                files[path]['removed'][normalise(v)] += 1
        elif line.startswith('+') and not line.startswith('+++'):
            for v in VALUE.findall(line):
                files[path]['added'][normalise(v)] += 1
            files[path]['touched'].add(new_line)
            new_line += 1
        elif line.startswith(' '):
            new_line += 1
    return files


def survivors(path, values, touched):
    """Lines in the current file, outside the diff's own additions, still
    carrying one of `values`."""
    try:
        with open(path, encoding='utf-8', errors='replace') as fh:
            lines = fh.read().splitlines()
    except OSError:
        return []                       # file deleted or renamed away
    patterns = [(v, token_pattern(v)) for v in values]
    out = []
    for n, line in enumerate(lines, 1):
        if n in touched:
            continue
        hit = [v for v, pat in patterns if pat.search(line)]
        if hit:
            out.append((n, sorted(set(hit)), line.strip()))
    return out


def selftest():
    diff = (
        '+++ b/a.md\n'
        '@@ -1,3 +1,3 @@\n'
        ' unchanged\n'
        '-| rate | 45% |\n'
        '+| rate | 35% |\n'
    )
    parsed = parse_diff(diff)
    assert parsed['a.md']['removed']['45%'] == 1, parsed
    assert parsed['a.md']['added']['35%'] == 1, parsed
    # the new file is "unchanged" then "| rate | 35% |", so the added line is
    # line 2. The removed line does not advance the new-file counter.
    assert parsed['a.md']['touched'] == {2}, parsed['a.md']['touched']

    # the Fiji bug: a removed 0% must not match inside 10%
    assert not token_pattern('0%').search('- withholding on interest 10%')
    assert token_pattern('0%').search('- withholding on royalties 0%')
    assert token_pattern('0%').search('- withholding 0 % with a space')
    # and a removed 15 must not match inside 150 or 2015
    assert not token_pattern('15').search('threshold of 150 units')
    assert not token_pattern('15').search('the Finance Act 2015')
    assert token_pattern('15').search('band of 15 years')

    # a value removed in one place and re-added in another is not a survivor
    both = parse_diff('+++ b/b.md\n@@ -1,2 +1,2 @@\n-old 12.5\n+new 12.5\n')
    left = set(both['b.md']['removed']) - set(both['b.md']['added'])
    assert not left, left

    # bare small integers are not tracked at all
    assert not VALUE.findall('see section 3 and item 12')
    assert VALUE.findall('BGN 1,077 and 12.5% and 0.4')

    # KNOWN MISS: a value restated in different units survives silently.
    # Removing "BGN 4,130" while the file still says "EUR 2,111.64" is the same
    # figure at the fixed conversion rate, and nothing here can see that. The
    # Bulgaria guides needed that caught and it was caught by hand.
    units = parse_diff('+++ b/c.md\n@@ -1,1 +1,1 @@\n-cap BGN 4,130\n+cap EUR 2,300\n')
    assert '2,111.64' not in units['c.md']['removed']
    print('selftest: diff parsing, token boundaries and known misses pass')


def main(base=DEFAULT_BASE):
    try:
        text = subprocess.run(['git', 'diff', '%s...HEAD' % base],
                              capture_output=True, text=True, check=True,
                              encoding='utf-8').stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print('could not read the diff against %s: %s' % (base, exc))
        return 0
    files = parse_diff(text)
    total = 0
    for path in sorted(files):
        state = files[path]
        dropped = set(state['removed']) - set(state['added'])
        if not dropped:
            continue
        rows = survivors(path, dropped, state['touched'])
        if not rows:
            continue
        total += 1
        print('\n%s' % path)
        for n, hit, line in rows:
            print('  %5d  %-18s %s' % (n, ', '.join(hit), line[:96]))
    print()
    print('files changed in the diff:', len(files))
    print('files where a value this diff removed still stands elsewhere:', total)
    print('Read each surviving line before touching it. A dated worked example, '
          'the other side of a supersession, and a figure that is right in a '
          'different cohort all show up here and all must stay.')
    return 0  # never gates CI: a surviving value is not a defect


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        b = DEFAULT_BASE
        if '--base' in sys.argv:
            b = sys.argv[sys.argv.index('--base') + 1]
        sys.exit(main(b))
