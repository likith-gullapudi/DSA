from math import gcd
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def can_sort_with_coprime_restriction(health):
    n = len(health)
    dsu = DSU(n)
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(health[i], health[j]) != 1:
                dsu.union(i, j)
    sorted_health = sorted(health)
    for i in range(n):
        if health[i] != sorted_health[i]:
            j = health.index(sorted_health[i])
            if dsu.find(i) != dsu.find(j):
                return False
    return True

n = int(input())
results = []
for _ in range(n):
    _ = int(input())
    health = [int(x) for x in input().split()]
    results.append(can_sort_with_coprime_restriction(health))

for i in results:
    print("Yes" if i else "No")
