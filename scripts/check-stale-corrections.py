#!/usr/bin/env python3
"""Find a value a guide says it retired that is still asserted elsewhere in that same guide.

WHY IT EXISTS

An outside review of PR #16 returned fourteen bugs. Five of them were one shape:

  * Paraguay     -- a new block recorded that the July 2026 minimum wage was
                    decreed at PYG 3,044,000, while the prohibitions section two
                    hundred lines down still called the adjustment unconfirmed
                    and forbade applying it.
  * UK           -- the 2026-27 Scottish worked example computed at the enacted
                    starter and basic limits while Section 1.4 still said the
                    Budget was not enacted and to use the 2025-26 bands.
  * Uruguay      -- Section 5.3 corrected the low-income deduction credit to 14%
                    and wrote a note saying so; the Section 7 working paper, the
                    reviewer checklist and the never-do list still offered 10%.
  * Liechtenstein-- 2026-effective AHV/IV/FAK rates landed in a guide whose
                    metadata, overview and sibling rates were still 2025.
  * Nigeria      -- ng-formation's rate bullets were corrected to the NTA 2025
                    two-band structure, and the Plc obligations, the filings
                    list and the comparison table went on charging tertiary
                    education tax next to the 4% levy that replaced it.

None of them was found by anything in scripts/. That is not bad luck, it is an
uncovered axis. Every contradiction checker here compares ACROSS FILES:

  check-fact-conflicts        percentages, guide vs sibling guide
  check-amount-conflicts      money amounts, guide vs sibling guide
  check-research-gap-conflicts a gap in one guide, a fact in its sibling
  check-superseded-rates      a rate change in one guide, stale in its sibling
  detect-contradictions       four jurisdictions, curated concept list
  check-tree-divergence       skills/ vs packages/ vs agent-skills/

and check-amount-conflicts says in as many words why it stops at the file
boundary: "Inside a single guide one label routinely carries several amounts by
design -- a band table has one row per band, a comparison table one column per
year." That is true, and it is the reason a within-file checker cannot work by
comparing labels to values.

list-incomplete-fixes.py does look inside one file, and asks exactly the right
question -- you retired a figure, did you catch every copy? But it reads YOUR
DIFF. It can only speak while the edit is still in your working tree. Every one
of the five above was introduced by an edit, merged, and thereby became
invisible: the diff is gone and no scan can reconstruct which value the author
meant to retire.

WHAT THIS DOES

It recovers that intent from the committed text. This corpus has a strong
convention of writing the retirement down -- "this guide previously stated 10%",
"the earlier figure of about 10.6%", "the old EGP 500,000 figure is superseded",
"is 14%, not 10%", "(was 10.5%)". Those notes name the retired value out loud.
So the note is the seed that check-amount-conflicts lacked: it distinguishes a
band table legitimately carrying six values from a file carrying a value its own
prose says is wrong.

For each guide: find the correction notes, take the values they retire, and look
for those values still stated on other lines of the same file.

WHAT IT IS NOT

It ranks, it does not accuse, and it always exits 0 -- the same contract as
list-incomplete-fixes.py and for the same reason. Survivors are split into

  ON SUBJECT  the line shares wording with the note, including at least one
              word rare enough in this file to mean something.
  off subject the value matches and nothing else does. Weaker, and the honest
              home for the false positives below.

The first version ranked by distance instead -- same heading as the note was
strong, further off was weak -- and the pre-fix Uruguay guide showed that is
backwards. The note sat in Section 5.3 and the stale copies in the Section 7
working paper, scored weak and hidden; the IRPF bracket rows where 10% is
simply a bracket sat nearer and scored strong. A stale copy is missed BECAUSE
it is far from the note, so distance cannot be the evidence. Subject is.

Rarity is measured per file, not from a fixed stopword list. "band" and
"income" shared between a note and a bracket row in uruguay-income-tax.md is
no evidence at all; "deduction" and "medium-company" are.

A survivor whose own line carries a historical marker ("was", "until", "prior
to", "no longer") is labelled rather than hidden, because that marker is
usually right and occasionally decorates a live figure.

KNOWN FALSE POSITIVES, none of which are worth suppressing blind:

  * A prior-year table. UK's 2025-26 Scottish band table holds GBP 15,397 and
    must. A note about the 2026-27 bands retires that number for 2026-27 only.
  * The other side of a supersession, stated deliberately so a reader can
    recognise the old figure -- "the 2% that circulates for Togo is the duty on
    extending a company's term".
  * A cohort rule. Pakistan charges 15% to one acquisition cohort and 12.5% to
    another; retiring 12.5% from one row says nothing about the other.

So read the surviving lines. Do not batch-edit them.

THE BLIND SPOT IT SHIPPED WITH

A correction note spanning two lines is not seen: each line is read on its own,
so "previously stated" on one line and the figure on the next is missed. Every
real case above happens to write the note on a single line, which is exactly the
kind of luck that hides a gap -- measured, not assumed. Fixing it means sentence
reassembly across the blockquote wrapping this corpus uses, and it is a real
gap, not a rounding error: see the selftest case marked KNOWN-MISS.

Usage:
    python3 scripts/check-stale-corrections.py [--verbose] [--selftest]
"""

