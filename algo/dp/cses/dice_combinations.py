n=int(input())
dp=[0 for i in range(n+1)]
dp[0]=1
for i in range(1,n+1):
    for j in range(1,7):
        dp[i]+=dp[i-j] if i-j>=0 else 0
print(dp[n])
