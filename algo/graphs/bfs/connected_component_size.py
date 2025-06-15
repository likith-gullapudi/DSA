for _ in range(1):
    n=int(input())
    m=n
    arr=[]
    for _ in range(n):
        arr.append([x for x in input().split()])
    visited=[[False for j in range(m)] for i in range(n)]
    parent=[[(-1,-1) for j in range(m)] for i in range(n)]
    def is_valid(x,y):
        return 0<=x<n and 0<=y<m
    def dfs(node,start):
        x,y=node
        visited[x][y]=True
        parent[x][y]=start
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            xx,yy=dx+x,dy+y
            if is_valid(xx,yy) and arr[xx][yy]=="." and not visited[xx][yy]:
                dfs((xx,yy),start)
    for i in range(n):
        for j in range(m):
            if arr[i][j]=="." and not visited[i][j]:
                dfs((i,j),(i,j))
    d={}
    for i in parent:
        for j in i:
            d[j]=d.get(j,0)+1

    for i in range(len(parent)):
        for j in range(len(parent[i])):
            if parent[i][j]==(-1,-1):
                parent[i][j]=1
                continue

            parent[i][j]=d[(parent[i][j])] if d[(parent[i][j])]!=1 else 0

    for i in parent:
        for j in i:
            print(j,end=" ")
        print()
