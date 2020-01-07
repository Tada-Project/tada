"""Constants used by the tada package"""

import os

# Parameters
SIZE_START = 1
FACTOR = 2
STEPS = 5
SIZE_STOP = SIZE_START * FACTOR ** STEPS
RUNNINGTIME = 200
INDICATOR = 0.1
STEP_START = 0

# Names
TADA = "tada"

# Separators
NONE = ""
PERIOD = "."
SEPARATOR = os.sep
SPACE = " "
UNDERSCORE = "_"

# Error codes
INCORRECT_ARGUMENTS = 2

# Directories
RESULTS = "_results"

# Files
SIZE = ".size.txt"
DIRECTORY = ".directory.txt"
CONFIGURATION = ".tada.json"

# Constants
UTF8 = "utf-8"

# Extensions
JSON_EXT = ".json"
PYTHON_EXT = ".py"

# Commands
PYTHON_EXEC = "python"

# Perf
DESCRIPTION_METANAME = "description"
PERF_BENCHMARK = "perf_benchmark"

# Experiment data storage
RESULT = 0
CPU_TYPE = ""
CPU_TEMP = ""
CPU_COUNT = 0
TOTAL_RUNNING_TIME = 0
QUIT_BY_MAX_RUNTIME = 0
QUIT_BY_INDICATOR = 0
QUIT_BY_BACKFILL = 0
MEM_MAX_RSS = 0
MEM_PEAK_PAGEFILE_USAGE = 0
OS = ""
INDICATOR_VALUE = 0
BACKFILL_TIMES = 0
PYPERF_AVG_EXPERIMENT_ROUNDS = 0
PYPERF_LAST_TWO_EXPERIMENT_ROUNDS_RATIO = 0
NAME_OF_EXPERIMENT = ""
PYTHON_VERSION = ""
