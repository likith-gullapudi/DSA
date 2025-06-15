import sys
sys.setrecursionlimit(10**6)
n,q=[int(x) for x in input().split()]
par=[int(x) for x in input().split()]
graph=[[] for i in range(n)]
for child,parent in enumerate(par):
    child+=1
    parent-=1
    graph[parent].append(child)
#print(graph)
#for every node maintain an arrays which stores 2**i higher node from this

higher=[[-1 for i in range(20)] for j in range(n)]
def dfs(node,par):
    higher[node][0]=par
    for i in range(1,20):
        higher[node][i]=higher[higher[node][i-1]][i-1] if higher[node][i-1]!=-1 else -1
    for ch in graph[node]:
        dfs(ch,node)
dfs(0,-1)
for _ in range(q):
    node,k=[int(x) for x in input().split()]
    node-=1
    ans=0
    for i in range(20):
        if k & (1 << i):
            node = higher[node][i]
            if node == -1:
                print(-1)
                break
    else:
        print(node+1)
