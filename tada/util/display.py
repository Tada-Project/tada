"""Display output for Tada"""


def display_start_message(size):
    """Display the start message for an experiment"""
    print("Start running experiment for size " + str(size) + " →\n")


def display_output(timing_output):
    """Display the timing output as long as it is not empty"""
    if timing_output != "":
        print(timing_output)
