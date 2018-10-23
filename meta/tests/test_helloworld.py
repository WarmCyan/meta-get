# meta.tests.test_helloworld.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""A sample testing set for the helloworld class."""

# pylint:disable=redefined-outer-name

import pytest

from meta.helloworld import HelloWorld


# --------------------------------------
#   Fixtures
# --------------------------------------


@pytest.fixture
def sample_world():
    """Returns a basic HelloWorld object with a constant of 13."""
    return HelloWorld(13)


# --------------------------------------
#   Tests
# --------------------------------------


def test_constant(sample_world):
    """Does the class contain the constant value we gave it?"""
    assert sample_world.extra_math_constant == 13


def test_initial_result(sample_world):
    """Is result 0 by default?"""
    assert sample_world.result == 0


def test_initial_greeting(sample_world):
    """Is the greeting blank by default?"""
    assert sample_world.greeting == ""


@pytest.mark.parametrize(
    "num1, num2, expected",
    [(5, 5, 23), (0, 0, 13), (0, 5, 18), (5, 0, 18), (-5, -5, 3)],
)
def test_maths(sample_world, num1, num2, expected):
    """Does summation still work the way I think it does?"""
    sample_world.do_the_maths(num1, num2)
    assert sample_world.result == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Nathan", "Hello there, Nathan! The class constant is 13"),
        ("", "Hello there, ! The class constant is 13"),
    ],
)
def test_string_thing(sample_world, name, expected):
    """Does the greeting get set the way we expect it to?"""
    sample_world.set_string_thing(name)
    assert sample_world.greeting == expected
