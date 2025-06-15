#Find length of longest subsequence of one string which is substring of another string
s=input()
t=input()
n,m=len(s),len(t)
dp=[[0 for i in range(m) ] for j in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if i==0:
            dp[0][j]=int(s[0] in t[:j+1])
            continue
        if j==0:
            if s[i]==t[0]:
                dp[i][0]=1
            else:
                dp[i][0]=0
            continue

        if s[i]==t[j]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=dp[i][j-1]
    ans=max(ans,max(dp[i]))
print(ans)

