"""Shared helpers for the scripts in this directory.

The scripts are hyphenated files (``build-index.py``, ``validate-guides.py``),
which Python cannot import by name, so for years each one carried its own copy
of the repository root, the guide walker and the frontmatter reader, or loaded
a sibling by file path with ``importlib``. This package is the one place those
live:

- :mod:`oa_tools.paths` -- where the repository is and which trees hold guides.
- :mod:`oa_tools.guides` -- which Markdown files are candidate guides.
- :mod:`oa_tools.frontmatter` -- the frontmatter reader, tolerant (the index
  generator's regex scanner) and strict (PyYAML, what validation gates on).

A script imports it after putting its own directory on ``sys.path``, because
the tests and the validator load scripts by file path, where the script's
directory is not on the path automatically::

    _HERE = os.path.dirname(os.path.abspath(__file__))
    if _HERE not in sys.path:
        sys.path.insert(0, _HERE)

    from oa_tools.frontmatter import read_frontmatter

Shared logic goes here, never into a second copy in another script.
"""

__all__ = ["frontmatter", "guides", "paths"]
