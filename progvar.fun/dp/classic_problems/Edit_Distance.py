#https://cses.fi/problemset/task/1639
#dp[i][j] edit distance of s[:i+1] to b[:j+1]
#base case dp[-1][j]=j and dp[i][-1]=i
#dp[i][j]=dp[i-1][j-1],dp[i-1][j],dp[j][i-1]
a=input()
b=input()
n,m=len(a),len(b)
dp=[[float('inf') for i in range(m+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i==0 or j==0:
            dp[i][j]=max(i,j)
            continue
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]
        dp[i][j]=min(dp[i][j],1+dp[i-1][j],1+dp[i][j-1],1+dp[i-1][j-1])

print(dp[n][m])