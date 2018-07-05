"""Benchmarks with perf for the function under analysis"""

import importlib
import perf

from tada.util import configuration
from tada.util import constants
from tada.util import run
from tada.util import package
from tada.util import read
from tada.util import save

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
    runner = perf.Runner()
    # give a by-configuration name to the experiment
    current_experiment_name = (
        constants.TADA
        + constants.UNDERSCORE
        + configuration.get_module(tada_configuration_dict).replace(
            constants.PERIOD, constants.NONE
        )
        + constants.UNDERSCORE
        + configuration.get_function(tada_configuration_dict).replace(
            constants.UNDERSCORE, constants.NONE
        )
        + constants.UNDERSCORE
        + constants.PERF_BENCHMARK
        + constants.UNDERSCORE
        + str(chosen_size)
    )
    runner.metadata[constants.DESCRIPTION_METANAME] = current_experiment_name
    # TODO: Handle this mcopies --- is it the metadata?
    current_benchmark = runner.bench_func(
        "mcopies", run.run_benchmark, analyzed_function, chosen_size
    )
    # save the perf results from running the benchmark
    save.save_bencmark_results(current_benchmark, current_experiment_name)
