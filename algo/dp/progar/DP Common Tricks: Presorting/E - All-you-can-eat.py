import sys
sys.setrecursionlimit(10**6)
n,t=[int(x) for x in input().split()]
arr=[]
for _ in range(n):
    arr.append([int(x) for x in input().split()])
arr.sort(key=lambda x:x[0])
dp=[[-1 for i in range(t)] for j in range(n)]
def fun(index,time):
    if time>t-0.5 or index==n:
        return 0
    if dp[index][time]!=-1:
        return dp[index][time]
    #take
    take=fun(index+1,time+arr[index][0])+arr[index][1]
    #Not take
    not_take=fun(index+1,time)
    dp[index][time]=max(take,not_take)
    return dp[index][time]
print(fun(0,0))