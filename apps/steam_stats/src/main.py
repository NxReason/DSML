import time
import pandas as pd
from pathlib import Path

import genre
import visual


def read_source_df():
    SOURCE_PATH = '../data/games.parquet'
    return pd.read_parquet(SOURCE_PATH)


def read_genre_df():
    GENRE_PATH = '../data/games_by_genre.parquet'
    return pd.read_parquet(GENRE_PATH)


def main():
    df = read_genre_df()
    genre.prices_compare_outliers(df, 'RPG')


def print_all(df):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(df)
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')


if __name__ == "__main__":
    main()


def to_parquet(filepath: str):
    path = Path(filepath)
    save_file = path.with_suffix('.parquet')

    df = pd.read_csv('../data/games.csv')
    df.to_parquet(save_file)


def print_ex_time(fn, msg: str = ''):
    start = time.perf_counter()
    fn()
    end = time.perf_counter()
    elapsed = f'{end - start:.4f}'
    print(f'{msg}: {elapsed}' if msg else elapsed)
