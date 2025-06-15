for _ in range(int(input())):
    n=int(input())
    s=[x for x in input().split()]
    print(s)
    def fun(l,r):
        if l>=r:
            return 1

        ans=1+fun(l+1,r)
        for k in range(l+1,r+1):
            if s[l]==s[k]:

                ans=min(ans,fun(l+1,k-1)+fun(k+1,r))
        return ans
    print(fun(0,len(s)-1))
