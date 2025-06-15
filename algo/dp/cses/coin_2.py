n,s=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
dp=[0 for i in range(s+1)]
MOD=10**9+7
dp[0]=1
for su in range(1,s+1):
    for coins in arr:
        if su-coins>=0:
            dp[su]+=dp[su-coins]
            dp[su]%=MOD

print(dp[s])