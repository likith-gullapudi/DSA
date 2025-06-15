n,m=[int(x) for x in input().split()]
arr=[]
for _ in range(n):
    arr.append([x for x in input()])
#run mutlisource bfs from monsters so that we can knwo at every index at what time mosnters can arrive
q=[]
dist=[[float('inf') for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]=='M':
            q.append((i,j,0))
            dist[i][j]=0
        elif arr[i][j]=='A':
            aa=(i,j)
while q:
    #print(q)
    x,y,d=q.pop(0)
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        xx,yy=dx+x,dy+y
        if 0<=xx<n and 0<=yy<m and arr[xx][yy]!='#' and   dist[xx][yy]>d+1:
            dist[xx][yy]=d+1
            q.append((xx,yy,d+1))
q=[(aa[0],aa[1],0)]
visited=[[False for i in range(m)] for j in range(n)]
parent=[[-1 for i in range(m)] for j in range(n)]
visited[aa[0]][aa[1]]=True
parent[aa[0]][aa[1]]=[-1,-1]
dir={(-1,0):'U',(1,0):'D',(0,1):'R',(0,-1):'L'}
#print(dist)
while q:
    #print(q)
    x,y,d=q.pop(0)
    if x==n-1 or y==m-1 or x==0 or y==0:
        print("YES")
        ans=[]
        while parent[x][y]!=[-1,-1]:
            ans.append(dir[x-parent[x][y][0],y-parent[x][y][1]])
            x,y=parent[x][y]
        print(len(ans))
        print(''.join(ans[::-1]))

        break



    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        xx,yy=dx+x,dy+y
        if 0<=xx<n and 0<=yy<m and arr[xx][yy]!='#' and  not visited[xx][yy] and d+1<dist[xx][yy]:
            visited[xx][yy]=True
            parent[xx][yy]=[x,y]
            q.append((xx,yy,d+1))
else:
    print("NO")




