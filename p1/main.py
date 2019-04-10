from dynamicSolver import dynamic_alg
from tester import get_test_data, generate_test_data, easy_path, easy_path_full, test_alg, hard_path
# from tester import *
# from knapsackSolver import *
from GASolver import ga_solver

data = get_test_data(hard_path)

# print("[dynamic_alg]:")
# test_alg(dynamic_alg, data)

# print("[ga_solver]")
# test_alg(ga_solver, data)

example = generate_test_data(50, 10)
example["optimum"] = dynamic_alg(example["capacity"], example["weights"], example["values"])
test_alg(ga_solver, [example])
