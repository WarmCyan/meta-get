# meta.api.shell.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for accessing backend shell functionality."""

import logging

import meta.shell


# NOTE: even though this currently doesn't add much functionality, since it's in the API, it will
# be expected to ensure some level of backwards compatibility if the backend changes any.
def execute(command, silent=False):
    """Executes the passed command in the system shell.

    :param str command: The string command to execute.
    :param bool silent: Whether to suppress the console output of the command or not.
    :returns: A string of everything written to stdout and stderr by the shell.
    """

    logging.info("Shell API accessed with command:%s", command)

    output = meta.shell.execute(command, silent=silent)
    return output
