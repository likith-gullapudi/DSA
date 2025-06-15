
for _ in range(int(input())):
    a,b,c=[x for x in input().split()]
    dp=[[[-1 for i in range(len(c))] for j in range(len(b))] for k in range(len(a))]
    def rec(i,j,k):

        if i==len(a) or j==len(b) or k==len(c):
            return 0
        if dp[i][j][k]!=-1:
            return dp[i][j][k]
        ans=-float('inf')
        if a[i]==b[j]==c[k]:
            ans=1+rec(i+1,j+1,k+1)
        ans=max(ans,rec(i+1,j,k),rec(i,j+1,k),rec(i,j,k+1))
        dp[i][j][k]=ans
        return ans
    print(rec(0,0,0))
