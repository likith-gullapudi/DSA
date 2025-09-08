for _ in range(int(input())):
    aa=int(input())
    passwords=[x for x in input().split()]
    s=input()
    # print(passwords,s)
    n=len(s)
    #dp[i]->returns what string we should take to complete the assignment
    #base case dp[n]=n
    #dp[i]=for j in range(i,n):dp[i]=x if passwords[x]==s[i:i+len(passwords[x]] and dp[i]!=-1
    dp=[-1 for i in range(n+1)]
    dp[n]=n
    for i in range(n-1,-1,-1):
        for x in range(len(passwords)):
            # if i+len(passwords[x])<=n:
            #     print(x,passwords[x],s[i:i+len(passwords)],passwords[x]==s[i:i+len(passwords)],dp[i+len(passwords[x])])
            if passwords[x]==s[i:i+len(passwords[x])] and i+len(passwords[x])<=n and dp[i+len(passwords[x])]!=-1:
                dp[i]=x
                continue
        # print(i,dp[i])
    if dp[0]==-1:
        print("WRONG PASSWORD")
    else:
        i=0
        while i!=n:
            print(passwords[dp[i]],end=" ")
            i+=len(passwords[dp[i]])

