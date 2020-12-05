# Tada!: auTomAtic orDer-of-growth Analysis

[![Build Status](https://api.travis-ci.org/Tada-Project/tada.svg?branch=master)](https://travis-ci.org/Tada-Project/tada) [![codecov.io](https://codecov.io/github/Tada-Project/tada/coverage.svg?branch=master)](http://codecov.io/github/Tada-Project/tada?branch=master) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

<a href="https://www.netlify.com">
  <img src="https://www.netlify.com/img/global/badges/netlify-dark.svg" alt="Deploys by Netlify" />
</a>

"Tada!: auTomAtic orDer-of-growth Analysis" is a tool that systematically runs a doubling experiment to ascertain the
likely worst-case order-of-growth function for an arbitrary Python function.
This documentation provides a brief overview about how to run the tool, its
provided test suite, and more.

## Install Tada

- Operating system: Linux · macOS/OS X · Windows
- Python version: Python 3.6+

### Install Tada with [pip](https://pip.pypa.io/en/stable/)

<div class="termy">

```console
$ pip install tada-predict
---> 100%
Successfully installed tada-predict
```

You can learn more about installing and building Tada from source through
[here](http://tada-predict.netlify.app/getting-started/#install-through-github-repo)

</div>

## Run Command

To run Tada, you can just type the following command with the arguments into the
terminal window within your preferred virtual environment:

```shell
tada [-h] --directory DIRECTORY \
          --module MODULE --function FUNCTION \
          --types TYPES [TYPES ...]
```

You can learn about Tada's checks and defaults by typing `tada -h` in your
terminal window and then reviewing all the different checks Tada provides. You
can also refer to [usage](http://tada-predict.netlify.app/getting-started/#run-command)
to inspect a sample output.

## Quick Start Example

### Speed-Surprises

We have provided an extensive library of functions and sample JSON schemas in [Speed-Surprises](https://github.com/Tada-Project/speed-surprises)
for you to run Tada in conjunction and experience how Tada automatically suggests
the likely worst-case order-of-growth function for various types of Python function.
You can follow the instructions in [Speed-Surprises](https://github.com/Tada-Project/speed-surprises)
to clone the repository and install the dependencies.

### Run Tada in Conjunction with Speed-Surprises

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

<div class="termy">

```console
$ tada --directory . --module speedsurprises.lists.sorting --function insertion_sort --types hypothesis --schema speedsurprises/jsonschema/single_int_list.json

        Tada!: auTomAtic orDer-of-growth Analysis!
          https://github.com/Tada-Project/tada/
          For Help Information Type: tada -h

Start running experiment insertion_sort for size 1 →


→ Done running experiment insertion_sort for size 1
.
.
.
→ Done running experiment insertion_sort for size 64
```

</div>

```shell
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

Please be sure to check out more about configuring different Tada checks and
tuning parameters at [Using Tada](https://tada-predict.netlify.app/using-tada/)
page.

## Adding New Features to Tada

You are welcome to add new features and contribute to Tada. If you are already
a collaborator on the project, you can simply get started by making a new branch.
Of course, if you are not yet a collaborator, we invite you to fork the repository
and then add your new feature. Please refer to [Contributing](https://tada-predict.netlify.app/contributing/)
to find details about setting up development environment and more.

## Problems or Praise

If you have any problems with installing or using the Tada or its provided test
suite, then please create an issue associated with this Git repository using the
[Issues](https://github.com/Tada-Project/tada/issues) link in the repository page.
The contributors to Tada will do all that they can to resolve your issue and
ensure that all of its features and the test suite work well in your development
environment.
