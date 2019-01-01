###
API
###

This module contains pre-defined functionality that can be utilized inside of
meta-package setup scripts.

Apt
###
.. automodule:: meta.api.pkg_managers.apt
.. autofunction:: install
.. autofunction:: uninstall

Autotracker
###########
.. automodule:: meta.api.autotracker
.. autofunction:: suppress

Filesystem
##########
.. automodule:: meta.api.filesystem

.. autofunction:: create_folder
.. autofunction:: create_file

Folder
======
.. autoclass:: Folder
    :members:
    :inherited-members:

File
====
.. autoclass:: File
    :members:
    :inherited-members:

Pacman
######
.. automodule:: meta.api.pkg_managers.pacman
.. autofunction:: install
.. autofunction:: uninstall

Pip
###
.. automodule:: meta.api.pkg_managers.pip
.. autofunction:: install
.. autofunction:: uninstall

Shell
#####
.. automodule:: meta.api.shell
.. autofunction:: execute

