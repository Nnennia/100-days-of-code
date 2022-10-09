def square(number):
    if number > 64 or number <= 0:
        raise ValueError("square must be between 1 and 64")
    n = number - 1
    square = 2 ** n
    return square


def total():
    total = 2 ** 64 - 1
    return total
