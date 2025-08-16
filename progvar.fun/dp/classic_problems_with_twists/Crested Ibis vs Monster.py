H,n=[int(x) for x in input().split()]
arr=[]
for _ in range(n):
    arr.append([int(x) for x in input().split()])
#dp[h][i] - min cost to decrease h heatlh using i to n-1 spells
#dp[0][...]=0 and dp[][n]=float('inf')
#dp[h][i]=dp[h-arr[i][0][i] or dp[h][i+1]
dp=[[float('inf') for i in range(n+1)] for j in range(H+1)]
for h in range(0,H+1):
    for i in range(n,-1,-1):
        if h==0:
            dp[h][i]=0
            continue
        if i==n:
            dp[h][n]=float('inf')
            continue
        dp[h][i]=min(dp[h][i],((dp[h-arr[i][0]][i]) if h-arr[i][0]>=0 else 0) +arr[i][1] ,dp[h][i+1])
print(dp[H][0])
