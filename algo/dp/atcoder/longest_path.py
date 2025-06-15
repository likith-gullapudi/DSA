from collections import deque
from functools import cache

n,m=[int(x) for x in input().split()]
graph=[[] for i in range(n)]
indegree=[0 for i in range(n)]
for _ in range(m):
    a,b=[int(x)-1 for x in input().split()]
    graph[a].append(b)
    indegree[b]+=1

# @cache
# def fun(node):
#     ans=1
#     for nei in graph[node]:
#         ans=max(ans,1+fun(nei))
#     return ans
# ans=1
# for i in range(n):
#     #print(i,fun(i))
#     ans=max(ans,fun(i))
#
# print(ans-1)
#findind topo sort
q=deque()
topo=[]
for i in range(len(indegree)):
    if indegree[i]==0:
        q.append(i)

while q:
    temp=q.popleft()
    topo.append(temp)
    for nei in graph[temp]:
        indegree[nei]-=1
        if indegree[nei]==0:
            q.append(nei)
#got topo sort
dp=[0 for i in range(n)]
for i in topo[::-1]:
    dp[i]=1
    for nei in graph[i]:
        dp[i]=max(dp[i],1+dp[nei])
print(max(dp)-1)
