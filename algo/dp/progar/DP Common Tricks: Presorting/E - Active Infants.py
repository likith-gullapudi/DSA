n=int(input())
arr=[(int(x),index) for index,x in enumerate(input().split())]
occupied=[False for i in range(n)]
arr.sort(reverse=True)
dp=[[-1 for i in range(n)]for j in range(n)]
def fun(x,y):

    index=x+y
    if index==n:
        return 0
    if dp[x][y]!=-1:
        return dp[x][y]
    #placing in left
    left=fun(x+1,y)+abs(arr[index][1]-x)*arr[index][0]
    #placing in right
    right=fun(x,y+1)+abs(arr[index][1]-(n-1-y))*arr[index][0]
    dp[x][y]=max(left,right)
    return max(left,right)
print(fun(0,0))






