n,m=[int(x) for x in input().split()]

edges=[]
for _ in range(m):
    a,b,c=[int(x) for x in input().split()]
    a-=1
    b-=1
    edges.append((a,b,-c))
dist=[float('inf') for i in range(n)]
dist[0]=0
for i in range(n):
    for start,end,cost in edges:
        dist[end]=min(dist[end], dist[start]+cost)
print(-dist[n-1])

