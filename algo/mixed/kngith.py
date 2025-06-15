i, j = [int(x) for x in input().split()]
m = int(input())
pawn = []
visited = [[False for i in range(8)] for j in range(8)]
for _ in range(m):
    pawn.append([int(x) for x in input().split()])


def is_valid(xx, yy):
    return 0 <= xx < 8 and 0 <= yy < 8


def dfs(x, y, attack, ans):
    print(x,y)
    now=attack
    visited[x][y] = True
    if (x, y) in pawn:
        now =attack+1
    if now == m:
        return ans
    temp = float('inf')
    for dx, dy in ((-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2)):

        xx, yy = x + dx, y + dy

        if is_valid(xx, yy) and not visited[xx][yy]:
            temp = min(temp, dfs(xx, yy, now, ans + 1))
    visited[x][y] = False
    return temp


print(dfs(i, j, 0, 0))

