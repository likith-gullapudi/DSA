'''
1 2 3 4 5
form-4
meaning:-dp[i][j] means cost to make array arr[i:j+1] to one element
transition:-dp[l][r]=min(dp[l][x]+dp[x+1][r]+(p[x]-p[l-1])*p[r]-p[x]) for x in range(l,r))
base case if i==j=0 dp[i][j]=0
time complexity=n^2*(1+n)=n^3


'''
n=int(input())
arr=[int(x) for x in input().split()]
p=[0 for i in range(n+1)]
for i in range(1,n+1):
    p[i]=p[i-1]+arr[i-1]
dp=[[0 for i in range(n)] for j in range(n)]
for k in range(1,n):
    for l in range(n):
        r=l+k
        if r==n:
            break
        dp[l][r]=float('inf')
        dp[l][r]= min(dp[l][x]+dp[x+1][r]+((p[x+1]-p[l])%100)*((p[r+1]-p[x+1])%100) for x in range(l,r))%100
print(dp[0][n-1])
