from collections import defaultdict

M = 10**9 + 7
N = 10**5 + 10
s = [0] * N

def f():
    for i in range(2, N):
        s[i] = i
    for i in range(2, int(N**0.5) + 1):
        if s[i] == i:
            for j in range(i*i, N, i):
                if s[j] == j:
                    s[j] = i

def g(x):
    d = defaultdict(int)
    while x > 1:
        d[s[x]] += 1
        x //= s[x]
    return d

def h(d):
    r = 1
    for v in d.values():
        r *= (v + 1)
    return r

def main():
    n = int(input())
    x = int(input())
    a = [int(input()) for _ in range(n)]

    f()
    pf = [g(v) for v in a]
    dp = [-1] * (n + 1)

    def go(i):
        if i == n:
            return 1
        if dp[i] != -1:
            return dp[i]
        w = 0
        m = defaultdict(int)
        for j in range(i, n):
            for p, c in pf[j].items():
                m[p] += c
            if h(m) >= x:
                w = (w + go(j + 1)) % M
        dp[i] = w
        return w

    print(go(0))

main()
