s=input()
t=input()
t=t[::-1]
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
def printsol(i,j,ans):
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            ans+=s[i]
            i+=1
            j+=1
        elif dp[i][j]==dp[i+1][j]:
            i+=1
        else:
            j+=1
    print(ans)

printsol(0,0,'')