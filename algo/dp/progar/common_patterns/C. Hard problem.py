n=int(input())
arr=[int(x) for x in input().split()]
s=[]
for _ in range(n):
    s.append(input())
dp=[[-1 for i in range(2)] for j in range(n)]
for i in range(n):
    if i==0:
        dp[i][0]=0
        dp[i][1]=arr[0]
        continue
    else:
        dp[i][0]=min(float('inf'),dp[i-1][0] if s[i]>=s[i-1] else float('inf'),
                        dp[i-1][1] if s[i]>=s[i-1][::-1] else float('inf') )
        dp[i][1]=arr[i]+min(float('inf'),dp[i-1][0] if s[i][::-1]>=s[i-1] else float('inf'),
                            dp[i-1][1] if s[i][::-1]>=s[i-1][::-1] else float('inf'))
#print(dp)
print(min(dp[n-1]) if min(dp[n-1])!=float('inf') else -1)


