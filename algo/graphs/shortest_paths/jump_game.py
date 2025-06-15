import sys
import heapq

# Faster input reading using sys.stdin
def get_int():
    return map(int, sys.stdin.readline().split())

n, a, b = get_int()
arr = list(get_int())

mp = {}
for j in range(n):
    i = j + 1
    if arr[j] in mp:
        mp[arr[j]].append(i)
    else:
        mp[arr[j]] = [i]

graph = [[] for _ in range(n + len(mp) + 1)]
for j in range(len(arr) - 1):
    i = j + 1
    graph[i].append((i + 1, a if arr[j] == arr[j + 1] else b))
    graph[i + 1].append((i, a if arr[j] == arr[j + 1] else b))

index = len(arr) + 1
for i, li in mp.items():
    for j in li:
        graph[index].append((j, a))
        graph[j].append((index, 0))
    index += 1

st = int(sys.stdin.readline())

def dijkstra(start):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    q = [(0, start)]

    while q:
        node_dist, temp = heapq.heappop(q)
        for nei, d in graph[temp]:
            if node_dist + d < dist[nei]:
                dist[nei] = node_dist + d
                heapq.heappush(q, (dist[nei], nei))

    # Print distances instead of returning
    for i in range(1, len(arr) + 1):
        print(dist[i], end=" ")

dijkstra(st)
