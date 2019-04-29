"""Analysis experiments for Tada"""


def analyze_big_oh(ratio):
    """analyze big oh"""
    if (0 <= ratio < 1.5):
        output = "constant or logarithmic"
    elif (1.5 <= ratio < 3):
        output = "linear or linearithmic"
    elif (3 <= ratio < 5):
        output = "quadratic"
    elif (5 <= ratio < 10):
        output = "cubic"
    else:
        output = "exponential"
    print(output)
