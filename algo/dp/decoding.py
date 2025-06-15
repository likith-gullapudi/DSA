'''
25114
form 1
meaning:- dp[i] no of diffenet ways from i to n

dp[i]=(dp[i+1] if arr[i]!=0)+(dp[i+2] if arr[i] in (1,2))

time complexity;-n*2

'''
n=int(input())
while n:
    arr=[x for x in str(n)]
    dp=[-1 for i in range(len(arr)+1)]
    #base case
    dp[len(arr)]=1
    for i in range(len(arr)-1,-1,-1):
        dp[i] = (dp[i + 1] if arr[i] != '0' else 0) + (dp[i + 2] if (i+2 <=len(arr) and arr[i] in ('1', '2')) else 0)
    print(dp[0])
    n=int(input())
