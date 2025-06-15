import math
# from collections import Counter
# import sys
# sys.setrecursionlimit(1 << 25)
#
#
# n = int(input())
# a = [(int(x), i+1) for i, x in enumerate(input().split())]
# b = [(int(x), i+1) for i, x in enumerate(input().split())]
# MOD = int(input())
# points = a + b
# points.sort()

# Precompute factorials and inverse factorials
# MAX = 2 * n + 10
# fact = [1] * (MAX+1)
# inv_fact = [1] * (MAX+1)
#
# for i in range(2,MAX+1):
#     fact[i]*=fact[i-1]*i
#     fact[i]%=MOD
#
# inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
#   # Fermat’s inverse of n!
# print(inv_fact[MAX])
# # Precompute inverse factorials using:
# # inv_fact[i-1] = inv_fact[i] * i % m
# for i in range(MAX-2, 0, -1):
#     inv_fact[i] = inv_fact[i+1] * i % MOD
# print(fact,inv_fact)
# # Count permutations with repetition
# ans = fact[2 * n]
# freq = Counter(points)
# for count in freq.values():
#     ans = ans * inv_fact[count] % MOD
#
# print(ans)

print(pow(15,-1,7),math.pow(1,-1,7))
