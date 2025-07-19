a="abc"
b="acb"
n,m=len(a),len(b)
#dp[i][j] means lcs if a[:i+1] and b[:j+1]
#base case dp[all][-1]=0 and dp[-1][all]=0
#equation : if dp[i][j]=max((dp[i-1][j-1]+1 if s[i]==s[j]) ,dp[i-1][j],dp[i][j-1])
dp=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i==0 or j==0:
            continue
        dp[i][j]=max(((dp[i-1][j-1]+1) if a[i-1]==b[j-1] else 0) ,dp[i-1][j],dp[i][j-1])
    print(i,dp)
print(dp[n][m])
