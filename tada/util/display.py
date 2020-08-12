"""Display output for Tada"""

from colorama import init, Fore, Style

init(autoreset=True)


def welcome_message() -> None:
    """Display a welcome message"""
    return "\n\t\tTada!: auTomAtic orDer-of-growth Analysis!\n\t\t  \
https://github.com/Tada-Project/tada/\n\t  For Help Information Type: \
python tada_a_bigoh.py -h"


def start_message(current_size: int, function: str) -> None:
    """Display the start message for an experiment"""
    return f"\nStart running experiment {blue(function)} for size \
{cyan(current_size)} →\n"


def end_message(current_size: int, function: str) -> None:
    """Display the end message for an experiment"""
    return f"\n→ Done running experiment {blue(function)} for size \
{cyan(current_size)}\n"


def output_message(timing_output: str, to_print: bool = False) -> None:
    """Display the timing output as long as it is not empty"""
    if (timing_output != "") & (to_print is True):
        print(timing_output)
        print_out = True
    else:
        print_out = False
    return print_out


def green(msg: str) -> str:
    """Display messages in green"""
    return f"{Fore.GREEN + Style.BRIGHT}{msg}{Style.RESET_ALL}"


def blue(msg: str) -> str:
    """Display messages in blue"""
    return f"{Fore.BLUE + Style.BRIGHT}{msg}{Style.RESET_ALL}"


def cyan(msg: int) -> str:
    """Display messages in cyan"""
    return f"{Fore.CYAN + Style.BRIGHT}{msg}{Style.RESET_ALL}"


def magenta(msg: str) -> str:
    """Display messages in magenta"""
    return f"{Fore.MAGENTA + Style.BRIGHT}{msg}{Style.RESET_ALL}"


def red(msg: str) -> str:
    """Display messages in red"""
    return f"{Fore.RED + Style.BRIGHT}{msg}{Style.RESET_ALL}"
