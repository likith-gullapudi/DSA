# https://cses.fi/problemset/task/1634
MOD=10**9+7
_,N=[int(x) for x in input().split()]
coins=[int(x) for x in input().split()]
dp=[0 for i in range(N+1)]
for coin in coins:
    dp[coin]=1
for i in range(1,N+1):
    for coin in coins:
        if i-coin>=0:
            dp[i]+=dp[i-coin]
            dp[i]%=MOD
print(dp[N])
