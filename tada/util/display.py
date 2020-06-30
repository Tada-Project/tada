"""Display output for Tada"""


def display_welcome_message() -> None:
    """Display a welcome message"""
    print()
    print("🎆  Tada!: auTomAtic orDer-of-growth Analysis! 🎆 ")
    print("    https://github.com/Tada-Project/tada/")
    print(
        "❓  For Help Information Type: pipenv run python tada_a_bigoh.py -h  ❓"
    )
    print()


def display_start_message(current_size: int, function: str) -> None:
    """Display the start message for an experiment"""
    print(
        f"\nStart running experiment {blue(function)} for size \
{cyan(current_size)} →\n"
    )


def display_end_message(current_size: int, function: str) -> None:
    """Display the end message for an experiment"""
    print(
        f"\n→ Done running experiment {blue(function)} for size \
{cyan(current_size)}\n"
    )


def display_output(timing_output: str, to_print: bool = False) -> None:
    """Display the timing output as long as it is not empty"""
    if (timing_output != "") & (to_print is True):
        print(timing_output)


def green(msg: str) -> str:
    """Display messages in green"""
    return f"{FontColor.Green}{msg}{FontColor.Reset}"


def blue(msg: str) -> str:
    """Display messages in blue"""
    return f"{FontColor.Blue}{msg}{FontColor.Reset}"


def cyan(msg: int) -> str:
    """Display messages in cyan"""
    return f"{FontColor.Cyan}{msg}{FontColor.Reset}"


def magenta(msg: str) -> str:
    """Display messages in magenta"""
    return f"{FontColor.Magenta}{msg}{FontColor.Reset}"


def red(msg: str) -> str:
    """Display messages in red"""
    return f"{FontColor.Red}{msg}{FontColor.Reset}"


class FontColor:  # pylint: disable=too-few-public-methods
    """ansi code for color print"""

    Green = "\u001b[32m\u001b[1m"
    Blue = "\u001b[34m\u001b[1m"
    Magenta = "\u001b[35m\u001b[1m"
    Cyan = "\u001b[36m\u001b[1m"
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Yellow = "\u001b[33m"
    White = "\u001b[37m"
    Reset = "\u001b[0m"
    Bold = "\u001b[1m"
    Underline = "\u001b[4m"
