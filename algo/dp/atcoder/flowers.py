n=int(input())
height=[int(x) for x in input().split()]
beauty=[int(x) for x in input().split()]
dp=[0 for i in range(n+1)]
for index in range(n):
    if index==0:
        dp[index]=beauty[0]
        continue
    else:
        dp[index]=beauty[index]
        for prev in range(index):
            if height[index]>=height[prev]:
                dp[index]=max(dp[index],dp[prev]+beauty[index])
print(max(dp))


