# meta.tests.test_shell.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""Test set to ensure the core interface to the OS's shell is functional."""

# pylint:disable=redefined-outer-name
# pylint:disable=unused-import

import subprocess

import pytest
import testfixtures
import testfixtures.popen
from testfixtures.outputcapture import OutputCapture
from pytest_mock import mocker

import meta.exceptions
import meta.shell

# --------------------------------------
#   Fixtures
# --------------------------------------


@pytest.fixture
def popen_mock_command():
    """Fixture for adding a command with specified output and return to the popen mock."""
    replacer = testfixtures.Replacer()
    popen = testfixtures.popen.MockPopen()

    def add_command(cmd, stdout=b"", stderr=b"", returncode=0):
        popen.set_command(cmd, stdout, stderr, returncode)
        replacer.replace("subprocess.Popen", popen)
        # return popen

    yield add_command
    replacer.restore()


# --------------------------------------
#   Tests
# --------------------------------------


def test_execute_raises_unsupportedos(mocker):
    """Ensure that trying to run this on an unsupported OS raises an exception."""
    system_check_mock = mocker.patch("platform.system", autospec=True)
    system_check_mock.return_value = "Java"

    with pytest.raises(meta.exceptions.UnsupportedOS):
        meta.shell.execute("echo 'hi'")


def test_blank_execute_raises_emptycommand():
    """Ensure running a blank command raises an exception."""
    with pytest.raises(meta.exceptions.EmptyCommand):
        meta.shell.execute("")


def test_invalid_command_raises_exception(popen_mock_command):
    """Ensure that a bad command raises the subprocesses CalledProcessError."""
    popen_mock_command("test command", stdout=b"command output", returncode=1)

    with pytest.raises(subprocess.CalledProcessError):
        meta.shell.execute("test command")


def test_valid_execute_return(popen_mock_command):
    """Ensure whether the output returned from execute is the same as stdout."""
    popen_mock_command("test command", stdout=b"command output", returncode=0)

    testfixtures.compare(meta.shell.execute("test command"), "command output")


def test_valid_execute_output(popen_mock_command):
    """Ensure that command output gets written to stdout."""
    popen_mock_command("test command", stdout=b"command output", returncode=0)

    with OutputCapture() as output:
        meta.shell.execute("test command", silent=False)

    output.compare("command output")


def test_valid_execute_silent_output(popen_mock_command):
    """Ensure that a command run silently prints no output to stdout."""
    popen_mock_command("test command", stdout=b"command output", returncode=0)

    with OutputCapture() as output:
        meta.shell.execute("test command", silent=True)

    output.compare("")


def test_valid_execute_silent_output_default(popen_mock_command):
    """Ensure that a command prints no output to stdout by default."""
    popen_mock_command("test command", stdout=b"command output", returncode=0)

    with OutputCapture() as output:
        meta.shell.execute("test command")

    output.compare("")


def test_execute_output_with_nonewline(popen_mock_command):
    """Ensure that if no newline printed on the last line, it still displays.

    This is particularly important for programs, such as pacman, that might prompt for input."""
    popen_mock_command("test command", stdout=b"first line\nsecond line", returncode=0)

    with OutputCapture() as output:
        meta.shell.execute("test command", silent=False)

    output.compare("first line\nsecond line")


def test_execute_stderr_in_stdout(popen_mock_command):
    """Ensure that stderr is also printed out along with stdout.

    NOTE: unsure if this is a good practice/desired functionality or not.
    Some programs (such as pacman) output prompts and things to stderr, so
    those don't show up unless handled."""
    popen_mock_command(
        "test command",
        stdout=b"normal output\n",
        stderr=b"things happened",
        returncode=0,
    )

    with OutputCapture() as output:
        meta.shell.execute("test command", silent=False)

    output.compare("normal output\nthings happened")


def test_nonmocked_shell_execute():
    """Ensure that running an actual command on the actual shell works."""

    with OutputCapture() as output:
        meta.shell.execute('echo "hello world"', silent=False)

    output.compare("hello world")
