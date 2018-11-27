# Tada!: auTomAtic orDer-of-growth Analysis

[![Build Status](https://api.travis-ci.org/gkapfham/tada.svg?branch=master)](https://travis-ci.org/gkapfham/tada) [![codecov.io](http://codecov.io/github/gkapfham/tada/coverage.svg?branch=master)](http://codecov.io/github/gkapfham/tada?branch=master) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

This repository contains the source code and usage instructions for a tool
called "Tada: auTomAtic orDer-of-growth Analysis" that is implemented in the
Python 3 language. The tool systematically runs a doubling experiment to
ascertain the likely worst-case order-of-growth function for an arbitrary Python
function. This documentation provides a brief overview about how to run the tool, its provided test suite, and more.

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

- `tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE --function FUNCTION [--types TYPES [TYPES ...]]`

You can learn about GatorGrader's checks and defaults by typing python3
`tada_a_bigoh.py -h` in your terminal window and then reviewing the following
output.

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

When completed, Tada will be used to estimate the worst-case time complexity for
Python functions.

Here is an example of Tada being used in conjunction with functions in the
[Speed-Surprises repository](https://github.com/gkapfham/speed-surprises).

```
$ python3 tada_a_bigoh.py --directory /Users/~/speed-surprises/ --module speedsurprises.numbers.factorial --function compute_factorial --types int

🎆  Tada!: auTomAtic orDer-of-growth Analysis! 🎆
    https://github.com/gkapfham/tada
❓  For Help Information Type: python3 tada_a_bigoh.py -h  ❓

Start running experiment for size 100 →

.....................
tada_speedsurprisesnumbersfactorial_computefactorial_100: Mean +- std dev: 24.3 us +- 1.1 us

Mean 2.4285669765218098e-05
Median 2.381323712158203e-05

→ Done running experiment for size 100

Start running experiment for size 200 →

.....................
tada_speedsurprisesnumbersfactorial_computefactorial_200: Mean +- std dev: 60.3 us +- 5.9 us

Mean 6.0340462410481774e-05
Median 5.978153637695312e-05

→ Done running experiment for size 200
```

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
