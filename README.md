# Tada!: auTomAtic orDer-of-growth Analysis

[![Build Status](https://api.travis-ci.org/Tada-Project/tada.svg?branch=master)](https://travis-ci.org/Tada-Project/tada) [![codecov.io](http://codecov.io/github/Tada-Project/tada/coverage.svg?branch=master)](http://codecov.io/github/Tada-Project/tada?branch=master) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

This repository contains the source code and usage instructions for a tool
called "Tada: auTomAtic orDer-of-growth Analysis" that is implemented in the
Python 3 language. The tool systematically runs a doubling experiment to
ascertain the likely worst-case order-of-growth function for an arbitrary Python
function. This documentation provides a brief overview about how to run the
tool, its provided test suite, and more.

## Installing and Testing Tada

This program uses [Pipenv](https://github.com/pypa/pipenv) for installation.
Once you have installed `pipenv` you can run the test suite for Tada's functions
by typing the following in your terminal window:

- `pipenv install`
- `pipenv run pytest`

You can also activate the `pipenv` shell by running this command: `pipenv shell`

If you want to collect the coverage of the provided test suite, then you can
run:

- `pipenv run pytest --cov-config pytest.cov --cov`

If you want to collect the coverage of the provided test suite and see what
lines of code are not covered, then you can run:

- `pipenv run pytest --cov-config pytest.cov --cov --cov-report term-missing`

## Using Tada

### Checks

Tada is currently under continuous development, it is not yet feature
complete. However, the documentation here and in
[Speed-Surprises](https://github.com/Tada-Project/speed-surprises) have featured
some examples on how to run the tool to automatically suggest the likely
worst-case order-of-growth function for various types of provided Python function.

If you want to run the tool, then you can run:

```bash
pipenv run python tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE --function FUNCTION --types TYPES [TYPES ...]
```

You can learn about Tada's checks and defaults by typing
`pipenv run python tada_a_bigoh.py -h` in your terminal window and then
reviewing the following output.

```
usage: tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE --function
                       FUNCTION --types TYPES [TYPES ...] [--schema SCHEMA]
                       [--startsize STARTSIZE] [--steps STEPS]
                       [--runningtime RUNNINGTIME] [--expect EXPECT]
                       [--backfill BACKFILL] [--indicator INDICATOR]
                       [--maxsize MAXSIZE] [--sorted SORTED] [--level LEVEL]

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY
                        Path to the package directory with functions to
                        analyze (default: None)
  --module MODULE       Module name with functions to analyze (default: None)
  --function FUNCTION   Name of the function to analyze (default: None)
  --types TYPES [TYPES ...]
                        Data generation type: hypothesis or parameter types of
                        the function (default: None)
  --schema SCHEMA       The path to the JSON schema that describes the data
                        format (default: None)
  --startsize STARTSIZE
                        Starting size of the doubling experiment (default: 1)
  --steps STEPS         Maximum rounds of the doubling experiment (default:
                        10)
  --runningtime RUNNINGTIME
                        Maximum running time of the doubling experiment
                        (default: 200)
  --expect EXPECT       Expected Growth Ratio:O(1) | O(logn) | O(n) | O(nlogn)
                        | O(n^2) | O(n^3) | O(c^n). By using this argument,
                        the experiment result will be stored in a csv file
                        (default: None)
  --backfill BACKFILL   Enable backfill to shrink experiments size according
                        to the Predicted True Value: (0|1) (default: 0)
  --indicator INDICATOR
                        Indicator value (default: 0.1)
  --maxsize MAXSIZE     Maximum size of the doubling experiment (default:
                        1500)
  --sorted SORTED       Enable input data to be sorted: (0|1) (default: 0)
  --level LEVEL         The level of nested data structure to apply doubling
                        experiment (default: 1)
  --position POSITION   The position of nested data structure to apply doubling
                        experiment (default: [0])

Sample usage: pipenv run python tada_a_bigoh.py --directory
/Users/myname/projectdirectory --module modulename.file --function
function_name --types hypothesis
```

It is worth noting that when the provided function is relied on an external Python
library, it is likely that Tada might not have this dependency, and thus, it might
cause an error when running the experiment. You can simply resolve this issue
by installing the required dependencies of the function by this following
command:

- `pipenv install <library-name>`

### Data Generation

Tada adopts `Hypothesis` and `Hypothesis-jsonschema` to generate random data for the
provided Python function. Therefore, we encourage you to create a file of
a JSON array that contains JSON schemas of each parameter passed into the provided
function. Tada also supports data generation through our builtin
[data generation functions](https://github.com/Tada-Project/tada/blob/master/tada/util/generate.py)
including these following types:
`int, int_list, char, char_list, boolean, string, float, bitdepth`

To specify the data generation strategy, we encourage you to set argument
`--types TYPES [TYPES ...]` with `hypothesis` or one of the aforementioned
generation types. When using `hypothesis` to generate experiment data, you can
simply set the `maxItems` and `minItems` in the json schema to zero. The size
doubling will be enabled through the command line check `--startsize STARTSIZE`,
which will be the starting size of the doubling experiment.

For further usage of JSON schemas and how to write them for various data types:
please refer to [JSON schema](https://json-schema.org/understanding-json-schema/reference/type.html)
and
[sample JSON schemas](https://github.com/Tada-Project/speed-surprises/tree/master/speedsurprises/jsonschema).

When completed, Tada will be used to estimate the worst-case time complexity for
Python functions.

### Speed-Surprises

We have provided an extensive library of functions and sample JSON schemas in
[Speed-Surprises repository](https://github.com/Tada-Project/speed-surprises).
You can use or test Tada in conjunction with functions in this repository.

### Sample Output

```bash
$ pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.lists.sorting --function insertion_sort --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 50

🎆  Tada!: auTomAtic orDer-of-growth Analysis! 🎆
    https://github.com/Tada-Project/tada/
❓  For Help Information Type: pipenv run python tada_a_bigoh.py -h  ❓

Start running experiment for size 50 →

.....................
tada_speedsurpriseslistssorting_insertionsort_50: Mean +- std dev: 6.76 us +- 0.38 us

Mean 6.756377457682293e-06
Median 6.655228393554689e-06
current indicator: 0.1
expected end time: 6.756377457682293e-06

→ Done running experiment for size 50

end time rate: 1
last end time rate: 1
Start running experiment for size 100 →
.
.
.
→ Done running experiment for size 800

end time rate: 1.0977868448462222
last end time rate: 1.0104045516442501
Quit due to researched max size
+------+------------------------+------------------------+--------------------+
| Size |          Mean          |         Median         |       Ratio        |
+------+------------------------+------------------------+--------------------+
|  50  | 6.860612288411459e-06  | 6.584678009033201e-06  |         0          |
| 100  | 1.3285847186279297e-05 | 1.2845127746582033e-05 | 1.9365395722362808 |
| 200  | 2.7495347680664065e-05 | 2.698630590820313e-05  | 2.069521596564753  |
| 400  | 5.5284626326497395e-05 |  5.4273513671875e-05   | 2.010690207251897  |
| 800  | 0.00011595141430664063 | 0.00011436475048828127 | 2.0973536769853545 |
+------+------------------------+------------------------+--------------------+
O(n) linear or O(nlogn) linearithmic
```

### Recording Tada Experiment Result(s)

If you would like to record the results of the doubling experiment, you can use
the command line argument `--expect` by specifying with a string of the expected
Big-Oh growth ratio of the provided function (e.g. `"O(1)"`, `"O(n^2)"`). The
following variables will be stored and exported to `experiment_data.csv`. :

- `EXPERIMENT_RELIABILITY`:  dummy variable := 1 if the result provided by tada tool is
  what user expected.
- `CPU_TYPE`: string := type information of CPU.
- `CPU_TEMP`: string := temperature information of CPU.
- `CPU_COUNT`: int := the number of physical CPUs.
- `TOTAL_RUNNING_TIME`: int := total time spent on running experiment.
- `QUIT_BY_MAX_RUNTIME`: dummy variable := 1 if the tool exits by reaching the
  max_runtime.
- `QUIT_BY_INDICATOR`: dummy variable := 1 if the tool exits by having indicator larger
  than the indicator bound.
- `QUIT_BY_BACKFILL`: dummy variable := 1 if the tool exits by having multiple times of backfills
- `QUIT_BY_MAX_SIZE`: dummy variable := 1 if the tool exits by reaching the max_size
  back-filling.
- `MEM_MAX_RSS`: int := track of current machine memory usage.
- `MEM_PEAK_PAGEFILE_USAGE`: int := track of current machine memory usage (windows).
- `OS`: string := information of current operating system.
- `INDICATOR_VALUE`: int := the value of the indicator boundary user set.
- `BACKFILL_TIMES`: int := the value of the back-fill time boundary user set.
- `PYPERF_AVG_EXPERIMENT_ROUNDS`: int := the average loops of all benchmarks in the
  experiment, the measurement of difficulty for PyPerf to analyze the target algorithm.
- `PYPERF_LAST_TWO_EXPERIMENT_ROUNDS_RATIO`: int := the growth ratio of the total loops
  in the last two benchmarks, the total loops is usually decreasing when the input get
  larger, the measurement of reliability of the experiment analysis.
- `NAME_OF_EXPERIMENT`: string := experiment information.
- `PYTHON_VERSION`: string := current version of Python.
- `DATA_GEN_STRATEGY`: string := the chosen data generation strategy
- `START_SIZE`: int := initial size of doubling experiments

To run with experiment data collected, add `expect` into the commannd like this:

```bash
pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.lists.sorting --function insertion_sort --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 50 --expect "O(n)"
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

To install development dependencies, type the following command in the terminal:

```
pipenv install --dev
```

Finally, you should open a pull request on the GitHub repository for the new
branch that you have created. This pull request should describe the new feature
that you are adding and give examples of how to run it on the command line. Of
course, if you are not a collaborator on this project, then you will need to
fork the repository, add your new feature, document and test it as appropriate,
and then create a pull request.

## Future Works

- Further verification of the accuracy and efficiency of the tool

## Problems or Praise

If you have any problems with installing or using the Tada or its provided test
suite, then please create an issue associated with this Git repository using the
"Issues" link at the top of this site. The contributors to Tada will do all that
they can to resolve your issue and ensure that all of its features and the test
suite work well in your development environment.
