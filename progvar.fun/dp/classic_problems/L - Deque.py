#https://atcoder.jp/contests/dp/tasks/dp_l
#dp[l][r][0/1] best answer from array (l,r) if it is 0 find we should add and value should be greater if 1 vice verse
#base case r>l return 0
#dp[l][r][0/1]=dp[l+1][r][0/1] or dp[l][r-1][0/1]
n=int(input())
arr=[int(x) for x in input().split()]
dp=[[[0,0] for i in range(n+1)] for j in range(n+1)]
for l in range(n-1,-1,-1):
    for r in range(l,n):
        for turn in range(0,2):
            if turn==0:
                dp[l][r][0]=max(arr[l]+dp[l+1][r][1],arr[r]+dp[l][r-1][1])
            else:
                dp[l][r][1] = min(-arr[l] + dp[l + 1][r][0], -arr[r] + dp[l][r - 1][0])
print(dp[0][n-1][0])
