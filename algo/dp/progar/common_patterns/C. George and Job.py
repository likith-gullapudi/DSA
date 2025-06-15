n,m,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
pre=[0 for i in range(n)]
pre[0]=arr[0]
for i in range(1,n):
    pre[i]+=pre[i-1]+arr[i]
dp=[[-1 for i in range(k+1)] for j in range(n+1)]
#dp[i][j] starting from index i and having j more pairs
#base case dp[][0]=0
#base case dp[n][]=0
for i in range(n,-1,-1):
    for j in range(k+1):
        if i==n:
            dp[i][j]=0
            continue
        if j==0:
            dp[i][j]=0
            continue
        if i+m-1>=n:
            dp[i][j]=-float('inf')
            continue
        dp[i][j]=max(dp[i+1][j],dp[i+m][j-1]+pre[i+m-1]-(pre[i-1] if i-1>=0 else 0))
print(dp[0][k])



