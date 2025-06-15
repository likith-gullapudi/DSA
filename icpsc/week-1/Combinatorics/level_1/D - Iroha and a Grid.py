h, w, a, b = [int(x) for x in input().split()]
m = 10 ** 9 + 7
n = h + w
fact = [1 for _ in range(n + 1)]

# Precompute factorials
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % m

inv_fact = [1] * (n + 1)
inv_fact[n] = pow(fact[n], m - 2, m)  # Fermat's little theorem for modular inverse

# Precompute inverse factorials
for i in range(n - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % m


def ncr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % m * inv_fact[n - r] % m


ans = 0
# Sum over all possible intermediate points (r, b-1) where r = 0 to h-a
for r in range(h - a + 1):  # Fixed: include h-a
    c = b - 1  # Fixed: last accessible column is b-1, not b

    # Part 1: Paths from (0, 0) to (r, c)
    # Need r steps down and c steps right
    left = ncr(r + c, r)

    # Part 2: Paths from (r, c) to (h-1, w-1)
    # Need (h-1-r) steps down and (w-1-c) steps right
    down = h - 1 - r
    right = w - 1 - c
    right_path = ncr(down + right, down)

    ans = (ans + left * right_path) % m

print(ans)