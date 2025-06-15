cities,roads=[int(x) for x in input().split()]
arr=[[] for i in range(cities)]
for _ in range(roads):
    x,y=[int(i)-1 for i in input().split()]
    arr[x].append(y)
    arr[y].append(x)

visited=[-1 for i in range(cities)]
cycle=False
def dfs(node,dist):
    global cycle
    visited[node]=dist

    for nei in arr[node]:
        #print(node, dist,nei, visited[nei],dist-visited[nei]>=3)
        if visited[nei]==-1:
            #print(visited[nei])
            dfs(nei,dist+1)
        elif dist-visited[nei]>=3:
            cycle=True
for i in range(cities):
    if visited[i]==-1:
        dfs(i,0)
if cycle:
    print('YES')
else:
    print('NO')
