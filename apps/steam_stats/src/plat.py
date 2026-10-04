import pandas as pd


def separate(df: pd.DataFrame):
    win = df[df['Windows'] == True]
    mac = df[df['Mac'] == True]
    linux = df[df['Linux'] == True]
    return (win, mac, linux)


def available(df: pd.DataFrame):
    total = len(df)
    win = df[df['Windows'] == True]
    mac = df[df['Mac'] == True]
    linux = df[df['Linux'] == True]

    print('Available on:')
    print(f'Windows: {len(win) / total:.4f}')
    print(f'Mac: {len(linux) / total:.4f}')
    print(f'Linux: {len(mac) / total:.4f}')


def avg_price(df: pd.DataFrame):
    win, mac, linux = separate(df)
    print('Average price on:')

    print(f'Windows: {win['Price'].mean():.2f}')
    print(f'Linux: {linux['Price'].mean():.2f}')
    print(f'Mac: {mac['Price'].mean():.2f}')
