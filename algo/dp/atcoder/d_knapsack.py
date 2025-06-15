n,w=[int(x) for x in input().split()]
arr=[]
for _ in range(n):
    arr.append([int(x) for x in input().split() ])
dp=[[-1 for i in range(w+1)] for j in range(n+1)]
for index in range(n,-1,-1):
    for wei in range(w+1):
        if index==n:
            dp[index][wei]=0
            continue
        if wei==0:
            dp[index][wei]=0
            continue
        dp[index][wei]=max(dp[index+1][wei],(dp[index+1][wei-arr[index][0]]+arr[index][1]) if wei-arr[index][0]>=0 else 0)
print(dp[0][w])
