n,m,x,y=[int(x) for x in input().split()]
#dp[i][0/1] means answer for i to n-1 where i-1 is 1/0(so now it should change)
#dp[i][0/1] means we are on ith column where prev column is 0/1
#dp[i][0/1] for j in range(i+x,y+1) +=dp[j][0/1] +cost[y][0/1]-cost[y][0/1]
#base case dp[n]-->0 and dp[n+1] is like infinity
# .--->0 and #---> 1
arr=[]
for i in range(n):
    arr.append([x for x in input()])
d=[".","#"]
def fun(index,temp):
    ans=0
    for j in range(n):
        if arr[j][index]==d[temp]:
            ans+=1
    return ans

dp=[[float('inf'),float('inf')] for i in range(m+1)]
cost=[[0,0] for i in range(m+1)]

for i in range(1,m+1):
    cost[i][0]=cost[i-1][0]+fun(i-1,0)
    cost[i][1]=cost[i-1][1]+fun(i-1,1)
# print(cost)
for i in range(m,-1,-1):
    if i==m:
        dp[i][0]=0
        dp[i][1]=0
        continue
    for j in range(i+x,min(m+1,i+y+1)):
        # print(i,j)
        dp[i][0]=min(dp[i][0],cost[j][1]-cost[i][1]+dp[j][1])
        dp[i][1]=min(dp[i][1],cost[j][0]-cost[i][0]+dp[j][0])
    # print(i,dp[i])
print(min(dp[0]))



