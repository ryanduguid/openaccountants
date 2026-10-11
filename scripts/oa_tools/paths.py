"""Where the repository is and which of its trees hold guides.

Every path is absolute and derived from this file's location. Review aids use
this checkout for default scans. Explicit directory arguments are resolved
from the caller's working directory.
"""

import os

#: The repository root: the directory holding ``skills/``, ``index.json`` and
#: this package's parent ``scripts/``.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#: The editable source tree (``docs/REPO-LAYOUT.md``).
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")

#: The generated per-jurisdiction bundles, except the hand-authored ones below.
PACKAGES_DIR = os.path.join(REPO_ROOT, "packages")

#: Directories under ``packages/`` that are maintained by hand and have no
#: builder in ``build-packages.py``: the build must never wipe or write into
#: them. Since 2026-09-28 ``us-federal`` holds only the federal rates JSONs
#: and their runbook; the federal guides live in ``skills/federal/`` and are
#: shared into every US package. ``docs/REPO-LAYOUT.md`` is the human-readable
#: statement of the same rule.
HAND_AUTHORED_PACKAGES = frozenset({"us-federal"})

#: The trees walked for guide files, relative to :data:`REPO_ROOT`: the source
#: tree. Generated packages are excluded on purpose; ``validate-guides.py``
#: checks those separately against the source.
GUIDE_TREES = ("skills",)


def repo_root():
    """The repository root, for callers that want a function rather than a constant."""
    return REPO_ROOT


def rel(path, root=REPO_ROOT):
    """``path`` relative to ``root`` with forward slashes, the form the index and
    the validator report paths in on every platform."""
    return os.path.relpath(path, root).replace(os.sep, "/")
