n,m=[int(x) for x in input().split()]
arr=[]
def is_valid(x,y):
    return 0<=x<n and 0<=y<m
for _ in range(n):
    arr.append(input())
visited=[[False for i in range(m)] for j in range(n)]
def dfs(x,y):
    visited[x][y]=True
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        xx,yy=dx+x,dy+y
        if is_valid(xx,yy) and  arr[xx][yy]=="." and not visited[xx][yy]:
            dfs(xx,yy)
ans=0
for i in range(n):
    for j in range(m):
        if arr[i][j]=="." and not visited[i][j]:

            ans+=1
            dfs(i,j)
print(ans)
print(int(2))