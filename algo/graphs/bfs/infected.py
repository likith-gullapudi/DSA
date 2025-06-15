from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# Create a separate grid to track infection state
infected = [[False] * m for _ in range(n)]
q = deque()

# Initialize the queue and count the initial number of uninfected people
ones = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i, j, 0))
            infected[i][j] = True
        elif arr[i][j] == 1:
            ones += 1
if ones==0: print(0)
else:

	# Perform BFS to simulate the spread of infection
    while q:
        x, y, time = q.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xx, yy = dx + x, dy + y
            if 0 <= xx < n and 0 <= yy < m and not infected[xx][yy] and arr[xx][yy] == 1:
                q.append((xx, yy, time + 1))
                infected[xx][yy] = True
                ones -= 1
        if ones == 0:
            print(time+1)
            break
    else:
        print(-1)