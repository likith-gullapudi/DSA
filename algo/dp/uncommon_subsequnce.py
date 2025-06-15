def fun(i,j):
    if i==-1:
        return float('inf')
    if j==-1:
        return 1

    if pre[i][j]==-1:
        return 1
    else:
        x=1+fun(i-1,pre[i][j]-1)
        y=fun(i-1,j)
        return min(x,y)
for _ in range(int(input())):
    a=input()
    b=input()
    pre=[[-1 for i in range(len(b))] for j in range(len(a))]
    for i in range(len(a)):
        temp=-1
        for j in range(len(b)):
            if a[i]==b[j]:
                temp=j
            #print(i,j,len(pre),len(pre[0]))
            pre[i][j]=temp
    print(fun(len(a)-1,len(b)-1))


    '''
    form-3
    dp[i][j] means shortest common subsequnce from a[:i] and d[:j]
    transition
    dp[i][j]=if pre[i][j]==-1: return 1 
else:
taking i into consideratino 
dp[i][j]=1+dp[i-1][pre[i][j]-1]
not taking i into consideration 
dp[i][j]=dp[i-1,j]
it is minimum of those
'''
