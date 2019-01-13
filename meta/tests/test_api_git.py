# meta.tests.test_api_git.py

# Copyright (C) 2019 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the git API is working as intended."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-argument

import os

import meta.api.git
import meta.current


def test_clone_cmd_default(shell_mock, common_autotracker, listdir_blank_mock):
    """Ensure the correct command is used for cloning a repo to the default location."""
    repo = "https://github.com/WildfireXIII/test.git"
    folder = meta.api.git.clone(repo)
    shell_mock.assert_called_with(
        "git clone {0} {1}/test".format(repo, meta.current.REPO_DIR), silent=False
    )
    assert folder.path == os.path.expanduser(meta.current.REPO_DIR + "/test")
    assert meta.current.PACKAGE_AUTOTRACKER.check_file(folder.path)


def test_clone_cmd_dest(shell_mock, common_autotracker, listdir_blank_mock):
    """Ensure the correct command is used for cloning a repo to a specified location."""
    repo = "https://github.com/WildfireXIII/test.git"
    folder = meta.api.git.clone(repo, destination="~/testing")
    dest_path = os.path.expanduser("~/testing")
    shell_mock.assert_called_with("git clone {0} {1}".format(repo, dest_path), silent=False)
    assert folder.path == os.path.expanduser("~/testing")
    assert meta.current.PACKAGE_AUTOTRACKER.check_file(folder.path)
