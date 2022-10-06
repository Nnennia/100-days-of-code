def get_rounds(round_number):
    return [round_number, round_number + 1, round_number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    rounds_1.extend(rounds_2)
    return rounds_1


def list_contains_round(rounds, round_number):
    return round_number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    '''

    :param hand: list - cards in hand.
    :return: int - approximate average value of the cards in the hand.
    '''
    avg = card_average(hand)
    avg == float(hand[len(hand) // 2]) or avg == (hand[0] + hand[-1]) / 2
    return avg


def average_even_is_odd(hand):
    ave = sum(hand) // len(hand)
    if ave % 2 == 0:
        return True
    else:
        return False


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
