"""Resultstable for Tada and perf"""



def add_resultstable(resultstable, current_size, mean, median):
    resultstable.add_row([current_size, mean, median])

def display_resultstable(resultstable):
    print(resultstable)
