import sys

n, m = map(int, sys.stdin.readline().strip().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    graph[a].append((0, b))
    graph[b].append((1, a))


def bfs(root):
    q = [(0, root)]
    dist = [float('inf') for i in range(n)]
    dist[root] = 0
    while q:
        dist_till_now, node = q.pop(0)
        if node == n - 1:
            return dist_till_now
        for edge_cost, nei in graph[node]:
            if dist_till_now + edge_cost < dist[nei]:

                dist[nei] = dist_till_now + edge_cost
                if edge_cost==0:
                    q.insert(0,(dist_till_now + edge_cost, nei))
                else:
                    q.append((dist_till_now + edge_cost, nei))
    return -1


print(bfs(0))

