for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    dp = [0 for i in range(n+1)]

    for i in range(n-1,-1,-1):
        dp[i]=1+min(dp[i+1],float('inf') if i+k>n else dp[i+k])
    print(dp[0])

