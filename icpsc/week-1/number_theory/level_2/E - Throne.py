import math

T = int(input())
for _ in range(T):
    n, s, k = map(int, input().split())
    g = math.gcd(k, n)

    if (n - s) % g != 0:
        print(-1)
        continue

    n_g = n // g
    k_g = k // g
    rhs = (n - s) // g

    # Using built-in pow to find modular inverse of k_g modulo n_g
    inv = pow(k_g, -1, n_g)
    m = (rhs * inv) % n_g
    print(m)
