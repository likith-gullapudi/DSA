n,m,q=[int(x) for x in input().split()]
graph=[[] for i in range(n)]
dist=[[float('inf') for i in range(n)] for j in range(n)]
for _ in range(m):
    a,b,c=[int(x)-1 for x in input().split()]

    dist[a][b]= min(dist[a][b],c+1)
    dist[b][a]= min(c+1,dist[b][a])
for i in range(n):
    dist[i][i]=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
for _ in range(q):
    i,j=[int(x)-1 for x in input().split()]
    print(dist[i][j] if dist[i][j]!=float('inf') else -1)
