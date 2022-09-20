import random

random_number = random.randrange(0,101)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty\nType 'easy' or 'hard' ").lower()

if difficulty == "easy":
	attempts = 10

	print(f"You have {attempts} attempts remaining to guess the number.")
	flag = True
	while flag != False:
		user = int(input("Make a guess: "))
		if user != random_number and user > random_number:
			flag = True
			attempts -= 1
			print("Too high")
			print (f"{attempts} attempts left to guess the number.\nGuess again.")
			if attempts == 0:
				flag = False
				print(f"The random number is {random_number}")
		elif user < random_number:
			flag = True
			print("Too low")
			attempts -= 1
			print(f"You have {attempts} attempts left.\nGuess again.")
			if attempts == 0:
				flag = False
				print(f"You lose. Random number was {random_number}")
		elif user == random_number:

			flag = False
			print(f"You win. You number was {user} and random number was {random_number}")
		else:
			print("Input a number")
elif difficulty == "hard":
	attempts = 5
	print(f"You have {attempts} attempts remainning to guess the number.")
	flag = True
	while flag != False:
		user = int(input("Make a guess: "))
		if user != random_number and user > random_number:
			flag = True
			attempts -= 1
			print("Too high")
			print (f"{attempts} attempts left to guess the number.\nGuess again.")
			if attempts == 0:
				flag = False
				print(f"The random number is {random_number}")
		elif user < random_number:
			flag = True
			print("Too low")
			attempts -= 1
			print(f"You have {attempts} attempts left.\nGuess again.")
			if attempts == 0:
				flag = False
				print(f"You lose. Random number was {random_number}")
		elif user == random_number:
			flag = False
			print(f"You win. You number was {user} and random number was {random_number}")
		else:
			print("Input a number")
