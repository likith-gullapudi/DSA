import heapq

n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
    i, j = [int(x) - 1 for x in input().split()]
    graph[i].append(j)
    graph[j].append(i)
ans = [-float('inf')]


def fun(root,par):
    l = []
    for nei in graph[root]:
        if nei==par:
            continue
        heapq.heappush(l, fun(nei,root))
        if len(l) >= 2:
            heapq.heappop(l)
    if len(l)==0:
        ans[0]=max(ans[0],1)
        return 1
    if len(l)==1:
        ans[0]=max(ans[0],l[0]+1)
    else:
        ans[0] = max(ans[0], l[0] + l[1] + 1)
    return max(l) + 1


fun(0,-1)
print(ans[0])



