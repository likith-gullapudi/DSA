n,k=[int(x) for x in input().split()]
h=[0]+[int(x) for x in input().split()]
dp=[float('inf') for i in range(n+1)]
for i in range(n,0,-1):
    if i==n:
        dp[i]=0
        continue
    else:
        for j in range(i+1,min(n+1,i+k+1)):
            dp[i]=min(dp[i],dp[j]+abs(h[j]-h[i]))
#print(dp)
print(dp[1])