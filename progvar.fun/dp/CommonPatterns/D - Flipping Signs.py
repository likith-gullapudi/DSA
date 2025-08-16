n=int(input())
arr=[int(x) for x in input().split()]
#dp[i][changed] means from i to n-1 how much max we can get such that present i changed changed times already
#dp[n-1][changed]=-arr[n-1] if changed else arr[n-1]
#dp[i][c]=
dp=[[-1,-1] for i in range(n)]
def helper(i,c):
    return arr[i] if c==0 else -arr[i]
for i in range(n-1,-1,-1):
    for c in range(2):
        if i==n-1:
            dp[i][c]=helper(i,c)
            continue
        #no_take
        dp[i][c]=helper(i,c)+dp[i+1][0]
        #take
        dp[i][c]=max(dp[i][c],helper(i,(c+1)%2)+dp[i+1][1])
    # print(i,dp[i])
print(dp[0][0])

