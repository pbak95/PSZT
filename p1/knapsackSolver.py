def init_array(n, m):
    """
	create n x m array filled with 0
	:param n:
	:param m:
	:return:
	"""
    return [[0 for x in range(n)] for y in range(m)]

def dynamic_alg(W, w, c):
    A = init_array(W, len(c))
    for i in range(1, len(c)):
        for j in range(1, W):
            old = A[i - 1][j]
            if w[i] > j:
                A[i][j] = old
            else:
                new = A[i - 1][j - w[i]] + c[i]
                if new > old:
                    A[i][j] = new
                else:
                    A[i][j] = old
    return A[len(c) - 1][W - 1]


# Cos z neta dla testów(https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
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
