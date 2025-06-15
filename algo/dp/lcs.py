def fun(i, j, memo):
    if i == -1 or j == -1:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    if a[i] == b[j]:
        memo[i][j] = 1 + fun(i - 1, j - 1, memo)
    else:
        memo[i][j] = 0
    return memo[i][j]

for _ in range(int(input())):
    a, b = input().split()
    n, m = len(a), len(b)
    ans = -1
    memo = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans = max(fun(i, j, memo), ans)
    print(ans)
