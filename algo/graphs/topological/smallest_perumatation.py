import heapq

n,m=[int(x) for x in input().split()]
graph=[[] for i in range(n)]
indegee=[0 for i in range(n)]
visited=[False for i in range(n)]
for _ in range(m):
    x,y=[int(x)-1 for x in input().split()]
    heapq.heappush(graph[x],y)

    indegee[y]+=1
ans=[]
def dfs(node):
    heap=[]
    for nei in graph[node]:
        indegee[nei]-=1
        if indegee[nei]==0:
            visited[nei]=True
            ans.append(str(nei+1))
            dfs(nei)
for i in range(n):
    if indegee[i]==0 and not visited[i]:
        visited[i]=True
        ans.append(str(i+1))
        dfs(i)
if len(ans)==n:
    print(" ".join(ans))
else:
    print(-1)





