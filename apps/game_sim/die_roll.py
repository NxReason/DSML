import random


def die_roll(sides: int = 6) -> int:
    return random.randint(1, sides)


# Events
def above(value: int):
    return lambda outcome: outcome > value


def below(value: int):
    return lambda outcome: outcome < value


def equal(value: int):
    return lambda outcome: outcome == value


def value_in(values: list[int]):
    return lambda outcome: outcome in values


def is_even(value: int):
    return value % 2 == 0


def is_odd(value: int):
    return value % 2 == 1


def union_event(events):
    def inner(outcome: int):
        for e in events:
            if e(outcome):
                return True
        return False
    return inner


def intersection_event(events):
    def inner(outcome: int):
        for e in events:
            if not e(outcome):
                return False
        return True
    return inner


# Simulations
# Utils
def sim_summary(name: str, result: float, expected: float):
    print(f"Event:  {name}")
    print(f"\tSim result: {result}")
    print(f"\tExpected result: {expected}")
    print(f"\tDelta: {expected - result}")


def run_sim(event, sides: int = 6, num_trials: int = 100_000):
    success = 0
    for _ in range(num_trials):
        outcome = die_roll(sides)
        if event(outcome):
            success += 1
    result = success / num_trials
    return result


# Sim cases
def sim_is_even():
    event = is_even
    result = run_sim(event)
    sim_summary("Die roll - is even", result, 0.5)


def sim_above_or_below():
    event = union_event([above(4), below(3)])
    result = run_sim(event)
    sim_summary("Die roll - below 3, above 4", result, 4 / 6)


def sim_odd_and_above():
    event = intersection_event([above(4), is_odd])
    result = run_sim(event)
    sim_summary("Die roll - above 4 and odd", result, 1 / 6)


# Combat sim
def sim_die_combat():
    e_miss = equal(1)
    e_hit = value_in([2, 3, 4, 5])
    e_crit = equal(6)

    r_miss = run_sim(e_miss)
    r_hit = run_sim(e_hit)
    r_crit = run_sim(e_crit)

    print(f'Miss: {r_miss}')
    print(f'Hit: {r_hit}')
    print(f'Crit: {r_crit}')
    print(f'Total: {r_miss + r_hit + r_crit}')
