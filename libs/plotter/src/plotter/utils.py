import matplotlib.pyplot as plt


def make_plot(title: str | None = None, xlabel: str | None = None, ylabel: str | None = None):
    fig, ax = plt.subplots(layout='constrained')

    ax.set(
        title=title,
        xlabel=xlabel,
        ylabel=ylabel
    )

    ax.grid()

    return fig, ax


def limit_to_data(ax, xdata, ydata):
    ax.set(
        xlim=(min(xdata), max(xdata)),
        ylim=(min(ydata), max(ydata)),
    )


def align_bar_chart(ax, x, y):
    max_y, min_y = max(y), min(y)
    delta = max_y - min_y
    ax.set(
        xlim=(x[0] - 0.5, len(x) - 0.5), xticks=x,
        ylim=(min_y, max_y + delta * 0.1)
    )
