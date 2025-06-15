import math

n,a,b=[int(x) for x in input().split()]
arr=[]
abmax=0
for _ in range(n):
    arr.append([int(x) for x in input().split()])
    abmax=max(abmax,arr[-1][1],arr[-1][0])
#fun(index,a_taken,b_taken)->minimum amount from index 1 having a_taken alrady and b_taken already
dp=[[[-1 for i in range(n*abmax+1)] for j in range(n*abmax+1)] for k in range(n)]
def fun(index,a_taken,b_taken):
    if index==n:
        return float('inf')
    if dp[index][a_taken][b_taken]!=-1:
        return dp[index][a_taken][b_taken]
    gcd=math.gcd(a_taken,b_taken)
    if gcd!=0 and  a_taken//gcd==a and b_taken//gcd==b:
        return 0
    #taking
    take=arr[index][2]+fun(index+1,a_taken+arr[index][0],b_taken+arr[index][1])
    #not takign
    not_take=fun(index+1,a_taken,b_taken)
    dp[index][a_taken][b_taken]=min(take,not_take)
    return min(take,not_take)
print(fun(0,0,0) if fun(0,0,0)!=float('inf') else -1)