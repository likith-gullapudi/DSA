n,m=[int(x) for x in input().split()]
graph=[[] for i in range(n+1)]
indegree=[0 for i in range(n+1)]
for _ in range(m):
    a,b=[int(x) for x in input().split()]
    graph[a].append(b)
    indegree[b]+=1
q=[]
for i in range(1,len(indegree)):
    if indegree[i]==0:
        q.append(i)
ans=[]
while q:
    node=q.pop(0)
    ans.append(str(node))
    for nei in graph[node]:
        indegree[nei]-=1
        if indegree[nei]==0:
            q.append(nei)
if len(ans)==n:
    print(" ".join(ans))
else:
    print("IMPOSSIBLE")