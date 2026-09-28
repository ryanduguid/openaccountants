"""Guide discovery: which Markdown files are candidate guides, and where.

A candidate is a ``.md`` file that is not a README. Whether it is a guide is
decided by its frontmatter afterwards: :func:`oa_tools.frontmatter.extract_frontmatter`
returns ``None`` for a plain document, and the index generator skips those.
"""

import os

from .paths import GUIDE_TREES, REPO_ROOT, rel


def is_guide_filename(filename):
    """``.md`` and not a README. READMEs are docs, never guides."""
    return filename.endswith(".md") and not filename.lower().startswith("readme")


def guide_files(root=REPO_ROOT, trees=GUIDE_TREES):
    """Sorted, de-duplicated, ``root``-relative POSIX paths of every candidate
    guide file under ``trees``.

    ``trees`` are directories relative to ``root``; one that does not exist is
    skipped, so a partial checkout still indexes what it has. Symbolic links to
    directories are not followed (``os.walk``'s default).
    """
    found = set()
    for tree in trees:
        base = os.path.join(root, tree)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames.sort()
            for filename in filenames:
                if is_guide_filename(filename):
                    found.add(rel(os.path.join(dirpath, filename), root))
    return sorted(found)


def read_text(rel_path, root=REPO_ROOT):
    """The file's text as the generators read it: UTF-8, undecodable bytes replaced."""
    with open(os.path.join(root, rel_path), encoding="utf-8", errors="replace") as fh:
        return fh.read()
