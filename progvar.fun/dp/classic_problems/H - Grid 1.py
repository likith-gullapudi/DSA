MOD=10**9+7
h,w=[int(x) for x in input().split()]
arr=[]
for _ in range(h):
    arr.append([x for x in input()])

#dp[h][w]=1
dp=[[0 for i in range(w+1)] for j in range(h+1)]
for i in range(h,0,-1):
    for j in range(w,0,-1):
        if i==h and j==w:
            dp[i][j]=1
            continue
        if arr[i-1][j-1]=="#":
            continue
        dp[i][j]=(dp[i+1][j] if i+1<=h  else 0) + (dp[i][j+1] if j+1<=w else 0)
        dp[i][j]%=MOD

print(dp[1][1])