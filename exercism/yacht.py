YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = None
COUNT = [ONES, TWOS, THREES, FOURS, FIVES, SIXES]


def score(dice, category):
    dice = sorted(dice)
    result = 0
    maximum = max(dice, key=dice.count)
    minimum = min(dice, key=dice.count)
    if category in COUNT:
        result = dice.count(category) * category
    if category is LITTLE_STRAIGHT:
        if dice == [1, 2, 3, 4, 5]:
            result = 30
    if category is BIG_STRAIGHT:
        if dice == [2, 3, 4, 5, 6]:
            result = 30
    if category is CHOICE:
        result = sum(dice)
    if category is FULL_HOUSE:
        if dice.count(maximum) == 3 and dice.count(minimum) == 2:
            result = sum(dice)
    if category is FOUR_OF_A_KIND:
        if dice.count(maximum) >= 4:
            result = maximum * 4
    if category is YACHT:
        if dice.count(5) == len(dice):
            return YACHT

    return result
