"""Run doubling experiments and 'Tada!' you get the time complexity"""

from __future__ import division
import json
import os
import sys
import time
import pandas as pd
import pyperf

from prettytable import PrettyTable

try:
    from tada.util import analysis
    from tada.util import arguments
    from tada.util import configuration
    from tada.util import constants
    from tada.util import display as dis
    from tada.util import package
    from tada.util import run
    from tada.util import save
    from tada.util import read
    from tada.util import results
except ImportError:
    from util import analysis
    from util import arguments
    from util import configuration
    from util import constants
    from util import display as dis
    from util import package
    from util import run
    from util import save
    from util import read
    from util import results


# pylint: disable=too-many-locals, too-many-branches, too-many-statements
def tada(tada_arguments):  # noqa: C901
    """A single tada experiment"""
    start_time = time.time()
    # read and verify the command-line arguments
    did_verify_arguments = arguments.verify(tada_arguments)
    resultstable = PrettyTable()
    resultstable.field_names = ["Size", "Mean", "Median", "Ratio"]
    meanlastround = 0
    result = {}
    indicator = 0
    steps = constants.STEP_START
    last_last_size = 0
    current_size = tada_arguments.startsize
    total_loop_list = []
    sum_of_loops = 0
    use_backfill = tada_arguments.backfill
    # get current directory for saving
    original_dir = os.getcwd()
    # use absolute path for import directories
    tada_arguments.directory = os.path.abspath(tada_arguments.directory)
    if tada_arguments.data_directory:
        tada_arguments.data_directory = os.path.abspath(tada_arguments.data_directory)
    if tada_arguments.schema:
        tada_arguments.schema = os.path.abspath(tada_arguments.schema)
    # display debug output
    to_print = tada_arguments.log
    # incorrect arguments, exit program
    if did_verify_arguments is False:
        dis.output_message("Incorrect command-line arguments.", to_print)
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
        while True:
            if use_backfill:
                # run the benchmark by using it through python
                # backfill checker
                if last_last_size == current_size:
                    dis.output_message(
                        f"lastlast: {last_last_size} \ncurrent: {current_size}",
                        to_print,
                    )
                    constants.BACKFILL_TIMES = constants.BACKFILL_TIMES + 1
                    dis.output_message(
                        dis.green("Backfill Count: ") + str(constants.BACKFILL_TIMES),
                        to_print,
                    )
                if constants.BACKFILL_TIMES == 2:
                    constants.QUIT_BY_BACKFILL = 1
                    dis.output_message("\nQuit due to backfill twice", to_print)
                    break
            if current_size >= tada_arguments.maxsize:
                constants.QUIT_BY_MAX_SIZE = 1
                dis.output_message(
                    "\nQuit due to reaching max size: " + str(tada_arguments.maxsize),
                    to_print,
                )
                break
            print(dis.start_message(current_size, tada_arguments.function))
            current_output, current_error = run.run_command(
                constants.PYTHON_EXEC
                + constants.SPACE
                + constants.PERF_BENCHMARK
                + constants.PYTHON_EXT
            )
            # display the standard output and error
            dis.output_message(current_output.decode(constants.UTF8), to_print)
            dis.output_message(current_error.decode(constants.UTF8), to_print=True)
            # read the JSON file containing the results
            current_benchmark = pyperf.Benchmark.load(
                constants.RESULTS
                + constants.SEPARATOR
                + configuration.get_experiment_name(vars(tada_arguments), current_size)
                + constants.JSON_EXT
            )
            # Numbers of benchmark run which include one warmup and twenty excution
            # print(current_benchmark.get_nrun())
            # Total Runtime of the benchmark excution
            # print(current_benchmark.get_total_duration())
            total_loop_list.append(current_benchmark.get_total_loops())
            # perform additional analysis of the results
            # reminder: print('Values {0}'.format(current_benchmark.get_values()))
            mean = current_benchmark.mean()
            median = current_benchmark.median()
            result.update({current_size: [mean, median]})
            dis.output_message(
                dis.green("Mean: ") + str(mean), to_print,
            )
            dis.output_message(
                dis.green("Median: ") + str(median), to_print,
            )
            if meanlastround == 0:
                ratio = 0
                indicator = tada_arguments.indicator
                end_time = mean
                last_size = 0
                last_end_time = end_time
                last_end_time_rate = 1
                end_time_rate = 1
            else:
                if current_size > last_size:
                    ratio = mean / meanlastround
                    avg = (mean + meanlastround) / 2
                    std = abs(mean - avg)
                    indicator = std / abs(avg)
                    end_time = (mean - 0.01 * meanlastround) / 0.99
                    last_end_time_rate = end_time_rate
                    end_time_rate = (end_time - last_end_time) / last_end_time
                else:  # backfill
                    ratio = meanlastround / mean
                    avg = (mean + meanlastround) / 2
                    std = abs(meanlastround - avg)
                    indicator = std / abs(avg)
                    end_time = (meanlastround - 0.01 * mean) / 0.99
                    last_end_time_rate = end_time_rate
                    end_time_rate = (end_time - last_end_time) / last_end_time
                dis.output_message(
                    dis.green("Last end time: ") + str(last_end_time), to_print,
                )
                last_end_time = end_time
            dis.output_message(
                dis.green("Current indicator: ") + str(indicator), to_print
            )
            dis.output_message(
                dis.green("Expected end time: ") + str(end_time), to_print
            )
            results.add_resultstable(resultstable, current_size, mean, median, ratio)
            # show that we are done running for a size
            print(dis.end_message(current_size, tada_arguments.function))
            # go to the next size for the doubling experiment
            last_last_size = last_size
            last_size = current_size
            dis.output_message(
                dis.green("End time rate: ") + str(end_time_rate), to_print
            )
            dis.output_message(
                dis.green("Last end time rate: ") + str(last_end_time_rate), to_print,
            )
            if last_end_time_rate > end_time_rate and use_backfill:
                current_size = int(current_size / constants.FACTOR)
            else:
                current_size = current_size * constants.FACTOR
            # check indicator and quit if smaller than decided indicator
            if indicator < tada_arguments.indicator:
                dis.output_message(f"\nQuit due to indicator: {indicator}", to_print)
                break
            save.save_experiment_size(constants.SIZE, current_size)
            meanlastround = mean
            current_runningtime = time.time() - start_time
            if current_runningtime > tada_arguments.runningtime:
                dis.output_message(
                    "\nQuit due to exceeding the max time limit: "
                    + current_runningtime,
                    to_print,
                )
                constants.QUIT_BY_MAX_RUNTIME = 1
                break
            steps += 1
            if steps > tada_arguments.steps:
                dis.output_message(f"\nQuit due to end of rounds: {steps}", to_print)
                constants.QUIT_BY_STEPS = 1
                break
        big_oh = analysis.analyze_big_oh(ratio)
        if tada_arguments.expect is not None:
            if indicator < tada_arguments.indicator:
                constants.QUIT_BY_INDICATOR = 1
            # store indicator
            constants.INDICATOR_VALUE = tada_arguments.indicator
            # store runningtime
            constants.TOTAL_RUNNING_TIME = time.time() - start_time
            constants.AVG_RUN_TIME = constants.TOTAL_RUNNING_TIME / steps
            last_bench_meta = current_benchmark.get_metadata()
            name = last_bench_meta.get("name")
            # store benchmark metadata
            constants.NAME_OF_EXPERIMENT = configuration.get_experiment_info(
                vars(tada_arguments)
            )
            if "cpu_model_name" in last_bench_meta:
                constants.CPU_TYPE = last_bench_meta.get("cpu_model_name")
            constants.CPU_COUNT = last_bench_meta.get("cpu_count")
            constants.OS = last_bench_meta.get("platform")
            constants.PYTHON_VERSION = last_bench_meta.get("python_version")
            # store run metadata
            with open(
                    constants.RESULTS
                    + constants.SEPARATOR + name + constants.JSON_EXT,
                    "r",
            ) as f:
                readlastjson = json.load(f)
            last_exp_run_metadata = readlastjson["benchmarks"][0]["runs"][0]["metadata"]
            constants.CPU_TEMP = last_exp_run_metadata.get("cpu_temp")
            if "mem_max_rss" in last_exp_run_metadata:
                constants.MEM_MAX_RSS = last_exp_run_metadata["mem_max_rss"]
            else:
                constants.MEM_PEAK_PAGEFILE_USAGE = last_exp_run_metadata[
                    "mem_peak_pagefile_usage"
                ]
            for item in total_loop_list:
                sum_of_loops += item
            # calculate avg total loops
            constants.PYPERF_AVG_EXPERIMENT_ROUNDS = sum_of_loops / len(total_loop_list)
            # calculate last two loop growth ratio
            if len(total_loop_list) >= 2:
                constants.PYPERF_LAST_TWO_EXPERIMENT_ROUNDS = (
                    total_loop_list[-1] / total_loop_list[-2]
                )
            # check if result is expected
            if tada_arguments.expect in analysis.analyze_big_oh(ratio):
                constants.RESULT = 1
            constants.DATA_GEN_STRATEGY = tada_arguments.types
            constants.START_SIZE = tada_arguments.startsize
            constants.INDICATOR_VALUE = tada_arguments.indicator
            # set numerical value to backfill for result storing
            use_backfill = 1 if use_backfill else 0
            # EXPERIMENT_RELIABILITY, CPU_TYPE, CPU_TEMP, TOTAL_RUNNING_TIME,
            # QUIT_BY_MAX_RUNTIME, QUIT_BY_INDICATOR, QUIT_BY_BACKFILL,
            # MEM_MAX_RSS, OS, INDICATOR_VALUE, BACKFILL_TIMES,
            # PYPERF_AVG_EXPERIMENT_ROUNDS, NAME_OF_EXPERIMENT
            df_new = pd.DataFrame(
                {
                    "EXPERIMENT_RELIABILITY": constants.RESULT,
                    "CPU_TYPE": constants.CPU_TYPE,
                    "CPU_TEMP": constants.CPU_TEMP,
                    "CPU_COUNT": constants.CPU_COUNT,
                    "TOTAL_RUNNING_TIME": constants.TOTAL_RUNNING_TIME,
                    "QUIT_BY_MAX_RUNTIME": constants.QUIT_BY_MAX_RUNTIME,
                    "QUIT_BY_INDICATOR": constants.QUIT_BY_INDICATOR,
                    "QUIT_BY_BACKFILL": constants.QUIT_BY_BACKFILL,
                    "QUIT_BY_STEPS": constants.QUIT_BY_STEPS,
                    "QUIT_BY_MAX_SIZE": constants.QUIT_BY_MAX_SIZE,
                    "MEM_MAX_RSS": constants.MEM_MAX_RSS,
                    "MEM_PEAK_PAGEFILE_USAGE": constants.MEM_PEAK_PAGEFILE_USAGE,
                    "OS": constants.OS,
                    "INDICATOR_VALUE": constants.INDICATOR_VALUE,
                    "BACKFILL_TIMES": constants.BACKFILL_TIMES,
                    "PYPERF_AVG_EXPERIMENT_ROUNDS": constants.PYPERF_AVG_EXPERIMENT_ROUNDS,
                    "PYPERF_LAST_TWO_EXPERIMENT_ROUNDS_RATIO":
                        constants.PYPERF_LAST_TWO_EXPERIMENT_ROUNDS_RATIO,
                    "NAME_OF_EXPERIMENT": constants.NAME_OF_EXPERIMENT,
                    "PYTHON_VERSION": constants.PYTHON_VERSION,
                    "DATA_GEN_STRATEGY": constants.DATA_GEN_STRATEGY,
                    "START_SIZE": constants.START_SIZE,
                    "USED_BACKFILL": use_backfill,
                    "AVG_RUN_TIME": constants.AVG_RUN_TIME,
                    "STEPS": steps,
                    "FUNCTION_NAME": tada_arguments.function,
                    "ARGUMENTS": str(vars(tada_arguments)),
                },
                index=[1],
            )
            # store to csv in current directory
            results_file_path = os.path.join(
                constants.SEPARATOR, original_dir, constants.EXPERIMENT
            )
            df_new.to_csv(results_file_path, index=False, header=False, mode="a")
        resultstable.title = dis.blue(f"{tada_arguments.function}: ") + big_oh
        # rest working
        os.chdir(original_dir)
        return resultstable, {tada_arguments.function: result}


def tada_main():
    """main"""
    tada_arg_list = arguments.parse_args(sys.argv[1:])
    resultstables = []
    tada_results = {}
    # display the welcome message
    print(dis.welcome_message())
    # run experiments
    for arg in tada_arg_list:
        table, result = tada(arg)
        resultstables.append(table)
        tada_results.update(result)
        contrast_flag = vars(arg)["contrast"]
        viz_flag = vars(arg)["viz"]
    # display results
    if viz_flag is True:
        tada_configuration_dict = configuration.read(constants.CONFIGURATION)
        chosen_size = read.read_experiment_size()
        results.linegraph_viz(tada_results, tada_configuration_dict, chosen_size)
    for table in resultstables:
        results.display_resultstable(table, tada_arg_list[0].md)
    if len(resultstables) > 1:
        results.compare(*results.greatest_common_size(tada_results))
        if contrast_flag is True:
            results.contrast(tada_results)


if __name__ == "__main__":
    tada_main()
