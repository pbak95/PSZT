from tester import *
from knapsackSolver import *
from GASolver import ga_solver

data = get_test_data(easy_path)

# print("knapSack")
# test_alg(lambda W, w, c: knapSack(W, w, c, len(c)), data)
print("ga")
test_alg(ga_solver, data)



W = 50
w = [10, 20, 30]
c = [60, 100, 120]
values_a = [135,139,149,150,156,163,173,184,192,201,210,214,221,229,240]
sizes_a = [70,73,77,80,82,87,90,94,98,106,110,113,115,118,120]
capacity_a = 750

ga_solver(capacity_a, sizes_a, values_a)