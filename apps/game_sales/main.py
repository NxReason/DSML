import csv

from df import DataFrame
import plat

import nxmath

# 0 Name
# 1 Platform
# 2 Year_of_Release
# 3 Genre
# 4 Publisher
# 5 NA_Sales
# 6 EU_Sales
# 7 JP_Sales
# 8 Other_Sales
# 9 Global_Sales
# 10 Critic_Score
# 11 Critic_Count
# 12 User_Score
# 13 User_Count
# 14 Developer
# 15 Rating


def main():
    with open('./data/sales.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)

        df = DataFrame(next(reader))
        for row in reader:
            df.data.append(row)

        plat.overview(df)


if __name__ == "__main__":
    main()
