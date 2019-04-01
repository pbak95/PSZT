import sys
import os

easy_path = r"..\test_data\low_dimensional"
hard_path = r"..\test_data\large_scale"

def get_test_data(path):
	data = []
	for name in os.listdir(path):
		with open(path+"\\"+name, "r") as file:
			example = {"weights": [], "values": []}
			example["capacity"] = int(file.readline().split(" ")[1])
			for line in file:
				pairs = line.split(" ")
				example["weights"].append(int(pairs[1]))
				example["values"].append(int(pairs[0]))

		with open(path+"_optimum"+"\\"+name, "r") as file:
			example["optimum"] = int(file.read().strip())

		data.append(example)

	return(data)


def test_alg(func, data):
	""" Tests given function with params: (capacity, weights, values) which returns optimum """
	for example in data:
		result = func(example["capacity"], example["weights"], example["values"])
		print("true: \t%d\ttested: \t%d" %(example["optimum"], result)) 	

