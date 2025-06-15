n,k=[int(x) for x in input().split()]
graph=[[] for _ in range(n)]
outdp=[[0 for j in range(k+1)] for i in range(n)]
indp=[[0 for j in range(k+1)] for i in range(n)]
for _ in range(n-1):
    a,b=[int(x)-1 for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
def dfs1(node,parent):

    indp[node][0] = 1
    for nei in graph[node]:
        if nei==parent:
            continue
        dfs1(nei,node)

        for kk in range(1,k+1):
            indp[node][kk]+=indp[nei][kk-1]
        #print(node,indp)
def dfs2(node,parent):


    outdp[node][0]=1
    for kk in range(1,k+1):
        outdp[node][kk] = (outdp[parent][kk - 1] if parent != -1 and kk - 1 >= 0 else 0) \
                          + (indp[parent][kk - 1] if parent != -1 and kk - 1 >= 0 else 0) \
                          - (indp[node][kk - 2] if parent!=-1 and  kk - 2 >= 0 else 0)
        outdp[node][kk]-=1 if kk-1==0 and parent!=-1 else 0
    #print(node, outdp)
    for nei in graph[node]:
        if nei==parent:
            continue
        dfs2(nei,node)


dfs1(0,-1)
dfs2(0,-1)
ans=0
for node in range(n):
    ans+=indp[node][k]
    ans+=outdp[node][k]
print(ans//2)