import collections, glob, re, sys

# ---------------------------------------------------------------------------
# Value tokens.
#
# The first version of list-incomplete-fixes.py matched values as plain
# substrings and flagged Fiji because a removed "0%" matched inside "10%" two
# lines down. Tokenising both sides and comparing normalised tuples makes that
# class impossible rather than merely unlikely: '0' and '10' are different
# strings, and neither is ever a substring test.
# ---------------------------------------------------------------------------

_NUM = r'\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?'
_CUR = r'(?:[A-Z]{3}|[€£$₦₹₨₪₩¥฿])'

TOKEN = re.compile(
    r'(?P<pct>(?P<pnum>' + _NUM + r')\s?%)'
    r'|(?P<cur_pre>' + _CUR + r'\s?(?P<cnum>' + _NUM + r')'
    r'(?P<cmag>\s?(?:[bB][nN]|[bB]illion|[mM]\b|[mM]illion))?)'
    r'|(?P<cur_post>(?P<pnum2>' + _NUM + r')\s?(?P<cur2>[A-Z]{3})\b)'
    r'|(?P<big>\d{1,3}(?:,\d{3})+(?:\.\d+)?)'
)

_MAG = {'bn': 1e9, 'billion': 1e9, 'm': 1e6, 'million': 1e6}


def _canon(num, mag=None):
    """Normalise a numeric string so 10.0, 10 and 10.00 are one value."""
    try:
        f = float(num.replace(',', ''))
    except ValueError:
        return None
    if mag:
        f *= _MAG[mag.strip().lower().rstrip('.')]
    s = '%.6f' % f
    return s.rstrip('0').rstrip('.') or '0'


def values(text):
    """Every value token in `text`, as a set of (kind, canonical) pairs.

    Bare integers are deliberately NOT tokens. A guide is full of section
    numbers, article numbers and years, and admitting them would bury the
    signal. A value qualifies only if it carries a percent sign, a currency, or
    a thousands separator -- which is what a tax figure looks like.
    """
    out = set()
    for m in TOKEN.finditer(text):
        if m.group('pct'):
            c = _canon(m.group('pnum'))
            if c is not None:
                out.add(('pct', c))
        elif m.group('cur_pre'):
            c = _canon(m.group('cnum'), m.group('cmag'))
            if c is not None:
                out.add(('amt', c))
        elif m.group('cur_post'):
            c = _canon(m.group('pnum2'))
            if c is not None:
                out.add(('amt', c))
        elif m.group('big'):
            c = _canon(m.group('big'))
            if c is not None:
                out.add(('amt', c))
    return out


