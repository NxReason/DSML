import pandas as pd
import matplotlib.pyplot as plt


def clean():
    df = pd.read_csv("./data/sales.csv")

    df['User_Score'] = pd.to_numeric(df['User_Score'], errors='coerce')

    df.to_csv('./data/sales_clean.csv', index=False)


def read():
    df = pd.read_csv("./data/sales_clean.csv")

    data = df.loc[df['User_Score'].notna(), ['Name', 'Genre', 'User_Score']].sort_values(
        'User_Score', ascending=False)
    print(data)

    print(df.Genre.unique())
