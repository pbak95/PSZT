from tester import *
from knapsackSolver import *

data = get_test_data(easy_path)

print("alg1")
test_alg(first_alg, data)
print("alg2")
test_alg(second_alg, data)
print("knapSack")
test_alg(lambda W, w, c: knapSack(W, w, c, len(c)), data)