# ---------------------------------------------------------------------------
# Correction notes.
#
# A trigger marks the point at which a guide names a value it has decided
# against -- but the value does not always sit after the trigger, and assuming
# it did cost two selftest failures on real corpus wording:
#
#   fwd   "is 14%, not 10%"                 window opens at ", not"
#   back  "no 20% band ... it is superseded" the retirement is stated last
#   self  "the old EGP 500,000 figure"       the value is inside the phrase
#
# A backward window walks back one clause at a time until a clause yields a
# value, at most two. That is what separates "no 20% band; ... it is
# superseded" (walk past the empty clause, reach 20%) from "the rate is 30%;
# the old 20% is superseded" (stop at the first clause, never retire 30%).
# ---------------------------------------------------------------------------

TRIGGERS = [
    (re.compile(r'\bpreviously\s+(?:stated|read|said|put|gave|listed|carried|had|showed|set)\b', re.I), 'fwd'),
    (re.compile(r'\bearlier\s+versions?\s+of\s+this\s+(?:file|guide|skill|block|section)\b', re.I), 'fwd'),
    (re.compile(r'\bthis\s+(?:guide|file|skill|block|section|table)\s+(?:previously|formerly|once|used to)\b', re.I), 'fwd'),
    # (?<![-\w]) keeps the noun from matching inside a hyphenated compound.
    # Without it "replacing the former four-band 0%/4%/8%/10% schedule" matched
    # on "band", and the forward window then retired 0%, 8% and 10% -- three
    # values the CURRENT Kosovo schedule still uses. It ranked first in the
    # corpus, which is the worst place for a false positive to appear.
    (re.compile(r'\bthe\s+(?:old|former|earlier|previous|prior|legacy|stale|superseded)\s+'
                r'[^.;]{0,40}?(?<![-\w])(?:figure|value|rate|threshold|amount|band|limit|ceiling|floor|number)s?\b',
                re.I), 'self'),
    (re.compile(r'\(\s*was\s+(?=[^)]*[\d%])', re.I), 'fwd'),
    (re.compile(r';\s*was\s+(?=[^;.]*[\d%])', re.I), 'fwd'),
    (re.compile(r',\s+not\s+(?=[^,.;]{0,40}?(?:\d\s?%|' + _CUR + r'\s?\d))', re.I), 'fwd-noquote'),
    (re.compile(r'\b(?:is|was|now|been)\s+superseded\b', re.I), 'back'),
]

# DELIBERATELY ABSENT: "raised from 22%", "reduced from 30%", "up from".
#
# The first live run carried them and they produced most of its false
# positives -- Belarus retiring 15% from a rate change and matching an
# unrelated royalty withholding at 15%, Rwanda matching "30%+ of shares" as a
# tax rate, Laos and Slovenia and San Marino each pairing a change sentence
# with the standard-rate bullet directly beneath it. That family is
# check-superseded-rates.py's subject, which handles it across siblings with
# filters for exactly these cases. Two checkers doing one job badly is worse
# than one doing it well, so this one keeps to the family that has no other
# home: a value an author wrote down as retired.
QUOTED = re.compile(r'"[^"]*"|“[^”]*”')

_CLAUSE = re.compile(r'[.;]')


def _window(line, m, direction):
    """The text a trigger points at, as a string."""
    if direction == 'self':
        # The value may be inside the phrase ("the old EGP 500,000 figure") or
        # just after it ("the old figure of EGP 500,000"), so take both.
        return line[m.start():m.end() + 60]
    if direction.startswith('fwd'):
        tail = line[m.end():]
        # A colon ends the retirement too: "not "EUR 340 up to EUR 1,540":
        # **EUR 340** up to EUR 50,000" puts the correct bands right after it,
        # and without this the window swallowed them as retired.
        cut = re.search(r'(?<=[.;:])\s|\s--\s|\s—\s', tail)
        w = (tail[:cut.start()] if cut else tail)[:160]
        # "Five bands by taxable income, not "EUR 340 up to EUR 1,540"" retires
        # a PHRASING, and EUR 340 is still the correct first band. What follows
        # "not" in quotes is old wording being shown, so the figures inside it
        # are being displayed, not condemned.
        return QUOTED.sub(' ', w) if direction == 'fwd-noquote' else w
    head = line[:m.start()]
    for _ in range(2):
        bounds = [c.start() for c in _CLAUSE.finditer(head)]
        start = bounds[-1] + 1 if bounds else 0
        clause = head[start:]
        if values(clause):
            return clause
        if not bounds:
            break
        head = head[:bounds[-1]]
    return ''

