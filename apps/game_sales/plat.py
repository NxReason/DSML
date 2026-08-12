from df import DataFrame
from utils import *
import nxmath


def overview(df: DataFrame):
    c = counts(df, order=SortingOrder.DESC)

    platforms = ['PC', 'PS3', 'X360', 'DS']
    ratings = avg_ratings(df, platforms)
    ratings_title = f'Ratings for {', '.join(platforms)}'

    best = best_games_on(df, names=['PC', 'PS3', 'X360'])

    q = quarts_on(df, platforms)

    devs = std_dev_on(df, platforms)

    save_report('platform.txt', {
        f'Standard deviations for {', '.join(platforms)}': devs,
        f'Quartiles for {', '.join(platforms)}': q,
        ** {f'Best games on {plat}': rep for plat, rep in best.items()},
        ratings_title: ratings,
        'Counts': c
    })


def counts(df: DataFrame, order: SortingOrder = SortingOrder.NONE) -> dict[str, int]:
    platforms = df['Platform']
    plat_counts = {}

    for plat in platforms:
        if plat not in plat_counts:
            plat_counts[plat] = 0
        plat_counts[plat] += 1

    match (order):
        case SortingOrder.DESC:
            plat_counts = dict(sorted(plat_counts.items(),
                               key=lambda item: item[1], reverse=True))
        case SortingOrder.ASC:
            plat_counts = dict(
                sorted(plat_counts.items(), key=lambda item: item[1]))

    return plat_counts


# tops
def best_games_on(df: DataFrame, count: int = 10, names: list[str] = []):
    out = {}
    for name in names:
        out[name] = best_games(df.filter_by('Platform', name), count)
    return out


def best_games(df: DataFrame, count: int = 10) -> dict[str, str]:
    filtered = [row for row in df.data if row[12] not in ['tbd', '']]
    from_top = sorted(filtered, key=lambda row: float(row[12]), reverse=True)
    out = {}
    for row in from_top[:count]:
        out[row[0]] = row[12]

    return out


# deviation
def std_dev_on(df: DataFrame, names: list[str]):
    return {
        name: std_dev(df.filter_by('Platform', name))
        for name in names
    }


def std_dev(df: DataFrame):
    values = [float(row[12])
              for row in df.data if row[12] not in ['tbd', '']]
    return nxmath.std_dev(values)


# quartiles
def quarts_on(df: DataFrame, names: list[str]):
    return {
        name: quarts(df.filter_by('Platform', name))
        for name in names
    }


def quarts(df: DataFrame):
    filtered = [float(row[12])
                for row in df.data if row[12] not in ['tbd', '']]
    return nxmath.quartiles(filtered), nxmath.iqr(filtered)


# describe by platform
def avg_ratings(df: DataFrame, names: list[str]) -> dict[str, str]:
    targets = {name: "" for name in names}

    for name in names:
        r, tbd, empty = avg_rating(df.filter_by('Platform', name))
        mode = r.mode[0][0]
        targets[name] = f'avg [{f_value(r.avg)}] / median [{f_value(r.median)}] / mode [{f_value(mode)}] / tbd [{f_value(tbd)}] / empty [{f_value(empty)}]'

    return targets


def avg_rating(df: DataFrame):
    col = df['User_Score']

    tbd = 0
    empty = 0
    values = []
    for val in col:
        match val.lower():
            case 'tbd':
                tbd += 1
            case '':
                empty += 1
            case _:
                num_value = float(val)
                values.append(num_value)

    avg = nxmath.mean(values)
    median = nxmath.median(values)
    mode = nxmath.mode(values)
    report = Report(avg, median, mode)
    return report, tbd, empty


def f_value(value):
    match value:
        case int(val):
            return f'{val:4}'
        case float(val):
            return f'{val:4.2f}'
        case _:
            return value
