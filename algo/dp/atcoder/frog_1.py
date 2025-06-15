n=int(input())
h=[0]+[int(x) for x in input().split()]
dp=[0 for i in range(n+1)]
for i in range(n,0,-1):
    if i==n:
        dp[i]=0
        continue
    else:
        dp[i]=min(dp[i+1]+abs(h[i+1]-h[i]),(dp[i+2]+abs(h[i+2]-h[i])) if i+2<=n else float('inf'))
#print(dp)
print(dp[1])