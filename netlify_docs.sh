#!/usr/bin/env bash
pip install --upgrade pip
pip install pipenv
pipenv install --dev
pipenv run mkdocs build
