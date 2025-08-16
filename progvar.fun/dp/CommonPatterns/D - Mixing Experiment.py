import math

n,ma,mb=[int(x) for x in input().split()]
arr=[]

for _ in range(n):
    arr.append([int(x) for x in input().split()])
#TC-40**3*100
# print(math.log10((40**3)*100))
#a can range from max(arr[1])*n and b also similar
dp=[[[float('inf') for i in range(n*10+1)]for j in range(n*10+1)] for k in range(n+1)]
present=[[float('inf') for i in range(n*10+1)]for j in range(n*10+1)]
future=[[float('inf') for i in range(n*10+1)]for j in range(n*10+1)]
def fun(index,a,b):
    if a!=0 and a%ma==0 and b%ma==0 and a//ma==b//mb:
        # print(index,a,b,a//ma,b//ma)
        return 0
    if index==n:
        return float('inf')
    #take
    take=arr[index][2]+fun(index+1,a+arr[index][0],b+arr[index][1])
    no_take=fun(index+1,a,b)
    return min(take,no_take)
for index in range(n,-1,-1):
    for a in range(n*10,-1,-1):
        for b in range(n*10,-1,-1):
            if a != 0 and a % ma == 0 and b % mb == 0 and a // ma == b // mb:
                # print(index,"here",a,b)
                present[a][b] = 0
                continue
            elif index==n:
                present[a][b]=float('inf')
                continue
            if a+arr[index][0]<len(dp[0]) and b+arr[index][1]<len(dp[0]):
                present[a][b]=future[a+arr[index][0]][b+arr[index][1]]+arr[index][2]
            present[a][b]=min(present[a][b],future[a][b])
    future=present[:]
    # print(index,min(dp[index]))
# ans=fun(0,0,0)
# if ans!=float('inf'):
#     print(ans)
# else:
#     print(-1)
# print("tabilation")
# for i in range(n):
#     print(dp[i][3][2])
ans=present[0][0]
if ans==float('inf'):
    print(-1)
else:
    print(ans)