n,m=[int(x) for x in input().split()]
graph=[[] for i in range(n)]
for _ in range(m):
    a,b=[int(x)-1 for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
dist=[-1 for i in range(n)]
parent=[i for i in range(n)]
ans=[]
def dfs(node,par):

    dist[node]=dist[par]+1 if par!=-1 else 0
    parent[node]=par
    for nei in graph[node]:
        if nei==par:
            continue
        if dist[nei]==-1:
            if dfs(nei,node):
                return True
        elif dist[node]-dist[nei]>1:
            #print(node,nei,dist,parent)
            ans.append(nei)
            while node!=nei:
                ans.append(node)
                node=parent[node]
            ans.append(nei)
            return True
    return False
for i in range(n):
    if dist[i]==-1:

        if dfs(i,-1):
            print(len(ans))
            for i in ans:
                print(i+1,end=" ")
            break
else:
    print('IMPOSSIBLE')




