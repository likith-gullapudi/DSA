n=int(input())
d=int(input())
#dp[index][prev]=dp[index+1][ucrr]
dp=[[0 for i in range(26)] for j in range(n+1)]
for index in range(n,-1,-1):
    for prev in range(26):
        if index==n:
            dp[index][prev]=1
            continue
        else:
            for curr in range(max(0,prev-d),min(26,prev+d+1)):
                dp[index][prev]+=dp[index+1][curr]
print(sum(dp[1]))
