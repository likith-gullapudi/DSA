import sys
sys.setrecursionlimit(10**6)
n,e=[int(x) for x in input().split()]
graph=[[] for _ in range(n)]
for _ in range(e):
    a,b=[int(x)-1 for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
ans=[0]
visited=[False for i in range(n)]
def dfs(node,parent):
    x=1
    visited[node]=True
    for nei in graph[node]:
        if nei==parent:
            continue
        x+=dfs(nei,node)
    # if x%2==0:
    #     print(node)
    ans[0]+=1 if x%2==0 else 0
    return x if x%2==1 else 0
for i in range(n):
    if not visited[i]:
        dfs(i,-1)
print(ans[0]-1)



