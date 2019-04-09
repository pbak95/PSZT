from p1.knapsackSolver import dynamic_alg, knapSack
from p1.tester import get_test_data, easy_path, test_alg, hard_path
# from tester import *
# from knapsackSolver import *

data = get_test_data(hard_path)

print("[dynamic_alg]:")
test_alg(dynamic_alg, data)
print("[knapSack]:")
test_alg(lambda W, w, c: knapSack(W, w, c, len(c)), data)