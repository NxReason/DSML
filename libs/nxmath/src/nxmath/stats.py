from collections import Counter
import math


# finding descriptive stats for a list of values
def mean(data):
    if len(data) == 0:
        return None
    return sum(data) / len(data)


def median(data) -> float | None:
    if len(data) == 0:
        return None

    d_sorted = sorted(data)
    is_odd = len(data) % 2 == 1
    middle = len(data) // 2
    if is_odd:
        return d_sorted[middle]
    else:
        return (d_sorted[middle] + d_sorted[middle - 1]) / 2


def mode(data):
    counts = {}
    for val in data:
        if val not in counts:
            counts[val] = 0
        counts[val] += 1

    counts_sorted = dict(sorted(
        counts.items(),
        key=lambda pair: pair[1],
        reverse=True
    ))

    result = []
    max_count = None
    for val, count in counts_sorted.items():
        if max_count is None:
            max_count = count
            result.append((val, count))
            continue

        if count != max_count:
            break

        result.append((val, count))

    return result


def percentile(data, perc: float):
    if perc > 1.0:
        perc /= 100
    d_sorted = sorted(data)
    idx = perc * (len(data) + 1) - 1
    low, high = math.floor(idx), math.ceil(idx)
    return (d_sorted[low] + d_sorted[high]) / 2


def percentile_of_value(data, value):
    if value not in data:
        return None

    d_sorted = sorted(data)
    dups_count = len([v for v in d_sorted if v == value])
    idx = d_sorted.index(value)

    return round(
        (idx + 0.5 * dups_count) / len(d_sorted),
        2
    )


def quartiles(data):
    d_sorted = sorted(data)
    second = median(d_sorted)

    middle = len(d_sorted) / 2
    lower, upper = math.floor(middle), math.ceil(middle)

    first = median(d_sorted[0:lower])
    third = median(d_sorted[upper:])

    return first, second, third


def iqr(data):
    first, _, third = quartiles(data)
    if first is None or third is None:
        return None
    return third - first


def outliers(data):
    first, _, third = quartiles(data)
    if first is None or third is None:
        return None
    d_iqr = third - first

    low = first - 1.5 * d_iqr
    high = third + 1.5 * d_iqr
    return [(i, val) for i, val in enumerate(data) if val < low or val > high]


def interval_mean(data):
    value_total = 0
    entry_count = 0
    for inter, freq in data.items():
        value_total += ((inter[0] + inter[1]) / 2) * freq
        entry_count += freq

    return value_total / entry_count if entry_count != 0 else None


# data transformations
def build_stem_table(values, div=10):
    stems = {}
    for v in values:
        stem = v // div
        leaf = v % div
        stems.setdefault(stem, []).append(leaf)
    return stems


def show_stem_table(stem_table):
    print('-' * 20)
    for stem in sorted(stem_table.keys()):
        leafs = stem_table[stem]
        print(stem, end='  |  ')
        for l in leafs:
            print(l, end=', ')
        print('\n' + '-' * 20)


def rel_frequency(data):
    total = sum(data)
    return [x / total for x in data]
