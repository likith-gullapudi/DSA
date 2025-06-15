import sys
sys.setrecursionlimit(10**6)
n=int(input())
arr=[int(x) for x in input().split()]
graph=[[] for _ in range(n)]
edges=[]
for _ in range(n-1):
    a,b=[int(x)-1 for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
    edges.append((a,b))
insum=[-1 for i in range(n)]
def dfs(node,parent):

    insum[node]=arr[node]
    for nei in graph[node]:
        if nei==parent:
            continue
        insum[node]+=dfs(nei,node)
    # print(node,insum[node])
    return insum[node]
outsum=[0 for i in range(n)]
def dfs2(node,parent):
    if parent!=-1:
        outsum[node]=insum[parent]-insum[node]+outsum[parent]
    for nei in graph[node]:
        if nei==parent:
            continue
        dfs2(nei,node)
dfs(0,-1)
dfs2(0,-1)
ans=float('inf')
# print(insum,outsum)
for i,j in edges:
    # print(i,j)
    # print(outsum)
    if outsum[j]==outsum[i]+insum[i]-insum[j]:
        # print("eneted here")
        one=insum[j]
        two=insum[0]-one
        diff=abs(one-two)
        ans=min(ans,diff)
    else:
        i,j=j,i
        one = insum[j]
        two = insum[0] - one
        diff = abs(one - two)
        ans = min(ans, diff)
        ans=min(ans,diff)
    # print(ans)
print(ans)


