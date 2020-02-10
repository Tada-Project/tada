"""Run doubling experiments and 'Tada!' you get the time complexity"""

import sys
import time
import pandas as pd
import pyperf
import json
from prettytable import PrettyTable


from tada.util import analysis
from tada.util import arguments
from tada.util import configuration
from tada.util import constants
from tada.util import display
from tada.util import generate
from tada.util import package
from tada.util import read
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
    resultstable = PrettyTable(["Size", "Mean", "Median", "Ratio"])
    meanlastround = 0
    indicator = 0
    steps = constants.STEP_START
    last_last_size = 0
    count = 0
    current_size = tada_arguments.startsize
    total_loop_list = []
    sum_of_loops = 0
    used_backfill = tada_arguments.backfill
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
        while True:
            if used_backfill == 1:
                # run the benchmark by using it through python
                used_backfill = 1
                analysis.backfill_checker(last_last_size, current_size)
                if constants.BACKFILL_TIMES == 2:
                    constants.QUIT_BY_BACKFILL = 1
                    print("Quit due to two backfills")
                    break
            if "hypothesis" in tada_arguments.types[0]:
                if current_size >= tada_arguments.maxsize:
                    constants.QUIT_BY_MAX_SIZE = 1
                    print("Quit due to researched max size")
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
            # Numbers of benchmark run which include one warmup and twenty excution
            # print(current_benchmark.get_nrun())
            # Total Runtime of the benchmark excution
            # print(current_benchmark.get_total_duration())
            total_loop_list.append(current_benchmark.get_total_loops())
            # perform additional analysis of the results
            # reminder: print('Values {0}'.format(current_benchmark.get_values()))
            mean = current_benchmark.mean()
            print("Mean {0}".format(mean))
            median = current_benchmark.median()
            print("Median {0}".format(median))
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
            if last_end_time_rate > end_time_rate and used_backfill == 1:
                current_size = int(current_size / constants.FACTOR)
            else:
                current_size = current_size * constants.FACTOR
            # check indicator and quit if smaller than decided indicator
            if indicator < tada_arguments.indicator:
                print("Quit due to indicator: ", indicator)
                break
            save.save_experiment_size(constants.SIZE, current_size)
            meanlastround = mean
            current_runningtime = time.time() - start_time
            if current_runningtime > tada_arguments.runningtime:
                print("Quit due to over maximum time:", current_runningtime)
                constants.QUIT_BY_MAX_RUNTIME = 1
                break
            steps += 1
            if steps > tada_arguments.steps:
                print("Quit due to end of rounds: ", steps)
                constants.QUIT_BY_STEPS = 1
                break
        results.display_resultstable(resultstable)
        print(analysis.analyze_big_oh(ratio))
        if indicator < tada_arguments.indicator:
            constants.QUIT_BY_INDICATOR = 1
        # store indicator
        constants.INDICATOR_VALUE = tada_arguments.indicator
        # store runningtime
        constants.TOTAL_RUNNING_TIME = time.time() - start_time
        constants.AVG_RUN_TIME = constants.TOTAL_RUNNING_TIME / steps
        last_bench_meta = current_benchmark.get_metadata()
        name = last_bench_meta["name"]
        # store benchmark metadata
        constants.NAME_OF_EXPERIMENT = configuration.get_experiment_info(
            vars(tada_arguments)
        )
        if "cpu_model_name" in last_bench_meta:
            constants.CPU_TYPE = last_bench_meta["cpu_model_name"]
        constants.CPU_COUNT = last_bench_meta["cpu_count"]
        constants.OS = last_bench_meta["platform"]
        constants.PYTHON_VERSION = last_bench_meta["python_version"]
        # store run metadata
        with open(
            "_results" + constants.SEPARATOR + name + constants.JSON_EXT, "r"
        ) as f:
            readlastjson = json.load(f)
        last_exp_run_metadata = readlastjson["benchmarks"][0]["runs"][0]["metadata"]
        if "cpu_temp" in last_exp_run_metadata:
            constants.CPU_TEMP = last_exp_run_metadata["cpu_temp"]
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
        if (
            tada_arguments.expect is not None
            and tada_arguments.expect in analysis.analyze_big_oh(ratio)
        ):
            constants.RESULT = 1
        constants.DATA_GEN_STRATEGY = tada_arguments.types
        constants.START_SIZE = tada_arguments.startsize
        constants.INDICATOR_VALUE = tada_arguments.indicator
        df = pd.read_csv("experiment_data.csv")
        # EXPERIMENT_RELIABILITY, CPU_TYPE, CPU_TEMP, TOTAL_RUNNING_TIME, QUIT_BY_MAX_RUNTIME, QUIT_BY_INDICATOR, QUIT_BY_BACKFILL, MEM_MAX_RSS, OS, INDICATOR_VALUE, BACKFILL_TIMES, PYPERF_AVG_EXPERIMENT_ROUNDS, NAME_OF_EXPERIMENT
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
                "PYPERF_LAST_TWO_EXPERIMENT_ROUNDS_RATIO": constants.PYPERF_LAST_TWO_EXPERIMENT_ROUNDS_RATIO,
                "NAME_OF_EXPERIMENT": constants.NAME_OF_EXPERIMENT,
                "PYTHON_VERSION": constants.PYTHON_VERSION,
                "DATA_GEN_STRATEGY": constants.DATA_GEN_STRATEGY,
                "START_SIZE": constants.START_SIZE,
                "USED_BACKFILL": used_backfill,
                "AVG_RUN_TIME": constants.AVG_RUN_TIME,
                "STEPS": steps,
            },
            index=[1],
        )
        # store to csv
        if tada_arguments.expect is not None:
            df_new.to_csv("experiment_data.csv", index=False, header=False, mode="a")
