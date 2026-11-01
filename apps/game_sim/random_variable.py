import statistics
import random
import math


class DRV:
    def __init__(self, drv: dict[int, float]):
        self.drv = drv

    def validate(self):
        total = 0.0
        epsilon = 0.000001
        for value in self.drv.values():
            if value < 0 or value > 1:
                return False
            total += value
        return abs(total - 1.0) < epsilon

    def calculate(self, predicate) -> float:
        probability = 0.0
        for key, value in self.drv.items():
            if predicate(key):
                probability += value
        return probability

    def probability_of(self, value: int) -> float:
        if value in self.drv:
            return self.drv[value]
        return 0.0

    def ev(self) -> float:
        ev = 0.0
        for key, value in self.drv.items():
            ev += key * value
        return ev

    def variance(self) -> float:
        var = 0.0
        ev = self.ev()
        for value, prob in self.drv.items():
            var += (value - ev) ** 2 * prob
        return var

    def std(self) -> float:
        return math.sqrt(self.variance())

    def get_value(self) -> int:
        rnd = random.random()
        total = 0.0
        for key, value in self.drv.items():
            total += value
            if rnd < total:
                return key
        return 0

    def get_total_prob(self) -> float:
        total = 0.0
        for prob in self.drv.values():
            total += prob
        return total


def random_var_run():
    drv = DRV({
        1: 0.1,
        2: 0.2,
        3: 0.4,
        4: 0.2,
        5: 0.1
    })
    print(drv.validate())

    print(drv.calculate(lambda val: val == 3))
    print(drv.calculate(lambda val: val >= 4))
    print(drv.calculate(lambda val: val % 2 == 0))


def pmf_run():
    gold_drops = DRV({
        0: 0.5,
        10: 0.25,
        25: 0.15,
        100: 0.1
    })
    print(gold_drops.validate())

    print('25 gold:', gold_drops.probability_of(25))
    print('at least 10 gold:', gold_drops.calculate(lambda val: val >= 10))
    print('10 <= x <= 25', gold_drops.calculate(
        lambda val: 10 <= val <= 25))


# expected value
def sim_opening(chest: DRV):
    total = 0
    trials = 100_000
    for _ in range(trials):
        total += chest.get_value()
    print('Sim value:', total / trials)


def expected_value_run():
    chest_1 = DRV({
        0: 0.5,
        10: 0.25,
        25: 0.15,
        100: 0.1
    })
    print(chest_1.validate())

    print(chest_1.ev())  # 16.25

    chest_2 = DRV({
        0: 0.7,
        20: 0.2,
        100: 0.1
    })
    print(chest_2.validate())
    print(chest_2.ev())
    # diff
    print(chest_1.ev() - chest_2.ev())
    # per 1000 chests
    print(chest_1.ev() * 1000)
    print(chest_2.ev() * 1000)

    sim_opening(chest_1)


# variance and std
def sim_var_and_std(drv: DRV):
    trials = 100_000
    values = []
    for _ in range(trials):
        values.append(drv.get_value())

    m = sum(values) / trials
    print('Sim mean:', m)

    variance = 0.0
    for val in values:
        variance += (val - m) ** 2
    variance /= trials

    print('Sim variance:', variance)
    print('Sim std:', math.sqrt(variance))


def var_and_std_run():
    weapon_a = DRV({6: 1.0})
    weapon_b = DRV({
        2: 0.5,
        10: 0.5
    })

    chest = DRV({
        0: 0.5,
        10: 0.25,
        25: 0.15,
        100: 0.1
    })

    print('w1 variance:', weapon_a.variance())
    print('w1 std:', weapon_a.std())

    print('w2 variance:', weapon_b.variance())
    print('w2 std:', weapon_b.std())

    print('chest variance:', chest.variance())
    print('chest std:', chest.std())

    sim_var_and_std(chest)


# Bernoulli
def sim_bernoulli(dist: DRV):
    trials = 100_000
    crits = 0
    for _ in range(trials):
        val = dist.get_value()
        if val == 1:
            crits += 1
    perc = crits / trials
    print(
        f'Sim percentage: {perc:.5f}, delta to theoretical: {dist.ev() - perc:.5f}')


def bernoulli_run():
    crit_10 = DRV({
        0: .90,
        1: .10
    })
    crit_50 = DRV({
        0: .50,
        1: .50
    })
    crit_90 = DRV({
        0: .10,
        1: .90
    })
    distribs = {
        'crit 10': crit_10,
        'crit 50': crit_50,
        'crit 90': crit_90,
    }
    for name, dist in distribs.items():
        print(name)
        print('EV:', dist.ev())
        print('Var:', dist.variance())
        print('Std:', dist.std())
        sim_bernoulli(dist)


# Binomial
def gen_binom_dist(n: int, p: float) -> DRV:
    dist_dict = {}
    for k in range(n + 1):
        comb = math.comb(n, k)
        success_total_prob = p ** k
        failure_total_prob = (1 - p) ** (n - k)
        dist_dict[k] = comb * success_total_prob * failure_total_prob
    return DRV(dist_dict)


