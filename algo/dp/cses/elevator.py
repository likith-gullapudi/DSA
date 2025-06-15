import math

print(math.log10(2**20))
n, x = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

# Initialize memoization dictionary
memo = {}


def fun(w, s):
    # Check if the result for this state (w, s) is already computed
    if (w, s) in memo:
        return memo[(w, s)]

    if s == (1 << n) - 1:
        return 0

    # Initialize the answer to infinity (minimization problem)
    ans = float('inf')

    # Iterate over all items
    for i in range(n):
        if (s & (1 << i)) == 0:  # Item i is not yet taken
            if arr[i] + w <= x:
                ans = min(ans, fun(w + arr[i], s | (1 << i)))
            else:
                ans = min(ans, 1 + fun(arr[i], s | (1 << i)))

    # Store the result in memo
    memo[(w, s)] = ans
    return ans


print(1 + fun(0, 0))