# A survivor line carrying one of these is usually labelling the value as past
# already. Labelled, never hidden: the marker is occasionally attached to a
# neighbouring figure rather than to the one that matched.
HISTORICAL = re.compile(
    r'\bwas\b|\bwere\b|\bpreviously\b|\bformerly\b|\bprior\s+to\b|\buntil\b|\bbefore\s+\d'
    r'|\bno\s+longer\b|\bsuperseded\b|\babolished\b|\brepealed\b|\blegacy\b|\bhistoric'
    r'|\bold\b|\bformer\b|\bera\s+o\s+valor\b|\bup\s+to\s+3[01]\b|\bto\s+3[01]\s+\w{3}\s+20',
    re.I)

# ---------------------------------------------------------------------------
# Ranking.
#
# The first version ranked by section proximity: a survivor under the same
# heading as the note was strong, one further off was weak. Running it against
# the pre-fix Uruguay guide showed that is exactly backwards. The note sat in
# Section 5.3 and the three stale copies sat in the Section 7 working paper --
# scored weak, and hidden from the default output. The band-table rows where
# 10% is a legitimate IRPF bracket sat nearer the note and scored strong.
#
# Distance is not the signal. SUBJECT is: the note says "deduction rate", the
# true survivors say "Deduction rate (8% or 10%)", and the false ones are table
# rows of bare numbers that say nothing at all. Ranking on words shared with
# the note separates them, and it separates them in the right direction --
# a stale copy is missed BECAUSE it is far away.
# ---------------------------------------------------------------------------

STOP = set('''this that with from than then they them their which when what where
have this been were will would should could about into over under also only more
most some such each both other does not and for are was per use used using the
its it's who whom while after before above below same very much many any all one
two per cent percent apply applied applies here there these those but you your
guide file skill section table line note value figure amount case cases'''.split())


def terms(text):
    return {w for w in re.findall(r'[a-z][a-z-]{3,}', text.lower()) if w not in STOP}


HEADING = re.compile(r'^\s{0,3}(#{1,6})\s+(.*)$')

# A correction note is prose. A table row that happens to contain ", not 10%"
# is far more often a live comparison than a retirement.
def _is_prose(line):
    s = line.strip()
    return not (s.startswith('|') and s.endswith('|'))


# A note naming this many values at once is describing a whole schedule, not
# correcting one figure -- "the former four-band 0%/4%/8%/10% schedule". Old and
# new schedules overlap heavily, so most of those values are still live and
# still right. Such a note is kept but can never rank as strong.
SCHEDULE_VALUES = 3


def notes_in(lines):
    """[(lineno, retired_values, trigger_text, is_schedule)] per correction note."""
    found = []
    for i, line in enumerate(lines, 1):
        if not _is_prose(line):
            continue
        for trig, direction in TRIGGERS:
            for m in trig.finditer(line):
                vals = values(_window(line, m, direction))
                if vals:
                    found.append((i, vals, line[m.start():m.end()].strip()[:40],
                                  len(vals) >= SCHEDULE_VALUES))
    return found


def section_of(lines):
    """Map line number -> nearest heading above it, so survivors can be ranked."""
    out, cur = {}, '(top of file)'
    for i, line in enumerate(lines, 1):
        h = HEADING.match(line)
        if h:
            cur = h.group(2).strip()
        out[i] = cur
    return out


