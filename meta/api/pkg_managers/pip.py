# meta.api.pip.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for accessing pip functionality."""

import meta.shell


def install(command, silent=False):
    """Executes the passed command as a pip install

    :param str command: The string of packages to install
    :param bool silent: Whether to supress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell
    """

    output = __execute("install %s" % command, silent=silent)
    return output


def __execute(command, silent=False):
    """Executes the passed command in the system's shell.

    :param str command: The string command to execute.
    :param bool silent: Whether to supress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell
    """

    output = meta.shell.execute("pip %s" % command, silent=silent)
    return output
