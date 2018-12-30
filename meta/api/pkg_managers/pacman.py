# meta.api.pacman.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for accessing pacman functionality."""

import logging

import meta.current
import meta.shell


def install(*pkgs, silent=False):
    """Installs the given packages with the `pacman -S` command."""

    pkg_list = " ".join(pkgs)
    logging.info("Pacman API requested to install packages %s", pkg_list)

    output = meta.shell.execute("sudo pacman -S {0}".format(pkg_list), silent=silent)

    # add to autotracker
    for pkg in pkgs:
        meta.current.PACKAGE_AUTOTRACKER.packages.append(
            {"name": pkg, "pkg_manager": "pacman"}
        )

    return output


def uninstall(pkg, silent=False):
    """Installs the given package with the `pacman -R` command."""

    logging.info("Pacman API request to uninstall package %s", pkg)

    output = meta.shell.execute("sudo pacman -R {0}".format(pkg), silent=silent)
    return output
