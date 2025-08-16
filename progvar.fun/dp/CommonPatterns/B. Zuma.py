n=int(input())
arr=[int(x) for x in input().split()]
#dp[i][j] time to destroy i to j
#dp[i][j] =dp[i+1][k-1]+dp[k+1][j]
#base case when there is no same letter we need to remove it so 1+dp[i+1][k]
#when a[i]==a[i+1] also answer is dp[i+2][j]+1
dp=[[0 for i in range(n+1)]for j in range(n+1)]
for l in range(1,n+1):
    for i in range(n):
        j=i+l-1
        if j>=n:
            continue
        if l==1:
            dp[i][j]=1
            continue

        dp[i][j]=1+dp[i+1][j]
        # if i==1 and j==3:
        #     print(dp[i][j])
        if arr[i]==arr[i+1]:
            dp[i][j]=min(dp[i][j],1+dp[i+2][j])
            # if i == 1 and j == 3:
            #     print(dp[i][j])
        for k in range(i+2,min(n,j+1)):
            if arr[k]==arr[i]:
                dp[i][j]=min(dp[i][j], dp[i+1][k-1]+dp[k+1][j])
                # if i == 1 and j == 3:
                #     print(dp[i][j])
        # print(dp[i][j],arr[i:j+1],i,j)
print(dp[0][n-1])


