#!/usr/bin/env python3
"""Merge origin/main (or another revision) into this branch and rebuild every derived file.

Every guide pull request rewrites the same derived files: the generated trees
(packages/, index.json, PARTNERS.md, llms-full.txt), the coverage figures in
README.md, llms.txt, docs/QUALITY-TIERS.md and docs/COVERAGE.md, and now and
then a gate baseline. Two pull requests that each add an unrelated guide
therefore conflict on the counts at the top of index.json, and a derived file
resolved by hand is easily left stale. The `oa-merge` attribute in
.gitattributes names those files and how each one merges:

  regenerate  rebuilt by `make build` from the merged sources;
  figures     hand-written, but `make build` writes its coverage figures
              (check-coverage-claims.py --write), so it is merged with those
              figures masked and only a conflict in its other text remains;
  baseline    a gate baseline, merged as a set: an entry either side added
              stays, one either side removed goes, and the checker re-gates it.

A git merge driver cannot do this: git runs drivers one file at a time before
the merged tree exists, so a driver can only pick a side, and GitHub ignores
custom drivers. So this script refuses uncommitted changes and (here and on
--continue) untracked files among the derived paths, then runs
`git merge --no-commit`. When any other
file conflicts it stops before resolving a derived file or running a
generator (git has already written its merge of each derived file, conflict
markers included); resolve and `git add` those files, then run it with
--continue. It then resolves the derived files, runs `make build`'s
generators, stages what they changed and gates the result with
check-coverage-claims.py and every baseline's checker. The merge is left
staged for you to review and commit.

Usage: python3 scripts/merge-main.py [REV]     (make merge-main [REV=<rev>])
       python3 scripts/merge-main.py --continue
"""
import argparse, importlib.util, io, os, subprocess, sys, tempfile

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPTS)
if SCRIPTS not in sys.path:
    sys.path.insert(0, SCRIPTS)
from oa_tools import findings  # noqa: E402

#: `make build`, in its order; tests/test_dev_entry_point.py pins the two together.
BUILD = (
    ('build-packages.py',),
    ('build-index.py',),
    ('check-coverage-claims.py', '--write'),
    ('build-partners.py',),
    ('build-llms-full.py',),
)
KINDS = ('regenerate', 'figures', 'baseline')


def git(*args, stdin=None, check=True):
    result = subprocess.run(('git',) + args, input=stdin, capture_output=True, text=True, encoding='utf-8')
    if check and result.returncode:
        sys.exit('merge-main: git %s failed:\n%s%s' % (' '.join(args), result.stdout, result.stderr))
    return result


def merging():
    return git('rev-parse', '-q', '--verify', 'MERGE_HEAD', check=False).returncode == 0


def nul_list(text):
    return [path for path in text.split('\0') if path]


def merge_kinds(paths):
    """Each path's oa-merge attribute: one of KINDS, or None for an ordinary file."""
    if not paths:
        return {}
    fields = git('check-attr', '-z', '--stdin', 'oa-merge', stdin='\0'.join(paths) + '\0').stdout.split('\0')
    return {path: value if value in KINDS else None
            for path, value in zip(fields[0::3], fields[2::3])}


def stage(number, path):
    """The text of one side of a conflict (1 base, 2 ours, 3 theirs), or None."""
    result = git('show', ':%d:%s' % (number, path), check=False)
    return result.stdout if result.returncode == 0 else None


def write_text(path, text):
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)


def merge_figures(path, mask):
    """The three-way merge of a figures file with its figures masked, or None
    when one side deleted it or its other text still conflicts."""
    base, ours, theirs = (stage(n, path) for n in (1, 2, 3))
    if ours is None or theirs is None:
        return None
    with tempfile.TemporaryDirectory() as tmp:
        sides = []
        for name, text in (('ours', ours), ('base', base or ''), ('theirs', theirs)):
            sides.append(os.path.join(tmp, name))
            write_text(sides[-1], mask(path, text))
        result = git('merge-file', '-p', *sides, check=False)
    return result.stdout if result.returncode == 0 else None


def baseline_entries(text):
    """findings.load_baseline's reading of a baseline's text."""
    if text is None:
        return None
    return {line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith('#')}


def merge_entries(base, ours, theirs):
    """A set's three-way merge: kept by both, or added by either."""
    return (ours & theirs) | (ours - base) | (theirs - base)


def merge_baseline(path):
    base, ours, theirs = (baseline_entries(stage(n, path)) for n in (1, 2, 3))
    if ours is None or theirs is None:
        return None
    return merge_entries(base or set(), ours, theirs)


