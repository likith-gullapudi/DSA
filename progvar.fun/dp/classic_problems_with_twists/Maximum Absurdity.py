n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
#dp[i][times] means max value we can from 0 to i taking t times
#base case dp[0..k-2][times]=0 and dp[k-1][1]=sum(arr[:k])
#eq : dp[i][times]=max(dp[i-k][times] ,dp[i-k][times-1]+sum(arr[i-k:i+1]

prefix_sum=[arr[i] for i in range(n)]
for i in range(1,n):
    prefix_sum[i]+=prefix_sum[i-1]

dp=[[0,0,0] for i in range(n)]
dp[k-1][1]=prefix_sum[k-1]
dp[k-1][2]=prefix_sum[k-1]
path=[[0,0,0] for i in range(n)]
path[k-1][1]=1
path[k-1][2]=1
for i in range(k,n):
    for time in range(3):
        if time==0 or (dp[i-1][time]>(dp[i-k][time-1]+prefix_sum[i]-prefix_sum[i-k])):
            path[i][time]=0
            dp[i][time]=dp[i-1][time]
        else:
            path[i][time]=1
            dp[i][time]=dp[i-k][time-1]+prefix_sum[i]-prefix_sum[i-k]

# print(dp[n-1][2])
ans=[]
index=n-1
time=2
ans=[]
while index>-1:
    # print(index,time)
    if path[index][time]==1:
        ans.append(index-k+1)

        index-=k
        time-=1
    else:
        index-=1
for i in ans[::-1]:
    print(i+1,end=" ")

