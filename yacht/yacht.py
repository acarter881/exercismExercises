import statistics

# Score categories.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
CHOICE = 'CHOICE'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
FULL_HOUSE = 'FULL_HOUSE'
YACHT = 'YACHT'

def score(dice, category):
    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return sum((number for number in dice if number == category))
    elif category == CHOICE:
        return sum(dice)
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]: return 30
        return 0
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]: return 30
        return 0 
    elif category == FOUR_OF_A_KIND:
        if max(set((dice.count(number) for number in dice))) >= 4: return 4 * statistics.mode(dice)
        return 0
    elif category == FULL_HOUSE:
        if set((dice.count(number) for number in dice)) == {2, 3}: return sum(dice)
        return 0
    elif category == YACHT:
        if max(set((dice.count(number) for number in dice))) == 5: return 50
        return 0

print(score([6, 6, 6, 6, 5], YACHT))