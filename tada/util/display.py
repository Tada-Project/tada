"""Display output for Tada"""


def display_welcome_message():
    """Display a welcome message"""
    print()
    print("🎆  Tada!: auTomAtic orDer-of-growth Analysis! 🎆 ")
    print("    https://github.com/Tada-Project/tada/")
    print("❓  For Help Information Type: pipenv run python tada_a_bigoh.py -h  ❓")
    print()


def display_start_message(current_size):
    """Display the start message for an experiment"""
    print("\nStart running experiment for size " + str(current_size) + " →\n")


def display_end_message(current_size):
    """Display the end message for an experiment"""
    print("\n→ Done running experiment for size " + str(current_size) + "\n")


def display_output(timing_output, to_print=False):
    """Display the timing output as long as it is not empty"""
    if (timing_output != "") & (to_print is True):
        print(timing_output)
