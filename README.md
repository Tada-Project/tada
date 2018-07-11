# Tada!: auTomAtic orDer-of-growth Analysis

[![Build Status](https://api.travis-ci.org/gkapfham/tada.svg?branch=master)](https://travis-ci.org/gkapfham/tada) [![codecov.io](http://codecov.io/github/gkapfham/tada/coverage.svg?branch=master)](http://codecov.io/github/gkapfham/tada?branch=master)

This repository contains a tool called "Tada: auTomAtic orDer-of-growth
Analysis" that is implemented in Python 3. This tool systematically runs a
doubling experiment to ascertain the likely worst-case time complexity class for
a Python function. This documentation provides a brief overview about how to run
the provided test suite in different configurations.

## Installing and Testing Tada

This program uses [Pipenv](https://github.com/pypa/pipenv) for installation.
Once you have installed `pipenv` you can run the test suite for the provided
modules and functions by typing the following in your terminal window:

- `pipenv install`
- `pipenv shell`
- `pipenv run pytest`

If you want to collect the coverage of the provided test suite, you can run:

- `pipenv run pytest --cov-config pytest.cov --cov`

## Adding New Features to Tada

You can follow these steps to add a new feature if you are already collaborator
on the project. If you want to add a new feature, please ensure that it is
accompanied by high coverage test cases and that you do not break any of the
existing test cases or features. First, you should type the following command,
substituting the name of your feature for the word `featurename`.

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

If you have any problems with installing or using the test suite provided for
this tool, then please create an issue associated with this Git repository using
the "Issues" link at the top of this site. The contributors to Tada will do all
that they can to resolve your issue and ensure that all of the features and the
test suite work well in your development environment.
