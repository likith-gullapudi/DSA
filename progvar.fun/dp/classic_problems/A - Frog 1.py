#https://atcoder.jp/contests/dp/tasks/dp_a
N=int(input())
arr=[0]+[int(x) for x in input().split()]
#have to find cost to reach N
#so cost to reach N to N is 0
#so base case dp[N]=0
dp=[0 for i in range(N+1)]
for n in range(N,0,-1):
    if N==n:
        dp[n]=0
        continue
    dp[n]=dp[n+1]+abs(arr[n]-arr[n+1])
    if n+2<=N:
        dp[n]=min(dp[n],dp[n+2]+abs(arr[n]-arr[n+2]))
print(dp[1])

