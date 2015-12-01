# *** MACIEJ CAPUTA ***
import csv
import random
import collections
import pprint


# *** SETTINGS ***
NUMBER_OF_RACES = 6
SEED = 57

if SEED:
	random.seed(SEED)


def total_score(sailor):
	"""
	Function takes a tuple containing name of sailor and a list of his/her finishing position.
	First the word position is discarted and then the sum of remainter is taken and returned.

	>>> total_score(("bob", [2,4,1,1,2,5]))
	10
	>>> total_score(("Alice", [1, 2, 1, 1, 1, 1]))
	5
	>>> total_score(('Bob', [3, 1, 5, 3, 2, 5]))
	14
	>>> total_score(('Clare', [2, 3, 2, 2, 4, 2]))
	11
	>>> total_score(('Dennis', [5, 4, 4, 4, 3, 4]))
	19
	>>> total_score(('Eva', [4, 5, 3, 5, 5, 3]))
	20
	"""
	name, scores = sailor # retriving list of scores from tuple
	return sum(sorted(scores)[:-1]) # discarding worst score and taking sum of remainder


def sorted_scores(scores):
	"""
	Function takes a list of scores and return a copy of this list sordet in ascending order of their series score.

	>>> sorted_scores([("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]), ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])])
	[('Alice', [1, 2, 1, 1, 1, 1]), ('Clare', [2, 3, 2, 2, 4, 2]), ('Bob', [3, 1, 5, 3, 2, 5]), ('Dennis', [5, 4, 4, 4, 3, 4]), ('Eva', [4, 5, 3, 5, 5, 3])]
	"""
	return sorted(scores, key=lambda sailor: (total_score(sailor), sailor[1][0]))


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
	

def position(simulation):
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
	results = collections.OrderedDict()

	db = read_database()
	print(db)
	for name in db.keys():
		results[name] = []


	for i in range(NUMBER_OF_RACES):
		simulation = simulate_performance(db)
		pos = position(simulation)

		for score, name in enumerate(pos,start = 1):
			results[name].append(score)
		

	print(results)
	results = list(results.items()) # converts OrderedDict to the list
	print(results)
	print()
	print("SORTED SCORES")
	print(sorted_scores(results))
	for idx, sailor in enumerate(sorted_scores(results), start=1):
		print("{:>2} {:>10} {:>10}".format(idx, sailor[0], total_score(sailor)))
	ss = sorted_scores(results)

	print("\n\n*** PLACINGS ***")
	print(results)
	return results

	print("\n\n*** THE ORDER ***")
	print([x[0] for x in sorted_scores(results)])
	return [x[0] for x in sorted_scores(results)]


if __name__ == '__main__': main()