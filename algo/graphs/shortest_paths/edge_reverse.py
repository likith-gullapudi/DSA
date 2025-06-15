import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    dist = [float('inf')] * n

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        graph[a].append((0, b))
        graph[b].append((1, a))

    q = deque()
    q.append((0, 0))
    dist[0] = 0

    while q:
        _, node = q.popleft()
        for cost, nei in graph[node]:
            if cost == 1:
                if cost + dist[node] < dist[nei]:
                    dist[nei] = cost + dist[node]
                    q.append((cost + dist[node], nei))
            elif cost == 0:
                if cost + dist[node] < dist[nei]:
                    dist[nei] = cost + dist[node]
                    q.appendleft((cost + dist[node], nei))

    print(dist[-1])
