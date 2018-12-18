# meta.exceptions.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Specific exception types for things that go wrong."""


class UnsupportedOS(Exception):
    """Raised if attempted on an unknown operating system."""


class EmptyCommand(Exception):
    """Raised if attempted to run a blank "" command."""


class RelativePathUnwise(Exception):
    """Raised if a relative path used where one doesn't make sense."""


class InvalidAutotrackerFile(Exception):
    """Raised if a key (files, packages, dependencies) not found in the json of a given file."""
