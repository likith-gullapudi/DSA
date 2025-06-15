n,w=[int(x) for x in input().split()]
arr=[]
max_price=0
for _ in range(n):
    arr.append([int(x) for x in input().split() ])
    max_price=max(max_price,arr[-1][1])
dp=[[float('inf') for i in range(max_price*n)] for j in range(n+1)]
for index in range(n,-1,-1):
    for pr in range(len(dp[0])):
        if index==n:
            dp[index][pr]=0
            continue

        else:
            dp[index][pr]=min(dp[index+1][pr],(dp[index+1][pr-arr[index][1]]+arr[index][0] if pr-arr[index[1]<=0 else float('inf')])
ans=-float('inf')
for i in range(len(dp[1])):
    if dp[0][i]<=w:
        ans=max(ans,i)
print(ans)