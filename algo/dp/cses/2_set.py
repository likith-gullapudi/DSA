MOD = 10**9 + 7
n = int(input())
d = {}

def fun(index, s):
    if index == n + 1:
        return int(s == 0)
    if (index, s) in d:
        return d[(index, s)]
    d[(index, s)] = 0
    d[(index, s)] += fun(index + 1, s + index)
    d[(index, s)] += fun(index + 1, s - index)
    d[(index, s)] %= MOD
    return d[(index, s)] % MOD

result = fun(1, 0)
result = (result * 500000004) % MOD  # Multiply by the modular inverse of 2
print(result)
