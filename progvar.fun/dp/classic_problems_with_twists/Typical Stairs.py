n,m=[int(x) for x in input().split()]
arr= set()
MOD=10**9+7
for _ in range(m):
    arr.add(int(input()))
dp=[0 for i in range(n+2)]
dp[n]=1
for i in range(n-1,-1,-1):
    if i in arr:
        continue
    dp[i]=dp[i+1]+dp[i+2]
    dp[i]%=MOD
print(dp[0])
