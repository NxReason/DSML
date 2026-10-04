import pandas as pd
import numpy as np
import nxmath

# Price
# User score
# Estimated owners
# Peak CCU
# Average playtime forever

DF = pd.DataFrame


# Descriptive statistics
def prices_std(df: DF):
    results = []
    for genre, group in df.groupby('Genre'):
        prices = group['Price']
        results.append({
            'Genre': genre,
            'Std (Pandas)': prices.std(ddof=0),
            'Std (nxmath)': nxmath.std_dev(prices.tolist()),
            'Variance (Pandas)': prices.var(ddof=0),
            'Variance (nxmath)': nxmath.variance(prices.tolist())
        })

    return DF(results)


def prices_std_diff(df: DF):
    diffs = DF({
        'Genre': df['Genre'],
        'Std diff': df['Std (Pandas)'] - df['Std (nxmath)'],
        'Std isclose': np.isclose(df['Std (Pandas)'], df['Std (nxmath)']),
        'Variance diff': df['Variance (Pandas)'] - df['Variance (nxmath)'],
        'Variance isclose': np.isclose(df['Variance (Pandas)'], df['Variance (nxmath)'])
    })
    return diffs


def price_outliers_for(df: DF, genre: str):
    games = of(df, genre)
    prices = games['Price']
    outliers = nxmath.iqr_outliers(prices.tolist())
    games['Outlier'] = outliers
    return games


def price_outliers_perc_for(df: DF, genre: str):
    games = of(df, genre)
    prices = games['Price']
    mask = nxmath.iqr_outliers(prices.tolist())
    outliers = prices[mask]
    print(
        f'Total: {prices.count()}, outliers: {outliers.count()}, [{prices.count() / outliers.count():.2f}%]')


def prices_compare_outliers(df: DF, genre: str):
    games = of(df, genre)

    prices = games['Price']
    iqr_mask = np.array(nxmath.iqr_outliers(prices.tolist()))
    iqr_no_out = games[~iqr_mask]
    std_mask = np.array(nxmath.std_outliers(prices.tolist()))
    std_no_out = games[~std_mask]

    print('Population')
    print(games['Price'].describe())

    print('No outliers (IQR)')
    print(iqr_no_out['Price'].describe())

    print('No outliers (STD)')
    print(std_no_out['Price'].describe())


def prices(df: pd.DataFrame):
    result = []
    for genre, group in df.groupby('Genre'):
        prices = group['Price']
        result.append({
            'Genre': genre,
            'Count': len(prices),
            'Count (paid)': (prices != 0.0).sum(),
            'Max': prices.max(),
            'Min (not free)': prices[prices != 0.0].min(),
            'Mean (Pandas)': prices.mean(),
            'Mean (nxmath)': nxmath.mean(prices.tolist()),
            'Median (Pandas)': prices.median(),
            'Median (nxmath)': nxmath.median(prices.tolist()),
            'Mode (Pandas)': prices.mode().tolist(),
            'Mode (nxmath)': [value for value, _ in nxmath.mode(prices.tolist())]
        })

    return pd.DataFrame(result)


def prices_iqr(df: DF):
    results = []
    for genre, group in df.groupby('Genre'):
        prices = group.loc[group['Price'] != 0.0, 'Price']
        q1 = prices.quantile(0.25)
        q2 = prices.quantile(0.50)
        q3 = prices.quantile(0.75)
        nxq = nxmath.quartiles_linear(prices.tolist())
        nxiqr = None if nxq[0] is None or nxq[2] is None else nxq[2] - nxq[0]
        results.append({
            'Genre': genre,
            'Count': len(prices),
            'Q1 (Pandas)': q1,
            'Q1 (nxmath)': nxq[0],
            'Q2 (Pandas)': q2,
            'Q2 (nxmath)': nxq[1],
            'Q3 (Pandas)': q3,
            'Q3 (nxmath)': nxq[2],
            'IQR (Pandas)': q3 - q1,
            'IQR (nxmath)': nxiqr
        })
    return DF(results)


def prices_diff(df: DF):
    diffs = DF({
        'Genre': df['Genre'],
        'Mean Diff': df['Mean (Pandas)'] - df['Mean (nxmath)'],
        'Mean isclose': np.isclose(df['Mean (Pandas)'], df['Mean (nxmath)']),
        'Median Diff': df['Median (Pandas)'] - df['Median (nxmath)']
    })
    return diffs


def prices_iqr_diff(df: DF):
    diffs = DF({
        'Genre': df['Genre'],
        'IQR Diff': df['IQR (Pandas)'] - df['IQR (nxmath)'],
        'IQR isclose': np.isclose(df['IQR (Pandas)'], df['IQR (nxmath)'])
    })
    return diffs


def most_expensive_f2p(df: pd.DataFrame):
    f2p = of(df, 'Free To Play')
    not_f2p = f2p[f2p['Price'] != 0.0]

    by_price = not_f2p.sort_values('Price', ascending=False)[['Name', 'Price']]
    most_expensive = by_price.head(10)
    print(most_expensive)
    most_expensive.to_csv('../output/most_expensive_f2p.csv')


def of(df: pd.DataFrame, genre: str):
    return df.loc[df['Genre'] == genre]


def make_dataset(df: pd.DataFrame):
    df['Genres'] = df['Genres'].str.split(',')
    return df.explode('Genres')


def list_unique(df: pd.DataFrame) -> set[str]:
    genres = set()

    for value in df['Genres'].dropna():
        for genre in value.split(','):
            genres.add(genre.strip())

    return genres


# out
def print_prices_of(df: pd.DataFrame, genre: str):
    print(f'Prices of {genre}')
    prices = df[df['Genre'] == genre]['Price']
    print('Mean')
    print(f'Pandas: {prices.mean():.2f}')
    print(f'nxmath: {nxmath.mean(prices.tolist()):.2f}')
    print('Median')
    print(f'Pandas: {prices.median():.2f}')
    print(f'nxmath: {nxmath.median(prices.tolist()):.2f}')
    print('Mode')
    print(f'Pandas: {prices.mode()}')
    print(f'nxmath: {nxmath.mode(prices.tolist())}\n')


def print_prices(df: pd.DataFrame):
    groups = df.groupby('Genre')
    for genre, group in groups:
        prices = group['Price']
        print(f'Prices of {genre}')
        print(
            f'Pandas: mean={prices.mean():.2f}, median={prices.median():.2f}')
        print(
            f'nxmath: mean={nxmath.mean(prices.tolist()):.2f}, median={nxmath.median(prices.tolist()):.2f}\n')
