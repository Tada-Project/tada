"""Analysis for Tada and perf"""

import json
import perf

from . import constants

Analysis = sys.modules[__name__]

details = {}
result_count = 0

FIRST = 0

OUTCOME = "outcome"
DIAGNOSTIC = "diagnostic"

TEXT = "output_text"
JSON = "output_json"

ARROW = "➔"
EMPTY_STRING = ""
NEWLINE = "\n"
SPACE = " "
TAB = "   "


def create_analysis(outcome, diagnostic):
    """Create a new analysis"""
    analysis_dictionary = {}
    analysis_dictionary[OUTCOME] = outcome
    analysis_dictionary[DIAGNOSTIC] = diagnostic
    return analysis_dictionary


def reset():
    """Reset the details dictionary and the count"""
    # pylint: disable=global-statement
    global details
    global result_count
    details = {}
    result_count = 0


def add_analysis(outcome, diagnostic):
    """Add a new result to the details dictionary"""
    # pylint: disable=global-statement
    global result_count
    global details
    new_result = create_result(outcome, diagnostic)
    details[result_count] = new_result
    new_result_count = result_count
    result_count = result_count + 1
    return new_result_count, new_result


def get_details():
    """Return the details dictionary"""
    return details


def get_detail(index):
    """Return a result from the details dictionary"""
    return details[index]


def get_size():
    """Return the size of the details dictionary"""
    return len(details)


def output(output_as_list):
    """Return the output that the list would produce"""
    if configurarion.is_json(output_as_list[FIRST]):
        produced_output = SPACE.join(output_as_list)
    else:
        produced_output = NEWLINE.join(output_as_list)
    return produced_output


def output_list(dictionary_result, dictionary_format=TEXT):
    """Return the output list that the dictionary would produce"""
    output_function = getattr(REPORT, dictionary_format)
    created_output_list = []
    output_function(dictionary_result, created_output_list)
    return created_output_list


'''
def form_single_output_line(outcome, diagnostic):
    """Produce a single line of output in a textual format"""
    # there is a diagnostic, so include it on the next line
    if diagnostic is not EMPTY_STRING:
        submitted = (
            measure_performance(outcome)
            + SPACE
            + NEWLINE
            + TAB
            + ARROW
            + SPACE
            + diagnostic
        )
    # there is no diagnostic, so do not include anything else
    else:
        submitted = measure_performance(outcome) + SPACE + diagnostic
    return submitted
'''

'''
def measure_performance(dictinput, function, ???, ???)
    runner.bench_time_func('dict[str]', bench_dict, mydict, inner_loops=10)
'''
