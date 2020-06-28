"""Analysis experiments for Tada"""


def analyze_big_oh(ratio: float) -> str:
    """analyze big oh"""
    if 0 <= ratio < 1.5:
        output = "O(1) constant or O(logn) logarithmic"
    elif 1.5 <= ratio < 3:
        output = "O(n) linear or O(nlogn) linearithmic"
    elif 3 <= ratio < 5:
        output = "O(n^2) quadratic"
    elif 5 <= ratio < 10:
        output = "O(n^3) cubic"
    else:
        output = "O(c^n) exponential"
    return output
