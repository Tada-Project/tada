"""Benchmarks with perf for the function under analysis"""

import importlib
import pyperf

try:
    from tada.util import configuration
    from tada.util import constants
    from tada.util import generate
    from tada.util import package
    from tada.util import read
    from tada.util import run
    from tada.util import save
except ImportError:
    from util import configuration
    from util import constants
    from util import generate
    from util import package
    from util import read
    from util import run
    from util import save

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
    # give a by-configuration name to the experiment
    current_experiment_name = configuration.get_experiment_name(
        tada_configuration_dict, chosen_size
    )
    # set the name of the experiment for perf
    runner.metadata[constants.DESCRIPTION_METANAME] = current_experiment_name
    # read the chosen types
    func_type = configuration.get_types(tada_configuration_dict)
    # initialize path for schema
    path = None
    gen_func = None
    # using hypothesis to generate experiment data
    if func_type[0] == "hypothesis":
        # read path from arguments
        path = configuration.get_schema_path(tada_configuration_dict)
    if func_type[0] == "custom":
        data_directory = configuration.get_data_directory(tada_configuration_dict)
        if data_directory != "":
            package.add_data_sys_path(
                configuration.get_data_directory(tada_configuration_dict)
            )
        data_module = importlib.import_module(
            configuration.get_data_module(tada_configuration_dict)
        )
        data_function = getattr(
            data_module, configuration.get_data_function(tada_configuration_dict)
        )
        gen_func = data_function
    level = configuration.get_level(tada_configuration_dict)
    position = configuration.get_position(tada_configuration_dict)
    # generate data
    data = generate.generate_data(
        func_type, chosen_size, level, position, path, gen_func
    )
    # run benchmark
    if configuration.get_sortinput(tada_configuration_dict):
        for t in data:
            if isinstance(t, list):
                t.sort()
    current_benchmark = runner.bench_func(
        current_experiment_name, run.run_benchmark, analyzed_function, *data,
    )

    # save the perf results from running the benchmark
    save.save_benchmark_results(current_benchmark, current_experiment_name)
