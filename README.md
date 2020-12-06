# Tada!: auTomAtic orDer-of-growth Analysis

[![Build Status](https://api.travis-ci.org/Tada-Project/tada.svg?branch=master)](https://travis-ci.org/Tada-Project/tada) [![codecov.io](https://codecov.io/github/Tada-Project/tada/coverage.svg?branch=master)](http://codecov.io/github/Tada-Project/tada?branch=master) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

Tada is a tool that systematically runs a doubling experiment to ascertain the
likely worst-case order-of-growth function for an arbitrary Python function.
This documentation provides a brief overview about how to run the tool, its
provided test suite, and more.

**Documentation**: https://tada-predict.netlify.app

## Install Tada

- Operating system: Linux · macOS/OS X · Windows
- Python version: Python 3.6+
- Dependency Management: [Pipenv](https://github.com/pypa/pipenv) · [Poetry](https://github.com/python-poetry/poetry)

### Install Tada with pip

Install Tada with [pip](https://pip.pypa.io/en/stable/):

```shell
pip install tada-predict
```

### Install through Github Repo

Alternatively, you can also install Tada manually by cloning the repository and
installing the dependencies through either [Pipenv](https://github.com/pypa/pipenv)
or [Poetry](https://github.com/python-poetry/poetry). This is also the common
way if you want to make changes to the code base.

First, you can clone this repository with the following command:

```shell
git clone git@github.com:Tada-Project/tada.git
```

#### Poetry

If you would like to install dependencies through `poetry`, you would first need
to install `poetry` on your local machine like this:

```shell
pip install poetry
```

Once you have installed `poetry`, you can then install the dependencies for
Tada with the following command.

```shell
poetry install
```

You can also activate the `poetry` shell by running this command:

```shell
poetry shell
```

#### Pipenv

Similarly, you can run the following command to install `pipenv` on your local
machine:

```shell
pip install pipenv
```

To install dependencies with `pipenv`, you can just run:

```shell
pipenv install --no-dev
```

You can activate the `pipenv` shell with this command:

```shell
pipenv shell
```

### Run Command

To run Tada, you can just type the following command with the arguments into the
terminal window within your preferred virtual environment:

```shell
tada [-h] --directory DIRECTORY --module MODULE --function FUNCTION --types TYPES [TYPES ...]
```

You can learn about Tada's checks and defaults by typing `tada -h` in your
terminal window and then reviewing the following output.

```shell
usage: tada [-h] --directory DIRECTORY [DIRECTORY ...]
            --module [MODULE [MODULE ...]
            --function FUNCTION [FUNCTION ...]
            --types TYPES [TYPES ...]
            [--data_directory DATA_DIRECTORY]
            [--data_module DATA_MODULE]
            [--data_function DATA_FUNCTION] [--schema SCHEMA]
            [--startsize STARTSIZE] [--steps STEPS]
            [--runningtime RUNNINGTIME] [--expect EXPECT]
            [--backfill] [--indicator INDICATOR]
            [--maxsize MAXSIZE] [--sorted] [--log] [--md]
            [--contrast] [--level LEVEL]
            [--position] POSITION [POSITION ...]]

optional arguments:
  -h, --help
        show this help message and exit
  --directory DIRECTORY [DIRECTORY ...]
        Path to the package directory with functions to
        analyze (default: None)
  --module MODULE [MODULE ...]
        Module name with functions to analyze (default: None)
  --function FUNCTION [FUNCTION ...]
        Name of the function to analyze (default: None)
  --types TYPES [TYPES ...]
        Data generation type: hypothesis or parameter types
        of the function (default: None)
  --data_directory DATA_DIRECTORY
        Path to the package directory with function to
        generate data (default: None)
  --data_module DATA_MODULE
        Module name with functions to generate data
        (default: None)
  --data_function DATA_FUNCTION
        Name of the data generation function (default: None)
  --schema SCHEMA
        The path to the JSON schema that describes the data
        format (default: None)
  --startsize STARTSIZE
        Starting size of the doubling experiment (default: 1)
  --steps STEPS
        Maximum rounds of the doubling experiment
        (default: 10)
  --runningtime RUNNINGTIME
        Maximum running time of the doubling experiment
        (default: 200)
  --expect EXPECT
        Expected Growth Ratio: O(1) | O(logn) | O(n) |
        O(nlogn) | O(n^2) | O(n^3) | O(c^n). By using this
        argument, the experiment result will be stored in a
        csv file (default: None)
  --backfill
        Enable backfill to shrink experiments size according
        to the Predicted True Value (default: False)
  --indicator INDICATOR
        Indicator value (default: 0.1)
  --maxsize MAXSIZE
        Maximum size of the doubling experiment
        (default: 1500)
  --sorted
        Enable input data to be sorted (default: False)
  --log
        Show log/debug/diagnostic output (default: False)
  --md
        Show results table in markdown format (default: False)
  --contrast
        Show contrast result table. Only works with multiple
        experiments (default: False)
  --viz
        Visualize a simple graph for the result
        (default: False)
  --level LEVEL
        The level of nested data structure to apply doubling
        experiment (default: 1)
  --position POSITION [POSITION ...]
        The position of input data to double in the
        multivariable doubling experiment. Must be the last
        argument (default: [0])

Sample usage:
  tada --directory /path/to/project_directory
       --module module_name.file_name --function function_name
       --types hypothesis
```

#### Running within Tada Repo

If you are running within the Tada repository, then you could also easily run
Tada within the shell activated by the dependency management tool you previously
installed like this:

```shell
python tada/tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE \
      --function FUNCTION --types TYPES [TYPES ...]
```

It is worth noting that when the provided experiment function is relied on an
external Python library, it is likely that Tada might not have this dependency,
and thus, it might cause an error when running the experiment. You can simply
resolve this issue by installing the required dependencies through your chosen
dependency management tool like this:

- With `pipenv`: `pipenv install <library-name>`
- With `poetry`: `poetry add <library-name>`

## Quick Start Example

We have provided some code examples in [Speed-Surprises](https://github.com/Tada-Project/speed-surprises)
for you to run Tada in conjunction and experience how Tada automatically suggests
the likely worst-case order-of-growth function for various types of Python function.
You can follow the instructions in [Speed-Surprises](https://github.com/Tada-Project/speed-surprises)
to clone the repository and install the dependencies.

After successfully setting up the repository on your local machine, you can
then run the following command to conduct an experiment for `insertion_sort`
within the `speed-surprises` repository:

```shell
tada --directory . --module speedsurprises.lists.sorting \
     --function insertion_sort --types hypothesis \
     --schema speedsurprises/jsonschema/single_int_list.json
```

Within a minute or so, you will be able to inspect an output similar to the
following with a results table provided at the end of the experiment.

```shell
        Tada!: auTomAtic orDer-of-growth Analysis!
          https://github.com/Tada-Project/tada/
        For Help Information Type: python tada -h

Start running experiment insertion_sort for size 1 →


→ Done running experiment insertion_sort for size 1
.
.
.
→ Done running experiment insertion_sort for size 64

+-----------------------------------------------------------------------------+
|             insertion_sort: O(n) linear or O(nlogn) linearithmic            |
+------+------------------------+------------------------+--------------------+
| Size |          Mean          |         Median         |       Ratio        |
+------+------------------------+------------------------+--------------------+
|  1   | 4.882118635177613e-07  | 4.6806960487365676e-07 |         0          |
|  2   | 7.456634746551513e-07  | 7.133920059204101e-07  | 1.527335835885569  |
|  4   |  9.27755012257894e-07  | 9.209306488037112e-07  | 1.2442006934655812 |
|  8   | 1.3545460286458332e-06 | 1.3353490028381343e-06 | 1.4600255571233727 |
|  16  | 2.2379635269165037e-06 | 2.2146971740722657e-06 | 1.6521871384125948 |
|  32  | 3.9610248652140306e-06 | 3.913619827270508e-06  | 1.7699237800678478 |
|  64  | 7.2769234293619794e-06 | 7.211799896240237e-06  | 1.837131468996415  |
+------+------------------------+------------------------+--------------------+
O(n) linear or O(nlogn) linearithmic
```

You can find more information about Tada usage, including experiment data
generation and using different flags and arguments to configure your Tada
experiment through our [documentation](https://tada-predict.netlify.app/using-tada/)
here.

## Add New Features to Tada

You can follow these steps to add a new feature if you are already a
collaborator on the project. First, you should create and publish your new branch
via the following command. Substitute the name of your feature/branch for the word
`feature-name`.

- `git checkout -b feature-name`
- `git checkout master`
- `git push -u origin feature-name`

To install development dependencies, type the following commands in the terminal:

```bash
poetry install
```

You can activate the shell with the following command:

```shell
poetry shell
```

Finally, you should open a pull request on the GitHub repository for the new
branch that you have created. This pull request should describe the new feature
that you are adding and give examples of how to run it on the command line.
Of course, if you are not a collaborator on this project, then you will need to
fork the repository, add your new feature, document and test it as appropriate,
and then create a pull request similarly.

We highly recommend you to provide tests along with the feature that you
implemented and you should not break the existing test cases or features.

### Test Tada

To run the test suite for Tada's functions within the shell by typing the
following in your terminal window:

```shell
pytest tests
```

If you want to collect the coverage of the provided test suite, then you can
run:

```shell
pytest --cov-config pytest.cov --cov
```

If you want to collect the coverage of the provided test suite and see what
lines of code are not covered, then you can run:

```shell
pytest --cov-config pytest.cov --cov --cov-report term-missing
```

## Problems or Praise

If you have any problems with installing or using the Tada or its provided test
suite, then please create an issue associated with this Git repository using the
[Issues](https://github.com/Tada-Project/tada/issues) link at the top of this site. The contributors to Tada will do all that
they can to resolve your issue and ensure that all of its features and the test
suite work well in your development environment.
