"""Results Table for Tada and perf."""

def add_resultstable(resultstable, current_size, mean, median, ratio):
    """Add elements into the resultstable."""
    resultstable.add_row([current_size, mean, median, ratio])

    
def display_resultstable(resultstable):
    """Print out the resultstable."""
    print(resultstable)
