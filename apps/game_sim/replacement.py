from enum import Enum
from random import choice


class Rarity(Enum):
    COMMON = 'Common'
    RARE = 'Rare'


def gen_loot(quantities: dict[Rarity, int]):
    loot = []
    for rarity, count in quantities.items():
        loot.extend([rarity for _ in range(count)])
    return loot


def is_rarity(rarity: Rarity):
    def inner(item: Rarity):
        return item == rarity
    return inner


def summary(name: str, expected: float, sim: float):
    print(f'{name}: expected {expected:.5f}, sim {sim:.5f}, delta {expected - sim:.5f}')


# project 1
def with_replacement_prob(target_rarity: Rarity, num_events: int, loot: list[Rarity]):
    target_total = len(list(filter(is_rarity(target_rarity), loot)))
    prob = 1.0
    for _ in range(num_events):
        prob *= target_total / len(loot)
    return prob


def with_replacement_sim(target_rarity: Rarity, num_events: int, loot: list[Rarity]):
    success = 0
    trials = 100_000
    for _ in range(trials):
        picks = [choice(loot) == target_rarity for _ in range(num_events)]
        if all(picks):
            success += 1
    return success / trials


def with_replacement(target_rarity: Rarity, num_events: int, loot: list[Rarity]):
    prob = with_replacement_prob(target_rarity, num_events, loot)
    sim_prob = with_replacement_sim(target_rarity, num_events, loot)

    summary('With replacement', prob, sim_prob)


def no_replacement_prob(target_rarity: Rarity, num_events: int, loot: list[Rarity]):
    target_left = len(list(filter(is_rarity(target_rarity), loot)))
    total_left = len(loot)
    prob = 1.0
    for _ in range(num_events):
        prob *= target_left / total_left
        target_left -= 1
        total_left -= 1
    return prob


def no_replacement_sim(target_rarity: Rarity, num_events: int, loot: list[Rarity]):
    success = 0
    trials = 100_000
    for _ in range(trials):
        loot_copy = loot[:]
        for _ in range(num_events):
            pick = choice(loot_copy)
            loot_copy.remove(pick)
            if pick is not target_rarity:
                break
        else:
            success += 1
    return success / trials


def no_replacement(target_rarity: Rarity, num_events: int, loot: list[Rarity]):
    prob = no_replacement_prob(target_rarity, num_events, loot)
    sim_prob = no_replacement_sim(target_rarity, num_events, loot)

    summary('No replacement', prob, sim_prob)


def sim_replacement():
    loot = gen_loot({Rarity.COMMON: 7, Rarity.RARE: 3})
    print('2 rares')
    with_replacement(Rarity.RARE, 2, loot)
    no_replacement(Rarity.RARE, 2, loot)


# project 2
def least_one_rare():
    loot = gen_loot({Rarity.COMMON: 7, Rarity.RARE: 3})

    print('At least 1 rare')
    with_repl_common = with_replacement_prob(Rarity.COMMON, 2, loot)
    with_repl_rare = 1 - with_repl_common
    with_repl_common_sim = with_replacement_sim(Rarity.COMMON, 2, loot)
    with_repl_rare_sim = 1 - with_repl_common_sim
    summary('With replacement', with_repl_rare, with_repl_rare_sim)

    no_repl_common = no_replacement_prob(Rarity.COMMON, 2, loot)
    no_repl_rare = 1 - no_repl_common
    no_repl_common_sim = no_replacement_sim(Rarity.COMMON, 2, loot)
    no_repl_rare_sim = 1 - no_repl_common_sim
    summary('No replacement', no_repl_rare, no_repl_rare_sim)


# project 3
def unique_rewards():
    rewards = ['COMMON', 'RARE', 'EPIC', 'LEGENDARY', 'DIVINE']
    count = len(rewards)

    print('Unique rewards')
    print(f'First 2 are same: {1 / count}')
    print(
        f'All 3 are different (with repl): {1.0 * (count - 1) / count * (count - 2) / count}')
