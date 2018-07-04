"""Display output for Tada"""


def welcome_message():
    """Display a welcome message"""
    print()
    print(
        "✨ Tada!: auTomAtic orDer of growth Analysis!"
    )
    print("https://github.com/gkapfham/tada")
    print()


def start_message(current_size):
    """Display the start message for an experiment"""
    print("Start running experiment for size " + str(current_size) + " →\n")


def display_end_message(current_size):
    """Display the end message for an experiment"""
    print("→ Done running experiment for size " + str(current_size) + "\n")


def display_output(timing_output):
    """Display the timing output as long as it is not empty"""
    if timing_output != "":
        print(timing_output)
