n=int(input())
board = [[0 for i in range(n)] for j in range(n)]



def check(index, ch):
    for row in range(index):
        for col in range(n):
            if board[row][col] == 1:
                if col == ch or abs(row - index) == abs(col - ch):
                    return False
    return True
ans=0
def fun(index):
    global ans
    if index == n:
        ans+=1
        return

    for ch in range(8):
        #print(index, len(board), ch, len(board[0]))
        if board[index][ch]=="*":
            continue
        if check(index, ch):
            board[index][ch] = 1
            fun(index + 1)

            board[index][ch] = 0

    return False

fun(0)
print(ans)
