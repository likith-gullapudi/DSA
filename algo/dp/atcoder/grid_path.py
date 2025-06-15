mod=10**9+7
n,m=[int(x) for x in input().split()]
arr=[]
for _ in range(n):
    arr.append([x for x in input()])
dp=[[-1 for i in range(m+1)] for j in range(n+1)]
for i in range(n,-1,-1):
    for j in range(m,-1,-1):
        #print(i,j)
        if i==n or j==m or arr[i][j]=='#':
            dp[i][j]=0
            continue

        elif i==n-1 and j==m-1:
            dp[i][j]=1
            continue
        else:
            dp[i][j]=(dp[i+1][j]+dp[i][j+1])%mod
print(dp[0][0])
