import sys
import os
import time
from random import randint


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

def generate_test_data(size, ratio):
    """Generates test data  where 
        size = number of items
        ratio = backpack capacity / average item weight (uniform dist.)
        or average number of items fitting in backpack"""
    max_weight = 100
    example = {"capacity": max_weight / 2 * ratio}
    example["weights"] = [randint(1, max_weight) for _ in range(size)]
    example["values"] = [randint(1, 100) for _ in range(size)]
    example["optimum"] = None
    return example


def test_alg(func, data):
    """ Tests given function with params: (capacity, weights, values) which returns optimum """
    for example in data:
        start_time = time.clock()
        result = func(example["capacity"], example["weights"], example["values"])
        print("execution time:\t", time.clock() - start_time, " seconds")
        print("optimum: \t%d\ttested: \t%d" % (example["optimum"], result))
