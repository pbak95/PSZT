import sys
import os
import time


easy_path = os.path.join("test_data", "low_dimensional")
hard_path = os.path.join("test_data", "large_scale")


def get_test_data(path):
    data = []
    for name in os.listdir(path):
        with open(os.path.join(path, name), "r") as file:
            example = {"weights": [], "values": []}
            example["capacity"] = int(file.readline().split(" ")[1])
            for line in file:
                pairs = line.split(" ")
                example["weights"].append(int(pairs[1]))
                example["values"].append(int(pairs[0]))

        with open(os.path.join(path + "_optimum", name), "r") as file:
            example["optimum"] = int(file.read().strip())

        data.append(example)

    return data


def test_alg(func, data):
	""" Tests given function with params: (capacity, weights, values) which returns optimum """
	for example in data:
		start_time = time.clock()
		result = func(example["capacity"], example["weights"], example["values"])
		print("execution time:\t", time.clock() - start_time, " seconds")
		print("true: \t%d\ttested: \t%d" %(example["optimum"], result)) 	


