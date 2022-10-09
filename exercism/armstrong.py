def is_armstrong_number(number):
    num = str(number)
    sum = 0
    for digit in num:
        sum += int(digit) ** len(num)
    return sum == number
