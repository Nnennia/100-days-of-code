from main import MENU,resources

money = 0
flag = True

while flag != False:
	user = input("What would you like? (espresso/latte/cappuccino): ")


	water = resources["water"]
	milk = resources["milk"]
	coffee = resources["coffee"]
	def report():
		print(f"Water:{water}ml\nMilk:{milk}ml\nCoffee:{coffee}g\nMoney:${money}")
	if user == "report":
		report()
	elif user == "off":
		break


	espresso = MENU["espresso"]["cost"]
	latte = MENU["latte"]["cost"]
	cappuccino = MENU["cappuccino"]["cost"]

	espresso_water =MENU["espresso"]["ingredients"]["water"]
	espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]

	def espresso_c():
		if water > espresso_water and coffee > espresso_coffee:
			return True
		elif water > espresso_water:
			print("Sorry there is not enough coffee")
		elif coffee < espresso_coffee:
			print("sorry, there is not enough coffee")


	latte_water = MENU["latte"]["ingredients"]["water"]
	latte_coffee = MENU["latte"]["ingredients"]["coffee"]
	latte_milk = MENU ["latte"]["ingredients"]["milk"]

	def latte_c():
		if water >  latte_water and milk > latte_milk and coffee > latte_coffee:
			return True
		elif water < latte_water:
			print("Sorry not enough water")
		elif coffee < latte_coffee:
			print("Sorry not enough coffee")
		elif milk < latte_milk:
			print("Sorry not enough milk")

	cappuccino_water =MENU["cappuccino"]["ingredients"]["water"]
	cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
	cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

	def cappuccino_c():
		if water > cappuccino_water and coffee > cappuccino_coffee and milk > cappuccino_milk:
			return True
		elif water < cappuccino_water:
			print("Sorry not enough water")
		elif coffee < cappuccino_coffee:
			print("Sorry not enough coffee")
		elif milk < cappuccino_milk:
			print("Sorry not enough milk")

	print("Please insert coins.")

	quarter = float(input("How many quarters? "))

	dime = float(input("How many dimes? "))

	nickel = float(input("How many nickles? "))

	penny = float(input("How many pennies? "))

	Sum_1 = round(((quarter*0.25) + (dime*0.1) + (nickel*0.05) + (penny*0.01)))

	#print(Sum_1)

	if user == "espresso":
		flag = True
		if Sum_1 == espresso:
			money += Sum_1
			print("Enjoy your espresso")
		elif Sum_1 > espresso:
			change_esp = Sum_1 - espresso
			money += espresso
			print(money)
			print(f"Enjoy your espresso.Here is  your change $ {change_esp}" )
		elif Sum_1 < espresso:
			print("Insufficent funds.Money refunded.")
	elif user == "latte":
		flag = True
		if Sum_1 == latte:
			money += Sum_1
			print("Enjoy your latte.")
		elif Sum_1 > latte:
			change_lat = Sum_1 - latte
			money += latte
			print(f"Enjoy your latte. Here is your change $ {change_lat}")
		elif Sum_1 < latte:
			print("Insufficent Funds.Money refunded.")
	elif user == "cappuccino":
		flag = True
		if Sum_1 == cappuccino:
			money += Sum_1
			print("Enjoy your cappuccino")
		elif Sum_1 > cappuccino:
			change_cap = Sum_1 - cappuccino
			money =+ cappuccino
			print(f"Enjoy your cappuccino. Here is your change $ {change_cap}")
		elif Sum_1 < cappuccino:
			print("Insufficent Funds.Money refunded.")
		else:
			print("Please input an option")
	else:
		print("Please pick a coffee type")


