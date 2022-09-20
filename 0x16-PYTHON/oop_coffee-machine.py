from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

flag = True

maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
Menuitem = MenuItem()

while flag != False:
    user = input("What would you like (espresso/latte/cappuccino): ").lower()

    if user == "report":
        maker.report()
        money.report()

    elif user == "off":
        flag = False

    else:
        choice = menu.find_drink(user)
        if maker.is_resource_sufficient(choice) == True:
            pay = money.process_coins()
            if money.make_payment(choice.cost) == True:
