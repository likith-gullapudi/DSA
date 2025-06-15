#LCS formed by consecutive segments of at least length K
s=input()
t=input()
k=int(input())
n,m=len(s),len(t)
dp=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n,-1,-1):
    for j in range(m,-1,-1):

        if i==n or j==m:
            dp[i][j]=0
            continue
        else:
            if i+k<=n and j+k<=m:
                if s[i:i+k]==t[j:j+k]:
                    dp[i][j]=k+dp[i+k][j+k]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
for i in dp:
    print(i)
print(dp[0][0])