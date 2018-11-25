# Tada!: auTomAtic orDer-of-growth Analysis

[![Build Status](https://api.travis-ci.org/gkapfham/tada.svg?branch=master)](https://travis-ci.org/gkapfham/tada) [![codecov.io](http://codecov.io/github/gkapfham/tada/coverage.svg?branch=master)](http://codecov.io/github/gkapfham/tada?branch=master) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

This repository contains the source code and usage instructions for a tool
called "Tada: auTomAtic orDer-of-growth Analysis" that is implemented in the
Python 3 language. The tool systematically runs a doubling experiment to
ascertain the likely worst-case order-of-growth function for an arbitrary Python
function. This documentation provides a brief overview about how to run the tool
and its provided test suite.

## Installing and Testing Tada

This program uses [Pipenv](https://github.com/pypa/pipenv) for installation.
Once you have installed `pipenv` you can run the test suite for Tada's functions
by typing the following in your terminal window:

- `pipenv install`
- `pipenv shell`
- `pipenv run pytest`

If you want to collect the coverage of the provided test suite, then you can
run:

- `pipenv run pytest --cov-config pytest.cov --cov`

If you want to collect the coverage of the provided test suite and see what
lines of code are not covered, then you can run:

- `pytest --cov-config pytest.cov --cov --cov-report term-missing`

## Using Tada

Since the Tada tool is currently under heavy development, it is not yet feature
complete. In the future, its documentation will feature examples of how to run
the tool to automatically suggest the likely worst-case order-of-growth function
for a provided Python function.

If you want to run the tool, then you can run:

- `tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE --function
                       FUNCTION [--types TYPES [TYPES ...]]`

You can learn about GatorGrader's checks and defaults by typing python3 `tada_a_bigoh.py -h` in your terminal window and then reviewing the following output.

```
usage: tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE --function
                       FUNCTION [--types TYPES [TYPES ...]]

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY
                        Package directory with functions to analyze (default:
                        None)
  --module MODULE       Module name with functions to analyze (default: None)
  --function FUNCTION   Name of the module's function to analyze (default:
                        None)
  --types TYPES [TYPES ...]
                        Parameter types for function to analyze (default: [])
```

## Tada in Action


## Adding New Features to Tada

You can follow these steps to add a new feature if you are already a
collaborator on the project. If you want to add a new feature, please ensure
that it is accompanied by high coverage test cases and that you do not break any
of the existing test cases or features. First, you should type the following
command, substituting the name of your feature for the word `featurename`.

- `git checkout -b new-featurename`
- `git checkout master`
- `git push -u origin new-featurename`

Finally, you should open a pull request on the GitHub repository for the new
branch that you have created. This pull request should describe the new feature
that you are adding and give examples of how to run it on the command line. Of
course, if you are not a collaborator on this project, then you will need to
fork the repository, add your new feature, document and test it as appropriate,
and then create a pull request.

## Problems or Praise

If you have any problems with installing or using the Tada or its provided test
suite, then please create an issue associated with this Git repository using the
"Issues" link at the top of this site. The contributors to Tada will do all that
they can to resolve your issue and ensure that all of its features and the test
suite work well in your development environment.
