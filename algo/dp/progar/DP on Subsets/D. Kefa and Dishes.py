n, M, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
d = {}

# Store rules in a dictionary
for _ in range(k):
    a, b, c = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    d[(a, b)] = max(d.get((a, b), -float('inf')), c)

# DP table: dp[bitset][prev]
dp = [[-float('inf')] * (n + 1) for _ in range(1 << n)]
dp[0][n] = 0  # Base case: no dishes selected, "prev" is dummy

# Iterate over all bitsets (subsets of dishes)
for bitset in range(1 << n):
    m = bin(bitset).count('1')  # Number of selected dishes
    if m > M:
        continue
    for prev in range(n + 1):  # Iterate over all possible previous dishes
        if dp[bitset][prev] == -float('inf'):
            continue
        for next_dish in range(n):  # Iterate over all possible next dishes
            if bitset & (1 << next_dish) == 0:  # Check if `next_dish` is not selected
                next_bitset = bitset | (1 << next_dish)
                bonus = d.get((prev, next_dish), 0) if prev < n else 0
                dp[next_bitset][next_dish] = max(
                    dp[next_bitset][next_dish],
                    dp[bitset][prev] + arr[next_dish] + bonus
                )

# Find the maximum satisfaction with exactly M dishes
max_satisfaction = -float('inf')
for bitset in range(1 << n):
    if bin(bitset).count('1') == M:  # Check if exactly M dishes are selected
        max_satisfaction = max(max_satisfaction, max(dp[bitset]))

print(max_satisfaction)
