"""Resultstable for Tada and perf"""

def add_resultstable(resultstable, current_size, mean, median):
    """Add stuff into the resultstable"""
    resultstable.add_row([current_size, mean, median])

def display_resultstable(resultstable):
    """Print out resultstable"""
    print(resultstable)
