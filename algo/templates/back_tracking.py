def fun(index):
    global ans
    if index == n:#base case
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