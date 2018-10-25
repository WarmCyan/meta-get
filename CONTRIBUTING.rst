========================
Contributing to Meta-Get
========================

I personally believe that a tool such as this one has the potential to be very 
useful, and ideally to more people than just me. My goal is for Meta-Get to NOT 
be 'Nathan's esoteric package manager', and instead end up as a utility that at 
least *some* other developers actually genuinely find useful. To this end, this 
is an open source project, and I welcome other people to help contribute to the 
project's development and design!

I've never really run a project where my goal is to get other people 
contributing, so please bear with me as I figure out how best to handle things.

If anyone has any questions, suggestions, or comments, you're free to shoot me 
an email at nathanamartindale@gmail.com.

Development Setup
-----------------

To get an environment set up, fork this repository, clone it to your machine,
and run ``pip install -r requirements.txt`` to get all of the relevant packages
used for development.

Conventions
-----------

Conventions are important for maintaining cleanliness and organization in a 
project! For me personally, this is the first project where I'm trying to stress 
sticking to conventions.

Code Formatting
~~~~~~~~~~~~~~~

I personally use `pylint <https://www.pylint.org/>`_ and `black 
<https://github.com/ambv/black>`_. You can use both of these by running ``make 
lint`` and ``make fix`` respectively in the project root directory.  

Any new files added should maintain an appropriate header, ex::

    # meta.shell.py

    # Copyright (C) 2018 Nathan Martindale <nathanamartindale@gmail.com>
    # Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

Tests
~~~~~

The testing suite uses ``pytest``, please include tests with any new things you
add in pull requests! The testing suite can be run with ``make tests``.

Documentation
~~~~~~~~~~~~~

A minimum amount of documentation is needed for everything in order to appease
the mighty linters: docstrings for the files, classes, and functions. For the 
API itself, please give more verbose RST style documentation (examples can be
found in the sample ``meta.helloworld`` class.)

Sphinx is used as the documentation generator, and the current documentation can
be generated with ``make docs``.

Git Commits
~~~~~~~~~~~

I have come to appreciate nicely formatted git commit messages! The format I'm 
using is described `here <https://chris.beams.io/posts/git-commit/>`_.

Ideas of Things To Contribute
-----------------------------

I'm keeping a pseudo kanban board for this project over on `trello 
<https://trello.com/b/G42dO29h>`_. Any of the cards in the upcoming version 
lists without an avatar is something no one is working on yet. If you would like
to become more involved, email me, and I can add you to the trello board.