def coverage_claims():
    spec = importlib.util.spec_from_file_location('coverage_claims', os.path.join(SCRIPTS, 'check-coverage-claims.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_script(*argv):
    return subprocess.run((sys.executable, os.path.join(SCRIPTS, argv[0])) + argv[1:]).returncode


def finish():
    """Resolve the derived conflicts, rebuild, stage and gate; returns the exit code."""
    conflicted = nul_list(git('diff', '--name-only', '-z', '--diff-filter=U').stdout)
    kinds = merge_kinds(conflicted)
    claims = coverage_claims()
    blank = claims.figures({'guides': []})
    figures, baselines, blocking = {}, {}, []
    for path in conflicted:
        kind = kinds[path]
        if kind == 'regenerate':
            continue  # make build rewrites it below
        if kind == 'figures':
            merged = figures[path] = merge_figures(path, lambda p, text: claims.rewrite(p, text, blank))
        elif kind == 'baseline':
            merged = baselines[path] = merge_baseline(path)
        else:
            merged = None
        if merged is None:
            blocking.append(path)
    if blocking:
        print('merge-main: these conflicts need a person. Resolve them, `git add` them, then run\n'
              '  python3 scripts/merge-main.py --continue')
        for path in blocking:
            print('  ' + path)
        print('Derived files stay conflicted until then; --continue resolves and rebuilds them.')
        return 1

    for path, text in figures.items():
        write_text(path, text)
    for path, entries in baselines.items():
        findings.write_baseline(path, os.path.basename(path)[:-len('.txt')], (), keep=entries)
    for step in BUILD:
        code = run_script(*step)
        if code:
            print('merge-main: %s failed (exit %d); the merge is not finished' % (' '.join(step), code))
            return code

    changed = nul_list(git('diff', '--name-only', '-z').stdout)
    changed += nul_list(git('ls-files', '--others', '--exclude-standard', '-z').stdout)
    derived = sorted(set(conflicted) | {p for p, kind in merge_kinds(changed).items() if kind})
    if derived:
        git('add', '-A', '--pathspec-from-file=-', '--pathspec-file-nul', stdin='\0'.join(derived) + '\0')
    left = nul_list(git('diff', '--name-only', '-z', '--diff-filter=U').stdout)
    if left:
        print('merge-main: still conflicted: ' + ', '.join(left))
        return 1

    # Every baseline's checker, not only the merged ones': a clean textual merge
    # can still list a fingerprint the merged tree no longer reproduces, and a
    # rerun with --continue must not skip a baseline that failed last time.
    tracked = nul_list(git('ls-files', '-z').stdout)
    gates = ['check-coverage-claims.py']
    gates += ['check-%s.py' % os.path.basename(path)[:-len('.txt')]
              for path, kind in sorted(merge_kinds(tracked).items()) if kind == 'baseline']
    failed = [gate for gate in gates if run_script(gate)]
    if failed:
        print('merge-main: %s failed on the merged tree; fix that before committing' % ', '.join(failed))
        return 1
    print('merge-main: merged and rebuilt. Review `git diff --cached`, run `make check`, then `git commit --no-edit`.')
    return 0


def refuse_untracked_derived():
    """Exit when an untracked file sits among the derived paths: the build
    replaces packages/ and finish() stages new derived paths, so the file
    would be lost or staged unasked."""
    untracked = nul_list(git('ls-files', '--others', '--exclude-standard', '-z').stdout)
    stray = sorted(path for path, kind in merge_kinds(untracked).items() if kind)
    if stray:
        sys.exit('merge-main: move or delete these untracked files first:\n  ' + '\n  '.join(stray))


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog='merge-main.py', description=__doc__.split('\n\n')[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('rev', nargs='?', default='origin/main', help='the revision to merge (default: %(default)s)')
    parser.add_argument('--continue', dest='resume', action='store_true',
                        help='finish a merge this script stopped, once the other conflicts are resolved and staged')
    args = parser.parse_args(argv)
    os.chdir(ROOT)

    if args.resume:
        if not merging():
            sys.exit('merge-main: no merge in progress; run python3 scripts/merge-main.py [REV]')
        refuse_untracked_derived()
        return finish()
    if merging():
        sys.exit('merge-main: a merge is already in progress; finish it with --continue or run git merge --abort')
    if git('status', '--porcelain', '--untracked-files=no').stdout.strip():
        sys.exit('merge-main: commit or stash your changes first')
    refuse_untracked_derived()
    result = git('merge', '--no-ff', '--no-commit', args.rev, check=False)
    print(result.stdout, end='')
    if not merging():  # already up to date, or the merge never started
        print(result.stderr, end='', file=sys.stderr)
        return result.returncode
    return finish()


if __name__ == '__main__':
    sys.exit(main())
