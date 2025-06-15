import math
def pow(base, exponent, mod):


    result = 1
    base %= mod
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent >>= 1
    return result
def mod_inverse(x, mod):

    return pow(x, mod - 2, mod)

def nCr_mod(n, r, mod):

    if r > n or r < 0:
        return 0
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator = (numerator * (n - i)) % mod
        denominator = (denominator * (i + 1)) % mod
    return (numerator * mod_inverse(denominator, mod)) % mod
n,a,b=[int(x) for x in input().split()]
mod=10**9+7
x,y=nCr_mod(n,a,mod),nCr_mod(n,b,mod)

print((pow(2,n,mod)-1-x-y)%mod)

