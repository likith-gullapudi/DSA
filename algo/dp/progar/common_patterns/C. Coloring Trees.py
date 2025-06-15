import sys
sys.setrecursionlimit(10**5)
n, m, K = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
cost = []
for _ in range(n):
    cost.append([int(x) for x in input().split()])

# Memoization dictionary
dp = {}


def fun(index, prev, k):
    # Memoization check
    if (index, prev, k) in dp:
        return dp[(index, prev, k)]

    # Base case
    if index == n:
        if k == K:
            return 0
        return float('inf')

    ans = float('inf')
    if arr[index] == 0:
        # Try all colors for the current tree
        for val in range(1, m + 1):
            if val == prev:
                ans = min(ans, cost[index][val - 1] + fun(index + 1, val, k))
            else:
                ans = min(ans, cost[index][val - 1] + fun(index + 1, val, k + 1))
    else:
        # If the tree is already painted
        if arr[index] == prev:
            ans = min(ans, fun(index + 1, prev, k))
        else:
            ans = min(ans, fun(index + 1, arr[index], k + 1))

    # Store in memoization dictionary
    dp[(index, prev, k)] = ans
    return ans


# Initial call
result = fun(0, 0, 0)
print(result if result != float('inf') else -1)
