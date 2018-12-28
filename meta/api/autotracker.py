# meta.api.autotracker.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for interacting with the autotracker."""

from meta import config

# NOTE: this will end up setting a flag somewhere in a global settings array that the cli will be
# using
def suppress():
    """Stops the autotracker from running on removal/installation of a meta package."""
    config.AUTOTRACKER_ENABLED = False
