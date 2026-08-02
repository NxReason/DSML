import random
import numpy as np
from numpy.typing import NDArray

import matplotlib.pyplot as plt


def desc_npa(a: NDArray):
    print('Data type:', a.dtype)
    print('N-dimensions:', a.ndim)
    print('Shape:', a.shape)
    print('Number of elements:', a.size)


def main():
    a = np.linspace(-30, 30, 61)
    squares = np.square(a)
    desc_npa(a)
    print(a)

    fig, ax = plt.subplots()
    x = np.arange(-30, 31)
    ax.plot(x, a)
    ax.plot(x, squares)

    ax.grid()

    plt.yscale('symlog', base=2)
    plt.show()


if __name__ == "__main__":
    main()
