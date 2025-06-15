n=int(input())
arr=[int(x) for x in input().split()]
dp=[[-1 for i in range(n)] for j in range(n)]
for l in range(n-1,-1,-1):
    for r in range(n):
        if l>r:
            continue
        elif l==r:
            dp[l][r]=arr[l]
            continue
        else:
            dp[l][r]=max(arr[l]-dp[l+1][r],arr[r]-dp[l][r-1])
print(dp[0][n-1])
