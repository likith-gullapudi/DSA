#https://cses.fi/problemset/task/1643
n=int(input())
arr=[int(x) for x in input().split()]
dp=[0 for i in range(n)]
dp[0]=arr[0]
for i in range(1,n):
    dp[i]=max(dp[i-1]+arr[i],arr[i])
print(max(dp))
