# Counting priciples
# project1

import itertools
import math


class CharacterCreator:
    def __init__(self, hairstyles: int, outfits: int, weapons: int, eye_colors: int):
        self.hairstyles = hairstyles
        self.outfits = outfits
        self.weapons = weapons
        self.eye_colors = eye_colors

    def combinations(self):
        return self.hairstyles * self.outfits * self.weapons * self.eye_colors


def character_creator():
    cc = CharacterCreator(4, 5, 3, 2)
    print('Combinations:', cc.combinations())


# project 2
class CharClass:
    def __init__(self, name: str, weapon_choices: int):
        self.weapon_choices = weapon_choices


def calc_total_loadouts(characters: list[CharClass], pet_count: int) -> int:
    total_weapons = 0
    for c in characters:
        total_weapons += c.weapon_choices
    return total_weapons * pet_count


def loadouts():
    characters = [
        CharClass('Warrior', 4),
        CharClass('Mage', 2),
        CharClass('Archer', 3)
    ]
    print('Total loadouts:', calc_total_loadouts(characters, 2))


# project 3
def verify_by_enum():
    hairstyles = ['Bald', 'Afro', 'Mohawk', 'Bowlcut']
    outfits = ['Casual', 'Uniform', 'Armor', 'Winter', 'NSFW']
    weapons = ['Sword', 'Bow', 'Axe']
    eye_colors = ['Green', 'Blue']
    permutations = list(itertools.product(
        hairstyles, outfits, weapons, eye_colors))
    print('Combinations (itertool.product):', len(permutations))


# Permutations
# project 1
def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n - 1)


def attack_orders():
    for i in range(10):
        print(f'Enemy count: {i}, attack orders: {factorial(i)}')


# project 2
def permutations(total: int, use: int) -> int:
    return factorial(total) // factorial(total - use)


def turn_queue():
    for i in range(10):
        print(f'{i} turns from 10: {permutations(10, i)}')


# project 3
def ability_seq():
    ability_count = 5
    action_count = 3

    print('No more than once:', permutations(ability_count, action_count))
    print('Repeated:', math.pow(ability_count, action_count))

    print('Verify (itertools.permutation):', len(list(itertools.permutations(
        range(ability_count), action_count))))
    print('Verify (itertools.product):', len(
        list(itertools.product(range(5), range(5), range(5)))))


# Combinations
def combinations(total: int, count: int) -> int:
    return factorial(total) // (factorial(count) * factorial(total - count))


def upgrade_selection():
    total = 12
    choices = 4
    print('Upgrade selection:', combinations(total, choices))


def party_composition():
    slots = 5
    characters = 10
    print('Parties:', combinations(characters, slots))
    print('Turns:', permutations(characters, slots))


def loot_crafting():
    magical = 5
    ordinary = 9
    total = magical + ordinary
    recipe = 4

    target_magical = 2
    m_combinations = combinations(magical, target_magical)
    o_combinations = combinations(ordinary, recipe - target_magical)
    total_valid = m_combinations * o_combinations
    total_combinations = combinations(total, recipe)
    print(f'{target_magical} magical in the recipe of {recipe}: {total_valid / total_combinations:.5f}')

    # verify
    m = ['Magical' for _ in range(5)]
    o = ['Ordinary' for _ in range(9)]
    it_combinations = itertools.combinations(m + o, 4)
    it_success = 0
    it_total = 0
    for comb in it_combinations:
        it_total += 1
        valid_comb = sum(item == 'Magical' for item in comb) == 2
        if valid_comb:
            it_success += 1

    print(it_success / it_total)


# Binomial theorem
# project 1
def get_binom_terms(n, k):
    coef = combinations(n, k) if n - k > 0 and k != 0 else ''
    a = f'a^{n - k}' if n - k > 0 else ''
    b = f'b^{k}' if k > 0 else ''
    return f"{coef}{a}{b}"


def expand_binomial():
    for i in range(6):
        coefs = [get_binom_terms(i, k) for k in range(i + 1)]
        print(' + '.join(coefs))


# project 3
def critical_hits():
    attack_count = 6
    crit_chance = 0.2

    total = 0.0
    for target_crits in range(attack_count + 1):
        any_crit_seq = (crit_chance ** target_crits) * \
            ((1 - crit_chance) ** (attack_count - target_crits))
        valid_combinations = combinations(6, target_crits)
        prob = valid_combinations * any_crit_seq
        print(f'{target_crits}: {prob:.5f}')
        total += prob
    print(total)


