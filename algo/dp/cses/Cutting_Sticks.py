n=int(input())+2
cuts=[0]+[int(x) for x in input().split()]
#dp[l][r] means cost of stick lenght l to r
#base case dp[l][r]==0 if r-l<=1
#dp[l][r]=min(dp[l][k]+dp[k+1][r] k in range(l+1,r)
