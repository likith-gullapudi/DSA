
#dp[l][r] cost of arr[l,r]
#dp[l][r]=dp[l][k]+dp[k+1][r] +sum(arr[k]-arr[i-1]+arr[r]-arr[k])
#dp[l][l]=0
def fun(l,r):
    if l==0:
        return prefix[r]
    return prefix[r]-prefix[l-1]


n=int(input())
arr=[int(x) for x in input().split()]
dp=[[float('inf') for i in range(n)] for j in range(n)]
prefix=[arr[i] for i in range(n)]
for i in range(1,n):
    prefix[i]+=prefix[i-1]

for l in range(1,n+1):
    for i in range(n):
        j=i+l-1
        if j>=n:
            continue
        if l==1:
            dp[i][j]=0
            continue
        for k in range(i+1,j+1):
            dp[i][j]=min(dp[i][j],dp[i][k-1]+dp[k][j]+fun(j,i))
        print(i,j,dp[i][j])
print(dp[0][n-1])





