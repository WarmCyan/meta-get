# meta.api.fileystem.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for managing files and folders."""

import logging
import os
import platform

import meta.shell

# NOTE: probably want to use shutil or os for some of these

# NOTE: all self.paths are ASSUMED to exist, so no fancy manual path resolution will be necessary

# NOTE: maybe this becomes File, and Folder just inherits from File?
class _FileUnit:
    """A parent class for Folder and File that contains common logic."""

    def __init__(self, path):
        self.name = ""
        self.path = os.path.abspath(os.path.expanduser(os.path.expandvars(path)))

    def move(self, dest_path):
        """Moves the file to the passed location.

        :param str dest_path: The destination path to move this file to.
        """

        logging.info("Requested move of file '%s' to '%s'", self.path, dest_path)

        cmd_word = ""
        # determine command based on OS
        if platform.system() == "Linux":
            cmd_word = "mv"
        elif platform.system() == "Windows":
            cmd_word = "move"

        # resolve if a relative path
        resolved_path = self.resolve_path(dest_path)

        # execute the movement shell command
        meta.shell.execute("{0} {1} {2}".format(cmd_word, self.path, resolved_path))

    def resolve_path(self, unresolved_path):
        """Handles fixing any relative paths.

        (all ./ and ../ will be based off of this file's directory, rather than the actual "cwd")

        :param str unresolved_path: The path to be resolved
        """

        resolved = ""
        with os.chdir(self.path):
            resolved = os.path.abspath(os.path.expanduser(os.path.expandvars(unresolved_path)))

        logging.debug("Resolving path '%s' to '%s'", unresolved_path, resolved)
        return resolved


class Folder(_FileUnit):
    """A file unit that contains other folders and files."""

    def __init__(self, path):
        super().__init__(path)
        self.contents = {}

    def delete(self):
        """Removes this folder from the file system."""

        logging.info("Requested removal of folder '%s'", self.path)

        # run command based off of OS
        if platform.system() == "Linux":
            meta.shell.execute("rm -rfd {0}".format(self.path))
        elif platform.system() == "Windows":
            meta.shell.execute("del /S /Q {0}".format(self.path))

    def copy(self, dest_path):
        """Makes and returns a copy of this folder at the designated location."""
        pass


class File(_FileUnit):
    """A file unit that contains data."""

    def delete(self):
        """Removes this file from the file system."""

        logging.info("Requested removal of file '%s'", self.path)

        cmd_word = ""
        # determine command based on OS
        if platform.system() == "Linux":
            cmd_word = "rm"
        elif platform.system() == "Windows":
            cmd_word = "del"

        # execute the command
        meta.shell.execute("{0} {1}".format(cmd_word, self.path))

    def copy(self, dest_path):
        """Makes and returns a copy of this file at the designated location."""
        pass
