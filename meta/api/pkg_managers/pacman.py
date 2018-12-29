# meta.api.pacman.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for accessing pacman functionality."""

import logging


def install(*pkgs, silent=False):
    """Installs the given packages with the `pacman -S` command."""

def uninstall(pkg, silent=False):
    """Installs the given package with the `pacman -R` command."""
