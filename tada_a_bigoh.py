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
    # TODO: move these to command-line arguments
    size = 100
    factor = 2
    size_stop = 100
    # display the welcome message
    display.welcome_message()
    # read and verify the command-line arguments
    tada_arguments = arguments.parse(sys.argv[1:])
    did_verify_arguments = arguments.verify(tada_arguments)
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
        save.save_experiment_size(constants.SIZE, size)
        # save the directory containing functions to be analyzed
        save.save_directory(constants.DIRECTORY, tada_arguments.directory)
        # perform the small doubling experiment
        while size <= size_stop:
            # run the benchmark by using it through python
            display.start_message(size)
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
                + constants.PERF_BENCHMARK
                + str(size)
                + constants.JSON_EXT
            )
            # print('Values {0}'.format(current_benchmark.get_values()))
            print("Mean {0}".format(current_benchmark.mean()))
            print("Median {0}".format(current_benchmark.median()))
            display.display_end_message(size)
            # go to the next size for the doubling experiment
            size = size * 2
            # write the next doubling experiment size to the file
            save.save_experiment_size(constants.SIZE, size)
