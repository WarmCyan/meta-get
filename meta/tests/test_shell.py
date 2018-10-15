# meta.tests.test_shell.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the core interface to the OS's shell is functional."""

import os
import subprocess
import tempfile

# import unittest.mock
import pytest
import testfixtures
import testfixtures.popen
from pytest_mock import mocker

import meta.shell

# pylint:disable=redefined-outer-name


#   Tests
# --------------------------------------


def test_valid_execute_return(mocker):
    # setup
    popen = testfixtures.popen.MockPopen()
    popen.set_command("testing", stdout=b"yep", stderr=b"nope", returncode=0)

    replacer = testfixtures.Replacer()
    replacer.replace("subprocess.Popen", popen)

    testfixtures.compare(meta.shell.execute("testing"), "yep")

    replacer.restore()
