"""Run doubling experiments and 'Tada!' you get the time complexity"""

import sys
import time
import pyperf
from prettytable import PrettyTable

from tada.util import analysis
from tada.util import arguments
from tada.util import configuration
from tada.util import constants
from tada.util import display
from tada.util import package
from tada.util import run
from tada.util import save
from tada.util import results

if __name__ == "__main__":
    start_time = time.time()

    # display the welcome message
    display.display_welcome_message()
    # read and verify the command-line arguments
    tada_arguments = arguments.parse(sys.argv[1:])
    did_verify_arguments = arguments.verify(tada_arguments)
    resultstable = PrettyTable(['Size', 'Mean', 'Median', 'Ratio'])
    meanlastround = 0
    indicator = constants.INDICATOR
    steps = constants.STEP_START
    last_last_size = 0
    count = 0
    current_size = tada_arguments.startsize
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
        while indicator >= 0.1 and steps <= tada_arguments.steps:
            # run the benchmark by using it through python
            analysis.backfill_checker(last_last_size, current_size, count)
            if count == 2:
                break
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
            current_benchmark = pyperf.Benchmark.load(
                constants.RESULTS
                + constants.SEPARATOR
                + configuration.get_experiment_name(vars(tada_arguments), current_size)
                + constants.JSON_EXT
            )
            # perform additional analysis of the results
            # reminder: print('Values {0}'.format(current_benchmark.get_values()))
            mean = current_benchmark.mean()
            print("Mean {0}".format(mean))
            median = current_benchmark.median()
            print("Median {0}".format(median))
            if meanlastround == 0:
                ratio = 0
                indicator = 0.1
                end_time = mean
                last_size = 0
                last_end_time = end_time
                last_end_time_rate = 1
                end_time_rate = 1
            else:
                if current_size > last_size:
                    ratio = mean / meanlastround
                    avg = (mean + meanlastround) / 2
                    std = mean - avg
                    indicator = std / avg
                    end_time = (mean - 0.01 * meanlastround) / 0.99
                    last_end_time_rate = end_time_rate
                    end_time_rate = (end_time - last_end_time) / last_end_time
                else:
                    ratio = meanlastround / mean
                    avg = (mean + meanlastround) / 2
                    std = meanlastround - avg
                    indicator = std / avg
                    end_time = (meanlastround - 0.01 * mean) / 0.99
                    last_end_time_rate = end_time_rate
                    end_time_rate = (end_time - last_end_time) / last_end_time
                print("last_end_time", last_end_time)
                last_end_time = end_time
            print("current indicator:", indicator)
            print("expected end time:", end_time)
            results.add_resultstable(resultstable, current_size, mean, median, ratio)
            # show that we are done running for a size
            display.display_end_message(current_size)
            # go to the next size for the doubling experiment
            last_last_size = last_size
            last_size = current_size
            print("end time rate:", end_time_rate)
            print("last end time rate:", last_end_time_rate)
            if last_end_time_rate > end_time_rate:
                current_size = int(current_size / constants.FACTOR)
            else:
                current_size = current_size * constants.FACTOR
            save.save_experiment_size(constants.SIZE, current_size)
            meanlastround = mean
            current_runningtime = time.time() - start_time
            if current_runningtime > tada_arguments.runningtime:
                print("out of time:", current_runningtime)
                break
            steps += 1
        results.display_resultstable(resultstable)
        analysis.analyze_big_oh(ratio)
