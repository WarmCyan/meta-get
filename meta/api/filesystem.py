# meta.api.fileystem.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for managing files and folders."""

import logging
import os
import platform

import meta.shell
from meta.exceptions import RelativePathUnwise

# NOTE: probably want to use shutil or os for some of these

# NOTE: all self.paths are ASSUMED to exist, so no fancy manual path resolution will be necessary

# NOTE: should path be the path WITHOUT the name? (at least for files?)

# NOTE: maybe this becomes File, and Folder just inherits from File?
class _FileUnit:
    """A parent class for Folder and File that contains common logic."""

    def __init__(self, path):
        self.path = os.path.abspath(os.path.expanduser(os.path.expandvars(path)))
        self.name = os.path.basename(self.path)

    def move(self, dest_path):
        """Moves the file to the passed location.

        :param str dest_path: The destination path to move this file to
        """

        logging.info("Requested move of file '%s' to '%s'", self.path, dest_path)

        # determine command based on OS
        cmd = ""
        if platform.system() == "Linux":
            cmd = "mv"
        elif platform.system() == "Windows":
            cmd = "move"

        # resolve if a relative path
        resolved_path = self.resolve_path(dest_path)

        # execute the movement shell command
        meta.shell.execute("{0} {1} {2}".format(cmd, self.path, resolved_path))

    def resolve_path(self, unresolved_path):
        """Handles fixing any relative paths.

        (all ./ and ../ will be based off of this file's directory, rather than the actual "cwd")

        :param str unresolved_path: The path to be resolved
        """

        resolved = ""
        with os.chdir(self.path):
            resolved = os.path.abspath(
                os.path.expanduser(os.path.expandvars(unresolved_path))
            )

        logging.debug("Resolving path '%s' to '%s'", unresolved_path, resolved)
        return resolved


class Folder(_FileUnit):
    """A file unit that contains other folders and files."""

    def __init__(self, path):
        super().__init__(path)
        self.contents = {}

        # get all of the files and subfolders within this folder
        for subpath in os.listdir(path):
            if os.path.isdir(subpath):
                subfolder = Folder(subpath)
                self.contents[subfolder.name] = subfolder
            else:
                subfile = File(subpath)
                self.contents[subfile.name] = subfile

    def delete(self):
        """Removes this folder from the file system."""

        logging.info("Requested removal of folder '%s'", self.path)

        # determine command based on OS
        cmd = ""
        if platform.system() == "Linux":
            cmd = "rm -rfd"
        elif platform.system() == "Windows":
            cmd = "del /S /Q"

        # execute the command
        meta.shell.execute("{0} {1}".format(cmd, self.path))

    def copy(self, dest_path):
        """Makes and returns a copy of this folder at the designated location.

        :param str dest_path: The destination path to copy this folder to
        :returns: a Folder pointing to the newly copied instance
        """

        logging.info("Request copy of folder '%s' at '%s'", self.path, dest_path)

        # resolve if a relative path
        resolved_path = self.resolve_path(dest_path)

        # determine command based on OS
        cmd = ""
        if platform.system() == "Linux":
            cmd = "cp -R"
        elif platform.system() == "Windows":
            cmd = "robocopy /copyall /e"

        # execute the command
        meta.shell.execute("{0} {1} {2}".format(cmd, self.path, resolved_path))

        # return an instance of the new copy
        new_copy = Folder(resolved_path)
        return new_copy


class File(_FileUnit):
    """A file unit that contains data."""

    def delete(self):
        """Removes this file from the file system."""

        logging.info("Requested removal of file '%s'", self.path)

        # determine command based on OS
        cmd = ""
        if platform.system() == "Linux":
            cmd = "rm"
        elif platform.system() == "Windows":
            cmd = "del"

        # execute the command
        meta.shell.execute("{0} {1}".format(cmd, self.path))

    def copy(self, dest_path):
        """Makes and returns a copy of this file at the designated location.

        :param str dest_path: The destination path to copy this file to
        :returns: a File pointing to the newly copied instance
        """

        logging.info("Request copy of file '%s' at '%s'", self.path, dest_path)

        # resolve if a relative path
        resolved_path = self.resolve_path(dest_path)

        # determine command based on OS
        cmd = ""
        if platform.system() == "Linux":
            cmd = "cp"
        elif platform.system() == "Windows":
            cmd = "copy"

        meta.shell.execute("{0} {1} {2}".format(cmd, self.path, resolved_path))

        # return an instance of the new copy
        new_copy = File(resolved_path)
        return new_copy


def create_folder(path, force=False):
    """Create the specified folder on the system and return a Folder instance of it."""

    logging.info("Requested new folder at '%s'", path)

    # ensure this isn't a relative path (unless user specified force)
    if path[0] != "/" and path[0] != "~" and path[0] != "%" and path[0] != "$":
        # pylint:disable=line-too-long
        if force:
            logging.warning(
                "Forcing creation of a relative folder '%s'. This is unwise as the resolved path of this will likely depend on where on your system you are running this command",
                str(path),
            )
        else:
            raise RelativePathUnwise("Relative path specified for folder creation. This is unwise as it can have inconsistent results depending on where the command is run."
            )
        # pylint:enable=line-too-long

    # determine command based on OS
    cmd = ""
    if platform.system() == "Linux":
        cmd = "mkdir"
    elif platform.system() == "Windows":
        cmd = "md"

    meta.shell.execute("{0} {1}".format(cmd, path))

    # make and return a Folder instance pointing to it
    new_folder = Folder(path)
    return new_folder