def binom_stats(dist: DRV, p: float):
    n = len(dist.drv) - 1
    print('EV:', n * p)
    var = n * p * (1 - p)
    print('Var:', var)
    print('Std:', math.sqrt(var))


def sim_binomial_dist(dist: DRV, p: float):
    trials = 100_000
    group_n = len(dist.drv) - 1

    sims = []
    for _ in range(trials):
        group = []
        for _ in range(group_n):
            val = random.random()
            group.append(1 if val < p else 0)
        sims.append(group)

    sim_results = {}
    for i in range(group_n + 1):
        sim_results[i] = 0

    for sim in sims:
        success_n = sum(sim)
        sim_results[success_n] += 1

    for value, count in sim_results.items():
        print(
            f'Crits {value}, sim {count / trials}, dist {dist.probability_of(value)}')


def binomial_dist_run():
    dist = gen_binom_dist(6, 0.25)
    print(dist.validate())
    binom_stats(dist, 0.25)

    sim_binomial_dist(dist, 0.25)


# uniform
def gen_uniform_drv(min, max) -> DRV:
    count = max - min + 1
    perc = 1 / count
    dist_dict = {}
    for i in range(min, max + 1):
        dist_dict[i] = perc
    return DRV(dist_dict)


def std(values: list[float]) -> float:
    mean = sum(values) / len(values)
    var = sum([(val - mean) ** 2 for val in values]) / len(values)
    return math.sqrt(var)


def sim_disc_uniform(dist: DRV):
    trials = 100_000
    outcomes = []
    for _ in range(trials):
        outcomes.append(dist.get_value())
    print(f'EV: sim {sum(outcomes)/trials}, dist {dist.ev()}')
    print(f'Std: sim {std(outcomes)}, dist {dist.std()}')

    results_dict = {i: 0 for i in range(1, len(dist.drv) + 1)}
    for out in outcomes:
        results_dict[out] += 1
    print('Percentages')
    for out, count in results_dict.items():
        print(
            f'Value {out}, perc {count / trials}, dist {dist.probability_of(out)}')


def disc_uniform_run():
    dist = gen_uniform_drv(1, 6)
    print(dist.validate())
    print(dist.ev())
    print(dist.std())
    sim_disc_uniform(dist)


# geometric
def gen_geometric_drv(p, max_trials):
    q = 1 - p
    return DRV({i: q ** (i - 1) * p for i in range(1, max_trials + 1)})


def sim_geom_dist(chance: float, dist: DRV):
    trials = 100_000
    dist_count = len(dist.drv)

    sim_results = {}
    success_count = 0
    t = 0
    for _ in range(trials):
        t += 1

        val = random.random()
        if val > chance:
            continue

        success_count += 1
        if t in sim_results:
            sim_results[t] += 1
        else:
            sim_results[t] = 1
        t = 0

    # compare
    for i in range(1, dist_count + 1):
        print(
            f'First success at: {i}, sim {sim_results[i] / success_count:.5f}, dist {dist.drv[i]:.5f}')

    print(f'Mean: sim {trials / success_count}, dist {1 / chance}')


def geom_dist_run():
    geom_dist = gen_geometric_drv(0.2, 20)

    total = 0.0
    for i in range(1, 21):
        total += geom_dist.drv[i]
    print(total)  # 0.98847, turned in this part into get_total_prob() method

    sim_geom_dist(0.2, geom_dist)


# Poisson dist
def gen_poisson_drv(lam, max_events):
    return DRV({
        i: (math.e ** (-lam) * lam ** i) / math.factorial(i)
        for i in range(max_events + 1)
    })


def poisson_dist_run():
    lam = 3
    poisson_dist = gen_poisson_drv(lam, 15)
    print(poisson_dist.get_total_prob())

    poisson_dist = gen_poisson_drv(lam, 25)
    print(poisson_dist.get_total_prob())

    print(f'EV: drv {poisson_dist.ev()}, poisson {lam}')
    print(f'Var: drv {poisson_dist.variance()}, poisson {lam}')
    print(f'Std: drv {poisson_dist.std()}, poisson {math.sqrt(lam)}')


# normal dist
def in_range(values: list[float], lower: float, upper: float) -> float:
    hits = 0
    for val in values:
        if lower <= val <= upper:
            hits += 1
    return hits / len(values)


def normal_dist_run():
    trials = 100_000
    values = [random.gauss(50, 10) for _ in range(trials)]

    print(f'Mean: {sum(values) / len(values)}')
    print(f'Std: {std(values)}')

    print(f'40-60: {in_range(values, 40, 60) * 100}%, expected: 68%')
    print(f'30-70: {in_range(values, 30, 70) * 100}%, expected: 95%')
    print(f'20-80: {in_range(values, 20, 80) * 100}%, expected: 99.7%')

    below_60 = sum(1 for val in values if val <= 60.0)
    print(f'<= 60: {below_60 / trials * 100}%, expected 84%')

    values = sorted(values)
    percentile = 0.95
    index = (int)(percentile * trials)
    print(f'95th percentile: {values[index]}, expected 66.45')
