n,M,co,do=[int(x) for x in input().split()]

s=[[0,0,co,do]]
for _ in range(M):
    s.append([int(x) for x in input().split()])
M+=1
# dp[w,m]-we are on model m with douhg left w dp[i,w] will give how much can earn from m to n-1 wiht w douhgt left
#base ease-dp[n]=0
#ew:dp[i][w]=dp[i+1][w-x*]
dp=[[0 for i in range(M+1)] for j in range(n+1)]
for w in range(n+1):
    for m in range(M-1,-1,-1):
        if m==M:
            dp[w][m]=0
            continue
        if w==0:
            dp[w][m]=0
            continue
        mul=0
        while s[m][0]>=mul*s[m][1] and w>=mul*s[m][2]:
            dp[w][m]=max(dp[w][m],dp[w-mul*s[m][2]][m+1]+mul*s[m][3])
            mul+=1


print(dp[n][0])



