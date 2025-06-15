import sys

for line in sys.stdin:
    n = int(line.strip())  # Read the size of the array
    arr = list(map(int, input().strip().split()))  # Read the array elements

    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Initialize dp table
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if i > j:
                continue
            if i == j:
                dp[i][j] = 0
                continue
            for k in range(i, j):
                left = (prefix_sum[k] - (prefix_sum[i - 1] if i - 1 >= 0 else 0)) % 100
                right = (prefix_sum[j] - prefix_sum[k]) % 100
                temp = left * right + dp[i][k] + dp[k + 1][j]
                dp[i][j] = min(dp[i][j], temp)

    print(dp[0][n - 1])
