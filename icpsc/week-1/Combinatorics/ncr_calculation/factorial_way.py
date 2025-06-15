n,r,m=[int(x) for x in input().split()]
fact=[1 for i in range(n+1)]
for i in range(2,n+1):
    fact[i]*=fact[i-1]*i
    fact[i]%=m
inv_fact = [1] * (n + 1)
inv_fact[n] = pow(fact[n], m - 2, m)  # Fermat’s inverse of n!

# Precompute inverse factorials using:
# inv_fact[i-1] = inv_fact[i] * i % m
for i in range(n-1, 0, -1):
    inv_fact[i] = inv_fact[i+1] * i % m
# fact_inverse=[1 for i in range(n+1)]
# for i in range(2,n+1):
#     fact_inverse[i]=pow(fact[i],-1,m)
# print(fact,fact_inverse)
#now find inverse for each
#fact(n)*inverse(fact(n-r))*inverse(fact(r))
print((fact[n]*inv_fact[n-r]*inv_fact[r])%m)

