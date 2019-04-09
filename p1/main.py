from p1.dynamicSolver import dynamic_alg
from p1.tester import get_test_data, easy_path, test_alg, hard_path
# from tester import *
# from knapsackSolver import *
from p1.GASolver import ga_solver

data = get_test_data(hard_path)

# print("[dynamic_alg]:")
# test_alg(dynamic_alg, data)

# print("[ga_solver]")
# test_alg(ga_solver, data)


W = 50
w = [10, 20, 30]
c = [60, 100, 120]
values_a = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
sizes_a = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
capacity_a = 750

#print(ga_solver(capacity_a, sizes_a, values_a))
test_alg(ga_solver, data)
