p=[int(x) for x in input().split()]
q=[int(x) for x in input().split()]
x=int(input())
n,m=len(p),len(q)
dp=[[[0 for i in range(x+1)] for j in range(m+1)] for k in range(m+1)]
for i in range(n,-1,-1):
    for j in range(m,-1,-1):
        for k in range(x+1):
            if i==n or j==m:
                dp[i][j][k]=0
                continue
            else:
                if p[i]==q[j]:
                    dp[i][j][k]=max(dp[i][j][k],1+dp[i+1][j+1][k])
                if k>0:
                    dp[i][j][k] = max(dp[i][j][k], 1 + dp[i + 1][j + 1][k-1])
                dp[i][j][k] = max(dp[i][j][k],  dp[i + 1][j ][k], dp[i ][j+1 ][k])
print(dp[0][0][x])
