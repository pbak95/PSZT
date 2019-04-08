from random import randint, choice
from itertools import chain
import math

class Backpack:
	def __init__(self, weights, values, capacity):
		self.weights = weights
		self.values = values
		self.capacity = capacity
		self.items_number = len(weights)

	def get_weight(self, item_array):
		weights = [x for x, y  in zip(self.weights, item_array) if y == 1]
		return sum(weights)
	def get_value(self, item_array):
		values = [x for x, y  in zip(self.values, item_array) if y == 1]
		return sum(values)
	def get_fit(self, item_array):
		weights = [x for x, y  in zip(self.weights, item_array) if y == 1]
		return self.capacity - sum(weights)


def crossover(x, y):
	size = len(x)
	locus = randint(0, size-1)
	child_a = x[:locus] + y[locus:]
	child_b = y[:locus] + x[locus:]
	return child_a, child_b

W = 50
w = [10, 20, 30]
c = [60, 100, 120]
values_a = [135,139,149,150,156,163,173,184,192,201,210,214,221,229,240]
sizes_a = [70,73,77,80,82,87,90,94,98,106,110,113,115,118,120]
capacity_a = 750

def ga_solver(capacity, sizes, values):
	b = Backpack(sizes, values, capacity)

	population_size = 5
	items_number = b.items_number

	population = [[randint(0, 1) for i in range(items_number)] for j in range(population_size)]
	best_of_iter = []

	for i in range(50):
		# print(i)
		# print("population", population)
		#evaluation
		fitnesses = [b.get_value(x)-min(0, b.get_fit(x))**2 for x in population]
		# print("fitnesses", fitnesses)
		#selection of pairs
		pairs = [(choice(population), choice(population)) for x in range(math.floor(population_size/2))]
		# print("pairs", pairs)
		#crossover
		new_population = [crossover(x, y) for (x, y) in pairs]
		new_population = list(chain.from_iterable(new_population))
		# print("new", new_population)
		#mutation
		#new_population = 
		population = new_population + [population[fitnesses.index(max(fitnesses))]]
		
		feasible_indexes = [x for x in range(len(population)) if b.get_fit(population[x])>=0]
		if (len(feasible_indexes) == 0):
			best_value = 0
		else:
			best_value = max([fitnesses[x] for x in feasible_indexes])
		best_of_iter.append(best_value)
		# print("feasible: ", len(feasible_indexes))
		# print("best: ", best_value)
		#stop criterium
		if(i>10):
			if (best_of_iter[i-10] == best_of_iter[i]): break

	return best_of_iter[-1]