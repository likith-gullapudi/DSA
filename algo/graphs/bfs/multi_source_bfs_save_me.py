from collections import deque

n,m=[int(x) for x in input().split()]
arr=[]

for _ in range(n):
    arr.append([x for x in input()])
monsters=deque()
persons=deque()

visited=[[False for i in range(len(arr[0]))] for j in range(len(arr))]


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]=='A':
            persons.append((i,j,0))
            visited[i][j]=True
        if arr[i][j]=='M':
            arr[i][j]=0
            monsters.append((i,j,0))

def bfs(q:deque):
    while q:
        x,y,dist=q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            xx,yy=x+dx,y+dy
            if not(xx>=0 and xx<len(arr) and yy>=0 and yy<len(arr[0])): continue
            if arr[xx][yy]!="#" and (arr[xx][yy]=='.'  or arr[xx][yy]=='A' or arr[xx][yy]>arr[x][y]):
                arr[xx][yy]=dist+1
                q.append((xx,yy,dist+1))
def bfsh(q:deque):
    while q:
        #print(q)
        x,y,dist=q.popleft()
        if x in [0,len(arr)-1] or y in [0,len(arr[0])-1]:
            print("YES")
            print(dist)
            return True
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            xx,yy=x+dx,y+dy
            if not(xx>=0 and xx<len(arr) and yy>=0 and yy<len(arr[0])): continue
            if arr[xx][yy]!="#" and arr[xx][yy]>dist+1 and not visited[xx][yy]:
                visited[xx][yy]=True
                arr[xx][yy]=dist+1
                q.append((xx,yy,dist+1))
bfs(monsters)
if not bfsh(persons):
    print("NO")





