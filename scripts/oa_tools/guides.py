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


def markdown_files(root=None, *, sort_filenames=True):
    """Yield display and filesystem paths for a review aid's Markdown files.

    A default scan reads this checkout's skills tree and reports repository-relative
    paths. An explicit root is resolved from the caller's working directory and
    keeps its spelling in reports. READMEs are included, as the review aids also
    inspect their claims. Directory symlinks are not followed. Callers can retain
    native filename order when their reports depend on it.
    """
    tree = "skills" if root is None else os.fspath(root)
    base = REPO_ROOT if root is None else os.curdir
    scan_root = os.path.join(base, tree)
    for directory, _, filenames in os.walk(scan_root):
        if sort_filenames:
            filenames.sort()
        for filename in filenames:
            if filename.endswith(".md"):
                source = os.path.join(directory, filename)
                yield os.path.join(tree, os.path.relpath(source, scan_root)), source


def skill_path_parts(path, root=None):
    """Layout components for grouping, independent of a root's spelling.

    Owned guides use this checkout's skills layout, including scopes such as
    '.' from within a country folder. Copied trees may have another root name;
    international, us-states and federal still identify their branches.
    Display paths are left to markdown_files().
    """
    tree = "skills" if root is None else os.fspath(root)
    base = REPO_ROOT if root is None else os.curdir
    source = os.path.normcase(os.path.abspath(os.path.join(base, path)))
    scan_root = os.path.normcase(os.path.abspath(os.path.join(base, tree)))
    try:
        owned = os.path.relpath(source, os.path.join(REPO_ROOT, "skills"))
    except ValueError:  # An explicit root can be on another Windows drive.
        owned = None
    if owned is not None and owned != os.pardir and not owned.startswith(os.pardir + os.sep):
        return ["skills", *owned.split(os.sep)]
    relative = os.path.relpath(source, scan_root).split(os.sep)
    branches = ("international", "us-states", "federal")
    if relative[0] in branches or any(os.path.isdir(os.path.join(scan_root, branch))
                                      for branch in branches):
        return ["skills", *relative]
    parts = source.split(os.sep)
    root_parts = scan_root.split(os.sep)
    for index in range(len(root_parts) - 1, -1, -1):
        if root_parts[index] == "skills":
            return parts[index:]
        if root_parts[index] in branches:
            return ["skills", *parts[index:]]
    return ["skills", *relative]


def skill_group(path, root=None):
    """Review label for a country/state folder or a flat guide tree.

    For example, skills/international/malta/a.md groups as malta and
    skills/federal/a.md groups as federal. The filename is never the label.
    """
    parts = skill_path_parts(path, root)
    if len(parts) < 3:
        return None
    return parts[2] if len(parts) >= 4 else parts[1]


def jurisdiction_group(path, root=None):
    """Country/state label for review rules that assume a single jurisdiction.

    Workflow, cross-border and other shared trees mix jurisdictions. Their
    folder names cannot supply a house currency, agency or filing rule.
    """
    parts = skill_path_parts(path, root)
    if len(parts) >= 3 and parts[1] == "federal":
        return "federal"
    if len(parts) >= 4 and parts[1] in ("international", "us-states"):
        return parts[2]
    return None
