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
	def get_fitness(self, item_array):
		values = [x for x, y  in zip(self.values, item_array) if y == 1]
		weights = [x for x, y  in zip(self.weights, item_array) if y == 1]
		return sum(values) if self.capacity >= sum(weights) else 0

def selection(population, fitnesses):
	fitness_sum = sum(fitnesses)
	a = randint(1, max(fitness_sum, 2))
	b = randint(1, max(fitness_sum, 2))
	selected_a = None
	selected_b = None

	for f in fitnesses:
		fitness_sum -= f
		if (fitness_sum < a): selected_a = population[fitnesses.index(f)]
		if (fitness_sum < b): selected_b = population[fitnesses.index(f)]
		if (fitness_sum <= 0 or(selected_a != None and selected_b != None)): break

	return (selected_a, selected_b)

def crossover(x, y):
	size = len(x)
	locus = randint(0, size-1)
	child_a = x[:locus] + y[locus:]
	child_b = y[:locus] + x[locus:]
	return child_a, child_b

def mutation(x):
	mutation_indices = [randint(0, 9) == 0  for i in range(len(x))]
	return [int(bool(a) ^ bool(b)) for a, b in zip(x, mutation_indices)]


def ga_solver(capacity, sizes, values):
	b = Backpack(sizes, values, capacity)

	population_size = 25
	items_number = b.items_number

	population = [[randint(0, 1) for i in range(items_number)] for j in range(population_size)]
	best_of_iter = []

	for i in range(50):
		#print(i)
		#print("population", population)

		#evaluation
		fitnesses = [b.get_fitness(x) for x in population]
		fitnesses, population = zip(*sorted(zip(fitnesses, population), reverse = True))
		#print("fitnesses", fitnesses)

		#selection of pairs
		pairs = [(selection(population, fitnesses)) for x in range(math.floor(population_size/2))]
		#print("pairs", pairs)

		#crossover
		new_population = [crossover(x, y) for (x, y) in pairs] #crossover returns tuples that must be unpacked
		new_population = list(chain.from_iterable(new_population))
		#print("crossed", new_population)

		#mutation
		new_population = list(map(mutation, new_population))
		#print("mutated", new_population)

		#update population
		population = new_population + [population[fitnesses.index(max(fitnesses))]]
		best_value = max(fitnesses)
		best_of_iter.append(best_value)
		# print("best: ", best_value)
		
		#stop criterium
		if(i>10):
			if (best_of_iter[i-10] == best_of_iter[i]): break

	return best_of_iter[-1]