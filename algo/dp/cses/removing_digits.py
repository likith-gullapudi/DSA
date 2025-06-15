s=int(input())
arr=[int(x) for x in str(s)]
n=len(arr)
dp=[float('inf') for i in range(s+1)]
for sum in range(s+1):
    for index in str(sum):
        index=int(index)
        if sum==0:
            dp[sum]=0
        else:
            dp[sum]=min(dp[sum],1+dp[sum-index])



print(dp[s])