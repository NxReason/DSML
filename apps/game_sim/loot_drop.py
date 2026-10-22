import random
from enum import Enum


class Rarity(Enum):
    COMMON = 'Common Potion'
    RARE = 'Rare Weapon'
    EPIC = 'Epic Armor'
    LEGENDARY = 'Legendary item'


drop_chance = {
    Rarity.COMMON: 0.60,
    Rarity.RARE: 0.25,
    Rarity.EPIC: 0.10,
    Rarity.LEGENDARY: 0.05,
}


def combined_chance(rarities: list[Rarity]) -> float:
    total = 0.0
    for r in rarities:
        if r in drop_chance:
            total += drop_chance[r]

    return total


def drop_loot() -> Rarity:
    val = random.random()
    c_common = drop_chance[Rarity.COMMON]
    c_rare = combined_chance([Rarity.COMMON, Rarity.RARE])
    c_epic = combined_chance([Rarity.COMMON, Rarity.RARE, Rarity.EPIC])
    match val:
        case _ if val < c_common: return Rarity.COMMON
        case _ if val < c_rare: return Rarity.RARE
        case _ if val < c_epic: return Rarity.EPIC
        case _: return Rarity.LEGENDARY


# Simulations
def sim_summary(name: str, result: float, expected: float):
    print(f"Event:  {name}")
    print(f"\tSim result: {result}")
    print(f"\tExpected result: {expected}")
    print(f"\tDelta: {expected - result}")


def run_sim(rarities: list[Rarity], num_trials: int = 100_000):
    success = 0
    for _ in range(num_trials):
        loot = drop_loot()
        if loot in rarities:
            success += 1
    return success / num_trials


def sim_rare():
    expected = drop_chance[Rarity.RARE]
    result = run_sim([Rarity.RARE])
    sim_summary('Rare drop', result, expected)


def sim_epic_and_leg():
    rarities = [Rarity.EPIC, Rarity.LEGENDARY]
    expected = combined_chance(rarities)
    result = run_sim(rarities)
    sim_summary('Epic or Legendary drop', result, expected)


def sim_all():
    trials = 100_000
    rarity_counter = {
        Rarity.COMMON: 0,
        Rarity.RARE: 0,
        Rarity.EPIC: 0,
        Rarity.LEGENDARY: 0
    }
    for _ in range(trials):
        loot = drop_loot()
        rarity_counter[loot] += 1

    print('Sim all')
    total = 0.0
    for key, value in rarity_counter.items():
        expected = drop_chance[key]
        print(f'\t {key}: sim = {value / trials}, expected = {expected}')
        total += value
    print(f'Total: {total / trials}')
