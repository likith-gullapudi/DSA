n=int(input())
arr=[int(x) for x in input().split()]
dp=[1 for i in range(n+1)]
for i in range(n):
    if i==0:
        dp[0]=1
        continue
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],1+dp[j])
print(max(dp))