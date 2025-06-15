import heapq

n,m=[int(x) for x in input().split()]
graph=[[] for i in range(n)]
for _ in range(m):
    a,b,cost=[int(x)-1 for x in input().split()]
    graph[a].append((cost+1,b))

def djyistra():
    q=[(0,0)]
    heapq.heapify(q)
    dist=[float('inf') for i in range(n)]
    dist[0]=0
    while q:
        cost_till,node=heapq.heappop(q)
        if cost_till>=dist[node]:
            continue
        for extra_coat,nei in graph[node]:
            if cost_till+extra_coat<dist[nei]:
                dist[nei]=cost_till+extra_coat
                heapq.heappush(q,(dist[nei],nei))
    for i in dist:
        print(i,end=" ")
djyistra()




