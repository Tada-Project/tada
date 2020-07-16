#!/usr/bin/env bash

# set -x

# cd /tmp
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# python get-pip.py --user

# cd -

# python -m pip install --user mkdocs
# python -m mkdocs build
# brew install pyenv
# pyenv install 3.7
# pipenv install --dev
# pipenv --python 3.7
# export PIPENV_IGNORE_VIRTUALENVS=1


# pip install pipenv
# pipenv install mkdocs
# pipenv run mkdocs build


set -x
set -e
# Install pip
cd /tmp
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.6 get-pip.py --user
cd -

python3.6 -m pip install --user mkdocs

python3.6 -m mkdocs build
