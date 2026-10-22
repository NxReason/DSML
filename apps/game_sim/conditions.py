from die_roll import *


# run_sim updated to included die sides number
# project 1
def verify(event, name: str, expected: float):
    result = run_sim(event, 10)
    print(f'{name}: expected {expected}, result {result}, delta {expected - result}')


def event_prob(event, sample_space) -> float:
    return len(list(filter(event, sample_space))) / len(sample_space)


def combined_events():
    sample_space = list(range(1, 11))
    event_a = is_even
    event_b = above(6)

    # calculate by enumerating
    p_a = event_prob(event_a, sample_space)
    p_b = event_prob(event_b, sample_space)
    p_and = p_a * p_b
    # addition rule
    p_or = p_a + p_b - p_and

    # verify
    event_and = intersection_event([event_a, event_b])
    event_or = union_event([event_a, event_b])

    verify(event_a, 'A', p_a)
    verify(event_b, 'B', p_b)
    verify(event_and, 'A and B', p_and)
    verify(event_or, 'A or B', p_or)


# project 2
def run_sim_all(events) -> float:
    if len(events) == 0:
        return 0.0

    result = 1.0
    for event in events:
        result *= run_sim(event)

    return result


def run_sim_least_one(events) -> float:
    if len(events) == 0:
        return 0.0

    neither = 1.0
    for event in events:
        neither *= run_sim(event)

    return 1 - neither


def independent_attacks():
    sample_space = list(range(1, 7))
    event_a1 = equal(6)
    event_a2 = equal(6)
    p_a1 = event_prob(event_a1, sample_space)
    p_a2 = event_prob(event_a2, sample_space)

    p_both = p_a1 * p_a2
    result_both = run_sim_all([event_a1, event_a2])
    print(
        f'Both attacks crit: expected {p_both:.5f}, result {result_both:.5f}, delta {p_both - result_both:.5f}')

    # neither crit
    event_nc1 = below(6)
    event_nc2 = below(6)
    p_least_one = 1 - event_prob(event_nc1, sample_space) * \
        event_prob(event_nc2, sample_space)
    result_least_one = run_sim_least_one([event_nc1, event_nc2])
    print(
        f'Neither crits: expected {p_least_one:.5f}, result {result_least_one:.5f}, delta {p_least_one - result_least_one:.5f}')


# project 3
def run_sim_cond(event_test, event_given, sides: int = 6, num_trials: int = 100_000):
    given_count = 0
    success_count = 0
    for _ in range(num_trials):
        outcome = die_roll(sides)
        if not event_given(outcome):
            continue
        given_count += 1
        if event_test(outcome):
            success_count += 1

    return success_count / given_count


def cond_combat_sim():
    sample_space = list(range(1, 11))
    event_a = above(5)
    event_b = is_even
    p_a = event_prob(event_a, sample_space)
    event_and = intersection_event([event_a, event_b])

    # manually from sample space
    p_and = event_prob(event_and, sample_space)
    p_cond = p_and / p_a

    # verify
    result_cond = run_sim_cond(event_b, event_a, 10)

    print(
        f'P(B|A): expected {p_cond:.5f}, result {result_cond:.5f}, delta {p_cond - result_cond:.5f}')
