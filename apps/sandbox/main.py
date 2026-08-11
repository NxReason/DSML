import matplotlib.pyplot as plt

import nxmath
import plotter
import numpy as np


import math


def main():
    grades = {
        (50, 56.5): 1,
        (56.5, 62.5): 0,
        (62.5, 68.5): 4,
        (68.5, 74.5): 4,
        (74.5, 80.5): 2,
        (80.5, 86.5): 3,
        (86.5, 92.5): 4,
        (92.5, 98.5): 1,
    }
    print(nxmath.interval_mean(grades))


if __name__ == "__main__":
    main()
