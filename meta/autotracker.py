# meta.autotracker.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Core functionality for tracking meta package dependencies, files, and packages."""

import json
import logging

from meta.exceptions import InvalidAutotrackerFile


class Autotracker:
    """A class that contains all autotracker information for a specific package."""

    def __init__(self):
        self.database = ""
        self.package_name = ""

        self.files = []
        self.packages = []
        self.dependencies = []

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

        # TODO: individual file for each meta package, need to figure out where these would be
        # stored
        filename = "autotracker.json"
        with open(filename, "w") as autotracker_file:
            json.dump(autotracker_info, autotracker_file)

    def load(self, database, package_name):
        """Load the autotracker information from the file for the given database and package
        name."""

        logging.info(
            "Loading autotracker information for %s:%s", database, package_name
        )

        self.database = database
        self.package_name = package_name

        # TODO: individual file for each meta package, need to figure out where these would be
        # stored
        filename = "autotracker.json"
        with open(filename) as autotracker_file:
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
