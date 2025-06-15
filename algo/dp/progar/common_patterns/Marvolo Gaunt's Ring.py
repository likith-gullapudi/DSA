n,p,q,r=[int(x) for x in input().split()]
b=[p,q,r]
a=[int(x) for x in input().split()]
dp=[[-1 for i in range(3)] for j in range(n)]
def fun(i,j):
    if j==3:
        return 0
    if i==n:
        return -float('inf')
    if dp[i][j]!=-1:
        return dp[i][j]
    #take
    take=a[i]*b[j]+ fun(i,j+1)
    #not take
    not_take=fun(i+1,j)
    dp[i][j]=max(take,not_take)
    return max(take,not_take)
print(fun(0,0))