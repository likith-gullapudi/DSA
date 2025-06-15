import sys
import math
sys.setrecursionlimit(10**7)

# Fast exponentiation modulo mod
def modpow(a, e, mod):
    res = 1
    a %= mod
    while e > 0:
        if e & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        e >>= 1
    return res

# Extended GCD for ax + by = gcd(a,b)
def extgcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extgcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

# Modular inverse using extended GCD (works for non-prime mod)
def invmod(a, m):
    g, x, y = extgcd(a, m)
    if g != 1:
        raise ValueError("Inverse does not exist")
    return x % m

# Precompute factorial ignoring multiples of p modulo pe
def fact_without_p(n, p, pe, fact):
    if n == 0:
        return 1
    res = fact[n % pe]
    res = (res * modpow(fact[pe], n // pe, pe)) % pe
    res = (res * fact_without_p(n // p, p, pe, fact)) % pe
    return res

# Count exponent of p in n!
def exponent_p_in_fact(n, p):
    cnt = 0
    while n > 0:
        n //= p
        cnt += n
    return cnt

# Calculate nCr mod p^e
def nCr_mod_prime_power(n, r, p, e):
    pe = p**e
    fact = [1] * (pe + 1)
    for i in range(1, pe + 1):
        if i % p == 0:
            fact[i] = fact[i - 1]
        else:
            fact[i] = (fact[i - 1] * i) % pe

    a = fact_without_p(n, p, pe, fact)
    b = fact_without_p(r, p, pe, fact)
    c = fact_without_p(n - r, p, pe, fact)

    exp_p = exponent_p_in_fact(n, p) - exponent_p_in_fact(r, p) - exponent_p_in_fact(n - r, p)

    denom = (b * c) % pe
    denom_inv = invmod(denom, pe)
    res = (a * denom_inv) % pe
    res = (res * modpow(p, exp_p, pe)) % pe
    return res

# CRT combine for two congruences
def crt_combine(r1, m1, r2, m2):
    g, s, t = extgcd(m1, m2)
    diff = (r2 - r1) % m2
    if diff < 0:
        diff += m2
    # diff must be divisible by g (assumed here)
    mul = (diff // g) % (m2 // g)
    x = (r1 + s * mul * m1) % (m1 // g * m2)
    return x

def prime_factorization(m):
    factors = []
    mm = m
    p = 2
    while p * p <= mm:
        if mm % p == 0:
            cnt = 0
            while mm % p == 0:
                mm //= p
                cnt += 1
            factors.append((p, cnt))
        p += 1 if p == 2 else 2
    if mm > 1:
        factors.append((mm, 1))
    return factors

def main():
    n, r, m = map(int, input().split())
    if r < 0 or r > n:
        print(0)
        return

    factors = prime_factorization(m)

    remainders = []
    moduli = []

    for (p, e) in factors:
        pe = p**e
        val = nCr_mod_prime_power(n, r, p, e)
        remainders.append(val)
        moduli.append(pe)

    # Combine all results using CRT
    x = remainders[0]
    M = moduli[0]
    for i in range(1, len(remainders)):
        x = crt_combine(x, M, remainders[i], moduli[i])
        M = M // math.gcd(M, moduli[i]) * moduli[i]

    print(x % m)

if __name__ == "__main__":
    main()
