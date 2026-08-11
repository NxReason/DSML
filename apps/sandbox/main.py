import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import nxmath
import plotter
import numpy as np

from collections import Counter
import math


def main():
    values = [4, 8, 15, 16, 23, 42]
    print(nxmath.mean(values))
    print(nxmath.std_dev(values))
    print(nxmath.z_score(values, 30))


if __name__ == "__main__":
    main()
