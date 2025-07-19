#https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=503#google_vignette
n=int(input())
coins=[int(x) for x in input().split()]
s=sum(coins)
#find is sum that is near to s//2 using all these coins
#dp[p][index] is it possible to make p amount from coins 0 to index
#base case
#dp[coin][coin_index]=True
#dp[p][index]=dp[p-coin[index]][index-1] or dp[p][index-1]
dp=[[False for i in range(n)] for j in range(s)]
for index,coin in enumerate(coins):
    dp[coin][index]=True
for p in range(s):
    for i in range(n):
        if p==0:
            dp[p][i]=True
            continue
        if p-p-coins[i]>=0:
            dp[p][i]=dp[p-coins[i]][i-1]
        dp[p][i]=dp[p][i] or dp[p][i-1]
for p in range(s//2,-1,-1):
    if dp[p][n-1]:
        print(abs(p-s+p))
        break

