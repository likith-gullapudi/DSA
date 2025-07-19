#https://cses.fi/problemset/task/1158
#dp[0][i...N]=0 #if money is zero what ever books you have you cant take pages
N,P=[int(x) for x in input().split()]
p=[int(x) for x in input().split()]
n=[int(x) for x in input().split()]
dp=[[0 for i in range(N+1)]for j in range(P+1)]
for i in range(P+1):
    for j in range(1,N+1):
        dp[i][j]=dp[i][j-1]
        if i-p[j-1]>=0:
            dp[i][j]=max(dp[i][j],n[j-1]+dp[i-p[j-1]][j-1])
    # print(i,dp[i])
print(max(dp[P]))