# Constraints
# project 1
def restricted_party():
    print('Restricted party')
    healers = 3
    non_healers = 9
    total_players = healers + non_healers
    party_size = 4

    # 1
    total_comb = combinations(total_players, party_size)
    total_no_healers = combinations(non_healers, party_size)
    print(total_comb - total_no_healers)

    # 2
    one_h = 3 * combinations(non_healers, party_size - 1)
    two_h = combinations(3, 2) * combinations(non_healers, party_size - 2)
    three_h = 1 * combinations(non_healers, party_size - 3)
    print(one_h + two_h + three_h)


# project 2
def restricted_ability_loadout():
    print('Restricted ability loadout')
    total_abilities = 11
    equiped_abilities = 5

    total_loadouts = combinations(total_abilities, equiped_abilities)
    invalid_loadouts = combinations(total_abilities - 2, equiped_abilities - 2)
    print(total_loadouts - invalid_loadouts)


# project 3
def pad_zeroes(pw: str, to: int):
    if len(pw) >= to:
        return pw
    pad_count = to - len(pw)
    return '0' * pad_count + pw


def password_constraints():
    print('Password constraints')
    positions = 6

    all_passwords = 10 ** positions
    no_five = 9 ** positions
    no_zero = 9 ** positions
    neither = 8 ** positions
    valid = all_passwords - no_five - no_zero + neither
    print(valid)

    # verify
    success = 0
    for i in range(10 ** positions):
        password = pad_zeroes(str(i), positions)
        if '0' in password and '5' in password:
            success += 1
    print(success)

# problem set


def problem_set():
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()
    problem7()
    problem8()


# 1. an adventurer chooses 3 items from 8 distinct items to carry.
# how many diff sets of items can they carry?
def problem1():
    print('P1:', combinations(8, 3))


# 2. 5 different enemies must act in sequence.
# how many possible turn orders are there?
def problem2():
    print('P2:', permutations(5, 5))


# 3. a recipe requires 2 distinct herbs chosen from 7
# 1 gem choosen from 5
# how many different recipes are possible
def problem3():
    herb_comb = combinations(7, 2)
    gem_comb = 5
    print('P3:', herb_comb * gem_comb)


# 4. choose a party of 4 from 11 chars, 3 of whom are healers
# how many parties contain at least one healer?
def problem4():
    all_comb = combinations(11, 4)
    no_healers = combinations(11 - 3, 4)
    print('P4:', all_comb - no_healers)


# 5. char equips 4 of 9 distinct abilities.
# two specific abilities cannot be equipped together
# how many valid loadouts?
def problem5():
    all_comb = combinations(9, 4)
    invalid_comb = combinations(9 - 2, 2)
    print('P5:', all_comb - invalid_comb)


# 6. 5-digit code uses digits 0-9, repetition allowed, and leading zeros are allowed
# how many codes contain at least one 2 and at least one 8?
def problem6():
    all_codes = 10 ** 5
    no_2 = 9 ** 5
    no_8 = 9 ** 5
    neither = 8 ** 5
    print('P6:', all_codes - no_2 - no_8 + neither)


# 7. char attacks 8 times. each attack independently crits with prob 0.25
# what is the probability of exactly 2 crits?
def crit_count(chance, crits, total):
    non_crits = total - crits
    any_crit_seq = (chance ** crits) * ((1 - chance) ** non_crits)
    combs = combinations(total, crits)
    print(
        f'Total: {total}, crits: {crits}, crit chance: {chance}, prob: {combs * any_crit_seq * 100:.3f}%')


def problem7():
    any_crit_seq = (0.25 ** 2) * (0.75 ** 6)
    combs = combinations(8, 2)
    print('P7:', any_crit_seq * combs)


# 8. choose 5 characters from 4 tanks, 6 dd, 3 healers
# how many parties with exactly 1 healer and at least 1 tank?
def problem8():
    healer_combs = 3

    rest_all_combs = combinations(4 + 6, 4)
    rest_no_tanks = combinations(6, 4)
    rest_valid_combs = rest_all_combs - rest_no_tanks

    print('P8:', healer_combs * rest_valid_combs)
