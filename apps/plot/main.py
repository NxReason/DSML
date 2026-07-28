from plotter.utils import make_plot
from plotter.themes import use_amethyst_theme
import matplotlib.pyplot as plt
import random


def plot_something():
    fig, ax = make_plot(title="Plot", xlabel="dates", ylabel="values")

    x = [x for x in range(10)]
    y1 = [y for y in range(10, 20)]
    y2 = [random.randrange(0, 20) for _ in range(10)]
    y3 = [random.randrange(0, 20) for _ in range(10)]
    y4 = [random.randrange(0, 20) for _ in range(10)]
    y5 = [random.randrange(0, 20) for _ in range(10)]
    ax.plot(x, y1)
    ax.plot(x, y2)
    ax.plot(x, y3)
    ax.plot(x, y4)
    ax.plot(x, y5)

    # fig.savefig('test.png')
    plt.show()


def scatter_something():
    fig, ax = make_plot(title="Scatter", xlabel="dates", ylabel="values")
    x = [random.randrange(1, 100) for _ in range(10)]
    y = [random.randrange(1, 100) for _ in range(10)]
    ax.scatter(x, y)
    ax.set(
        xlim=(0, 100),
        ylim=(0, 100)
    )
    plt.show()


def bar_something():
    fig, ax = make_plot(title="Bar", xlabel="dates", ylabel="values")

    x = [x for x in range(10)]
    y = [random.randrange(1, 250) for _ in range(10)]
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(
        xlim=(x[0] - 0.5, len(x) - 0.5), xticks=x,
        ylim=(0, 100)
    )

    plt.show()


def pie_something():
    fig, ax = make_plot("Pie")
    x = [random.randrange(0, 50) for _ in range(4)]
    y = ['foo', 'bar', 'baz', 'ing']
    ax.pie(x, labels=y, autopct="%1.1f%%",
           textprops={"color": "white"},
           wedgeprops={"linewidth": 1, "edgecolor": "white"})
    plt.show()


def main():
    use_amethyst_theme()
    pie_something()


if __name__ == "__main__":
    main()
