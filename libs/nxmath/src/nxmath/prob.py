# binomial distribution
def binom(total: int, success_rate: float):
    out = {}
    for i in range(total + 1):
        out[i] = binom_pmf(total, i, success_rate)
    return out


def binom_le(n: int, success_rate: float, value: int):
    total = 0
    data = binom(n, success_rate)
    for i in range(value + 1):
        total += data[i]
    return total


def binom_pmf(total: int, success_n: int, success_rate: float):
    failure_rate = 1 - success_rate
    failure_n = total - success_n
    return combinations(total, success_n) * (success_rate ** success_n) * (failure_rate ** failure_n)


# geometric distribution
def geom(n: int, success_rate: float):
    dist = {}
    for i in range(1, n + 1):
        dist[i] = geom_pmf(i, success_rate)
    return dist


def geom_pmf(n: int, success_rate: float):
    failure_rate = 1 - success_rate
    return failure_rate ** (n - 1) * success_rate


# utils
def combinations(n: int, exp: int) -> int:
    return int(factorial(n) / (factorial(exp) * factorial(n - exp)))


def factorial(value: int) -> int:
    if value == 0:
        return 1

    result = 1
    for i in range(2, value + 1):
        result *= i

    return result
