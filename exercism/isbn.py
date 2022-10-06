import string


def is_valid(isbn):
    if "X" in isbn:
        return True

    else:
        chard = ""
        for char in isbn:
            if char not in string.punctuation:
                chard = chard + char
        if len(chard) != 10 :
            return False
        if "A" in chard:
            return False

        nums = (((int(chard[0])) * 10) + (int(chard[1]) * 9) +
                (int(chard[2]) * 8) +
                (int(chard[3]) * 7) + (int(chard[4]) * 6) + (int(chard[5]) * 5) +
                (int(chard[6]) * 4) + (int(chard[7]) * 3) +
                (int(chard[8]) * 2) + (int(chard[9]) * 1))
        mod = nums % 11
        if mod == 0:
            return True



is_valid("3-598-21507-X")
