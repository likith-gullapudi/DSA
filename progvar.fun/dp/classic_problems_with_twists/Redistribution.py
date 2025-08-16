#dp[i][s] means from i to s how many ways we can make it to s
#base case dp[s][s]=1
#dp[i][s]=dp[i+1][s-i]+dp[i+1][s]
S=int(input())
dp=[[0 for i in range(S+1)] for j in range(S+2)]

for i in range(S,-1,-1):
    for s in range(S+1):
        # print(i,S)
        if s==0:
            dp[i][s]=1
            continue
        dp[i][s]=(dp[i][s-i] if s-i>=0 else 0)+dp[i+1][s]
    print(i,dp[i][S])
print(dp[3][S])