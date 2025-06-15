n = int(input())
arr = [int(x) for x in input().split()]

# Initialize a DP table with -1 to indicate uncomputed states
dp = [[-1] * n for _ in range(n)]
mode=[[-1]*n for _ in range(n)]
def min_with_index(options):
    """Find the minimum value and its index."""
    min_val, min_idx = float('inf'), -1
    for idx, val in enumerate(options):
        if val < min_val:
            min_val, min_idx = val, idx
    return min_idx, min_val
def printsol(i,j):
    if j >= n:
        print(i+1)
        return
    if j == n - 1:
        print(i+1,j+1)
        return
    if mode[i][j]==0:
        print(j+1,j+1+1)
        printsol(i,j+2)
    elif mode[i][j]==1:
        print(i+1,j+1+1)
        printsol(j,j+2)
    else:
        print(i+1,j+1)
        printsol(j+1,j+2)

def fun(i, j):
    # Base cases
    if j >= n:
        return arr[i]
    if j == n - 1:
        return max(arr[i], arr[j])

    # If already computed, return the value
    if dp[i][j] != -1:
        return dp[i][j]

    # Compute the minimum of the three possible cases
    #taking j and j+1
    one=fun(i, j + 2) + max(arr[j], arr[j + 1])
    #taking i and j+1
    two=fun(j, j + 2) + max(arr[i], arr[j + 1])
    #taking i and j+2
    three=fun(j + 1, j + 2) + max(arr[i], arr[j])

    mode[i][j],dp[i][j] = min_with_index([one,two,three])
    return dp[i][j]


# Call the function and print the result
print(fun(0, 1))
printsol(0,1)
