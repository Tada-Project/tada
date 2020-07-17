#!/usr/bin/env bash

# install pipenv
pip install pipenv
# install all dev dependencies (including mkdocs)
pipenv install --dev
# build mkdocs site
mkdocs build
