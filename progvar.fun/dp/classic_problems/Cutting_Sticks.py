l=int(input())
n=int(input())+2
cuts=[0]+[int(x) for x in input().split()]+[l]
#dp[l][r] means cost of stick lenght l to r
#base case dp[l][r]==0 if r-l<=1
#dp[l][r]=min(dp[l][k]+dp[k+1][r] k in range(l+1,r)
dp=[[float('inf') for i in range(n)] for j in range(n)]
for l in range(n-1,-1,-1):
    for r in range(n):
        if r-l<=1:
            dp[l][r]=0
            continue
        for k in range(l+1,r):
            dp[l][r]=min(dp[l][r],dp[l][k]+dp[k][r]+(cuts[r] - cuts[l]))
    print(l,dp[l])
print(dp[0][n-1])
