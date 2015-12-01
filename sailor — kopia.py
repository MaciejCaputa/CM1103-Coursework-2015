# *** SAILOR CLASS ***
import random

class Sailor:
	pass

class ListOfSailors:
	"""
	Dynamic list of mean skill and standard deviation of every sailor. This list allows only for reading values.
	Deleting, assigning and any other build in function is disabled.
	"""
	def __init__(self, A):
		self.A = A
		self.seed = random.randint(1,10000) # different random seed for every build of th eprogram
	

	def __getitem__(self, key):
		random.seed(key * self.seed) # makes sure that values for particular index don't change (by means of key)

		mean_performance = random.randint(0,100)
		standard_deviation = random.randint(0,100)
		simulated_performance = random.normalvariate(mean_performance, standard_deviation)
		
		return key, random.randint(0,100), random.randint(0,100), random.normalvariate(mean_performance, standard_deviation)
		return Sailor


	def __repr__(self): # returns a printable representation of the object
		s = "{:>10} {:>15} {:>15} {:>15}\n".format("SAILOR'S ID", "MEAN SKILL", "STANDARD DEVIATION", "DESCRIPTION")
		for i in range(self.A):
			s += "{:>10} {:>15} {:>15} {:>15}\n".format(i+1, self[i][0], self[i][1], "-")

		s += "\n\n"
		return s