import sys
sys.setrecursionlimit(10**6)
n=int(input())
graph=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=[int(x)-1 for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
dp2={}
def fun2(node,parent,index,taken):
    #take
    if index==len(graph[node]):
        return 0
    if (node,parent,index,taken) in dp2:
        return dp2[(node,parent,index,taken)]
    if graph[node][index]==parent:
        return fun2(node,parent,index+1,taken)
    ans=0
    a=b=0
    if not taken:
        a+=fun2(node,parent,index+1,True)
        a+=1+fun(graph[node][index],node,True)
    #not taking

    b+=fun2(node,parent,index+1,taken)
    b+=fun(graph[node][index],node,False)
    dp2[(node, parent, index, taken)]=max(a,b)
    return max(a,b)
dp={}
def fun(node,parent,taken):
    if (node,parent,taken) in dp:
        return dp[(node,parent,taken)]
    dp[(node, parent, taken)]=fun2(node,parent,0,taken)
    return dp[(node, parent, taken)]
print(fun(0,-1,False))