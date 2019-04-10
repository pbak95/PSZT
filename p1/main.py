from p1.dynamicSolver import dynamic_alg
from p1.tester import get_test_data, generate_test_data, easy_path, easy_path_full, test_alg, hard_path
# from tester import *
# from knapsackSolver import *
from p1.GASolver import ga_solver

data = get_test_data(easy_path)

print("[dynamic_alg]:")
test_alg(dynamic_alg, data, 10)

print("[ga_solver]")
test_alg(ga_solver, data, 10)

# example = generate_test_data(50, 10)
# example["optimum"] = dynamic_alg(example["capacity"], example["weights"], example["values"])
# test_alg(ga_solver, [example])
