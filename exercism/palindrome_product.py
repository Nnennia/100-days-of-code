def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of
             the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    factors = []
    for x in range(max_factor ** 2, min_factor ** 2 - 1, -1):
        pali = str(x)
        if pali[::-1] == pali:
            for y in range(min_factor, max_factor + 1):
                if x % y == 0 and min_factor <= x / y <= max_factor:
                    factors.append([y, int(x/y)])
        if factors:
            return x, factors
    return None, factors


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the
    palindrome in an arbitrary order.
    """

    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    factors = []
    for x in range((min_factor ** 2), (max_factor ** 2 + 1)):
        pali = str(x)
        if pali[::-1] == pali:
            for y in range(min_factor, max_factor + 1):
                if x % y == 0 and min_factor <= x / y <= max_factor:
                    factors.append([y, int(x/y)])
        if factors:
            return x, factors
    return None, factors
