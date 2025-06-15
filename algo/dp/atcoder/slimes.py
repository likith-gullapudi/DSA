n=int(input())
arr=[int(x) for x in input().split()]
prefix_sum=[0 for i in range(n+1)]
for i in range(1,n+1):
    prefix_sum[i]=prefix_sum[i-1]+arr[i-1]
dp=[[-1 for i in range(n)] for j in range(n)]
for l in range(n-1,-1,-1):
    for r in range(n):
        if l>r:
            continue
        elif l==r:
            dp[l][r]=0
            continue
        else:
            dp[l][r]=float('inf')
            for k in range(l,r):
                dp[l][r]=min(dp[l][r], dp[l][k]+dp[k+1][r]+prefix_sum[r+1]-prefix_sum[l])
print(dp[0][n-1])

