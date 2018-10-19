# meta.shell.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Functions for accessing and interacting with the system's shell."""

import platform
import shlex
import subprocess
import sys

from meta.exceptions import UnsupportedOS, EmptyCommand


def execute(command, silent=True):
    """Runs the passed shell command based on the operating system and returns the
    output."""

    # check that the command isn't an empty string
    if command == "":
        raise EmptyCommand()

    # determine how subprocess expects the command to be split,
    # based on operating system (windows doesn't require split)
    if platform.system() == "Windows":
        args = command
    elif platform.system() == "Linux":
        args = shlex.split(command)
    else:
        raise UnsupportedOS

    # TODO: check if better way to handle stderr?
    cmd_process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        bufsize=1,
    )

    # handle command output as it occurs
    # TODO: incorporate into logging
    output = ""
    with cmd_process.stdout:
        for character in iter(lambda: cmd_process.stdout.read(1).decode("utf-8"), ""):
            output += character

            if not silent:
                sys.stdout.write(character)
                sys.stdout.flush()

    # check for problems with the execution
    if cmd_process.wait() != 0:
        raise subprocess.CalledProcessError(cmd_process.returncode, args)

    return output
