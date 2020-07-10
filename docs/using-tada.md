# Using Tada

## Data Generation

Tada adopts [Hypothesis](https://hypothesis.works) and
[Hypothesis-jsonschema](https://github.com/Zac-HD/hypothesis-jsonschema) to
generate random data for the provided Python function. Therefore, we encourage
you to create a file of a JSON array that contains JSON schemas of each parameter
passed into the provided function. Tada also supports data generation through our
built-in [data generation functions](https://github.com/Tada-Project/tada/blob/master/tada/util/generate.py)
including these following types:
`int, int_list, char, char_list, boolean, string, float, bitdepth`

To specify the data generation strategy, we encourage you to set argument
`--types TYPES [TYPES ...]` with `Hypothesis` or one of the aforementioned
generation types. When using `Hypothesis` to generate experiment data, you can
simply set the `maxItems` and `minItems` in the json schema to zero. The size
doubling will be enabled through the command line check `--startsize STARTSIZE`,
which will be the starting size of the doubling experiment.

For further usage of JSON schemas and how to write them for various data types:
please refer to [JSON schema](https://json-schema.org/understanding-json-schema/reference/type.html)
and
[sample JSON schemas](https://github.com/Tada-Project/speed-surprises/tree/master/speedsurprises/jsonschema).

When completed, Tada will be used to estimate the worst-case time complexity for
the given Python function(s).

## Speed-Surprises

We have provided an extensive library of functions, experiment scripts, and
sample JSON schemas in [Speed-Surprises repository](https://github.com/Tada-Project/speed-surprises).
You can use or test Tada in conjunction with functions in this repository.

## Configurations

### Compare two algorithms' performance with Tada

If you would like to run Tada to compare the performance of two functions, you
will just need to specify the additional function with its directory and module
(if it's different from the first function) like this:

```bash
pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.lists.sorting --function insertion_sort bubble_sort --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 25
```

#### `Compare` sample output

```bash
            Tada!: auTomAtic orDer-of-growth Analysis!
              https://github.com/Tada-Project/tada/
    For Help Information Type: pipenv run python tada_a_bigoh.py -h


Start running experiment insertion_sort for size 25 →
.
.
.
→ Done running experiment bubble_sort for size 800

+-----------------------------------------------------------------------------+
|             insertion_sort: O(n) linear or O(nlogn) linearithmic            |
+------+------------------------+------------------------+--------------------+
| Size |          Mean          |         Median         |       Ratio        |
+------+------------------------+------------------------+--------------------+
|  25  | 3.644364811706543e-06  | 3.498709533691405e-06  |         0          |
|  50  | 6.535123836263021e-06  | 6.483351989746092e-06  | 1.793213405878218  |
| 100  | 1.2902192108154296e-05 | 1.2540842590332028e-05 | 1.9742842571032526 |
| 200  | 2.5023900944010416e-05 | 2.4608139038085928e-05 | 1.9395077002608803 |
| 400  | 5.526396857910156e-05  | 5.3515207031250005e-05 | 2.2084473840729952 |
| 800  | 0.00011801120257161459 |  0.00011251379296875   | 2.1354094829925283 |
+------+------------------------+------------------------+--------------------+
+-----------------------------------------------------------------------------+
|                        bubble_sort: O(n^2) quadratic                        |
+------+------------------------+------------------------+--------------------+
| Size |          Mean          |         Median         |       Ratio        |
+------+------------------------+------------------------+--------------------+
|  25  | 2.8776128824869792e-05 | 2.846207250976562e-05  |         0          |
|  50  | 0.00010703222574869792 | 0.00010308191601562499 | 3.7194796562140504 |
| 100  | 0.0004109644687825521  | 0.00039437410449218743 | 3.8396330255474633 |
| 200  |   0.0015730586140625   | 0.0015326660937500002  | 3.8277241308051635 |
| 400  |    0.00632440301875    |  0.006229572156249999  | 4.020449690947576  |
| 800  |  0.029292134683333335  |  0.028519337000000006  | 4.631604690038055  |
+------+------------------------+------------------------+--------------------+

At the greatest common size 800:
Mean: insertion_sort is 99.60% faster than bubble_sort
Median: insertion_sort is 99.61% faster than bubble_sort
```

### Contrast result tables of two algorithms' performance with Tada

If you would like to contrast run time of two different algorithms where the run
time of one might be included in another, you can use the `--contrast` feature
to get the result table generated based on the subtraction of the two algorithms
with the growth ratio analysis of the run time difference:

```bash
pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module=speedsurprises.graph.graph_gen --function  graph_gen graph_gen_BFS --types hypothesis --schema=../speed-surprises/speedsurprises/jsonschema/int_and_int.json --sta rtsize=50  --max=1000 --position 0 --contrast
```

#### `--contrast` sample output

```bash
            Tada!: auTomAtic orDer-of-growth Analysis!
              https://github.com/Tada-Project/tada/
    For Help Information Type: pipenv run python tada_a_bigoh.py -h

Start running experiment graph_gen for size 25 →
.
.
.
→ Done running experiment graph_gen_BFS for size 800

+-----------------------------------------------------------------------------+
|               graph_gen: O(n) linear or O(nlogn) linearithmic               |
+------+------------------------+------------------------+--------------------+
| Size |          Mean          |         Median         |       Ratio        |
+------+------------------------+------------------------+--------------------+
|  50  |  9.94538065592448e-06  | 9.501693725585938e-06  |         0          |
| 100  | 1.8558588460286458e-05 | 1.8363348388671875e-05 | 1.8660510947090876 |
| 200  | 3.7122855631510415e-05 | 3.560983886718751e-05  | 2.000305988300223  |
| 400  | 7.208413248697916e-05  | 7.197658691406252e-05  | 1.9417722925871337 |
| 800  | 0.00015173049479166666 | 0.00014575283203125002 | 2.104908383534675  |
+------+------------------------+------------------------+--------------------+
+-------------------------------------------------------------------------+
|                     graph_gen_BFS: O(n^2) quadratic                     |
+------+-----------------------+---------------------+--------------------+
| Size |          Mean         |        Median       |       Ratio        |
+------+-----------------------+---------------------+--------------------+
|  50  |   0.0010322848828125  |  0.000936182421875  |         0          |
| 100  | 0.0037961446354166668 |   0.0036485609375   | 3.6774195753733445 |
| 200  |  0.014912410624999999 |    0.01433645625    | 3.928304123576473  |
| 400  |  0.06095087833333333  | 0.05791582499999999 | 4.087258583877236  |
| 800  |      0.252504645      | 0.23859980000000003 | 4.1427564606875915 |
+------+-----------------------+---------------------+--------------------+

At the greatest common size 800:
Mean: graph_gen is 99.94% faster than graph_gen_BFS
Median: graph_gen is 99.94% faster than graph_gen_BFS

+----------------------------------------------------------------------------------------+
|               Contrast for graph_gen and graph_gen_BFS: O(n^2) quadratic               |
+-------+---------------------------+---------------------------+------------------------+
|  Size |            Mean           |           Median          |         Ratio          |
+-------+---------------------------+---------------------------+------------------------+
|   50  |   0.0010223395021565756   |   0.0009266807281494141   |           0            |
|  100  |   0.0037775860469563805   |    0.003630197589111328   |   3.6950406777667753   |
|  200  |    0.014875287769368488   |    0.014300846411132813   |   3.9377760253412575   |
|  400  |    0.06087879420084635    |    0.05784384841308593    |   4.092612872082332    |
|  800  |    0.25235291450520836    |    0.23845404716796878    |   4.145169394660909    |
+-------+---------------------------+---------------------------+------------------------+
```

### Display debug output with `--log`

```bash
pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.lists.sorting --function insertion_sort --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 50 --log
```

#### `--log` sample output

```bash
            Tada!: auTomAtic orDer-of-growth Analysis!
              https://github.com/Tada-Project/tada/
    For Help Information Type: pipenv run python tada_a_bigoh.py -h

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

### Record Tada experiment result(s)

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

To run with experiment data collected, add `expect` into the command like this:

```bash
pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.lists.sorting --function insertion_sort --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 50 --expect "O(n)"
```
