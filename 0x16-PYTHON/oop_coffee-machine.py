from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

flag = True

while flag != False:
    user = input(f"What would you like? (espresso/latte/cappuccino) ").lower()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    menu_items = MenuItem()
    if user == "report":
        coffee_maker.report()
        money_machine.report()


