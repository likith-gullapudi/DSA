#finding nuymber of components using bfs
from collections import deque

n,m=[int(x) for x in input().split()]
q=deque()
visited=[False for i in range(n)]
arr=[[] for i in range(n)]
for _ in range(m):
    x,y=[int(x)-1 for x in input().split()]
    arr[x].append(y)
    arr[y].append(x)
ans=0
def bfs(node):
    visited[node]=True
    q=deque([node])
    while q:
        temp=q.popleft()
        #print(q, visited, temp)

        for nei in arr[temp]:
            if not visited[nei]:
                visited[nei]=True
                q.append(nei)
for i in range(n):
    if not visited[i]:
        bfs(i)
        ans+=1
print(ans-1)


