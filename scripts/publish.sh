#!/usr/bin/env bash

set -e

# Update project version with the tag version
version=$(git describe --tags --abbrev=0)
poetry version "${version}"

# https://python-poetry.org/docs/libraries/
# https://python-poetry.org/docs/cli/#publish
poetry publish  --build
