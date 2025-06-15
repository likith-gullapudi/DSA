n = int(input())
ans = 0
board = [[0 for i in range(n)] for j in range(n)]
row = [-1 for i in range(n)]

def check(index, ch):

    for dx, dy in [(-1, -2), (-2, -1), (-1, 2), (-2, 1)]:
        if 0<=index + dx < n and 0<=ch + dy < n and board[index + dx][ch + dy] == 1:
            return False
    for i in range(index):
        if (abs(ch - row[i]) == abs(index - i)) or (ch == row[i]):
            return False
    return True

def rec(index):
    global ans
    if index == n:
        ans += 1

        return
    for ch in range(0, n):
        if check(index, ch):
            board[index][ch] = 1
            row[index] = ch
            rec(index + 1)
            board[index][ch] = 0
            row[index] = -1

rec(0)
print(ans)
