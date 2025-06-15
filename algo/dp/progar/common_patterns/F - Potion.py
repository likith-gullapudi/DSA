n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Initialize answer
ans = float('inf')

# Iterate over possible k values
for k in range(1, n + 1):
    # Create a DP table: dp[index][k][remain_sum]
    dp = [[[-float('inf')] * k for _ in range(k + 1)] for _ in range(n + 1)]

    # Base case: If we select 0 elements, the sum is 0, and remainder is 0
    dp[0][0][0] = 0

    # Fill the DP table
    for index in range(1, n + 1):
        for count in range(k + 1):
            for remain_sum in range(k):
                # Option 1: Don't take the current element
                dp[index][count][remain_sum] = dp[index - 1][count][remain_sum]

                # Option 2: Take the current element, if possible
                if count > 0:
                    prev_remain = (remain_sum - arr[index - 1]) % k
                    dp[index][count][remain_sum] = max(
                        dp[index][count][remain_sum],
                        dp[index - 1][count - 1][prev_remain] + arr[index - 1]
                    )

    # Check the result for this k\
    if dp[n][k][x % k] != -float('inf'):
        max_sum = dp[n][k][x % k]
        ans = min(ans, (x - max_sum) // k)

# Output the answer
print(ans if ans != float('inf') else -1)
