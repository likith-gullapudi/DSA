#Minimum cost to make Longest Common Subsequence of length k
def f(s):
    return ord(s)-ord('a')
s=input()
t=input()
dp=[[-1 for i in range(len(t)+1)] for j in range(len(s)+1)]
for i in range(len(s),-1,-1):
    for j in range(len(t),-1,-1):
        if i==len(s) or j==len(t):
            dp[i][j]=0
            continue
        else:
            if s[i]==t[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])
lcs=dp[0][0]


x=int(input())
n,m=len(s),len(t)

required=x-lcs
dp=[[[0 for i in range(required+1)] for j in range(m+1)] for k in range(n+1)]
print(f('l')^f('i'))
for i in range(n,-1,-1):
    for j in range(m,-1,-1):
        for changed in range(required+1):
            if i==n or j==m:
                dp[i][j][changed]=0 if changed==required else float('inf')
                #print(dp[i][j][changed])
                continue
            if s[i]==t[j]:
                dp[i][j][changed]=dp[i+1][j+1][changed]
                continue
            else:
                dp[i][j][changed]=min(dp[i][j+1][changed],dp[i+1][j][changed])
                if changed+1<=required:
                    print(s[i],t[j],(f(s[i])^f(t[j])))
                    dp[i][j][changed]=min((f(s[i])^f(t[j]))+dp[i+1][j+1][changed+1],dp[i][j][changed])

print(dp[0][0][0])





