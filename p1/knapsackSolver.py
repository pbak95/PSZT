W = 50
w = [10, 20, 30]
c = [60, 100, 120]


def init_array(n, m):
    """
    create n x m array filled with 0
    :param n:
    :param m:
    :return:
    """
    return [[0 for x in range(n)] for y in range(m)]


A = init_array(W, len(c))
print('Columns: ', len(A[0]))
print('Rows: ', len(A))


# Should return max value which could be placed in knapsack
# Alg with duplicating items (http://algorytmika.wikidot.com/problem-plecakowy)
for i in range(1, len(c)):
    for j in range(1, W):
        if j > w[i] and A[i-1][j] < A[i][j - w[i]] + c[i]:
            A[i][j] = A[i][j - w[i]] + c[i]
        else:
            A[i][j] = A[i - 1][j]

print('First alg: ', A[len(c) - 1][W - 1])

A = init_array(W, len(c))

# Alg with one number of each item (https://sites.google.com/site/topinfo12/home/programowanie-dynamiczne/problem-plecakowy-dyskretny)
for i in range(1, len(c)):
    for j in range(1, W):
        old = A[i-1][j]
        if w[i] > j:
            A[i][j] = old
        else:
            new = A[i - 1][j - w[i]] + c[i]
            if new > old:
                A[i][j] = new
            else:
                A[i][j] = old

print('Second alg: ', A[len(c) - 1][W - 1])


# Cos z neta(https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

print('Code from net: ', knapSack(W, w, c, len(c)))
