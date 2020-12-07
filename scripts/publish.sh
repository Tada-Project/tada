#!/usr/bin/env bash

set -e

version=$(git describe --tags --abbrev=0)
poetry version "${version}"

# https://python-poetry.org/docs/libraries/
# https://python-poetry.org/docs/cli/#publish
poetry publish  --build