def scan(path, text):
    lines = text.splitlines()
    notes = notes_in(lines)
    if not notes:
        return []
    note_lines = {n for n, _, _, _ in notes}

    retired = {}
    for n, vals, trig, sched in notes:
        for v in vals:
            retired.setdefault(v, []).append((n, trig, sched))

    note_terms = {n: terms(lines[n - 1]) for n, _, _, _ in notes}

    # A shared word only discriminates if it is rare IN THIS FILE. Measured on
    # the pre-fix Uruguay guide: the note and two legitimate bracket rows both
    # said "band" and "income", which is no evidence at all in a file called
    # uruguay-income-tax.md. "deduction" and "medium-company" are evidence.
    # A fixed stopword list cannot know that; per-file frequency can.
    df = collections.Counter()
    body = [ln for ln in lines if ln.strip()]
    for ln in body:
        df.update(terms(ln))
    rare_max = max(3, int(0.02 * len(body)))

    hits = []
    for v, seeds in sorted(retired.items()):
        # Only a note that names one or two values can vouch for a strong hit.
        precise = [n for n, _, sched in seeds if not sched]
        subject = set().union(set(), *[note_terms[n] for n in precise]) if precise else set()
        strong, weak = [], []
        for i, line in enumerate(lines, 1):
            if i in note_lines or v not in values(line):
                continue
            shared = terms(line) & subject
            rare = {w for w in shared if len(w) >= 6 and df[w] <= rare_max}
            entry = (i, line.strip()[:150], bool(HISTORICAL.search(line)),
                     sorted(rare) or sorted(shared)[:4])
            # Two shared words, at least one of them rare enough in this file
            # to mean something. One word alone is noise in a corpus where
            # every other line says "rate" or "tax".
            if len(shared) >= 2 and rare:
                strong.append(entry)
            else:
                weak.append(entry)
        if strong or weak:
            hits.append((v, [(n, t) for n, t, _ in seeds], strong, weak))
    return hits


def main():
    verbose = '--verbose' in sys.argv
    files = sorted(glob.glob('skills/**/*.md', recursive=True))
    reports = []
    for p in files:
        try:
            text = open(p, encoding='utf-8').read()
        except OSError:
            continue
        hits = scan(p, text)
        if hits:
            strong = sum(len(s) for _, _, s, _ in hits)
            reports.append((strong, sum(len(e) for _, _, _, e in hits), p, hits))

    reports.sort(key=lambda r: (-r[0], -r[1], r[2]))
    shown = [r for r in reports if r[0]] if not verbose else reports

    for strong, weak, p, hits in shown:
        print('\n%s  (%d on subject, %d off subject)' % (p, strong, weak))
        for (kind, val), seeds, on_subject, off in hits:
            if not on_subject and not verbose:
                continue
            disp = val + '%' if kind == 'pct' else val
            seed_txt = ', '.join('L%d "%s"' % (n, t) for n, t in seeds[:3])
            print('  retired %-14s seeded at %s' % (disp, seed_txt))
            for label, group in (('  ON SUBJECT', on_subject), ('  off subj  ', off)):
                if not verbose and label.strip() == 'off subj':
                    continue
                for i, snippet, hist, shared in group:
                    print('%s L%-5d %s%s%s'
                          % (label, i, snippet,
                             '   [shares: %s]' % ', '.join(shared) if shared else '',
                             '   [historical marker]' if hist else ''))

    print('\n%d guide(s) scanned; %d with a survivor on the note\'s subject; '
          '%d with any survivor.'
          % (len(files), sum(1 for r in reports if r[0]), len(reports)))
    if not verbose:
        print('Pass --verbose for off-subject survivors and the weak files.')
    return 0


# ---------------------------------------------------------------------------

