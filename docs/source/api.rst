###
API
###

This module contains pre-defined functionality that can be utilized inside of
meta-package setup scripts.

filesystem
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

pip
###
.. automodule:: meta.api.pkg_managers.pip
.. autofunction:: install
.. autofunction:: uninstall
.. autofunction:: execute

shell
#####
.. automodule:: meta.api.shell
.. autofunction:: execute

