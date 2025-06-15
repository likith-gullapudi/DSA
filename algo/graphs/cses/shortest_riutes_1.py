import heapq

n,m=[int(x) for x in input().split()]
graph=[[] for i in range(n)]
for _ in range(m):
    a,b,c=[int(x)-1 for x in input().split()]
    graph[a].append((c+1,b))
def dyjistra():
    dist=[float('inf') for i in range(n)]
    dist[0]=0
    q=[(0,0)]
    heapq.heapify(q)
    while q:
        dist_till_now,node=heapq.heappop(q)
        if dist_till_now>dist[node]:
            continue
        for cost,nei in graph[node]:
            if dist_till_now+cost<dist[nei]:
                dist[nei]=dist_till_now+cost
                heapq.heappush(q,(dist_till_now+cost,nei))
    for i in dist:
        print(i,end=" ")
dyjistra()

