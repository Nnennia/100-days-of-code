from art import logo,vs
from game_data import data
import random
import os

print(logo)
score = 0
against_B = random.choice(data)

def data_formart(datas):
	"""Takes the account data and returns the printable formart

	Args:
		datas (list): fetches data from a list
	"""
	name =  datas["name"]
	descr =  datas["description"]
	country =  datas["country"]
	return(f"{name}, a {descr} from {country}")


def answer(user,a_follower,b_follower):
	if a_follower > b_follower:
		return user == "a"
	else:
		return user == "b"

flag = True

while  flag != False:
	compare_A = against_B
	against_B = random.choice(data)
	while compare_A == against_B:
		compare_A = random.choice(data)

	#print(logo)
	print(f"Compare A: {data_formart(compare_A)}")
	print(vs)
	print(f"Against B: {data_formart(against_B)}")

	user = input("Who has more followers? Type 'A' or 'B': ").lower()
	a_follower_count = compare_A["follower_count"]
	b_follower_count = against_B["follower_count"]

	correct = answer(user,a_follower_count,b_follower_count)
	os.system("cls")
	print(logo)
	if correct:

		score += 1
		print(f"You are right. Current score is {score}")
	else:
		flag = False
		print(f"You lose. Current score is {score}")
