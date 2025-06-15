MOD=10**9+7
def mod_inverse(base, modulus):
    # Calculate the modular inverse using Fermat's Little Theorem
    return pow(base, modulus - 2, modulus)

def calculate_inverse_powers(k, n, p):
    # Calculate k^(-i) mod p for i from 1 to n
    inverse_powers = [0] * (n + 1)
    inverse_powers[1] = mod_inverse(k, p)
    for i in range(2, n + 1):
        inverse_powers[i] = (inverse_powers[i - 1] * inverse_powers[1]) % p
    return inverse_powers

# Example usage:
n,q,k=[int(x) for x in input().split()]
arr=[int(x)%MOD for x in input().split()]
a=[0 for i in range(n+1)]
b=[0 for i in range(n+1)]
for i in range(1,n+1):
    a[i]=a[i-1]+pow(arr[i-1],i,MOD)
    a[i]%=MOD
    b[i]=(b[i-1]+arr[i-1])%MOD
k_inverses=calculate_inverse_powers(k,n,MOD)
for _ in range(q):
    l,r=[int(x) for x in input().split()]
    x=(a[r]-a[l-1])%MOD
    y=((b[r]-b[l-1])*k_inverses[l])%MOD
    print((x*y)%MOD)

