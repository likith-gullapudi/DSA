def bellamon_ford(st):

    dist=[float('inf') for i in range(n+1)]
    dist[st]=0
    for j in range(n-1):
        for i in range(m):
            a,b,c=edges[i]
            if dist[b]>dist[a]+c:
                dist[b]=dist[a]+c
    temp=dist[:]
    #checking negative cycles
    for i in range(m):
        a, b, c = edges[i]
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
    return [temp,dist]