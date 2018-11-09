# meta.api.fileystem.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for managing files and folders."""

import logging
import platform
import os

import meta.shell

# NOTE: probably want to use shutil or os for some of these


# NOTE: maybe this becomes File, and Folder just inherits from File?
class _FileUnit:
    """A parent class for Folder and File that contains common logic."""

    def __init__(self, path):
        self.name = ""
        self.path = path

    def move(self, dest_path):
        """Moves the file unit to the passed location.

        :param str dest_path: The destination path to move this file unit to.
        """

        logging.info("Requested move of fileunit '%s' to '%s'", self.path, dest_path)

        # determine command based on OS
        cmd_word = ""
        if platform.system() == "Linux":
            cmd_word = "mv"
        elif platform.system() == "Windows":
            cmd_word = "move"

        # resolve if a relative path
        resolved_path = os.path.abspath(dest_path)
        logging.debug("Path '%s' resolved to '%s'", dest_path, resolved_path)

        # execute the movement shell command
        meta.shell.execute("{0} {1} {2}".format(cmd_word, self.path, resolved_path))


class Folder(_FileUnit):
    """A file unit that contains other folders and files."""

    def __init__(self, path):
        super().__init__(path)
        self.contents = {}

    def delete(self):
        """Removes this folder from the file system."""
        pass

    def copy(self, dest_path):
        """Makes and returns a copy of this folder at the designated location."""
        pass


class File(_FileUnit):
    """A file unit that contains data."""

    def delete(self):
        """Removes this folder from the file system."""
        pass

    def copy(self, dest_path):
        """Makes and returns a copy of this file at the designated location."""
        pass
