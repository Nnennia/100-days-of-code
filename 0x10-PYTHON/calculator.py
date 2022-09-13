import os
from art import logo
def mul(num1,num2):
	return num1 * num2

def add(num1,num2):
	return num1 + num2

def minus(num1, num2):
	return num1 - num2

def divide(num1,num2):
	return num1 / num2

operator = {"+":add, "-":minus, "*":mul, "/":divide}

def calculator():
	print(logo)
	num1 = float(input("What is the first number?\n"))
	num2 = float(input("What is the second number?\n"))

	for key in operator:
		print(key)

	choose_operator = input("Pick an operator\n")
	operation = operator[choose_operator]

	result_1 = operation(num1,num2)
	print(f"{num1} {choose_operator} {num2} = {result_1}")

	flag = True
	while flag != False:
		choose_operator = input(f"Would you like to countiue calculating with {result_1}?\nType 'y' for yes and 'n' for no.\n").lower()
		if choose_operator == "y":
			flag = False
			choose_operator = input("choose an operator\n")
			new_num = float(input("Enter another number\n"))

			operation = operator[choose_operator]
			new_ans = operation(result_1, new_num)
			print(f"{result_1} {choose_operator} {new_num} = {new_ans}")
			result_1 = new_ans
		elif choose_operator == "n":
			os.system("cls")
			calculator()
calculator()
