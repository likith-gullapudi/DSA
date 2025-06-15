dp=[[-1 for i in range(2000)] for j in range(2000)]
def rec(index,k):
    if index==n-1:
        return int(k==0)
    else:
        if dp[index][k]!=-1:
            return dp[index][k]
        dp[index][k]= (m-1)*rec(index+1,k-1)+rec(index+1,k)
        return dp[index][k]
for _ in range(int(input())):
    n,m,k=[int(x) for x in input().split()]
    for i in range(n+2):
        for j in range(m+2):
            dp[i][j]=-1

    print(m*rec(0,k))







