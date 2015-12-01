# *** MACIEJ CAPUTA ***
import csv
import random
import collections
import pprint
import math
import matplotlib.pyplot as plt


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# *** SETTINGS ***
NUMBER_OF_RACES = 6		# number of races that make up one competition
NUMBER_OF_BOATS = 100	# number of boats participating in competition
# I assume that mean skill is in a range 0..100. However foward assuptions can be made, 
# let say that you can make it to olypics only if your mean skill is greater than 75.
# However for the purpose of invesitgation it's better to assume this rage.
MEAN_SKILL_MAX = 100
MEAN_SKILL_MIN = 70
# It' wise to choose standart deviation to be between 0 and MEAN_SKILL_MAX/3 since we that really want standard deviation to be much bigger than mean skill

STANDARD_DEVIATION_MAX = 10
STANDARD_DEVIATION_MIN = 0
SEED = 0 # 57

if SEED:
	random.seed(SEED)

def generate_database():
	with open('database.csv', 'w') as csvfile:
		csv_writer = csv.writer(csvfile)

		for i in range(NUMBER_OF_BOATS):
			mean_performance = random.randint(MEAN_SKILL_MIN, MEAN_SKILL_MAX)
			standard_deviation = random.randint(STANDARD_DEVIATION_MIN, STANDARD_DEVIATION_MAX)
			csv_writer.writerow([i+1, mean_performance, standard_deviation])


def total_score(sailor):
	"""
	Function takes a tuple containing name of sailor and a list of his/her finishing position.
	First the word position is discarted and then the sum of remainter is taken and returned.
	"""
	name, scores = sailor # retriving list of scores from tuple
	return sum(sorted(scores)[1:]) # discarding worst score and taking sum of remainder


def sorted_scores(scores):
	"""
	Function takes a list of scores and return a copy of this list sordet in ascending order of their series score.
	"""
	return sorted(scores, key=lambda sailor: (-total_score(sailor), sailor[1][0]))


def read_database(file_name = "file.csv"):
	"""
	Assuming that sailors perfmances are given in a csv file with the format:
	name, mean performance, std dev
	Alice, 100, 0,
	Bob, 100, 5,
	Clare, 100, 10,
	Dennis, 90, 0,
	Eva, 90, 5,
	where each record specifies their name, mean performance and standart deviation.
	This function reads in csv file of this format and returns OrderedDict with names as keys whose values are performance and standard deviation pairs.

	>>> read_database()
	OrderedDict([('Alice', (100.0, 0.0)), ('Bob', (100.0, 5.0)), ('Clare', (100.0, 10.0)), ('Dennis', (90.0, 0.0)), ('Eva', (90.0, 5.0))])
	"""
	d = collections.OrderedDict()
	with open(file_name) as csvfile:
		rdr = csv.reader(csvfile)
		
		next(rdr, None) # ommiting first line

		for row in rdr:
			if row:
				d[row[0]] = float(row[1]), float(row[2]) # assigning tuple to the key

		csvfile.close()

	return d


def simulate_performance(data_base):
	"""
	This function takes an OrderedDict of the format returned by your answer to 1c as an argument,
	generates a random performance value using the normal distribution for each sailor,
	and returns these in another OrderedDict with names as keys.

	>>> normal_distribution(collections.OrderedDict([('Alice', (100.0, 0.0)), ('Bob', (100.0, 5.0)), ('Clare', (100.0, 10.0)), ('Dennis', (90.0, 0.0)), ('Eva', (90.0, 5.0))]))
	OrderedDict([('Alice', 100.0), ('Bob', 105.76045089520113), ('Clare', 108.36452152548142), ('Dennis', 90.0), ('Eva', 96.10844089749128)])
	"""
	sailors_performances = collections.OrderedDict()
	# initialisation of OrderedDict
	# mean performance µ and standard deviation σ.
	for key, values in data_base.items():
		mean_performance, standard_deviation = values
		sailors_performances[key] = random.normalvariate(mean_performance, standard_deviation) # mu - mean, sigma - standard deviation

	return sailors_performances
	

