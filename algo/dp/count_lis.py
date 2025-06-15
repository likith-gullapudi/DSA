'''
form -2
meaning
dp[i] length of longest increasing sequnce from i to n
trnasiitinos
dp[i]=1+max(dp[j]) for j in i+1 to n-1 if arr[i]<arr[j]
base case
dp[n-1]=1
time complexity=n*n
'''
for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]

    dp=[0 for i in range(n+1)]
    dp[n]=0
    dp[n-1]=1
    for i in range(n-2,-1,-1):
        dp[i] =1+ max((dp[j] for j in range(i+1, n) if arr[i] < arr[j]),default=0)
    '''
    cnt[i] no of subsequnces with lenght[dp[i]] form i to n-1
    '''
    cnt=[1 for i in range(n+1)]
    cnt[n]=1
    cnt[n-1]=1
    arr.append(10**9)
    for i in range(n-2,-1,-1):
        cnt[i]=sum(cnt[j] for j in range(i+1,n+1) if ( arr[i]<arr[j] and dp[i]==dp[j]+1))
    m=max(dp)

    ans=0

    for index,i in enumerate(dp):
        if i==m:
            ans+=cnt[index]

    print(ans)





