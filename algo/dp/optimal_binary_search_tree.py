n=int(input())
keys=[int(x) for x in input().split()]
fre=[int(x) for x in input().split()]
dp=[[-1 for i in range(n)] for j in range(n)]
def fun(i,l,r):
    if l>r:
        return 0
    if l==r:
        return i*fre[l]
    if dp[l][r]!=-1:
        return dp[l][r]
    temp=float('inf')
    for k in range(l,r+1):
        temp=min(temp,fun(i+1,l,k-1)+fun(i+1,k+1,r) +fre[k-1]*i )
    dp[l][r]=temp
    return temp
print(fun(1,0,n-1))
