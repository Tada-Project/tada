"""Display output for Tada"""


def display_welcome_message():
    """Display a welcome message"""
    print()
    print("🎆  Tada!: auTomAtic orDer-of-growth Analysis! 🎆 ")
    print("    https://github.com/Tada-Project/tada/")
    print(
        "❓  For Help Information Type: pipenv run python tada_a_bigoh.py -h  ❓"
    )
    print()


def display_start_message(current_size, function):
    """Display the start message for an experiment"""
    print(
        f"\nStart running experiment \
{FontColor.Blue}{function}{FontColor.Reset} for size \
{FontColor.Cyan}{current_size}{FontColor.Reset} →\n"
    )


def display_end_message(current_size, function):
    """Display the end message for an experiment"""
    print(
        f"\n→ Done running experiment \
{FontColor.Blue}{function}{FontColor.Reset} for size \
{FontColor.Cyan}{current_size}{FontColor.Reset} \n"
    )


def display_output(timing_output, to_print=False):
    """Display the timing output as long as it is not empty"""
    if (timing_output != "") & (to_print is True):
        print(timing_output)


class FontColor:
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Green = "\u001b[32m\u001b[1m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m\u001b[1m"
    Magenta = "\u001b[35m\u001b[1m"
    Cyan = "\u001b[36m\u001b[1m"
    White = "\u001b[37m"
    Reset = "\u001b[0m"
    Bold = "\u001b[1m"
    Underline = "\u001b[4m"
