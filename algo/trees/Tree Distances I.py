n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=[int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
indp=[[0,0] for i in range(n+1)]
outdp=[0 for i in range(n+1)]

def dfs(node,par):
    for nei in graph[node]:
        if nei==par:
            continue
        temp=1+dfs(nei,node)
        if temp>indp[node][0]:
            indp[node][1]=indp[node][0]
            indp[node][0]=temp
        elif temp>indp[node][1]:
            indp[node][1]=temp
    return indp[node][0]
def fun(node,par):
    if node==1:
        outdp[1]=0
    else:
        outdp[node]=max(1+outdp[par],1+indp[par][0] if indp[par][0]!=1+indp[node][0] else 1+indp[par][1])
    for nei in graph[node]:
        if nei==par:
            continue
        fun(nei,node)


dfs(1,0)
fun(1,0)
for i in range(1,n+1):
    print(max(indp[i][0],outdp[i]),end=' ')


