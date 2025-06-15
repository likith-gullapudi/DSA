#form-2
#meaning no of ways to reach (n-1,m-1) from (i,j) having k valus as k
MOD=10**9+7
def rec(i,j,k):
    #base case

    if i==n-1 and j==n-1:
        return 1
    #print(i,j,len(dp),len(dp[0]),len(dp[0][0]))
    if dp[i][j][k]!=-1:
        return dp[i][j][k]
    ans=0
    if 0<=(i+1)<n and 0<=j<m:
        if arr[i+1][j]==0:
            if k>0:
                ans+=rec(i+1,j,k-1)
        else:
            ans+=rec(i+1,j,k)
    if 0<=i<n and 0<=(j+1)<m:
        if arr[i][j+1]==0:
            if k>0:
                ans+=rec(i,j+1,k-1)
        else:
            ans+=rec(i,j+1,k)
    dp[i][j][k]=ans%MOD
    return ans



for _ in range(int(input())):
    n,m,k=[int(x) for x in input().split()]
    arr=[]

    for _ in range(n):
        arr.append([int(x) for x in input().split()])
    dp=[[[-1 for k in range(k+1)] for i in range(m)] for j in range(n)]
    print(rec(0,0,k-int(arr[0][0]==1)))


