print("Welcome to the tip calculator.")
bill = float(input("what was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15 ? "))
people = int(input("How many people to split the bill? "))

tipPercent = tip / 100
tipAmount = bill * tipPercent
totalBill = bill + tipAmount
billperPerson = totalBill / people

print(round(billperPerson, 2))
