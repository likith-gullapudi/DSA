import sys
sys.setrecursionlimit(10**6)
n,q=[int(x) for x in input().split()]
graph=[[] for i in range(n+1)]

for _ in range(n-1):
    a,b=[int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

#for every node maintain an arrays which stores 2**i higher node from this
higher=[[-1 for i in range(20)] for j in range(n+1)]
depth={}
def dfs(node,par,d):
    depth[node]=d
    higher[node][0]=par
    for i in range(1,20):
        higher[node][i]=higher[higher[node][i-1]][i-1] if higher[node][i-1]!=-1 else -1
    for ch in graph[node]:
        if ch==par:
            continue
        dfs(ch,node,d+1)
dfs(1,0,0)
def move(node,k):
    for i in range(20):
        if k & (1 << i):
            node = higher[node][i]
            if node == -1:
                return -1
    else:
        return node
def lca(a,b):
    #print(a,b)

    adep=depth[a]
    bdep=depth[b]
    if adep > bdep:
        a, b = b, a
        adep = depth[a]
        bdep = depth[b]

    b=move(b,bdep-adep)
    if a==b:
        return a
    for i in range(19,-1,-1):
        if higher[a][i]!=higher[b][i]:
            a = higher[a][i]
            b = higher[b][i]
    return higher[a][0]








for _ in range(q):
    a,b=[int(x) for x in input().split()]
    l=lca(a,b)
    #print(l)
    print(depth[a]+depth[b]-2*depth[l])


