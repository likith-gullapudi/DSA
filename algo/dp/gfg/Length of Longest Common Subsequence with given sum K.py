a=[9, 11, 2, 1, 6, 2, 7]
b=[1, 2, 6, 9, 2, 3, 11, 7]
n,m=len(a),len(b)
x=int(input())
dp=[[[0 for i in range(x+1)] for k in range(m+1)] for z in range(n+1)]
for i in range(n,-1,-1):
    for j in range(m,-1,-1):
        for k in range(x,-1,-1):
            if i==n or j==m:
                dp[i][j][k]=0 if k==x else -float('inf')
                continue
            else:
                if a[i]==b[j]:
                    if k+a[i]<=x:
                        dp[i][j][k]=max(dp[i][j][k],1+dp[i+1][j+1][k+a[i]])
                dp[i][j][k]=max(dp[i][j][k],dp[i+1][j][k],dp[i][j+1][k])
print(dp[0][0][0])
