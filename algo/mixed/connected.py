def is_valid(x,y):
    return 0<=x<n and 0<=y<m
def dfs(node, start):
    x, y = node
    visited[x][y] = True
    parent[x][y] = start
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        xx, yy = dx + x, dy + y
        if is_valid(xx, yy) and arr[xx][yy] == 0 and not visited[xx][yy]:
            dfs((xx, yy), start)

for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    arr=[]
    for _ in range(n):
        arr.append([int(x) for x in input().split()])
    visited=[[False for i in range(m)] for j in range(n)]
    parent=[[(-1,-1) for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j]!=1:
                dfs((i,j),(i,j))
    d={}
    for i in parent:
        for j in i:
            d[j]=d.get(j,0)+1

    for i in range(n):
        for j in range(m):
            if  arr[i][j] != 1:
                arr[i][j]=d[parent[i][j]] if d[parent[i][j]]!=1 else 0
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()

