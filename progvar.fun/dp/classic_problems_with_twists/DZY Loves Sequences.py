n=int(input())
arr=[int(x) for x in input().split()]
dp=[[0,0] for i in range(n)]
#meaning
#dp[i][used/not_used] means best increasing lenght from 0 to i with one used or not
#base case: dp[0][]=1
#equation: if arr[i]>arr[j] dp[i][j]+=max(dp[i-1])
ans=0
for i in range(n):
    for used in range(2):
        if i==0:
            dp[i][used]=1
            continue
        if arr[i]>arr[i-1]:
            dp[i][used]=1+dp[i-1][used]

        else:
            if used==0:
                dp[i][used]=1
            else:
                dp[i][used]=1+dp[i-1][0]
        if i >= 2 and arr[i] > arr[i - 2]:
            dp[i][1] = max(dp[i][1], dp[i - 2][0] + 2)

    ans=max(ans,max(dp[i]))
    # print(arr[i],i,dp[i])
print(ans)

