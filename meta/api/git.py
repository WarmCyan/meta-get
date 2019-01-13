# meta.api.git.py

# Copyright (C) 2019 Nathan Martindale <nathanamartindale@gmail.com>
# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""API for interacting with git repositories."""

import logging

from meta.api.filesystem import Folder
import meta.current
import meta.shell


def clone(url, destination=None, silent=False):
    """Clones the desired github repo locally."""

    logging.info("Git API requested to clone %s", url)

    # figure out what the result folder would be based on url
    # (in other words, just get the repo name)
    stripped_url = url
    if url[-4:] == ".git":
        stripped_url = url[:-4]
    name = stripped_url[stripped_url.rfind("/") + 1 :]

    # determine where to clone the repo
    dest_path = meta.current.REPO_DIR + "/" + name
    if destination is not None:
        dest_path = destination
        name = destination[destination.rfind("/") + 1 :]

    logging.info("Git API cloning into %s", destination)

    meta.shell.execute("git clone {0} {1}".format(url, dest_path), silent=silent)
    local_repo = Folder(dest_path)

    # add to autotracker
    meta.current.PACKAGE_AUTOTRACKER.files.append(local_repo.path)

    return local_repo
