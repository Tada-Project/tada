#!/usr/bin/env bash

# force pipenv to create its own new virtualenv
export PIPENV_IGNORE_VIRTUALENVS=1;
# install pipenv
pip install pipenv
# install all dev dependencies (including mkdocs)
pipenv install --dev
# build mkdocs site
mkdocs build
