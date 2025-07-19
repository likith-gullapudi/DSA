# https://cses.fi/problemset/task/1634
_,N=[int(x) for x in input().split()]
coins=[int(x) for x in input().split()]
dp=[float('inf') for i in range(N+1)]
for i in range(N+1):
    if i==0:
        dp[i]=0
    for coin in coins:
        if i-coin>=0:
            dp[i]=min(dp[i],1+dp[i-coin])
print(dp[N])
