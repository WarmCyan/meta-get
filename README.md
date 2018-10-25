# Meta-Get 

[![Build Status](https://travis-ci.org/WildfireXIII/meta-get.svg?branch=master)](https://travis-ci.org/WildfireXIII/meta-get)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

If you work on multiple machines/environments, it’s likely that at some point or 
another, you’ve wanted those environments to be similar or to have all your usual 
applications, plugins, and config files quickly installed and synced. The goal of 
meta-get is to act as a sort of meta package manager that can aid you in getting 
these standardized aspects set up in your environments - to allow you to create 
and list your own collections of files, libraries, or applications that you want 
selectively set up on all of your systems with a minimum amount of hassle and 
regardless of what architecture or OS you’re running on. In addition, the goal 
is to allow configuration or setup changes made on one system to be easily 
propagated to any other systems you use.

## Status

This project is still in early development and is not yet in a usable state.

## Basic Features (eventually)

* Apt-like/pip-like commandline syntax (`meta install <packagename>`)
* Ability to define "meta packages" or sets of "installation instructions", 
hosted in a git repository, with a predefined python API containing functions
that allow you to:
	* Clone git repositories
	* Move files/folders around
	* Remove files/folders
	* Download files from URLs
	* Extract archives
	* Interact with a set of known/common package managers (apt-get, pacman,
	chocolatey, pip, etc.)
	* Execute shell scripts/commands
* Optionally automatically remove a meta package's installed files and packages,
instead of (or in addition to) having to manually remove them
* Ability to draw from multiple sets (repositories) of meta-packages
* Commands to quickly open/edit a meta-package and sync it with its git
repository
* Configurable via commandline flags or .config files

## Contributing

I want this project to be a tool that more people than just me find useful! I
welcome anyone who's interested in contributing to help with either design
and/or development. More information can be found in the [contributing
doc](https://github.com/WildfireXIII/meta-get/blob/master/CONTRIBUTING.rst).

## Links

[Github repo](https://github.com/WildfireXIII/meta-get)  
[Trello board](https://trello.com/b/G42dO29h)  
[Design doc](https://docs.google.com/document/d/1F8nmGumkkPaMFxNUKbDfSeaOZaNSd6m-kj-Yj7I-QT8)
