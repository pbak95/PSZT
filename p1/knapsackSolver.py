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
    return [[0] * m for i in range(n)]


A = init_array(len(c), W)
# print(A)

# Should return max value which could be placed in
for i in range(1, len(c)):
    for j in range(W):
        if w[i] > j:
            A[i][j] = A[i - 1][j]
        else:
            A[i][j] = max(A[i - 1][j], A[i - 1][j - w[i]] + c[i])

print(A[len(c) - 1][W - 1])

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


print(knapSack(W, w, c, len(c)))
