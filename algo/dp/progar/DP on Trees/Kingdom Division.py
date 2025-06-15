import sys
sys.setrecursionlimit(10**6)
n = int(input())
edges = []
graph = [[] for _ in range(n)]
MOD=10**9+7

# Input edges and build the tree
for _ in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

# Memoization table
# dp[node][color][ally]: Result for (node, parent, color, ally)
dp = {}


def fun2(node, parent, child_id, color, ally):
    # Base case: all children processed
    if child_id == len(graph[node]):
        return 1 if ally else 0

    # Skip the parent node
    if graph[node][child_id] == parent:
        return fun2(node, parent, child_id + 1, color, ally)

    child = graph[node][child_id]

    # Make child an ally
    a = fun(child, node, color, min(1,ally + 1)) * fun2(node, parent, child_id + 1, color, min(1,ally + 1))
    # Don't include child as an ally
    b = fun(child, node, 1 - color, 0) * fun2(node, parent, child_id + 1, color, ally)


    return (a + b)%MOD


def fun(node, parent, color, ally):
    # Check memoized result
    if (node, parent, color, ally) in dp:
        return dp[(node, parent, color, ally)]%MOD

    # Compute and memoize result
    dp[(node, parent, color, ally)] = fun2(node, parent, 0, color, ally)%MOD
    return dp[(node, parent, color, ally)]%MOD


# Compute and print result
print((fun(0, -1, 0, 0) + fun(0, -1, 1, 0))%MOD)
