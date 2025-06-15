n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=[int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
indp=[0 for i in range(n+1)]
outdp=[0 for i in range(n+1)]
size=[0 for i in range(n+1)]
def dfs(node,par):
    dist=0
    size[node]=1
    for nei in graph[node]:
        if nei==par:
            continue
        dfs(nei,node)
        indp[node]+=indp[nei]+size[nei]
        size[node]+=size[nei]
dfs(1,0)
#print(indp,size)
def fun(node,par):
    outdp[node]=n-size[node]+outdp[par]
    #have to find siblings now
    if node!=1:
        outdp[node]+=indp[par]-indp[node]-size[node]
    for nei in graph[node]:
        if nei==par:
            continue
        fun(nei,node)
fun(1,0)
#print(outdp)
print(' '.join([str(i+j) for i,j in zip(indp,outdp)][1:]))

