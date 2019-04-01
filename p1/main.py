from tester import *
from knapsackSolver import *

# print('Code from net: ', knapSack(W, w, c, len(c)))
# print('First alg: ', first_alg(W, w, c))
# print('Second alg: ', second_alg(W, w, c))

data = get_test_data(easy_path)
print("alg1")
test_alg(first_alg, data)
print("alg2")
test_alg(second_alg, data)
print("knapSack")
test_alg(lambda W, w, c: knapSack(W, w, c, len(c)), data)