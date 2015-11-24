import random

# Simulate n goes at the problem
def monty(n):

	stick_wins = 0
	swap_wins = 0

	# Run n tests
	for i in range(n):

		# Decide what is behind each door randomly
		doors = [1, 2, 3]
		car_door = random.choice(doors)
		# print( " car door : ", car_door)

		# Contestant picks a door randomly
		selection = random.choice(doors)
		# print( " selection : ", selection)

		# Reveal a goat
		goat_door = random.choice(list(set(doors) - set([car_door, selection])))
		# print( " goat door : ", goat_door)

		# Work out the result of each strategy
		swap_selection = list(set(doors) - set([selection, goat_door]))[0]

		if selection == car_door:
			stick_wins = stick_wins + 1
		elif swap_selection == car_door:
			swap_wins = swap_wins + 1
		else:
			print("Something wrong")

	return stick_wins, swap_wins
	
