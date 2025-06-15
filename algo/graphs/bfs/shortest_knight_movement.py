from collections import deque


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n
for _ in range(int(input())):
    n,a,b,A,B=[int(x)-1 for x in input().split()]
    n+=1
    visited=[[False for i in range(n)] for j in range(n)]
    def bfs(a,b):
        q=deque()
        q.append((a,b,0))
        visited[a][b]=True
        while q:
            x,y,dist=q.popleft()
            if x==A and y==B:
                ans=dist
                return dist
            for dx,dy in [(-2,-1),(-1,-2),(-1,2),(-2,1),(1,-2),(2,-1),(1,2),(2,1)]:
                xx,yy=dx+x,dy+y

                if is_valid(xx,yy) and not visited[xx][yy]:
                    visited[xx][yy] = True
                    q.append((xx,yy,dist+1))

        return -1
    print(bfs(a,b))