def simulate_race(simulation):
	"""
	This function takes an OrderedDict of the format returned by your answer to 1d as an argument,
	and returns a list of each sailor’s position in the race.
	
	>>> position(collections.OrderedDict([('Alice', 100.0), ('Bob', 105.76045089520113), ('Clare', 108.36452152548142), ('Dennis', 90.0), ('Eva', 96.10844089749128)]))
	['Clare', 'Bob', 'Alice', 'Eva', 'Dennis']
	"""
	return [x[0] for x in sorted(simulation.items(), key=lambda sailor: -sailor[1])]


def main():
	"""
	Create an OrderedDict named results with names as the keys, and empty lists as the values.
	Using the functions above, run 6 races, appending the positions of each sailor to the corresponding list,
	calculate their series score and output their names in order.
	"""

	results_I = collections.OrderedDict()
	results_II = collections.OrderedDict()

	generate_database()

	db = read_database('database.csv')
	number_of_boats = len(db)
	for name in db.keys():
		results_I[name] = []
		results_II[name] = []


	for i in range(NUMBER_OF_RACES):
		simulation = simulate_performance(db)
		position = simulate_race(simulation)

		for position_in_the_race, name in enumerate(position, start = 1):
			results_I[name].append(-position_in_the_race) # I scoring stystem can be seen as assigning minus points to the sailors
			results_II[name].append(101 + 1000*math.log(number_of_boats) - 1000*math.log(position_in_the_race))
		

	results_I = list(results_I.items()) # converts OrderedDict to the list
	results_II = list(results_II.items()) # converts OrderedDict to the list



	plt.figure(1)
	fig = plt.figure(2)
	ax = fig.gca(projection='3d')
	print("*** SORTED SCORES: SYSTEM I ***")
	
	for idx, sailor in enumerate(sorted_scores(results_I), start=1):
		name = sailor[0]
		scores = sailor[1]
		performance = total_score(sailor)
		mean_skill = db[name][0]
		standard_deviation = db[name][1]
		print("{:>2} {:>10} {:>10} {:>10} {:>20}".format(idx, name, mean_skill, standard_deviation, performance))
		
		ax.scatter(mean_skill, standard_deviation, idx, 'bo')

		plt.figure(1)
		plt.subplot(211)
		plt.plot(idx, mean_skill, 'go', label='SYSTEM I')
		plt.subplot(212)
		plt.plot(idx, standard_deviation, 'go', label='SYSTEM I')
		# print(scores)





	print("THE ORDER I: ")
	print([x[0] for x in sorted_scores(results_I)])

	print()
	print()

	print("*** SORTED SCORES: SYSTEM II ***")

	for idx, sailor in enumerate(sorted_scores(results_II), start=1):
		name = sailor[0]
		scores = sailor[1]
		performance = total_score(sailor)
		mean_skill = db[name][0]
		standard_deviation = db[name][1]
		print("{:>2} {:>10} {:>10} {:>10} {:>20}".format(idx, name, mean_skill, standard_deviation, performance))

		ax.scatter(mean_skill, standard_deviation, idx, c='r')
		
		plt.subplot(211)
		plt.plot(idx, mean_skill, 'ro', label='SYSTEM I')
		plt.subplot(212)
		plt.plot(idx, standard_deviation, 'ro', label='SYSTEM I')
		# print(scores)
	plt.subplot(211)
	plt.title("Sailor's Mean Skill Impact on Score")
	plt.xlabel("sailor's position")
	plt.ylabel("sailor's mean skill")
	plt.subplot(212)
	plt.title("Sailor's Standard Deviation Impact on Score")
	plt.xlabel("sailor's position")
	plt.ylabel("sailor's standard deviation")


	print("THE ORDER II: ")
	print([x[0] for x in sorted_scores(results_II)])


	print("1) Is the final order the same?")


	# mean_plot.ylabel('mean skill')
	#mean_plot.xlabel('position')

	# consistency_plot.ylabel("standard deviation")
	#consistency_plot.xlabel("position")

	


	ax.set_xlabel("Mean Skill")
	ax.set_ylabel('Standard Deviation')
	ax.set_zlabel('Position')

	plt.show()


if __name__ == '__main__': main()