MOD=10**9+7
n,P=[int(x) for x in input().split()]
coins=[int(x) for x in input().split()]
dp=[[0 for i in range(n)] for j in range(P+1)]
for index,coin in enumerate(coins):
    dp[coin][index]=1
for p in range(P+1):
    for j in range(n):
        if p-coins[j]>=0:
            dp[p][j]+=dp[p-coins[j]][j]
        dp[p][j]+=dp[p][j-1] if j-1>=0 else 0
    # print(p,dp[p])
print(dp[P][n-1])