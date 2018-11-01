# meta.api.pip.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for accessing pip functionality."""

import logging

import meta.shell


def install(command, version="", user_install=True, silent=False):
    """Executes the passed command as a pip install

    :param str command: The string of packages to install
    :param str version: The version of pip executable being used (e.g. 2, 3, 3.4, etc.)
    :param bool user_install: Whether to install using the user scheme or not
    :param bool silent: Whether to supress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell
    """

    logging.info("PIP API accessed with command install %s, pip version %s, user_install %s",
                 command, version, user_install)

    if user_install:
        command = "{0} --user".format(command)

    output = execute("install {0}".format(command), version=version, silent=silent)
    return output


def uninstall(command, version="", silent=False):
    """Executes the passed command as a pip uninstall

    :param str command: The string of packages to uninstall
    :param str version: The version of pip executable being used (e.g. 2, 3, 3.4, etc.)
    :param bool silent: Whether to supress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell
    """

    logging.info("PIP API accessed with command uninstall %s, pip version %s", command, version)

    output = execute("uninstall {0}".format(command), version=version, silent=silent)
    return output


def execute(command, version="", silent=False):
    """Executes the passed command in the system's shell.

    :param str command: The string command to execute.
    :param str version: The version of pip executable being used (e.g. 2, 3, 3.4, etc.)
    :param bool silent: Whether to supress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell
    """

    output = meta.shell.execute("pip{0} {1}".format(version, command), silent=silent)
    return output
