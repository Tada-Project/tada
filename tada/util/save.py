"""Run entities for Tada"""


def save_configuration(configurationfile, current_size):
    """Save the current size configuration for the experiment to a file"""
    with open(configurationfile, "w") as file_pointer:
        file_pointer.write(str(current_size))
