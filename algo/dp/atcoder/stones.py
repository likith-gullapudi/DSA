n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
dp=[False for i in range(k+1)]
for i in range(min(arr),k+1):
    dp[i]=True if any(dp[i-j]==False for j in arr if i-j>=0) else False


print('First' if dp[k] else 'Second')