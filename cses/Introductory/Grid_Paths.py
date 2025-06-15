s = "??????R??????U??????????????????????????LD????D?"
visited = [[False]*8 for _ in range(8)]
count = 0

def fun(index, i, j):
    global count
    if i < 0 or i >= 7 or j < 0 or j >= 7 or visited[i][j]:
        return
    if i == 6 and j == 0:
        if index == len(s):
            count += 1
        return
    if (visited[i][j - 1] and visited[i][j + 1]) and (not visited[i - 1][j] and not visited[i + 1][j]):
        return 0
    if (visited[i - 1][j] and visited[i + 1][j]) and (not visited[i][j - 1] and not visited[i][j + 1]):
        return 0

    visited[i][j] = True

    if index < len(s):
        if s[index] == '?':
            if i + 1 < 7 and not visited[i + 1][j]:  # Down
                fun(index + 1, i + 1, j)
            if i - 1 >= 0 and not visited[i - 1][j]:  # Up
                fun(index + 1, i - 1, j)
            if j + 1 < 7 and not visited[i][j + 1]:  # Right
                fun(index + 1, i, j + 1)
            if j - 1 >= 0 and not visited[i][j - 1]:  # Left
                fun(index + 1, i, j - 1)
        elif s[index] == 'D' and i + 1 < 7 and not visited[i + 1][j]:
            fun(index + 1, i + 1, j)
        elif s[index] == 'U' and i - 1 >= 0 and not visited[i - 1][j]:
            fun(index + 1, i - 1, j)
        elif s[index] == 'R' and j + 1 < 7 and not visited[i][j + 1]:
            fun(index + 1, i, j + 1)
        elif s[index] == 'L' and j - 1 >= 0 and not visited[i][j - 1]:
            fun(index + 1, i, j - 1)

    visited[i][j] = False

fun(0, 0, 0)
print(count)
