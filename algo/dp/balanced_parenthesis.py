dp=[[-1 for i in range(10**3+5)] for j in range(10**3+5)]
def fun(index,temp):
    if temp<0:
        return 0
    if index==n:
        if temp==0:
            return 1
        return 0
    if dp[index][temp]!=-1:
        return dp[index][temp]
    if s[index]==")":
        temp=fun(index+1,temp-1)
    elif s[index]=="(":
        temp=fun(index+1,temp+1)
    else:
        temp=fun(index+1,temp+1)+fun(index+1,temp-1)
    dp[index][temp]=temp
    return temp


for _ in range(int(input())):
    s=input()
    n=len(s)
    for i in range(n):
        for j in range(n):
            dp[i][j]=-1
    print(fun(0,0))

'''

'''