
n,m=[int(x) for x in input().split()]
arr=[set() for i in range(n)]
visited=[-1 for i in range(n)]
ans=10**10
def dfs(node,par):

    global ans

    visited[node]=visited[par]+1 if par!=-1 else 0
    for nei in arr[node]:

        if nei==par:continue
        elif visited[nei]!=-1:
            print(node+1,nei+1)
            ans = min(ans, abs(visited[node] - visited[nei]) + 1)
            if visited[nei]>visited[node]+1:
                dfs(nei,node)
        else:
            dfs(nei, node)



for _ in range(m):
    a,b=[int(x)-1 for x in input().split()]
    if a==b:
        continue
    arr[a].add(b)
    arr[b].add(a)

for i in range(n):
    if  visited[i]==-1:
        dfs(i,-1)

if ans==10**10:
    print(-1)
else:
    print(ans)
