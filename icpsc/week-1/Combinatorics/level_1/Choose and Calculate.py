n, r = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
mod = 10**9 + 7

# Precompute factorials
fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % mod

# Precompute inverse factorials using Fermat’s Little Theorem
inv_fact = [1] * (n + 1)
inv_fact[n] = pow(fact[n], mod - 2, mod)
for i in range(n - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

# Sort in descending order for min_sum calculation
arr.sort(reverse=True)

min_sum = max_sum = 0

# Min contribution loop
for i in range(n):
    possible = i
    have_to_take = r - 1
    if possible < have_to_take:
        continue
    comb = (fact[possible] * inv_fact[have_to_take] % mod * inv_fact[possible - have_to_take]) % mod
    min_sum = (min_sum + comb * arr[i]) % mod

# Reverse array for max_sum calculation
arr.reverse()

# Max contribution loop
for i in range(n):
    possible = i
    have_to_take = r - 1
    if possible < have_to_take:
        continue
    comb = (fact[possible] * inv_fact[have_to_take] % mod * inv_fact[possible - have_to_take]) % mod
    max_sum = (max_sum + comb * arr[i]) % mod

# Final result
print((max_sum - min_sum + mod) % mod)
