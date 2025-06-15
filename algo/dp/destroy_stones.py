def fun(l,r):
    if l>r:
        return 0
    if l==r:
        return 1
    if dp[l][r]!=-1:
        return dp[l][r]
    ans=1+fun(l+1,r)
    if s[l]==s[l+1]:
        ans=min(ans,1+fun(l+2,r))
    for k in range(l+2,r+1):
        if s[l]==s[k]:
            ans=min(ans,fun(l+1,k-1)+fun(k+1,r))
    dp[l][r]=ans
    return ans

for _ in range(int(input())):
    n=int(input())
    s=[int(x) for x in input().split()]
    dp=[[-1 for i in range(n)] for j in range(n)]

    print(fun(0,len(s)-1))
