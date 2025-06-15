#dp[i]=or(dp[i-coins])
n=int(input())
coins=[int(x) for x in input().split()]
s=n*max(coins)
#THIS WHEN WE CAN USE COIN ANY NUMBER OF TIME
# dp=[False for i in range(s+1)]
# dp[0]=True
# ans=0
# for i in range(1,s+1):
#     for j in coins:
#         dp[i]|=dp[i-j] if i-j>=0 else False
#     if dp[i]:
#         print(i)
# print(ans)
#WHEN WE CAN USE ONE COIUN ONE TIME
#

#dp[s][j]=dp[s-coins[j][j-1] or dp[s][j-1]
#base case dp[0][...]=True
dp=[[False for i in range(n)]for j in range(s+1)]
ans=[]
for su in range(s+1):
    for j in range(n):
        if j==0:
            if su==0 or su==coins[0]:
                dp[su][j]=True
            continue
        elif su==0:
            dp[su][j]=True
            continue
        dp[su][j]=(dp[su-coins[j]][j-1] if su-coins[j]>=0 else False) or (dp[su][j-1])

    if su!=0 and any(dp[su]):
        ans.append(str(su))
print(len(ans))
print(' '.join(ans))

