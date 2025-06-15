import sys

sys.setrecursionlimit(110000)
n=int(input())
graph=[[] for i in range(n)]
for _ in range(n-1):
    a,b=[int(x)-1 for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
MOD=10**9+7
def dfs(node,parent):
    #present is white and present is black
    ans=[1,1]
    for nei in graph[node]:
        if nei==parent:
            continue
        temp=dfs(nei,node)
        ans[0]*=(temp[0]+temp[1])
        ans[1]*=temp[0]
        ans[0]%=MOD
        ans[1]%= MOD

    return ans
print(sum(dfs(0,-1))%MOD)
