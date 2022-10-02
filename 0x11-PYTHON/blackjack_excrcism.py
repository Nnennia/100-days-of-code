def value_of_card(card):
    """scoring value of a card

    Args:
        card (str)
        return (int)
    """
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)

def higher_card(card_one, card_two):
    """ Determine which card has a higher value
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return (card_one, card_two)

def value_of_ace(card_one, card_two):
    """Calculate the value of ace (1 or 11)
    """
    if (value_of_card(card_one) + value_of_card(card_two) > 10) or (card_one == "A" or card_two == "A"):
        return 1
    return 11

def is_blackjack(card_one, card_two):
    """Blackjack
    """
    if card_one == 'A' or card_two == 'A':
        return value_of_card(card_one) == 10 or value_of_card(card_two) == 10
    return False

def can_split_pairs(card_one, card_two):
    """split pairs"""
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """can double down"""
    return value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]
