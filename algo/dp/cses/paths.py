n=int(input())
arr=[]
for _ in range(n):
    arr.append([x for x in input()])
dp=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n,-1,-1):
    for j in range(n,-1,-1):
        if i==n or j==n:
            dp[i][j]=0
        elif arr[i][j]=="*":
            dp[i][j]=0
        elif i==n-1 and j==n-1:
            dp[i][j]=1

        else:
            dp[i][j]=(dp[i+1][j]+dp[i][j+1])%(10**9+7)
#print(dp)
print(dp[0][0])