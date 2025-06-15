n=int(input())

p=[float(i) for i in input().split()]
dp=[[-1 for i in range(n+1)] for j in range(n+1)]
for index in range(n,-1,-1):
    for head in range(index,-1,-1):
        if index==n:
            tails=n-head
            dp[index][head]=int(head>tails)
            continue
        else:
            dp[index][head]=p[index]*dp[index+1][head+1]+(1-p[index])*dp[index+1][head]
print(dp[0][0])