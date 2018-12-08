"""Run doubling experiments and 'Tada!' you get the time complexity"""

import sys
import perf

from tada.util import arguments
from tada.util import configuration
from tada.util import constants
from tada.util import display
from tada.util import package
from tada.util import run
from tada.util import save

if __name__ == "__main__":
    current_size = constants.SIZE_START
    # display the welcome message
    display.display_welcome_message()
    # read and verify the command-line arguments
    tada_arguments = arguments.parse(sys.argv[1:])
    did_verify_arguments = arguments.verify(tada_arguments)
    resultstable = PrettyTable(['Size', 'Mean', 'Median'])
    # incorrect arguments, exit program
    if did_verify_arguments is False:
        print("Incorrect command-line arguments.")
        sys.exit(constants.INCORRECT_ARGUMENTS)
    # correct arguments, run doubling experiment
    else:
        # add the directory to the sys.path
        package.add_sys_path(tada_arguments.directory)
        # create and save a configuration dictionary from the arguments
        configuration.save(constants.CONFIGURATION, vars(tada_arguments))
        # save the size of the experiment in the constants.file
        save.save_experiment_size(constants.SIZE, current_size)
        # save the directory containing functions to be analyzed
        save.save_directory(constants.DIRECTORY, tada_arguments.directory)
        # perform the small doubling experiment
        while current_size <= constants.SIZE_STOP:
            # run the benchmark by using it through python
            display.display_start_message(current_size)
            current_output, current_error = run.run_command(
                constants.PYTHON_EXEC
                + constants.SPACE
                + constants.PERF_BENCHMARK
                + constants.PYTHON_EXT
            )
            # display the standard output and error
            display.display_output(current_output.decode(constants.UTF8))
            display.display_output(current_error.decode(constants.UTF8))
            # read the JSON file containing the results
            current_benchmark = perf.Benchmark.load(
                constants.RESULTS
                + constants.SEPARATOR
                + configuration.get_experiment_name(vars(tada_arguments), current_size)
                + constants.JSON_EXT
            )
            # perform additional analysis of the results
            # reminder: print('Values {0}'.format(current_benchmark.get_values()))
            mean = "Mean {0}".format(current_benchmark.mean())
            print(mean)
            median = "Median {0}".format(current_benchmark.median())
            print(median)
            results.add_resultstable(resultstable, current_size, mean, median)
            # show that we are done running for a size
            display.display_end_message(current_size)
            # go to the next size for the doubling experiment
            current_size = current_size * constants.FACTOR
            # write the next doubling experiment size to the file
            save.save_experiment_size(constants.SIZE, current_size)
        results.display_resultstable(resultstable)
