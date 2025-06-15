import sys
sys.setrecursionlimit(10**6)
n,q=[int(x) for x in input().split()]
par=[int(x) for x in input().split()]
graph=[[] for i in range(n)]
for child,parent in enumerate(par):
    child+=1
    parent-=1
    graph[parent].append(child)
#print(graph)
#for every node maintain an arrays which stores 2**i higher node from this
higher=[[-1 for i in range(20)] for j in range(n)]
depth={}
def dfs(node,par,d):
    depth[node]=d
    higher[node][0]=par
    for i in range(1,20):
        higher[node][i]=higher[higher[node][i-1]][i-1] if higher[node][i-1]!=-1 else -1
    for ch in graph[node]:
        dfs(ch,node,d+1)
dfs(0,-1,0)
def move(node,k):
    for i in range(20):
        if k & (1 << i):
            node = higher[node][i]
            if node == -1:
                return -1
    else:
        return node

for _ in range(q):
    a,b=[int(x)-1 for x in input().split()]
    adep=depth[a]
    bdep=depth[b]
    if adep > bdep:
        a, b = b, a
        adep = depth[a]
        bdep = depth[b]

    b=move(b,bdep-adep)
    #print(a,b)
    while True:
        #print(a,b)
        changed=False
        if a==b:
            print(a+1)
            break
        for i in range(19, -1, -1):  # Fix: Check the ancestors from the highest to lowest power of 2
            if  higher[a][i] != higher[b][i]:  # If a and b differ at this level, move both upwards
                a = higher[a][i]
                b = higher[b][i]
                break
        else:
            print(higher[a][0] + 1)
            break





