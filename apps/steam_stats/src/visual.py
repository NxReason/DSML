import matplotlib.pyplot as plt


def prices_boxplot_range(data, genre: str, low: float, high: float):
    fit = data[(data >= low) & (data <= high)]
    prices_boxplot(fit, genre)


def prices_boxplot(data, genre: str):
    plt.boxplot(data)
    plt.ylabel('Price')
    plt.title(f'{genre} game prices')
    plt.show()


def price_hist_range(data, genre: str, low: float, high: float):
    fit = data[(data >= low) & (data <= high)]
    price_hist(fit, genre)


def price_hist(data, genre: str):
    plt.hist(data, bins=40)
    plt.xlabel('Price')
    plt.ylabel('Number of games')
    plt.title(f'{genre} game prices')
    plt.show()
