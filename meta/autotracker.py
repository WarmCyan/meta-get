# meta.autotracker.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Core functionality for tracking meta package dependencies, files, and packages."""

import json
import logging

from meta import config
from meta.exceptions import InvalidAutotrackerFile


class Autotracker:
    """A class that contains all autotracker information for a specific package."""

    def __init__(self):
        #: The name of the package database of the meta package this autotracker tracks.
        self.database = ""

        #: The name of the meta package that this autotracker tracks.
        self.package_name = ""

        #: The array of filepaths that are associated with the installation of this meta package.
        self.files = []

        #: The dictionary of package information for each package that this meta package installed.
        self.packages = []

        #: The array of other meta packages that this meta package installs as dependencies
        self.dependencies = []

    def change_filepath(self, old_path, new_path):
        """Change the given path in the autotracker's file list to a new given path."""
        for i in range(0, len(self.files)):
            if self.files[i] == old_path:
                self.files[i] = new_path

    def check_file(self, path):
        """Check if the given file is in the autotracker's file list."""
        if path in self.files:
            return True
        return False

    def check_package(self, package_manager, package_name):
        """Check if the given package is in the autotracker's package list."""
        for package in self.packages:
            if (
                package["pkg_manager"] == package_manager
                and package["name"] == package_name
            ):
                return True
        return False

    def check_dependency(self, package_name):
        """Check if the given meta package is in the autotracker's dependency list."""
        if package_name in self.dependencies:
            return True
        return False

    def save(self):
        """Save the autotracker information to a file based on database and package name."""
        logging.info(
            "Saving autotracker information for %s:%s", self.database, self.package_name
        )

        autotracker_info = {
            "files": self.files,
            "packages": self.packages,
            "dependencies": self.dependencies,
        }

        # NOTE: path might still need to be expanded?
        filename = "{0}_{1}.json".format(self.database, self.package_name)
        filepath = config.AUTOTRACKER_DIR + filename
        with open(filepath, "w") as autotracker_file:
            json.dump(autotracker_info, autotracker_file)

    def load(self, database, package_name):
        """Load the autotracker information from the file for the given database and package
        name."""
        logging.info(
            "Loading autotracker information for %s:%s", database, package_name
        )

        self.database = database
        self.package_name = package_name

        # NOTE: path might still need to be expanded?
        filename = "{0}_{1}.json".format(self.database, self.package_name)
        filepath = config.AUTOTRACKER_DIR + filename
        with open(filepath) as autotracker_file:
            autotracker_info = json.load(autotracker_file)

            # check for valid autotracker file
            if "files" not in autotracker_info:
                logging.error("No 'files' array found in autotracker file")
                raise InvalidAutotrackerFile
            elif "packages" not in autotracker_info:
                logging.error("No 'packages' array found in autotracker file")
                raise InvalidAutotrackerFile
            elif "dependencies" not in autotracker_info:
                logging.error("No 'dependencies' array found in autotracker file")
                raise InvalidAutotrackerFile

            self.files = autotracker_info["files"]
            self.packages = autotracker_info["packages"]
            self.dependencies = autotracker_info["dependencies"]
