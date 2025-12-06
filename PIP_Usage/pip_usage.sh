#!/bin/bash

# PIP stands for "Pip installs packages, and it's nothing but a package manager for Python.
# It can be used to install third-party libraries from the Python Package Index (also known
# as PyPI).

TARGET_PKG="requests"
REQS_FILE="requirements.txt"

# Install a package.
pip install ${TARGET_PKG}

# Update to its latest version.
pip install --upgrade ${TARGET_PKG}

# Displays package details.
pip show ${TARGET_PKG}

# Lists all installed packages.
pip list

# # Removes a package.
# pip uninstall ${TARGET_PKG}

# Lists dependencies needed to reproduce your environment.
pip freeze > ${REQS_FILE}

# # The file generated above can later by used by fellow environments by using the following
# # command:
# pip install -r ${REQS_FILE}

# pip freeze will only use == by default, but other operators can be used if writing the file
# manually:
# · != : excludes a version.
# · > :  greater than.
# · < :  less than.
# · >= : greater or equal than.
# · <= : less or equal than.
# · ~= : compatible release.
