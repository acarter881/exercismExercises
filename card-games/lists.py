def get_rounds(number):
    '''

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    '''
    return [number, number + 1, number + 2]
    
def concatenate_rounds(rounds_1, rounds_2):
    '''

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    '''
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    '''

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    '''
    return True if number in rounds else False
    
def card_average(hand):
    '''

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    '''
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    '''

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    '''
    return True if (hand[0] + hand[-1]) / 2 == card_average(hand) or hand[(len(hand) // 2) + 1] == card_average(hand) else False
    
def average_even_is_average_odd(hand):
    '''

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    '''
    odd_total = 0
    odd_count = 0
    even_total = 0
    even_count = 0

    for index, number in enumerate(hand):
        if index % 2 == 0:
            even_count += 1
            even_total += number
        else:
            odd_count += 1
            odd_total += number

    return True if (even_total / even_count) == (odd_total / odd_count) else False
        
def maybe_double_last(hand):
    '''

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    '''
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand