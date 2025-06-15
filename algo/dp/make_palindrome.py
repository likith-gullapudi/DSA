for _ in range(int(input())):
    s=input()
    dp=[[-1 for i in range(len(s))] for j in range(len(s))]
    def rec(l,r):
        if l>=r:
            return 0
        if dp[l][r]!=-1:
            return dp[l][r]
        if s[l]==s[r]:
            temp=rec(l+1,r-1)
        else:
            temp=min(rec(l,r-1),rec(l+1,r))+1
        dp[l][r]=temp
        return temp
    print(rec(0,len(s)-1))
