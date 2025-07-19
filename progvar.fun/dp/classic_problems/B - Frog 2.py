#https://atcoder.jp/contests/dp/tasks/dp_a
N,K=[int(x) for x in input().split()]
arr=[0]+[int(x) for x in input().split()]
#have to find cost to reach N
#so cost to reach N to N is 0
#so base case dp[N]=0
dp=[float('inf') for i in range(N+1)]
for n in range(N,0,-1):
    if n==N:
        dp[n]=0
        continue
    for k in range(n+1,min(N+1,n+K+1)):
        dp[n]=min(dp[n],dp[k]+abs(arr[n]-arr[k]))

print(dp[1])