def selftest():
    fail = 0

    def check(label, cond):
        nonlocal fail
        if not cond:
            fail += 1
            print('FAIL: %s' % label)

    # Tokeniser: the exact trap the first list-incomplete-fixes shipped with.
    check('0% does not match inside 10%', ('pct', '0') not in values('a rate of 10% applies'))
    check('10% is found', ('pct', '10') in values('a rate of 10% applies'))
    check('10.0 and 10 are one value', values('10.0%') == values('10%'))
    check('money with code', ('amt', '500000') in values('EGP 500,000 of turnover'))
    check('money with symbol', ('amt', '2090') in values('roughly €2,090 per month'))
    check('trailing currency code', ('amt', '3044000') in values('3,044,000 PYG floor'))
    check('separated number alone', ('amt', '15397') in values('GBP 12,571 -- 15,397'))
    check('magnitude suffix', ('amt', '50000000000') in values('turnover > NGN 50bn'))
    check('bare year is not a value', values('effective 2026') == set())
    check('section number is not a value', values('see s.202 and art. 56') == set())

    # Uruguay, real shape: a note naming the retired rate, survivors in a
    # different section of the same file.
    uy = '\n'.join([
        '## 5. Tax computation',
        '- Multiply by the deduction rate: **14%** at or below the threshold; **8%** above.',
        '> **Corrected: the rate is 14%, not 10%.** Earlier versions of this file put the lower rate at 10%.',
        '## 7. Working paper',
        '  D7. Deduction rate (8% or 10%) ___________',
        '  [ ] Deduction rate (8% vs 10%) confirmed against income?',
    ])
    hits = scan('uy.md', uy)
    got = {v for v, _, _, _ in hits}
    check('uruguay: 10% is recovered as retired', ('pct', '10') in got)
    check('uruguay: 14% is not retired by its own note',
          ('pct', '14') not in got)
    surv = [h for h in hits if h[0] == ('pct', '10')][0]
    check('uruguay: both survivors reported', len(surv[2]) + len(surv[3]) == 2)

    # Nigeria, real shape, copied from the bullet as it is actually written:
    # the retirement is stated last, and the clause between it and the retired
    # value holds no figure at all.
    ng = '\n'.join([
        '## Tax',
        '- **CIT** — **30%**. NTA 2025 s.56 has two bands only. There is no medium-company'
        ' 20% band from 1 January 2026; that was the Finance Act 2019/2020 structure and it'
        ' is superseded  _(NTA 2025 s.56)_',
        '## Comparison',
        '| Ltd | CIT | 20% medium company | ... |',
    ])
    hits = scan('ng.md', ng)
    got = {v for v, _, _, _ in hits}
    check('nigeria: 20% recovered by walking back past an empty clause',
          ('pct', '20') in got)
    check('nigeria: the live 30% is not retired with it', ('pct', '30') not in got)

    # The backward walk must stop at the first clause that has a value, or it
    # would retire the replacement along with the thing replaced. Tested
    # through notes_in rather than scan: scan only reports a retired value that
    # still has a survivor somewhere, and here it has none by construction.
    stop = ['- The rate is 30%; the old 20% is superseded.']
    got = set().union(*[v for _, v, _, _ in notes_in(stop)])
    check('backward walk stops at the first clause with a value',
          ('pct', '20') in got and ('pct', '30') not in got)

    # Liechtenstein, real shape: "The earlier figure of about 10.6%".
    li = '\n'.join([
        '## Rates',
        '- AHV/IV/FAK total 12.285%. The earlier figure of about 10.6% split evenly was',
        '  the Swiss model borrowed for want of a source.',
        '## Overview',
        '- Social contributions run to roughly 10.6% of gross salary.',
    ])
    check('liechtenstein: 10.6% recovered from "the earlier figure of"',
          ('pct', '10.6') in {v for v, _, _, _ in scan('li.md', li)})

    # Egypt, real shape: "The old EGP 500,000 figure is superseded" -- and note
    # the corpus later decided the OPPOSITE was true. The checker's job is to
    # surface the disagreement, not to know which side wins.
    eg = '## VAT\n- The old EGP 500,000 figure is superseded, not merely doubtful.\n' \
         '## Registration\n- Register at EGP 500,000 of annual turnover.'
    check('egypt: 500,000 recovered from "the old ... figure"',
          ('amt', '500000') in {v for v, _, _, _ in scan('eg.md', eg)})

    # REGRESSIONS from the first live run over the corpus. Both were silent:
    # they produced plausible-looking output, which is how a checker bug
    # survives review.
    #
    # Slovakia: the note retires a PHRASING, and the numbers inside the quoted
    # phrasing are still correct. Worse, the window ran past the closing quote
    # and swallowed the live bands that follow the colon.
    sk = ['- Five bands by taxable income, not "EUR 340 up to EUR 1,540": **EUR 340**'
          ' up to EUR 50,000, **EUR 940** from 50,000 to 250,000.']
    got = set().union(set(), *[v for _, v, _, _ in notes_in(sk)])
    check('slovakia: a quoted wrong phrasing retires nothing', got == set())

    # Nepal: "NPR 2M" tokenised as the value 2, because the magnitude suffix
    # was matched case-sensitively against a lowercase alternation.
    check('NPR 2M is two million, not two',
          ('amt', '2000000') in values('services raised from NPR 2M eff.'))

    # Kosovo: ranked FIRST in the corpus with 25 in-section survivors, all
    # false. "band" matched inside the compound "four-band", and the window
    # then retired the three rates the current schedule still uses.
    ks = ['**PIT (primary employer)**  _(PwC; EY (Law 08/L-142, effective 23 Aug 2024,'
          ' replacing the former four-band 0%/4%/8%/10% schedule).)_']
    check('kosovo: "four-band" is not the noun "band"', notes_in(ks) == [])

    # A note that names a whole schedule can never rank as strong, because old
    # and new schedules overlap and most of the shared values are still right.
    sched = '\n'.join([
        '## Bands',
        '- The old rates of 0%, 8% and 10% applied before the reform.',
        '| Band 1 | 8% |',
    ])
    h = scan('sc.md', sched)
    check('a schedule-wide note yields no in-section survivors',
          all(not same for _, _, same, _ in h))

    # Ranking, measured against the pre-fix Uruguay guide: the true survivors
    # share the note's subject ("deduction rate"), the false ones are bracket
    # rows of bare numbers that share nothing. Distance told the opposite story.
    rank = '\n'.join([
        '## 5',
        '- The deduction credit rate is 14%, not 10%.',
        '## 7',
        '  D7. Deduction credit rate (8% or 10%) ______',
        '| 576,576 -- 823,680 | 84 -- 120 | 10% | 24,710.40 |',
    ])
    h = [x for x in scan('rank.md', rank) if x[0] == ('pct', '10')]
    check('ranking: the working-paper line is on subject',
          h and any('deduction' in s[3] for s in h[0][2]))
    check('ranking: a bare bracket row is off subject',
          h and any(i == 5 for i, _, _, _ in h[0][3]))

    # NEGATIVE CONTROLS -- these must stay silent.
    band = '\n'.join([
        '## Bands',
        '| Band 1 | 10% |', '| Band 2 | 20% |', '| Band 3 | 30% |',
    ])
    check('a plain band table raises nothing', scan('b.md', band) == [])

    row = '## T\n| Rate | 15%, not 10% | a live comparison column |'
    check('a table row is not read as a correction note', scan('r.md', row) == [])

    nofig = '## X\n- This block previously read "TBC -- not yet enacted".'
    check('a note naming no figure raises nothing', scan('n.md', nofig) == [])

    # KNOWN-MISS, asserted so the gap stays measured rather than assumed.
    wrapped = '\n'.join([
        '## Rates',
        '> **Corrected.** This guide previously stated',
        '> the lower rate as 10%.',
        '## Working paper',
        '- Deduction rate 10%.',
    ])
    check('KNOWN-MISS: a note wrapped across two lines is not seen (documented)',
          scan('w.md', wrapped) == [])

    if fail:
        print('selftest: %d case(s) FAILED' % fail)
        return 1
    print('selftest: tokenising, the three window directions, ranking and '
          '4 corpus regressions pass (1 documented miss)')
    return 0


if __name__ == '__main__':
    sys.exit(selftest() if '--selftest' in sys.argv else main())
