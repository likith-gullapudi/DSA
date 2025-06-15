n = int(input())
arr = [int(x) for x in input().split()]
dp = [[float('inf')] * n for _ in range(n)]  # Initialize with infinity for minimum comparison

for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if i == j:
            dp[i][j] = 1  # Single element needs 1 partition
        else:
            # Default: Increment partition size
            dp[i][j] = 1 + dp[i + 1][j]

            # If two consecutive elements are the same
            if i + 1 < n and arr[i] == arr[i + 1]:
                dp[i][j] = min(dp[i][j], 1 + (dp[i + 2][j] if i + 2 <= j else 0))

            # Check for matching elements in the range
            for k in range(i + 2, j + 1):
                if arr[i] == arr[k]:
                    dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + (dp[k + 1][j] if k + 1 <= j else 0))

print(dp[0][n - 1])
