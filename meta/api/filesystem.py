# meta.api.fileystem.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for managing files and folders."""

# NOTE: probably want to use shutil or os for some of these


# NOTE: maybe this becomes File, and Folder just inherits from File?
class _FileUnit:
    """A parent class for Folder and File that contains common logic."""

    def __init__(self, path):
        self.name = ""
        self.path = path

    def move(self, dest_path):
        """Moves the file unit to the passed location."""
        pass


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
