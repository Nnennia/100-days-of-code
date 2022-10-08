import os
from art import logo

print(logo)
data_bidding = {}

clear = True

while clear is False:

    name = input("What is your name?\n")
    bid = int(input("How much are you going to bid?\n"))
    data_bidding[name] = bid
    clear = input("Are there other bidders in the room? Y or N\n").lower()

    if clear == "y":
        flag = False
        os.system("cls")
        # print(data_bidding)
    elif clear == "n":
        clear = False
        os.system("cls")
max_key = max(data_bidding)
max_value = max(data_bidding.values())
print(f"The winner is {max_key} with a bid of $ {max_value}")
