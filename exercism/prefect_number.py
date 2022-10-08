def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only"
                         "possible for positive integers.")
    x = 0
    for y in range(1, number):
        if number % y == 0:
            x += y
    if x == number:
        return "perfect"
    elif x > number:
        return "abundant"
    else:
        return "deficient"
