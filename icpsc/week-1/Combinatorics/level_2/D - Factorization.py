import math
mod=10**9+7
# fact=[1 for i in range(N+1)]
# for i in range(2,N+1):
#     fact[i]*=fact[i-1]*i
#     fact[i]%=N
# inv_fact = [1] * (N + 1)
# inv_fact[N] = pow(fact[N], mod - 2, mod)  # Fermat’s inverse of n!
#
# # Precompute inverse factorials using:
# # inv_fact[i-1] = inv_fact[i] * i % m
# for i in range(N-1, 0, -1):
#     inv_fact[i] = inv_fact[i+1] * i % mod
m,n=[int(x) for x in input().split()]
def prime_factors(n):
    d={}
    i = 2
    while i * i <= n:
        while n % i == 0:
            d[i]=d.get(i,0)+1
            n //= i
        i += 1
    if n > 1:
        d[n]=d.get(n,0)+1
    return d
d=prime_factors(n)
ans=1
# print(d)
for prime,count in d.items():
    #have to share this count to all m values
    #think bars and rocks combinatino method
    ans*=math.comb(m+count-1,m-1)
    ans%=mod
    # print(prime,count,ans)

print(ans)

