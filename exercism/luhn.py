class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if (len(self.card_num) <= 1) or (not self.card_num.isdigit()):
            return False
        number = [int(element) for element in str(self.card_num[::-1])]
        for x in range(1, len(number), 2):
            number[x] *= 2
            if number[x] > 9:
                number[x] -= 9
        return sum(number) % 10 == 0


num = Luhn("3658 2362 3608 536")
print(num.valid())
