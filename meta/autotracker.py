# meta.autotracker.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Core functionality for tracking meta package dependencies, files, and packages."""


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

    def load(self, database, package_name):
        """Load the autotracker information from the file for the given database and package
        name."""
