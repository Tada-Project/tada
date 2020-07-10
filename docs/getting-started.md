# Getting Started

"Tada!: auTomAtic orDer-of-growth Analysis" systematically runs a doubling
experiment to ascertain the likely worst-case order-of-growth function for an
arbitrary Python function.

## Installation

Tada can be directly used from [GitHub](https://github.com/Tada-Project/tada) by
cloning the repository into your local directory:

```bash
git clone https://github.com/Tada-Project/tada.git
```

Tada uses [Pipenv](https://github.com/pypa/pipenv) for dependency management. In
order to to install and run Tada correctly, we recommend you to install `Pipenv`
by running the following command at the prompt of your terminal window::

```bash
pip install pipenv --user
```

Once you have installed `Pipenv` successfully, you can install the dependencies
with the following commmand. Once finished, you will be able to run Tada with
the virtual environment created:

```bash
pipenv install
```

## Usage

To get a quick start on the tool, you can run:

```bash
pipenv run python tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE --function FUNCTION --types TYPES [TYPES ...]
```

To learn more about Tada's checks and defaults, you can type the following command
in your terminal window and then review the following output:

```bash
pipenv run python tada_a_bigoh.py -h
```

```
usage: tada_a_bigoh.py [-h] --directory DIRECTORY [DIRECTORY ...] --module
                       MODULE [MODULE ...] --function FUNCTION [FUNCTION ...]
                       --types TYPES [TYPES ...]
                       [--data_directory DATA_DIRECTORY]
                       [--data_module DATA_MODULE]
                       [--data_function DATA_FUNCTION] [--schema SCHEMA]
                       [--startsize STARTSIZE] [--steps STEPS]
                       [--runningtime RUNNINGTIME] [--expect EXPECT]
                       [--backfill] [--indicator INDICATOR]
                       [--maxsize MAXSIZE] [--sorted] [--log] [--md]
                       [--contrast] [--level LEVEL]
                       [--position POSITION [POSITION ...]]

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY [DIRECTORY ...]
                        Path to the package directory with functions to
                        analyze (default: None)
  --module MODULE [MODULE ...]
                        Module name with functions to analyze (default: None)
  --function FUNCTION [FUNCTION ...]
                        Name of the function to analyze (default: None)
  --types TYPES [TYPES ...]
                        Data generation type: hypothesis or parameter types of
                        the function (default: None)
  --data_directory DATA_DIRECTORY
                        Path to the package directory with function to
                        generate data (default: None)
  --data_module DATA_MODULE
                        Module name with functions to generate data (default:
                        None)
  --data_function DATA_FUNCTION
                        Name of the data generation function (default: None)
  --schema SCHEMA       The path to the JSON schema that describes the data
                        format (default: None)
  --startsize STARTSIZE
                        Starting size of the doubling experiment (default: 1)
  --steps STEPS         Maximum rounds of the doubling experiment (default:
                        10)
  --runningtime RUNNINGTIME
                        Maximum running time of the doubling experiment
                        (default: 200)
  --expect EXPECT       Expected Growth Ratio: O(1) | O(logn) | O(n) |
                        O(nlogn) | O(n^2) | O(n^3) | O(c^n). By using this
                        argument, the experiment result will be stored in a
                        csv file (default: None)
  --backfill            Enable backfill to shrink experiments size according
                        to the Predicted True Value (default: False)
  --indicator INDICATOR
                        Indicator value (default: 0.1)
  --maxsize MAXSIZE     Maximum size of the doubling experiment (default:
                        1500)
  --sorted              Enable input data to be sorted (default: False)
  --log                 Show log/debug/diagnostic output (default: False)
  --md                  Show results table in markdown format (default: False)
  --contrast            Show contrast result table. Only works with multiple
                        experiments (default: False)
  --level LEVEL         The level of nested data structure to apply doubling
                        experiment (default: 1)
  --position POSITION [POSITION ...]
                        The position of input data to double in the
                        multivariable doubling experiment. Must be the last
                        argument (default: [0])

Sample usage: pipenv run python tada_a_bigoh.py --directory
/Users/myname/projectdirectory --module modulename.file --function
function_name --types hypothesis
```

It is worth noting that when the provided function is relied on an external Python
library, it is likely that Tada might not have this dependency, and thus, it might
cause an error when running the experiment. You can simply resolve this issue
by installing the required dependencies. Type in this command if you are using
`Pipenv`:

```bash
pipenv install <library-name>
```

Otherwise, type in the installation command that is appropriate for your own
chosen installation method.

### Sample Output

```bash
$ pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.lists.sorting --function insertion_sort --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 50

🎆  Tada!: auTomAtic orDer-of-growth Analysis! 🎆
    https://github.com/Tada-Project/tada/
❓  For Help Information Type: pipenv run python tada_a_bigoh.py -h  ❓

Start running experiment for size 50 →


→ Done running experiment for size 50
.
.
.
→ Done running experiment for size 800

+------+------------------------+------------------------+--------------------+
| Size |          Mean          |         Median         |       Ratio        |
+------+------------------------+------------------------+--------------------+
|  50  | 6.651357379150391e-06  | 6.475323577880859e-06  |         0          |
| 100  | 1.2518058905029296e-05 | 1.2485851135253904e-05 | 1.8820307181612135 |
| 200  | 2.4886978169759115e-05 | 2.4602192504882815e-05 | 1.9880860410203407 |
| 400  | 5.414438324381511e-05  | 5.275118505859373e-05  | 2.1756109911972965 |
| 800  | 0.00012107856030273438 | 0.00011683380078125006 | 2.2362164466351206 |
+------+------------------------+------------------------+--------------------+
O(n) linear or O(nlogn) linearithmic
```

## Test

You can run the test suite for Tada's functions by typing the following in your
terminal window:

```bash
pipenv run pytest
```

If you want to collect the coverage of the provided test suite, then you can
run:

```bash
pipenv run pytest --cov-config pytest.cov --cov
```

If you want to collect the coverage of the provided test suite and see what
lines of code are not covered, then you can run:

```bash
pipenv run pytest --cov-config pytest.cov --cov --cov-report term-missing
```
