import random
from art import logo
import os

def black_jack():
	print (logo)
	user_card = []
	computer_card = []
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

	def deal_card(number):
		#number = 2
		random_card = random.choices(cards, k = number)
		return random_card

	user_card.extend(deal_card(2))
	computer_card.extend(deal_card(2))

	flag = True
	while flag != False:
		def calculate_score(cards):
			score = sum(cards)
			if user_card == 21:
				return 0
			for n in range(len(cards)):
				if cards[n] == 11 and score > 21:
					cards[n] = 1
					new_score = sum(cards)
					return new_score
				return score

		print(f"Your cards are {user_card}\n Your current score is: {calculate_score(user_card)}")
		print(f"The computer's first card: is {computer_card[0]}")

		if calculate_score(user_card) == 0:
			print("you win!")
			break
		elif calculate_score(computer_card) == 0:
			print("You lose! Computer wins")
			break
		elif calculate_score(user_card) > 21:
			print("You lose!")
		choose = input("Do you want to pick another card?\n Type 'y' for yes and 'n' for no ").lower()
		if choose == "y":
			user_card.extend(deal_card(1))
		elif choose == "n":
			flag = False
			while calculate_score(computer_card) <= 17:
				computer_card.extend(deal_card(1))
			print(f"Your final hand is {user_card}\n Your final score is {calculate_score(user_card)}")
			print(f"The computer's final hand is {computer_card}\nThe computer's final score is {calculate_score(computer_card)}")
	def compare(user_score,computer_score): # comparing final scores
		if calculate_score(user_score) == calculate_score(computer_score):
			print("It is a draw!")
		elif calculate_score(user_score) > calculate_score(computer_score) and calculate_score(user_score) < 21:
			print("You win!")
		elif calculate_score(computer_score) > calculate_score(user_score) and calculate_score(computer_score) < 21:
			print("The computer wins! You lose!")
		elif calculate_score(user_score) > 21 and calculate_score (computer_score):
			print("You lose!")
		elif calculate_score(computer_score) > 21 and calculate_score(user_score) < 21:
				print("You win!")
	compare(user_score = user_card, computer_score= computer_card) # passing user and computer's card to the compare function


player = input("Do you want to play a game of black jack? \nType 'y' for yes and 'n' for no ").lower()

flag = True

while flag != False:
	if player == "y":
		flag = False
		os.system("cls")
		black_jack()
	elif player == "n":
		flag = False
		print("Sorry to see you go!")
	else:
		print("Please input a correct option.")