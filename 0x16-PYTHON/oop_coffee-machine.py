from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

flag = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while flag != False:
    option = menu.get_items()
    user = input(f"What would you like {option}: ").lower()

    if user == "report":
        coffee_maker.report()
        money_machine.report()

    elif user == "off":
        flag = False

    else:
        drink = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink) == True and  money_machine.make_payment(drink.cost) == True:
            coffee_maker.make_coffee(drink)

