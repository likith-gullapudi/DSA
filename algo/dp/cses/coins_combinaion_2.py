n,sum=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]

dp=[[0 for i in range(n+1)] for j in range(sum+1)]
for sum in range(0,sum+1):
    for index in range(n,-1,-1):
        #print(sum,index,len(dp),len(dp[0]))
        if sum==0:
            dp[sum][index]=1
        elif index==n:
            dp[sum][index]=0
        else:
            dp[sum][index]+=(dp[sum-arr[index]][index] if sum-arr[index]>=0 else 0)+dp[sum][index+1]
#print(dp)
print(dp[sum][0]%(10**9+7))

