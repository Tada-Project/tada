"""Analysis experiments for Tada"""


def analyze_big_oh(ratio):
    if (0 <= ratio < 1.5):
        print("constant or logarithmic")
    elif (1.5 <= ratio < 3):
        print("linear or linearithmic")
    elif (3 <= ratio < 5):
        print("quadratic")
    elif (5<= ratio < 10):
        print("cubic")
    else:
        print("exponential")
