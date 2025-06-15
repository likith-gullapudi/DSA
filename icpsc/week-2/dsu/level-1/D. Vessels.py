import sys
input = sys.stdin.readline

n = int(input())
cap = list(map(int, input().split()))
cur = [0] * n
nxt = list(range(n + 2))  # DSU parent pointers

def find(v):
    path = []
    while v != nxt[v] and v < n:
        path.append(v)
        v = nxt[v]
    for u in path:
        nxt[u] = v
    return v

def add(v, x):
    while x > 0:
        v = find(v)
        if v == n:
            break  # spill
        free = cap[v] - cur[v]
        take = min(free, x)
        cur[v] += take
        x -= take
        if cur[v] == cap[v]:
            nxt[v] = find(v + 1)

m = int(input())
for _ in range(m):
    q = input().split()
    if q[0] == '1':
        p = int(q[1]) - 1
        x = int(q[2])
        add(p, x)
    else:
        k = int(q[1]) - 1
        print(cur[k])
