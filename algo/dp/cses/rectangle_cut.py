a,b=[int(x) for x in input().split()]
dp=[[float('inf') for i in range(b+1)] for j in range(a+1)]

for l in range(1,a+1):
    for b in range(1,b+1):
        if l==b:
            dp[l][b]=0
            continue
        for k in range(1,l):
            dp[l][b]=min(dp[l][b],1+dp[k][b]+dp[l-k][b])
        for k in range(1,b):
            dp[l][b]=min(dp[l][b],1+dp[l][k]+dp[l][b-k])
print(dp[a][b])
