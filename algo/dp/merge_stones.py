n = int(input())
arr = [int(x) for x in input().split()]
prefix = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]
# print(prefix)
dp = [[float('inf') for i in range(n)] for j in range(n)]


def rec(l, r):
    if l == r:
        return 0
    if dp[l][r] != -1:
        return dp[l][r]
    ans = float('inf')

    for k in range(l, r):
        cost = ((prefix[k + 1] - prefix[l]) % 100) * ((prefix[r + 1] - prefix[k + 1]) % 100)

        ans = min(ans, cost + rec(l, k) + rec(k + 1, r))
    dp[l][r] = ans
    return ans
for l in range(n-1,-1,-1):
    for r in range(n):
        if l>r:
            continue
        elif l==r:
            dp[l][r]=0
        else:
            for k in range(l,r):
                cost = ((prefix[k + 1] - prefix[l]) % 100) * ((prefix[r + 1] - prefix[k + 1]) % 100)
                print(l, k, r, cost)
                dp[l][r] = min(dp[l][r], cost + dp[l][k]+ dp[k+1][r])
print(dp)
print(dp[0][n-1])

