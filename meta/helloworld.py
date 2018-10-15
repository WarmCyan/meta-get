# meta.helloworld.py

# Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""A testing/sample class for the project.

Intended for examples of proper testing and documentation."""


class HelloWorld:
    """A class that holds a number to add to a sum,
    and can give you a personalized greeting.

    :param constant: A number that will be added when doing math
    :type constant: int, float

    .. note::
        This is an example note

    >>> print("This is some example code")
    "This is some example code"

    """

    def __init__(self, constant):
        self.extra_math_constant = constant
        self.result = 0
        self.greeting = ""

    def set_string_thing(self, name):
        """Returns a greeting directed at the person calling it."""
        self.greeting = "Hello there, {0}! The class constant is {1}".format(
            name, self.extra_math_constant
        )

    def do_the_maths(self, num1, num2):
        """Should set the class's result to the sum of the numbers
        and the extra class constant.

        :param int num1: The first number to add
        :param int num2: The second number to add
        """
        self.result = num1 + num2 + self.extra_math_constant
