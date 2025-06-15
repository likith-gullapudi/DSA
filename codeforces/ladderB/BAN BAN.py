#https://codeforces.com/contest/1747/problem/B
t = int(input())
for _ in range(t):
    n = int(input())
    print((n + 1) // 2)  # Minimum operations

    for i in range((n + 1) // 2):
        b_idx = i * 3 + 1
        n_idx = (n - i - 1) * 3 + 3
        print(b_idx, n_idx)
#BANBANBAN