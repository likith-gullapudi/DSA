a = input()
b = input()
n, m = len(a), len(b)
dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

def fun(i, j):
    if i == n:
        return m - j
    if j == m:
        return n - i
    if dp[i][j] != -1:
        return dp[i][j]
    ans=100
    if a[i] == b[j]:
        ans = fun(i + 1, j + 1)
    ans=min(ans,1+fun(i + 1, j),1+fun(i, j + 1),1+fun(i + 1, j + 1))
    # Consider deletion of a character from 'a'
    dp[i][j]=ans
    return ans

print(fun(0, 0))
