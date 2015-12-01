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
import numpy as np

# *** SETTINGS ***
SEED = 57 # 57 as default, change to 0 if not needed

if SEED:
	random.seed(SEED)


def generate_database(mean_skill_range, standard_deviaiton_range, number_of_boats = 100):
	mean_skill_min, mean_skill_max = mean_skill_range
	standard_deviation_min, standard_deviation_max = standard_deviaiton_range

	with open('database.csv', 'w') as csvfile:
		csv_writer = csv.writer(csvfile)

		for i in range(number_of_boats):
			mean_performance = random.randint(mean_skill_min, mean_skill_max)
			standard_deviation = random.randint(standard_deviation_min, standard_deviation_max)
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
	"""
	return [x[0] for x in sorted(simulation.items(), key=lambda sailor: -sailor[1])]


def simulation(mean_skill_range, standard_deviaiton_range, number_of_races = 6, number_of_boats = 100):
	"""
	Create an OrderedDict named results with names as the keys, and empty lists as the values.
	Using the functions above, run 6 races, appending the positions of each sailor to the corresponding list,
	calculate their series score and output their names in order.
	"""
	results_I = collections.OrderedDict()
	results_II = collections.OrderedDict()

	generate_database(mean_skill_range, standard_deviaiton_range)

	db = read_database('database.csv')
	number_of_boats = len(db)
	for name in db.keys():
		results_I[name] = []
		results_II[name] = []

	for i in range(number_of_races):
		simulated_performance = simulate_performance(db)
		position = simulate_race(simulated_performance)

		for position_in_the_race, name in enumerate(position, start = 1):
			results_I[name].append(-position_in_the_race) # I scoring stystem can be seen as assigning minus points to the sailors
			results_II[name].append(101 + 1000*math.log(number_of_boats) - 1000*math.log(position_in_the_race))
		

	results_I = list(results_I.items()) # converts OrderedDict to the list
	results_II = list(results_II.items()) # converts OrderedDict to the list

	# 2D figure: initialisation
	plt.figure(1)

	# 3D figure: initialisation
	fig = plt.figure(2)
	ax = fig.gca(projection='3d')


	# *** SORTED SCORES: SYSTEM I ***
	for idx, sailor in enumerate(sorted_scores(results_I), start=1):
		name = sailor[0]
		scores = sailor[1]
		performance = total_score(sailor)
		mean_skill = db[name][0]
		standard_deviation = db[name][1]
		
		# 2D figure: plot
		plt.figure(1)
		plt.subplot(211)
		plt.plot(idx, mean_skill, 'go')
		plt.subplot(212)
		plt.plot(idx, standard_deviation, 'go')

		# 3D figure: plot
		ax.scatter(mean_skill, standard_deviation, idx, c='g')

		# print("{:>2} {:>10} {:>10} {:>10} {:>20}".format(idx, name, mean_skill, standard_deviation, performance))

	
	# *** SORTED SCORES: SYSTEM II ***")
	for idx, sailor in enumerate(sorted_scores(results_II), start=1):
		name = sailor[0]
		scores = sailor[1]
		performance = total_score(sailor)
		mean_skill = db[name][0]
		standard_deviation = db[name][1]
		
		# 2D figure: plot
		plt.figure(1)
		plt.subplot(211)
		plt.plot(idx, mean_skill, 'ro')
		plt.subplot(212)
		plt.plot(idx, standard_deviation, 'ro')

		# 3D figure: plot
		ax.scatter(mean_skill, standard_deviation, idx, c='r')

		# print("{:>2} {:>10} {:>10} {:>10} {:>20}".format(idx, name, mean_skill, standard_deviation, performance))

	# 2D figure: labels
	plt.subplot(211)
	plt.title("Sailor's Mean Skill Impact on Score")
	plt.xlabel("sailor's position")
	plt.ylabel("sailor's mean skill")

	# 2D figure: legend
	go = plt.Line2D([0,0],[0,1], color='Green', marker='o', linestyle='')
	ro = plt.Line2D([0,0],[0,1], color='Red', marker='o', linestyle='')
	plt.legend([go,ro], ["System I", "System II"])

	plt.subplot(212)
	plt.title("Sailor's Standard Deviation Impact on Score")
	plt.xlabel("sailor's position")
	plt.ylabel("sailor's standard deviation")

	# 3D figure: labels
	ax.set_xlabel("Mean Skill")
	ax.set_ylabel('Standard Deviation')
	ax.set_zlabel('Position')

	plt.show()


def main():
	# supplying variables by names makes calling function more readable
	simulation(mean_skill_range = (0,100), standard_deviaiton_range = (0,20))
	simulation(mean_skill_range = (70,100), standard_deviaiton_range = (0,10))



if __name__ == '__main__': main()