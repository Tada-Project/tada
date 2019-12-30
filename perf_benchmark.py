"""Benchmarks with perf for the function under analysis"""

import importlib
import pyperf
import json

from tada.util import configuration
from tada.util import constants
from tada.util import generate
from tada.util import package
from tada.util import read
from tada.util import run
from tada.util import save
from hypothesis import given, settings
from hypothesis_jsonschema import from_schema

if __name__ == "__main__":
    # read the configuration file to access the configuration dictionary
    tada_configuration_dict = configuration.read(constants.CONFIGURATION)
    # add the specified directory to the system path
    package.add_sys_path(configuration.get_directory(tada_configuration_dict))
    # reflectively import the chosen module
    analyzed_module = importlib.import_module(
        configuration.get_module(tada_configuration_dict)
    )
    # reflectively access the chosen function
    analyzed_function = getattr(
        analyzed_module, configuration.get_function(tada_configuration_dict)
    )

    # read the chosen_size
    chosen_size = read.read_experiment_size()
    # configure perf
    runner = pyperf.Runner()

    fakefunction = generate.generate_strategy(
        generate.generate_fake_hypothesis,
        configuration.get_schema_path(tada_configuration_dict),
        chosen_size,
    )

    fakefunction()
    f = open("data.txt", "r")
    oridata = f.read()
    formatteddata = oridata[1:-1]
    data = list(formatteddata.split(","))

    # give a by-configuration name to the experiment
    current_experiment_name = configuration.get_experiment_name(
        tada_configuration_dict, chosen_size
    )
    # set the name of the experiment for perf
    runner.metadata[constants.DESCRIPTION_METANAME] = current_experiment_name
    # run the benchmark using the bench_func from perf
    current_benchmark = runner.bench_func(
        current_experiment_name, run.run_benchmark, analyzed_function, data
    )
    # save the perf results from running the benchmark
    save.save_benchmark_results(current_benchmark, current_experiment_name)
