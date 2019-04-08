from tester import *
from knapsackSolver import *
from GASolver import ga_solver

data = get_test_data(easy_path)

print("knapSack")
test_alg(lambda W, w, c: knapSack(W, w, c, len(c)), data)
print("ga")
test_alg(ga_solver, data)