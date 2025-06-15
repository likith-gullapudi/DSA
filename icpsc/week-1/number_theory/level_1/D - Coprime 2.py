def find_coprimes(N, M, A):
    MAX = 10**5
    # Step 1: Find all unique prime factors from A
    prime_factors = set()

    def prime_factorization(x):
        factors = set()
        d = 2
        while d * d <= x:
            while x % d == 0:
                factors.add(d)
                x //= d
            d += 1 if d == 2 else 2
        if x > 1:
            factors.add(x)
        return factors

    for num in A:
        prime_factors.update(prime_factorization(num))

    # Step 2: Use sieve to mark multiples of these prime factors up to M
    sieve = [False] * (M + 1)
    for p in prime_factors:
        for multiple in range(p, M + 1, p):
            sieve[multiple] = True

    # Step 3: Collect numbers that are not marked in sieve (gcd=1 for all A[i])
    result = [k for k in range(1, M + 1) if not sieve[k]]

    return result


# Example usage:
N,M=[int(x) for x in input().split()]
A=[int(x) for x in input().split()]
coprimes = find_coprimes(N, M, A)
print(len(coprimes))
for ans in coprimes:
    print(ans)
