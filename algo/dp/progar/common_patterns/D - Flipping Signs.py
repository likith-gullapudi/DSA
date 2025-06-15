n=int(input())
arr=[int(x) for x in input().split()]
#dp[i] best answer from i to end
dp=[[0 for j in range(2)]  for i in range(n+1)]
#dp[i][change] means best answer from i( hanged if cahnge==1 else 0)#
#cahnging
#dp[i][change]=dp[i+1][1]+(arr[i] if change ==1 else -arr[i]
#

for i in range(n,-1,-1):
    for change in range(2):
        if i==n:
            dp[i][change]=0
            continue
        elif i==n-1:
            dp[i][change]=arr[i] if change==0 else -arr[i]
        else:
            #changing
            dp[i][change]=dp[i+1][1]+(arr[i] if change==1 else -arr[i])
            #Not chanigng
            dp[i][change]=max(dp[i][change],dp[i+1][0]+(-arr[i] if change==1 else arr[i]))
#print(dp)
print(dp[0][0])

