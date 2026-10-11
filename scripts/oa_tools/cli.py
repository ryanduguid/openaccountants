"""Argument types and parsing shared by repository commands."""

import argparse
import os
import sys


def directory(value):
    """Keep a caller-relative directory spelling, rejecting missing and file paths."""
    if not os.path.isdir(value):
        raise argparse.ArgumentTypeError(f"not a directory: {value!r}")
    return value


def non_negative_integer(value):
    """Parse a count threshold, including zero."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a non-negative integer: {value!r}") from None
    if number < 0:
        raise argparse.ArgumentTypeError(f"not a non-negative integer: {value!r}")
    return number


def _output_path(value):
    if not value:
        raise argparse.ArgumentTypeError('--out requires a file path')
    return value


def metadata_arguments(description, argv=None):
    """Validate metadata editor arguments before help or write intent is used."""
    parser = argparse.ArgumentParser(description=description, allow_abbrev=False, add_help=False)
    parser.add_argument('-h', '--help', action='store_true', help='show this help message and exit')
    parser.add_argument('--apply', action='store_true', help='write the reported metadata changes')
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.help:
        parser.print_help()
    return args


def generator_arguments(description, argv=None, *, output=None, selftest=False):
    """Validate all arguments before help; keep output paths as literal strings."""
    parser = argparse.ArgumentParser(description=description, allow_abbrev=False, add_help=False)
    parser.add_argument('-h', '--help', action='store_true', help='show this help message and exit')
    arguments = list(sys.argv[1:] if argv is None else argv)
    if output is not None:
        parser.add_argument('--out', action='append', type=_output_path, metavar='PATH',
                            help='write to PATH instead of the repository default')
        # The existing CLI accepts separate single-hyphen filenames, including '-'.
        # Attach consumed values so argparse keeps that spelling as a path.
        normalised = []
        remaining = iter(arguments)
        for value in remaining:
            if value == '--':
                normalised.append(value)
                normalised.extend(remaining)
                break
            if value == '--out':
                path = next(remaining, None)
                if path is None or path.startswith('--'):
                    parser.error('--out requires a file path')
                normalised.append('--out=' + path)
            else:
                normalised.append(value)
        arguments = normalised
    if selftest:
        parser.add_argument('--selftest', action='store_true', help='run the offline selftest')
    args = parser.parse_args(arguments)
    if output is not None:
        if args.out and len(args.out) > 1:
            parser.error('--out may be supplied only once')
        args.out = args.out[0] if args.out else output
    if args.help:
        parser.print_help()
    return args
