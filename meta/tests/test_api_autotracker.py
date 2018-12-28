# meta.tests.test_api_autotracker.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the interactions with the autotracker work as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-import
# pylint:disable=unused-argument

import meta.config
from meta.api import autotracker

def test_suppress_disables_autotracker():
    autotracker.suppress()
    assert meta.config.AUTOTRACKER_ENABLED == False
