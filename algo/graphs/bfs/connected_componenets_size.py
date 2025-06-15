def connected_componenets_size(i,j):
    q=[(i,j)]
    parent[i][j]=(i,j)
    visited[i][j]=True
    s=0
    while q:
        x,y=q.pop(0)
        s+=1
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            xx,yy=dx+x,dy+y
            if 0<=xx<n and 0<=yy<m and  not visited[xx][yy] and arr[xx][yy]==0:
                visited[xx][yy]=True
                parent[xx][yy]=(i,j)
                q.append((xx,yy))
    size[i][j]=s if s!=1 else 0
for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    arr=[]
    for _ in range(n):
        arr.append([int(x) for x in input().split()])
    visited=[[False for i in range(m)] for j in range(n)]
    parent=[[(i,j) for j in range(m)] for i in range(n)]
    size=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j]==0:
                connected_componenets_size(i,j)
    #print(parent)
    for i in range(n):
        for j in range(m):
            arr[i][j]=size[parent[i][j][0]][parent[i][j][1]] if arr[i][j]!=1 else 1
            print(arr[i][j],end=" ")
        print()






