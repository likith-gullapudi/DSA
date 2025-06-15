n,m=[int(x) for x in input().split()]
visited=[0 for _ in range(n)]
arr=[[] for _ in range(n)]
_can=True
for _ in range(m):
    x,y=[int(i)-1 for i in input().split()]
    arr[x].append(y)
    arr[y].append(x)
def dfs(node,color):
    global _can
    visited[node]=color
    #print(node, visited)
    for nei in arr[node]:
        #print(node,nei,visited[nei])
        if visited[nei]==color:
            #print("here")
            _can=False

        elif visited[nei]==0:
            dfs(nei,3-color)
for i in range(n):
    if visited[i]==0:
        dfs(i,1)

if _can:
    print('YES')
else:
    print('NO')

