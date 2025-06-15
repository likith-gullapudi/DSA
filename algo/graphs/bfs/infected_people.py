n, m = [int(x) for x in input().split()]
arr = []
for _ in range(n):
    arr.append([int(x) for x in input().split()])
infected = []
normal = 0


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            infected.append((i, j))
        elif arr[i][j] == 1:
            normal += 1
        # applying bfs
time = 0
while infected:

    if normal == 0:
        break
    x = len(infected)
    for i in range(x):
        x, y = infected.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            xx, yy = dx + x, dy + y
            if is_valid(xx, yy) and arr[xx][yy] == 1:
                arr[xx][yy] = 2
                normal -= 1
                infected.append((xx, yy))
    time += 1
if normal != 0:
    print(-1)
else:
    print(time)