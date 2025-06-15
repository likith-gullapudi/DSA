for _ in range(int(input())):
    n=int(input())
    a="".join([x for x in input().split()])
    dp=[[-1 for j in range(n)] for i in range(n)]
    def fun(l,r):
        if l>=r:
            return True
        if dp[l][r]!=-1:
            return dp[l][r]
        temp= a[l]==a[r] and fun(l+1,r-1)
        dp[l][r]=temp
        return temp


    '''
    form 4
    dp(l,r) means minimum number of seconds needed to destroy all the gemstones.
    
    transitino
    dp(l,r)=dp(l,l'-1)+dp(r'+1,r) if dp[a[l':r'+1]] for  l',r' belongs to all pairs possible form l to r
    
    time complexity=n^2*n^2=n^4
    '''
    rec=[[-1 for i in range(len(a))] for j in range(len(a))]
    def destroy(l,r):

        if l>r:
            return 0
        if l==r:
            return 1
        if rec[l][r]!=-1:
            return rec[l][r]
        temp=float('inf')
        for l_dash in range(l,r+1):
            for r_dash in range(l_dash,r+1):
                if fun(l_dash,r_dash):
                    temp=min(temp,destroy(l,l_dash-1)+destroy(r_dash+1,r)+1)
        rec[l][r]=temp

        return temp
    print(fun(2,4))
    print(destroy(0,n-1))




